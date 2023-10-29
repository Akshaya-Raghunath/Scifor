Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

class Solution(object):
    def setZeroes(self, matrix):
        row = [False]*len(matrix)
        col = [False]*len(matrix[0])
        
        m= len(matrix)
        n= len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]==0):
                    row[i]=True
                    col[j]=True
        
        for i in range(m):
            for j in range(n):
                if(row[i] or col[j]):
                    matrix[i][j]=0   
