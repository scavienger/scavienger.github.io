---
layout: post
title: "Minimum Operations to Make Array Sum Divisible by K"
date: 2025-11-29 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Math"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minOperations(std::vector<int>& nums,\
        \ int k) {\n        long long total_sum = 0;\n        for (int num : nums) {\n\
        \            total_sum += num;\n        }\n        return total_sum % k;\n \
        \   }\n};"
      java: "import java.util.List;\n\nclass Solution {\n    public int minOperations(List<Integer>\
        \ nums, int k) {\n        long totalSum = 0;\n        for (int num : nums) {\n\
        \            totalSum += num;\n        }\n        return (int) (totalSum % k);\n\
        \    }\n}"
      python: "class Solution:\n    def minOperations(self, nums: List[int], k: int)\
        \ -> int:\n        total_sum = sum(nums)\n        return total_sum % k"
      python3: "class Solution:\n    def minOperations(self, nums: List[int], k: int)\
        \ -> int:\n        total_sum = sum(nums)\n        return total_sum % k"
      c: "#include <stddef.h>\n\nint minOperations(int* nums, int numsSize, int k) {\n\
        \    long long total_sum = 0;\n    for (int i = 0; i < numsSize; i++) {\n  \
        \      total_sum += nums[i];\n    }\n    return (int)(total_sum % k);\n}"
      csharp: "using System;\nusing System.Linq;\nusing System.Collections.Generic;\n\
        \npublic class Solution {\n    public int MinOperations(int[] nums, int k) {\n\
        \        long totalSum = 0;\n        foreach (int num in nums) {\n         \
        \   totalSum += num;\n        }\n        return (int)(totalSum % k);\n    }\n\
        }"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @return\
        \ {number}\n */\nvar minOperations = function(nums, k) {\n    let totalSum =\
        \ 0;\n    for (let i = 0; i < nums.length; i++) {\n        totalSum += nums[i];\n\
        \    }\n    return totalSum % k;\n};"
      typescript: "function minOperations(nums: number[], k: number): number {\n   \
        \ let totalSum: number = 0;\n    for (let i = 0; i < nums.length; i++) {\n \
        \       totalSum += nums[i];\n    }\n    return totalSum % k;\n}"
      php: "<?php\nclass Solution {\n\n    /**\n     * @param Integer[] $nums\n    \
        \ * @param Integer $k\n     * @return Integer\n     */\n    function minOperations($nums,\
        \ $k) {\n        $totalSum = array_sum($nums);\n        return $totalSum % $k;\n\
        \    }\n}"
      swift: "class Solution {\n    func minOperations(_ nums: [Int], _ k: Int) -> Int\
        \ {\n        let totalSum = nums.reduce(0, +)\n        return totalSum % k\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun minOperations(nums: IntArray, k: Int): Int\
        \ {\n        val totalSum = nums.sumOf { it.toLong() }\n        return (totalSum\
        \ % k).toInt()\n    }\n}"
      dart: "class Solution {\n  int minOperations(List<int> nums, int k) {\n    int\
        \ totalSum = 0;\n    for (int num in nums) {\n      totalSum += num;\n    }\n\
        \    return totalSum % k;\n  }\n}"
      go: "func minOperations(nums []int, k int) int {\n    totalSum := 0\n    for _,\
        \ num := range nums {\n        totalSum += num\n    }\n    return totalSum %\
        \ k\n}"
      ruby: "class Solution\n    def min_operations(nums, k)\n        total_sum = nums.sum\n\
        \        total_sum % k\n    end\nend"
      scala: "object Solution {\n    def minOperations(nums: Array[Int], k: Int): Int\
        \ = {\n        val totalSum = nums.map(_.toLong).sum\n        (totalSum % k).toInt\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32\
        \ {\n        let total_sum: i64 = nums.iter().map(|&x| x as i64).sum();\n  \
        \      (total_sum % (k as i64)) as i32\n    }\n}"
      racket: "#lang racket\n\n(define (min-operations nums k)\n  (let ([total-sum (apply\
        \ + nums)])\n    (modulo total-sum k)))"
      erlang: "-module(solution).\n-export([min_operations/2]).\n\nmin_operations(Nums,\
        \ K) ->\n    TotalSum = lists:sum(Nums),\n    TotalSum rem K."
      elixir: "defmodule Solution do\n  @spec min_operations(nums :: [integer], k ::\
        \ integer) :: integer\n  def min_operations(nums, k) do\n    total_sum = Enum.sum(nums)\n\
        \    rem(total_sum, k)\n  end\nend"
    approach: The core idea is to understand that each operation reduces the total sum
      of the array by exactly 1. We want to find the minimum number of operations to
      make the array's sum divisible by `k`. Let the current sum of the array be `S`.
      If `S` is already divisible by `k`, then `S % k == 0`, and no operations are needed.
      If `S` is not divisible by `k`, then `S % k` will yield a remainder `r` where
      `0 < r < k`. To make the sum divisible by `k`, we need to reduce the sum `S` by
      at least `r` to reach the largest multiple of `k` that is less than or equal to
      `S`. For example, if `S = 19` and `k = 5`, `S % k = 4`. We need to reduce `S`
      by 4 to get 15, which is divisible by 5. Any further reduction would require more
      operations than necessary to achieve divisibility.
    time_complexity: The time complexity is O(N), where N is the number of elements
      in the `nums` array. This is because we need to iterate through the entire array
      once to calculate its sum. All subsequent operations (modulo) take constant time.
    space_complexity: The space complexity is O(1). We only use a few variables to store
      the total sum and the result, regardless of the input array's size. No auxiliary
      data structures that scale with input size are used.
    elapsed_time: 18.408785581588745
    model: gemini-2.5-flash
    generated_at: '2025-11-29 01:02:23 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int minOperations(vector<int>& nums, int\
        \ k) {\n        int sum = 0;\n        for (int num : nums) {\n            sum\
        \ += num;\n        }\n        return sum % k;\n    }\n};"
      java: "class Solution {\n    public int minOperations(int[] nums, int k) {\n \
        \       int sum = 0;\n        for (int num : nums) {\n            sum += num;\n\
        \        }\n        return sum % k;\n    }\n}"
      python: "class Solution:\n    def minOperations(self, nums: list[int], k: int)\
        \ -> int:\n        return sum(nums) % k"
      python3: "class Solution:\n    def minOperations(self, nums: list[int], k: int)\
        \ -> int:\n        return sum(nums) % k"
      c: "int minOperations(int* nums, int numsSize, int k) {\n    int sum = 0;\n  \
        \  for (int i = 0; i < numsSize; i++) {\n        sum += nums[i];\n    }\n  \
        \  return sum % k;\n}"
      csharp: "public class Solution {\n    public int MinOperations(int[] nums, int\
        \ k) {\n        int sum = 0;\n        foreach (int num in nums) {\n        \
        \    sum += num;\n        }\n        return sum % k;\n    }\n}"
      javascript: "var minOperations = function(nums, k) {\n    let sum = 0;\n    for\
        \ (let num of nums) {\n        sum += num;\n    }\n    return sum % k;\n};"
      typescript: "function minOperations(nums: number[], k: number): number {\n   \
        \ let sum = 0;\n    for (let num of nums) {\n        sum += num;\n    }\n  \
        \  return sum % k;\n}"
      php: "class Solution {\n    function minOperations($nums, $k) {\n        $sum\
        \ = 0;\n        foreach ($nums as $num) {\n            $sum += $num;\n     \
        \   }\n        return $sum % $k;\n    }\n}"
      swift: "class Solution {\n    func minOperations(_ nums: [Int], _ k: Int) -> Int\
        \ {\n        return nums.reduce(0, +) % k\n    }\n}"
      kotlin: "class Solution {\n    fun minOperations(nums: IntArray, k: Int): Int\
        \ {\n        return nums.sum() % k\n    }\n}"
      dart: "class Solution {\n    int minOperations(List<int> nums, int k) {\n    \
        \    return nums.reduce((a, b) => a + b) % k;\n    }\n}"
      go: "func minOperations(nums []int, k int) int {\n    sum := 0\n    for _, num\
        \ := range nums {\n        sum += num\n    }\n    return sum % k\n}"
      ruby: "class Solution\n    def min_operations(nums, k)\n        nums.sum % k\n\
        \    end\nend"
      scala: "object Solution {\n    def minOperations(nums: Array[Int], k: Int): Int\
        \ = {\n        nums.sum % k\n    }\n}"
      rust: "impl Solution {\n    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32\
        \ {\n        nums.into_iter().sum::<i32>() % k\n    }\n}"
      racket: "(define (min-operations nums k)\n    (modulo (apply + nums) k))"
      erlang: "-module(solution).\n-export([min_operations/2]).\nmin_operations(Nums,\
        \ K) ->\n    lists:sum(Nums) rem K."
      elixir: "defmodule Solution do\n    def min_operations(nums, k) do\n        Enum.sum(nums)\
        \ |> rem(k)\n    end\nend"
    approach: "The problem can be solved by first calculating the sum of the array and\
      \ then finding the remainder when the sum is divided by k. If the remainder is\
      \ 0, then no operations are needed. Otherwise, the minimum number of operations\
      \ required is the remainder. This is because we can always reduce the sum by 1\
      \ by performing an operation on any element in the array. The key intuition here\
      \ is that the minimum number of operations required is the smallest number that\
      \ can be added to the sum to make it divisible by k. \n  The algorithm works by\
      \ first calculating the sum of the array using a loop. Then, it calculates the\
      \ remainder when the sum is divided by k using the modulus operator. If the remainder\
      \ is 0, then the function returns 0. Otherwise, it returns the remainder. This\
      \ solution has a time complexity of O(n), where n is the number of elements in\
      \ the array, because it needs to iterate over all elements in the array once to\
      \ calculate the sum."
    time_complexity: The time complexity of this solution is O(n), where n is the number
      of elements in the array. This is because the solution needs to iterate over all
      elements in the array once to calculate the sum. The space complexity is O(1),
      which means the space required does not change with the size of the input array,
      making it very efficient for large inputs.
    space_complexity: The space complexity of this solution is O(1), which means the
      space required does not change with the size of the input array. This is because
      the solution only uses a constant amount of space to store the sum and the remainder,
      regardless of the size of the input array.
    elapsed_time: 2.761709451675415
    model: llama-3.3-70b-versatile
    generated_at: '2025-11-29 01:02:26 '
