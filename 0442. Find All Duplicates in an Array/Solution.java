class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        int n = nums.length;
        boolean[] a = new boolean[n];
        List<Integer> l = new ArrayList<>();
        for (int i : nums) {
            if (a[i-1]) {
                l.add(i);
            } else {
                a[i-1] = true;
            }
        }
        return l;
    }
}