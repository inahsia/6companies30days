class Solution:
    def convertToTitle(self,num: int) -> str:
        r=[]
        while num>0:
            num-=1
            rem=num%26
            r.append(chr(rem+ord('A')))
            num=num//26
        return ''.join(r[::-1])