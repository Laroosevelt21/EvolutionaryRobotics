from solution import SOLUTION
import constants as c
import copy
import os
import numpy

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del body*.urdf")
        os.system("del world*.sdf")
        os.system("del box*.sdf")
        self.parents = {}
        self.nextAvailableID = 0
        for parent in range(c.populationSize):
            self.parents[parent]=SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID+1

    def Evolve(self):
        ## Passing in all parents in the parent-
        ## dictionary to the "Evaluate" method
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
            self.nextAvailableID = self.nextAvailableID+1

    def Mutate(self):
        for j in self.children.keys():
            self.children[j].Mutate()

    def Evaluate(self, solutions):
        for parent in range(c.populationSize):
            ## solutions = parents (dictionary) which is a Solution object = an array of weights
            ## Create_Simulation call will produce populationSize amounts of: Bodies, Brains, and Worlds
            solutions[parent].Start_Simulation("DIRECT")
        for parent in range(c.populationSize):
            solutions[parent].Wait_For_Simulation_To_End()

    def Select(self):
        for k in self.parents.keys():
            ##print(self.parents[k].fitness)
            if(numpy.mean(self.parents[k].fitness) > numpy.mean(self.children[k].fitness)):
                ##print("Child Swarm Selected")
                self.parents = self.children

    def Print(self):
        for keys in self.parents.keys():
            for member in range(10):
                print("Parent Swarm " + str(keys) + " Member " + str(member) + " Fitness: " + str(self.parents[keys].fitness[member]) + " " + "Child Swarm " + str(keys) + " Member " + str(member) + " Fitness: " + str(self.children[keys].fitness[member]))

    def Show_Best(self):
        bestParent = self.parents[0]
        for p in range(0, len(self.parents.keys())):
            if(numpy.mean(bestParent.fitness) > numpy.mean(self.parents[p].fitness)):
                bestParent = self.parents[p]
        ##print("Best Fitness: " + str(bestParent.fitness[9]))
        bestParent.Start_Simulation("GUI")
        
