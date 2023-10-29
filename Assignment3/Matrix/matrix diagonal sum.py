Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

class Solution(object):
    def diagonalSum(self, mat):
        size = len(mat)
        primary_sum = sum(mat[i][i] for i in range(size))
        secondary_sum = sum(mat[i][size - i - 1] for i in range(size) if i != size - i - 1)
        return primary_sum + secondary_sum
