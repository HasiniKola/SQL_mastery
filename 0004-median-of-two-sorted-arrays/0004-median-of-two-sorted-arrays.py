class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res= sorted(nums1+nums2)
        n=len(res)
        if n==1:
            return res[n-1]
        elif n%2!=0:
            return res[n//2]
        else:
            index=int(n/2)
            add = (res[index] + res[index-1])/ 2
            return float(add)
        