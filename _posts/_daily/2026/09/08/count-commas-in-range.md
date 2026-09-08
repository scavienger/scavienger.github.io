---
layout: post
title: "Count Commas in Range"
date: 2026-09-08 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Math"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/count-commas-in-range/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int countCommas(int n) {\n        long long\
        \ res = 0;\n        for (long long p = 1000; p <= n; p *= 1000) {\n        \
        \    res += (n - p + 1);\n        }\n        return (int)res;\n    }\n};"
      java: "class Solution {\n    public int countCommas(int n) {\n        long res\
        \ = 0;\n        for (long p = 1000; p <= n; p *= 1000) {\n            res +=\
        \ (n - p + 1);\n        }\n        return (int) res;\n    }\n}"
      python: "class Solution(object):\n    def countCommas(self, n):\n        \"\"\"\
        \n        :type n: int\n        :rtype: int\n        \"\"\"\n        res = 0\n\
        \        p = 1000\n        while p <= n:\n            res += (n - p + 1)\n \
        \           p *= 1000\n        return res"
      python3: "class Solution:\n    def countCommas(self, n: int) -> int:\n       \
        \ res = 0\n        p = 1000\n        while p <= n:\n            res += (n -\
        \ p + 1)\n            p *= 1000\n        return res"
      c: "int countCommas(int n) {\n    long long res = 0;\n    for (long long p = 1000;\
        \ p <= (long long)n; p *= 1000) {\n        res += (n - p + 1);\n    }\n    return\
        \ (int)res;\n}"
      csharp: "public class Solution {\n    public int CountCommas(int n) {\n      \
        \  long res = 0;\n        for (long p = 1000; p <= (long)n; p *= 1000) {\n \
        \           res += (n - p + 1);\n        }\n        return (int)res;\n    }\n\
        }"
      javascript: "/**\n * @param {number} n\n * @return {number}\n */\nvar countCommas\
        \ = function(n) {\n    let res = 0;\n    for (let p = 1000; p <= n; p *= 1000)\
        \ {\n        res += (n - p + 1);\n    }\n    return res;\n};"
      typescript: "function countCommas(n: number): number {\n    if (n < 1000) {\n\
        \        return 0;\n    }\n    return n - 999;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @return Integer\n\
        \     */\n    function countCommas($n) {\n        if ($n < 1000) {\n       \
        \     return 0;\n        }\n        return $n - 999;\n    }\n}"
      swift: "class Solution {\n    func countCommas(_ n: Int) -> Int {\n        if\
        \ n < 1000 {\n            return 0\n        }\n        return n - 999\n    }\n\
        }"
      kotlin: "class Solution {\n    fun countCommas(n: Int): Int {\n        if (n <\
        \ 1000) {\n            return 0\n        }\n        return n - 999\n    }\n}"
      dart: "class Solution {\n  int countCommas(int n) {\n    if (n < 1000) {\n   \
        \   return 0;\n    }\n    return n - 999;\n  }\n}"
      go: "func countCommas(n int) int {\n    if n < 1000 {\n        return 0\n    }\n\
        \    return n - 999\n}"
      ruby: "# @param {Integer} n\n# @return {Integer}\ndef count_commas(n)\n  if n\
        \ < 1000\n    0\n  else\n    n - 999\n  end\nend"
      scala: "object Solution {\n    def countCommas(n: Int): Int = {\n        if (n\
        \ < 1000) 0 else n - 999\n    }\n}"
      rust: "impl Solution {\n    pub fn count_commas(n: i32) -> i32 {\n        if n\
        \ < 1000 {\n            0\n        } else {\n            n - 999\n        }\n\
        \    }\n}"
      racket: "(define/contract (count-commas n)\n  (-> exact-integer? exact-integer?)\n\
        \  (if (< n 1000) 0 (- n 999))\n  )"
      erlang: "-spec count_commas(N :: integer()) -> integer().\ncount_commas(N) ->\n\
        \  if\n    N < 1000 -> 0;\n    true -> N - 999\n  end."
      elixir: "defmodule Solution do\n  @spec count_commas(n :: integer) :: integer\n\
        \  def count_commas(n) do\n    if n < 1000 do\n      0\n    else\n      n -\
        \ 999\n    end\n  end\nend"
    approach: 'The total count of commas can be calculated by identifying how many numbers
      in the range [1, n] contain at least one, two, or more commas. According to standard
      formatting, a comma is added every three digits from the right, starting at the
      thousands place (1,000). Therefore, numbers from 1,000 up to $n$ each contribute
      at least one comma, numbers from 1,000,000 up to $n$ each contribute a second
      comma, and so on.


      By iterating through the thresholds where commas are first introduced ($10^3,
      10^6, 10^9, \dots$), we can compute the number of integers that reach each threshold
      level. For any specific threshold $P$, if $n \ge P$, there are exactly $n - P
      + 1$ integers in the range $[1, n]$ that contain at least that many commas. Summing
      these values for all $P \le n$ provides the total count of commas used across
      all integers in the given range.'
    time_complexity: O(log n). The algorithm iterates through powers of 1000 that are
      less than or equal to $n$. Since the threshold increases exponentially ($1000^i$),
      the number of iterations is logarithmic with respect to $n$, specifically $O(\log_{1000}
      n)$. For the given constraint $n \le 10^5$, the loop runs at most once.
    space_complexity: O(1). The solution uses a constant amount of extra space to store
      the running sum and the current power of 1000, regardless of the magnitude of
      the input $n$.
    elapsed_time: 140.87139058113098
    model: gemini-3-flash-preview
    generated_at: '2026-09-08 02:24:12 '
