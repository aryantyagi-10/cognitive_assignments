import pandas as pd;
data = {"Employee_ID" : [101,102,103,104,105], "Name" : ["Alice","Bob","Charlie","Diana","Edward"],
        "Department" : ["HR","IT","IT","Marketing","Sales"], "Age" : [29,34,41,28,38], 
        "Salary" : [50000,70000,65000,55000,60000],"Year_Of_Experience" : [4,8,10,3,12],
        "Joining_Date" : ["2020-03-15","2017-07-19","2013-06-01","2021-02-10","2010-11-25"],
        "Gender" : ["Female","Male","Male","Female","Male"], "Bonus" : [5000,7000,6000,4500,5000],
        "Rating" : [4.5,4.0,3.8,4.7,3.5]};
df = pd.DataFrame(data);
#a part
print(df.shape);
#b part
print(df.info());
#c part
print(df.describe());
#d part
print(df.head());
print(df.tail(3));
#e part
print(df['Salary'].mean());
print(df['Bonus'].sum());
print(df['Age'].min());
print(df['Rating'].max());
#f part
print(df.sort_values('Salary',ascending = False));
#g,h part
A = [4.5,4.0,3.8,4.7,3.5];
B = [];
for i in A:
    if(i >= 4.5):
        B.append("Excellent");
    elif(i >= 4.0 and i < 4.5):
        B.append('Good');
    else:
        B.append('Average');
df['Performance'] = B;
print(df);
#i part
df.rename(columns={'Employee_ID':'ID'},inplace = True);
print(df);
#j part
experience = df[(df['Year_Of_Experience'] > 5)];
department = df[(df['Department'] == 'IT')];
print(experience);
print(department);
#k part
df['Tax'] = df['Salary'] * 0.1;
print(df);
#l part
df.to_csv('modified_employee.csv');