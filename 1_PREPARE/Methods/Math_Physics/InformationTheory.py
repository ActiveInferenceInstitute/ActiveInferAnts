import numpy as np
from scipy.stats import entropy, multivariate_normal
from scipy.special import rel_entr, digamma
from scipy.spatial.distance import cdist
from sklearn.metrics import mutual_info_score
import networkx as nx
from sklearn.neighbors import KernelDensity
from sklearn.feature_selection import mutual_info_regression
from scipy.integrate import quad
from scipy.optimize import minimize
from sklearn.neighbors import KNeighborsRegressor
from ripser import ripser
from persim import plot_diagrams

def shannon_entropy(p, base=None):
    """
    Compute the Shannon entropy of a probability distribution.
    
    Args:
    p (numpy.ndarray): Array-like probability distribution
    base (float, optional): The logarithmic base to use (default: e)
    
    Returns:
    float: The Shannon entropy
    
    Raises:
    ValueError: If p contains negative values or does not sum to 1 (within numerical precision)
    """
    if np.any(p < 0) or not np.isclose(np.sum(p), 1, atol=1e-8):
        raise ValueError("Input must be a valid probability distribution")
    return entropy(p, base=base)

def kullback_leibler_divergence(p, q):
    """
    Compute the Kullback-Leibler divergence between two probability distributions.
    
    Args:
    p (numpy.ndarray): Array-like probability distribution
    q (numpy.ndarray): Array-like probability distribution
    
    Returns:
    float: The KL divergence
    
    Raises:
    ValueError: If p and q have different shapes or contain invalid probability values
    """
    if p.shape != q.shape:
        raise ValueError("Input distributions must have the same shape")
    if np.any(p < 0) or np.any(q <= 0) or not np.isclose(np.sum(p), 1, atol=1e-8) or not np.isclose(np.sum(q), 1, atol=1e-8):
        raise ValueError("Inputs must be valid probability distributions")
    return np.sum(rel_entr(p, q))

def jensen_shannon_divergence(p, q):
    """
    Compute the Jensen-Shannon divergence between two probability distributions.
    
    Args:
    p (numpy.ndarray): Array-like probability distribution
    q (numpy.ndarray): Array-like probability distribution
    
    Returns:
    float: The JS divergence
    
    Raises:
    ValueError: If p and q have different shapes or contain invalid probability values
    """
    if p.shape != q.shape:
        raise ValueError("Input distributions must have the same shape")
    if np.any(p < 0) or np.any(q < 0) or not np.isclose(np.sum(p), 1, atol=1e-8) or not np.isclose(np.sum(q), 1, atol=1e-8):
        raise ValueError("Inputs must be valid probability distributions")
    m = 0.5 * (p + q)
    return 0.5 * (kullback_leibler_divergence(p, m) + kullback_leibler_divergence(q, m))

def mutual_information(X, Y, method='sklearn', n_neighbors=3, bandwidth=0.1):
    """
    Compute the mutual information between two random variables.
    
    Args:
    X (numpy.ndarray): Array-like random variable
    Y (numpy.ndarray): Array-like random variable
    method (str): 'sklearn' for discrete variables, 'kde' for continuous variables, 'knn' for k-nearest neighbors estimator
    n_neighbors (int): Number of neighbors for KNN method (default: 3)
    bandwidth (float): Bandwidth for KDE method (default: 0.1)
    
    Returns:
    float: The mutual information
    
    Raises:
    ValueError: If the method is not supported or if inputs have different lengths
    """
    if len(X) != len(Y):
        raise ValueError("Input arrays must have the same length")
    
    if method == 'sklearn':
        return mutual_info_score(X, Y)
    elif method == 'kde':
        return mutual_information_kde(X, Y, bandwidth=bandwidth)
    elif method == 'knn':
        return mutual_information_knn(X, Y, n_neighbors=n_neighbors)
    else:
        raise ValueError("Unsupported method. Choose 'sklearn', 'kde', or 'knn'.")

def mutual_information_kde(X, Y, bandwidth=0.1):
    """
    Compute mutual information using kernel density estimation for continuous variables.
    
    Args:
    X (numpy.ndarray): Array-like continuous random variable
    Y (numpy.ndarray): Array-like continuous random variable
    bandwidth (float): Bandwidth for KDE (default: 0.1)
    
    Returns:
    float: The mutual information
    """
    xy = np.column_stack((X, Y))
    kde_xy = KernelDensity(bandwidth=bandwidth).fit(xy)
    kde_x = KernelDensity(bandwidth=bandwidth).fit(X.reshape(-1, 1))
    kde_y = KernelDensity(bandwidth=bandwidth).fit(Y.reshape(-1, 1))
    
    samples = np.column_stack((X, Y))
    log_pxy = kde_xy.score_samples(samples)
    log_px = kde_x.score_samples(X.reshape(-1, 1))
    log_py = kde_y.score_samples(Y.reshape(-1, 1))
    
    return np.mean(log_pxy - log_px - log_py)

