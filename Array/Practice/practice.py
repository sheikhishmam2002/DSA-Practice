# ## Find Number of Days Above Average Temperature

# days_temp = int(input("How many day's temperature? "))
# days_temp_list = []
# above_avg_count = 0
# filtered_temp = []

# for i in range(days_temp):
#     temp_input = int(input(f"Day {i+1}'s temp: "))
#     days_temp_list.append(temp_input)

# def calculate_average(temp_list):
#     return sum(temp_list) / len(temp_list)

# result = calculate_average(days_temp_list)
# print('Average: ',result)

# for i in days_temp_list:
#     if i > result:
#         filtered_temp.append(i)

# print(len(filtered_temp))

### Two Sum

# def findPairs(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] == nums[j]:
#                 continue
#             elif nums[i] + nums[j] == target:
#                 print(f"[{i},{j}]")

# myList = [1,2,3,2,3,3,4,5,6]
# findPairs(myList, 6)

# ## Two Sum - LeetCode
# def twoSum(nums, target):
#     num_map = {}
    
#     for i, num in enumerate(nums):
#         complement = target - num
        
#         if complement in num_map:
#             return [num_map[complement], i]
#         num_map[num] = i
#     return []

# result = twoSum([2,7,11,15], 9)
# print(result)

# from itertools import combinations
     
# out_list = []
# my_input_initial = input("Enter two number")
# my_input_final = [int(x) for x in str(my_input_initial)]
# combo = list(combinations(my_input_final, 2))
# for pair in combo:
#     result = pair[0] * pair[1]
#     out_list.append(result)
# print(max(out_list))


# import numpy as np

# def arr_conversion(list, row, col):
#     arr = np.array(list)
#     if row * col == len(arr):
#         arr_2d = arr.reshape(row, col)
#         return arr_2d.tolist()
#     else:
#         return []
    
# result = arr_conversion([1,2,3,4,5,6],3,2)
# print(result)

import numpy as np
arr2d = np.array([[1,2],[3,4]])
arr1d = arr2d.flatten()
print(arr1d)
