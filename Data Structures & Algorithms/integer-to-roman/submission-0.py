class Solution:
    def intToRoman(self, num: int) -> str:
        # harcode bank of possible values
        # iterate through from largest to smallest, 
        # append hardcoded string to result num // value times
        # set num to num % value

        bank = [(1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'),
                (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'), 
                (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M')]

        result = ''
        for value in reversed(bank):
            count = num // value[0]
            for _ in range(count):
                result += value[1]
            num %= value[0]

        return result



        