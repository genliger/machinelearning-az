#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 18:27:11 2020

@author: panda
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#importar el dataset
dataset = pd.read_csv("Salary_Data.csv")
x = dataset.iloc[:, : -1].values
y = dataset.iloc[:, 1].values

#dividir dataset en entrenamiento y prueba
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 1/3, random_state = 0)

#escalado de variables
"""from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)

"""
#crear el modelo de regresion lineal simple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regretion = LinearRegression()
regretion.fit(x_train,y_train)
regretion
#predicción del conjunto con test
y_pred = regretion.predict(x_test)
y_pred
# visualiar datos de entrenamiento
plt.scatter(x_train,y_train, color = "red")
plt.plot(x_train, regretion.predict(x_train), color = "blue")
plt.title("sueldo vs años de experiencia, solo training")
plt.xlabel("años de experiencia")
plt.ylabel("sueldo")
plt.show()


#visualizar datos de test
plt.scatter(x_test,y_test, color = "red")
plt.plot(x_train, regretion.predict(x_train), color = "blue")
plt.title("sueldo vs años de experiencia, solo training")
plt.xlabel("años de experiencia")
plt.ylabel("sueldo")
plt.show()

























