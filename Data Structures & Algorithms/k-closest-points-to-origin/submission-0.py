import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        heapq.heapify_max(max_heap)

        for coords in points:
            x1 = coords[0]
            y1 = coords[1]
            distance = x1**2 + (y1)**2
            if len(max_heap) < k:
                heapq.heappush_max(max_heap, (distance, coords))
            else:
                peek = max_heap[0][0]
                if peek > distance:
                    heapq.heappop_max(max_heap)
                    heapq.heappush_max(max_heap, (distance, coords))
                else:
                    continue
        res = []
        for i in max_heap:
            res.append(i[1])
        return res
                
                
            
        