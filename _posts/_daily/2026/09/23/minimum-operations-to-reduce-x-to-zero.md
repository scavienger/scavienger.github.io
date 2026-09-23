---
layout: post
title: "Minimum Operations to Reduce X to Zero"
date: 2026-09-23 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Binary Search", "Sliding Window", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minOperations(vector<int>& nums, int\
        \ x) {\n        int totalSum = 0;\n        for (int num : nums) totalSum +=\
        \ num;\n        int target = totalSum - x;\n        if (target < 0) return -1;\n\
        \        if (target == 0) return nums.size();\n\n        int n = nums.size();\n\
        \        int currentSum = 0;\n        int maxLen = -1;\n        int left = 0;\n\
        \n        for (int right = 0; right < n; ++right) {\n            currentSum\
        \ += nums[right];\n            while (currentSum > target && left <= right)\
        \ {\n                currentSum -= nums[left];\n                left++;\n  \
        \          }\n            if (currentSum == target) {\n                maxLen\
        \ = max(maxLen, right - left + 1);\n            }\n        }\n\n        return\
        \ maxLen == -1 ? -1 : n - maxLen;\n    }\n};"
      java: "class Solution {\n    public int minOperations(int[] nums, int x) {\n \
        \       int totalSum = 0;\n        for (int num : nums) totalSum += num;\n \
        \       int target = totalSum - x;\n        if (target < 0) return -1;\n   \
        \     if (target == 0) return nums.length;\n\n        int n = nums.length;\n\
        \        int currentSum = 0;\n        int maxLen = -1;\n        int left = 0;\n\
        \n        for (int right = 0; right < n; right++) {\n            currentSum\
        \ += nums[right];\n            while (currentSum > target && left <= right)\
        \ {\n                currentSum -= nums[left];\n                left++;\n  \
        \          }\n            if (currentSum == target) {\n                maxLen\
        \ = Math.max(maxLen, right - left + 1);\n            }\n        }\n\n      \
        \  return maxLen == -1 ? -1 : n - maxLen;\n    }\n}"
      python: "class Solution(object):\n    def minOperations(self, nums, x):\n    \
        \    \"\"\"\n        :type nums: List[int]\n        :type x: int\n        :rtype:\
        \ int\n        \"\"\"\n        total_sum = sum(nums)\n        target = total_sum\
        \ - x\n        if target < 0:\n            return -1\n        if target == 0:\n\
        \            return len(nums)\n\n        n = len(nums)\n        max_len = -1\n\
        \        current_sum = 0\n        left = 0\n\n        for right in range(n):\n\
        \            current_sum += nums[right]\n            while current_sum > target\
        \ and left <= right:\n                current_sum -= nums[left]\n          \
        \      left += 1\n            if current_sum == target:\n                max_len\
        \ = max(max_len, right - left + 1)\n\n        return n - max_len if max_len\
        \ != -1 else -1"
      python3: "class Solution:\n    def minOperations(self, nums: list[int], x: int)\
        \ -> int:\n        total_sum = sum(nums)\n        target = total_sum - x\n \
        \       if target < 0:\n            return -1\n        if target == 0:\n   \
        \         return len(nums)\n\n        n = len(nums)\n        max_len = -1\n\
        \        current_sum = 0\n        left = 0\n\n        for right in range(n):\n\
        \            current_sum += nums[right]\n            while current_sum > target\
        \ and left <= right:\n                current_sum -= nums[left]\n          \
        \      left += 1\n            if current_sum == target:\n                max_len\
        \ = max(max_len, right - left + 1)\n\n        return n - max_len if max_len\
        \ != -1 else -1"
      c: "int minOperations(int* nums, int numsSize, int x) {\n    long long totalSum\
        \ = 0;\n    for (int i = 0; i < numsSize; i++) {\n        totalSum += nums[i];\n\
        \    }\n\n    long long target = totalSum - x;\n    if (target < 0) return -1;\n\
        \    if (target == 0) return numsSize;\n\n    int maxLen = -1;\n    long long\
        \ currentSum = 0;\n    int left = 0;\n\n    for (int right = 0; right < numsSize;\
        \ right++) {\n        currentSum += nums[right];\n        while (currentSum\
        \ > target && left <= right) {\n            currentSum -= nums[left];\n    \
        \        left++;\n        }\n        if (currentSum == target) {\n         \
        \   int currentLen = right - left + 1;\n            if (currentLen > maxLen)\
        \ {\n                maxLen = currentLen;\n            }\n        }\n    }\n\
        \n    return (maxLen == -1) ? -1 : numsSize - maxLen;\n}"
      csharp: "public class Solution {\n    public int MinOperations(int[] nums, int\
        \ x) {\n        int totalSum = 0;\n        for (int i = 0; i < nums.Length;\
        \ i++) {\n            totalSum += nums[i];\n        }\n        int target =\
        \ totalSum - x;\n        if (target < 0) return -1;\n        if (target == 0)\
        \ return nums.Length;\n\n        int n = nums.Length;\n        int left = 0;\n\
        \        int currentSum = 0;\n        int maxLen = -1;\n\n        for (int right\
        \ = 0; right < n; right++) {\n            currentSum += nums[right];\n     \
        \       while (currentSum > target && left <= right) {\n                currentSum\
        \ -= nums[left];\n                left++;\n            }\n            if (currentSum\
        \ == target) {\n                maxLen = System.Math.Max(maxLen, right - left\
        \ + 1);\n            }\n        }\n\n        return maxLen == -1 ? -1 : n -\
        \ maxLen;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} x\n * @return\
        \ {number}\n */\nvar minOperations = function(nums, x) {\n    let totalSum =\
        \ 0;\n    for (let i = 0; i < nums.length; i++) {\n        totalSum += nums[i];\n\
        \    }\n    const target = totalSum - x;\n    if (target < 0) return -1;\n \
        \   if (target === 0) return nums.length;\n\n    let left = 0;\n    let currentSum\
        \ = 0;\n    let maxLen = -1;\n    const n = nums.length;\n\n    for (let right\
        \ = 0; right < n; right++) {\n        currentSum += nums[right];\n        while\
        \ (currentSum > target && left <= right) {\n            currentSum -= nums[left];\n\
        \            left++;\n        }\n        if (currentSum === target) {\n    \
        \        maxLen = Math.max(maxLen, right - left + 1);\n        }\n    }\n\n\
        \    return maxLen === -1 ? -1 : n - maxLen;\n};"
      typescript: "function minOperations(nums: number[], x: number): number {\n   \
        \ let totalSum = 0;\n    for (let i = 0; i < nums.length; i++) {\n        totalSum\
        \ += nums[i];\n    }\n    const target = totalSum - x;\n    if (target < 0)\
        \ return -1;\n    if (target === 0) return nums.length;\n\n    let left = 0;\n\
        \    let currentSum = 0;\n    let maxLen = -1;\n    const n = nums.length;\n\
        \n    for (let right = 0; right < n; right++) {\n        currentSum += nums[right];\n\
        \        while (currentSum > target && left <= right) {\n            currentSum\
        \ -= nums[left];\n            left++;\n        }\n        if (currentSum ===\
        \ target) {\n            maxLen = Math.max(maxLen, right - left + 1);\n    \
        \    }\n    }\n\n    return maxLen === -1 ? -1 : n - maxLen;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $x\n     * @return Integer\n     */\n    function minOperations($nums,\
        \ $x) {\n        $totalSum = 0;\n        foreach ($nums as $num) {\n       \
        \     $totalSum += $num;\n        }\n        $target = $totalSum - $x;\n   \
        \     if ($target < 0) return -1;\n        if ($target == 0) return count($nums);\n\
        \n        $n = count($nums);\n        $left = 0;\n        $currentSum = 0;\n\
        \        $maxLen = -1;\n\n        for ($right = 0; $right < $n; $right++) {\n\
        \            $currentSum += $nums[$right];\n            while ($currentSum >\
        \ $target && $left <= $right) {\n                $currentSum -= $nums[$left];\n\
        \                $left++;\n            }\n            if ($currentSum == $target)\
        \ {\n                $maxLen = max($maxLen, $right - $left + 1);\n         \
        \   }\n        }\n\n        return $maxLen == -1 ? -1 : $n - $maxLen;\n    }\n\
        }"
      swift: "class Solution {\n    func minOperations(_ nums: [Int], _ x: Int) -> Int\
        \ {\n        var totalSum = 0\n        for num in nums { totalSum += num }\n\
        \        let target = totalSum - x\n        if target < 0 {\n            return\
        \ -1\n        }\n        if target == 0 {\n            return nums.count\n \
        \       }\n\n        let n = nums.count\n        var left = 0\n        var currentSum\
        \ = 0\n        var maxLen = -1\n\n        for right in 0..<n {\n           \
        \ currentSum += nums[right]\n            while currentSum > target && left <=\
        \ right {\n                currentSum -= nums[left]\n                left +=\
        \ 1\n            }\n            if currentSum == target {\n                maxLen\
        \ = max(maxLen, right - left + 1)\n            }\n        }\n\n        return\
        \ maxLen == -1 ? -1 : n - maxLen\n    }\n}"
      kotlin: "class Solution {\n    fun minOperations(nums: IntArray, x: Int): Int\
        \ {\n        val totalSum = nums.sum()\n        val target = totalSum - x\n\
        \        if (target < 0) return -1\n\n        var maxLen = -1\n        var currentSum\
        \ = 0\n        var left = 0\n        for (right in nums.indices) {\n       \
        \     currentSum += nums[right]\n            while (currentSum > target && left\
        \ <= right) {\n                currentSum -= nums[left]\n                left++\n\
        \            }\n            if (currentSum == target) {\n                val\
        \ currentLen = right - left + 1\n                if (currentLen > maxLen) {\n\
        \                    maxLen = currentLen\n                }\n            }\n\
        \        }\n\n        return if (maxLen == -1) -1 else nums.size - maxLen\n\
        \    }\n}"
      dart: "class Solution {\n  int minOperations(List<int> nums, int x) {\n    int\
        \ totalSum = 0;\n    for (int num in nums) {\n      totalSum += num;\n    }\n\
        \    int target = totalSum - x;\n    if (target < 0) return -1;\n\n    int maxLen\
        \ = -1;\n    int currentSum = 0;\n    int left = 0;\n    for (int right = 0;\
        \ right < nums.length; right++) {\n      currentSum += nums[right];\n      while\
        \ (currentSum > target && left <= right) {\n        currentSum -= nums[left];\n\
        \        left++;\n      }\n      if (currentSum == target) {\n        int currentLen\
        \ = right - left + 1;\n        if (currentLen > maxLen) {\n          maxLen\
        \ = currentLen;\n        }\n      }\n    }\n\n    return maxLen == -1 ? -1 :\
        \ nums.length - maxLen;\n  }\n}"
      go: "func minOperations(nums []int, x int) int {\n    totalSum := 0\n    for _,\
        \ num := range nums {\n        totalSum += num\n    }\n    target := totalSum\
        \ - x\n    if target < 0 {\n        return -1\n    }\n\n    maxLen := -1\n \
        \   currentSum := 0\n    left := 0\n    for right := 0; right < len(nums); right++\
        \ {\n        currentSum += nums[right]\n        for currentSum > target && left\
        \ <= right {\n            currentSum -= nums[left]\n            left++\n   \
        \     }\n        if currentSum == target {\n            if right-left+1 > maxLen\
        \ {\n                maxLen = right - left + 1\n            }\n        }\n \
        \   }\n\n    if maxLen == -1 {\n        return -1\n    }\n    return len(nums)\
        \ - maxLen\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer} x\n# @return {Integer}\n\
        def min_operations(nums, x)\n  total_sum = nums.sum\n  target = total_sum -\
        \ x\n  return -1 if target < 0\n\n  max_len = -1\n  current_sum = 0\n  left\
        \ = 0\n\n  nums.each_with_index do |num, right|\n    current_sum += num\n  \
        \  while current_sum > target && left <= right\n      current_sum -= nums[left]\n\
        \      left += 1\n    end\n    if current_sum == target\n      current_len =\
        \ right - left + 1\n      max_len = current_len if current_len > max_len\n \
        \   end\n  end\n\n  max_len == -1 ? -1 : nums.length - max_len\nend"
      scala: "object Solution {\n    def minOperations(nums: Array[Int], x: Int): Int\
        \ = {\n        var totalSum = 0\n        for (num <- nums) {\n            totalSum\
        \ += num\n        }\n        val target = totalSum - x\n        if (target <\
        \ 0) return -1\n\n        var maxLen = -1\n        var currentSum = 0\n    \
        \    var left = 0\n        for (right <- nums.indices) {\n            currentSum\
        \ += nums(right)\n            while (currentSum > target && left <= right) {\n\
        \                currentSum -= nums(left)\n                left += 1\n     \
        \       }\n            if (currentSum == target) {\n                maxLen =\
        \ math.max(maxLen, right - left + 1)\n            }\n        }\n\n        if\
        \ (maxLen == -1) -1 else nums.length - maxLen\n    }\n}"
      rust: "impl Solution {\n    pub fn min_operations(nums: Vec<i32>, x: i32) -> i32\
        \ {\n        let total_sum: i64 = nums.iter().map(|&val| val as i64).sum();\n\
        \        let target = total_sum - x as i64;\n        let n = nums.len();\n\n\
        \        if target < 0 {\n            return -1;\n        }\n        if target\
        \ == 0 {\n            return n as i32;\n        }\n\n        let mut max_len\
        \ = -1;\n        let mut current_sum = 0i64;\n        let mut left = 0;\n\n\
        \        for right in 0..n {\n            current_sum += nums[right] as i64;\n\
        \            while current_sum > target && left <= right {\n               \
        \ current_sum -= nums[left] as i64;\n                left += 1;\n          \
        \  }\n            if current_sum == target {\n                let current_len\
        \ = (right - left + 1) as i32;\n                if current_len > max_len {\n\
        \                    max_len = current_len;\n                }\n           \
        \ }\n        }\n\n        if max_len == -1 {\n            -1\n        } else\
        \ {\n            (n as i32) - max_len\n        }\n    }\n}"
      racket: "(define/contract (min-operations nums x)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer?)\n  (let* ([total-sum (foldl + 0 nums)]\n  \
        \       [target (- total-sum x)]\n         [len (length nums)])\n    (cond\n\
        \      [(< target 0) -1]\n      [(= target 0) len]\n      [else\n       (let\
        \ ([nums-vec (list->vector nums)])\n         (let loop ([left 0]\n         \
        \           [right 0]\n                    [current-sum 0]\n               \
        \     [max-len -1])\n           (if (< right len)\n               (let* ([new-sum\
        \ (+ current-sum (vector-ref nums-vec right))])\n                 (let-values\
        \ ([(shrunk-sum new-left)\n                               (let shrink ([l left]\
        \ [s new-sum])\n                                 (if (and (> s target) (<= l\
        \ right))\n                                     (shrink (+ l 1) (- s (vector-ref\
        \ nums-vec l)))\n                                     (values s l)))])\n   \
        \                (let ([updated-max-len (if (= shrunk-sum target)\n        \
        \                                      (max max-len (+ (- right new-left) 1))\n\
        \                                              max-len)])\n                \
        \     (loop new-left (+ right 1) shrunk-sum updated-max-len))))\n          \
        \     (if (= max-len -1) -1 (- len max-len))))])))"
      erlang: "-spec min_operations(Nums :: [integer()], X :: integer()) -> integer().\n\
        min_operations(Nums, X) ->\n    TotalSum = lists:sum(Nums),\n    Target = TotalSum\
        \ - X,\n    Len = length(Nums),\n    if\n        Target < 0 -> -1;\n       \
        \ Target =:= 0 -> Len;\n        true ->\n            NumsTuple = list_to_tuple(Nums),\n\
        \            MaxLen = solve_sliding_window(NumsTuple, Len, Target),\n      \
        \      if MaxLen =:= -1 -> -1; true -> Len - MaxLen end\n    end.\n\nsolve_sliding_window(NumsTuple,\
        \ Len, Target) ->\n    recursive_window(NumsTuple, Len, Target, 1, 1, 0, -1).\n\
        \nrecursive_window(NumsTuple, Len, Target, Left, Right, CurrentSum, MaxLen)\
        \ ->\n    if\n        Right =< Len ->\n            Val = element(Right, NumsTuple),\n\
        \            NewSum = CurrentSum + Val,\n            {ShrunkSum, NewLeft} =\
        \ shrink_window(NumsTuple, Target, Left, Right, NewSum),\n            NewMaxLen\
        \ = if\n                ShrunkSum =:= Target -> \n                    L = Right\
        \ - NewLeft + 1,\n                    if L > MaxLen -> L; true -> MaxLen end;\n\
        \                true -> MaxLen\n            end,\n            recursive_window(NumsTuple,\
        \ Len, Target, NewLeft, Right + 1, ShrunkSum, NewMaxLen);\n        true ->\n\
        \            MaxLen\n    end.\n\nshrink_window(NumsTuple, Target, Left, Right,\
        \ CurrentSum) ->\n    if\n        CurrentSum > Target, Left =< Right ->\n  \
        \          Val = element(Left, NumsTuple),\n            shrink_window(NumsTuple,\
        \ Target, Left + 1, Right, CurrentSum - Val);\n        true ->\n           \
        \ {CurrentSum, Left}\n    end."
      elixir: "defmodule Solution do\n  @spec min_operations(nums :: [integer], x ::\
        \ integer) :: integer\n  def min_operations(nums, x) do\n    total_sum = Enum.sum(nums)\n\
        \    target = total_sum - x\n    len = length(nums)\n\n    cond do\n      target\
        \ < 0 -> -1\n      target == 0 -> len\n      true ->\n        nums_tuple = List.to_tuple(nums)\n\
        \        max_len = solve_sliding_window(nums_tuple, len, target)\n        if\
        \ max_len == -1, do: -1, else: len - max_len\n    end\n  end\n\n  defp solve_sliding_window(nums_tuple,\
        \ len, target) do\n    recursive_window(nums_tuple, len, target, 0, 0, 0, -1)\n\
        \  end\n\n  defp recursive_window(nums_tuple, len, target, left, right, current_sum,\
        \ max_len) do\n    if right < len do\n      val = elem(nums_tuple, right)\n\
        \      new_sum = current_sum + val\n      {shrunk_sum, new_left} = shrink_window(nums_tuple,\
        \ target, left, right, new_sum)\n\n      new_max_len = if shrunk_sum == target\
        \ do\n        max(max_len, right - new_left + 1)\n      else\n        max_len\n\
        \      end\n\n      recursive_window(nums_tuple, len, target, new_left, right\
        \ + 1, shrunk_sum, new_max_len)\n    else\n      max_len\n    end\n  end\n\n\
        \  defp shrink_window(nums_tuple, target, left, right, current_sum) do\n   \
        \ if current_sum > target and left <= right do\n      shrink_window(nums_tuple,\
        \ target, left + 1, right, current_sum - elem(nums_tuple, left))\n    else\n\
        \      {current_sum, left}\n    end\n  end\nend"
    approach: 'The problem asks for the minimum number of elements to remove from the
      ends of an array to sum to x, which is mathematically equivalent to finding the
      maximum length of a contiguous subarray whose sum equals total_sum - x. This transformation
      allows us to use a sliding window approach to find a target value T = total_sum
      - x. If the target sum T is less than zero, it is impossible to reach x, and we
      return -1 immediately.


      To find the longest subarray summing to T, we use two pointers, left and right,
      to maintain a window. As the right pointer expands the window by adding elements
      to a running sum, we check if the sum exceeds T. If it does, we contract the window
      from the left until the sum is less than or equal to T. Whenever the current window
      sum equals T, we update the maximum subarray length found so far. The final answer
      is the total length of the array minus this maximum length, provided a valid subarray
      was found.'
    time_complexity: O(n) where n is the length of the input array. This is because
      both the left and right pointers traverse the array exactly once, meaning each
      element is added and subtracted from the window sum at most once.
    space_complexity: O(1) because the solution only uses a fixed number of integer
      variables (sum, target, pointers, and max length) to track state, regardless of
      the size of the input array.
    elapsed_time: 189.8913917541504
    model: gemini-3-flash-preview
    generated_at: '2026-09-23 02:44:08 '
