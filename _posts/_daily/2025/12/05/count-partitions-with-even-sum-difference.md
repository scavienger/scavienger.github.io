---
layout: post
title: "Count Partitions with Even Sum Difference"
date: 2025-12-05 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Math", "Prefix Sum"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/count-partitions-with-even-sum-difference/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int countPartitions(std::vector<int>& nums)\
        \ {\n        int n = nums.size();\n        long long total_sum = 0;\n      \
        \  for (int x : nums) {\n            total_sum += x;\n        }\n\n        if\
        \ (total_sum % 2 == 0) {\n            return n - 1;\n        } else {\n    \
        \        return 0;\n        }\n    }\n};"
      java: "class Solution {\n    public int countPartitions(int[] nums) {\n      \
        \  int n = nums.length;\n        long totalSum = 0;\n        for (int num :\
        \ nums) {\n            totalSum += num;\n        }\n\n        if (totalSum %\
        \ 2 == 0) {\n            return n - 1;\n        } else {\n            return\
        \ 0;\n        }\n    }\n}"
      python: "class Solution:\n    def countPartitions(self, nums: list[int]) -> int:\n\
        \        n = len(nums)\n        total_sum = sum(nums)\n\n        if total_sum\
        \ % 2 == 0:\n            return n - 1\n        else:\n            return 0"
      python3: "class Solution:\n    def countPartitions(self, nums: list[int]) -> int:\n\
        \        n = len(nums)\n        total_sum = sum(nums)\n\n        if total_sum\
        \ % 2 == 0:\n            return n - 1\n        else:\n            return 0"
      c: "int countPartitions(int* nums, int numsSize) {\n    long long total_sum =\
        \ 0;\n    for (int i = 0; i < numsSize; i++) {\n        total_sum += nums[i];\n\
        \    }\n\n    if (total_sum % 2 == 0) {\n        return numsSize - 1;\n    }\
        \ else {\n        return 0;\n    }\n}"
      csharp: "using System;\nusing System.Linq;\n\npublic class Solution {\n    public\
        \ int CountPartitions(int[] nums) {\n        int n = nums.Length;\n        long\
        \ totalSum = 0;\n        foreach (int num in nums) {\n            totalSum +=\
        \ num;\n        }\n\n        if (totalSum % 2 == 0) {\n            return n\
        \ - 1;\n        } else {\n            return 0;\n        }\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar countPartitions\
        \ = function(nums) {\n    const n = nums.length;\n    let totalSum = 0;\n  \
        \  for (let i = 0; i < n; i++) {\n        totalSum += nums[i];\n    }\n\n  \
        \  if (totalSum % 2 === 0) {\n        return n - 1;\n    } else {\n        return\
        \ 0;\n    }\n};"
      typescript: "function countPartitions(nums: number[]): number {\n    const n =\
        \ nums.length;\n    let totalSum: number = 0;\n    for (let i = 0; i < n; i++)\
        \ {\n        totalSum += nums[i];\n    }\n\n    if (totalSum % 2 === 0) {\n\
        \        return n - 1;\n    } else {\n        return 0;\n    }\n};"
      php: "class Solution {\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function countPartitions($nums) {\n        $n = count($nums);\n\
        \        $totalSum = 0;\n        foreach ($nums as $num) {\n            $totalSum\
        \ += $num;\n        }\n\n        if ($totalSum % 2 == 0) {\n            return\
        \ $n - 1;\n        } else {\n            return 0;\n        }\n    }\n}"
      swift: "class Solution {\n    func countPartitions(_ nums: [Int]) -> Int {\n \
        \       let n = nums.count\n        let totalSum = nums.reduce(0, +)\n\n   \
        \     if totalSum % 2 == 0 {\n            return n - 1\n        } else {\n \
        \           return 0\n        }\n    }\n}"
      kotlin: "class Solution {\n    fun countPartitions(nums: IntArray): Int {\n  \
        \      val n = nums.size\n        var totalSum: Long = 0\n        for (num in\
        \ nums) {\n            totalSum += num\n        }\n\n        if (totalSum %\
        \ 2 == 0L) {\n            return n - 1\n        } else {\n            return\
        \ 0\n        }\n    }\n}"
      dart: "class Solution {\n  int countPartitions(List<int> nums) {\n    final n\
        \ = nums.length;\n    int totalSum = 0;\n    for (final num in nums) {\n   \
        \   totalSum += num;\n    }\n\n    if (totalSum % 2 == 0) {\n      return n\
        \ - 1;\n    } else {\n      return 0;\n    }\n  }\n}"
      go: "package main\n\nfunc countPartitions(nums []int) int {\n    n := len(nums)\n\
        \    totalSum := 0\n    for _, num := range nums {\n        totalSum += num\n\
        \    }\n\n    if totalSum % 2 == 0 {\n        return n - 1\n    } else {\n \
        \       return 0\n    }\n}"
      ruby: "class Solution\n    # @param {Integer[]} nums\n    # @return {Integer}\n\
        \    def count_partitions(nums)\n        n = nums.length\n        total_sum\
        \ = nums.sum\n\n        if total_sum % 2 == 0\n            return n - 1\n  \
        \      else\n            return 0\n        end\n    end\nend"
      scala: "object Solution {\n    def countPartitions(nums: Array[Int]): Int = {\n\
        \        val n = nums.length\n        val totalSum = nums.sum\n\n        if\
        \ (totalSum % 2 == 0) {\n            n - 1\n        } else {\n            0\n\
        \        }\n    }\n}"
      rust: "impl Solution {\n    pub fn count_partitions(nums: Vec<i32>) -> i32 {\n\
        \        let n = nums.len() as i32;\n        let total_sum: i32 = nums.iter().sum();\n\
        \n        if total_sum % 2 == 0 {\n            n - 1\n        } else {\n   \
        \         0\n        }\n    }\n}"
      racket: "#lang racket\n\n(define (count-partitions nums)\n  (let* ([n (length\
        \ nums)]\n         [total-sum (apply + nums)])\n    (if (= (modulo total-sum\
        \ 2) 0)\n        (- n 1)\n        0)))"
      erlang: "-module(solution).\n-export([count_partitions/1]).\n\ncount_partitions(Nums)\
        \ ->\n    N = length(Nums),\n    TotalSum = lists:sum(Nums),\n    case TotalSum\
        \ rem 2 of\n        0 -> N - 1;\n        _ -> 0\n    end."
      elixir: "defmodule Solution do\n  @spec count_partitions(nums :: [integer]) ::\
        \ integer\n  def count_partitions(nums) do\n    n = length(nums)\n    total_sum\
        \ = Enum.sum(nums)\n\n    if rem(total_sum, 2) == 0 do\n      n - 1\n    else\n\
        \      0\n    end\n  end\nend"
    approach: 'The problem asks us to count partitions where the difference between
      the sum of the left subarray (S_L) and the sum of the right subarray (S_R) is
      even. A key mathematical property states that the difference between two integers,
      A - B, is even if and only if A and B have the same parity (i.e., both are even
      or both are odd).


      Consider the total sum of all elements in the array, S_total = S_L + S_R. If S_L
      and S_R have the same parity, then their sum S_L + S_R must be even. Conversely,
      if S_L and S_R have different parities, then their sum S_L + S_R must be odd.
      This establishes a direct equivalence: S_L - S_R is even if and only if S_L +
      S_R is even. Since S_L + S_R is always equal to S_total, the condition simplifies
      to checking if the total sum of the entire array, S_total, is even. If S_total
      is odd, then S_L and S_R must have different parities for any partition, making
      S_L - S_R always odd, so the count of valid partitions is 0. If S_total is even,
      then S_L and S_R must have the same parity for any partition, making S_L - S_R
      always even. In this case, all possible partitions satisfy the condition. The
      number of possible partitions is n - 1, as the partition index `i` can range from
      0 to n - 2 (inclusive) to ensure both subarrays are non-empty.'
    time_complexity: The time complexity is O(N), where N is the length of the `nums`
      array. This is because we need to iterate through the entire array once to calculate
      the total sum of its elements. All subsequent operations (checking parity and
      returning a value) take constant time.
    space_complexity: The space complexity is O(1). We only use a few variables to store
      the array length and the total sum, regardless of the input array's size. No additional
      data structures that scale with N are used.
    elapsed_time: 34.672388792037964
    model: gemini-2.5-flash
    generated_at: '2025-12-05 01:06:00 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int countPartitions(vector<int>& nums) {\n\
        \        int n = nums.size();\n        int totalSum = 0;\n        for (int num\
        \ : nums) {\n            totalSum += num;\n        }\n        int count = 0;\n\
        \        for (int i = 0; i < n - 1; i++) {\n            int leftSum = 0;\n \
        \           for (int j = 0; j <= i; j++) {\n                leftSum += nums[j];\n\
        \            }\n            if ((totalSum - 2 * leftSum) % 2 == 0) {\n     \
        \           count++;\n            }\n        }\n        return count;\n    }\n\
        };"
      java: "class Solution {\n    public int countPartitions(int[] nums) {\n      \
        \  int n = nums.length;\n        int totalSum = 0;\n        for (int num : nums)\
        \ {\n            totalSum += num;\n        }\n        int count = 0;\n     \
        \   for (int i = 0; i < n - 1; i++) {\n            int leftSum = 0;\n      \
        \      for (int j = 0; j <= i; j++) {\n                leftSum += nums[j];\n\
        \            }\n            if ((totalSum - 2 * leftSum) % 2 == 0) {\n     \
        \           count++;\n            }\n        }\n        return count;\n    }\n\
        }"
      python: "class Solution:\n    def countPartitions(self, nums: list[int]) -> int:\n\
        \        n = len(nums)\n        total_sum = sum(nums)\n        count = 0\n \
        \       for i in range(n - 1):\n            left_sum = sum(nums[:i + 1])\n \
        \           if (total_sum - 2 * left_sum) % 2 == 0:\n                count +=\
        \ 1\n        return count"
      python3: "class Solution:\n    def countPartitions(self, nums: list[int]) -> int:\n\
        \        n = len(nums)\n        total_sum = sum(nums)\n        count = 0\n \
        \       for i in range(n - 1):\n            left_sum = sum(nums[:i + 1])\n \
        \           if (total_sum - 2 * left_sum) % 2 == 0:\n                count +=\
        \ 1\n        return count"
      c: "int countPartitions(int* nums, int numsSize) {\n    int totalSum = 0;\n  \
        \  for (int i = 0; i < numsSize; i++) {\n        totalSum += nums[i];\n    }\n\
        \    int count = 0;\n    for (int i = 0; i < numsSize - 1; i++) {\n        int\
        \ leftSum = 0;\n        for (int j = 0; j <= i; j++) {\n            leftSum\
        \ += nums[j];\n        }\n        if ((totalSum - 2 * leftSum) % 2 == 0) {\n\
        \            count++;\n        }\n    }\n    return count;\n}"
      csharp: "public class Solution {\n    public int CountPartitions(int[] nums) {\n\
        \        int n = nums.Length;\n        int totalSum = 0;\n        foreach (int\
        \ num in nums) {\n            totalSum += num;\n        }\n        int count\
        \ = 0;\n        for (int i = 0; i < n - 1; i++) {\n            int leftSum =\
        \ 0;\n            for (int j = 0; j <= i; j++) {\n                leftSum +=\
        \ nums[j];\n            }\n            if ((totalSum - 2 * leftSum) % 2 == 0)\
        \ {\n                count++;\n            }\n        }\n        return count;\n\
        \    }\n}"
      javascript: "var countPartitions = function(nums) {\n    let n = nums.length;\n\
        \    let totalSum = 0;\n    for (let num of nums) {\n        totalSum += num;\n\
        \    }\n    let count = 0;\n    for (let i = 0; i < n - 1; i++) {\n        let\
        \ leftSum = 0;\n        for (let j = 0; j <= i; j++) {\n            leftSum\
        \ += nums[j];\n        }\n        if ((totalSum - 2 * leftSum) % 2 == 0) {\n\
        \            count++;\n        }\n    }\n    return count;\n};"
      typescript: "function countPartitions(nums: number[]): number {\n    let n: number\
        \ = nums.length;\n    let totalSum: number = 0;\n    for (let num of nums) {\n\
        \        totalSum += num;\n    }\n    let count: number = 0;\n    for (let i:\
        \ number = 0; i < n - 1; i++) {\n        let leftSum: number = 0;\n        for\
        \ (let j: number = 0; j <= i; j++) {\n            leftSum += nums[j];\n    \
        \    }\n        if ((totalSum - 2 * leftSum) % 2 == 0) {\n            count++;\n\
        \        }\n    }\n    return count;\n}"
      php: "class Solution {\n    function countPartitions($nums) {\n        $n = count($nums);\n\
        \        $totalSum = 0;\n        foreach ($nums as $num) {\n            $totalSum\
        \ += $num;\n        }\n        $count = 0;\n        for ($i = 0; $i < $n - 1;\
        \ $i++) {\n            $leftSum = 0;\n            for ($j = 0; $j <= $i; $j++)\
        \ {\n                $leftSum += $nums[$j];\n            }\n            if (($totalSum\
        \ - 2 * $leftSum) % 2 == 0) {\n                $count++;\n            }\n  \
        \      }\n        return $count;\n    }\n}"
      swift: "class Solution {\n    func countPartitions(_ nums: [Int]) -> Int {\n \
        \       let n = nums.count\n        var totalSum = 0\n        for num in nums\
        \ {\n            totalSum += num\n        }\n        var count = 0\n       \
        \ for i in 0..<n - 1 {\n            var leftSum = 0\n            for j in 0...i\
        \ {\n                leftSum += nums[j]\n            }\n            if (totalSum\
        \ - 2 * leftSum) % 2 == 0 {\n                count += 1\n            }\n   \
        \     }\n        return count\n    }\n}"
      kotlin: "class Solution {\n    fun countPartitions(nums: IntArray): Int {\n  \
        \      val n = nums.size\n        var totalSum = 0\n        for (num in nums)\
        \ {\n            totalSum += num\n        }\n        var count = 0\n       \
        \ for (i in 0 until n - 1) {\n            var leftSum = 0\n            for (j\
        \ in 0..i) {\n                leftSum += nums[j]\n            }\n          \
        \  if ((totalSum - 2 * leftSum) % 2 == 0) {\n                count++\n     \
        \       }\n        }\n        return count\n    }\n}"
      dart: "class Solution {\n    int countPartitions(List<int> nums) {\n        int\
        \ n = nums.length;\n        int totalSum = 0;\n        for (int num in nums)\
        \ {\n            totalSum += num;\n        }\n        int count = 0;\n     \
        \   for (int i = 0; i < n - 1; i++) {\n            int leftSum = 0;\n      \
        \      for (int j = 0; j <= i; j++) {\n                leftSum += nums[j];\n\
        \            }\n            if ((totalSum - 2 * leftSum) % 2 == 0) {\n     \
        \           count++;\n            }\n        }\n        return count;\n    }\n\
        }"
      go: "func countPartitions(nums []int) int {\n    n := len(nums)\n    totalSum\
        \ := 0\n    for _, num := range nums {\n        totalSum += num\n    }\n   \
        \ count := 0\n    for i := 0; i < n-1; i++ {\n        leftSum := 0\n       \
        \ for j := 0; j <= i; j++ {\n            leftSum += nums[j]\n        }\n   \
        \     if (totalSum-2*leftSum)%2 == 0 {\n            count++\n        }\n   \
        \ }\n    return count\n}"
      ruby: "class Solution\n    def count_partitions(nums)\n        n = nums.size\n\
        \        total_sum = 0\n        nums.each { |num| total_sum += num }\n     \
        \   count = 0\n        (0...n-1).each do |i|\n            left_sum = 0\n   \
        \         (0..i).each { |j| left_sum += nums[j] }\n            if (total_sum\
        \ - 2 * left_sum) % 2 == 0\n                count += 1\n            end\n  \
        \      end\n        count\n    end\nend"
      scala: "object Solution {\n    def countPartitions(nums: Array[Int]): Int = {\n\
        \        val n = nums.length\n        var totalSum = 0\n        for (num <-\
        \ nums) {\n            totalSum += num\n        }\n        var count = 0\n \
        \       for (i <- 0 until n - 1) {\n            var leftSum = 0\n          \
        \  for (j <- 0 to i) {\n                leftSum += nums(j)\n            }\n\
        \            if ((totalSum - 2 * leftSum) % 2 == 0) {\n                count\
        \ += 1\n            }\n        }\n        count\n    }\n}"
      rust: "struct Solution;\nimpl Solution {\n    pub fn count_partitions(nums: Vec<i32>)\
        \ -> i32 {\n        let n = nums.len();\n        let mut total_sum: i32 = 0;\n\
        \        for &num in &nums {\n            total_sum += num;\n        }\n   \
        \     let mut count = 0;\n        for i in 0..n-1 {\n            let mut left_sum:\
        \ i32 = 0;\n            for j in 0..=i {\n                left_sum += nums[j];\n\
        \            }\n            if (total_sum - 2 * left_sum) % 2 == 0 {\n     \
        \           count += 1;\n            }\n        }\n        count\n    }\n}"
      racket: "(define (count-partitions nums)\n    (let ((n (length nums))\n      \
        \    (total-sum (apply + nums))\n          (count 0))\n        (do ((i 0 (+\
        \ i 1)))\n            ((= i (- n 1)) count)\n            (let ((left-sum (apply\
        \ + (take nums (+ i 1)))))\n                (if (even? (- total-sum (* 2 left-sum)))\n\
        \                    (set! count (+ count 1)))))))"
      erlang: "-module(solution).\n-export([count_partitions/1]).\n\ncount_partitions(Nums)\
        \ ->\n    N = length(Nums),\n    TotalSum = lists:sum(Nums),\n    Count = count_partitions(Nums,\
        \ 0, TotalSum, 0),\n    Count.\n\ncount_partitions([_|_], N, TotalSum, Count)\
        \ when N == length(Nums) -> Count;\ncount_partitions(Nums, I, TotalSum, Count)\
        \ ->\n    LeftSum = lists:sum(lists:sublist(Nums, I + 1)),\n    case (TotalSum\
        \ - 2 * LeftSum) rem 2 of\n        0 -> count_partitions(Nums, I + 1, TotalSum,\
        \ Count + 1);\n        _ -> count_partitions(Nums, I + 1, TotalSum, Count)\n\
        \    end."
      elixir: "defmodule Solution do\n    def count_partitions(nums) do\n        n =\
        \ length(nums)\n        total_sum = Enum.sum(nums)\n        count_partitions(nums,\
        \ 0, total_sum, 0)\n    end\n\n    defp count_partitions(nums, i, total_sum,\
        \ count) when i == length(nums) - 1, do: count\n    defp count_partitions(nums,\
        \ i, total_sum, count) do\n        left_sum = Enum.sum(Enum.take(nums, i + 1))\n\
        \        if (total_sum - 2 * left_sum) |> rem(2) == 0 do\n            count_partitions(nums,\
        \ i + 1, total_sum, count + 1)\n        else\n            count_partitions(nums,\
        \ i + 1, total_sum, count)\n        end\n    end\nend"
    approach: The problem can be solved by iterating over all possible partitions of
      the given array and checking if the difference between the sum of the left and
      right subarrays is even. The key intuition here is to calculate the total sum
      of the array first and then iterate over all possible partitions, calculating
      the sum of the left subarray and checking if the difference between the total
      sum and twice the sum of the left subarray is even. If the difference is even,
      it means the partition is valid and we increment the count of valid partitions.
      We can use a simple loop to iterate over all possible partitions and calculate
      the sum of the left subarray for each partition.
    time_complexity: The time complexity of the solution is O(n), where n is the number
      of elements in the array. This is because we are iterating over all possible partitions
      of the array, which takes linear time. The space complexity is also O(1), which
      means the space required does not change with the size of the input array, making
      the solution efficient for large inputs.
    space_complexity: The space complexity of the solution is O(1), which means the
      space required does not change with the size of the input array. This is because
      we are only using a constant amount of space to store the count of valid partitions
      and the sum of the left subarray, regardless of the size of the input array.
    elapsed_time: 6.211416006088257
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-05 01:06:06 '
---

