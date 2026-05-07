class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        prefix_maxes = size*[0]
        suffix_maxes = size*[0]

        temp_max = 0
        for i in range(size):
            if height[i] > temp_max:
                temp_max = height[i]
            prefix_maxes[i] = temp_max

        temp_max = 0
        for i in range(size - 1, -1, -1):
            if height[i] > temp_max:
                temp_max = height[i]
            suffix_maxes[i] = temp_max
        
        total = 0
        for i in range(size):
            total += min(prefix_maxes[i], suffix_maxes[i]) - height[i]
        
        return total