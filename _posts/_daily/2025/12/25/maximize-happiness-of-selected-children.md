---
layout: post
title: "Maximize Happiness of Selected Children"
date: 2025-12-25 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Greedy", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximize-happiness-of-selected-children/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n\nclass Solution {\npublic:\n \
        \   long long maximumHappinessSum(std::vector<int>& happiness, int k) {\n  \
        \      std::sort(happiness.rbegin(), happiness.rend());\n\n        long long\
        \ totalHappinessSum = 0;\n        long long decrements = 0;\n\n        for (int\
        \ i = 0; i < k; ++i) {\n            long long currentHappiness = happiness[i];\n\
        \n            long long selectedHappiness = std::max(0LL, currentHappiness -\
        \ decrements);\n            totalHappinessSum += selectedHappiness;\n      \
        \      decrements++;\n        }\n\n        return totalHappinessSum;\n    }\n\
        };"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public long maximumHappinessSum(int[]\
        \ happiness, int k) {\n        Arrays.sort(happiness);\n\n        long totalHappinessSum\
        \ = 0;\n        long decrements = 0;\n\n        for (int i = 0; i < k; i++)\
        \ {\n            int currentHappiness = happiness[happiness.length - 1 - i];\n\
        \n            long selectedHappiness = Math.max(0L, currentHappiness - decrements);\n\
        \            totalHappinessSum += selectedHappiness;\n            decrements++;\n\
        \        }\n\n        return totalHappinessSum;\n    }\n}"
      python: "class Solution:\n    def maximumHappinessSum(self, happiness: list[int],\
        \ k: int) -> int:\n        happiness.sort(reverse=True)\n\n        total_happiness_sum\
        \ = 0\n        decrements = 0\n\n        for i in range(k):\n            current_happiness\
        \ = happiness[i]\n\n            selected_happiness = max(0, current_happiness\
        \ - decrements)\n            total_happiness_sum += selected_happiness\n   \
        \         decrements += 1\n\n        return total_happiness_sum"
      python3: "class Solution:\n    def maximumHappinessSum(self, happiness: list[int],\
        \ k: int) -> int:\n        happiness.sort(reverse=True)\n\n        total_happiness_sum\
        \ = 0\n        decrements = 0\n\n        for i in range(k):\n            current_happiness\
        \ = happiness[i]\n\n            selected_happiness = max(0, current_happiness\
        \ - decrements)\n            total_happiness_sum += selected_happiness\n   \
        \         decrements += 1\n\n        return total_happiness_sum"
      c: "#include <stdlib.h>\n\nint compare(const void *a, const void *b) {\n    return\
        \ (*(int*)b - *(int*)a);\n}\n\nlong long maximumHappinessSum(int* happiness,\
        \ int happinessSize, int k) {\n    qsort(happiness, happinessSize, sizeof(int),\
        \ compare);\n\n    long long totalHappinessSum = 0;\n    long long decrements\
        \ = 0;\n\n    for (int i = 0; i < k; ++i) {\n        long long currentHappiness\
        \ = happiness[i];\n\n        long long selectedHappiness = currentHappiness\
        \ - decrements;\n        if (selectedHappiness < 0) {\n            selectedHappiness\
        \ = 0;\n        }\n        totalHappinessSum += selectedHappiness;\n       \
        \ decrements++;\n    }\n\n    return totalHappinessSum;\n}"
      csharp: "using System;\nusing System.Linq;\n\npublic class Solution {\n    public\
        \ long MaximumHappinessSum(int[] happiness, int k) {\n        Array.Sort(happiness);\n\
        \n        long totalHappinessSum = 0;\n        long decrements = 0;\n\n    \
        \    for (int i = 0; i < k; i++) {\n            int currentHappiness = happiness[happiness.Length\
        \ - 1 - i];\n\n            long selectedHappiness = Math.Max(0L, currentHappiness\
        \ - decrements);\n            totalHappinessSum += selectedHappiness;\n    \
        \        decrements++;\n        }\n\n        return totalHappinessSum;\n   \
        \ }\n}"
      javascript: "/**\n * @param {number[]} happiness\n * @param {number} k\n * @return\
        \ {number}\n */\nvar maximumHappinessSum = function(happiness, k) {\n    happiness.sort((a,\
        \ b) => b - a);\n\n    let totalHappinessSum = 0;\n    let decrements = 0;\n\
        \n    for (let i = 0; i < k; i++) {\n        let currentHappiness = happiness[i];\n\
        \n        let selectedHappiness = Math.max(0, currentHappiness - decrements);\n\
        \        totalHappinessSum += selectedHappiness;\n        decrements++;\n  \
        \  }\n\n    return totalHappinessSum;\n};"
      typescript: "function maximumHappinessSum(happiness: number[], k: number): number\
        \ {\n    happiness.sort((a, b) => b - a);\n\n    let totalHappinessSum: number\
        \ = 0;\n    let decrements: number = 0;\n\n    for (let i = 0; i < k; i++) {\n\
        \        let currentHappiness: number = happiness[i];\n\n        let selectedHappiness:\
        \ number = Math.max(0, currentHappiness - decrements);\n        totalHappinessSum\
        \ += selectedHappiness;\n        decrements++;\n    }\n\n    return totalHappinessSum;\n\
        };"
      php: "<?php\n\nclass Solution {\n    /**\n     * @param int[] $happiness\n   \
        \  * @param int $k\n     * @return int\n     */\n    function maximumHappinessSum($happiness,\
        \ $k) {\n        rsort($happiness);\n\n        $totalHappinessSum = 0;\n   \
        \     $decrements = 0;\n\n        for ($i = 0; $i < $k; $i++) {\n          \
        \  $currentHappiness = $happiness[$i];\n\n            $selectedHappiness = max(0,\
        \ $currentHappiness - $decrements);\n            $totalHappinessSum += $selectedHappiness;\n\
        \            $decrements++;\n        }\n\n        return $totalHappinessSum;\n\
        \    }\n}"
      swift: "class Solution {\n    func maximumHappinessSum(_ happiness: [Int], _ k:\
        \ Int) -> Int {\n        var sortedHappiness = happiness.sorted(by: >)\n\n \
        \       var totalHappinessSum: Int = 0\n        var decrements: Int = 0\n\n\
        \        for i in 0..<k {\n            let currentHappiness = sortedHappiness[i]\n\
        \n            let selectedHappiness = max(0, currentHappiness - decrements)\n\
        \            totalHappinessSum += selectedHappiness\n            decrements\
        \ += 1\n        }\n\n        return totalHappinessSum\n    }\n}"
      kotlin: "import kotlin.math.max\n\nclass Solution {\n    fun maximumHappinessSum(happiness:\
        \ IntArray, k: Int): Long {\n        happiness.sortDescending()\n\n        var\
        \ totalHappinessSum: Long = 0\n        var decrements: Long = 0\n\n        for\
        \ (i in 0 until k) {\n            val currentHappiness = happiness[i].toLong()\n\
        \n            val selectedHappiness = max(0L, currentHappiness - decrements)\n\
        \            totalHappinessSum += selectedHappiness\n            decrements++\n\
        \        }\n\n        return totalHappinessSum\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int maximumHappinessSum(List<int>\
        \ happiness, int k) {\n    happiness.sort((a, b) => b.compareTo(a));\n\n   \
        \ int totalHappinessSum = 0;\n    int decrements = 0;\n\n    for (int i = 0;\
        \ i < k; i++) {\n      int currentHappiness = happiness[i];\n\n      int selectedHappiness\
        \ = max(0, currentHappiness - decrements);\n      totalHappinessSum += selectedHappiness;\n\
        \      decrements++;\n    }\n\n    return totalHappinessSum;\n  }\n}"
      go: "import (\n\t\"sort\"\n)\n\nfunc maximumHappinessSum(happiness []int, k int)\
        \ int64 {\n    sort.Slice(happiness, func(i, j int) bool {\n        return happiness[i]\
        \ > happiness[j]\n    })\n\n    var totalHappinessSum int64 = 0\n    var decrements\
        \ int64 = 0\n\n    for i := 0; i < k; i++ {\n        currentHappiness := int64(happiness[i])\n\
        \n        selectedHappiness := currentHappiness - decrements\n        if selectedHappiness\
        \ < 0 {\n            selectedHappiness = 0\n        }\n        totalHappinessSum\
        \ += selectedHappiness\n        decrements++\n    }\n\n    return totalHappinessSum\n\
        }"
      ruby: "# @param {Integer[]} happiness\n# @param {Integer} k\n# @return {Integer}\n\
        def maximum_happiness_sum(happiness, k)\n    happiness.sort! { |a, b| b <=>\
        \ a }\n\n    total_happiness_sum = 0\n    decrements = 0\n\n    (0...k).each\
        \ do |i|\n        current_happiness = happiness[i]\n\n        selected_happiness\
        \ = [0, current_happiness - decrements].max\n        total_happiness_sum +=\
        \ selected_happiness\n        decrements += 1\n    end\n\n    total_happiness_sum\n\
        end"
      scala: "import scala.math.max\n\nobject Solution {\n    def maximumHappinessSum(happiness:\
        \ Array[Int], k: Int): Long = {\n        val sortedHappiness = happiness.sorted.reverse\n\
        \n        var totalHappinessSum: Long = 0\n        var decrements: Long = 0\n\
        \n        for (i <- 0 until k) {\n            val currentHappiness = sortedHappiness(i).toLong\n\
        \n            val selectedHappiness = max(0L, currentHappiness - decrements)\n\
        \            totalHappinessSum += selectedHappiness\n            decrements\
        \ += 1\n        }\n\n        totalHappinessSum\n    }\n}"
      rust: "impl Solution {\n    pub fn maximum_happiness_sum(mut happiness: Vec<i32>,\
        \ k: i32) -> i64 {\n        happiness.sort_by(|a, b| b.cmp(a));\n\n        let\
        \ mut total_happiness_sum: i64 = 0;\n        let mut decrements: i64 = 0;\n\n\
        \        for i in 0..k as usize {\n            let current_happiness: i64 =\
        \ happiness[i] as i64;\n\n            let selected_happiness = (current_happiness\
        \ - decrements).max(0);\n            total_happiness_sum += selected_happiness;\n\
        \            decrements += 1;\n        }\n\n        total_happiness_sum\n  \
        \  }\n}"
      racket: "#lang racket\n\n(define/contract (maximum-happiness-sum happiness k)\n\
        \  (-> (listof exact-integer?) exact-integer? exact-integer?)\n  (let* ([sorted-happiness\
        \ (sort happiness >)]\n         [total-happiness-sum 0]\n         [decrements\
        \ 0])\n    (for ([i (in-range k)])\n      (let* ([current-happiness (list-ref\
        \ sorted-happiness i)]\n             [selected-happiness (max 0 (- current-happiness\
        \ decrements))])\n        (set! total-happiness-sum (+ total-happiness-sum selected-happiness))\n\
        \        (set! decrements (+ decrements 1))))\n    total-happiness-sum))"
      erlang: "-module(solution).\n-export([maximum_happiness_sum/2]).\n\nmaximum_happiness_sum(Happiness,\
        \ K) ->\n    SortedHappiness = lists:sort(fun(A, B) -> A >= B end, Happiness),\n\
        \n    maximum_happiness_sum_loop(SortedHappiness, K, 0, 0).\n\nmaximum_happiness_sum_loop(_SortedHappiness,\
        \ 0, AccSum, _Decrements) ->\n    AccSum;\nmaximum_happiness_sum_loop([H|T],\
        \ K, AccSum, Decrements) ->\n    SelectedHappiness = max(0, H - Decrements),\n\
        \    maximum_happiness_sum_loop(T, K - 1, AccSum + SelectedHappiness, Decrements\
        \ + 1)."
      elixir: "defmodule Solution do\n  @spec maximum_happiness_sum(happiness :: [integer],\
        \ k :: integer) :: integer\n  def maximum_happiness_sum(happiness, k) do\n \
        \   sorted_happiness = Enum.sort(happiness, :desc)\n\n    do_sum(sorted_happiness,\
        \ k, 0, 0)\n  end\n\n  defp do_sum(_sorted_happiness, 0, acc_sum, _decrements),\
        \ do: acc_sum\n  defp do_sum([current_happiness | rest], k, acc_sum, decrements)\
        \ do\n    selected_happiness = max(0, current_happiness - decrements)\n    do_sum(rest,\
        \ k - 1, acc_sum + selected_happiness, decrements + 1)\n  end\n\n  defp max(a,\
        \ b) when a > b, do: a\n  defp max(_a, b), do: b\nend"
    approach: The core idea is to greedily select children with the highest happiness
      values. Since the happiness of all unselected children decreases by 1 in each
      turn, it is always optimal to pick the child that currently offers the most happiness.
      By picking the child with the highest happiness, we 'lock in' its value before
      it can be reduced further. All other unselected children will suffer the same
      decrement regardless of which child we pick, so we might as well secure the largest
      possible value first.
    time_complexity: The time complexity is dominated by sorting the `happiness` array,
      which takes O(N log N) time, where N is the number of children. After sorting,
      we iterate `k` times, which takes O(k) time. Since `k <= N`, the overall time
      complexity is O(N log N).
    space_complexity: The space complexity depends on the sorting algorithm used. If
      an in-place sort is used (like C++ `std::sort` or Java `Arrays.sort` for primitives),
      the auxiliary space complexity is O(log N) or O(1). If a sort that requires auxiliary
      space is used (like Python's `list.sort()` or `sorted()`, or Java `Arrays.sort`
      for objects), the space complexity is O(N). Given that we might modify the input
      array or use a new sorted array, O(N) is a safe upper bound for auxiliary space.
    elapsed_time: 37.08306169509888
    model: gemini-2.5-flash
    generated_at: '2025-12-25 01:07:40 '
  - solutions:
      cpp: "class Solution {\npublic:\n    long long maximumHappinessSum(vector<int>&\
        \ happiness, int k) {\n        sort(happiness.rbegin(), happiness.rend());\n\
        \        long long sum = 0;\n        for (int i = 0; i < k; i++) {\n       \
        \     sum += max(0, happiness[i] - i);\n        }\n        return sum;\n   \
        \ }\n};"
      java: "class Solution {\n    public long maximumHappinessSum(int[] happiness,\
        \ int k) {\n        Arrays.sort(happiness);\n        long sum = 0;\n       \
        \ for (int i = happiness.length - 1; i >= happiness.length - k; i--) {\n   \
        \         sum += Math.max(0, happiness[i] - (happiness.length - 1 - i));\n \
        \       }\n        return sum;\n    }\n}"
      python: "class Solution:\n    def maximumHappinessSum(self, happiness: list[int],\
        \ k: int) -> int:\n        happiness.sort(reverse=True)\n        return sum(max(0,\
        \ x - i) for i, x in enumerate(happiness[:k]))"
      python3: "class Solution:\n    def maximumHappinessSum(self, happiness: list[int],\
        \ k: int) -> int:\n        happiness.sort(reverse=True)\n        return sum(max(0,\
        \ x - i) for i, x in enumerate(happiness[:k]))"
      c: "long long maximumHappinessSum(int* happiness, int happinessSize, int k) {\n\
        \    qsort(happiness, happinessSize, sizeof(int), compare);\n    long long sum\
        \ = 0;\n    for (int i = happinessSize - 1; i >= happinessSize - k; i--) {\n\
        \        sum += (happiness[i] - (happinessSize - 1 - i) > 0) ? happiness[i]\
        \ - (happinessSize - 1 - i) : 0;\n    }\n    return sum;\n}\nint compare(const\
        \ void* a, const void* b) {\n    return (*(int*)b - *(int*)a);\n}"
      csharp: "public class Solution {\n    public long MaximumHappinessSum(int[] happiness,\
        \ int k) {\n        Array.Sort(happiness);\n        Array.Reverse(happiness);\n\
        \        long sum = 0;\n        for (int i = 0; i < k; i++) {\n            sum\
        \ += Math.Max(0, happiness[i] - i);\n        }\n        return sum;\n    }\n\
        }"
      javascript: "var maximumHappinessSum = function(happiness, k) {\n    happiness.sort((a,\
        \ b) => b - a);\n    let sum = 0;\n    for (let i = 0; i < k; i++) {\n     \
        \   sum += Math.max(0, happiness[i] - i);\n    }\n    return sum;\n};"
      typescript: "function maximumHappinessSum(happiness: number[], k: number): number\
        \ {\n    happiness.sort((a, b) => b - a);\n    let sum = 0;\n    for (let i\
        \ = 0; i < k; i++) {\n        sum += Math.max(0, happiness[i] - i);\n    }\n\
        \    return sum;\n}"
      php: "$happiness = $happiness;\nrsort($happiness);\n$sum = 0;\nfor ($i = 0; $i\
        \ < $k; $i++) {\n    $sum += max(0, $happiness[$i] - $i);\n}\necho $sum;"
      swift: "class Solution {\n    func maximumHappinessSum(_ happiness: [Int], _ k:\
        \ Int) -> Int {\n        let sortedHappiness = happiness.sorted { $0 > $1 }\n\
        \        return sortedHappiness.prefix(k).enumerated().map { max(0, $0.1 - $0.0)\
        \ }.reduce(0, +)\n    }\n}"
      kotlin: "class Solution {\n    fun maximumHappinessSum(happiness: IntArray, k:\
        \ Int): Long {\n        happiness.sortDescending()\n        return happiness.take(k).mapIndexed\
        \ { index, i -> maxOf(0, i - index) }.sumOf { it.toLong() }\n    }\n}"
      dart: "class Solution {\n    int maximumHappinessSum(List<int> happiness, int\
        \ k) {\n        happiness.sort((a, b) => b.compareTo(a));\n        int sum =\
        \ 0;\n        for (int i = 0; i < k; i++) {\n            sum += max(0, happiness[i]\
        \ - i);\n        }\n        return sum;\n    }\n}"
      go: "package main\nimport (\n    \"sort\"\n)\nfunc maximumHappinessSum(happiness\
        \ []int, k int) int64 {\n    sort.Sort(sort.Reverse(sort.IntSlice(happiness)))\n\
        \    sum := int64(0)\n    for i := 0; i < k; i++ {\n        if happiness[i]-i\
        \ > 0 {\n            sum += int64(happiness[i] - i)\n        }\n    }\n    return\
        \ sum\n}"
      ruby: "def maximum_happiness_sum(happiness, k)\n    happiness.sort!.reverse!\n\
        \    sum = 0\n    k.times do |i|\n        sum += [happiness[i] - i, 0].max\n\
        \    end\n    sum\nend"
      scala: "object Solution {\n    def maximumHappinessSum(happiness: Array[Int],\
        \ k: Int): Long = {\n        val sortedHappiness = happiness.sorted(Ordering.Int.reverse)\n\
        \        sortedHappiness.take(k).zipWithIndex.map { case (x, i) => math.max(0,\
        \ x - i) }.sum\n    }\n}"
      rust: "struct Solution;\nimpl Solution {\n    pub fn maximum_happiness_sum(mut\
        \ happiness: Vec<i32>, k: i32) -> i64 {\n        happiness.sort_unstable_by(|a,\
        \ b| b.cmp(a));\n        let mut sum = 0;\n        for i in 0..k {\n       \
        \     sum += happiness[i as usize].max(0) as i64 - i as i64;\n        }\n  \
        \      sum\n    }\n}"
      racket: "(define (maximum-happiness-sum happiness k)\n    (let ((sorted-happiness\
        \ (sort happiness >)))\n        (let loop ((i 0) (sum 0))\n            (if (=\
        \ i k)\n                sum\n                (loop (+ i 1) (+ sum (max 0 (-\
        \ (list-ref sorted-happiness i) i))))))))"
      erlang: "-module(solution).\n-export([maximum_happiness_sum/2]).\nmaximum_happiness_sum(Happiness,\
        \ K) ->\n    lists:sum(lists:map(fun({X, I}) -> max(0, X - I) end, lists:zip(lists:reverse(lists:sort(Happiness)),\
        \ lists:seq(0, K - 1))))."
      elixir: "defmodule Solution do\n    def maximum_happiness_sum(happiness, k) do\n\
        \        happiness\n        |> Enum.sort(&(&1 >= &2))\n        |> Enum.take(k)\n\
        \        |> Enum.with_index()\n        |> Enum.map(fn {x, i} -> max(0, x - i)\n\
        \        |> Enum.sum()\n    end\nend"
    approach: The problem can be solved by using a greedy approach. We first sort the
      happiness array in descending order. Then, we iterate over the sorted array and
      add the happiness value of each child to the total sum. However, since the happiness
      value of all unselected children decreases by 1 in each turn, we need to subtract
      (i - 1) from the happiness value of the i-th child. If the resulting value is
      negative, we add 0 to the total sum instead. This approach ensures that we maximize
      the sum of the happiness values of the selected children. The key intuition behind
      this approach is that we should always select the child with the highest happiness
      value first, as this will result in the maximum possible sum of happiness values.
    time_complexity: The time complexity of this solution is O(n log n) due to the sorting
      operation, where n is the number of children. The subsequent for loop has a time
      complexity of O(k), where k is the number of children to be selected. However,
      since k is less than or equal to n, the overall time complexity remains O(n log
      n).
    space_complexity: The space complexity of this solution is O(n) for storing the
      sorted happiness array. In the worst-case scenario, the space complexity can be
      O(n) if we need to store all the happiness values in the sorted array.
    elapsed_time: 4.6064770221710205
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-25 01:07:45 '
---

