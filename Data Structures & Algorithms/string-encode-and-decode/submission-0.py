class Solution:

    def encode(self, strs: List[str]) -> str:
        numbered_strs_with_indicator = []
        for word in strs:
            str_len = len(word)
            parts = [str(str_len), "#", word]
            s = "".join(parts)
            numbered_strs_with_indicator.append(s)
        numbered_strs_with_indicator = "".join(numbered_strs_with_indicator)
        return numbered_strs_with_indicator

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            word = s[i:i+length]
            result.append(word)
            i = i + length

        return result
    