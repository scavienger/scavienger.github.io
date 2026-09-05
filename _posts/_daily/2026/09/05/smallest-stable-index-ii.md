---
layout: post
title: "Smallest Stable Index II"
date: 2026-09-05 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/smallest-stable-index-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int firstStableIndex(vector<int>& nums, int\
        \ k) {\n        int n = nums.size();\n        if (n == 0) return -1;\n\n   \
        \     vector<int> suffMin(n);\n        suffMin[n - 1] = nums[n - 1];\n     \
        \   for (int i = n - 2; i >= 0; --i) {\n            suffMin[i] = min(nums[i],\
        \ suffMin[i + 1]);\n        }\n\n        int prefMax = nums[0];\n        for\
        \ (int i = 0; i < n; ++i) {\n            if (nums[i] > prefMax) prefMax = nums[i];\n\
        \            if ((long long)prefMax - suffMin[i] <= (long long)k) {\n      \
        \          return i;\n            }\n        }\n\n        return -1;\n    }\n\
        };"
      java: "class Solution {\n    public int firstStableIndex(int[] nums, int k) {\n\
        \        int n = nums.length;\n        if (n == 0) return -1;\n\n        int[]\
        \ suffMin = new int[n];\n        suffMin[n - 1] = nums[n - 1];\n        for\
        \ (int i = n - 2; i >= 0; i--) {\n            suffMin[i] = Math.min(nums[i],\
        \ suffMin[i + 1]);\n        }\n\n        int prefMax = nums[0];\n        for\
        \ (int i = 0; i < n; i++) {\n            prefMax = Math.max(prefMax, nums[i]);\n\
        \            if ((long) prefMax - suffMin[i] <= (long) k) {\n              \
        \  return i;\n            }\n        }\n\n        return -1;\n    }\n}"
      python: "class Solution(object):\n    def firstStableIndex(self, nums, k):\n \
        \       \"\"\"\n        :type nums: List[int]\n        :type k: int\n      \
        \  :rtype: int\n        \"\"\"\n        n = len(nums)\n        if n == 0: return\
        \ -1\n\n        suffMin = [0] * n\n        suffMin[n - 1] = nums[n - 1]\n  \
        \      for i in range(n - 2, -1, -1):\n            if nums[i] < suffMin[i +\
        \ 1]:\n                suffMin[i] = nums[i]\n            else:\n           \
        \     suffMin[i] = suffMin[i + 1]\n\n        prefMax = -float('inf')\n     \
        \   for i in range(n):\n            if nums[i] > prefMax:\n                prefMax\
        \ = nums[i]\n            if prefMax - suffMin[i] <= k:\n                return\
        \ i\n\n        return -1"
      python3: "class Solution:\n    def firstStableIndex(self, nums: list[int], k:\
        \ int) -> int:\n        n = len(nums)\n        if n == 0: return -1\n\n    \
        \    suffMin = [0] * n\n        suffMin[n - 1] = nums[n - 1]\n        for i\
        \ in range(n - 2, -1, -1):\n            suffMin[i] = min(nums[i], suffMin[i\
        \ + 1])\n\n        prefMax = -float('inf')\n        for i in range(n):\n   \
        \         prefMax = max(prefMax, nums[i])\n            if prefMax - suffMin[i]\
        \ <= k:\n                return i\n\n        return -1"
      c: "int firstStableIndex(int* nums, int numsSize, int k) {\n    if (numsSize ==\
        \ 0) return -1;\n\n    int* suffMin = (int*)malloc(numsSize * sizeof(int));\n\
        \    suffMin[numsSize - 1] = nums[numsSize - 1];\n    for (int i = numsSize\
        \ - 2; i >= 0; --i) {\n        if (nums[i] < suffMin[i + 1]) {\n           \
        \ suffMin[i] = nums[i];\n        } else {\n            suffMin[i] = suffMin[i\
        \ + 1];\n        }\n    }\n\n    int prefMax = nums[0];\n    int result = -1;\n\
        \    for (int i = 0; i < numsSize; ++i) {\n        if (nums[i] > prefMax) prefMax\
        \ = nums[i];\n        if ((long long)prefMax - suffMin[i] <= (long long)k) {\n\
        \            result = i;\n            break;\n        }\n    }\n\n    free(suffMin);\n\
        \    return result;\n}"
      csharp: "public class Solution {\n    public int FirstStableIndex(int[] nums,\
        \ int k) {\n        int n = nums.Length;\n        if (n == 0) return -1;\n\n\
        \        int[] suffMin = new int[n];\n        suffMin[n - 1] = nums[n - 1];\n\
        \        for (int i = n - 2; i >= 0; i--) {\n            suffMin[i] = Math.Min(suffMin[i\
        \ + 1], nums[i]);\n        }\n\n        int currentPrefMax = nums[0];\n    \
        \    for (int i = 0; i < n; i++) {\n            if (nums[i] > currentPrefMax)\
        \ {\n                currentPrefMax = nums[i];\n            }\n            if\
        \ (currentPrefMax - suffMin[i] <= k) {\n                return i;\n        \
        \    }\n        }\n\n        return -1;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @return\
        \ {number}\n */\nvar firstStableIndex = function(nums, k) {\n    const n = nums.length;\n\
        \    if (n === 0) return -1;\n\n    const suffMin = new Int32Array(n);\n   \
        \ suffMin[n - 1] = nums[n - 1];\n    for (let i = n - 2; i >= 0; i--) {\n  \
        \      suffMin[i] = Math.min(suffMin[i + 1], nums[i]);\n    }\n\n    let currentPrefMax\
        \ = nums[0];\n    for (let i = 0; i < n; i++) {\n        currentPrefMax = Math.max(currentPrefMax,\
        \ nums[i]);\n        if (currentPrefMax - suffMin[i] <= k) {\n            return\
        \ i;\n        }\n    }\n\n    return -1;\n};"
      typescript: "function firstStableIndex(nums: number[], k: number): number {\n\
        \    const n: number = nums.length;\n    if (n === 0) return -1;\n\n    const\
        \ suffMin: Int32Array = new Int32Array(n);\n    suffMin[n - 1] = nums[n - 1];\n\
        \    for (let i = n - 2; i >= 0; i--) {\n        suffMin[i] = Math.min(suffMin[i\
        \ + 1], nums[i]);\n    }\n\n    let currentPrefMax: number = nums[0];\n    for\
        \ (let i = 0; i < n; i++) {\n        currentPrefMax = Math.max(currentPrefMax,\
        \ nums[i]);\n        if (currentPrefMax - suffMin[i] <= k) {\n            return\
        \ i;\n        }\n    }\n\n    return -1;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $k\n     * @return Integer\n     */\n    function firstStableIndex($nums,\
        \ $k) {\n        $n = count($nums);\n        if ($n === 0) return -1;\n\n  \
        \      $suffMin = array_fill(0, $n, 0);\n        $suffMin[$n - 1] = $nums[$n\
        \ - 1];\n        for ($i = $n - 2; $i >= 0; $i--) {\n            $suffMin[$i]\
        \ = min($suffMin[$i + 1], $nums[$i]);\n        }\n\n        $currentPrefMax\
        \ = $nums[0];\n        for ($i = 0; $i < $n; $i++) {\n            if ($nums[$i]\
        \ > $currentPrefMax) {\n                $currentPrefMax = $nums[$i];\n     \
        \       }\n            if ($currentPrefMax - $suffMin[$i] <= $k) {\n       \
        \         return $i;\n            }\n        }\n\n        return -1;\n    }\n\
        }"
      swift: "class Solution {\n    func firstStableIndex(_ nums: [Int], _ k: Int) ->\
        \ Int {\n        let n = nums.count\n        if n == 0 { return -1 }\n\n   \
        \     var suffMin = Array(repeating: 0, count: n)\n        suffMin[n - 1] =\
        \ nums[n - 1]\n        if n > 1 {\n            for i in (0..<n - 1).reversed()\
        \ {\n                suffMin[i] = min(suffMin[i + 1], nums[i])\n           \
        \ }\n        }\n\n        var currentPrefMax = nums[0]\n        for i in 0..<n\
        \ {\n            currentPrefMax = max(currentPrefMax, nums[i])\n           \
        \ if currentPrefMax - suffMin[i] <= k {\n                return i\n        \
        \    }\n        }\n\n        return -1\n    }\n}"
      kotlin: "class Solution {\n    fun firstStableIndex(nums: IntArray, k: Int): Int\
        \ {\n        val n = nums.size\n        if (n == 0) return -1\n        val prefMax\
        \ = IntArray(n)\n        val suffMin = IntArray(n)\n        prefMax[0] = nums[0]\n\
        \        for (i in 1 until n) {\n            prefMax[i] = if (nums[i] > prefMax[i\
        \ - 1]) nums[i] else prefMax[i - 1]\n        }\n        suffMin[n - 1] = nums[n\
        \ - 1]\n        for (i in n - 2 downTo 0) {\n            suffMin[i] = if (nums[i]\
        \ < suffMin[i + 1]) nums[i] else suffMin[i + 1]\n        }\n        for (i in\
        \ 0 until n) {\n            if (prefMax[i] - suffMin[i] <= k) {\n          \
        \      return i\n            }\n        }\n        return -1\n    }\n}"
      dart: "class Solution {\n  int firstStableIndex(List<int> nums, int k) {\n   \
        \ int n = nums.length;\n    if (n == 0) return -1;\n    List<int> prefMax =\
        \ List.filled(n, 0);\n    List<int> suffMin = List.filled(n, 0);\n    prefMax[0]\
        \ = nums[0];\n    for (int i = 1; i < n; i++) {\n      prefMax[i] = nums[i]\
        \ > prefMax[i - 1] ? nums[i] : prefMax[i - 1];\n    }\n    suffMin[n - 1] =\
        \ nums[n - 1];\n    for (int i = n - 2; i >= 0; i--) {\n      suffMin[i] = nums[i]\
        \ < suffMin[i + 1] ? nums[i] : suffMin[i + 1];\n    }\n    for (int i = 0; i\
        \ < n; i++) {\n      if (prefMax[i] - suffMin[i] <= k) {\n        return i;\n\
        \      }\n    }\n    return -1;\n  }\n}"
      go: "func firstStableIndex(nums []int, k int) int {\n    n := len(nums)\n    if\
        \ n == 0 {\n        return -1\n    }\n    prefMax := make([]int, n)\n    suffMin\
        \ := make([]int, n)\n    prefMax[0] = nums[0]\n    for i := 1; i < n; i++ {\n\
        \        if nums[i] > prefMax[i-1] {\n            prefMax[i] = nums[i]\n   \
        \     } else {\n            prefMax[i] = prefMax[i-1]\n        }\n    }\n  \
        \  suffMin[n-1] = nums[n-1]\n    for i := n - 2; i >= 0; i-- {\n        if nums[i]\
        \ < suffMin[i+1] {\n            suffMin[i] = nums[i]\n        } else {\n   \
        \         suffMin[i] = suffMin[i+1]\n        }\n    }\n    for i := 0; i < n;\
        \ i++ {\n        if prefMax[i]-suffMin[i] <= k {\n            return i\n   \
        \     }\n    }\n    return -1\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer} k\n# @return {Integer}\n\
        def first_stable_index(nums, k)\n  n = nums.length\n  return -1 if n == 0\n\
        \  pref_max = Array.new(n)\n  suff_min = Array.new(n)\n  pref_max[0] = nums[0]\n\
        \  (1...n).each { |i| pref_max[i] = nums[i] > pref_max[i-1] ? nums[i] : pref_max[i-1]\
        \ }\n  suff_min[n-1] = nums[n-1]\n  (n-2).downto(0) { |i| suff_min[i] = nums[i]\
        \ < suff_min[i+1] ? nums[i] : suff_min[i+1] }\n  (0...n).each { |i| return i\
        \ if pref_max[i] - suff_min[i] <= k }\n  -1\nend"
      scala: "object Solution {\n  def firstStableIndex(nums: Array[Int], k: Int): Int\
        \ = {\n    val n = nums.length\n    if (n == 0) return -1\n    val prefMax =\
        \ new Array[Int](n)\n    val suffMin = new Array[Int](n)\n    prefMax(0) = nums(0)\n\
        \    for (i <- 1 until n) {\n      prefMax(i) = Math.max(prefMax(i - 1), nums(i))\n\
        \    }\n    suffMin(n - 1) = nums(n - 1)\n    for (i <- (n - 2) to 0 by -1)\
        \ {\n      suffMin(i) = Math.min(suffMin(i + 1), nums(i))\n    }\n    for (i\
        \ <- 0 until n) {\n      if (prefMax(i) - suffMin(i) <= k) return i\n    }\n\
        \    -1\n  }\n}"
      rust: "impl Solution {\n    pub fn first_stable_index(nums: Vec<i32>, k: i32)\
        \ -> i32 {\n        let n = nums.len();\n        if n == 0 {\n            return\
        \ -1;\n        }\n\n        let mut pref_max = vec![0; n];\n        let mut\
        \ suff_min = vec![0; n];\n\n        pref_max[0] = nums[0];\n        for i in\
        \ 1..n {\n            pref_max[i] = std::cmp::max(pref_max[i - 1], nums[i]);\n\
        \        }\n\n        suff_min[n - 1] = nums[n - 1];\n        for i in (0..n\
        \ - 1).rev() {\n            suff_min[i] = std::cmp::min(suff_min[i + 1], nums[i]);\n\
        \        }\n\n        for i in 0..n {\n            if pref_max[i] - suff_min[i]\
        \ <= k {\n                return i as i32;\n            }\n        }\n\n   \
        \     -1\n    }\n}"
      racket: "(define/contract (first-stable-index nums k)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer?)\n  (let* ([n (length nums)])\n    (if (= n\
        \ 0)\n        -1\n        (let* ([arr (list->vector nums)]\n               [pref-max\
        \ (make-vector n)]\n               [suff-min (make-vector n)])\n          (vector-set!\
        \ pref-max 0 (vector-ref arr 0))\n          (for ([i (in-range 1 n)])\n    \
        \        (vector-set! pref-max i (max (vector-ref pref-max (- i 1)) (vector-ref\
        \ arr i))))\n          (vector-set! suff-min (- n 1) (vector-ref arr (- n 1)))\n\
        \          (for ([i (in-range (- n 2) -1 -1)])\n            (vector-set! suff-min\
        \ i (min (vector-ref suff-min (+ i 1)) (vector-ref arr i))))\n          (let\
        \ loop ([i 0])\n            (cond\n              [(= i n) -1]\n            \
        \  [(<= (- (vector-ref pref-max i) (vector-ref suff-min i)) k) i]\n        \
        \      [else (loop (+ i 1))]))))))"
      erlang: "-spec first_stable_index(Nums :: [integer()], K :: integer()) -> integer().\n\
        first_stable_index(Nums, K) ->\n    [H | _] = Nums,\n    PrefMaxes = calculate_pref_maxes(Nums,\
        \ H, []),\n    SuffMins = calculate_suff_mins(lists:reverse(Nums), 2000000001,\
        \ []),\n    find_stable(PrefMaxes, SuffMins, K, 0).\n\ncalculate_pref_maxes([],\
        \ _Max, Acc) -> \n    lists:reverse(Acc);\ncalculate_pref_maxes([H | T], Max,\
        \ Acc) ->\n    NewMax = erlang:max(H, Max),\n    calculate_pref_maxes(T, NewMax,\
        \ [NewMax | Acc]).\n\ncalculate_suff_mins([], _Min, Acc) -> \n    Acc;\ncalculate_suff_mins([H\
        \ | T], Min, Acc) ->\n    NewMin = erlang:min(H, Min),\n    calculate_suff_mins(T,\
        \ NewMin, [NewMin | Acc]).\n\nfind_stable([], _, _, _) -> \n    -1;\nfind_stable([P\
        \ | PT], [S | ST], K, Index) ->\n    if P - S =< K -> Index;\n       true ->\
        \ find_stable(PT, ST, K, Index + 1)\n    end."
      elixir: "defmodule Solution do\n  @spec first_stable_index(nums :: [integer],\
        \ k :: integer) :: integer\n  def first_stable_index(nums, k) do\n    pref_maxes\
        \ = Enum.scan(nums, &max/2)\n\n    suff_mins = nums\n    |> Enum.reverse()\n\
        \    |> Enum.scan(&min/2)\n    |> Enum.reverse()\n\n    Enum.zip(pref_maxes,\
        \ suff_mins)\n    |> Enum.find_index(fn {p, s} -> p - s <= k end)\n    |> case\
        \ do\n      nil -> -1\n      idx -> idx\n    end\n  end\nend"
    approach: The algorithm precomputes suffix minimums to efficiently determine the
      minimum value in the range [i..n-1] for any index i. By iterating through the
      array from right to left, we can construct an auxiliary array where each entry
      i represents the minimum value found from index i to the end of the input. This
      preprocessing allows us to fetch the required minimum value for any instability
      score calculation in constant time.
    time_complexity: O(n) where n is the length of the input array. The algorithm performs
      one linear pass to precompute the suffix minimums and a second linear pass to
      compute the instability scores and identify the smallest stable index.
    space_complexity: O(n) to store the suffix minimum array. Aside from this auxiliary
      array, the algorithm uses only a constant amount of extra space for the running
      prefix maximum and loop variables.
    elapsed_time: 167.25067734718323
    model: gemini-3-flash-preview
    generated_at: '2026-09-05 02:19:40 '
