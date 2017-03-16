#steak and cheese melt:
	#gripper: the wide squares (right)
	#holding force: 100

#oatmeal raisin cookie( both ):
	#gripper: narrow (left)
	#holding force: 50


#oatmeal raisin cookie( one ):
	#gripper: narrow (left)
	#holding force: 40

#replace cookie with drink 

#individually wrapped triangle sandwich will not do

#!/usr/bin/env python

import rospy, baxter_interface
from baxter_interface import Gripper, Head, Limb

rospy.init_node('deli_Baxter')
rightg = Gripper('right')
rightg.set_holding_force(100)
leftg = Gripper('left')
right = Limb('right')
left = Limb('left')
head = Head()
head.set_pan(0.0, speed = 0.8, timeout = 0.0)

Gripper.calibrate(rightg)
Gripper.calibrate(leftg)

neutral_right ={'right_s0': 0.5971020216843973, 'right_s1': -0.4237621926533455, 'right_w0': 0.4226117070624315, 'right_w1': 0.8471408901097197, 'right_w2': -0.9725438195193523, 'right_e0': -0.40727189918357737, 'right_e1': 1.161990446823201}

neutral_left = {'left_w0': -0.3006602344255411, 'left_w1': 0.5549175500175484, 'left_w2': 3.050704291907117, 'left_e0': 0.5161845351234418, 'left_e1': 1.1984224905354794, 'left_s0': -0.8904758473674826, 'left_s1': -0.38387869216832476}


right.move_to_joint_positions(neutral_right)
left.move_to_joint_positions(neutral_left)



####PART 1 ("what would you like today")
#can we track the person with Baxter's head?


###PART 2 (COOKIE)
Head.set_pan(head, 0.45, speed = 1.0, timeout = 0.0) #looks at cookie section

#lifts arm above cookies
left.move_to_joint_positions({'left_w0': -0.177941771394708, 'left_w1': 1.131694326262464, 'left_w2': 3.0161897241796947, 'left_e0': 0.24965537322835107, 'left_e1': 0.8038059328519568, 'left_s0': -0.7320923310183137, 'left_s1': -0.4571262747898533}
)

#lowers to grab cookie
left.move_to_joint_positions({'left_w0': -1.2367720102326147, 'left_w1': 0.5027622032294443, 'left_w2': 3.008519820240268, 'left_e0': 0.33709227813781967, 'left_e1': 1.2870098810358621, 'left_s0': -0.5944175553055978, 'left_s1': -0.3739078170470696}
)

#swoops in
left.move_to_joint_positions({'left_w0': -1.4741555371578825, 'left_w1': 0.4049709280017492, 'left_w2': 3.0158062289827234, 'left_e0': 0.3324903357741634, 'left_e1': 1.2421409429902137, 'left_s0': -0.6270146470481629, 'left_s1': -0.27228158984966094}
)

#grippers close
leftg.close()

#lifts a little bit
left.move_to_joint_positions({'left_w0': -1.474539032354854, 'left_w1': 0.3278883934105072, 'left_w2': 3.0165732193766663, 'left_e0': 0.33325732616810616, 'left_e1': 1.2950632801722606, 'left_s0': -0.6645971763513555, 'left_s1': -0.362402961137929}
)

#lifts more
left.move_to_joint_positions({'left_w0': -1.476840003536682, 'left_w1': 0.26307770512234846, 'left_w2': 3.0108207914220957, 'left_e0': 0.35856800916821546, 'left_e1': 1.4848934026730805, 'left_s0': -0.8279661302611521, 'left_s1': -0.7827136970185323}
)

#head turns to customer
head.set_pan(0.0, speed = 0.8, timeout = 0.0)

#lowers
left.move_to_joint_positions({'left_w0': -1.5079031144913617, 'left_w1': 0.2067039111675595, 'left_w2': 3.008519820240268, 'left_e0': 0.3466796580621035, 'left_e1': 0.8847234194129123, 'left_s0': -0.9955535313376335, 'left_s1': -0.11543205428837738}
)

#sets on table
left.move_to_joint_positions({'left_w0': -1.5082866096883332, 'left_w1': 0.2059369207736168, 'left_w2': 3.0158062289827234, 'left_e0': 0.33977674451661916, 'left_e1': 0.9265243958827899, 'left_s0': -0.9963205217315763, 'left_s1': -0.07017962104575767}
)

