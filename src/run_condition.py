#!/usr/bin/env python

import sys
import time
import rospy
from std_msgs.msg import UInt32
from msg_types import *
import baxter_interface
from baxter_interface import Gripper, Head, Limb
rospy.init_node('run_condition')
voice_pub = rospy.Publisher('/voice', UInt32, queue_size=10)
time.sleep(1)

rightg = Gripper('right')
rightg.set_holding_force(50)
leftg = Gripper('left')
right = Limb('right')
left = Limb('left')
head = Head()
neutral_right = {'right_s0': 0.476301034638421, 'right_s1': -0.5606699779721187, 'right_w0': 0.07094661143970038, 'right_w1': 0.7037136864424336, 'right_w2': -0.28033498898605935, 'right_e0': -0.16566992509162468, 'right_e1': 1.3077186216723151}
neutral_left = {'left_w0': -0.15339807878854136, 'left_w1': 0.34552917247118947, 'left_w2': 3.0158062289827234, 'left_e0': 0.18676216092504913, 'left_e1': 1.5715633171886063, 'left_s0': -0.5836796897904, 'left_s1': -0.6845389265938658}


right.move_to_joint_positions(neutral_right)
left.move_to_joint_positions(neutral_left)

head.set_pan(0.0, speed = 0.8, timeout = 0.0)

Gripper.calibrate(rightg)
Gripper.calibrate(leftg)

def wait():
	raw_input("Press Enter to continue...")

def send_voice(msg):
	print "Baxter: %s" % index_to_string[msg]
	voice_pub.publish(data = msg)


def arm_give_cookie():
        print "<give customer a granola bar>"
        leftg.open()
        Head.set_pan(head, 0.45, speed = 1.0, timeout = 0.0) #looks at cookie section

        left.move_to_joint_positions(neutral_left)

	left.move_to_joint_positions({'left_w0': 0.029529130166794215, 'left_w1': 0.6051554208207958, 'left_w2': 3.049937301513174, 'left_e0': 0.08053399136398422, 'left_e1':    	  2.185155632342772, 'left_s0': -0.7328593214122564, 'left_s1': -1.113286556807839})

	left.move_to_joint_positions({'left_w0': 0.21552430069790063, 'left_w1': 0.10661166475803625, 'left_w2': 3.050320796710145, 'left_e0': 0.006135923151541655, 'left_e1': 2.0455633806451994, 'left_s0': -0.5518495884417776, 'left_s1': -0.6258641614572488})

	leftg.close()

	left.move_to_joint_positions({'left_w0': -0.0030679615757708274, 'left_w1': 0.09433981845495294, 'left_w2': 3.049170311119231, 'left_e0': 0.10852914074289302, 'left_e1': 	  2.456286736601519, 'left_s0': -0.7083156288060898, 'left_s1': -1.1270923838988078})


	#head turns to customer
	head.set_pan(0.0, speed = 0.8, timeout = 0.0)


	left.move_to_joint_positions({'left_w0': -0.2166747862888147, 'left_w1': 0.6715000898968398, 'left_w2': 2.7139955089662684, 'left_e0': 0.18484468494019235, 'left_e1':   	 1.3506700837331067, 'left_s0': -1.3146215352177997, 'left_s1': -0.4747670538505356})

	left.move_to_joint_positions({'left_w0': -0.22204371904641365, 'left_w1': 0.6458059116997592, 'left_w2': 2.715912984951125, 'left_e0': 0.19251458887961942, 'left_e1': 1.3219079439602552, 'left_s0': -1.3192234775814558, 'left_s1': -0.4099563655623768})

        leftg.open()

	#lifts
	#left.move_to_joint_positions({'left_w0': -0.3804272353955826, 'left_w1': -0.6055389160177671, 'left_w2': 1.6241021591736817, 'left_e0': 0.10239321759135137, 'left_e1': 1.973849778811556, 'left_s0': -1.4273691231273775, 'left_s1': -0.5311408478053246})

	#lifts more
	left.move_to_joint_positions({'left_w0': -0.17679128580379394, 'left_w1': 0.890859342564454, 'left_w2': 2.9325877712399397, 'left_e0': 0.2151408055009293, 'left_e1': 		1.4902623354306794, 'left_s0': -1.14473316295949, 'left_s1': -0.8003544760792146})


	#move to neutral
	left.move_to_joint_positions(neutral_left)

	#close grippers
	leftg.close()


