class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_set_1 = set(nums1)
        num_set_2 = set(nums2)
        intersection_set = list(num_set_1 & num_set_2)
        return intersection_set