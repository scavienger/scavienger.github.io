---
layout: post
title: "Number of Unique XOR Triplets I"
date: 2026-07-23 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Bit Manipulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/number-of-unique-xor-triplets-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int uniqueXorTriplets(vector<int>& nums)\
        \ {\n        int n = nums.size();\n        if (n <= 2) {\n            return\
        \ n;\n        }\n        int p = 1;\n        while (p <= n) {\n            p\
        \ <<= 1;\n        }\n        return p;\n    }\n};"
      java: "class Solution {\n    public int uniqueXorTriplets(int[] nums) {\n    \
        \    int n = nums.length;\n        if (n <= 2) {\n            return n;\n  \
        \      }\n        int p = 1;\n        while (p <= n) {\n            p <<= 1;\n\
        \        }\n        return p;\n    }\n}"
      python: "class Solution(object):\n    def uniqueXorTriplets(self, nums):\n   \
        \     \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\
        \"\"\n        n = len(nums)\n        if n <= 2:\n            return n\n    \
        \    p = 1\n        while p <= n:\n            p <<= 1\n        return p"
      python3: "class Solution:\n    def uniqueXorTriplets(self, nums: List[int]) ->\
        \ int:\n        n = len(nums)\n        if n <= 2:\n            return n\n  \
        \      p = 1\n        while p <= n:\n            p <<= 1\n        return p"
      c: "int uniqueXorTriplets(int* nums, int numsSize) {\n    if (numsSize <= 2) {\n\
        \        return numsSize;\n    }\n    int p = 1;\n    while (p <= numsSize)\
        \ {\n        p <<= 1;\n    }\n    return p;\n}"
      csharp: "public class Solution {\n    public int UniqueXorTriplets(int[] nums)\
        \ {\n        int n = nums.Length;\n        if (n == 1) return 1;\n        if\
        \ (n == 2) return 2;\n\n        int k = 0;\n        int temp = n;\n        while\
        \ (temp > 0) {\n            temp >>= 1;\n            k++;\n        }\n     \
        \   return 1 << k;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar uniqueXorTriplets\
        \ = function(nums) {\n    let n = nums.length;\n    if (n === 1) return 1;\n\
        \    if (n === 2) return 2;\n\n    let k = 0;\n    let temp = n;\n    while\
        \ (temp > 0) {\n        temp >>= 1;\n        k++;\n    }\n    return 1 << k;\n\
        };"
      typescript: "function uniqueXorTriplets(nums: number[]): number {\n    let n =\
        \ nums.length;\n    if (n === 1) return 1;\n    if (n === 2) return 2;\n\n \
        \   let k = 0;\n    let temp = n;\n    while (temp > 0) {\n        temp >>=\
        \ 1;\n        k++;\n    }\n    return 1 << k;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function uniqueXorTriplets($nums) {\n        $n = count($nums);\n\
        \        if ($n == 1) return 1;\n        if ($n == 2) return 2;\n\n        $k\
        \ = 0;\n        $temp = $n;\n        while ($temp > 0) {\n            $temp\
        \ >>= 1;\n            $k++;\n        }\n        return 1 << $k;\n    }\n}"
      swift: "class Solution {\n    func uniqueXorTriplets(_ nums: [Int]) -> Int {\n\
        \        let n = nums.count\n        if n == 1 { return 1 }\n        if n ==\
        \ 2 { return 2 }\n\n        var k = 0\n        var temp = n\n        while temp\
        \ > 0 {\n            temp >>= 1\n            k += 1\n        }\n        return\
        \ 1 << k\n    }\n}"
      kotlin: "class Solution {\n    fun uniqueXorTriplets(nums: IntArray): Int {\n\
        \        val n = nums.size\n        if (n == 1) return 1\n        if (n == 2)\
        \ return 2\n        var p = 1\n        while (p <= n) {\n            p = p shl\
        \ 1\n        }\n        return p\n    }\n}"
      dart: "class Solution {\n  int uniqueXorTriplets(List<int> nums) {\n    int n\
        \ = nums.length;\n    if (n == 1) return 1;\n    if (n == 2) return 2;\n   \
        \ int p = 1;\n    while (p <= n) {\n      p <<= 1;\n    }\n    return p;\n \
        \ }\n}"
      go: "func uniqueXorTriplets(nums []int) int {\n    n := len(nums)\n    if n ==\
        \ 1 {\n        return 1\n    }\n    if n == 2 {\n        return 2\n    }\n \
        \   p := 1\n    for p <= n {\n        p <<= 1\n    }\n    return p\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef unique_xor_triplets(nums)\n\
        \    n = nums.length\n    return 1 if n == 1\n    return 2 if n == 2\n    p\
        \ = 1\n    while p <= n\n        p <<= 1\n    end\n    p\nend"
      scala: "object Solution {\n    def uniqueXorTriplets(nums: Array[Int]): Int =\
        \ {\n        val n = nums.length\n        if (n == 1) return 1\n        if (n\
        \ == 2) return 2\n        var p = 1\n        while (p <= n) {\n            p\
        \ <<= 1\n        }\n        p\n    }\n}"
      rust: "impl Solution {\n    pub fn unique_xor_triplets(nums: Vec<i32>) -> i32\
        \ {\n        let n = nums.len();\n        if n == 1 {\n            return 1;\n\
        \        }\n        if n == 2 {\n            return 2;\n        }\n\n      \
        \  let mut val: usize = 1;\n        while val <= n {\n            val *= 2;\n\
        \        }\n        val as i32\n    }\n}"
      racket: "(define/contract (unique-xor-triplets nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let ([n (length nums)])\n    (cond\n      [(= n 1) 1]\n\
        \      [(= n 2) 2]\n      [else\n       (let loop ([val 1])\n         (if (>\
        \ val n)\n             val\n             (loop (* val 2))))])))"
      erlang: "-spec unique_xor_triplets(Nums :: [integer()]) -> integer().\nunique_xor_triplets(Nums)\
        \ ->\n  N = length(Nums),\n  if\n    N =:= 1 -> 1;\n    N =:= 2 -> 2;\n    true\
        \ ->\n      F = fun Loop(V) when V > N -> V;\n              Loop(V) -> Loop(V\
        \ * 2)\n          end,\n      F(1)\n  end."
      elixir: "defmodule Solution do\n  @spec unique_xor_triplets(nums :: [integer])\
        \ :: integer\n  def unique_xor_triplets(nums) do\n    n = length(nums)\n   \
        \ cond do\n      n == 1 -> 1\n      n == 2 -> 2\n      true -> \n        next_pow2(1,\
        \ n)\n    end\n  end\n\n  defp next_pow2(val, n) when val > n, do: val\n  defp\
        \ next_pow2(val, n), do: next_pow2(val * 2, n)\nend"
    approach: 'The core intuition for this problem is based on the properties of XOR
      sums within a permutation of integers from 1 to $n$. By selecting indices such
      that $i=j$, the XOR sum of a triplet simplifies to the third element itself: $nums[i]
      \oplus nums[i] \oplus nums[k] = nums[k]$. Since $nums$ is a permutation of $1,
      \dots, n$, every integer from $1$ to $n$ is always a reachable XOR value. For
      $n \ge 3$, the set contains $1, 2,$ and $3$, allowing us to form $1 \oplus 2 \oplus
      3 = 0$. Once $0$ is reachable and we have access to all elements from $1$ to $n$,
      the unique XOR values will span the entire range of the linear basis formed by
      these numbers.


      For $n \ge 3$, the linear basis of the set $\{1, \dots, n\}$ contains all powers
      of $2$ up to the largest power of $2$ less than or equal to $n$. This basis spans
      all integers from $0$ up to $2^{\lfloor \log_2 n \rfloor + 1} - 1$. For the edge
      cases $n=1$ and $n=2$, the XOR space is restricted because $0$ cannot be formed
      as an XOR of three elements from the set. Specifically, for $n=1$, only the value
      $\{1\}$ is reachable, and for $n=2$, only the values $\{1, 2\}$ are reachable.
      For $n \ge 3$, the answer is the smallest power of 2 strictly greater than $n$.'
    time_complexity: O(1) relative to the size of the array, provided that the length
      of the input array can be retrieved in constant time (which is true for Java,
      Python, C++, and C). The bitwise calculations to find the next power of two take
      $O(\log n)$ or $O(1)$ time.
    space_complexity: O(1) extra space is used as we only maintain a few integer variables
      to calculate the result and do not store any intermediate triplets or unique XOR
      values.
    elapsed_time: 324.67695140838623
    model: gemini-3-flash-preview
    generated_at: '2026-07-23 02:08:44 '
