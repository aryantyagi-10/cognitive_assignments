import numpy as np;
array = np.array([[1,-2,3],[-4,5,-6]]);
absolute = np.abs(array);
print("Element wise absolute values are");
for i in range(array.shape[0]):
    for j in range(array.shape[1]): 
        print(f"Absolute value of element at position ({i}, {j}) = {absolute[i, j]}");
flatten_array = array.flatten();
percentiles = np.percentile(flatten_array,[25,50,75]);
print("\nPercentiles (25th, 50th, 75th) of the flattened array:\n", percentiles);
percentiles_columns = np.percentile(array, [25, 50, 75], axis = 0);
print("\nPercentiles (25th, 50th, 75th) for each column:\n", percentiles_columns);
percentiles_rows = np.percentile(array, [25, 50, 75], axis = 1);
print("\nPercentiles (25th, 50th, 75th) for each row:\n", percentiles_rows);
mean_flat = np.mean(flatten_array);
median_flat = np.median(flatten_array);
std_flat = np.std(flatten_array);
print("\n Flatten array mean,median and mode is: ",mean_flat,median_flat,std_flat);
mean_column = np.mean(array, axis = 0);
median_column = np.median(array, axis = 0);
std_column = np.std(array, axis = 0);
print("\n Every column mean,median and mode is: ",mean_column,median_column,std_column);
mean_row = np.mean(array, axis = 1);
median_row = np.median(array, axis = 1);
std_row = np.std(array, axis = 1);
print("\n Every row mean,median and mode is: ",mean_row,median_row,std_row);