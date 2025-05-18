a = int(input("Enter a number: "));
sum = 0;
for i in range (1,a+1,1):
    if (i % 7 == 0) & (i % 9 == 0):
        sum += i;
print(sum);