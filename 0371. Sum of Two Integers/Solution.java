public class Solution {
    public int getSum(int a, int b) {
        int t;
        while(b!=0){
            t = a & b;
            a ^= b;
            b = t << 1;
        }
        return a;
    }
}