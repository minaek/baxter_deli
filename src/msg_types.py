## Common message definitions

## Voice commands

index_to_string = dict()
index_to_path = dict()

V_WELCOME = 1
V_GET_ORDER = 2
V_GIVE_ORDER = 3
V_WARN = 4

index_to_string[V_WELCOME] = "Welcome to Baxter Deli.  May I take your order?"
index_to_string[V_GET_ORDER] = "Okay, let me get that for you."
index_to_string[V_GIVE_ORDER] = "Here you go. Have a nice day."
index_to_string[V_WARN] = "I sometimes have difficulty with more complex orders."

index_to_path[V_WELCOME] = "/home/baxter_deli/ros_ws/src/competence_study/Welcome.wav" 
index_to_path[V_GET_ORDER] = "/home/cs4752/ros_ws/src/competence_study/get_order.wav"
index_to_path[V_GIVE_ORDER] = "/home/cs4752/ros_ws/src/competence_study/give_order.wav"
index_to_path[V_WARN] = "/home/cs4752/ros_ws/src/competence_study/warn.wav"

