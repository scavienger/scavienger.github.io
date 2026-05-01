---
layout: post
title: "Rotate Function"
date: 2026-05-01 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Dynamic Programming"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/rotate-function/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxRotateFunction(vector<int>& nums)\
        \ {\n        int n = nums.size();\n        long long totalSum = 0;\n       \
        \ long long currentF = 0;\n        for (int i = 0; i < n; i++) {\n         \
        \   totalSum += (long long)nums[i];\n            currentF += (long long)i *\
        \ nums[i];\n        }\n        long long maxF = currentF;\n        for (int\
        \ i = 1; i < n; i++) {\n            currentF = currentF + totalSum - (long long)n\
        \ * nums[n - i];\n            if (currentF > maxF) {\n                maxF =\
        \ currentF;\n            }\n        }\n        return (int)maxF;\n    }\n};"
      java: "class Solution {\n    public int maxRotateFunction(int[] nums) {\n    \
        \    int n = nums.length;\n        long totalSum = 0;\n        long currentF\
        \ = 0;\n        for (int i = 0; i < n; i++) {\n            totalSum += nums[i];\n\
        \            currentF += (long) i * nums[i];\n        }\n        long maxF =\
        \ currentF;\n        for (int i = 1; i < n; i++) {\n            currentF = currentF\
        \ + totalSum - (long) n * nums[n - i];\n            if (currentF > maxF) {\n\
        \                maxF = currentF;\n            }\n        }\n        return\
        \ (int) maxF;\n    }\n}"
      python: "class Solution(object):\n    def maxRotateFunction(self, nums):\n   \
        \     \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\
        \"\"\n        n = len(nums)\n        total_sum = sum(nums)\n        current_f\
        \ = sum(i * x for i, x in enumerate(nums))\n        max_f = current_f\n    \
        \    for i in range(1, n):\n            current_f = current_f + total_sum -\
        \ n * nums[n - i]\n            if current_f > max_f:\n                max_f\
        \ = current_f\n        return max_f"
      python3: "class Solution:\n    def maxRotateFunction(self, nums: List[int]) ->\
        \ int:\n        n = len(nums)\n        total_sum = sum(nums)\n        current_f\
        \ = sum(i * x for i, x in enumerate(nums))\n        max_f = current_f\n    \
        \    for i in range(1, n):\n            current_f = current_f + total_sum -\
        \ n * nums[n - i]\n            if current_f > max_f:\n                max_f\
        \ = current_f\n        return max_f"
      c: "int maxRotateFunction(int* nums, int numsSize) {\n    long long totalSum =\
        \ 0;\n    long long currentF = 0;\n    for (int i = 0; i < numsSize; i++) {\n\
        \        totalSum += (long long)nums[i];\n        currentF += (long long)i *\
        \ nums[i];\n    }\n    long long maxF = currentF;\n    for (int i = 1; i < numsSize;\
        \ i++) {\n        currentF = currentF + totalSum - (long long)numsSize * nums[numsSize\
        \ - i];\n        if (currentF > maxF) {\n            maxF = currentF;\n    \
        \    }\n    }\n    return (int)maxF;\n}"
      csharp: "public class Solution {\n    public int MaxRotateFunction(int[] nums)\
        \ {\n        int n = nums.Length;\n        long sum = 0;\n        long f = 0;\n\
        \        for (int i = 0; i < n; i++) {\n            sum += nums[i];\n      \
        \      f += (long)i * nums[i];\n        }\n        long maxF = f;\n        for\
        \ (int i = n - 1; i >= 1; i--) {\n            f = f + sum - (long)n * nums[i];\n\
        \            if (f > maxF) {\n                maxF = f;\n            }\n   \
        \     }\n        return (int)maxF;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar maxRotateFunction\
        \ = function(nums) {\n    var n = nums.length;\n    var sum = 0;\n    var f\
        \ = 0;\n    for (var i = 0; i < n; i++) {\n        sum += nums[i];\n       \
        \ f += i * nums[i];\n    }\n    var maxF = f;\n    for (var i = n - 1; i >=\
        \ 1; i--) {\n        f = f + sum - n * nums[i];\n        if (f > maxF) {\n \
        \           maxF = f;\n        }\n    }\n    return maxF;\n};"
      typescript: "function maxRotateFunction(nums: number[]): number {\n    const n\
        \ = nums.length;\n    let sum = 0;\n    let f = 0;\n    for (let i = 0; i <\
        \ n; i++) {\n        sum += nums[i];\n        f += i * nums[i];\n    }\n   \
        \ let maxF = f;\n    for (let i = n - 1; i >= 1; i--) {\n        f = f + sum\
        \ - n * nums[i];\n        if (f > maxF) {\n            maxF = f;\n        }\n\
        \    }\n    return maxF;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function maxRotateFunction($nums) {\n        $n = count($nums);\n\
        \        $sum = 0;\n        $f = 0;\n        for ($i = 0; $i < $n; $i++) {\n\
        \            $sum += $nums[$i];\n            $f += $i * $nums[$i];\n       \
        \ }\n        $maxF = $f;\n        for ($i = $n - 1; $i >= 1; $i--) {\n     \
        \       $f = $f + $sum - $n * $nums[$i];\n            if ($f > $maxF) {\n  \
        \              $maxF = $f;\n            }\n        }\n        return (int)$maxF;\n\
        \    }\n}"
      swift: "class Solution {\n    func maxRotateFunction(_ nums: [Int]) -> Int {\n\
        \        let n = nums.count\n        if n == 0 {\n            return 0\n   \
        \     }\n        var sum = 0\n        var f = 0\n        for i in 0..<n {\n\
        \            sum += nums[i]\n            f += i * nums[i]\n        }\n     \
        \   var maxF = f\n        if n > 1 {\n            for i in (1..<n).reversed()\
        \ {\n                f = f + sum - n * nums[i]\n                if f > maxF\
        \ {\n                    maxF = f\n                }\n            }\n      \
        \  }\n        return maxF\n    }\n}"
      kotlin: "class Solution {\n    fun maxRotateFunction(nums: IntArray): Int {\n\
        \        val n = nums.size\n        var sum: Long = 0\n        var f: Long =\
        \ 0\n        for (i in 0 until n) {\n            sum += nums[i].toLong()\n \
        \           f += i.toLong() * nums[i]\n        }\n\n        var maxF = f\n \
        \       for (i in n - 1 downTo 1) {\n            f = f + sum - n.toLong() *\
        \ nums[i]\n            if (f > maxF) {\n                maxF = f\n         \
        \   }\n        }\n\n        return maxF.toInt()\n    }\n}"
      dart: "class Solution {\n  int maxRotateFunction(List<int> nums) {\n    int n\
        \ = nums.length;\n    int sum = 0;\n    int f = 0;\n    for (int i = 0; i <\
        \ n; i++) {\n      sum += nums[i];\n      f += i * nums[i];\n    }\n\n    int\
        \ maxF = f;\n    for (int i = n - 1; i >= 1; i--) {\n      f = f + sum - n *\
        \ nums[i];\n      if (f > maxF) {\n        maxF = f;\n      }\n    }\n\n   \
        \ return maxF;\n  }\n}"
      go: "func maxRotateFunction(nums []int) int {\n    n := len(nums)\n    sum :=\
        \ 0\n    f := 0\n    for i, val := range nums {\n        sum += val\n      \
        \  f += i * val\n    }\n\n    maxF := f\n    for i := n - 1; i >= 1; i-- {\n\
        \        f = f + sum - n*nums[i]\n        if f > maxF {\n            maxF =\
        \ f\n        }\n    }\n\n    return maxF\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef max_rotate_function(nums)\n\
        \    n = nums.length\n    sum = 0\n    f = 0\n    nums.each_with_index do |val,\
        \ i|\n        sum += val\n        f += i * val\n    end\n\n    max_f = f\n \
        \   (n - 1).downto(1) do |i|\n        f = f + sum - n * nums[i]\n        max_f\
        \ = f if f > max_f\n    end\n\n    max_f\nend"
      scala: "object Solution {\n    def maxRotateFunction(nums: Array[Int]): Int =\
        \ {\n        val n = nums.length\n        var sum: Long = 0\n        var f:\
        \ Long = 0\n        for (i <- 0 until n) {\n            sum += nums(i).toLong\n\
        \            f += i.toLong * nums(i)\n        }\n\n        var maxF = f\n  \
        \      for (i <- n - 1 until 0 by -1) {\n            f = f + sum - n.toLong\
        \ * nums(i)\n            if (f > maxF) {\n                maxF = f\n       \
        \     }\n        }\n\n        maxF.toInt\n    }\n}"
      rust: "impl Solution {\n    pub fn max_rotate_function(nums: Vec<i32>) -> i32\
        \ {\n        let n = nums.len() as i64;\n        let mut sum: i64 = 0;\n   \
        \     let mut f: i64 = 0;\n        for (i, &num) in nums.iter().enumerate()\
        \ {\n            let num_64 = num as i64;\n            sum += num_64;\n    \
        \        f += (i as i64) * num_64;\n        }\n\n        let mut max_f = f;\n\
        \        let n_usize = nums.len();\n        for i in 1..n_usize {\n        \
        \    f = f + sum - n * (nums[n_usize - i] as i64);\n            if f > max_f\
        \ {\n                max_f = f;\n            }\n        }\n        max_f as\
        \ i32\n    }\n}"
      racket: "(define/contract (max-rotate-function nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let* ([v (list->vector nums)]\n         [n (vector-length\
        \ v)]\n         [sum (for/fold ([s 0]) ([x nums]) (+ s x))]\n         [f0 (for/fold\
        \ ([f 0]) ([i (in-range n)]) (+ f (* i (vector-ref v i))))])\n    (let loop\
        \ ([k 1] [f f0] [max-f f0])\n      (if (= k n)\n          max-f\n          (let\
        \ ([next-f (+ f (- sum (* n (vector-ref v (- n k)))))])\n            (loop (+\
        \ k 1) next-f (max max-f next-f)))))))"
      erlang: "-spec max_rotate_function(Nums :: [integer()]) -> integer().\nmax_rotate_function(Nums)\
        \ ->\n    N = length(Nums),\n    Sum = lists:sum(Nums),\n    {F0, _} = lists:foldl(fun(X,\
        \ {Acc, I}) -> {Acc + X * I, I + 1} end, {0, 0}, Nums),\n    Vec = list_to_tuple(Nums),\n\
        \    Loop = fun Loop(K, F, MaxF) ->\n        if\n            K >= N -> MaxF;\n\
        \            true ->\n                NextF = F + Sum - N * element(N - K +\
        \ 1, Vec),\n                Loop(K + 1, NextF, if NextF > MaxF -> NextF; true\
        \ -> MaxF end)\n        end\n    end,\n    Loop(1, F0, F0)."
      elixir: "defmodule Solution do\n  @spec max_rotate_function(nums :: [integer])\
        \ :: integer\n  def max_rotate_function(nums) do\n    n = length(nums)\n   \
        \ sum = Enum.sum(nums)\n    f0 = nums\n         |> Enum.with_index()\n     \
        \    |> Enum.reduce(0, fn {val, i}, acc -> acc + val * i end)\n\n    nums_tuple\
        \ = List.to_tuple(nums)\n\n    if n > 1 do\n      Enum.reduce(1..(n - 1), {f0,\
        \ f0}, fn k, {curr_f, max_f} ->\n        next_f = curr_f + sum - n * elem(nums_tuple,\
        \ n - k)\n        {next_f, max(max_f, next_f)}\n      end)\n      |> elem(1)\n\
        \    else\n      f0\n    end\n  end\nend"
    approach: 'The problem asks for the maximum value of the rotation function F(k),
      which can be solved efficiently using a dynamic programming-like approach. Instead
      of recalculating F(k) for each rotation in $O(n^2)$ time, we derive a mathematical
      relationship between F(k) and F(k-1). By comparing the terms of F(k) and F(k-1),
      we observe that during a clockwise rotation, every element''s multiplier increases
      by 1, except for the element that was at the last position, which moves to the
      front and has its multiplier change from $n-1$ to 0. This leads to the recurrence
      relation: $F(k) = F(k-1) + \text{totalSum} - n \cdot nums[n-k]$.


      To implement this, we first calculate the total sum of the elements in the array
      and the initial rotation function value $F(0)$. We then iterate from $k = 1$ to
      $n-1$, updating the function value in $O(1)$ time per step using the derived formula.
      Because the intermediate sums and rotation values can exceed the range of a 32-bit
      signed integer (up to $10^{12}$), we use 64-bit integers (long or long long) for
      these calculations to prevent overflow, then return the maximum value found as
      an integer.'
    time_complexity: 'O(n) with one-paragraph explanation: The algorithm consists of
      two linear passes over the array. The first pass calculates the sum of the elements
      and the initial value $F(0)$, and the second pass iteratively calculates the remaining
      $n-1$ rotation values using the recurrence relation. Both passes take $O(n)$ time.'
    space_complexity: 'O(1) with one-paragraph explanation: The solution uses only a
      constant amount of extra space to store variables for the total sum, the current
      rotation function value, and the maximum value encountered during the iterations.
      No auxiliary data structures are required.'
    elapsed_time: 165.74358582496643
    model: gemini-3-flash-preview
    generated_at: '2026-05-01 02:28:35 '
