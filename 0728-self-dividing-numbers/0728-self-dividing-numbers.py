class Solution(object):
    def selfDividingNumbers(self, left, right):
        a = []

        for i in range(left, right + 1):
            temp = i
            x = i
            isSelfDividing = True

            while temp > 0:
                rem = temp % 10

                if rem == 0 or x % rem != 0:
                    isSelfDividing = False
                    break

                temp = temp // 10

            if isSelfDividing:
                a.append(x)

        return a
