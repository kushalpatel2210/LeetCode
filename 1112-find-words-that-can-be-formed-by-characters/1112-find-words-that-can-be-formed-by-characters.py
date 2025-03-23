from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        counterChars = Counter(chars)

        for word in words:
            counterWords = Counter(word)
            canFormWord = True

            for val, freq in counterWords.items():
                if val not in counterChars or freq > counterChars[val]:
                    canFormWord = False
            
            if canFormWord:
                res += len(word)

        return res