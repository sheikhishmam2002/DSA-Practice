def isSortedBetter(a, start_index):
    l = len(a)
    
    if start_index == l -1 or start_index == l:
        return True
    
    if a[start_index] > a[start_index + 1]:
        return False
    
    isSmallerPartSorted = isSortedBetter(a, start_index + 1)
    return isSmallerPartSorted

result = isSortedBetter([1,2,3,4,5,6], 0)

print("The list is sorted") if result else print("The list is not sorted")