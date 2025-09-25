class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0  # number of distinct words containing this substring


class Solution:
    def buildTrie(self, arr):
        root = TrieNode()
        for word in arr:
            visited_nodes = set()  # track nodes visited for this word
            n = len(word)
            for i in range(n):
                node = root
                for j in range(i, n):
                    ch = word[j]
                    if ch not in node.children:
                        node.children[ch] = TrieNode()
                    node = node.children[ch]

                    # increment count only once per word per node
                    if node not in visited_nodes:
                        node.count += 1
                        visited_nodes.add(node)
        return root

    def findUniqueSubstring(self, word, root):
        n = len(word)
        best = None
        for i in range(n):
            node = root
            substring = ""
            for j in range(i, n):
                ch = word[j]
                if ch not in node.children:
                    break
                node = node.children[ch]
                substring += ch
                if node.count == 1:  # unique substring found
                    if best is None or len(substring) < len(best) or \
                       (len(substring) == len(best) and substring < best):
                        best = substring
                    break
        return best if best else ""

    def shortestSubstrings(self, arr):
        root = self.buildTrie(arr)
        return [self.findUniqueSubstring(word, root) for word in arr]