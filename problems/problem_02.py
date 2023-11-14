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
        
        greater_string = max(str1, str2, key = len)
        lower_string = min(str2, str1, key = len)

        aux_str = ''

        for i in range(len(lower_string), 0, -1):
            if greater_string.count(lower_string[:i]) == len(greater_string)/len(lower_string[:i]):
                aux_str = lower_string[:i]
                break

        return aux_str