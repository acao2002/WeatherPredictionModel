import numpy as np 

Pmatrix = np.array([[0.7,0.5,0.2],[0.2,0.3,0.5],[0.1,0.2,0.3]],np.float32)
today = np.array([[0],[1],[0]],np.float32)
prediction = np.matmul(Pmatrix,today)
print(prediction)