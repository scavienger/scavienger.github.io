---
layout: post
title: "Transformed Array"
date: 2026-02-05 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Simulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/transformed-array/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> constructTransformedArray(vector<int>&\
        \ nums) {\n        int n = nums.size();\n        vector<int> result(n);\n  \
        \      for (int i = 0; i < n; i++) {\n            int target = (i + nums[i])\
        \ % n;\n            if (target < 0) target += n;\n            result[i] = nums[target];\n\
        \        }\n        return result;\n    }\n};"
      java: "class Solution {\n    public int[] constructTransformedArray(int[] nums)\
        \ {\n        int n = nums.length;\n        int[] result = new int[n];\n    \
        \    for (int i = 0; i < n; i++) {\n            int target = (i + nums[i]) %\
        \ n;\n            if (target < 0) target += n;\n            result[i] = nums[target];\n\
        \        }\n        return result;\n    }\n}"
      python: "class Solution(object):\n    def constructTransformedArray(self, nums):\n\
        \        \"\"\"\n        :type nums: List[int]\n        :rtype: List[int]\n\
        \        \"\"\"\n        n = len(nums)\n        result = [0] * n\n        for\
        \ i in range(n):\n            result[i] = nums[(i + nums[i]) % n]\n        return\
        \ result"
      python3: "class Solution:\n    def constructTransformedArray(self, nums: List[int])\
        \ -> List[int]:\n        n = len(nums)\n        result = [0] * n\n        for\
        \ i in range(n):\n            result[i] = nums[(i + nums[i]) % n]\n        return\
        \ result"
      c: "/**\n * Note: The returned array must be malloced, assume caller calls free().\n\
        \ */\nint* constructTransformedArray(int* nums, int numsSize, int* returnSize)\
        \ {\n    *returnSize = numsSize;\n    int* result = (int*)malloc(numsSize *\
        \ sizeof(int));\n    for (int i = 0; i < numsSize; i++) {\n        int target\
        \ = (i + nums[i]) % numsSize;\n        if (target < 0) target += numsSize;\n\
        \        result[i] = nums[target];\n    }\n    return result;\n}"
      csharp: "public class Solution {\n    public int[] ConstructTransformedArray(int[]\
        \ nums) {\n        int n = nums.Length;\n        int[] result = new int[n];\n\
        \        for (int i = 0; i < n; i++) {\n            int target = (i + nums[i])\
        \ % n;\n            if (target < 0) target += n;\n            result[i] = nums[target];\n\
        \        }\n        return result;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number[]}\n */\nvar constructTransformedArray\
        \ = function(nums) {\n    const n = nums.length;\n    const result = new Array(n);\n\
        \    for (let i = 0; i < n; i++) {\n        let target = (i + nums[i]) % n;\n\
        \        if (target < 0) target += n;\n        result[i] = nums[target];\n \
        \   }\n    return result;\n};"
      typescript: "function constructTransformedArray(nums: number[]): number[] {\n\
        \    const n = nums.length;\n    const result = new Array(n);\n    for (let\
        \ i = 0; i < n; i++) {\n        let target = (i + nums[i]) % n;\n        if\
        \ (target < 0) {\n            target += n;\n        }\n        result[i] = nums[target];\n\
        \    }\n    return result;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer[]\n     */\n    function constructTransformedArray($nums) {\n    \
        \    $n = count($nums);\n        $result = array_fill(0, $n, 0);\n        for\
        \ ($i = 0; $i < $n; $i++) {\n            $target = ($i + $nums[$i]) % $n;\n\
        \            if ($target < 0) {\n                $target += $n;\n          \
        \  }\n            $result[$i] = $nums[$target];\n        }\n        return $result;\n\
        \    }\n}"
      swift: "class Solution {\n    func constructTransformedArray(_ nums: [Int]) ->\
        \ [Int] {\n        let n = nums.count\n        var result = [Int](repeating:\
        \ 0, count: n)\n        for i in 0..<n {\n            var target = (i + nums[i])\
        \ % n\n            if target < 0 {\n                target += n\n          \
        \  }\n            result[i] = nums[target]\n        }\n        return result\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun constructTransformedArray(nums: IntArray):\
        \ IntArray {\n        val n = nums.size\n        val result = IntArray(n)\n\
        \        for (i in 0 until n) {\n            var target = (i + nums[i]) % n\n\
        \            if (target < 0) {\n                target += n\n            }\n\
        \            result[i] = nums[target]\n        }\n        return result\n  \
        \  }\n}"
      dart: "class Solution {\n  List<int> constructTransformedArray(List<int> nums)\
        \ {\n    int n = nums.length;\n    List<int> result = List<int>.filled(n, 0);\n\
        \    for (int i = 0; i < n; i++) {\n      int target = (i + nums[i]) % n;\n\
        \      if (target < 0) {\n        target += n;\n      }\n      result[i] = nums[target];\n\
        \    }\n    return result;\n  }\n}"
      go: "func constructTransformedArray(nums []int) []int {\n    n := len(nums)\n\
        \    result := make([]int, n)\n    for i := 0; i < n; i++ {\n        target\
        \ := (i + nums[i]) % n\n        if target < 0 {\n            target += n\n \
        \       }\n        result[i] = nums[target]\n    }\n    return result\n}"
      ruby: "def construct_transformed_array(nums)\n  n = nums.length\n  nums.each_with_index.map\
        \ do |val, i|\n    nums[(i + val) % n]\n  end\nend"
      scala: "object Solution {\n  def constructTransformedArray(nums: Array[Int]):\
        \ Array[Int] = {\n    val n = nums.length\n    val result = new Array[Int](n)\n\
        \    for (i <- 0 until n) {\n      val targetIndex = ((i + nums(i)) % n + n)\
        \ % n\n      result(i) = nums(targetIndex)\n    }\n    result\n  }\n}"
      rust: "impl Solution {\n    pub fn construct_transformed_array(nums: Vec<i32>)\
        \ -> Vec<i32> {\n        let n = nums.len() as i32;\n        let mut result\
        \ = vec![0; n as usize];\n        for i in 0..n {\n            let target_index\
        \ = (((i + nums[i as usize]) % n + n) % n) as usize;\n            result[i as\
        \ usize] = nums[target_index];\n        }\n        result\n    }\n}"
      racket: "(define/contract (construct-transformed-array nums)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?))\n  (let ([n (length nums)])\n    (map (lambda (i)\n\
        \           (let* ([val (list-ref nums i)]\n                  [target-idx (modulo\
        \ (+ i val) n)])\n             (list-ref nums target-idx)))\n         (range\
        \ n))))"
      erlang: "-spec construct_transformed_array(Nums :: [integer()]) -> [integer()].\n\
        construct_transformed_array(Nums) ->\n  N = length(Nums),\n  NumsArray = list_to_tuple(Nums),\n\
        \  Indices = lists:seq(0, N - 1),\n  lists:map(fun(I) ->\n    Val = element(I\
        \ + 1, NumsArray),\n    TargetIndex = ((I + Val) rem N + N) rem N,\n    element(TargetIndex\
        \ + 1, NumsArray)\n  end, Indices)."
      elixir: "defmodule Solution do\n  @spec construct_transformed_array(nums :: [integer])\
        \ :: [integer]\n  def construct_transformed_array(nums) do\n    n = length(nums)\n\
        \    nums_tuple = List.to_tuple(nums)\n    nums\n    |> Enum.with_index()\n\
        \    |> Enum.map(fn {val, i} ->\n      target_index = Integer.mod(i + val, n)\n\
        \      elem(nums_tuple, target_index)\n    end)\n  end\nend"
    approach: 'The algorithm constructs a new array by iterating through the original
      array and calculating a target index for each element. For each index $i$, we
      calculate the destination index using the displacement given by the value at that
      index. This shift is calculated as $(i + nums[i]) \pmod n$, where $n$ is the length
      of the array. This unified approach handles moving right for positive values,
      moving left for negative values, and remaining in place when the value is zero.


      In many programming languages, the remainder operator can return a negative value
      if the dividend is negative. To resolve this for circular indexing, if the calculated
      target index is negative, we add $n$ to it to map it back into the valid range
      $[0, n-1]$. Once the landing index is determined, the value from the original
      array at that index is assigned to the current position in the result array. This
      process ensures that each action is independent and based on the original state
      of the circular array.'
    time_complexity: O(n), where n is the length of the input array. We perform a single
      pass through the array, doing a constant amount of arithmetic work for each element.
    space_complexity: O(n) for the output array. Aside from the result array, we only
      use a constant amount of auxiliary space for variables used during iteration.
    elapsed_time: 161.1049680709839
    model: gemini-3-flash-preview
    generated_at: '2026-02-05 01:23:09 '
