class Solution:
    def countElements(self, arr: List[int]) -> int:
        freq = {}
        result = 0
        for i in range(len(arr)):
            freq[arr[i]] = freq.get(arr[i],0) + 1
        for n in arr:
            if (n+1) in freq:
                result += 1 
        return result