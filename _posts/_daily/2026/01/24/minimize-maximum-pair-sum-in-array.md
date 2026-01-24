---
layout: post
title: "Minimize Maximum Pair Sum in Array"
date: 2026-01-24 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Two Pointers", "Greedy", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minPairSum(std::vector<int>& nums) {\n\
        \        std::sort(nums.begin(), nums.end());\n        int max_pair_sum = 0;\n\
        \        int n = nums.size();\n        for (int i = 0; i < n / 2; ++i) {\n \
        \           max_pair_sum = std::max(max_pair_sum, nums[i] + nums[n - 1 - i]);\n\
        \        }\n        return max_pair_sum;\n    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public int minPairSum(int[]\
        \ nums) {\n        Arrays.sort(nums);\n        int maxPairSum = 0;\n       \
        \ int n = nums.length;\n        for (int i = 0; i < n / 2; i++) {\n        \
        \    maxPairSum = Math.max(maxPairSum, nums[i] + nums[n - 1 - i]);\n       \
        \ }\n        return maxPairSum;\n    }\n}"
      python: "class Solution(object):\n    def minPairSum(self, nums):\n        \"\"\
        \"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\n   \
        \     nums.sort()\n        max_pair_sum = 0\n        n = len(nums)\n       \
        \ for i in range(n // 2):\n            max_pair_sum = max(max_pair_sum, nums[i]\
        \ + nums[n - 1 - i])\n        return max_pair_sum"
      python3: "class Solution:\n    def minPairSum(self, nums: List[int]) -> int:\n\
        \        nums.sort()\n        max_pair_sum = 0\n        n = len(nums)\n    \
        \    for i in range(n // 2):\n            max_pair_sum = max(max_pair_sum, nums[i]\
        \ + nums[n - 1 - i])\n        return max_pair_sum"
      c: "#include <stdlib.h>\n\nint compare(const void *a, const void *b) {\n    return\
        \ (*(int*)a - *(int*)b);\n}\n\nint minPairSum(int* nums, int numsSize){\n  \
        \  qsort(nums, numsSize, sizeof(int), compare);\n\n    int max_pair_sum = 0;\n\
        \    for (int i = 0; i < numsSize / 2; ++i) {\n        int current_sum = nums[i]\
        \ + nums[numsSize - 1 - i];\n        if (current_sum > max_pair_sum) {\n   \
        \         max_pair_sum = current_sum;\n        }\n    }\n    return max_pair_sum;\n\
        }"
      csharp: "public class Solution {\n    public int MinPairSum(int[] nums) {\n  \
        \      Array.Sort(nums);\n        int maxPairSum = 0;\n        int n = nums.Length;\n\
        \        for (int i = 0; i < n / 2; i++) {\n            maxPairSum = Math.Max(maxPairSum,\
        \ nums[i] + nums[n - 1 - i]);\n        }\n        return maxPairSum;\n    }\n\
        }"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minPairSum\
        \ = function(nums) {\n    nums.sort((a, b) => a - b);\n    let maxPairSum =\
        \ 0;\n    const n = nums.length;\n    for (let i = 0; i < n / 2; i++) {\n  \
        \      maxPairSum = Math.max(maxPairSum, nums[i] + nums[n - 1 - i]);\n    }\n\
        \    return maxPairSum;\n};"
      typescript: "function minPairSum(nums: number[]): number {\n    nums.sort((a,\
        \ b) => a - b);\n    let maxPairSum: number = 0;\n    const n: number = nums.length;\n\
        \    for (let i = 0; i < n / 2; i++) {\n        maxPairSum = Math.max(maxPairSum,\
        \ nums[i] + nums[n - 1 - i]);\n    }\n    return maxPairSum;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function minPairSum($nums) {\n        sort($nums);\n\
        \        $maxPairSum = 0;\n        $n = count($nums);\n        for ($i = 0;\
        \ $i < $n / 2; $i++) {\n            $maxPairSum = max($maxPairSum, $nums[$i]\
        \ + $nums[$n - 1 - $i]);\n        }\n        return $maxPairSum;\n    }\n}"
      swift: "class Solution {\n    func minPairSum(_ nums: [Int]) -> Int {\n      \
        \  var sortedNums = nums.sorted()\n        var maxPairSum = 0\n        let n\
        \ = sortedNums.count\n        for i in 0..<n/2 {\n            maxPairSum = max(maxPairSum,\
        \ sortedNums[i] + sortedNums[n - 1 - i])\n        }\n        return maxPairSum\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun minPairSum(nums: IntArray): Int {\n       \
        \ nums.sort()\n        var maxPairSum = 0\n        val n = nums.size\n     \
        \   for (i in 0 until n / 2) {\n            val currentPairSum = nums[i] + nums[n\
        \ - 1 - i]\n            if (currentPairSum > maxPairSum) {\n               \
        \ maxPairSum = currentPairSum\n            }\n        }\n        return maxPairSum\n\
        \    }\n}"
      dart: "import 'dart:math' as math;\n\nclass Solution {\n  int minPairSum(List<int>\
        \ nums) {\n    nums.sort();\n    int maxPairSum = 0;\n    int n = nums.length;\n\
        \    for (int i = 0; i < n ~/ 2; i++) {\n      int currentPairSum = nums[i]\
        \ + nums[n - 1 - i];\n      maxPairSum = math.max(maxPairSum, currentPairSum);\n\
        \    }\n    return maxPairSum;\n  }\n}"
      go: "import (\n    \"sort\"\n)\n\nfunc minPairSum(nums []int) int {\n    sort.Ints(nums)\n\
        \    maxPairSum := 0\n    n := len(nums)\n    for i := 0; i < n/2; i++ {\n \
        \       currentPairSum := nums[i] + nums[n - 1 - i]\n        if currentPairSum\
        \ > maxPairSum {\n            maxPairSum = currentPairSum\n        }\n    }\n\
        \    return maxPairSum\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef min_pair_sum(nums)\n\
        \    nums.sort!\n    max_pair_sum = 0\n    n = nums.length\n    (0...n/2).each\
        \ do |i|\n        current_pair_sum = nums[i] + nums[n - 1 - i]\n        max_pair_sum\
        \ = [max_pair_sum, current_pair_sum].max\n    end\n    max_pair_sum\nend"
      scala: "object Solution {\n    def minPairSum(nums: Array[Int]): Int = {\n   \
        \     val sortedNums = nums.sorted\n        var maxPairSum = 0\n        val\
        \ n = sortedNums.length\n        for (i <- 0 until n / 2) {\n            val\
        \ currentPairSum = sortedNums(i) + sortedNums(n - 1 - i)\n            if (currentPairSum\
        \ > maxPairSum) {\n                maxPairSum = currentPairSum\n           \
        \ }\n        }\n        maxPairSum\n    }\n}"
      rust: "impl Solution {\n    pub fn min_pair_sum(mut nums: Vec<i32>) -> i32 {\n\
        \        nums.sort();\n        let mut max_pair_sum = 0;\n        let n = nums.len();\n\
        \        for i in 0..n/2 {\n            let current_pair_sum = nums[i] + nums[n\
        \ - 1 - i];\n            if current_pair_sum > max_pair_sum {\n            \
        \    max_pair_sum = current_pair_sum;\n            }\n        }\n        max_pair_sum\n\
        \    }\n}"
      racket: "(define/contract (min-pair-sum nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (let* ([sorted-nums (list->vector (sort nums <))]\n         [n (vector-length\
        \ sorted-nums)])\n    (for/fold ([max-sum 0])\n              ([i (in-range (/\
        \ n 2))])\n      (let ([current-pair-sum (+ (vector-ref sorted-nums i)\n   \
        \                              (vector-ref sorted-nums (- (- n 1) i)))])\n \
        \       (max max-sum current-pair-sum)))))"
      erlang: "-module(solution).\n-export([min_pair_sum/1]).\n\nmin_pair_sum(Nums)\
        \ ->\n    SortedNums = lists:sort(Nums),\n    N = length(SortedNums),\n    HalfN\
        \ = N div 2,\n    {LeftHalf, RightHalf} = lists:split(HalfN, SortedNums),\n\
        \    ReversedRightHalf = lists:reverse(RightHalf),\n\n    ZippedPairs = lists:zip(LeftHalf,\
        \ ReversedRightHalf),\n\n    lists:foldl(fun({A, B}, AccMax) ->\n          \
        \              max(AccMax, A + B)\n                end, 0, ZippedPairs)."
      elixir: "defmodule Solution do\n  @spec min_pair_sum(nums :: [integer]) :: integer\n\
        \  def min_pair_sum(nums) do\n    sorted_nums = Enum.sort(nums)\n    n = length(sorted_nums)\n\
        \    half_n = div(n, 2)\n\n    {left_half, right_half} = Enum.split(sorted_nums,\
        \ half_n)\n\n    reversed_right_half = Enum.reverse(right_half)\n\n    Enum.zip(left_half,\
        \ reversed_right_half)\n    |> Enum.reduce(0, fn {a, b}, acc_max ->\n      max(acc_max,\
        \ a + b)\n    end)\n  end\nend"
    approach: 'The problem asks to minimize the maximum pair sum by optimally pairing
      elements from an array of even length. The key insight is that to minimize the
      largest sum, we should try to make all sums as balanced as possible. This can
      be achieved by pairing the smallest available number with the largest available
      number.


      Therefore, the optimal strategy involves first sorting the input array nums in
      ascending order. After sorting, we iterate from both ends of the array simultaneously.
      We pair the element at index i (smallest available) with the element at index
      n - 1 - i (largest available) for i from 0 to n/2 - 1. For each such pair, we
      calculate their sum and keep track of the maximum sum encountered. This maximum
      sum will be the minimized maximum pair sum.'
    time_complexity: The dominant operation is sorting the array, which takes O(N log
      N) time, where N is the number of elements in nums. The subsequent loop to form
      pairs and find the maximum sum iterates N/2 times, contributing O(N) time. Thus,
      the overall time complexity is O(N log N).
    space_complexity: The space complexity depends on the sorting algorithm used. If
      an in-place sort (like heapsort or quicksort in some implementations) is used,
      the space complexity can be O(1) or O(log N) for recursion stack. If a non-in-place
      sort (like merge sort or Python's Timsort) is used, it may require O(N) auxiliary
      space. Given that standard library sort functions often use O(N) space in the
      worst case (e.g., Timsort in Python), the space complexity is O(N).
    elapsed_time: 53.51784539222717
    model: gemini-2.5-flash
    generated_at: '2026-01-24 01:08:38 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int minPairSum(vector<int>& nums) {\n   \
        \     sort(nums.begin(), nums.end());\n        int max_sum = 0;\n        int\
        \ left = 0, right = nums.size() - 1;\n        while (left < right) {\n     \
        \       max_sum = max(max_sum, nums[left] + nums[right]);\n            left++;\n\
        \            right--;\n        }\n        return max_sum;\n    }\n};"
      java: "class Solution {\n    public int minPairSum(int[] nums) {\n        Arrays.sort(nums);\n\
        \        int max_sum = 0;\n        int left = 0, right = nums.length - 1;\n\
        \        while (left < right) {\n            max_sum = Math.max(max_sum, nums[left]\
        \ + nums[right]);\n            left++;\n            right--;\n        }\n  \
        \      return max_sum;\n    }\n}"
      python: "class Solution(object):\n    def minPairSum(self, nums):\n        nums.sort()\n\
        \        max_sum = 0\n        left, right = 0, len(nums) - 1\n        while\
        \ left < right:\n            max_sum = max(max_sum, nums[left] + nums[right])\n\
        \            left += 1\n            right -= 1\n        return max_sum"
      python3: "class Solution:\n    def minPairSum(self, nums: list[int]) -> int:\n\
        \        nums.sort()\n        max_sum = 0\n        left, right = 0, len(nums)\
        \ - 1\n        while left < right:\n            max_sum = max(max_sum, nums[left]\
        \ + nums[right])\n            left += 1\n            right -= 1\n        return\
        \ max_sum"
      c: "int minPairSum(int* nums, int numsSize) {\n    qsort(nums, numsSize, sizeof(int),\
        \ compare);\n    int max_sum = 0;\n    int left = 0, right = numsSize - 1;\n\
        \    while (left < right) {\n        max_sum = (max_sum > nums[left] + nums[right])\
        \ ? max_sum : nums[left] + nums[right];\n        left++;\n        right--;\n\
        \    }\n    return max_sum;\n}\nint compare(const void *a, const void *b) {\n\
        \    return (*(int*)a - *(int*)b);\n}"
      csharp: "public class Solution {\n    public int MinPairSum(int[] nums) {\n  \
        \      Array.Sort(nums);\n        int max_sum = 0;\n        int left = 0, right\
        \ = nums.Length - 1;\n        while (left < right) {\n            max_sum =\
        \ Math.Max(max_sum, nums[left] + nums[right]);\n            left++;\n      \
        \      right--;\n        }\n        return max_sum;\n    }\n}"
      javascript: "var minPairSum = function(nums) {\n    nums.sort((a, b) => a - b);\n\
        \    let max_sum = 0;\n    let left = 0, right = nums.length - 1;\n    while\
        \ (left < right) {\n        max_sum = Math.max(max_sum, nums[left] + nums[right]);\n\
        \        left++;\n        right--;\n    }\n    return max_sum;\n};"
      typescript: "function minPairSum(nums: number[]): number {\n    nums.sort((a,\
        \ b) => a - b);\n    let max_sum = 0;\n    let left = 0, right = nums.length\
        \ - 1;\n    while (left < right) {\n        max_sum = Math.max(max_sum, nums[left]\
        \ + nums[right]);\n        left++;\n        right--;\n    }\n    return max_sum;\n\
        }"
      php: "class Solution {\n    function minPairSum($nums) {\n        sort($nums);\n\
        \        $max_sum = 0;\n        $left = 0;\n        $right = count($nums) -\
        \ 1;\n        while ($left < $right) {\n            $max_sum = max($max_sum,\
        \ $nums[$left] + $nums[$right]);\n            $left++;\n            $right--;\n\
        \        }\n        return $max_sum;\n    }\n}"
      swift: "class Solution {\n    func minPairSum(_ nums: [Int]) -> Int {\n      \
        \  let sortedNums = nums.sorted()\n        var max_sum = 0\n        var left\
        \ = 0\n        var right = sortedNums.count - 1\n        while left < right\
        \ {\n            max_sum = max(max_sum, sortedNums[left] + sortedNums[right])\n\
        \            left += 1\n            right -= 1\n        }\n        return max_sum\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun minPairSum(nums: IntArray): Int {\n       \
        \ nums.sort()\n        var maxSum = 0\n        var left = 0\n        var right\
        \ = nums.size - 1\n        while (left < right) {\n            maxSum = maxOf(maxSum,\
        \ nums[left] + nums[right])\n            left++\n            right--\n     \
        \   }\n        return maxSum\n    }\n}"
      dart: "class Solution {\n    int minPairSum(List<int> nums) {\n        nums.sort()\n\
        \        int maxSum = 0\n        int left = 0\n        int right = nums.length\
        \ - 1\n        while (left < right) {\n            maxSum = max(maxSum, nums[left]\
        \ + nums[right])\n            left++\n            right--\n        }\n     \
        \   return maxSum\n    }\n}"
      go: "func minPairSum(nums []int) int {\n    sort.Ints(nums)\n    maxSum := 0\n\
        \    left, right := 0, len(nums)-1\n    for left < right {\n        if nums[left]+nums[right]\
        \ > maxSum {\n            maxSum = nums[left] + nums[right]\n        }\n   \
        \     left++\n        right--\n    }\n    return maxSum\n}"
      ruby: "def min_pair_sum(nums)\n    nums.sort!\n    max_sum = 0\n    left, right\
        \ = 0, nums.size - 1\n    while left < right\n        max_sum = [max_sum, nums[left]\
        \ + nums[right]].max\n        left += 1\n        right -= 1\n    end\n    max_sum\n\
        end"
      scala: "object Solution {\n    def minPairSum(nums: Array[Int]): Int = {\n   \
        \     val sortedNums = nums.sorted\n        var maxSum = 0\n        var left\
        \ = 0\n        var right = sortedNums.length - 1\n        while (left < right)\
        \ {\n            maxSum = Math.max(maxSum, sortedNums(left) + sortedNums(right))\n\
        \            left += 1\n            right -= 1\n        }\n        maxSum\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn min_pair_sum(nums: Vec<i32>) -> i32 {\n   \
        \     let mut nums = nums;\n        nums.sort_unstable();\n        let mut max_sum\
        \ = 0;\n        let mut left = 0;\n        let mut right = nums.len() - 1;\n\
        \        while left < right {\n            max_sum = max_sum.max(nums[left]\
        \ + nums[right]);\n            left += 1;\n            right -= 1;\n       \
        \ }\n        max_sum\n    }\n}"
      racket: "(define/contract (min-pair-sum nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (let* (\n           (sorted-nums (sort nums <))\n           (max-sum 0)\n\
        \           (left 0)\n           (right (sub1 (length sorted-nums))))\n    (let\
        \ loop ((left left) (right right))\n      (if (< left right)\n          (loop\
        \ (add1 left) (sub1 right)\n                (max max-sum (+ (list-ref sorted-nums\
        \ left) (list-ref sorted-nums right))))\n          max-sum))))"
      erlang: "min_pair_sum(Nums) ->\n    lists:max([lists:nth(I, lists:sort(Nums))\
        \ + lists:nth(length(Nums) - I + 1, lists:sort(Nums)) || I <- lists:seq(1, length(Nums)\
        \ div 2)])."
      elixir: "def min_pair_sum(nums) do\n    sorted_nums = Enum.sort(nums)\n    max_sum\
        \ = 0\n    left = 0\n    right = length(sorted_nums) - 1\n    while left < right\
        \ do\n        max_sum = max(max_sum, Enum.at(sorted_nums, left) + Enum.at(sorted_nums,\
        \ right))\n        left = left + 1\n        right = right - 1\n    end\n   \
        \ max_sum\nend"
    approach: The problem can be solved by first sorting the array in ascending order.
      Then, we pair the smallest element with the largest element, the second smallest
      element with the second largest element, and so on. This approach ensures that
      the maximum pair sum is minimized because the largest numbers are paired with
      the smallest numbers, resulting in the smallest possible maximum pair sum. The
      key intuition behind this approach is that by pairing the smallest numbers with
      the largest numbers, we are effectively reducing the maximum pair sum as much
      as possible.
    time_complexity: The time complexity of this solution is O(n log n) because we are
      sorting the array, which takes O(n log n) time in the worst case. After sorting,
      we iterate through the array to find the maximum pair sum, which takes O(n) time.
      Therefore, the overall time complexity is O(n log n) + O(n) = O(n log n).
    space_complexity: The space complexity of this solution is O(1) if we are allowed
      to modify the input array, or O(n) if we need to create a copy of the array. This
      is because we only need a constant amount of space to store the maximum pair sum,
      or we need to create a copy of the array if we are not allowed to modify the input
      array.
    elapsed_time: 5.068329334259033
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-24 01:08:48 '
---

## Problem #1877: Minimize Maximum Pair Sum in Array

**Difficulty:** Medium

**Topics:** Array, Two Pointers, Greedy, Sorting

## Problem Description

<p>The <strong>pair sum</strong> of a pair <code>(a,b)</code> is equal to <code>a + b</code>. The <strong>maximum pair sum</strong> is the largest <strong>pair sum</strong> in a list of pairs.</p>

<ul>
	<li>For example, if we have pairs <code>(1,5)</code>, <code>(2,3)</code>, and <code>(4,4)</code>, the <strong>maximum pair sum</strong> would be <code>max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8</code>.</li>
</ul>

<p>Given an array <code>nums</code> of <strong>even</strong> length <code>n</code>, pair up the elements of <code>nums</code> into <code>n / 2</code> pairs such that:</p>

<ul>
	<li>Each element of <code>nums</code> is in <strong>exactly one</strong> pair, and</li>
	<li>The <strong>maximum pair sum </strong>is <strong>minimized</strong>.</li>
</ul>

<p>Return <em>the minimized <strong>maximum pair sum</strong> after optimally pairing up the elements</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,5,2,3]
<strong>Output:</strong> 7
<strong>Explanation:</strong> The elements can be paired up into pairs (3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,5,4,2,4,6]
<strong>Output:</strong> 8
<strong>Explanation:</strong> The elements can be paired up into pairs (3,5), (4,4), and (6,2).
The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>n</code> is <strong>even</strong>.</li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

