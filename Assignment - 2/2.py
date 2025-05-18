T = (45,89.5,76,45.4,89,92,58,45);
print("Original tuple is",T);
print("Maximum element of tuple is",max(T),"and its index is",T.index(max(T)));
print("Minimum element of tuple is",min(T),"and it appears",T.count(min(T)),"times");
L = list(T);
print("Tuple as list is",L);
L.reverse();
T = tuple(L);
print("Tuple in reverse is",T);
n = int(input("Enter score you want to search: "));
if (n in T):
    print("Element found at index",T.index(n));
else:
    print("Element not present in tuple");