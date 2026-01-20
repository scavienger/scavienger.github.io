---
layout: post
title: "Construct the Minimum Bitwise Array I"
date: 2026-01-20 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Bit Manipulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    std::vector<int> minBitwiseArray(std::vector<int>&\
        \ nums) {\n        std::vector<int> ans;\n        for (int target : nums) {\n\
        \            int found_x = -1;\n            for (int x = 0; x < target; ++x)\
        \ {\n                if ((x | (x + 1)) == target) {\n                    found_x\
        \ = x;\n                    break;\n                }\n            }\n     \
        \       ans.push_back(found_x);\n        }\n        return ans;\n    }\n};"
      java: "import java.util.List;\nimport java.util.ArrayList;\n\nclass Solution {\n\
        \    public int[] minBitwiseArray(List<Integer> nums) {\n        int[] ans =\
        \ new int[nums.size()];\n        for (int i = 0; i < nums.size(); ++i) {\n \
        \           int target = nums.get(i);\n            int found_x = -1;\n     \
        \       for (int x = 0; x < target; ++x) {\n                if ((x | (x + 1))\
        \ == target) {\n                    found_x = x;\n                    break;\n\
        \                }\n            }\n            ans[i] = found_x;\n        }\n\
        \        return ans;\n    }\n}"
      python: "class Solution(object):\n    def minBitwiseArray(self, nums):\n     \
        \   \"\"\"\n        :type nums: List[int]\n        :rtype: List[int]\n     \
        \   \"\"\"\n        ans = []\n        for target in nums:\n            found_x\
        \ = -1\n            for x in range(target):\n                if (x | (x + 1))\
        \ == target:\n                    found_x = x\n                    break\n \
        \           ans.append(found_x)\n        return ans"
      python3: "class Solution:\n    def minBitwiseArray(self, nums: List[int]) -> List[int]:\n\
        \        ans = []\n        for target in nums:\n            found_x = -1\n \
        \           for x in range(target):\n                if (x | (x + 1)) == target:\n\
        \                    found_x = x\n                    break\n            ans.append(found_x)\n\
        \        return ans"
      c: "#include <stdlib.h> // For malloc\n#include <stdbool.h> // For bool\n\n/**\n\
        \ * Note: The returned array must be malloced, assume caller calls free().\n\
        \ */\nint* minBitwiseArray(int* nums, int numsSize, int* returnSize) {\n   \
        \ int* ans = (int*)malloc(numsSize * sizeof(int));\n    *returnSize = numsSize;\n\
        \n    for (int i = 0; i < numsSize; ++i) {\n        int target = nums[i];\n\
        \        int found_x = -1;\n        for (int x = 0; x < target; ++x) {\n   \
        \         if ((x | (x + 1)) == target) {\n                found_x = x;\n   \
        \             break;\n            }\n        }\n        ans[i] = found_x;\n\
        \    }\n    return ans;\n}"
      csharp: "using System.Collections.Generic;\n\npublic class Solution {\n    public\
        \ int[] MinBitwiseArray(IList<int> nums) {\n        int[] ans = new int[nums.Count];\n\
        \        for (int i = 0; i < nums.Count; ++i) {\n            int target = nums[i];\n\
        \            int found_x = -1;\n            for (int x = 0; x < target; ++x)\
        \ {\n                if ((x | (x + 1)) == target) {\n                    found_x\
        \ = x;\n                    break;\n                }\n            }\n     \
        \       ans[i] = found_x;\n        }\n        return ans;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number[]}\n */\nvar minBitwiseArray\
        \ = function(nums) {\n    const ans = [];\n    for (let i = 0; i < nums.length;\
        \ ++i) {\n        const target = nums[i];\n        let found_x = -1;\n     \
        \   for (let x = 0; x < target; ++x) {\n            if ((x | (x + 1)) === target)\
        \ {\n                found_x = x;\n                break;\n            }\n \
        \       }\n        ans.push(found_x);\n    }\n    return ans;\n};"
      typescript: "function minBitwiseArray(nums: number[]): number[] {\n    const ans:\
        \ number[] = [];\n    for (let i = 0; i < nums.length; ++i) {\n        const\
        \ target = nums[i];\n        let found_x: number = -1;\n        for (let x =\
        \ 0; x < target; ++x) {\n            if ((x | (x + 1)) === target) {\n     \
        \           found_x = x;\n                break;\n            }\n        }\n\
        \        ans.push(found_x);\n    }\n    return ans;\n};"
      php: "<?php\n\nclass Solution {\n\n    /**\n     * @param Integer[] $nums\n  \
        \   * @return Integer[]\n     */\n    function minBitwiseArray($nums) {\n  \
        \      $ans = [];\n        foreach ($nums as $target) {\n            $found_x\
        \ = -1;\n            for ($x = 0; $x < $target; ++$x) {\n                if\
        \ (($x | ($x + 1)) === $target) {\n                    $found_x = $x;\n    \
        \                break;\n                }\n            }\n            $ans[]\
        \ = $found_x;\n        }\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func minBitwiseArray(_ nums: [Int]) -> [Int] {\n\
        \        var ans: [Int] = []\n        for target in nums {\n            var\
        \ foundX: Int = -1\n            for x in 0..<target {\n                if (x\
        \ | (x + 1)) == target {\n                    foundX = x\n                 \
        \   break\n                }\n            }\n            ans.append(foundX)\n\
        \        }\n        return ans\n    }\n}"
      kotlin: "class Solution {\n    fun minBitwiseArray(nums: List<Int>): IntArray\
        \ {\n        val ans = IntArray(nums.size)\n        for (i in nums.indices)\
        \ {\n            val n = nums[i]\n            if (n == 2) {\n              \
        \  ans[i] = -1\n            } else {\n                var foundX = -1\n    \
        \            for (x in 0..n) {\n                    if ((x or (x + 1)) == n)\
        \ {\n                        foundX = x\n                        break\n   \
        \                 }\n                }\n                ans[i] = foundX\n  \
        \          }\n        }\n        return ans\n    }\n}"
      dart: "class Solution {\n  List<int> minBitwiseArray(List<int> nums) {\n    List<int>\
        \ ans = List<int>.filled(nums.length, 0);\n    for (int i = 0; i < nums.length;\
        \ i++) {\n      int n = nums[i];\n      if (n == 2) {\n        ans[i] = -1;\n\
        \      } else {\n        int foundX = -1;\n        for (int x = 0; x <= n; x++)\
        \ {\n          if ((x | (x + 1)) == n) {\n            foundX = x;\n        \
        \    break;\n          }\n        }\n        ans[i] = foundX;\n      }\n   \
        \ }\n    return ans;\n  }\n}"
      go: "func minBitwiseArray(nums []int) []int {\n    ans := make([]int, len(nums))\n\
        \    for i, n := range nums {\n        if n == 2 {\n            ans[i] = -1\n\
        \        } else {\n            foundX := -1\n            for x := 0; x <= n;\
        \ x++ {\n                if (x | (x + 1)) == n {\n                    foundX\
        \ = x\n                    break\n                }\n            }\n       \
        \     ans[i] = foundX\n        }\n    }\n    return ans\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer[]}\ndef min_bitwise_array(nums)\n\
        \    ans = Array.new(nums.length)\n    nums.each_with_index do |n, i|\n    \
        \    if n == 2\n            ans[i] = -1\n        else\n            found_x =\
        \ -1\n            (0..n).each do |x|\n                if (x | (x + 1)) == n\n\
        \                    found_x = x\n                    break\n              \
        \  end\n            end\n            ans[i] = found_x\n        end\n    end\n\
        \    ans\nend"
      scala: "object Solution {\n    def minBitwiseArray(nums: List[Int]): Array[Int]\
        \ = {\n        val ans = Array.ofDim[Int](nums.length)\n        for (i <- nums.indices)\
        \ {\n            val n = nums(i)\n            if (n == 2) {\n              \
        \  ans(i) = -1\n            } else {\n                var foundX = -1\n    \
        \            var x = 0\n                while (x <= n) {\n                 \
        \   if ((x | (x + 1)) == n) {\n                        foundX = x\n        \
        \                break\n                    }\n                    x += 1\n\
        \                }\n                ans(i) = foundX\n            }\n       \
        \ }\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32>\
        \ {\n        let mut ans = Vec::with_capacity(nums.len());\n        for &n in\
        \ nums.iter() {\n            if n == 2 {\n                ans.push(-1);\n  \
        \          } else {\n                let mut found_x = -1;\n               \
        \ for x in 0..=n {\n                    if (x | (x + 1)) == n {\n          \
        \              found_x = x;\n                        break;\n              \
        \      }\n                }\n                ans.push(found_x);\n          \
        \  }\n        }\n        ans\n    }\n}"
      racket: "(define/contract (min-bitwise-array nums)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?))\n  (map (lambda (n)\n         (if (= n 2)\n     \
        \        -1\n             (let loop ([x 0])\n               (if (> x n)\n  \
        \                 -1 ; This case should not be reached for odd primes as a solution\
        \ always exists.\n                   (if (= (bitwise-ior x (+ x 1)) n)\n   \
        \                    x\n                       (loop (+ x 1)))))))\n       nums))"
      erlang: "-spec min_bitwise_array(Nums :: [integer()]) -> [integer()].\nmin_bitwise_array(Nums)\
        \ ->\n  lists:map(fun(N) ->\n    if\n      N == 2 ->\n        -1;\n      true\
        \ ->\n        find_min_x(0, N)\n    end\n  end, Nums).\n\nfind_min_x(X, N) when\
        \ X =< N ->\n  case (X bor (X + 1)) of\n    N -> X;\n    _ -> find_min_x(X +\
        \ 1, N)\n  end;\nfind_min_x(_, _) ->\n  -1. %% This case should not be reached\
        \ for odd primes as a solution always exists."
      elixir: "defmodule Solution do\n  @spec min_bitwise_array(nums :: [integer]) ::\
        \ [integer]\n  def min_bitwise_array(nums) do\n    Enum.map(nums, fn n ->\n\
        \      if n == 2 do\n        -1\n      else\n        find_min_x(0, n)\n    \
        \  end\n    end)\n  end\n\n  defp find_min_x(x, n) when x <= n do\n    if (x\
        \ ||| (x + 1)) == n do\n      x\n    else\n      find_min_x(x + 1, n)\n    end\n\
        \  end\n\n  defp find_min_x(_x, _n), do: -1 # This case should not be reached\
        \ for odd primes as a solution always exists.\nend"
    approach: 'The problem requires constructing an array `ans` where for each `nums[i]`,
      `ans[i] OR (ans[i] + 1)` equals `nums[i]`, and `ans[i]` must be minimized. If
      no such `ans[i]` exists, it should be -1. The constraints state that `nums[i]`
      are prime numbers between 2 and 1000.


      We observe the property of the bitwise OR operation `x OR (x + 1)`. If `x` is
      even, its least significant bit (LSB) is 0, so `x = ...0_2` and `x + 1 = ...1_2`.
      Their OR is `...1_2`, meaning `x OR (x + 1)` will have its LSB set to 1. If `x`
      is odd, its LSB is 1. Let `x = A01...1_2` (where `A` is a prefix, `0` is the rightmost
      zero bit, and `1...1` are `k` ones). Then `x + 1 = A10...0_2`. Their OR is `A11...1_2`,
      which also has its LSB set to 1. In both cases, the result `x OR (x + 1)` always
      has its LSB set to 1. This implies that if `nums[i]` is an even number, no solution
      `ans[i]` can exist, so `ans[i]` must be -1. Since `nums[i]` are prime, the only
      even prime is 2. Thus, for `nums[i] = 2`, `ans[i]` is -1. For any other prime
      `nums[i]` (which must be odd), a solution `ans[i]` is guaranteed to exist (e.g.,
      `nums[i] - 1` is always a valid candidate, though not necessarily the smallest).
      To find the minimum `ans[i]`, we can iterate `x` starting from 0 up to `nums[i]`
      and check the condition `(x OR (x + 1)) == nums[i]`. The first `x` that satisfies
      this condition will be the minimum.'
    time_complexity: The time complexity is O(N_len * N_max), where N_len is the length
      of the `nums` array and N_max is the maximum value in `nums`. For each number
      in `nums`, we iterate `x` from 0 up to `nums[i]` (at most `N_max`) to find the
      smallest `ans[i]`. The bitwise OR operation takes constant time. Given `N_len
      <= 100` and `N_max <= 1000`, the total operations are approximately `100 * 1000
      = 10^5`, which is very efficient and well within typical time limits.
    space_complexity: The space complexity is O(N_len), where N_len is the length of
      the `nums` array. This is because we need to store the `ans` array, which has
      the same length as `nums`. No additional data structures are used that scale with
      the input values beyond the output array itself.
    elapsed_time: 113.88942694664001
    model: gemini-2.5-flash
    generated_at: '2026-01-20 01:11:04 '
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> minBitwiseArray(vector<int>&\
        \ nums) {\n        vector<int> ans;\n        for (int num : nums) {\n      \
        \      int val = -1;\n            for (int i = 0; i < num; i++) {\n        \
        \        if ((i | (i + 1)) == num) {\n                    val = i;\n       \
        \             break;\n                }\n            }\n            ans.push_back(val);\n\
        \        }\n        return ans;\n    }\n};"
      java: "class Solution {\n    public int[] minBitwiseArray(List<Integer> nums)\
        \ {\n        int[] ans = new int[nums.size()];\n        for (int i = 0; i <\
        \ nums.size(); i++) {\n            int num = nums.get(i);\n            int val\
        \ = -1;\n            for (int j = 0; j < num; j++) {\n                if ((j\
        \ | (j + 1)) == num) {\n                    val = j;\n                    break;\n\
        \                }\n            }\n            ans[i] = val;\n        }\n  \
        \      return ans;\n    }\n}"
      python: "class Solution(object):\n    def minBitwiseArray(self, nums):\n     \
        \   ans = []\n        for num in nums:\n            val = -1\n            for\
        \ i in range(num):\n                if (i | (i + 1)) == num:\n             \
        \       val = i\n                    break\n            ans.append(val)\n  \
        \      return ans"
      python3: "class Solution:\n    def minBitwiseArray(self, nums: list[int]) -> list[int]:\n\
        \        ans = []\n        for num in nums:\n            val = -1\n        \
        \    for i in range(num):\n                if (i | (i + 1)) == num:\n      \
        \              val = i\n                    break\n            ans.append(val)\n\
        \        return ans"
      c: "int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {\n    int*\
        \ ans = (int*)malloc(numsSize * sizeof(int));\n    *returnSize = numsSize;\n\
        \    for (int i = 0; i < numsSize; i++) {\n        int num = nums[i];\n    \
        \    int val = -1;\n        for (int j = 0; j < num; j++) {\n            if\
        \ ((j | (j + 1)) == num) {\n                val = j;\n                break;\n\
        \            }\n        }\n        ans[i] = val;\n    }\n    return ans;\n}"
      csharp: "public class Solution {\n    public int[] MinBitwiseArray(IList<int>\
        \ nums) {\n        int[] ans = new int[nums.Count];\n        for (int i = 0;\
        \ i < nums.Count; i++) {\n            int num = nums[i];\n            int val\
        \ = -1;\n            for (int j = 0; j < num; j++) {\n                if ((j\
        \ | (j + 1)) == num) {\n                    val = j;\n                    break;\n\
        \                }\n            }\n            ans[i] = val;\n        }\n  \
        \      return ans;\n    }\n}"
      javascript: "var minBitwiseArray = function(nums) {\n    let ans = [];\n    for\
        \ (let num of nums) {\n        let val = -1;\n        for (let i = 0; i < num;\
        \ i++) {\n            if ((i | (i + 1)) === num) {\n                val = i;\n\
        \                break;\n            }\n        }\n        ans.push(val);\n\
        \    }\n    return ans;\n};"
      typescript: "function minBitwiseArray(nums: number[]): number[] {\n    let ans:\
        \ number[] = [];\n    for (let num of nums) {\n        let val: number = -1;\n\
        \        for (let i = 0; i < num; i++) {\n            if ((i | (i + 1)) ===\
        \ num) {\n                val = i;\n                break;\n            }\n\
        \        }\n        ans.push(val);\n    }\n    return ans;\n}"
      php: "class Solution {\n    function minBitwiseArray($nums) {\n        $ans =\
        \ [];\n        foreach ($nums as $num) {\n            $val = -1;\n         \
        \   for ($i = 0; $i < $num; $i++) {\n                if (($i | ($i + 1)) ==\
        \ $num) {\n                    $val = $i;\n                    break;\n    \
        \            }\n            }\n            $ans[] = $val;\n        }\n     \
        \   return $ans;\n    }\n}"
      swift: "class Solution {\n    func minBitwiseArray(_ nums: [Int]) -> [Int] {\n\
        \        var ans: [Int] = []\n        for num in nums {\n            var val\
        \ = -1\n            for i in 0..<num {\n                if (i | (i + 1)) ==\
        \ num {\n                    val = i\n                    break\n          \
        \      }\n            }\n            ans.append(val)\n        }\n        return\
        \ ans\n    }\n}"
      kotlin: "class Solution {\n    fun minBitwiseArray(nums: List<Int>): IntArray\
        \ {\n        val result = IntArray(nums.size)\n        for (i in nums.indices)\
        \ {\n            var found = false\n            for (j in 0 until nums[i]) {\n\
        \                if ((j or (j + 1)) == nums[i]) {\n                    result[i]\
        \ = j\n                    found = true\n                    break\n       \
        \         }\n            }\n            if (!found) result[i] = -1\n       \
        \ }\n        return result\n    }\n}"
      dart: "class Solution {\n  List<int> minBitwiseArray(List<int> nums) {\n    List<int>\
        \ result = List<int>.filled(nums.length, 0);\n    for (int i = 0; i < nums.length;\
        \ i++) {\n      bool found = false;\n      for (int j = 0; j < nums[i]; j++)\
        \ {\n        if ((j | (j + 1)) == nums[i]) {\n          result[i] = j;\n   \
        \       found = true;\n          break;\n        }\n      }\n      if (!found)\
        \ result[i] = -1;\n    }\n    return result;\n  }\n}"
      go: "func minBitwiseArray(nums []int) []int {\n    result := make([]int, len(nums))\n\
        \    for i, num := range nums {\n        found := false\n        for j := 0;\
        \ j < num; j++ {\n            if (j | (j + 1)) == num {\n                result[i]\
        \ = j\n                found = true\n                break\n            }\n\
        \        }\n        if !found {\n            result[i] = -1\n        }\n   \
        \ }\n    return result\n}"
      ruby: "def min_bitwise_array(nums)\n    result = Array.new(nums.size, 0)\n   \
        \ nums.each_with_index do |num, i|\n        found = false\n        (0...num).each\
        \ do |j|\n            if (j | (j + 1)) == num\n                result[i] = j\n\
        \                found = true\n                break\n            end\n    \
        \    end\n        result[i] = -1 if !found\n    end\n    result\nend"
      scala: "object Solution {\n    def minBitwiseArray(nums: List[Int]): Array[Int]\
        \ = {\n        val result = Array.ofDim[Int](nums.size)\n        for (i <- nums.indices)\
        \ {\n            var found = false\n            for (j <- 0 until nums(i)) {\n\
        \                if ((j | (j + 1)) == nums(i)) {\n                    result(i)\
        \ = j\n                    found = true\n                    sys.exit()\n  \
        \              }\n            }\n            if (!found) result(i) = -1\n  \
        \      }\n        result\n    }\n}"
      rust: "impl Solution {\n    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32>\
        \ {\n        let mut result = vec![0; nums.len()];\n        for (i, &num) in\
        \ nums.iter().enumerate() {\n            let mut found = false;\n          \
        \  for j in 0..num {\n                if (j | (j + 1)) == num {\n          \
        \          result[i] = j;\n                    found = true;\n             \
        \       break;\n                }\n            }\n            if !found {\n\
        \                result[i] = -1;\n            }\n        }\n        result\n\
        \    }\n}"
      racket: "(define/contract (min-bitwise-array nums)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?))\n  (let ([result (make-list (length nums) 0)])\n\
        \    (for ([i (in-range (length nums))])\n      (let ([num (list-ref nums i)])\n\
        \        (let loop ([j 0])\n          (cond\n            [(= j num) (list-set!\
        \ result i -1)]\n            [(= (bitwise-ior j (+ j 1)) num) (list-set! result\
        \ i j)]\n            [else (loop (+ j 1))]))))\n    result))"
      erlang: "-module(solution).\n-export([min_bitwise_array/1]).\nmin_bitwise_array(Nums)\
        \ ->\n    lists:map(fun(X) ->\n        case lists:foldl(fun(Y, Acc) ->\n   \
        \         case (Y bor (Y + 1)) of\n                X -> Y;\n               \
        \ _ -> Acc\n            end\n        end, -1, lists:seq(0, X - 1)) of\n    \
        \        -1 -> -1;\n            Val -> Val\n        end\n    end, Nums)."
      elixir: "defmodule Solution do\n  @spec min_bitwise_array(nums :: [integer]) ::\
        \ [integer]\n  def min_bitwise_array(nums) do\n    Enum.map(nums, fn num ->\n\
        \      case Enum.find(0..(num - 1), fn x -> (x ||| (x + 1)) == num) do\n   \
        \     nil -> -1\n        val -> val\n      end\n    end)\n  end\nend"
    approach: 'The problem requires constructing an array ans of length n, such that
      for each index i, the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i].
      To solve this, we can iterate over all possible values for ans[i] and check if
      the condition is satisfied. We start from 0 and go up to nums[i] - 1, and for
      each value, we check if the bitwise OR of the value and the value plus one is
      equal to nums[i]. If we find such a value, we add it to the ans array. If we don''t
      find any such value, we add -1 to the ans array. This approach ensures that we
      find the smallest possible value for ans[i] that satisfies the condition.


      The key intuition behind this approach is that the bitwise OR operation has a
      property that a | (a + 1) will always result in a value that has all the bits
      set to the right of the rightmost set bit in a. This means that if we want a |
      (a + 1) to be equal to a prime number, a must have all the bits set to the right
      of the rightmost set bit in the prime number. This property helps us to quickly
      find the smallest possible value for ans[i] that satisfies the condition.'
    time_complexity: The time complexity of this solution is O(n * m), where n is the
      length of the input array and m is the maximum value in the input array. This
      is because for each element in the input array, we are iterating up to the value
      of the element to find the smallest possible value that satisfies the condition.
    space_complexity: The space complexity of this solution is O(n), where n is the
      length of the input array. This is because we are storing the result in an array
      of the same length as the input array.
    elapsed_time: 7.003205299377441
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-20 01:11:16 '
---

