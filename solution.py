import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:

    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = self.weights * 2 - 1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGUI):
        self.Create_World(self.myID)
        self.Create_Body(self.myID)
        self.Create_Brain(self.myID)
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.5)

        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.readline())
        f.close()
        os.system("del fitness" + str(self.myID) + ".txt")
        os.system("del world" + str(self.myID) + ".sdf")
        
    def Mutate(self):
        self.weights[random.randrange(c.numSensorNeurons)][random.randrange(c.numMotorNeurons)] = random.random()*2-1

    def Create_World(self, ID):
        pyrosim.Start_SDF("world" + str(ID) + ".sdf")
        pyrosim.Send_Cube(name="Box", pos=[-2,2,0.5] , size=[1,1,1])
        pyrosim.End()

    def Create_Body(self, ID):
        pyrosim.Start_URDF("body" + str(ID) + ".urdf")  
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" ,type = "revolute", position = "0.0, 0.5, 1.0", jointAxis = "1 0 0")
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" ,type = "revolute", position = "0.0, -0.5, 1.0", jointAxis = "1 0 0")
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" ,type = "revolute", position = "-0.5, 0.0, 1.0", jointAxis = "0 1 0")
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" ,type = "revolute", position = "0.5, 0.0, 1.0", jointAxis = "0 1 0")
        pyrosim.Send_Joint( name = "FrontLeg_LowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" ,type = "revolute", position = "0.0, 1.0, 0.0", jointAxis = "1 0 0")
        pyrosim.Send_Joint( name = "BackLeg_LowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" ,type = "revolute", position = "0.0, -1.0, 0.0", jointAxis = "1 0 0")
        pyrosim.Send_Joint( name = "LeftLeg_LowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" ,type = "revolute", position = "-1.0, 0.0, 0.0", jointAxis = "0 1 0")
        pyrosim.Send_Joint( name = "RightLeg_LowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" ,type = "revolute", position = "1.0, 0.0, 0.0", jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.0,0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Cube(name="BackLeg", pos=[0.0,-0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0.0,0] , size=[1,0.2,0.2])
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0.0,0] , size=[1,0.2,0.2])
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1])
        pyrosim.End()

    def Create_Brain(self, ID):
        pyrosim.Start_NeuralNetwork("brain" + str(ID) + ".nndf")
##        pyrosim.Send_Sensor_Neuron(name= 0, linkName = "Torso")
##        pyrosim.Send_Sensor_Neuron(name= 1, linkName = "BackLeg")
##        pyrosim.Send_Sensor_Neuron(name= 2, linkName = "FrontLeg")
##        pyrosim.Send_Sensor_Neuron(name= 3, linkName = "LeftLeg")
##        pyrosim.Send_Sensor_Neuron(name= 4, linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name= 0, linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name= 1, linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name= 2, linkName = "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name= 3, linkName = "RightLowerLeg")
        pyrosim.Send_Motor_Neuron(name= 4, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name= 5, jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name= 6, jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name= 7, jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name= 8, jointName = "FrontLeg_LowerLeg")
        pyrosim.Send_Motor_Neuron(name= 9, jointName = "BackLeg_LowerLeg")
        pyrosim.Send_Motor_Neuron(name= 10, jointName = "LeftLeg_LowerLeg")
        pyrosim.Send_Motor_Neuron(name= 11, jointName = "RightLeg_LowerLeg")
        for currentColumn in range(0,c.numSensorNeurons):
            for currentRow in range (0,c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentColumn, targetNeuronName = currentRow+4, weight = self.weights[currentColumn][currentRow])
        pyrosim.End()
