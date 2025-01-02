from typing import List
from itertools import product

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        m, n = len(M), len(M[0])
        A = [[0] * n for _ in range(m)]  # Initialize the result matrix with zeros

        for i, j in product(range(m), range(n)):
            r1, r2 = max(0, i-1), min(i+2, m)  # Row range
            c1, c2 = max(0, j-1), min(j+2, n)  # Column range
            
            # Calculate the sum and count of the neighbors (including the current cell)
            s_sum = sum(M[I][J] for I in range(r1, r2) for J in range(c1, c2))
            count = (r2 - r1) * (c2 - c1)
            
            A[i][j] = s_sum // count  # Compute the integer average
        
        return A