## Problem #3075: Maximize Happiness of Selected Children

**Difficulty:** Medium

**Topics:** Array, Greedy, Sorting

## Problem Description

<p>You are given an array <code>happiness</code> of length <code>n</code>, and a <strong>positive</strong> integer <code>k</code>.</p>

<p>There are <code>n</code> children standing in a queue, where the <code>i<sup>th</sup></code> child has <strong>happiness value</strong> <code>happiness[i]</code>. You want to select <code>k</code> children from these <code>n</code> children in <code>k</code> turns.</p>

<p>In each turn, when you select a child, the <strong>happiness value</strong> of all the children that have <strong>not</strong> been selected till now decreases by <code>1</code>. Note that the happiness value <strong>cannot</strong> become negative and gets decremented <strong>only</strong> if it is positive.</p>

<p>Return <em>the <strong>maximum</strong> sum of the happiness values of the selected children you can achieve by selecting </em><code>k</code> <em>children</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> happiness = [1,2,3], k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> We can pick 2 children in the following way:
- Pick the child with the happiness value == 3. The happiness value of the remaining children becomes [0,1].
- Pick the child with the happiness value == 1. The happiness value of the remaining child becomes [0]. Note that the happiness value cannot become less than 0.
The sum of the happiness values of the selected children is 3 + 1 = 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> happiness = [1,1,1,1], k = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can pick 2 children in the following way:
- Pick any child with the happiness value == 1. The happiness value of the remaining children becomes [0,0,0].
- Pick the child with the happiness value == 0. The happiness value of the remaining child becomes [0,0].
The sum of the happiness values of the selected children is 1 + 0 = 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> happiness = [2,3,4,5], k = 1
<strong>Output:</strong> 5
<strong>Explanation:</strong> We can pick 1 child in the following way:
- Pick the child with the happiness value == 5. The happiness value of the remaining children becomes [1,2,3].
The sum of the happiness values of the selected children is 5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == happiness.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= happiness[i] &lt;= 10<sup>8</sup></code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>


