from itertools import combinations

class Solution:
    def maxProduct(self, n: int) -> int:
        output_list = []
        input_nums = [int(x) for x in str(n)]
        nums_combination = list(combinations(input_nums, 2)) ## generates all unique combinations of a specific length
        for pair in nums_combination:
            result = pair[0] * pair[1]
            output_list.append(result)
        return max(output_list)