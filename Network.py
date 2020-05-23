import numpy as np
import random
import copy

def m_sum(m):
    val=0
    for i in range(0, len(m)):
        val+=m[i]
    return val

def m_add(m1, m2):
    if len(m1)==len(m2):
        tempArray=[]
        for i in range(0, len(m1)):
            tempArray.append(m1[i]+m2[i])
        return tempArray

def m_sub(m1, m2):
    if len(m1)==len(m2):
        tempArray=[]
        for i in range(0, len(m1)):
            tempArray.append(m1[i]-m2[i])
        return tempArray

def m_pow(m1, power):
    tempArray=[]
    for i in range(0, len(m1)):
        tempArray.append(pow(m1[i],power))
    return tempArray

def sigmoid(z):
    return 1/(1+np.exp(-z))

def inverseSigmoid(z):
    return -1*np.log(z/(1-z))

class NeuralNetwork():
    def __init__(self, layers):
        self.layers = layers
        self.wb=[[[2.748184120932902, 19.374810094464504, 24.262936077055294, 4.632522941660126, -37.292407760504894]]]
        """for i in range(0, len(self.layers)-1):
            self.wb.append([])
            for j in range(0, self.layers[i+1]):
                self.wb[i].append([])
                for k in range(0, self.layers[i]+1):
                    self.wb[i][j].append(0.000001)"""
        self.best=self.wb

    def calc(self, val):
        for i in range(0, len(val)):
            val[i]=sigmoid(val[i])
        answer=self.func(val)
        for i in range(0, len(answer)):
            answer[i]=inverseSigmoid(answer[i])
        return answer

    def func(self, val):
        neurons=[]
        for i in range(0, len(self.layers)):
            neurons.append([])
            for j in range(0, self.layers[i]):
                neurons[i].append(0)

        neurons[0]=val
        for i in range(0, len(self.layers)-1):
            for j in range(0, self.layers[i+1]):
                tempVar=0
                for k in range(0, self.layers[i]):
                    tempVar+=self.wb[i][j][k]*neurons[i][k]
                tempVar+=self.wb[i][j][len(self.wb)-1]
                neurons[i+1][j]=tempVar
        return neurons[len(neurons)-1]

    def cost(self, val):
        return m_sum(m_pow(m_sub(self.func(val[0]), val[1]), 2))

    def bestVals(self):
        self.best=copy.deepcopy(self.wb)

    def nudge(self, alpha):
        for i in range(0, len(self.wb)):
            for j in range(0, len(self.wb[i])):
                for k in range(0, len(self.wb[i][j])):
                    self.wb[i][j][k]=self.best[i][j][k]+(random.random()-0.5)*alpha