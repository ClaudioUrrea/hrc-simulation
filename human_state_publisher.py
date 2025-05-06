#!/usr/bin/env python3
import rospy
import numpy as np
from std_msgs.msg import Float32MultiArray

def human_state_publisher():
    rospy.init_node('human_state_publisher', anonymous=True)
    pub = rospy.Publisher('human_state', Float32MultiArray, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        # Simular estados: [fatigue (0-1), skill_level (0-2), task_completion_time (seconds)]
        fatigue = np.clip(np.random.normal(0.5, 0.1), 0, 1)  # Fatigue: low (0), medium, high (1)
        skill_level = np.random.randint(0, 3)  # 0: novice, 1: intermediate, 2: expert
        task_completion_time = np.random.normal(10, 2)  # Normal distribution (mean 10s, SD 2s)

        state = Float32MultiArray()
        state.data = [fatigue, skill_level, task_completion_time]
        pub.publish(state)
        rospy.loginfo(f"Published human state: {state.data}")
        rate.sleep()

if __name__ == '__main__':
    try:
        human_state_publisher()
    except rospy.ROSInterruptException:
        pass
