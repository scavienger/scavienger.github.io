---
layout: post
title: "Concatenate Non-Zero Digits and Multiply by Sum I"
date: 2026-07-07 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Math"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/
ai_solutions:
  - solutions:
      cpp: "#include <string>\n\nclass Solution {\npublic:\n    long long sumAndMultiply(int\
        \ n) {\n        std::string s = std::to_string(n);\n        long long x = 0;\n\
        \        long long sum = 0;\n        for (char c : s) {\n            if (c !=\
        \ '0') {\n                int digit = c - '0';\n                x = x * 10 +\
        \ digit;\n                sum += digit;\n            }\n        }\n        return\
        \ x * sum;\n    }\n};"
      java: "class Solution {\n    public long sumAndMultiply(int n) {\n        String\
        \ s = String.valueOf(n);\n        long x = 0;\n        long sum = 0;\n     \
        \   for (int i = 0; i < s.length(); i++) {\n            char c = s.charAt(i);\n\
        \            if (c != '0') {\n                int digit = c - '0';\n       \
        \         x = x * 10 + digit;\n                sum += digit;\n            }\n\
        \        }\n        return x * sum;\n    }\n}"
      python: "class Solution(object):\n    def sumAndMultiply(self, n):\n        \"\
        \"\"\n        :type n: int\n        :rtype: int\n        \"\"\"\n        s_n\
        \ = str(n)\n        x = 0\n        digit_sum = 0\n        for char in s_n:\n\
        \            if char != '0':\n                digit = int(char)\n          \
        \      x = x * 10 + digit\n                digit_sum += digit\n        return\
        \ x * digit_sum"
      python3: "class Solution:\n    def sumAndMultiply(self, n: int) -> int:\n    \
        \    s_n = str(n)\n        x = 0\n        digit_sum = 0\n        for char in\
        \ s_n:\n            if char != '0':\n                digit = int(char)\n   \
        \             x = x * 10 + digit\n                digit_sum += digit\n     \
        \   return x * digit_sum"
      c: "long long sumAndMultiply(int n) {\n    if (n == 0) return 0;\n    int digits[12];\n\
        \    int count = 0;\n    int temp = n;\n    while (temp > 0) {\n        digits[count++]\
        \ = temp % 10;\n        temp /= 10;\n    }\n    long long x = 0;\n    long long\
        \ sum = 0;\n    for (int i = count - 1; i >= 0; i--) {\n        if (digits[i]\
        \ != 0) {\n            x = x * 10 + digits[i];\n            sum += (long long)digits[i];\n\
        \        }\n    }\n    return x * sum;\n}"
      csharp: "public class Solution {\n    public long SumAndMultiply(int n) {\n  \
        \      string s = n.ToString();\n        long x = 0;\n        long sum = 0;\n\
        \        foreach (char c in s) {\n            if (c != '0') {\n            \
        \    int digit = c - '0';\n                x = x * 10 + digit;\n           \
        \     sum += digit;\n            }\n        }\n        return x * sum;\n   \
        \ }\n}"
      javascript: "/**\n * @param {number} n\n * @return {number}\n */\nvar sumAndMultiply\
        \ = function(n) {\n    let s = n.toString();\n    let x = 0;\n    let sum =\
        \ 0;\n    for (let i = 0; i < s.length; i++) {\n        if (s[i] !== '0') {\n\
        \            let digit = s[i] - '0';\n            x = x * 10 + digit;\n    \
        \        sum += digit;\n        }\n    }\n    return x * sum;\n};"
      typescript: "function sumAndMultiply(n: number): number {\n    const s = n.toString();\n\
        \    let xStr = \"\";\n    let sum = 0;\n    for (let i = 0; i < s.length; i++)\
        \ {\n        if (s[i] !== '0') {\n            xStr += s[i];\n            sum\
        \ += parseInt(s[i], 10);\n        }\n    }\n    if (xStr === \"\") return 0;\n\
        \    const x = parseInt(xStr, 10);\n    return x * sum;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @return Integer\n\
        \     */\n    function sumAndMultiply($n) {\n        $s = (string)$n;\n    \
        \    $xStr = \"\";\n        $sum = 0;\n        for ($i = 0; $i < strlen($s);\
        \ $i++) {\n            if ($s[$i] !== '0') {\n                $xStr .= $s[$i];\n\
        \                $sum += (int)$s[$i];\n            }\n        }\n        if\
        \ ($xStr === \"\") return 0;\n        $x = (int)$xStr;\n        return $x *\
        \ $sum;\n    }\n}"
      swift: "class Solution {\n    func sumAndMultiply(_ n: Int) -> Int {\n       \
        \ let s = String(n)\n        var xStr = \"\"\n        var sum = 0\n        for\
        \ char in s {\n            if char != \"0\" {\n                xStr.append(char)\n\
        \                if let digit = Int(String(char)) {\n                    sum\
        \ += digit\n                }\n            }\n        }\n        if xStr.isEmpty\
        \ { return 0 }\n        if let x = Int(xStr) {\n            return x * sum\n\
        \        }\n        return 0\n    }\n}"
      kotlin: "class Solution {\n    fun sumAndMultiply(n: Int): Long {\n        val\
        \ s = n.toString()\n        var xStr = \"\"\n        var sum: Long = 0\n   \
        \     for (char in s) {\n            if (char != '0') {\n                xStr\
        \ += char\n                sum += (char - '0').toLong()\n            }\n   \
        \     }\n        if (xStr == \"\") return 0L\n        val x = xStr.toLong()\n\
        \        return x * sum\n    }\n}"
      dart: "class Solution {\n  int sumAndMultiply(int n) {\n    String s = n.toString();\n\
        \    String xStr = \"\";\n    int sum = 0;\n    for (int i = 0; i < s.length;\
        \ i++) {\n      if (s[i] != '0') {\n        xStr += s[i];\n        sum += int.parse(s[i]);\n\
        \      }\n    }\n    if (xStr == \"\") return 0;\n    int x = int.parse(xStr);\n\
        \    return x * sum;\n  }\n}"
      go: "func sumAndMultiply(n int) int64 {\n    if n == 0 {\n        return 0\n \
        \   }\n    var digits []int\n    temp := n\n    for temp > 0 {\n        d :=\
        \ temp % 10\n        if d != 0 {\n            digits = append(digits, d)\n \
        \       }\n        temp /= 10\n    }\n    if len(digits) == 0 {\n        return\
        \ 0\n    }\n    var x int64 = 0\n    var sum int64 = 0\n    for i := len(digits)\
        \ - 1; i >= 0; i-- {\n        x = x*10 + int64(digits[i])\n        sum += int64(digits[i])\n\
        \    }\n    return x * sum\n}"
      ruby: "def sum_and_multiply(n)\n  digits = n.to_s.chars.reject { |c| c == '0'\
        \ }\n  if digits.empty?\n    0\n  else\n    x = digits.join.to_i\n    sum =\
        \ digits.map(&:to_i).sum\n    x * sum\n  end\nend"
      scala: "object Solution {\n  def sumAndMultiply(n: Int): Long = {\n    val nonZeroDigits\
        \ = n.toString.filter(_ != '0')\n    if (nonZeroDigits.isEmpty) {\n      0L\n\
        \    } else {\n      val x = nonZeroDigits.toLong\n      val sum = nonZeroDigits.map(_.asDigit).sum.toLong\n\
        \      x * sum\n    }\n  }\n}"
      rust: "impl Solution {\n  pub fn sum_and_multiply(n: i32) -> i64 {\n    let digits:\
        \ String = n.to_string().chars().filter(|&c| c != '0').collect();\n    if digits.is_empty()\
        \ {\n      0\n    } else {\n      let x: i64 = digits.parse().unwrap();\n  \
        \    let sum: i64 = digits.chars().map(|c| (c as i64) - ('0' as i64)).sum();\n\
        \      x * sum\n    }\n  }\n}"
      racket: "(define/contract (sum-and-multiply n)\n  (-> exact-integer? exact-integer?)\n\
        \  (let ([non-zeros (filter (lambda (c) (not (char=? c #\\0))) (string->list\
        \ (number->string n)))])\n    (if (null? non-zeros)\n        0\n        (let*\
        \ ([x (string->number (list->string non-zeros))]\n               [sum (foldl\
        \ (lambda (c acc) (+ acc (- (char->integer c) (char->integer #\\0)))) 0 non-zeros)])\n\
        \          (* x sum))))\n)"
      erlang: "-spec sum_and_multiply(N :: integer()) -> integer().\nsum_and_multiply(N)\
        \ ->\n  NonZeros = lists:filter(fun(C) -> C /= $0 end, integer_to_list(N)),\n\
        \  case NonZeros of\n    [] -> 0;\n    _ ->\n      X = list_to_integer(NonZeros),\n\
        \      Sum = lists:foldl(fun(C, Acc) -> Acc + (C - $0) end, 0, NonZeros),\n\
        \      X * Sum\n  end."
      elixir: "defmodule Solution do\n  @spec sum_and_multiply(n :: integer) :: integer\n\
        \  def sum_and_multiply(n) do\n    digits = Integer.to_charlist(n) |> Enum.filter(fn\
        \ c -> c != ?0 end)\n    if digits == [] do\n      0\n    else\n      x = List.to_integer(digits)\n\
        \      sum = Enum.reduce(digits, 0, fn c, acc -> acc + (c - ?0) end)\n     \
        \ x * sum\n    end\n  end\nend"
    approach: 'The algorithm extracts all non-zero digits from the given integer n while
      maintaining their original relative order. We process each digit of n, and for
      every digit that is not zero, we construct a new integer x by appending that digit
      to the right of the current value. Simultaneously, we maintain a running total,
      sum, which accumulates the values of all these non-zero digits.


      Once all digits of n have been processed, the new integer x representing the concatenated
      non-zero digits and the calculated sum are available. The final result is the
      product of x and sum. Because the product can reach approximately 81 billion (for
      n = 999,999,999), we utilize 64-bit integer types in languages like C++, Java,
      and C# to prevent overflow and ensure the result fits within the appropriate numeric
      range.'
    time_complexity: O(log n). The number of digits in the integer n is given by floor(log10(n))
      + 1. Since the algorithm iterates through each digit of n exactly once to identify
      non-zero digits and calculate the sum, the time complexity is logarithmic with
      respect to the input value n.
    space_complexity: O(log n). The algorithm typically converts the integer n into
      a string or stores its digits in an array to facilitate iteration. The space required
      to store these digits is proportional to the number of digits in n, which is logarithmic
      with respect to n.
    elapsed_time: 191.7646734714508
    model: gemini-3-flash-preview
    generated_at: '2026-07-07 02:27:33 '
