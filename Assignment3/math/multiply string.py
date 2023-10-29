Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
    def multiply(self, num1, num2):
        num = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        r1=0
        r2=0
        
        for i in num1:
            r1=10*r1+num[i]
        for j in num2:
            r2=10*r2+num[j]
            
        return str(r1*r2)