#opens gripper
leftg.open()

#lifts
left.move_to_joint_positions({'left_w0': -1.5293788455217574, 'left_w1': 0.23431556534949696, 'left_w2': 3.017340209770609, 'left_e0': 0.381961216183468, 'left_e1': 1.3245924103390547, 'left_s0': -1.0672671331712766, 'left_s1': -0.3508981052287884}
)

#lifts higher
#left.move_to_joint_positions({'left_w0': -0.171422353046195, 'left_w1': 0.48703890015361884, 'left_w2': 3.0169567145736376, 'left_e0': 0.24773789724349432, 'left_e1': 1.4162477624152083, 'left_s0': -0.9368787662010164, 'left_s1': -0.7044806768363763}
#)

#move to neutral
left.move_to_joint_positions(neutral_left)

#close grippers
leftg.close()

####PART 3 (SANDWICH)#################

leftg.open()

#gaze shifts to left
head.set_pan(0.55, speed = 0.3, timeout = 0.0)

#moves towards the plate
left.move_to_joint_positions({'left_w0': 1.244441914172042, 'left_w1': -0.68568941218478, 'left_w2': 2.079310957978678, 'left_e0': 0.22050973825852824, 'left_e1': 1.9500730765993322, 'left_s0': -0.2726650850466323, 'left_s1': -0.4007524808350643}
)

#grabs the plate
left.move_to_joint_positions({'left_w0': 1.00590790165586, 'left_w1': -0.6599952339876992, 'left_w2': 2.1629129109184335, 'left_e0': 0.2542573155920073, 'left_e1': 1.995325509841952, 'left_s0': -0.388480634531981, 'left_s1': -0.3846456825622675}
)

#grippers close
leftg.close()

#lifts plate
left.move_to_joint_positions({'left_w0': 0.4195437454866607, 'left_w1': -1.2985147369450027, 'left_w2': 1.5489371005672965, 'left_e0': 0.3685388842894706, 'left_e1': 2.2457478734642455, 'left_s0': -0.7842476778064178, 'left_s1': -0.6312330942148477}
)

#shift gaze towards center
head.set_pan(0.0, speed = 0.3, timeout = 0.0)


#lifts further
left.move_to_joint_positions({'left_w0': 0.324436936637765, 'left_w1': -0.6668981475331837, 'left_w2': 1.5892040962492886, 'left_e0': 0.26691265709206197, 'left_e1': 1.634073034294937, 'left_s0': -0.9414807085646727, 'left_s1': -0.4667136547141371}
)

#moves plate towards center
left.move_to_joint_positions({'left_w0': 0.2646116859102339, 'left_w1': -0.4789855010172204, 'left_w2': 1.2950632801722606, 'left_e0': 0.3390097541226764, 'left_e1': 1.4231506759606927, 'left_s0': -1.1819321970657113, 'left_s1': -0.2922233400921713}
)

#sets plate down
left.move_to_joint_positions({'left_w0': 0.2634612003193198, 'left_w1': -0.2109223583342444, 'left_w2': 1.29774774655106, 'left_e0': 0.3378592685317624, 'left_e1': 1.1524030668989171, 'left_s0': -1.2057088992779352, 'left_s1': -0.10431069357620813}
, timeout = 20.0)

#grippers open
leftg.open()

#lifts
left.move_to_joint_positions({'left_w0': 0.3551165523954733, 'left_w1': -0.8459904045188057, 'left_w2': 1.2198982215658754, 'left_e0': 0.3834951969713534, 'left_e1': 1.393238050596927, 'left_s0': -1.1117525760199536, 'left_s1': -0.11389807350049197}
)

#moves to neutral 
left.move_to_joint_positions(neutral_left)




Head.set_pan(head, -0.45, speed = 1.0, timeout = 0.0) #looks at cookie section
#lifts arm above sandwiches
right.move_to_joint_positions({'right_s0': 0.7719758315033345, 'right_s1': -0.6446554261088451, 'right_w0': 0.27074760906177553, 'right_w1': 0.984048675428493, 'right_w2': -0.2922233400921713, 'right_e0': -0.26307770512234846, 'right_e1': 1.2616991980357528}
)


