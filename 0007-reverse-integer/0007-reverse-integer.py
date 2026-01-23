class Solution(object):
    def reverse(self, x):
        rev=0
        temp=x #store x in temp
        if(x<0):
            x=x*-1 #convert -ve integer to +ve to find reverse

        if(x >= -2**31 and x <= 2**31-1):
            while(x>0):
                rem=x%10
                rev=rev*10+rem
                x//=10

            if temp<0:
                rev=rev*-1   #add -ve sign to rev if temp < 0

            if(rev >= -2**31 and rev <= 2**31-1):
                return rev
            else:
                return 0
        else:
            return 0
       


        