class Solution:
    def reverseWords(self, s: str) -> str:
        wordsList = s.split()
        wordsList.reverse()
        return ' '.join(wordsList)