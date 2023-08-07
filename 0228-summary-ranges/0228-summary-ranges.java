class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> ranges = new ArrayList<>();
        int n = nums.length;

        if (n == 1) {
            ranges.add(nums[n - 1] + "");
            return ranges;
        }
        for (int i = 0; i < n; i ++) {
            int start = nums[i];

            while (i + 1 < n && nums[i + 1] - nums[i] == 1) {
                i++;
            }

            if (nums[i] != start) {
                ranges.add(start + "->" + nums[i]);
            } else {
                ranges.add(start + "");
            }
        }
        return ranges;
    }
}