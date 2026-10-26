import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    lolz=np.asarray(x);
    return np.maximum(lolz,0);
    pass