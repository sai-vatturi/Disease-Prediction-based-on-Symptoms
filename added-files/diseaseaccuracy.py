from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import csv, numpy as np, pandas as pd
import os

# Load the data
data = pd.read_csv(os.path.join("templates", "Training.csv"))
df = pd.DataFrame(data)

# Split the data into training and test sets
cols = df.columns
cols = cols[:-1]
x = df[cols]
y = df['prognosis']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

# Train the decision tree classifier
print("Training Decision Tree")
dt = DecisionTreeClassifier()
clf_dt = dt.fit(x_train, y_train)

# Evaluate the accuracy on the test data
accuracy = clf_dt.score(x_test, y_test)
print(f"Accuracy on test data: {accuracy}")