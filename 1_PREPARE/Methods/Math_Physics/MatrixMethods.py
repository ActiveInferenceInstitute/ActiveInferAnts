import numpy as np
from scipy import linalg
from scipy.sparse import csr_matrix, random as sparse_random
from scipy.sparse.linalg import eigsh, svds
from sklearn.utils.extmath import randomized_svd
import warnings
from typing import Union, Tuple, List, Optional
from numpy.typing import ArrayLike

def spectral_norm(matrix: ArrayLike) -> float:
    """
    Compute the spectral norm (largest singular value) of a matrix.
    
    Args:
    matrix (ArrayLike): Input matrix
    
    Returns:
    float: The spectral norm of the matrix.
    
    Raises:
    ValueError: If the input is not a 2D array.
    """
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError("Input must be a 2D numpy array.")
    return np.linalg.norm(matrix, ord=2)

def condition_number(matrix: ArrayLike, p: Optional[Union[int, str]] = None) -> float:
    """
    Compute the condition number of a matrix.
    
    The condition number is the ratio of the largest to smallest singular value.
    A large condition number indicates that the matrix is ill-conditioned.
    
    Args:
    matrix (ArrayLike): Input matrix
    p (Optional[Union[int, str]]): Order of the norm. Can be 1, 2, inf, or 'fro'. Default is 2.
    
    Returns:
    float: The condition number of the matrix.
    
    Raises:
    ValueError: If the input is not a 2D array or if p is not a valid norm order.
    """
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError("Input must be a 2D numpy array.")
    
    valid_p_values = [None, 1, 2, np.inf, 'fro']
    if p not in valid_p_values:
        raise ValueError(f"Invalid norm order. Must be one of {valid_p_values}")
    
    return np.linalg.cond(matrix, p=p)

def matrix_rank(matrix: ArrayLike, tol: Optional[float] = None, hermitian: bool = False) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
    matrix (ArrayLike): Input matrix
    tol (Optional[float]): Tolerance for considering singular values as zero. If None, machine precision is used.
    hermitian (bool): If True, matrix is assumed to be Hermitian (symmetric if real-valued).
    
    Returns:
    int: The rank of the matrix.
    
    Raises:
    ValueError: If the input is not a 2D array.
    """
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError("Input must be a 2D numpy array.")
    
    return np.linalg.matrix_rank(matrix, tol=tol, hermitian=hermitian)

def pseudoinverse(matrix: ArrayLike, rcond: Optional[float] = None, hermitian: bool = False) -> np.ndarray:
    """
    Compute the Moore-Penrose pseudoinverse of a matrix.
    
    Args:
    matrix (ArrayLike): Input matrix
    rcond (Optional[float]): Cutoff for small singular values. Default is 1e-15.
    hermitian (bool): If True, matrix is assumed to be Hermitian (symmetric if real-valued).
    
    Returns:
    np.ndarray: The pseudoinverse of the matrix.
    
    Raises:
    ValueError: If the input is not a 2D array.
    """
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError("Input must be a 2D numpy array.")
    
    return np.linalg.pinv(matrix, rcond=rcond, hermitian=hermitian)

def random_orthogonal_matrix(n: int, random_state: Optional[Union[int, np.random.RandomState]] = None) -> np.ndarray:
    """
    Generate a random orthogonal matrix using QR decomposition.
    
    Args:
    n (int): Size of the square matrix
    random_state (Optional[Union[int, np.random.RandomState]]): Seed for random number generator
    
    Returns:
    np.ndarray: A random orthogonal matrix of size n x n.
    
    Raises:
    ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")
    
    rng = np.random.default_rng(random_state)
    Q, _ = np.linalg.qr(rng.standard_normal((n, n)))
    return Q

