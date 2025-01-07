class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans,left,list1=0,-1,deque()
        for i in range(len(nums)):
            if nums[i]%2:#odd
                list1.append(i)
                if len(list1)>k:
                    left=list1.popleft()
            if len(list1)==k:
                ans+=list1[0]-left
        return ans

        
        