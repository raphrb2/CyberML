from sklearn.datasets import make_blobs
import numpy as np

def get_distributions(centers, cluster_std, n_samples):
    """
    Generate Gaussian data distributions for machine learning.
    
    :param centers: the barycenter of the distributions (also implicitly defines the number of distributions)
    :param cluster_std: the standard deviation of the clusters. Value is common for all clusters.
    :param n_samples: the total number of samples in the distributions to be generated
    :return: Gaussian data distributions matching given params.
    """
    X, y = make_blobs(n_samples=n_samples, centers=centers, cluster_std=cluster_std, random_state=0)
    return X, y

