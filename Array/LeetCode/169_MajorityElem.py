class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        for val,val_count in counter.items():
            if val_count > len(nums) // 2:
                return val
        return None