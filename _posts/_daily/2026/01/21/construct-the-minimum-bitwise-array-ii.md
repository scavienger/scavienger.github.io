---
layout: post
title: "Construct the Minimum Bitwise Array II"
date: 2026-01-21 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Bit Manipulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    std::vector<int> minBitwiseArray(std::vector<int>&\
        \ nums) {\n        std::vector<int> ans;\n        for (int num : nums) {\n \
        \           if (num % 2 == 0) {\n                ans.push_back(-1);\n      \
        \      } else {\n                int m = 0;\n                int temp_num =\
        \ num;\n                while ((temp_num & 1) == 1) {\n                    m++;\n\
        \                    temp_num >>= 1;\n                }\n                ans.push_back(num\
        \ ^ (1 << (m - 1)));\n            }\n        }\n        return ans;\n    }\n\
        };"
      java: "import java.util.List;\nimport java.util.ArrayList;\n\nclass Solution {\n\
        \    public int[] minBitwiseArray(List<Integer> nums) {\n        int[] ans =\
        \ new int[nums.size()];\n        for (int i = 0; i < nums.size(); i++) {\n \
        \           int num = nums.get(i);\n            if (num % 2 == 0) {\n      \
        \          ans[i] = -1;\n            } else {\n                int m = 0;\n\
        \                int temp_num = num;\n                while ((temp_num & 1)\
        \ == 1) {\n                    m++;\n                    temp_num >>= 1;\n \
        \               }\n                ans[i] = num ^ (1 << (m - 1));\n        \
        \    }\n        }\n        return ans;\n    }\n}"
      python: "# Failed to parse response\n# Check logs for full output.\n# Full Response:\n\
        '''\n{\n  \"approach\": \"The core of this problem lies in understanding the\
        \ bitwise OR operation between an integer `x` and `x + 1`. When `x` is represented\
        \ in binary, `x + 1` flips the rightmost zero bit of `x` to one, and all subsequent\
        \ one bits to its right become zero. For example, if `x = A01...1` (where 'A'\
        \ is a prefix, '0' is the rightmost zero at bit position `k`, and there are\
        \ `k` ones to its right), then `x + 1 = A10...0`. Performing `x OR (x + 1)`\
        \ results in `A11...1`, meaning all bits from position `0` up to and including\
        \ position `k` are set to `1`, while bits to the left of `k` remain unchanged\
        \ from `x` (and `x+1`). This implies that for `ans[i] OR (ans[i] + 1)` to equal\
        \ `nums[i]`, `nums[i]` must have all its bits set from the least significant\
        \ bit up to the position of the rightmost zero in `ans[i]`. Consequently, `nums[i]`\
        \ must be an odd number, as `A11...1` always ends with a `1`. If `nums[i]` is\
        \ even, no solution exists, and `ans[i]` is -1.\",\n  \"time_complexity\": \"\
        The time complexity is O(N * log(max(nums[i]))), where N is the length of the\
        \ `nums` array. For each number in `nums`, we perform a constant number of bitwise\
        \ operations and a loop to find the highest set bit, which takes logarithmic\
        \ time with respect to the value of `nums[i]` (up to 30-31 bits for 10^9).\"\
        ,\n  \"space_complexity\": \"The space complexity is O(N) to store the `ans`\
        \ array. No additional significant space is used beyond the output array.\"\
        ,\n  \"solutions\": {\n    \"kotlin\": \"class Solution {\\n    fun minBitwiseArray(nums:\
        \ List<Int>): IntArray {\\n        val ans = IntArray(nums.size)\\n        for\
        \ (i in nums.indices) {\\n            val n = nums[i]\\n            if (n %\
        \ 2 == 0) {\\n                ans[i] = -1\\n            } else {\\n        \
        \        // Find the highest set bit position\\n                var highestBitPos\
        \ = 0\\n                for (j in 30 downTo 0) { // Max 10^9 is less than 2^30\\\
        n                    if ((n shr j) and 1 == 1) {\\n                        highestBitPos\
        \ = j\\n                        break\\n                    }\\n           \
        \     }\\n                \\n                // The target x must have all bits\
        \ from 0 to highestBitPos-1 unset\\n                // and the highestBitPos\
        \ bit unset, to become N when OR-ed with x+1\\n                // This means\
        \ x should be N XOR (2^k - 1) where k is the position of the rightmost 0 in\
        \ x\\n                // Or, more simply, x = N ^ (N & (N-1))\\n           \
        \     // This is equivalent to x = N ^ (1 << (position of rightmost 0 in N))\\\
        n                // No, this is not correct. Let's use the property: x OR (x+1)\
        \ = N\\n                // The smallest x is N XOR (1 << k) where k is the position\
        \ of the rightmost 0 in N-1\\n                // This is equivalent to x = N\
        \ - (N & (N-1))\\n                // Let's re-derive: x OR (x+1) = N. We want\
        \ smallest x.\\n                // If x = A01...1 (k ones), then x+1 = A10...0,\
        \ and N = A11...1 (k+1 ones).\\n                // So N must be of the form\
        \ (prefix)11...1. If N has a 0 in its lower bits, it's impossible.\\n      \
        \          // Example: N=5 (101). Highest bit is 2. Rightmost 0 is at bit 1.\\\
        n                // If x=4 (100), x+1=5 (101). 4 OR 5 = 5. Correct.\\n     \
        \           // Example: N=7 (111). Highest bit is 2. No 0s in lower bits.\\\
        n                // If x=3 (011), x+1=4 (100). 3 OR 4 = 7. Correct.\\n     \
        \           // The value of x is N XOR (1 << k) where k is the position of the\
        \ rightmost 0 in N-1.\\n                // This is equivalent to N - (N & (N-1)).\\\
        n                // N & (N-1) clears the LSB of N. So N - (N & (N-1)) is N -\
        \ (LSB of N).\\n                // This is N - (N & -N).\\n                //\
        \ Let's test this: N=5 (101). N & -N = 1 (001). N - (N & -N) = 5 - 1 = 4. Correct.\\\
        n                // N=7 (111). N & -N = 1 (001). N - (N & -N) = 7 - 1 = 6. Incorrect.\
        \ Expected 3.\\n                // The logic for N & -N is for finding the LSB.\
        \ This is not what we want.\\n                \\n                // The property\
        \ is that N must be of the form (prefix)11...1. If N has a 0 bit at position\
        \ j\\n                // and there is a 1 bit at position j+1, then it's impossible.\\\
        n                // For example, N=5 (101). It has 0 at bit 1. This means x\
        \ cannot have its rightmost 0 at bit 1.\\n                // If x has its rightmost\
        \ 0 at bit k, then N must have all bits from 0 to k set to 1.\\n           \
        \     // So, if N has a 0 at bit j, then k must be > j.\\n                //\
        \ This means x must be N with some trailing 1s flipped to 0s.\\n           \
        \     // Specifically, x = N XOR (1 << (k+1) - 1) where k is the position of\
        \ the rightmost 0 in x.\\n                // This is equivalent to x = N ^ (N\
        \ & (N-1)).\\n                // Let's re-examine the examples:\\n         \
        \       // N=3 (011). x=1 (001). 1 OR 2 = 3. N & (N-1) = 3 & 2 = 2. N ^ (N &\
        \ (N-1)) = 3 ^ 2 = 1. Correct.\\n                // N=5 (101). x=4 (100). 4\
        \ OR 5 = 5. N & (N-1) = 5 & 4 = 4. N ^ (N & (N-1)) = 5 ^ 4 = 1. Incorrect. Expected\
        \ 4.\\n                // N=7 (111). x=3 (011). 3 OR 4 = 7. N & (N-1) = 7 &\
        \ 6 = 6. N ^ (N & (N-1)) = 7 ^ 6 = 1. Incorrect. Expected 3.\\n            \
        \    \\n                // The correct approach is: find the highest bit `msb`\
        \ of `N`. Let `mask = (1 << (msb + 1)) - 1`. This is `2^(msb+1) - 1` (all ones\
        \ up to `msb`).\\n                // If `N` is not equal to `mask`, then `N`\
        \ has a zero bit somewhere below `msb`. In this case, `ans[i]` is -1.\\n   \
        \             // Example: N=5 (101). msb=2. mask = (1 << 3) - 1 = 7 (111). 5\
        \ != 7. So ans[i] should be -1. But example says 4.\\n                // This\
        \ means my understanding of the `A11...1` form is flawed or incomplete.\\n \
        \               \\n                // Let's re-check the property: `x OR (x+1)\
        \ = N`\\n                // `x` and `x+1` differ at the rightmost `0` bit of\
        \ `x` and all bits to its right.\\n                // If `x` ends with `01...1`\
        \ (k ones), then `x+1` ends with `10...0` (k zeros).\\n                // `x\
        \ OR (x+1)` will have `k+1` ones at the end.\\n                // So `N` must\
        \ have its `k+1` least significant bits set to `1`.\\n                // If\
        \ `N` has a `0` at bit position `j`, then `x` must also have a `0` at bit position\
        \ `j`.\\n                // And `x+1` must also have a `0` at bit position `j`.\\\
        n                // This means `j` cannot be the position of the rightmost `0`\
        \ in `x`.\\n                // So, if `N` has a `0` at bit `j`, then `x` must\
        \ have `0` at bit `j`, and its rightmost `0` must be at a position `k > j`.\\\
        n                // This implies that `x` must be `N` with some trailing `1`s\
        \ unset.\\n                // To minimize `x`, we want to unset as few bits\
        \ as possible, and from the rightmost positions.\\n                // Consider\
        \ `N`. Find the highest bit `msb_N` of `N`.\\n                // The result\
        \ `x OR (x+1)` will have its highest bit at `msb_N`.\\n                // This\
        \ means `x` must have its highest bit at `msb_N` or `msb_N - 1`.\\n        \
        \        // If `x` has its highest bit at `msb_N`, then `x` must be `N` with\
        \ some trailing bits unset.\\n                // If `x` has its highest bit\
        \ at `msb_N - 1`, then `x+1` must have its highest bit at `msb_N`.\\n      \
        \          // This happens when `x = (1 << msb_N) - 1`. Then `x+1 = (1 << msb_N)`.\
        \ `x OR (x+1) = (1 << (msb_N + 1)) - 1`.\\n                // This is the case\
        \ for N = 3, 7, 15, 31, etc. Here x = (N-1)/2.\\n                // For N=3\
        \ (011), msb_N=1. x=(3-1)/2=1. Correct.\\n                // For N=7 (111),\
        \ msb_N=2. x=(7-1)/2=3. Correct.\\n                \\n                // What\
        \ if N is not `2^k - 1`?\\n                // N=5 (101). msb_N=2. `x` must be\
        \ 4 (100). `4 OR 5 = 5`. This works.\\n                // N=11 (1011). msb_N=3.\
        \ `x` must\n'''"
      python3: "class Solution:\n    def minBitwiseArray(self, nums: List[int]) -> List[int]:\n\
        \        ans = []\n        for num in nums:\n            if num % 2 == 0:\n\
        \                ans.append(-1)\n            else:\n                m = 0\n\
        \                temp_num = num\n                while (temp_num & 1) == 1:\n\
        \                    m += 1\n                    temp_num >>= 1\n          \
        \      ans.append(num ^ (1 << (m - 1)))\n        return ans"
      c: "#include <stdlib.h> // For malloc\n\n/**\n * Note: The returned array must\
        \ be malloced, assume caller calls free().\n */\nint* minBitwiseArray(int* nums,\
        \ int numsSize, int* returnSize) {\n    int* ans = (int*)malloc(numsSize * sizeof(int));\n\
        \    *returnSize = numsSize;\n\n    for (int i = 0; i < numsSize; i++) {\n \
        \       int num = nums[i];\n        if (num % 2 == 0) {\n            ans[i]\
        \ = -1;\n        } else {\n            int m = 0;\n            int temp_num\
        \ = num;\n            while ((temp_num & 1) == 1) {\n                m++;\n\
        \                temp_num >>= 1;\n            }\n            ans[i] = num ^\
        \ (1 << (m - 1));\n        }\n    }\n    return ans;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int[] MinBitwiseArray(IList<int> nums) {\n        int[] ans\
        \ = new int[nums.Count];\n        for (int i = 0; i < nums.Count; i++) {\n \
        \           int num = nums[i];\n            if (num % 2 == 0) {\n          \
        \      ans[i] = -1;\n            } else {\n                int m = 0;\n    \
        \            int temp_num = num;\n                while ((temp_num & 1) == 1)\
        \ {\n                    m++;\n                    temp_num >>= 1;\n       \
        \         }\n                ans[i] = num ^ (1 << (m - 1));\n            }\n\
        \        }\n        return ans;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number[]}\n */\nvar minBitwiseArray\
        \ = function(nums) {\n    const ans = [];\n    for (let i = 0; i < nums.length;\
        \ i++) {\n        const num = nums[i];\n        if (num % 2 === 0) {\n     \
        \       ans.push(-1);\n        } else {\n            let m = 0;\n          \
        \  let temp_num = num;\n            while ((temp_num & 1) === 1) {\n       \
        \         m++;\n                temp_num >>= 1;\n            }\n           \
        \ ans.push(num ^ (1 << (m - 1)));\n        }\n    }\n    return ans;\n};"
      typescript: "function minBitwiseArray(nums: number[]): number[] {\n    const ans:\
        \ number[] = [];\n    for (let i = 0; i < nums.length; i++) {\n        const\
        \ num = nums[i];\n        if (num % 2 === 0) {\n            ans.push(-1);\n\
        \        } else {\n            let m = 0;\n            let temp_num = num;\n\
        \            while ((temp_num & 1) === 1) {\n                m++;\n        \
        \        temp_num >>= 1;\n            }\n            ans.push(num ^ (1 << (m\
        \ - 1)));\n        }\n    }\n    return ans;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer[]\n     */\n    function minBitwiseArray($nums) {\n        $ans =\
        \ [];\n        foreach ($nums as $num) {\n            if ($num % 2 == 0) {\n\
        \                $ans[] = -1;\n            } else {\n                $m = 0;\n\
        \                $temp_num = $num;\n                while (($temp_num & 1) ==\
        \ 1) {\n                    $m++;\n                    $temp_num >>= 1;\n  \
        \              }\n                $ans[] = $num ^ (1 << ($m - 1));\n       \
        \     }\n        }\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func minBitwiseArray(_ nums: [Int]) -> [Int] {\n\
        \        var ans: [Int] = []\n        for num in nums {\n            if num\
        \ % 2 == 0 {\n                ans.append(-1)\n            } else {\n       \
        \         var m = 0\n                var temp_num = num\n                while\
        \ (temp_num & 1) == 1 {\n                    m += 1\n                    temp_num\
        \ >>= 1\n                }\n                ans.append(num ^ (1 << (m - 1)))\n\
        \            }\n        }\n        return ans\n    }\n}"
    approach: 'The problem asks us to find the minimum ans[i] such that ans[i] OR (ans[i]
      + 1) == nums[i]. We begin by analyzing the bitwise operation x OR (x + 1). If
      x is an even number, its binary representation ends with a ''0''. Then x + 1 ends
      with a ''1''. The bitwise OR x OR (x + 1) will result in x + 1. Since x + 1 is
      always odd, if nums[i] is an even number, no such x can exist that satisfies the
      condition, so ans[i] must be -1. This covers cases like nums[i] = 2.


      If nums[i] is an odd number, we need to find the minimum x. The operation x OR
      (x + 1) effectively finds the rightmost ''0'' bit of x (at position k), flips
      it to ''1'', and keeps all bits to its right (which were already ''1''s) as ''1''s.
      This means that for a given nums[i], it must be of the form A11...1_2 (where A
      is some prefix and there are m ones at the end). The corresponding x would then
      be A01...1_2 (where A is the same prefix, ''0'' at bit m-1, and m-1 ones after
      it). To find this x, we first determine m, the count of trailing ''1''s in nums[i].
      Then, x can be obtained by flipping the (m-1)-th bit of nums[i] from ''1'' to
      ''0''. This is equivalent to nums[i] ^ (1 << (m-1)). This construction yields
      the smallest possible x because it preserves the most significant bits of nums[i]
      while making the least significant changes necessary to satisfy the x OR (x+1)
      condition.'
    time_complexity: The time complexity is O(N * log(max_val)), where N is the length
      of the nums array and max_val is the maximum value in nums. For each number in
      nums, we perform a constant number of bitwise operations and a loop to count trailing
      ones. This loop iterates at most log(max_val) times (up to 30-31 times for 10^9).
      Therefore, the total time complexity is proportional to N multiplied by the number
      of bits in the maximum possible nums[i].
    space_complexity: The space complexity is O(N), where N is the length of the nums
      array. This is because we need to store the ans array, which has the same length
      as the input nums array. No additional data structures are used that scale with
      the input values.
    elapsed_time: 334.1726016998291
    model: gemini-2.5-flash
    generated_at: '2026-01-21 18:15:03 '
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> minBitwiseArray(vector<int>&\
        \ nums) {\n        vector<int> ans;\n        for (int num : nums) {\n      \
        \      if (num % 2 == 0) {\n                ans.push_back(-1);\n           \
        \ } else {\n                int x = num;\n                while ((x | (x + 1))\
        \ != num) {\n                    x++;\n                }\n                ans.push_back(x);\n\
        \            }\n        }\n        return ans;\n    }\n};"
      java: "class Solution {\n    public int[] minBitwiseArray(List<Integer> nums)\
        \ {\n        int[] ans = new int[nums.size()];\n        for (int i = 0; i <\
        \ nums.size(); i++) {\n            int num = nums.get(i);\n            if (num\
        \ % 2 == 0) {\n                ans[i] = -1;\n            } else {\n        \
        \        int x = num;\n                while ((x | (x + 1)) != num) {\n    \
        \                x++;\n                }\n                ans[i] = x;\n    \
        \        }\n        }\n        return ans;\n    }\n}"
      python: "class Solution(object):\n    def minBitwiseArray(self, nums):\n     \
        \   ans = []\n        for num in nums:\n            if num % 2 == 0:\n     \
        \           ans.append(-1)\n            else:\n                x = num\n   \
        \             while (x | (x + 1)) != num:\n                    x += 1\n    \
        \            ans.append(x)\n        return ans"
      python3: "class Solution:\n    def minBitwiseArray(self, nums: list[int]) -> list[int]:\n\
        \        ans = []\n        for num in nums:\n            if num % 2 == 0:\n\
        \                ans.append(-1)\n            else:\n                x = num\n\
        \                while (x | (x + 1)) != num:\n                    x += 1\n \
        \               ans.append(x)\n        return ans"
      c: "int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {\n    int*\
        \ ans = (int*)malloc(numsSize * sizeof(int));\n    *returnSize = numsSize;\n\
        \    for (int i = 0; i < numsSize; i++) {\n        int num = nums[i];\n    \
        \    if (num % 2 == 0) {\n            ans[i] = -1;\n        } else {\n     \
        \       int x = num;\n            while ((x | (x + 1)) != num) {\n         \
        \       x++;\n            }\n            ans[i] = x;\n        }\n    }\n   \
        \ return ans;\n}"
      csharp: "public class Solution {\n    public int[] MinBitwiseArray(IList<int>\
        \ nums) {\n        int[] ans = new int[nums.Count];\n        for (int i = 0;\
        \ i < nums.Count; i++) {\n            int num = nums[i];\n            if (num\
        \ % 2 == 0) {\n                ans[i] = -1;\n            } else {\n        \
        \        int x = num;\n                while ((x | (x + 1)) != num) {\n    \
        \                x++;\n                }\n                ans[i] = x;\n    \
        \        }\n        }\n        return ans;\n    }\n}"
      javascript: "var minBitwiseArray = function(nums) {\n    let ans = [];\n    for\
        \ (let num of nums) {\n        if (num % 2 == 0) {\n            ans.push(-1);\n\
        \        } else {\n            let x = num;\n            while ((x | (x + 1))\
        \ != num) {\n                x++;\n            }\n            ans.push(x);\n\
        \        }\n    }\n    return ans;\n};"
      typescript: "function minBitwiseArray(nums: number[]): number[] {\n    let ans:\
        \ number[] = [];\n    for (let num of nums) {\n        if (num % 2 == 0) {\n\
        \            ans.push(-1);\n        } else {\n            let x = num;\n   \
        \         while ((x | (x + 1)) != num) {\n                x++;\n           \
        \ }\n            ans.push(x);\n        }\n    }\n    return ans;\n}"
      php: "class Solution {\n    function minBitwiseArray($nums) {\n        $ans =\
        \ [];\n        foreach ($nums as $num) {\n            if ($num % 2 == 0) {\n\
        \                $ans[] = -1;\n            } else {\n                $x = $num;\n\
        \                while (($x | ($x + 1)) != $num) {\n                    $x++;\n\
        \                }\n                $ans[] = $x;\n            }\n        }\n\
        \        return $ans;\n    }\n}"
      swift: "class Solution {\n    func minBitwiseArray(_ nums: [Int]) -> [Int] {\n\
        \        var ans: [Int] = []\n        for num in nums {\n            if num\
        \ % 2 == 0 {\n                ans.append(-1)\n            } else {\n       \
        \         var x = num\n                while (x | (x + 1)) != num {\n      \
        \              x += 1\n                }\n                ans.append(x)\n  \
        \          }\n        }\n        return ans\n    }\n}"
      kotlin: "class Solution {\n    fun minBitwiseArray(nums: List<Int>): IntArray\
        \ {\n        val result = IntArray(nums.size)\n        for (i in nums.indices)\
        \ {\n            if (nums[i] % 2 == 0) {\n                result[i] = -1\n \
        \           } else {\n                result[i] = nums[i] - 1\n            }\n\
        \        }\n        return result\n    }\n}"
      dart: "class Solution {\n  List<int> minBitwiseArray(List<int> nums) {\n    List<int>\
        \ result = List<int>.filled(nums.length, 0);\n    for (int i = 0; i < nums.length;\
        \ i++) {\n      if (nums[i] % 2 == 0) {\n        result[i] = -1;\n      } else\
        \ {\n        result[i] = nums[i] - 1;\n      }\n    }\n    return result;\n\
        \  }\n}"
      go: "func minBitwiseArray(nums []int) []int {\n    result := make([]int, len(nums))\n\
        \    for i, num := range nums {\n        if num % 2 == 0 {\n            result[i]\
        \ = -1\n        } else {\n            result[i] = num - 1\n        }\n    }\n\
        \    return result\n}"
      ruby: "def min_bitwise_array(nums)\n    result = Array.new(nums.size, 0)\n   \
        \ nums.each_with_index do |num, i|\n        if num % 2 == 0\n            result[i]\
        \ = -1\n        else\n            result[i] = num - 1\n        end\n    end\n\
        \    result\nend"
      scala: "object Solution {\n    def minBitwiseArray(nums: List[Int]): Array[Int]\
        \ = {\n        val result = Array.ofDim[Int](nums.size)\n        for (i <- nums.indices)\
        \ {\n            if (nums(i) % 2 == 0) {\n                result(i) = -1\n \
        \           } else {\n                result(i) = nums(i) - 1\n            }\n\
        \        }\n        result\n    }\n}"
      rust: "impl Solution {\n    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32>\
        \ {\n        let mut result = vec![0; nums.len()];\n        for (i, num) in\
        \ nums.into_iter().enumerate() {\n            if num % 2 == 0 {\n          \
        \      result[i] = -1;\n            } else {\n                result[i] = num\
        \ - 1;\n            }\n        }\n        result\n    }\n}"
      racket: "(define/contract (min-bitwise-array nums)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?))\n  (let ([result (make-list (length nums) 0)])\n\
        \    (for ([i (in-range (length nums))])\n      (let ([num (list-ref nums i)])\n\
        \        (if (even? num)\n            (list-set! result i -1)\n            (list-set!\
        \ result i (- num 1)))))\n    result))"
      erlang: "-module(solution).\n-export([min_bitwise_array/1]).\nmin_bitwise_array(Nums)\
        \ ->\n    lists:map(fun(N) when N rem 2 == 0 -> -1;\n                   (N)\
        \ -> N - 1 end, Nums)."
      elixir: "defmodule Solution do\n  @spec min_bitwise_array(nums :: [integer]) ::\
        \ [integer]\n  def min_bitwise_array(nums) do\n    Enum.map(nums, fn num when\
        \ rem(num, 2) == 0 -> -1; num -> num - 1 end)\n  end\nend"
    approach: The problem requires constructing an array where each element's bitwise
      OR operation with its next element equals a given prime number. To solve this,
      we can analyze the binary representation of each prime number. If a prime number
      is even, it's impossible to find a value that satisfies the condition, so we set
      the answer to -1. For odd prime numbers, we can try unsetting a single bit from
      the prime number to find the smallest value that satisfies the condition. This
      approach works because unsetting a bit from an odd number will always result in
      an even number, and the bitwise OR operation of an even number and its next number
      (which is odd) will be the original odd number.
    time_complexity: The time complexity of this solution is O(n * log(m)), where n
      is the number of elements in the input array and m is the maximum value in the
      array. This is because for each element, we potentially iterate through all its
      bits to find the smallest value that satisfies the condition.
    space_complexity: The space complexity of this solution is O(n), where n is the
      number of elements in the input array. This is because we need to store the result
      for each element in the input array.
    elapsed_time: 5.935218811035156
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-21 18:15:14 '
---

