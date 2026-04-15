class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            length = str(len(word))
            encoded += length + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        n = len(s)
        i = 0
        while i < n:
            hash_index = s.index('#', i)
            length = int(s[i:hash_index])
            start_index = hash_index + 1
            word = ""
            for j in range(start_index, start_index + length):
                word += s[j]
            result.append(word)
            i = start_index + length
        return result

                