""" "
Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


Constraints:
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of English uppercase letters.
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_len = len(str1)
        str2_len = len(str2)

        if str1_len < 1:
            raise ValueError('Word 1 length must be greater than 1')

        if str2_len > 1000:
            raise ValueError('Word 2 length must be lower than 100')

        if (
            str1.islower()
            or str2.islower()
            or not str1.isalpha()
            or not str2.isalpha()
        ):
            raise ValueError(
                'The word must be only consist of lowercase English letters.'
            )

        greater_string = max(str1, str2, key=len)
        lower_string = min(str2, str1, key=len)

        common_prefix_str = ''

        for i in range(len(lower_string), 0, -1):
            if greater_string.count(lower_string[:i]) == len(
                greater_string
            ) / len(lower_string[:i]) and lower_string.count(
                lower_string[:i]
            ) == len(
                lower_string
            ) / len(
                lower_string[:i]
            ):
                common_prefix_str = lower_string[:i]
                break

        return common_prefix_str
