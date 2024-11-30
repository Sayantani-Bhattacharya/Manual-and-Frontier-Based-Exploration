import rclpy
from rclpy.node import Node
import numpy as np
from nav_msgs.msg import OccupancyGrid
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
# nav2_simple_commander

class Explore(Node):
    """Autonomous navigation."""

    def __init__(self):
        super().__init__('explore')
        self.get_logger().info('Exploring the navigation stack init')
        self.map = None

        #  to get the current map.
        self.map_sub = self.create_subscription(OccupancyGrid, "map", self.map_callback, qos_profile=10)

        # Use /cmd_vel to publish velocity commands or /navigate_to_pose for higher-level navigation.

        self.targetPose = PoseStamped()
        self.targetPose.header.frame_id = "map"
        self.currentPose = PoseStamped()
        self.currentPose.header.frame_id = "map"

        self.posesub = self.create_subscription(PoseWithCovarianceStamped, "pose", self.pose_callback, qos_profile=10)
        self.goalposepub = self.create_publisher(PoseStamped, "goal_pose", 10)

        self.timer = self.create_timer(1.0, self.timer_callback)



    def map_callback(self, msg:OccupancyGrid):
        """
        Get the map explored by nubot.
        """
        self.map = msg

        # Map information
        self.map_width = msg.info.width
        self.map_height = msg.info.height
        self.map_resolution = msg.info.resolution
        self.map_origin = msg.info.origin
        self.map_load_time = msg.info.map_load_time

        self.grid = np.array(msg.data, dtype=np.int8).reshape((msg.info.height, msg.info.width))
        self.get_logger().info(f"Map received: shape={self.grid.shape}")
        self.get_logger().info(f"Free cells: {np.sum(self.grid == 0)}, Occupied cells: {np.sum(self.grid == 100)}, Unkown cells: {np.sum(self.grid == -1)}")


    def pose_callback(self,msg:PoseWithCovarianceStamped):
        """
        Get the current pose of the nubot.
        """
        self.currentPose.header.stamp = self.get_clock().now().to_msg()
        self.currentPose.pose = msg.pose.pose
        self.get_logger().info(f'Current pose received {self.currentPose.pose}')        

    def frontier_exp_algo(self):
        '''
        function to identify unexplored areas (frontiers) and send navigation goals to the robot.
        '''
        # Evedence Grids:
            # open: having an occupancy probability < prior probability       ----> 0
            # unknown: having an occupancy probability = prior probability    ----> -1
            # occupied: having an occupancy probability > prior probability   ----> 100

        # convert self.map to a matrix and output the pose where the robot should move next
        nextPose = 0
        return nextPose

    def timer_callback(self):
        if self.map is None:
            self.get_logger().info('Waiting for map...')
            return
        else:
            nextPose = self.frontier_exp_algo()
        
        # this should publish goalPose to nubot.
        # demo publishing
        self.targetPose.header.stamp = self.get_clock().now().to_msg()
        self.targetPose.pose = self.currentPose.pose 
        self.targetPose.pose.position.x = (self.currentPose.pose.position.x + 0.1)  
        self.targetPose.pose.position.x = (self.currentPose.pose.position.x + 0.2)  
        self.goalposepub.publish(self.targetPose)

    def save_final_map(self):
        self.get_logger().info('Saving the final generated map.')



def main(args=None):
    rclpy.init(args=args)
    node = Explore()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    import sys
    main(args=sys.argv)