---

## Problem #3870: Count Commas in Range

**Difficulty:** Easy

**Topics:** Math

## Problem Description

<p>You are given an integer <code>n</code>.</p>

<p>Return the <strong>total</strong> number of commas used when writing all integers from <code>[1, n]</code> (inclusive) in <strong>standard</strong> number formatting.</p>

<p>In <strong>standard</strong> formatting:</p>

<ul>
	<li>A comma is inserted after <strong>every three</strong> digits from the right.</li>
	<li>Numbers with <strong>fewer</strong> than 4 digits contain no commas.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 1002</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The numbers <code>&quot;1,000&quot;</code>, <code>&quot;1,001&quot;</code>, and <code>&quot;1,002&quot;</code> each contain one comma, giving a total of 3.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 998</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Numbers in the range `[1000, 100000]` have one comma.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The total count of commas can be calculated by identifying how many numbers in the range [1, n] contain at least one, two, or more commas. According to standard formatting, a comma is added every three digits from the right, starting at the thousands place (1,000). Therefore, numbers from 1,000 up to $n$ each contribute at least one comma, numbers from 1,000,000 up to $n$ each contribute a second comma, and so on.

By iterating through the thresholds where commas are first introduced ($10^3, 10^6, 10^9, \dots$), we can compute the number of integers that reach each threshold level. For any specific threshold $P$, if $n \ge P$, there are exactly $n - P + 1$ integers in the range $[1, n]$ that contain at least that many commas. Summing these values for all $P \le n$ provides the total count of commas used across all integers in the given range.

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
    int countCommas(int n) {
        long long res = 0;
        for (long long p = 1000; p <= n; p *= 1000) {
            res += (n - p + 1);
        }
        return (int)res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countCommas(int n) {
        long res = 0;
        for (long p = 1000; p <= n; p *= 1000) {
            res += (n - p + 1);
        }
        return (int) res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        p = 1000
        while p <= n:
            res += (n - p + 1)
            p *= 1000
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        p = 1000
        while p <= n:
            res += (n - p + 1)
            p *= 1000
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countCommas(int n) {
    long long res = 0;
    for (long long p = 1000; p <= (long long)n; p *= 1000) {
        res += (n - p + 1);
    }
    return (int)res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountCommas(int n) {
        long res = 0;
        for (long p = 1000; p <= (long)n; p *= 1000) {
            res += (n - p + 1);
        }
        return (int)res;
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
var countCommas = function(n) {
    let res = 0;
    for (let p = 1000; p <= n; p *= 1000) {
        res += (n - p + 1);
    }
    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countCommas(n: number): number {
    if (n < 1000) {
        return 0;
    }
    return n - 999;
}
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
    function countCommas($n) {
        if ($n < 1000) {
            return 0;
        }
        return $n - 999;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countCommas(_ n: Int) -> Int {
        if n < 1000 {
            return 0
        }
        return n - 999
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countCommas(n: Int): Int {
        if (n < 1000) {
            return 0
        }
        return n - 999
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int countCommas(int n) {
    if (n < 1000) {
      return 0;
    }
    return n - 999;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func countCommas(n int) int {
    if n < 1000 {
        return 0
    }
    return n - 999
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @return {Integer}
def count_commas(n)
  if n < 1000
    0
  else
    n - 999
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countCommas(n: Int): Int = {
        if (n < 1000) 0 else n - 999
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_commas(n: i32) -> i32 {
        if n < 1000 {
            0
        } else {
            n - 999
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (count-commas n)
  (-> exact-integer? exact-integer?)
  (if (< n 1000) 0 (- n 999))
  )
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec count_commas(N :: integer()) -> integer().
count_commas(N) ->
  if
    N < 1000 -> 0;
    true -> N - 999
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_commas(n :: integer) :: integer
  def count_commas(n) do
    if n < 1000 do
      0
    else
      n - 999
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(log n). The algorithm iterates through powers of 1000 that are less than or equal to $n$. Since the threshold increases exponentially ($1000^i$), the number of iterations is logarithmic with respect to $n$, specifically $O(\log_{1000} n)$. For the given constraint $n \le 10^5$, the loop runs at most once.
- **Space Complexity:** O(1). The solution uses a constant amount of extra space to store the running sum and the current power of 1000, regardless of the magnitude of the input $n$.