---

## Problem #3513: Number of Unique XOR Triplets I

**Difficulty:** Medium

**Topics:** Array, Math, Bit Manipulation

## Problem Description

<p>You are given an integer array <code>nums</code> of length <code>n</code>, where <code>nums</code> is a <strong><span data-keyword="permutation">permutation</span></strong> of the numbers in the range <code>[1, n]</code>.</p>

<p>A <strong>XOR triplet</strong> is defined as the XOR of three elements <code>nums[i] XOR nums[j] XOR nums[k]</code> where <code>i &lt;= j &lt;= k</code>.</p>

<p>Return the number of <strong>unique</strong> XOR triplet values from all possible triplets <code>(i, j, k)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The possible XOR triplet values are:</p>

<ul>
	<li><code>(0, 0, 0) &rarr; 1 XOR 1 XOR 1 = 1</code></li>
	<li><code>(0, 0, 1) &rarr; 1 XOR 1 XOR 2 = 2</code></li>
	<li><code>(0, 1, 1) &rarr; 1 XOR 2 XOR 2 = 1</code></li>
	<li><code>(1, 1, 1) &rarr; 2 XOR 2 XOR 2 = 2</code></li>
</ul>

<p>The unique XOR values are <code>{1, 2}</code>, so the output is 2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The possible XOR triplet values include:</p>

