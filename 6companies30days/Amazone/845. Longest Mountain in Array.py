class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr)<3:
            return 0
        
        max_len=0
        for i in range(1,len(arr)-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                left=i-1
                right=i+1
                while left > 0 and arr[left]>arr[left-1]:
                    left-=1
                while right < len(arr)-1 and arr[right]>arr[right+1]:
                    right+=1
                mountain_lenght=right-left+1
                max_len=max(mountain_lenght,max_len)
        return max_len