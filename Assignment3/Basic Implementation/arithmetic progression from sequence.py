A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        d = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            if arr[i + 1] - arr[i] != d:
                return False
        return True
    arr = [3, 5, 1]
    print(arr)
