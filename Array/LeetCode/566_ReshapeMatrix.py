import numpy as np

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        arr_2d = np.array(mat)
        if arr_2d.size != r*c:
            return mat
        else:
            reshaped = arr_2d.reshape(r,c)
            return reshaped.tolist()