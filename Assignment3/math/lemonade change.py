At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

class Solution(object):
    def lemonadeChange(self, bills):
        five_bills = ten_bills = 0

        for bill in bills:
            if bill == 5:
                five_bills += 1
            elif bill == 10:
                if five_bills > 0:
                    five_bills -= 1
                    ten_bills += 1
                else:
                    return False
            elif bill == 20:
                if ten_bills > 0 and five_bills > 0:
                    ten_bills -= 1
                    five_bills -= 1
                elif five_bills >= 3:
                    five_bills -= 3
                else:
                    return False

        return True
