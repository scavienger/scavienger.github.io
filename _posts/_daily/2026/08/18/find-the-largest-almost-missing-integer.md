---
layout: post
title: "Find the Largest Almost Missing Integer"
date: 2026-08-18 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Hash Table"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/find-the-largest-almost-missing-integer/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int largestInteger(vector<int>& nums, int\
        \ k) {\n        int n = nums.size();\n        int subarray_counts[51] = {0};\n\
        \n        for (int i = 0; i <= n - k; ++i) {\n            bool seen[51] = {false};\n\
        \            for (int j = i; j < i + k; ++j) {\n                int val = nums[j];\n\
        \                if (!seen[val]) {\n                    subarray_counts[val]++;\n\
        \                    seen[val] = true;\n                }\n            }\n \
        \       }\n\n        int max_val = -1;\n        for (int i = 0; i <= 50; ++i)\
        \ {\n            if (subarray_counts[i] == 1) {\n                max_val = i;\n\
        \            }\n        }\n        return max_val;\n    }\n};"
      java: "class Solution {\n    public int largestInteger(int[] nums, int k) {\n\
        \        int n = nums.length;\n        int[] subarrayCounts = new int[51];\n\
        \n        for (int i = 0; i <= n - k; i++) {\n            boolean[] seen = new\
        \ boolean[51];\n            for (int j = i; j < i + k; j++) {\n            \
        \    int val = nums[j];\n                if (!seen[val]) {\n               \
        \     subarrayCounts[val]++;\n                    seen[val] = true;\n      \
        \          }\n            }\n        }\n\n        int max_val = -1;\n      \
        \  for (int i = 0; i <= 50; i++) {\n            if (subarrayCounts[i] == 1)\
        \ {\n                max_val = i;\n            }\n        }\n        return\
        \ max_val;\n    }\n}"
      python: "class Solution(object):\n    def largestInteger(self, nums, k):\n   \
        \     \"\"\"\n        :type nums: List[int]\n        :type k: int\n        :rtype:\
        \ int\n        \"\"\"\n        n = len(nums)\n        subarray_counts = {}\n\
        \n        for i in range(n - k + 1):\n            subarray = nums[i : i + k]\n\
        \            unique_elements = set(subarray)\n            for x in unique_elements:\n\
        \                subarray_counts[x] = subarray_counts.get(x, 0) + 1\n\n    \
        \    max_val = -1\n        for x, count in subarray_counts.items():\n      \
        \      if count == 1:\n                if x > max_val:\n                   \
        \ max_val = x\n        return max_val"
      python3: "class Solution:\n    def largestInteger(self, nums: List[int], k: int)\
        \ -> int:\n        n = len(nums)\n        subarray_counts = {}\n\n        for\
        \ i in range(n - k + 1):\n            subarray = nums[i : i + k]\n         \
        \   unique_elements = set(subarray)\n            for x in unique_elements:\n\
        \                subarray_counts[x] = subarray_counts.get(x, 0) + 1\n\n    \
        \    max_val = -1\n        for x, count in subarray_counts.items():\n      \
        \      if count == 1:\n                if x > max_val:\n                   \
        \ max_val = x\n        return max_val"
      c: "int largestInteger(int* nums, int numsSize, int k) {\n    int subarray_counts[51];\n\
        \    for (int i = 0; i < 51; i++) {\n        subarray_counts[i] = 0;\n    }\n\
        \n    for (int i = 0; i <= numsSize - k; i++) {\n        int seen[51];\n   \
        \     for (int j = 0; j < 51; j++) {\n            seen[j] = 0;\n        }\n\
        \        for (int j = i; j < i + k; j++) {\n            int val = nums[j];\n\
        \            if (!seen[val]) {\n                subarray_counts[val]++;\n  \
        \              seen[val] = 1;\n            }\n        }\n    }\n\n    int max_val\
        \ = -1;\n    for (int i = 0; i < 51; i++) {\n        if (subarray_counts[i]\
        \ == 1) {\n            max_val = i;\n        }\n    }\n    return max_val;\n\
        }"
      csharp: "public class Solution {\n    public int LargestInteger(int[] nums, int\
        \ k) {\n        int n = nums.Length;\n        int[] subarrayCounts = new int[51];\n\
        \n        for (int i = 0; i <= n - k; i++) {\n            bool[] seen = new\
        \ bool[51];\n            for (int j = i; j < i + k; j++) {\n               \
        \ int val = nums[j];\n                if (!seen[val]) {\n                  \
        \  subarrayCounts[val]++;\n                    seen[val] = true;\n         \
        \       }\n            }\n        }\n\n        int maxVal = -1;\n        for\
        \ (int i = 0; i <= 50; i++) {\n            if (subarrayCounts[i] == 1) {\n \
        \               maxVal = i;\n            }\n        }\n        return maxVal;\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @return\
        \ {number}\n */\nvar largestInteger = function(nums, k) {\n    const n = nums.length;\n\
        \    const subarrayCounts = new Array(51).fill(0);\n\n    for (let i = 0; i\
        \ <= n - k; i++) {\n        const seen = new Array(51).fill(false);\n      \
        \  for (let j = i; j < i + k; j++) {\n            const val = nums[j];\n   \
        \         if (!seen[val]) {\n                subarrayCounts[val]++;\n      \
        \          seen[val] = true;\n            }\n        }\n    }\n\n    let maxVal\
        \ = -1;\n    for (let i = 0; i <= 50; i++) {\n        if (subarrayCounts[i]\
        \ === 1) {\n            maxVal = i;\n        }\n    }\n    return maxVal;\n\
        };"
      typescript: "function largestInteger(nums: number[], k: number): number {\n  \
        \  const counts = new Map<number, number>();\n    const n = nums.length;\n\n\
        \    for (let i = 0; i <= n - k; i++) {\n        const subarray = nums.slice(i,\
        \ i + k);\n        const unique = new Set(subarray);\n        for (const val\
        \ of unique) {\n            counts.set(val, (counts.get(val) || 0) + 1);\n \
        \       }\n    }\n\n    let maxVal = -1;\n    for (const [val, count] of counts.entries())\
        \ {\n        if (count === 1) {\n            if (val > maxVal) {\n         \
        \       maxVal = val;\n            }\n        }\n    }\n\n    return maxVal;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $k\n     * @return Integer\n     */\n    function largestInteger($nums,\
        \ $k) {\n        $counts = [];\n        $n = count($nums);\n\n        for ($i\
        \ = 0; $i <= $n - $k; $i++) {\n            $subarray = array_slice($nums, $i,\
        \ $k);\n            $unique = array_unique($subarray);\n            foreach\
        \ ($unique as $val) {\n                if (!isset($counts[$val])) {\n      \
        \              $counts[$val] = 0;\n                }\n                $counts[$val]++;\n\
        \            }\n        }\n\n        $maxVal = -1;\n        foreach ($counts\
        \ as $val => $count) {\n            if ($count == 1) {\n                if ($val\
        \ > $maxVal) {\n                    $maxVal = $val;\n                }\n   \
        \         }\n        }\n\n        return $maxVal;\n    }\n}"
      swift: "class Solution {\n    func largestInteger(_ nums: [Int], _ k: Int) ->\
        \ Int {\n        var counts = [Int: Int]()\n        let n = nums.count\n\n \
        \       for i in 0...(n - k) {\n            let subarray = nums[i..<(i + k)]\n\
        \            let unique = Set(subarray)\n            for val in unique {\n \
        \               counts[val, default: 0] += 1\n            }\n        }\n\n \
        \       var maxVal = -1\n        for (val, count) in counts {\n            if\
        \ count == 1 {\n                if val > maxVal {\n                    maxVal\
        \ = val\n                }\n            }\n        }\n\n        return maxVal\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun largestInteger(nums: IntArray, k: Int): Int\
        \ {\n        val counts = mutableMapOf<Int, Int>()\n        val n = nums.size\n\
        \n        for (i in 0..(n - k)) {\n            val subarray = nums.sliceArray(i\
        \ until i + k)\n            val unique = subarray.toSet()\n            for (valItem\
        \ in unique) {\n                counts[valItem] = counts.getOrDefault(valItem,\
        \ 0) + 1\n            }\n        }\n\n        var maxVal = -1\n        for ((valItem,\
        \ count) in counts) {\n            if (count == 1) {\n                if (valItem\
        \ > maxVal) {\n                    maxVal = valItem\n                }\n   \
        \         }\n        }\n\n        return maxVal\n    }\n}"
      dart: "class Solution {\n  int largestInteger(List<int> nums, int k) {\n    Map<int,\
        \ int> counts = {};\n    int n = nums.length;\n\n    for (int i = 0; i <= n\
        \ - k; i++) {\n      Set<int> unique = nums.sublist(i, i + k).toSet();\n   \
        \   for (int val in unique) {\n        counts[val] = (counts[val] ?? 0) + 1;\n\
        \      }\n    }\n\n    int maxVal = -1;\n    counts.forEach((val, count) {\n\
        \      if (count == 1) {\n        if (val > maxVal) {\n          maxVal = val;\n\
        \        }\n      }\n    });\n\n    return maxVal;\n  }\n}"
      go: "func largestInteger(nums []int, k int) int {\n    counts := make(map[int]int)\n\
        \    n := len(nums)\n\n    for i := 0; i <= n-k; i++ {\n        unique := make(map[int]bool)\n\
        \        for _, val := range nums[i : i+k] {\n            unique[val] = true\n\
        \        }\n        for val := range unique {\n            counts[val]++\n \
        \       }\n    }\n\n    maxVal := -1\n    for val, count := range counts {\n\
        \        if count == 1 {\n            if val > maxVal {\n                maxVal\
        \ = val\n            }\n        }\n    }\n\n    return maxVal\n}"
      ruby: "def largest_integer(nums, k)\n  n = nums.length\n  if k == n\n    return\
        \ nums.max\n  end\n\n  if k == 1\n    counts = Hash.new(0)\n    nums.each {\
        \ |x| counts[x] += 1 }\n    ones = counts.select { |x, count| count == 1 }.keys\n\
        \    return ones.empty? ? -1 : ones.max\n  end\n\n  first = nums[0]\n  last\
        \ = nums[n - 1]\n  candidates = []\n  candidates << first if nums.count(first)\
        \ == 1\n  candidates << last if nums.count(last) == 1\n\n  candidates.empty?\
        \ ? -1 : candidates.max\nend"
      scala: "object Solution {\n    def largestInteger(nums: Array[Int], k: Int): Int\
        \ = {\n        val n = nums.length\n        if (k == n) {\n            return\
        \ nums.max\n        }\n\n        if (k == 1) {\n            val counts = nums.groupBy(identity).map\
        \ { case (k, v) => (k, v.length) }\n            val ones = counts.filter { case\
        \ (_, count) => count == 1 }.keys\n            if (ones.isEmpty) -1 else ones.max\n\
        \        } else {\n            var ans = -1\n            val first = nums(0)\n\
        \            val last = nums(n - 1)\n\n            if (nums.count(_ == first)\
        \ == 1) {\n                ans = Math.max(ans, first)\n            }\n     \
        \       if (nums.count(_ == last) == 1) {\n                ans = Math.max(ans,\
        \ last)\n            }\n            ans\n        }\n    }\n}"
      rust: "impl Solution {\n    pub fn largest_integer(nums: Vec<i32>, k: i32) ->\
        \ i32 {\n        let n = nums.len();\n        let k_size = k as usize;\n   \
        \     if k_size == n {\n            return *nums.iter().max().unwrap_or(&-1);\n\
        \        }\n\n        if k_size == 1 {\n            let mut counts = std::collections::HashMap::new();\n\
        \            for &x in &nums {\n                *counts.entry(x).or_insert(0)\
        \ += 1;\n            }\n            let mut ans = -1;\n            for (&x,\
        \ &count) in &counts {\n                if count == 1 && x > ans {\n       \
        \             ans = x;\n                }\n            }\n            return\
        \ ans;\n        }\n\n        let mut ans = -1;\n        let first = nums[0];\n\
        \        let last = nums[n - 1];\n\n        if nums.iter().filter(|&&x| x ==\
        \ first).count() == 1 {\n            if first > ans {\n                ans =\
        \ first;\n            }\n        }\n        if nums.iter().filter(|&&x| x ==\
        \ last).count() == 1 {\n            if last > ans {\n                ans = last;\n\
        \            }\n        }\n        ans\n    }\n}"
      racket: "(define/contract (largest-integer nums k)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer?)\n  (let ([n (length nums)])\n    (cond\n  \
        \    [(= k n) (apply max nums)]\n      [(= k 1)\n       (let ([counts (make-hash)])\n\
        \         (for-each (lambda (x) (hash-set! counts x (+ 1 (hash-ref counts x\
        \ 0)))) nums)\n         (let ([ones (filter (lambda (x) (= (hash-ref counts\
        \ x) 1)) (hash-keys counts))])\n           (if (null? ones) -1 (apply max ones))))]\n\
        \      [else\n       (let* ([first-val (list-ref nums 0)]\n              [last-val\
        \ (list-ref nums (- n 1))]\n              [first-count (length (filter (lambda\
        \ (x) (= x first-val)) nums))]\n              [last-count (length (filter (lambda\
        \ (x) (= x last-val)) nums))]\n              [ans -1])\n         (let* ([ans1\
        \ (if (= first-count 1) (max ans first-val) ans)]\n                [ans2 (if\
        \ (= last-count 1) (max ans1 last-val) ans1)])\n           ans2))]))"
      erlang: "largest_integer(Nums, K) ->\n  N = length(Nums),\n  if\n    K == N ->\
        \ lists:max(Nums);\n    K == 1 ->\n      Counts = lists:foldl(fun(X, Acc) ->\n\
        \        maps:put(X, maps:get(X, Acc, 0) + 1, Acc)\n      end, #{}, Nums),\n\
        \      Ones = [X || {X, Count} <- maps:to_list(Counts), Count == 1],\n     \
        \ case Ones of\n        [] -> -1;\n        _ -> lists:max(Ones)\n      end;\n\
        \    true ->\n      First = hd(Nums),\n      Last = lists:last(Nums),\n    \
        \  FirstCount = length([X || X <- Nums, X == First]),\n      LastCount = length([X\
        \ || X <- Nums, X == Last]),\n      Candidates = (if FirstCount == 1 -> [First];\
        \ true -> [] end) ++\n                   (if LastCount == 1 -> [Last]; true\
        \ -> [] end),\n      case Candidates of\n        [] -> -1;\n        _ -> lists:max(Candidates)\n\
        \      end\n  end."
      elixir: "defmodule Solution do\n  @spec largest_integer(nums :: [integer], k ::\
        \ integer) :: integer\n  def largest_integer(nums, k) do\n    n = length(nums)\n\
        \    cond do\n      k == n ->\n        Enum.max(nums)\n      k == 1 ->\n   \
        \     ones = nums\n        |> Enum.reduce(%{}, fn x, acc -> Map.update(acc,\
        \ x, 1, &(&1 + 1)) end)\n        |> Enum.filter(fn {_, count} -> count == 1\
        \ end)\n        |> Enum.map(fn {val, _} -> val end)\n        if ones == [],\
        \ do: -1, else: Enum.max(ones)\n      true ->\n        first = List.first(nums)\n\
        \        last = List.last(nums)\n        first_count = Enum.count(nums, &(&1\
        \ == first))\n        last_count = Enum.count(nums, &(&1 == last))\n       \
        \ ans = -1\n        ans = if first_count == 1, do: max(ans, first), else: ans\n\
        \        ans = if last_count == 1, do: max(ans, last), else: ans\n        ans\n\
        \    end\n  end\nend"
    approach: 'The problem asks to find the largest integer appearing in exactly one
      contiguous subarray of size $k$. Given the small constraints (array length $n
      \le 50$ and values up to 50), we can directly simulate the subarray counting process.
      We iterate through each starting position $i$ from $0$ to $n - k$ and extract
      the subarray starting at $i$ with length $k$. For each subarray, we identify the
      set of unique elements it contains and increment their respective counts in a
      global frequency map or array, representing the number of distinct subarrays each
      element appears in.


      After processing all possible subarrays, we iterate through the frequency map
      and identify all integers that have a count of exactly one. The largest of these
      integers is our ''largest almost missing'' integer. If no such integer is found,
      we return -1. This approach is robust as it naturally handles special cases, such
      as when $k=1$ (where we look for the largest unique element in the array) or $k=n$
      (where we find the largest element in the entire array).'
    time_complexity: O(n^2). There are $n - k + 1$ subarrays of size $k$. In the worst
      case, $n - k + 1 \approx n/2$ and $k \approx n/2$, leading to approximately $n^2
      / 4$ operations. With $n \le 50$, this results in at most 2,500 operations, making
      it extremely efficient.
    space_complexity: O(n). We use a frequency map or an array of size 51 (since $0
      \le nums[i] \le 50$) to store the number of subarrays each unique integer appears
      in. This requires space proportional to the number of unique elements or the maximum
      value in the input array.
    elapsed_time: 474.05817675590515
    model: gemini-3-flash-preview
    generated_at: '2026-08-18 00:54:16 '
---

## Problem #3471: Find the Largest Almost Missing Integer

**Difficulty:** Easy

**Topics:** Array, Hash Table

## Problem Description

<p>You are given an integer array <code>nums</code> and an integer <code>k</code>.</p>

<p>An integer <code>x</code> is <strong>almost missing</strong> from <code>nums</code> if <code>x</code> appears in <em>exactly</em> one subarray of size <code>k</code> within <code>nums</code>.</p>

<p>Return the <b>largest</b> <strong>almost missing</strong> integer from <code>nums</code>. If no such integer exists, return <code>-1</code>.</p>
A <strong>subarray</strong> is a contiguous sequence of elements within an array.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,9,2,1,7], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>1 appears in 2 subarrays of size 3: <code>[9, 2, 1]</code> and <code>[2, 1, 7]</code>.</li>
	<li>2 appears in 3 subarrays of size 3: <code>[3, 9, 2]</code>, <code>[9, 2, 1]</code>, <code>[2, 1, 7]</code>.</li>
	<li index="2">3 appears in 1 subarray of size 3: <code>[3, 9, 2]</code>.</li>
	<li index="3">7 appears in 1 subarray of size 3: <code>[2, 1, 7]</code>.</li>
	<li index="4">9 appears in 2 subarrays of size 3: <code>[3, 9, 2]</code>, and <code>[9, 2, 1]</code>.</li>
</ul>

<p>We return 7 since it is the largest integer that appears in exactly one subarray of size <code>k</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,9,7,2,1,7], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>1 appears in 2 subarrays of size 4: <code>[9, 7, 2, 1]</code>, <code>[7, 2, 1, 7]</code>.</li>
	<li>2 appears in 3 subarrays of size 4: <code>[3, 9, 7, 2]</code>, <code>[9, 7, 2, 1]</code>, <code>[7, 2, 1, 7]</code>.</li>
	<li>3 appears in 1 subarray of size 4: <code>[3, 9, 7, 2]</code>.</li>
	<li>7 appears in 3 subarrays of size 4: <code>[3, 9, 7, 2]</code>, <code>[9, 7, 2, 1]</code>, <code>[7, 2, 1, 7]</code>.</li>
	<li>9 appears in 2 subarrays of size 4: <code>[3, 9, 7, 2]</code>, <code>[9, 7, 2, 1]</code>.</li>
</ul>

<p>We return 3 since it is the largest and only integer that appears in exactly one subarray of size <code>k</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,0], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no integer that appears in only one subarray of size 1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 50</code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>


## Hints

1. Solve the problem for three different cases: `k = 1`, `k = n`, and `1 < k < n`

2. If `k = 1`, return the largest element that occurs exactly once in `nums`

