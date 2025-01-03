class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects=rects
        self.points=0
        self.store_points=[]
        for rect in rects:
            self.points+=(rect[2]-rect[0]+1)*(rect[3]-rect[1]+1)
            self.store_points.append(self.points)
    def pick(self) -> List[int]:
        point=random.randint(0,self.points-1)
        l,r=0,len(self.rects)-1
        while l<r:
            mid=l+(r-l)//2
            if self.store_points[mid]<=point:
                l=mid+1
            else: r=mid
        rect=self.rects[l]
        x=rect[2]-rect[0]+1
        y=rect[3]-rect[1]+1
        pts_in_rect=x*y
        start=self.store_points[l]-pts_in_rect
        ofset=point-start
        return [rect[0]+ofset%x,rect[1]+ofset//x]


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()