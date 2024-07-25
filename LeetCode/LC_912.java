//Om Namah Shivaya
import java.util.*;
class Solution {
    public int[] sortArray(int[] nums) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i:nums){
            pq.add(i);
        }
        int[] ans = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            ans[i] = pq.remove();
        }
        return ans;
    }
}