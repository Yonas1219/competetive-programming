class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        # merged.sort()
        n= len(merged)

        if n % 2 == 1:
            mid = merged[n // 2] + 1
        mid1, mid2 = merged[(n // 2) - 1],merged[n // 2]
        return (mid1 + mid2) / 2
     
        