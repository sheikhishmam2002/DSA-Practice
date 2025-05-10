from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        permuted_arr = permutations(nums, n)
        final_arr = [list(p) for p in permuted_arr]
        return final_arr
