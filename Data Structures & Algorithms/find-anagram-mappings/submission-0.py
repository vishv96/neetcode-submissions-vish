class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = {}
        result = []
        for i in range(len(nums2)):
            lookup[nums2[i]] = i
        for n in nums1:
            result.append(lookup[n])
        return result