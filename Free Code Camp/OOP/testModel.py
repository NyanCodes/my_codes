from sklearn.base import BaseEstimator
from sklearn.metrics import r2_score
import numpy as np

class myDummyModel(BaseEstimator):
    
    def __init__(self, use_median=False):
        self.use_median = use_median
    
    def fit(self, X, y):
        if self.use_median:
            self.value_ = np.median(y)
        else:
            self.value_ = np.mean(y) 
        return self
    
    def predict(self, X):
        output = np.empty(len(X))
        output.fill(self.value_)
        return output

    def score(self, X, y):
        pred = self.predict(X)
        return r2_score(y, pred)

X = np.arange(60).reshape([20, 3])
y = np.arange(20)
y[-1] = 200

# Estimator
estimator = myDummyModel(use_median=True)
print(estimator.get_params())

# Predictor
predictor = myDummyModel(use_median=True)
predictor = predictor.fit(X, y)
print(predictor.predict(X)) 

# Model 
model = myDummyModel(use_median=True)

model = model.fit(X, y)
print(model.score(X, y))