# ROS Track | Module 2
Writing subscribers and publishers, visualizing data

[Back to the README](README.md)

---
## Topics to be discussed
* ROS package structure
* ROS programming
* ROS client libraries
    * C++ library (roscpp)
    * Python library (rospy)
* ROS subscribers and publishers
* ROS parameter server
* RViz visualization

---
## Readings
* [Lecture 2 Slides](readings/lecture2.pdf)
* [ROS official documentation](http://wiki.ros.org/)
    * [ROS packages](http://wiki.ros.org/Packages)
    * [ROS package manifest](http://wiki.ros.org/Manifest)
    * [ROS makelists](http://wiki.ros.org/catkin/CMakeLists.txt)
    * ROS Client Libraries
        * [rospy](http://wiki.ros.org/rospy/Overview)
        * [roscpp](http://wiki.ros.org/roscpp/Overview)
    * ROS Publishers and Subscribers
        * [rospy](http://wiki.ros.org/rospy/Overview/Publishers%20and%20Subscribers)
        * [roscpp](http://wiki.ros.org/roscpp/Overview/Publishers%20and%20Subscribers)
    * [rosconsole](http://wiki.ros.org/rosconsole)
    * [ROS parameter server](http://wiki.ros.org/Parameter%20Server)
    * [rviz user guide](http://wiki.ros.org/rviz/UserGuide)
* Other links
    * [ROS Cheatsheet](https://github.com/ros/cheatsheet/releases/download/0.0.1/ROScheatsheet_catkin.pdf)
    * [ROS Best Practices](https://github.com/ethz-asl/ros_best_practices/wiki)
    * [ROS Package Template](https://github.com/ethz-asl/ros_best_practices/tree/master/ros_package_template)
* Textbook 
    * [Chapter 3 | Writing ROS programs](https://www.cse.sc.edu/~jokane/agitr/agitr-letter-intro.pdf)
    * [Chapter 4 | Log messages](https://www.cse.sc.edu/~jokane/agitr/agitr-letter-start.pdf)
    * [Chapter 5 | Graph resource names](https://www.cse.sc.edu/~jokane/agitr/agitr-letter-start.pdf)
    * [Chapter 6 | Launch files](https://www.cse.sc.edu/~jokane/agitr/agitr-letter-start.pdf)

---
## Lecture Videos
* [Lecture 2](https://www.youtube.com/watch?v=jYqDnuxTwK8&list=PLE-BQwvVGf8HOvwXPgtDfWoxd4Cc6ghiP&index=2)
    * Use of Eclipse is **NOT** necessary, we recommend [VS Code](https://code.visualstudio.com/) instead
    * We will run a similar tutorial using VS Code on Wednesday, but feel free to follow along the tutorial starting at 32:18

---
## [Tutorials](http://wiki.ros.org/ROS/Tutorials)
1. [Understanding ROS topics](http://wiki.ros.org/ROS/Tutorials/UnderstandingTopics)
2. [Understanding ROS Services and Parameters](http://wiki.ros.org/ROS/Tutorials/UnderstandingServicesParams)
3. [Using rqt_console and roslaunch](http://wiki.ros.org/ROS/Tutorials/UsingRqtconsoleRoslaunch)
4. Writing a Simple Publisher and Subscriber
    * [Using `roscpp` (C++)](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29)
    * [Using `rospy` (Python)](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)
5. [Examining the Simple Publisher and Subscriber](http://wiki.ros.org/ROS/Tutorials/ExaminingPublisherSubscriber)

---
## Assignment
* [Exercise 2](assignments/exercise2.pdf)
    * The `husky_highlevel_controller.zip` compressed package template is already in this repo at [`assignments/assets/husky_highlevel_controller.zip`](assignments/assets/husky_highlevel_controller.zip), but you are recommended to create the package from scratch