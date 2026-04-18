---
layout: post
title: "Mirror Distance of an Integer"
date: 2026-04-18 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Math"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/mirror-distance-of-an-integer/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int mirrorDistance(int n) {\n        long\
        \ long original = n;\n        long long reversed = 0;\n        long long temp\
        \ = n;\n        while (temp > 0) {\n            reversed = reversed * 10 + (temp\
        \ % 10);\n            temp /= 10;\n        }\n        long long diff = original\
        \ - reversed;\n        return (int)(diff < 0 ? -diff : diff);\n    }\n};"
      java: "class Solution {\n    public int mirrorDistance(int n) {\n        long\
        \ original = n;\n        long reversed = 0;\n        long temp = n;\n      \
        \  while (temp > 0) {\n            reversed = reversed * 10 + (temp % 10);\n\
        \            temp /= 10;\n        }\n        long diff = original - reversed;\n\
        \        return (int) Math.abs(diff);\n    }\n}"
      python: "class Solution(object):\n    def mirrorDistance(self, n):\n        \"\
        \"\"\n        :type n: int\n        :rtype: int\n        \"\"\"\n        original\
        \ = n\n        reversed_n = 0\n        temp = n\n        while temp > 0:\n \
        \           reversed_n = reversed_n * 10 + (temp % 10)\n            temp //=\
        \ 10\n        return abs(original - reversed_n)"
      python3: "class Solution:\n    def mirrorDistance(self, n: int) -> int:\n    \
        \    original = n\n        reversed_n = 0\n        temp = n\n        while temp\
        \ > 0:\n            reversed_n = reversed_n * 10 + (temp % 10)\n           \
        \ temp //= 10\n        return abs(original - reversed_n)"
      c: "int mirrorDistance(int n) {\n    long long original = n;\n    long long reversed\
        \ = 0;\n    long long temp = n;\n    while (temp > 0) {\n        reversed =\
        \ reversed * 10 + (temp % 10);\n        temp /= 10;\n    }\n    long long diff\
        \ = original - reversed;\n    if (diff < 0) return (int)(-diff);\n    return\
        \ (int)diff;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public int MirrorDistance(int\
        \ n) {\n        long original = n;\n        long reversed = 0;\n        long\
        \ temp = n;\n        while (temp > 0) {\n            reversed = reversed * 10\
        \ + (temp % 10);\n            temp /= 10;\n        }\n        long diff = original\
        \ - reversed;\n        return (int)Math.Abs(diff);\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @return {number}\n */\nvar mirrorDistance\
        \ = function(n) {\n    let original = n;\n    let reversed = 0;\n    let temp\
        \ = n;\n    while (temp > 0) {\n        reversed = reversed * 10 + (temp % 10);\n\
        \        temp = Math.floor(temp / 10);\n    }\n    return Math.abs(original\
        \ - reversed);\n};"
      typescript: "function mirrorDistance(n: number): number {\n    let rev = 0;\n\
        \    let temp = n;\n    while (temp > 0) {\n        rev = rev * 10 + (temp %\
        \ 10);\n        temp = Math.floor(temp / 10);\n    }\n    return Math.abs(n\
        \ - rev);\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @return Integer\n\
        \     */\n    function mirrorDistance($n) {\n        $rev = 0;\n        $temp\
        \ = $n;\n        while ($temp > 0) {\n            $rev = $rev * 10 + ($temp\
        \ % 10);\n            $temp = intdiv($temp, 10);\n        }\n        return\
        \ abs($n - $rev);\n    }\n}"
      swift: "class Solution {\n    func mirrorDistance(_ n: Int) -> Int {\n       \
        \ var rev = 0\n        var temp = n\n        while temp > 0 {\n            rev\
        \ = rev * 10 + (temp % 10)\n            temp /= 10\n        }\n        return\
        \ abs(n - rev)\n    }\n}"
      kotlin: "class Solution {\n    fun mirrorDistance(n: Int): Int {\n        var\
        \ rev = 0\n        var temp = n\n        while (temp > 0) {\n            rev\
        \ = rev * 10 + (temp % 10)\n            temp /= 10\n        }\n        return\
        \ Math.abs(n - rev)\n    }\n}"
      dart: "class Solution {\n  int mirrorDistance(int n) {\n    int rev = 0;\n   \
        \ int temp = n;\n    while (temp > 0) {\n      rev = rev * 10 + (temp % 10);\n\
        \      temp ~/= 10;\n    }\n    return (n - rev).abs();\n  }\n}"
      go: "func mirrorDistance(n int) int {\n    rev := 0\n    temp := n\n    for temp\
        \ > 0 {\n        rev = rev*10 + (temp % 10)\n        temp /= 10\n    }\n   \
        \ diff := n - rev\n    if diff < 0 {\n        return -diff\n    }\n    return\
        \ diff\n}"
      ruby: "# @param {Integer} n\n# @return {Integer}\ndef mirror_distance(n)\n  rev_n\
        \ = n.to_s.reverse.to_i\n  (n - rev_n).abs\nend"
      scala: "object Solution {\n    def mirrorDistance(n: Int): Int = {\n        var\
        \ original = n\n        var reversed = 0\n        while (original > 0) {\n \
        \           reversed = reversed * 10 + (original % 10)\n            original\
        \ /= 10\n        }\n        if (n > reversed) n - reversed else reversed - n\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn mirror_distance(n: i32) -> i32 {\n        let\
        \ mut original = n;\n        let mut reversed: i32 = 0;\n        while original\
        \ > 0 {\n            reversed = reversed * 10 + (original % 10);\n         \
        \   original /= 10;\n        }\n        (n - reversed).abs()\n    }\n}"
      racket: "(define/contract (mirror-distance n)\n  (-> exact-integer? exact-integer?)\n\
        \  (let* ([s (number->string n)]\n         [rev-s (list->string (reverse (string->list\
        \ s)))]\n         [rev-n (string->number rev-s)])\n    (abs (- n rev-n))))"
      erlang: "-spec mirror_distance(N :: integer()) -> integer().\nmirror_distance(N)\
        \ ->\n  RevN = list_to_integer(lists:reverse(integer_to_list(N))),\n  abs(N\
        \ - RevN)."
      elixir: "defmodule Solution do\n  @spec mirror_distance(n :: integer) :: integer\n\
        \  def mirror_distance(n) do\n    rev_n = n\n      |> Integer.to_string()\n\
        \      |> String.reverse()\n      |> String.to_integer()\n    abs(n - rev_n)\n\
        \  end\nend"
    approach: 'To calculate the mirror distance, we first reverse the digits of the
      given integer n. This is done by repeatedly taking the last digit of the number
      using the modulo operator (n % 10) and building the reversed number digit by digit.
      Each new digit is added by multiplying the current reversed value by 10 and then
      adding the digit, while the original number is reduced by integer division until
      it reaches zero.


      After obtaining the reversed integer, the mirror distance is simply the absolute
      difference between the original integer and its reversed version. We calculate
      this by subtracting the reversed value from the stored original value and applying
      the absolute value operation. This process correctly handles cases where the reverse
      is larger, smaller, or equal to the original number, returning the non-negative
      distance between them.'
    time_complexity: 'O(log n) with one-paragraph explanation.

      The time complexity is determined by the number of digits in the integer n, which
      is floor(log10(n)) + 1. Since the algorithm iterates through each digit exactly
      once to reverse the number, the total number of operations is proportional to
      the number of digits in the input.'
    space_complexity: 'O(1) with one-paragraph explanation.

      The algorithm uses a fixed amount of extra space to store the original number,
      the reversed number, and temporary variables for the calculation. This space does
      not grow with the size of the input, leading to constant space complexity.'
    elapsed_time: 169.1436309814453
    model: gemini-3-flash-preview
    generated_at: '2026-04-18 01:49:09 '
