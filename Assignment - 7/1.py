import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;
roll_number = 102317081;
np.random.seed(roll_number);

sales_data = np.random.randint(1000,5001,size = (12,4));
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports'];
df = pd.DataFrame(sales_data, columns = categories, index = months);
print(df);

print("First 5 rows of sales data: ");
print(df.head());
print("\nSummary statistis of the DataFrame: ");
print(df.describe());
df['Total Sales'] = df.sum(axis = 1);
category_total = df[categories].sum(axis = 0);
print("Total sales per category is\n",category_total);
print("\nTotal sales per month is\n",df['Total Sales']);
growth_rate = df[categories].pct_change() * 100;
print("Sales growth rate for each category is\n",growth_rate);
df['Growth Rate'] = df['Total Sales'].pct_change() * 100;
print("DataFrame with Total Sales and Growth Rate added\n",df[['Total Sales', 'Growth Rate']], "\n");
if roll_number % 2 == 0:  
    df['Electronics'] *= 0.90;  
    print("\nApplied 10% discount to Electronics category.")
else: 
    df['Clothing'] *= 0.85;
    print("\nApplied 15% discount to Clothing category.")
print("Updated DataFrame with Discounts\n");
print(df);

for it in categories:
    plt.plot(df.index,df[it]);
plt.title('Monthly Sales Trends for Each Category');
plt.xlabel('Month');
plt.ylabel('Sales');
plt.show();
sns.boxplot(data = df[categories]);
plt.title('Sales Distribution for Each Category');
plt.xlabel('Category');
plt.ylabel('Sales');
plt.show();