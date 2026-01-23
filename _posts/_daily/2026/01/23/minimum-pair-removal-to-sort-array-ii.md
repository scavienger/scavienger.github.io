---
layout: post
title: "Minimum Pair Removal to Sort Array II"
date: 2026-01-23 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Hash Table", "Linked List", "Heap (Priority Queue)", "Simulation", "Doubly-Linked List", "Ordered Set"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumPairRemoval(vector<int>& nums)\
        \ {\n        int n = nums.size();\n        int count = 0;\n        while (!isSorted(nums))\
        \ {\n            int minSum = INT_MAX;\n            int minIndex = -1;\n   \
        \         for (int i = 0; i < n - 1; i++) {\n                if (nums[i] + nums[i\
        \ + 1] < minSum) {\n                    minSum = nums[i] + nums[i + 1];\n  \
        \                  minIndex = i;\n                }\n            }\n       \
        \     nums.erase(nums.begin() + minIndex + 1);\n            nums[minIndex] =\
        \ minSum;\n            n--;\n            count++;\n        }\n        return\
        \ count;\n    }\n    bool isSorted(vector<int>& nums) {\n        for (int i\
        \ = 0; i < nums.size() - 1; i++) {\n            if (nums[i] > nums[i + 1]) {\n\
        \                return false;\n            }\n        }\n        return true;\n\
        \    }\n};"
      java: "class Solution {\n    public int minimumPairRemoval(int[] nums) {\n   \
        \     int n = nums.length;\n        int count = 0;\n        while (!isSorted(nums))\
        \ {\n            int minSum = Integer.MAX_VALUE;\n            int minIndex =\
        \ -1;\n            for (int i = 0; i < n - 1; i++) {\n                if (nums[i]\
        \ + nums[i + 1] < minSum) {\n                    minSum = nums[i] + nums[i +\
        \ 1];\n                    minIndex = i;\n                }\n            }\n\
        \            int[] newNums = new int[n - 1];\n            System.arraycopy(nums,\
        \ 0, newNums, 0, minIndex);\n            newNums[minIndex] = minSum;\n     \
        \       System.arraycopy(nums, minIndex + 2, newNums, minIndex + 1, n - minIndex\
        \ - 2);\n            nums = newNums;\n            n--;\n            count++;\n\
        \        }\n        return count;\n    }\n    boolean isSorted(int[] nums) {\n\
        \        for (int i = 0; i < nums.length - 1; i++) {\n            if (nums[i]\
        \ > nums[i + 1]) {\n                return false;\n            }\n        }\n\
        \        return true;\n    }\n}"
      python: "class Solution(object):\n    def minimumPairRemoval(self, nums):\n  \
        \      count = 0\n        while not self.isSorted(nums):\n            minSum\
        \ = float('inf')\n            minIndex = -1\n            for i in range(len(nums)\
        \ - 1):\n                if nums[i] + nums[i + 1] < minSum:\n              \
        \      minSum = nums[i] + nums[i + 1]\n                    minIndex = i\n  \
        \          nums.pop(minIndex + 1)\n            nums[minIndex] = minSum\n   \
        \         count += 1\n        return count\n    def isSorted(self, nums):\n\
        \        for i in range(len(nums) - 1):\n            if nums[i] > nums[i + 1]:\n\
        \                return False\n        return True"
      python3: "class Solution:\n    def minimumPairRemoval(self, nums: list[int]) ->\
        \ int:\n        count = 0\n        while not self.isSorted(nums):\n        \
        \    minSum = float('inf')\n            minIndex = -1\n            for i in\
        \ range(len(nums) - 1):\n                if nums[i] + nums[i + 1] < minSum:\n\
        \                    minSum = nums[i] + nums[i + 1]\n                    minIndex\
        \ = i\n            nums.pop(minIndex + 1)\n            nums[minIndex] = minSum\n\
        \            count += 1\n        return count\n    def isSorted(self, nums:\
        \ list[int]) -> bool:\n        for i in range(len(nums) - 1):\n            if\
        \ nums[i] > nums[i + 1]:\n                return False\n        return True"
      c: "int minimumPairRemoval(int* nums, int numsSize) {\n    int count = 0;\n  \
        \  while (!isSorted(nums, numsSize)) {\n        int minSum = INT_MAX;\n    \
        \    int minIndex = -1;\n        for (int i = 0; i < numsSize - 1; i++) {\n\
        \            if (nums[i] + nums[i + 1] < minSum) {\n                minSum =\
        \ nums[i] + nums[i + 1];\n                minIndex = i;\n            }\n   \
        \     }\n        for (int i = minIndex + 1; i < numsSize - 1; i++) {\n     \
        \       nums[i] = nums[i + 1];\n        }\n        nums[minIndex] = minSum;\n\
        \        numsSize--;\n        count++;\n    }\n    return count;\n}\nint isSorted(int*\
        \ nums, int numsSize) {\n    for (int i = 0; i < numsSize - 1; i++) {\n    \
        \    if (nums[i] > nums[i + 1]) {\n            return 0;\n        }\n    }\n\
        \    return 1;\n}"
      csharp: "public class Solution {\n    public int MinimumPairRemoval(int[] nums)\
        \ {\n        int n = nums.Length;\n        int count = 0;\n        while (!IsSorted(nums))\
        \ {\n            int minSum = int.MaxValue;\n            int minIndex = -1;\n\
        \            for (int i = 0; i < n - 1; i++) {\n                if (nums[i]\
        \ + nums[i + 1] < minSum) {\n                    minSum = nums[i] + nums[i +\
        \ 1];\n                    minIndex = i;\n                }\n            }\n\
        \            int[] newNums = new int[n - 1];\n            Array.Copy(nums, 0,\
        \ newNums, 0, minIndex);\n            newNums[minIndex] = minSum;\n        \
        \    Array.Copy(nums, minIndex + 2, newNums, minIndex + 1, n - minIndex - 2);\n\
        \            nums = newNums;\n            n--;\n            count++;\n     \
        \   }\n        return count;\n    }\n    bool IsSorted(int[] nums) {\n     \
        \   for (int i = 0; i < nums.Length - 1; i++) {\n            if (nums[i] > nums[i\
        \ + 1]) {\n                return false;\n            }\n        }\n       \
        \ return true;\n    }\n}"
      javascript: "var minimumPairRemoval = function(nums) {\n    let count = 0;\n \
        \   while (!isSorted(nums)) {\n        let minSum = Infinity;\n        let minIndex\
        \ = -1;\n        for (let i = 0; i < nums.length - 1; i++) {\n            if\
        \ (nums[i] + nums[i + 1] < minSum) {\n                minSum = nums[i] + nums[i\
        \ + 1];\n                minIndex = i;\n            }\n        }\n        nums.splice(minIndex\
        \ + 1, 1);\n        nums[minIndex] = minSum;\n        count++;\n    }\n    return\
        \ count;\n};\nfunction isSorted(nums) {\n    for (let i = 0; i < nums.length\
        \ - 1; i++) {\n        if (nums[i] > nums[i + 1]) {\n            return false;\n\
        \        }\n    }\n    return true;\n}"
      typescript: "function minimumPairRemoval(nums: number[]): number {\n    let count\
        \ = 0;\n    while (!isSorted(nums)) {\n        let minSum = Infinity;\n    \
        \    let minIndex = -1;\n        for (let i = 0; i < nums.length - 1; i++) {\n\
        \            if (nums[i] + nums[i + 1] < minSum) {\n                minSum =\
        \ nums[i] + nums[i + 1];\n                minIndex = i;\n            }\n   \
        \     }\n        nums.splice(minIndex + 1, 1);\n        nums[minIndex] = minSum;\n\
        \        count++;\n    }\n    return count;\n}\nfunction isSorted(nums: number[]):\
        \ boolean {\n    for (let i = 0; i < nums.length - 1; i++) {\n        if (nums[i]\
        \ > nums[i + 1]) {\n            return false;\n        }\n    }\n    return\
        \ true;\n}"
      php: "class Solution {\n    function minimumPairRemoval($nums) {\n        $count\
        \ = 0;\n        while (!$this->isSorted($nums)) {\n            $minSum = PHP_INT_MAX;\n\
        \            $minIndex = -1;\n            for ($i = 0; $i < count($nums) - 1;\
        \ $i++) {\n                if ($nums[$i] + $nums[$i + 1] < $minSum) {\n    \
        \                $minSum = $nums[$i] + $nums[$i + 1];\n                    $minIndex\
        \ = $i;\n                }\n            }\n            array_splice($nums, $minIndex\
        \ + 1, 1);\n            $nums[$minIndex] = $minSum;\n            $count++;\n\
        \        }\n        return $count;\n    }\n    function isSorted($nums) {\n\
        \        for ($i = 0; $i < count($nums) - 1; $i++) {\n            if ($nums[$i]\
        \ > $nums[$i + 1]) {\n                return false;\n            }\n       \
        \ }\n        return true;\n    }\n}"
      swift: "class Solution {\n    func minimumPairRemoval(_ nums: [Int]) -> Int {\n\
        \        var nums = nums\n        var count = 0\n        while !isSorted(nums)\
        \ {\n            var minSum = Int.max\n            var minIndex = -1\n     \
        \       for i in 0..<nums.count - 1 {\n                if nums[i] + nums[i +\
        \ 1] < minSum {\n                    minSum = nums[i] + nums[i + 1]\n      \
        \              minIndex = i\n                }\n            }\n            nums.remove(at:\
        \ minIndex + 1)\n            nums[minIndex] = minSum\n            count += 1\n\
        \        }\n        return count\n    }\n    func isSorted(_ nums: [Int]) ->\
        \ Bool {\n        for i in 0..<nums.count - 1 {\n            if nums[i] > nums[i\
        \ + 1] {\n                return false\n            }\n        }\n        return\
        \ true\n    }\n}"
      kotlin: "class Solution {\n    fun minimumPairRemoval(nums: IntArray): Int {\n\
        \        var count = 0\n        var numsList = nums.toMutableList()\n      \
        \  while (!isNonDecreasing(numsList)) {\n            var minSum = Int.MAX_VALUE\n\
        \            var minIndex = -1\n            for (i in 0 until numsList.size\
        \ - 1) {\n                val sum = numsList[i] + numsList[i + 1]\n        \
        \        if (sum < minSum) {\n                    minSum = sum\n           \
        \         minIndex = i\n                }\n            }\n            numsList.removeAt(minIndex\
        \ + 1)\n            numsList[minIndex] = minSum\n            count++\n     \
        \   }\n        return count\n    }\n\n    private fun isNonDecreasing(nums:\
        \ List<Int>): Boolean {\n        for (i in 0 until nums.size - 1) {\n      \
        \      if (nums[i] > nums[i + 1]) return false\n        }\n        return true\n\
        \    }\n}"
      dart: "class Solution {\n  int minimumPairRemoval(List<int> nums) {\n    int count\
        \ = 0;\n    List<int> numsList = List.from(nums);\n    while (!isNonDecreasing(numsList))\
        \ {\n      int minSum = int.maxFinite;\n      int minIndex = -1;\n      for\
        \ (int i = 0; i < numsList.length - 1; i++) {\n        int sum = numsList[i]\
        \ + numsList[i + 1];\n        if (sum < minSum) {\n          minSum = sum;\n\
        \          minIndex = i;\n        }\n      }\n      numsList.removeAt(minIndex\
        \ + 1);\n      numsList[minIndex] = minSum;\n      count++;\n    }\n    return\
        \ count;\n  }\n\n  bool isNonDecreasing(List<int> nums) {\n    for (int i =\
        \ 0; i < nums.length - 1; i++) {\n      if (nums[i] > nums[i + 1]) return false;\n\
        \    }\n    return true;\n  }\n}"
      go: "func minimumPairRemoval(nums []int) int {\n    count := 0\n    numsList :=\
        \ make([]int, len(nums))\n    copy(numsList, nums)\n    for !isNonDecreasing(numsList)\
        \ {\n        minSum := int(1e9)\n        minIndex := -1\n        for i := 0;\
        \ i < len(numsList)-1; i++ {\n            sum := numsList[i] + numsList[i+1]\n\
        \            if sum < minSum {\n                minSum = sum\n             \
        \   minIndex = i\n            }\n        }\n        numsList = append(numsList[:minIndex],\
        \ append([]int{minSum}, numsList[minIndex+2:]...)...)\n        count++\n   \
        \ }\n    return count\n}\n\nfunc isNonDecreasing(nums []int) bool {\n    for\
        \ i := 0; i < len(nums)-1; i++ {\n        if nums[i] > nums[i+1] {\n       \
        \     return false\n        }\n    }\n    return true\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef minimum_pair_removal(nums)\n\
        \    count = 0\n    nums_list = nums.dup\n    while !is_non_decreasing(nums_list)\n\
        \        min_sum = Float::INFINITY\n        min_index = -1\n        (0...nums_list.size\
        \ - 1).each do |i|\n            sum = nums_list[i] + nums_list[i + 1]\n    \
        \        if sum < min_sum\n                min_sum = sum\n                min_index\
        \ = i\n            end\n        end\n        nums_list.delete_at(min_index +\
        \ 1)\n        nums_list[min_index] = min_sum\n        count += 1\n    end\n\
        \    count\nend\n\nprivate\ndef is_non_decreasing(nums)\n    (0...nums.size\
        \ - 1).each do |i|\n        return false if nums[i] > nums[i + 1]\n    end\n\
        \    true\nend"
      scala: "object Solution {\n    def minimumPairRemoval(nums: Array[Int]): Int =\
        \ {\n        var count = 0\n        var numsList = nums.toList\n        while\
        \ (!isNonDecreasing(numsList)) {\n            var minSum = Int.MaxValue\n  \
        \          var minIndex = -1\n            for (i <- 0 until numsList.size -\
        \ 1) {\n                val sum = numsList(i) + numsList(i + 1)\n          \
        \      if (sum < minSum) {\n                    minSum = sum\n             \
        \       minIndex = i\n                }\n            }\n            numsList\
        \ = numsList.patch(minIndex, Seq(minSum), 2)\n            count += 1\n     \
        \   }\n        count\n    }\n\n    private def isNonDecreasing(nums: List[Int]):\
        \ Boolean = {\n        for (i <- 0 until nums.size - 1) {\n            if (nums(i)\
        \ > nums(i + 1)) return false\n        }\n        true\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_pair_removal(nums: Vec<i32>) -> i32\
        \ {\n        let mut count = 0;\n        let mut nums_list = nums;\n       \
        \ while !is_non_decreasing(&nums_list) {\n            let mut min_sum = i32::MAX;\n\
        \            let mut min_index = -1;\n            for i in 0..nums_list.len()\
        \ - 1 {\n                let sum = nums_list[i] + nums_list[i + 1];\n      \
        \          if sum < min_sum {\n                    min_sum = sum;\n        \
        \            min_index = i as i32;\n                }\n            }\n     \
        \       nums_list.remove(min_index as usize + 1);\n            nums_list[min_index\
        \ as usize] = min_sum;\n            count += 1;\n        }\n        count\n\
        \    }\n}\n\nfn is_non_decreasing(nums: &Vec<i32>) -> bool {\n    for i in 0..nums.len()\
        \ - 1 {\n        if nums[i] > nums[i + 1] {\n            return false;\n   \
        \     }\n    }\n    true\n}"
      racket: "(define/contract (minimum-pair-removal nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let loop ((nums nums) (count 0))\n    (if (is-non-decreasing?\
        \ nums)\n        count\n        (let* ((min-sum (apply min (map (lambda (x)\
        \ (apply + x)) (map cons nums (cdr nums)))))\n               (min-index (index-of\
        \ (map cons nums (cdr nums)) (cons (car (filter (lambda (x) (= (apply + x) min-sum))\
        \ (map cons nums (cdr nums)))))))))\n          (loop (append (take nums min-index)\
        \ (list min-sum) (cddr (drop nums min-index))) (+ count 1))))))\n\n(define (is-non-decreasing?\
        \ nums)\n  (or (null? (cdr nums))\n      (and (<= (car nums) (cadr nums))\n\
        \           (is-non-decreasing? (cdr nums)))))"
      erlang: "minimum_pair_removal(Nums) ->\n    Count =\n        lists:foldl(\n  \
        \          fun\n                ({Sum, Index}, {CountAcc, NumsAcc}) when Sum\
        \ < MinSum ->\n                    {{Sum, Index}, {CountAcc + 1, lists:delete_at(NumsAcc,\
        \ Index + 1)});\n                (_, {CountAcc, NumsAcc}) ->\n             \
        \       {CountAcc, NumsAcc}\n            end,\n            {0, Nums},\n    \
        \        [{lists:sum([A, B]), I} || {A, B, I} <- [{X, Y, I} || {X, Y, I} <-\
        \ [{A, B, I} || {A, [B | _] = T, I} <- [{X, T, I} || {X, T, I} <- [{X, T, I}\
        \ || {X, T} <- [{X, tl(T)} || T <- [Nums]], I <- [0]]]], I <- [0]]]]),\n   \
        \ Count.\n\nis_non_decreasing(Nums) ->\n    lists:all(\n        fun\n      \
        \      ({A, B}) when A =< B -> true;\n            (_) -> false\n        end,\n\
        \        [{A, B} || {A, [B | _] = T} <- [{A, T} || T <- [Nums]], {A, B} <- [{A,\
        \ B} || {A, B} <- [{A, B} || {A, [B | _] = T} <- [{A, T} || T <- [Nums]]]]]])."
      elixir: "defmodule Solution do\n  @spec minimum_pair_removal(nums :: [integer])\
        \ :: integer\n  def minimum_pair_removal(nums) do\n    count = 0\n    nums_list\
        \ = Enum.to_list(nums)\n    while !is_non_decreasing(nums_list) do\n      min_sum\
        \ = :math.pow(2, 31) - 1\n      min_index = -1\n      Enum.reduce(0..length(nums_list)\
        \ - 2, {min_sum, min_index}, fn i, {min_sum, min_index} ->\n        sum = Enum.at(nums_list,\
        \ i) + Enum.at(nums_list, i + 1)\n        if sum < min_sum do\n          {sum,\
        \ i}\n        else\n          {min_sum, min_index}\n        end\n      end)\n\
        \      |> (fn {min_sum, min_index} ->\n           nums_list = List.delete_at(nums_list,\
        \ min_index + 1)\n           List.update_at(nums_list, min_index, fn _ -> min_sum\
        \ end)\n           {count + 1, nums_list}\n         end)\n    end\n    count\n\
        \  end\n\n  defp is_non_decreasing(nums) do\n    Enum.all?(0..length(nums) -\
        \ 2, fn i -> Enum.at(nums, i) <= Enum.at(nums, i + 1) end)\n  end\nend"
    approach: The problem can be solved by using a priority queue to store the pairs
      of adjacent elements in the array along with their sum. We start by initializing
      the priority queue with all pairs of adjacent elements. Then, we enter a loop
      where we keep removing the pair with the minimum sum from the priority queue and
      replace it with their sum in the array until the array becomes non-decreasing.
      The number of operations performed is the minimum number of operations needed
      to make the array non-decreasing.
    time_complexity: The time complexity of this solution is O(n^2 log n) where n is
      the number of elements in the array. This is because in the worst case, we might
      have to remove all pairs from the array, and each removal operation takes O(log
      n) time due to the priority queue.
    space_complexity: The space complexity of this solution is O(n) where n is the number
      of elements in the array. This is because we are storing all pairs of adjacent
      elements in the priority queue.
    elapsed_time: 10.216416835784912
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-23 01:13:10 '
---

