---
layout: post
title: "Count Odd Numbers in an Interval Range"
date: 2025-12-07 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Math"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int countOdds(int low, int high) {\n    \
        \    return (high + 1) / 2 - low / 2;\n    }\n};"
      java: "class Solution {\n    public int countOdds(int low, int high) {\n     \
        \   return (high + 1) / 2 - low / 2;\n    }\n}"
      python: "class Solution:\n    def countOdds(self, low: int, high: int) -> int:\n\
        \        return (high + 1) // 2 - (low // 2)"
      python3: "class Solution:\n    def countOdds(self, low: int, high: int) -> int:\n\
        \        return (high + 1) // 2 - (low // 2)"
      c: "int countOdds(int low, int high) {\n    return (high + 1) / 2 - low / 2;\n\
        }"
      csharp: "public class Solution {\n    public int CountOdds(int low, int high)\
        \ {\n        return (high + 1) / 2 - low / 2;\n    }\n}"
      javascript: "/**\n * @param {number} low\n * @param {number} high\n * @return\
        \ {number}\n */\nvar countOdds = function(low, high) {\n    return Math.floor((high\
        \ + 1) / 2) - Math.floor(low / 2);\n};"
      typescript: "function countOdds(low: number, high: number): number {\n    return\
        \ Math.floor((high + 1) / 2) - Math.floor(low / 2);\n}"
      php: "class Solution {\n    /**\n     * @param Integer $low\n     * @param Integer\
        \ $high\n     * @return Integer\n     */\n    function countOdds($low, $high)\
        \ {\n        return floor(($high + 1) / 2) - floor($low / 2);\n    }\n}"
      swift: "class Solution {\n    func countOdds(_ low: Int, _ high: Int) -> Int {\n\
        \        return (high + 1) / 2 - low / 2\n    }\n}"
      kotlin: "class Solution {\n    fun countOdds(low: Int, high: Int): Int {\n   \
        \     return (high + 1) / 2 - low / 2\n    }\n}"
      dart: "class Solution {\n  int countOdds(int low, int high) {\n    return (high\
        \ + 1) ~/ 2 - low ~/ 2;\n  }\n}"
      go: "func countOdds(low int, high int) int {\n    return (high + 1) / 2 - low\
        \ / 2\n}"
      ruby: "def count_odds(low, high)\n    (high + 1) / 2 - low / 2\nend"
      scala: "object Solution {\n    def countOdds(low: Int, high: Int): Int = {\n \
        \       (high + 1) / 2 - low / 2\n    }\n}"
      rust: "impl Solution {\n    pub fn count_odds(low: i32, high: i32) -> i32 {\n\
        \        (high + 1) / 2 - low / 2\n    }\n}"
      racket: "(define/contract (count-odds low high)\n  (-> exact-integer? exact-integer?\
        \ exact-integer?)\n  (- (quotient (+ high 1) 2) (quotient low 2)))"
      erlang: "-spec count_odds(Low :: integer(), High :: integer()) -> integer().\n\
        count_odds(Low, High) ->\n  (High + 1) div 2 - Low div 2."
      elixir: "defmodule Solution do\n  @spec count_odds(low :: integer(), high :: integer())\
        \ :: integer()\n  def count_odds(low, high) do\n    div(high + 1, 2) - div(low,\
        \ 2)\n  end\nend"
    approach: The problem asks us to count the number of odd integers within a given
      inclusive range [low, high]. A straightforward approach involves calculating the
      count of odd numbers up to 'high' and subtracting the count of odd numbers up
      to 'low - 1'. This effectively isolates the odd numbers within the desired range.
      We define a helper function, or directly use the logic, to count odd numbers from
      0 (or 1) up to a given number N. For any non-negative integer N, the count of
      odd numbers in the range [0, N] (or [1, N]) can be found using integer division
      as (N + 1) // 2. For example, for N=7, (7+1)//2 = 4 (odds are 1, 3, 5, 7). For
      N=8, (8+1)//2 = 4 (odds are 1, 3, 5, 7). This formula correctly handles both even
      and odd N.
    time_complexity: The time complexity is O(1). The solution involves a fixed number
      of arithmetic operations (addition, subtraction, and division), which take constant
      time regardless of the input values 'low' and 'high'.
    space_complexity: The space complexity is O(1). The solution uses a constant amount
      of extra space to store a few integer variables for calculations, which does not
      depend on the size of the input range.
    elapsed_time: 17.625544548034668
    model: gemini-2.5-flash
    generated_at: '2025-12-07 01:11:50 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int countOdds(int low, int high) {\n    \
        \    return (high + 1) / 2 - low / 2;\n    }\n};"
      java: "class Solution {\n    public int countOdds(int low, int high) {\n     \
        \   return (high + 1) / 2 - low / 2;\n    }\n}"
      python: "class Solution:\n    def countOdds(self, low: int, high: int) -> int:\n\
        \        return (high + 1) // 2 - low // 2"
      python3: "class Solution:\n    def countOdds(self, low: int, high: int) -> int:\n\
        \        return (high + 1) // 2 - low // 2"
      c: "int countOdds(int low, int high) {\n    return (high + 1) / 2 - low / 2;\n\
        }"
      csharp: "public class Solution {\n    public int CountOdds(int low, int high)\
        \ {\n        return (high + 1) / 2 - low / 2;\n    }\n}"
      javascript: "var countOdds = function(low, high) {\n    return Math.floor((high\
        \ + 1) / 2) - Math.floor(low / 2);\n};"
      typescript: "function countOdds(low: number, high: number): number {\n    return\
        \ Math.floor((high + 1) / 2) - Math.floor(low / 2);\n}"
      php: "function countOdds($low, $high) {\n    return floor(($high + 1) / 2) - floor($low\
        \ / 2);\n}"
      swift: "class Solution {\n    func countOdds(_ low: Int, _ high: Int) -> Int {\n\
        \        return (high + 1) / 2 - low / 2\n    }\n}"
      kotlin: "class Solution {\n    fun countOdds(low: Int, high: Int): Int {\n   \
        \     return (high + 1) / 2 - low / 2\n    }\n}"
      dart: "class Solution {\n    int countOdds(int low, int high) {\n        return\
        \ (high + 1) ~/ 2 - low ~/ 2;\n    }\n}"
      go: "func countOdds(low int, high int) int {\n    return (high + 1) / 2 - low\
        \ / 2\n}"
      ruby: "def count_odds(low, high)\n    (high + 1) / 2 - low / 2\nend"
      scala: "object Solution {\n    def countOdds(low: Int, high: Int): Int = (high\
        \ + 1) / 2 - low / 2\n}"
      rust: "impl Solution {\n    pub fn count_odds(low: i32, high: i32) -> i32 {\n\
        \        (high + 1) / 2 - low / 2\n    }\n}"
      racket: "(define (count-odds low high)\n    (quotient (+ high 1) 2) - (quotient\
        \ low 2))"
      erlang: count_odds(Low, High) -> (High + 1) div 2 - Low div 2.
      elixir: "def count_odds(low, high) do\n    div(high + 1, 2) - div(low, 2)\nend"
    approach: The problem can be solved by first calculating the total number of integers
      in the range from low to high, and then determining the number of odd integers
      in this range. If the range (high - low + 1) is even, the number of even and odd
      numbers in this range will be the same. If the range (high - low + 1) is odd,
      the solution will depend on the parity of high and low. We can use the formula
      (high + 1) // 2 - low // 2 to calculate the number of odd integers in the range.
    time_complexity: The time complexity of this solution is O(1) because it involves
      a constant number of operations, regardless of the input size. The solution does
      not contain any loops or recursive calls that depend on the input size, so the
      time complexity is constant.
    space_complexity: The space complexity of this solution is O(1) because it uses
      a constant amount of space to store the input variables and the result. The solution
      does not use any data structures that grow with the input size, so the space complexity
      is constant.
    elapsed_time: 2.1811559200286865
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-07 01:11:52 '
---

