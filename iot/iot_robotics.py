import rospy
from std_msgs.msg import String

class IOTRobotics:
    def __init__(self):
        self.pub = rospy.Publisher('iot_robotics', String, queue_size=10)
        self.sub = rospy.Subscriber('iot_robotics', String, self.callback)

    def callback(self, data):
        print(f'Received message: {data.data}')

    def send_message(self, message):
        self.pub.publish(String(message))

# Example usage:
iot_robotics = IOTRobotics()
rospy.init_node('iot_robotics_node')
iot_robotics.send_message('Hello, IoT robotics!')
rospy.spin()