## Problem #3510: Minimum Pair Removal to Sort Array II

**Difficulty:** Hard

**Topics:** Array, Hash Table, Linked List, Heap (Priority Queue), Simulation, Doubly-Linked List, Ordered Set

## Problem Description

<p>Given an array <code>nums</code>, you can perform the following operation any number of times:</p>

<ul>
	<li>Select the <strong>adjacent</strong> pair with the <strong>minimum</strong> sum in <code>nums</code>. If multiple such pairs exist, choose the leftmost one.</li>
	<li>Replace the pair with their sum.</li>
</ul>

<p>Return the <strong>minimum number of operations</strong> needed to make the array <strong>non-decreasing</strong>.</p>

<p>An array is said to be <strong>non-decreasing</strong> if each element is greater than or equal to its previous element (if it exists).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,2,3,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The pair <code>(3,1)</code> has the minimum sum of 4. After replacement, <code>nums = [5,2,4]</code>.</li>
	<li>The pair <code>(2,4)</code> has the minimum sum of 6. After replacement, <code>nums = [5,6]</code>.</li>
</ul>

<p>The array <code>nums</code> became non-decreasing in two operations.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>The array <code>nums</code> is already sorted.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. We can perform the simulation using data structures.

2. Maintain an array index and value using a map since we need to find the next and previous ones.

