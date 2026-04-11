---
layout: post
title: "Minimum Distance Between Three Equal Elements II"
date: 2026-04-11 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumDistance(vector<int>& nums) {\n\
        \        int n = nums.size();\n        if (n < 3) return -1;\n\n        vector<vector<int>>\
        \ groups(n + 1);\n        for (int i = 0; i < n; ++i) {\n            groups[nums[i]].push_back(i);\n\
        \        }\n\n        int min_dist = -1;\n        for (int i = 1; i <= n; ++i)\
        \ {\n            if (groups[i].size() >= 3) {\n                for (int j =\
        \ 0; j < (int)groups[i].size() - 2; ++j) {\n                    int dist = 2\
        \ * (groups[i][j + 2] - groups[i][j]);\n                    if (min_dist ==\
        \ -1 || dist < min_dist) {\n                        min_dist = dist;\n     \
        \               }\n                }\n            }\n        }\n\n        return\
        \ min_dist;\n    }\n};"
      java: "class Solution {\n    public int minimumDistance(int[] nums) {\n      \
        \  int n = nums.length;\n        if (n < 3) return -1;\n\n        java.util.List<Integer>[]\
        \ groups = new java.util.ArrayList[n + 1];\n        for (int i = 0; i < n; i++)\
        \ {\n            if (groups[nums[i]] == null) {\n                groups[nums[i]]\
        \ = new java.util.ArrayList<>();\n            }\n            groups[nums[i]].add(i);\n\
        \        }\n\n        int minDist = -1;\n        for (int i = 1; i <= n; i++)\
        \ {\n            if (groups[i] != null && groups[i].size() >= 3) {\n       \
        \         for (int j = 0; j < groups[i].size() - 2; j++) {\n               \
        \     int dist = 2 * (groups[i].get(j + 2) - groups[i].get(j));\n          \
        \          if (minDist == -1 || dist < minDist) {\n                        minDist\
        \ = dist;\n                    }\n                }\n            }\n       \
        \ }\n\n        return minDist;\n    }\n}"
      python: "import collections\n\nclass Solution(object):\n    def minimumDistance(self,\
        \ nums):\n        \"\"\"\n        :type nums: List[int]\n        :rtype: int\n\
        \        \"\"\"\n        idx_map = collections.defaultdict(list)\n        for\
        \ i, val in enumerate(nums):\n            idx_map[val].append(i)\n\n       \
        \ min_dist = -1\n        for val in idx_map:\n            indices = idx_map[val]\n\
        \            if len(indices) >= 3:\n                for i in range(len(indices)\
        \ - 2):\n                    dist = 2 * (indices[i + 2] - indices[i])\n    \
        \                if min_dist == -1 or dist < min_dist:\n                   \
        \     min_dist = dist\n\n        return min_dist"
      python3: "class Solution:\n    def minimumDistance(self, nums: List[int]) -> int:\n\
        \        from collections import defaultdict\n        idx_map = defaultdict(list)\n\
        \        for i, val in enumerate(nums):\n            idx_map[val].append(i)\n\
        \n        min_dist = -1\n        for val in idx_map:\n            indices =\
        \ idx_map[val]\n            if len(indices) >= 3:\n                for i in\
        \ range(len(indices) - 2):\n                    dist = 2 * (indices[i + 2] -\
        \ indices[i])\n                    if min_dist == -1 or dist < min_dist:\n \
        \                       min_dist = dist\n\n        return min_dist"
      c: "#include <stdlib.h>\n\nint minimumDistance(int* nums, int numsSize) {\n  \
        \  if (numsSize < 3) return -1;\n\n    int* count = (int*)calloc(numsSize +\
        \ 1, sizeof(int));\n    for (int i = 0; i < numsSize; i++) {\n        count[nums[i]]++;\n\
        \    }\n\n    int* offset = (int*)malloc((numsSize + 2) * sizeof(int));\n  \
        \  offset[0] = 0;\n    for (int i = 0; i <= numsSize; i++) {\n        offset[i\
        \ + 1] = offset[i] + count[i];\n    }\n\n    int* curPos = (int*)malloc((numsSize\
        \ + 1) * sizeof(int));\n    for (int i = 0; i <= numsSize; i++) {\n        curPos[i]\
        \ = offset[i];\n    }\n\n    int* sorted_indices = (int*)malloc(numsSize * sizeof(int));\n\
        \    for (int i = 0; i < numsSize; i++) {\n        sorted_indices[curPos[nums[i]]++]\
        \ = i;\n    }\n\n    int min_dist = -1;\n    for (int i = 1; i <= numsSize;\
        \ i++) {\n        if (count[i] >= 3) {\n            for (int j = offset[i];\
        \ j <= offset[i + 1] - 3; j++) {\n                int dist = 2 * (sorted_indices[j\
        \ + 2] - sorted_indices[j]);\n                if (min_dist == -1 || dist < min_dist)\
        \ {\n                    min_dist = dist;\n                }\n            }\n\
        \        }\n    }\n\n    free(count);\n    free(offset);\n    free(curPos);\n\
        \    free(sorted_indices);\n\n    return min_dist;\n}"
      csharp: "public class Solution {\n    public int MinimumDistance(int[] nums) {\n\
        \        int n = nums.Length;\n        int[] last1 = new int[n + 1];\n     \
        \   int[] last2 = new int[n + 1];\n        for (int i = 0; i <= n; i++) {\n\
        \            last1[i] = -1;\n            last2[i] = -1;\n        }\n\n     \
        \   int minDist = int.MaxValue;\n        for (int i = 0; i < n; i++) {\n   \
        \         int v = nums[i];\n            if (last2[v] != -1) {\n            \
        \    int dist = 2 * (i - last2[v]);\n                if (dist < minDist) {\n\
        \                    minDist = dist;\n                }\n            }\n   \
        \         if (last1[v] != -1) {\n                last2[v] = last1[v];\n    \
        \        }\n            last1[v] = i;\n        }\n\n        return minDist ==\
        \ int.MaxValue ? -1 : minDist;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minimumDistance\
        \ = function(nums) {\n    const n = nums.length;\n    const last1 = new Int32Array(n\
        \ + 1).fill(-1);\n    const last2 = new Int32Array(n + 1).fill(-1);\n    let\
        \ minDist = Infinity;\n\n    for (let i = 0; i < n; i++) {\n        const v\
        \ = nums[i];\n        if (last2[v] !== -1) {\n            const dist = 2 * (i\
        \ - last2[v]);\n            if (dist < minDist) {\n                minDist =\
        \ dist;\n            }\n        }\n        if (last1[v] !== -1) {\n        \
        \    last2[v] = last1[v];\n        }\n        last1[v] = i;\n    }\n\n    return\
        \ minDist === Infinity ? -1 : minDist;\n};"
      typescript: "function minimumDistance(nums: number[]): number {\n    const n =\
        \ nums.length;\n    const last1 = new Int32Array(n + 1).fill(-1);\n    const\
        \ last2 = new Int32Array(n + 1).fill(-1);\n    let minDist: number = Infinity;\n\
        \n    for (let i = 0; i < n; i++) {\n        const v = nums[i];\n        if\
        \ (last2[v] !== -1) {\n            const dist = 2 * (i - last2[v]);\n      \
        \      if (dist < minDist) {\n                minDist = dist;\n            }\n\
        \        }\n        if (last1[v] !== -1) {\n            last2[v] = last1[v];\n\
        \        }\n        last1[v] = i;\n    }\n\n    return minDist === Infinity\
        \ ? -1 : minDist;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function minimumDistance($nums) {\n        $n = count($nums);\n\
        \        $last1 = array_fill(0, $n + 1, -1);\n        $last2 = array_fill(0,\
        \ $n + 1, -1);\n        $minDist = PHP_INT_MAX;\n\n        for ($i = 0; $i <\
        \ $n; $i++) {\n            $v = $nums[$i];\n            if ($last2[$v] !== -1)\
        \ {\n                $dist = 2 * ($i - $last2[$v]);\n                if ($dist\
        \ < $minDist) {\n                    $minDist = $dist;\n                }\n\
        \            }\n            if ($last1[$v] !== -1) {\n                $last2[$v]\
        \ = $last1[$v];\n            }\n            $last1[$v] = $i;\n        }\n\n\
        \        return $minDist === PHP_INT_MAX ? -1 : $minDist;\n    }\n}"
      swift: "class Solution {\n    func minimumDistance(_ nums: [Int]) -> Int {\n \
        \       let n = nums.count\n        var last1 = [Int](repeating: -1, count:\
        \ n + 1)\n        var last2 = [Int](repeating: -1, count: n + 1)\n        var\
        \ minDist = Int.max\n\n        for i in 0..<n {\n            let v = nums[i]\n\
        \            if last2[v] != -1 {\n                let dist = 2 * (i - last2[v])\n\
        \                if dist < minDist {\n                    minDist = dist\n \
        \               }\n            }\n            if last1[v] != -1 {\n        \
        \        last2[v] = last1[v]\n            }\n            last1[v] = i\n    \
        \    }\n\n        return minDist == Int.max ? -1 : minDist\n    }\n}"
      kotlin: "class Solution {\n    fun minimumDistance(nums: IntArray): Int {\n  \
        \      val n = nums.size\n        val last = IntArray(n + 1) { -1 }\n      \
        \  val secondLast = IntArray(n + 1) { -1 }\n        var minDiff = Int.MAX_VALUE\n\
        \        for (i in 0 until n) {\n            val v = nums[i]\n            if\
        \ (secondLast[v] != -1) {\n                val diff = i - secondLast[v]\n  \
        \              if (diff < minDiff) {\n                    minDiff = diff\n \
        \               }\n            }\n            secondLast[v] = last[v]\n    \
        \        last[v] = i\n        }\n        return if (minDiff == Int.MAX_VALUE)\
        \ -1 else 2 * minDiff\n    }\n}"
      dart: "class Solution {\n  int minimumDistance(List<int> nums) {\n    int n =\
        \ nums.length;\n    List<int> last = List<int>.filled(n + 1, -1);\n    List<int>\
        \ secondLast = List<int>.filled(n + 1, -1);\n    int minDiff = n + 1;\n    for\
        \ (int i = 0; i < n; i++) {\n      int v = nums[i];\n      if (secondLast[v]\
        \ != -1) {\n        int diff = i - secondLast[v];\n        if (diff < minDiff)\
        \ {\n          minDiff = diff;\n        }\n      }\n      secondLast[v] = last[v];\n\
        \      last[v] = i;\n    }\n    return minDiff == n + 1 ? -1 : 2 * minDiff;\n\
        \  }\n}"
      go: "func minimumDistance(nums []int) int {\n    n := len(nums)\n    last := make([]int,\
        \ n+1)\n    secondLast := make([]int, n+1)\n    for i := 0; i <= n; i++ {\n\
        \        last[i] = -1\n        secondLast[i] = -1\n    }\n    minDiff := n +\
        \ 1\n    for i, v := range nums {\n        if secondLast[v] != -1 {\n      \
        \      diff := i - secondLast[v]\n            if diff < minDiff {\n        \
        \        minDiff = diff\n            }\n        }\n        secondLast[v] = last[v]\n\
        \        last[v] = i\n    }\n    if minDiff == n+1 {\n        return -1\n  \
        \  }\n    return 2 * minDiff\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef minimum_distance(nums)\n\
        \  n = nums.length\n  last = Array.new(n + 1, -1)\n  second_last = Array.new(n\
        \ + 1, -1)\n  min_diff = n + 1\n  nums.each_with_index do |v, i|\n    if second_last[v]\
        \ != -1\n      diff = i - second_last[v]\n      min_diff = diff if diff < min_diff\n\
        \    end\n    second_last[v] = last[v]\n    last[v] = i\n  end\n  min_diff ==\
        \ n + 1 ? -1 : 2 * min_diff\nend"
      scala: "object Solution {\n    def minimumDistance(nums: Array[Int]): Int = {\n\
        \        val n = nums.length\n        val last = Array.fill(n + 1)(-1)\n   \
        \     val secondLast = Array.fill(n + 1)(-1)\n        var minDiff = Int.MaxValue\n\
        \        var i = 0\n        while (i < n) {\n            val v = nums(i)\n \
        \           if (secondLast(v) != -1) {\n                val diff = i - secondLast(v)\n\
        \                if (diff < minDiff) {\n                    minDiff = diff\n\
        \                }\n            }\n            secondLast(v) = last(v)\n   \
        \         last(v) = i\n            i += 1\n        }\n        if (minDiff ==\
        \ Int.MaxValue) -1 else 2 * minDiff\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_distance(nums: Vec<i32>) -> i32 {\n\
        \        let n = nums.len();\n        let mut indices_map: Vec<Vec<i32>> = vec![Vec::new();\
        \ n + 1];\n        for (idx, &num) in nums.iter().enumerate() {\n          \
        \  indices_map[num as usize].push(idx as i32);\n        }\n\n        let mut\
        \ min_dist = -1;\n        for indices in indices_map {\n            if indices.len()\
        \ >= 3 {\n                for i in 0..indices.len() - 2 {\n                \
        \    let dist = 2 * (indices[i + 2] - indices[i]);\n                    if min_dist\
        \ == -1 || dist < min_dist {\n                        min_dist = dist;\n   \
        \                 }\n                }\n            }\n        }\n        min_dist\n\
        \    }\n}"
      racket: "(define/contract (minimum-distance nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let ([h (make-hasheq)])\n    (for ([x (in-list nums)]\
        \ [i (in-naturals)])\n      (hash-update! h x (lambda (v) (cons i v)) '()))\n\
        \    (let ([ans (for/fold ([min-all -1])\n                         ([lst (in-hash-values\
        \ h)])\n                 (let ([min-local \n                        (let loop\
        \ ([l lst] [m -1])\n                          (match l\n                   \
        \         [(list-rest i j k rest)\n                             (let* ([dist\
        \ (* 2 (- i k))]\n                                    [next-m (if (or (= m -1)\
        \ (< dist m)) dist m)])\n                               (loop (cdr l) next-m))]\n\
        \                            [_ m]))])\n                   (if (and (not (=\
        \ min-local -1)) \n                            (or (= min-all -1) (< min-local\
        \ min-all)))\n                       min-local\n                       min-all)))])\n\
        \      ans)))"
      erlang: "-spec minimum_distance(Nums :: [integer()]) -> integer().\nminimum_distance(Nums)\
        \ ->\n    Map = build_map(Nums, 0, #{}),\n    find_min(maps:values(Map), -1).\n\
        \nbuild_map([], _, Map) -> Map;\nbuild_map([H | T], Idx, Map) ->\n    NewMap\
        \ = maps:update_with(H, fun(V) -> [Idx | V] end, [Idx], Map),\n    build_map(T,\
        \ Idx + 1, NewMap).\n\nfind_min([], Min) -> Min;\nfind_min([H | T], Min) ->\n\
        \    case H of\n        [I, J, K | Rest] ->\n            LocalMin = calc_local_min([I,\
        \ J, K | Rest], -1),\n            NewMin = if\n                Min == -1 ->\
        \ LocalMin;\n                LocalMin < Min -> LocalMin;\n                true\
        \ -> Min\n            end,\n            find_min(T, NewMin);\n        _ ->\n\
        \            find_min(T, Min)\n    end.\n\ncalc_local_min([I, J, K | T], CurrentMin)\
        \ ->\n    Dist = 2 * (I - K),\n    NewMin = if\n        CurrentMin == -1 orelse\
        \ Dist < CurrentMin -> Dist;\n        true -> CurrentMin\n    end,\n    calc_local_min([J,\
        \ K | T], NewMin);\ncalc_local_min(_, CurrentMin) -> CurrentMin."
      elixir: "defmodule Solution do\n  @spec minimum_distance(nums :: [integer]) ::\
        \ integer\n  def minimum_distance(nums) do\n    nums\n    |> Enum.with_index()\n\
        \    |> Enum.reduce(%{}, fn {val, idx}, acc ->\n      Map.update(acc, val, [idx],\
        \ &[idx | &1])\n    end)\n    |> Map.values()\n    |> Enum.reduce(-1, fn indices,\
        \ acc_min ->\n      case indices do\n        [i, j, k | rest] ->\n         \
        \ local_min = calc_local_min([i, j, k | rest], -1)\n          if acc_min ==\
        \ -1 or local_min < acc_min, do: local_min, else: acc_min\n        _ ->\n  \
        \        acc_min\n      end\n    end)\n  end\n\n  defp calc_local_min([i, j,\
        \ k | rest], current_min) do\n    dist = 2 * (i - k)\n    new_min = if current_min\
        \ == -1 or dist < current_min, do: dist, else: current_min\n    calc_local_min([j,\
        \ k | rest], new_min)\n  end\n\n  defp calc_local_min(_, current_min) do\n \
        \   current_min\n  end\nend"
    approach: "The distance formula abs(i - j) + abs(j - k) + abs(k - i) for a good\
      \ tuple (i, j, k) simplifies to 2 * (max(i, j, k) - min(i, j, k)). This reduction\
      \ indicates that the total distance depends only on the span between the smallest\
      \ and largest indices of the triple, while the middle index must simply lie between\
      \ them. Consequently, to minimize this distance for any value that appears at\
      \ least three times, we must find two indices of that value as close together\
      \ as possible while ensuring at least one additional index of the same value exists\
      \ between them. \n\nThis is achieved by grouping all indices of each unique value.\
      \ Since we traverse the input array linearly, the lists of indices for each value\
      \ are naturally sorted. We then iterate through each value's list of indices and\
      \ examine every window of three consecutive indices (idx[i], idx[i+1], idx[i+2]).\
      \ The distance for each such window is 2 * (idx[i+2] - idx[i]). By tracking the\
      \ minimum distance found across all such triples for all values, we find the global\
      \ minimum. If no value appears at least three times, we return -1."
    time_complexity: O(N), where N is the length of the input array. We traverse the
      array once to group the indices, which takes O(N) time. Then, we iterate through
      the list of indices for each unique value. Since every index is processed exactly
      once during this phase, the total time spent is O(N).
    space_complexity: O(N), where N is the length of the input array. We use auxiliary
      storage to group indices for each unique value. In the worst case, every index
      is stored once in a mapping or an array of lists, leading to linear space complexity.
    elapsed_time: 247.8946669101715
    model: gemini-3-flash-preview
    generated_at: '2026-04-11 01:33:54 '
