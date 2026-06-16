class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charaSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charaSet:
                charaSet.remove(s[l])
                l += 1
            charaSet.add(s[r])
            res = max(res, r - l + 1)
        return res

        