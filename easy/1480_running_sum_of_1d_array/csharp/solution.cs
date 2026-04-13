class Solution{
    public int[] running_sum (int[] nums)
    {
        int[] result = [];
        int sum = 0;
        for (int i = 0; i<nums.Count; i++)
        {
            sum += nums[i];
            result.Add(sum);
        }
        return result;
    }
}

class Program {
    static void Main(string[] args) {
        Solution solution = new Solution();
        List<int> nums = [1,2,3,4];
        Console.WriteLine(string.Join(", ", solution.running_sum(nums)));
    }
}