# Create two pointers, l and r, increment them. If they point to distinct elements, return false. If they meet in the middle (len(s) is odd) or if l is greater than r (len(s) is even), return true

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while not s[l].isalnum():
                l += 1
                if l >= len(s): 
                    return True
            while not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True