---
layout: post
title: "Removing Minimum and Maximum From Array"
date: 2026-08-30 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Greedy"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/removing-minimum-and-maximum-from-array/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumDeletions(vector<int>& nums) {\n\
        \        int n = nums.size();\n        if (n <= 2) return n;\n        int minIdx\
        \ = 0, maxIdx = 0;\n        for (int i = 1; i < n; ++i) {\n            if (nums[i]\
        \ < nums[minIdx]) minIdx = i;\n            if (nums[i] > nums[maxIdx]) maxIdx\
        \ = i;\n        }\n        int a = std::min(minIdx, maxIdx);\n        int b\
        \ = std::max(minIdx, maxIdx);\n        int opt1 = b + 1;\n        int opt2 =\
        \ n - a;\n        int opt3 = (a + 1) + (n - b);\n        return std::min({opt1,\
        \ opt2, opt3});\n    }\n};"
      java: "class Solution {\n    public int minimumDeletions(int[] nums) {\n     \
        \   int n = nums.length;\n        if (n <= 2) return n;\n        int minIdx\
        \ = 0, maxIdx = 0;\n        for (int i = 1; i < n; i++) {\n            if (nums[i]\
        \ < nums[minIdx]) minIdx = i;\n            if (nums[i] > nums[maxIdx]) maxIdx\
        \ = i;\n        }\n        int a = Math.min(minIdx, maxIdx);\n        int b\
        \ = Math.max(minIdx, maxIdx);\n        int opt1 = b + 1;\n        int opt2 =\
        \ n - a;\n        int opt3 = (a + 1) + (n - b);\n        return Math.min(opt1,\
        \ Math.min(opt2, opt3));\n    }\n}"
      python: "class Solution(object):\n    def minimumDeletions(self, nums):\n    \
        \    \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\
        \"\n        n = len(nums)\n        if n <= 2: return n\n        min_val = min(nums)\n\
        \        max_val = max(nums)\n        min_idx = nums.index(min_val)\n      \
        \  max_idx = nums.index(max_val)\n        a = min(min_idx, max_idx)\n      \
        \  b = max(min_idx, max_idx)\n        return min(b + 1, n - a, (a + 1) + (n\
        \ - b))"
      python3: "class Solution:\n    def minimumDeletions(self, nums: List[int]) ->\
        \ int:\n        n = len(nums)\n        if n <= 2: return n\n        min_idx\
        \ = nums.index(min(nums))\n        max_idx = nums.index(max(nums))\n       \
        \ a, b = min(min_idx, max_idx), max(min_idx, max_idx)\n        return min(b\
        \ + 1, n - a, a + 1 + n - b)"
      c: "int minimumDeletions(int* nums, int numsSize) {\n    if (numsSize <= 2) return\
        \ numsSize;\n    int minIdx = 0, maxIdx = 0;\n    for (int i = 1; i < numsSize;\
        \ i++) {\n        if (nums[i] < nums[minIdx]) minIdx = i;\n        if (nums[i]\
        \ > nums[maxIdx]) maxIdx = i;\n    }\n    int a = minIdx < maxIdx ? minIdx :\
        \ maxIdx;\n    int b = minIdx > maxIdx ? minIdx : maxIdx;\n    int opt1 = b\
        \ + 1;\n    int opt2 = numsSize - a;\n    int opt3 = (a + 1) + (numsSize - b);\n\
        \    int res = opt1 < opt2 ? opt1 : opt2;\n    return res < opt3 ? res : opt3;\n\
        }"
      csharp: "using System;\n\npublic class Solution {\n    public int MinimumDeletions(int[]\
        \ nums) {\n        int n = nums.Length;\n        if (n <= 2) return n;\n\n \
        \       int minIdx = 0, maxIdx = 0;\n        for (int i = 1; i < n; i++) {\n\
        \            if (nums[i] < nums[minIdx]) minIdx = i;\n            if (nums[i]\
        \ > nums[maxIdx]) maxIdx = i;\n        }\n\n        int a = Math.Min(minIdx,\
        \ maxIdx);\n        int b = Math.Max(minIdx, maxIdx);\n\n        int opt1 =\
        \ b + 1;\n        int opt2 = n - a;\n        int opt3 = (a + 1) + (n - b);\n\
        \n        return Math.Min(opt1, Math.Min(opt2, opt3));\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minimumDeletions\
        \ = function(nums) {\n    const n = nums.length;\n    if (n <= 2) return n;\n\
        \n    let minIdx = 0, maxIdx = 0;\n    for (let i = 1; i < n; i++) {\n     \
        \   if (nums[i] < nums[minIdx]) minIdx = i;\n        if (nums[i] > nums[maxIdx])\
        \ maxIdx = i;\n    }\n\n    const a = Math.min(minIdx, maxIdx);\n    const b\
        \ = Math.max(minIdx, maxIdx);\n\n    const opt1 = b + 1;\n    const opt2 = n\
        \ - a;\n    const opt3 = (a + 1) + (n - b);\n\n    return Math.min(opt1, opt2,\
        \ opt3);\n};"
      typescript: "function minimumDeletions(nums: number[]): number {\n    const n\
        \ = nums.length;\n    if (n <= 2) return n;\n\n    let minIdx = 0, maxIdx =\
        \ 0;\n    for (let i = 1; i < n; i++) {\n        if (nums[i] < nums[minIdx])\
        \ minIdx = i;\n        if (nums[i] > nums[maxIdx]) maxIdx = i;\n    }\n\n  \
        \  const a = Math.min(minIdx, maxIdx);\n    const b = Math.max(minIdx, maxIdx);\n\
        \n    const opt1 = b + 1;\n    const opt2 = n - a;\n    const opt3 = (a + 1)\
        \ + (n - b);\n\n    return Math.min(opt1, opt2, opt3);\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function minimumDeletions($nums) {\n        $n = count($nums);\n\
        \        if ($n <= 2) return $n;\n\n        $minIdx = 0;\n        $maxIdx =\
        \ 0;\n        for ($i = 1; $i < $n; $i++) {\n            if ($nums[$i] < $nums[$minIdx])\
        \ $minIdx = $i;\n            if ($nums[$i] > $nums[$maxIdx]) $maxIdx = $i;\n\
        \        }\n\n        $a = min($minIdx, $maxIdx);\n        $b = max($minIdx,\
        \ $maxIdx);\n\n        $opt1 = $b + 1;\n        $opt2 = $n - $a;\n        $opt3\
        \ = ($a + 1) + ($n - $b);\n\n        return min($opt1, $opt2, $opt3);\n    }\n\
        }"
      swift: "class Solution {\n    func minimumDeletions(_ nums: [Int]) -> Int {\n\
        \        let n = nums.count\n        if n <= 2 { return n }\n\n        var minIdx\
        \ = 0\n        var maxIdx = 0\n        for i in 1..<n {\n            if nums[i]\
        \ < nums[minIdx] { minIdx = i }\n            if nums[i] > nums[maxIdx] { maxIdx\
        \ = i }\n        }\n\n        let a = min(minIdx, maxIdx)\n        let b = max(minIdx,\
        \ maxIdx)\n\n        let opt1 = b + 1\n        let opt2 = n - a\n        let\
        \ opt3 = (a + 1) + (n - b)\n\n        return min(opt1, min(opt2, opt3))\n  \
        \  }\n}"
      kotlin: "class Solution {\n    fun minimumDeletions(nums: IntArray): Int {\n \
        \       val n = nums.size\n        if (n <= 2) return n\n\n        var minIdx\
        \ = 0\n        var maxIdx = 0\n        for (k in 1 until n) {\n            if\
        \ (nums[k] < nums[minIdx]) minIdx = k\n            if (nums[k] > nums[maxIdx])\
        \ maxIdx = k\n        }\n\n        val i = if (minIdx < maxIdx) minIdx else\
        \ maxIdx\n        val j = if (minIdx > maxIdx) minIdx else maxIdx\n\n      \
        \  val opt1 = j + 1\n        val opt2 = n - i\n        val opt3 = (i + 1) +\
        \ (n - j)\n\n        return minOf(opt1, minOf(opt2, opt3))\n    }\n}"
      dart: "class Solution {\n  int minimumDeletions(List<int> nums) {\n    int n =\
        \ nums.length;\n    if (n <= 2) return n;\n\n    int minIdx = 0;\n    int maxIdx\
        \ = 0;\n    for (int k = 1; k < n; k++) {\n      if (nums[k] < nums[minIdx])\
        \ minIdx = k;\n      if (nums[k] > nums[maxIdx]) maxIdx = k;\n    }\n\n    int\
        \ i = minIdx < maxIdx ? minIdx : maxIdx;\n    int j = minIdx > maxIdx ? minIdx\
        \ : maxIdx;\n\n    int opt1 = j + 1;\n    int opt2 = n - i;\n    int opt3 =\
        \ (i + 1) + (n - j);\n\n    int res = opt1 < opt2 ? opt1 : opt2;\n    return\
        \ res < opt3 ? res : opt3;\n  }\n}"
      go: "func minimumDeletions(nums []int) int {\n    n := len(nums)\n    if n <=\
        \ 2 {\n        return n\n    }\n\n    minIdx, maxIdx := 0, 0\n    for k := 1;\
        \ k < n; k++ {\n        if nums[k] < nums[minIdx] {\n            minIdx = k\n\
        \        }\n        if nums[k] > nums[maxIdx] {\n            maxIdx = k\n  \
        \      }\n    }\n\n    i, j := minIdx, maxIdx\n    if i > j {\n        i, j\
        \ = j, i\n    }\n\n    opt1 := j + 1\n    opt2 := n - i\n    opt3 := (i + 1)\
        \ + (n - j)\n\n    res := opt1\n    if opt2 < res {\n        res = opt2\n  \
        \  }\n    if opt3 < res {\n        res = opt3\n    }\n    return res\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef minimum_deletions(nums)\n\
        \    n = nums.length\n    return n if n <= 2\n\n    min_val = nums[0]\n    max_val\
        \ = nums[0]\n    min_idx = 0\n    max_idx = 0\n\n    nums.each_with_index do\
        \ |num, idx|\n        if num < min_val\n            min_val = num\n        \
        \    min_idx = idx\n        end\n        if num > max_val\n            max_val\
        \ = num\n            max_idx = idx\n        end\n    end\n\n    i = min_idx\
        \ < max_idx ? min_idx : max_idx\n    j = min_idx > max_idx ? min_idx : max_idx\n\
        \n    opt1 = j + 1\n    opt2 = n - i\n    opt3 = (i + 1) + (n - j)\n\n    [opt1,\
        \ opt2, opt3].min\nend"
      scala: "object Solution {\n    def minimumDeletions(nums: Array[Int]): Int = {\n\
        \        val n = nums.length\n        if (n <= 2) return n\n\n        var minIdx\
        \ = 0\n        var maxIdx = 0\n        for (k <- 1 until n) {\n            if\
        \ (nums(k) < nums(minIdx)) minIdx = k\n            if (nums(k) > nums(maxIdx))\
        \ maxIdx = k\n        }\n\n        val i = Math.min(minIdx, maxIdx)\n      \
        \  val j = Math.max(minIdx, maxIdx)\n\n        val opt1 = j + 1\n        val\
        \ opt2 = n - i\n        val opt3 = (i + 1) + (n - j)\n\n        Math.min(opt1,\
        \ Math.min(opt2, opt3))\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_deletions(nums: Vec<i32>) -> i32 {\n\
        \        let n = nums.len();\n        if n == 1 {\n            return 1;\n \
        \       }\n\n        let mut min_idx = 0;\n        let mut max_idx = 0;\n\n\
        \        for idx in 0..n {\n            if nums[idx] < nums[min_idx] {\n   \
        \             min_idx = idx;\n            }\n            if nums[idx] > nums[max_idx]\
        \ {\n                max_idx = idx;\n            }\n        }\n\n        let\
        \ i = if min_idx < max_idx { min_idx } else { max_idx };\n        let j = if\
        \ min_idx > max_idx { min_idx } else { max_idx };\n\n        let scenario1 =\
        \ j + 1;\n        let scenario2 = n - i;\n        let scenario3 = (i + 1) +\
        \ (n - j);\n\n        let result = std::cmp::min(scenario1, std::cmp::min(scenario2,\
        \ scenario3));\n        result as i32\n    }\n}"
      racket: "(define/contract (minimum-deletions nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let* ([len (length nums)]\n         [first-val (car nums)])\n\
        \    (let-values ([(final-mv final-mi final-Mv final-Mi)\n                 \
        \ (for/fold ([mv first-val] [mi 0] [Mv first-val] [Mi 0])\n                \
        \            ([val (in-list nums)] [idx (in-naturals)])\n                  \
        \  (let ([nmv (if (< val mv) val mv)]\n                          [nmi (if (<\
        \ val mv) idx mi)]\n                          [nMv (if (> val Mv) val Mv)]\n\
        \                          [nMi (if (> val Mv) idx Mi)])\n                 \
        \     (values nmv nmi nMv nMi)))])\n      (let ([idx-i (if (< final-mi final-Mi)\
        \ final-mi final-Mi)]\n            [idx-j (if (> final-mi final-Mi) final-mi\
        \ final-Mi)])\n        (min (+ idx-j 1)\n             (- len idx-i)\n      \
        \       (+ (+ idx-i 1) (- len idx-j)))))))"
      erlang: "-spec minimum_deletions(Nums :: [integer()]) -> integer().\nminimum_deletions(Nums)\
        \ ->\n    N = length(Nums),\n    [H|T] = Nums,\n    {MinI, MaxI} = find_indices(T,\
        \ 1, H, 0, H, 0),\n    {I, J} = if MinI < MaxI -> {MinI, MaxI}; true -> {MaxI,\
        \ MinI} end,\n    S1 = J + 1,\n    S2 = N - I,\n    S3 = (I + 1) + (N - J),\n\
        \    lists:min([S1, S2, S3]).\n\nfind_indices([], _Pos, _MinV, MinI, _MaxV,\
        \ MaxI) ->\n    {MinI, MaxI};\nfind_indices([H|T], Pos, MinV, MinI, MaxV, MaxI)\
        \ ->\n    {NMinV, NMinI} = if H < MinV -> {H, Pos}; true -> {MinV, MinI} end,\n\
        \    {NMaxV, NMaxI} = if H > MaxV -> {H, Pos}; true -> {MaxV, MaxI} end,\n \
        \   find_indices(T, Pos + 1, NMinV, NMinI, NMaxV, NMaxI)."
      elixir: "defmodule Solution do\n  @spec minimum_deletions(nums :: [integer]) ::\
        \ integer\n  def minimum_deletions(nums) do\n    n = length(nums)\n    indexed\
        \ = Enum.with_index(nums)\n    {{_min_v, min_idx}, {_max_v, max_idx}} = Enum.min_max_by(indexed,\
        \ fn {v, _i} -> v end)\n\n    i = min(min_idx, max_idx)\n    j = max(min_idx,\
        \ max_idx)\n\n    s1 = j + 1\n    s2 = n - i\n    s3 = (i + 1) + (n - j)\n\n\
        \    Enum.min([s1, s2, s3])\n  end\nend"
    approach: 'The core strategy for solving this problem involves identifying the indices
      of the minimum and maximum elements in the array and then evaluating the three
      possible ways to remove them. Since the array contains distinct integers, there
      is exactly one minimum and one maximum. Let $n$ be the length of the array, and
      let $a$ and $b$ be the indices of these two target elements such that $a < b$.
      The goal is to find the minimum number of deletions from the ends (front or back)
      to include both indices in the set of removed elements.


      There are three potential scenarios to remove both elements: 1) Both elements
      are removed from the front, which requires $b + 1$ deletions. 2) Both elements
      are removed from the back, requiring $n - a$ deletions. 3) One element is removed
      from the front and the other from the back, requiring $(a + 1) + (n - b)$ deletions.
      By calculating the cost of each scenario and taking the minimum, we determine
      the most efficient approach. This logic covers all cases, including when the minimum
      and maximum are adjacent or when they are at opposite ends of the array.'
    time_complexity: O(n) because finding the minimum and maximum elements and their
      indices requires traversing the array exactly once (or a constant number of times).
      The subsequent calculation of the three scenarios and their minimum is performed
      in O(1) time.
    space_complexity: O(1) as we only store a few integer variables for the indices
      and the length of the array, independent of the input size.
    elapsed_time: 203.97956800460815
    model: gemini-3-flash-preview
    generated_at: '2026-08-30 02:52:09 '
