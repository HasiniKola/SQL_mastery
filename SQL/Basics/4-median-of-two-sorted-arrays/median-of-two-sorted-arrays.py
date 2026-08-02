class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = sorted(nums1 + nums2)   # ensure merged array is sorted
        n = len(res)
        
        if n % 2 == 1:   # odd length
            return float(res[n//2])
        else:            # even length
            return float((res[n//2 - 1] + res[n//2]) / 2)