---

## Problem #3512: Minimum Operations to Make Array Sum Divisible by K

**Difficulty:** Easy

**Topics:** Array, Math

## Problem Description

<p>You are given an integer array <code>nums</code> and an integer <code>k</code>. You can perform the following operation any number of times:</p>

<ul>
	<li>Select an index <code>i</code> and replace <code>nums[i]</code> with <code>nums[i] - 1</code>.</li>
</ul>

<p>Return the <strong>minimum</strong> number of operations required to make the sum of the array divisible by <code>k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,9,7], k = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Perform 4 operations on <code>nums[1] = 9</code>. Now, <code>nums = [3, 5, 7]</code>.</li>
	<li>The sum is 15, which is divisible by 5.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,1,3], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The sum is 8, which is already divisible by 4. Hence, no operations are needed.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,2], k = 6</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Perform 3 operations on <code>nums[0] = 3</code> and 2 operations on <code>nums[1] = 2</code>. Now, <code>nums = [0, 0]</code>.</li>
	<li>The sum is 0, which is divisible by 6.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
</ul>


## Hints

1. ` sum(nums) % k `

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-29 01:02:23 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The core idea is to understand that each operation reduces the total sum of the array by exactly 1. We want to find the minimum number of operations to make the array's sum divisible by `k`. Let the current sum of the array be `S`. If `S` is already divisible by `k`, then `S % k == 0`, and no operations are needed. If `S` is not divisible by `k`, then `S % k` will yield a remainder `r` where `0 < r < k`. To make the sum divisible by `k`, we need to reduce the sum `S` by at least `r` to reach the largest multiple of `k` that is less than or equal to `S`. For example, if `S = 19` and `k = 5`, `S % k = 4`. We need to reduce `S` by 4 to get 15, which is divisible by 5. Any further reduction would require more operations than necessary to achieve divisibility.

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
class Solution {
public:
    int minOperations(std::vector<int>& nums, int k) {
        long long total_sum = 0;
        for (int num : nums) {
            total_sum += num;
        }
        return total_sum % k;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.List;

class Solution {
    public int minOperations(List<Integer> nums, int k) {
        long totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
        return (int) (totalSum % k);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total_sum = sum(nums)
        return total_sum % k
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total_sum = sum(nums)
        return total_sum % k
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stddef.h>

int minOperations(int* nums, int numsSize, int k) {
    long long total_sum = 0;
    for (int i = 0; i < numsSize; i++) {
        total_sum += nums[i];
    }
    return (int)(total_sum % k);
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
    public int MinOperations(int[] nums, int k) {
        long totalSum = 0;
        foreach (int num in nums) {
            totalSum += num;
        }
        return (int)(totalSum % k);
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
var minOperations = function(nums, k) {
    let totalSum = 0;
    for (let i = 0; i < nums.length; i++) {
        totalSum += nums[i];
    }
    return totalSum % k;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minOperations(nums: number[], k: number): number {
    let totalSum: number = 0;
    for (let i = 0; i < nums.length; i++) {
        totalSum += nums[i];
    }
    return totalSum % k;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minOperations($nums, $k) {
        $totalSum = array_sum($nums);
        return $totalSum % $k;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        let totalSum = nums.reduce(0, +)
        return totalSum % k
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minOperations(nums: IntArray, k: Int): Int {
        val totalSum = nums.sumOf { it.toLong() }
        return (totalSum % k).toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minOperations(List<int> nums, int k) {
    int totalSum = 0;
    for (int num in nums) {
      totalSum += num;
    }
    return totalSum % k;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minOperations(nums []int, k int) int {
    totalSum := 0
    for _, num := range nums {
        totalSum += num
    }
    return totalSum % k
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def min_operations(nums, k)
        total_sum = nums.sum
        total_sum % k
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minOperations(nums: Array[Int], k: Int): Int = {
        val totalSum = nums.map(_.toLong).sum
        (totalSum % k).toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let total_sum: i64 = nums.iter().map(|&x| x as i64).sum();
        (total_sum % (k as i64)) as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (min-operations nums k)
  (let ([total-sum (apply + nums)])
    (modulo total-sum k)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([min_operations/2]).

min_operations(Nums, K) ->
    TotalSum = lists:sum(Nums),
    TotalSum rem K.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_operations(nums :: [integer], k :: integer) :: integer
  def min_operations(nums, k) do
    total_sum = Enum.sum(nums)
    rem(total_sum, k)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N), where N is the number of elements in the `nums` array. This is because we need to iterate through the entire array once to calculate its sum. All subsequent operations (modulo) take constant time.

- **Space Complexity:** The space complexity is O(1). We only use a few variables to store the total sum and the result, regardless of the input array's size. No auxiliary data structures that scale with input size are used.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-29 01:02:26 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by first calculating the sum of the array and then finding the remainder when the sum is divided by k. If the remainder is 0, then no operations are needed. Otherwise, the minimum number of operations required is the remainder. This is because we can always reduce the sum by 1 by performing an operation on any element in the array. The key intuition here is that the minimum number of operations required is the smallest number that can be added to the sum to make it divisible by k. 
  The algorithm works by first calculating the sum of the array using a loop. Then, it calculates the remainder when the sum is divided by k using the modulus operator. If the remainder is 0, then the function returns 0. Otherwise, it returns the remainder. This solution has a time complexity of O(n), where n is the number of elements in the array, because it needs to iterate over all elements in the array once to calculate the sum.

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
    int minOperations(vector<int>& nums, int k) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return sum % k;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minOperations(int[] nums, int k) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return sum % k;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        return sum(nums) % k
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        return sum(nums) % k
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minOperations(int* nums, int numsSize, int k) {
    int sum = 0;
    for (int i = 0; i < numsSize; i++) {
        sum += nums[i];
    }
    return sum % k;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinOperations(int[] nums, int k) {
        int sum = 0;
        foreach (int num in nums) {
            sum += num;
        }
        return sum % k;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var minOperations = function(nums, k) {
    let sum = 0;
    for (let num of nums) {
        sum += num;
    }
    return sum % k;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minOperations(nums: number[], k: number): number {
    let sum = 0;
    for (let num of nums) {
        sum += num;
    }
    return sum % k;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function minOperations($nums, $k) {
        $sum = 0;
        foreach ($nums as $num) {
            $sum += $num;
        }
        return $sum % $k;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        return nums.reduce(0, +) % k
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minOperations(nums: IntArray, k: Int): Int {
        return nums.sum() % k
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int minOperations(List<int> nums, int k) {
        return nums.reduce((a, b) => a + b) % k;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minOperations(nums []int, k int) int {
    sum := 0
    for _, num := range nums {
        sum += num
    }
    return sum % k
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def min_operations(nums, k)
        nums.sum % k
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minOperations(nums: Array[Int], k: Int): Int = {
        nums.sum % k
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        nums.into_iter().sum::<i32>() % k
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define (min-operations nums k)
    (modulo (apply + nums) k))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([min_operations/2]).
min_operations(Nums, K) ->
    lists:sum(Nums) rem K.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def min_operations(nums, k) do
        Enum.sum(nums) |> rem(k)
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n), where n is the number of elements in the array. This is because the solution needs to iterate over all elements in the array once to calculate the sum. The space complexity is O(1), which means the space required does not change with the size of the input array, making it very efficient for large inputs.

- **Space Complexity:** The space complexity of this solution is O(1), which means the space required does not change with the size of the input array. This is because the solution only uses a constant amount of space to store the sum and the remainder, regardless of the size of the input array.

</div>
</details>
