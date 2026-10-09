# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
#Exercice 1
# Importez les modules nécessaires à la réalisation de cet exercice
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# #Construisez un jeu de données formé de m échantillons aléatoires
np.random.seed(0)
m=100
# X = np.linspace(0,10,m).reshape(m,1)
# Y = X + np.random.random_sample((m,1)) 
# #Affichage des nuages de points
# plt.scatter(X,Y)
# #Modele de regression lineaire 
# model = LinearRegression() 
# #entrainement 
# model.fit(X,Y)
#evaluation du modele
# score = model.score(X,Y)
#print ('Score du modèle : ', score)
#Superposez sur le nuage de points, le modèle prédit
#plt.plot(X, model.predict(X), c='r')
#plt.show()
#Nouveau jeu de données 
X = np.linspace(0,10,m).reshape(m,1)
Y = X**2 + np.random.random(m,1) 
plt.scatter(X,Y)