---

## Problem #3741: Minimum Distance Between Three Equal Elements II

**Difficulty:** Medium

**Topics:** Array, Hash Table

## Problem Description

<p>You are given an integer array <code>nums</code>.</p>

<p>A tuple <code>(i, j, k)</code> of 3 <strong>distinct</strong> indices is <strong>good</strong> if <code>nums[i] == nums[j] == nums[k]</code>.</p>

<p>The <strong>distance</strong> of a <strong>good</strong> tuple is <code>abs(i - j) + abs(j - k) + abs(k - i)</code>, where <code>abs(x)</code> denotes the <strong>absolute value</strong> of <code>x</code>.</p>

<p>Return an integer denoting the <strong>minimum</strong> possible <strong>distance</strong> of a <strong>good</strong> tuple. If no <strong>good</strong> tuples exist, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,1,1,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>The minimum distance is achieved by the good tuple <code>(0, 2, 3)</code>.</p>

<p><code>(0, 2, 3)</code> is a good tuple because <code>nums[0] == nums[2] == nums[3] == 1</code>. Its distance is <code>abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,2,3,2,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<p>The minimum distance is achieved by the good tuple <code>(2, 4, 6)</code>.</p>

<p><code>(2, 4, 6)</code> is a good tuple because <code>nums[2] == nums[4] == nums[6] == 2</code>. Its distance is <code>abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no good tuples. Therefore, the answer is -1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
</ul>


