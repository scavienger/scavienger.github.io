---
layout: post
title: "GCD of Odd and Even Sums"
date: 2026-07-15 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Math", "Number Theory"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/gcd-of-odd-and-even-sums/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int gcdOfOddEvenSums(int n) {\n        return\
        \ n;\n    }\n};"
      java: "class Solution {\n    public int gcdOfOddEvenSums(int n) {\n        return\
        \ n;\n    }\n}"
      python: "class Solution(object):\n    def gcdOfOddEvenSums(self, n):\n       \
        \ \"\"\"\n        :type n: int\n        :rtype: int\n        \"\"\"\n      \
        \  return n"
      python3: "class Solution:\n    def gcdOfOddEvenSums(self, n: int) -> int:\n  \
        \      return n"
      c: "int gcdOfOddEvenSums(int n) {\n    return n;\n}"
      csharp: "public class Solution {\n    public int GcdOfOddEvenSums(int n) {\n \
        \       return n;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @return {number}\n */\nvar gcdOfOddEvenSums\
        \ = function(n) {\n    return n;\n};"
      typescript: "function gcdOfOddEvenSums(n: number): number {\n  return n;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @return Integer\n\
        \     */\n    function gcdOfOddEvenSums($n) {\n        return $n;\n    }\n}"
      swift: "class Solution {\n    func gcdOfOddEvenSums(_ n: Int) -> Int {\n     \
        \   return n\n    }\n}"
      kotlin: "class Solution {\n    fun gcdOfOddEvenSums(n: Int): Int {\n        return\
        \ n\n    }\n}"
      dart: "class Solution {\n  int gcdOfOddEvenSums(int n) {\n    return n;\n  }\n\
        }"
      go: "func gcdOfOddEvenSums(n int) int {\n    return n\n}"
      ruby: "# @param {Integer} n\n# @return {Integer}\ndef gcd_of_odd_even_sums(n)\n\
        \  n\nend"
      scala: "object Solution {\n    def gcdOfOddEvenSums(n: Int): Int = {\n       \
        \ n\n    }\n}"
      rust: "impl Solution {\n    pub fn gcd_of_odd_even_sums(n: i32) -> i32 {\n   \
        \     n\n    }\n}"
      racket: "(define/contract (gcd-of-odd-even-sums n)\n  (-> exact-integer? exact-integer?)\n\
        \  n\n)"
      erlang: "-spec gcd_of_odd_even_sums(N :: integer()) -> integer().\ngcd_of_odd_even_sums(N)\
        \ ->\n  N."
      elixir: "defmodule Solution do\n  @spec gcd_of_odd_even_sums(n :: integer) ::\
        \ integer\n  def gcd_of_odd_even_sums(n) do\n    n\n  end\nend"
    approach: 'The sum of the first n positive odd numbers is an arithmetic progression
      that simplifies to $n^2$. Similarly, the sum of the first n positive even numbers
      is an arithmetic progression starting from 2 with a common difference of 2, which
      simplifies to $n(n + 1)$. Therefore, the problem reduces to finding the greatest
      common divisor of $n^2$ and $n(n + 1)$.


      Using the Euclidean property $GCD(a, b) = GCD(a, b - a)$, we can simplify $GCD(n^2,
      n^2 + n)$ to $GCD(n^2, n)$. Since $n$ is a factor of $n^2$, the greatest common
      divisor of $n^2$ and $n$ is simply $n$. Thus, for any positive integer $n$, the
      result of the calculation is always $n$.'
    time_complexity: 'O(1) with one-paragraph explanation.

      The solution returns the input value directly or performs a constant number of
      arithmetic operations, resulting in constant time complexity regardless of the
      size of $n$.'
    space_complexity: 'O(1) with one-paragraph explanation.

      The solution uses a fixed amount of space to store the input and does not require
      any additional data structures or recursion.'
    elapsed_time: 13.21441912651062
    model: gemini-3-flash-preview
    generated_at: '2026-07-15 01:44:27 '
---

