---
layout: post
title: "Maximize Sum of Squares of Digits"
date: 2026-10-14 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Math", "Greedy"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximize-sum-of-squares-of-digits/
ai_solutions:
  - solutions:
      cpp: '// Generation failed for C++

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      java: '// Generation failed for Java

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      python: '// Generation failed for Python

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      python3: '// Generation failed for Python3

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      c: '// Generation failed for C

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      csharp: "public class Solution {\n    public string MaxSumOfSquares(int num, int\
        \ sum) {\n        if (sum > 9 * num) {\n            return \"\";\n        }\n\
        \n        int k = sum / 9;\n        int r = sum % 9;\n\n        if (k == num)\
        \ {\n            return new string('9', num);\n        }\n\n        string result\
        \ = new string('9', k) + r.ToString() + new string('0', num - k - 1);\n    \
        \    return result;\n    }\n}"
      javascript: "/**\n * @param {number} num\n * @param {number} sum\n * @return {string}\n\
        \ */\nvar maxSumOfSquares = function(num, sum) {\n    if (sum > 9 * num) {\n\
        \        return \"\";\n    }\n\n    const k = Math.floor(sum / 9);\n    const\
        \ r = sum % 9;\n\n    if (k === num) {\n        return '9'.repeat(num);\n  \
        \  }\n\n    return '9'.repeat(k) + r.toString() + '0'.repeat(num - k - 1);\n\
        };"
      typescript: "function maxSumOfSquares(num: number, sum: number): string {\n  \
        \  if (sum > 9 * num) {\n        return \"\";\n    }\n\n    const k: number\
        \ = Math.floor(sum / 9);\n    const r: number = sum % 9;\n\n    if (k === num)\
        \ {\n        return '9'.repeat(num);\n    }\n\n    return '9'.repeat(k) + r.toString()\
        \ + '0'.repeat(num - k - 1);\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $num\n     * @param Integer\
        \ $sum\n     * @return String\n     */\n    function maxSumOfSquares($num, $sum)\
        \ {\n        if ($sum > 9 * $num) {\n            return \"\";\n        }\n\n\
        \        $k = (int)($sum / 9);\n        $r = $sum % 9;\n\n        if ($k ===\
        \ $num) {\n            return str_repeat('9', $num);\n        }\n\n        return\
        \ str_repeat('9', $k) . (string)$r . str_repeat('0', $num - $k - 1);\n    }\n\
        }"
      swift: "class Solution {\n    func maxSumOfSquares(_ num: Int, _ sum: Int) ->\
        \ String {\n        if sum > 9 * num {\n            return \"\"\n        }\n\
        \n        let k = sum / 9\n        let r = sum % 9\n\n        if k == num {\n\
        \            return String(repeating: \"9\", count: num)\n        }\n\n    \
        \    let result = String(repeating: \"9\", count: k) + String(r) + String(repeating:\
        \ \"0\", count: num - k - 1)\n        return result\n    }\n}"
      kotlin: "class Solution {\n    fun maxSumOfSquares(num: Int, sum: Int): String\
        \ {\n        if (sum > 9 * num) return \"\"\n\n        val numNines = sum /\
        \ 9\n        val remainder = sum % 9\n        val sb = StringBuilder()\n\n \
        \       sb.append(\"9\".repeat(numNines))\n\n        if (remainder > 0) {\n\
        \            sb.append(remainder.toString())\n        }\n\n        while (sb.length\
        \ < num) {\n            sb.append('0')\n        }\n\n        return sb.toString()\n\
        \    }\n}"
      dart: "class Solution {\n  String maxSumOfSquares(int num, int sum) {\n    if\
        \ (sum > 9 * num) return \"\";\n\n    int numNines = sum ~/ 9;\n    int remainder\
        \ = sum % 9;\n    StringBuffer sb = StringBuffer();\n\n    sb.write('9' * numNines);\n\
        \n    if (remainder > 0) {\n      sb.write(remainder.toString());\n    }\n\n\
        \    while (sb.length < num) {\n      sb.write('0');\n    }\n\n    return sb.toString();\n\
        \  }\n}"
      go: "import \"strings\"\n\nfunc maxSumOfSquares(num int, sum int) string {\n \
        \   if sum > 9*num {\n        return \"\"\n    }\n\n    numNines := sum / 9\n\
        \    remainder := sum % 9\n\n    var builder strings.Builder\n    builder.Grow(num)\n\
        \n    for i := 0; i < numNines; i++ {\n        builder.WriteByte('9')\n    }\n\
        \n    if remainder > 0 {\n        builder.WriteByte(byte('0' + remainder))\n\
        \    }\n\n    for builder.Len() < num {\n        builder.WriteByte('0')\n  \
        \  }\n\n    return builder.String()\n}"
      ruby: "# @param {Integer} num\n# @param {Integer} sum\n# @return {String}\ndef\
        \ max_sum_of_squares(num, sum)\n    if sum > 9 * num\n        return \"\"\n\
        \    end\n\n    num_nines = sum / 9\n    remainder = sum % 9\n    res = \"9\"\
        \ * num_nines\n\n    if remainder > 0\n        res += remainder.to_s\n    end\n\
        \n    res += \"0\" * (num - res.length)\n    res\nend"
      scala: "object Solution {\n    def maxSumOfSquares(num: Int, sum: Int): String\
        \ = {\n        if (sum > 9 * num) {\n            \"\"\n        } else {\n  \
        \          val numNines = sum / 9\n            val remainder = sum % 9\n   \
        \         val sb = new StringBuilder()\n\n            for (_ <- 0 until numNines)\
        \ sb.append('9')\n\n            if (remainder > 0) {\n                sb.append(remainder)\n\
        \            }\n\n            while (sb.length < num) {\n                sb.append('0')\n\
        \            }\n\n            sb.toString()\n        }\n    }\n}"
      rust: "impl Solution {\n    pub fn max_sum_of_squares(num: i32, sum: i32) -> String\
        \ {\n        let n = num as usize;\n        let s = sum as usize;\n        if\
        \ s < 1 || s > n * 9 {\n            return \"\".to_string();\n        }\n\n\
        \        let full_nines = s / 9;\n        let remainder = s % 9;\n        let\
        \ has_remainder = if remainder > 0 { 1 } else { 0 };\n        let zeros = n\
        \ - full_nines - has_remainder;\n\n        let mut res = String::with_capacity(n);\n\
        \        for _ in 0..full_nines {\n            res.push('9');\n        }\n \
        \       if remainder > 0 {\n            res.push((b'0' + remainder as u8) as\
        \ char);\n        }\n        for _ in 0..zeros {\n            res.push('0');\n\
        \        }\n        res\n    }\n}"
      racket: "(define/contract (max-sum-of-squares num sum)\n  (-> exact-integer? exact-integer?\
        \ string?)\n  (if (or (< sum 1) (> sum (* num 9)))\n      \"\"\n      (let*\
        \ ([full-nines (quotient sum 9)]\n             [rem-digit (remainder sum 9)]\n\
        \             [has-rem (if (> rem-digit 0) 1 0)]\n             [num-zeros (-\
        \ num full-nines has-rem)])\n        (string-append\n         (make-string full-nines\
        \ #\\9)\n         (if (> has-rem 0)\n             (string (integer->char (+\
        \ rem-digit (char->integer #\\0))))\n             \"\")\n         (make-string\
        \ num-zeros #\\0)))))"
      erlang: "-spec max_sum_of_squares(Num :: integer(), Sum :: integer()) -> unicode:unicode_binary().\n\
        max_sum_of_squares(Num, Sum) ->\n    if\n        Sum < 1; Sum > Num * 9 -> <<>>;\n\
        \        true ->\n            FullNines = Sum div 9,\n            Remainder\
        \ = Sum rem 9,\n            HasRemainder = if Remainder > 0 -> 1; true -> 0\
        \ end,\n            Zeros = Num - FullNines - HasRemainder,\n            Nines\
        \ = lists:duplicate(FullNines, $9),\n            RemPart = if Remainder > 0\
        \ -> [Remainder + $0]; true -> [] end,\n            ZerosPart = lists:duplicate(Zeros,\
        \ $0),\n            list_to_binary(Nines ++ RemPart ++ ZerosPart)\n    end."
      elixir: "defmodule Solution do\n  @spec max_sum_of_squares(num :: integer, sum\
        \ :: integer) :: String.t\n  def max_sum_of_squares(num, sum) do\n    if sum\
        \ < 1 or sum > num * 9 do\n      \"\"\n    else\n      full_nines = div(sum,\
        \ 9)\n      remainder = rem(sum, 9)\n      has_remainder = if remainder > 0,\
        \ do: 1, else: 0\n      num_zeros = num - full_nines - has_remainder\n\n   \
        \   String.duplicate(\"9\", full_nines) <>\n      (if remainder > 0, do: Integer.to_string(remainder),\
        \ else: \"\") <>\n      String.duplicate(\"0\", num_zeros)\n    end\n  end\n\
        end"
    approach: 'To maximize the sum of squares of digits for a fixed digit sum, we leverage
      the mathematical property of convexity. For any two digits $x$ and $y$ with $0
      \le x \le y \le 9$, if we increase the larger digit and decrease the smaller digit
      by the same amount, the sum of their squares increases (e.g., $5^2+5^2=50 < 4^2+6^2=52$).
      Consequently, the maximum sum of squares is achieved when digits are as extreme
      as possible, meaning as many digits as possible are either 9 or 0, with at most
      one digit falling in the range [1, 8].


      To achieve the maximum possible integer value among those with the maximum score,
      we must place the largest digits in the most significant positions. This naturally
      leads to a greedy construction: fill the leftmost positions with as many 9s as
      possible until the remaining sum is less than 9, place that remaining value in
      the next position, and fill all remaining positions with 0s. This approach ensures
      both the highest possible sum of squares and the lexicographically largest integer
      while satisfying the constraint that the first digit cannot be 0 (guaranteed since
      $sum \ge 1$).'
    time_complexity: O(num) where $num$ is the required number of digits. The algorithm
      performs a few arithmetic operations and then constructs a string of length $num$
      using efficient repetition methods.
    space_complexity: O(num) to store the result string. Apart from the output string,
      the algorithm uses only a constant amount of auxiliary space.
    elapsed_time: 229.4033386707306
    model: gemini-3-flash-preview
    generated_at: '2026-10-14 03:12:43 '
