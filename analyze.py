import numpy
import os
import matplotlib.pyplot

backLegSensorValues = numpy.load(os.path.join('data', 'backLegSensorValues.npy'))
##print(backLegSensorValues)
frontLegSensorValues = numpy.load(os.path.join('data', 'frontLegSensorValues.npy'))

matplotlib.pyplot.plot(backLegSensorValues,linewidth=3)
matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
