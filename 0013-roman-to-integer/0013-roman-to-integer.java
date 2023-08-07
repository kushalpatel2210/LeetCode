class Solution {
    public int romanToInt(String s) {
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        int output = 0;
        map.put("I", 1);
        map.put("V", 5);
        map.put("X", 10);
        map.put("L", 50);
        map.put("C", 100);
        map.put("D", 500);
        map.put("M", 1000);

        for(int i = 0; i < s.length(); i++){
            String currentChar = Character.toString(s.charAt(i));
            String nextChar = i < (s.length() - 1) ? Character.toString(s.charAt(i+1)) : null;
            if(nextChar != null) {
                if(map.get(currentChar) >= map.get(nextChar)){
                    output += map.get(currentChar);
                } else {
                    output -= map.get(currentChar);
                }
            } else{
                output += map.get(currentChar);
            }  
        }

        return output;
    }
}