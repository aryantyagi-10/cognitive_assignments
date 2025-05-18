result = {1:8.8,2:9.77,3:9,4:8.66};
print(result);
print(len(result));
print(result[2]);
for i in result:
    print(result[i]);
print(list(result.keys()),end = " ");
print(list(result.values()),end = " ");