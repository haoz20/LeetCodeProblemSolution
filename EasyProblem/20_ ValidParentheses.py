class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        check = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                check.append(i)
            elif i == ")" or i == "}" or i == "]":
                if not check:
                    return False
                top = check.pop()
                if (i, top) in [(')', '('), ('}', '{'), (']', '[')]:
                    continue
                else:
                    return False
        return len(check) == 0