def grab_plate():
	print "<grabbing a plate>"
	leftg.open()

	#gaze shifts to left
	head.set_pan(0.55, speed = 0.3, timeout = 0.0)

	#moves on top of the plate
	left.move_to_joint_positions({'left_w0': 1.5941895338099161, 'left_w1': -0.8736020587007431, 'left_w2': 2.7661508557543724, 'left_e0': 0.3781262642137545, 'left_e1': 2.540272184738245, 'left_s0': -0.2795679985921167, 'left_s1': -0.9361117758070737})

	#lowers towards the plate
	left.move_to_joint_positions({'left_w0': 1.530912826309643, 'left_w1': -0.7428301965335116, 'left_w2': 3.0334470080434057, 'left_e0': 0.24351945007680942, 'left_e1': 2.271825546858298, 'left_s0': -0.17487380981893716, 'left_s1': -0.40727189918357737}, timeout=15.0)

	#grippers close
	leftg.close()
	head.set_pan(0.0, speed = 0.3, timeout = 10.0)

	#lifts plate
	left.move_to_joint_positions({'left_w0': 1.3633254252331615, 'left_w1': -1.2034079280961072, 'left_w2': 2.350058567040454, 'left_e0': 0.29030586410731457, 'left_e1': 2.4417139191166073, 'left_s0': -0.5334418189871526, 'left_s1': -0.6979612584878633},
	timeout=15.0)

	#shift gaze towards center
	head.set_pan(0.0, speed = 0.3, timeout = 0.0)


	#lifts further
	left.move_to_joint_positions({'left_w0': 0.7735098122912198, 'left_w1': -1.1861506442323961, 'left_w2': 1.5025341817337627, 'left_e0': 0.23009711818281206, 'left_e1': 2.313626523328175, 'left_s0': -1.0411894597772247, 'left_s1': -0.7198204847152304})

	#moves plate towards center
	#left.move_to_joint_positions({'left_w0': 0.2646116859102339, 'left_w1': -0.4789855010172204, 'left_w2': 1.2950632801722606, 'left_e0': 0.3390097541226764, 'left_e1': 1.4231506759606927, 'left_s0': -1.1819321970657113, 'left_s1': -0.2922233400921713}
	#

	#sets plate down
	left.move_to_joint_positions( {'left_w0': 0.5602864827751474, 'left_w1': -1.288927357020719, 'left_w2': 1.5926555530220308, 'left_e0': 0.16912138186436687, 'left_e1': 1.8476798590079808, 'left_s0': -1.017796252761972, 'left_s1': -0.12041749184900498})

	#grippers open
	leftg.open()

	#lifts
	left.move_to_joint_positions({'left_w0': 0.5606699779721187, 'left_w1': -1.33456328546031, 'left_w2': 1.58958759144626, 'left_e0': 0.2239611950312704, 'left_e1': 2.1579274733578058, 'left_s0': -1.0197137287468288, 'left_s1': -0.3321068405771921})

	#moves to neutral
	left.move_to_joint_positions(neutral_left)