---

## Problem #3904: Smallest Stable Index II

**Difficulty:** Medium

**Topics:** Array, Prefix Sum

## Problem Description

<p>You are given an integer array <code>nums</code> of length <code>n</code> and an integer <code>k</code>.</p>

<p>For each index <code>i</code>, define its <strong>instability score</strong> as <code>max(nums[0..i]) - min(nums[i..n - 1])</code>.</p>

<p>In other words:</p>

<ul>
	<li><code>max(nums[0..i])</code> is the <strong>largest</strong> value among the elements from index 0 to index <code>i</code>.</li>
	<li><code>min(nums[i..n - 1])</code> is the <strong>smallest</strong> value among the elements from index <code>i</code> to index <code>n - 1</code>.</li>
</ul>

<p>An index <code>i</code> is called <strong>stable</strong> if its instability score is <strong>less than or equal to</strong> <code>k</code>.</p>

<p>Return the <strong>smallest</strong> stable index. If no such index exists, return -1.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,0,1,4], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>At index 0: The maximum in <code>[5]</code> is 5, and the minimum in <code>[5, 0, 1, 4]</code> is 0, so the instability score is <code>5 - 0 = 5</code>.</li>
	<li>At index 1: The maximum in <code>[5, 0]</code> is 5, and the minimum in <code>[0, 1, 4]</code> is 0, so the instability score is <code>5 - 0 = 5</code>.</li>
	<li>At index 2: The maximum in <code>[5, 0, 1]</code> is 5, and the minimum in <code>[1, 4]</code> is 1, so the instability score is <code>5 - 1 = 4</code>.</li>
	<li>At index 3: The maximum in <code>[5, 0, 1, 4]</code> is 5, and the minimum in <code>[4]</code> is 4, so the instability score is <code>5 - 4 = 1</code>.</li>
	<li>This is the first index with an instability score less than or equal to <code>k = 3</code>. Thus, the answer is 3.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,2,1], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>At index 0, the instability score is <code>3 - 1 = 2</code>.</li>
	<li>At index 1, the instability score is <code>3 - 1 = 2</code>.</li>
	<li>At index 2, the instability score is <code>3 - 1 = 2</code>.</li>
	<li>None of these values is less than or equal to <code>k = 1</code>, so the answer is -1.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0], k = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>At index 0, the instability score is <code>0 - 0 = 0</code>, which is less than or equal to <code>k = 0</code>. Therefore, the answer is 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Precompute prefix maximums in an array `prefMax`, where `prefMax[i]` is the maximum of `nums[0..i]`

