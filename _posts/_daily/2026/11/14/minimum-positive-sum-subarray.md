---
layout: post
title: "Minimum Positive Sum Subarray "
date: 2026-11-14 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Sliding Window", "Prefix Sum"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/minimum-positive-sum-subarray/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumSumSubarray(vector<int>& nums,\
        \ int l, int r) {\n        int n = nums.size();\n        int minSum = -1;\n\n\
        \        for (int i = 0; i < n; ++i) {\n            int currentSum = 0;\n  \
        \          for (int j = i; j < n; ++j) {\n                currentSum += nums[j];\n\
        \                int len = j - i + 1;\n                if (len > r) break;\n\
        \                if (len >= l && currentSum > 0) {\n                    if (minSum\
        \ == -1 || currentSum < minSum) {\n                        minSum = currentSum;\n\
        \                    }\n                }\n            }\n        }\n      \
        \  return minSum;\n    }\n};"
      java: "class Solution {\n    public int minimumSumSubarray(List<Integer> nums,\
        \ int l, int r) {\n        int n = nums.size();\n        int minSum = -1;\n\n\
        \        for (int i = 0; i < n; i++) {\n            int currentSum = 0;\n  \
        \          for (int j = i; j < n; j++) {\n                currentSum += nums.get(j);\n\
        \                int len = j - i + 1;\n                if (len > r) break;\n\
        \                if (len >= l && currentSum > 0) {\n                    if (minSum\
        \ == -1 || currentSum < minSum) {\n                        minSum = currentSum;\n\
        \                    }\n                }\n            }\n        }\n      \
        \  return minSum;\n    }\n}"
      python: "class Solution(object):\n    def minimumSumSubarray(self, nums, l, r):\n\
        \        \"\"\"\n        :type nums: List[int]\n        :type l: int\n     \
        \   :type r: int\n        :rtype: int\n        \"\"\"\n        n = len(nums)\n\
        \        min_sum = -1\n        for i in range(n):\n            current_sum =\
        \ 0\n            for j in range(i, n):\n                current_sum += nums[j]\n\
        \                length = j - i + 1\n                if length > r:\n      \
        \              break\n                if length >= l and current_sum > 0:\n\
        \                    if min_sum == -1 or current_sum < min_sum:\n          \
        \              min_sum = current_sum\n        return min_sum"
      python3: "class Solution:\n    def minimumSumSubarray(self, nums: List[int], l:\
        \ int, r: int) -> int:\n        n = len(nums)\n        min_sum = -1\n      \
        \  for i in range(n):\n            current_sum = 0\n            for j in range(i,\
        \ n):\n                current_sum += nums[j]\n                length = j -\
        \ i + 1\n                if length > r:\n                    break\n       \
        \         if length >= l and current_sum > 0:\n                    if min_sum\
        \ == -1 or current_sum < min_sum:\n                        min_sum = current_sum\n\
        \        return min_sum"
      c: "int minimumSumSubarray(int* nums, int numsSize, int l, int r) {\n    int minSum\
        \ = -1;\n    for (int i = 0; i < numsSize; i++) {\n        int currentSum =\
        \ 0;\n        for (int j = i; j < numsSize; j++) {\n            currentSum +=\
        \ nums[j];\n            int len = j - i + 1;\n            if (len > r) break;\n\
        \            if (len >= l && currentSum > 0) {\n                if (minSum ==\
        \ -1 || currentSum < minSum) {\n                    minSum = currentSum;\n \
        \               }\n            }\n        }\n    }\n    return minSum;\n}"
      csharp: "public class Solution {\n    public int MinimumSumSubarray(IList<int>\
        \ nums, int l, int r) {\n        int n = nums.Count;\n        int minSum = -1;\n\
        \        for (int i = 0; i < n; i++) {\n            int currentSum = 0;\n  \
        \          for (int j = i; j < n; j++) {\n                currentSum += nums[j];\n\
        \                int len = j - i + 1;\n                if (len > r) break;\n\
        \                if (len >= l && currentSum > 0) {\n                    if (minSum\
        \ == -1 || currentSum < minSum) {\n                        minSum = currentSum;\n\
        \                    }\n                }\n            }\n        }\n      \
        \  return minSum;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} l\n * @param {number}\
        \ r\n * @return {number}\n */\nvar minimumSumSubarray = function(nums, l, r)\
        \ {\n    let n = nums.length;\n    let minSum = -1;\n    for (let i = 0; i <\
        \ n; i++) {\n        let currentSum = 0;\n        for (let j = i; j < n; j++)\
        \ {\n            currentSum += nums[j];\n            let len = j - i + 1;\n\
        \            if (len > r) break;\n            if (len >= l && currentSum > 0)\
        \ {\n                if (minSum === -1 || currentSum < minSum) {\n         \
        \           minSum = currentSum;\n                }\n            }\n       \
        \ }\n    }\n    return minSum;\n};"
      typescript: "function minimumSumSubarray(nums: number[], l: number, r: number):\
        \ number {\n    const n = nums.length;\n    let minSum = -1;\n    for (let i\
        \ = 0; i < n; i++) {\n        let currentSum = 0;\n        for (let j = i; j\
        \ < n; j++) {\n            currentSum += nums[j];\n            const length\
        \ = j - i + 1;\n            if (length > r) {\n                break;\n    \
        \        }\n            if (length >= l && currentSum > 0) {\n             \
        \   if (minSum === -1 || currentSum < minSum) {\n                    minSum\
        \ = currentSum;\n                }\n            }\n        }\n    }\n    return\
        \ minSum;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $l\n     * @param Integer $r\n     * @return Integer\n     */\n  \
        \  function minimumSumSubarray($nums, $l, $r) {\n        $n = count($nums);\n\
        \        $minSum = -1;\n        for ($i = 0; $i < $n; $i++) {\n            $currentSum\
        \ = 0;\n            for ($j = $i; $j < $n; $j++) {\n                $currentSum\
        \ += $nums[$j];\n                $length = $j - $i + 1;\n                if\
        \ ($length > $r) {\n                    break;\n                }\n        \
        \        if ($length >= $l && $currentSum > 0) {\n                    if ($minSum\
        \ == -1 || $currentSum < $minSum) {\n                        $minSum = $currentSum;\n\
        \                    }\n                }\n            }\n        }\n      \
        \  return $minSum;\n    }\n}"
      swift: "class Solution {\n    func minimumSumSubarray(_ nums: [Int], _ l: Int,\
        \ _ r: Int) -> Int {\n        let n = nums.count\n        var minSum = -1\n\
        \        for i in 0..<n {\n            var currentSum = 0\n            for j\
        \ in i..<n {\n                currentSum += nums[j]\n                let length\
        \ = j - i + 1\n                if length > r {\n                    break\n\
        \                }\n                if length >= l && currentSum > 0 {\n   \
        \                 if minSum == -1 || currentSum < minSum {\n               \
        \         minSum = currentSum\n                    }\n                }\n  \
        \          }\n        }\n        return minSum\n    }\n}"
      kotlin: "class Solution {\n    fun minimumSumSubarray(nums: List<Int>, l: Int,\
        \ r: Int): Int {\n        val n = nums.size\n        var minSum = -1\n     \
        \   for (i in 0 until n) {\n            var currentSum = 0\n            for\
        \ (j in i until n) {\n                currentSum += nums[j]\n              \
        \  val length = j - i + 1\n                if (length > r) {\n             \
        \       break\n                }\n                if (length >= l && currentSum\
        \ > 0) {\n                    if (minSum == -1 || currentSum < minSum) {\n \
        \                       minSum = currentSum\n                    }\n       \
        \         }\n            }\n        }\n        return minSum\n    }\n}"
      dart: "class Solution {\n  int minimumSumSubarray(List<int> nums, int l, int r)\
        \ {\n    int n = nums.length;\n    int minSum = -1;\n    for (int i = 0; i <\
        \ n; i++) {\n      int currentSum = 0;\n      for (int j = i; j < n; j++) {\n\
        \        currentSum += nums[j];\n        int length = j - i + 1;\n        if\
        \ (length > r) {\n          break;\n        }\n        if (length >= l && currentSum\
        \ > 0) {\n          if (minSum == -1 || currentSum < minSum) {\n           \
        \ minSum = currentSum;\n          }\n        }\n      }\n    }\n    return minSum;\n\
        \  }\n}"
      go: "func minimumSumSubarray(nums []int, l int, r int) int {\n    n := len(nums)\n\
        \    minSum := -1\n    for i := 0; i < n; i++ {\n        currentSum := 0\n \
        \       for j := i; j < n; j++ {\n            currentSum += nums[j]\n      \
        \      length := j - i + 1\n            if length > r {\n                break\n\
        \            }\n            if length >= l && currentSum > 0 {\n           \
        \     if minSum == -1 || currentSum < minSum {\n                    minSum =\
        \ currentSum\n                }\n            }\n        }\n    }\n    return\
        \ minSum\n}"
      ruby: "def minimum_sum_subarray(nums, l, r)\n  n = nums.length\n  min_sum = -1\n\
        \  (0...n).each do |i|\n    current_sum = 0\n    (i...n).each do |j|\n     \
        \ current_sum += nums[j]\n      length = j - i + 1\n      break if length >\
        \ r\n      if length >= l && current_sum > 0\n        if min_sum == -1 || current_sum\
        \ < min_sum\n          min_sum = current_sum\n        end\n      end\n    end\n\
        \  end\n  min_sum\nend"
      scala: "object Solution {\n    def minimumSumSubarray(nums: List[Int], l: Int,\
        \ r: Int): Int = {\n        val n = nums.length\n        val numsArr = nums.toArray\n\
        \        var minSum = -1\n        for (i <- 0 until n) {\n            var currentSum\
        \ = 0\n            var j = i\n            var stopInner = false\n          \
        \  while (j < n && !stopInner) {\n                currentSum += numsArr(j)\n\
        \                val len = j - i + 1\n                if (len > r) {\n     \
        \               stopInner = true\n                } else {\n               \
        \     if (len >= l && currentSum > 0) {\n                        if (minSum\
        \ == -1 || currentSum < minSum) {\n                            minSum = currentSum\n\
        \                        }\n                    }\n                    j +=\
        \ 1\n                }\n            }\n        }\n        minSum\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_sum_subarray(nums: Vec<i32>, l: i32,\
        \ r: i32) -> i32 {\n        let n = nums.len();\n        let mut min_sum = -1;\n\
        \        for i in 0..n {\n            let mut current_sum = 0;\n           \
        \ for j in i..n {\n                current_sum += nums[j];\n               \
        \ let length = (j - i + 1) as i32;\n                if length > r {\n      \
        \              break;\n                }\n                if length >= l &&\
        \ current_sum > 0 {\n                    if min_sum == -1 || current_sum < min_sum\
        \ {\n                        min_sum = current_sum;\n                    }\n\
        \                }\n            }\n        }\n        min_sum\n    }\n}"
      racket: "(define/contract (minimum-sum-subarray nums l r)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer? exact-integer?)\n  (let* ([n (length nums)]\n\
        \         [arr (list->vector nums)]\n         [min-sum -1])\n    (for ([i (in-range\
        \ n)])\n      (let loop ([j i] [current-sum 0])\n        (when (< j n)\n   \
        \       (let* ([new-sum (+ current-sum (vector-ref arr j))]\n              \
        \   [len (+ (- j i) 1)])\n            (cond\n              [(> len r) (void)]\n\
        \              [else\n               (when (and (>= len l) (> new-sum 0))\n\
        \                 (if (or (= min-sum -1) (< new-sum min-sum))\n            \
        \         (set! min-sum new-sum)\n                     (void)))\n          \
        \     (loop (+ j 1) new-sum)])))))\n    min-sum))"
      erlang: "-spec minimum_sum_subarray(Nums :: [integer()], L :: integer(), R ::\
        \ integer()) -> integer().\nminimum_sum_subarray(Nums, L, R) ->\n    NumsArr\
        \ = list_to_tuple(Nums),\n    N = tuple_size(NumsArr),\n    outer_loop(1, N,\
        \ L, R, NumsArr, -1).\n\nouter_loop(I, N, L, R, Arr, MinSum) when I =< N ->\n\
        \    NewMinSum = inner_loop(I, I, N, L, R, Arr, 0, MinSum),\n    outer_loop(I\
        \ + 1, N, L, R, Arr, NewMinSum);\nouter_loop(_, _, _, _, _, MinSum) ->\n   \
        \ MinSum.\n\ninner_loop(I, J, N, L, R, Arr, CurrentSum, MinSum) when J =< N\
        \ ->\n    NewSum = CurrentSum + element(J, Arr),\n    Len = J - I + 1,\n   \
        \ if\n        Len > R -> MinSum;\n        Len >= L, NewSum > 0 ->\n        \
        \    NewMinSum = if\n                MinSum =:= -1 -> NewSum;\n            \
        \    NewSum < MinSum -> NewSum;\n                true -> MinSum\n          \
        \  end,\n            inner_loop(I, J + 1, N, L, R, Arr, NewSum, NewMinSum);\n\
        \        true ->\n            inner_loop(I, J + 1, N, L, R, Arr, NewSum, MinSum)\n\
        \    end;\ninner_loop(_, _, _, _, _, _, _, MinSum) ->\n    MinSum."
      elixir: "defmodule Solution do\n  @spec minimum_sum_subarray(nums :: [integer],\
        \ l :: integer, r :: integer) :: integer\n  def minimum_sum_subarray(nums, l,\
        \ r) do\n    nums_tuple = List.to_tuple(nums)\n    n = tuple_size(nums_tuple)\n\
        \n    Enum.reduce(0..(n - 1), -1, fn i, min_sum ->\n      {_, final_min} = Enum.reduce_while(i..(n\
        \ - 1), {0, min_sum}, fn j, {current_sum, current_min} ->\n        val = elem(nums_tuple,\
        \ j)\n        new_sum = current_sum + val\n        len = j - i + 1\n       \
        \ if len > r do\n          {:halt, {new_sum, current_min}}\n        else\n \
        \         new_min = if len >= l and new_sum > 0 do\n            if current_min\
        \ == -1 or new_sum < current_min, do: new_sum, else: current_min\n         \
        \ else\n            current_min\n          end\n          {:cont, {new_sum,\
        \ new_min}}\n        end\n      end)\n      final_min\n    end)\n  end\nend"
    approach: 'The algorithm utilizes a nested loop strategy to explore all possible
      contiguous subarrays within the given range of lengths $[l, r]$. By iterating
      through each potential starting index in the array and incrementally building
      subarrays, we can maintain a running sum of the current subarray''s elements.
      This approach avoids redundant calculations by adding the next element to the
      existing sum as the subarray extends, effectively evaluating each subarray in
      constant time during the expansion process.


      For each generated subarray, the algorithm evaluates whether its length falls
      within the inclusive range $[l, r]$ and if its calculated sum is strictly greater
      than 0. If both criteria are met, the algorithm updates a tracking variable with
      the minimum positive sum encountered so far. If no such subarray exists after
      inspecting all valid start and end positions, the function returns -1, ensuring
      that the solution handles the absence of valid subarrays correctly.'
    time_complexity: 'O(n^2). The algorithm consists of two nested loops: the outer
      loop iterates over every possible starting position (up to $n$ times), and the
      inner loop iterates over potential ending positions until the subarray length
      exceeds $r$. Since $r \le n$, the total number of subarrays checked is at most
      $n(n+1)/2$, which results in a quadratic complexity.'
    space_complexity: O(1). The solution only uses a fixed number of auxiliary variables,
      such as the current running sum and the minimum sum found, regardless of the input
      array size. No additional data structures proportional to the input are allocated.
    elapsed_time: 110.05821657180786
    model: gemini-3-flash-preview
    generated_at: '2026-11-14 04:23:17 '
