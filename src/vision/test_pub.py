#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import time

TOPIC = "control"

class Controller:
    def __init__(self):
        self.target_pub = rospy.Publisher(TOPIC,
                           String, #determine ros data structure for image data
                           queue_size = 10)
        rospy.init_node("test_pub", anonymous=True)

        i = 0
        while True:
            self.target_pub.publish(str(i) + "," + str(i*100))
            i += 1
            time.sleep(2)

if __name__ == "__main__":
	Controller()
            
     