## Problem #1523: Count Odd Numbers in an Interval Range

**Difficulty:** Easy

**Topics:** Math

## Problem Description

<p>Given two non-negative integers <code>low</code> and <code><font face="monospace">high</font></code>. Return the <em>count of odd numbers between </em><code>low</code><em> and </em><code><font face="monospace">high</font></code><em>&nbsp;(inclusive)</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> low = 3, high = 7
<strong>Output:</strong> 3
<b>Explanation: </b>The odd numbers between 3 and 7 are [3,5,7].</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> low = 8, high = 10
<strong>Output:</strong> 1
<b>Explanation: </b>The odd numbers between 8 and 10 are [9].</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= low &lt;= high&nbsp;&lt;= 10^9</code></li>
</ul>

## Hints

1. If the range (high - low + 1) is even, the number of even and odd numbers in this range will be the same.

2. If the range (high - low + 1) is odd, the solution will depend on the parity of high and low.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-07 01:11:50 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to count the number of odd integers within a given inclusive range [low, high]. A straightforward approach involves calculating the count of odd numbers up to 'high' and subtracting the count of odd numbers up to 'low - 1'. This effectively isolates the odd numbers within the desired range. We define a helper function, or directly use the logic, to count odd numbers from 0 (or 1) up to a given number N. For any non-negative integer N, the count of odd numbers in the range [0, N] (or [1, N]) can be found using integer division as (N + 1) // 2. For example, for N=7, (7+1)//2 = 4 (odds are 1, 3, 5, 7). For N=8, (8+1)//2 = 4 (odds are 1, 3, 5, 7). This formula correctly handles both even and odd N.

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
    int countOdds(int low, int high) {
        return (high + 1) / 2 - low / 2;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countOdds(int low, int high) {
        return (high + 1) / 2 - low / 2;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - (low // 2)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - (low // 2)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countOdds(int low, int high) {
    return (high + 1) / 2 - low / 2;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountOdds(int low, int high) {
        return (high + 1) / 2 - low / 2;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countOdds = function(low, high) {
    return Math.floor((high + 1) / 2) - Math.floor(low / 2);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countOdds(low: number, high: number): number {
    return Math.floor((high + 1) / 2) - Math.floor(low / 2);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    /**
     * @param Integer $low
     * @param Integer $high
     * @return Integer
     */
    function countOdds($low, $high) {
        return floor(($high + 1) / 2) - floor($low / 2);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countOdds(_ low: Int, _ high: Int) -> Int {
        return (high + 1) / 2 - low / 2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countOdds(low: Int, high: Int): Int {
        return (high + 1) / 2 - low / 2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int countOdds(int low, int high) {
    return (high + 1) ~/ 2 - low ~/ 2;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func countOdds(low int, high int) int {
    return (high + 1) / 2 - low / 2
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def count_odds(low, high)
    (high + 1) / 2 - low / 2
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countOdds(low: Int, high: Int): Int = {
        (high + 1) / 2 - low / 2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_odds(low: i32, high: i32) -> i32 {
        (high + 1) / 2 - low / 2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (count-odds low high)
  (-> exact-integer? exact-integer? exact-integer?)
  (- (quotient (+ high 1) 2) (quotient low 2)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec count_odds(Low :: integer(), High :: integer()) -> integer().
count_odds(Low, High) ->
  (High + 1) div 2 - Low div 2.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_odds(low :: integer(), high :: integer()) :: integer()
  def count_odds(low, high) do
    div(high + 1, 2) - div(low, 2)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(1). The solution involves a fixed number of arithmetic operations (addition, subtraction, and division), which take constant time regardless of the input values 'low' and 'high'.

- **Space Complexity:** The space complexity is O(1). The solution uses a constant amount of extra space to store a few integer variables for calculations, which does not depend on the size of the input range.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-07 01:11:52 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by first calculating the total number of integers in the range from low to high, and then determining the number of odd integers in this range. If the range (high - low + 1) is even, the number of even and odd numbers in this range will be the same. If the range (high - low + 1) is odd, the solution will depend on the parity of high and low. We can use the formula (high + 1) // 2 - low // 2 to calculate the number of odd integers in the range.

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
    int countOdds(int low, int high) {
        return (high + 1) / 2 - low / 2;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countOdds(int low, int high) {
        return (high + 1) / 2 - low / 2;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countOdds(int low, int high) {
    return (high + 1) / 2 - low / 2;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountOdds(int low, int high) {
        return (high + 1) / 2 - low / 2;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var countOdds = function(low, high) {
    return Math.floor((high + 1) / 2) - Math.floor(low / 2);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countOdds(low: number, high: number): number {
    return Math.floor((high + 1) / 2) - Math.floor(low / 2);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
function countOdds($low, $high) {
    return floor(($high + 1) / 2) - floor($low / 2);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countOdds(_ low: Int, _ high: Int) -> Int {
        return (high + 1) / 2 - low / 2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countOdds(low: Int, high: Int): Int {
        return (high + 1) / 2 - low / 2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int countOdds(int low, int high) {
        return (high + 1) ~/ 2 - low ~/ 2;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func countOdds(low int, high int) int {
    return (high + 1) / 2 - low / 2
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def count_odds(low, high)
    (high + 1) / 2 - low / 2
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countOdds(low: Int, high: Int): Int = (high + 1) / 2 - low / 2
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_odds(low: i32, high: i32) -> i32 {
        (high + 1) / 2 - low / 2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define (count-odds low high)
    (quotient (+ high 1) 2) - (quotient low 2))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
count_odds(Low, High) -> (High + 1) div 2 - Low div 2.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def count_odds(low, high) do
    div(high + 1, 2) - div(low, 2)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(1) because it involves a constant number of operations, regardless of the input size. The solution does not contain any loops or recursive calls that depend on the input size, so the time complexity is constant.

- **Space Complexity:** The space complexity of this solution is O(1) because it uses a constant amount of space to store the input variables and the result. The solution does not use any data structures that grow with the input size, so the space complexity is constant.

</div>
</details>