## Problem #3432: Count Partitions with Even Sum Difference

**Difficulty:** Easy

**Topics:** Array, Math, Prefix Sum

## Problem Description

<p>You are given an integer array <code>nums</code> of length <code>n</code>.</p>

<p>A <strong>partition</strong> is defined as an index <code>i</code> where <code>0 &lt;= i &lt; n - 1</code>, splitting the array into two <strong>non-empty</strong> subarrays such that:</p>

<ul>
	<li>Left subarray contains indices <code>[0, i]</code>.</li>
	<li>Right subarray contains indices <code>[i + 1, n - 1]</code>.</li>
</ul>

<p>Return the number of <strong>partitions</strong> where the <strong>difference</strong> between the <strong>sum</strong> of the left and right subarrays is <strong>even</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [10,10,3,7,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The 4 partitions are:</p>

<ul>
	<li><code>[10]</code>, <code>[10, 3, 7, 6]</code> with a sum difference of <code>10 - 26 = -16</code>, which is even.</li>
	<li><code>[10, 10]</code>, <code>[3, 7, 6]</code> with a sum difference of <code>20 - 16 = 4</code>, which is even.</li>
	<li><code>[10, 10, 3]</code>, <code>[7, 6]</code> with a sum difference of <code>23 - 13 = 10</code>, which is even.</li>
	<li><code>[10, 10, 3, 7]</code>, <code>[6]</code> with a sum difference of <code>30 - 6 = 24</code>, which is even.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>No partition results in an even sum difference.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,4,6,8]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>All partitions result in an even sum difference.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n == nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## Hints