## Problem #3314: Construct the Minimum Bitwise Array I

**Difficulty:** Easy

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
	<li><code>2 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>nums[i]</code> is a prime number.</li>
</ul>


## Hints

1. The constraints are small, allowing you to iterate over all potential values for `ans[i]` directly.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-20 01:11:04 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires constructing an array `ans` where for each `nums[i]`, `ans[i] OR (ans[i] + 1)` equals `nums[i]`, and `ans[i]` must be minimized. If no such `ans[i]` exists, it should be -1. The constraints state that `nums[i]` are prime numbers between 2 and 1000.

We observe the property of the bitwise OR operation `x OR (x + 1)`. If `x` is even, its least significant bit (LSB) is 0, so `x = ...0_2` and `x + 1 = ...1_2`. Their OR is `...1_2`, meaning `x OR (x + 1)` will have its LSB set to 1. If `x` is odd, its LSB is 1. Let `x = A01...1_2` (where `A` is a prefix, `0` is the rightmost zero bit, and `1...1` are `k` ones). Then `x + 1 = A10...0_2`. Their OR is `A11...1_2`, which also has its LSB set to 1. In both cases, the result `x OR (x + 1)` always has its LSB set to 1. This implies that if `nums[i]` is an even number, no solution `ans[i]` can exist, so `ans[i]` must be -1. Since `nums[i]` are prime, the only even prime is 2. Thus, for `nums[i] = 2`, `ans[i]` is -1. For any other prime `nums[i]` (which must be odd), a solution `ans[i]` is guaranteed to exist (e.g., `nums[i] - 1` is always a valid candidate, though not necessarily the smallest). To find the minimum `ans[i]`, we can iterate `x` starting from 0 up to `nums[i]` and check the condition `(x OR (x + 1)) == nums[i]`. The first `x` that satisfies this condition will be the minimum.

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
class Solution {
public:
    std::vector<int> minBitwiseArray(std::vector<int>& nums) {
        std::vector<int> ans;
        for (int target : nums) {
            int found_x = -1;
            for (int x = 0; x < target; ++x) {
                if ((x | (x + 1)) == target) {
                    found_x = x;
                    break;
                }
            }
            ans.push_back(found_x);
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
        for (int i = 0; i < nums.size(); ++i) {
            int target = nums.get(i);
            int found_x = -1;
            for (int x = 0; x < target; ++x) {
                if ((x | (x + 1)) == target) {
                    found_x = x;
                    break;
                }
            }
            ans[i] = found_x;
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
        for target in nums:
            found_x = -1
            for x in range(target):
                if (x | (x + 1)) == target:
                    found_x = x
                    break
            ans.append(found_x)
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
        for target in nums:
            found_x = -1
            for x in range(target):
                if (x | (x + 1)) == target:
                    found_x = x
                    break
            ans.append(found_x)
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h> // For malloc
#include <stdbool.h> // For bool

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc(numsSize * sizeof(int));
    *returnSize = numsSize;

    for (int i = 0; i < numsSize; ++i) {
        int target = nums[i];
        int found_x = -1;
        for (int x = 0; x < target; ++x) {
            if ((x | (x + 1)) == target) {
                found_x = x;
                break;
            }
        }
        ans[i] = found_x;
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Collections.Generic;

public class Solution {
    public int[] MinBitwiseArray(IList<int> nums) {
        int[] ans = new int[nums.Count];
        for (int i = 0; i < nums.Count; ++i) {
            int target = nums[i];
            int found_x = -1;
            for (int x = 0; x < target; ++x) {
                if ((x | (x + 1)) == target) {
                    found_x = x;
                    break;
                }
            }
            ans[i] = found_x;
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
    for (let i = 0; i < nums.length; ++i) {
        const target = nums[i];
        let found_x = -1;
        for (let x = 0; x < target; ++x) {
            if ((x | (x + 1)) === target) {
                found_x = x;
                break;
            }
        }
        ans.push(found_x);
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
    for (let i = 0; i < nums.length; ++i) {
        const target = nums[i];
        let found_x: number = -1;
        for (let x = 0; x < target; ++x) {
            if ((x | (x + 1)) === target) {
                found_x = x;
                break;
            }
        }
        ans.push(found_x);
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
        foreach ($nums as $target) {
            $found_x = -1;
            for ($x = 0; $x < $target; ++$x) {
                if (($x | ($x + 1)) === $target) {
                    $found_x = $x;
                    break;
                }
            }
            $ans[] = $found_x;
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
        for target in nums {
            var foundX: Int = -1
            for x in 0..<target {
                if (x | (x + 1)) == target {
                    foundX = x
                    break
                }
            }
            ans.append(foundX)
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
            val n = nums[i]
            if (n == 2) {
                ans[i] = -1
            } else {
                var foundX = -1
                for (x in 0..n) {
                    if ((x or (x + 1)) == n) {
                        foundX = x
                        break
                    }
                }
                ans[i] = foundX
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
      int n = nums[i];
      if (n == 2) {
        ans[i] = -1;
      } else {
        int foundX = -1;
        for (int x = 0; x <= n; x++) {
          if ((x | (x + 1)) == n) {
            foundX = x;
            break;
          }
        }
        ans[i] = foundX;
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
    for i, n := range nums {
        if n == 2 {
            ans[i] = -1
        } else {
            foundX := -1
            for x := 0; x <= n; x++ {
                if (x | (x + 1)) == n {
                    foundX = x
                    break
                }
            }
            ans[i] = foundX
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
    ans = Array.new(nums.length)
    nums.each_with_index do |n, i|
        if n == 2
            ans[i] = -1
        else
            found_x = -1
            (0..n).each do |x|
                if (x | (x + 1)) == n
                    found_x = x
                    break
                end
            end
            ans[i] = found_x
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
            val n = nums(i)
            if (n == 2) {
                ans(i) = -1
            } else {
                var foundX = -1
                var x = 0
                while (x <= n) {
                    if ((x | (x + 1)) == n) {
                        foundX = x
                        break
                    }
                    x += 1
                }
                ans(i) = foundX
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
        let mut ans = Vec::with_capacity(nums.len());
        for &n in nums.iter() {
            if n == 2 {
                ans.push(-1);
            } else {
                let mut found_x = -1;
                for x in 0..=n {
                    if (x | (x + 1)) == n {
                        found_x = x;
                        break;
                    }
                }
                ans.push(found_x);
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
  (map (lambda (n)
         (if (= n 2)
             -1
             (let loop ([x 0])
               (if (> x n)
                   -1 ; This case should not be reached for odd primes as a solution always exists.
                   (if (= (bitwise-ior x (+ x 1)) n)
                       x
                       (loop (+ x 1)))))))
       nums))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_bitwise_array(Nums :: [integer()]) -> [integer()].
min_bitwise_array(Nums) ->
  lists:map(fun(N) ->
    if
      N == 2 ->
        -1;
      true ->
        find_min_x(0, N)
    end
  end, Nums).

find_min_x(X, N) when X =< N ->
  case (X bor (X + 1)) of
    N -> X;
    _ -> find_min_x(X + 1, N)
  end;
find_min_x(_, _) ->
  -1. %% This case should not be reached for odd primes as a solution always exists.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_bitwise_array(nums :: [integer]) :: [integer]
  def min_bitwise_array(nums) do
    Enum.map(nums, fn n ->
      if n == 2 do
        -1
      else
        find_min_x(0, n)
      end
    end)
  end

  defp find_min_x(x, n) when x <= n do
    if (x ||| (x + 1)) == n do
      x
    else
      find_min_x(x + 1, n)
    end
  end

  defp find_min_x(_x, _n), do: -1 # This case should not be reached for odd primes as a solution always exists.
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N_len * N_max), where N_len is the length of the `nums` array and N_max is the maximum value in `nums`. For each number in `nums`, we iterate `x` from 0 up to `nums[i]` (at most `N_max`) to find the smallest `ans[i]`. The bitwise OR operation takes constant time. Given `N_len <= 100` and `N_max <= 1000`, the total operations are approximately `100 * 1000 = 10^5`, which is very efficient and well within typical time limits.

- **Space Complexity:** The space complexity is O(N_len), where N_len is the length of the `nums` array. This is because we need to store the `ans` array, which has the same length as `nums`. No additional data structures are used that scale with the input values beyond the output array itself.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-20 01:11:16 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires constructing an array ans of length n, such that for each index i, the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i]. To solve this, we can iterate over all possible values for ans[i] and check if the condition is satisfied. We start from 0 and go up to nums[i] - 1, and for each value, we check if the bitwise OR of the value and the value plus one is equal to nums[i]. If we find such a value, we add it to the ans array. If we don't find any such value, we add -1 to the ans array. This approach ensures that we find the smallest possible value for ans[i] that satisfies the condition.

The key intuition behind this approach is that the bitwise OR operation has a property that a | (a + 1) will always result in a value that has all the bits set to the right of the rightmost set bit in a. This means that if we want a | (a + 1) to be equal to a prime number, a must have all the bits set to the right of the rightmost set bit in the prime number. This property helps us to quickly find the smallest possible value for ans[i] that satisfies the condition.

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
            int val = -1;
            for (int i = 0; i < num; i++) {
                if ((i | (i + 1)) == num) {
                    val = i;
                    break;
                }
            }
            ans.push_back(val);
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
            int val = -1;
            for (int j = 0; j < num; j++) {
                if ((j | (j + 1)) == num) {
                    val = j;
                    break;
                }
            }
            ans[i] = val;
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
            val = -1
            for i in range(num):
                if (i | (i + 1)) == num:
                    val = i
                    break
            ans.append(val)
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
            val = -1
            for i in range(num):
                if (i | (i + 1)) == num:
                    val = i
                    break
            ans.append(val)
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
        int val = -1;
        for (int j = 0; j < num; j++) {
            if ((j | (j + 1)) == num) {
                val = j;
                break;
            }
        }
        ans[i] = val;
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
            int val = -1;
            for (int j = 0; j < num; j++) {
                if ((j | (j + 1)) == num) {
                    val = j;
                    break;
                }
            }
            ans[i] = val;
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
        let val = -1;
        for (let i = 0; i < num; i++) {
            if ((i | (i + 1)) === num) {
                val = i;
                break;
            }
        }
        ans.push(val);
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
        let val: number = -1;
        for (let i = 0; i < num; i++) {
            if ((i | (i + 1)) === num) {
                val = i;
                break;
            }
        }
        ans.push(val);
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
            $val = -1;
            for ($i = 0; $i < $num; $i++) {
                if (($i | ($i + 1)) == $num) {
                    $val = $i;
                    break;
                }
            }
            $ans[] = $val;
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
            var val = -1
            for i in 0..<num {
                if (i | (i + 1)) == num {
                    val = i
                    break
                }
            }
            ans.append(val)
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
            var found = false
            for (j in 0 until nums[i]) {
                if ((j or (j + 1)) == nums[i]) {
                    result[i] = j
                    found = true
                    break
                }
            }
            if (!found) result[i] = -1
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
      bool found = false;
      for (int j = 0; j < nums[i]; j++) {
        if ((j | (j + 1)) == nums[i]) {
          result[i] = j;
          found = true;
          break;
        }
      }
      if (!found) result[i] = -1;
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
        found := false
        for j := 0; j < num; j++ {
            if (j | (j + 1)) == num {
                result[i] = j
                found = true
                break
            }
        }
        if !found {
            result[i] = -1
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
        found = false
        (0...num).each do |j|
            if (j | (j + 1)) == num
                result[i] = j
                found = true
                break
            end
        end
        result[i] = -1 if !found
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
            var found = false
            for (j <- 0 until nums(i)) {
                if ((j | (j + 1)) == nums(i)) {
                    result(i) = j
                    found = true
                    sys.exit()
                }
            }
            if (!found) result(i) = -1
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
        for (i, &num) in nums.iter().enumerate() {
            let mut found = false;
            for j in 0..num {
                if (j | (j + 1)) == num {
                    result[i] = j;
                    found = true;
                    break;
                }
            }
            if !found {
                result[i] = -1;
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
        (let loop ([j 0])
          (cond
            [(= j num) (list-set! result i -1)]
            [(= (bitwise-ior j (+ j 1)) num) (list-set! result i j)]
            [else (loop (+ j 1))]))))
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
    lists:map(fun(X) ->
        case lists:foldl(fun(Y, Acc) ->
            case (Y bor (Y + 1)) of
                X -> Y;
                _ -> Acc
            end
        end, -1, lists:seq(0, X - 1)) of
            -1 -> -1;
            Val -> Val
        end
    end, Nums).
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
      case Enum.find(0..(num - 1), fn x -> (x ||| (x + 1)) == num) do
        nil -> -1
        val -> val
      end
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n * m), where n is the length of the input array and m is the maximum value in the input array. This is because for each element in the input array, we are iterating up to the value of the element to find the smallest possible value that satisfies the condition.

- **Space Complexity:** The space complexity of this solution is O(n), where n is the length of the input array. This is because we are storing the result in an array of the same length as the input array.

</div>
</details>