---

## Problem #1658: Minimum Operations to Reduce X to Zero

**Difficulty:** Medium

**Topics:** Array, Hash Table, Binary Search, Sliding Window, Prefix Sum

## Problem Description

<p>You are given an integer array <code>nums</code> and an integer <code>x</code>. In one operation, you can either remove the leftmost or the rightmost element from the array <code>nums</code> and subtract its value from <code>x</code>. Note that this <strong>modifies</strong> the array for future operations.</p>

<p>Return <em>the <strong>minimum number</strong> of operations to reduce </em><code>x</code> <em>to <strong>exactly</strong></em> <code>0</code> <em>if it is possible</em><em>, otherwise, return </em><code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,4,2,3], x = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> The optimal solution is to remove the last two elements to reduce x to zero.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,6,7,8,9], x = 4
<strong>Output:</strong> -1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,20,1,1,3], x = 10
<strong>Output:</strong> 5
<strong>Explanation:</strong> The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= x &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Think in reverse; instead of finding the minimum prefix + suffix, find the maximum subarray.

2. Finding the maximum subarray is standard and can be done greedily.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the minimum number of elements to remove from the ends of an array to sum to x, which is mathematically equivalent to finding the maximum length of a contiguous subarray whose sum equals total_sum - x. This transformation allows us to use a sliding window approach to find a target value T = total_sum - x. If the target sum T is less than zero, it is impossible to reach x, and we return -1 immediately.

