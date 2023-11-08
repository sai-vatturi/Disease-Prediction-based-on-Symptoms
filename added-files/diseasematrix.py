import os
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

data = pd.read_csv(os.path.join("templates", "Training.csv"))
df = pd.DataFrame(data)

# drop non-numeric column
df = df.select_dtypes(include=[np.number])

cols = df.columns
cols = cols[:-1]
x = df[cols]
y = df['prognosis']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

print("DecisionTree")
dt = DecisionTreeClassifier()
clf_dt = dt.fit(x_train, y_train)

y_pred = clf_dt.predict(x_test)

# print accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# print confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion matrix:\n", conf_matrix)

# compute correlation matrix
corr = df.corr()
print("Correlation matrix:\n", corr)
