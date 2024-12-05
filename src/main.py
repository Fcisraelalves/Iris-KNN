import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import joblib

encoder = LabelEncoder()
scaler = StandardScaler()
knn = KNeighborsClassifier(n_neighbors=9)

data = pd.read_csv("iris.data")
X = np.array(data.iloc[:, :-1])
y = np.array(data.iloc[:, -1])

y_data = encoder.fit_transform((y))
X_data = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2, random_state=0)

knn.fit(X_train, y_train)

y_train_pred = knn.predict(X_train)

print("Resultados de treinamento: ")
resultadosTreinamento = classification_report(y_train, y_train_pred)
print(resultadosTreinamento)


y_test_pred = knn.predict(X_test)

print("\nResultados de teste: ")
resultadosTeste = classification_report(y_test, y_test_pred)
print(resultadosTeste)

joblib.dump(knn, "IrisKNN.pkl")


