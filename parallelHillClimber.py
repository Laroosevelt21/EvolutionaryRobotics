from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for parent in range(c.populationSize):
            self.parents[parent]=SOLUTION(self.nextAvailableID)
            ##print("nextAvailableID = " + str(self.nextAvailableID))
            self.nextAvailableID = self.nextAvailableID+1
            
            
        

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for i in self.parents.keys():
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            ##print("nextAvailableID = " + str(self.nextAvailableID))
            self.nextAvailableID = self.nextAvailableID+1


    def Mutate(self):
        for j in self.children.keys():
            self.children[j].Mutate()

    def Evaluate(self, solutions):
        for parent in range(c.populationSize):
            solutions[parent].Start_Simulation("DIRECT")
        for parent in range(c.populationSize):
            solutions[parent].Wait_For_Simulation_To_End()

    def Select(self):
        for k in self.parents.keys():
            if(self.parents[k].fitness > self.children[k].fitness):
                self.parents[k] = self.children[k]

    def Print(self):
        for keys in self.parents.keys():
            print("Parent " + str(keys) + " Fitness: " + str(self.parents[keys].fitness) + " " + "Child " + str(keys) + " Fitness: " + str(self.children[keys].fitness))

    def Show_Best(self):
        for p in range(0, len(self.parents.keys())-1):
            if(self.parents[p].fitness<self.parents[p+1].fitness):
                bestParent = self.parents[p]
            else:
                bestParent = self.parents[p+1]
        ##print(bestParent.fitness)
        bestParent.Start_Simulation("GUI")
        
