---
layout: post
title: "Minimum Distance Between Three Equal Elements I"
date: 2026-04-10 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Hash Table"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n#include <climits>\n\nusing namespace\
        \ std;\n\nclass Solution {\npublic:\n    int minimumDistance(vector<int>& nums)\
        \ {\n        int n = nums.size();\n        int minDist = INT_MAX;\n        for\
        \ (int i = 0; i < n; i++) {\n            for (int j = i + 1; j < n; j++) {\n\
        \                for (int k = j + 1; k < n; k++) {\n                    if (nums[i]\
        \ == nums[j] && nums[j] == nums[k]) {\n                        minDist = min(minDist,\
        \ 2 * (k - i));\n                    }\n                }\n            }\n \
        \       }\n        return (minDist == INT_MAX) ? -1 : minDist;\n    }\n};"
      java: "class Solution {\n    public int minimumDistance(int[] nums) {\n      \
        \  int n = nums.length;\n        int minDist = Integer.MAX_VALUE;\n        for\
        \ (int i = 0; i < n; i++) {\n            for (int j = i + 1; j < n; j++) {\n\
        \                for (int k = j + 1; k < n; k++) {\n                    if (nums[i]\
        \ == nums[j] && nums[j] == nums[k]) {\n                        minDist = Math.min(minDist,\
        \ 2 * (k - i));\n                    }\n                }\n            }\n \
        \       }\n        return (minDist == Integer.MAX_VALUE) ? -1 : minDist;\n \
        \   }\n}"
      python: "class Solution(object):\n    def minimumDistance(self, nums):\n     \
        \   \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\
        \"\n        n = len(nums)\n        min_dist = float('inf')\n        for i in\
        \ range(n):\n            for j in range(i + 1, n):\n                for k in\
        \ range(j + 1, n):\n                    if nums[i] == nums[j] and nums[j] ==\
        \ nums[k]:\n                        d = 2 * (k - i)\n                      \
        \  if d < min_dist:\n                            min_dist = d\n        return\
        \ int(min_dist) if min_dist != float('inf') else -1"
      python3: "class Solution:\n    def minimumDistance(self, nums: List[int]) -> int:\n\
        \        n = len(nums)\n        min_dist = float('inf')\n        for i in range(n):\n\
        \            for j in range(i + 1, n):\n                for k in range(j + 1,\
        \ n):\n                    if nums[i] == nums[j] == nums[k]:\n             \
        \           d = 2 * (k - i)\n                        if d < min_dist:\n    \
        \                        min_dist = d\n        return int(min_dist) if min_dist\
        \ != float('inf') else -1"
      c: "#include <limits.h>\n\nint minimumDistance(int* nums, int numsSize) {\n  \
        \  int minDist = INT_MAX;\n    for (int i = 0; i < numsSize; i++) {\n      \
        \  for (int j = i + 1; j < numsSize; j++) {\n            for (int k = j + 1;\
        \ k < numsSize; k++) {\n                if (nums[i] == nums[j] && nums[j] ==\
        \ nums[k]) {\n                    int currentDist = 2 * (k - i);\n         \
        \           if (currentDist < minDist) {\n                        minDist =\
        \ currentDist;\n                    }\n                }\n            }\n  \
        \      }\n    }\n    return (minDist == INT_MAX) ? -1 : minDist;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public int MinimumDistance(int[]\
        \ nums) {\n        int n = nums.Length;\n        int minDist = int.MaxValue;\n\
        \        for (int i = 0; i < n; i++) {\n            for (int j = i + 1; j <\
        \ n; j++) {\n                for (int k = j + 1; k < n; k++) {\n           \
        \         if (nums[i] == nums[j] && nums[j] == nums[k]) {\n                \
        \        minDist = Math.Min(minDist, 2 * (k - i));\n                    }\n\
        \                }\n            }\n        }\n        return minDist == int.MaxValue\
        \ ? -1 : minDist;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minimumDistance\
        \ = function(nums) {\n    let n = nums.length;\n    let minDist = Infinity;\n\
        \    for (let i = 0; i < n; i++) {\n        for (let j = i + 1; j < n; j++)\
        \ {\n            for (let k = j + 1; k < n; k++) {\n                if (nums[i]\
        \ === nums[j] && nums[j] === nums[k]) {\n                    let currentDist\
        \ = 2 * (k - i);\n                    if (currentDist < minDist) {\n       \
        \                 minDist = currentDist;\n                    }\n          \
        \      }\n            }\n        }\n    }\n    return minDist === Infinity ?\
        \ -1 : minDist;\n};"
      typescript: "function minimumDistance(nums: number[]): number {\n  const n = nums.length;\n\
        \  let minDist = -1;\n  for (let i = 0; i < n; i++) {\n    for (let j = i +\
        \ 1; j < n; j++) {\n      if (nums[i] === nums[j]) {\n        for (let k = j\
        \ + 1; k < n; k++) {\n          if (nums[j] === nums[k]) {\n            const\
        \ dist = 2 * (k - i);\n            if (minDist === -1 || dist < minDist) {\n\
        \              minDist = dist;\n            }\n          }\n        }\n    \
        \  }\n    }\n  }\n  return minDist;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function minimumDistance($nums) {\n        $n = count($nums);\n\
        \        $minDist = -1;\n        for ($i = 0; $i < $n; $i++) {\n           \
        \ for ($j = $i + 1; $j < $n; $j++) {\n                if ($nums[$i] == $nums[$j])\
        \ {\n                    for ($k = $j + 1; $k < $n; $k++) {\n              \
        \          if ($nums[$j] == $nums[$k]) {\n                            $dist\
        \ = 2 * ($k - $i);\n                            if ($minDist == -1 || $dist\
        \ < $minDist) {\n                                $minDist = $dist;\n       \
        \                     }\n                        }\n                    }\n\
        \                }\n            }\n        }\n        return $minDist;\n   \
        \ }\n}"
      swift: "class Solution {\n    func minimumDistance(_ nums: [Int]) -> Int {\n \
        \       let n = nums.count\n        var minDist = -1\n        for i in 0..<n\
        \ {\n            for j in (i + 1)..<n {\n                if nums[i] == nums[j]\
        \ {\n                    for k in (j + 1)..<n {\n                        if\
        \ nums[j] == nums[k] {\n                            let dist = 2 * (k - i)\n\
        \                            if minDist == -1 || dist < minDist {\n        \
        \                        minDist = dist\n                            }\n   \
        \                     }\n                    }\n                }\n        \
        \    }\n        }\n        return minDist\n    }\n}"
      kotlin: "class Solution {\n    fun minimumDistance(nums: IntArray): Int {\n  \
        \      val n = nums.size\n        var minDist = -1\n        for (i in 0 until\
        \ n) {\n            for (j in i + 1 until n) {\n                if (nums[i]\
        \ == nums[j]) {\n                    for (k in j + 1 until n) {\n          \
        \              if (nums[j] == nums[k]) {\n                            val dist\
        \ = 2 * (k - i)\n                            if (minDist == -1 || dist < minDist)\
        \ {\n                                minDist = dist\n                      \
        \      }\n                        }\n                    }\n               \
        \ }\n            }\n        }\n        return minDist\n    }\n}"
      dart: "class Solution {\n  int minimumDistance(List<int> nums) {\n    int n =\
        \ nums.length;\n    int minDist = -1;\n    for (int i = 0; i < n; i++) {\n \
        \     for (int j = i + 1; j < n; j++) {\n        if (nums[i] == nums[j]) {\n\
        \          for (int k = j + 1; k < n; k++) {\n            if (nums[j] == nums[k])\
        \ {\n              int dist = 2 * (k - i);\n              if (minDist == -1\
        \ || dist < minDist) {\n                minDist = dist;\n              }\n \
        \           }\n          }\n        }\n      }\n    }\n    return minDist;\n\
        \  }\n}"
      go: "func minimumDistance(nums []int) int {\n    n := len(nums)\n    minDist :=\
        \ -1\n    for i := 0; i < n; i++ {\n        for j := i + 1; j < n; j++ {\n \
        \           if nums[i] == nums[j] {\n                for k := j + 1; k < n;\
        \ k++ {\n                    if nums[j] == nums[k] {\n                     \
        \   dist := 2 * (k - i)\n                        if minDist == -1 || dist <\
        \ minDist {\n                            minDist = dist\n                  \
        \      }\n                    }\n                }\n            }\n        }\n\
        \    }\n    return minDist\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef minimum_distance(nums)\n\
        \  n = nums.length\n  min_dist = -1\n  (0...n).each do |i|\n    ((i + 1)...n).each\
        \ do |j|\n      ((j + 1)...n).each do |k|\n        if nums[i] == nums[j] &&\
        \ nums[j] == nums[k]\n          dist = 2 * (k - i)\n          if min_dist ==\
        \ -1 || dist < min_dist\n            min_dist = dist\n          end\n      \
        \  end\n      end\n    end\n  end\n  min_dist\nend"
      scala: "object Solution {\n    def minimumDistance(nums: Array[Int]): Int = {\n\
        \        val n = nums.length\n        var minDist = -1\n        for (i <- 0\
        \ until n) {\n            for (j <- i + 1 until n) {\n                for (k\
        \ <- j + 1 until n) {\n                    if (nums(i) == nums(j) && nums(j)\
        \ == nums(k)) {\n                        val dist = 2 * (k - i)\n          \
        \              if (minDist == -1 || dist < minDist) {\n                    \
        \        minDist = dist\n                        }\n                    }\n\
        \                }\n            }\n        }\n        minDist\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_distance(nums: Vec<i32>) -> i32 {\n\
        \        let n = nums.len();\n        let mut min_dist = -1;\n        for i\
        \ in 0..n {\n            for j in i + 1..n {\n                for k in j + 1..n\
        \ {\n                    if nums[i] == nums[j] && nums[j] == nums[k] {\n   \
        \                     let dist = 2 * (k as i32 - i as i32);\n              \
        \          if min_dist == -1 || dist < min_dist {\n                        \
        \    min_dist = dist;\n                        }\n                    }\n  \
        \              }\n            }\n        }\n        min_dist\n    }\n}"
      racket: "(define/contract (minimum-distance nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let* ([n (length nums)]\n         [arr (list->vector nums)]\n\
        \         [min-dist -1])\n    (for ([i (in-range n)])\n      (for ([j (in-range\
        \ (+ i 1) n)])\n        (for ([k (in-range (+ j 1) n)])\n          (when (and\
        \ (= (vector-ref arr i) (vector-ref arr j))\n                     (= (vector-ref\
        \ arr j) (vector-ref arr k)))\n            (let ([dist (* 2 (- k i))])\n   \
        \           (when (or (= min-dist -1) (< dist min-dist))\n                (set!\
        \ min-dist dist)))))))\n    min-dist))"
      erlang: "-spec minimum_distance(Nums :: [integer()]) -> integer().\nminimum_distance(Nums)\
        \ ->\n  N = length(Nums),\n  if\n    N < 3 -> -1;\n    true ->\n      Arr =\
        \ list_to_tuple(Nums),\n      Distances = [2 * (K - I) || \n        I <- lists:seq(1,\
        \ N - 2),\n        J <- lists:seq(I + 1, N - 1),\n        K <- lists:seq(J +\
        \ 1, N),\n        element(I, Arr) =:= element(J, Arr),\n        element(J, Arr)\
        \ =:= element(K, Arr)],\n      case Distances of\n        [] -> -1;\n      \
        \  _ -> lists:min(Distances)\n      end\n  end."
      elixir: "defmodule Solution do\n  @spec minimum_distance(nums :: [integer]) ::\
        \ integer\n  def minimum_distance(nums) do\n    n = length(nums)\n    if n <\
        \ 3 do\n      -1\n    else\n      arr = List.to_tuple(nums)\n      distances\
        \ = for i <- 0..(n-1),\n                      j <- 0..(n-1),\n             \
        \         k <- 0..(n-1),\n                      i < j, j < k,\n            \
        \          elem(arr, i) == elem(arr, j),\n                      elem(arr, j)\
        \ == elem(arr, k) do\n        2 * (k - i)\n      end\n\n      if distances ==\
        \ [] do\n        -1\n      else\n        Enum.min(distances)\n      end\n  \
        \  end\n  end\nend"
    approach: 'The algorithm employs a brute-force approach to find all ''good'' tuples
      (i, j, k) where nums[i] == nums[j] == nums[k]. Since the indices must be distinct
      and the distance formula abs(i - j) + abs(j - k) + abs(k - i) is symmetric, we
      can assume i < j < k without loss of generality. For any such sorted triplet,
      the distance expression simplifies to 2 * (k - i), which represents twice the
      difference between the largest and smallest index.


      We use three nested loops to iterate through all possible combinations of three
      distinct indices. For each triplet, we check if the elements at these indices
      are identical. If they are, we calculate the simplified distance and update a
      running minimum. If no good tuple is found after checking all combinations, the
      function returns -1 because the minimum distance remains at its initial sentinel
      value.'
    time_complexity: O(N^3). The solution uses three nested loops to iterate through
      every possible combination of three distinct indices from an array of size N,
      resulting in cubic time complexity relative to the input size.
    space_complexity: O(1). The algorithm only uses a fixed amount of additional space
      for loop counters and a single variable to track the minimum distance, requiring
      no auxiliary data structures.
    elapsed_time: 369.1022403240204
    model: gemini-3-flash-preview
    generated_at: '2026-04-10 01:57:52 '
