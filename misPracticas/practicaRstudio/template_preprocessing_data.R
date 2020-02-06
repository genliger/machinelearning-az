# platilla para cargar datos
#importar dataset

dataset = read.csv("Data.csv")




#dividir set de datos en test y entrenamiento
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
split
training_set  = subset(dataset, split == TRUE)
testing_set  = subset(dataset, split == FALSE)
View(training_set)

# escalado de valores
training_set[,2:3] = scale(training_set[,2:3])
testing_set[,2:3] = scale(testing_set[,2:3])
 































