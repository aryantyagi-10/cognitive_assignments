import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;
data = {'Subjects' : ['Maths','AI','DBMS','DAA','EDP'], 'Marks' : [92,95,97,99,89]};
df = pd.DataFrame(data);
print(df);
color = ['red','green','yellow','orange','purple'];
sns.barplot(x = "Subjects",y = "Marks",data = df,palette = color);
for index,value in enumerate(df['Marks']):
    plt.text(index,value+1,str(value),ha = 'center', va = 'bottom');
plt.title("Marks in different subjects");
plt.grid();
plt.show();