## Problem #3315: Construct the Minimum Bitwise Array II

**Difficulty:** Medium

**Topics:** Array, Bit Manipulation

## Problem Description

<p>You are given an array <code>nums</code> consisting of <code>n</code> <span data-keyword="prime-number">prime</span> integers.</p>

<p>You need to construct an array <code>ans</code> of length <code>n</code>, such that, for each index <code>i</code>, the bitwise <code>OR</code> of <code>ans[i]</code> and <code>ans[i] + 1</code> is equal to <code>nums[i]</code>, i.e. <code>ans[i] OR (ans[i] + 1) == nums[i]</code>.</p>

<p>Additionally, you must <strong>minimize</strong> each value of <code>ans[i]</code> in the resulting array.</p>

<p>If it is <em>not possible</em> to find such a value for <code>ans[i]</code> that satisfies the <strong>condition</strong>, then set <code>ans[i] = -1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,5,7]</span></p>

<p><strong>Output:</strong> <span class="example-io">[-1,1,4,3]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For <code>i = 0</code>, as there is no value for <code>ans[0]</code> that satisfies <code>ans[0] OR (ans[0] + 1) = 2</code>, so <code>ans[0] = -1</code>.</li>
	<li>For <code>i = 1</code>, the smallest <code>ans[1]</code> that satisfies <code>ans[1] OR (ans[1] + 1) = 3</code> is <code>1</code>, because <code>1 OR (1 + 1) = 3</code>.</li>
	<li>For <code>i = 2</code>, the smallest <code>ans[2]</code> that satisfies <code>ans[2] OR (ans[2] + 1) = 5</code> is <code>4</code>, because <code>4 OR (4 + 1) = 5</code>.</li>
	<li>For <code>i = 3</code>, the smallest <code>ans[3]</code> that satisfies <code>ans[3] OR (ans[3] + 1) = 7</code> is <code>3</code>, because <code>3 OR (3 + 1) = 7</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [11,13,31]</span></p>

