import pandas as pd;
df = pd.read_csv('C:/Users/Acer/Downloads/archive/Iris.csv');
df.drop(3,axis = 0,inplace = True);
df.drop(df.columns[2],axis = 1,inplace = True);
print(df);
