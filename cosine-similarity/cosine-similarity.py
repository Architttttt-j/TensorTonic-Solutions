import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    
    a = np.array(a)
    b = np.array(b)

    magA = np.linalg.norm(a)
    magB = np.linalg.norm(b)

    if(magA == 0 or magB == 0):
        return float(0)

    result = np.dot(a,b) / ((magA) * (magB))
    return float(result)