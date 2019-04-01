import random
import pandas as pd
import numpy as np
from Population import *

def readcsv(filename):
	data = np.loadtxt(filename, delimiter=',', skiprows=0, dtype = int)
	
	return(data)


def train():
	initState = readcsv("input.csv")

	p = Population(20)   
	p.initPop(initState)


	numGen = 100000

	bestFit = 28
	for i in range(0, numGen):

	    p.fitPop()

	    bFit = p.getBest()

	    if bFit < bestFit:
	    	bestFit = bFit

	    print("gen ", i," ", bFit)

	    popAux = []
        
	    for j in range(0, p.getDim()):
               
	        M = p.selection()
	        F = p.selection()
	        xo = Population.xo(M,F)

	        if(random.uniform(0,1) <= 0.1):
	            xo = Population.mutation(xo)
            
	        popAux.append(xo)
	    p.setPop(popAux)
        
	p.fitPop()
	
	bFit = p.getBest()

	if bFit < bestFit:
	   	bestFit = bFit

	print("impresionant fitness   :   ", bestFit, "!!!!Q")

train()


	