#shifts gaze left
Head.set_pan(head, -0.30, speed = 0.3, timeout = 0.0)
#shifts left
right.move_to_joint_positions({'right_s0': 1.0511603348984797, 'right_s1': -0.6799369842302097, 'right_w0': 0.2607767339405203, 'right_w1': 0.7972865145034438, 'right_w2': -0.17027186745528092, 'right_e0': -0.3136990711225671, 'right_e1': 1.393238050596927}
)

#shifts gaze back right
Head.set_pan(head, -0.55, speed = 0.3, timeout = 0.0)
#shifts back right
right.move_to_joint_positions({'right_s0': 0.8080243800186417, 'right_s1': -0.6273981422451342, 'right_w0': 0.324436936637765, 'right_w1': 0.7792622402457902, 'right_w2': -0.24275245968286674, 'right_e0': -0.3037281960013119, 'right_e1': 1.367160377202875}
)

#shifts gaze left
Head.set_pan(head, -0.30, speed = 0.3, timeout = 0.0)
#shifts left
right.move_to_joint_positions({'right_s0': 1.0511603348984797, 'right_s1': -0.6799369842302097, 'right_w0': 0.2607767339405203, 'right_w1': 0.7972865145034438, 'right_w2': -0.17027186745528092, 'right_e0': -0.3136990711225671, 'right_e1': 1.393238050596927}
)

#shifts gaze back right
Head.set_pan(head, -0.55, speed = 0.3, timeout = 0.0)

#shifts back right
right.move_to_joint_positions({'right_s0': 0.8080243800186417, 'right_s1': -0.6273981422451342, 'right_w0': 0.324436936637765, 'right_w1': 0.7792622402457902, 'right_w2': -0.24275245968286674, 'right_e0': -0.3037281960013119, 'right_e1': 1.367160377202875}
)


#lowers to grab it 
right.move_to_joint_positions({'right_s0': 0.8041894280489281, 'right_s1': -0.30871363356193954, 'right_w0': 0.47246608266870743, 'right_w1': 0.7156020375485456, 'right_w2': -0.3485971340469603, 'right_e0': -0.33325732616810616, 'right_e1': 1.1293933550806359}
)

#grippers close
rightg.close()

#lifts
right.move_to_joint_positions({'right_s0': 0.8041894280489281, 'right_s1': -0.48051948180510584, 'right_w0': 0.4628787027444236, 'right_w1': 0.7911505913519021, 'right_w2': -0.3508981052287884, 'right_e0': -0.3432282012893613, 'right_e1': 1.2317865726719872}
)


#set gaze back to customer
head.set_pan(0.0, speed = 0.8, timeout = 0.0)

#lifts higher
right.move_to_joint_positions({'right_s0': 0.9978545025194616, 'right_s1': -0.6435049405179311, 'right_w0': 0.4222282118654601, 'right_w1': 1.1501020957170889, 'right_w2': -0.34131072530450457, 'right_e0': -0.5986360024722828, 'right_e1': 1.1953545289597087}
)



#moves to middle
right.move_to_joint_positions({'right_s0': 1.315005030414771, 'right_s1': -0.24236896448589537, 'right_w0': 0.705247667230319, 'right_w1': 1.1117525760199536, 'right_w2': -0.0030679615757708274, 'right_e0': -0.6768690226544388, 'right_e1': 0.7827136970185323}
)

#lowers sandwich 
right.move_to_joint_positions({'right_s0': 1.3165390112026563, 'right_s1': 0.11543205428837738, 'right_w0': 0.7025632008515195, 'right_w1': 0.34092723010753323, 'right_w2': -0.1499466220157992, 'right_e0': -0.68568941218478, 'right_e1': 0.4437039428958559}
)

#sets sandwich on palte
right.move_to_joint_positions({'right_s0': 1.2958302705662033, 'right_s1': 0.20325245439481732, 'right_w0': 0.6952767921090638, 'right_w1': 0.22626216621309853, 'right_w2': -0.02339320701525256, 'right_e0': -0.6929758209272356, 'right_e1': 0.40151947122900705}
)

#opens gripper
rightg.open()

#lifts
right.move_to_joint_positions({'right_s0': 1.2693691019751798, 'right_s1': -0.13192234775814557, 'right_w0': 0.7911505913519021, 'right_w1': 0.9008302176857093, 'right_w2': -0.0030679615757708274, 'right_e0': -0.6929758209272356, 'right_e1': 0.66306319556347}
)

