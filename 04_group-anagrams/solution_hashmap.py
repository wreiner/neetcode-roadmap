class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        # loop over words, sort words, put words into hashmap with sorted order as key
        for word in strs:
            sorted_word = "".join(sorted(word))
            if not sorted_word in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)

        return anagrams.values()

