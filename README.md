# ROS1Tutorials

## Start a ros node from terminal

to start ros master type : `roscore`
TO start Talker example you have to type :`rosrun rospy_tutorials talker`
To start listener: `rosrun rospy_tutorials listener`
TO show the graph of nodes type `rqt_graph`

try different nodes
Run with : `rosrun turtlesim  turtlesim_node`
To control it with keyboadr : `rosrun turtlesim  turtle_teleop_key`

## Create catkin_ws

* `cd ROS1Tutorials`
* `mkdir catkin_ws`
* `cd catkin_ws`
* `mkdir src`
* `catkin_make `

  If we go to the devel folder
* `cd devel/`
* and type `ls`

So you will se a folder name `setup.bash`. To use the code we written we have to source this setup.bash file.

To source it you can type `cd `than source `~/ROS1Tutorials/catkin_ws/devel/setup.bash`

Or add it to .bahrc file and source it(preffered)

* First go to home directory by typing `cd`.
* Add it to .bashrc using `gedit ~/.bashrc`
* Save and source .bashrc using   `source ~/.bashrc`

## Create a Ros Package

* Go to source folder `cd ~/ROS1Tutorials/catkin_ws/src`
* To create a package you have to write `catkin_create_pkg <package name> < dependecies>` in our case we will create like this `catkin_create_pkg my_robot_controller rospy turtlesim`
* Inside source my_robot_controller package is created. Inside it you can see CMakeLists.txt file this file help us to create excutables and compile code for C++ And with ROS it also help us to create custom ros messages
* Let's explain packae.xml you can take a look to default comments to add ad depend later you can it like `<exec_depend>turtlesim</exec_depend>`
* After any change you do you have to go the the workspace main folder directory here it is catkin_ws and build it using `catkin_make` command
* if you go inside build you will have to see a folder named my_robot_controller

## Write a ROS Node with Python

* Go to src file

  ```
  cd ~/ROS1Tutorials/catkin_ws/src/my_robot_controller/

  ```
* Create a file named scripts for our python scripts `mkdir scripts`
* Go to the direction created and make a new python file

  ```
  cd scripts
  touch my_first_node.py
  ```
* Let's make it excutable with this command

  ```
  chmod +x my_first_node.py
  ```
* Let's write a node in our python file
* You can install Cmake , python and ROS extensions in vscode
* run it with `python3 my_first_node.py`
* Because it is executable you can also run it `./my_first_node.py`
* Go to home directory with `cd` than run `rosrun my_robot_controller my_first_node.py`
* You can use `rosnode list` command to list ros nodes
* You can use `rosnode kill/<node_name>` for us it will be `rosnode kill /test_node`

  ## ROS Topic
* Run `roscore` if we run `rosrun rospy_tutorials talker` and `rosrun rospy_tutorials talker`
* `rostopic list` list your topics you will have the chatter topic you can see it also with `rqt_graph`
* To get info about the topic run `rostopic info /chatter` this will give you the following output

  ```
  Type: std_msgs/String

  Publishers: 
   * /talker_66445_1694860591067 (http://ubuntu:43059/)

  Subscribers: 
   * /listener_66698_1694860618145 (http://ubuntu:42305/)

  ```
* `rosmsg show std_msgs/String` the output of this command wiill be string data it is is the containt of it.
* To listen a topic and what is send to it `rostopic echo /chatter`

### Rostopic with turtlesim

* Run `rosrun turtlesim turtlesim_node`
* To draw square `rosrun turtlesim draw_square`
* run `rqt_graph` ![1694862683096](image/README/1694862683096.png)
* `rostopic list`
* `rostopic info /turtle1/pose`
* Run `rosmsg show turtlesim/Pose` you will get output

  ```
  float32 x
  float32 y
  float32 theta
  float32 linear_velocity
  float32 angular_velocity
  ```

  This is the data inside the message
* To listen the topic `rostopic echo /turtle1/pose`

## Write a ROS publisher with python

* `cd ~/ROS1Tutorials/catkin_ws/src/my_robot_controller/scripts/`
* Create a new python file `touch draw_circle.py`
* make it executable `chmod +x draw_circle.py`
* `rosrun turtlesim turtlesim_node`
* Run `rostopic list` this will give the following output

  ```
  /rosout
  /rosout_agg
  /turtle1/cmd_vel
  /turtle1/color_sensor
  /turtle1/pose
  ```
* Get topic info bu running `rostopic info /turtle1/cmd_vel` this will give this output

  ```
  Type: geometry_msgs/Twist

  Publishers: None

  Subscribers: 
   * /turtlesim (http://ubuntu:32789/)
  ```