def mutual_information_knn(X, Y, n_neighbors=3):
    """
    Compute mutual information using k-nearest neighbors estimator.
    
    Args:
    X (numpy.ndarray): Array-like random variable
    Y (numpy.ndarray): Array-like random variable
    n_neighbors (int): Number of neighbors (default: 3)
    
    Returns:
    float: The mutual information
    """
    xy = np.column_stack((X, Y))
    x_tree = KNeighborsRegressor(n_neighbors=n_neighbors, metric='chebyshev')
    y_tree = KNeighborsRegressor(n_neighbors=n_neighbors, metric='chebyshev')
    xy_tree = KNeighborsRegressor(n_neighbors=n_neighbors, metric='chebyshev')
    
    x_tree.fit(X.reshape(-1, 1), np.zeros(len(X)))
    y_tree.fit(Y.reshape(-1, 1), np.zeros(len(Y)))
    xy_tree.fit(xy, np.zeros(len(X)))
    
    rx = x_tree.kneighbors()[0][:, -1]
    ry = y_tree.kneighbors()[0][:, -1]
    rxy = xy_tree.kneighbors()[0][:, -1]
    
    n = len(X)
    return digamma(n) + digamma(n_neighbors) - np.mean(digamma(rx+1) + digamma(ry+1) - digamma(rxy+1))

def conditional_entropy(X, Y):
    """
    Compute the conditional entropy of X given Y.
    
    Args:
    X (numpy.ndarray): Array-like random variable
    Y (numpy.ndarray): Array-like random variable
    
    Returns:
    float: The conditional entropy
    """
    return shannon_entropy(np.column_stack((X, Y))) - shannon_entropy(Y)

def information_gain(X, Y):
    """
    Compute the information gain of X with respect to Y.
    
    Args:
    X (numpy.ndarray): Array-like random variable
    Y (numpy.ndarray): Array-like random variable
    
    Returns:
    float: The information gain
    """
    return shannon_entropy(X) - conditional_entropy(X, Y)

def fisher_information_matrix(log_likelihood, theta, epsilon=1e-8):
    """
    Compute the Fisher Information Matrix using numerical differentiation.
    
    Args:
    log_likelihood (callable): Function that computes the log-likelihood
    theta (numpy.ndarray): Parameter vector
    epsilon (float): Small value for numerical differentiation (default: 1e-8)
    
    Returns:
    numpy.ndarray: The Fisher Information Matrix
    """
    n = len(theta)
    fim = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            theta_plus_i = theta.copy()
            theta_minus_i = theta.copy()
            theta_plus_i[i] += epsilon
            theta_minus_i[i] -= epsilon
            
            theta_plus_j = theta.copy()
            theta_minus_j = theta.copy()
            theta_plus_j[j] += epsilon
            theta_minus_j[j] -= epsilon
            
            d2l_didj = (log_likelihood(theta_plus_i + theta_plus_j) - 
                        log_likelihood(theta_plus_i + theta_minus_j) - 
                        log_likelihood(theta_minus_i + theta_plus_j) + 
                        log_likelihood(theta_minus_i + theta_minus_j)) / (4 * epsilon**2)
            
            fim[i, j] = -d2l_didj
    
    return fim