---

## Problem #3379: Transformed Array

**Difficulty:** Easy

**Topics:** Array, Simulation

## Problem Description

<p>You are given an integer array <code>nums</code> that represents a circular array. Your task is to create a new array <code>result</code> of the <strong>same</strong> size, following these rules:</p>
For each index <code>i</code> (where <code>0 &lt;= i &lt; nums.length</code>), perform the following <strong>independent</strong> actions:

<ul>
	<li>If <code>nums[i] &gt; 0</code>: Start at index <code>i</code> and move <code>nums[i]</code> steps to the <strong>right</strong> in the circular array. Set <code>result[i]</code> to the value of the index where you land.</li>
	<li>If <code>nums[i] &lt; 0</code>: Start at index <code>i</code> and move <code>abs(nums[i])</code> steps to the <strong>left</strong> in the circular array. Set <code>result[i]</code> to the value of the index where you land.</li>
	<li>If <code>nums[i] == 0</code>: Set <code>result[i]</code> to <code>nums[i]</code>.</li>
</ul>

<p>Return the new array <code>result</code>.</p>

<p><strong>Note:</strong> Since <code>nums</code> is circular, moving past the last element wraps around to the beginning, and moving before the first element wraps back to the end.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,-2,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,1,1,3]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For <code>nums[0]</code> that is equal to 3, If we move 3 steps to right, we reach <code>nums[3]</code>. So <code>result[0]</code> should be 1.</li>
	<li>For <code>nums[1]</code> that is equal to -2, If we move 2 steps to left, we reach <code>nums[3]</code>. So <code>result[1]</code> should be 1.</li>
	<li>For <code>nums[2]</code> that is equal to 1, If we move 1 step to right, we reach <code>nums[3]</code>. So <code>result[2]</code> should be 1.</li>
	<li>For <code>nums[3]</code> that is equal to 1, If we move 1 step to right, we reach <code>nums[0]</code>. So <code>result[3]</code> should be 3.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [-1,4,-1]</span></p>

