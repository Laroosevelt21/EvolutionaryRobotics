import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import os.path
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

backLegAmplitude = numpy.pi/4.15
backLegFrequency = 8.0
backLegPhaseOffset = 0

frontLegAmplitude = numpy.pi/7
frontLegFrequency = 7.9
frontLegPhaseOffset = numpy.pi/2.9

backLegTargetAngles = backLegAmplitude * numpy.sin(numpy.linspace(-backLegFrequency *numpy.pi +backLegPhaseOffset, backLegFrequency *numpy.pi + backLegPhaseOffset, num=1000))

frontLegTargetAngles = frontLegAmplitude * numpy.sin(numpy.linspace(-frontLegFrequency*numpy.pi +frontLegPhaseOffset, frontLegFrequency *numpy.pi+frontLegPhaseOffset, num=1000))
##numpy.save(os.path.join('data', 'backLegTargetAngles.npy'), backLegTargetAngles)
##numpy.save(os.path.join('data', 'frontLegTargetAngles.npy'), frontLegTargetAngles)


for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = backLegTargetAngles[i], maxForce = 30)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL, targetPosition = frontLegTargetAngles[i], maxForce = 30)
    time.sleep(1.0/500.0)
    
p.disconnect()
##numpy.save(os.path.join('data', 'backLegSensorValues.npy'), backLegSensorValues)
##numpy.save(os.path.join('data', 'frontLegSensorValues.npy'), frontLegSensorValues)
##print(backLegSensorValues)
    
