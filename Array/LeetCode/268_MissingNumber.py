class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums1 = sum(range(0, len(nums) + 1))
        missing_number = nums1 - sum(nums)
        return missing_number