<p><strong>Output:</strong> <span class="example-io">[-1,-1,4]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For <code>nums[0]</code> that is equal to -1, If we move 1 step to left, we reach <code>nums[2]</code>. So <code>result[0]</code> should be -1.</li>
	<li>For <code>nums[1]</code> that is equal to 4, If we move 4 steps to right, we reach <code>nums[2]</code>. So <code>result[1]</code> should be -1.</li>
	<li>For <code>nums[2]</code> that is equal to -1, If we move 1 step to left, we reach <code>nums[1]</code>. So <code>result[2]</code> should be 4.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## Hints

1. Simulate the operations as described in the statement

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm constructs a new array by iterating through the original array and calculating a target index for each element. For each index $i$, we calculate the destination index using the displacement given by the value at that index. This shift is calculated as $(i + nums[i]) \pmod n$, where $n$ is the length of the array. This unified approach handles moving right for positive values, moving left for negative values, and remaining in place when the value is zero.

In many programming languages, the remainder operator can return a negative value if the dividend is negative. To resolve this for circular indexing, if the calculated target index is negative, we add $n$ to it to map it back into the valid range $[0, n-1]$. Once the landing index is determined, the value from the original array at that index is assigned to the current position in the result array. This process ensures that each action is independent and based on the original state of the circular array.

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
    vector<int> constructTransformedArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n);
        for (int i = 0; i < n; i++) {
            int target = (i + nums[i]) % n;
            if (target < 0) target += n;
            result[i] = nums[target];
        }
        return result;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int[] constructTransformedArray(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            int target = (i + nums[i]) % n;
            if (target < 0) target += n;
            result[i] = nums[target];
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        for i in range(n):
            result[i] = nums[(i + nums[i]) % n]
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            result[i] = nums[(i + nums[i]) % n]
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* constructTransformedArray(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* result = (int*)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        int target = (i + nums[i]) % numsSize;
        if (target < 0) target += numsSize;
        result[i] = nums[target];
    }
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] ConstructTransformedArray(int[] nums) {
        int n = nums.Length;
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            int target = (i + nums[i]) % n;
            if (target < 0) target += n;
            result[i] = nums[target];
        }
        return result;
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
 * @return {number[]}
 */
