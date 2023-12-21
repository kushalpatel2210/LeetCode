class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> listOfResults = new ArrayList<Boolean>();
        int maxNoOfcandies = 0;

        for (int candy : candies) {
            maxNoOfcandies = Math.max(candy, maxNoOfcandies);
        }

        for (int candy : candies) {
            listOfResults.add(candy + extraCandies >= maxNoOfcandies);  
        }
        return listOfResults;
    }
}