# Create two pointers, l and r, increment them. If they point to distinct elements, return false. If they meet in the middle (len(s) is odd) or if l is greater than r (len(s) is even), return true

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ""
        for char in s:
            if char.isalnum():
                clean_str += char.lower()

        return clean_str == clean_str[::-1]