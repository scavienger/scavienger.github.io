---
layout: post
title: "Find Greatest Common Divisor of Array"
date: 2026-07-18 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Math", "Number Theory"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/find-greatest-common-divisor-of-array/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int findGCD(vector<int>& nums) {\n      \
        \  int mn = nums[0];\n        int mx = nums[0];\n        for (int i = 1; i <\
        \ nums.size(); ++i) {\n            if (nums[i] < mn) mn = nums[i];\n       \
        \     if (nums[i] > mx) mx = nums[i];\n        }\n        while (mn > 0) {\n\
        \            int temp = mx % mn;\n            mx = mn;\n            mn = temp;\n\
        \        }\n        return mx;\n    }\n};"
      java: "class Solution {\n    public int findGCD(int[] nums) {\n        int mn\
        \ = nums[0];\n        int mx = nums[0];\n        for (int i = 1; i < nums.length;\
        \ i++) {\n            if (nums[i] < mn) mn = nums[i];\n            if (nums[i]\
        \ > mx) mx = nums[i];\n        }\n        while (mn > 0) {\n            int\
        \ temp = mx % mn;\n            mx = mn;\n            mn = temp;\n        }\n\
        \        return mx;\n    }\n}"
      python: "class Solution(object):\n    def findGCD(self, nums):\n        \"\"\"\
        \n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\n     \
        \   mn = min(nums)\n        mx = max(nums)\n        while mn:\n            mx,\
        \ mn = mn, mx % mn\n        return mx"
      python3: "class Solution:\n    def findGCD(self, nums: List[int]) -> int:\n  \
        \      mn = min(nums)\n        mx = max(nums)\n        while mn:\n         \
        \   mx, mn = mn, mx % mn\n        return mx"
      c: "int findGCD(int* nums, int numsSize) {\n    int mn = nums[0];\n    int mx\
        \ = nums[0];\n    for (int i = 1; i < numsSize; i++) {\n        if (nums[i]\
        \ < mn) mn = nums[i];\n        if (nums[i] > mx) mx = nums[i];\n    }\n    while\
        \ (mn > 0) {\n        int temp = mx % mn;\n        mx = mn;\n        mn = temp;\n\
        \    }\n    return mx;\n}"
      csharp: "public class Solution {\n    public int FindGCD(int[] nums) {\n     \
        \   int mn = nums[0];\n        int mx = nums[0];\n        foreach (int x in\
        \ nums) {\n            if (x < mn) mn = x;\n            if (x > mx) mx = x;\n\
        \        }\n        while (mn > 0) {\n            int temp = mx % mn;\n    \
        \        mx = mn;\n            mn = temp;\n        }\n        return mx;\n \
        \   }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar findGCD\
        \ = function(nums) {\n    let mn = nums[0];\n    let mx = nums[0];\n    for\
        \ (let i = 1; i < nums.length; i++) {\n        if (nums[i] < mn) mn = nums[i];\n\
        \        if (nums[i] > mx) mx = nums[i];\n    }\n    while (mn > 0) {\n    \
        \    let temp = mx % mn;\n        mx = mn;\n        mn = temp;\n    }\n    return\
        \ mx;\n};"
      typescript: "function findGCD(nums: number[]): number {\n    let minVal = nums[0];\n\
        \    let maxVal = nums[0];\n    for (let i = 1; i < nums.length; i++) {\n  \
        \      if (nums[i] < minVal) minVal = nums[i];\n        if (nums[i] > maxVal)\
        \ maxVal = nums[i];\n    }\n\n    let a = minVal;\n    let b = maxVal;\n   \
        \ while (b !== 0) {\n        let temp = b;\n        b = a % b;\n        a =\
        \ temp;\n    }\n    return a;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function findGCD($nums) {\n        $minVal = $nums[0];\n\
        \        $maxVal = $nums[0];\n        foreach ($nums as $num) {\n          \
        \  if ($num < $minVal) $minVal = $num;\n            if ($num > $maxVal) $maxVal\
        \ = $num;\n        }\n\n        $a = $minVal;\n        $b = $maxVal;\n     \
        \   while ($b != 0) {\n            $temp = $b;\n            $b = $a % $b;\n\
        \            $a = $temp;\n        }\n        return $a;\n    }\n}"
      swift: "class Solution {\n    func findGCD(_ nums: [Int]) -> Int {\n        var\
        \ minVal = nums[0]\n        var maxVal = nums[0]\n        for i in 1..<nums.count\
        \ {\n            if nums[i] < minVal { minVal = nums[i] }\n            if nums[i]\
        \ > maxVal { maxVal = nums[i] }\n        }\n\n        var a = minVal\n     \
        \   var b = maxVal\n        while b != 0 {\n            let temp = b\n     \
        \       b = a % b\n            a = temp\n        }\n        return a\n    }\n\
        }"
      kotlin: "class Solution {\n    fun findGCD(nums: IntArray): Int {\n        var\
        \ minVal = nums[0]\n        var maxVal = nums[0]\n        for (i in 1 until\
        \ nums.size) {\n            if (nums[i] < minVal) minVal = nums[i]\n       \
        \     if (nums[i] > maxVal) maxVal = nums[i]\n        }\n\n        var a = minVal\n\
        \        var b = maxVal\n        while (b != 0) {\n            val temp = b\n\
        \            b = a % b\n            a = temp\n        }\n        return a\n\
        \    }\n}"
      dart: "class Solution {\n  int findGCD(List<int> nums) {\n    int minVal = nums[0];\n\
        \    int maxVal = nums[0];\n    for (int i = 1; i < nums.length; i++) {\n  \
        \    if (nums[i] < minVal) minVal = nums[i];\n      if (nums[i] > maxVal) maxVal\
        \ = nums[i];\n    }\n\n    int a = minVal;\n    int b = maxVal;\n    while (b\
        \ != 0) {\n      int temp = b;\n      b = a % b;\n      a = temp;\n    }\n \
        \   return a;\n  }\n}"
      go: "func findGCD(nums []int) int {\n    minVal := nums[0]\n    maxVal := nums[0]\n\
        \    for i := 1; i < len(nums); i++ {\n        if nums[i] < minVal {\n     \
        \       minVal = nums[i]\n        }\n        if nums[i] > maxVal {\n       \
        \     maxVal = nums[i]\n        }\n    }\n\n    a, b := minVal, maxVal\n   \
        \ for b != 0 {\n        a, b = b, a % b\n    }\n    return a\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef find_gcd(nums)\n  min_val,\
        \ max_val = nums.minmax\n  min_val.gcd(max_val)\nend"
      scala: "object Solution {\n    def findGCD(nums: Array[Int]): Int = {\n      \
        \  val minVal = nums.min\n        val maxVal = nums.max\n\n        def gcd(a:\
        \ Int, b: Int): Int = {\n            if (b == 0) a else gcd(b, a % b)\n    \
        \    }\n\n        gcd(minVal, maxVal)\n    }\n}"
      rust: "impl Solution {\n    pub fn find_gcd(nums: Vec<i32>) -> i32 {\n       \
        \ let min_val = *nums.iter().min().unwrap();\n        let max_val = *nums.iter().max().unwrap();\n\
        \n        fn gcd(a: i32, b: i32) -> i32 {\n            if b == 0 {\n       \
        \         a\n            } else {\n                gcd(b, a % b)\n         \
        \   }\n        }\n\n        gcd(min_val, max_val)\n    }\n}"
      racket: "(define/contract (find-gcd nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (gcd (apply min nums) (apply max nums)))"
      erlang: "-spec find_gcd(Nums :: [integer()]) -> integer().\nfind_gcd(Nums) ->\n\
        \  Min = lists:min(Nums),\n  Max = lists:max(Nums),\n  do_gcd(Min, Max).\n\n\
        do_gcd(A, 0) -> A;\ndo_gcd(A, B) -> do_gcd(B, A rem B)."
      elixir: "defmodule Solution do\n  @spec find_gcd(nums :: [integer]) :: integer\n\
        \  def find_gcd(nums) do\n    gcd(Enum.min(nums), Enum.max(nums))\n  end\n\n\
        \  defp gcd(a, 0), do: a\n  defp gcd(a, b), do: gcd(b, rem(a, b))\nend"
    approach: The problem asks for the greatest common divisor (GCD) of the smallest
      and largest numbers in a given array. The algorithm first identifies these two
      boundary values, mn and mx, by iterating through the array. This is efficiently
      done in a single linear pass by comparing each element with the current minimum
      and maximum values found so far.
    time_complexity: O(N + log(M)) where N is the length of the array and M is the maximum
      value in the array. Finding the minimum and maximum takes O(N) time, and the Euclidean
      algorithm for two numbers up to M takes O(log M) time.
    space_complexity: O(1) because the algorithm only uses a fixed number of integer
      variables (mn, mx, and temp variables) regardless of the size of the input array.
    elapsed_time: 239.57396483421326
    model: gemini-3-flash-preview
    generated_at: '2026-07-18 01:51:46 '
