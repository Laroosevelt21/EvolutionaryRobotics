import numpy
import os
import matplotlib.pyplot

##backLegSensorValues = numpy.load(os.path.join('data', 'backLegSensorValues.npy'))
##print(backLegSensorValues)
##frontLegSensorValues = numpy.load(os.path.join('data', 'frontLegSensorValues.npy'))

backLegTargetAngles = numpy.load(os.path.join('data', 'backLegTargetAngles.npy'))
frontLegTargetAngles = numpy.load(os.path.join('data', 'frontLegTargetAngles.npy'))

##matplotlib.pyplot.plot(backLegSensorValues,linewidth=3)
##matplotlib.pyplot.plot(frontLegSensorValues)
##matplotlib.pyplot.legend()
##matplotlib.pyplot.show()

matplotlib.pyplot.plot(backLegTargetAngles, linewidth=5, label = 'Back Leg Motor Values')
matplotlib.pyplot.plot(frontLegTargetAngles, linewidth=2, label = 'Front Leg Motor Values')
matplotlib.pyplot.legend(loc = 'upper left')
matplotlib.pyplot.show()
