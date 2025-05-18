def addPrime(n):
    sum = 0;
    for i in range (2,n+1,1):
        flag = 0;
        for j in range(2,i,1):
            if i % j == 0:
                flag = 1;
                break;
        if flag != 1:
            sum += i;
    return sum;
print(addPrime(10));
print(addPrime(11));