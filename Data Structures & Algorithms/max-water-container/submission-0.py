class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
      
        max_area = 0
        while p1 < p2:
            width = (p2 - p1)
            height = min(heights[p1], heights[p2])
            if (width*height) > max_area:
                max_area = width*height

            if heights[p1] < heights[p2]:
                p1+=1
            elif heights[p2] < heights[p1]:
                p2-=1
            elif heights[p2] == heights[p1]:
                p2-=1
        
        return max_area