---

## Problem #2091: Removing Minimum and Maximum From Array

**Difficulty:** Medium

**Topics:** Array, Greedy

## Problem Description

<p>You are given a <strong>0-indexed</strong> array of <strong>distinct</strong> integers <code>nums</code>.</p>

<p>There is an element in <code>nums</code> that has the <strong>lowest</strong> value and an element that has the <strong>highest</strong> value. We call them the <strong>minimum</strong> and <strong>maximum</strong> respectively. Your goal is to remove <strong>both</strong> these elements from the array.</p>

<p>A <strong>deletion</strong> is defined as either removing an element from the <strong>front</strong> of the array or removing an element from the <strong>back</strong> of the array.</p>

<p>Return <em>the <strong>minimum</strong> number of deletions it would take to remove <strong>both</strong> the minimum and maximum element from the array.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,<u><strong>10</strong></u>,7,5,4,<u><strong>1</strong></u>,8,6]
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
The minimum element in the array is nums[5], which is 1.
The maximum element in the array is nums[1], which is 10.
We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
This results in 2 + 3 = 5 deletions, which is the minimum number possible.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,<u><strong>-4</strong></u>,<u><strong>19</strong></u>,1,8,-2,-3,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
The minimum element in the array is nums[1], which is -4.
The maximum element in the array is nums[2], which is 19.
We can remove both the minimum and maximum by removing 3 elements from the front.
This results in only 3 deletions, which is the minimum number possible.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [<u><strong>101</strong></u>]
<strong>Output:</strong> 1
<strong>Explanation:</strong>  
There is only one element in the array, which makes it both the minimum and maximum element.
We can remove it with 1 deletion.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li>The integers in <code>nums</code> are <strong>distinct</strong>.</li>
</ul>


