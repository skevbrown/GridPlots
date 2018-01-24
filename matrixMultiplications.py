
import numpy as np
import matplotlib.pyplot as plt

matrixA = np.zeros([4,4])
matrixA[0,:] = [-2,1,0,1];
matrixA[1,:] = [1,-2,1,0]
matrixA[2,:] = [0,1,-2,1]
matrixA[3,:] = [1,0,1,-2]

vec1= np.array([-2,1,0,1])

print( matrixA.dot(vec1) )