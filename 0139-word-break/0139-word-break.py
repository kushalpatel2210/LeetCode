class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordSet:
                if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                    if dp[i + len(word)]:
                        dp[i] = True
                        break
        
        return dp[0]