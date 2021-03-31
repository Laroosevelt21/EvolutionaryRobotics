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
        if(self.directOrGUI == "DIRECT"):
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)        
        self.world = WORLD()
        self.robot = ROBOT(self.solutionID)

    def Run(self):
        for t in range(c.timeSteps):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            if(self.directOrGUI == "GUI"):
                time.sleep(c.sleepTime)

    def Get_Fitness(self, solutionID):
        self.robot.Get_Fitness(solutionID)
    
    def __del__(self):
        ##SENSOR.Save_Values(self)
        ##MOTOR.Save_Values(self)
        p.disconnect()

