Given two binary strings a and b, return their sum as a binary string

class Solution(object):
    def addBinary(self, a, b):
        s = int(a,2) + int(b,2)
        s = bin(s)
        return s[2:]
