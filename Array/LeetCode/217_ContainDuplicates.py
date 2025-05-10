class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n_before = len(nums)
        n_after = len(set(nums))

        if n_before != n_after:
            return True
        else:
            return False