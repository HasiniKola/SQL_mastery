class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        for c in dic.values():
            if c>1:
                return True
        return False
        