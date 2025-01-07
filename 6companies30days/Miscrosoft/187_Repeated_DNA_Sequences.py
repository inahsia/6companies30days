class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen,result=set(),set()
        for i in range(len(s)-9):
            if s[i:i+10] in seen:
                result.add(s[i:i+10])
            seen.add(s[i:i+10])
        return list(result)
        