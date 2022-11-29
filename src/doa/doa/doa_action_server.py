import time

from action_doa.action import DOAaction

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

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
        feedback_msg.partial_sequence = [0, 1]

        for i in range(1, goal_handle.request.order):
            msg = "DOA: "+str(self.Mic_tuning.direction) + " VA: "+ str(self.Mic_tuning.is_voice())

            feedback_msg.partial_sequence.append(
                feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i-1])
            self.get_logger().info('Feedbacko: {0}'.format(feedback_msg.partial_sequence))
            self.get_logger().info('Feedbacko: {0}'.format(msg))
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)

        goal_handle.succeed()

        result = DOAaction.Result()
        result.sequence = feedback_msg.partial_sequence
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