def random_positive_definite_matrix(n: int, eigenvalue_range: Tuple[float, float] = (1, 10), random_state: Optional[Union[int, np.random.RandomState]] = None) -> np.ndarray:
    """
    Generate a random positive definite matrix.
    
    Args:
    n (int): Size of the square matrix
    eigenvalue_range (Tuple[float, float]): Tuple specifying the range for eigenvalues
    random_state (Optional[Union[int, np.random.RandomState]]): Seed for random number generator
    
    Returns:
    np.ndarray: A random positive definite matrix of size n x n.
    
    Raises:
    ValueError: If n is not a positive integer or if eigenvalue_range is invalid.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")
    
    if not isinstance(eigenvalue_range, tuple) or len(eigenvalue_range) != 2 or eigenvalue_range[0] >= eigenvalue_range[1]:
        raise ValueError("eigenvalue_range must be a tuple of two floats with the first value less than the second.")
    
    rng = np.random.default_rng(random_state)
    eigvals = rng.uniform(*eigenvalue_range, size=n)
    Q = random_orthogonal_matrix(n, random_state=rng)
    return Q @ np.diag(eigvals) @ Q.T

def sparse_random_matrix(m: int, n: int, density: float = 0.1, format: str = 'csr', dtype: Optional[np.dtype] = None, random_state: Optional[Union[int, np.random.RandomState]] = None) -> csr_matrix:
    """
    Generate a sparse random matrix.
    
    Args:
    m (int): Number of rows
    n (int): Number of columns
    density (float): Density of non-zero elements (default: 0.1)
    format (str): Sparse matrix format (default: 'csr')
    dtype (Optional[np.dtype]): Data type of the matrix elements
    random_state (Optional[Union[int, np.random.RandomState]]): Seed for random number generator
    
    Returns:
    csr_matrix: A sparse random matrix.
    
    Raises:
    ValueError: If m or n are not positive integers, or if density is not in (0, 1].
    """
    if not isinstance(m, int) or m <= 0 or not isinstance(n, int) or n <= 0:
        raise ValueError("m and n must be positive integers.")
    
    if not 0 < density <= 1:
        raise ValueError("density must be in the range (0, 1].")
    
    return sparse_random(m, n, density=density, format=format, dtype=dtype, random_state=random_state)

def truncated_svd(matrix: ArrayLike, k: int, n_iter: int = 5, random_state: Optional[Union[int, np.random.RandomState]] = None) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Compute truncated SVD using randomized algorithm.
    
    Args:
    matrix (ArrayLike): Input matrix
    k (int): Number of singular values and vectors to compute
    n_iter (int): Number of power iterations (default: 5)
    random_state (Optional[Union[int, np.random.RandomState]]): Random state for reproducibility
    
    Returns:
    Tuple[np.ndarray, np.ndarray, np.ndarray]: Left singular vectors, singular values, and right singular vectors
    
    Raises:
    ValueError: If k is not a positive integer or if n_iter is negative.
    """
    if not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer.")
    
    if not isinstance(n_iter, int) or n_iter < 0:
        raise ValueError("n_iter must be a non-negative integer.")
    
    U, S, Vt = randomized_svd(matrix, n_components=k, n_iter=n_iter, random_state=random_state)
    return U, S, Vt

