class Solution {
    public int maximumWealth(int[][] accounts) {
        int max = 0;
        for (int row = 0; row < accounts.length; row++) {
            int customer_wealth = 0;
            for (int col = 0; col < accounts[row].length; col++) {
                customer_wealth += accounts[row][col];
            }
            if (customer_wealth > max)
            {
                max = customer_wealth;
            }
        }
        return max;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] accounts = {{1,2,3}, {3,2,1}};
        System.out.println(solution.maximumWealth(accounts));
        int[][] accounts2 = {{1,5}, {7,3}, {3,5}};
        System.out.println(solution.maximumWealth(accounts2));
    }
}
