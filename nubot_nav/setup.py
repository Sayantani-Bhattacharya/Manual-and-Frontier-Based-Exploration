from setuptools import find_packages, setup

package_name = 'nubot_nav'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),                                   
        ('share/' + package_name + '/config', ['config/nubot_urdf.rviz', 'config/slam_params_async.yaml']),
        # ('share/' + package_name + '/urdf', ['urdf/nubot.urdf.xacro', 'urdf/nubot.gazebo.xacro']),
        # ('share/' + package_name + '/env-hooks', ['env-hooks/nubot.dsv']),
        # ('share/' + package_name + '/worlds', ['worlds/nubot_world.sdf', 'worlds/nubot_simple.sdf']),
        ('share/' + package_name + '/launch', ['launch/manual_explore.launch.xml'])
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sayantani',
    maintainer_email='sayantanibhattacharya2025@u.northwestern.edu',
    description='Navigation for nubot',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
