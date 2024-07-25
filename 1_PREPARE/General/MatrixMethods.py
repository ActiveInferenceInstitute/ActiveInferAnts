import numpy as np
from scipy import linalg
from scipy.sparse import csr_matrix, random as sparse_random
from scipy.sparse.linalg import eigsh, svds
from sklearn.utils.extmath import randomized_svd
import warnings

def spectral_norm(matrix):
    """
    Compute the spectral norm (largest singular value) of a matrix.
    
    Args:
    matrix: Input matrix
    
    Returns:
    The spectral norm of the matrix.
    """
    return np.linalg.norm(matrix, ord=2)

def condition_number(matrix):
    """
    Compute the condition number of a matrix.
    
    The condition number is the ratio of the largest to smallest singular value.
    A large condition number indicates that the matrix is ill-conditioned.
    
    Args:
    matrix: Input matrix
    
    Returns:
    The condition number of the matrix.
    """
    s = np.linalg.svd(matrix, compute_uv=False)
    return s[0] / s[-1]

def matrix_rank(matrix, tol=None):
    """
    Compute the rank of a matrix.
    
    Args:
    matrix: Input matrix
    tol: Tolerance for considering singular values as zero. If None, machine precision is used.
    
    Returns:
    The rank of the matrix.
    """
    return np.linalg.matrix_rank(matrix, tol=tol)

def pseudoinverse(matrix, rcond=None):
    """
    Compute the Moore-Penrose pseudoinverse of a matrix.
    
    Args:
    matrix: Input matrix
    rcond: Cutoff for small singular values. Default is 1e-15.
    
    Returns:
    The pseudoinverse of the matrix.
    """
    return np.linalg.pinv(matrix, rcond=rcond)

def random_orthogonal_matrix(n):
    """
    Generate a random orthogonal matrix using QR decomposition.
    
    Args:
    n: Size of the square matrix
    
    Returns:
    A random orthogonal matrix of size n x n.
    """
    Q, _ = np.linalg.qr(np.random.randn(n, n))
    return Q

def random_positive_definite_matrix(n, eigenvalue_range=(1, 10)):
    """
    Generate a random positive definite matrix.
    
    Args:
    n: Size of the square matrix
    eigenvalue_range: Tuple specifying the range for eigenvalues
    
    Returns:
    A random positive definite matrix of size n x n.
    """
    eigvals = np.random.uniform(*eigenvalue_range, size=n)
    Q = random_orthogonal_matrix(n)
    return Q @ np.diag(eigvals) @ Q.T

def sparse_random_matrix(m, n, density=0.1, format='csr', dtype=None, random_state=None):
    """
    Generate a sparse random matrix.
    
    Args:
    m, n: Dimensions of the matrix
    density: Density of non-zero elements (default: 0.1)
    format: Sparse matrix format (default: 'csr')
    dtype: Data type of the matrix elements
    random_state: Seed for random number generator
    
    Returns:
    A sparse random matrix.
    """
    return sparse_random(m, n, density=density, format=format, dtype=dtype, random_state=random_state)

def truncated_svd(matrix, k, n_iter=5, random_state=None):
    """
    Compute truncated SVD using randomized algorithm.
    
    Args:
    matrix: Input matrix
    k: Number of singular values and vectors to compute
    n_iter: Number of power iterations (default: 5)
    random_state: Random state for reproducibility
    
    Returns:
    U, S, Vt: Left singular vectors, singular values, and right singular vectors
    """
    U, S, Vt = randomized_svd(matrix, n_components=k, n_iter=n_iter, random_state=random_state)
    return U, S, Vt

def sparse_eigsh(matrix, k, which='LM', sigma=None, maxiter=None, tol=0):
    """
    Compute k largest (or smallest) eigenvalues and eigenvectors of a sparse symmetric matrix.
    
    Args:
    matrix: Input sparse symmetric matrix
    k: Number of eigenvalues/vectors to compute
    which: Which eigenvalues to find ('LM', 'SM', 'LA', 'SA', or 'BE')
    sigma: Shift-invert mode for near shifts
    maxiter: Maximum number of Arnoldi update iterations
    tol: Relative accuracy for eigenvalues
    
    Returns:
    eigenvalues, eigenvectors
    """
    return eigsh(matrix, k=k, which=which, sigma=sigma, maxiter=maxiter, tol=tol)

def sparse_svds(matrix, k, ncv=None, tol=0, which='LM', v0=None, maxiter=None, return_singular_vectors=True):
    """
    Compute k largest singular values and vectors of a sparse matrix.
    
    Args:
    matrix: Input sparse matrix
    k: Number of singular values/vectors to compute
    ncv: Number of Lanczos vectors generated
    tol: Tolerance for singular values
    which: Which singular values to find ('LM' or 'SM')
    v0: Starting vector for iteration
    maxiter: Maximum number of iterations
    return_singular_vectors: Whether to return singular vectors
    
    Returns:
    U, s, Vt: Left singular vectors, singular values, and right singular vectors
    """
    return svds(matrix, k=k, ncv=ncv, tol=tol, which=which, v0=v0, maxiter=maxiter, return_singular_vectors=return_singular_vectors)

def toeplitz_matrix(c, r=None):
    """
    Generate a Toeplitz matrix.
    
    Args:
    c: First column of the matrix
    r: First row of the matrix (if different from c)
    
    Returns:
    A Toeplitz matrix.
    """
    return linalg.toeplitz(c, r)

def circulant_matrix(c):
    """
    Generate a circulant matrix.
    
    Args:
    c: First column of the circulant matrix
    
    Returns:
    A circulant matrix.
    """
    return linalg.circulant(c)

def hadamard_matrix(n):
    """
    Generate a Hadamard matrix of order n.
    
    Args:
    n: Order of the Hadamard matrix (must be a power of 2)
    
    Returns:
    A Hadamard matrix of order n.
    """
    if n & (n - 1) != 0:
        raise ValueError("n must be a power of 2")
    return linalg.hadamard(n)

def is_positive_definite(matrix, tol=1e-8):
    """
    Check if a matrix is positive definite.
    
    Args:
    matrix: Input symmetric matrix
    tol: Tolerance for eigenvalue positivity check
    
    Returns:
    True if the matrix is positive definite, False otherwise.
    """
    return np.all(np.linalg.eigvalsh(matrix) > tol)

def nearest_positive_definite(matrix, epsilon=0):
    """
    Find the nearest positive definite matrix to the input matrix.
    
    Args:
    matrix: Input matrix
    epsilon: Small number added to the diagonal for numerical stability
    
    Returns:
    The nearest positive definite matrix.
    """
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

