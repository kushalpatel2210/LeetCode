class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
        int[] result = new int[2];
        int iterator = 0;

        for(int i=0; i<nums.length ; i++){
            if(!hashMap.containsKey(nums[i])){
                hashMap.put(nums[i], i);
            } else {
                if(target == nums[i] + nums[i]){
                    result[0] = hashMap.get(nums[i]);
                    result[1] = iterator;
                    return result;
                }
            }
            iterator ++;
        }

        System.out.println(hashMap);

        for(Map.Entry<Integer,Integer> entry: hashMap.entrySet()) {
            int currentElement = entry.getKey();
            int desiredElement = target - currentElement;
            if(hashMap.containsKey(desiredElement)){
                    System.out.println(hashMap);
                    result[0] = hashMap.get(currentElement);
                    result[1] = hashMap.get(target - currentElement);
                    break;
            }       
        }

        return result;
    }
}