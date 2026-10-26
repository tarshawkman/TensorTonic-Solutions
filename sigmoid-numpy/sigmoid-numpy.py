import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    lolz=np.asarray(x);
    return 1/(1+np.power(np.e,-1*lolz));
    pass