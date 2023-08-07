class RandomizedSet {

    private Random random;
    private HashMap map;
    private List<Integer> list;

    public RandomizedSet() {
        random = new Random();
        map = new HashMap<>();
        list = new ArrayList<Integer>();
    }
    
    public boolean insert(int val) {
        if(!map.containsKey(val)){
            list.add(val);
            map.put(val, list.size() - 1);
            return true;
        }
        return false;
        
    }
    
    public boolean remove(int val) {
        int lastIndex = (int) map.getOrDefault(val, -1);
        if(lastIndex == -1){
            return false;
        }
        Collections.swap(list, lastIndex, list.size() - 1);
        int otherSwapedValue = list.get(lastIndex);
        map.put(otherSwapedValue, lastIndex);
        list.remove(list.size() - 1);
        map.remove(val);
        return true;
    }
    
    public int getRandom() {
        int randomIndex = random.nextInt(list.size());
        return list.get(randomIndex);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */