---
layout: post
title: "Apple Redistribution into Boxes"
date: 2025-12-24 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Greedy", "Sorting"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/apple-redistribution-into-boxes/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <numeric>\n#include <algorithm>\n#include <functional>\n\
        \nclass Solution {\npublic:\n    int minimumBoxes(std::vector<int>& apple, std::vector<int>&\
        \ capacity) {\n        long long totalApples = std::accumulate(apple.begin(),\
        \ apple.end(), 0LL);\n\n        std::sort(capacity.begin(), capacity.end(),\
        \ std::greater<int>());\n\n        long long currentCapacity = 0;\n        int\
        \ boxesCount = 0;\n        for (int cap : capacity) {\n            currentCapacity\
        \ += cap;\n            boxesCount++;\n            if (currentCapacity >= totalApples)\
        \ {\n                break;\n            }\n        }\n\n        return boxesCount;\n\
        \    }\n};"
      java: "import java.util.Arrays;\nimport java.util.Collections;\n\nclass Solution\
        \ {\n    public int minimumBoxes(int[] apple, int[] capacity) {\n        long\
        \ totalApples = 0;\n        for (int a : apple) {\n            totalApples +=\
        \ a;\n        }\n\n        // Sort capacity in descending order\n        Integer[]\
        \ capacityObj = new Integer[capacity.length];\n        for (int i = 0; i < capacity.length;\
        \ i++) {\n            capacityObj[i] = capacity[i];\n        }\n        Arrays.sort(capacityObj,\
        \ Collections.reverseOrder());\n\n        long currentCapacity = 0;\n      \
        \  int boxesCount = 0;\n        for (int cap : capacityObj) {\n            currentCapacity\
        \ += cap;\n            boxesCount++;\n            if (currentCapacity >= totalApples)\
        \ {\n                break;\n            }\n        }\n\n        return boxesCount;\n\
        \    }\n}"
      python: "from typing import List\n\nclass Solution:\n    def minimumBoxes(self,\
        \ apple: List[int], capacity: List[int]) -> int:\n        total_apples = sum(apple)\n\
        \n        capacity.sort(reverse=True)\n\n        current_capacity = 0\n    \
        \    boxes_count = 0\n        for cap in capacity:\n            current_capacity\
        \ += cap\n            boxes_count += 1\n            if current_capacity >= total_apples:\n\
        \                break\n\n        return boxes_count"
      python3: "from typing import List\n\nclass Solution:\n    def minimumBoxes(self,\
        \ apple: List[int], capacity: List[int]) -> int:\n        total_apples = sum(apple)\n\
        \n        capacity.sort(reverse=True)\n\n        current_capacity = 0\n    \
        \    boxes_count = 0\n        for cap in capacity:\n            current_capacity\
        \ += cap\n            boxes_count += 1\n            if current_capacity >= total_apples:\n\
        \                break\n\n        return boxes_count"
      c: "#include <stdio.h>\n#include <stdlib.h> // For qsort\n\n// Comparison function\
        \ for qsort in descending order\nint compare(const void *a, const void *b) {\n\
        \    return (*(int*)b - *(int*)a);\n}\n\nint minimumBoxes(int* apple, int appleSize,\
        \ int* capacity, int capacitySize) {\n    long long totalApples = 0;\n    for\
        \ (int i = 0; i < appleSize; i++) {\n        totalApples += apple[i];\n    }\n\
        \n    qsort(capacity, capacitySize, sizeof(int), compare);\n\n    long long\
        \ currentCapacity = 0;\n    int boxesCount = 0;\n    for (int i = 0; i < capacitySize;\
        \ i++) {\n        currentCapacity += capacity[i];\n        boxesCount++;\n \
        \       if (currentCapacity >= totalApples) {\n            break;\n        }\n\
        \    }\n\n    return boxesCount;\n}"
      csharp: "using System;\nusing System.Linq;\nusing System.Collections.Generic;\n\
        \npublic class Solution {\n    public int MinimumBoxes(int[] apple, int[] capacity)\
        \ {\n        long totalApples = apple.Sum();\n\n        Array.Sort(capacity);\n\
        \        Array.Reverse(capacity);\n\n        long currentCapacity = 0;\n   \
        \     int boxesCount = 0;\n        foreach (int cap in capacity) {\n       \
        \     currentCapacity += cap;\n            boxesCount++;\n            if (currentCapacity\
        \ >= totalApples) {\n                break;\n            }\n        }\n\n  \
        \      return boxesCount;\n    }\n}"
      javascript: "/**\n * @param {number[]} apple\n * @param {number[]} capacity\n\
        \ * @return {number}\n */\nvar minimumBoxes = function(apple, capacity) {\n\
        \    const totalApples = apple.reduce((sum, val) => sum + val, 0);\n\n    capacity.sort((a,\
        \ b) => b - a);\n\n    let currentCapacity = 0;\n    let boxesCount = 0;\n \
        \   for (let i = 0; i < capacity.length; i++) {\n        currentCapacity +=\
        \ capacity[i];\n        boxesCount++;\n        if (currentCapacity >= totalApples)\
        \ {\n            break;\n        }\n    }\n\n    return boxesCount;\n};"
      typescript: "function minimumBoxes(apple: number[], capacity: number[]): number\
        \ {\n    const totalApples: number = apple.reduce((sum, val) => sum + val, 0);\n\
        \n    capacity.sort((a, b) => b - a);\n\n    let currentCapacity: number = 0;\n\
        \    let boxesCount: number = 0;\n    for (let i = 0; i < capacity.length; i++)\
        \ {\n        currentCapacity += capacity[i];\n        boxesCount++;\n      \
        \  if (currentCapacity >= totalApples) {\n            break;\n        }\n  \
        \  }\n\n    return boxesCount;\n};"
      php: "<?php\nclass Solution {\n\n    /**\n     * @param Integer[] $apple\n   \
        \  * @param Integer[] $capacity\n     * @return Integer\n     */\n    function\
        \ minimumBoxes($apple, $capacity) {\n        $totalApples = array_sum($apple);\n\
        \n        rsort($capacity); // Sort in reverse (descending) order\n\n      \
        \  $currentCapacity = 0;\n        $boxesCount = 0;\n        foreach ($capacity\
        \ as $cap) {\n            $currentCapacity += $cap;\n            $boxesCount++;\n\
        \            if ($currentCapacity >= $totalApples) {\n                break;\n\
        \            }\n        }\n\n        return $boxesCount;\n    }\n}"
      swift: "class Solution {\n    func minimumBoxes(_ apple: [Int], _ capacity: [Int])\
        \ -> Int {\n        let totalApples = apple.reduce(0, +)\n\n        let sortedCapacity\
        \ = capacity.sorted(by: >)\n\n        var currentCapacity = 0\n        var boxesCount\
        \ = 0\n        for cap in sortedCapacity {\n            currentCapacity += cap\n\
        \            boxesCount += 1\n            if currentCapacity >= totalApples\
        \ {\n                break\n            }\n        }\n\n        return boxesCount\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun minimumBoxes(apple: IntArray, capacity: IntArray):\
        \ Int {\n        val totalApples = apple.sum().toLong()\n\n        val sortedCapacity\
        \ = capacity.sortedDescending()\n\n        var currentCapacity: Long = 0\n \
        \       var boxesCount = 0\n        for (cap in sortedCapacity) {\n        \
        \    currentCapacity += cap\n            boxesCount++\n            if (currentCapacity\
        \ >= totalApples) {\n                break\n            }\n        }\n\n   \
        \     return boxesCount\n    }\n}"
      dart: "class Solution {\n  int minimumBoxes(List<int> apple, List<int> capacity)\
        \ {\n    int totalApples = apple.fold(0, (sum, element) => sum + element);\n\
        \n    capacity.sort((a, b) => b.compareTo(a)); // Sort in descending order\n\
        \n    int currentCapacity = 0;\n    int boxesCount = 0;\n    for (int cap in\
        \ capacity) {\n      currentCapacity += cap;\n      boxesCount++;\n      if\
        \ (currentCapacity >= totalApples) {\n        break;\n      }\n    }\n\n   \
        \ return boxesCount;\n  }\n}"
      go: "import (\n\t\"sort\"\n)\n\nfunc minimumBoxes(apple []int, capacity []int)\
        \ int {\n    totalApples := 0\n    for _, a := range apple {\n        totalApples\
        \ += a\n    }\n\n    sort.Slice(capacity, func(i, j int) bool {\n        return\
        \ capacity[i] > capacity[j]\n    })\n\n    currentCapacity := 0\n    boxesCount\
        \ := 0\n    for _, cap := range capacity {\n        currentCapacity += cap\n\
        \        boxesCount++\n        if currentCapacity >= totalApples {\n       \
        \     break\n        }\n    }\n\n    return boxesCount\n}"
      ruby: "class Solution\n    def minimum_boxes(apple, capacity)\n        total_apples\
        \ = apple.sum\n\n        capacity.sort!.reverse!\n\n        current_capacity\
        \ = 0\n        boxes_count = 0\n        capacity.each do |cap|\n           \
        \ current_capacity += cap\n            boxes_count += 1\n            if current_capacity\
        \ >= total_apples\n                break\n            end\n        end\n\n \
        \       boxes_count\n    end\nend"
      scala: "object Solution {\n    def minimumBoxes(apple: Array[Int], capacity: Array[Int]):\
        \ Int = {\n        val totalApples = apple.sum.toLong\n\n        val sortedCapacity\
        \ = capacity.sorted(Ordering.Int.reverse)\n\n        var currentCapacity: Long\
        \ = 0\n        var boxesCount = 0\n        for (cap <- sortedCapacity) {\n \
        \           currentCapacity += cap\n            boxesCount += 1\n          \
        \  if (currentCapacity >= totalApples) {\n                return boxesCount\n\
        \            }\n        }\n        boxesCount // Should not be reached if problem\
        \ guarantees possibility\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_boxes(apple: Vec<i32>, capacity: Vec<i32>)\
        \ -> i32 {\n        let total_apples: i64 = apple.iter().map(|&x| x as i64).sum();\n\
        \n        let mut capacity_mut = capacity;\n        capacity_mut.sort_unstable_by(|a,\
        \ b| b.cmp(a)); // Sort descending\n\n        let mut current_capacity: i64\
        \ = 0;\n        let mut boxes_count = 0;\n        for cap in capacity_mut {\n\
        \            current_capacity += cap as i64;\n            boxes_count += 1;\n\
        \            if current_capacity >= total_apples {\n                break;\n\
        \            }\n        }\n\n        boxes_count\n    }\n}"
      racket: "#lang racket\n(define/contract (minimum-boxes apple capacity)\n  (->\
        \ (listof exact-integer?) (listof exact-integer?) exact-integer?)\n  (let* ((total-apples\
        \ (apply + apple))\n         (sorted-capacity (sort capacity >)))\n    (let\
        \ loop ((current-capacity 0)\n               (boxes-count 0)\n             \
        \  (remaining-capacity sorted-capacity))\n      (if (>= current-capacity total-apples)\n\
        \          boxes-count\n          (loop (+ current-capacity (car remaining-capacity))\n\
        \                (+ boxes-count 1)\n                (cdr remaining-capacity))))))"
      erlang: "-module(solution).\n-export([minimum_boxes/2]).\n\nminimum_boxes(Apple,\
        \ Capacity) ->\n    TotalApples = lists:sum(Apple),\n    SortedCapacity = lists:reverse(lists:sort(Capacity)),\n\
        \n    minimum_boxes_recursive(TotalApples, SortedCapacity, 0, 0).\n\nminimum_boxes_recursive(TotalApples,\
        \ [H|T], CurrentCapacity, BoxesCount) when CurrentCapacity < TotalApples ->\n\
        \    minimum_boxes_recursive(TotalApples, T, CurrentCapacity + H, BoxesCount\
        \ + 1);\nminimum_boxes_recursive(_TotalApples, _Capacity, _CurrentCapacity,\
        \ BoxesCount) ->\n    BoxesCount."
      elixir: "defmodule Solution do\n  @spec minimum_boxes(apple :: [integer], capacity\
        \ :: [integer]) :: integer\n  def minimum_boxes(apple, capacity) do\n    total_apples\
        \ = Enum.sum(apple)\n\n    sorted_capacity = Enum.sort(capacity, :desc)\n\n\
        \    do_minimum_boxes(total_apples, sorted_capacity, 0, 0)\n  end\n\n  defp\
        \ do_minimum_boxes(total_apples, [head | tail], current_capacity, boxes_count)\
        \ when current_capacity < total_apples do\n    do_minimum_boxes(total_apples,\
        \ tail, current_capacity + head, boxes_count + 1)\n  end\n\n  defp do_minimum_boxes(_total_apples,\
        \ _capacity, _current_capacity, boxes_count) do\n    boxes_count\n  end\nend"
    approach: 'The core idea behind solving this problem is recognizing that since apples
      from the same pack can be distributed into different boxes, the specific distribution
      of individual packs doesn''t matter. What matters is the total sum of all apples
      and the total capacity of the selected boxes. To find the minimum number of boxes,
      we should always prioritize using boxes with the largest capacities first. This
      is a classic greedy approach, as selecting a larger capacity box always helps
      satisfy the total apple requirement faster than a smaller capacity box, thus minimizing
      the count of boxes needed.


      The algorithm proceeds in two main steps. First, calculate the total number of
      apples by summing all elements in the `apple` array. Second, sort the `capacity`
      array in descending order to ensure we always pick the largest available capacities.
      Then, iterate through the sorted `capacity` array, accumulating the capacity of
      selected boxes and incrementing a counter for each box used. This process continues
      until the accumulated capacity is greater than or equal to the total sum of apples.
      The final value of the box counter will be the minimum number of boxes required.'
    time_complexity: 'The time complexity is dominated by two operations: calculating
      the sum of apples and sorting the capacities. Summing the `apple` array takes
      O(N) time, where N is the number of apple packs. Sorting the `capacity` array
      takes O(M log M) time, where M is the number of boxes. The subsequent iteration
      through the sorted capacities takes at most O(M) time. Therefore, the overall
      time complexity is O(N + M log M).'
    space_complexity: The space complexity is O(1) if the sorting algorithm used for
      the `capacity` array is in-place (e.g., `std::sort` in C++ or `sort()` in Python
      for primitive types often have O(log M) or O(1) auxiliary space). If the sorting
      algorithm requires creating a copy of the array, or if the language's sort implementation
      uses O(M) auxiliary space, then the space complexity would be O(M). In most practical
      competitive programming contexts for these constraints, it's considered O(1) auxiliary
      space.
    elapsed_time: 38.40998911857605
    model: gemini-2.5-flash
    generated_at: '2025-12-24 01:06:58 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumBoxes(vector<int>& apple, vector<int>&\
        \ capacity) {\n        sort(capacity.begin(), capacity.end());\n        int\
        \ n = apple.size();\n        int m = capacity.size();\n        int i = m - 1;\n\
        \        int count = 0;\n        int remaining = 0;\n        for (int j = n\
        \ - 1; j >= 0; j--) {\n            if (remaining < apple[j]) {\n           \
        \     if (i < 0) return -1;\n                remaining = capacity[i--];\n  \
        \              count++;\n            }\n            remaining -= apple[j];\n\
        \        }\n        return count;\n    }\n};"
      java: "class Solution {\n    public int minimumBoxes(int[] apple, int[] capacity)\
        \ {\n        Arrays.sort(capacity);\n        int n = apple.length;\n       \
        \ int m = capacity.length;\n        int i = m - 1;\n        int count = 0;\n\
        \        int remaining = 0;\n        for (int j = n - 1; j >= 0; j--) {\n  \
        \          if (remaining < apple[j]) {\n                if (i < 0) return -1;\n\
        \                remaining = capacity[i--];\n                count++;\n    \
        \        }\n            remaining -= apple[j];\n        }\n        return count;\n\
        \    }\n}"
      python: "class Solution:\n    def minimumBoxes(self, apple: list[int], capacity:\
        \ list[int]) -> int:\n        capacity.sort()\n        n = len(apple)\n    \
        \    m = len(capacity)\n        i = m - 1\n        count = 0\n        remaining\
        \ = 0\n        for j in range(n - 1, -1, -1):\n            if remaining < apple[j]:\n\
        \                if i < 0: return -1\n                remaining = capacity[i]\n\
        \                i -= 1\n                count += 1\n            remaining -=\
        \ apple[j]\n        return count"
      python3: "class Solution:\n    def minimumBoxes(self, apple: list[int], capacity:\
        \ list[int]) -> int:\n        capacity.sort()\n        n = len(apple)\n    \
        \    m = len(capacity)\n        i = m - 1\n        count = 0\n        remaining\
        \ = 0\n        for j in range(n - 1, -1, -1):\n            if remaining < apple[j]:\n\
        \                if i < 0: return -1\n                remaining = capacity[i]\n\
        \                i -= 1\n                count += 1\n            remaining -=\
        \ apple[j]\n        return count"
      c: "int compare(const void *a, const void *b) {\n    return (*(int*)a - *(int*)b);\n\
        }\n\nint minimumBoxes(int* apple, int appleSize, int* capacity, int capacitySize)\
        \ {\n    qsort(capacity, capacitySize, sizeof(int), compare);\n    int i = capacitySize\
        \ - 1;\n    int count = 0;\n    int remaining = 0;\n    for (int j = appleSize\
        \ - 1; j >= 0; j--) {\n        if (remaining < apple[j]) {\n            if (i\
        \ < 0) return -1;\n            remaining = capacity[i--];\n            count++;\n\
        \        }\n        remaining -= apple[j];\n    }\n    return count;\n}"
      csharp: "public class Solution {\n    public int MinimumBoxes(int[] apple, int[]\
        \ capacity) {\n        Array.Sort(capacity);\n        int n = apple.Length;\n\
        \        int m = capacity.Length;\n        int i = m - 1;\n        int count\
        \ = 0;\n        int remaining = 0;\n        for (int j = n - 1; j >= 0; j--)\
        \ {\n            if (remaining < apple[j]) {\n                if (i < 0) return\
        \ -1;\n                remaining = capacity[i--];\n                count++;\n\
        \            }\n            remaining -= apple[j];\n        }\n        return\
        \ count;\n    }\n}"
      javascript: "var minimumBoxes = function(apple, capacity) {\n    capacity.sort((a,\
        \ b) => a - b);\n    let n = apple.length;\n    let m = capacity.length;\n \
        \   let i = m - 1;\n    let count = 0;\n    let remaining = 0;\n    for (let\
        \ j = n - 1; j >= 0; j--) {\n        if (remaining < apple[j]) {\n         \
        \   if (i < 0) return -1;\n            remaining = capacity[i--];\n        \
        \    count++;\n        }\n        remaining -= apple[j];\n    }\n    return\
        \ count;\n};"
      typescript: "function minimumBoxes(apple: number[], capacity: number[]): number\
        \ {\n    capacity.sort((a, b) => a - b);\n    let n = apple.length;\n    let\
        \ m = capacity.length;\n    let i = m - 1;\n    let count = 0;\n    let remaining\
        \ = 0;\n    for (let j = n - 1; j >= 0; j--) {\n        if (remaining < apple[j])\
        \ {\n            if (i < 0) return -1;\n            remaining = capacity[i--];\n\
        \            count++;\n        }\n        remaining -= apple[j];\n    }\n  \
        \  return count;\n}"
      php: "function minimumBoxes($apple, $capacity) {\n    sort($capacity);\n    $n\
        \ = count($apple);\n    $m = count($capacity);\n    $i = $m - 1;\n    $count\
        \ = 0;\n    $remaining = 0;\n    for ($j = $n - 1; $j >= 0; $j--) {\n      \
        \  if ($remaining < $apple[$j]) {\n            if ($i < 0) return -1;\n    \
        \        $remaining = $capacity[$i--];\n            $count++;\n        }\n \
        \       $remaining -= $apple[$j];\n    }\n    return $count;\n}"
      swift: "class Solution {\n    func minimumBoxes(_ apple: [Int], _ capacity: [Int])\
        \ -> Int {\n        let sortedCapacity = capacity.sorted()\n        let n =\
        \ apple.count\n        let m = capacity.count\n        var i = m - 1\n     \
        \   var count = 0\n        var remaining = 0\n        for j in stride(from:\
        \ n - 1, through: 0, by: -1) {\n            if remaining < apple[j] {\n    \
        \            if i < 0 { return -1 }\n                remaining = sortedCapacity[i]\n\
        \                i -= 1\n                count += 1\n            }\n       \
        \     remaining -= apple[j]\n        }\n        return count\n    }\n}"
      kotlin: "class Solution {\n    fun minimumBoxes(apple: IntArray, capacity: IntArray):\
        \ Int {\n        capacity.sort()\n        val n = apple.size\n        val m\
        \ = capacity.size\n        var i = m - 1\n        var count = 0\n        var\
        \ remaining = 0\n        for (j in n - 1 downTo 0) {\n            if (remaining\
        \ < apple[j]) {\n                if (i < 0) return -1\n                remaining\
        \ = capacity[i--]\n                count++\n            }\n            remaining\
        \ -= apple[j]\n        }\n        return count\n    }\n}"
      dart: "class Solution {\n    int minimumBoxes(List<int> apple, List<int> capacity)\
        \ {\n        capacity.sort()\n        int n = apple.length;\n        int m =\
        \ capacity.length;\n        int i = m - 1;\n        int count = 0;\n       \
        \ int remaining = 0;\n        for (int j = n - 1; j >= 0; j--) {\n         \
        \   if (remaining < apple[j]) {\n                if (i < 0) return -1;\n   \
        \             remaining = capacity[i--];\n                count++;\n       \
        \     }\n            remaining -= apple[j];\n        }\n        return count;\n\
        \    }\n}"
      go: "func minimumBoxes(apple []int, capacity []int) int {\n    sort.Ints(capacity)\n\
        \    n := len(apple)\n    m := len(capacity)\n    i := m - 1\n    count := 0\n\
        \    remaining := 0\n    for j := n - 1; j >= 0; j-- {\n        if remaining\
        \ < apple[j] {\n            if i < 0 { return -1 }\n            remaining =\
        \ capacity[i]\n            i--\n            count++\n        }\n        remaining\
        \ -= apple[j]\n    }\n    return count\n}"
      ruby: "def minimum_boxes(apple, capacity)\n    capacity.sort!\n    n = apple.size\n\
        \    m = capacity.size\n    i = m - 1\n    count = 0\n    remaining = 0\n  \
        \  (n - 1).downto(0) do |j|\n        if remaining < apple[j]\n            if\
        \ i < 0\n                return -1\n            end\n            remaining =\
        \ capacity[i]\n            i -= 1\n            count += 1\n        end\n   \
        \     remaining -= apple[j]\n    end\n    count\nend"
      scala: "object Solution {\n    def minimumBoxes(apple: Array[Int], capacity: Array[Int]):\
        \ Int = {\n        val sortedCapacity = capacity.sorted\n        val n = apple.length\n\
        \        val m = capacity.length\n        var i = m - 1\n        var count =\
        \ 0\n        var remaining = 0\n        for (j <- n - 1 to 0 by -1) {\n    \
        \        if (remaining < apple(j)) {\n                if (i < 0) return -1\n\
        \                remaining = sortedCapacity(i)\n                i -= 1\n   \
        \             count += 1\n            }\n            remaining -= apple(j)\n\
        \        }\n        count\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_boxes(apple: Vec<i32>, capacity: Vec<i32>)\
        \ -> i32 {\n        let mut capacity = capacity;\n        capacity.sort_unstable();\n\
        \        let n = apple.len();\n        let m = capacity.len();\n        let\
        \ mut i = m - 1;\n        let mut count = 0;\n        let mut remaining = 0;\n\
        \        for j in (0..n).rev() {\n            if remaining < apple[j] {\n  \
        \              if i < 0 { return -1; }\n                remaining = capacity[i]\n\
        \                i -= 1;\n                count += 1;\n            }\n     \
        \       remaining -= apple[j]\n        }\n        count\n    }\n}"
      racket: "define (minimum-boxes apple capacity)\n    (let* (\n        (capacity\
        \ (sort capacity <))\n        (n (length apple))\n        (m (length capacity))\n\
        \        (i (- m 1))\n        (count 0)\n        (remaining 0))\n        (do\
        \ (\n            (j (- n 1)))\n            ((< j 0))\n            (if (< remaining\
        \ (list-ref apple j))\n                (if (< i 0)\n                    -1\n\
        \                    (begin\n                        (set! remaining (list-ref\
        \ capacity i))\n                        (set! i (- i 1))\n                 \
        \       (set! count (+ count 1))\n                        ))\n            (set!\
        \ remaining (- remaining (list-ref apple j)))\n            (set! j (- j 1))\n\
        \        )\n        count)\n    )"
      erlang: "minimum_boxes(Apple, Capacity) ->\n    lists:foldl(\n        fun(J, {Count,\
        \ Remaining, I}) ->\n            case Remaining < lists:nth(J + 1, Apple) of\n\
        \                true ->\n                    case I < 0 of\n              \
        \          true -> -1;\n                        false ->\n                 \
        \           {Count + 1, lists:nth(I + 1, Capacity), I - 1}\n               \
        \     end;\n                false ->\n                    {Count, Remaining\
        \ - lists:nth(J + 1, Apple), I}\n            end\n        end,\n        {0,\
        \ 0, length(Capacity) - 1},\n        lists:seq(0, length(Apple) - 1))\n    ."
      elixir: "def minimum_boxes(apple, capacity) do\n    capacity = Enum.sort(capacity)\n\
        \    n = length(apple)\n    m = length(capacity)\n    i = m - 1\n    count =\
        \ 0\n    remaining = 0\n    Enum.reduce((n - 1)..0, {count, remaining, i}, fn\
        \ j, {count, remaining, i} ->\n        if remaining < Enum.at(apple, j) do\n\
        \            if i < 0 do\n                -1\n            else\n           \
        \     {count + 1, Enum.at(capacity, i), i - 1}\n            end\n        else\n\
        \            {count, remaining - Enum.at(apple, j), i}\n        end\n    end)\n\
        \    |> elem(0)\nend"
    approach: 'The problem can be solved by first sorting the capacity array in non-decreasing
      order. Then, we can use a greedy approach to select the boxes with the largest
      capacities to redistribute the apples. The key intuition here is that we want
      to use the boxes with the largest capacities first to minimize the number of boxes
      needed. We can iterate over the apple array and try to fill the boxes with the
      largest capacities until we have filled all the apples or used all the boxes.


      The algorithm works by maintaining a pointer to the current box and the remaining
      capacity of the current box. We iterate over the apple array and for each apple,
      we try to fill the current box. If the current box is not enough to hold the apple,
      we move to the next box. We repeat this process until we have filled all the apples
      or used all the boxes. The number of boxes used is the minimum number of boxes
      needed to redistribute the apples.'
    time_complexity: The time complexity of the algorithm is O(n log n + m log m) where
      n is the number of apples and m is the number of boxes. This is because we first
      sort the capacity array which takes O(m log m) time and then we iterate over the
      apple array which takes O(n) time. The sorting of the apple array is not needed
      as we are not using it to decide which box to use, but rather we are using the
      capacity array to decide which box to use. The greedy approach ensures that we
      use the boxes with the largest capacities first, which minimizes the number of
      boxes needed.
    space_complexity: The space complexity of the algorithm is O(1) as we are not using
      any extra space that scales with the input size. We are only using a constant
      amount of space to store the pointers and the remaining capacity of the current
      box.
    elapsed_time: 7.1560046672821045
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-24 01:07:05 '
---

