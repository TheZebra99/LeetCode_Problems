class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): #start at i+1 to avoid duplication
                if (nums[i] + nums[j]) == target:
                    return [i,j]

if __name__ == '__main__':
    test = Solution()
    nums = [2,7,11,15]
    target = 9
    print(test.twoSum(nums, target))