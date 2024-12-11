from setuptools import find_packages, setup

package_name = 'spawn_tortoisebots'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/spawn_tortoisebots']),
        ('share/spawn_tortoisebots', ['package.xml']),
        ('share/spawn_tortoisebots/launch', ['launch/spawn.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rishang',
    maintainer_email='b23173@students.iitmandi.ac.in',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
