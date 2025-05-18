result = {1:8.8,2:9.77,3:9,4:8.66};
print(result);
result[1] = 9.2;
print(result);
result[4] = 9;
print(result);
del result[3];
print(result);
if 1 in result:
    print("Present");
else:
    print("Not present");
if 0 in result:
    print("Present");
else:
    print("Not present");