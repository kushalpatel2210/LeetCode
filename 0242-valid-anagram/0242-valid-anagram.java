class Solution {
    public boolean isAnagram(String s, String t) {
        char[] s_array = new char[s.length()];
        char[] t_array = new char[t.length()];

        for(int i = 0; i < s.length(); i++) {
            s_array[i] = s.charAt(i);
        }

        for(int i = 0; i < t.length(); i++) {
            t_array[i] = t.charAt(i);
        }
        
        Arrays.sort(s_array);
        Arrays.sort(t_array);

        return Arrays.equals(s_array, t_array);
    }
}