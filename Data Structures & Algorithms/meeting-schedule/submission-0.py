"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)
        last_end_time = 0
        for interval in intervals:
            if interval.start < last_end_time:
                return False
            else:
                last_end_time = interval.end
        
        return True