---

## Problem #3754: Concatenate Non-Zero Digits and Multiply by Sum I

**Difficulty:** Easy

**Topics:** Math

## Problem Description

<p>You are given an integer <code>n</code>.</p>

<p>Form a new integer <code>x</code> by concatenating all the <strong>non-zero digits</strong> of <code>n</code> in their original order. If there are no <strong>non-zero</strong> digits, <code>x = 0</code>.</p>

<p>Let <code>sum</code> be the <strong>sum of digits</strong> in <code>x</code>.</p>

<p>Return an integer representing the value of <code>x * sum</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 10203004</span></p>

<p><strong>Output:</strong> <span class="example-io">12340</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The non-zero digits are 1, 2, 3, and 4. Thus, <code>x = 1234</code>.</li>
	<li>The sum of digits is <code>sum = 1 + 2 + 3 + 4 = 10</code>.</li>
	<li>Therefore, the answer is <code>x * sum = 1234 * 10 = 12340</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 1000</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The non-zero digit is 1, so <code>x = 1</code> and <code>sum = 1</code>.</li>
	<li>Therefore, the answer is <code>x * sum = 1 * 1 = 1</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Simulate as described

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm extracts all non-zero digits from the given integer n while maintaining their original relative order. We process each digit of n, and for every digit that is not zero, we construct a new integer x by appending that digit to the right of the current value. Simultaneously, we maintain a running total, sum, which accumulates the values of all these non-zero digits.

