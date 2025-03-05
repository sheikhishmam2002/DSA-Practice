# Approach-1: My Approach

def firstOccurance(a, start_idx, val):
    l = len(a)
    
    # Base case
    if start_idx == l:
        return -1
    
    # Induction Hypothesis
    if a[start_idx] == val:
        return start_idx
    
    # Induction Step
    occuranceStep = firstOccurance(a,start_idx+1, val)
    return occuranceStep

result = firstOccurance([1,2,2,3,3,4,3,5], 0, 5)
print(result)

#

# # Approach-2: Using Copy

# def firstIndex(a,x):
#     l = len(a)
    
#     # Base Case
#     if l == 0 : 
#         return -1
    
#     # Induction Hypothesis
#     if a[0] == x:
#         return 0
    
#     # Indcution Steps
#     smallerList = [1:]
#     smallerListOutput = firstIndex(smallerList, x)
    
#     if smallerListOutput == -1:
#         return -1
#     else:
#         return smallerListOutput + 1
    
    
    