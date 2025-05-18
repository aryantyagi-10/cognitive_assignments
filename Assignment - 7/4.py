def swap(list,idx1,idx2):
    temp = list[idx1];
    list[idx1] = list[idx2];
    list[idx2] = temp;
    return list;
list = [10,20,40,30,50];
print("Original List: ",list);
swapped_list = swap(list,2,3);
print("\nList after swapping",swapped_list);