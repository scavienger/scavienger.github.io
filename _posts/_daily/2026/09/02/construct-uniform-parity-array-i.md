---
layout: post
title: "Construct Uniform Parity Array I"
date: 2026-09-02 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Math"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/construct-uniform-parity-array-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool uniformArray(vector<int>& nums1) {\n\
        \        return true;\n    }\n};"
      java: "class Solution {\n    public boolean uniformArray(int[] nums1) {\n    \
        \    return true;\n    }\n}"
      python: "class Solution(object):\n    def uniformArray(self, nums1):\n       \
        \ \"\"\"\n        :type nums1: List[int]\n        :rtype: bool\n        \"\"\
        \"\n        return True"
      python3: "class Solution:\n    def uniformArray(self, nums1: list[int]) -> bool:\n\
        \        return True"
      c: "bool uniformArray(int* nums1, int nums1Size) {\n    return true;\n}"
      csharp: "public class Solution {\n    public bool UniformArray(int[] nums1) {\n\
        \        return true;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums1\n * @return {boolean}\n */\nvar uniformArray\
        \ = function(nums1) {\n    return true;\n};"
      typescript: "function uniformArray(nums1: number[]): boolean {\n    return true;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums1\n     * @return\
        \ Boolean\n     */\n    function uniformArray($nums1) {\n        return true;\n\
        \    }\n}"
      swift: "class Solution {\n    func uniformArray(_ nums1: [Int]) -> Bool {\n  \
        \      return true\n    }\n}"
      kotlin: "class Solution {\n    fun uniformArray(nums1: IntArray): Boolean {\n\
        \        return true\n    }\n}"
      dart: "class Solution {\n  bool uniformArray(List<int> nums1) {\n    return true;\n\
        \  }\n}"
      go: "func uniformArray(nums1 []int) bool {\n    return true\n}"
      ruby: "# @param {Integer[]} nums1\n# @return {Boolean}\ndef uniform_array(nums1)\n\
        \  true\nend"
      scala: "object Solution {\n    def uniformArray(nums1: Array[Int]): Boolean =\
        \ {\n        true\n    }\n}"
      rust: "impl Solution {\n    pub fn uniform_array(nums1: Vec<i32>) -> bool {\n\
        \        true\n    }\n}"
      racket: "(define/contract (uniform-array nums1)\n  (-> (listof exact-integer?)\
        \ boolean?)\n  #t\n)"
      erlang: "-spec uniform_array(Nums1 :: [integer()]) -> boolean().\nuniform_array(_Nums1)\
        \ ->\n  true."
      elixir: "defmodule Solution do\n  @spec uniform_array(nums1 :: [integer]) :: boolean\n\
        \  def uniform_array(nums1) do\n    true\n  end\nend"
    approach: 'The problem asks whether we can construct an array `nums2` where all
      elements are either even or odd, given the construction rules. Each `nums2[i]`
      can be either `nums1[i]` or `nums1[i] - nums1[j]` for any $j \neq i$. We can analyze
      the possibility by considering the count of odd numbers in the input array, denoted
      as $|O|$. To make all elements in `nums2` even, we need to ensure every odd element
      in `nums1` can be transformed into an even one by subtracting another odd element.
      This is possible if $|O| = 0$ (already even) or if $|O| \ge 2$ (each odd element
      can subtract another). Thus, "all even" is possible if $|O| \neq 1$.


      To make all elements in `nums2` odd, we need to ensure every even element in `nums1`
      can be transformed into an odd one by subtracting an odd element. This is possible
      if there is at least one odd element in the original array ($|O| \ge 1$) to act
      as the subtrahend. If $|O| \ge 1$, we can keep odd elements as they are and subtract
      the odd element from all even ones. Since any array must satisfy either $|O| \neq
      1$ or $|O| \ge 1$, at least one uniform parity (either all even or all odd) is
      always achievable. For the case where $n=1$, a single-element array is vacuously
      uniform in parity. Thus, the answer is always `true`.'
    time_complexity: O(1). The algorithm always returns `true` regardless of the input
      size, as a uniform parity construction is mathematically guaranteed for any valid
      input under the given rules.
    space_complexity: O(1). No extra space is utilized as the solution directly returns
      the boolean result.
    elapsed_time: 806.0872848033905
    model: gemini-3-flash-preview
    generated_at: '2026-09-02 02:27:17 '
