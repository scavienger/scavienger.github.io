---
layout: post
title: "Smallest Stable Index I"
date: 2026-09-04 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Prefix Sum"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/smallest-stable-index-i/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nclass\
        \ Solution {\npublic:\n    int firstStableIndex(vector<int>& nums, int k) {\n\
        \        int n = nums.size();\n        if (n == 0) return -1;\n        vector<int>\
        \ suffixMin(n);\n        suffixMin[n - 1] = nums[n - 1];\n        for (int i\
        \ = n - 2; i >= 0; i--) {\n            suffixMin[i] = min(nums[i], suffixMin[i\
        \ + 1]);\n        }\n        int currentMax = nums[0];\n        for (int i =\
        \ 0; i < n; i++) {\n            if (nums[i] > currentMax) currentMax = nums[i];\n\
        \            if ((long long)currentMax - suffixMin[i] <= (long long)k) {\n \
        \               return i;\n            }\n        }\n        return -1;\n  \
        \  }\n};"
      java: "class Solution {\n    public int firstStableIndex(int[] nums, int k) {\n\
        \        int n = nums.length;\n        if (n == 0) return -1;\n        int[]\
        \ suffixMin = new int[n];\n        suffixMin[n - 1] = nums[n - 1];\n       \
        \ for (int i = n - 2; i >= 0; i--) {\n            suffixMin[i] = Math.min(nums[i],\
        \ suffixMin[i + 1]);\n        }\n        int currentMax = nums[0];\n       \
        \ for (int i = 0; i < n; i++) {\n            currentMax = Math.max(currentMax,\
        \ nums[i]);\n            if ((long) currentMax - suffixMin[i] <= (long) k) {\n\
        \                return i;\n            }\n        }\n        return -1;\n \
        \   }\n}"
      python: "class Solution(object):\n    def firstStableIndex(self, nums, k):\n \
        \       \"\"\"\n        :type nums: List[int]\n        :type k: int\n      \
        \  :rtype: int\n        \"\"\"\n        n = len(nums)\n        if n == 0:\n\
        \            return -1\n        suffix_min = [0] * n\n        suffix_min[n -\
        \ 1] = nums[n - 1]\n        for i in range(n - 2, -1, -1):\n            suffix_min[i]\
        \ = min(nums[i], suffix_min[i + 1])\n\n        curr_max = nums[0]\n        for\
        \ i in range(n):\n            if nums[i] > curr_max:\n                curr_max\
        \ = nums[i]\n            if curr_max - suffix_min[i] <= k:\n               \
        \ return i\n        return -1"
      python3: "class Solution:\n    def firstStableIndex(self, nums: list[int], k:\
        \ int) -> int:\n        n = len(nums)\n        if n == 0:\n            return\
        \ -1\n        suffix_min = [0] * n\n        suffix_min[n - 1] = nums[n - 1]\n\
        \        for i in range(n - 2, -1, -1):\n            suffix_min[i] = min(nums[i],\
        \ suffix_min[i + 1])\n\n        curr_max = nums[0]\n        for i in range(n):\n\
        \            if nums[i] > curr_max:\n                curr_max = nums[i]\n  \
        \          if curr_max - suffix_min[i] <= k:\n                return i\n   \
        \     return -1"
      c: "int firstStableIndex(int* nums, int numsSize, int k) {\n    if (numsSize ==\
        \ 0) return -1;\n    int suffixMin[numsSize];\n    suffixMin[numsSize - 1] =\
        \ nums[numsSize - 1];\n    for (int i = numsSize - 2; i >= 0; i--) {\n     \
        \   suffixMin[i] = (nums[i] < suffixMin[i + 1]) ? nums[i] : suffixMin[i + 1];\n\
        \    }\n    int currentMax = nums[0];\n    for (int i = 0; i < numsSize; i++)\
        \ {\n        if (nums[i] > currentMax) currentMax = nums[i];\n        if ((long\
        \ long)currentMax - suffixMin[i] <= (long long)k) {\n            return i;\n\
        \        }\n    }\n    return -1;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public int FirstStableIndex(int[]\
        \ nums, int k) {\n        int n = nums.Length;\n        if (n == 0) return -1;\n\
        \        int[] suffixMin = new int[n];\n        suffixMin[n - 1] = nums[n -\
        \ 1];\n        for (int i = n - 2; i >= 0; i--) {\n            suffixMin[i]\
        \ = Math.Min(nums[i], suffixMin[i + 1]);\n        }\n        int currentMax\
        \ = nums[0];\n        for (int i = 0; i < n; i++) {\n            if (nums[i]\
        \ > currentMax) currentMax = nums[i];\n            if ((long)currentMax - suffixMin[i]\
        \ <= (long)k) {\n                return i;\n            }\n        }\n     \
        \   return -1;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @return\
        \ {number}\n */\nvar firstStableIndex = function(nums, k) {\n    const n = nums.length;\n\
        \    if (n === 0) return -1;\n    const suffixMin = new Array(n);\n    suffixMin[n\
        \ - 1] = nums[n - 1];\n    for (let i = n - 2; i >= 0; i--) {\n        suffixMin[i]\
        \ = Math.min(nums[i], suffixMin[i + 1]);\n    }\n    let currentMax = nums[0];\n\
        \    for (let i = 0; i < n; i++) {\n        if (nums[i] > currentMax) currentMax\
        \ = nums[i];\n        if (currentMax - suffixMin[i] <= k) {\n            return\
        \ i;\n        }\n    }\n    return -1;\n};"
      typescript: "function firstStableIndex(nums: number[], k: number): number {\n\
        \    const n = nums.length;\n    const suffixMin: number[] = new Array(n).fill(0);\n\
        \    suffixMin[n - 1] = nums[n - 1];\n    for (let i = n - 2; i >= 0; i--) {\n\
        \        suffixMin[i] = Math.min(nums[i], suffixMin[i + 1]);\n    }\n    let\
        \ currentMax = nums[0];\n    for (let i = 0; i < n; i++) {\n        currentMax\
        \ = Math.max(currentMax, nums[i]);\n        if (currentMax - suffixMin[i] <=\
        \ k) {\n            return i;\n        }\n    }\n    return -1;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $k\n     * @return Integer\n     */\n    function firstStableIndex($nums,\
        \ $k) {\n        $n = count($nums);\n        $suffixMin = array_fill(0, $n,\
        \ 0);\n        $suffixMin[$n - 1] = $nums[$n - 1];\n        for ($i = $n - 2;\
        \ $i >= 0; $i--) {\n            $suffixMin[$i] = min($nums[$i], $suffixMin[$i\
        \ + 1]);\n        }\n        $currentMax = $nums[0];\n        for ($i = 0; $i\
        \ < $n; $i++) {\n            $currentMax = max($currentMax, $nums[$i]);\n  \
        \          if ($currentMax - $suffixMin[$i] <= $k) {\n                return\
        \ $i;\n            }\n        }\n        return -1;\n    }\n}"
      swift: "class Solution {\n    func firstStableIndex(_ nums: [Int], _ k: Int) ->\
        \ Int {\n        let n = nums.count\n        var suffixMin = Array(repeating:\
        \ 0, count: n)\n        suffixMin[n - 1] = nums[n - 1]\n        if n > 1 {\n\
        \            for i in stride(from: n - 2, through: 0, by: -1) {\n          \
        \      suffixMin[i] = min(nums[i], suffixMin[i + 1])\n            }\n      \
        \  }\n        var currentMax = nums[0]\n        for i in 0..<n {\n         \
        \   currentMax = max(currentMax, nums[i])\n            if currentMax - suffixMin[i]\
        \ <= k {\n                return i\n            }\n        }\n        return\
        \ -1\n    }\n}"
      kotlin: "class Solution {\n    fun firstStableIndex(nums: IntArray, k: Int): Int\
        \ {\n        val n = nums.size\n        val suffixMin = IntArray(n)\n      \
        \  suffixMin[n - 1] = nums[n - 1]\n        for (i in n - 2 downTo 0) {\n   \
        \         suffixMin[i] = if (nums[i] < suffixMin[i + 1]) nums[i] else suffixMin[i\
        \ + 1]\n        }\n        var currentMax = nums[0]\n        for (i in 0 until\
        \ n) {\n            if (nums[i] > currentMax) {\n                currentMax\
        \ = nums[i]\n            }\n            if (currentMax.toLong() - suffixMin[i].toLong()\
        \ <= k.toLong()) {\n                return i\n            }\n        }\n   \
        \     return -1\n    }\n}"
      dart: "class Solution {\n  int firstStableIndex(List<int> nums, int k) {\n   \
        \ int n = nums.length;\n    List<int> suffixMin = List.filled(n, 0);\n    suffixMin[n\
        \ - 1] = nums[n - 1];\n    for (int i = n - 2; i >= 0; i--) {\n      suffixMin[i]\
        \ = nums[i] < suffixMin[i + 1] ? nums[i] : suffixMin[i + 1];\n    }\n    int\
        \ currentMax = nums[0];\n    for (int i = 0; i < n; i++) {\n      if (nums[i]\
        \ > currentMax) {\n        currentMax = nums[i];\n      }\n      if (currentMax\
        \ - suffixMin[i] <= k) {\n        return i;\n      }\n    }\n    return -1;\n\
        \  }\n}"
      go: "func firstStableIndex(nums []int, k int) int {\n    n := len(nums)\n    if\
        \ n == 0 {\n        return -1\n    }\n    suffixMin := make([]int, n)\n    suffixMin[n-1]\
        \ = nums[n-1]\n    for i := n - 2; i >= 0; i-- {\n        if nums[i] < suffixMin[i+1]\
        \ {\n            suffixMin[i] = nums[i]\n        } else {\n            suffixMin[i]\
        \ = suffixMin[i+1]\n        }\n    }\n    currentMax := nums[0]\n    for i :=\
        \ 0; i < n; i++ {\n        if nums[i] > currentMax {\n            currentMax\
        \ = nums[i]\n        }\n        if currentMax-suffixMin[i] <= k {\n        \
        \    return i\n        }\n    }\n    return -1\n}"
      ruby: "def first_stable_index(nums, k)\n  n = nums.length\n  return -1 if n ==\
        \ 0\n\n  prefix_max = Array.new(n)\n  suffix_min = Array.new(n)\n\n  cur_max\
        \ = nums[0]\n  (0...n).each do |i|\n    cur_max = nums[i] if nums[i] > cur_max\n\
        \    prefix_max[i] = cur_max\n  end\n\n  cur_min = nums[n - 1]\n  (n - 1).step(0,\
        \ -1) do |i|\n    cur_min = nums[i] if nums[i] < cur_min\n    suffix_min[i]\
        \ = cur_min\n  end\n\n  (0...n).each do |i|\n    return i if prefix_max[i] -\
        \ suffix_min[i] <= k\n  end\n  -1\nend"
      scala: "object Solution {\n    def firstStableIndex(nums: Array[Int], k: Int):\
        \ Int = {\n        val n = nums.length\n        if (n == 0) return -1\n    \
        \    val prefixMax = new Array[Int](n)\n        val suffixMin = new Array[Int](n)\n\
        \n        var curMax = nums(0)\n        for (i <- 0 until n) {\n           \
        \ if (nums(i) > curMax) curMax = nums(i)\n            prefixMax(i) = curMax\n\
        \        }\n\n        var curMin = nums(n - 1)\n        for (i <- n - 1 to 0\
        \ by -1) {\n            if (nums(i) < curMin) curMin = nums(i)\n           \
        \ suffixMin(i) = curMin\n        }\n\n        for (i <- 0 until n) {\n     \
        \       if (prefixMax(i).toLong - suffixMin(i).toLong <= k.toLong) {\n     \
        \           return i\n            }\n        }\n        -1\n    }\n}"
      rust: "impl Solution {\n    pub fn first_stable_index(nums: Vec<i32>, k: i32)\
        \ -> i32 {\n        let n = nums.len();\n        if n == 0 {\n            return\
        \ -1;\n        }\n        let mut prefix_max = vec![0; n];\n        let mut\
        \ suffix_min = vec![0; n];\n\n        let mut cur_max = nums[0];\n        for\
        \ i in 0..n {\n            if nums[i] > cur_max {\n                cur_max =\
        \ nums[i];\n            }\n            prefix_max[i] = cur_max;\n        }\n\
        \n        let mut cur_min = nums[n - 1];\n        for i in (0..n).rev() {\n\
        \            if nums[i] < cur_min {\n                cur_min = nums[i];\n  \
        \          }\n            suffix_min[i] = cur_min;\n        }\n\n        for\
        \ i in 0..n {\n            if (prefix_max[i] as i64) - (suffix_min[i] as i64)\
        \ <= k as i64 {\n                return i as i32;\n            }\n        }\n\
        \        -1\n    }\n}"
      racket: "(define/contract (first-stable-index nums k)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer?)\n  (if (null? nums)\n      -1\n      (let*\
        \ ([prefix-max (let loop ([xs (cdr nums)] [cur (car nums)] [acc (list (car nums))])\n\
        \                           (if (null? xs)\n                               (reverse\
        \ acc)\n                               (let ([new-max (max cur (car xs))])\n\
        \                                 (loop (cdr xs) new-max (cons new-max acc)))))]\n\
        \             [rev-nums (reverse nums)]\n             [suffix-min (let loop\
        \ ([xs (cdr rev-nums)] [cur (car rev-nums)] [acc (list (car rev-nums))])\n \
        \                          (if (null? xs)\n                               acc\n\
        \                               (let ([new-min (min cur (car xs))])\n      \
        \                           (loop (cdr xs) new-min (cons new-min acc)))))])\n\
        \        (let loop-find ([i 0] [pm prefix-max] [sm suffix-min])\n          (cond\n\
        \            [(null? pm) -1]\n            [(<= (- (car pm) (car sm)) k) i]\n\
        \            [else (loop-find (+ i 1) (cdr pm) (cdr sm))])))))"
      erlang: "-spec first_stable_index(Nums :: [integer()], K :: integer()) -> integer().\n\
        first_stable_index(Nums, K) ->\n    PrefixMax = get_prefix_max(Nums),\n    SuffixMin\
        \ = get_suffix_min(lists:reverse(Nums)),\n    find_first(PrefixMax, SuffixMin,\
        \ K, 0).\n\nget_prefix_max([H|T]) -> get_prefix_max(T, H, [H]).\nget_prefix_max([],\
        \ _, Acc) -> lists:reverse(Acc);\nget_prefix_max([H|T], Cur, Acc) ->\n    NewMax\
        \ = erlang:max(Cur, H),\n    get_prefix_max(T, NewMax, [NewMax|Acc]).\n\nget_suffix_min([H|T])\
        \ -> get_suffix_min(T, H, [H]).\nget_suffix_min([], _, Acc) -> Acc;\nget_suffix_min([H|T],\
        \ Cur, Acc) ->\n    NewMin = erlang:min(Cur, H),\n    get_suffix_min(T, NewMin,\
        \ [NewMin|Acc]).\n\nfind_first([], [], _, _) -> -1;\nfind_first([PM|PMT], [SM|SMT],\
        \ K, I) ->\n    if PM - SM =< K -> I;\n       true -> find_first(PMT, SMT, K,\
        \ I + 1)\n    end."
      elixir: "defmodule Solution do\n  @spec first_stable_index(nums :: [integer],\
        \ k :: integer) :: integer\n  def first_stable_index(nums, k) do\n    prefix_max\
        \ = Enum.scan(nums, &max/2)\n    suffix_min = nums |> Enum.reverse() |> Enum.scan(&min/2)\
        \ |> Enum.reverse()\n\n    Enum.zip(prefix_max, suffix_min)\n    |> Enum.find_index(fn\
        \ {p_max, s_min} -> p_max - s_min <= k end)\n    |> case do\n      nil -> -1\n\
        \      index -> index\n    end\n  end\nend"
    approach: 'The instability score for each index i is calculated as the difference
      between the maximum value in the prefix subarray nums[0...i] and the minimum value
      in the suffix subarray nums[i...n-1]. To solve this efficiently, we first precompute
      all possible suffix minimums in a single backward pass. By storing these in an
      auxiliary array, we can access the minimum of any suffix nums[i...n-1] in constant
      time.


      Next, we iterate through the array from left to right while keeping track of the
      current maximum element encountered so far, which represents the prefix maximum.
      At each index i, we calculate the instability score by subtracting the precomputed
      suffix minimum from this running prefix maximum. The first index where this score
      is less than or equal to k is returned as the smallest stable index. If no such
      index is found after a complete traversal, we return -1.'
    time_complexity: O(n) where n is the length of the array. The algorithm performs
      one backward pass to compute the suffix minimums and one forward pass to find
      the first index satisfying the stability condition, resulting in linear time complexity.
    space_complexity: O(n) to store the suffix minimums array. While we track the prefix
      maximum using only a single variable, the auxiliary array for suffix minimums
      is necessary to allow O(1) score calculation at each index.
    elapsed_time: 179.76586604118347
    model: gemini-3-flash-preview
    generated_at: '2026-09-04 02:19:08 '
