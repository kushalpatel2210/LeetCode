class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words_id = set()

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, word_id):
        n = len(word)

        for i in range(n):
            curr = self.root
            for j in range(i, n):
                ch = word[j]
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
                curr.words_id.add(word_id)
    
    def find(self, word, word_id):
        n = len(word)

        best = ""
        for i in range(n):
            curr = self.root
            substring = ""
            for j in range(i, n):
                ch = word[j]

                if ch not in curr.children:
                    break
                
                curr = curr.children[ch]
                substring += ch

                if curr.words_id == {word_id}: # unique
                    if (best == "" or len(substring) < len(best) or (len(substring) == len(best) and substring < best)):
                        best = substring
                    break # once we find the word no need to go in-depth as length of word will always be higher
        
        return best

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        trie = Trie()

        for idx, word in enumerate(arr):
            trie.insert(word, idx)

        result = []
        for idx, word in enumerate(arr):
            result.append(trie.find(word, idx))
        
        return result