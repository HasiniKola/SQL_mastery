class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dic1 = {}
        dic2 = {}

        # Count frequency of characters in s
        for ch in s:
            if ch in dic1:
                dic1[ch] += 1
            else:
                dic1[ch] = 1

        # Count frequency of characters in t
        for ch in t:
            if ch in dic2:
                dic2[ch] += 1
            else:
                dic2[ch] = 1

        # Compare both dictionaries
        if dic1 == dic2:
            return True

        return False