def arm_give_sandwichA():
	print "<give customer a sandwich A>"
	#shifts gaze right
        Head.set_pan(head, -0.55, speed = 0.3, timeout = 0.0)

	#shifts right
	right.move_to_joint_positions({'right_s0': 0.4935583185021319, 'right_s1': -0.9790632378678653, 'right_w0': 0.0030679615757708274, 'right_w1': 0.28877188331942916, 'right_w2': -0.49816026086578813, 'right_e0': -0.15033011721277054, 'right_e1': 2.216602238494423})

	#lowers
	right.move_to_joint_positions({'right_s0': 0.43526704856248616, 'right_s1': -0.8417719573521208, 'right_w0': -0.2703641138648042, 'right_w1': 0.10162622719740866, 'right_w2': -0.28685440733457235, 'right_e0': -0.07439806821244256, 'right_e1': 2.1870731083276285})

	#lowers to grab it 
	right.move_to_joint_positions({'right_s0': 0.42529617344123094, 'right_s1': -0.6699661091089545, 'right_w0': -0.2607767339405203, 'right_w1': 0.03566505331833587, 'right_w2': -0.28033498898605935, 'right_e0': -0.06864564025787226, 'right_e1': 2.085063385933249})


        #grippers close
	rightg.close()

	#lifts
	right.move_to_joint_positions({'right_s0': 0.558752501987262, 'right_s1': -1.2156797743991905, 'right_w0': 0.1250194342126612, 'right_w1': 0.768140879533621, 'right_w2': -0.4183932598957466, 'right_e0': -0.23508255574343967, 'right_e1': 2.074709015615022})

	#set gaze back to customer
	head.set_pan(0.0, speed = 0.8, timeout = 0.0)

	#moves to middle
	right.move_to_joint_positions({'right_s0': 0.960271973216269, 'right_s1': -0.9759952762920945, 'right_w0': 0.08858739050038264, 'right_w1': 1.228335115899245, 'right_w2': 0.15953400194008302, 'right_e0': -0.049854375606275945, 'right_e1': 1.4829759266882236})

	#lowers sandwich 0
	right.move_to_joint_positions({'right_s0': 1.0618982004136777, 'right_s1': -0.6515583396543295, 'right_w0': 0.10584467436409355, 'right_w1': 0.6239466854723921, 'right_w2': 0.14879613642488512, 'right_e0': -0.05330583237901813, 'right_e1': 1.5194079704005024})

	#lowers sandwich 
	right.move_to_joint_positions({'right_s0': 1.0937283017623, 'right_s1': -0.49279132810818915, 'right_w0': 0.09165535207615347, 'right_w1': 0.5472476460781214, 'right_w2': 0.17487380981893716, 'right_e0': -0.04295146206079158, 'right_e1': 1.4135632960364088})

	#opens gripper
	rightg.open()

	#lifts
	right.move_to_joint_positions({'right_s0': 1.0415729549741959, 'right_s1': -0.705247667230319, 'right_w0': 0.10507768397015084, 'right_w1': 0.7612379659881365, 'right_w2': 0.17564080021287987, 'right_e0': -0.04180097646987752, 'right_e1': 1.4442429117941171})






def arm_give_condimentA():
	print "<give customer a condiment A>"
	#shifts gaze back right
	Head.set_pan(head, -0.55, speed = 0.3, timeout = 0.0)

	#move towards ketchup
	right.move_to_joint_positions({'right_s0': 0.09357282806101024, 'right_s1': -0.9641069251859825, 'right_w0': -0.2741990658345177, 'right_w1': 0.05790777474267437, 'right_w2': -0.34476218207724674, 'right_e0': 0.04601942363656241, 'right_e1': 2.2607041861461283})

	#move lower
	right.move_to_joint_positions({'right_s0': 0.1457281748491143, 'right_s1': -0.7673738891396782, 'right_w0': -0.13077186216723152, 'right_w1': 0.13077186216723152, 'right_w2': -0.4506068564413403, 'right_e0': 0.04908738521233324, 'right_e1': 2.052082798993712})

	#lowers down on ketchup #changed
	right.move_to_joint_positions({'right_s0': 0.13614079492483047, 'right_s1': -0.6818544602150665, 'right_w0': -0.07861651537912745, 'right_w1': 0.07439806821244256, 'right_w2': -0.4463884092746554, 'right_e0': 0.04563592843959106, 'right_e1': 2.021786678432975})

	#grippers close
	rightg.close()

	#lifts
	right.move_to_joint_positions({'right_s0': 0.3271214030165645, 'right_s1': -1.071869075534933, 'right_w0': -0.03911651009107805, 'right_w1': 0.14304370847031483, 'right_w2': -0.5997864880631968, 'right_e0': -0.08820389530341129, 'right_e1': 2.2844808883583525})


	#shifts gaze back center
	Head.set_pan(head, 0.0, speed = 0.3, timeout = 0.0)

	#lifts more
	right.move_to_joint_positions({'right_s0': 0.4437039428958559, 'right_s1': -1.2647671596115235, 'right_w0': -0.037582529303192634, 'right_w1': 0.7715923363063631, 'right_w2': -0.4049709280017492, 'right_e0': 0.06404369789421602, 'right_e1': 1.9308983167507645})

	#moves over
	right.move_to_joint_positions({'right_s0': 0.9384127469889019, 'right_s1': -0.9955535313376335, 'right_w0': -0.05675728915176031, 'right_w1': 1.021247709534714, 'right_w2': 0.2822524649709161, 'right_e0': 0.2231942046373277, 'right_e1': 1.5132720472489607})


	#sets down on plate
	right.move_to_joint_positions({'right_s0': 1.2183642407779898, 'right_s1': -0.47975249141116316, 'right_w0': 0.04141748127290617, 'right_w1': 0.6718835850938112, 'right_w2': 0.34131072530450457, 'right_e0': -0.046402918833533764, 'right_e1': 1.318456487187513})

	#opens gripper
	rightg.open()

	#lifts
	right.move_to_joint_positions({'right_s0': 1.1984224905354794, 'right_s1': -0.7957525337155584, 'right_w0': 0.05138835639416136, 'right_w1': 0.7182865039273449, 'right_w2': 0.10239321759135137, 'right_e0': -0.0839854481367264, 'right_e1': 1.5953400194008303})

	#move back to neutral
	right.move_to_joint_positions(neutral_right)

	#close gripper
	rightg.close()

