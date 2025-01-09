class Solution:
    def firstUniqChar(self, s: str) -> int:
        ch=Counter(s)
        for i in range(len(s)):
            if ch[s[i]]==1:
                return i#use of counter
        return -1

        