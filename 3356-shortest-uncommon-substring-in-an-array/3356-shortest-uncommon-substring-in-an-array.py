class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word_ids = set()

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
                curr.word_ids.add(word_id)
    
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

                if curr.word_ids == {word_id}: # unique
                    if (best == "" or len(substring) < len(best) or (len(substring) == len(best) and substring < best)):
                        best = substring
                    break

        return best

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        trie = Trie()

        for i, word in enumerate(arr):
            trie.insert(word, i)
        
        res = []
        for i, word in enumerate(arr):
            shortest = trie.find(word, i)
            res.append(shortest)
        
        return res