## Hints

1. Would sorting help find the optimal order?

2. Given a specific element, how would you minimize its specific pairwise sum?

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-24 01:08:38 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks to minimize the maximum pair sum by optimally pairing elements from an array of even length. The key insight is that to minimize the largest sum, we should try to make all sums as balanced as possible. This can be achieved by pairing the smallest available number with the largest available number.

Therefore, the optimal strategy involves first sorting the input array nums in ascending order. After sorting, we iterate from both ends of the array simultaneously. We pair the element at index i (smallest available) with the element at index n - 1 - i (largest available) for i from 0 to n/2 - 1. For each such pair, we calculate their sum and keep track of the maximum sum encountered. This maximum sum will be the minimized maximum pair sum.

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
    int minPairSum(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int max_pair_sum = 0;
        int n = nums.size();
        for (int i = 0; i < n / 2; ++i) {
            max_pair_sum = std::max(max_pair_sum, nums[i] + nums[n - 1 - i]);
        }
        return max_pair_sum;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;

class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int maxPairSum = 0;
        int n = nums.length;
        for (int i = 0; i < n / 2; i++) {
            maxPairSum = Math.max(maxPairSum, nums[i] + nums[n - 1 - i]);
        }
        return maxPairSum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_pair_sum = 0
        n = len(nums)
        for i in range(n // 2):
            max_pair_sum = max(max_pair_sum, nums[i] + nums[n - 1 - i])
        return max_pair_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_pair_sum = 0
        n = len(nums)
        for i in range(n // 2):
            max_pair_sum = max(max_pair_sum, nums[i] + nums[n - 1 - i])
        return max_pair_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int minPairSum(int* nums, int numsSize){
    qsort(nums, numsSize, sizeof(int), compare);

    int max_pair_sum = 0;
    for (int i = 0; i < numsSize / 2; ++i) {
        int current_sum = nums[i] + nums[numsSize - 1 - i];
        if (current_sum > max_pair_sum) {
            max_pair_sum = current_sum;
        }
    }
    return max_pair_sum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinPairSum(int[] nums) {
        Array.Sort(nums);
        int maxPairSum = 0;
        int n = nums.Length;
        for (int i = 0; i < n / 2; i++) {
            maxPairSum = Math.Max(maxPairSum, nums[i] + nums[n - 1 - i]);
        }
        return maxPairSum;
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
var minPairSum = function(nums) {
    nums.sort((a, b) => a - b);
    let maxPairSum = 0;
    const n = nums.length;
    for (let i = 0; i < n / 2; i++) {
        maxPairSum = Math.max(maxPairSum, nums[i] + nums[n - 1 - i]);
    }
    return maxPairSum;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minPairSum(nums: number[]): number {
    nums.sort((a, b) => a - b);
    let maxPairSum: number = 0;
    const n: number = nums.length;
    for (let i = 0; i < n / 2; i++) {
        maxPairSum = Math.max(maxPairSum, nums[i] + nums[n - 1 - i]);
    }
    return maxPairSum;
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
    function minPairSum($nums) {
        sort($nums);
        $maxPairSum = 0;
        $n = count($nums);
        for ($i = 0; $i < $n / 2; $i++) {
            $maxPairSum = max($maxPairSum, $nums[$i] + $nums[$n - 1 - $i]);
        }
        return $maxPairSum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minPairSum(_ nums: [Int]) -> Int {
        var sortedNums = nums.sorted()
        var maxPairSum = 0
        let n = sortedNums.count
        for i in 0..<n/2 {
            maxPairSum = max(maxPairSum, sortedNums[i] + sortedNums[n - 1 - i])
        }
        return maxPairSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minPairSum(nums: IntArray): Int {
        nums.sort()
        var maxPairSum = 0
        val n = nums.size
        for (i in 0 until n / 2) {
            val currentPairSum = nums[i] + nums[n - 1 - i]
            if (currentPairSum > maxPairSum) {
                maxPairSum = currentPairSum
            }
        }
        return maxPairSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:math' as math;

class Solution {
  int minPairSum(List<int> nums) {
    nums.sort();
    int maxPairSum = 0;
    int n = nums.length;
    for (int i = 0; i < n ~/ 2; i++) {
      int currentPairSum = nums[i] + nums[n - 1 - i];
      maxPairSum = math.max(maxPairSum, currentPairSum);
    }
    return maxPairSum;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
    "sort"
)

func minPairSum(nums []int) int {
    sort.Ints(nums)
    maxPairSum := 0
    n := len(nums)
    for i := 0; i < n/2; i++ {
        currentPairSum := nums[i] + nums[n - 1 - i]
        if currentPairSum > maxPairSum {
            maxPairSum = currentPairSum
        }
    }
    return maxPairSum
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def min_pair_sum(nums)
    nums.sort!
    max_pair_sum = 0
    n = nums.length
    (0...n/2).each do |i|
        current_pair_sum = nums[i] + nums[n - 1 - i]
        max_pair_sum = [max_pair_sum, current_pair_sum].max
    end
    max_pair_sum
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minPairSum(nums: Array[Int]): Int = {
        val sortedNums = nums.sorted
        var maxPairSum = 0
        val n = sortedNums.length
        for (i <- 0 until n / 2) {
            val currentPairSum = sortedNums(i) + sortedNums(n - 1 - i)
            if (currentPairSum > maxPairSum) {
                maxPairSum = currentPairSum
            }
        }
        maxPairSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_pair_sum(mut nums: Vec<i32>) -> i32 {
        nums.sort();
        let mut max_pair_sum = 0;
        let n = nums.len();
        for i in 0..n/2 {
            let current_pair_sum = nums[i] + nums[n - 1 - i];
            if current_pair_sum > max_pair_sum {
                max_pair_sum = current_pair_sum;
            }
        }
        max_pair_sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-pair-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([sorted-nums (list->vector (sort nums <))]
         [n (vector-length sorted-nums)])
    (for/fold ([max-sum 0])
              ([i (in-range (/ n 2))])
      (let ([current-pair-sum (+ (vector-ref sorted-nums i)
                                 (vector-ref sorted-nums (- (- n 1) i)))])
        (max max-sum current-pair-sum)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([min_pair_sum/1]).

min_pair_sum(Nums) ->
    SortedNums = lists:sort(Nums),
    N = length(SortedNums),
    HalfN = N div 2,
    {LeftHalf, RightHalf} = lists:split(HalfN, SortedNums),
    ReversedRightHalf = lists:reverse(RightHalf),

    ZippedPairs = lists:zip(LeftHalf, ReversedRightHalf),

    lists:foldl(fun({A, B}, AccMax) ->
                        max(AccMax, A + B)
                end, 0, ZippedPairs).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_pair_sum(nums :: [integer]) :: integer
  def min_pair_sum(nums) do
    sorted_nums = Enum.sort(nums)
    n = length(sorted_nums)
    half_n = div(n, 2)

    {left_half, right_half} = Enum.split(sorted_nums, half_n)

    reversed_right_half = Enum.reverse(right_half)

    Enum.zip(left_half, reversed_right_half)
    |> Enum.reduce(0, fn {a, b}, acc_max ->
      max(acc_max, a + b)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The dominant operation is sorting the array, which takes O(N log N) time, where N is the number of elements in nums. The subsequent loop to form pairs and find the maximum sum iterates N/2 times, contributing O(N) time. Thus, the overall time complexity is O(N log N).

- **Space Complexity:** The space complexity depends on the sorting algorithm used. If an in-place sort (like heapsort or quicksort in some implementations) is used, the space complexity can be O(1) or O(log N) for recursion stack. If a non-in-place sort (like merge sort or Python's Timsort) is used, it may require O(N) auxiliary space. Given that standard library sort functions often use O(N) space in the worst case (e.g., Timsort in Python), the space complexity is O(N).

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-24 01:08:48 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by first sorting the array in ascending order. Then, we pair the smallest element with the largest element, the second smallest element with the second largest element, and so on. This approach ensures that the maximum pair sum is minimized because the largest numbers are paired with the smallest numbers, resulting in the smallest possible maximum pair sum. The key intuition behind this approach is that by pairing the smallest numbers with the largest numbers, we are effectively reducing the maximum pair sum as much as possible.

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
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int max_sum = 0;
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            max_sum = max(max_sum, nums[left] + nums[right]);
            left++;
            right--;
        }
        return max_sum;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int max_sum = 0;
        int left = 0, right = nums.length - 1;
        while (left < right) {
            max_sum = Math.max(max_sum, nums[left] + nums[right]);
            left++;
            right--;
        }
        return max_sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        max_sum = 0
        left, right = 0, len(nums) - 1
        while left < right:
            max_sum = max(max_sum, nums[left] + nums[right])
            left += 1
            right -= 1
        return max_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        max_sum = 0
        left, right = 0, len(nums) - 1
        while left < right:
            max_sum = max(max_sum, nums[left] + nums[right])
            left += 1
            right -= 1
        return max_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minPairSum(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), compare);
    int max_sum = 0;
    int left = 0, right = numsSize - 1;
    while (left < right) {
        max_sum = (max_sum > nums[left] + nums[right]) ? max_sum : nums[left] + nums[right];
        left++;
        right--;
    }
    return max_sum;
}
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinPairSum(int[] nums) {
        Array.Sort(nums);
        int max_sum = 0;
        int left = 0, right = nums.Length - 1;
        while (left < right) {
            max_sum = Math.Max(max_sum, nums[left] + nums[right]);
            left++;
            right--;
        }
        return max_sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var minPairSum = function(nums) {
    nums.sort((a, b) => a - b);
    let max_sum = 0;
    let left = 0, right = nums.length - 1;
    while (left < right) {
        max_sum = Math.max(max_sum, nums[left] + nums[right]);
        left++;
        right--;
    }
    return max_sum;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minPairSum(nums: number[]): number {
    nums.sort((a, b) => a - b);
    let max_sum = 0;
    let left = 0, right = nums.length - 1;
    while (left < right) {
        max_sum = Math.max(max_sum, nums[left] + nums[right]);
        left++;
        right--;
    }
    return max_sum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function minPairSum($nums) {
        sort($nums);
        $max_sum = 0;
        $left = 0;
        $right = count($nums) - 1;
        while ($left < $right) {
            $max_sum = max($max_sum, $nums[$left] + $nums[$right]);
            $left++;
            $right--;
        }
        return $max_sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minPairSum(_ nums: [Int]) -> Int {
        let sortedNums = nums.sorted()
        var max_sum = 0
        var left = 0
        var right = sortedNums.count - 1
        while left < right {
            max_sum = max(max_sum, sortedNums[left] + sortedNums[right])
            left += 1
            right -= 1
        }
        return max_sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minPairSum(nums: IntArray): Int {
        nums.sort()
        var maxSum = 0
        var left = 0
        var right = nums.size - 1
        while (left < right) {
            maxSum = maxOf(maxSum, nums[left] + nums[right])
            left++
            right--
        }
        return maxSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int minPairSum(List<int> nums) {
        nums.sort()
        int maxSum = 0
        int left = 0
        int right = nums.length - 1
        while (left < right) {
            maxSum = max(maxSum, nums[left] + nums[right])
            left++
            right--
        }
        return maxSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minPairSum(nums []int) int {
    sort.Ints(nums)
    maxSum := 0
    left, right := 0, len(nums)-1
    for left < right {
        if nums[left]+nums[right] > maxSum {
            maxSum = nums[left] + nums[right]
        }
        left++
        right--
    }
    return maxSum
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def min_pair_sum(nums)
    nums.sort!
    max_sum = 0
    left, right = 0, nums.size - 1
    while left < right
        max_sum = [max_sum, nums[left] + nums[right]].max
        left += 1
        right -= 1
    end
    max_sum
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minPairSum(nums: Array[Int]): Int = {
        val sortedNums = nums.sorted
        var maxSum = 0
        var left = 0
        var right = sortedNums.length - 1
        while (left < right) {
            maxSum = Math.max(maxSum, sortedNums(left) + sortedNums(right))
            left += 1
            right -= 1
        }
        maxSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_pair_sum(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        nums.sort_unstable();
        let mut max_sum = 0;
        let mut left = 0;
        let mut right = nums.len() - 1;
        while left < right {
            max_sum = max_sum.max(nums[left] + nums[right]);
            left += 1;
            right -= 1;
        }
        max_sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-pair-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* (
           (sorted-nums (sort nums <))
           (max-sum 0)
           (left 0)
           (right (sub1 (length sorted-nums))))
    (let loop ((left left) (right right))
      (if (< left right)
          (loop (add1 left) (sub1 right)
                (max max-sum (+ (list-ref sorted-nums left) (list-ref sorted-nums right))))
          max-sum))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
min_pair_sum(Nums) ->
    lists:max([lists:nth(I, lists:sort(Nums)) + lists:nth(length(Nums) - I + 1, lists:sort(Nums)) || I <- lists:seq(1, length(Nums) div 2)]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def min_pair_sum(nums) do
    sorted_nums = Enum.sort(nums)
    max_sum = 0
    left = 0
    right = length(sorted_nums) - 1
    while left < right do
        max_sum = max(max_sum, Enum.at(sorted_nums, left) + Enum.at(sorted_nums, right))
        left = left + 1
        right = right - 1
    end
    max_sum
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n log n) because we are sorting the array, which takes O(n log n) time in the worst case. After sorting, we iterate through the array to find the maximum pair sum, which takes O(n) time. Therefore, the overall time complexity is O(n log n) + O(n) = O(n log n).

- **Space Complexity:** The space complexity of this solution is O(1) if we are allowed to modify the input array, or O(n) if we need to create a copy of the array. This is because we only need a constant amount of space to store the maximum pair sum, or we need to create a copy of the array if we are not allowed to modify the input array.

</div>
</details>
