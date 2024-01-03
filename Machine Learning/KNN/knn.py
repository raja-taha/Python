import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model, preprocessing
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load the dataset
car = pd.read_csv('car.data')
print(car.shape)
print(car.head())

le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(car["buying"]))
maint = le.fit_transform(list(car["maint"]))
door = le.fit_transform(list(car["door"]))
persons = le.fit_transform(list(car["persons"]))
lug_boot = le.fit_transform(list(car["lug_boot"]))
safety = le.fit_transform(list(car["safety"]))
cls = le.fit_transform(list(car["class"]))

X = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(cls)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

knn_classifier = KNeighborsClassifier(n_neighbors=9)

knn_classifier.fit(X_train, y_train)

knn_preds = knn_classifier.predict(X_test)

accuracy_knn = accuracy_score(y_test, knn_preds)
precision_knn = precision_score(y_test, knn_preds, average='weighted', zero_division=0)
recall_knn = recall_score(y_test, knn_preds, average='weighted')

print("\nK-Nearest Neighbors (KNN):")
print("Accuracy:", accuracy_knn)
print("Precision:", precision_knn)
print("Recall:", recall_knn)

names = ["unacc", "acc", "good", "vgood"]

for x in range (len(knn_preds)):
    print(names[knn_preds[x]], X_test[x], names[y_test[x]])

p = "safety"
style.use("ggplot")
plt.scatter(car[p], car['class'])
plt.xlabel(p)
plt.ylabel("Class")
plt.show()