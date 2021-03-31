import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time

class SOLUTION:

    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = numpy.array([[numpy.random.rand(), numpy.random.rand()],
                                    [numpy.random.rand(), numpy.random.rand()],
                                    [numpy.random.rand(), numpy.random.rand()]])
        self.weights = self.weights * 2 - 1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain(self.myID)
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID))        

    def Wait_For_Simulation_To_End(self):
        iteration = 0
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(1)
            print("while loop")
            iteration = iteration + 1
            if(iteration > 10):
                break
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.readline())
        ##print("read: fitness" + str(self.myID) + ".txt")
        f.close()
        ##print("deleting: fitness" + str(self.myID) + ".txt")
        os.system("del fitness" + str(self.myID) + ".txt")
        
    def Mutate(self):
        self.weights[random.randint(0,2)][random.randint(0,1)] = random.random()*2-1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-2,2,0.5] , size=[1,1,1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")  
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" ,type = "revolute", position = "2.0, 0, 1.0")
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" ,type = "revolute", position = "1.0, 0, 1.0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[1,1,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[1,1,1])
        pyrosim.End()

    def Create_Brain(self, ID):
        pyrosim.Start_NeuralNetwork("brain" + str(ID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name= 0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name= 1, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name= 2, linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron(name= 3, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name= 4, jointName = "Torso_FrontLeg")
        for currentColumn in range(0,3):
            for currentRow in range (0,2):
                pyrosim.Send_Synapse(sourceNeuronName = currentColumn, targetNeuronName = currentRow+3, weight = self.weights[currentColumn][currentRow])
        pyrosim.End()