<ul>
	<li><code>(0, 0, 0) &rarr; 3 XOR 3 XOR 3 = 3</code></li>
	<li><code>(0, 0, 1) &rarr; 3 XOR 3 XOR 1 = 1</code></li>
	<li><code>(0, 0, 2) &rarr; 3 XOR 3 XOR 2 = 2</code></li>
	<li><code>(0, 1, 2) &rarr; 3 XOR 1 XOR 2 = 0</code></li>
</ul>

<p>The unique XOR values are <code>{0, 1, 2, 3}</code>, so the output is 4.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
	<li><code>nums</code> is a permutation of integers from <code>1</code> to <code>n</code>.</li>
</ul>


## Hints

1. What is the maximum and minimum value we can obtain using the given numbers?

2. Can we generate all numbers within that range?

3. For `n >= 3` we can obtain all numbers in `[0, 2^(msb(n) + 1) - 1]`, where `msb(n)` is the index of the most significant bit in `n`’s binary representation (i.e., the highest power of 2 less than or equal to `n`). Handle the case when `n <= 2` separately.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core intuition for this problem is based on the properties of XOR sums within a permutation of integers from 1 to $n$. By selecting indices such that $i=j$, the XOR sum of a triplet simplifies to the third element itself: $nums[i] \oplus nums[i] \oplus nums[k] = nums[k]$. Since $nums$ is a permutation of $1, \dots, n$, every integer from $1$ to $n$ is always a reachable XOR value. For $n \ge 3$, the set contains $1, 2,$ and $3$, allowing us to form $1 \oplus 2 \oplus 3 = 0$. Once $0$ is reachable and we have access to all elements from $1$ to $n$, the unique XOR values will span the entire range of the linear basis formed by these numbers.

