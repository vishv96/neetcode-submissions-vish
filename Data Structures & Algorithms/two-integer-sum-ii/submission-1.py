class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        for i in range(len(numbers)):
            n = target - numbers[i]
            if dic[n]:
                return [dic[n], i + 1]
            dic[numbers[i]] = i + 1
        return []

        