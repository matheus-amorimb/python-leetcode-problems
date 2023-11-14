"""
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d


Constraints:
- 1 <= word1.length, word2.length <= 100
- word1 and word2 consist of lowercase English letters.
"""
from .execution_time import timing_decorator

class Solution:
    
    @timing_decorator
    def mergeAlternately(self, word1: str, word2: str):
        word1_len, word2_len = len(word1), len(word2)
        word_aux = ''
        
        if word1_len < 1:
            raise ValueError('Word 1 length must be greater than 1')

        if word2_len > 100:
            raise ValueError('Word 2 length must be lower than 100')

        if (
            not word1.islower()
            or not word2.islower()
            or not word1.isalpha()
            or not word2.isalpha()
        ):
            raise ValueError(
                'The word must be only consist of lowercase English letters.'
            )
        
        if word1_len < word2_len:
            word1 += (word2_len - word1_len) * ' '
        else:
            word2 += (word1_len - word2_len) * ' '
        
        #The join() method takes all items in an iterable and joins them into one string.
        word_aux = ''.join([a + b for a, b in zip(word1, word2)]).replace(' ', '')

        return word_aux