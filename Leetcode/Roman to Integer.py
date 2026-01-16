from openpyxl.styles.builtins import total


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        prev_val = 0
        for char in reversed(s):
            val = dict_nums[char]
            if val < prev_val:
                res -= val
            else:
                res += val
            prev_val = val
        return res


s = Solution()
stri = "MCMXCIV"
print(s.romanToInt(stri))