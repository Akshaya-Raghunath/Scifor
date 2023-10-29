There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product) 

class Solution(object):
    def arraySign(self, x):
        product = 1
        for i in x:
            product = product * i
        if product>0:
            return 1
        elif product<0:
            return -1
        else:
            return 0
    x = [-1, -2, -3, -4, 3, 2, 1]
    print(x)