<p><strong>Output:</strong> <span class="example-io">[9,12,15]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For <code>i = 0</code>, the smallest <code>ans[0]</code> that satisfies <code>ans[0] OR (ans[0] + 1) = 11</code> is <code>9</code>, because <code>9 OR (9 + 1) = 11</code>.</li>
	<li>For <code>i = 1</code>, the smallest <code>ans[1]</code> that satisfies <code>ans[1] OR (ans[1] + 1) = 13</code> is <code>12</code>, because <code>12 OR (12 + 1) = 13</code>.</li>
	<li>For <code>i = 2</code>, the smallest <code>ans[2]</code> that satisfies <code>ans[2] OR (ans[2] + 1) = 31</code> is <code>15</code>, because <code>15 OR (15 + 1) = 31</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>2 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>nums[i]</code> is a prime number.</li>
</ul>


## Hints

1. Consider the binary representation of `nums[i]`.

2. Answer is -1 for even `nums[i]`.

3. Try unsetting a single bit from `nums[i]`.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-21 18:15:03 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to find the minimum ans[i] such that ans[i] OR (ans[i] + 1) == nums[i]. We begin by analyzing the bitwise operation x OR (x + 1). If x is an even number, its binary representation ends with a '0'. Then x + 1 ends with a '1'. The bitwise OR x OR (x + 1) will result in x + 1. Since x + 1 is always odd, if nums[i] is an even number, no such x can exist that satisfies the condition, so ans[i] must be -1. This covers cases like nums[i] = 2.

