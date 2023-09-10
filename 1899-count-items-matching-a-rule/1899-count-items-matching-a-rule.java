class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int count = 0;
        Map<String, Integer> ruleMapping = new HashMap<>();
        ruleMapping.put("type", 0);
        ruleMapping.put("color", 1);
        ruleMapping.put("name", 2);

        for (int i = 0; i < items.size(); i++) {
            List<String> item = items.get(i);
            if (ruleValue.equals(item.get(ruleMapping.get(ruleKey)))) {
                count++;
            }
        }

        return count;
    }
}