class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        most_freq_count = 0
        l = 0
        longest_repeating_char = 0
        
        for r in range(len(s)):
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            most_freq_count = max(most_freq_count, freq_map[s[r]])
            
            # If the number of characters to replace (window length - most freq count) exceeds k
            if (r - l + 1) - most_freq_count > k:
                freq_map[s[l]] -= 1
                l += 1
            
            longest_repeating_char = max(longest_repeating_char, r - l + 1)

        return longest_repeating_char