---

## Problem #1979: Find Greatest Common Divisor of Array

**Difficulty:** Easy

**Topics:** Array, Math, Number Theory

## Problem Description

<p>Given an integer array <code>nums</code>, return<strong> </strong><em>the <strong>greatest common divisor</strong> of the smallest number and largest number in </em><code>nums</code>.</p>

<p>The <strong>greatest common divisor</strong> of two numbers is the largest positive integer that evenly divides both numbers.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,5,6,9,10]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,5,6,8,3]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## Hints

1. Find the minimum and maximum in one iteration. Let them be mn and mx.

2. Try all the numbers in the range [1, mn] and check the largest number which divides both of them.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the greatest common divisor (GCD) of the smallest and largest numbers in a given array. The algorithm first identifies these two boundary values, mn and mx, by iterating through the array. This is efficiently done in a single linear pass by comparing each element with the current minimum and maximum values found so far.

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
    int findGCD(vector<int>& nums) {
        int mn = nums[0];
        int mx = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] < mn) mn = nums[i];
            if (nums[i] > mx) mx = nums[i];
        }
        while (mn > 0) {
            int temp = mx % mn;
            mx = mn;
            mn = temp;
        }
        return mx;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int findGCD(int[] nums) {
        int mn = nums[0];
        int mx = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < mn) mn = nums[i];
            if (nums[i] > mx) mx = nums[i];
        }
        while (mn > 0) {
            int temp = mx % mn;
            mx = mn;
            mn = temp;
        }
        return mx;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = min(nums)
        mx = max(nums)
        while mn:
            mx, mn = mn, mx % mn
        return mx
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        while mn:
            mx, mn = mn, mx % mn
        return mx
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int findGCD(int* nums, int numsSize) {
    int mn = nums[0];
    int mx = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < mn) mn = nums[i];
        if (nums[i] > mx) mx = nums[i];
    }
    while (mn > 0) {
        int temp = mx % mn;
        mx = mn;
        mn = temp;
    }
    return mx;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int FindGCD(int[] nums) {
        int mn = nums[0];
        int mx = nums[0];
        foreach (int x in nums) {
            if (x < mn) mn = x;
            if (x > mx) mx = x;
        }
        while (mn > 0) {
            int temp = mx % mn;
            mx = mn;
            mn = temp;
        }
        return mx;
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
var findGCD = function(nums) {
    let mn = nums[0];
    let mx = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] < mn) mn = nums[i];
        if (nums[i] > mx) mx = nums[i];
    }
    while (mn > 0) {
        let temp = mx % mn;
        mx = mn;
        mn = temp;
    }
    return mx;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findGCD(nums: number[]): number {
    let minVal = nums[0];
    let maxVal = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] < minVal) minVal = nums[i];
        if (nums[i] > maxVal) maxVal = nums[i];
    }

    let a = minVal;
    let b = maxVal;
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
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
    function findGCD($nums) {
        $minVal = $nums[0];
        $maxVal = $nums[0];
        foreach ($nums as $num) {
            if ($num < $minVal) $minVal = $num;
            if ($num > $maxVal) $maxVal = $num;
        }

        $a = $minVal;
        $b = $maxVal;
        while ($b != 0) {
            $temp = $b;
            $b = $a % $b;
            $a = $temp;
        }
        return $a;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func findGCD(_ nums: [Int]) -> Int {
        var minVal = nums[0]
        var maxVal = nums[0]
        for i in 1..<nums.count {
            if nums[i] < minVal { minVal = nums[i] }
            if nums[i] > maxVal { maxVal = nums[i] }
        }

        var a = minVal
        var b = maxVal
        while b != 0 {
            let temp = b
            b = a % b
            a = temp
        }
        return a
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun findGCD(nums: IntArray): Int {
        var minVal = nums[0]
        var maxVal = nums[0]
        for (i in 1 until nums.size) {
            if (nums[i] < minVal) minVal = nums[i]
            if (nums[i] > maxVal) maxVal = nums[i]
        }

        var a = minVal
        var b = maxVal
        while (b != 0) {
            val temp = b
            b = a % b
            a = temp
        }
        return a
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int findGCD(List<int> nums) {
    int minVal = nums[0];
    int maxVal = nums[0];
    for (int i = 1; i < nums.length; i++) {
      if (nums[i] < minVal) minVal = nums[i];
      if (nums[i] > maxVal) maxVal = nums[i];
    }

    int a = minVal;
    int b = maxVal;
    while (b != 0) {
      int temp = b;
      b = a % b;
      a = temp;
    }
    return a;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func findGCD(nums []int) int {
    minVal := nums[0]
    maxVal := nums[0]
    for i := 1; i < len(nums); i++ {
        if nums[i] < minVal {
            minVal = nums[i]
        }
        if nums[i] > maxVal {
            maxVal = nums[i]
        }
    }

    a, b := minVal, maxVal
    for b != 0 {
        a, b = b, a % b
    }
    return a
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def find_gcd(nums)
  min_val, max_val = nums.minmax
  min_val.gcd(max_val)
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def findGCD(nums: Array[Int]): Int = {
        val minVal = nums.min
        val maxVal = nums.max

        def gcd(a: Int, b: Int): Int = {
            if (b == 0) a else gcd(b, a % b)
        }

        gcd(minVal, maxVal)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn find_gcd(nums: Vec<i32>) -> i32 {
        let min_val = *nums.iter().min().unwrap();
        let max_val = *nums.iter().max().unwrap();

        fn gcd(a: i32, b: i32) -> i32 {
            if b == 0 {
                a
            } else {
                gcd(b, a % b)
            }
        }

        gcd(min_val, max_val)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (find-gcd nums)
  (-> (listof exact-integer?) exact-integer?)
  (gcd (apply min nums) (apply max nums)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec find_gcd(Nums :: [integer()]) -> integer().
find_gcd(Nums) ->
  Min = lists:min(Nums),
  Max = lists:max(Nums),
  do_gcd(Min, Max).

do_gcd(A, 0) -> A;
do_gcd(A, B) -> do_gcd(B, A rem B).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec find_gcd(nums :: [integer]) :: integer
  def find_gcd(nums) do
    gcd(Enum.min(nums), Enum.max(nums))
  end

  defp gcd(a, 0), do: a
  defp gcd(a, b), do: gcd(b, rem(a, b))
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N + log(M)) where N is the length of the array and M is the maximum value in the array. Finding the minimum and maximum takes O(N) time, and the Euclidean algorithm for two numbers up to M takes O(log M) time.
- **Space Complexity:** O(1) because the algorithm only uses a fixed number of integer variables (mn, mx, and temp variables) regardless of the size of the input array.