## Hints

1. There can only be three scenarios for deletions such that both minimum and maximum elements are removed:

2. Scenario 1: Both elements are removed by only deleting from the front.

3. Scenario 2: Both elements are removed by only deleting from the back.

4. Scenario 3: Delete from the front to remove one of the elements, and delete from the back to remove the other element.

5. Compare which of the three scenarios results in the minimum number of moves.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core strategy for solving this problem involves identifying the indices of the minimum and maximum elements in the array and then evaluating the three possible ways to remove them. Since the array contains distinct integers, there is exactly one minimum and one maximum. Let $n$ be the length of the array, and let $a$ and $b$ be the indices of these two target elements such that $a < b$. The goal is to find the minimum number of deletions from the ends (front or back) to include both indices in the set of removed elements.

There are three potential scenarios to remove both elements: 1) Both elements are removed from the front, which requires $b + 1$ deletions. 2) Both elements are removed from the back, requiring $n - a$ deletions. 3) One element is removed from the front and the other from the back, requiring $(a + 1) + (n - b)$ deletions. By calculating the cost of each scenario and taking the minimum, we determine the most efficient approach. This logic covers all cases, including when the minimum and maximum are adjacent or when they are at opposite ends of the array.

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
    int minimumDeletions(vector<int>& nums) {
        int n = nums.size();
        if (n <= 2) return n;
        int minIdx = 0, maxIdx = 0;
        for (int i = 1; i < n; ++i) {
            if (nums[i] < nums[minIdx]) minIdx = i;
            if (nums[i] > nums[maxIdx]) maxIdx = i;
        }
        int a = std::min(minIdx, maxIdx);
        int b = std::max(minIdx, maxIdx);
        int opt1 = b + 1;
        int opt2 = n - a;
        int opt3 = (a + 1) + (n - b);
        return std::min({opt1, opt2, opt3});
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minimumDeletions(int[] nums) {
        int n = nums.length;
        if (n <= 2) return n;
        int minIdx = 0, maxIdx = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] < nums[minIdx]) minIdx = i;
            if (nums[i] > nums[maxIdx]) maxIdx = i;
        }
        int a = Math.min(minIdx, maxIdx);
        int b = Math.max(minIdx, maxIdx);
        int opt1 = b + 1;
        int opt2 = n - a;
        int opt3 = (a + 1) + (n - b);
        return Math.min(opt1, Math.min(opt2, opt3));
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2: return n
        min_val = min(nums)
        max_val = max(nums)
        min_idx = nums.index(min_val)
        max_idx = nums.index(max_val)
        a = min(min_idx, max_idx)
        b = max(min_idx, max_idx)
        return min(b + 1, n - a, (a + 1) + (n - b))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2: return n
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        a, b = min(min_idx, max_idx), max(min_idx, max_idx)
        return min(b + 1, n - a, a + 1 + n - b)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minimumDeletions(int* nums, int numsSize) {
    if (numsSize <= 2) return numsSize;
    int minIdx = 0, maxIdx = 0;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < nums[minIdx]) minIdx = i;
        if (nums[i] > nums[maxIdx]) maxIdx = i;
    }
    int a = minIdx < maxIdx ? minIdx : maxIdx;
    int b = minIdx > maxIdx ? minIdx : maxIdx;
    int opt1 = b + 1;
    int opt2 = numsSize - a;
    int opt3 = (a + 1) + (numsSize - b);
    int res = opt1 < opt2 ? opt1 : opt2;
    return res < opt3 ? res : opt3;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int MinimumDeletions(int[] nums) {
        int n = nums.Length;
        if (n <= 2) return n;

        int minIdx = 0, maxIdx = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] < nums[minIdx]) minIdx = i;
            if (nums[i] > nums[maxIdx]) maxIdx = i;
        }

        int a = Math.Min(minIdx, maxIdx);
        int b = Math.Max(minIdx, maxIdx);

        int opt1 = b + 1;
        int opt2 = n - a;
        int opt3 = (a + 1) + (n - b);

        return Math.Min(opt1, Math.Min(opt2, opt3));
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
var minimumDeletions = function(nums) {
    const n = nums.length;
    if (n <= 2) return n;

    let minIdx = 0, maxIdx = 0;
    for (let i = 1; i < n; i++) {
        if (nums[i] < nums[minIdx]) minIdx = i;
        if (nums[i] > nums[maxIdx]) maxIdx = i;
    }

    const a = Math.min(minIdx, maxIdx);
    const b = Math.max(minIdx, maxIdx);

    const opt1 = b + 1;
    const opt2 = n - a;
    const opt3 = (a + 1) + (n - b);

    return Math.min(opt1, opt2, opt3);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumDeletions(nums: number[]): number {
    const n = nums.length;
    if (n <= 2) return n;

    let minIdx = 0, maxIdx = 0;
    for (let i = 1; i < n; i++) {
        if (nums[i] < nums[minIdx]) minIdx = i;
        if (nums[i] > nums[maxIdx]) maxIdx = i;
    }

    const a = Math.min(minIdx, maxIdx);
    const b = Math.max(minIdx, maxIdx);

    const opt1 = b + 1;
    const opt2 = n - a;
    const opt3 = (a + 1) + (n - b);

    return Math.min(opt1, opt2, opt3);
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
    function minimumDeletions($nums) {
        $n = count($nums);
        if ($n <= 2) return $n;

        $minIdx = 0;
        $maxIdx = 0;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] < $nums[$minIdx]) $minIdx = $i;
            if ($nums[$i] > $nums[$maxIdx]) $maxIdx = $i;
        }

        $a = min($minIdx, $maxIdx);
        $b = max($minIdx, $maxIdx);

        $opt1 = $b + 1;
        $opt2 = $n - $a;
        $opt3 = ($a + 1) + ($n - $b);

        return min($opt1, $opt2, $opt3);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumDeletions(_ nums: [Int]) -> Int {
        let n = nums.count
        if n <= 2 { return n }

        var minIdx = 0
        var maxIdx = 0
        for i in 1..<n {
            if nums[i] < nums[minIdx] { minIdx = i }
            if nums[i] > nums[maxIdx] { maxIdx = i }
        }

        let a = min(minIdx, maxIdx)
        let b = max(minIdx, maxIdx)

        let opt1 = b + 1
        let opt2 = n - a
        let opt3 = (a + 1) + (n - b)

        return min(opt1, min(opt2, opt3))
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumDeletions(nums: IntArray): Int {
        val n = nums.size
        if (n <= 2) return n

        var minIdx = 0
        var maxIdx = 0
        for (k in 1 until n) {
            if (nums[k] < nums[minIdx]) minIdx = k
            if (nums[k] > nums[maxIdx]) maxIdx = k
        }

        val i = if (minIdx < maxIdx) minIdx else maxIdx
        val j = if (minIdx > maxIdx) minIdx else maxIdx

        val opt1 = j + 1
        val opt2 = n - i
        val opt3 = (i + 1) + (n - j)

        return minOf(opt1, minOf(opt2, opt3))
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumDeletions(List<int> nums) {
    int n = nums.length;
    if (n <= 2) return n;

    int minIdx = 0;
    int maxIdx = 0;
    for (int k = 1; k < n; k++) {
      if (nums[k] < nums[minIdx]) minIdx = k;
      if (nums[k] > nums[maxIdx]) maxIdx = k;
    }

    int i = minIdx < maxIdx ? minIdx : maxIdx;
    int j = minIdx > maxIdx ? minIdx : maxIdx;

    int opt1 = j + 1;
    int opt2 = n - i;
    int opt3 = (i + 1) + (n - j);

    int res = opt1 < opt2 ? opt1 : opt2;
    return res < opt3 ? res : opt3;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumDeletions(nums []int) int {
    n := len(nums)
    if n <= 2 {
        return n
    }

    minIdx, maxIdx := 0, 0
    for k := 1; k < n; k++ {
        if nums[k] < nums[minIdx] {
            minIdx = k
        }
        if nums[k] > nums[maxIdx] {
            maxIdx = k
        }
    }

    i, j := minIdx, maxIdx
    if i > j {
        i, j = j, i
    }

    opt1 := j + 1
    opt2 := n - i
    opt3 := (i + 1) + (n - j)

    res := opt1
    if opt2 < res {
        res = opt2
    }
    if opt3 < res {
        res = opt3
    }
    return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def minimum_deletions(nums)
    n = nums.length
    return n if n <= 2

    min_val = nums[0]
    max_val = nums[0]
    min_idx = 0
    max_idx = 0

    nums.each_with_index do |num, idx|
        if num < min_val
            min_val = num
            min_idx = idx
        end
        if num > max_val
            max_val = num
            max_idx = idx
        end
    end

    i = min_idx < max_idx ? min_idx : max_idx
    j = min_idx > max_idx ? min_idx : max_idx

    opt1 = j + 1
    opt2 = n - i
    opt3 = (i + 1) + (n - j)

    [opt1, opt2, opt3].min
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumDeletions(nums: Array[Int]): Int = {
        val n = nums.length
        if (n <= 2) return n

        var minIdx = 0
        var maxIdx = 0
        for (k <- 1 until n) {
            if (nums(k) < nums(minIdx)) minIdx = k
            if (nums(k) > nums(maxIdx)) maxIdx = k
        }

        val i = Math.min(minIdx, maxIdx)
        val j = Math.max(minIdx, maxIdx)

        val opt1 = j + 1
        val opt2 = n - i
        val opt3 = (i + 1) + (n - j)

        Math.min(opt1, Math.min(opt2, opt3))
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_deletions(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 1 {
            return 1;
        }

        let mut min_idx = 0;
        let mut max_idx = 0;

        for idx in 0..n {
            if nums[idx] < nums[min_idx] {
                min_idx = idx;
            }
            if nums[idx] > nums[max_idx] {
                max_idx = idx;
            }
        }

        let i = if min_idx < max_idx { min_idx } else { max_idx };
        let j = if min_idx > max_idx { min_idx } else { max_idx };

        let scenario1 = j + 1;
        let scenario2 = n - i;
        let scenario3 = (i + 1) + (n - j);

        let result = std::cmp::min(scenario1, std::cmp::min(scenario2, scenario3));
        result as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-deletions nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([len (length nums)]
         [first-val (car nums)])
    (let-values ([(final-mv final-mi final-Mv final-Mi)
                  (for/fold ([mv first-val] [mi 0] [Mv first-val] [Mi 0])
                            ([val (in-list nums)] [idx (in-naturals)])
                    (let ([nmv (if (< val mv) val mv)]
                          [nmi (if (< val mv) idx mi)]
                          [nMv (if (> val Mv) val Mv)]
                          [nMi (if (> val Mv) idx Mi)])
                      (values nmv nmi nMv nMi)))])
      (let ([idx-i (if (< final-mi final-Mi) final-mi final-Mi)]
            [idx-j (if (> final-mi final-Mi) final-mi final-Mi)])
        (min (+ idx-j 1)
             (- len idx-i)
             (+ (+ idx-i 1) (- len idx-j)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_deletions(Nums :: [integer()]) -> integer().
minimum_deletions(Nums) ->
    N = length(Nums),
    [H|T] = Nums,
    {MinI, MaxI} = find_indices(T, 1, H, 0, H, 0),
    {I, J} = if MinI < MaxI -> {MinI, MaxI}; true -> {MaxI, MinI} end,
    S1 = J + 1,
    S2 = N - I,
    S3 = (I + 1) + (N - J),
    lists:min([S1, S2, S3]).

find_indices([], _Pos, _MinV, MinI, _MaxV, MaxI) ->
    {MinI, MaxI};
find_indices([H|T], Pos, MinV, MinI, MaxV, MaxI) ->
    {NMinV, NMinI} = if H < MinV -> {H, Pos}; true -> {MinV, MinI} end,
    {NMaxV, NMaxI} = if H > MaxV -> {H, Pos}; true -> {MaxV, MaxI} end,
    find_indices(T, Pos + 1, NMinV, NMinI, NMaxV, NMaxI).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_deletions(nums :: [integer]) :: integer
  def minimum_deletions(nums) do
    n = length(nums)
    indexed = Enum.with_index(nums)
    {{_min_v, min_idx}, {_max_v, max_idx}} = Enum.min_max_by(indexed, fn {v, _i} -> v end)

    i = min(min_idx, max_idx)
    j = max(min_idx, max_idx)

    s1 = j + 1
    s2 = n - i
    s3 = (i + 1) + (n - j)

    Enum.min([s1, s2, s3])
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) because finding the minimum and maximum elements and their indices requires traversing the array exactly once (or a constant number of times). The subsequent calculation of the three scenarios and their minimum is performed in O(1) time.
- **Space Complexity:** O(1) as we only store a few integer variables for the indices and the length of the array, independent of the input size.