2. Precompute suffix minimums in an array `suffMin`, where `suffMin[i]` is the minimum of `nums[i..n-1]`

3. For each index `i`, compute the instability score as `prefMax[i] - suffMin[i]`

4. Return the smallest index where the instability score is `<= k`. If no such index exists, return `-1`

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm precomputes suffix minimums to efficiently determine the minimum value in the range [i..n-1] for any index i. By iterating through the array from right to left, we can construct an auxiliary array where each entry i represents the minimum value found from index i to the end of the input. This preprocessing allows us to fetch the required minimum value for any instability score calculation in constant time.

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
    int firstStableIndex(vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 0) return -1;

        vector<int> suffMin(n);
        suffMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            suffMin[i] = min(nums[i], suffMin[i + 1]);
        }

        int prefMax = nums[0];
        for (int i = 0; i < n; ++i) {
            if (nums[i] > prefMax) prefMax = nums[i];
            if ((long long)prefMax - suffMin[i] <= (long long)k) {
                return i;
            }
        }

        return -1;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int firstStableIndex(int[] nums, int k) {
        int n = nums.length;
        if (n == 0) return -1;

        int[] suffMin = new int[n];
        suffMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffMin[i] = Math.min(nums[i], suffMin[i + 1]);
        }

        int prefMax = nums[0];
        for (int i = 0; i < n; i++) {
            prefMax = Math.max(prefMax, nums[i]);
            if ((long) prefMax - suffMin[i] <= (long) k) {
                return i;
            }
        }

        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0: return -1

        suffMin = [0] * n
        suffMin[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            if nums[i] < suffMin[i + 1]:
                suffMin[i] = nums[i]
            else:
                suffMin[i] = suffMin[i + 1]

        prefMax = -float('inf')
        for i in range(n):
            if nums[i] > prefMax:
                prefMax = nums[i]
            if prefMax - suffMin[i] <= k:
                return i

        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0: return -1

        suffMin = [0] * n
        suffMin[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffMin[i] = min(nums[i], suffMin[i + 1])

        prefMax = -float('inf')
        for i in range(n):
            prefMax = max(prefMax, nums[i])
            if prefMax - suffMin[i] <= k:
                return i

        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int firstStableIndex(int* nums, int numsSize, int k) {
    if (numsSize == 0) return -1;

    int* suffMin = (int*)malloc(numsSize * sizeof(int));
    suffMin[numsSize - 1] = nums[numsSize - 1];
    for (int i = numsSize - 2; i >= 0; --i) {
        if (nums[i] < suffMin[i + 1]) {
            suffMin[i] = nums[i];
        } else {
            suffMin[i] = suffMin[i + 1];
        }
    }

    int prefMax = nums[0];
    int result = -1;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] > prefMax) prefMax = nums[i];
        if ((long long)prefMax - suffMin[i] <= (long long)k) {
            result = i;
            break;
        }
    }

    free(suffMin);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int FirstStableIndex(int[] nums, int k) {
        int n = nums.Length;
        if (n == 0) return -1;

        int[] suffMin = new int[n];
        suffMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffMin[i] = Math.Min(suffMin[i + 1], nums[i]);
        }

        int currentPrefMax = nums[0];
        for (int i = 0; i < n; i++) {
            if (nums[i] > currentPrefMax) {
                currentPrefMax = nums[i];
            }
            if (currentPrefMax - suffMin[i] <= k) {
                return i;
            }
        }

        return -1;
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
var firstStableIndex = function(nums, k) {
    const n = nums.length;
    if (n === 0) return -1;

    const suffMin = new Int32Array(n);
    suffMin[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        suffMin[i] = Math.min(suffMin[i + 1], nums[i]);
    }

    let currentPrefMax = nums[0];
    for (let i = 0; i < n; i++) {
        currentPrefMax = Math.max(currentPrefMax, nums[i]);
        if (currentPrefMax - suffMin[i] <= k) {
            return i;
        }
    }

    return -1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function firstStableIndex(nums: number[], k: number): number {
    const n: number = nums.length;
    if (n === 0) return -1;

    const suffMin: Int32Array = new Int32Array(n);
    suffMin[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        suffMin[i] = Math.min(suffMin[i + 1], nums[i]);
    }

    let currentPrefMax: number = nums[0];
    for (let i = 0; i < n; i++) {
        currentPrefMax = Math.max(currentPrefMax, nums[i]);
        if (currentPrefMax - suffMin[i] <= k) {
            return i;
        }
    }

    return -1;
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
    function firstStableIndex($nums, $k) {
        $n = count($nums);
        if ($n === 0) return -1;

        $suffMin = array_fill(0, $n, 0);
        $suffMin[$n - 1] = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) {
            $suffMin[$i] = min($suffMin[$i + 1], $nums[$i]);
        }

        $currentPrefMax = $nums[0];
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] > $currentPrefMax) {
                $currentPrefMax = $nums[$i];
            }
            if ($currentPrefMax - $suffMin[$i] <= $k) {
                return $i;
            }
        }

        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func firstStableIndex(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        if n == 0 { return -1 }

        var suffMin = Array(repeating: 0, count: n)
        suffMin[n - 1] = nums[n - 1]
        if n > 1 {
            for i in (0..<n - 1).reversed() {
                suffMin[i] = min(suffMin[i + 1], nums[i])
            }
        }

        var currentPrefMax = nums[0]
        for i in 0..<n {
            currentPrefMax = max(currentPrefMax, nums[i])
            if currentPrefMax - suffMin[i] <= k {
                return i
            }
        }

        return -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun firstStableIndex(nums: IntArray, k: Int): Int {
        val n = nums.size
        if (n == 0) return -1
        val prefMax = IntArray(n)
        val suffMin = IntArray(n)
        prefMax[0] = nums[0]
        for (i in 1 until n) {
            prefMax[i] = if (nums[i] > prefMax[i - 1]) nums[i] else prefMax[i - 1]
        }
        suffMin[n - 1] = nums[n - 1]
        for (i in n - 2 downTo 0) {
            suffMin[i] = if (nums[i] < suffMin[i + 1]) nums[i] else suffMin[i + 1]
        }
        for (i in 0 until n) {
            if (prefMax[i] - suffMin[i] <= k) {
                return i
            }
        }
        return -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int firstStableIndex(List<int> nums, int k) {
    int n = nums.length;
    if (n == 0) return -1;
    List<int> prefMax = List.filled(n, 0);
    List<int> suffMin = List.filled(n, 0);
    prefMax[0] = nums[0];
    for (int i = 1; i < n; i++) {
      prefMax[i] = nums[i] > prefMax[i - 1] ? nums[i] : prefMax[i - 1];
    }
    suffMin[n - 1] = nums[n - 1];
    for (int i = n - 2; i >= 0; i--) {
      suffMin[i] = nums[i] < suffMin[i + 1] ? nums[i] : suffMin[i + 1];
    }
    for (int i = 0; i < n; i++) {
      if (prefMax[i] - suffMin[i] <= k) {
        return i;
      }
    }
    return -1;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func firstStableIndex(nums []int, k int) int {
    n := len(nums)
    if n == 0 {
        return -1
    }
    prefMax := make([]int, n)
    suffMin := make([]int, n)
    prefMax[0] = nums[0]
    for i := 1; i < n; i++ {
        if nums[i] > prefMax[i-1] {
            prefMax[i] = nums[i]
        } else {
            prefMax[i] = prefMax[i-1]
        }
    }
    suffMin[n-1] = nums[n-1]
    for i := n - 2; i >= 0; i-- {
        if nums[i] < suffMin[i+1] {
            suffMin[i] = nums[i]
        } else {
            suffMin[i] = suffMin[i+1]
        }
    }
    for i := 0; i < n; i++ {
        if prefMax[i]-suffMin[i] <= k {
            return i
        }
    }
    return -1
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def first_stable_index(nums, k)
  n = nums.length
  return -1 if n == 0
  pref_max = Array.new(n)
  suff_min = Array.new(n)
  pref_max[0] = nums[0]
  (1...n).each { |i| pref_max[i] = nums[i] > pref_max[i-1] ? nums[i] : pref_max[i-1] }
  suff_min[n-1] = nums[n-1]
  (n-2).downto(0) { |i| suff_min[i] = nums[i] < suff_min[i+1] ? nums[i] : suff_min[i+1] }
  (0...n).each { |i| return i if pref_max[i] - suff_min[i] <= k }
  -1
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def firstStableIndex(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    if (n == 0) return -1
    val prefMax = new Array[Int](n)
    val suffMin = new Array[Int](n)
    prefMax(0) = nums(0)
    for (i <- 1 until n) {
      prefMax(i) = Math.max(prefMax(i - 1), nums(i))
    }
    suffMin(n - 1) = nums(n - 1)
    for (i <- (n - 2) to 0 by -1) {
      suffMin(i) = Math.min(suffMin(i + 1), nums(i))
    }
    for (i <- 0 until n) {
      if (prefMax(i) - suffMin(i) <= k) return i
    }
    -1
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn first_stable_index(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        if n == 0 {
            return -1;
        }

        let mut pref_max = vec![0; n];
        let mut suff_min = vec![0; n];

        pref_max[0] = nums[0];
        for i in 1..n {
            pref_max[i] = std::cmp::max(pref_max[i - 1], nums[i]);
        }

        suff_min[n - 1] = nums[n - 1];
        for i in (0..n - 1).rev() {
            suff_min[i] = std::cmp::min(suff_min[i + 1], nums[i]);
        }

        for i in 0..n {
            if pref_max[i] - suff_min[i] <= k {
                return i as i32;
            }
        }

        -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (first-stable-index nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([n (length nums)])
    (if (= n 0)
        -1
        (let* ([arr (list->vector nums)]
               [pref-max (make-vector n)]
               [suff-min (make-vector n)])
          (vector-set! pref-max 0 (vector-ref arr 0))
          (for ([i (in-range 1 n)])
            (vector-set! pref-max i (max (vector-ref pref-max (- i 1)) (vector-ref arr i))))
          (vector-set! suff-min (- n 1) (vector-ref arr (- n 1)))
          (for ([i (in-range (- n 2) -1 -1)])
            (vector-set! suff-min i (min (vector-ref suff-min (+ i 1)) (vector-ref arr i))))
          (let loop ([i 0])
            (cond
              [(= i n) -1]
              [(<= (- (vector-ref pref-max i) (vector-ref suff-min i)) k) i]
              [else (loop (+ i 1))]))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec first_stable_index(Nums :: [integer()], K :: integer()) -> integer().
first_stable_index(Nums, K) ->
    [H | _] = Nums,
    PrefMaxes = calculate_pref_maxes(Nums, H, []),
    SuffMins = calculate_suff_mins(lists:reverse(Nums), 2000000001, []),
    find_stable(PrefMaxes, SuffMins, K, 0).

calculate_pref_maxes([], _Max, Acc) -> 
    lists:reverse(Acc);
calculate_pref_maxes([H | T], Max, Acc) ->
    NewMax = erlang:max(H, Max),
    calculate_pref_maxes(T, NewMax, [NewMax | Acc]).

calculate_suff_mins([], _Min, Acc) -> 
    Acc;
calculate_suff_mins([H | T], Min, Acc) ->
    NewMin = erlang:min(H, Min),
    calculate_suff_mins(T, NewMin, [NewMin | Acc]).

find_stable([], _, _, _) -> 
    -1;
find_stable([P | PT], [S | ST], K, Index) ->
    if P - S =< K -> Index;
       true -> find_stable(PT, ST, K, Index + 1)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec first_stable_index(nums :: [integer], k :: integer) :: integer
  def first_stable_index(nums, k) do
    pref_maxes = Enum.scan(nums, &max/2)

    suff_mins = nums
    |> Enum.reverse()
    |> Enum.scan(&min/2)
    |> Enum.reverse()

    Enum.zip(pref_maxes, suff_mins)
    |> Enum.find_index(fn {p, s} -> p - s <= k end)
    |> case do
      nil -> -1
      idx -> idx
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the input array. The algorithm performs one linear pass to precompute the suffix minimums and a second linear pass to compute the instability scores and identify the smallest stable index.
- **Space Complexity:** O(n) to store the suffix minimum array. Aside from this auxiliary array, the algorithm uses only a constant amount of extra space for the running prefix maximum and loop variables.
