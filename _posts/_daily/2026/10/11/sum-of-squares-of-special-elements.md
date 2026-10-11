---
layout: post
title: "Sum of Squares of Special Elements "
date: 2026-10-11 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Enumeration"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/sum-of-squares-of-special-elements/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int sumOfSquares(vector<int>& nums) {\n \
        \       int n = nums.size();\n        int sum = 0;\n        for (int i = 0;\
        \ i < n; ++i) {\n            if (n % (i + 1) == 0) {\n                sum +=\
        \ nums[i] * nums[i];\n            }\n        }\n        return sum;\n    }\n\
        };"
      java: "class Solution {\n    public int sumOfSquares(int[] nums) {\n        int\
        \ n = nums.length;\n        int sum = 0;\n        for (int i = 0; i < n; i++)\
        \ {\n            if (n % (i + 1) == 0) {\n                sum += nums[i] * nums[i];\n\
        \            }\n        }\n        return sum;\n    }\n}"
      python: "class Solution(object):\n    def sumOfSquares(self, nums):\n        \"\
        \"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\n \
        \       n = len(nums)\n        total_sum = 0\n        for i in range(n):\n \
        \           if n % (i + 1) == 0:\n                total_sum += nums[i] * nums[i]\n\
        \        return total_sum"
      python3: "class Solution:\n    def sumOfSquares(self, nums: List[int]) -> int:\n\
        \        n = len(nums)\n        total_sum = 0\n        for i in range(n):\n\
        \            if n % (i + 1) == 0:\n                total_sum += nums[i] ** 2\n\
        \        return total_sum"
      c: "int sumOfSquares(int* nums, int numsSize) {\n    int sum = 0;\n    for (int\
        \ i = 0; i < numsSize; i++) {\n        if (numsSize % (i + 1) == 0) {\n    \
        \        sum += nums[i] * nums[i];\n        }\n    }\n    return sum;\n}"
      csharp: "public class Solution {\n    public int SumOfSquares(int[] nums) {\n\
        \        int n = nums.Length;\n        int sum = 0;\n        for (int i = 0;\
        \ i < n; i++) {\n            if (n % (i + 1) == 0) {\n                sum +=\
        \ nums[i] * nums[i];\n            }\n        }\n        return sum;\n    }\n\
        }"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar sumOfSquares\
        \ = function(nums) {\n    const n = nums.length;\n    let sum = 0;\n    for\
        \ (let i = 0; i < n; i++) {\n        if (n % (i + 1) === 0) {\n            sum\
        \ += nums[i] * nums[i];\n        }\n    }\n    return sum;\n};"
      typescript: "function sumOfSquares(nums: number[]): number {\n    const n = nums.length;\n\
        \    let sum = 0;\n    for (let i = 1; i <= n; i++) {\n        if (n % i ===\
        \ 0) {\n            sum += nums[i - 1] * nums[i - 1];\n        }\n    }\n  \
        \  return sum;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function sumOfSquares($nums) {\n        $n = count($nums);\n\
        \        $sum = 0;\n        for ($i = 1; $i <= $n; $i++) {\n            if ($n\
        \ % $i == 0) {\n                $sum += $nums[$i - 1] * $nums[$i - 1];\n   \
        \         }\n        }\n        return $sum;\n    }\n}"
      swift: "class Solution {\n    func sumOfSquares(_ nums: [Int]) -> Int {\n    \
        \    let n = nums.count\n        var sum = 0\n        for i in 1...n {\n   \
        \         if n % i == 0 {\n                sum += nums[i - 1] * nums[i - 1]\n\
        \            }\n        }\n        return sum\n    }\n}"
      kotlin: "class Solution {\n    fun sumOfSquares(nums: IntArray): Int {\n     \
        \   val n = nums.size\n        var sum = 0\n        for (i in 1..n) {\n    \
        \        if (n % i == 0) {\n                sum += nums[i - 1] * nums[i - 1]\n\
        \            }\n        }\n        return sum\n    }\n}"
      dart: "class Solution {\n  int sumOfSquares(List<int> nums) {\n    int n = nums.length;\n\
        \    int sum = 0;\n    for (int i = 1; i <= n; i++) {\n      if (n % i == 0)\
        \ {\n        sum += nums[i - 1] * nums[i - 1];\n      }\n    }\n    return sum;\n\
        \  }\n}"
      go: "func sumOfSquares(nums []int) int {\n    n := len(nums)\n    sum := 0\n \
        \   for i := 1; i <= n; i++ {\n        if n % i == 0 {\n            sum += nums[i\
        \ - 1] * nums[i - 1]\n        }\n    }\n    return sum\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef sum_of_squares(nums)\n\
        \  n = nums.length\n  sum = 0\n  nums.each_with_index do |num, idx|\n    i =\
        \ idx + 1\n    if n % i == 0\n      sum += num * num\n    end\n  end\n  sum\n\
        end"
      scala: "object Solution {\n    def sumOfSquares(nums: Array[Int]): Int = {\n \
        \       val n = nums.length\n        var sum = 0\n        for (i <- 1 to n)\
        \ {\n            if (n % i == 0) {\n                sum += nums(i - 1) * nums(i\
        \ - 1)\n            }\n        }\n        sum\n    }\n}"
      rust: "impl Solution {\n    pub fn sum_of_squares(nums: Vec<i32>) -> i32 {\n \
        \       let n = nums.len();\n        let mut sum = 0;\n        for i in 1..=n\
        \ {\n            if n % i == 0 {\n                sum += nums[i - 1] * nums[i\
        \ - 1];\n            }\n        }\n        sum\n    }\n}"
      racket: "(define/contract (sum-of-squares nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let ([n (length nums)])\n    (for/sum ([i (in-range 1\
        \ (+ n 1))]\n              [x nums])\n      (if (zero? (remainder n i))\n  \
        \        (* x x)\n          0))))"
      erlang: "-spec sum_of_squares(Nums :: [integer()]) -> integer().\nsum_of_squares(Nums)\
        \ ->\n  N = length(Nums),\n  lists:sum([X * X || {X, I} <- lists:zip(Nums, lists:seq(1,\
        \ N)), N rem I =:= 0])."
      elixir: "defmodule Solution do\n  @spec sum_of_squares(nums :: [integer]) :: integer\n\
        \  def sum_of_squares(nums) do\n    n = length(nums)\n    nums\n    |> Enum.with_index(1)\n\
        \    |> Enum.filter(fn {_, i} -> rem(n, i) == 0 end)\n    |> Enum.map(fn {val,\
        \ _} -> val * val end)\n    |> Enum.sum()\n  end\nend"
    approach: 'The problem asks for the sum of squares of elements whose 1-indexed positions
      divide the total length $n$ of the array. Since standard programming arrays are
      0-indexed, we iterate through the array using a loop variable $i$ from $0$ to
      $n-1$. For each element, the corresponding 1-indexed position is $i + 1$. We check
      if $n$ is divisible by this 1-indexed position using the modulo operator: $n \%
      (i + 1) == 0$.


      When the divisibility condition is satisfied, the element $nums[i]$ is considered
      special. We calculate its square by multiplying the element by itself and add
      this value to a running accumulator. After checking all elements in the array,
      the accumulated sum represents the total sum of squares of all special elements.'
    time_complexity: O(n) where n is the length of the input array. We perform a single
      linear pass through the array to check each element against the divisibility condition.
    space_complexity: O(1) because we only use a single integer variable to store the
      cumulative sum and an index variable for the loop, regardless of the input size.
    elapsed_time: 333.34434270858765
    model: gemini-3-flash-preview
    generated_at: '2026-10-11 03:17:52 '
