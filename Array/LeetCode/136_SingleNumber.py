class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
    
"""
XOR Approach
- Every number that appears twice will cancel itself out when XOR-ed
2^2 = 0 and 1^0 = 1

For nums = [4,1,2,1,2]:

result = 0 ^ 4 ^ 1 ^ 2 ^ 1 ^ 2
       = ((0 ^ 4) ^ (1 ^ 1)) ^ (2 ^ 2)
       = 4 ^ 0 ^ 0 = 4

So, it returns 4 (the correct ans)
"""