---

## Problem #3723: Maximize Sum of Squares of Digits

**Difficulty:** Medium

**Topics:** Math, Greedy

## Problem Description

<p>You are given two <strong>positive</strong> integers <code>num</code> and <code>sum</code>.</p>

<p>A positive integer <code>n</code> is <strong>good</strong> if it satisfies both of the following:</p>

<ul>
	<li>The number of digits in <code>n</code> is <strong>exactly</strong> <code>num</code>.</li>
	<li>The sum of digits in <code>n</code> is <strong>exactly</strong> <code>sum</code>.</li>
</ul>

<p>The <strong>score</strong> of a <strong>good</strong> integer <code>n</code> is the sum of the squares of digits in <code>n</code>.</p>

<p>Return a <strong>string</strong> denoting the <strong>good</strong> integer <code>n</code> that achieves the <strong>maximum</strong> <strong>score</strong>. If there are multiple possible integers, return the <strong>maximum </strong>​​​​​​​one. If no such integer exists, return an empty string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num = 2, sum = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;30&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>There are 3 good integers: 12, 21, and 30.</p>

<ul>
	<li>The score of 12 is <code>1<sup>2</sup> + 2<sup>2</sup> = 5</code>.</li>
	<li>The score of 21 is <code>2<sup>2</sup> + 1<sup>2</sup> = 5</code>.</li>
	<li>The score of 30 is <code>3<sup>2</sup> + 0<sup>2</sup> = 9</code>.</li>