## Hints

1. Since all the unselected numbers are decreasing at the same rate, we should greedily select `k` largest values.

2. The `ith` largest number (`i = 1, 2, 3,…k`) should decrease by `(i - 1)` when it is picked.

3. Add `0` if the decreased value is negative.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-25 01:07:40 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The core idea is to greedily select children with the highest happiness values. Since the happiness of all unselected children decreases by 1 in each turn, it is always optimal to pick the child that currently offers the most happiness. By picking the child with the highest happiness, we 'lock in' its value before it can be reduced further. All other unselected children will suffer the same decrement regardless of which child we pick, so we might as well secure the largest possible value first.

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
#include <algorithm>

class Solution {
public:
    long long maximumHappinessSum(std::vector<int>& happiness, int k) {
        std::sort(happiness.rbegin(), happiness.rend());

        long long totalHappinessSum = 0;
        long long decrements = 0;

        for (int i = 0; i < k; ++i) {
            long long currentHappiness = happiness[i];

            long long selectedHappiness = std::max(0LL, currentHappiness - decrements);
            totalHappinessSum += selectedHappiness;
            decrements++;
        }

        return totalHappinessSum;
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
    public long maximumHappinessSum(int[] happiness, int k) {
        Arrays.sort(happiness);

        long totalHappinessSum = 0;
        long decrements = 0;

        for (int i = 0; i < k; i++) {
            int currentHappiness = happiness[happiness.length - 1 - i];

            long selectedHappiness = Math.max(0L, currentHappiness - decrements);
            totalHappinessSum += selectedHappiness;
            decrements++;
        }

        return totalHappinessSum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)

        total_happiness_sum = 0
        decrements = 0

        for i in range(k):
            current_happiness = happiness[i]

            selected_happiness = max(0, current_happiness - decrements)
            total_happiness_sum += selected_happiness
            decrements += 1

        return total_happiness_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)

