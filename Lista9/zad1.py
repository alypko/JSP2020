import numpy as np 

A = np.array([[1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8],[2,6,7,-5,1],[1,2,6,-4,-10]])
B = np.array([6,2,-5,17,12])
Variables = np.linalg.inv(A).dot(B)
print("x=",Variables[0]," y=",Variables[1]," z=",Variables[2], " t=",Variables[3]," u=",Variables[4])