---

## Problem #2778: Sum of Squares of Special Elements 

**Difficulty:** Easy

**Topics:** Array, Enumeration

## Problem Description

<p>You are given a <strong>1-indexed</strong> integer array <code>nums</code> of length <code>n</code>.</p>

<p>An element <code>nums[i]</code> of <code>nums</code> is called <strong>special</strong> if <code>i</code> divides <code>n</code>, i.e. <code>n % i == 0</code>.</p>

<p>Return <em>the <strong>sum of the squares</strong> of all <strong>special</strong> elements of </em><code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> 21
<strong>Explanation:</strong> There are exactly 3 special elements in nums: nums[1] since 1 divides 4, nums[2] since 2 divides 4, and nums[4] since 4 divides 4. 
Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[4] * nums[4] = 1 * 1 + 2 * 2 + 4 * 4 = 21.  
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,1,19,18,3]
<strong>Output:</strong> 63
<strong>Explanation:</strong> There are exactly 4 special elements in nums: nums[1] since 1 divides 6, nums[2] since 2 divides 6, nums[3] since 3 divides 6, and nums[6] since 6 divides 6. 
Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[3] * nums[3] + nums[6] * nums[6] = 2 * 2 + 7 * 7 + 1 * 1 + 3 * 3 = 63. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length == n &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>


## Hints

1. Iterate over all the elements of the array. For each index i, check if it is special using the modulo operator.

2. if n%i == 0, index i is special and you should add nums[i] to the answer.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the sum of squares of elements whose 1-indexed positions divide the total length $n$ of the array. Since standard programming arrays are 0-indexed, we iterate through the array using a loop variable $i$ from $0$ to $n-1$. For each element, the corresponding 1-indexed position is $i + 1$. We check if $n$ is divisible by this 1-indexed position using the modulo operator: $n \% (i + 1) == 0$.

