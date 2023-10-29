You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted

class Solution(object):
    def average(self, salary):
        salary.sort()
        salary[0], salary[-1] = 0, 0
        return float((sum(salary)*1.0) / (len(salary) - 2))
