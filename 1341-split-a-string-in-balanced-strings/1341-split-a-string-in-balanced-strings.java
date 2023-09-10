class Solution {
    public int balancedStringSplit(String s) {
        int balancedCount = 0, lCount = 0, rCount = 0;
        for(char c: s.toCharArray()){
            if (c == 'R') {
                rCount++;
            }

            if (c == 'L') {
                lCount++;
            }

            if (lCount == rCount) {
                balancedCount++;
                lCount = 0;
                rCount = 0;
            }
        }

        return balancedCount;
    }
}