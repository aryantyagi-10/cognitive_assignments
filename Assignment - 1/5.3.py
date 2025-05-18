a = int(input("Enter a number: "));
sum = 0;
for i in range (2,a+1,1):
    flag = 0;
    for j in range(2,i,1):
        if i % j == 0:
            flag = 1;
            break;
    if flag != 1:
        sum += i;
print(sum);