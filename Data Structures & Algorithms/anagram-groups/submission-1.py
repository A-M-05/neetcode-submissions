class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for s in strs:
            counts = self.countFrequency(s)
            if counts in anagrams:
                anagrams[counts].append(s)
            else:
                anagrams[counts] = [s]
        
        return list(anagrams.values())

    def countFrequency(self, s: str) -> tuple:
        counts = list(0 for _ in range(0, 26))
        for c in s:
            counts[ord(c) - ord('a')] += 1
        
        return tuple(counts)
