#!/usr/bin/env python

## Play back pre-recorded voice files

import os
import sys
import time
import rospy
from std_msgs.msg import UInt32
from msg_types import *


def callback(msg):
    try:
        print "command: %s" % index_to_string[msg.data]
        filename = index_to_path[msg.data]
        cmd = "aplay %s" % filename
        os.system(cmd)
    except KeyError:
        print "Invalid voice message: %d" % msg.data
    #except NameError:
    #    print "Invalid WAV file path: %s" % filename


if __name__ == "__main__":
    rospy.init_node('voice_server')
    voice_sub = rospy.Subscriber('/voice', UInt32, callback)
    print "initialized"
    time.sleep(1)

    rospy.spin()