When the divisibility condition is satisfied, the element $nums[i]$ is considered special. We calculate its square by multiplying the element by itself and add this value to a running accumulator. After checking all elements in the array, the accumulated sum represents the total sum of squares of all special elements.

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
    int sumOfSquares(vector<int>& nums) {
        int n = nums.size();
        int sum = 0;
        for (int i = 0; i < n; ++i) {
            if (n % (i + 1) == 0) {
                sum += nums[i] * nums[i];
            }
        }
        return sum;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int sumOfSquares(int[] nums) {
        int n = nums.length;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            if (n % (i + 1) == 0) {
                sum += nums[i] * nums[i];
            }
        }
        return sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = 0
        for i in range(n):
            if n % (i + 1) == 0:
                total_sum += nums[i] * nums[i]
        return total_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        for i in range(n):
            if n % (i + 1) == 0:
                total_sum += nums[i] ** 2
        return total_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int sumOfSquares(int* nums, int numsSize) {
    int sum = 0;
    for (int i = 0; i < numsSize; i++) {
        if (numsSize % (i + 1) == 0) {
            sum += nums[i] * nums[i];
        }
    }
    return sum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int SumOfSquares(int[] nums) {
        int n = nums.Length;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            if (n % (i + 1) == 0) {
                sum += nums[i] * nums[i];
            }
        }
        return sum;
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
var sumOfSquares = function(nums) {
    const n = nums.length;
    let sum = 0;
    for (let i = 0; i < n; i++) {
        if (n % (i + 1) === 0) {
            sum += nums[i] * nums[i];
        }
    }
    return sum;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function sumOfSquares(nums: number[]): number {
    const n = nums.length;
    let sum = 0;
    for (let i = 1; i <= n; i++) {
        if (n % i === 0) {
            sum += nums[i - 1] * nums[i - 1];
        }
    }
    return sum;
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
    function sumOfSquares($nums) {
        $n = count($nums);
        $sum = 0;
        for ($i = 1; $i <= $n; $i++) {
            if ($n % $i == 0) {
                $sum += $nums[$i - 1] * $nums[$i - 1];
            }
        }
        return $sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func sumOfSquares(_ nums: [Int]) -> Int {
        let n = nums.count
        var sum = 0
        for i in 1...n {
            if n % i == 0 {
                sum += nums[i - 1] * nums[i - 1]
            }
        }
        return sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun sumOfSquares(nums: IntArray): Int {
        val n = nums.size
        var sum = 0
        for (i in 1..n) {
            if (n % i == 0) {
                sum += nums[i - 1] * nums[i - 1]
            }
        }
        return sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int sumOfSquares(List<int> nums) {
    int n = nums.length;
    int sum = 0;
    for (int i = 1; i <= n; i++) {
      if (n % i == 0) {
        sum += nums[i - 1] * nums[i - 1];
      }
    }
    return sum;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func sumOfSquares(nums []int) int {
    n := len(nums)
    sum := 0
    for i := 1; i <= n; i++ {
        if n % i == 0 {
            sum += nums[i - 1] * nums[i - 1]
        }
    }
    return sum
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def sum_of_squares(nums)
  n = nums.length
  sum = 0
  nums.each_with_index do |num, idx|
    i = idx + 1
    if n % i == 0
      sum += num * num
    end
  end
  sum
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def sumOfSquares(nums: Array[Int]): Int = {
        val n = nums.length
        var sum = 0
        for (i <- 1 to n) {
            if (n % i == 0) {
                sum += nums(i - 1) * nums(i - 1)
            }
        }
        sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn sum_of_squares(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut sum = 0;
        for i in 1..=n {
            if n % i == 0 {
                sum += nums[i - 1] * nums[i - 1];
            }
        }
        sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (sum-of-squares nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ([n (length nums)])
    (for/sum ([i (in-range 1 (+ n 1))]
              [x nums])
      (if (zero? (remainder n i))
          (* x x)
          0))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec sum_of_squares(Nums :: [integer()]) -> integer().
sum_of_squares(Nums) ->
  N = length(Nums),
  lists:sum([X * X || {X, I} <- lists:zip(Nums, lists:seq(1, N)), N rem I =:= 0]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec sum_of_squares(nums :: [integer]) :: integer
  def sum_of_squares(nums) do
    n = length(nums)
    nums
    |> Enum.with_index(1)
    |> Enum.filter(fn {_, i} -> rem(n, i) == 0 end)
    |> Enum.map(fn {val, _} -> val * val end)
    |> Enum.sum()
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the input array. We perform a single linear pass through the array to check each element against the divisibility condition.
- **Space Complexity:** O(1) because we only use a single integer variable to store the cumulative sum and an index variable for the loop, regardless of the input size.
