## Part1: Manual Exploration

#### To launch:
ros2 launch nubot_nav manual_explore.launch.xml

#### The video of nubot exploring the entire scene:
https://github.com/ME495-EmbeddedSystems/homework-4-Sayantani-Bhattacharya/issues/1#issue-2704242083

## Part2: Frontier-Based Autonomous Exploration

#### Explanation of the algorithm:
 Occupancy grid generated by the slam toolbox, from gazebo sensor data is used to detect all 
 the possible frontiers in the current map. All the elements in grid are checked, and if the currect element 
 is free and at least one neighbout is unknown then that is added to a list of frontiers.

 This list is then used to evaluate the pose that is closest to the current pose of the nubot, but more than 
 a threshold distance. The threshold distance was added, because the least ditance was too small, and caused the
 bot to assume it reached goal, and it remained motionless.

 The value of threshold distance can be tuned as well. Increasing this value will causse it to explore faster, 
 but too high will leave sections unexplored [Works well with 0.6].

#### Future: 
   The frontiers' selection could be cluster based, and the centroid of the chosen cluster can be used as target pose.

#### To launch:
ros2 launch nubot_nav explore.launch.xml

#### The video of nubot exploring the entire scene:
https://github.com/ME495-EmbeddedSystems/homework-4-Sayantani-Bhattacharya/issues/2#issue-2713177773
