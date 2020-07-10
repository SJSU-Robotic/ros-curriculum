# ROS Track | Module 4
Handling remote procedure calls, telemetry, and bugs

Navigate to [README](README.md) | [Module 3](module3.md) ⬅️ Module 4 ➡️ [Module 5](module5.md)

---
## Topics to be discussed
* ROS services
* ROS actions (actionlib)
* ROS time
* ROS bags
* Debugging strategies

---
## Readings
* [Lecture 4 Slides](readings/lecture4.pdf)
* [ROS official documentation](http://wiki.ros.org/)
    * [ROS Services](http://wiki.ros.org/Services)
    * [`actionlib` package summary](http://wiki.ros.org/actionlib)
    * [ROS Clock](http://wiki.ros.org/Clock)
    * Handling time and duration in ROS
        * [Using `roscpp` (C++)](http://wiki.ros.org/roscpp/Overview/Time)
        * [Using `rospy` (Python)](http://wiki.ros.org/rospy/Overview/Time)
    * [ROS Bags](http://wiki.ros.org/Bags)
    * [`rosbag` package summary](http://wiki.ros.org/rosbag)
    * Testing and debugging resources
        * [Unit Testing](http://wiki.ros.org/action/show/Quality/Tutorials/UnitTesting?action=show&redirect=UnitTesting)
            * [`gtest` package for `roscpp` nodes using Google Test](http://wiki.ros.org/gtest)
            * [`unittest` package for `rospy` nodes using Python's unit testing framework](http://wiki.ros.org/unittest)
            * [`rostest` package for integrating tests into ROS build and test setups](http://wiki.ros.org/rostest)
        * [How to Roslaunch Nodes in Valgrind or GDB](http://wiki.ros.org/roslaunch/Tutorials/Roslaunch%20Nodes%20in%20Valgrind%20or%20GDB)
* Textbook 
    * [Chapter 7 | Parameters](readings/rostext-ch7.pdf)
    * [Chapter 8 | Services](readings/rostext-ch8.pdf)
    * [Chapter 9 | Recording and replaying messages](readings/rostext-ch9.pdf)

---
## Lecture Videos
* [Lecture 4](https://www.youtube.com/watch?v=feXC7aQrkeM&list=PLE-BQwvVGf8HOvwXPgtDfWoxd4Cc6ghiP&index=4)

---
## [Tutorials](http://wiki.ros.org/ROS/Tutorials)
1. [Creating a ROS `msg` and `srv`](http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv)
2. [Using `msg`s and `srv`s in your node implementation files](http://wiki.ros.org/ROS/Tutorials/DefiningCustomMessages)
    * For `roscpp` nodes, be sure to declare your `msg` and `srv` dependencies in the `package.xml` and `CMakeList.txt` as shown [in this example](http://wiki.ros.org/ROS/Tutorials/DefiningCustomMessages)
2. Writing a Simple Service and Client
    * [Using `roscpp` (C++)](http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28c%2B%2B%29)
    * [Using `rospy` (Python)](http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28python%29)
3. [Examining the Simple Service and Client](http://wiki.ros.org/ROS/Tutorials/ExaminingServiceClient)
4. [Recording and playing back data](http://wiki.ros.org/ROS/Tutorials/Recording%20and%20playing%20back%20data)
5. [Getting started with `roswtf`](http://wiki.ros.org/ROS/Tutorials/Getting%20started%20with%20roswtf)
    * [`roswtf` allegedly](https://answers.ros.org/question/277428/what-does-roswtf-mean/) stands for "where's the fire" 🔥
6. [`actionlib` tutorials](http://wiki.ros.org/actionlib/Tutorials)
7. [`rosbag` tutorials](http://wiki.ros.org/rosbag/Tutorials)

---
## Assignment
* [Exercise 4](assignments/exercise4.pdf)
    * The `husky_navigation.bag` file is available at [this Google Drive link](https://drive.google.com/file/d/1nEjQloB1lQNSKgFCU6TovC-YJktFa9ez/view?usp=sharing)