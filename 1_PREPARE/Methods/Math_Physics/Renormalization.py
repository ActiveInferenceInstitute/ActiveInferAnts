import numpy as np
from scipy.linalg import svd

def create_initial_tensor(beta):
    """Create the initial tensor for the 2D Ising model using a more efficient approach."""
    cosh_beta = np.cosh(beta)
    sinh_beta = np.sinh(beta)
    T = np.array([[[[cosh_beta if i == j == k == l else sinh_beta
                     for l in range(2)] for k in range(2)]
                   for j in range(2)] for i in range(2)])
    T *= np.outer(np.outer([cosh_beta, sinh_beta], [cosh_beta, sinh_beta]),
                  np.outer([cosh_beta, sinh_beta], [cosh_beta, sinh_beta])).reshape((2, 2, 2, 2))
    return T

def svd_decompose(tensor):
    """Perform SVD on the tensor and split it into two smaller tensors using a more compact form."""
    reshaped_tensor = tensor.reshape((np.prod(tensor.shape[:2]), np.prod(tensor.shape[2:])))
    U, S, Vh = svd(reshaped_tensor, full_matrices=False)
    S = np.sqrt(S)
    U = U @ np.diag(S)
    Vh = np.diag(S) @ Vh
    
    # Calculate the new dimensions for reshaping
    split_dim_U = U.shape[1]
    split_dim_Vh = Vh.shape[0]
    
    U = U.reshape(tensor.shape[0], tensor.shape[1], split_dim_U)
    Vh = Vh.reshape(split_dim_Vh, tensor.shape[2], tensor.shape[3])
    
    return U, Vh

def contract_tensors(tensor1, tensor2):
    """Contract two tensors along their common dimension using a more generalized approach."""
    return np.tensordot(tensor1, tensor2, axes=([len(tensor1.shape)-1], [0]))

def trg_step(tensor):
    """Perform one step of the TRG algorithm with improved readability and efficiency."""
    U1, V1 = svd_decompose(tensor)
    U2, V2 = svd_decompose(np.transpose(tensor, (1, 2, 3, 0)))
    
    # Ensure the dimensions match for tensor contraction
    U1 = U1.reshape(U1.shape[0], U1.shape[1], -1)
    V1 = V1.reshape(-1, V1.shape[1], V1.shape[2])
    U2 = U2.reshape(U2.shape[0], U2.shape[1], -1)
    V2 = V2.reshape(-1, V2.shape[1], V2.shape[2])
    
    new_tensor = contract_tensors(U1, U2)
    new_tensor = contract_tensors(new_tensor, V1)
    new_tensor = contract_tensors(new_tensor, V2)
    return new_tensor

def compute_partition_function(tensor, steps):
    """Compute the partition function by iterating the TRG steps with enhanced clarity."""
    for step in range(steps):
        tensor = trg_step(tensor)
    return np.sum(tensor)

# Numerical Example
beta = 0.5  # Inverse temperature
steps = 3   # Number of TRG steps for a simple example

# Create the initial tensor
initial_tensor = create_initial_tensor(beta)
print(f"Initial tensor:\n{initial_tensor}")

# Perform TRG steps and compute the partition function
Z = compute_partition_function(initial_tensor, steps)
print(f"Partition function after {steps} TRG steps: {Z}")