def arm_give_sandwichB():

	print "<give customer a sandwich B>"
	

	Head.set_pan(head, -0.45, speed = 1.0, timeout = 0.0)

	#move right
	right.move_to_joint_positions({'right_s0': 0.40535442319872056, 'right_s1': -1.0277671278832272, 'right_w0': 0.1277039005914607, 'right_w1': 0.42299520225940285, 'right_w2': -0.7907670961549308, 'right_e0': -0.14802914603094242, 'right_e1': 2.1705828148578603})

	#shifts gaze left
	Head.set_pan(head, -0.25, speed = 0.3, timeout = 0.0)

	#shifts left
	right.move_to_joint_positions({'right_s0': 0.7915340865488735, 'right_s1': -1.090276844989558, 'right_w0': 0.18637866572807776, 'right_w1': 0.23853401251618184, 'right_w2': -0.40727189918357737, 'right_e0': -0.16336895390979655, 'right_e1': 2.3887915819345604})

	#shifts gaze back right
	Head.set_pan(head, -0.55, speed = 0.3, timeout = 0.0)

	#shifts back right
	right.move_to_joint_positions({'right_s0': 0.40535442319872056, 'right_s1': -1.0277671278832272, 'right_w0': 0.1277039005914607, 'right_w1': 0.42299520225940285, 'right_w2': -0.7907670961549308, 'right_e0': -0.14802914603094242, 'right_e1': 2.1705828148578603})

	#shifts gaze left
	Head.set_pan(head, -0.25, speed = 0.3, timeout = 0.0)

	#shifts left
	right.move_to_joint_positions({'right_s0': 0.7915340865488735, 'right_s1': -1.090276844989558, 'right_w0': 0.18637866572807776, 'right_w1': 0.23853401251618184, 'right_w2': -0.40727189918357737, 'right_e0': -0.16336895390979655, 'right_e1': 2.3887915819345604})

	#shifts gaze back right
	Head.set_pan(head, -0.55, speed = 0.3, timeout = 0.0)

	#shifts back right
	right.move_to_joint_positions({'right_s0': 0.4935583185021319, 'right_s1': -0.9790632378678653, 'right_w0': 0.0030679615757708274, 'right_w1': 0.28877188331942916, 'right_w2': -0.49816026086578813, 'right_e0': -0.15033011721277054, 'right_e1': 2.216602238494423})

	#lowers
	right.move_to_joint_positions({'right_s0': 0.43526704856248616, 'right_s1': -0.8417719573521208, 'right_w0': -0.2703641138648042, 'right_w1': 0.10162622719740866, 'right_w2': -0.28685440733457235, 'right_e0': -0.07439806821244256, 'right_e1': 2.1870731083276285})

	#lowers to grab it 
	right.move_to_joint_positions({'right_s0': 0.42529617344123094, 'right_s1': -0.6699661091089545, 'right_w0': -0.2607767339405203, 'right_w1': 0.03566505331833587, 'right_w2': -0.28033498898605935, 'right_e0': -0.06864564025787226, 'right_e1': 2.085063385933249})


        #grippers close
	rightg.close()

	#lifts
	right.move_to_joint_positions({'right_s0': 0.558752501987262, 'right_s1': -1.2156797743991905, 'right_w0': 0.1250194342126612, 'right_w1': 0.768140879533621, 'right_w2': -0.4183932598957466, 'right_e0': -0.23508255574343967, 'right_e1': 2.074709015615022})

	#set gaze back to customer
	head.set_pan(0.0, speed = 0.8, timeout = 0.0)

	#moves to middle
	right.move_to_joint_positions({'right_s0': 0.960271973216269, 'right_s1': -0.9759952762920945, 'right_w0': 0.08858739050038264, 'right_w1': 1.228335115899245, 'right_w2': 0.15953400194008302, 'right_e0': -0.049854375606275945, 'right_e1': 1.4829759266882236})

	#lowers sandwich 0
	right.move_to_joint_positions({'right_s0': 1.0618982004136777, 'right_s1': -0.6515583396543295, 'right_w0': 0.10584467436409355, 'right_w1': 0.6239466854723921, 'right_w2': 0.14879613642488512, 'right_e0': -0.05330583237901813, 'right_e1': 1.5194079704005024})

	#lowers sandwich 
	right.move_to_joint_positions({'right_s0': 1.0937283017623, 'right_s1': -0.49279132810818915, 'right_w0': 0.09165535207615347, 'right_w1': 0.5472476460781214, 'right_w2': 0.17487380981893716, 'right_e0': -0.04295146206079158, 'right_e1': 1.4135632960364088})

	#opens gripper
	rightg.open()

	#lifts
	right.move_to_joint_positions({'right_s0': 1.023165185519571, 'right_s1': -0.7098496095939753, 'right_w0': 0.11159710231866385, 'right_w1': 0.8920098281553681, 'right_w2': 0.15186409800065595, 'right_e0': -0.05829126993964572, 'right_e1': 1.4262186375364634})