---

## Problem #3783: Mirror Distance of an Integer

**Difficulty:** Easy

**Topics:** Math

## Problem Description

<p>You are given an integer <code>n</code>.</p>

<p>Define its <strong>mirror distance</strong> as: <code>abs(n - reverse(n))</code>​​​​​​​ where <code>reverse(n)</code> is the integer formed by reversing the digits of <code>n</code>.</p>

<p>Return an integer denoting the mirror distance of <code>n</code>​​​​​​​.</p>

<p><code>abs(x)</code> denotes the absolute value of <code>x</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 25</span></p>

<p><strong>Output:</strong> <span class="example-io">27</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>reverse(25) = 52</code>.</li>
	<li>Thus, the answer is <code>abs(25 - 52) = 27</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 10</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>reverse(10) = 01</code> which is 1.</li>
	<li>Thus, the answer is <code>abs(10 - 1) = 9</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 7</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>reverse(7) = 7</code>.</li>
	<li>Thus, the answer is <code>abs(7 - 7) = 0</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Simulate as described

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To calculate the mirror distance, we first reverse the digits of the given integer n. This is done by repeatedly taking the last digit of the number using the modulo operator (n % 10) and building the reversed number digit by digit. Each new digit is added by multiplying the current reversed value by 10 and then adding the digit, while the original number is reduced by integer division until it reaches zero.