Once all digits of n have been processed, the new integer x representing the concatenated non-zero digits and the calculated sum are available. The final result is the product of x and sum. Because the product can reach approximately 81 billion (for n = 999,999,999), we utilize 64-bit integer types in languages like C++, Java, and C# to prevent overflow and ensure the result fits within the appropriate numeric range.

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
#include <string>

class Solution {
public:
    long long sumAndMultiply(int n) {
        std::string s = std::to_string(n);
        long long x = 0;
        long long sum = 0;
        for (char c : s) {
            if (c != '0') {
                int digit = c - '0';
                x = x * 10 + digit;
                sum += digit;
            }
        }
        return x * sum;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long sumAndMultiply(int n) {
        String s = String.valueOf(n);
        long x = 0;
        long sum = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c != '0') {
                int digit = c - '0';
                x = x * 10 + digit;
                sum += digit;
            }
        }
        return x * sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        s_n = str(n)
        x = 0
        digit_sum = 0
        for char in s_n:
            if char != '0':
                digit = int(char)
                x = x * 10 + digit
                digit_sum += digit
        return x * digit_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s_n = str(n)
        x = 0
        digit_sum = 0
        for char in s_n:
            if char != '0':
                digit = int(char)
                x = x * 10 + digit
                digit_sum += digit
        return x * digit_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
long long sumAndMultiply(int n) {
    if (n == 0) return 0;
    int digits[12];
    int count = 0;
    int temp = n;
    while (temp > 0) {
        digits[count++] = temp % 10;
        temp /= 10;
    }
    long long x = 0;
    long long sum = 0;
    for (int i = count - 1; i >= 0; i--) {
        if (digits[i] != 0) {
            x = x * 10 + digits[i];
            sum += (long long)digits[i];
        }
    }
    return x * sum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long SumAndMultiply(int n) {
        string s = n.ToString();
        long x = 0;
        long sum = 0;
        foreach (char c in s) {
            if (c != '0') {
                int digit = c - '0';
                x = x * 10 + digit;
                sum += digit;
            }
        }
        return x * sum;
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
var sumAndMultiply = function(n) {
    let s = n.toString();
    let x = 0;
    let sum = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] !== '0') {
            let digit = s[i] - '0';
            x = x * 10 + digit;
            sum += digit;
        }
    }
    return x * sum;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function sumAndMultiply(n: number): number {
    const s = n.toString();
    let xStr = "";
    let sum = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] !== '0') {
            xStr += s[i];
            sum += parseInt(s[i], 10);
        }
    }
    if (xStr === "") return 0;
    const x = parseInt(xStr, 10);
    return x * sum;
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
    function sumAndMultiply($n) {
        $s = (string)$n;
        $xStr = "";
        $sum = 0;
        for ($i = 0; $i < strlen($s); $i++) {
            if ($s[$i] !== '0') {
                $xStr .= $s[$i];
                $sum += (int)$s[$i];
            }
        }
        if ($xStr === "") return 0;
        $x = (int)$xStr;
        return $x * $sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func sumAndMultiply(_ n: Int) -> Int {
        let s = String(n)
        var xStr = ""
        var sum = 0
        for char in s {
            if char != "0" {
                xStr.append(char)
                if let digit = Int(String(char)) {
                    sum += digit
                }
            }
        }
        if xStr.isEmpty { return 0 }
        if let x = Int(xStr) {
            return x * sum
        }
        return 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun sumAndMultiply(n: Int): Long {
        val s = n.toString()
        var xStr = ""
        var sum: Long = 0
        for (char in s) {
            if (char != '0') {
                xStr += char
                sum += (char - '0').toLong()
            }
        }
        if (xStr == "") return 0L
        val x = xStr.toLong()
        return x * sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int sumAndMultiply(int n) {
    String s = n.toString();
    String xStr = "";
    int sum = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] != '0') {
        xStr += s[i];
        sum += int.parse(s[i]);
      }
    }
    if (xStr == "") return 0;
    int x = int.parse(xStr);
    return x * sum;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func sumAndMultiply(n int) int64 {
    if n == 0 {
        return 0
    }
    var digits []int
    temp := n
    for temp > 0 {
        d := temp % 10
        if d != 0 {
            digits = append(digits, d)
        }
        temp /= 10
    }
    if len(digits) == 0 {
        return 0
    }
    var x int64 = 0
    var sum int64 = 0
    for i := len(digits) - 1; i >= 0; i-- {
        x = x*10 + int64(digits[i])
        sum += int64(digits[i])
    }
    return x * sum
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def sum_and_multiply(n)
  digits = n.to_s.chars.reject { |c| c == '0' }
  if digits.empty?
    0
  else
    x = digits.join.to_i
    sum = digits.map(&:to_i).sum
    x * sum
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def sumAndMultiply(n: Int): Long = {
    val nonZeroDigits = n.toString.filter(_ != '0')
    if (nonZeroDigits.isEmpty) {
      0L
    } else {
      val x = nonZeroDigits.toLong
      val sum = nonZeroDigits.map(_.asDigit).sum.toLong
      x * sum
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
  pub fn sum_and_multiply(n: i32) -> i64 {
    let digits: String = n.to_string().chars().filter(|&c| c != '0').collect();
    if digits.is_empty() {
      0
    } else {
      let x: i64 = digits.parse().unwrap();
      let sum: i64 = digits.chars().map(|c| (c as i64) - ('0' as i64)).sum();
      x * sum
    }
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (sum-and-multiply n)
  (-> exact-integer? exact-integer?)
  (let ([non-zeros (filter (lambda (c) (not (char=? c #\0))) (string->list (number->string n)))])
    (if (null? non-zeros)
        0
        (let* ([x (string->number (list->string non-zeros))]
               [sum (foldl (lambda (c acc) (+ acc (- (char->integer c) (char->integer #\0)))) 0 non-zeros)])
          (* x sum))))
)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec sum_and_multiply(N :: integer()) -> integer().
sum_and_multiply(N) ->
  NonZeros = lists:filter(fun(C) -> C /= $0 end, integer_to_list(N)),
  case NonZeros of
    [] -> 0;
    _ ->
      X = list_to_integer(NonZeros),
      Sum = lists:foldl(fun(C, Acc) -> Acc + (C - $0) end, 0, NonZeros),
      X * Sum
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec sum_and_multiply(n :: integer) :: integer
  def sum_and_multiply(n) do
    digits = Integer.to_charlist(n) |> Enum.filter(fn c -> c != ?0 end)
    if digits == [] do
      0
    else
      x = List.to_integer(digits)
      sum = Enum.reduce(digits, 0, fn c, acc -> acc + (c - ?0) end)
      x * sum
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(log n). The number of digits in the integer n is given by floor(log10(n)) + 1. Since the algorithm iterates through each digit of n exactly once to identify non-zero digits and calculate the sum, the time complexity is logarithmic with respect to the input value n.
- **Space Complexity:** O(log n). The algorithm typically converts the integer n into a string or stores its digits in an array to facilitate iteration. The space required to store these digits is proportional to the number of digits in n, which is logarithmic with respect to n.
