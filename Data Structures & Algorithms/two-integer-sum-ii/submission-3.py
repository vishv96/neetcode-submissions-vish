class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []

        i = 0
        j = len(numbers) - 1

        while i < j:
            sum = numbers[i] + numbers[j]
            if target < sum :
                j -= 1
            elif target > sum:
                i += 1
            else:
                break
            
        res = [i + 1, j+1]
        return res