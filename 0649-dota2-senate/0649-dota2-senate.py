from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()

        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            r_turn = radiant.popleft()
            d_turn = dire.popleft()

            if r_turn < d_turn:
                radiant.append(r_turn + len(senate))
            else:
                dire.append(d_turn + len(senate))
        
        return "Radiant" if radiant else "Dire"