#lifts higher
right.move_to_joint_positions({'right_s0': 1.2693691019751798, 'right_s1': -0.13038836697026016, 'right_w0': 0.7926845721397876, 'right_w1': 0.9012137128826806, 'right_w2': -0.002684466378799474, 'right_e0': -0.693359316124207, 'right_e1': 0.66306319556347}
)

#shifts gaze back right
Head.set_pan(head, -0.55, speed = 0.3, timeout = 0.0)

#move to ketchup
right.move_to_joint_positions({'right_s0': 0.8287331206550947, 'right_s1': -0.5115825927597855, 'right_w0': 0.35971849475912954, 'right_w1': 0.5073641455931006, 'right_w2': -3.0591411862404865, 'right_e0': -0.4237621926533455, 'right_e1': 1.3905535842181276}
)

#move to mustard
right.move_to_joint_positions({'right_s0': 0.7474321388971679, 'right_s1': -0.28532042654668693, 'right_w0': 0.39346607209260864, 'right_w1': 0.8302671014429802, 'right_w2': -3.058757691043515, 'right_e0': -0.4249126782442596, 'right_e1': 0.8732185635037718}
)

#move to ketchup
right.move_to_joint_positions({'right_s0': 0.8287331206550947, 'right_s1': -0.5115825927597855, 'right_w0': 0.35971849475912954, 'right_w1': 0.5073641455931006, 'right_w2': -3.0591411862404865, 'right_e0': -0.4237621926533455, 'right_e1': 1.3905535842181276}
)

#lowers down on ketchup
right.move_to_joint_positions({'right_s0': 0.768140879533621, 'right_s1': -0.2665291618950906, 'right_w0': 0.43526704856248616, 'right_w1': 0.49547579448698864, 'right_w2': -3.058757691043515, 'right_e0': -0.4019029664259784, 'right_e1': 1.15892248524743}
,timeout = 15.0)

#grippers close
rightg.close()

#lifts
right.move_to_joint_positions({'right_s0': 0.9821311994436361, 'right_s1': -0.6178107623208504, 'right_w0': 0.33555829734993425, 'right_w1': 0.5303738574113818, 'right_w2': -3.0591411862404865, 'right_e0': -0.4778350154263064, 'right_e1': 1.504068162521648}
)


#shifts gaze back center
Head.set_pan(head, 0.0, speed = 0.3, timeout = 0.0)

#lifts more
right.move_to_joint_positions({'right_s0': 1.1362962686261202, 'right_s1': -0.7340098070031704, 'right_w0': 0.27074760906177553, 'right_w1': 1.0833739314440736, 'right_w2': -3.0591411862404865, 'right_e0': -0.4759175394414496, 'right_e1': 1.1255584031109223}
)



#moves towards plate
right.move_to_joint_positions({'right_s0': 1.2996652225359169, 'right_s1': -0.16298545871282522, 'right_w0': 0.2987427584406843, 'right_w1': 1.0051409112619174, 'right_w2': -3.0591411862404865, 'right_e0': -0.514267059138585, 'right_e1': 0.3324903357741634}
)

#lowers on plate
#right.move_to_joint_positions({'right_s0': 1.303116679308659, 'right_s1': 0.0674951546669582, 'right_w0': 0.30871363356193954, 'right_w1': 0.6028544496389676, 'right_w2': -3.0572237102556294, 'right_e0': -0.4341165629715721, 'right_e1': 0.31408256631953846}
#)

#sets down on plate
right.move_to_joint_positions({'right_s0': 1.331495323884539, 'right_s1': 0.16336895390979655, 'right_w0': 0.2972087776527989, 'right_w1': 0.18062623777350748, 'right_w2': -3.058757691043515, 'right_e0': -0.5146505543355563, 'right_e1': 0.41225733674420495}
)

#opens gripper
rightg.open()

#lifts
right.move_to_joint_positions({'right_s0': 1.2720535683539793, 'right_s1': 0.009587379924283835, 'right_w0': 0.2964417872588562, 'right_w1': 0.6703496043059258, 'right_w2': -3.0572237102556294, 'right_e0': -0.5725583290782307, 'right_e1': 0.146495165243057}
)

#move back to neutral
right.move_to_joint_positions(neutral_right)

#close gripper
rightg.close()