def information_bottleneck(X, Y, beta, num_iterations=100, num_clusters=10):
    """
    Implement the Information Bottleneck method using deterministic annealing.
    
    Args:
    X (numpy.ndarray): Input variable
    Y (numpy.ndarray): Output variable
    beta (float): Trade-off parameter
    num_iterations (int): Number of iterations (default: 100)
    num_clusters (int): Number of clusters for the compressed representation (default: 10)
    
    Returns:
    numpy.ndarray: Compressed representation of X
    """
    p_x = np.mean(X, axis=0)
    p_y_given_x = np.mean(Y[:, np.newaxis, :] == X[np.newaxis, :, :], axis=0)
    p_t_given_x = np.random.rand(len(X), num_clusters)
    p_t_given_x /= p_t_given_x.sum(axis=1, keepdims=True)
    
    for _ in range(num_iterations):
        p_t = np.sum(p_t_given_x * p_x[:, np.newaxis], axis=0)
        p_y_given_t = np.dot(p_t_given_x.T, p_x[:, np.newaxis] * p_y_given_x) / p_t[:, np.newaxis]
        d_kl = rel_entr(p_y_given_x, p_y_given_t[np.newaxis, :, :])
        p_t_given_x_new = p_t[np.newaxis, :] * np.exp(-beta * np.sum(p_y_given_x * d_kl, axis=1))
        p_t_given_x_new /= p_t_given_x_new.sum(axis=1, keepdims=True)
        p_t_given_x = p_t_given_x_new
    
    return p_t_given_x

def information_geometry_distance(p, q, metric='fisher'):
    """
    Compute the distance between two probability distributions in the information geometry.
    
    Args:
    p (numpy.ndarray): Array-like probability distribution
    q (numpy.ndarray): Array-like probability distribution
    metric (str): 'fisher' for Fisher information metric, 'wasserstein' for Wasserstein metric,
                  'hellinger' for Hellinger distance
    
    Returns:
    float: The distance between p and q
    
    Raises:
    ValueError: If the metric is not supported or if inputs are invalid probability distributions
    """
    if np.any(p < 0) or np.any(q < 0) or not np.isclose(np.sum(p), 1, atol=1e-8) or not np.isclose(np.sum(q), 1, atol=1e-8):
        raise ValueError("Inputs must be valid probability distributions")
    
    if metric == 'fisher':
        return np.sqrt(np.sum((np.sqrt(p) - np.sqrt(q))**2))
    elif metric == 'wasserstein':
        return cdist(p.reshape(-1, 1), q.reshape(-1, 1), metric='euclidean').item()
    elif metric == 'hellinger':
        return np.sqrt(0.5 * np.sum((np.sqrt(p) - np.sqrt(q))**2))
    else:
        raise ValueError("Unsupported metric. Choose 'fisher', 'wasserstein', or 'hellinger'.")

def topological_data_analysis(data, max_dimension=2):
    """
    Perform topological data analysis using persistent homology.
    
    Args:
    data (numpy.ndarray): Input data points
    max_dimension (int): Maximum homology dimension to compute (default: 2)
    
    Returns:
    list: A summary of topological features (persistence diagrams)
    """
    diagrams = ripser(data, maxdim=max_dimension)['dgms']
    plot_diagrams(diagrams, show=False)
    return diagrams

def information_flow_graph(data, threshold, method='mi'):
    """
    Construct an information flow graph based on mutual information or transfer entropy.
    
    Args:
    data (numpy.ndarray): Input data (each column is a variable)
    threshold (float): Minimum information measure to create an edge
    method (str): 'mi' for mutual information, 'te' for transfer entropy
    
    Returns:
    networkx.DiGraph: A NetworkX graph representing information flow
    
    Raises:
    ValueError: If the method is not supported
    """
    n_vars = data.shape[1]
    G = nx.DiGraph()
    
    for i in range(n_vars):
        for j in range(n_vars):
            if i != j:
                if method == 'mi':
                    info_measure = mutual_information(data[:, i], data[:, j])
                elif method == 'te':
                    info_measure = transfer_entropy(data[:, i], data[:, j])
                else:
                    raise ValueError("Unsupported method. Choose 'mi' or 'te'.")
                
                if info_measure > threshold:
                    G.add_edge(i, j, weight=info_measure)
    
    return G