---

## Problem #3364: Minimum Positive Sum Subarray 

**Difficulty:** Easy

**Topics:** Array, Sliding Window, Prefix Sum

## Problem Description

<p>You are given an integer array <code>nums</code> and <strong>two</strong> integers <code>l</code> and <code>r</code>. Your task is to find the <strong>minimum</strong> sum of a <strong>subarray</strong> whose size is between <code>l</code> and <code>r</code> (inclusive) and whose sum is greater than 0.</p>

<p>Return the <strong>minimum</strong> sum of such a subarray. If no such subarray exists, return -1.</p>

<p>A <strong>subarray</strong> is a contiguous <b>non-empty</b> sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3, -2, 1, 4], l = 2, r = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The subarrays of length between <code>l = 2</code> and <code>r = 3</code> where the sum is greater than 0 are:</p>

<ul>
	<li><code>[3, -2]</code> with a sum of 1</li>
	<li><code>[1, 4]</code> with a sum of 5</li>
	<li><code>[3, -2, 1]</code> with a sum of 2</li>
	<li><code>[-2, 1, 4]</code> with a sum of 3</li>
</ul>

<p>Out of these, the subarray <code>[3, -2]</code> has a sum of 1, which is the smallest positive sum. Hence, the answer is 1.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [-2, 2, -3, 1], l = 2, r = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no subarray of length between <code>l</code> and <code>r</code> that has a sum greater than 0. So, the answer is -1.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1, 2, 3, 4], l = 2, r = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The subarray <code>[1, 2]</code> has a length of 2 and the minimum sum greater than 0. So, the answer is 3.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= l &lt;= r &lt;= nums.length</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## Hints

