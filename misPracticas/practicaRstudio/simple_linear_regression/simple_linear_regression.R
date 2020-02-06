#importar dataset

dataset = read.csv("Salary_Data.csv")
#dividir set de datos en test y entrenamiento
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
split
training_set  = subset(dataset, split == TRUE)
testing_set  = subset(dataset, split == FALSE)
View(training_set)

# escalado de valores
#training_set[,2:3] = scale(training_set[,2:3])
#testing_set[,2:3] = scale(testing_set[,2:3])

#ajustar el modelo de regresion lineal simple con el conjunto de entrenamiento
regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)
#summary ayuda a describir 
#summary(regressor)

#predecir con el conjunto de testing
y_pred = predict(regressor, newdata = testing_set)
y_pred

#visualización en el conjunto de entrenamiento
ggplot()+
  geom_point(aes(x=training_set$YearsExperience, y=training_set$Salary),
             colour = "red") +
  geom_line(aes(x=training_set$YearsExperience,
                y = predict(regressor,newdata = training_set)),
            colour = "blue") +
  ggtitle("suelvos vs años, conjunto de entrenaiento") +
  xlab("años de experiencia") +
  ylab("sueldo $")

## visualizacion de resultados en conjunto de testing
ggplot()+
  geom_point(aes(x=testing_set$YearsExperience, y=testing_set$Salary),
             colour = "red") +
  geom_line(aes(x=training_set$YearsExperience,
                y = predict(regressor,newdata = training_set)),
            colour = "blue") +
  ggtitle("suelvos vs años, conjunto de entrenaiento") +
  xlab("años de experiencia") +
  ylab("sueldo $")

























