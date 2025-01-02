class Solution:
    def checkOverlap(self, radius: int, xcenter: int, ycenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        #first we need to find the nearest point on rectangle from circle
        x_nearest=max(x1,min(x2,xcenter))
        y_nearest=max(y1,min(y2,ycenter))
        x_distance=x_nearest-xcenter
        y_distance=y_nearest-ycenter
        return x_distance**2+y_distance**2<=radius**2