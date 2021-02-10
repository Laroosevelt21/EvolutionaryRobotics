import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5
##x2 = 1
##y2 = 0
##z2 = 1.5
##pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
##pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2] , size=[length,width,height])

##sumheight = z
for j in range(6):
    for k in range(6):
        for i in range(0,10):
            ##    if i == 0:
            ##        pyrosim.Send_Cube(name="Box"+str(i), pos=[x,y,z] , size=[length*(0.9**i),width*(0.9**i),height*(0.9**i)])
            ##    else:
            ##        sumheight = sumheight + 0.9**i
            pyrosim.Send_Cube(name="Box"+str(i), pos=[x+k,y+j,z+i] , size=[length*(0.9**i),width*(0.9**i),height*(0.9**i)])

pyrosim.End()
