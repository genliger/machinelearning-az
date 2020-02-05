# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#platilla de procesado
#como improtar
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print("hola mundo")


#importar el dataset
dataset = pd.read_csv("Data.csv")
x = dataset.iloc[:, : -1].values
y = dataset.iloc[:, 3].values


#tratamiento de los N
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
imputer = imputer.fit(x[:,1:3])
x[:, 1:3]=imputer.transform(x[:, 1:3])


#Codificar categorias nombres
from sklearn.preprocessing import  OneHotEncoder, LabelEncoder
from sklearn.compose import make_column_transformer

onehotencoder = make_column_transformer((OneHotEncoder(), [0]), remainder = "passthrough")
x = onehotencoder.fit_transform(x)

#codificar caterias purchased
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
#dividir dataset en entrenamiento y prueba
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 0)


#escalado de variables
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)



































































