class Solution {
    public int[] twoSum(int[] numbers, int target) {
       HashMap<Integer, Integer> map = new HashMap<>();
       int[] resultingArray = new int[2];

       for(int i = 0; i < numbers.length; i ++) {
           int currentElement = numbers[i];
           int difference = target - currentElement;

           if(!map.containsKey(difference)) {
               map.put(currentElement, i);
           } else {
               return new int[] {map.get(difference) + 1, i + 1};
           }
       }
       
       return resultingArray;
    }
}