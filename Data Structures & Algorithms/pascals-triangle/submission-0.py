class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]]

        for i in range(1, numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = dp[i-1][j-1] + dp[i-1][j]

            dp.append(row)

        return dp[:numRows]