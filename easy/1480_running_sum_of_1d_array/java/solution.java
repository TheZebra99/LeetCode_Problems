import java.util.Arrays;

class solution {
    public int[] runningSum (int[] nums)
    {
        int[] result = new int[nums.length];
        int sum = 0;
        for (int i = 0; i< nums.length; i++)
        {
            sum += nums[i];
            result[i] = sum;
        }
        return result;
    }

    public static void main(String[] args) {
        solution solution = new solution();
        int[] nums = {1,2,3,4};
        System.out.println(Arrays.toString(solution.runningSum(nums)));
    }
}
