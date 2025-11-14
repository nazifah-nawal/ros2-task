import rclpy

from rclpy.node import Node

from std_msgs.msg import Float32

topic1='float_topic'

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')

        self.pub_float = self.create_publisher(Float32,topic1,10)

        self.period = 1.0/60.0
        self.timer = self.create_timer(self.period,self.callback_fun)
        self.value = 0
    def callback_fun(self):
        message1=Float32()

        self.value=self.value+0.01
        message1.data=self.value
        self.pub_float.publish(message1)
        self.get_logger().info('Publishing: value %s'%(message1))

def main(args=None):

    rclpy.init(args=args)

    publisher_node=PublisherNode()
    rclpy.spin(publisher_node)
    publisher_node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()



            
        