def arm_give_sandwichC():
	print "<give customer a sandwich B,C>"
	

	Head.set_pan(head, -0.45, speed = 1.0, timeout = 0.0) 

	#move right
	right.move_to_joint_positions({'right_s0': 0.40535442319872056, 'right_s1': -1.0277671278832272, 'right_w0': 0.1277039005914607, 'right_w1': 0.42299520225940285, 'right_w2': -0.7907670961549308, 'right_e0': -0.14802914603094242, 'right_e1': 2.1705828148578603})

	#shifts gaze left
	Head.set_pan(head, -0.25, speed = 0.3, timeout = 0.0)

	#shifts left
	right.move_to_joint_positions({'right_s0': 0.7915340865488735, 'right_s1': -1.090276844989558, 'right_w0': 0.18637866572807776, 'right_w1': 0.23853401251618184, 'right_w2': -0.40727189918357737, 'right_e0': -0.16336895390979655, 'right_e1': 2.3887915819345604})

	#shifts gaze back right
	Head.set_pan(head, -0.55, speed = 0.3, timeout = 0.0)

	#shifts back right
	right.move_to_joint_positions({'right_s0': 0.40535442319872056, 'right_s1': -1.0277671278832272, 'right_w0': 0.1277039005914607, 'right_w1': 0.42299520225940285, 'right_w2': -0.7907670961549308, 'right_e0': -0.14802914603094242, 'right_e1': 2.1705828148578603})

	#shifts gaze left
	Head.set_pan(head, -0.25, speed = 0.3, timeout = 0.0)

	#shifts left
	right.move_to_joint_positions({'right_s0': 0.7915340865488735, 'right_s1': -1.090276844989558, 'right_w0': 0.18637866572807776, 'right_w1': 0.23853401251618184, 'right_w2': -0.40727189918357737, 'right_e0': -0.16336895390979655, 'right_e1': 2.3887915819345604})

	#shifts gaze back right
	Head.set_pan(head, -0.55, speed = 0.3, timeout = 0.0)

	#shifts back right
	right.move_to_joint_positions({'right_s0': 0.4935583185021319, 'right_s1': -0.9790632378678653, 'right_w0': 0.0030679615757708274, 'right_w1': 0.28877188331942916, 'right_w2': -0.49816026086578813, 'right_e0': -0.15033011721277054, 'right_e1': 2.216602238494423})

	send_voice(V_WARN)

	wait()

	#lowers
	right.move_to_joint_positions({'right_s0': 0.43526704856248616, 'right_s1': -0.8417719573521208, 'right_w0': -0.2703641138648042, 'right_w1': 0.10162622719740866, 'right_w2': -0.28685440733457235, 'right_e0': -0.07439806821244256, 'right_e1': 2.1870731083276285})

	#lowers to grab it 
	right.move_to_joint_positions({'right_s0': 0.42529617344123094, 'right_s1': -0.6699661091089545, 'right_w0': -0.2607767339405203, 'right_w1': 0.03566505331833587, 'right_w2': -0.28033498898605935, 'right_e0': -0.06864564025787226, 'right_e1': 2.085063385933249})

        #grippers close
	rightg.close()

	#lifts
	right.move_to_joint_positions({'right_s0': 0.558752501987262, 'right_s1': -1.2156797743991905, 'right_w0': 0.1250194342126612, 'right_w1': 0.768140879533621, 'right_w2': -0.4183932598957466, 'right_e0': -0.23508255574343967, 'right_e1': 2.074709015615022})

	#set gaze back to customer
	head.set_pan(0.0, speed = 0.8, timeout = 0.0)

	#moves to middle
	right.move_to_joint_positions({'right_s0': 0.960271973216269, 'right_s1': -0.9759952762920945, 'right_w0': 0.08858739050038264, 'right_w1': 1.228335115899245, 'right_w2': 0.15953400194008302, 'right_e0': -0.049854375606275945, 'right_e1': 1.4829759266882236})

	#lowers sandwich 0
	right.move_to_joint_positions({'right_s0': 1.0618982004136777, 'right_s1': -0.6515583396543295, 'right_w0': 0.10584467436409355, 'right_w1': 0.6239466854723921, 'right_w2': 0.14879613642488512, 'right_e0': -0.05330583237901813, 'right_e1': 1.5194079704005024})

	#lowers sandwich 
	right.move_to_joint_positions({'right_s0': 1.0937283017623, 'right_s1': -0.49279132810818915, 'right_w0': 0.09165535207615347, 'right_w1': 0.5472476460781214, 'right_w2': 0.17487380981893716, 'right_e0': -0.04295146206079158, 'right_e1': 1.4135632960364088})

	#opens gripper
	rightg.open()

	#lifts
	right.move_to_joint_positions({'right_s0': 1.023165185519571, 'right_s1': -0.7098496095939753, 'right_w0': 0.11159710231866385, 'right_w1': 0.8920098281553681, 'right_w2': 0.15186409800065595, 'right_e0': -0.05829126993964572, 'right_e1': 1.4262186375364634})





