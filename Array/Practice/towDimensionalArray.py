import numpy as np

# Creation of 2D array
print("Creation of 2D array: \n")
twoDArray = np.array([[11,15,10,6],[10,14,11,5], [12,17,12,8],[15,18,14,9]])
print(twoDArray)

###

# # Adding Column
# print("Adding Column: \n")
# newTwoDArray1 = np.insert(twoDArray, 0, [[1,2,3,4]], axis=1) # axis=1 -> top to bottom
# print(newTwoDArray1)

# # Adding Row
# print("Adding Row: \n")
# newTwoDArray2 = np.insert(twoDArray, 0, [[1,2,3,4]], axis=0) # axis=0 -> left to right
# print(newTwoDArray2)

###

# # Accessing Element of a 2D array
# def accessElement(array, rowIndex, colIndex):
#     if rowIndex >= len(array) or colIndex >= len(array[0]):
#         return "Incorrect Index"
#     else:
#         return array[rowIndex][colIndex]
    
# print("Element at the searched index: {}".format(accessElement(twoDArray, 2, 3)))

###

# # Traversing 2D Array
# def traverse2DArray(array):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             print(f"a[{i}][{j}]: {array[i][j]}")

# traverse2DArray(twoDArray)

###

# Deletion in 2D Array
new2DArray = np.delete(twoDArray, 1, axis=1)
print(new2DArray)