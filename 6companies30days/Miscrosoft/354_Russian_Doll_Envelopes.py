class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # first we will sort 
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        list1=[]
        size=0
        for (w,h) in envelopes:
            if not  list1 or h  >list1[-1]:
                list1.append(h)
                size+=1
            else:
                l,r=0,size
                while l<r:
                    #doing the binary search
                    mid=l+(r-l)//2
                    if list1[mid]<h:
                        l=mid+1
                    else:
                        r=mid
                list1[l]=h
        return size
        
        