def arm_give_condimentC():
	print "<give customer a condimentBC>"
	#shifts gaze back right
	Head.set_pan(head, -0.55, speed = 0.3, timeout = 0.0)

	#move to ketchup
	right.move_to_joint_positions({'right_s0': 0.08168447695489828, 'right_s1': -0.9131020639887926, 'right_w0': -0.38924762492592374, 'right_w1': 0.19213109368264808, 'right_w2': -0.38656315854712425, 'right_e0': 0.1284708909854034, 'right_e1': 2.1422041702819805})

	#move to mustard
	right.move_to_joint_positions({'right_s0': 0.3861796633501529, 'right_s1': -0.9422476989586154, 'right_w0': -0.03029612056073692, 'right_w1': 0.35128160042575973, 'right_w2': -0.6017039640480536, 'right_e0': -0.10737865515197896, 'right_e1': 1.9803691971600692})

	#START HERE#

	#move towards ketchup
	right.move_to_joint_positions({'right_s0': 0.09357282806101024, 'right_s1': -0.9641069251859825, 'right_w0': -0.2741990658345177, 'right_w1': 0.05790777474267437, 'right_w2': -0.34476218207724674, 'right_e0': 0.04601942363656241, 'right_e1': 2.2607041861461283})

	#move lower
	right.move_to_joint_positions({'right_s0': 0.1457281748491143, 'right_s1': -0.7673738891396782, 'right_w0': -0.13077186216723152, 'right_w1': 0.13077186216723152, 'right_w2': -0.4506068564413403, 'right_e0': 0.04908738521233324, 'right_e1': 2.052082798993712})

	#lowers down on ketchup #changed
	right.move_to_joint_positions({'right_s0': 0.13614079492483047, 'right_s1': -0.6818544602150665, 'right_w0': -0.07861651537912745, 'right_w1': 0.07439806821244256, 'right_w2': -0.4463884092746554, 'right_e0': 0.04563592843959106, 'right_e1': 2.021786678432975})

	#grippers close
	rightg.close()


	#lifts
	right.move_to_joint_positions({'right_s0': 0.3271214030165645, 'right_s1': -1.071869075534933, 'right_w0': -0.03911651009107805, 'right_w1': 0.14304370847031483, 'right_w2': -0.5997864880631968, 'right_e0': -0.08820389530341129, 'right_e1': 2.2844808883583525})


	#shifts gaze back center
	Head.set_pan(head, 0.0, speed = 0.3, timeout = 0.0)

	#lifts more
	right.move_to_joint_positions({'right_s0': 0.4437039428958559, 'right_s1': -1.2647671596115235, 'right_w0': -0.037582529303192634, 'right_w1': 0.7715923363063631, 'right_w2': -0.4049709280017492, 'right_e0': 0.06404369789421602, 'right_e1': 1.9308983167507645})

	#moves over
	right.move_to_joint_positions({'right_s0': 0.9384127469889019, 'right_s1': -0.9955535313376335, 'right_w0': -0.05675728915176031, 'right_w1': 1.021247709534714, 'right_w2': 0.2822524649709161, 'right_e0': 0.2231942046373277, 'right_e1': 1.5132720472489607})
		

	#sets down on plate
	right.move_to_joint_positions({'right_s0': 1.2183642407779898, 'right_s1': -0.47975249141116316, 'right_w0': 0.04141748127290617, 'right_w1': 0.6718835850938112, 'right_w2': 0.34131072530450457, 'right_e0': -0.046402918833533764, 'right_e1': 1.318456487187513}
)

	#opens gripper
	rightg.open()

	#lifts
	right.move_to_joint_positions({'right_s0': 1.1984224905354794, 'right_s1': -0.7957525337155584, 'right_w0': 0.05138835639416136, 'right_w1': 0.7182865039273449, 'right_w2': 0.10239321759135137, 'right_e0': -0.0839854481367264, 'right_e1': 1.5953400194008303})

	#move back to neutral
	right.move_to_joint_positions(neutral_right)

	#close gripper
	rightg.close()


