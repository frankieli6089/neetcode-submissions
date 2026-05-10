class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_size = len(s1)
        s2_size = len(s2)

        if s1_size > s2_size:
            return False

        s1_count = 26 * [0]
        window_count = [0] * 26
        for i in range(s1_size):
            s1_count[ord(s1[i]) - 97] += 1
            window_count[ord(s2[i]) - 97] += 1

        if s1_count == window_count:
            return True
        
        l = 0
        for r in range(s1_size, s2_size):
            window_count[ord(s2[r]) - ord('a')] += 1
            window_count[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if s1_count == window_count:
                return True
        return False