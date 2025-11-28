class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        results = []
        for i in range(len(nums1)):
            if nums1[i] in nums2 and nums1[i] not in results:
                results.append(nums1[i])
        return results