def sparse_eigsh(matrix: csr_matrix, k: int, which: str = 'LM', sigma: Optional[float] = None, maxiter: Optional[int] = None, tol: float = 0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute k largest (or smallest) eigenvalues and eigenvectors of a sparse symmetric matrix.
    
    Args:
    matrix (csr_matrix): Input sparse symmetric matrix
    k (int): Number of eigenvalues/vectors to compute
    which (str): Which eigenvalues to find ('LM', 'SM', 'LA', 'SA', or 'BE')
    sigma (Optional[float]): Shift-invert mode for near shifts
    maxiter (Optional[int]): Maximum number of Arnoldi update iterations
    tol (float): Relative accuracy for eigenvalues
    
    Returns:
    Tuple[np.ndarray, np.ndarray]: eigenvalues, eigenvectors
    
    Raises:
    ValueError: If k is not a positive integer or if which is not a valid option.
    """
    if not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer.")
    
    valid_which = ['LM', 'SM', 'LA', 'SA', 'BE']
    if which not in valid_which:
        raise ValueError(f"which must be one of {valid_which}")
    
    return eigsh(matrix, k=k, which=which, sigma=sigma, maxiter=maxiter, tol=tol)

def sparse_svds(matrix: csr_matrix, k: int, ncv: Optional[int] = None, tol: float = 0, which: str = 'LM', v0: Optional[np.ndarray] = None, maxiter: Optional[int] = None, return_singular_vectors: bool = True) -> Union[Tuple[np.ndarray, np.ndarray, np.ndarray], np.ndarray]:
    """
    Compute k largest singular values and vectors of a sparse matrix.
    
    Args:
    matrix (csr_matrix): Input sparse matrix
    k (int): Number of singular values/vectors to compute
    ncv (Optional[int]): Number of Lanczos vectors generated
    tol (float): Tolerance for singular values
    which (str): Which singular values to find ('LM' or 'SM')
    v0 (Optional[np.ndarray]): Starting vector for iteration
    maxiter (Optional[int]): Maximum number of iterations
    return_singular_vectors (bool): Whether to return singular vectors
    
    Returns:
    Union[Tuple[np.ndarray, np.ndarray, np.ndarray], np.ndarray]: 
        If return_singular_vectors is True: (U, s, Vt) - Left singular vectors, singular values, and right singular vectors
        If return_singular_vectors is False: s - Singular values
    
    Raises:
    ValueError: If k is not a positive integer or if which is not a valid option.
    """
    if not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer.")
    
    valid_which = ['LM', 'SM']
    if which not in valid_which:
        raise ValueError(f"which must be one of {valid_which}")
    
    return svds(matrix, k=k, ncv=ncv, tol=tol, which=which, v0=v0, maxiter=maxiter, return_singular_vectors=return_singular_vectors)

def toeplitz_matrix(c: ArrayLike, r: Optional[ArrayLike] = None) -> np.ndarray:
    """
    Generate a Toeplitz matrix.
    
    Args:
    c (ArrayLike): First column of the matrix
    r (Optional[ArrayLike]): First row of the matrix (if different from c)
    
    Returns:
    np.ndarray: A Toeplitz matrix.
    
    Raises:
    ValueError: If c and r have incompatible shapes.
    """
    return linalg.toeplitz(c, r)

def circulant_matrix(c: ArrayLike) -> np.ndarray:
    """
    Generate a circulant matrix.
    
    Args:
    c (ArrayLike): First column of the circulant matrix
    
    Returns:
    np.ndarray: A circulant matrix.
    """
    return linalg.circulant(c)

def hadamard_matrix(n: int) -> np.ndarray:
    """
    Generate a Hadamard matrix of order n.
    
    Args:
    n (int): Order of the Hadamard matrix (must be a power of 2)
    
    Returns:
    np.ndarray: A Hadamard matrix of order n.
    
    Raises:
    ValueError: If n is not a power of 2.
    """
    if n & (n - 1) != 0:
        raise ValueError("n must be a power of 2")
    return linalg.hadamard(n)

def is_positive_definite(matrix: ArrayLike, tol: float = 1e-8) -> bool:
    """
    Check if a matrix is positive definite.
    
    Args:
    matrix (ArrayLike): Input symmetric matrix
    tol (float): Tolerance for eigenvalue positivity check
    
    Returns:
    bool: True if the matrix is positive definite, False otherwise.
    
    Raises:
    ValueError: If the input is not a 2D square array.
    """
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input must be a 2D square numpy array.")
    
    return np.all(np.linalg.eigvalsh(matrix) > tol)

def nearest_positive_definite(matrix: ArrayLike, epsilon: float = 0) -> np.ndarray:
    """
    Find the nearest positive definite matrix to the input matrix.
    
    Args:
    matrix (ArrayLike): Input matrix
    epsilon (float): Small number added to the diagonal for numerical stability
    
    Returns:
    np.ndarray: The nearest positive definite matrix.
    
    Raises:
    ValueError: If the input is not a 2D square array.
    """
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input must be a 2D square numpy array.")
    
    B = (matrix + matrix.T) / 2
    _, s, V = np.linalg.svd(B)
    H = V.T @ np.diag(np.maximum(s, epsilon)) @ V
    A2 = (B + H) / 2
    A3 = (A2 + A2.T) / 2
    if is_positive_definite(A3):
        return A3
    
    spacing = np.spacing(np.linalg.norm(matrix))
    I = np.eye(matrix.shape[0])
    k = 1
    while not is_positive_definite(A3):
        mineig = np.min(np.real(np.linalg.eigvals(A3)))
        A3 += I * (-mineig * k**2 + spacing)
        k += 1
    return A3

def matrix_power(matrix, n):
    """
    Compute the nth power of a matrix.
    
    Args:
    matrix: Input square matrix
    n: Power to raise the matrix to (can be negative)
    
    Returns:
    The matrix raised to the nth power.
    """
    return np.linalg.matrix_power(matrix, n)

def kronecker_product(A, B):
    """
    Compute the Kronecker product of two matrices.
    
    Args:
    A, B: Input matrices
    
    Returns:
    The Kronecker product of A and B.
    """
    return np.kron(A, B)

def matrix_exponential(matrix):
    """
    Compute the matrix exponential.
    
    Args:
    matrix: Input square matrix
    
    Returns:
    The matrix exponential of the input matrix.
    """
    return linalg.expm(matrix)

def matrix_logarithm(matrix):
    """
    Compute the matrix logarithm.
    
    Args:
    matrix: Input square matrix
    
    Returns:
    The matrix logarithm of the input matrix.
    """
    return linalg.logm(matrix)

def is_unitary(matrix, rtol=1e-5, atol=1e-8):
    """
    Check if a matrix is unitary.
    
    Args:
    matrix: Input square matrix
    rtol, atol: Relative and absolute tolerance for the check
    
    Returns:
    True if the matrix is unitary, False otherwise.
    """
    n = matrix.shape[0]
    return np.allclose(np.eye(n), matrix @ matrix.conj().T, rtol=rtol, atol=atol)

def gram_schmidt(vectors):
    """
    Perform Gram-Schmidt orthogonalization on a set of vectors.
    
    Args:
    vectors: List of input vectors
    
    Returns:
    List of orthonormalized vectors.
    """
    orthonormalized = []
    for vector in vectors:
        temp_vec = vector
        for orthonormal in orthonormalized:
            temp_vec = temp_vec - np.dot(orthonormal, vector) * orthonormal
        if np.allclose(temp_vec, 0):
            warnings.warn("Linearly dependent vectors detected in Gram-Schmidt process.")
        else:
            temp_vec = temp_vec / np.linalg.norm(temp_vec)
            orthonormalized.append(temp_vec)
    return orthonormalized

def matrix_sign(matrix):
    """
    Compute the matrix sign function.
    
    Args:
    matrix: Input square matrix
    
    Returns:
    The matrix sign of the input matrix.
    """
    return linalg.signm(matrix)

def matrix_sqrt(matrix):
    """
    Compute the matrix square root.
    
    Args:
    matrix: Input square matrix
    
    Returns:
    The matrix square root of the input matrix.
    """
    return linalg.sqrtm(matrix)

def is_symmetric(matrix, rtol=1e-5, atol=1e-8):
    """
    Check if a matrix is symmetric.
    
    Args:
    matrix: Input square matrix
    rtol, atol: Relative and absolute tolerance for the check
    
    Returns:
    True if the matrix is symmetric, False otherwise.
    """
    return np.allclose(matrix, matrix.T, rtol=rtol, atol=atol)

def is_hermitian(matrix, rtol=1e-5, atol=1e-8):
    """
    Check if a matrix is Hermitian.
    
    Args:
    matrix: Input square matrix
    rtol, atol: Relative and absolute tolerance for the check
    
    Returns:
    True if the matrix is Hermitian, False otherwise.
    """
    return np.allclose(matrix, matrix.conj().T, rtol=rtol, atol=atol)

def matrix_trace(matrix):
    """
    Compute the trace of a matrix.
    
    Args:
    matrix: Input square matrix
    
    Returns:
    The trace of the matrix.
    """
    return np.trace(matrix)

def matrix_determinant(matrix):
    """
    Compute the determinant of a matrix.
    
    Args:
    matrix: Input square matrix
    
    Returns:
    The determinant of the matrix.
    """
    return np.linalg.det(matrix)

def matrix_inverse(matrix):
    """
    Compute the inverse of a matrix.
    
    Args:
    matrix: Input square matrix
    
    Returns:
    The inverse of the matrix.
    """
    return np.linalg.inv(matrix)

def matrix_nullspace(matrix, tol=1e-10):
    """
    Compute the nullspace of a matrix.
    
    Args:
    matrix: Input matrix
    tol: Tolerance for singular values
    
    Returns:
    A matrix whose columns form an orthonormal basis for the nullspace.
    """
    _, s, vh = np.linalg.svd(matrix)
    null_mask = (s <= tol)
    null_space = vh[null_mask]
    return null_space.T

def matrix_range(matrix, tol=1e-10):
    """
    Compute the range (column space) of a matrix.
    
    Args:
    matrix: Input matrix
    tol: Tolerance for singular values
    
    Returns:
    A matrix whose columns form an orthonormal basis for the range.
    """
    u, s, _ = np.linalg.svd(matrix, full_matrices=False)
    range_mask = (s > tol)
    return u[:, range_mask]

