# ROS Track | Module 1
ROS framework basics

Navigate to [README](README.md) | Module 1 ➡️ [Module 2](module2.md)

---
## Topics to be discussed
* ROS architecture & philosophy
* ROS master, nodes, and topics
* Console commands
* Catkin workspace and build system
* Launch-​files
* Gazebo simulator
* Programming Tools

---
## Readings
* [Lecture 1 Slides](readings/lecture1.pdf)
* [ROS official documentation](http://wiki.ros.org/)
    * [Navigating the ROS wiki](http://wiki.ros.org/ROS/Tutorials/NavigatingTheWiki)
    * [Technical overview](http://wiki.ros.org/ROS/Technical%20Overview)
    * [ROS master](http://wiki.ros.org/Master)
    * [ROS nodes](http://wiki.ros.org/Nodes)
    * [ROS topics](http://wiki.ros.org/Topics)
    * [ROS messages](http://wiki.ros.org/Messages)
    * [roscore](http://wiki.ros.org/roscore)
    * [ROS concepts and names](http://wiki.ros.org/ROS/Concepts)
        * Concepts
            * Filesystem
            * Computation graph
            * Community
        * Names
            * Graph resources
            * Package resources
    * [A rundown of the `catkin` workspace file structure](http://wiki.ros.org/catkin/workspaces)
    * [XML syntax](https://www.w3schools.com/xml/xml_syntax.asp), which are used in `.launch`, `.urdf`, and `.sdf` files
    * [YAML syntax](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html), which are used in `.msg`, and `.srv` files
        * **Note**: YAML syntax is also used in the [ROS command line](http://wiki.ros.org/ROS/YAMLCommandLine)
    * [`roslaunch` tips for large project](http://wiki.ros.org/roslaunch/Tutorials/Roslaunch%20tips%20for%20larger%20projects)
* [Cheatsheet for `catkin-tools`](https://catkin-tools.readthedocs.io/en/latest/cheat_sheet.html)
* [(Optional) Gazebo Tutorials](http://www.gazebosim.org/tutorials)
* Textbook 
    * [Chapter 1 | Introduction](https://www.cse.sc.edu/~jokane/agitr/agitr-letter-intro.pdf)
    * [Chapter 2 | Getting started](https://www.cse.sc.edu/~jokane/agitr/agitr-letter-start.pdf)

---
## Lecture Videos
* [Lecture 1](https://youtu.be/0BxVPCInS3M?list=PLE-BQwvVGf8HOvwXPgtDfWoxd4Cc6ghiP)

---
## [Tutorials](http://wiki.ros.org/ROS/Tutorials)
1. [Installing and configuring your ROS environment](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)
    * [Compare with the `catkin-tools` quickstart quide](https://catkin-tools.readthedocs.io/en/latest/quick_start.html)
    * [Using `catkin init` instead of `catkin_make`](https://catkin-tools.readthedocs.io/en/latest/verbs/catkin_init.html)
    * [Using `catkin` vs `catkin_make`](https://catkin-tools.readthedocs.io/en/latest/migration.html#important-distinctions-between-catkin-make-and-catkin-build)
2. [Navigating the ROS filesystem](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)
3. [Creating a ROS package](http://wiki.ros.org/ROS/Tutorials/CreatingPackage)
    * [Using `catkin create pkg` instead of `catkin_create_pkg`](https://catkin-tools.readthedocs.io/en/latest/verbs/catkin_create.html)
4. [Building a ROS package](http://wiki.ros.org/ROS/Tutorials/BuildingPackages)
    * [Using `catkin build` instead of `catkin_make`](https://catkin-tools.readthedocs.io/en/latest/verbs/catkin_build.html)
5. [Understanding ROS nodes](http://wiki.ros.org/ROS/Tutorials/UnderstandingNodes)

---
## Assignment
* [Exercise 1](assignments/exercise1.pdf)
    * [Link to `husky_gazebo/Tutorials/Simulating%20Husky`](http://wiki.ros.org/husky_gazebo/Tutorials/Simulating%20Husky)