After obtaining the reversed integer, the mirror distance is simply the absolute difference between the original integer and its reversed version. We calculate this by subtracting the reversed value from the stored original value and applying the absolute value operation. This process correctly handles cases where the reverse is larger, smaller, or equal to the original number, returning the non-negative distance between them.

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
    int mirrorDistance(int n) {
        long long original = n;
        long long reversed = 0;
        long long temp = n;
        while (temp > 0) {
            reversed = reversed * 10 + (temp % 10);
            temp /= 10;
        }
        long long diff = original - reversed;
        return (int)(diff < 0 ? -diff : diff);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int mirrorDistance(int n) {
        long original = n;
        long reversed = 0;
        long temp = n;
        while (temp > 0) {
            reversed = reversed * 10 + (temp % 10);
            temp /= 10;
        }
        long diff = original - reversed;
        return (int) Math.abs(diff);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        original = n
        reversed_n = 0
        temp = n
        while temp > 0:
            reversed_n = reversed_n * 10 + (temp % 10)
            temp //= 10
        return abs(original - reversed_n)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def mirrorDistance(self, n: int) -> int:
        original = n
        reversed_n = 0
        temp = n
        while temp > 0:
            reversed_n = reversed_n * 10 + (temp % 10)
            temp //= 10
        return abs(original - reversed_n)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int mirrorDistance(int n) {
    long long original = n;
    long long reversed = 0;
    long long temp = n;
    while (temp > 0) {
        reversed = reversed * 10 + (temp % 10);
        temp /= 10;
    }
    long long diff = original - reversed;
    if (diff < 0) return (int)(-diff);
    return (int)diff;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int MirrorDistance(int n) {
        long original = n;
        long reversed = 0;
        long temp = n;
        while (temp > 0) {
            reversed = reversed * 10 + (temp % 10);
            temp /= 10;
        }
        long diff = original - reversed;
        return (int)Math.Abs(diff);
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
var mirrorDistance = function(n) {
    let original = n;
    let reversed = 0;
    let temp = n;
    while (temp > 0) {
        reversed = reversed * 10 + (temp % 10);
        temp = Math.floor(temp / 10);
    }
    return Math.abs(original - reversed);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function mirrorDistance(n: number): number {
    let rev = 0;
    let temp = n;
    while (temp > 0) {
        rev = rev * 10 + (temp % 10);
        temp = Math.floor(temp / 10);
    }
    return Math.abs(n - rev);
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
    function mirrorDistance($n) {
        $rev = 0;
        $temp = $n;
        while ($temp > 0) {
            $rev = $rev * 10 + ($temp % 10);
            $temp = intdiv($temp, 10);
        }
        return abs($n - $rev);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func mirrorDistance(_ n: Int) -> Int {
        var rev = 0
        var temp = n
        while temp > 0 {
            rev = rev * 10 + (temp % 10)
            temp /= 10
        }
        return abs(n - rev)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun mirrorDistance(n: Int): Int {
        var rev = 0
        var temp = n
        while (temp > 0) {
            rev = rev * 10 + (temp % 10)
            temp /= 10
        }
        return Math.abs(n - rev)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int mirrorDistance(int n) {
    int rev = 0;
    int temp = n;
    while (temp > 0) {
      rev = rev * 10 + (temp % 10);
      temp ~/= 10;
    }
    return (n - rev).abs();
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func mirrorDistance(n int) int {
    rev := 0
    temp := n
    for temp > 0 {
        rev = rev*10 + (temp % 10)
        temp /= 10
    }
    diff := n - rev
    if diff < 0 {
        return -diff
    }
    return diff
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @return {Integer}
def mirror_distance(n)
  rev_n = n.to_s.reverse.to_i
  (n - rev_n).abs
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def mirrorDistance(n: Int): Int = {
        var original = n
        var reversed = 0
        while (original > 0) {
            reversed = reversed * 10 + (original % 10)
            original /= 10
        }
        if (n > reversed) n - reversed else reversed - n
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn mirror_distance(n: i32) -> i32 {
        let mut original = n;
        let mut reversed: i32 = 0;
        while original > 0 {
            reversed = reversed * 10 + (original % 10);
            original /= 10;
        }
        (n - reversed).abs()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (mirror-distance n)
  (-> exact-integer? exact-integer?)
  (let* ([s (number->string n)]
         [rev-s (list->string (reverse (string->list s)))]
         [rev-n (string->number rev-s)])
    (abs (- n rev-n))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec mirror_distance(N :: integer()) -> integer().
mirror_distance(N) ->
  RevN = list_to_integer(lists:reverse(integer_to_list(N))),
  abs(N - RevN).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec mirror_distance(n :: integer) :: integer
  def mirror_distance(n) do
    rev_n = n
      |> Integer.to_string()
      |> String.reverse()
      |> String.to_integer()
    abs(n - rev_n)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(log n) with one-paragraph explanation.
The time complexity is determined by the number of digits in the integer n, which is floor(log10(n)) + 1. Since the algorithm iterates through each digit exactly once to reverse the number, the total number of operations is proportional to the number of digits in the input.
- **Space Complexity:** O(1) with one-paragraph explanation.
The algorithm uses a fixed amount of extra space to store the original number, the reversed number, and temporary variables for the calculation. This space does not grow with the size of the input, leading to constant space complexity.
