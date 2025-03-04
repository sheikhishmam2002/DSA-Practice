class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        nums_arr = []

        # Only adding elementst that are not equal to val
        for num in nums:
            if num != val:
                nums_arr.append(num)
        
        # Copying back to nums
        for i in range(len(nums_arr)):
            nums[i] = nums_arr[i]

        return len(nums_arr)