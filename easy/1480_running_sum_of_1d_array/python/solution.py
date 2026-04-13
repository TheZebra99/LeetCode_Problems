class Solution(object):
    def running_sum(self, nums):
        result = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            result.append(sum)
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,4]
    print(solution.running_sum(nums))
    nums2 = [1,1,1,1,1]
    print(solution.running_sum(nums2))
    nums3 = [3,1,2,10,1]
    print(solution.running_sum(nums3))
