import rclpy
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup
from geometry_msgs.msg import Twist

from action_doa.action import DOAaction

from .tuning import Tuning
import usb.core
import usb.util

class DOAActionServer(Node):

    # Creacion del nodo doa_action_server
    def __init__(self):
        super().__init__('doa_action_server')
        self._action_server = ActionServer(
            self,
            DOAaction,
            'doaaction',
            execute_callback = self.execute_callback, 
            callback_group = ReentrantCallbackGroup(),
            goal_callback = self.goal_callback,
            cancel_callback = self.cancel_callback)

        # Busqueda del microfono
        self.dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
        self.Mic_tuning = Tuning(self.dev)


    # Callback a ejecutar en caso de pedir una meta
    def execute_callback(self, goal_handle):
        self.get_logger().info('Ejecutando escucha...')
        
        # Objeto del feedback de la accion
        feedback_msg = DOAaction.Feedback()

        # Banderas para buscar 
        encontrado = False

        # Publicador para manejar a la kobuki
        nodo = rclpy.create_node("doa_velocista")
        publisher = nodo.create_publisher(Twist, '/commands/velocity', 10)
        move_cmd = Twist()
        velocidad_angular = 0.3

        # Configuraciones del campo de audicion del microfono
        esp_audible = 40
        centro = 90

        # Ejecucion de la meta
        while(not encontrado):
            # Si se cancela el servicio
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Operacion cancelada')
                return DOAaction.Result()

            direccion = None
            va = None

            # Microfono muerto
            try:
                direccion = self.Mic_tuning.direction
                va = self.Mic_tuning.is_voice()
            except:
                print("RECONECTA EL MICROFONO")
                goal_handle.abort()
                return DOAaction.Result()

            dir_giro = ''
            
            if(direccion < (centro + esp_audible/2) % 360 and direccion > (centro - esp_audible/2) % 360):
                encontrado = True
            
            # Derecha
            if(direccion > esp_audible + 180 or direccion < esp_audible):
                move_cmd.angular.z = -velocidad_angular
                dir_giro = 'derecha'
            # Izquierda
            if(direccion > esp_audible and direccion < esp_audible + 180):
                move_cmd.angular.z = velocidad_angular
                dir_giro = 'izquierda'

            publisher.publish(move_cmd)

            # Mensaje de feedback
            msg = "{DOA: "+str(direccion) + ", VA: "+ str(va) + ", DG: "+ dir_giro + "}"
            self.get_logger().info('Feedback: {0}'.format(msg))
            feedback_msg.feedback = msg
            goal_handle.publish_feedback(feedback_msg)

        # La meta se ha cumplido
        goal_handle.succeed()
        nodo.destroy_node()

        result = DOAaction.Result()
        result.resultado = "Encontrado"
        return result

    def destroy(self):
        self._action_server.destroy()
        super().destroy_node()

    def goal_callback(self, goal_request):
        self.get_logger().info('Recibida peticion de meta')
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_request):
        self.get_logger().info('Recibida peticion de cancelacion')
        return CancelResponse.ACCEPT


def main(args=None):
    rclpy.init(args=args)
    print("DOA ACTION SERVER STARTED")

    doa_action_server = DOAActionServer()
    executor = MultiThreadedExecutor()

    try:
        rclpy.spin(doa_action_server, executor=executor)
    except KeyboardInterrupt:
        pass

    doa_action_server.destroy()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
