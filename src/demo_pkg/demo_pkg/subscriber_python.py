import rclpy

from rclpy.node import Node

from std_msgs.msg import Float32

topic1='float_topic'

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')

        self.sub_float = self.create_subscription(Float32,topic1,self.callback_fun1,10)

        self.sub_float
    def callback_fun1(self,msg):
       self.get_logger().info('Message received: "%s"'%msg.data)

def main(args=None):

    rclpy.init(args=args)

    subscriber_node=SubscriberNode()
    rclpy.spin(subscriber_node)
    subscriber_node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()



            
        