import numpy as np 

Pmatrix = np.array([[0.7,0.5,0.2],[0.2,0.3,0.5],[0.1,0.2,0.3]],np.float32)
today = np.array([[0],[0],[0]],np.float32)

class weather:
    def predict(self,state,days):
        today[state] = 1
        for i in range(days-1):
            global Pmatrix
            Pmatrix = np.matmul(Pmatrix,Pmatrix)
        prediction = np.matmul(Pmatrix,today)
        return prediction