---

## Problem #396: Rotate Function

**Difficulty:** Medium

**Topics:** Array, Math, Dynamic Programming

## Problem Description

<p>You are given an integer array <code>nums</code> of length <code>n</code>.</p>

<p>Assume <code>arr<sub>k</sub></code> to be an array obtained by rotating <code>nums</code> by <code>k</code> positions clock-wise. We define the <strong>rotation function</strong> <code>F</code> on <code>nums</code> as follow:</p>

<ul>
	<li><code>F(k) = 0 * arr<sub>k</sub>[0] + 1 * arr<sub>k</sub>[1] + ... + (n - 1) * arr<sub>k</sub>[n - 1].</code></li>
</ul>

<p>Return <em>the maximum value of</em> <code>F(0), F(1), ..., F(n-1)</code>.</p>

<p>The test cases are generated so that the answer fits in a <strong>32-bit</strong> integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,3,2,6]
<strong>Output:</strong> 26
<strong>Explanation:</strong>
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [100]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the maximum value of the rotation function F(k), which can be solved efficiently using a dynamic programming-like approach. Instead of recalculating F(k) for each rotation in $O(n^2)$ time, we derive a mathematical relationship between F(k) and F(k-1). By comparing the terms of F(k) and F(k-1), we observe that during a clockwise rotation, every element's multiplier increases by 1, except for the element that was at the last position, which moves to the front and has its multiplier change from $n-1$ to 0. This leads to the recurrence relation: $F(k) = F(k-1) + \text{totalSum} - n \cdot nums[n-k]$.

