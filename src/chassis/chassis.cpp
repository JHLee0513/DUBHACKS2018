#include "ros/ros.h"
#include "std_msgs/String.h"

#include <JHPWMPCA9685.h>
#include <chassis.h>
#include <steering.h>
#include <throttle.h>

int main(int argc, char **argv) {
    PCA9685 *pca9685 = new PCA9685() ;
    int err = pca9685->openPCA9685();
    if (err < 0){
        printf("Error: %d", pca9685->error);
    } else {
        printf("PCA9685 Device Address: 0x%02X\n",pca9685->kI2CAddress) ;
        pca9685->setAllPWM(0,0) ;
        pca9685->reset() ;
        pca9685->setPWMFrequency(60) ;
	}
    ros::init(argc, argv, "chassis_listener");
    ros::NodeHandle n;
    ros::Subscriber sub = n.subscribe("control", 1000, control_callback);
    ros::spin();
    return 0;
}

void control_callback(const std_msgs::String::ConstPtr& msg) {
    ROS_INFO("I heard: [%s]", msg->data.c_str());
}
