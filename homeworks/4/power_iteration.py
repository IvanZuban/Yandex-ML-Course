import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps
    
    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    x = np.random.rand(data.shape[0])
    x = x / np.linalg.norm(x)

    for i in range(num_steps):
        x = np.dot(data) / np.linalg.norm(data, x) 
    
    eigenvalue = np.dot(x.T, np.dot(data, x))

    return eigenvalue.item(), x