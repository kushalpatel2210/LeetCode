class Solution {
    public boolean wordPattern(String pattern, String s) {
        HashMap<Character, Integer> map_patterm = new HashMap<>();
        HashMap<String, Integer> map_s = new HashMap<>();
        String[] words = s.split(" ");
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        int i = 0;

        for(char c: pattern.toCharArray()) {
            if(!map_patterm.containsKey(c)) {
                map_patterm.put(c, i);
            }

            sb1.append(Integer.toString(map_patterm.get(c)));
            sb1.append(" ");
            i++;
        }

        for(int k = 0; k < words.length; k++) {
            if(!map_s.containsKey(words[k])) {
                map_s.put(words[k], k);
            }

            sb2.append(Integer.toString(map_s.get(words[k])));
            sb2.append(" ");
        }

        return sb1.toString().equals(sb2.toString());
    }
}