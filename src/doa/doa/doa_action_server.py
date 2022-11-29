import time

from action_doa.action import DOAaction

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from geometry_msgs.msg import Twist

from .tuning import Tuning
import usb.core
import usb.util

class DOAActionServer(Node):

    def __init__(self):
        super().__init__('doa_action_server')
        self._action_server = ActionServer(
            self,
            DOAaction,
            'doaaction',
            self.execute_callback)

        self.dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
        self.Mic_tuning = Tuning(self.dev)


    def execute_callback(self, goal_handle):
        self.get_logger().info('Ejecutando meta...')

        feedback_msg = DOAaction.Feedback()

        encontrado = False
        nodo = rclpy.create_node("velocista")
        publisher = nodo.create_publisher(Twist, '/commands/velocity', 10)

        move_cmd = Twist()

        while(not encontrado):
            direccion = self.Mic_tuning.direction
            msg = "DOA: "+str(direccion) + " VA: "+ str(self.Mic_tuning.is_voice())
            self.get_logger().info('Feedbacko: {0}'.format(msg))
            feedback_msg.feedback = msg
            goal_handle.publish_feedback(feedback_msg)
            
            if(direccion < 10 and direccion > 0):
                encontrado = True
            
            # Izquierda
            if(direccion > 10 and direccion < 180):
                move_cmd.angular.z = -0.3
            # Derecha
            if(direccion > 180 and direccion < 360):
                move_cmd.angular.z = 0.3
            publisher.publish(move_cmd)
            

            # time.sleep(0.5)


        goal_handle.succeed()

        result = DOAaction.Result()
        result.resultado = "Terminado"
        return result


def main(args=None):
    rclpy.init(args=args)
    print("DOA ACTION SERVER STARTED")

    doa_action_server = DOAActionServer()

    try:
        rclpy.spin(doa_action_server)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
