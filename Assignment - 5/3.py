import numpy as np;
X = ord('D') + ord('S');
arr = np.array([X,X+50,X+100,X+150,X+200]);
print("Dataset is: ",arr,"\n");
tax = (((X % 5) + 5) / 100); 
print("Tax rate is: ",tax,"\n");
sales = arr * (1 + tax);
print("Sales is: ",sales,"\n");
discount = [];
for i in range(len(sales)):
    if sales[i] < (X + 100):
        discount.append(float(sales[i]) * 0.95);
    else:
        discount.append(float(sales[i]) * 0.90);
print("Sales after applying discount is: ",discount,"\n");
matrix = np.tile(arr,(3,1));
print("Sales matrix is: ",matrix,"\n");
sales_matrix = matrix * (1 + (0.02 * np.arange(3).reshape(-1,1)));
print("Sales matrix after 2% increase is: ",sales_matrix,"\n");