---

## Problem #3740: Minimum Distance Between Three Equal Elements I

**Difficulty:** Easy

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
	<li><code>1 &lt;= n == nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
</ul>


## Hints

1. Use bruteforce

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm employs a brute-force approach to find all 'good' tuples (i, j, k) where nums[i] == nums[j] == nums[k]. Since the indices must be distinct and the distance formula abs(i - j) + abs(j - k) + abs(k - i) is symmetric, we can assume i < j < k without loss of generality. For any such sorted triplet, the distance expression simplifies to 2 * (k - i), which represents twice the difference between the largest and smallest index.

We use three nested loops to iterate through all possible combinations of three distinct indices. For each triplet, we check if the elements at these indices are identical. If they are, we calculate the simplified distance and update a running minimum. If no good tuple is found after checking all combinations, the function returns -1 because the minimum distance remains at its initial sentinel value.

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
#include <climits>

using namespace std;

class Solution {
public:
    int minimumDistance(vector<int>& nums) {
        int n = nums.size();
        int minDist = INT_MAX;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (nums[i] == nums[j] && nums[j] == nums[k]) {
                        minDist = min(minDist, 2 * (k - i));
                    }
                }
            }
        }
        return (minDist == INT_MAX) ? -1 : minDist;
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
        int minDist = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (nums[i] == nums[j] && nums[j] == nums[k]) {
                        minDist = Math.min(minDist, 2 * (k - i));
                    }
                }
            }
        }
        return (minDist == Integer.MAX_VALUE) ? -1 : minDist;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_dist = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] == nums[j] and nums[j] == nums[k]:
                        d = 2 * (k - i)
                        if d < min_dist:
                            min_dist = d
        return int(min_dist) if min_dist != float('inf') else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        min_dist = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] == nums[j] == nums[k]:
                        d = 2 * (k - i)
                        if d < min_dist:
                            min_dist = d
        return int(min_dist) if min_dist != float('inf') else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <limits.h>

