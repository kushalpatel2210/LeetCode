class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int totalGas = Arrays.stream(gas).sum();
        int totalCost = Arrays.stream(cost).sum();
        int result = 0;
        int gasTank = 0;

        if (totalCost > totalGas) {
            return -1;
        }

        for(int i = 0; i < gas.length; i++) {
            gasTank += (gas[i] - cost[i]);

            if (gasTank < 0) {
                gasTank = 0;
                result = i + 1;
            }
        }

        return result;
    }
}