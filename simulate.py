import pybullet as p
import time
physicsClient = p.connect(p.GUI)

for i in range(1001):
    p.stepSimulation()
    time.sleep(1.0/60.0)
    
p.disconnect()

