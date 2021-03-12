from world import WORLD
from robot import ROBOT
from motor import MOTOR
from sensor import SENSOR
import constants as c
import pybullet as p
import time

class SIMULATION:

    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for t in range(c.timeSteps):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            time.sleep(c.sleepTime)
    
    def __del__(self):
        ##SENSOR.Save_Values(self)
        ##MOTOR.Save_Values(self)
        p.disconnect()