## Hints

1. The distance formula `abs(i - j) + abs(j - k) + abs(k - i)` simplifies to `2 * (max(i, j, k) - min(i, j, k))`.

2. Group the indices for each unique number. For a number to form a good tuple, it must appear at least 3 times.

3. For each number that appears at least 3 times, we want to find three of its indices `p < q < r` that minimize `r - p`. This is achieved by considering every three consecutive indices in the sorted list of indices.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The distance formula abs(i - j) + abs(j - k) + abs(k - i) for a good tuple (i, j, k) simplifies to 2 * (max(i, j, k) - min(i, j, k)). This reduction indicates that the total distance depends only on the span between the smallest and largest indices of the triple, while the middle index must simply lie between them. Consequently, to minimize this distance for any value that appears at least three times, we must find two indices of that value as close together as possible while ensuring at least one additional index of the same value exists between them. 

This is achieved by grouping all indices of each unique value. Since we traverse the input array linearly, the lists of indices for each value are naturally sorted. We then iterate through each value's list of indices and examine every window of three consecutive indices (idx[i], idx[i+1], idx[i+2]). The distance for each such window is 2 * (idx[i+2] - idx[i]). By tracking the minimum distance found across all such triples for all values, we find the global minimum. If no value appears at least three times, we return -1.

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
    int minimumDistance(vector<int>& nums) {
        int n = nums.size();
        if (n < 3) return -1;

        vector<vector<int>> groups(n + 1);
        for (int i = 0; i < n; ++i) {
            groups[nums[i]].push_back(i);
        }

        int min_dist = -1;
        for (int i = 1; i <= n; ++i) {
            if (groups[i].size() >= 3) {
                for (int j = 0; j < (int)groups[i].size() - 2; ++j) {
                    int dist = 2 * (groups[i][j + 2] - groups[i][j]);
                    if (min_dist == -1 || dist < min_dist) {
                        min_dist = dist;
                    }
                }
            }
        }

        return min_dist;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minimumDistance(int[] nums) {
        int n = nums.length;
        if (n < 3) return -1;

        java.util.List<Integer>[] groups = new java.util.ArrayList[n + 1];
        for (int i = 0; i < n; i++) {
            if (groups[nums[i]] == null) {
                groups[nums[i]] = new java.util.ArrayList<>();
            }
            groups[nums[i]].add(i);
        }

        int minDist = -1;
        for (int i = 1; i <= n; i++) {
            if (groups[i] != null && groups[i].size() >= 3) {
                for (int j = 0; j < groups[i].size() - 2; j++) {
                    int dist = 2 * (groups[i].get(j + 2) - groups[i].get(j));
                    if (minDist == -1 || dist < minDist) {
                        minDist = dist;
                    }
                }
            }
        }

        return minDist;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import collections

class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx_map = collections.defaultdict(list)
        for i, val in enumerate(nums):
            idx_map[val].append(i)

        min_dist = -1
        for val in idx_map:
            indices = idx_map[val]
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    dist = 2 * (indices[i + 2] - indices[i])
                    if min_dist == -1 or dist < min_dist:
                        min_dist = dist

        return min_dist
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        from collections import defaultdict
        idx_map = defaultdict(list)
        for i, val in enumerate(nums):
            idx_map[val].append(i)

        min_dist = -1
        for val in idx_map:
            indices = idx_map[val]
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    dist = 2 * (indices[i + 2] - indices[i])
                    if min_dist == -1 or dist < min_dist:
                        min_dist = dist

        return min_dist
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int minimumDistance(int* nums, int numsSize) {
    if (numsSize < 3) return -1;

    int* count = (int*)calloc(numsSize + 1, sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        count[nums[i]]++;
    }

    int* offset = (int*)malloc((numsSize + 2) * sizeof(int));
    offset[0] = 0;
    for (int i = 0; i <= numsSize; i++) {
        offset[i + 1] = offset[i] + count[i];
    }

    int* curPos = (int*)malloc((numsSize + 1) * sizeof(int));
    for (int i = 0; i <= numsSize; i++) {
        curPos[i] = offset[i];
    }

    int* sorted_indices = (int*)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        sorted_indices[curPos[nums[i]]++] = i;
    }

    int min_dist = -1;
    for (int i = 1; i <= numsSize; i++) {
        if (count[i] >= 3) {
            for (int j = offset[i]; j <= offset[i + 1] - 3; j++) {
                int dist = 2 * (sorted_indices[j + 2] - sorted_indices[j]);
                if (min_dist == -1 || dist < min_dist) {
                    min_dist = dist;
                }
            }
        }
    }

    free(count);
    free(offset);
    free(curPos);
    free(sorted_indices);

    return min_dist;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinimumDistance(int[] nums) {
        int n = nums.Length;
        int[] last1 = new int[n + 1];
        int[] last2 = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            last1[i] = -1;
            last2[i] = -1;
        }

        int minDist = int.MaxValue;
        for (int i = 0; i < n; i++) {
            int v = nums[i];
            if (last2[v] != -1) {
                int dist = 2 * (i - last2[v]);
                if (dist < minDist) {
                    minDist = dist;
                }
            }
            if (last1[v] != -1) {
                last2[v] = last1[v];
            }
            last1[v] = i;
        }

        return minDist == int.MaxValue ? -1 : minDist;
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
var minimumDistance = function(nums) {
    const n = nums.length;
    const last1 = new Int32Array(n + 1).fill(-1);
    const last2 = new Int32Array(n + 1).fill(-1);
    let minDist = Infinity;

    for (let i = 0; i < n; i++) {
        const v = nums[i];
        if (last2[v] !== -1) {
            const dist = 2 * (i - last2[v]);
            if (dist < minDist) {
                minDist = dist;
            }
        }
        if (last1[v] !== -1) {
            last2[v] = last1[v];
        }
        last1[v] = i;
    }

    return minDist === Infinity ? -1 : minDist;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumDistance(nums: number[]): number {
    const n = nums.length;
    const last1 = new Int32Array(n + 1).fill(-1);
    const last2 = new Int32Array(n + 1).fill(-1);
    let minDist: number = Infinity;

    for (let i = 0; i < n; i++) {
        const v = nums[i];
        if (last2[v] !== -1) {
            const dist = 2 * (i - last2[v]);
            if (dist < minDist) {
                minDist = dist;
            }
        }
        if (last1[v] !== -1) {
            last2[v] = last1[v];
        }
        last1[v] = i;
    }

    return minDist === Infinity ? -1 : minDist;
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
    function minimumDistance($nums) {
        $n = count($nums);
        $last1 = array_fill(0, $n + 1, -1);
        $last2 = array_fill(0, $n + 1, -1);
        $minDist = PHP_INT_MAX;

        for ($i = 0; $i < $n; $i++) {
            $v = $nums[$i];
            if ($last2[$v] !== -1) {
                $dist = 2 * ($i - $last2[$v]);
                if ($dist < $minDist) {
                    $minDist = $dist;
                }
            }
            if ($last1[$v] !== -1) {
                $last2[$v] = $last1[$v];
            }
            $last1[$v] = $i;
        }

        return $minDist === PHP_INT_MAX ? -1 : $minDist;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumDistance(_ nums: [Int]) -> Int {
        let n = nums.count
        var last1 = [Int](repeating: -1, count: n + 1)
        var last2 = [Int](repeating: -1, count: n + 1)
        var minDist = Int.max

        for i in 0..<n {
            let v = nums[i]
            if last2[v] != -1 {
                let dist = 2 * (i - last2[v])
                if dist < minDist {
                    minDist = dist
                }
            }
            if last1[v] != -1 {
                last2[v] = last1[v]
            }
            last1[v] = i
        }

        return minDist == Int.max ? -1 : minDist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumDistance(nums: IntArray): Int {
        val n = nums.size
        val last = IntArray(n + 1) { -1 }
        val secondLast = IntArray(n + 1) { -1 }
        var minDiff = Int.MAX_VALUE
        for (i in 0 until n) {
            val v = nums[i]
            if (secondLast[v] != -1) {
                val diff = i - secondLast[v]
                if (diff < minDiff) {
                    minDiff = diff
                }
            }
            secondLast[v] = last[v]
            last[v] = i
        }
        return if (minDiff == Int.MAX_VALUE) -1 else 2 * minDiff
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumDistance(List<int> nums) {
    int n = nums.length;
    List<int> last = List<int>.filled(n + 1, -1);
    List<int> secondLast = List<int>.filled(n + 1, -1);
    int minDiff = n + 1;
    for (int i = 0; i < n; i++) {
      int v = nums[i];
      if (secondLast[v] != -1) {
        int diff = i - secondLast[v];
        if (diff < minDiff) {
          minDiff = diff;
        }
      }
      secondLast[v] = last[v];
      last[v] = i;
    }
    return minDiff == n + 1 ? -1 : 2 * minDiff;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumDistance(nums []int) int {
    n := len(nums)
    last := make([]int, n+1)
    secondLast := make([]int, n+1)
    for i := 0; i <= n; i++ {
        last[i] = -1
        secondLast[i] = -1
    }
    minDiff := n + 1
    for i, v := range nums {
        if secondLast[v] != -1 {
            diff := i - secondLast[v]
            if diff < minDiff {
                minDiff = diff
            }
        }
        secondLast[v] = last[v]
        last[v] = i
    }
    if minDiff == n+1 {
        return -1
    }
    return 2 * minDiff
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def minimum_distance(nums)
  n = nums.length
  last = Array.new(n + 1, -1)
  second_last = Array.new(n + 1, -1)
  min_diff = n + 1
  nums.each_with_index do |v, i|
    if second_last[v] != -1
      diff = i - second_last[v]
      min_diff = diff if diff < min_diff
    end
    second_last[v] = last[v]
    last[v] = i
  end
  min_diff == n + 1 ? -1 : 2 * min_diff
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumDistance(nums: Array[Int]): Int = {
        val n = nums.length
        val last = Array.fill(n + 1)(-1)
        val secondLast = Array.fill(n + 1)(-1)
        var minDiff = Int.MaxValue
        var i = 0
        while (i < n) {
            val v = nums(i)
            if (secondLast(v) != -1) {
                val diff = i - secondLast(v)
                if (diff < minDiff) {
                    minDiff = diff
                }
            }
            secondLast(v) = last(v)
            last(v) = i
            i += 1
        }
        if (minDiff == Int.MaxValue) -1 else 2 * minDiff
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_distance(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut indices_map: Vec<Vec<i32>> = vec![Vec::new(); n + 1];
        for (idx, &num) in nums.iter().enumerate() {
            indices_map[num as usize].push(idx as i32);
        }

        let mut min_dist = -1;
        for indices in indices_map {
            if indices.len() >= 3 {
                for i in 0..indices.len() - 2 {
                    let dist = 2 * (indices[i + 2] - indices[i]);
                    if min_dist == -1 || dist < min_dist {
                        min_dist = dist;
                    }
                }
            }
        }
        min_dist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-distance nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ([h (make-hasheq)])
    (for ([x (in-list nums)] [i (in-naturals)])
      (hash-update! h x (lambda (v) (cons i v)) '()))
    (let ([ans (for/fold ([min-all -1])
                         ([lst (in-hash-values h)])
                 (let ([min-local 
                        (let loop ([l lst] [m -1])
                          (match l
                            [(list-rest i j k rest)
                             (let* ([dist (* 2 (- i k))]
                                    [next-m (if (or (= m -1) (< dist m)) dist m)])
                               (loop (cdr l) next-m))]
                            [_ m]))])
                   (if (and (not (= min-local -1)) 
                            (or (= min-all -1) (< min-local min-all)))
                       min-local
                       min-all)))])
      ans)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_distance(Nums :: [integer()]) -> integer().
minimum_distance(Nums) ->
    Map = build_map(Nums, 0, #{}),
    find_min(maps:values(Map), -1).

build_map([], _, Map) -> Map;
build_map([H | T], Idx, Map) ->
    NewMap = maps:update_with(H, fun(V) -> [Idx | V] end, [Idx], Map),
    build_map(T, Idx + 1, NewMap).

find_min([], Min) -> Min;
find_min([H | T], Min) ->
    case H of
        [I, J, K | Rest] ->
            LocalMin = calc_local_min([I, J, K | Rest], -1),
            NewMin = if
                Min == -1 -> LocalMin;
                LocalMin < Min -> LocalMin;
                true -> Min
            end,
            find_min(T, NewMin);
        _ ->
            find_min(T, Min)
    end.

calc_local_min([I, J, K | T], CurrentMin) ->
    Dist = 2 * (I - K),
    NewMin = if
        CurrentMin == -1 orelse Dist < CurrentMin -> Dist;
        true -> CurrentMin
    end,
    calc_local_min([J, K | T], NewMin);
calc_local_min(_, CurrentMin) -> CurrentMin.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_distance(nums :: [integer]) :: integer
  def minimum_distance(nums) do
    nums
    |> Enum.with_index()
    |> Enum.reduce(%{}, fn {val, idx}, acc ->
      Map.update(acc, val, [idx], &[idx | &1])
    end)
    |> Map.values()
    |> Enum.reduce(-1, fn indices, acc_min ->
      case indices do
        [i, j, k | rest] ->
          local_min = calc_local_min([i, j, k | rest], -1)
          if acc_min == -1 or local_min < acc_min, do: local_min, else: acc_min
        _ ->
          acc_min
      end
    end)
  end

  defp calc_local_min([i, j, k | rest], current_min) do
    dist = 2 * (i - k)
    new_min = if current_min == -1 or dist < current_min, do: dist, else: current_min
    calc_local_min([j, k | rest], new_min)
  end

  defp calc_local_min(_, current_min) do
    current_min
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N), where N is the length of the input array. We traverse the array once to group the indices, which takes O(N) time. Then, we iterate through the list of indices for each unique value. Since every index is processed exactly once during this phase, the total time spent is O(N).
- **Space Complexity:** O(N), where N is the length of the input array. We use auxiliary storage to group indices for each unique value. In the worst case, every index is stored once in a mapping or an array of lists, leading to linear space complexity.
