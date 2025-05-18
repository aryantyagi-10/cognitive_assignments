desc = ("Danishveer","Singh",19,2.456);
l = list(desc);
l.append(4);
l.insert(2,"Hello");
del l[3];
desc = tuple(l);
print(desc);