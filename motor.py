import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
import os.path

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = numpy.zeros(c.timeSteps)
        self.Prepare_To_Act(self.jointName)
         

    def Prepare_To_Act(self, jointName):
        if jointName == 'Torso_BackLeg':
            self.amplitude = c.backLegAmplitude
            self.frequency = c.backLegFrequency
            self.offset = c.backLegPhaseOffset
            self.motorValues = self.amplitude * numpy.sin(numpy.linspace(-self.frequency *numpy.pi +self.offset, self.frequency *numpy.pi + self.offset, num=c.timeSteps))
        else:
            self.amplitude = c.frontLegAmplitude
            self.frequency = c.frontLegFrequency
            self.offset = c.frontLegPhaseOffset
            self.motorValues = self.amplitude * numpy.sin(numpy.linspace(-self.frequency *numpy.pi +self.offset, self.frequency *numpy.pi + self.offset, num=c.timeSteps))
            

        
    def Set_Value(self, robot, timeStep):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = self.motorValues[timeStep], maxForce = c.motorForce)

    def Save_Values(self):
        numpy.save(os.path.join('data', str(self.jointName) + 'MotorValues.npy'), self.motorValues)
        
