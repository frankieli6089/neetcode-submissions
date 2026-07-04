import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = 26 * [0]
        for task in tasks:
            freq[int(ord(task)) - 65] += 1

        maxHeap = []
        for i in freq:
            if i > 0:
                heapq.heappush_max(maxHeap, i)

        q = deque()
        time = 0
        while maxHeap or q:
            time += 1

            if maxHeap:
                count = heapq.heappop_max(maxHeap)
                count -= 1

                if count > 0:
                    q.append((count, time + n))

            if q and q[0][1] == time:
                count, _ = q.popleft()
                heapq.heappush_max(maxHeap, count)

        return time
                                                    
    
