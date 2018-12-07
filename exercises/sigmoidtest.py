from numpy import *
import math



inputVec1 = array([0,1])
inputVec2 = array([1,1])


for i in range(1,11):
    weight = array([-2*i,-2*i])
    biases = 3*i
    output = sum(inputVec1*weight) +biases
    output = 1.0/(1+math.exp(-output*1.0))
    print(output)
    
for i in range(1,11):
    weight = array([-2*i,-2*i])
    biases = -3*i
    output = sum(inputVec2*weight) +biases
    output = 1.0/(1+math.exp(-output*1.0))
    print(output)
