class Solution {
    public String restoreString(String s, int[] indices) {
        char[] restoreString = new char[s.length()];
        
        for (int i = 0; i < indices.length; i++) {
            restoreString[indices[i]] = s.charAt(i);
        }

        return new String(restoreString);
    }
}