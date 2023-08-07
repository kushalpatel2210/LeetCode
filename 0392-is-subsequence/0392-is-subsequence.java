class Solution {
    public boolean isSubsequence(String s, String t) {
        int sPointer = 0, tPointer = 0;

        if (s.length() == 0) {
            return true;
        }

        if (t.length() == 0) {
            return false;
        }

        while(sPointer < s.length() && tPointer < t.length()) {
            Character sChar = s.charAt(sPointer);
            Character tChar = t.charAt(tPointer);

            if (!tChar.equals(sChar)) {
                tPointer++;
            } else {
                sPointer++;
                tPointer++;
            }
        }

        if(sPointer == s.length()) {
            return true;
        } else {
            return false;
        }
    }
}