</ul>

<p>The maximum score is 9, which is achieved by the good integer 30. Therefore, the answer is <code>&quot;30&quot;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num = 2, sum = 17</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;98&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>There are 2 good integers: 89 and 98.</p>

<ul>
	<li>The score of 89 is <code>8<sup>2</sup> + 9<sup>2</sup> = 145</code>.</li>
	<li>The score of 98 is <code>9<sup>2</sup> + 8<sup>2</sup> = 145</code>.</li>
</ul>

<p>The maximum score is 145. The maximum good integer that achieves this score is 98. Therefore, the answer is <code>&quot;98&quot;</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num = 1, sum = 10</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no integers that have exactly 1 digit and whose digits sum to 10. Therefore, the answer is <code>&quot;&quot;</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= sum &lt;= 2 * 10<sup>6</sup></code></li>
</ul>


## Hints

1. Use a greedy approach.

2. Fill the leftmost digits with 9s first (as much as possible).

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To maximize the sum of squares of digits for a fixed digit sum, we leverage the mathematical property of convexity. For any two digits $x$ and $y$ with $0 \le x \le y \le 9$, if we increase the larger digit and decrease the smaller digit by the same amount, the sum of their squares increases (e.g., $5^2+5^2=50 < 4^2+6^2=52$). Consequently, the maximum sum of squares is achieved when digits are as extreme as possible, meaning as many digits as possible are either 9 or 0, with at most one digit falling in the range [1, 8].

