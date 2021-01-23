import numpy as np 



class weather:
    Pmatrix = np.array([[0.7,0.5,0.2],[0.2,0.3,0.5],[0.1,0.2,0.3]],np.float32)
    today = np.array([[0],[0],[0]],np.float32)
    def predict(self,state,days):
        self.resetPMatrix()
        self.resetState()
        self.today[state] = 1
        for i in range(days-1):
            self.Pmatrix = np.matmul(self.Pmatrix,self.Pmatrix)
        prediction = np.matmul(self.Pmatrix,self.today)
        return prediction
    
    def resetState(self):
        self.today = np.array([[0],[0],[0]],np.float32)
    
    def resetPMatrix(self):
        Pmatrix = np.array([[0.7,0.5,0.2],[0.2,0.3,0.5],[0.1,0.2,0.3]],np.float32)
