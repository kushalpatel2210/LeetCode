class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);  // Sort the array in non-decreasing order
        int n = citations.length;
        
        for (int i = 0; i < n; i++) {
            if (citations[i] >= n - i) {
                return n - i;
            }
        }
        
        return 0;
    }
}

/*      
        -------------- My Own Solution ----------------
        HashMap<Integer, Integer> map = new HashMap<>();
        int n = citations.length;
        int hIndex = 0;

        Arrays.sort(citations);

        for(int i = 0; i < n; i++) {
            if (map.containsKey(citations[i]) || citations[i] == 0) {
               continue;
            } 
            map.put(Math.min(citations[i], n - i), n - i);
        }   
        
        if (map.isEmpty()) {
            return 0;
        } else {
            for(Map.Entry<Integer, Integer> entry: map.entrySet()) {
                if(entry.getValue() >= entry.getKey()) {
                    hIndex = entry.getKey();
                }
            }
        }

        return hIndex;
*/