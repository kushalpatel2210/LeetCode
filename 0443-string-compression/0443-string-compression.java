class Solution {
    public int compress(char[] chars) {
        int charsLength = chars.length;
        int res = 0;

        for (int i = 0; i < charsLength; i++) {
            Character current = chars[i];
            int currentCharLength = 1;

            while (i + 1 < charsLength && chars[i + 1] == current) {
                currentCharLength++;
                i++; 
            }

            chars[res++] = current;

            if (currentCharLength > 1) {
                for (char c : Integer.toString(currentCharLength).toCharArray()){
                    chars[res++] = c;
                }
            }
        }

        return res;
    }
}