1. Check every subarray, since constraints are small.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm utilizes a nested loop strategy to explore all possible contiguous subarrays within the given range of lengths $[l, r]$. By iterating through each potential starting index in the array and incrementally building subarrays, we can maintain a running sum of the current subarray's elements. This approach avoids redundant calculations by adding the next element to the existing sum as the subarray extends, effectively evaluating each subarray in constant time during the expansion process.

For each generated subarray, the algorithm evaluates whether its length falls within the inclusive range $[l, r]$ and if its calculated sum is strictly greater than 0. If both criteria are met, the algorithm updates a tracking variable with the minimum positive sum encountered so far. If no such subarray exists after inspecting all valid start and end positions, the function returns -1, ensuring that the solution handles the absence of valid subarrays correctly.

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
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int n = nums.size();
        int minSum = -1;

        for (int i = 0; i < n; ++i) {
            int currentSum = 0;
            for (int j = i; j < n; ++j) {
                currentSum += nums[j];
                int len = j - i + 1;
                if (len > r) break;
                if (len >= l && currentSum > 0) {
                    if (minSum == -1 || currentSum < minSum) {
                        minSum = currentSum;
                    }
                }
            }
        }
        return minSum;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minimumSumSubarray(List<Integer> nums, int l, int r) {
        int n = nums.size();
        int minSum = -1;

        for (int i = 0; i < n; i++) {
            int currentSum = 0;
            for (int j = i; j < n; j++) {
                currentSum += nums.get(j);
                int len = j - i + 1;
                if (len > r) break;
                if (len >= l && currentSum > 0) {
                    if (minSum == -1 || currentSum < minSum) {
                        minSum = currentSum;
                    }
                }
            }
        }
        return minSum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n = len(nums)
        min_sum = -1
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                length = j - i + 1
                if length > r:
                    break
                if length >= l and current_sum > 0:
                    if min_sum == -1 or current_sum < min_sum:
                        min_sum = current_sum
        return min_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = -1
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                length = j - i + 1
                if length > r:
                    break
                if length >= l and current_sum > 0:
                    if min_sum == -1 or current_sum < min_sum:
                        min_sum = current_sum
        return min_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minimumSumSubarray(int* nums, int numsSize, int l, int r) {
    int minSum = -1;
    for (int i = 0; i < numsSize; i++) {
        int currentSum = 0;
        for (int j = i; j < numsSize; j++) {
            currentSum += nums[j];
            int len = j - i + 1;
            if (len > r) break;
            if (len >= l && currentSum > 0) {
                if (minSum == -1 || currentSum < minSum) {
                    minSum = currentSum;
                }
            }
        }
    }
    return minSum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinimumSumSubarray(IList<int> nums, int l, int r) {
        int n = nums.Count;
        int minSum = -1;
        for (int i = 0; i < n; i++) {
            int currentSum = 0;
            for (int j = i; j < n; j++) {
                currentSum += nums[j];
                int len = j - i + 1;
                if (len > r) break;
                if (len >= l && currentSum > 0) {
                    if (minSum == -1 || currentSum < minSum) {
                        minSum = currentSum;
                    }
                }
            }
        }
        return minSum;
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
 * @param {number} l
 * @param {number} r
 * @return {number}
 */
var minimumSumSubarray = function(nums, l, r) {
    let n = nums.length;
    let minSum = -1;
    for (let i = 0; i < n; i++) {
        let currentSum = 0;
        for (let j = i; j < n; j++) {
            currentSum += nums[j];
            let len = j - i + 1;
            if (len > r) break;
            if (len >= l && currentSum > 0) {
                if (minSum === -1 || currentSum < minSum) {
                    minSum = currentSum;
                }
            }
        }
    }
    return minSum;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumSumSubarray(nums: number[], l: number, r: number): number {
    const n = nums.length;
    let minSum = -1;
    for (let i = 0; i < n; i++) {
        let currentSum = 0;
        for (let j = i; j < n; j++) {
            currentSum += nums[j];
            const length = j - i + 1;
            if (length > r) {
                break;
            }
            if (length >= l && currentSum > 0) {
                if (minSum === -1 || currentSum < minSum) {
                    minSum = currentSum;
                }
            }
        }
    }
    return minSum;
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
     * @param Integer $l
     * @param Integer $r
     * @return Integer
     */
    function minimumSumSubarray($nums, $l, $r) {
        $n = count($nums);
        $minSum = -1;
        for ($i = 0; $i < $n; $i++) {
            $currentSum = 0;
            for ($j = $i; $j < $n; $j++) {
                $currentSum += $nums[$j];
                $length = $j - $i + 1;
                if ($length > $r) {
                    break;
                }
                if ($length >= $l && $currentSum > 0) {
                    if ($minSum == -1 || $currentSum < $minSum) {
                        $minSum = $currentSum;
                    }
                }
            }
        }
        return $minSum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumSumSubarray(_ nums: [Int], _ l: Int, _ r: Int) -> Int {
        let n = nums.count
        var minSum = -1
        for i in 0..<n {
            var currentSum = 0
            for j in i..<n {
                currentSum += nums[j]
                let length = j - i + 1
                if length > r {
                    break
                }
                if length >= l && currentSum > 0 {
                    if minSum == -1 || currentSum < minSum {
                        minSum = currentSum
                    }
                }
            }
        }
        return minSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumSumSubarray(nums: List<Int>, l: Int, r: Int): Int {
        val n = nums.size
        var minSum = -1
        for (i in 0 until n) {
            var currentSum = 0
            for (j in i until n) {
                currentSum += nums[j]
                val length = j - i + 1
                if (length > r) {
                    break
                }
                if (length >= l && currentSum > 0) {
                    if (minSum == -1 || currentSum < minSum) {
                        minSum = currentSum
                    }
                }
            }
        }
        return minSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumSumSubarray(List<int> nums, int l, int r) {
    int n = nums.length;
    int minSum = -1;
    for (int i = 0; i < n; i++) {
      int currentSum = 0;
      for (int j = i; j < n; j++) {
        currentSum += nums[j];
        int length = j - i + 1;
        if (length > r) {
          break;
        }
        if (length >= l && currentSum > 0) {
          if (minSum == -1 || currentSum < minSum) {
            minSum = currentSum;
          }
        }
      }
    }
    return minSum;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumSumSubarray(nums []int, l int, r int) int {
    n := len(nums)
    minSum := -1
    for i := 0; i < n; i++ {
        currentSum := 0
        for j := i; j < n; j++ {
            currentSum += nums[j]
            length := j - i + 1
            if length > r {
                break
            }
            if length >= l && currentSum > 0 {
                if minSum == -1 || currentSum < minSum {
                    minSum = currentSum
                }
            }
        }
    }
    return minSum
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def minimum_sum_subarray(nums, l, r)
  n = nums.length
  min_sum = -1
  (0...n).each do |i|
    current_sum = 0
    (i...n).each do |j|
      current_sum += nums[j]
      length = j - i + 1
      break if length > r
      if length >= l && current_sum > 0
        if min_sum == -1 || current_sum < min_sum
          min_sum = current_sum
        end
      end
    end
  end
  min_sum
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumSumSubarray(nums: List[Int], l: Int, r: Int): Int = {
        val n = nums.length
        val numsArr = nums.toArray
        var minSum = -1
        for (i <- 0 until n) {
            var currentSum = 0
            var j = i
            var stopInner = false
            while (j < n && !stopInner) {
                currentSum += numsArr(j)
                val len = j - i + 1
                if (len > r) {
                    stopInner = true
                } else {
                    if (len >= l && currentSum > 0) {
                        if (minSum == -1 || currentSum < minSum) {
                            minSum = currentSum
                        }
                    }
                    j += 1
                }
            }
        }
        minSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_sum_subarray(nums: Vec<i32>, l: i32, r: i32) -> i32 {
        let n = nums.len();
        let mut min_sum = -1;
        for i in 0..n {
            let mut current_sum = 0;
            for j in i..n {
                current_sum += nums[j];
                let length = (j - i + 1) as i32;
                if length > r {
                    break;
                }
                if length >= l && current_sum > 0 {
                    if min_sum == -1 || current_sum < min_sum {
                        min_sum = current_sum;
                    }
                }
            }
        }
        min_sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-sum-subarray nums l r)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ([n (length nums)]
         [arr (list->vector nums)]
         [min-sum -1])
    (for ([i (in-range n)])
      (let loop ([j i] [current-sum 0])
        (when (< j n)
          (let* ([new-sum (+ current-sum (vector-ref arr j))]
                 [len (+ (- j i) 1)])
            (cond
              [(> len r) (void)]
              [else
               (when (and (>= len l) (> new-sum 0))
                 (if (or (= min-sum -1) (< new-sum min-sum))
                     (set! min-sum new-sum)
                     (void)))
               (loop (+ j 1) new-sum)])))))
    min-sum))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_sum_subarray(Nums :: [integer()], L :: integer(), R :: integer()) -> integer().
minimum_sum_subarray(Nums, L, R) ->
    NumsArr = list_to_tuple(Nums),
    N = tuple_size(NumsArr),
    outer_loop(1, N, L, R, NumsArr, -1).

outer_loop(I, N, L, R, Arr, MinSum) when I =< N ->
    NewMinSum = inner_loop(I, I, N, L, R, Arr, 0, MinSum),
    outer_loop(I + 1, N, L, R, Arr, NewMinSum);
outer_loop(_, _, _, _, _, MinSum) ->
    MinSum.

inner_loop(I, J, N, L, R, Arr, CurrentSum, MinSum) when J =< N ->
    NewSum = CurrentSum + element(J, Arr),
    Len = J - I + 1,
    if
        Len > R -> MinSum;
        Len >= L, NewSum > 0 ->
            NewMinSum = if
                MinSum =:= -1 -> NewSum;
                NewSum < MinSum -> NewSum;
                true -> MinSum
            end,
            inner_loop(I, J + 1, N, L, R, Arr, NewSum, NewMinSum);
        true ->
            inner_loop(I, J + 1, N, L, R, Arr, NewSum, MinSum)
    end;
inner_loop(_, _, _, _, _, _, _, MinSum) ->
    MinSum.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_sum_subarray(nums :: [integer], l :: integer, r :: integer) :: integer
  def minimum_sum_subarray(nums, l, r) do
    nums_tuple = List.to_tuple(nums)
    n = tuple_size(nums_tuple)

    Enum.reduce(0..(n - 1), -1, fn i, min_sum ->
      {_, final_min} = Enum.reduce_while(i..(n - 1), {0, min_sum}, fn j, {current_sum, current_min} ->
        val = elem(nums_tuple, j)
        new_sum = current_sum + val
        len = j - i + 1
        if len > r do
          {:halt, {new_sum, current_min}}
        else
          new_min = if len >= l and new_sum > 0 do
            if current_min == -1 or new_sum < current_min, do: new_sum, else: current_min
          else
            current_min
          end
          {:cont, {new_sum, new_min}}
        end
      end)
      final_min
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n^2). The algorithm consists of two nested loops: the outer loop iterates over every possible starting position (up to $n$ times), and the inner loop iterates over potential ending positions until the subarray length exceeds $r$. Since $r \le n$, the total number of subarrays checked is at most $n(n+1)/2$, which results in a quadratic complexity.
- **Space Complexity:** O(1). The solution only uses a fixed number of auxiliary variables, such as the current running sum and the minimum sum found, regardless of the input array size. No additional data structures proportional to the input are allocated.