To implement this, we first calculate the total sum of the elements in the array and the initial rotation function value $F(0)$. We then iterate from $k = 1$ to $n-1$, updating the function value in $O(1)$ time per step using the derived formula. Because the intermediate sums and rotation values can exceed the range of a 32-bit signed integer (up to $10^{12}$), we use 64-bit integers (long or long long) for these calculations to prevent overflow, then return the maximum value found as an integer.

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
    int maxRotateFunction(vector<int>& nums) {
        int n = nums.size();
        long long totalSum = 0;
        long long currentF = 0;
        for (int i = 0; i < n; i++) {
            totalSum += (long long)nums[i];
            currentF += (long long)i * nums[i];
        }
        long long maxF = currentF;
        for (int i = 1; i < n; i++) {
            currentF = currentF + totalSum - (long long)n * nums[n - i];
            if (currentF > maxF) {
                maxF = currentF;
            }
        }
        return (int)maxF;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxRotateFunction(int[] nums) {
        int n = nums.length;
        long totalSum = 0;
        long currentF = 0;
        for (int i = 0; i < n; i++) {
            totalSum += nums[i];
            currentF += (long) i * nums[i];
        }
        long maxF = currentF;
        for (int i = 1; i < n; i++) {
            currentF = currentF + totalSum - (long) n * nums[n - i];
            if (currentF > maxF) {
                maxF = currentF;
            }
        }
        return (int) maxF;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = sum(nums)
        current_f = sum(i * x for i, x in enumerate(nums))
        max_f = current_f
        for i in range(1, n):
            current_f = current_f + total_sum - n * nums[n - i]
            if current_f > max_f:
                max_f = current_f
        return max_f
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        current_f = sum(i * x for i, x in enumerate(nums))
        max_f = current_f
        for i in range(1, n):
            current_f = current_f + total_sum - n * nums[n - i]
            if current_f > max_f:
                max_f = current_f
        return max_f
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maxRotateFunction(int* nums, int numsSize) {
    long long totalSum = 0;
    long long currentF = 0;
    for (int i = 0; i < numsSize; i++) {
        totalSum += (long long)nums[i];
        currentF += (long long)i * nums[i];
    }
    long long maxF = currentF;
    for (int i = 1; i < numsSize; i++) {
        currentF = currentF + totalSum - (long long)numsSize * nums[numsSize - i];
        if (currentF > maxF) {
            maxF = currentF;
        }
    }
    return (int)maxF;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxRotateFunction(int[] nums) {
        int n = nums.Length;
        long sum = 0;
        long f = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            f += (long)i * nums[i];
        }
        long maxF = f;
        for (int i = n - 1; i >= 1; i--) {
            f = f + sum - (long)n * nums[i];
            if (f > maxF) {
                maxF = f;
            }
        }
        return (int)maxF;
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
var maxRotateFunction = function(nums) {
    var n = nums.length;
    var sum = 0;
    var f = 0;
    for (var i = 0; i < n; i++) {
        sum += nums[i];
        f += i * nums[i];
    }
    var maxF = f;
    for (var i = n - 1; i >= 1; i--) {
        f = f + sum - n * nums[i];
        if (f > maxF) {
            maxF = f;
        }
    }
    return maxF;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxRotateFunction(nums: number[]): number {
    const n = nums.length;
    let sum = 0;
    let f = 0;
    for (let i = 0; i < n; i++) {
        sum += nums[i];
        f += i * nums[i];
    }
    let maxF = f;
    for (let i = n - 1; i >= 1; i--) {
        f = f + sum - n * nums[i];
        if (f > maxF) {
            maxF = f;
        }
    }
    return maxF;
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
    function maxRotateFunction($nums) {
        $n = count($nums);
        $sum = 0;
        $f = 0;
        for ($i = 0; $i < $n; $i++) {
            $sum += $nums[$i];
            $f += $i * $nums[$i];
        }
        $maxF = $f;
        for ($i = $n - 1; $i >= 1; $i--) {
            $f = $f + $sum - $n * $nums[$i];
            if ($f > $maxF) {
                $maxF = $f;
            }
        }
        return (int)$maxF;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxRotateFunction(_ nums: [Int]) -> Int {
        let n = nums.count
        if n == 0 {
            return 0
        }
        var sum = 0
        var f = 0
        for i in 0..<n {
            sum += nums[i]
            f += i * nums[i]
        }
        var maxF = f
        if n > 1 {
            for i in (1..<n).reversed() {
                f = f + sum - n * nums[i]
                if f > maxF {
                    maxF = f
                }
            }
        }
        return maxF
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxRotateFunction(nums: IntArray): Int {
        val n = nums.size
        var sum: Long = 0
        var f: Long = 0
        for (i in 0 until n) {
            sum += nums[i].toLong()
            f += i.toLong() * nums[i]
        }

        var maxF = f
        for (i in n - 1 downTo 1) {
            f = f + sum - n.toLong() * nums[i]
            if (f > maxF) {
                maxF = f
            }
        }

        return maxF.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxRotateFunction(List<int> nums) {
    int n = nums.length;
    int sum = 0;
    int f = 0;
    for (int i = 0; i < n; i++) {
      sum += nums[i];
      f += i * nums[i];
    }

    int maxF = f;
    for (int i = n - 1; i >= 1; i--) {
      f = f + sum - n * nums[i];
      if (f > maxF) {
        maxF = f;
      }
    }

    return maxF;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxRotateFunction(nums []int) int {
    n := len(nums)
    sum := 0
    f := 0
    for i, val := range nums {
        sum += val
        f += i * val
    }

    maxF := f
    for i := n - 1; i >= 1; i-- {
        f = f + sum - n*nums[i]
        if f > maxF {
            maxF = f
        }
    }

    return maxF
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def max_rotate_function(nums)
    n = nums.length
    sum = 0
    f = 0
    nums.each_with_index do |val, i|
        sum += val
        f += i * val
    end

    max_f = f
    (n - 1).downto(1) do |i|
        f = f + sum - n * nums[i]
        max_f = f if f > max_f
    end

    max_f
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxRotateFunction(nums: Array[Int]): Int = {
        val n = nums.length
        var sum: Long = 0
        var f: Long = 0
        for (i <- 0 until n) {
            sum += nums(i).toLong
            f += i.toLong * nums(i)
        }

        var maxF = f
        for (i <- n - 1 until 0 by -1) {
            f = f + sum - n.toLong * nums(i)
            if (f > maxF) {
                maxF = f
            }
        }

        maxF.toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_rotate_function(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i64;
        let mut sum: i64 = 0;
        let mut f: i64 = 0;
        for (i, &num) in nums.iter().enumerate() {
            let num_64 = num as i64;
            sum += num_64;
            f += (i as i64) * num_64;
        }

        let mut max_f = f;
        let n_usize = nums.len();
        for i in 1..n_usize {
            f = f + sum - n * (nums[n_usize - i] as i64);
            if f > max_f {
                max_f = f;
            }
        }
        max_f as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-rotate-function nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([v (list->vector nums)]
         [n (vector-length v)]
         [sum (for/fold ([s 0]) ([x nums]) (+ s x))]
         [f0 (for/fold ([f 0]) ([i (in-range n)]) (+ f (* i (vector-ref v i))))])
    (let loop ([k 1] [f f0] [max-f f0])
      (if (= k n)
          max-f
          (let ([next-f (+ f (- sum (* n (vector-ref v (- n k)))))])
            (loop (+ k 1) next-f (max max-f next-f)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_rotate_function(Nums :: [integer()]) -> integer().
max_rotate_function(Nums) ->
    N = length(Nums),
    Sum = lists:sum(Nums),
    {F0, _} = lists:foldl(fun(X, {Acc, I}) -> {Acc + X * I, I + 1} end, {0, 0}, Nums),
    Vec = list_to_tuple(Nums),
    Loop = fun Loop(K, F, MaxF) ->
        if
            K >= N -> MaxF;
            true ->
                NextF = F + Sum - N * element(N - K + 1, Vec),
                Loop(K + 1, NextF, if NextF > MaxF -> NextF; true -> MaxF end)
        end
    end,
    Loop(1, F0, F0).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_rotate_function(nums :: [integer]) :: integer
  def max_rotate_function(nums) do
    n = length(nums)
    sum = Enum.sum(nums)
    f0 = nums
         |> Enum.with_index()
         |> Enum.reduce(0, fn {val, i}, acc -> acc + val * i end)

    nums_tuple = List.to_tuple(nums)

    if n > 1 do
      Enum.reduce(1..(n - 1), {f0, f0}, fn k, {curr_f, max_f} ->
        next_f = curr_f + sum - n * elem(nums_tuple, n - k)
        {next_f, max(max_f, next_f)}
      end)
      |> elem(1)
    else
      f0
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) with one-paragraph explanation: The algorithm consists of two linear passes over the array. The first pass calculates the sum of the elements and the initial value $F(0)$, and the second pass iteratively calculates the remaining $n-1$ rotation values using the recurrence relation. Both passes take $O(n)$ time.
- **Space Complexity:** O(1) with one-paragraph explanation: The solution uses only a constant amount of extra space to store variables for the total sum, the current rotation function value, and the maximum value encountered during the iterations. No auxiliary data structures are required.
