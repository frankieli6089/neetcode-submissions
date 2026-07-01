import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        max_heap = stones
        while len(max_heap) > 1:
            x = heapq.heappop_max(max_heap)
            y = heapq.heappop_max(max_heap)

            if x == y:
                continue
            elif x < y:
                y = y - x
                heapq.heappush_max(max_heap, y)
            else:
                x = x - y
                heapq.heappush_max(max_heap, x)

        if max_heap:
            return max_heap[0]
        else:
            return 0