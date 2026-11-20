class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memoization = {}
        def dp(i, min_cost):
            if (i >= len(cost)):
                return min_cost

            min_cost += cost[i]
            if (i, min_cost) in memoization:
                return memoization[(i, min_cost)]
            temp = min(dp(i+1, min_cost), dp(i+2, min_cost))
            memoization[(i, min_cost)] = temp
            return temp

        return min(dp(0,0), dp(1,0))