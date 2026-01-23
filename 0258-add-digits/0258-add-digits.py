class Solution(object):
    def addDigits(self, num):

        while num >= 10:      # repeat until single digit
            sum = 0

            while num > 0:
                rem = num % 10
                sum = sum + rem
                num //= 10

            num = sum         # assign back for next round

        return num