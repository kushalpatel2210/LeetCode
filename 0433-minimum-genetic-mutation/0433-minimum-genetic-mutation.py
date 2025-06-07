from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankSet = set(bank) # for fast lookup
        q = deque([(startGene, 0)])
        mutationMap = {
            'A': 'TCG',
            'T': 'ACG',
            'C': 'ATG',
            'G': 'ATC'
        }       

        while q:
            currGene, count = q.popleft()

            if currGene == endGene:
                return count
            
            for i, gene in enumerate(currGene):
                for mutation in mutationMap[gene]:
                    nextGene = currGene[:i] + mutation + currGene[i + 1:]

                    if nextGene in bankSet:
                        q.append((nextGene, count + 1))
                        bankSet.remove(nextGene)
            
        return -1
