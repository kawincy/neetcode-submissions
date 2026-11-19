class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if len(s) == 1:
        #     return True
        l = 0
        r = len(s) - 1

        # s = s.lower()
        while r >= l:
            

            while r >= l and (ord(s[l]) < 48 \
                or (ord(s[l]) > 57 and  ord(s[l]) < 65) \
                or (ord(s[l]) > 90 and  ord(s[l]) < 97) \
                or ord(s[l]) > 122):

                l += 1

            while r >= l and (ord(s[r]) < 48 \
                or (ord(s[r]) > 57 and  ord(s[r]) < 65) \
                or (ord(s[r]) > 90 and  ord(s[r]) < 97) \
                or ord(s[r]) > 122):

                r -= 1

            if l > r:
                continue
            if ord(s[l]) | 32 != ord(s[r]) | 32:
                return False


            l += 1
            r -= 1

        return True

        