import numpy as np
from collections import Counter
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.utils.validation import check_X_y, check_array


'''
Building a classifier that Use temperature, luminosity, color_index, log_g as input to predict a star’s spectral class and stage on the HR.
Using the Euclidean distance: to compare the test star x_vector to neigbouring training stars,

K-Nearest Neighbors Classifier for Stellar Spectral Classification:
D = sqrt [(x1 - xi1)**2 + (x2 - xi2)**2 + ... (xn - xin)**2]
'''



class KNNClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, k=5, distance_metric='euclidean'):
        '''Initializes the KNNClassifier.

        Args:
            k (int): Number of nearest neighbors to use. Defaults to 5.
            distance_metric (str): The distance metric to use.
                                             Currently, only 'euclidean' is supported.
                                             Defaults to 'euclidean'.
        '''
        self.k = k
        self.distance_metric = distance_metric
        self.scaler = StandardScaler()

    def fit(self, X, y):
        '''Fit the KNN classifier from the training dataset.

        This method scales the training data and stores it for later use in prediction.

        Args:
            X (array-like of shape (n_samples, n_features)): The training input samples.
            y (array-like of shape (n_samples,)): The target values.

        Returns:
            KNNClassifier: The fitted classifier instance.
        '''

        X, y = check_X_y(X, y)
        self.X_train_ = self.scaler.fit_transform(X)
        self.y_train_ = y
        return self

    def compute_distances(self, X):
        '''Compute distances between each test point and all training points.

        Args:
            X (np.ndarray of shape (n_test_samples, n_features)): The input test samples,
                                                                  which should already be scaled.

        Returns:
            np.ndarray of shape (n_test_samples, n_train_samples): The computed distances.

        Raises:
            ValueError: If an unsupported distance metric is used.
        '''

        if self.distance_metric == 'euclidean':

            # More efficient L2 distance calculation using broadcasting and matrix multiplication
            # (A-B)^2 = A^2 - 2AB + B^2
            X_sq = np.sum(X**2, axis= 1, keepdims= True)
            X_train_sq = np.sum(self.X_train_**2, axis= 1)
            dot_product = np.dot(X, self.X_train_.T)
            distances_sq = X_sq - 2 * dot_product + X_train_sq

            # Ensure no negative values due to floating point inaccuracies before sqrt
            return np.sqrt(np.maximum(distances_sq, 0))
        else:
            raise ValueError(f'Unsupported distance metric: {self.distance_metric}')

    def predict(self, X):
        '''Predict the class labels for the provided data.

        For each test sample, it finds the k-nearest neighbors in the training data
        and predicts the label by majority vote.

        Args:
            X (array-like of shape (n_samples, n_features)): The input samples to predict.

        Returns:
            np.ndarray of shape (n_samples,): The predicted class labels.
        '''
        X = check_array(X)
        X_scaled = self.scaler.transform(X)
        distances = self.compute_distances(X_scaled)

        # indices of the k nearest neighbors for each test sample
        k_indices = np.argsort(distances, axis=1)[:, :self.k]

        # labels of the k nearest neighbors
        k_labels = self.y_train_[k_indices]

        # For each test sample, the most common label among its neighbors using a list comprehension
        y_pred = [Counter(labels).most_common(1)[0][0] for labels in k_labels]

        return np.array(y_pred)

    def score(self, X, y):
        '''Return the mean accuracy on the given test data and labels.

        Args:
            X (array-like of shape (n_samples, n_features)): Test samples.
            y (array-like of shape (n_samples,)): True labels for X.

        Returns:
            float: Mean accuracy of self.predict(X) wrt. y.
        '''

        y_pred = self.predict(X)
        return accuracy_score(y, y_pred)