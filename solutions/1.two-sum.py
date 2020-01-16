#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start


import itertools
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for (i, x), (j, y) in itertools.combinations(enumerate(nums), 2):
            if x + y == target:
                return [i, j]


# @lc code=end
