# Leetcode#125 - Valid Palindrome
# T.C O(n) S.C. O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()

        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return False
            start, end = start+1, end-1
        return True
