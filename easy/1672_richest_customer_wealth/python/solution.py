class Solution(object):
    def maximumWealth(self, accounts):
        max = 0
        for row in range(len(accounts)):
            customer_wealth = 0
            for col in range(len(accounts[0])):
                customer_wealth += accounts[row][col]
            if customer_wealth > max:
                max = customer_wealth
        return max


if __name__ == '__main__':
    solution = Solution()
    accounts = [[1,2,3], [3,2,1]]
    print(solution.maximumWealth(accounts))
    accounts2 = [[1,5], [7,3], [3,5]]
    print(solution.maximumWealth(accounts2))
