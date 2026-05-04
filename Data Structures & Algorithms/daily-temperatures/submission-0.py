class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        res = [0] * size
        #stack containing indices
        stack = []
        for i in range(size - 1, -1 , -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            
            if stack:
                res[i] = stack[-1] - i

            stack.append(i)

        return res
        



        