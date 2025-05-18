import random as r;
A = list(range(100,901));
L = r.sample(A,100);
cntEven = 0;
cntOdd = 0;
cntPrime = 0;
for i in L:
    if(i % 2 == 0):
        cntEven += 1;
    elif(i % 2 == 1):
        cntOdd += 1;
print("No of even numbers are",cntEven);
for i in L:
    if(i % 2 == 0):
        print(i,end = " ");
print("\n");
print("No of odd numbers are",cntOdd);
for i in L:
    if(i % 2 == 1):
        print(i,end = " ");
print("\n");
for i in L:
    flag = 0;
    for j in range(2,i):
        if(i % j == 0):
            flag = 1;
            break;
    if(flag == 0):
        cntPrime += 1;
        print(i,end = " ");
print("No of prime numbers are",cntPrime);