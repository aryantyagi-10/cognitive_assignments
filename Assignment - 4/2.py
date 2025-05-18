import numpy as np;
arr = np.array([1,2,3,6,4,5]);
print("Original array is: ",arr,"\n");
arr1 = np.flip(arr);
print("Reversed array is: ",arr1,"\n");

x = np.array([1,2,3,4,5,1,2,1,1,1]);
print("Original array is: ",x);
a = np.bincount(x);
count1 = np.max(a);
mod = np.where(a == count1)[0];
mode1 = np.max(mod);
print("Most frequent value in array is: ",mode1);
print("Index of most frequent element of array is");
for i in range (len(x)):
    if x[i] == mode1:
        print(i,end = " ");
print("\n");

y = np.array([1,1,1,2,3,4,2,4,3,3]);
print("Original array is: ",y);
b = np.bincount(y);
count2 = np.max(b);
mode = np.where(b == count2)[0];
mode2 = np.max(mode);
print("Most frequent value in array is: ",mode2);
print("Index of most frequent element of array is");
for i in range (len(y)):
    if y[i] == mode2:
        print(i,end = " ");
print("\n");