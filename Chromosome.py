import random
import numpy as np

class Chromosome():
    def __init__(self, initState):
        self.__initState = initState
        self.__repr = []
        self.__fitness = 0

    def initRepr(self):
        self.__repr = [random.randint(0,9) for _ in range(81)]

    def getFitness(self):
        return self.__fitness

    def getRepr(self):
        return self.__repr
    
    def getReprPos(self,pos):
        return self.__repr[pos]
    def setReprPos(self,pos,val):
        self.__repr[pos] = val


    def is_valid(self,line):
        return np.unique(line).shape == line.shape

    def evalChromosome(self):
       
        for i in range(81):
            if self.__initState[i] != 0:
                self.__repr[i] = self.__initState[i]

        matr = []
        for i in range(0,81,9):
            matr.append(self.__repr[i:i+9])
        
        matr = np.asarray(matr)

        numC, numL = 0, 0
        for i in range(0,9):
            if not self.is_valid(matr[i,:]):
                numL += 1
            if not self.is_valid(matr[:,i]):
                numC += 1

        numSubGrid = 0
        for i in range(0,9,3):
            for j in range(0,9,3):
                # extractsubmatrix
                subMatr = matr[i:i+3,j:j+3]
                if not self.is_valid(subMatr.reshape(-1)):
                    numSubGrid += 1

        # return error
        self.__fitness = (numL+numC+numSubGrid)