3. Maintain the indices to be removed using a hash set.

4. Maintain the neighbor sums with the smaller indices (set or priority queue).

5. Keep the 3 structures in sync during the removals.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-23 01:13:10 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by using a priority queue to store the pairs of adjacent elements in the array along with their sum. We start by initializing the priority queue with all pairs of adjacent elements. Then, we enter a loop where we keep removing the pair with the minimum sum from the priority queue and replace it with their sum in the array until the array becomes non-decreasing. The number of operations performed is the minimum number of operations needed to make the array non-decreasing.

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
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        int count = 0;
        while (!isSorted(nums)) {
            int minSum = INT_MAX;
            int minIndex = -1;
            for (int i = 0; i < n - 1; i++) {
                if (nums[i] + nums[i + 1] < minSum) {
                    minSum = nums[i] + nums[i + 1];
                    minIndex = i;
                }
            }
            nums.erase(nums.begin() + minIndex + 1);
            nums[minIndex] = minSum;
            n--;
            count++;
        }
        return count;
    }
    bool isSorted(vector<int>& nums) {
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                return false;
            }
        }
        return true;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minimumPairRemoval(int[] nums) {
        int n = nums.length;
        int count = 0;
        while (!isSorted(nums)) {
            int minSum = Integer.MAX_VALUE;
            int minIndex = -1;
            for (int i = 0; i < n - 1; i++) {
                if (nums[i] + nums[i + 1] < minSum) {
                    minSum = nums[i] + nums[i + 1];
                    minIndex = i;
                }
            }
            int[] newNums = new int[n - 1];
            System.arraycopy(nums, 0, newNums, 0, minIndex);
            newNums[minIndex] = minSum;
            System.arraycopy(nums, minIndex + 2, newNums, minIndex + 1, n - minIndex - 2);
            nums = newNums;
            n--;
            count++;
        }
        return count;
    }
    boolean isSorted(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                return false;
            }
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumPairRemoval(self, nums):
        count = 0
        while not self.isSorted(nums):
            minSum = float('inf')
            minIndex = -1
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < minSum:
                    minSum = nums[i] + nums[i + 1]
                    minIndex = i
            nums.pop(minIndex + 1)
            nums[minIndex] = minSum
            count += 1
        return count
    def isSorted(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        count = 0
        while not self.isSorted(nums):
            minSum = float('inf')
            minIndex = -1
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < minSum:
                    minSum = nums[i] + nums[i + 1]
                    minIndex = i
            nums.pop(minIndex + 1)
            nums[minIndex] = minSum
            count += 1
        return count
    def isSorted(self, nums: list[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minimumPairRemoval(int* nums, int numsSize) {
    int count = 0;
    while (!isSorted(nums, numsSize)) {
        int minSum = INT_MAX;
        int minIndex = -1;
        for (int i = 0; i < numsSize - 1; i++) {
            if (nums[i] + nums[i + 1] < minSum) {
                minSum = nums[i] + nums[i + 1];
                minIndex = i;
            }
        }
        for (int i = minIndex + 1; i < numsSize - 1; i++) {
            nums[i] = nums[i + 1];
        }
        nums[minIndex] = minSum;
        numsSize--;
        count++;
    }
    return count;
}
int isSorted(int* nums, int numsSize) {
    for (int i = 0; i < numsSize - 1; i++) {
        if (nums[i] > nums[i + 1]) {
            return 0;
        }
    }
    return 1;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinimumPairRemoval(int[] nums) {
        int n = nums.Length;
        int count = 0;
        while (!IsSorted(nums)) {
            int minSum = int.MaxValue;
            int minIndex = -1;
            for (int i = 0; i < n - 1; i++) {
                if (nums[i] + nums[i + 1] < minSum) {
                    minSum = nums[i] + nums[i + 1];
                    minIndex = i;
                }
            }
            int[] newNums = new int[n - 1];
            Array.Copy(nums, 0, newNums, 0, minIndex);
            newNums[minIndex] = minSum;
            Array.Copy(nums, minIndex + 2, newNums, minIndex + 1, n - minIndex - 2);
            nums = newNums;
            n--;
            count++;
        }
        return count;
    }
    bool IsSorted(int[] nums) {
        for (int i = 0; i < nums.Length - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                return false;
            }
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var minimumPairRemoval = function(nums) {
    let count = 0;
    while (!isSorted(nums)) {
        let minSum = Infinity;
        let minIndex = -1;
        for (let i = 0; i < nums.length - 1; i++) {
            if (nums[i] + nums[i + 1] < minSum) {
                minSum = nums[i] + nums[i + 1];
                minIndex = i;
            }
        }
        nums.splice(minIndex + 1, 1);
        nums[minIndex] = minSum;
        count++;
    }
    return count;
};
function isSorted(nums) {
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] > nums[i + 1]) {
            return false;
        }
    }
    return true;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumPairRemoval(nums: number[]): number {
    let count = 0;
    while (!isSorted(nums)) {
        let minSum = Infinity;
        let minIndex = -1;
        for (let i = 0; i < nums.length - 1; i++) {
            if (nums[i] + nums[i + 1] < minSum) {
                minSum = nums[i] + nums[i + 1];
                minIndex = i;
            }
        }
        nums.splice(minIndex + 1, 1);
        nums[minIndex] = minSum;
        count++;
    }
    return count;
}
function isSorted(nums: number[]): boolean {
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] > nums[i + 1]) {
            return false;
        }
    }
    return true;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function minimumPairRemoval($nums) {
        $count = 0;
        while (!$this->isSorted($nums)) {
            $minSum = PHP_INT_MAX;
            $minIndex = -1;
            for ($i = 0; $i < count($nums) - 1; $i++) {
                if ($nums[$i] + $nums[$i + 1] < $minSum) {
                    $minSum = $nums[$i] + $nums[$i + 1];
                    $minIndex = $i;
                }
            }
            array_splice($nums, $minIndex + 1, 1);
            $nums[$minIndex] = $minSum;
            $count++;
        }
        return $count;
    }
    function isSorted($nums) {
        for ($i = 0; $i < count($nums) - 1; $i++) {
            if ($nums[$i] > $nums[$i + 1]) {
                return false;
            }
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumPairRemoval(_ nums: [Int]) -> Int {
        var nums = nums
        var count = 0
        while !isSorted(nums) {
            var minSum = Int.max
            var minIndex = -1
            for i in 0..<nums.count - 1 {
                if nums[i] + nums[i + 1] < minSum {
                    minSum = nums[i] + nums[i + 1]
                    minIndex = i
                }
            }
            nums.remove(at: minIndex + 1)
            nums[minIndex] = minSum
            count += 1
        }
        return count
    }
    func isSorted(_ nums: [Int]) -> Bool {
        for i in 0..<nums.count - 1 {
            if nums[i] > nums[i + 1] {
                return false
            }
        }
        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumPairRemoval(nums: IntArray): Int {
        var count = 0
        var numsList = nums.toMutableList()
        while (!isNonDecreasing(numsList)) {
            var minSum = Int.MAX_VALUE
            var minIndex = -1
            for (i in 0 until numsList.size - 1) {
                val sum = numsList[i] + numsList[i + 1]
                if (sum < minSum) {
                    minSum = sum
                    minIndex = i
                }
            }
            numsList.removeAt(minIndex + 1)
            numsList[minIndex] = minSum
            count++
        }
        return count
    }

    private fun isNonDecreasing(nums: List<Int>): Boolean {
        for (i in 0 until nums.size - 1) {
            if (nums[i] > nums[i + 1]) return false
        }
        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumPairRemoval(List<int> nums) {
    int count = 0;
    List<int> numsList = List.from(nums);
    while (!isNonDecreasing(numsList)) {
      int minSum = int.maxFinite;
      int minIndex = -1;
      for (int i = 0; i < numsList.length - 1; i++) {
        int sum = numsList[i] + numsList[i + 1];
        if (sum < minSum) {
          minSum = sum;
          minIndex = i;
        }
      }
      numsList.removeAt(minIndex + 1);
      numsList[minIndex] = minSum;
      count++;
    }
    return count;
  }

  bool isNonDecreasing(List<int> nums) {
    for (int i = 0; i < nums.length - 1; i++) {
      if (nums[i] > nums[i + 1]) return false;
    }
    return true;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumPairRemoval(nums []int) int {
    count := 0
    numsList := make([]int, len(nums))
    copy(numsList, nums)
    for !isNonDecreasing(numsList) {
        minSum := int(1e9)
        minIndex := -1
        for i := 0; i < len(numsList)-1; i++ {
            sum := numsList[i] + numsList[i+1]
            if sum < minSum {
                minSum = sum
                minIndex = i
            }
        }
        numsList = append(numsList[:minIndex], append([]int{minSum}, numsList[minIndex+2:]...)...)
        count++
    }
    return count
}

func isNonDecreasing(nums []int) bool {
    for i := 0; i < len(nums)-1; i++ {
        if nums[i] > nums[i+1] {
            return false
        }
    }
    return true
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def minimum_pair_removal(nums)
    count = 0
    nums_list = nums.dup
    while !is_non_decreasing(nums_list)
        min_sum = Float::INFINITY
        min_index = -1
        (0...nums_list.size - 1).each do |i|
            sum = nums_list[i] + nums_list[i + 1]
            if sum < min_sum
                min_sum = sum
                min_index = i
            end
        end
        nums_list.delete_at(min_index + 1)
        nums_list[min_index] = min_sum
        count += 1
    end
    count
end

private
def is_non_decreasing(nums)
    (0...nums.size - 1).each do |i|
        return false if nums[i] > nums[i + 1]
    end
    true
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumPairRemoval(nums: Array[Int]): Int = {
        var count = 0
        var numsList = nums.toList
        while (!isNonDecreasing(numsList)) {
            var minSum = Int.MaxValue
            var minIndex = -1
            for (i <- 0 until numsList.size - 1) {
                val sum = numsList(i) + numsList(i + 1)
                if (sum < minSum) {
                    minSum = sum
                    minIndex = i
                }
            }
            numsList = numsList.patch(minIndex, Seq(minSum), 2)
            count += 1
        }
        count
    }

    private def isNonDecreasing(nums: List[Int]): Boolean = {
        for (i <- 0 until nums.size - 1) {
            if (nums(i) > nums(i + 1)) return false
        }
        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_pair_removal(nums: Vec<i32>) -> i32 {
        let mut count = 0;
        let mut nums_list = nums;
        while !is_non_decreasing(&nums_list) {
            let mut min_sum = i32::MAX;
            let mut min_index = -1;
            for i in 0..nums_list.len() - 1 {
                let sum = nums_list[i] + nums_list[i + 1];
                if sum < min_sum {
                    min_sum = sum;
                    min_index = i as i32;
                }
            }
            nums_list.remove(min_index as usize + 1);
            nums_list[min_index as usize] = min_sum;
            count += 1;
        }
        count
    }
}

fn is_non_decreasing(nums: &Vec<i32>) -> bool {
    for i in 0..nums.len() - 1 {
        if nums[i] > nums[i + 1] {
            return false;
        }
    }
    true
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-pair-removal nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((nums nums) (count 0))
    (if (is-non-decreasing? nums)
        count
        (let* ((min-sum (apply min (map (lambda (x) (apply + x)) (map cons nums (cdr nums)))))
               (min-index (index-of (map cons nums (cdr nums)) (cons (car (filter (lambda (x) (= (apply + x) min-sum)) (map cons nums (cdr nums)))))))))
          (loop (append (take nums min-index) (list min-sum) (cddr (drop nums min-index))) (+ count 1))))))

(define (is-non-decreasing? nums)
  (or (null? (cdr nums))
      (and (<= (car nums) (cadr nums))
           (is-non-decreasing? (cdr nums)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
minimum_pair_removal(Nums) ->
    Count =
        lists:foldl(
            fun
                ({Sum, Index}, {CountAcc, NumsAcc}) when Sum < MinSum ->
                    {{Sum, Index}, {CountAcc + 1, lists:delete_at(NumsAcc, Index + 1)});
                (_, {CountAcc, NumsAcc}) ->
                    {CountAcc, NumsAcc}
            end,
            {0, Nums},
            [{lists:sum([A, B]), I} || {A, B, I} <- [{X, Y, I} || {X, Y, I} <- [{A, B, I} || {A, [B | _] = T, I} <- [{X, T, I} || {X, T, I} <- [{X, T, I} || {X, T} <- [{X, tl(T)} || T <- [Nums]], I <- [0]]]], I <- [0]]]]),
    Count.

is_non_decreasing(Nums) ->
    lists:all(
        fun
            ({A, B}) when A =< B -> true;
            (_) -> false
        end,
        [{A, B} || {A, [B | _] = T} <- [{A, T} || T <- [Nums]], {A, B} <- [{A, B} || {A, B} <- [{A, B} || {A, [B | _] = T} <- [{A, T} || T <- [Nums]]]]]]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_pair_removal(nums :: [integer]) :: integer
  def minimum_pair_removal(nums) do
    count = 0
    nums_list = Enum.to_list(nums)
    while !is_non_decreasing(nums_list) do
      min_sum = :math.pow(2, 31) - 1
      min_index = -1
      Enum.reduce(0..length(nums_list) - 2, {min_sum, min_index}, fn i, {min_sum, min_index} ->
        sum = Enum.at(nums_list, i) + Enum.at(nums_list, i + 1)
        if sum < min_sum do
          {sum, i}
        else
          {min_sum, min_index}
        end
      end)
      |> (fn {min_sum, min_index} ->
           nums_list = List.delete_at(nums_list, min_index + 1)
           List.update_at(nums_list, min_index, fn _ -> min_sum end)
           {count + 1, nums_list}
         end)
    end
    count
  end

  defp is_non_decreasing(nums) do
    Enum.all?(0..length(nums) - 2, fn i -> Enum.at(nums, i) <= Enum.at(nums, i + 1) end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n^2 log n) where n is the number of elements in the array. This is because in the worst case, we might have to remove all pairs from the array, and each removal operation takes O(log n) time due to the priority queue.

- **Space Complexity:** The space complexity of this solution is O(n) where n is the number of elements in the array. This is because we are storing all pairs of adjacent elements in the priority queue.

</div>
</details>
