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
