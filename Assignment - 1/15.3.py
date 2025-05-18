import sys;
print(sys.argv);
sum = 0;
for s in sys.argv[1:]:
    sum += int(s);
print(sum);