## Problem #3658: GCD of Odd and Even Sums

**Difficulty:** Easy

**Topics:** Math, Number Theory

## Problem Description

<p>You are given an integer <code>n</code>. Your task is to compute the <strong>GCD</strong> (greatest common divisor) of two values:</p>

<ul>
	<li>
	<p><code>sumOdd</code>: the sum of the smallest&nbsp;<code>n</code>&nbsp;positive odd numbers.</p>
	</li>
	<li>
	<p><code>sumEven</code>: the sum of the smallest&nbsp;<code>n</code>&nbsp;positive even numbers.</p>
	</li>
</ul>

<p>Return the GCD of <code>sumOdd</code> and <code>sumEven</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Sum of the first 4 odd numbers <code>sumOdd = 1 + 3 + 5 + 7 = 16</code></li>
	<li>Sum of the first 4 even numbers <code>sumEven = 2 + 4 + 6 + 8 = 20</code></li>
</ul>

<p>Hence, <code>GCD(sumOdd, sumEven) = GCD(16, 20) = 4</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Sum of the first 5 odd numbers <code>sumOdd = 1 + 3 + 5 + 7 + 9 = 25</code></li>
	<li>Sum of the first 5 even numbers <code>sumEven = 2 + 4 + 6 + 8 + 10 = 30</code></li>
</ul>

<p>Hence, <code>GCD(sumOdd, sumEven) = GCD(25, 30) = 5</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10​​​​​​​00</code></li>
</ul>


## Hints

1. The first `n` odd numbers sum to `n * n`

2. First `n` even numbers sum to `n * (n + 1)`

3. `gcd(n, n + 1) = 1`, so the answer is `n`

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The sum of the first n positive odd numbers is an arithmetic progression that simplifies to $n^2$. Similarly, the sum of the first n positive even numbers is an arithmetic progression starting from 2 with a common difference of 2, which simplifies to $n(n + 1)$. Therefore, the problem reduces to finding the greatest common divisor of $n^2$ and $n(n + 1)$.

Using the Euclidean property $GCD(a, b) = GCD(a, b - a)$, we can simplify $GCD(n^2, n^2 + n)$ to $GCD(n^2, n)$. Since $n$ is a factor of $n^2$, the greatest common divisor of $n^2$ and $n$ is simply $n$. Thus, for any positive integer $n$, the result of the calculation is always $n$.

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
    int gcdOfOddEvenSums(int n) {
        return n;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int gcdOfOddEvenSums(int n) {
        return n;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int gcdOfOddEvenSums(int n) {
    return n;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int GcdOfOddEvenSums(int n) {
        return n;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} n
 * @return {number}
 */
var gcdOfOddEvenSums = function(n) {
    return n;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function gcdOfOddEvenSums(n: number): number {
  return n;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function gcdOfOddEvenSums($n) {
        return $n;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func gcdOfOddEvenSums(_ n: Int) -> Int {
        return n
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun gcdOfOddEvenSums(n: Int): Int {
        return n
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int gcdOfOddEvenSums(int n) {
    return n;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func gcdOfOddEvenSums(n int) int {
    return n
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @return {Integer}
def gcd_of_odd_even_sums(n)
  n
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def gcdOfOddEvenSums(n: Int): Int = {
        n
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn gcd_of_odd_even_sums(n: i32) -> i32 {
        n
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (gcd-of-odd-even-sums n)
  (-> exact-integer? exact-integer?)
  n
)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec gcd_of_odd_even_sums(N :: integer()) -> integer().
gcd_of_odd_even_sums(N) ->
  N.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec gcd_of_odd_even_sums(n :: integer) :: integer
  def gcd_of_odd_even_sums(n) do
    n
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(1) with one-paragraph explanation.
The solution returns the input value directly or performs a constant number of arithmetic operations, resulting in constant time complexity regardless of the size of $n$.
- **Space Complexity:** O(1) with one-paragraph explanation.
The solution uses a fixed amount of space to store the input and does not require any additional data structures or recursion.
