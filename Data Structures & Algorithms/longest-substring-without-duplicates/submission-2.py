class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 'y' < 'z' = True
        max_substring_len = 0
        l = 0
        charset = set()

        for r in range(len(s)):
            if s[r] in charset:
                while s[r] in charset:
                    charset.remove(s[l])
                    l+=1
            if (r-l+1) > max_substring_len:
                max_substring_len = (r-l+1)
            
            charset.add(s[r])


        return max_substring_len
 

        