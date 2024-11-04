class Solution(object):
    def makeFancyString(self, s):
        char = []
        for i in range(len(s)):
            if i == 0:
                char.append(s[i])
                count = 1
            else:
                if s[i] == s[i-1]:
                    count += 1
                    if count != 3:
                        char.append(s[i])
                else:
                    count = 1
                    char.append(s[i])

        return ''.join(char)