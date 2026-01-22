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
      cpp: "#include <vector>\n#include <numeric>\n\nclass Solution {\npublic:\n   \
        \ int countTrailingOnes(int n) {\n        int count = 0;\n        while ((n\
        \ & 1) == 1) {\n            n >>= 1;\n            count++;\n        }\n    \
        \    return count;\n    }\n\n    std::vector<int> minBitwiseArray(std::vector<int>&\
        \ nums) {\n        std::vector<int> ans;\n        ans.reserve(nums.size());\n\
        \n        for (int num : nums) {\n            if (num % 2 == 0) {\n        \
        \        ans.push_back(-1);\n            } else {\n                int c = countTrailingOnes(num);\n\
        \                int result = num - (1 << (c - 1));\n                ans.push_back(result);\n\
        \            }\n        }\n        return ans;\n    }\n};"
      java: "import java.util.ArrayList;\nimport java.util.List;\n\nclass Solution {\n\
        \    private int countTrailingOnes(int n) {\n        int count = 0;\n      \
        \  while ((n & 1) == 1) {\n            n >>= 1;\n            count++;\n    \
        \    }\n        return count;\n    }\n\n    public int[] minBitwiseArray(List<Integer>\
        \ nums) {\n        int[] ans = new int[nums.size()];\n\n        for (int i =\
        \ 0; i < nums.size(); i++) {\n            int num = nums.get(i);\n         \
        \   if (num % 2 == 0) {\n                ans[i] = -1;\n            } else {\n\
        \                int c = countTrailingOnes(num);\n                int result\
        \ = num - (1 << (c - 1));\n                ans[i] = result;\n            }\n\
        \        }\n        return ans;\n    }\n}"
      python: "class Solution(object):\n    def minBitwiseArray(self, nums):\n     \
        \   \"\"\"\n        :type nums: List[int]\n        :rtype: List[int]\n     \
        \   \"\"\"\n        ans = []\n        for num in nums:\n            if num %\
        \ 2 == 0:\n                ans.append(-1)\n            else:\n             \
        \   c = 0\n                temp_num = num\n                while (temp_num &\
        \ 1) == 1:\n                    temp_num >>= 1\n                    c += 1\n\
        \n                result = num - (1 << (c - 1))\n                ans.append(result)\n\
        \        return ans"
      python3: "class Solution:\n    def minBitwiseArray(self, nums: List[int]) -> List[int]:\n\
        \        ans = []\n        for num in nums:\n            if num % 2 == 0:\n\
        \                ans.append(-1)\n            else:\n                c = 0\n\
        \                temp_num = num\n                while (temp_num & 1) == 1:\n\
        \                    temp_num >>= 1\n                    c += 1\n\n        \
        \        result = num - (1 << (c - 1))\n                ans.append(result)\n\
        \        return ans"
      c: "#include <stdlib.h>\n\n/**\n * Note: The returned array must be malloced,\
        \ assume caller calls free().\n */\nint* minBitwiseArray(int* nums, int numsSize,\
        \ int* returnSize) {\n    int* ans = (int*)malloc(numsSize * sizeof(int));\n\
        \    *returnSize = numsSize;\n\n    for (int i = 0; i < numsSize; i++) {\n \
        \       int num = nums[i];\n        if (num % 2 == 0) {\n            ans[i]\
        \ = -1;\n        } else {\n            int c = 0;\n            int temp_num\
        \ = num;\n            while ((temp_num & 1) == 1) {\n                temp_num\
        \ >>= 1;\n                c++;\n            }\n\n            int result = num\
        \ - (1 << (c - 1));\n            ans[i] = result;\n        }\n    }\n    return\
        \ ans;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int[] MinBitwiseArray(IList<int> nums) {\n        int[] ans\
        \ = new int[nums.Count];\n\n        for (int i = 0; i < nums.Count; i++) {\n\
        \            int num = nums[i];\n            if (num % 2 == 0) {\n         \
        \       ans[i] = -1;\n            } else {\n                int c = 0;\n   \
        \             int tempNum = num;\n                while ((tempNum & 1) == 1)\
        \ {\n                    tempNum >>= 1;\n                    c++;\n        \
        \        }\n\n                int result = num - (1 << (c - 1));\n         \
        \       ans[i] = result;\n            }\n        }\n        return ans;\n  \
        \  }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number[]}\n */\nvar minBitwiseArray\
        \ = function(nums) {\n    const ans = [];\n    for (let i = 0; i < nums.length;\
        \ i++) {\n        const num = nums[i];\n        if (num % 2 === 0) {\n     \
        \       ans.push(-1);\n        } else {\n            let c = 0;\n          \
        \  let tempNum = num;\n            while ((tempNum & 1) === 1) {\n         \
        \       tempNum >>= 1;\n                c++;\n            }\n\n            const\
        \ result = num - (1 << (c - 1));\n            ans.push(result);\n        }\n\
        \    }\n    return ans;\n};"
      typescript: "function minBitwiseArray(nums: number[]): number[] {\n    const ans:\
        \ number[] = [];\n    for (let i = 0; i < nums.length; i++) {\n        const\
        \ num = nums[i];\n        if (num % 2 === 0) {\n            ans.push(-1);\n\
        \        } else {\n            let c = 0;\n            let tempNum = num;\n\
        \            while ((tempNum & 1) === 1) {\n                tempNum >>= 1;\n\
        \                c++;\n            }\n\n            const result = num - (1\
        \ << (c - 1));\n            ans.push(result);\n        }\n    }\n    return\
        \ ans;\n};"
      php: "<?php\n\nclass Solution {\n\n    /**\n     * @param Integer[] $nums\n  \
        \   * @return Integer[]\n     */\n    function minBitwiseArray($nums) {\n  \
        \      $ans = [];\n        foreach ($nums as $num) {\n            if ($num %\
        \ 2 == 0) {\n                $ans[] = -1;\n            } else {\n          \
        \      $c = 0;\n                $tempNum = $num;\n                while (($tempNum\
        \ & 1) == 1) {\n                    $tempNum >>= 1;\n                    $c++;\n\
        \                }\n\n                $result = $num - (1 << ($c - 1));\n  \
        \              $ans[] = $result;\n            }\n        }\n        return $ans;\n\
        \    }\n}"
      swift: "import Foundation\n\nclass Solution {\n    func minBitwiseArray(_ nums:\
        \ [Int]) -> [Int] {\n        var ans: [Int] = []\n        ans.reserveCapacity(nums.count)\n\
        \n        for num in nums {\n            if num % 2 == 0 {\n               \
        \ ans.append(-1)\n            } else {\n                var c = 0\n        \
        \        var tempNum = num\n                while (tempNum & 1) == 1 {\n   \
        \                 tempNum >>= 1\n                    c += 1\n              \
        \  }\n\n                let result = num - (1 << (c - 1))\n                ans.append(result)\n\
        \            }\n        }\n        return ans\n    }\n}"
      kotlin: "class Solution {\n    fun minBitwiseArray(nums: List<Int>): IntArray\
        \ {\n        val ans = IntArray(nums.size)\n        for (i in nums.indices)\
        \ {\n            val num = nums[i]\n            if (num % 2 == 0) {\n      \
        \          ans[i] = -1\n            } else {\n                var k0 = 0\n \
        \               while ((num shr k0) and 1 == 1) {\n                    k0++\n\
        \                }\n                ans[i] = num xor (1 shl (k0 - 1))\n    \
        \        }\n        }\n        return ans\n    }\n}"
      dart: "class Solution {\n  List<int> minBitwiseArray(List<int> nums) {\n    List<int>\
        \ ans = List<int>.filled(nums.length, 0);\n    for (int i = 0; i < nums.length;\
        \ i++) {\n      int num = nums[i];\n      if (num % 2 == 0) {\n        ans[i]\
        \ = -1;\n      } else {\n        int k0 = 0;\n        while (((num >> k0) &\
        \ 1) == 1) {\n          k0++;\n        }\n        ans[i] = num ^ (1 << (k0 -\
        \ 1));\n      }\n    }\n    return ans;\n  }\n}"
      go: "func minBitwiseArray(nums []int) []int {\n    ans := make([]int, len(nums))\n\
        \    for i, num := range nums {\n        if num % 2 == 0 {\n            ans[i]\
        \ = -1\n        } else {\n            k0 := 0\n            for ((num >> k0)\
        \ & 1) == 1 {\n                k0++\n            }\n            ans[i] = num\
        \ ^ (1 << (k0 - 1))\n        }\n    }\n    return ans\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer[]}\ndef min_bitwise_array(nums)\n\
        \    ans = []\n    nums.each do |num|\n        if num % 2 == 0\n           \
        \ ans << -1\n        else\n            k0 = 0\n            while ((num >> k0)\
        \ & 1) == 1\n                k0 += 1\n            end\n            ans << (num\
        \ ^ (1 << (k0 - 1)))\n        end\n    end\n    ans\nend"
      scala: "object Solution {\n    def minBitwiseArray(nums: List[Int]): Array[Int]\
        \ = {\n        val ans = Array.ofDim[Int](nums.length)\n        for (i <- nums.indices)\
        \ {\n            val num = nums(i)\n            if (num % 2 == 0) {\n      \
        \          ans(i) = -1\n            } else {\n                var k0 = 0\n \
        \               while (((num >> k0) & 1) == 1) {\n                    k0 +=\
        \ 1\n                }\n                ans(i) = num ^ (1 << (k0 - 1))\n   \
        \         }\n        }\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32>\
        \ {\n        let mut ans: Vec<i32> = Vec::with_capacity(nums.len());\n     \
        \   for num in nums {\n            if num % 2 == 0 {\n                ans.push(-1);\n\
        \            } else {\n                let mut k0 = 0;\n                while\
        \ ((num >> k0) & 1) == 1 {\n                    k0 += 1;\n                }\n\
        \                ans.push(num ^ (1 << (k0 - 1)));\n            }\n        }\n\
        \        ans\n    }\n}"
      racket: "(define/contract (min-bitwise-array nums)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?))\n  (map (lambda (num)\n         (if (even? num)\n\
        \             -1\n             (let loop ((k0 0))\n               (if (= (bitwise-and\
        \ (bitwise-rshift num k0) 1) 1)\n                   (loop (+ k0 1))\n      \
        \             (bitwise-xor num (bitwise-lshift 1 (- k0 1)))))))\n       nums))"
      erlang: "-spec min_bitwise_array(Nums :: [integer()]) -> [integer()].\nmin_bitwise_array(Nums)\
        \ ->\n  lists:map(fun(Num) ->\n                if\n                    Num rem\
        \ 2 == 0 ->\n                        -1;\n                    true ->\n    \
        \                    k0_loop(Num, 0)\n                end\n            end,\
        \ Nums).\n\nk0_loop(Num, K0) ->\n    if\n        (bsr(Num, K0) band 1) == 1\
        \ ->\n            k0_loop(Num, K0 + 1);\n        true ->\n            Num bxor\
        \ (1 bsl (K0 - 1))\n    end."
      elixir: "defmodule Solution do\n  @spec min_bitwise_array(nums :: [integer]) ::\
        \ [integer]\n  def min_bitwise_array(nums) do\n    Enum.map(nums, fn num ->\n\
        \      if rem(num, 2) == 0 do\n        -1\n      else\n        k0 = find_k0(num,\
        \ 0)\n        Bitwise.bxor(num, Bitwise.bsl(1, k0 - 1))\n      end\n    end)\n\
        \  end\n\n  defp find_k0(num, k0) do\n    if Bitwise.band(Bitwise.bsr(num, k0),\
        \ 1) == 1 do\n      find_k0(num, k0 + 1)\n    else\n      k0\n    end\n  end\n\
        end"
    approach: The problem asks us to find the minimum `ans[i]` for each `nums[i]` such
      that `ans[i] OR (ans[i] + 1) == nums[i]`. We analyze the bitwise OR operation
      `x OR (x + 1)`. If `x` is an even number, its least significant bit (LSB) is 0.
      Then `x = ...0` and `x + 1 = ...1`. Their bitwise OR, `x OR (x + 1)`, will always
      have its LSB as 1, making it an odd number. Therefore, if `nums[i]` is even, no
      `ans[i]` can satisfy the condition, and we set `ans[i] = -1`. This covers the
      case where `nums[i] = 2` (the only even prime).
    time_complexity: The time complexity is O(N * log(max_val)) where N is the length
      of the `nums` array and `max_val` is the maximum value in `nums`. For each number
      in `nums`, we perform a constant number of arithmetic operations and a loop to
      count trailing ones. This loop iterates at most `log(max_val)` times (approximately
      30 for `10^9`).
    space_complexity: The space complexity is O(N) to store the `ans` array, where N
      is the length of the `nums` array. No additional data structures are used that
      scale with the input values.
    elapsed_time: 120.6303162574768
    model: gemini-2.5-flash
    generated_at: '2026-01-22 02:33:31 '
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> minBitwiseArray(vector<int>&\
        \ nums) {\n        vector<int> ans;\n        for (int num : nums) {\n      \
        \      if (num % 2 == 0) {\n                ans.push_back(-1);\n           \
        \ } else {\n                int x = num;\n                while ((x | (x + 1))\
        \ != num) {\n                    x--;\n                }\n                ans.push_back(x);\n\
        \            }\n        }\n        return ans;\n    }\n};"
      java: "class Solution {\n    public int[] minBitwiseArray(List<Integer> nums)\
        \ {\n        int[] ans = new int[nums.size()];\n        for (int i = 0; i <\
        \ nums.size(); i++) {\n            int num = nums.get(i);\n            if (num\
        \ % 2 == 0) {\n                ans[i] = -1;\n            } else {\n        \
        \        int x = num;\n                while ((x | (x + 1)) != num) {\n    \
        \                x--;\n                }\n                ans[i] = x;\n    \
        \        }\n        }\n        return ans;\n    }\n}"
      python: "class Solution(object):\n    def minBitwiseArray(self, nums):\n     \
        \   ans = []\n        for num in nums:\n            if num % 2 == 0:\n     \
        \           ans.append(-1)\n            else:\n                x = num\n   \
        \             while (x | (x + 1)) != num:\n                    x -= 1\n    \
        \            ans.append(x)\n        return ans"
      python3: "class Solution:\n    def minBitwiseArray(self, nums: list[int]) -> list[int]:\n\
        \        ans = []\n        for num in nums:\n            if num % 2 == 0:\n\
        \                ans.append(-1)\n            else:\n                x = num\n\
        \                while (x | (x + 1)) != num:\n                    x -= 1\n \
        \               ans.append(x)\n        return ans"
      c: "int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {\n    int*\
        \ ans = (int*)malloc(numsSize * sizeof(int));\n    *returnSize = numsSize;\n\
        \    for (int i = 0; i < numsSize; i++) {\n        int num = nums[i];\n    \
        \    if (num % 2 == 0) {\n            ans[i] = -1;\n        } else {\n     \
        \       int x = num;\n            while ((x | (x + 1)) != num) {\n         \
        \       x--;\n            }\n            ans[i] = x;\n        }\n    }\n   \
        \ return ans;\n}"
      csharp: "public class Solution {\n    public int[] MinBitwiseArray(IList<int>\
        \ nums) {\n        int[] ans = new int[nums.Count];\n        for (int i = 0;\
        \ i < nums.Count; i++) {\n            int num = nums[i];\n            if (num\
        \ % 2 == 0) {\n                ans[i] = -1;\n            } else {\n        \
        \        int x = num;\n                while ((x | (x + 1)) != num) {\n    \
        \                x--;\n                }\n                ans[i] = x;\n    \
        \        }\n        }\n        return ans;\n    }\n}"
      javascript: "var minBitwiseArray = function(nums) {\n    let ans = [];\n    for\
        \ (let num of nums) {\n        if (num % 2 == 0) {\n            ans.push(-1);\n\
        \        } else {\n            let x = num;\n            while ((x | (x + 1))\
        \ != num) {\n                x--;\n            }\n            ans.push(x);\n\
        \        }\n    }\n    return ans;\n};"
      typescript: "function minBitwiseArray(nums: number[]): number[] {\n    let ans:\
        \ number[] = [];\n    for (let num of nums) {\n        if (num % 2 == 0) {\n\
        \            ans.push(-1);\n        } else {\n            let x = num;\n   \
        \         while ((x | (x + 1)) != num) {\n                x--;\n           \
        \ }\n            ans.push(x);\n        }\n    }\n    return ans;\n}"
      php: "class Solution {\n    function minBitwiseArray($nums) {\n        $ans =\
        \ array();\n        foreach ($nums as $num) {\n            if ($num % 2 == 0)\
        \ {\n                array_push($ans, -1);\n            } else {\n         \
        \       $x = $num;\n                while (($x | ($x + 1)) != $num) {\n    \
        \                $x--;\n                }\n                array_push($ans,\
        \ $x);\n            }\n        }\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func minBitwiseArray(_ nums: [Int]) -> [Int] {\n\
        \        var ans: [Int] = []\n        for num in nums {\n            if num\
        \ % 2 == 0 {\n                ans.append(-1)\n            } else {\n       \
        \         var x = num\n                while (x | (x + 1)) != num {\n      \
        \              x -= 1\n                }\n                ans.append(x)\n  \
        \          }\n        }\n        return ans\n    }\n}"
      kotlin: "class Solution {\n    fun minBitwiseArray(nums: List<Int>): IntArray\
        \ {\n        return nums.map { num ->\n            if (num % 2 == 0) -1\n  \
        \          else num - 1\n        }.toIntArray()\n    }\n}"
      dart: "class Solution {\n  List<int> minBitwiseArray(List<int> nums) {\n    return\
        \ nums.map((num) => num % 2 == 0 ? -1 : num - 1).toList();\n  }\n}"
      go: "func minBitwiseArray(nums []int) []int {\n    ans := make([]int, len(nums))\n\
        \    for i, num := range nums {\n        if num%2 == 0 {\n            ans[i]\
        \ = -1\n        } else {\n            ans[i] = num - 1\n        }\n    }\n \
        \   return ans\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer[]}\ndef min_bitwise_array(nums)\n\
        \    nums.map do |num|\n        num.even? ? -1 : num - 1\n    end\nend"
      scala: "object Solution {\n    def minBitwiseArray(nums: List[Int]): Array[Int]\
        \ = {\n        nums.map(num => if (num % 2 == 0) -1 else num - 1).toArray\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32>\
        \ {\n        nums.into_iter().map(|num| if num % 2 == 0 { -1 } else { num -\
        \ 1 }).collect()\n    }\n}"
      racket: "(define/contract (min-bitwise-array nums)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?))\n  (map (lambda (num) (if (even? num) -1 (- num 1)))\
        \ nums))"
      erlang: "-spec min_bitwise_array(Nums :: [integer()]) -> [integer()].\nmin_bitwise_array(Nums)\
        \ ->\n    lists:map(fun(N) when N rem 2 == 0 -> -1; (N) -> N - 1 end, Nums)."
      elixir: "defmodule Solution do\n  @spec min_bitwise_array(nums :: [integer]) ::\
        \ [integer]\n  def min_bitwise_array(nums) do\n    Enum.map(nums, fn num ->\
        \ if rem(num, 2) == 0, do: -1, else: num - 1 end)\n  end\nend"
    approach: 'The problem requires constructing an array ans of length n, such that
      for each index i, the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i].
      To solve this problem, we can iterate over each number in the input array and
      find the smallest number that satisfies the condition. We can use the fact that
      the bitwise OR of a number and the number plus one will have all the bits set
      to the right of the rightmost set bit in the number. Therefore, we can start from
      the number itself and keep subtracting the rightmost set bit until we find a number
      that satisfies the condition.


      The key intuition here is to understand how the bitwise OR operation works and
      how it can be used to find the smallest number that satisfies the condition. We
      can use bitwise operations to find the rightmost set bit in a number and then
      subtract it from the number. This process can be repeated until we find a number
      that satisfies the condition. If no such number is found, we can set ans[i] to
      -1 to indicate that it is not possible to find a value for ans[i] that satisfies
      the condition.'
    time_complexity: O(n log m) where n is the length of the input array and m is the
      maximum value in the array. This is because for each number in the input array,
      we are performing a constant amount of work to find the smallest number that satisfies
      the condition. The work involves iterating over the bits of the number, which
      takes O(log m) time. Therefore, the overall time complexity is O(n log m).
    space_complexity: O(n) where n is the length of the input array. This is because
      we need to store the result for each number in the input array. The space complexity
      is linear because we are using a constant amount of space to store each result.
    elapsed_time: 5.254392147064209
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-21 19:53:31 '
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
  <small class="solution-timestamp">(2026-01-22 02:33:31 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to find the minimum `ans[i]` for each `nums[i]` such that `ans[i] OR (ans[i] + 1) == nums[i]`. We analyze the bitwise OR operation `x OR (x + 1)`. If `x` is an even number, its least significant bit (LSB) is 0. Then `x = ...0` and `x + 1 = ...1`. Their bitwise OR, `x OR (x + 1)`, will always have its LSB as 1, making it an odd number. Therefore, if `nums[i]` is even, no `ans[i]` can satisfy the condition, and we set `ans[i] = -1`. This covers the case where `nums[i] = 2` (the only even prime).

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
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-kotlin-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-dart-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-go-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-ruby-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-scala-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-rust-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-racket-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-erlang-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-elixir-gemini-2-5-flash">
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
    <label for="lang-kotlin-gemini-2-5-flash">Kotlin</label>
    <label for="lang-dart-gemini-2-5-flash">Dart</label>
    <label for="lang-go-gemini-2-5-flash">Go</label>
    <label for="lang-ruby-gemini-2-5-flash">Ruby</label>
    <label for="lang-scala-gemini-2-5-flash">Scala</label>
    <label for="lang-rust-gemini-2-5-flash">Rust</label>
    <label for="lang-racket-gemini-2-5-flash">Racket</label>
    <label for="lang-erlang-gemini-2-5-flash">Erlang</label>
    <label for="lang-elixir-gemini-2-5-flash">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
#include <vector>
#include <numeric>

class Solution {
public:
    int countTrailingOnes(int n) {
        int count = 0;
        while ((n & 1) == 1) {
            n >>= 1;
            count++;
        }
        return count;
    }

    std::vector<int> minBitwiseArray(std::vector<int>& nums) {
        std::vector<int> ans;
        ans.reserve(nums.size());

        for (int num : nums) {
            if (num % 2 == 0) {
                ans.push_back(-1);
            } else {
                int c = countTrailingOnes(num);
                int result = num - (1 << (c - 1));
                ans.push_back(result);
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
import java.util.ArrayList;
import java.util.List;

class Solution {
    private int countTrailingOnes(int n) {
        int count = 0;
        while ((n & 1) == 1) {
            n >>= 1;
            count++;
        }
        return count;
    }

    public int[] minBitwiseArray(List<Integer> nums) {
        int[] ans = new int[nums.size()];

        for (int i = 0; i < nums.size(); i++) {
            int num = nums.get(i);
            if (num % 2 == 0) {
                ans[i] = -1;
            } else {
                int c = countTrailingOnes(num);
                int result = num - (1 << (c - 1));
                ans[i] = result;
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
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:
            if num % 2 == 0:
                ans.append(-1)
            else:
                c = 0
                temp_num = num
                while (temp_num & 1) == 1:
                    temp_num >>= 1
                    c += 1

                result = num - (1 << (c - 1))
                ans.append(result)
        return ans
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
                c = 0
                temp_num = num
                while (temp_num & 1) == 1:
                    temp_num >>= 1
                    c += 1

                result = num - (1 << (c - 1))
                ans.append(result)
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

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
            int c = 0;
            int temp_num = num;
            while ((temp_num & 1) == 1) {
                temp_num >>= 1;
                c++;
            }

            int result = num - (1 << (c - 1));
            ans[i] = result;
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
                int c = 0;
                int tempNum = num;
                while ((tempNum & 1) == 1) {
                    tempNum >>= 1;
                    c++;
                }

                int result = num - (1 << (c - 1));
                ans[i] = result;
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
            let c = 0;
            let tempNum = num;
            while ((tempNum & 1) === 1) {
                tempNum >>= 1;
                c++;
            }

            const result = num - (1 << (c - 1));
            ans.push(result);
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
            let c = 0;
            let tempNum = num;
            while ((tempNum & 1) === 1) {
                tempNum >>= 1;
                c++;
            }

            const result = num - (1 << (c - 1));
            ans.push(result);
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
<?php

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
                $c = 0;
                $tempNum = $num;
                while (($tempNum & 1) == 1) {
                    $tempNum >>= 1;
                    $c++;
                }

                $result = $num - (1 << ($c - 1));
                $ans[] = $result;
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
import Foundation

class Solution {
    func minBitwiseArray(_ nums: [Int]) -> [Int] {
        var ans: [Int] = []
        ans.reserveCapacity(nums.count)

        for num in nums {
            if num % 2 == 0 {
                ans.append(-1)
            } else {
                var c = 0
                var tempNum = num
                while (tempNum & 1) == 1 {
                    tempNum >>= 1
                    c += 1
                }

                let result = num - (1 << (c - 1))
                ans.append(result)
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
        val ans = IntArray(nums.size)
        for (i in nums.indices) {
            val num = nums[i]
            if (num % 2 == 0) {
                ans[i] = -1
            } else {
                var k0 = 0
                while ((num shr k0) and 1 == 1) {
                    k0++
                }
                ans[i] = num xor (1 shl (k0 - 1))
            }
        }
        return ans
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
    List<int> ans = List<int>.filled(nums.length, 0);
    for (int i = 0; i < nums.length; i++) {
      int num = nums[i];
      if (num % 2 == 0) {
        ans[i] = -1;
      } else {
        int k0 = 0;
        while (((num >> k0) & 1) == 1) {
          k0++;
        }
        ans[i] = num ^ (1 << (k0 - 1));
      }
    }
    return ans;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minBitwiseArray(nums []int) []int {
    ans := make([]int, len(nums))
    for i, num := range nums {
        if num % 2 == 0 {
            ans[i] = -1
        } else {
            k0 := 0
            for ((num >> k0) & 1) == 1 {
                k0++
            }
            ans[i] = num ^ (1 << (k0 - 1))
        }
    }
    return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer[]}
def min_bitwise_array(nums)
    ans = []
    nums.each do |num|
        if num % 2 == 0
            ans << -1
        else
            k0 = 0
            while ((num >> k0) & 1) == 1
                k0 += 1
            end
            ans << (num ^ (1 << (k0 - 1)))
        end
    end
    ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minBitwiseArray(nums: List[Int]): Array[Int] = {
        val ans = Array.ofDim[Int](nums.length)
        for (i <- nums.indices) {
            val num = nums(i)
            if (num % 2 == 0) {
                ans(i) = -1
            } else {
                var k0 = 0
                while (((num >> k0) & 1) == 1) {
                    k0 += 1
                }
                ans(i) = num ^ (1 << (k0 - 1))
            }
        }
        ans
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
        let mut ans: Vec<i32> = Vec::with_capacity(nums.len());
        for num in nums {
            if num % 2 == 0 {
                ans.push(-1);
            } else {
                let mut k0 = 0;
                while ((num >> k0) & 1) == 1 {
                    k0 += 1;
                }
                ans.push(num ^ (1 << (k0 - 1)));
            }
        }
        ans
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
  (map (lambda (num)
         (if (even? num)
             -1
             (let loop ((k0 0))
               (if (= (bitwise-and (bitwise-rshift num k0) 1) 1)
                   (loop (+ k0 1))
                   (bitwise-xor num (bitwise-lshift 1 (- k0 1)))))))
       nums))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_bitwise_array(Nums :: [integer()]) -> [integer()].
min_bitwise_array(Nums) ->
  lists:map(fun(Num) ->
                if
                    Num rem 2 == 0 ->
                        -1;
                    true ->
                        k0_loop(Num, 0)
                end
            end, Nums).

k0_loop(Num, K0) ->
    if
        (bsr(Num, K0) band 1) == 1 ->
            k0_loop(Num, K0 + 1);
        true ->
            Num bxor (1 bsl (K0 - 1))
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_bitwise_array(nums :: [integer]) :: [integer]
  def min_bitwise_array(nums) do
    Enum.map(nums, fn num ->
      if rem(num, 2) == 0 do
        -1
      else
        k0 = find_k0(num, 0)
        Bitwise.bxor(num, Bitwise.bsl(1, k0 - 1))
      end
    end)
  end

  defp find_k0(num, k0) do
    if Bitwise.band(Bitwise.bsr(num, k0), 1) == 1 do
      find_k0(num, k0 + 1)
    else
      k0
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N * log(max_val)) where N is the length of the `nums` array and `max_val` is the maximum value in `nums`. For each number in `nums`, we perform a constant number of arithmetic operations and a loop to count trailing ones. This loop iterates at most `log(max_val)` times (approximately 30 for `10^9`).

- **Space Complexity:** The space complexity is O(N) to store the `ans` array, where N is the length of the `nums` array. No additional data structures are used that scale with the input values.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-21 19:53:31 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires constructing an array ans of length n, such that for each index i, the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i]. To solve this problem, we can iterate over each number in the input array and find the smallest number that satisfies the condition. We can use the fact that the bitwise OR of a number and the number plus one will have all the bits set to the right of the rightmost set bit in the number. Therefore, we can start from the number itself and keep subtracting the rightmost set bit until we find a number that satisfies the condition.

The key intuition here is to understand how the bitwise OR operation works and how it can be used to find the smallest number that satisfies the condition. We can use bitwise operations to find the rightmost set bit in a number and then subtract it from the number. This process can be repeated until we find a number that satisfies the condition. If no such number is found, we can set ans[i] to -1 to indicate that it is not possible to find a value for ans[i] that satisfies the condition.

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
                    x--;
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
                    x--;
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
                    x -= 1
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
                    x -= 1
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
                x--;
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
                    x--;
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
                x--;
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
                x--;
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
        $ans = array();
        foreach ($nums as $num) {
            if ($num % 2 == 0) {
                array_push($ans, -1);
            } else {
                $x = $num;
                while (($x | ($x + 1)) != $num) {
                    $x--;
                }
                array_push($ans, $x);
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
                    x -= 1
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
        return nums.map { num ->
            if (num % 2 == 0) -1
            else num - 1
        }.toIntArray()
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
    return nums.map((num) => num % 2 == 0 ? -1 : num - 1).toList();
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minBitwiseArray(nums []int) []int {
    ans := make([]int, len(nums))
    for i, num := range nums {
        if num%2 == 0 {
            ans[i] = -1
        } else {
            ans[i] = num - 1
        }
    }
    return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer[]}
def min_bitwise_array(nums)
    nums.map do |num|
        num.even? ? -1 : num - 1
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minBitwiseArray(nums: List[Int]): Array[Int] = {
        nums.map(num => if (num % 2 == 0) -1 else num - 1).toArray
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
        nums.into_iter().map(|num| if num % 2 == 0 { -1 } else { num - 1 }).collect()
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
  (map (lambda (num) (if (even? num) -1 (- num 1))) nums))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_bitwise_array(Nums :: [integer()]) -> [integer()].
min_bitwise_array(Nums) ->
    lists:map(fun(N) when N rem 2 == 0 -> -1; (N) -> N - 1 end, Nums).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_bitwise_array(nums :: [integer]) :: [integer]
  def min_bitwise_array(nums) do
    Enum.map(nums, fn num -> if rem(num, 2) == 0, do: -1, else: num - 1 end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log m) where n is the length of the input array and m is the maximum value in the array. This is because for each number in the input array, we are performing a constant amount of work to find the smallest number that satisfies the condition. The work involves iterating over the bits of the number, which takes O(log m) time. Therefore, the overall time complexity is O(n log m).

- **Space Complexity:** O(n) where n is the length of the input array. This is because we need to store the result for each number in the input array. The space complexity is linear because we are using a constant amount of space to store each result.

</div>
</details>
