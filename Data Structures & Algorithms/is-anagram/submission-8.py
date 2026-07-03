class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        dict_one = {}
        dict_two = {}
        
        for c in s:
            dict_one[c] = dict_one.get(c, 0) + 1
        
        for c in t:
            dict_two[c] = dict_two.get(c, 0) + 1


        if dict_one == dict_two:
            return True 

        return False