For $n \ge 3$, the linear basis of the set $\{1, \dots, n\}$ contains all powers of $2$ up to the largest power of $2$ less than or equal to $n$. This basis spans all integers from $0$ up to $2^{\lfloor \log_2 n \rfloor + 1} - 1$. For the edge cases $n=1$ and $n=2$, the XOR space is restricted because $0$ cannot be formed as an XOR of three elements from the set. Specifically, for $n=1$, only the value $\{1\}$ is reachable, and for $n=2$, only the values $\{1, 2\}$ are reachable. For $n \ge 3$, the answer is the smallest power of 2 strictly greater than $n$.

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
    int uniqueXorTriplets(vector<int>& nums) {
        int n = nums.size();
        if (n <= 2) {
            return n;
        }
        int p = 1;
        while (p <= n) {
            p <<= 1;
        }
        return p;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int uniqueXorTriplets(int[] nums) {
        int n = nums.length;
        if (n <= 2) {
            return n;
        }
        int p = 1;
        while (p <= n) {
            p <<= 1;
        }
        return p;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n
        p = 1
        while p <= n:
            p <<= 1
        return p
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        p = 1
        while p <= n:
            p <<= 1
        return p
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int uniqueXorTriplets(int* nums, int numsSize) {
    if (numsSize <= 2) {
        return numsSize;
    }
    int p = 1;
    while (p <= numsSize) {
        p <<= 1;
    }
    return p;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int UniqueXorTriplets(int[] nums) {
        int n = nums.Length;
        if (n == 1) return 1;
        if (n == 2) return 2;

        int k = 0;
        int temp = n;
        while (temp > 0) {
            temp >>= 1;
            k++;
        }
        return 1 << k;
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
var uniqueXorTriplets = function(nums) {
    let n = nums.length;
    if (n === 1) return 1;
    if (n === 2) return 2;

    let k = 0;
    let temp = n;
    while (temp > 0) {
        temp >>= 1;
        k++;
    }
    return 1 << k;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function uniqueXorTriplets(nums: number[]): number {
    let n = nums.length;
    if (n === 1) return 1;
    if (n === 2) return 2;

    let k = 0;
    let temp = n;
    while (temp > 0) {
        temp >>= 1;
        k++;
    }
    return 1 << k;
}
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
    function uniqueXorTriplets($nums) {
        $n = count($nums);
        if ($n == 1) return 1;
        if ($n == 2) return 2;

        $k = 0;
        $temp = $n;
        while ($temp > 0) {
            $temp >>= 1;
            $k++;
        }
        return 1 << $k;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func uniqueXorTriplets(_ nums: [Int]) -> Int {
        let n = nums.count
        if n == 1 { return 1 }
        if n == 2 { return 2 }

        var k = 0
        var temp = n
        while temp > 0 {
            temp >>= 1
            k += 1
        }
        return 1 << k
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun uniqueXorTriplets(nums: IntArray): Int {
        val n = nums.size
        if (n == 1) return 1
        if (n == 2) return 2
        var p = 1
        while (p <= n) {
            p = p shl 1
        }
        return p
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int uniqueXorTriplets(List<int> nums) {
    int n = nums.length;
    if (n == 1) return 1;
    if (n == 2) return 2;
    int p = 1;
    while (p <= n) {
      p <<= 1;
    }
    return p;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func uniqueXorTriplets(nums []int) int {
    n := len(nums)
    if n == 1 {
        return 1
    }
    if n == 2 {
        return 2
    }
    p := 1
    for p <= n {
        p <<= 1
    }
    return p
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def unique_xor_triplets(nums)
    n = nums.length
    return 1 if n == 1
    return 2 if n == 2
    p = 1
    while p <= n
        p <<= 1
    end
    p
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def uniqueXorTriplets(nums: Array[Int]): Int = {
        val n = nums.length
        if (n == 1) return 1
        if (n == 2) return 2
        var p = 1
        while (p <= n) {
            p <<= 1
        }
        p
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn unique_xor_triplets(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 1 {
            return 1;
        }
        if n == 2 {
            return 2;
        }

        let mut val: usize = 1;
        while val <= n {
            val *= 2;
        }
        val as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (unique-xor-triplets nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ([n (length nums)])
    (cond
      [(= n 1) 1]
      [(= n 2) 2]
      [else
       (let loop ([val 1])
         (if (> val n)
             val
             (loop (* val 2))))])))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec unique_xor_triplets(Nums :: [integer()]) -> integer().
unique_xor_triplets(Nums) ->
  N = length(Nums),
  if
    N =:= 1 -> 1;
    N =:= 2 -> 2;
    true ->
      F = fun Loop(V) when V > N -> V;
              Loop(V) -> Loop(V * 2)
          end,
      F(1)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec unique_xor_triplets(nums :: [integer]) :: integer
  def unique_xor_triplets(nums) do
    n = length(nums)
    cond do
      n == 1 -> 1
      n == 2 -> 2
      true -> 
        next_pow2(1, n)
    end
  end

  defp next_pow2(val, n) when val > n, do: val
  defp next_pow2(val, n), do: next_pow2(val * 2, n)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(1) relative to the size of the array, provided that the length of the input array can be retrieved in constant time (which is true for Java, Python, C++, and C). The bitwise calculations to find the next power of two take $O(\log n)$ or $O(1)$ time.
- **Space Complexity:** O(1) extra space is used as we only maintain a few integer variables to calculate the result and do not store any intermediate triplets or unique XOR values.
