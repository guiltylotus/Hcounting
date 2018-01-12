import numpy as np 

class Sample():

    def takeSample(self,frame, rate):
        h,w = np.shape(frame)

        for i in range(h):
            for j in range(w):
                if (frame[i,j] != 0):
                    r = np.random.randint(100)
                    # print(r)
                    if (r >= rate):
                        frame[i,j] = 0
                
        return frame