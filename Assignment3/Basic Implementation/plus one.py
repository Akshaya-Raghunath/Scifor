You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

class Solution(object):
    def plusOne(self, digits):
        i = len(digits) - 1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0 
            i -= 1
        digits.insert(0, 1)
        return digits
    digits = [1, 2, 3]
    print(digits) 
