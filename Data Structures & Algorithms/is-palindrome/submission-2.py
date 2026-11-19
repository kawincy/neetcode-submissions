class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1
        while front < back:
            if ord(s[front]) < 48 or ord(s[front]) >= 58:
                if ord(s[front]) | 32 < 97 or ord(s[front]) | 32 > 122:
                    front += 1
                    continue
            if ord(s[back]) < 48 or ord(s[back]) >= 58:
                if ord(s[back]) | 32 < 97 or ord(s[back]) | 32 > 122:
                    back -= 1
                    continue
            if ord(s[front]) | 32 != ord(s[back]) | 32:
                    return False
            front += 1
            back -= 1
        return True
