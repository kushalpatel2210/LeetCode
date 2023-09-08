class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int jewelsInStone = 0;
        List<Character> jewelsList = jewels.chars()
                                        .mapToObj(e -> (char)e)
                                        .collect(Collectors.toList());

        for (int i = 0; i < stones.length(); i++) {
            if (jewelsList.contains(stones.charAt(i))) {
                jewelsInStone++;
            }
        }

        return jewelsInStone;
    }
}