def arm_take_pos():
	print "<hand item to Baxter>"
	pass # do arm command


def arm_reset_sandwich():
	print "<put sandwich back>"
	#pick up position
	right.move_to_joint_positions({'right_s0': 0.8248981686853812, 'right_s1': -0.6300826086239337, 'right_w0': -0.23776702212223913, 'right_w1': 0.41072335595631954, 'right_w2': 0.14534467965214296, 'right_e0': -0.19903400722813244, 'right_e1': 1.6152817696433406})

	#lower
	right.move_to_joint_positions({'right_s0': 0.6853059169878086, 'right_s1': -0.6059224112147384, 'right_w0': -0.10737865515197896, 'right_w1': 0.16835439147042416, 'right_w2': -0.18599517053110642, 'right_e0': -0.10200972239438001, 'right_e1': 1.6938982850224682})

	#gripper close
	rightg.close()

	#lowers
	right.move_to_joint_positions({'right_s0': 0.7040971816394049, 'right_s1': -0.8429224429430349, 'right_w0': 0.06212622190935926, 'right_w1': -0.1499466220157992, 'right_w2': -0.41225733674420495, 'right_e0': -0.23278158456161155, 'right_e1': 2.3147770089190893}
	)

	#lowers to grab it 
	right.move_to_joint_positions({'right_s0': 0.7225049510940299, 'right_s1': -0.6661311571392409, 'right_w0': 0.07094661143970038, 'right_w1': -0.19136410328870537, 'right_w2': -0.41225733674420495, 'right_e0': -0.22089323345549958, 'right_e1': 2.1989614594337406})

	#rightg.open()
	rightg.open()

	#lifts
	right.move_to_joint_positions({'right_s0': 0.7033301912454623, 'right_s1': -1.1424321917776619, 'right_w0': 0.006902913545484362, 'right_w1': 0.2880048929254864, 'right_w2': -0.4111068511532909, 'right_e0': -0.2703641138648042, 'right_e1': 2.317461475297889}
	)

	rightg.open()