---

## Problem #3903: Smallest Stable Index I

**Difficulty:** Easy

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
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Simulate as described

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The instability score for each index i is calculated as the difference between the maximum value in the prefix subarray nums[0...i] and the minimum value in the suffix subarray nums[i...n-1]. To solve this efficiently, we first precompute all possible suffix minimums in a single backward pass. By storing these in an auxiliary array, we can access the minimum of any suffix nums[i...n-1] in constant time.

Next, we iterate through the array from left to right while keeping track of the current maximum element encountered so far, which represents the prefix maximum. At each index i, we calculate the instability score by subtracting the precomputed suffix minimum from this running prefix maximum. The first index where this score is less than or equal to k is returned as the smallest stable index. If no such index is found after a complete traversal, we return -1.

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
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 0) return -1;
        vector<int> suffixMin(n);
        suffixMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffixMin[i] = min(nums[i], suffixMin[i + 1]);
        }
        int currentMax = nums[0];
        for (int i = 0; i < n; i++) {
            if (nums[i] > currentMax) currentMax = nums[i];
            if ((long long)currentMax - suffixMin[i] <= (long long)k) {
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
        int[] suffixMin = new int[n];
        suffixMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffixMin[i] = Math.min(nums[i], suffixMin[i + 1]);
        }
        int currentMax = nums[0];
        for (int i = 0; i < n; i++) {
            currentMax = Math.max(currentMax, nums[i]);
            if ((long) currentMax - suffixMin[i] <= (long) k) {
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
        if n == 0:
            return -1
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        curr_max = nums[0]
        for i in range(n):
            if nums[i] > curr_max:
                curr_max = nums[i]
            if curr_max - suffix_min[i] <= k:
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
        if n == 0:
            return -1
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        curr_max = nums[0]
        for i in range(n):
            if nums[i] > curr_max:
                curr_max = nums[i]
            if curr_max - suffix_min[i] <= k:
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
    int suffixMin[numsSize];
    suffixMin[numsSize - 1] = nums[numsSize - 1];
    for (int i = numsSize - 2; i >= 0; i--) {
        suffixMin[i] = (nums[i] < suffixMin[i + 1]) ? nums[i] : suffixMin[i + 1];
    }
    int currentMax = nums[0];
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > currentMax) currentMax = nums[i];
        if ((long long)currentMax - suffixMin[i] <= (long long)k) {
            return i;
        }
    }
    return -1;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int FirstStableIndex(int[] nums, int k) {
        int n = nums.Length;
        if (n == 0) return -1;
        int[] suffixMin = new int[n];
        suffixMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffixMin[i] = Math.Min(nums[i], suffixMin[i + 1]);
        }
        int currentMax = nums[0];
        for (int i = 0; i < n; i++) {
            if (nums[i] > currentMax) currentMax = nums[i];
            if ((long)currentMax - suffixMin[i] <= (long)k) {
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
    const suffixMin = new Array(n);
    suffixMin[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        suffixMin[i] = Math.min(nums[i], suffixMin[i + 1]);
    }
    let currentMax = nums[0];
    for (let i = 0; i < n; i++) {
        if (nums[i] > currentMax) currentMax = nums[i];
        if (currentMax - suffixMin[i] <= k) {
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
    const n = nums.length;
    const suffixMin: number[] = new Array(n).fill(0);
    suffixMin[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        suffixMin[i] = Math.min(nums[i], suffixMin[i + 1]);
    }
    let currentMax = nums[0];
    for (let i = 0; i < n; i++) {
        currentMax = Math.max(currentMax, nums[i]);
        if (currentMax - suffixMin[i] <= k) {
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
        $suffixMin = array_fill(0, $n, 0);
        $suffixMin[$n - 1] = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) {
            $suffixMin[$i] = min($nums[$i], $suffixMin[$i + 1]);
        }
        $currentMax = $nums[0];
        for ($i = 0; $i < $n; $i++) {
            $currentMax = max($currentMax, $nums[$i]);
            if ($currentMax - $suffixMin[$i] <= $k) {
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
        var suffixMin = Array(repeating: 0, count: n)
        suffixMin[n - 1] = nums[n - 1]
        if n > 1 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                suffixMin[i] = min(nums[i], suffixMin[i + 1])
            }
        }
        var currentMax = nums[0]
        for i in 0..<n {
            currentMax = max(currentMax, nums[i])
            if currentMax - suffixMin[i] <= k {
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
        val suffixMin = IntArray(n)
        suffixMin[n - 1] = nums[n - 1]
        for (i in n - 2 downTo 0) {
            suffixMin[i] = if (nums[i] < suffixMin[i + 1]) nums[i] else suffixMin[i + 1]
        }
        var currentMax = nums[0]
        for (i in 0 until n) {
            if (nums[i] > currentMax) {
                currentMax = nums[i]
            }
            if (currentMax.toLong() - suffixMin[i].toLong() <= k.toLong()) {
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
    List<int> suffixMin = List.filled(n, 0);
    suffixMin[n - 1] = nums[n - 1];
    for (int i = n - 2; i >= 0; i--) {
      suffixMin[i] = nums[i] < suffixMin[i + 1] ? nums[i] : suffixMin[i + 1];
    }
    int currentMax = nums[0];
    for (int i = 0; i < n; i++) {
      if (nums[i] > currentMax) {
        currentMax = nums[i];
      }
      if (currentMax - suffixMin[i] <= k) {
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
    suffixMin := make([]int, n)
    suffixMin[n-1] = nums[n-1]
    for i := n - 2; i >= 0; i-- {
        if nums[i] < suffixMin[i+1] {
            suffixMin[i] = nums[i]
        } else {
            suffixMin[i] = suffixMin[i+1]
        }
    }
    currentMax := nums[0]
    for i := 0; i < n; i++ {
        if nums[i] > currentMax {
            currentMax = nums[i]
        }
        if currentMax-suffixMin[i] <= k {
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
def first_stable_index(nums, k)
  n = nums.length
  return -1 if n == 0

  prefix_max = Array.new(n)
  suffix_min = Array.new(n)

  cur_max = nums[0]
  (0...n).each do |i|
    cur_max = nums[i] if nums[i] > cur_max
    prefix_max[i] = cur_max
  end

  cur_min = nums[n - 1]
  (n - 1).step(0, -1) do |i|
    cur_min = nums[i] if nums[i] < cur_min
    suffix_min[i] = cur_min
  end

  (0...n).each do |i|
    return i if prefix_max[i] - suffix_min[i] <= k
  end
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
        val prefixMax = new Array[Int](n)
        val suffixMin = new Array[Int](n)

        var curMax = nums(0)
        for (i <- 0 until n) {
            if (nums(i) > curMax) curMax = nums(i)
            prefixMax(i) = curMax
        }

        var curMin = nums(n - 1)
        for (i <- n - 1 to 0 by -1) {
            if (nums(i) < curMin) curMin = nums(i)
            suffixMin(i) = curMin
        }

        for (i <- 0 until n) {
            if (prefixMax(i).toLong - suffixMin(i).toLong <= k.toLong) {
                return i
            }
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
        let mut prefix_max = vec![0; n];
        let mut suffix_min = vec![0; n];

        let mut cur_max = nums[0];
        for i in 0..n {
            if nums[i] > cur_max {
                cur_max = nums[i];
            }
            prefix_max[i] = cur_max;
        }

        let mut cur_min = nums[n - 1];
        for i in (0..n).rev() {
            if nums[i] < cur_min {
                cur_min = nums[i];
            }
            suffix_min[i] = cur_min;
        }

        for i in 0..n {
            if (prefix_max[i] as i64) - (suffix_min[i] as i64) <= k as i64 {
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
  (if (null? nums)
      -1
      (let* ([prefix-max (let loop ([xs (cdr nums)] [cur (car nums)] [acc (list (car nums))])
                           (if (null? xs)
                               (reverse acc)
                               (let ([new-max (max cur (car xs))])
                                 (loop (cdr xs) new-max (cons new-max acc)))))]
             [rev-nums (reverse nums)]
             [suffix-min (let loop ([xs (cdr rev-nums)] [cur (car rev-nums)] [acc (list (car rev-nums))])
                           (if (null? xs)
                               acc
                               (let ([new-min (min cur (car xs))])
                                 (loop (cdr xs) new-min (cons new-min acc)))))])
        (let loop-find ([i 0] [pm prefix-max] [sm suffix-min])
          (cond
            [(null? pm) -1]
            [(<= (- (car pm) (car sm)) k) i]
            [else (loop-find (+ i 1) (cdr pm) (cdr sm))])))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec first_stable_index(Nums :: [integer()], K :: integer()) -> integer().
first_stable_index(Nums, K) ->
    PrefixMax = get_prefix_max(Nums),
    SuffixMin = get_suffix_min(lists:reverse(Nums)),
    find_first(PrefixMax, SuffixMin, K, 0).

get_prefix_max([H|T]) -> get_prefix_max(T, H, [H]).
get_prefix_max([], _, Acc) -> lists:reverse(Acc);
get_prefix_max([H|T], Cur, Acc) ->
    NewMax = erlang:max(Cur, H),
    get_prefix_max(T, NewMax, [NewMax|Acc]).

get_suffix_min([H|T]) -> get_suffix_min(T, H, [H]).
get_suffix_min([], _, Acc) -> Acc;
get_suffix_min([H|T], Cur, Acc) ->
    NewMin = erlang:min(Cur, H),
    get_suffix_min(T, NewMin, [NewMin|Acc]).

find_first([], [], _, _) -> -1;
find_first([PM|PMT], [SM|SMT], K, I) ->
    if PM - SM =< K -> I;
       true -> find_first(PMT, SMT, K, I + 1)
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
    prefix_max = Enum.scan(nums, &max/2)
    suffix_min = nums |> Enum.reverse() |> Enum.scan(&min/2) |> Enum.reverse()

    Enum.zip(prefix_max, suffix_min)
    |> Enum.find_index(fn {p_max, s_min} -> p_max - s_min <= k end)
    |> case do
      nil -> -1
      index -> index
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the array. The algorithm performs one backward pass to compute the suffix minimums and one forward pass to find the first index satisfying the stability condition, resulting in linear time complexity.
- **Space Complexity:** O(n) to store the suffix minimums array. While we track the prefix maximum using only a single variable, the auxiliary array for suffix minimums is necessary to allow O(1) score calculation at each index.