var constructTransformedArray = function(nums) {
    const n = nums.length;
    const result = new Array(n);
    for (let i = 0; i < n; i++) {
        let target = (i + nums[i]) % n;
        if (target < 0) target += n;
        result[i] = nums[target];
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function constructTransformedArray(nums: number[]): number[] {
    const n = nums.length;
    const result = new Array(n);
    for (let i = 0; i < n; i++) {
        let target = (i + nums[i]) % n;
        if (target < 0) {
            target += n;
        }
        result[i] = nums[target];
    }
    return result;
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
     * @return Integer[]
     */
    function constructTransformedArray($nums) {
        $n = count($nums);
        $result = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $target = ($i + $nums[$i]) % $n;
            if ($target < 0) {
                $target += $n;
            }
            $result[$i] = $nums[$target];
        }
        return $result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func constructTransformedArray(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var result = [Int](repeating: 0, count: n)
        for i in 0..<n {
            var target = (i + nums[i]) % n
            if target < 0 {
                target += n
            }
            result[i] = nums[target]
        }
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun constructTransformedArray(nums: IntArray): IntArray {
        val n = nums.size
        val result = IntArray(n)
        for (i in 0 until n) {
            var target = (i + nums[i]) % n
            if (target < 0) {
                target += n
            }
            result[i] = nums[target]
        }
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> constructTransformedArray(List<int> nums) {
    int n = nums.length;
    List<int> result = List<int>.filled(n, 0);
    for (int i = 0; i < n; i++) {
      int target = (i + nums[i]) % n;
      if (target < 0) {
        target += n;
      }
      result[i] = nums[target];
    }
    return result;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func constructTransformedArray(nums []int) []int {
    n := len(nums)
    result := make([]int, n)
    for i := 0; i < n; i++ {
        target := (i + nums[i]) % n
        if target < 0 {
            target += n
        }
        result[i] = nums[target]
    }
    return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def construct_transformed_array(nums)
  n = nums.length
  nums.each_with_index.map do |val, i|
    nums[(i + val) % n]
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def constructTransformedArray(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val result = new Array[Int](n)
    for (i <- 0 until n) {
      val targetIndex = ((i + nums(i)) % n + n) % n
      result(i) = nums(targetIndex)
    }
    result
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn construct_transformed_array(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len() as i32;
        let mut result = vec![0; n as usize];
        for i in 0..n {
            let target_index = (((i + nums[i as usize]) % n + n) % n) as usize;
            result[i as usize] = nums[target_index];
        }
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (construct-transformed-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let ([n (length nums)])
    (map (lambda (i)
           (let* ([val (list-ref nums i)]
                  [target-idx (modulo (+ i val) n)])
             (list-ref nums target-idx)))
         (range n))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec construct_transformed_array(Nums :: [integer()]) -> [integer()].
construct_transformed_array(Nums) ->
  N = length(Nums),
  NumsArray = list_to_tuple(Nums),
  Indices = lists:seq(0, N - 1),
  lists:map(fun(I) ->
    Val = element(I + 1, NumsArray),
    TargetIndex = ((I + Val) rem N + N) rem N,
    element(TargetIndex + 1, NumsArray)
  end, Indices).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec construct_transformed_array(nums :: [integer]) :: [integer]
  def construct_transformed_array(nums) do
    n = length(nums)
    nums_tuple = List.to_tuple(nums)
    nums
    |> Enum.with_index()
    |> Enum.map(fn {val, i} ->
      target_index = Integer.mod(i + val, n)
      elem(nums_tuple, target_index)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the input array. We perform a single pass through the array, doing a constant amount of arithmetic work for each element.
- **Space Complexity:** O(n) for the output array. Aside from the result array, we only use a constant amount of auxiliary space for variables used during iteration.