3. If `k = n`, return the largest element in `nums`

4. If `1 < k < n`, all elements different from `nums[0]` and `nums[n - 1]` will occur in more than one subarray of size `k`. Hence, the answer is the largest of `nums[0]` and `nums[n - 1]` if they both occur exactly once in the array. If one of them occurs more than once, return the other. If both of them occur more than once, return -1.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks to find the largest integer appearing in exactly one contiguous subarray of size $k$. Given the small constraints (array length $n \le 50$ and values up to 50), we can directly simulate the subarray counting process. We iterate through each starting position $i$ from $0$ to $n - k$ and extract the subarray starting at $i$ with length $k$. For each subarray, we identify the set of unique elements it contains and increment their respective counts in a global frequency map or array, representing the number of distinct subarrays each element appears in.

After processing all possible subarrays, we iterate through the frequency map and identify all integers that have a count of exactly one. The largest of these integers is our 'largest almost missing' integer. If no such integer is found, we return -1. This approach is robust as it naturally handles special cases, such as when $k=1$ (where we look for the largest unique element in the array) or $k=n$ (where we find the largest element in the entire array).

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
    int largestInteger(vector<int>& nums, int k) {
        int n = nums.size();
        int subarray_counts[51] = {0};

        for (int i = 0; i <= n - k; ++i) {
            bool seen[51] = {false};
            for (int j = i; j < i + k; ++j) {
                int val = nums[j];
                if (!seen[val]) {
                    subarray_counts[val]++;
                    seen[val] = true;
                }
            }
        }

        int max_val = -1;
        for (int i = 0; i <= 50; ++i) {
            if (subarray_counts[i] == 1) {
                max_val = i;
            }
        }
        return max_val;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int largestInteger(int[] nums, int k) {
        int n = nums.length;
        int[] subarrayCounts = new int[51];

        for (int i = 0; i <= n - k; i++) {
            boolean[] seen = new boolean[51];
            for (int j = i; j < i + k; j++) {
                int val = nums[j];
                if (!seen[val]) {
                    subarrayCounts[val]++;
                    seen[val] = true;
                }
            }
        }

        int max_val = -1;
        for (int i = 0; i <= 50; i++) {
            if (subarrayCounts[i] == 1) {
                max_val = i;
            }
        }
        return max_val;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        subarray_counts = {}

        for i in range(n - k + 1):
            subarray = nums[i : i + k]
            unique_elements = set(subarray)
            for x in unique_elements:
                subarray_counts[x] = subarray_counts.get(x, 0) + 1

        max_val = -1
        for x, count in subarray_counts.items():
            if count == 1:
                if x > max_val:
                    max_val = x
        return max_val
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subarray_counts = {}

        for i in range(n - k + 1):
            subarray = nums[i : i + k]
            unique_elements = set(subarray)
            for x in unique_elements:
                subarray_counts[x] = subarray_counts.get(x, 0) + 1

        max_val = -1
        for x, count in subarray_counts.items():
            if count == 1:
                if x > max_val:
                    max_val = x
        return max_val
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int largestInteger(int* nums, int numsSize, int k) {
    int subarray_counts[51];
    for (int i = 0; i < 51; i++) {
        subarray_counts[i] = 0;
    }

    for (int i = 0; i <= numsSize - k; i++) {
        int seen[51];
        for (int j = 0; j < 51; j++) {
            seen[j] = 0;
        }
        for (int j = i; j < i + k; j++) {
            int val = nums[j];
            if (!seen[val]) {
                subarray_counts[val]++;
                seen[val] = 1;
            }
        }
    }

    int max_val = -1;
    for (int i = 0; i < 51; i++) {
        if (subarray_counts[i] == 1) {
            max_val = i;
        }
    }
    return max_val;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int LargestInteger(int[] nums, int k) {
        int n = nums.Length;
        int[] subarrayCounts = new int[51];

        for (int i = 0; i <= n - k; i++) {
            bool[] seen = new bool[51];
            for (int j = i; j < i + k; j++) {
                int val = nums[j];
                if (!seen[val]) {
                    subarrayCounts[val]++;
                    seen[val] = true;
                }
            }
        }

        int maxVal = -1;
        for (int i = 0; i <= 50; i++) {
            if (subarrayCounts[i] == 1) {
                maxVal = i;
            }
        }
        return maxVal;
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
 * @param {number} k
 * @return {number}
 */
var largestInteger = function(nums, k) {
    const n = nums.length;
    const subarrayCounts = new Array(51).fill(0);

    for (let i = 0; i <= n - k; i++) {
        const seen = new Array(51).fill(false);
        for (let j = i; j < i + k; j++) {
            const val = nums[j];
            if (!seen[val]) {
                subarrayCounts[val]++;
                seen[val] = true;
            }
        }
    }

    let maxVal = -1;
    for (let i = 0; i <= 50; i++) {
        if (subarrayCounts[i] === 1) {
            maxVal = i;
        }
    }
    return maxVal;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function largestInteger(nums: number[], k: number): number {
    const counts = new Map<number, number>();
    const n = nums.length;

    for (let i = 0; i <= n - k; i++) {
        const subarray = nums.slice(i, i + k);
        const unique = new Set(subarray);
        for (const val of unique) {
            counts.set(val, (counts.get(val) || 0) + 1);
        }
    }

    let maxVal = -1;
    for (const [val, count] of counts.entries()) {
        if (count === 1) {
            if (val > maxVal) {
                maxVal = val;
            }
        }
    }

    return maxVal;
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
     * @param Integer $k
     * @return Integer
     */
    function largestInteger($nums, $k) {
        $counts = [];
        $n = count($nums);

        for ($i = 0; $i <= $n - $k; $i++) {
            $subarray = array_slice($nums, $i, $k);
            $unique = array_unique($subarray);
            foreach ($unique as $val) {
                if (!isset($counts[$val])) {
                    $counts[$val] = 0;
                }
                $counts[$val]++;
            }
        }

        $maxVal = -1;
        foreach ($counts as $val => $count) {
            if ($count == 1) {
                if ($val > $maxVal) {
                    $maxVal = $val;
                }
            }
        }

        return $maxVal;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func largestInteger(_ nums: [Int], _ k: Int) -> Int {
        var counts = [Int: Int]()
        let n = nums.count

        for i in 0...(n - k) {
            let subarray = nums[i..<(i + k)]
            let unique = Set(subarray)
            for val in unique {
                counts[val, default: 0] += 1
            }
        }

        var maxVal = -1
        for (val, count) in counts {
            if count == 1 {
                if val > maxVal {
                    maxVal = val
                }
            }
        }

        return maxVal
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun largestInteger(nums: IntArray, k: Int): Int {
        val counts = mutableMapOf<Int, Int>()
        val n = nums.size

        for (i in 0..(n - k)) {
            val subarray = nums.sliceArray(i until i + k)
            val unique = subarray.toSet()
            for (valItem in unique) {
                counts[valItem] = counts.getOrDefault(valItem, 0) + 1
            }
        }

        var maxVal = -1
        for ((valItem, count) in counts) {
            if (count == 1) {
                if (valItem > maxVal) {
                    maxVal = valItem
                }
            }
        }

        return maxVal
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int largestInteger(List<int> nums, int k) {
    Map<int, int> counts = {};
    int n = nums.length;

    for (int i = 0; i <= n - k; i++) {
      Set<int> unique = nums.sublist(i, i + k).toSet();
      for (int val in unique) {
        counts[val] = (counts[val] ?? 0) + 1;
      }
    }

    int maxVal = -1;
    counts.forEach((val, count) {
      if (count == 1) {
        if (val > maxVal) {
          maxVal = val;
        }
      }
    });

    return maxVal;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func largestInteger(nums []int, k int) int {
    counts := make(map[int]int)
    n := len(nums)

    for i := 0; i <= n-k; i++ {
        unique := make(map[int]bool)
        for _, val := range nums[i : i+k] {
            unique[val] = true
        }
        for val := range unique {
            counts[val]++
        }
    }

    maxVal := -1
    for val, count := range counts {
        if count == 1 {
            if val > maxVal {
                maxVal = val
            }
        }
    }

    return maxVal
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def largest_integer(nums, k)
  n = nums.length
  if k == n
    return nums.max
  end

  if k == 1
    counts = Hash.new(0)
    nums.each { |x| counts[x] += 1 }
    ones = counts.select { |x, count| count == 1 }.keys
    return ones.empty? ? -1 : ones.max
  end

  first = nums[0]
  last = nums[n - 1]
  candidates = []
  candidates << first if nums.count(first) == 1
  candidates << last if nums.count(last) == 1

  candidates.empty? ? -1 : candidates.max
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def largestInteger(nums: Array[Int], k: Int): Int = {
        val n = nums.length
        if (k == n) {
            return nums.max
        }

        if (k == 1) {
            val counts = nums.groupBy(identity).map { case (k, v) => (k, v.length) }
            val ones = counts.filter { case (_, count) => count == 1 }.keys
            if (ones.isEmpty) -1 else ones.max
        } else {
            var ans = -1
            val first = nums(0)
            val last = nums(n - 1)

            if (nums.count(_ == first) == 1) {
                ans = Math.max(ans, first)
            }
            if (nums.count(_ == last) == 1) {
                ans = Math.max(ans, last)
            }
            ans
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
    pub fn largest_integer(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k_size = k as usize;
        if k_size == n {
            return *nums.iter().max().unwrap_or(&-1);
        }

        if k_size == 1 {
            let mut counts = std::collections::HashMap::new();
            for &x in &nums {
                *counts.entry(x).or_insert(0) += 1;
            }
            let mut ans = -1;
            for (&x, &count) in &counts {
                if count == 1 && x > ans {
                    ans = x;
                }
            }
            return ans;
        }

        let mut ans = -1;
        let first = nums[0];
        let last = nums[n - 1];

        if nums.iter().filter(|&&x| x == first).count() == 1 {
            if first > ans {
                ans = first;
            }
        }
        if nums.iter().filter(|&&x| x == last).count() == 1 {
            if last > ans {
                ans = last;
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
(define/contract (largest-integer nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ([n (length nums)])
    (cond
      [(= k n) (apply max nums)]
      [(= k 1)
       (let ([counts (make-hash)])
         (for-each (lambda (x) (hash-set! counts x (+ 1 (hash-ref counts x 0)))) nums)
         (let ([ones (filter (lambda (x) (= (hash-ref counts x) 1)) (hash-keys counts))])
           (if (null? ones) -1 (apply max ones))))]
      [else
       (let* ([first-val (list-ref nums 0)]
              [last-val (list-ref nums (- n 1))]
              [first-count (length (filter (lambda (x) (= x first-val)) nums))]
              [last-count (length (filter (lambda (x) (= x last-val)) nums))]
              [ans -1])
         (let* ([ans1 (if (= first-count 1) (max ans first-val) ans)]
                [ans2 (if (= last-count 1) (max ans1 last-val) ans1)])
           ans2))]))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
largest_integer(Nums, K) ->
  N = length(Nums),
  if
    K == N -> lists:max(Nums);
    K == 1 ->
      Counts = lists:foldl(fun(X, Acc) ->
        maps:put(X, maps:get(X, Acc, 0) + 1, Acc)
      end, #{}, Nums),
      Ones = [X || {X, Count} <- maps:to_list(Counts), Count == 1],
      case Ones of
        [] -> -1;
        _ -> lists:max(Ones)
      end;
    true ->
      First = hd(Nums),
      Last = lists:last(Nums),
      FirstCount = length([X || X <- Nums, X == First]),
      LastCount = length([X || X <- Nums, X == Last]),
      Candidates = (if FirstCount == 1 -> [First]; true -> [] end) ++
                   (if LastCount == 1 -> [Last]; true -> [] end),
      case Candidates of
        [] -> -1;
        _ -> lists:max(Candidates)
      end
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec largest_integer(nums :: [integer], k :: integer) :: integer
  def largest_integer(nums, k) do
    n = length(nums)
    cond do
      k == n ->
        Enum.max(nums)
      k == 1 ->
        ones = nums
        |> Enum.reduce(%{}, fn x, acc -> Map.update(acc, x, 1, &(&1 + 1)) end)
        |> Enum.filter(fn {_, count} -> count == 1 end)
        |> Enum.map(fn {val, _} -> val end)
        if ones == [], do: -1, else: Enum.max(ones)
      true ->
        first = List.first(nums)
        last = List.last(nums)
        first_count = Enum.count(nums, &(&1 == first))
        last_count = Enum.count(nums, &(&1 == last))
        ans = -1
        ans = if first_count == 1, do: max(ans, first), else: ans
        ans = if last_count == 1, do: max(ans, last), else: ans
        ans
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n^2). There are $n - k + 1$ subarrays of size $k$. In the worst case, $n - k + 1 \approx n/2$ and $k \approx n/2$, leading to approximately $n^2 / 4$ operations. With $n \le 50$, this results in at most 2,500 operations, making it extremely efficient.
- **Space Complexity:** O(n). We use a frequency map or an array of size 51 (since $0 \le nums[i] \le 50$) to store the number of subarrays each unique integer appears in. This requires space proportional to the number of unique elements or the maximum value in the input array.
