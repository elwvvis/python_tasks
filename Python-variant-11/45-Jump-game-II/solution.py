class Solution(object):
    def jump(self, nums):
        jumps = 0
        end = 0
        distant = 0
        for i in range(len(nums) - 1):
            distant = max(distant, i + nums[i])

            if i == end:
                jumps += 1
                end = distant

        return jumps
        