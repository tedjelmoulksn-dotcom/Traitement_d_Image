
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y= iris.target
print(X.shape)
print(np.unique(y)) #question 3
print(len(np.unique(y))) #question 4
plt.scatter(X[ :,0],X[ :,1], c=y, alpha=0.8)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,y, test_size=0.2,random_state =None)
print("Train set :", X_train.shape)
print("Test set :", X_test.shape)

plt.figure(figsize=(12,4))
plt.subplot(121)
plt.scatter(X_train[ :,0], X_train[ :,1], c=Y_train, alpha = 0.8)
plt.title("Train Set")
plt.subplot(122)

plt.scatter(X_test[ :,0], X_test[ :,1], c=Y_test, alpha = 0.8)
plt.title("Test Set")