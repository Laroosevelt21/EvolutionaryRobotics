from world import WORLD
from robot import ROBOT
from motor import MOTOR
from sensor import SENSOR
import constants as c
import pybullet as p
import time

class SIMULATION:

    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        self.solutionID = solutionID
        self.robots = {}
        if(self.directOrGUI == "DIRECT"):
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)        
        self.world = WORLD(self.solutionID)
        for robot in range (int(self.solutionID)*10, int(self.solutionID)*10+10):
            self.robots[robot]= ROBOT(robot)

    def Run(self):
        for t in range(c.timeSteps):
            p.stepSimulation()
            for robot in range (int(self.solutionID)*10, int(self.solutionID)*10+10):
                self.robots[robot].Sense(t)
                self.robots[robot].Think()
                self.robots[robot].Act(t)
            if(self.directOrGUI == "GUI"):
                time.sleep(c.sleepTime)

    def Get_Fitness(self):
        for robot in range (int(self.solutionID)*10, int(self.solutionID)*10+10):
            self.robots[robot].Get_Fitness(robot)
    
    def __del__(self):
        ##SENSOR.Save_Values(self)
        ##MOTOR.Save_Values(self)
        p.disconnect()
