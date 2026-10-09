from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
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
X_train, X_test, Y_train, Y_test = train_test_split(X,y, test_size=0.5,random_state =5)
print("Train set :", X_train.shape)
print("Test set :", X_test.shape)

plt.figure(figsize=(12,4))
plt.subplot(121)
plt.scatter(X_train[ :,0], X_train[ :,1], c=Y_train, alpha = 0.8)
plt.title("Train Set")
plt.subplot(122)

plt.scatter(X_test[ :,0], X_test[ :,1], c=Y_test, alpha = 0.8)

plt.title("Test Set")


X_train, X_test, Y_train, Y_test = train_test_split(X,y, test_size=0.8,random_state =5)
#modification du decoupage 
# Maintenant, découper les 80% d'entraînement en 72% pour l'entraînement et 8% pour la validation
#X_train_final, X_val, y_train_final, y_val = train_test_split(X_train, Y_train, test_size=0.1, random_state=5)



from sklearn.neighbors import KNeighborsClassifier

# Définir le modèle avec k
model = KNeighborsClassifier(n_neighbors=4)
scores = cross_val_score(model, X_train, Y_train, cv=5, scoring='accuracy')  # 5-fold cross-validation
print("Cross-validation scores for K=4 (5 folds):", scores)
# Entraîner le modèle sur les données d'entraînement finale  

# Initialisation de la liste pour sauvegarder les scores
val_score = []

# Boucle pour tester différents nombres de voisins
for k in range(1, 50):  # Test des voisins de 1 à 49
    model = KNeighborsClassifier(n_neighbors=k)  # Initialisation du modèle
    # Validation croisée sur le jeu d'entraînement
    scores = cross_val_score(model, X_train, Y_train, cv=5, scoring='accuracy').mean()  # 5-fold cross-validation
    val_score.append(scores)  # Moyenne des scores pour ce k

# Afficher les scores moyens pour chaque valeur de k
print("Scores moyens pour chaque k :", val_score)
#qst d
#affichage Tracez les scores en fonction du nombre de voisins fixés
plt.figure(figsize=(10, 6))
plt.plot(range(1, 50), val_score, marker='o', label="Validation Accuracy")
plt.xlabel("Number of Neighbors (k)")
plt.ylabel("Cross-Validated Accuracy")
plt.title("KNN Accuracy vs. Number of Neighbors")
plt.legend()
plt.grid()
plt.show()


# Évaluation sur les données d'entraînement
#train_score = model.score(X_train, Y_train)
#print("Train score: ", train_score)

# Évaluation sur les données de test
#test_score = model.score(X_test, Y_test)
#print("Test score: ", test_score)
