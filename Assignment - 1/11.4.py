L1 = [1,3,5,7];
L2 = [2,4,6,8];
L3 = L1 + L2;
print(L3);
L = [i*3 for i in L1];
print(L);
if(6 in L1) == True:
    print("Found");
else:
    print("Not found");
if(6 in L3) == True:
    print("Found");
else:
    print("Not found");