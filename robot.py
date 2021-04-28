from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c

class ROBOT:

    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robot = p.loadURDF("body" + str(self.solutionID) + ".urdf")
        pyrosim.Prepare_To_Simulate("body" + str(self.solutionID) + ".urdf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain" + str(self.solutionID) + ".nndf")
        os.system("del brain" + str(self.solutionID) + ".nndf")
        os.system("del body" + str(self.solutionID) + ".urdf")
        

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, timeStep):
        for i in self.sensors:
            self.sensors[i].Get_Value(timeStep)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            
    def Act(self, timeStep):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = (c.motorJointRange*self.nn.Get_Value_Of(neuronName))
                self.motors[jointName].Set_Value(self.robot, desiredAngle)

    def Think(self):
        self.nn.Update()

    def Get_Fitness(self, fitnessID):
        self.fitnessID = fitnessID
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        f = open("tmp" + str(self.fitnessID) + ".txt", "w")
        f.write(str(xPosition))
        f.close()
        os.system("rename" + " " + "tmp" + str(self.fitnessID) + ".txt" + " " + "fitness" + str(self.fitnessID) + ".txt")