* Take a look to message data by running `rosmsg show geometry_msgs/Twist ` that will show

  ```
  rosmsg show geometry_msgs/Twist
  geometry_msgs/Vector3 linear
    float64 x
    float64 y
    float64 z
  geometry_msgs/Vector3 angular
    float64 x
    float64 y
    float64 z
  ```
* Add geometry_msgs to dependencies inside package.xml

  ```
  <build_depend>geometry_msgs</build_depend>
  <build_export_depend>geometry_msgs</build_export_depend>
  <exec_depend>geometry_msgs</exec_depend>
  ```
* Than run the drawcircle.py file

## Write a ROS subscriber with python

* Run `roscore`
* Run the turtlesim node `rosrun turtlesim turtlesim_node`
* Run `rostopic list `will give you the following topics

  ```
  /rosout
  /rosout_agg
  /turtle1/cmd_vel
  /turtle1/color_sensor
  /turtle1/pose
  ```
* Run `rostopic info /turtle1/pose ` give you:

  ```
  Type: turtlesim/PosePublishers:/turtlesim (http://ubuntu:39733/)Subscribers: None
  ```
* So we can write a subscriber that subscriber to this topic

  ```
  cd ~/ROS1Tutorials/catkin_ws/src/my_robot_controller/scripts
  touch pose_subscriber.py
  chmod +x pose_subscriber.py 

  ```
* Run you script and you can run `rosrun turtlesim turtle_teleop_key` for test it

## Combine Publisher and Subscriber in a closed loop system

* Let's write a new file

  ```
  cd ~/ROS1Tutorials/catkin_ws/src/my_robot_controller/scripts
  touch turtle_controller.py
  chmod +x turtle_controller.py 

  ```
* We will write a code the turtle have to go and when it will near the wall it will be turn smoothly and complete going.

## Understand what is ROS Service

We have topics to communicate between node but we want a kind of client server interaction . A node have to be able to send a request to anathor node and the other node response.

* Run `roscore`
* Run `rosrun rospy_tutorials add_two_ints_server` it seems not do anything
* Run in other terminal `rosservice list` this will has output as follow:

  ```
  /add_two_ints
  /add_two_ints_server/get_loggers
  /add_two_ints_server/set_logger_level
  /rosout/get_loggers
  /rosout/set_logger_level

  ```
* Run `rosservice info /add_two_ints` the output will be as follow:

  ```
  Node: /add_two_ints_server
  URI: rosrpc://ubuntu:33689
  Type: rospy_tutorials/AddTwoInts
  Args: a b
  ```

  This mean that this service is advertised by the add_two_ints_server node. and have input arguments a and b
* Let's send a client request by running `rosservice call /add_two_ints "a: 4 b: 2"` the output will be `sum:6` and you will be able to see in window we run the service this output : `Returning [4 + 2 = 6]`
* You can run the following command to show the message data type : `rossrv show rospy_tutorials/AddTwoInts` this will return

  ```
  int64 a
  int64 b
  ---
  int64 sum
  ```

### Let's try it with turtlesim

* Close the service before and Run `rosrun turtlesim turtlesim_node`
* list the rosservice by `rosservice list` the output will be

  ```
  /clear
  /kill
  /reset
  /rosout/get_loggers
  /rosout/set_logger_level
  /spawn
  /turtle1/set_pen
  /turtle1/teleport_absolute
  /turtle1/teleport_relative
  /turtlesim/get_loggers
  /turtlesim/set_logger_level

  ```
* Let's run `rosservice info /turtle1/set_pen` to take a look to set_pen. output will be:

  ```
  Node: /turtlesim
  URI: rosrpc://ubuntu:40265
  Type: turtlesim/SetPen
  Args: r g b width off
  ```
* Run `rossrv show turtlesim/SetPen` to get info about the message type. Output will be:

  ```
  uint8 r
  uint8 g
  uint8 b
  uint8 width
  uint8 off
  ```
* Let's change the color of the white  line that appear back to the turtle when turtle run. First run `rosrun turtlesim turtle_teleop_key` and move the turtle to see the white line. Than run `rosservice call /turtle1/set_pen "{r: 255, g: 0, b: 0, width: 4, 'off': 0}"` to make the line red and move the turtle and see it.
* Remind that you can't see services in rqt_graph
* You can use topics when you need to fast data like velocity , services will be usable to request a data that is required in a specific time

## Write a ROS Service Client with python

* First take a look previews tutorial.
* We will split the screen to 2 the left side will be use red pen , in the right side green pin.
* rewrite turtle_controller.py by adding a service waite and rename it turtle_controller_service.py and make it executable using `chmod +x turtle_controller_service.py`
* To show the frequency of a topic you can write

  ```
  rostopic hz <topicname>
  ```
  for us it will be `rostopic hz /turtle1/pose`
