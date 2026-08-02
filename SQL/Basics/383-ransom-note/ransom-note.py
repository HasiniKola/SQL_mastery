class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic={}
        for ch in magazine:
            if ch in dic:
                dic[ch]+=1
            else:
                dic[ch]=1
        for ch in ransomNote:
            if ch not in dic:
                return False
            if dic[ch]==0:
                return False
            dic[ch]-=1
        return True
        


        