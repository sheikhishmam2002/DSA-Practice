import numpy as np
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        arr = np.array(original)
        if m*n == len(arr):
            arr_2d = arr.reshape(m,n)
            return arr_2d.tolist()
        else:
            return []