To achieve the maximum possible integer value among those with the maximum score, we must place the largest digits in the most significant positions. This naturally leads to a greedy construction: fill the leftmost positions with as many 9s as possible until the remaining sum is less than 9, place that remaining value in the next position, and fill all remaining positions with 0s. This approach ensures both the highest possible sum of squares and the lexicographically largest integer while satisfying the constraint that the first digit cannot be 0 (guaranteed since $sum \ge 1$).

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
// Generation failed for C++
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public string MaxSumOfSquares(int num, int sum) {
        if (sum > 9 * num) {
            return "";
        }

        int k = sum / 9;
        int r = sum % 9;

        if (k == num) {
            return new string('9', num);
        }

        string result = new string('9', k) + r.ToString() + new string('0', num - k - 1);
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
 * @param {number} num
 * @param {number} sum
 * @return {string}
 */
var maxSumOfSquares = function(num, sum) {
    if (sum > 9 * num) {
        return "";
    }

    const k = Math.floor(sum / 9);
    const r = sum % 9;

    if (k === num) {
        return '9'.repeat(num);
    }

    return '9'.repeat(k) + r.toString() + '0'.repeat(num - k - 1);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxSumOfSquares(num: number, sum: number): string {
    if (sum > 9 * num) {
        return "";
    }

    const k: number = Math.floor(sum / 9);
    const r: number = sum % 9;

    if (k === num) {
        return '9'.repeat(num);
    }

    return '9'.repeat(k) + r.toString() + '0'.repeat(num - k - 1);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $num
     * @param Integer $sum
     * @return String
     */
    function maxSumOfSquares($num, $sum) {
        if ($sum > 9 * $num) {
            return "";
        }

        $k = (int)($sum / 9);
        $r = $sum % 9;

        if ($k === $num) {
            return str_repeat('9', $num);
        }

        return str_repeat('9', $k) . (string)$r . str_repeat('0', $num - $k - 1);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxSumOfSquares(_ num: Int, _ sum: Int) -> String {
        if sum > 9 * num {
            return ""
        }

        let k = sum / 9
        let r = sum % 9

        if k == num {
            return String(repeating: "9", count: num)
        }

        let result = String(repeating: "9", count: k) + String(r) + String(repeating: "0", count: num - k - 1)
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
    fun maxSumOfSquares(num: Int, sum: Int): String {
        if (sum > 9 * num) return ""

        val numNines = sum / 9
        val remainder = sum % 9
        val sb = StringBuilder()

        sb.append("9".repeat(numNines))

        if (remainder > 0) {
            sb.append(remainder.toString())
        }

        while (sb.length < num) {
            sb.append('0')
        }

        return sb.toString()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String maxSumOfSquares(int num, int sum) {
    if (sum > 9 * num) return "";

    int numNines = sum ~/ 9;
    int remainder = sum % 9;
    StringBuffer sb = StringBuffer();

    sb.write('9' * numNines);

    if (remainder > 0) {
      sb.write(remainder.toString());
    }

    while (sb.length < num) {
      sb.write('0');
    }

    return sb.toString();
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "strings"

func maxSumOfSquares(num int, sum int) string {
    if sum > 9*num {
        return ""
    }

    numNines := sum / 9
    remainder := sum % 9

    var builder strings.Builder
    builder.Grow(num)

    for i := 0; i < numNines; i++ {
        builder.WriteByte('9')
    }

    if remainder > 0 {
        builder.WriteByte(byte('0' + remainder))
    }

    for builder.Len() < num {
        builder.WriteByte('0')
    }

    return builder.String()
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} num
# @param {Integer} sum
# @return {String}
def max_sum_of_squares(num, sum)
    if sum > 9 * num
        return ""
    end

    num_nines = sum / 9
    remainder = sum % 9
    res = "9" * num_nines

    if remainder > 0
        res += remainder.to_s
    end

    res += "0" * (num - res.length)
    res
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxSumOfSquares(num: Int, sum: Int): String = {
        if (sum > 9 * num) {
            ""
        } else {
            val numNines = sum / 9
            val remainder = sum % 9
            val sb = new StringBuilder()

            for (_ <- 0 until numNines) sb.append('9')

            if (remainder > 0) {
                sb.append(remainder)
            }

            while (sb.length < num) {
                sb.append('0')
            }

            sb.toString()
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_sum_of_squares(num: i32, sum: i32) -> String {
        let n = num as usize;
        let s = sum as usize;
        if s < 1 || s > n * 9 {
            return "".to_string();
        }

        let full_nines = s / 9;
        let remainder = s % 9;
        let has_remainder = if remainder > 0 { 1 } else { 0 };
        let zeros = n - full_nines - has_remainder;

        let mut res = String::with_capacity(n);
        for _ in 0..full_nines {
            res.push('9');
        }
        if remainder > 0 {
            res.push((b'0' + remainder as u8) as char);
        }
        for _ in 0..zeros {
            res.push('0');
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-sum-of-squares num sum)
  (-> exact-integer? exact-integer? string?)
  (if (or (< sum 1) (> sum (* num 9)))
      ""
      (let* ([full-nines (quotient sum 9)]
             [rem-digit (remainder sum 9)]
             [has-rem (if (> rem-digit 0) 1 0)]
             [num-zeros (- num full-nines has-rem)])
        (string-append
         (make-string full-nines #\9)
         (if (> has-rem 0)
             (string (integer->char (+ rem-digit (char->integer #\0))))
             "")
         (make-string num-zeros #\0)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_sum_of_squares(Num :: integer(), Sum :: integer()) -> unicode:unicode_binary().
max_sum_of_squares(Num, Sum) ->
    if
        Sum < 1; Sum > Num * 9 -> <<>>;
        true ->
            FullNines = Sum div 9,
            Remainder = Sum rem 9,
            HasRemainder = if Remainder > 0 -> 1; true -> 0 end,
            Zeros = Num - FullNines - HasRemainder,
            Nines = lists:duplicate(FullNines, $9),
            RemPart = if Remainder > 0 -> [Remainder + $0]; true -> [] end,
            ZerosPart = lists:duplicate(Zeros, $0),
            list_to_binary(Nines ++ RemPart ++ ZerosPart)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_sum_of_squares(num :: integer, sum :: integer) :: String.t
  def max_sum_of_squares(num, sum) do
    if sum < 1 or sum > num * 9 do
      ""
    else
      full_nines = div(sum, 9)
      remainder = rem(sum, 9)
      has_remainder = if remainder > 0, do: 1, else: 0
      num_zeros = num - full_nines - has_remainder

      String.duplicate("9", full_nines) <>
      (if remainder > 0, do: Integer.to_string(remainder), else: "") <>
      String.duplicate("0", num_zeros)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(num) where $num$ is the required number of digits. The algorithm performs a few arithmetic operations and then constructs a string of length $num$ using efficient repetition methods.
- **Space Complexity:** O(num) to store the result string. Apart from the output string, the algorithm uses only a constant amount of auxiliary space.
