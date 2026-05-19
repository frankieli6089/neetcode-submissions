class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = 1
        size = len(piles)
        for i in range(size):
            if piles[i] > high:
                high = piles[i]
        answer = 1
        low = 1
        while low <= high:
            mid = ((high - low) // 2 ) + low 
            h_count = 0
            for i in range(size):
                h_count += piles[i] // mid
                if piles[i] % mid != 0:
                    h_count += 1

            if h_count <= h:
                high = mid - 1
                answer = mid
            else:
                low = mid + 1

        return answer
            
                