int minimumDistance(int* nums, int numsSize) {
    int minDist = INT_MAX;
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            for (int k = j + 1; k < numsSize; k++) {
                if (nums[i] == nums[j] && nums[j] == nums[k]) {
                    int currentDist = 2 * (k - i);
                    if (currentDist < minDist) {
                        minDist = currentDist;
                    }
                }
            }
        }
    }
    return (minDist == INT_MAX) ? -1 : minDist;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int MinimumDistance(int[] nums) {
        int n = nums.Length;
        int minDist = int.MaxValue;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (nums[i] == nums[j] && nums[j] == nums[k]) {
                        minDist = Math.Min(minDist, 2 * (k - i));
                    }
                }
            }
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
    let n = nums.length;
    let minDist = Infinity;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            for (let k = j + 1; k < n; k++) {
                if (nums[i] === nums[j] && nums[j] === nums[k]) {
                    let currentDist = 2 * (k - i);
                    if (currentDist < minDist) {
                        minDist = currentDist;
                    }
                }
            }
        }
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
  let minDist = -1;
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      if (nums[i] === nums[j]) {
        for (let k = j + 1; k < n; k++) {
          if (nums[j] === nums[k]) {
            const dist = 2 * (k - i);
            if (minDist === -1 || dist < minDist) {
              minDist = dist;
            }
          }
        }
      }
    }
  }
  return minDist;
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
        $minDist = -1;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                if ($nums[$i] == $nums[$j]) {
                    for ($k = $j + 1; $k < $n; $k++) {
                        if ($nums[$j] == $nums[$k]) {
                            $dist = 2 * ($k - $i);
                            if ($minDist == -1 || $dist < $minDist) {
                                $minDist = $dist;
                            }
                        }
                    }
                }
            }
        }
        return $minDist;
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
        var minDist = -1
        for i in 0..<n {
            for j in (i + 1)..<n {
                if nums[i] == nums[j] {
                    for k in (j + 1)..<n {
                        if nums[j] == nums[k] {
                            let dist = 2 * (k - i)
                            if minDist == -1 || dist < minDist {
                                minDist = dist
                            }
                        }
                    }
                }
            }
        }
        return minDist
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
        var minDist = -1
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                if (nums[i] == nums[j]) {
                    for (k in j + 1 until n) {
                        if (nums[j] == nums[k]) {
                            val dist = 2 * (k - i)
                            if (minDist == -1 || dist < minDist) {
                                minDist = dist
                            }
                        }
                    }
                }
            }
        }
        return minDist
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
    int minDist = -1;
    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        if (nums[i] == nums[j]) {
          for (int k = j + 1; k < n; k++) {
            if (nums[j] == nums[k]) {
              int dist = 2 * (k - i);
              if (minDist == -1 || dist < minDist) {
                minDist = dist;
              }
            }
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

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumDistance(nums []int) int {
    n := len(nums)
    minDist := -1
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            if nums[i] == nums[j] {
                for k := j + 1; k < n; k++ {
                    if nums[j] == nums[k] {
                        dist := 2 * (k - i)
                        if minDist == -1 || dist < minDist {
                            minDist = dist
                        }
                    }
                }
            }
        }
    }
    return minDist
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
  min_dist = -1
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      ((j + 1)...n).each do |k|
        if nums[i] == nums[j] && nums[j] == nums[k]
          dist = 2 * (k - i)
          if min_dist == -1 || dist < min_dist
            min_dist = dist
          end
        end
      end
    end
  end
  min_dist
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
        var minDist = -1
        for (i <- 0 until n) {
            for (j <- i + 1 until n) {
                for (k <- j + 1 until n) {
                    if (nums(i) == nums(j) && nums(j) == nums(k)) {
                        val dist = 2 * (k - i)
                        if (minDist == -1 || dist < minDist) {
                            minDist = dist
                        }
                    }
                }
            }
        }
        minDist
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
        let mut min_dist = -1;
        for i in 0..n {
            for j in i + 1..n {
                for k in j + 1..n {
                    if nums[i] == nums[j] && nums[j] == nums[k] {
                        let dist = 2 * (k as i32 - i as i32);
                        if min_dist == -1 || dist < min_dist {
                            min_dist = dist;
                        }
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
  (let* ([n (length nums)]
         [arr (list->vector nums)]
         [min-dist -1])
    (for ([i (in-range n)])
      (for ([j (in-range (+ i 1) n)])
        (for ([k (in-range (+ j 1) n)])
          (when (and (= (vector-ref arr i) (vector-ref arr j))
                     (= (vector-ref arr j) (vector-ref arr k)))
            (let ([dist (* 2 (- k i))])
              (when (or (= min-dist -1) (< dist min-dist))
                (set! min-dist dist)))))))
    min-dist))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_distance(Nums :: [integer()]) -> integer().
minimum_distance(Nums) ->
  N = length(Nums),
  if
    N < 3 -> -1;
    true ->
      Arr = list_to_tuple(Nums),
      Distances = [2 * (K - I) || 
        I <- lists:seq(1, N - 2),
        J <- lists:seq(I + 1, N - 1),
        K <- lists:seq(J + 1, N),
        element(I, Arr) =:= element(J, Arr),
        element(J, Arr) =:= element(K, Arr)],
      case Distances of
        [] -> -1;
        _ -> lists:min(Distances)
      end
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_distance(nums :: [integer]) :: integer
  def minimum_distance(nums) do
    n = length(nums)
    if n < 3 do
      -1
    else
      arr = List.to_tuple(nums)
      distances = for i <- 0..(n-1),
                      j <- 0..(n-1),
                      k <- 0..(n-1),
                      i < j, j < k,
                      elem(arr, i) == elem(arr, j),
                      elem(arr, j) == elem(arr, k) do
        2 * (k - i)
      end

      if distances == [] do
        -1
      else
        Enum.min(distances)
      end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N^3). The solution uses three nested loops to iterate through every possible combination of three distinct indices from an array of size N, resulting in cubic time complexity relative to the input size.
- **Space Complexity:** O(1). The algorithm only uses a fixed amount of additional space for loop counters and a single variable to track the minimum distance, requiring no auxiliary data structures.
