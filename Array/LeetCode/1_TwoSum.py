class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map: # If complement exists in map, return indics
                return [num_map[complement], i]
            num_map[num] = i # Store index of the current number
        return []