class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for info in shift:
            direction = info[0]
            amount = info[1]
            if direction == 0:
                s = s[amount:] + s[:amount]
                print(s)
            else:
                s = s[-amount:] + s[:-amount]

        return s 