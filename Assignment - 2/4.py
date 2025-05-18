A = set([34,56,78,90]);
B = set([78,45,90,23]);
print("Unique scores achieved by both teams are",A.union(B));
print("Common scores of both teams are",A.intersection(B));
print("Scores exclusive of team A is",A-B);
print("Scores exclusive of team B is",B-A);
print("A is subset of B -->",A.issubset(B));
print("B is subset of A -->",B.issubset(A));
n = int(input("Enter score you want to remove: "));
if (n in A):
    A.remove(n);
    print("Set A after removing the score is",A);
else:
    print("Element is not present in set A");