        total_happiness_sum = 0
        decrements = 0

        for i in range(k):
            current_happiness = happiness[i]

            selected_happiness = max(0, current_happiness - decrements)
            total_happiness_sum += selected_happiness
            decrements += 1

        return total_happiness_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int*)b - *(int*)a);
}

long long maximumHappinessSum(int* happiness, int happinessSize, int k) {
    qsort(happiness, happinessSize, sizeof(int), compare);

    long long totalHappinessSum = 0;
    long long decrements = 0;

    for (int i = 0; i < k; ++i) {
        long long currentHappiness = happiness[i];

        long long selectedHappiness = currentHappiness - decrements;
        if (selectedHappiness < 0) {
            selectedHappiness = 0;
        }
        totalHappinessSum += selectedHappiness;
        decrements++;
    }

    return totalHappinessSum;
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
    public long MaximumHappinessSum(int[] happiness, int k) {
        Array.Sort(happiness);

        long totalHappinessSum = 0;
        long decrements = 0;

        for (int i = 0; i < k; i++) {
            int currentHappiness = happiness[happiness.Length - 1 - i];

            long selectedHappiness = Math.Max(0L, currentHappiness - decrements);
            totalHappinessSum += selectedHappiness;
            decrements++;
        }

        return totalHappinessSum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} happiness
 * @param {number} k
 * @return {number}
 */
var maximumHappinessSum = function(happiness, k) {
    happiness.sort((a, b) => b - a);

    let totalHappinessSum = 0;
    let decrements = 0;

    for (let i = 0; i < k; i++) {
        let currentHappiness = happiness[i];

        let selectedHappiness = Math.max(0, currentHappiness - decrements);
        totalHappinessSum += selectedHappiness;
        decrements++;
    }

    return totalHappinessSum;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maximumHappinessSum(happiness: number[], k: number): number {
    happiness.sort((a, b) => b - a);

    let totalHappinessSum: number = 0;
    let decrements: number = 0;

    for (let i = 0; i < k; i++) {
        let currentHappiness: number = happiness[i];

        let selectedHappiness: number = Math.max(0, currentHappiness - decrements);
        totalHappinessSum += selectedHappiness;
        decrements++;
    }

    return totalHappinessSum;
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
     * @param int[] $happiness
     * @param int $k
     * @return int
     */
    function maximumHappinessSum($happiness, $k) {
        rsort($happiness);

        $totalHappinessSum = 0;
        $decrements = 0;

        for ($i = 0; $i < $k; $i++) {
            $currentHappiness = $happiness[$i];

            $selectedHappiness = max(0, $currentHappiness - $decrements);
            $totalHappinessSum += $selectedHappiness;
            $decrements++;
        }

        return $totalHappinessSum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maximumHappinessSum(_ happiness: [Int], _ k: Int) -> Int {
        var sortedHappiness = happiness.sorted(by: >)

        var totalHappinessSum: Int = 0
        var decrements: Int = 0

        for i in 0..<k {
            let currentHappiness = sortedHappiness[i]

            let selectedHappiness = max(0, currentHappiness - decrements)
            totalHappinessSum += selectedHappiness
            decrements += 1
        }

        return totalHappinessSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import kotlin.math.max

class Solution {
    fun maximumHappinessSum(happiness: IntArray, k: Int): Long {
        happiness.sortDescending()

        var totalHappinessSum: Long = 0
        var decrements: Long = 0

        for (i in 0 until k) {
            val currentHappiness = happiness[i].toLong()

            val selectedHappiness = max(0L, currentHappiness - decrements)
            totalHappinessSum += selectedHappiness
            decrements++
        }

        return totalHappinessSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:math';

class Solution {
  int maximumHappinessSum(List<int> happiness, int k) {
    happiness.sort((a, b) => b.compareTo(a));

    int totalHappinessSum = 0;
    int decrements = 0;

    for (int i = 0; i < k; i++) {
      int currentHappiness = happiness[i];

      int selectedHappiness = max(0, currentHappiness - decrements);
      totalHappinessSum += selectedHappiness;
      decrements++;
    }

    return totalHappinessSum;
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

func maximumHappinessSum(happiness []int, k int) int64 {
    sort.Slice(happiness, func(i, j int) bool {
        return happiness[i] > happiness[j]
    })

    var totalHappinessSum int64 = 0
    var decrements int64 = 0

    for i := 0; i < k; i++ {
        currentHappiness := int64(happiness[i])

        selectedHappiness := currentHappiness - decrements
        if selectedHappiness < 0 {
            selectedHappiness = 0
        }
        totalHappinessSum += selectedHappiness
        decrements++
    }

    return totalHappinessSum
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} happiness
# @param {Integer} k
# @return {Integer}
def maximum_happiness_sum(happiness, k)
    happiness.sort! { |a, b| b <=> a }

    total_happiness_sum = 0
    decrements = 0

    (0...k).each do |i|
        current_happiness = happiness[i]

        selected_happiness = [0, current_happiness - decrements].max
        total_happiness_sum += selected_happiness
        decrements += 1
    end

    total_happiness_sum
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.math.max

object Solution {
    def maximumHappinessSum(happiness: Array[Int], k: Int): Long = {
        val sortedHappiness = happiness.sorted.reverse

        var totalHappinessSum: Long = 0
        var decrements: Long = 0

        for (i <- 0 until k) {
            val currentHappiness = sortedHappiness(i).toLong

            val selectedHappiness = max(0L, currentHappiness - decrements)
            totalHappinessSum += selectedHappiness
            decrements += 1
        }

        totalHappinessSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn maximum_happiness_sum(mut happiness: Vec<i32>, k: i32) -> i64 {
        happiness.sort_by(|a, b| b.cmp(a));

        let mut total_happiness_sum: i64 = 0;
        let mut decrements: i64 = 0;

        for i in 0..k as usize {
            let current_happiness: i64 = happiness[i] as i64;

            let selected_happiness = (current_happiness - decrements).max(0);
            total_happiness_sum += selected_happiness;
            decrements += 1;
        }

        total_happiness_sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define/contract (maximum-happiness-sum happiness k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([sorted-happiness (sort happiness >)]
         [total-happiness-sum 0]
         [decrements 0])
    (for ([i (in-range k)])
      (let* ([current-happiness (list-ref sorted-happiness i)]
             [selected-happiness (max 0 (- current-happiness decrements))])
        (set! total-happiness-sum (+ total-happiness-sum selected-happiness))
        (set! decrements (+ decrements 1))))
    total-happiness-sum))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([maximum_happiness_sum/2]).

maximum_happiness_sum(Happiness, K) ->
    SortedHappiness = lists:sort(fun(A, B) -> A >= B end, Happiness),

    maximum_happiness_sum_loop(SortedHappiness, K, 0, 0).

maximum_happiness_sum_loop(_SortedHappiness, 0, AccSum, _Decrements) ->
    AccSum;
maximum_happiness_sum_loop([H|T], K, AccSum, Decrements) ->
    SelectedHappiness = max(0, H - Decrements),
    maximum_happiness_sum_loop(T, K - 1, AccSum + SelectedHappiness, Decrements + 1).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximum_happiness_sum(happiness :: [integer], k :: integer) :: integer
  def maximum_happiness_sum(happiness, k) do
    sorted_happiness = Enum.sort(happiness, :desc)

    do_sum(sorted_happiness, k, 0, 0)
  end

  defp do_sum(_sorted_happiness, 0, acc_sum, _decrements), do: acc_sum
  defp do_sum([current_happiness | rest], k, acc_sum, decrements) do
    selected_happiness = max(0, current_happiness - decrements)
    do_sum(rest, k - 1, acc_sum + selected_happiness, decrements + 1)
  end

  defp max(a, b) when a > b, do: a
  defp max(_a, b), do: b
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is dominated by sorting the `happiness` array, which takes O(N log N) time, where N is the number of children. After sorting, we iterate `k` times, which takes O(k) time. Since `k <= N`, the overall time complexity is O(N log N).

- **Space Complexity:** The space complexity depends on the sorting algorithm used. If an in-place sort is used (like C++ `std::sort` or Java `Arrays.sort` for primitives), the auxiliary space complexity is O(log N) or O(1). If a sort that requires auxiliary space is used (like Python's `list.sort()` or `sorted()`, or Java `Arrays.sort` for objects), the space complexity is O(N). Given that we might modify the input array or use a new sorted array, O(N) is a safe upper bound for auxiliary space.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-25 01:07:45 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by using a greedy approach. We first sort the happiness array in descending order. Then, we iterate over the sorted array and add the happiness value of each child to the total sum. However, since the happiness value of all unselected children decreases by 1 in each turn, we need to subtract (i - 1) from the happiness value of the i-th child. If the resulting value is negative, we add 0 to the total sum instead. This approach ensures that we maximize the sum of the happiness values of the selected children. The key intuition behind this approach is that we should always select the child with the highest happiness value first, as this will result in the maximum possible sum of happiness values.

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
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.rbegin(), happiness.rend());
        long long sum = 0;
        for (int i = 0; i < k; i++) {
            sum += max(0, happiness[i] - i);
        }
        return sum;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        Arrays.sort(happiness);
        long sum = 0;
        for (int i = happiness.length - 1; i >= happiness.length - k; i--) {
            sum += Math.max(0, happiness[i] - (happiness.length - 1 - i));
        }
        return sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)
        return sum(max(0, x - i) for i, x in enumerate(happiness[:k]))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)
        return sum(max(0, x - i) for i, x in enumerate(happiness[:k]))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
long long maximumHappinessSum(int* happiness, int happinessSize, int k) {
    qsort(happiness, happinessSize, sizeof(int), compare);
    long long sum = 0;
    for (int i = happinessSize - 1; i >= happinessSize - k; i--) {
        sum += (happiness[i] - (happinessSize - 1 - i) > 0) ? happiness[i] - (happinessSize - 1 - i) : 0;
    }
    return sum;
}
int compare(const void* a, const void* b) {
    return (*(int*)b - *(int*)a);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long MaximumHappinessSum(int[] happiness, int k) {
        Array.Sort(happiness);
        Array.Reverse(happiness);
        long sum = 0;
        for (int i = 0; i < k; i++) {
            sum += Math.Max(0, happiness[i] - i);
        }
        return sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var maximumHappinessSum = function(happiness, k) {
    happiness.sort((a, b) => b - a);
    let sum = 0;
    for (let i = 0; i < k; i++) {
        sum += Math.max(0, happiness[i] - i);
    }
    return sum;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maximumHappinessSum(happiness: number[], k: number): number {
    happiness.sort((a, b) => b - a);
    let sum = 0;
    for (let i = 0; i < k; i++) {
        sum += Math.max(0, happiness[i] - i);
    }
    return sum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
$happiness = $happiness;
rsort($happiness);
$sum = 0;
for ($i = 0; $i < $k; $i++) {
    $sum += max(0, $happiness[$i] - $i);
}
echo $sum;
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maximumHappinessSum(_ happiness: [Int], _ k: Int) -> Int {
        let sortedHappiness = happiness.sorted { $0 > $1 }
        return sortedHappiness.prefix(k).enumerated().map { max(0, $0.1 - $0.0) }.reduce(0, +)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maximumHappinessSum(happiness: IntArray, k: Int): Long {
        happiness.sortDescending()
        return happiness.take(k).mapIndexed { index, i -> maxOf(0, i - index) }.sumOf { it.toLong() }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int maximumHappinessSum(List<int> happiness, int k) {
        happiness.sort((a, b) => b.compareTo(a));
        int sum = 0;
        for (int i = 0; i < k; i++) {
            sum += max(0, happiness[i] - i);
        }
        return sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main
import (
    "sort"
)
func maximumHappinessSum(happiness []int, k int) int64 {
    sort.Sort(sort.Reverse(sort.IntSlice(happiness)))
    sum := int64(0)
    for i := 0; i < k; i++ {
        if happiness[i]-i > 0 {
            sum += int64(happiness[i] - i)
        }
    }
    return sum
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def maximum_happiness_sum(happiness, k)
    happiness.sort!.reverse!
    sum = 0
    k.times do |i|
        sum += [happiness[i] - i, 0].max
    end
    sum
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maximumHappinessSum(happiness: Array[Int], k: Int): Long = {
        val sortedHappiness = happiness.sorted(Ordering.Int.reverse)
        sortedHappiness.take(k).zipWithIndex.map { case (x, i) => math.max(0, x - i) }.sum
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
    pub fn maximum_happiness_sum(mut happiness: Vec<i32>, k: i32) -> i64 {
        happiness.sort_unstable_by(|a, b| b.cmp(a));
        let mut sum = 0;
        for i in 0..k {
            sum += happiness[i as usize].max(0) as i64 - i as i64;
        }
        sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define (maximum-happiness-sum happiness k)
    (let ((sorted-happiness (sort happiness >)))
        (let loop ((i 0) (sum 0))
            (if (= i k)
                sum
                (loop (+ i 1) (+ sum (max 0 (- (list-ref sorted-happiness i) i))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([maximum_happiness_sum/2]).
maximum_happiness_sum(Happiness, K) ->
    lists:sum(lists:map(fun({X, I}) -> max(0, X - I) end, lists:zip(lists:reverse(lists:sort(Happiness)), lists:seq(0, K - 1)))).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def maximum_happiness_sum(happiness, k) do
        happiness
        |> Enum.sort(&(&1 >= &2))
        |> Enum.take(k)
        |> Enum.with_index()
        |> Enum.map(fn {x, i} -> max(0, x - i)
        |> Enum.sum()
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n log n) due to the sorting operation, where n is the number of children. The subsequent for loop has a time complexity of O(k), where k is the number of children to be selected. However, since k is less than or equal to n, the overall time complexity remains O(n log n).

- **Space Complexity:** The space complexity of this solution is O(n) for storing the sorted happiness array. In the worst-case scenario, the space complexity can be O(n) if we need to store all the happiness values in the sorted array.

</div>
</details>
