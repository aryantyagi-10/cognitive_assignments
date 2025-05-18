import numpy as np;
x = np.array([10,52,62,16,16,54,453]);
print("Original array is\n",x,"\n");
y = np.sort(x);
print("Array in sorted order is\n",y,"\n");
z = np.argsort(x);
print("Indices of sorted elements are\n",z,"\n");
print("Four smallest elements are\n");
for i in range(4):
    print(y[i],end = " ");
print("\n");
print("Five largest elements are\n");
a = np.sort(x)[::-1];
for i in range(5):
    print(a[i],end = " ");