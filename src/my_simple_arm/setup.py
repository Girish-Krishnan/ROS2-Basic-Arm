from setuptools import find_packages, setup

package_name = 'my_simple_arm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
        data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/my_simple_arm']),
        ('share/my_simple_arm', ['package.xml']),
        ('share/my_simple_arm/launch', ['launch/display.launch.py']),
        ('share/my_simple_arm/urdf', ['urdf/simple_arm.urdf.xacro']),
        ('share/my_simple_arm/rviz', ['rviz/arm.rviz']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='ubuntu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
