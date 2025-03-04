class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: # Handles empty arry
            return 0 

        nums_arr = []
        
        # Collecting unique elements
        for num in nums: 
            if num not in nums_arr:
                nums_arr.append(num)
        
        # Copying unique elements back to the nums
        for i in range(1,len(nums_arr)):
            nums[i] = nums_arr[i]

        # Returning the count of unique element
        return len(nums_arr)