---

## Problem #3875: Construct Uniform Parity Array I

**Difficulty:** Easy

**Topics:** Array, Math

## Problem Description

<p>You are given an array <code>nums1</code> of <code>n</code> <strong>distinct</strong> integers.</p>

<p>You want to construct another array <code>nums2</code> of length <code>n</code> such that the elements in <code>nums2</code> are either <strong>all odd or all even</strong>.</p>

<p>For each index <code>i</code>, you must choose <strong>exactly one</strong> of the following (in any order):</p>

<ul>
	<li><code>nums2[i] = nums1[i]</code></li>
	<li><code>nums2[i] = nums1[i] - nums1[j]</code>, for an index <code>j != i</code></li>
</ul>

<p>Return <code>true</code> if it is possible to construct such an array, otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums1 = [2,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Choose <code>nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1</code>.</li>
	<li>Choose <code>nums2[1] = nums1[1] = 3</code>.</li>
	<li><code>nums2 = [-1, 3]</code>, and both elements are odd. Thus, the answer is <code>true</code>​​​​​​​.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums1 = [4,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong>​​​​​​​</p>

<ul>
	<li>Choose <code>nums2[0] = nums1[0] = 4</code>.</li>
	<li>Choose <code>nums2[1] = nums1[1] = 6</code>.</li>
	<li><code>nums2 = [4, 6]</code>, and all elements are even. Thus, the answer is <code>true</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums1.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums1[i] &lt;= 100</code></li>
	<li><code>nums1</code> consists of distinct integers.</li>
</ul>


## Hints

1. There is only one possible answer.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks whether we can construct an array `nums2` where all elements are either even or odd, given the construction rules. Each `nums2[i]` can be either `nums1[i]` or `nums1[i] - nums1[j]` for any $j \neq i$. We can analyze the possibility by considering the count of odd numbers in the input array, denoted as $|O|$. To make all elements in `nums2` even, we need to ensure every odd element in `nums1` can be transformed into an even one by subtracting another odd element. This is possible if $|O| = 0$ (already even) or if $|O| \ge 2$ (each odd element can subtract another). Thus, "all even" is possible if $|O| \neq 1$.

To make all elements in `nums2` odd, we need to ensure every even element in `nums1` can be transformed into an odd one by subtracting an odd element. This is possible if there is at least one odd element in the original array ($|O| \ge 1$) to act as the subtrahend. If $|O| \ge 1$, we can keep odd elements as they are and subtract the odd element from all even ones. Since any array must satisfy either $|O| \neq 1$ or $|O| \ge 1$, at least one uniform parity (either all even or all odd) is always achievable. For the case where $n=1$, a single-element array is vacuously uniform in parity. Thus, the answer is always `true`.

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
    bool uniformArray(vector<int>& nums1) {
        return true;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean uniformArray(int[] nums1) {
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool uniformArray(int* nums1, int nums1Size) {
    return true;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool UniformArray(int[] nums1) {
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} nums1
 * @return {boolean}
 */
var uniformArray = function(nums1) {
    return true;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function uniformArray(nums1: number[]): boolean {
    return true;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $nums1
     * @return Boolean
     */
    function uniformArray($nums1) {
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func uniformArray(_ nums1: [Int]) -> Bool {
        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun uniformArray(nums1: IntArray): Boolean {
        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool uniformArray(List<int> nums1) {
    return true;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func uniformArray(nums1 []int) bool {
    return true
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums1
# @return {Boolean}
def uniform_array(nums1)
  true
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def uniformArray(nums1: Array[Int]): Boolean = {
        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn uniform_array(nums1: Vec<i32>) -> bool {
        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (uniform-array nums1)
  (-> (listof exact-integer?) boolean?)
  #t
)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec uniform_array(Nums1 :: [integer()]) -> boolean().
uniform_array(_Nums1) ->
  true.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec uniform_array(nums1 :: [integer]) :: boolean
  def uniform_array(nums1) do
    true
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(1). The algorithm always returns `true` regardless of the input size, as a uniform parity construction is mathematically guaranteed for any valid input under the given rules.
- **Space Complexity:** O(1). No extra space is utilized as the solution directly returns the boolean result.
