from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1) # Count occurrance in nums1
        result = []

        for num in nums2:
            if count[num] > 0: # Only add if num is present in nums1
                result.append(num)
                count[num] -= 1 # Reduce count to prevent extra duplicates
        return result