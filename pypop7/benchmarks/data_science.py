import numpy as np

from pypop7.benchmarks.base_functions import BaseFunction


def logistic_regression(w, x, y):
    """"Cross-Entropy Loss Function of (Binary) Logistic Regression.

        https://web.stanford.edu/~jurafsky/slp3/5.pdf
    ""
    loss = np.empty(len(w))
    for i in range(len(w)):
        p = 1.0/(1.0 + np.exp(-np.dot(x[i], w)))
        loss[i] = -y[i]*np.log(p) - (1.0 - y[i])*np.log(1.0 - p))
    return np.mean(loss)


class LogisticRegression(BaseFunction):
    def __call__(self, w, x, y):
        return logistic_regression(w, x, y)