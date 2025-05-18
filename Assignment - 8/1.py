from sklearn import datasets;
from sklearn.model_selection import train_test_split;
from sklearn.preprocessing import StandardScaler;
from sklearn.linear_model import LogisticRegression;
from sklearn.metrics import accuracy_score;
import pandas as pd;

iris = datasets.load_iris();
x = iris.data;
y = iris.target;
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state = 42);
scaler = StandardScaler();
x_train_scaled = scaler.fit_transform(x_train);
x_test_scaled = scaler.transform(x_test);
model = LogisticRegression();
model.fit(x_train_scaled,y_train);
y_pred = model.predict(x_test_scaled);
accuracy = accuracy_score(y_test,y_pred);
print(f"Accuracy: {accuracy * 100}");