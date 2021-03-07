import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
import os.path

class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.timeSteps)

    def Get_Value(self, timeStep):
        self.values[timeStep] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        numpy.save(os.path.join('data', str(self.linkName) + 'SensorValues.npy'), self.values)
        
        
        
