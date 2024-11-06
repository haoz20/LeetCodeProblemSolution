class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        n = x
        reversed_num = 0
        while n != 0:
            last_digit = n % 10
            reversed_num = reversed_num * 10 + last_digit
            n = (n - last_digit)//10

        if x == reversed_num:
            return True

        return False



        # s = str(x)
        # n = len(s)
        # for i in range(n/2):
        #     if s[i] != s[-1*(i+1)]:
        #         return False
        # return True


s = Solution()
print(s.isPalindrome(-121))
