from Chromosome import Chromosome
import random

class Population():
    def __init__(self, dim):
        self.__dimension = dim
        self.__population = []


    def initPop(self, initState):
        for i in range(0, self.__dimension):
            self.__population.append(Chromosome(initState))
            self.__population[i].initRepr()

    def fitPop(self):
        for i in range(0, self.__dimension):
            self.__population[i].evalChromosome()


    def getBest(self):
        posBest = 0
        for i in range(1, self.__dimension):
            if self.__population[posBest].getFitness() > self.__population[i].getFitness():
                posBest = i
        
        return self.__population[posBest].getFitness()


    def getDim(self):
        return self.__dimension


    def setPop(self, pop):
        for i in range(0, self.__dimension):
            self.__population[i] = pop[i]

            '''
    def selection(self):
        max     = sum([c.getFitness() for c in self.__population])
        pick    = random.uniform(0, max)
        current = 0
        for chromosome in self.__population:
            current += chromosome.getFitness()
            if current > pick:
                return chromosome
    '''
    def selection(self):
        pos = []

        n = random.randint(5,10)

        for i in range(n):
            pos.append( random.randint(0, self.__dimension-1))

        bestPos = pos[0]
        for i in range(1,n):
            if(self.__population[bestPos].getFitness() > self.__population[pos[i]].getFitness()):
                bestPos = pos[i]
        return self.__population[bestPos]
    

    def xo(M, F):
        xo = M

        for i in range(0,81):
            if random.uniform(0,1) >= 0.5:
                xo.setReprPos(i,F.getReprPos(i))
        return xo


    def mutation(c):
        n = random.randint(2,5)
        for i in range(n):
            p = random.randint(0,80)
            c.setReprPos(p, random.randint(0,9))

        return c