def transfer_entropy(X, Y, k=1, l=1, estimator='knn'):
    """
    Compute transfer entropy from X to Y.
    
    Args:
    X (numpy.ndarray): Time series data
    Y (numpy.ndarray): Time series data
    k (int): History length for X (default: 1)
    l (int): History length for Y (default: 1)
    estimator (str): 'knn' for k-nearest neighbors, 'kernel' for kernel density estimation
    
    Returns:
    float: The transfer entropy from X to Y
    
    Raises:
    ValueError: If the estimator is not supported
    """
    def get_histories(data, length):
        return np.array([data[i:i+length] for i in range(len(data)-length+1)])
    
    X_hist = get_histories(X[:-1], k)
    Y_hist = get_histories(Y[:-1], l)
    Y_future = Y[l:]
    
    XY_hist = np.column_stack((X_hist, Y_hist))
    
    if estimator == 'knn':
        knn = KNeighborsRegressor(n_neighbors=k+1)
        knn.fit(Y_hist, Y_future)
        H_Y_given_Y_hist = -np.mean(np.log(knn.predict(Y_hist)))
        
        knn.fit(XY_hist, Y_future)
        H_Y_given_XY_hist = -np.mean(np.log(knn.predict(XY_hist)))
    elif estimator == 'kernel':
        kde_Y = KernelDensity().fit(np.column_stack((Y_hist, Y_future)))
        H_Y_given_Y_hist = -np.mean(kde_Y.score_samples(np.column_stack((Y_hist, Y_future))))
        
        kde_XY = KernelDensity().fit(np.column_stack((XY_hist, Y_future)))
        H_Y_given_XY_hist = -np.mean(kde_XY.score_samples(np.column_stack((XY_hist, Y_future))))
    else:
        raise ValueError("Unsupported estimator. Choose 'knn' or 'kernel'.")
    
    return H_Y_given_Y_hist - H_Y_given_XY_hist

def renyi_entropy(p, alpha=2):
    """
    Compute the Renyi entropy of a probability distribution.
    
    Args:
    p: Array-like probability distribution
    alpha: Order of the Renyi entropy (alpha > 0, alpha != 1)
    
    Returns:
    The Renyi entropy
    """
    if alpha == 1:
        return shannon_entropy(p)
    else:
        return (1 / (1 - alpha)) * np.log(np.sum(p**alpha))

def tsallis_entropy(p, q):
    """
    Compute the Tsallis entropy of a probability distribution.
    
    Args:
    p: Array-like probability distribution
    q: Entropic index (q > 0, q != 1)
    
    Returns:
    The Tsallis entropy
    """
    if q == 1:
        return shannon_entropy(p)
    else:
        return (1 / (q - 1)) * (1 - np.sum(p**q))

def differential_entropy(pdf, lower_bound, upper_bound):
    """
    Compute the differential entropy of a continuous probability distribution.
    
    Args:
    pdf: Probability density function
    lower_bound: Lower bound of the distribution support
    upper_bound: Upper bound of the distribution support
    
    Returns:
    The differential entropy
    """
    def integrand(x):
        p = pdf(x)
        return -p * np.log(p) if p > 0 else 0
    
    return quad(integrand, lower_bound, upper_bound)[0]

def maximum_entropy_distribution(constraints, domain):
    """
    Find the maximum entropy distribution subject to given constraints.
    
    Args:
    constraints: List of constraint functions
    domain: Tuple (lower_bound, upper_bound) of the distribution support
    
    Returns:
    The maximum entropy probability density function
    """
    def neg_entropy(params):
        def pdf(x):
            return np.exp(-params[0] - sum(p * c(x) for p, c in zip(params[1:], constraints)))
        
        Z = quad(pdf, domain[0], domain[1])[0]
        normalized_pdf = lambda x: pdf(x) / Z
        return -differential_entropy(normalized_pdf, domain[0], domain[1])
    
    def constraint_satisfaction(params):
        def pdf(x):
            return np.exp(-params[0] - sum(p * c(x) for p, c in zip(params[1:], constraints)))
        
        Z = quad(pdf, domain[0], domain[1])[0]
        normalized_pdf = lambda x: pdf(x) / Z
        return [quad(lambda x: c(x) * normalized_pdf(x), domain[0], domain[1])[0] for c in constraints]
    
    initial_params = np.zeros(len(constraints) + 1)
    res = minimize(neg_entropy, initial_params, method='SLSQP', constraints={'type': 'eq', 'fun': constraint_satisfaction})
    
    def max_ent_pdf(x):
        return np.exp(-res.x[0] - sum(p * c(x) for p, c in zip(res.x[1:], constraints)))
    
    Z = quad(max_ent_pdf, domain[0], domain[1])[0]
    return lambda x: max_ent_pdf(x) / Z

def information_projection(target_dist, constraint_dists, domain):
    """
    Perform information projection of a target distribution onto a set of constraint distributions.
    
    Args:
    target_dist: Target probability distribution
    constraint_dists: List of constraint probability distributions
    domain: Tuple (lower_bound, upper_bound) of the distribution support
    
    Returns:
    The projected probability distribution
    """
    def kl_divergence(p, q):
        return quad(lambda x: p(x) * np.log(p(x) / q(x)), domain[0], domain[1])[0]
    
    def objective(params):
        q = lambda x: np.exp(sum(p * np.log(c(x)) for p, c in zip(params, constraint_dists)))
