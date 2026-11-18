import numpy as np

def dot_product(x, y):
    x = np.asarray(x,dtype=float)
    y = np.asarray(y,dtype=float)
    result = np.dot(x,y)
    return float(result)