## Problem #3074: Apple Redistribution into Boxes

**Difficulty:** Easy

**Topics:** Array, Greedy, Sorting

## Problem Description

<p>You are given an array <code>apple</code> of size <code>n</code> and an array <code>capacity</code> of size <code>m</code>.</p>

<p>There are <code>n</code> packs where the <code>i<sup>th</sup></code> pack contains <code>apple[i]</code> apples. There are <code>m</code> boxes as well, and the <code>i<sup>th</sup></code> box has a capacity of <code>capacity[i]</code> apples.</p>

<p>Return <em>the <strong>minimum</strong> number of boxes you need to select to redistribute these </em><code>n</code><em> packs of apples into boxes</em>.</p>

<p><strong>Note</strong> that, apples from the same pack can be distributed into different boxes.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> apple = [1,3,2], capacity = [4,3,1,5,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong> We will use boxes with capacities 4 and 5.
It is possible to distribute the apples as the total capacity is greater than or equal to the total number of apples.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> apple = [5,5,5], capacity = [2,4,2,7]
<strong>Output:</strong> 4
<strong>Explanation:</strong> We will need to use all the boxes.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == apple.length &lt;= 50</code></li>
	<li><code>1 &lt;= m == capacity.length &lt;= 50</code></li>
	<li><code>1 &lt;= apple[i], capacity[i] &lt;= 50</code></li>
	<li>The input is generated such that it&#39;s possible to redistribute packs of apples into boxes.</li>
</ul>


## Hints

1. Sort array `capacity` in non-decreasing order.

2. Greedily select boxes with the largest capacities to redistribute apples optimally.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-24 01:06:58 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The core idea behind solving this problem is recognizing that since apples from the same pack can be distributed into different boxes, the specific distribution of individual packs doesn't matter. What matters is the total sum of all apples and the total capacity of the selected boxes. To find the minimum number of boxes, we should always prioritize using boxes with the largest capacities first. This is a classic greedy approach, as selecting a larger capacity box always helps satisfy the total apple requirement faster than a smaller capacity box, thus minimizing the count of boxes needed.

The algorithm proceeds in two main steps. First, calculate the total number of apples by summing all elements in the `apple` array. Second, sort the `capacity` array in descending order to ensure we always pick the largest available capacities. Then, iterate through the sorted `capacity` array, accumulating the capacity of selected boxes and incrementing a counter for each box used. This process continues until the accumulated capacity is greater than or equal to the total sum of apples. The final value of the box counter will be the minimum number of boxes required.

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
#include <algorithm>
#include <functional>

class Solution {
public:
    int minimumBoxes(std::vector<int>& apple, std::vector<int>& capacity) {
        long long totalApples = std::accumulate(apple.begin(), apple.end(), 0LL);

        std::sort(capacity.begin(), capacity.end(), std::greater<int>());

        long long currentCapacity = 0;
        int boxesCount = 0;
        for (int cap : capacity) {
            currentCapacity += cap;
            boxesCount++;
            if (currentCapacity >= totalApples) {
                break;
            }
        }

        return boxesCount;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {
        long totalApples = 0;
        for (int a : apple) {
            totalApples += a;
        }

        // Sort capacity in descending order
        Integer[] capacityObj = new Integer[capacity.length];
        for (int i = 0; i < capacity.length; i++) {
            capacityObj[i] = capacity[i];
        }
        Arrays.sort(capacityObj, Collections.reverseOrder());

        long currentCapacity = 0;
        int boxesCount = 0;
        for (int cap : capacityObj) {
            currentCapacity += cap;
            boxesCount++;
            if (currentCapacity >= totalApples) {
                break;
            }
        }

        return boxesCount;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)

        capacity.sort(reverse=True)

        current_capacity = 0
        boxes_count = 0
        for cap in capacity:
            current_capacity += cap
            boxes_count += 1
            if current_capacity >= total_apples:
                break

        return boxes_count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)

        capacity.sort(reverse=True)

        current_capacity = 0
        boxes_count = 0
        for cap in capacity:
            current_capacity += cap
            boxes_count += 1
            if current_capacity >= total_apples:
                break

        return boxes_count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h> // For qsort

// Comparison function for qsort in descending order
int compare(const void *a, const void *b) {
    return (*(int*)b - *(int*)a);
}

int minimumBoxes(int* apple, int appleSize, int* capacity, int capacitySize) {
    long long totalApples = 0;
    for (int i = 0; i < appleSize; i++) {
        totalApples += apple[i];
    }

    qsort(capacity, capacitySize, sizeof(int), compare);

    long long currentCapacity = 0;
    int boxesCount = 0;
    for (int i = 0; i < capacitySize; i++) {
        currentCapacity += capacity[i];
        boxesCount++;
        if (currentCapacity >= totalApples) {
            break;
        }
    }

    return boxesCount;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int MinimumBoxes(int[] apple, int[] capacity) {
        long totalApples = apple.Sum();

        Array.Sort(capacity);
        Array.Reverse(capacity);

        long currentCapacity = 0;
        int boxesCount = 0;
        foreach (int cap in capacity) {
            currentCapacity += cap;
            boxesCount++;
            if (currentCapacity >= totalApples) {
                break;
            }
        }

        return boxesCount;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} apple
 * @param {number[]} capacity
 * @return {number}
 */
var minimumBoxes = function(apple, capacity) {
    const totalApples = apple.reduce((sum, val) => sum + val, 0);

    capacity.sort((a, b) => b - a);

    let currentCapacity = 0;
    let boxesCount = 0;
    for (let i = 0; i < capacity.length; i++) {
        currentCapacity += capacity[i];
        boxesCount++;
        if (currentCapacity >= totalApples) {
            break;
        }
    }

    return boxesCount;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumBoxes(apple: number[], capacity: number[]): number {
    const totalApples: number = apple.reduce((sum, val) => sum + val, 0);

    capacity.sort((a, b) => b - a);

    let currentCapacity: number = 0;
    let boxesCount: number = 0;
    for (let i = 0; i < capacity.length; i++) {
        currentCapacity += capacity[i];
        boxesCount++;
        if (currentCapacity >= totalApples) {
            break;
        }
    }

    return boxesCount;
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
     * @param Integer[] $apple
     * @param Integer[] $capacity
     * @return Integer
     */
    function minimumBoxes($apple, $capacity) {
        $totalApples = array_sum($apple);

        rsort($capacity); // Sort in reverse (descending) order

        $currentCapacity = 0;
        $boxesCount = 0;
        foreach ($capacity as $cap) {
            $currentCapacity += $cap;
            $boxesCount++;
            if ($currentCapacity >= $totalApples) {
                break;
            }
        }

        return $boxesCount;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumBoxes(_ apple: [Int], _ capacity: [Int]) -> Int {
        let totalApples = apple.reduce(0, +)

        let sortedCapacity = capacity.sorted(by: >)

        var currentCapacity = 0
        var boxesCount = 0
        for cap in sortedCapacity {
            currentCapacity += cap
            boxesCount += 1
            if currentCapacity >= totalApples {
                break
            }
        }

        return boxesCount
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumBoxes(apple: IntArray, capacity: IntArray): Int {
        val totalApples = apple.sum().toLong()

        val sortedCapacity = capacity.sortedDescending()

        var currentCapacity: Long = 0
        var boxesCount = 0
        for (cap in sortedCapacity) {
            currentCapacity += cap
            boxesCount++
            if (currentCapacity >= totalApples) {
                break
            }
        }

        return boxesCount
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumBoxes(List<int> apple, List<int> capacity) {
    int totalApples = apple.fold(0, (sum, element) => sum + element);

    capacity.sort((a, b) => b.compareTo(a)); // Sort in descending order

    int currentCapacity = 0;
    int boxesCount = 0;
    for (int cap in capacity) {
      currentCapacity += cap;
      boxesCount++;
      if (currentCapacity >= totalApples) {
        break;
      }
    }

    return boxesCount;
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

func minimumBoxes(apple []int, capacity []int) int {
    totalApples := 0
    for _, a := range apple {
        totalApples += a
    }

    sort.Slice(capacity, func(i, j int) bool {
        return capacity[i] > capacity[j]
    })

    currentCapacity := 0
    boxesCount := 0
    for _, cap := range capacity {
        currentCapacity += cap
        boxesCount++
        if currentCapacity >= totalApples {
            break
        }
    }

    return boxesCount
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def minimum_boxes(apple, capacity)
        total_apples = apple.sum

        capacity.sort!.reverse!

        current_capacity = 0
        boxes_count = 0
        capacity.each do |cap|
            current_capacity += cap
            boxes_count += 1
            if current_capacity >= total_apples
                break
            end
        end

        boxes_count
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumBoxes(apple: Array[Int], capacity: Array[Int]): Int = {
        val totalApples = apple.sum.toLong

        val sortedCapacity = capacity.sorted(Ordering.Int.reverse)

        var currentCapacity: Long = 0
        var boxesCount = 0
        for (cap <- sortedCapacity) {
            currentCapacity += cap
            boxesCount += 1
            if (currentCapacity >= totalApples) {
                return boxesCount
            }
        }
        boxesCount // Should not be reached if problem guarantees possibility
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_boxes(apple: Vec<i32>, capacity: Vec<i32>) -> i32 {
        let total_apples: i64 = apple.iter().map(|&x| x as i64).sum();

        let mut capacity_mut = capacity;
        capacity_mut.sort_unstable_by(|a, b| b.cmp(a)); // Sort descending

        let mut current_capacity: i64 = 0;
        let mut boxes_count = 0;
        for cap in capacity_mut {
            current_capacity += cap as i64;
            boxes_count += 1;
            if current_capacity >= total_apples {
                break;
            }
        }

        boxes_count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
(define/contract (minimum-boxes apple capacity)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((total-apples (apply + apple))
         (sorted-capacity (sort capacity >)))
    (let loop ((current-capacity 0)
               (boxes-count 0)
               (remaining-capacity sorted-capacity))
      (if (>= current-capacity total-apples)
          boxes-count
          (loop (+ current-capacity (car remaining-capacity))
                (+ boxes-count 1)
                (cdr remaining-capacity))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([minimum_boxes/2]).

minimum_boxes(Apple, Capacity) ->
    TotalApples = lists:sum(Apple),
    SortedCapacity = lists:reverse(lists:sort(Capacity)),

    minimum_boxes_recursive(TotalApples, SortedCapacity, 0, 0).

minimum_boxes_recursive(TotalApples, [H|T], CurrentCapacity, BoxesCount) when CurrentCapacity < TotalApples ->
    minimum_boxes_recursive(TotalApples, T, CurrentCapacity + H, BoxesCount + 1);
minimum_boxes_recursive(_TotalApples, _Capacity, _CurrentCapacity, BoxesCount) ->
    BoxesCount.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_boxes(apple :: [integer], capacity :: [integer]) :: integer
  def minimum_boxes(apple, capacity) do
    total_apples = Enum.sum(apple)

    sorted_capacity = Enum.sort(capacity, :desc)

    do_minimum_boxes(total_apples, sorted_capacity, 0, 0)
  end

  defp do_minimum_boxes(total_apples, [head | tail], current_capacity, boxes_count) when current_capacity < total_apples do
    do_minimum_boxes(total_apples, tail, current_capacity + head, boxes_count + 1)
  end

  defp do_minimum_boxes(_total_apples, _capacity, _current_capacity, boxes_count) do
    boxes_count
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is dominated by two operations: calculating the sum of apples and sorting the capacities. Summing the `apple` array takes O(N) time, where N is the number of apple packs. Sorting the `capacity` array takes O(M log M) time, where M is the number of boxes. The subsequent iteration through the sorted capacities takes at most O(M) time. Therefore, the overall time complexity is O(N + M log M).

- **Space Complexity:** The space complexity is O(1) if the sorting algorithm used for the `capacity` array is in-place (e.g., `std::sort` in C++ or `sort()` in Python for primitive types often have O(log M) or O(1) auxiliary space). If the sorting algorithm requires creating a copy of the array, or if the language's sort implementation uses O(M) auxiliary space, then the space complexity would be O(M). In most practical competitive programming contexts for these constraints, it's considered O(1) auxiliary space.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-24 01:07:05 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by first sorting the capacity array in non-decreasing order. Then, we can use a greedy approach to select the boxes with the largest capacities to redistribute the apples. The key intuition here is that we want to use the boxes with the largest capacities first to minimize the number of boxes needed. We can iterate over the apple array and try to fill the boxes with the largest capacities until we have filled all the apples or used all the boxes.

The algorithm works by maintaining a pointer to the current box and the remaining capacity of the current box. We iterate over the apple array and for each apple, we try to fill the current box. If the current box is not enough to hold the apple, we move to the next box. We repeat this process until we have filled all the apples or used all the boxes. The number of boxes used is the minimum number of boxes needed to redistribute the apples.

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
    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
        sort(capacity.begin(), capacity.end());
        int n = apple.size();
        int m = capacity.size();
        int i = m - 1;
        int count = 0;
        int remaining = 0;
        for (int j = n - 1; j >= 0; j--) {
            if (remaining < apple[j]) {
                if (i < 0) return -1;
                remaining = capacity[i--];
                count++;
            }
            remaining -= apple[j];
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
    public int minimumBoxes(int[] apple, int[] capacity) {
        Arrays.sort(capacity);
        int n = apple.length;
        int m = capacity.length;
        int i = m - 1;
        int count = 0;
        int remaining = 0;
        for (int j = n - 1; j >= 0; j--) {
            if (remaining < apple[j]) {
                if (i < 0) return -1;
                remaining = capacity[i--];
                count++;
            }
            remaining -= apple[j];
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
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        capacity.sort()
        n = len(apple)
        m = len(capacity)
        i = m - 1
        count = 0
        remaining = 0
        for j in range(n - 1, -1, -1):
            if remaining < apple[j]:
                if i < 0: return -1
                remaining = capacity[i]
                i -= 1
                count += 1
            remaining -= apple[j]
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        capacity.sort()
        n = len(apple)
        m = len(capacity)
        i = m - 1
        count = 0
        remaining = 0
        for j in range(n - 1, -1, -1):
            if remaining < apple[j]:
                if i < 0: return -1
                remaining = capacity[i]
                i -= 1
                count += 1
            remaining -= apple[j]
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int minimumBoxes(int* apple, int appleSize, int* capacity, int capacitySize) {
    qsort(capacity, capacitySize, sizeof(int), compare);
    int i = capacitySize - 1;
    int count = 0;
    int remaining = 0;
    for (int j = appleSize - 1; j >= 0; j--) {
        if (remaining < apple[j]) {
            if (i < 0) return -1;
            remaining = capacity[i--];
            count++;
        }
        remaining -= apple[j];
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
    public int MinimumBoxes(int[] apple, int[] capacity) {
        Array.Sort(capacity);
        int n = apple.Length;
        int m = capacity.Length;
        int i = m - 1;
        int count = 0;
        int remaining = 0;
        for (int j = n - 1; j >= 0; j--) {
            if (remaining < apple[j]) {
                if (i < 0) return -1;
                remaining = capacity[i--];
                count++;
            }
            remaining -= apple[j];
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
var minimumBoxes = function(apple, capacity) {
    capacity.sort((a, b) => a - b);
    let n = apple.length;
    let m = capacity.length;
    let i = m - 1;
    let count = 0;
    let remaining = 0;
    for (let j = n - 1; j >= 0; j--) {
        if (remaining < apple[j]) {
            if (i < 0) return -1;
            remaining = capacity[i--];
            count++;
        }
        remaining -= apple[j];
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumBoxes(apple: number[], capacity: number[]): number {
    capacity.sort((a, b) => a - b);
    let n = apple.length;
    let m = capacity.length;
    let i = m - 1;
    let count = 0;
    let remaining = 0;
    for (let j = n - 1; j >= 0; j--) {
        if (remaining < apple[j]) {
            if (i < 0) return -1;
            remaining = capacity[i--];
            count++;
        }
        remaining -= apple[j];
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
function minimumBoxes($apple, $capacity) {
    sort($capacity);
    $n = count($apple);
    $m = count($capacity);
    $i = $m - 1;
    $count = 0;
    $remaining = 0;
    for ($j = $n - 1; $j >= 0; $j--) {
        if ($remaining < $apple[$j]) {
            if ($i < 0) return -1;
            $remaining = $capacity[$i--];
            $count++;
        }
        $remaining -= $apple[$j];
    }
    return $count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumBoxes(_ apple: [Int], _ capacity: [Int]) -> Int {
        let sortedCapacity = capacity.sorted()
        let n = apple.count
        let m = capacity.count
        var i = m - 1
        var count = 0
        var remaining = 0
        for j in stride(from: n - 1, through: 0, by: -1) {
            if remaining < apple[j] {
                if i < 0 { return -1 }
                remaining = sortedCapacity[i]
                i -= 1
                count += 1
            }
            remaining -= apple[j]
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
    fun minimumBoxes(apple: IntArray, capacity: IntArray): Int {
        capacity.sort()
        val n = apple.size
        val m = capacity.size
        var i = m - 1
        var count = 0
        var remaining = 0
        for (j in n - 1 downTo 0) {
            if (remaining < apple[j]) {
                if (i < 0) return -1
                remaining = capacity[i--]
                count++
            }
            remaining -= apple[j]
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
    int minimumBoxes(List<int> apple, List<int> capacity) {
        capacity.sort()
        int n = apple.length;
        int m = capacity.length;
        int i = m - 1;
        int count = 0;
        int remaining = 0;
        for (int j = n - 1; j >= 0; j--) {
            if (remaining < apple[j]) {
                if (i < 0) return -1;
                remaining = capacity[i--];
                count++;
            }
            remaining -= apple[j];
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
func minimumBoxes(apple []int, capacity []int) int {
    sort.Ints(capacity)
    n := len(apple)
    m := len(capacity)
    i := m - 1
    count := 0
    remaining := 0
    for j := n - 1; j >= 0; j-- {
        if remaining < apple[j] {
            if i < 0 { return -1 }
            remaining = capacity[i]
            i--
            count++
        }
        remaining -= apple[j]
    }
    return count
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def minimum_boxes(apple, capacity)
    capacity.sort!
    n = apple.size
    m = capacity.size
    i = m - 1
    count = 0
    remaining = 0
    (n - 1).downto(0) do |j|
        if remaining < apple[j]
            if i < 0
                return -1
            end
            remaining = capacity[i]
            i -= 1
            count += 1
        end
        remaining -= apple[j]
    end
    count
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumBoxes(apple: Array[Int], capacity: Array[Int]): Int = {
        val sortedCapacity = capacity.sorted
        val n = apple.length
        val m = capacity.length
        var i = m - 1
        var count = 0
        var remaining = 0
        for (j <- n - 1 to 0 by -1) {
            if (remaining < apple(j)) {
                if (i < 0) return -1
                remaining = sortedCapacity(i)
                i -= 1
                count += 1
            }
            remaining -= apple(j)
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
impl Solution {
    pub fn minimum_boxes(apple: Vec<i32>, capacity: Vec<i32>) -> i32 {
        let mut capacity = capacity;
        capacity.sort_unstable();
        let n = apple.len();
        let m = capacity.len();
        let mut i = m - 1;
        let mut count = 0;
        let mut remaining = 0;
        for j in (0..n).rev() {
            if remaining < apple[j] {
                if i < 0 { return -1; }
                remaining = capacity[i]
                i -= 1;
                count += 1;
            }
            remaining -= apple[j]
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
define (minimum-boxes apple capacity)
    (let* (
        (capacity (sort capacity <))
        (n (length apple))
        (m (length capacity))
        (i (- m 1))
        (count 0)
        (remaining 0))
        (do (
            (j (- n 1)))
            ((< j 0))
            (if (< remaining (list-ref apple j))
                (if (< i 0)
                    -1
                    (begin
                        (set! remaining (list-ref capacity i))
                        (set! i (- i 1))
                        (set! count (+ count 1))
                        ))
            (set! remaining (- remaining (list-ref apple j)))
            (set! j (- j 1))
        )
        count)
    )
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
minimum_boxes(Apple, Capacity) ->
    lists:foldl(
        fun(J, {Count, Remaining, I}) ->
            case Remaining < lists:nth(J + 1, Apple) of
                true ->
                    case I < 0 of
                        true -> -1;
                        false ->
                            {Count + 1, lists:nth(I + 1, Capacity), I - 1}
                    end;
                false ->
                    {Count, Remaining - lists:nth(J + 1, Apple), I}
            end
        end,
        {0, 0, length(Capacity) - 1},
        lists:seq(0, length(Apple) - 1))
    .
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def minimum_boxes(apple, capacity) do
    capacity = Enum.sort(capacity)
    n = length(apple)
    m = length(capacity)
    i = m - 1
    count = 0
    remaining = 0
    Enum.reduce((n - 1)..0, {count, remaining, i}, fn j, {count, remaining, i} ->
        if remaining < Enum.at(apple, j) do
            if i < 0 do
                -1
            else
                {count + 1, Enum.at(capacity, i), i - 1}
            end
        else
            {count, remaining - Enum.at(apple, j), i}
        end
    end)
    |> elem(0)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the algorithm is O(n log n + m log m) where n is the number of apples and m is the number of boxes. This is because we first sort the capacity array which takes O(m log m) time and then we iterate over the apple array which takes O(n) time. The sorting of the apple array is not needed as we are not using it to decide which box to use, but rather we are using the capacity array to decide which box to use. The greedy approach ensures that we use the boxes with the largest capacities first, which minimizes the number of boxes needed.

- **Space Complexity:** The space complexity of the algorithm is O(1) as we are not using any extra space that scales with the input size. We are only using a constant amount of space to store the pointers and the remaining capacity of the current box.

</div>
</details>