To find the longest subarray summing to T, we use two pointers, left and right, to maintain a window. As the right pointer expands the window by adding elements to a running sum, we check if the sum exceeds T. If it does, we contract the window from the left until the sum is less than or equal to T. Whenever the current window sum equals T, we update the maximum subarray length found so far. The final answer is the total length of the array minus this maximum length, provided a valid subarray was found.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang" id="lang-cpp" checked>
  <input type="radio" name="code-lang" id="lang-java">
  <input type="radio" name="code-lang" id="lang-python">
  <input type="radio" name="code-lang" id="lang-python3">
  <input type="radio" name="code-lang" id="lang-c">
  <input type="radio" name="code-lang" id="lang-csharp">
  <input type="radio" name="code-lang" id="lang-javascript">
  <input type="radio" name="code-lang" id="lang-typescript">
  <input type="radio" name="code-lang" id="lang-php">
  <input type="radio" name="code-lang" id="lang-swift">
  <input type="radio" name="code-lang" id="lang-kotlin">
  <input type="radio" name="code-lang" id="lang-dart">
  <input type="radio" name="code-lang" id="lang-go">
  <input type="radio" name="code-lang" id="lang-ruby">
  <input type="radio" name="code-lang" id="lang-scala">
  <input type="radio" name="code-lang" id="lang-rust">
  <input type="radio" name="code-lang" id="lang-racket">
  <input type="radio" name="code-lang" id="lang-erlang">
  <input type="radio" name="code-lang" id="lang-elixir">
  <div class="tab-labels">
    <label for="lang-cpp">C++</label>
    <label for="lang-java">Java</label>
    <label for="lang-python">Python</label>
    <label for="lang-python3">Python3</label>
    <label for="lang-c">C</label>
    <label for="lang-csharp">C#</label>
    <label for="lang-javascript">JavaScript</label>
    <label for="lang-typescript">TypeScript</label>
    <label for="lang-php">PHP</label>
    <label for="lang-swift">Swift</label>
    <label for="lang-kotlin">Kotlin</label>
    <label for="lang-dart">Dart</label>
    <label for="lang-go">Go</label>
    <label for="lang-ruby">Ruby</label>
    <label for="lang-scala">Scala</label>
    <label for="lang-rust">Rust</label>
    <label for="lang-racket">Racket</label>
    <label for="lang-erlang">Erlang</label>
    <label for="lang-elixir">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int totalSum = 0;
        for (int num : nums) totalSum += num;
        int target = totalSum - x;
        if (target < 0) return -1;
        if (target == 0) return nums.size();

        int n = nums.size();
        int currentSum = 0;
        int maxLen = -1;
        int left = 0;

        for (int right = 0; right < n; ++right) {
            currentSum += nums[right];
            while (currentSum > target && left <= right) {
                currentSum -= nums[left];
                left++;
            }
            if (currentSum == target) {
                maxLen = max(maxLen, right - left + 1);
            }
        }

        return maxLen == -1 ? -1 : n - maxLen;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minOperations(int[] nums, int x) {
        int totalSum = 0;
        for (int num : nums) totalSum += num;
        int target = totalSum - x;
        if (target < 0) return -1;
        if (target == 0) return nums.length;

        int n = nums.length;
        int currentSum = 0;
        int maxLen = -1;
        int left = 0;

        for (int right = 0; right < n; right++) {
            currentSum += nums[right];
            while (currentSum > target && left <= right) {
                currentSum -= nums[left];
                left++;
            }
            if (currentSum == target) {
                maxLen = Math.max(maxLen, right - left + 1);
            }
        }

        return maxLen == -1 ? -1 : n - maxLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        total_sum = sum(nums)
        target = total_sum - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        n = len(nums)
        max_len = -1
        current_sum = 0
        left = 0

        for right in range(n):
            current_sum += nums[right]
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                max_len = max(max_len, right - left + 1)

        return n - max_len if max_len != -1 else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        n = len(nums)
        max_len = -1
        current_sum = 0
        left = 0

        for right in range(n):
            current_sum += nums[right]
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                max_len = max(max_len, right - left + 1)

        return n - max_len if max_len != -1 else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minOperations(int* nums, int numsSize, int x) {
    long long totalSum = 0;
    for (int i = 0; i < numsSize; i++) {
        totalSum += nums[i];
    }

    long long target = totalSum - x;
    if (target < 0) return -1;
    if (target == 0) return numsSize;

    int maxLen = -1;
    long long currentSum = 0;
    int left = 0;

    for (int right = 0; right < numsSize; right++) {
        currentSum += nums[right];
        while (currentSum > target && left <= right) {
            currentSum -= nums[left];
            left++;
        }
        if (currentSum == target) {
            int currentLen = right - left + 1;
            if (currentLen > maxLen) {
                maxLen = currentLen;
            }
        }
    }

    return (maxLen == -1) ? -1 : numsSize - maxLen;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinOperations(int[] nums, int x) {
        int totalSum = 0;
        for (int i = 0; i < nums.Length; i++) {
            totalSum += nums[i];
        }
        int target = totalSum - x;
        if (target < 0) return -1;
        if (target == 0) return nums.Length;

        int n = nums.Length;
        int left = 0;
        int currentSum = 0;
        int maxLen = -1;

        for (int right = 0; right < n; right++) {
            currentSum += nums[right];
            while (currentSum > target && left <= right) {
                currentSum -= nums[left];
                left++;
            }
            if (currentSum == target) {
                maxLen = System.Math.Max(maxLen, right - left + 1);
            }
        }

        return maxLen == -1 ? -1 : n - maxLen;
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
 * @param {number} x
 * @return {number}
 */
var minOperations = function(nums, x) {
    let totalSum = 0;
    for (let i = 0; i < nums.length; i++) {
        totalSum += nums[i];
    }
    const target = totalSum - x;
    if (target < 0) return -1;
    if (target === 0) return nums.length;

    let left = 0;
    let currentSum = 0;
    let maxLen = -1;
    const n = nums.length;

    for (let right = 0; right < n; right++) {
        currentSum += nums[right];
        while (currentSum > target && left <= right) {
            currentSum -= nums[left];
            left++;
        }
        if (currentSum === target) {
            maxLen = Math.max(maxLen, right - left + 1);
        }
    }

    return maxLen === -1 ? -1 : n - maxLen;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minOperations(nums: number[], x: number): number {
    let totalSum = 0;
    for (let i = 0; i < nums.length; i++) {
        totalSum += nums[i];
    }
    const target = totalSum - x;
    if (target < 0) return -1;
    if (target === 0) return nums.length;

    let left = 0;
    let currentSum = 0;
    let maxLen = -1;
    const n = nums.length;

    for (let right = 0; right < n; right++) {
        currentSum += nums[right];
        while (currentSum > target && left <= right) {
            currentSum -= nums[left];
            left++;
        }
        if (currentSum === target) {
            maxLen = Math.max(maxLen, right - left + 1);
        }
    }

    return maxLen === -1 ? -1 : n - maxLen;
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
     * @param Integer $x
     * @return Integer
     */
    function minOperations($nums, $x) {
        $totalSum = 0;
        foreach ($nums as $num) {
            $totalSum += $num;
        }
        $target = $totalSum - $x;
        if ($target < 0) return -1;
        if ($target == 0) return count($nums);

        $n = count($nums);
        $left = 0;
        $currentSum = 0;
        $maxLen = -1;

        for ($right = 0; $right < $n; $right++) {
            $currentSum += $nums[$right];
            while ($currentSum > $target && $left <= $right) {
                $currentSum -= $nums[$left];
                $left++;
            }
            if ($currentSum == $target) {
                $maxLen = max($maxLen, $right - $left + 1);
            }
        }

        return $maxLen == -1 ? -1 : $n - $maxLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minOperations(_ nums: [Int], _ x: Int) -> Int {
        var totalSum = 0
        for num in nums { totalSum += num }
        let target = totalSum - x
        if target < 0 {
            return -1
        }
        if target == 0 {
            return nums.count
        }

        let n = nums.count
        var left = 0
        var currentSum = 0
        var maxLen = -1

        for right in 0..<n {
            currentSum += nums[right]
            while currentSum > target && left <= right {
                currentSum -= nums[left]
                left += 1
            }
            if currentSum == target {
                maxLen = max(maxLen, right - left + 1)
            }
        }

        return maxLen == -1 ? -1 : n - maxLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minOperations(nums: IntArray, x: Int): Int {
        val totalSum = nums.sum()
        val target = totalSum - x
        if (target < 0) return -1

        var maxLen = -1
        var currentSum = 0
        var left = 0
        for (right in nums.indices) {
            currentSum += nums[right]
            while (currentSum > target && left <= right) {
                currentSum -= nums[left]
                left++
            }
            if (currentSum == target) {
                val currentLen = right - left + 1
                if (currentLen > maxLen) {
                    maxLen = currentLen
                }
            }
        }

        return if (maxLen == -1) -1 else nums.size - maxLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minOperations(List<int> nums, int x) {
    int totalSum = 0;
    for (int num in nums) {
      totalSum += num;
    }
    int target = totalSum - x;
    if (target < 0) return -1;

    int maxLen = -1;
    int currentSum = 0;
    int left = 0;
    for (int right = 0; right < nums.length; right++) {
      currentSum += nums[right];
      while (currentSum > target && left <= right) {
        currentSum -= nums[left];
        left++;
      }
      if (currentSum == target) {
        int currentLen = right - left + 1;
        if (currentLen > maxLen) {
          maxLen = currentLen;
        }
      }
    }

    return maxLen == -1 ? -1 : nums.length - maxLen;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minOperations(nums []int, x int) int {
    totalSum := 0
    for _, num := range nums {
        totalSum += num
    }
    target := totalSum - x
    if target < 0 {
        return -1
    }

    maxLen := -1
    currentSum := 0
    left := 0
    for right := 0; right < len(nums); right++ {
        currentSum += nums[right]
        for currentSum > target && left <= right {
            currentSum -= nums[left]
            left++
        }
        if currentSum == target {
            if right-left+1 > maxLen {
                maxLen = right - left + 1
            }
        }
    }

    if maxLen == -1 {
        return -1
    }
    return len(nums) - maxLen
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @param {Integer} x
# @return {Integer}
def min_operations(nums, x)
  total_sum = nums.sum
  target = total_sum - x
  return -1 if target < 0

  max_len = -1
  current_sum = 0
  left = 0

  nums.each_with_index do |num, right|
    current_sum += num
    while current_sum > target && left <= right
      current_sum -= nums[left]
      left += 1
    end
    if current_sum == target
      current_len = right - left + 1
      max_len = current_len if current_len > max_len
    end
  end

  max_len == -1 ? -1 : nums.length - max_len
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minOperations(nums: Array[Int], x: Int): Int = {
        var totalSum = 0
        for (num <- nums) {
            totalSum += num
        }
        val target = totalSum - x
        if (target < 0) return -1

        var maxLen = -1
        var currentSum = 0
        var left = 0
        for (right <- nums.indices) {
            currentSum += nums(right)
            while (currentSum > target && left <= right) {
                currentSum -= nums(left)
                left += 1
            }
            if (currentSum == target) {
                maxLen = math.max(maxLen, right - left + 1)
            }
        }

        if (maxLen == -1) -1 else nums.length - maxLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_operations(nums: Vec<i32>, x: i32) -> i32 {
        let total_sum: i64 = nums.iter().map(|&val| val as i64).sum();
        let target = total_sum - x as i64;
        let n = nums.len();

        if target < 0 {
            return -1;
        }
        if target == 0 {
            return n as i32;
        }

        let mut max_len = -1;
        let mut current_sum = 0i64;
        let mut left = 0;

        for right in 0..n {
            current_sum += nums[right] as i64;
            while current_sum > target && left <= right {
                current_sum -= nums[left] as i64;
                left += 1;
            }
            if current_sum == target {
                let current_len = (right - left + 1) as i32;
                if current_len > max_len {
                    max_len = current_len;
                }
            }
        }

        if max_len == -1 {
            -1
        } else {
            (n as i32) - max_len
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-operations nums x)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([total-sum (foldl + 0 nums)]
         [target (- total-sum x)]
         [len (length nums)])
    (cond
      [(< target 0) -1]
      [(= target 0) len]
      [else
       (let ([nums-vec (list->vector nums)])
         (let loop ([left 0]
                    [right 0]
                    [current-sum 0]
                    [max-len -1])
           (if (< right len)
               (let* ([new-sum (+ current-sum (vector-ref nums-vec right))])
                 (let-values ([(shrunk-sum new-left)
                               (let shrink ([l left] [s new-sum])
                                 (if (and (> s target) (<= l right))
                                     (shrink (+ l 1) (- s (vector-ref nums-vec l)))
                                     (values s l)))])
                   (let ([updated-max-len (if (= shrunk-sum target)
                                              (max max-len (+ (- right new-left) 1))
                                              max-len)])
                     (loop new-left (+ right 1) shrunk-sum updated-max-len))))
               (if (= max-len -1) -1 (- len max-len))))])))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_operations(Nums :: [integer()], X :: integer()) -> integer().
min_operations(Nums, X) ->
    TotalSum = lists:sum(Nums),
    Target = TotalSum - X,
    Len = length(Nums),
    if
        Target < 0 -> -1;
        Target =:= 0 -> Len;
        true ->
            NumsTuple = list_to_tuple(Nums),
            MaxLen = solve_sliding_window(NumsTuple, Len, Target),
            if MaxLen =:= -1 -> -1; true -> Len - MaxLen end
    end.

solve_sliding_window(NumsTuple, Len, Target) ->
    recursive_window(NumsTuple, Len, Target, 1, 1, 0, -1).

recursive_window(NumsTuple, Len, Target, Left, Right, CurrentSum, MaxLen) ->
    if
        Right =< Len ->
            Val = element(Right, NumsTuple),
            NewSum = CurrentSum + Val,
            {ShrunkSum, NewLeft} = shrink_window(NumsTuple, Target, Left, Right, NewSum),
            NewMaxLen = if
                ShrunkSum =:= Target -> 
                    L = Right - NewLeft + 1,
                    if L > MaxLen -> L; true -> MaxLen end;
                true -> MaxLen
            end,
            recursive_window(NumsTuple, Len, Target, NewLeft, Right + 1, ShrunkSum, NewMaxLen);
        true ->
            MaxLen
    end.

shrink_window(NumsTuple, Target, Left, Right, CurrentSum) ->
    if
        CurrentSum > Target, Left =< Right ->
            Val = element(Left, NumsTuple),
            shrink_window(NumsTuple, Target, Left + 1, Right, CurrentSum - Val);
        true ->
            {CurrentSum, Left}
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_operations(nums :: [integer], x :: integer) :: integer
  def min_operations(nums, x) do
    total_sum = Enum.sum(nums)
    target = total_sum - x
    len = length(nums)

    cond do
      target < 0 -> -1
      target == 0 -> len
      true ->
        nums_tuple = List.to_tuple(nums)
        max_len = solve_sliding_window(nums_tuple, len, target)
        if max_len == -1, do: -1, else: len - max_len
    end
  end

  defp solve_sliding_window(nums_tuple, len, target) do
    recursive_window(nums_tuple, len, target, 0, 0, 0, -1)
  end

  defp recursive_window(nums_tuple, len, target, left, right, current_sum, max_len) do
    if right < len do
      val = elem(nums_tuple, right)
      new_sum = current_sum + val
      {shrunk_sum, new_left} = shrink_window(nums_tuple, target, left, right, new_sum)

      new_max_len = if shrunk_sum == target do
        max(max_len, right - new_left + 1)
      else
        max_len
      end

      recursive_window(nums_tuple, len, target, new_left, right + 1, shrunk_sum, new_max_len)
    else
      max_len
    end
  end

  defp shrink_window(nums_tuple, target, left, right, current_sum) do
    if current_sum > target and left <= right do
      shrink_window(nums_tuple, target, left + 1, right, current_sum - elem(nums_tuple, left))
    else
      {current_sum, left}
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the input array. This is because both the left and right pointers traverse the array exactly once, meaning each element is added and subtracted from the window sum at most once.
- **Space Complexity:** O(1) because the solution only uses a fixed number of integer variables (sum, target, pointers, and max length) to track state, regardless of the size of the input array.
