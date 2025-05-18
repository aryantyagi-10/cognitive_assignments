T1 = (1,3,5,7);
T2 = (2,4,6,8);
T3 = T2 + T1;
print(T3);
T4 = T1[1:2] + T2[0:1];
print(T4);
if(6 in T1) == True:
    print("Found");
else:
    print("Not found");
if(6 in T3) == True:
    print("Found");
else:
    print("Not found");