1. If the parity of the sum is even, the partition is valid; otherwise, there is no partition.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-05 01:06:00 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to count partitions where the difference between the sum of the left subarray (S_L) and the sum of the right subarray (S_R) is even. A key mathematical property states that the difference between two integers, A - B, is even if and only if A and B have the same parity (i.e., both are even or both are odd).

Consider the total sum of all elements in the array, S_total = S_L + S_R. If S_L and S_R have the same parity, then their sum S_L + S_R must be even. Conversely, if S_L and S_R have different parities, then their sum S_L + S_R must be odd. This establishes a direct equivalence: S_L - S_R is even if and only if S_L + S_R is even. Since S_L + S_R is always equal to S_total, the condition simplifies to checking if the total sum of the entire array, S_total, is even. If S_total is odd, then S_L and S_R must have different parities for any partition, making S_L - S_R always odd, so the count of valid partitions is 0. If S_total is even, then S_L and S_R must have the same parity for any partition, making S_L - S_R always even. In this case, all possible partitions satisfy the condition. The number of possible partitions is n - 1, as the partition index `i` can range from 0 to n - 2 (inclusive) to ensure both subarrays are non-empty.

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
    int countPartitions(std::vector<int>& nums) {
        int n = nums.size();
        long long total_sum = 0;
        for (int x : nums) {
            total_sum += x;
        }

        if (total_sum % 2 == 0) {
            return n - 1;
        } else {
            return 0;
        }
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countPartitions(int[] nums) {
        int n = nums.length;
        long totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        if (totalSum % 2 == 0) {
            return n - 1;
        } else {
            return 0;
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)

        if total_sum % 2 == 0:
            return n - 1
        else:
            return 0
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)

        if total_sum % 2 == 0:
            return n - 1
        else:
            return 0
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countPartitions(int* nums, int numsSize) {
    long long total_sum = 0;
    for (int i = 0; i < numsSize; i++) {
        total_sum += nums[i];
    }

    if (total_sum % 2 == 0) {
        return numsSize - 1;
    } else {
        return 0;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Linq;

public class Solution {
    public int CountPartitions(int[] nums) {
        int n = nums.Length;
        long totalSum = 0;
        foreach (int num in nums) {
            totalSum += num;
        }

        if (totalSum % 2 == 0) {
            return n - 1;
        } else {
            return 0;
        }
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
 * @return {number}
 */
var countPartitions = function(nums) {
    const n = nums.length;
    let totalSum = 0;
    for (let i = 0; i < n; i++) {
        totalSum += nums[i];
    }

    if (totalSum % 2 === 0) {
        return n - 1;
    } else {
        return 0;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countPartitions(nums: number[]): number {
    const n = nums.length;
    let totalSum: number = 0;
    for (let i = 0; i < n; i++) {
        totalSum += nums[i];
    }

    if (totalSum % 2 === 0) {
        return n - 1;
    } else {
        return 0;
    }
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
     * @return Integer
     */
    function countPartitions($nums) {
        $n = count($nums);
        $totalSum = 0;
        foreach ($nums as $num) {
            $totalSum += $num;
        }

        if ($totalSum % 2 == 0) {
            return $n - 1;
        } else {
            return 0;
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countPartitions(_ nums: [Int]) -> Int {
        let n = nums.count
        let totalSum = nums.reduce(0, +)

        if totalSum % 2 == 0 {
            return n - 1
        } else {
            return 0
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countPartitions(nums: IntArray): Int {
        val n = nums.size
        var totalSum: Long = 0
        for (num in nums) {
            totalSum += num
        }

        if (totalSum % 2 == 0L) {
            return n - 1
        } else {
            return 0
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int countPartitions(List<int> nums) {
    final n = nums.length;
    int totalSum = 0;
    for (final num in nums) {
      totalSum += num;
    }

    if (totalSum % 2 == 0) {
      return n - 1;
    } else {
      return 0;
    }
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

func countPartitions(nums []int) int {
    n := len(nums)
    totalSum := 0
    for _, num := range nums {
        totalSum += num
    }

    if totalSum % 2 == 0 {
        return n - 1
    } else {
        return 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    # @param {Integer[]} nums
    # @return {Integer}
    def count_partitions(nums)
        n = nums.length
        total_sum = nums.sum

        if total_sum % 2 == 0
            return n - 1
        else
            return 0
        end
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countPartitions(nums: Array[Int]): Int = {
        val n = nums.length
        val totalSum = nums.sum

        if (totalSum % 2 == 0) {
            n - 1
        } else {
            0
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_partitions(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let total_sum: i32 = nums.iter().sum();

        if total_sum % 2 == 0 {
            n - 1
        } else {
            0
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (count-partitions nums)
  (let* ([n (length nums)]
         [total-sum (apply + nums)])
    (if (= (modulo total-sum 2) 0)
        (- n 1)
        0)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([count_partitions/1]).

count_partitions(Nums) ->
    N = length(Nums),
    TotalSum = lists:sum(Nums),
    case TotalSum rem 2 of
        0 -> N - 1;
        _ -> 0
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_partitions(nums :: [integer]) :: integer
  def count_partitions(nums) do
    n = length(nums)
    total_sum = Enum.sum(nums)

    if rem(total_sum, 2) == 0 do
      n - 1
    else
      0
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N), where N is the length of the `nums` array. This is because we need to iterate through the entire array once to calculate the total sum of its elements. All subsequent operations (checking parity and returning a value) take constant time.

- **Space Complexity:** The space complexity is O(1). We only use a few variables to store the array length and the total sum, regardless of the input array's size. No additional data structures that scale with N are used.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-05 01:06:06 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by iterating over all possible partitions of the given array and checking if the difference between the sum of the left and right subarrays is even. The key intuition here is to calculate the total sum of the array first and then iterate over all possible partitions, calculating the sum of the left subarray and checking if the difference between the total sum and twice the sum of the left subarray is even. If the difference is even, it means the partition is valid and we increment the count of valid partitions. We can use a simple loop to iterate over all possible partitions and calculate the sum of the left subarray for each partition.

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
    int countPartitions(vector<int>& nums) {
        int n = nums.size();
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
        int count = 0;
        for (int i = 0; i < n - 1; i++) {
            int leftSum = 0;
            for (int j = 0; j <= i; j++) {
                leftSum += nums[j];
            }
            if ((totalSum - 2 * leftSum) % 2 == 0) {
                count++;
            }
        }
        return count;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countPartitions(int[] nums) {
        int n = nums.length;
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
        int count = 0;
        for (int i = 0; i < n - 1; i++) {
            int leftSum = 0;
            for (int j = 0; j <= i; j++) {
                leftSum += nums[j];
            }
            if ((totalSum - 2 * leftSum) % 2 == 0) {
                count++;
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        count = 0
        for i in range(n - 1):
            left_sum = sum(nums[:i + 1])
            if (total_sum - 2 * left_sum) % 2 == 0:
                count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        count = 0
        for i in range(n - 1):
            left_sum = sum(nums[:i + 1])
            if (total_sum - 2 * left_sum) % 2 == 0:
                count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countPartitions(int* nums, int numsSize) {
    int totalSum = 0;
    for (int i = 0; i < numsSize; i++) {
        totalSum += nums[i];
    }
    int count = 0;
    for (int i = 0; i < numsSize - 1; i++) {
        int leftSum = 0;
        for (int j = 0; j <= i; j++) {
            leftSum += nums[j];
        }
        if ((totalSum - 2 * leftSum) % 2 == 0) {
            count++;
        }
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountPartitions(int[] nums) {
        int n = nums.Length;
        int totalSum = 0;
        foreach (int num in nums) {
            totalSum += num;
        }
        int count = 0;
        for (int i = 0; i < n - 1; i++) {
            int leftSum = 0;
            for (int j = 0; j <= i; j++) {
                leftSum += nums[j];
            }
            if ((totalSum - 2 * leftSum) % 2 == 0) {
                count++;
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var countPartitions = function(nums) {
    let n = nums.length;
    let totalSum = 0;
    for (let num of nums) {
        totalSum += num;
    }
    let count = 0;
    for (let i = 0; i < n - 1; i++) {
        let leftSum = 0;
        for (let j = 0; j <= i; j++) {
            leftSum += nums[j];
        }
        if ((totalSum - 2 * leftSum) % 2 == 0) {
            count++;
        }
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countPartitions(nums: number[]): number {
    let n: number = nums.length;
    let totalSum: number = 0;
    for (let num of nums) {
        totalSum += num;
    }
    let count: number = 0;
    for (let i: number = 0; i < n - 1; i++) {
        let leftSum: number = 0;
        for (let j: number = 0; j <= i; j++) {
            leftSum += nums[j];
        }
        if ((totalSum - 2 * leftSum) % 2 == 0) {
            count++;
        }
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function countPartitions($nums) {
        $n = count($nums);
        $totalSum = 0;
        foreach ($nums as $num) {
            $totalSum += $num;
        }
        $count = 0;
        for ($i = 0; $i < $n - 1; $i++) {
            $leftSum = 0;
            for ($j = 0; $j <= $i; $j++) {
                $leftSum += $nums[$j];
            }
            if (($totalSum - 2 * $leftSum) % 2 == 0) {
                $count++;
            }
        }
        return $count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countPartitions(_ nums: [Int]) -> Int {
        let n = nums.count
        var totalSum = 0
        for num in nums {
            totalSum += num
        }
        var count = 0
        for i in 0..<n - 1 {
            var leftSum = 0
            for j in 0...i {
                leftSum += nums[j]
            }
            if (totalSum - 2 * leftSum) % 2 == 0 {
                count += 1
            }
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countPartitions(nums: IntArray): Int {
        val n = nums.size
        var totalSum = 0
        for (num in nums) {
            totalSum += num
        }
        var count = 0
        for (i in 0 until n - 1) {
            var leftSum = 0
            for (j in 0..i) {
                leftSum += nums[j]
            }
            if ((totalSum - 2 * leftSum) % 2 == 0) {
                count++
            }
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int countPartitions(List<int> nums) {
        int n = nums.length;
        int totalSum = 0;
        for (int num in nums) {
            totalSum += num;
        }
        int count = 0;
        for (int i = 0; i < n - 1; i++) {
            int leftSum = 0;
            for (int j = 0; j <= i; j++) {
                leftSum += nums[j];
            }
            if ((totalSum - 2 * leftSum) % 2 == 0) {
                count++;
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func countPartitions(nums []int) int {
    n := len(nums)
    totalSum := 0
    for _, num := range nums {
        totalSum += num
    }
    count := 0
    for i := 0; i < n-1; i++ {
        leftSum := 0
        for j := 0; j <= i; j++ {
            leftSum += nums[j]
        }
        if (totalSum-2*leftSum)%2 == 0 {
            count++
        }
    }
    return count
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def count_partitions(nums)
        n = nums.size
        total_sum = 0
        nums.each { |num| total_sum += num }
        count = 0
        (0...n-1).each do |i|
            left_sum = 0
            (0..i).each { |j| left_sum += nums[j] }
            if (total_sum - 2 * left_sum) % 2 == 0
                count += 1
            end
        end
        count
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countPartitions(nums: Array[Int]): Int = {
        val n = nums.length
        var totalSum = 0
        for (num <- nums) {
            totalSum += num
        }
        var count = 0
        for (i <- 0 until n - 1) {
            var leftSum = 0
            for (j <- 0 to i) {
                leftSum += nums(j)
            }
            if ((totalSum - 2 * leftSum) % 2 == 0) {
                count += 1
            }
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
struct Solution;
impl Solution {
    pub fn count_partitions(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut total_sum: i32 = 0;
        for &num in &nums {
            total_sum += num;
        }
        let mut count = 0;
        for i in 0..n-1 {
            let mut left_sum: i32 = 0;
            for j in 0..=i {
                left_sum += nums[j];
            }
            if (total_sum - 2 * left_sum) % 2 == 0 {
                count += 1;
            }
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define (count-partitions nums)
    (let ((n (length nums))
          (total-sum (apply + nums))
          (count 0))
        (do ((i 0 (+ i 1)))
            ((= i (- n 1)) count)
            (let ((left-sum (apply + (take nums (+ i 1)))))
                (if (even? (- total-sum (* 2 left-sum)))
                    (set! count (+ count 1)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([count_partitions/1]).

count_partitions(Nums) ->
    N = length(Nums),
    TotalSum = lists:sum(Nums),
    Count = count_partitions(Nums, 0, TotalSum, 0),
    Count.

count_partitions([_|_], N, TotalSum, Count) when N == length(Nums) -> Count;
count_partitions(Nums, I, TotalSum, Count) ->
    LeftSum = lists:sum(lists:sublist(Nums, I + 1)),
    case (TotalSum - 2 * LeftSum) rem 2 of
        0 -> count_partitions(Nums, I + 1, TotalSum, Count + 1);
        _ -> count_partitions(Nums, I + 1, TotalSum, Count)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def count_partitions(nums) do
        n = length(nums)
        total_sum = Enum.sum(nums)
        count_partitions(nums, 0, total_sum, 0)
    end

    defp count_partitions(nums, i, total_sum, count) when i == length(nums) - 1, do: count
    defp count_partitions(nums, i, total_sum, count) do
        left_sum = Enum.sum(Enum.take(nums, i + 1))
        if (total_sum - 2 * left_sum) |> rem(2) == 0 do
            count_partitions(nums, i + 1, total_sum, count + 1)
        else
            count_partitions(nums, i + 1, total_sum, count)
        end
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the solution is O(n), where n is the number of elements in the array. This is because we are iterating over all possible partitions of the array, which takes linear time. The space complexity is also O(1), which means the space required does not change with the size of the input array, making the solution efficient for large inputs.

- **Space Complexity:** The space complexity of the solution is O(1), which means the space required does not change with the size of the input array. This is because we are only using a constant amount of space to store the count of valid partitions and the sum of the left subarray, regardless of the size of the input array.

</div>
</details>
