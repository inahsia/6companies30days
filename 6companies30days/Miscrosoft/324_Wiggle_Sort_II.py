from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:

        nums.sort()
        half = len(nums[::2]) - 1
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]


    

        # nums.sort()
        # for i in range(0,len(nums)-1):
        #     if (i % 2 == 0 and nums[i] > nums[i + 1]) or (i % 2 != 0 and nums[i] < nums[i + 1]):
        #          nums[i],nums[i+1]=nums[i+1],nums[i]

        return nums



        