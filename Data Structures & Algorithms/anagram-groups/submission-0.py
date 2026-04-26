class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        word_groups = {}
        for word in strs:
            anagram_count = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                anagram_count[index] += 1
            word_key = tuple(anagram_count)

            if word_key in word_groups:
                word_groups[word_key].append(word)
            else:
                word_groups[word_key] = [word]

        res = []
        for value in word_groups.values():
            res.append(value)

        return res
