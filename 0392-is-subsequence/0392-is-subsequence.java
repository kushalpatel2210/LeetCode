class Solution {
    public boolean isSubsequence(String s, String t) {
        int lengthofs = s.length();
        int lengthoft = t.length();
        int currentIndexofs = 0;
        int currentIndexoft = 0;
        
        while (currentIndexoft < lengthoft && currentIndexofs < lengthofs) {
            if(s.charAt(currentIndexofs) == t.charAt(currentIndexoft)) {
                currentIndexofs++;
            }

            currentIndexoft++;
        }

        return currentIndexofs == lengthofs;
    }
}

/*
// Solution 2
class Solution {
    public boolean isSubsequence(String s, String t) {
        int currentIndexoft = 0;
        int currentIndexofs = 0;

        for (int i = 0; i < s.length(); i++) {
            Character cs = s.charAt(currentIndexofs);

            while(currentIndexoft < t.length()) {
                if (cs == t.charAt(currentIndexoft)) {
                    currentIndexoft++;
                    currentIndexofs++;
                    break;
                }
                currentIndexoft++;
            }
        }

        return currentIndexofs == s.length();
    }
}
*/