def arm_reset_condiment():
	print "<put condiment back>"

	#lift above pick up position 
	right.move_to_joint_positions({'right_s0': 0.7370777685789413, 'right_s1': -1.1232574319290942, 'right_w0': 0.03681553890924993, 'right_w1': 0.5944175553055978, 'right_w2': -0.43603403895642884, 'right_e0': -0.054072822772960834, 'right_e1': 2.0003109474025793})

	#pick up position
	right.move_to_joint_positions({'right_s0': 0.8640146787764593, 'right_s1': -0.7148350471546028, 'right_w0': 0.2757330466224031, 'right_w1': 0.31676703269833795, 'right_w2': -0.2964417872588562, 'right_e0': -0.1787087617886507, 'right_e1': 1.8219856808109003})

	#lower
	right.move_to_joint_positions({'right_s0': 0.8663156499582874, 'right_s1': -0.6051554208207958, 'right_w0': 0.2880048929254864, 'right_w1': 0.2044029399857314, 'right_w2': -0.2972087776527989, 'right_e0': -0.15838351634916897, 'right_e1': 1.7916895602501632})

	#close
	rightg.close()

	#lift
	right.move_to_joint_positions({'right_s0': 0.4667136547141371, 'right_s1': -1.219514726368904, 'right_w0': -0.043334957257762936, 'right_w1': 0.5395777421386942, 'right_w2': -0.4410194765170565, 'right_e0': -0.05944175553055978, 'right_e1': 2.1360682471304386})

	#lift and move towards position
	right.move_to_joint_positions({'right_s0': 0.3271214030165645, 'right_s1': -1.071869075534933, 'right_w0': -0.03911651009107805, 'right_w1': 0.14304370847031483, 'right_w2': -0.5997864880631968, 'right_e0': -0.08820389530341129, 'right_e1': 2.2844808883583525})

	#set it down
	right.move_to_joint_positions({'right_s0': 0.1564660403643122, 'right_s1': -0.6569272724119284, 'right_w0': -0.41762626950180387, 'right_w1': -0.17640779060682257, 'right_w2': -0.2757330466224031, 'right_e0': -0.004601942363656241, 'right_e1': 2.1406701894940947})

	#settt it down
	right.move_to_joint_positions({'right_s0': 0.1392087565006013, 'right_s1': -0.6626797003664987, 'right_w0': -0.5184855063052698, 'right_w1': -0.23623304133435372, 'right_w2': -0.3144660615165098, 'right_e0': -0.013038836697026017, 'right_e1': 2.1705828148578603})

	#open
	rightg.open()

	#lift
	right.move_to_joint_positions({'right_s0': 0.3271214030165645, 'right_s1': -1.071869075534933, 'right_w0': -0.03911651009107805, 'right_w1': 0.14304370847031483, 'right_w2': -0.5997864880631968, 'right_e0': -0.08820389530341129, 'right_e1': 2.2844808883583525})

	rightg.open()

def run_cookie():
	#print "running cookie"
	wait()
	send_voice(V_WELCOME)
	wait()
	send_voice(V_GET_ORDER)
	wait()
	arm_give_cookie()
	wait()
	send_voice(V_GIVE_ORDER)


def run_A():
	print "Condition A"
	run_cookie()
	wait()
	send_voice(V_WELCOME)
	wait()
	send_voice(V_GET_ORDER)
	wait()
	arm_give_sandwichA()
	arm_give_condimentA()
	wait()
	send_voice(V_GIVE_ORDER)


def run_B():
	print "Condition B"
	run_cookie()
	wait()
	send_voice(V_WELCOME)
	wait()
	send_voice(V_GET_ORDER)
	wait()
	arm_give_sandwichB()
	arm_give_condimentC()
	wait()
	send_voice(V_GIVE_ORDER)


def run_C():
	print "Condition C"
        run_cookie()
	wait()
	send_voice(V_WELCOME)
	wait()
	send_voice(V_GET_ORDER)
	wait()
	arm_give_sandwichC()
	arm_give_condimentC()
	wait()
	send_voice(V_GIVE_ORDER)


def reset():
	print "Reset food"
	arm_take_pos()
	wait()
	arm_reset_cookie()
	arm_take_pos()
	wait()
	arm_reset_sandwich()
	arm_take_pos()
	wait()
	arm_reset_condiment()
	print "Finished reset."


def run_condition(cond):
	if cond == 'A':
	    run_A()
	elif cond == 'B':
	    run_B()
	elif cond == 'C':
	    run_C()
	elif cond == 'r':
	    reset()
	else:
	    print "Invalid condition: %s (enter only A, B, or C)" % condition
	    sys.exit(2)


if __name__ == "__main__":

# Read condition
	if len(sys.argv) < 2:
	    print "Please specify a condition (A, B, C, or reset)"
	    sys.exit(1)

	condition = sys.argv[1][0]

	run_condition(condition)

	time.sleep(2)
