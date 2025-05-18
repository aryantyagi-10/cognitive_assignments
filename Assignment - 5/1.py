import numpy as np;
gfg = np.array([[4,1,9],[12,3,1],[4,5,6]]);
sum = np.sum(gfg);
print("Sum of all elements of matrix is: ",sum,"\n");
row_sum = np.sum(gfg,axis = 1);
print("Sum of all elements of matrix row wise is: ",row_sum,"\n");
col_sum = np.sum(gfg,axis = 0);
print("Sum of all elements of matrix column wise is: ",col_sum,"\n");