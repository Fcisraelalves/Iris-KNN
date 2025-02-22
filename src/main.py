from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import joblib

iris = load_iris()

X = iris.data
y = iris.target

#dividindo em teste e treino
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=3)
knnModel = KNeighborsClassifier(11)
knnModel.fit(X_train, y_train)

y_pred = knnModel.predict(X_test)

resultados = classification_report(y_test, y_pred)
print(resultados)

#salvando o modelo
joblib.dump(knnModel, "iris_knn.pkl")