If nums[i] is an odd number, we need to find the minimum x. The operation x OR (x + 1) effectively finds the rightmost '0' bit of x (at position k), flips it to '1', and keeps all bits to its right (which were already '1's) as '1's. This means that for a given nums[i], it must be of the form A11...1_2 (where A is some prefix and there are m ones at the end). The corresponding x would then be A01...1_2 (where A is the same prefix, '0' at bit m-1, and m-1 ones after it). To find this x, we first determine m, the count of trailing '1's in nums[i]. Then, x can be obtained by flipping the (m-1)-th bit of nums[i] from '1' to '0'. This is equivalent to nums[i] ^ (1 << (m-1)). This construction yields the smallest possible x because it preserves the most significant bits of nums[i] while making the least significant changes necessary to satisfy the x OR (x+1) condition.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-cpp-gemini-2-5-flash" checked>
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-java-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python3-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-c-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-csharp-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-javascript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-typescript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-php-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-swift-gemini-2-5-flash">
  <div class="tab-labels">
    <label for="lang-cpp-gemini-2-5-flash">C++</label>
    <label for="lang-java-gemini-2-5-flash">Java</label>
    <label for="lang-python-gemini-2-5-flash">Python</label>
    <label for="lang-python3-gemini-2-5-flash">Python3</label>
    <label for="lang-c-gemini-2-5-flash">C</label>
    <label for="lang-csharp-gemini-2-5-flash">C#</label>
    <label for="lang-javascript-gemini-2-5-flash">JavaScript</label>
    <label for="lang-typescript-gemini-2-5-flash">TypeScript</label>
    <label for="lang-php-gemini-2-5-flash">PHP</label>
    <label for="lang-swift-gemini-2-5-flash">Swift</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    std::vector<int> minBitwiseArray(std::vector<int>& nums) {
        std::vector<int> ans;
        for (int num : nums) {
            if (num % 2 == 0) {
                ans.push_back(-1);
            } else {
                int m = 0;
                int temp_num = num;
                while ((temp_num & 1) == 1) {
                    m++;
                    temp_num >>= 1;
                }
                ans.push_back(num ^ (1 << (m - 1)));
            }
        }
        return ans;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] minBitwiseArray(List<Integer> nums) {
        int[] ans = new int[nums.size()];
        for (int i = 0; i < nums.size(); i++) {
            int num = nums.get(i);
            if (num % 2 == 0) {
                ans[i] = -1;
            } else {
                int m = 0;
                int temp_num = num;
                while ((temp_num & 1) == 1) {
                    m++;
                    temp_num >>= 1;
                }
                ans[i] = num ^ (1 << (m - 1));
            }
        }
        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
# Failed to parse response
# Check logs for full output.
# Full Response:
'''
{
  "approach": "The core of this problem lies in understanding the bitwise OR operation between an integer `x` and `x + 1`. When `x` is represented in binary, `x + 1` flips the rightmost zero bit of `x` to one, and all subsequent one bits to its right become zero. For example, if `x = A01...1` (where 'A' is a prefix, '0' is the rightmost zero at bit position `k`, and there are `k` ones to its right), then `x + 1 = A10...0`. Performing `x OR (x + 1)` results in `A11...1`, meaning all bits from position `0` up to and including position `k` are set to `1`, while bits to the left of `k` remain unchanged from `x` (and `x+1`). This implies that for `ans[i] OR (ans[i] + 1)` to equal `nums[i]`, `nums[i]` must have all its bits set from the least significant bit up to the position of the rightmost zero in `ans[i]`. Consequently, `nums[i]` must be an odd number, as `A11...1` always ends with a `1`. If `nums[i]` is even, no solution exists, and `ans[i]` is -1.",
  "time_complexity": "The time complexity is O(N * log(max(nums[i]))), where N is the length of the `nums` array. For each number in `nums`, we perform a constant number of bitwise operations and a loop to find the highest set bit, which takes logarithmic time with respect to the value of `nums[i]` (up to 30-31 bits for 10^9).",
  "space_complexity": "The space complexity is O(N) to store the `ans` array. No additional significant space is used beyond the output array.",
  "solutions": {
    "kotlin": "class Solution {\n    fun minBitwiseArray(nums: List<Int>): IntArray {\n        val ans = IntArray(nums.size)\n        for (i in nums.indices) {\n            val n = nums[i]\n            if (n % 2 == 0) {\n                ans[i] = -1\n            } else {\n                // Find the highest set bit position\n                var highestBitPos = 0\n                for (j in 30 downTo 0) { // Max 10^9 is less than 2^30\n                    if ((n shr j) and 1 == 1) {\n                        highestBitPos = j\n                        break\n                    }\n                }\n                \n                // The target x must have all bits from 0 to highestBitPos-1 unset\n                // and the highestBitPos bit unset, to become N when OR-ed with x+1\n                // This means x should be N XOR (2^k - 1) where k is the position of the rightmost 0 in x\n                // Or, more simply, x = N ^ (N & (N-1))\n                // This is equivalent to x = N ^ (1 << (position of rightmost 0 in N))\n                // No, this is not correct. Let's use the property: x OR (x+1) = N\n                // The smallest x is N XOR (1 << k) where k is the position of the rightmost 0 in N-1\n                // This is equivalent to x = N - (N & (N-1))\n                // Let's re-derive: x OR (x+1) = N. We want smallest x.\n                // If x = A01...1 (k ones), then x+1 = A10...0, and N = A11...1 (k+1 ones).\n                // So N must be of the form (prefix)11...1. If N has a 0 in its lower bits, it's impossible.\n                // Example: N=5 (101). Highest bit is 2. Rightmost 0 is at bit 1.\n                // If x=4 (100), x+1=5 (101). 4 OR 5 = 5. Correct.\n                // Example: N=7 (111). Highest bit is 2. No 0s in lower bits.\n                // If x=3 (011), x+1=4 (100). 3 OR 4 = 7. Correct.\n                // The value of x is N XOR (1 << k) where k is the position of the rightmost 0 in N-1.\n                // This is equivalent to N - (N & (N-1)).\n                // N & (N-1) clears the LSB of N. So N - (N & (N-1)) is N - (LSB of N).\n                // This is N - (N & -N).\n                // Let's test this: N=5 (101). N & -N = 1 (001). N - (N & -N) = 5 - 1 = 4. Correct.\n                // N=7 (111). N & -N = 1 (001). N - (N & -N) = 7 - 1 = 6. Incorrect. Expected 3.\n                // The logic for N & -N is for finding the LSB. This is not what we want.\n                \n                // The property is that N must be of the form (prefix)11...1. If N has a 0 bit at position j\n                // and there is a 1 bit at position j+1, then it's impossible.\n                // For example, N=5 (101). It has 0 at bit 1. This means x cannot have its rightmost 0 at bit 1.\n                // If x has its rightmost 0 at bit k, then N must have all bits from 0 to k set to 1.\n                // So, if N has a 0 at bit j, then k must be > j.\n                // This means x must be N with some trailing 1s flipped to 0s.\n                // Specifically, x = N XOR (1 << (k+1) - 1) where k is the position of the rightmost 0 in x.\n                // This is equivalent to x = N ^ (N & (N-1)).\n                // Let's re-examine the examples:\n                // N=3 (011). x=1 (001). 1 OR 2 = 3. N & (N-1) = 3 & 2 = 2. N ^ (N & (N-1)) = 3 ^ 2 = 1. Correct.\n                // N=5 (101). x=4 (100). 4 OR 5 = 5. N & (N-1) = 5 & 4 = 4. N ^ (N & (N-1)) = 5 ^ 4 = 1. Incorrect. Expected 4.\n                // N=7 (111). x=3 (011). 3 OR 4 = 7. N & (N-1) = 7 & 6 = 6. N ^ (N & (N-1)) = 7 ^ 6 = 1. Incorrect. Expected 3.\n                \n                // The correct approach is: find the highest bit `msb` of `N`. Let `mask = (1 << (msb + 1)) - 1`. This is `2^(msb+1) - 1` (all ones up to `msb`).\n                // If `N` is not equal to `mask`, then `N` has a zero bit somewhere below `msb`. In this case, `ans[i]` is -1.\n                // Example: N=5 (101). msb=2. mask = (1 << 3) - 1 = 7 (111). 5 != 7. So ans[i] should be -1. But example says 4.\n                // This means my understanding of the `A11...1` form is flawed or incomplete.\n                \n                // Let's re-check the property: `x OR (x+1) = N`\n                // `x` and `x+1` differ at the rightmost `0` bit of `x` and all bits to its right.\n                // If `x` ends with `01...1` (k ones), then `x+1` ends with `10...0` (k zeros).\n                // `x OR (x+1)` will have `k+1` ones at the end.\n                // So `N` must have its `k+1` least significant bits set to `1`.\n                // If `N` has a `0` at bit position `j`, then `x` must also have a `0` at bit position `j`.\n                // And `x+1` must also have a `0` at bit position `j`.\n                // This means `j` cannot be the position of the rightmost `0` in `x`.\n                // So, if `N` has a `0` at bit `j`, then `x` must have `0` at bit `j`, and its rightmost `0` must be at a position `k > j`.\n                // This implies that `x` must be `N` with some trailing `1`s unset.\n                // To minimize `x`, we want to unset as few bits as possible, and from the rightmost positions.\n                // Consider `N`. Find the highest bit `msb_N` of `N`.\n                // The result `x OR (x+1)` will have its highest bit at `msb_N`.\n                // This means `x` must have its highest bit at `msb_N` or `msb_N - 1`.\n                // If `x` has its highest bit at `msb_N`, then `x` must be `N` with some trailing bits unset.\n                // If `x` has its highest bit at `msb_N - 1`, then `x+1` must have its highest bit at `msb_N`.\n                // This happens when `x = (1 << msb_N) - 1`. Then `x+1 = (1 << msb_N)`. `x OR (x+1) = (1 << (msb_N + 1)) - 1`.\n                // This is the case for N = 3, 7, 15, 31, etc. Here x = (N-1)/2.\n                // For N=3 (011), msb_N=1. x=(3-1)/2=1. Correct.\n                // For N=7 (111), msb_N=2. x=(7-1)/2=3. Correct.\n                \n                // What if N is not `2^k - 1`?\n                // N=5 (101). msb_N=2. `x` must be 4 (100). `4 OR 5 = 5`. This works.\n                // N=11 (1011). msb_N=3. `x` must
'''
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num % 2 == 0:
                ans.append(-1)
            else:
                m = 0
                temp_num = num
                while (temp_num & 1) == 1:
                    m += 1
                    temp_num >>= 1
                ans.append(num ^ (1 << (m - 1)))
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h> // For malloc

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc(numsSize * sizeof(int));
    *returnSize = numsSize;

    for (int i = 0; i < numsSize; i++) {
        int num = nums[i];
        if (num % 2 == 0) {
            ans[i] = -1;
        } else {
            int m = 0;
            int temp_num = num;
            while ((temp_num & 1) == 1) {
                m++;
                temp_num >>= 1;
            }
            ans[i] = num ^ (1 << (m - 1));
        }
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;

public class Solution {
    public int[] MinBitwiseArray(IList<int> nums) {
        int[] ans = new int[nums.Count];
        for (int i = 0; i < nums.Count; i++) {
            int num = nums[i];
            if (num % 2 == 0) {
                ans[i] = -1;
            } else {
                int m = 0;
                int temp_num = num;
                while ((temp_num & 1) == 1) {
                    m++;
                    temp_num >>= 1;
                }
                ans[i] = num ^ (1 << (m - 1));
            }
        }
        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var minBitwiseArray = function(nums) {
    const ans = [];
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        if (num % 2 === 0) {
            ans.push(-1);
        } else {
            let m = 0;
            let temp_num = num;
            while ((temp_num & 1) === 1) {
                m++;
                temp_num >>= 1;
            }
            ans.push(num ^ (1 << (m - 1)));
        }
    }
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minBitwiseArray(nums: number[]): number[] {
    const ans: number[] = [];
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        if (num % 2 === 0) {
            ans.push(-1);
        } else {
            let m = 0;
            let temp_num = num;
            while ((temp_num & 1) === 1) {
                m++;
                temp_num >>= 1;
            }
            ans.push(num ^ (1 << (m - 1)));
        }
    }
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function minBitwiseArray($nums) {
        $ans = [];
        foreach ($nums as $num) {
            if ($num % 2 == 0) {
                $ans[] = -1;
            } else {
                $m = 0;
                $temp_num = $num;
                while (($temp_num & 1) == 1) {
                    $m++;
                    $temp_num >>= 1;
                }
                $ans[] = $num ^ (1 << ($m - 1));
            }
        }
        return $ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minBitwiseArray(_ nums: [Int]) -> [Int] {
        var ans: [Int] = []
        for num in nums {
            if num % 2 == 0 {
                ans.append(-1)
            } else {
                var m = 0
                var temp_num = num
                while (temp_num & 1) == 1 {
                    m += 1
                    temp_num >>= 1
                }
                ans.append(num ^ (1 << (m - 1)))
            }
        }
        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N * log(max_val)), where N is the length of the nums array and max_val is the maximum value in nums. For each number in nums, we perform a constant number of bitwise operations and a loop to count trailing ones. This loop iterates at most log(max_val) times (up to 30-31 times for 10^9). Therefore, the total time complexity is proportional to N multiplied by the number of bits in the maximum possible nums[i].

- **Space Complexity:** The space complexity is O(N), where N is the length of the nums array. This is because we need to store the ans array, which has the same length as the input nums array. No additional data structures are used that scale with the input values.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-21 18:15:14 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires constructing an array where each element's bitwise OR operation with its next element equals a given prime number. To solve this, we can analyze the binary representation of each prime number. If a prime number is even, it's impossible to find a value that satisfies the condition, so we set the answer to -1. For odd prime numbers, we can try unsetting a single bit from the prime number to find the smallest value that satisfies the condition. This approach works because unsetting a bit from an odd number will always result in an even number, and the bitwise OR operation of an even number and its next number (which is odd) will be the original odd number.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-cpp-llama-3-3-70b-versatile" checked>
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-java-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python3-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-c-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-csharp-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-javascript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-typescript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-php-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-swift-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-kotlin-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-dart-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-go-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-ruby-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-scala-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-rust-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-racket-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-erlang-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-elixir-llama-3-3-70b-versatile">
  <div class="tab-labels">
    <label for="lang-cpp-llama-3-3-70b-versatile">C++</label>
    <label for="lang-java-llama-3-3-70b-versatile">Java</label>
    <label for="lang-python-llama-3-3-70b-versatile">Python</label>
    <label for="lang-python3-llama-3-3-70b-versatile">Python3</label>
    <label for="lang-c-llama-3-3-70b-versatile">C</label>
    <label for="lang-csharp-llama-3-3-70b-versatile">C#</label>
    <label for="lang-javascript-llama-3-3-70b-versatile">JavaScript</label>
    <label for="lang-typescript-llama-3-3-70b-versatile">TypeScript</label>
    <label for="lang-php-llama-3-3-70b-versatile">PHP</label>
    <label for="lang-swift-llama-3-3-70b-versatile">Swift</label>
    <label for="lang-kotlin-llama-3-3-70b-versatile">Kotlin</label>
    <label for="lang-dart-llama-3-3-70b-versatile">Dart</label>
    <label for="lang-go-llama-3-3-70b-versatile">Go</label>
    <label for="lang-ruby-llama-3-3-70b-versatile">Ruby</label>
    <label for="lang-scala-llama-3-3-70b-versatile">Scala</label>
    <label for="lang-rust-llama-3-3-70b-versatile">Rust</label>
    <label for="lang-racket-llama-3-3-70b-versatile">Racket</label>
    <label for="lang-erlang-llama-3-3-70b-versatile">Erlang</label>
    <label for="lang-elixir-llama-3-3-70b-versatile">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        vector<int> ans;
        for (int num : nums) {
            if (num % 2 == 0) {
                ans.push_back(-1);
            } else {
                int x = num;
                while ((x | (x + 1)) != num) {
                    x++;
                }
                ans.push_back(x);
            }
        }
        return ans;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int[] minBitwiseArray(List<Integer> nums) {
        int[] ans = new int[nums.size()];
        for (int i = 0; i < nums.size(); i++) {
            int num = nums.get(i);
            if (num % 2 == 0) {
                ans[i] = -1;
            } else {
                int x = num;
                while ((x | (x + 1)) != num) {
                    x++;
                }
                ans[i] = x;
            }
        }
        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minBitwiseArray(self, nums):
        ans = []
        for num in nums:
            if num % 2 == 0:
                ans.append(-1)
            else:
                x = num
                while (x | (x + 1)) != num:
                    x += 1
                ans.append(x)
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        ans = []
        for num in nums:
            if num % 2 == 0:
                ans.append(-1)
            else:
                x = num
                while (x | (x + 1)) != num:
                    x += 1
                ans.append(x)
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc(numsSize * sizeof(int));
    *returnSize = numsSize;
    for (int i = 0; i < numsSize; i++) {
        int num = nums[i];
        if (num % 2 == 0) {
            ans[i] = -1;
        } else {
            int x = num;
            while ((x | (x + 1)) != num) {
                x++;
            }
            ans[i] = x;
        }
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] MinBitwiseArray(IList<int> nums) {
        int[] ans = new int[nums.Count];
        for (int i = 0; i < nums.Count; i++) {
            int num = nums[i];
            if (num % 2 == 0) {
                ans[i] = -1;
            } else {
                int x = num;
                while ((x | (x + 1)) != num) {
                    x++;
                }
                ans[i] = x;
            }
        }
        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var minBitwiseArray = function(nums) {
    let ans = [];
    for (let num of nums) {
        if (num % 2 == 0) {
            ans.push(-1);
        } else {
            let x = num;
            while ((x | (x + 1)) != num) {
                x++;
            }
            ans.push(x);
        }
    }
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minBitwiseArray(nums: number[]): number[] {
    let ans: number[] = [];
    for (let num of nums) {
        if (num % 2 == 0) {
            ans.push(-1);
        } else {
            let x = num;
            while ((x | (x + 1)) != num) {
                x++;
            }
            ans.push(x);
        }
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function minBitwiseArray($nums) {
        $ans = [];
        foreach ($nums as $num) {
            if ($num % 2 == 0) {
                $ans[] = -1;
            } else {
                $x = $num;
                while (($x | ($x + 1)) != $num) {
                    $x++;
                }
                $ans[] = $x;
            }
        }
        return $ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minBitwiseArray(_ nums: [Int]) -> [Int] {
        var ans: [Int] = []
        for num in nums {
            if num % 2 == 0 {
                ans.append(-1)
            } else {
                var x = num
                while (x | (x + 1)) != num {
                    x += 1
                }
                ans.append(x)
            }
        }
        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minBitwiseArray(nums: List<Int>): IntArray {
        val result = IntArray(nums.size)
        for (i in nums.indices) {
            if (nums[i] % 2 == 0) {
                result[i] = -1
            } else {
                result[i] = nums[i] - 1
            }
        }
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> minBitwiseArray(List<int> nums) {
    List<int> result = List<int>.filled(nums.length, 0);
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] % 2 == 0) {
        result[i] = -1;
      } else {
        result[i] = nums[i] - 1;
      }
    }
    return result;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minBitwiseArray(nums []int) []int {
    result := make([]int, len(nums))
    for i, num := range nums {
        if num % 2 == 0 {
            result[i] = -1
        } else {
            result[i] = num - 1
        }
    }
    return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def min_bitwise_array(nums)
    result = Array.new(nums.size, 0)
    nums.each_with_index do |num, i|
        if num % 2 == 0
            result[i] = -1
        else
            result[i] = num - 1
        end
    end
    result
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minBitwiseArray(nums: List[Int]): Array[Int] = {
        val result = Array.ofDim[Int](nums.size)
        for (i <- nums.indices) {
            if (nums(i) % 2 == 0) {
                result(i) = -1
            } else {
                result(i) = nums(i) - 1
            }
        }
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32> {
        let mut result = vec![0; nums.len()];
        for (i, num) in nums.into_iter().enumerate() {
            if num % 2 == 0 {
                result[i] = -1;
            } else {
                result[i] = num - 1;
            }
        }
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-bitwise-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let ([result (make-list (length nums) 0)])
    (for ([i (in-range (length nums))])
      (let ([num (list-ref nums i)])
        (if (even? num)
            (list-set! result i -1)
            (list-set! result i (- num 1)))))
    result))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([min_bitwise_array/1]).
min_bitwise_array(Nums) ->
    lists:map(fun(N) when N rem 2 == 0 -> -1;
                   (N) -> N - 1 end, Nums).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_bitwise_array(nums :: [integer]) :: [integer]
  def min_bitwise_array(nums) do
    Enum.map(nums, fn num when rem(num, 2) == 0 -> -1; num -> num - 1 end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n * log(m)), where n is the number of elements in the input array and m is the maximum value in the array. This is because for each element, we potentially iterate through all its bits to find the smallest value that satisfies the condition.

- **Space Complexity:** The space complexity of this solution is O(n), where n is the number of elements in the input array. This is because we need to store the result for each element in the input array.

</div>
</details>
