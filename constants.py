##Constants that are used in simulate.py for robot and simulation environment
import numpy
##Robot
backLegAmplitude = numpy.pi/4
backLegFrequency = 14.0
backLegPhaseOffset = 0
frontLegAmplitude = numpy.pi/4
frontLegFrequency = 7.0
frontLegPhaseOffset = 0
motorForce = 30
numSensorNeurons = 4
numMotorNeurons = 8
motorJointRange = 0.4

##Simulation/Environment
timeSteps = 2000
gravity = -9.8
sleepTime = 1.0/1000.0

##Fitness Evaluation
numberOfGenerations = 20
populationSize = 50
