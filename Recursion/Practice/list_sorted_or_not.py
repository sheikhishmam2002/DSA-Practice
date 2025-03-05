# Base: l==0 or l == 1 return True
# Induction Hypothesis: It works for l=1 sized lists
# Induction State: 
#                Check [0] > [1] return false
#                else check for smaller list starting from [1,_____]

def isSorted(a):
    l = len(a)
    
    if l == 0 or l == 1:
        return True
    
    if a[0] > a[1]:
        return False
    
    smallerList = a[1:] # It is not efficient for larger list as it take more memory space
    isSmallerListSorted = isSorted(smallerList)
    return isSmallerListSorted

result = isSorted([1,3,2,4,5])
print(result)