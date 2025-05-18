def swap(st,idx1,idx2):
    lst = list(st);
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1];
    swapped_set = set(lst);
    return swapped_set;
st = {10,20,40,30,50};
print("Original Set:", st);
swapped_set = swap(st,2,3);
print("Set after swapping:", swapped_set);
