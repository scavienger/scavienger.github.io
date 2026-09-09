---
layout: post
title: "Count Commas in Range II"
date: 2026-09-09 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Math"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-commas-in-range-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long countCommas(long long n) {\n  \
        \      long long ans = 0;\n        long long start = 1000LL;\n        while\
        \ (start <= n) {\n            ans += (n - start + 1);\n            if (start\
        \ > n / 1000) break;\n            start *= 1000;\n        }\n        return\
        \ ans;\n    }\n};"
      java: "class Solution {\n    public long countCommas(long n) {\n        long ans\
        \ = 0;\n        long start = 1000L;\n        while (start <= n) {\n        \
        \    ans += (n - start + 1);\n            if (start > n / 1000) break;\n   \
        \         start *= 1000;\n        }\n        return ans;\n    }\n}"
      python: "class Solution(object):\n    def countCommas(self, n):\n        \"\"\"\
        \n        :type n: int\n        :rtype: int\n        \"\"\"\n        ans = 0\n\
        \        start = 1000\n        while start <= n:\n            ans += (n - start\
        \ + 1)\n            start *= 1000\n        return ans"
      python3: "class Solution:\n    def countCommas(self, n: int) -> int:\n       \
        \ ans = 0\n        start = 1000\n        while start <= n:\n            ans\
        \ += (n - start + 1)\n            start *= 1000\n        return ans"
      c: "long long countCommas(long long n) {\n    long long ans = 0;\n    long long\
        \ start = 1000LL;\n    while (start <= n) {\n        ans += (n - start + 1);\n\
        \        if (start > n / 1000) break;\n        start *= 1000;\n    }\n    return\
        \ ans;\n}"
      csharp: "public class Solution {\n    public long CountCommas(long n) {\n    \
        \    long total = 0;\n        long threshold = 1000;\n        while (threshold\
        \ <= n) {\n            total += (n - threshold + 1);\n            if (threshold\
        \ > n / 1000) {\n                break;\n            }\n            threshold\
        \ *= 1000;\n        }\n        return total;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @return {number}\n */\nvar countCommas\
        \ = function(n) {\n    let total = 0;\n    let threshold = 1000;\n    while\
        \ (threshold <= n) {\n        total += (n - threshold + 1);\n        if (threshold\
        \ > n / 1000) {\n            break;\n        }\n        threshold *= 1000;\n\
        \    }\n    return total;\n};"
      typescript: "function countCommas(n: number): number {\n    let total: number\
        \ = 0;\n    let threshold: number = 1000;\n    while (threshold <= n) {\n  \
        \      total += (n - threshold + 1);\n        if (threshold > n / 1000) {\n\
        \            break;\n        }\n        threshold *= 1000;\n    }\n    return\
        \ total;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @return Integer\n\
        \     */\n    function countCommas($n) {\n        $total = 0;\n        $threshold\
        \ = 1000;\n        while ($threshold <= $n) {\n            $total += ($n - $threshold\
        \ + 1);\n            if ($threshold > $n / 1000) {\n                break;\n\
        \            }\n            $threshold *= 1000;\n        }\n        return $total;\n\
        \    }\n}"
      swift: "class Solution {\n    func countCommas(_ n: Int) -> Int {\n        var\
        \ total = 0\n        var threshold = 1000\n        while threshold <= n {\n\
        \            total += (n - threshold + 1)\n            if threshold > n / 1000\
        \ {\n                break\n            }\n            threshold *= 1000\n \
        \       }\n        return total\n    }\n}"
      kotlin: "class Solution {\n    fun countCommas(n: Long): Long {\n        var total:\
        \ Long = 0\n        var p: Long = 1000\n        while (p <= n) {\n         \
        \   total += (n - p + 1)\n            if (p >= 1000000000000000L) break\n  \
        \          p *= 1000\n        }\n        return total\n    }\n}"
      dart: "class Solution {\n  int countCommas(int n) {\n    int total = 0;\n    int\
        \ p = 1000;\n    while (p <= n) {\n      total += (n - p + 1);\n      if (p\
        \ >= 1000000000000000) break;\n      p *= 1000;\n    }\n    return total;\n\
        \  }\n}"
      go: "func countCommas(n int64) int64 {\n    var total int64 = 0\n    var p int64\
        \ = 1000\n    for p <= n {\n        total += (n - p + 1)\n        if p >= 1000000000000000\
        \ {\n            break\n        }\n        p *= 1000\n    }\n    return total\n\
        }"
      ruby: "# @param {Integer} n\n# @return {Integer}\ndef count_commas(n)\n  total\
        \ = 0\n  p = 1000\n  while p <= n\n    total += (n - p + 1)\n    break if p\
        \ >= 1000000000000000\n    p *= 1000\n  end\n  total\nend"
      scala: "object Solution {\n    def countCommas(n: Long): Long = {\n        var\
        \ total: Long = 0\n        var p: Long = 1000\n        var keepGoing = true\n\
        \        while (p <= n && keepGoing) {\n            total += (n - p + 1)\n \
        \           if (p >= 1000000000000000L) {\n                keepGoing = false\n\
        \            } else {\n                p *= 1000\n            }\n        }\n\
        \        total\n    }\n}"
      rust: "impl Solution {\n    pub fn count_commas(n: i64) -> i64 {\n        let\
        \ mut total: i64 = 0;\n        let mut threshold: i64 = 1000;\n        while\
        \ threshold <= n {\n            total += n - threshold + 1;\n            if\
        \ threshold >= 1_000_000_000_000_000 {\n                break;\n           \
        \ }\n            threshold *= 1000;\n        }\n        total\n    }\n}"
      racket: "(define/contract (count-commas n)\n  (-> exact-integer? exact-integer?)\n\
        \  (let loop ([threshold 1000]\n             [total 0])\n    (if (<= threshold\
        \ n)\n        (loop (* threshold 1000) (+ total (+ (- n threshold) 1)))\n  \
        \      total)))"
      erlang: "-spec count_commas(N :: integer()) -> integer().\ncount_commas(N) ->\n\
        \    do_count(N, 1000, 0).\n\ndo_count(N, Threshold, Total) when Threshold =<\
        \ N ->\n    do_count(N, Threshold * 1000, Total + (N - Threshold + 1));\ndo_count(_N,\
        \ _Threshold, Total) ->\n    Total."
      elixir: "defmodule Solution do\n  @spec count_commas(n :: integer) :: integer\n\
        \  def count_commas(n) do\n    do_count(n, 1000, 0)\n  end\n\n  defp do_count(n,\
        \ threshold, total) when threshold <= n do\n    do_count(n, threshold * 1000,\
        \ total + (n - threshold + 1))\n  end\n\n  defp do_count(_n, _threshold, total)\
        \ do\n    total\n  end\nend"
    approach: 'The problem can be solved by counting the total number of commas contributed
      at each comma-introduction threshold. In standard number formatting, a comma is
      added for every three digits from the right. This means that integers from 1,000
      to 999,999 have at least one comma, integers from 1,000,000 to 999,999,999 have
      at least two commas, and so on. Generalizing this, a number contains at least
      $k$ commas if it is greater than or equal to $10^{3k}$.


      By iterating through powers of 1,000 (starting from 1,000), we can calculate how
      many integers in the range [1, n] reach each comma tier. For a given tier $P =
      10^{3k}$, the count of numbers contributing at least one comma from that tier
      is $n - P + 1$ (if $n \ge P$). By summing these counts across all tiers $k \ge
      1$, we capture every comma exactly once: a number with exactly $m$ commas will
      be $\ge 10^{3k}$ for $k=1, 2, \dots, m$, thus contributing exactly $m$ to the
      total sum. This allows us to calculate the result in logarithmic time without
      iterating through each individual number.'
    time_complexity: O(\log n) because the algorithm iterates through the powers of
      1,000. Since $1,000^k$ grows exponentially, the total number of iterations is
      proportional to the number of digits in $n$ divided by 3. For $n = 10^{15}$, this
      involves only 5 iterations, making the algorithm extremely efficient.
    space_complexity: O(1) because the algorithm only uses a fixed number of long integer
      variables to track the current tier and the accumulated sum, regardless of the
      size of $n$.
    elapsed_time: 256.9350936412811
    model: gemini-3-flash-preview
    generated_at: '2026-09-09 02:29:05 '
---

## Problem #3871: Count Commas in Range II

**Difficulty:** Medium

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

<p><strong>​​​​​​​</strong>All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>15</sup></code></li>
</ul>


## Hints

1. Count the numbers in each comma group (1-3 digits, 4-6 digits, 7-9 digits, ...) and multiply by how many commas each number in that group has.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be solved by counting the total number of commas contributed at each comma-introduction threshold. In standard number formatting, a comma is added for every three digits from the right. This means that integers from 1,000 to 999,999 have at least one comma, integers from 1,000,000 to 999,999,999 have at least two commas, and so on. Generalizing this, a number contains at least $k$ commas if it is greater than or equal to $10^{3k}$.

By iterating through powers of 1,000 (starting from 1,000), we can calculate how many integers in the range [1, n] reach each comma tier. For a given tier $P = 10^{3k}$, the count of numbers contributing at least one comma from that tier is $n - P + 1$ (if $n \ge P$). By summing these counts across all tiers $k \ge 1$, we capture every comma exactly once: a number with exactly $m$ commas will be $\ge 10^{3k}$ for $k=1, 2, \dots, m$, thus contributing exactly $m$ to the total sum. This allows us to calculate the result in logarithmic time without iterating through each individual number.

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
    long long countCommas(long long n) {
        long long ans = 0;
        long long start = 1000LL;
        while (start <= n) {
            ans += (n - start + 1);
            if (start > n / 1000) break;
            start *= 1000;
        }
        return ans;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long countCommas(long n) {
        long ans = 0;
        long start = 1000L;
        while (start <= n) {
            ans += (n - start + 1);
            if (start > n / 1000) break;
            start *= 1000;
        }
        return ans;
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
        ans = 0
        start = 1000
        while start <= n:
            ans += (n - start + 1)
            start *= 1000
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        start = 1000
        while start <= n:
            ans += (n - start + 1)
            start *= 1000
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
long long countCommas(long long n) {
    long long ans = 0;
    long long start = 1000LL;
    while (start <= n) {
        ans += (n - start + 1);
        if (start > n / 1000) break;
        start *= 1000;
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long CountCommas(long n) {
        long total = 0;
        long threshold = 1000;
        while (threshold <= n) {
            total += (n - threshold + 1);
            if (threshold > n / 1000) {
                break;
            }
            threshold *= 1000;
        }
        return total;
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
    let total = 0;
    let threshold = 1000;
    while (threshold <= n) {
        total += (n - threshold + 1);
        if (threshold > n / 1000) {
            break;
        }
        threshold *= 1000;
    }
    return total;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countCommas(n: number): number {
    let total: number = 0;
    let threshold: number = 1000;
    while (threshold <= n) {
        total += (n - threshold + 1);
        if (threshold > n / 1000) {
            break;
        }
        threshold *= 1000;
    }
    return total;
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
    function countCommas($n) {
        $total = 0;
        $threshold = 1000;
        while ($threshold <= $n) {
            $total += ($n - $threshold + 1);
            if ($threshold > $n / 1000) {
                break;
            }
            $threshold *= 1000;
        }
        return $total;
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
        var total = 0
        var threshold = 1000
        while threshold <= n {
            total += (n - threshold + 1)
            if threshold > n / 1000 {
                break
            }
            threshold *= 1000
        }
        return total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countCommas(n: Long): Long {
        var total: Long = 0
        var p: Long = 1000
        while (p <= n) {
            total += (n - p + 1)
            if (p >= 1000000000000000L) break
            p *= 1000
        }
        return total
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
    int total = 0;
    int p = 1000;
    while (p <= n) {
      total += (n - p + 1);
      if (p >= 1000000000000000) break;
      p *= 1000;
    }
    return total;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func countCommas(n int64) int64 {
    var total int64 = 0
    var p int64 = 1000
    for p <= n {
        total += (n - p + 1)
        if p >= 1000000000000000 {
            break
        }
        p *= 1000
    }
    return total
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
  total = 0
  p = 1000
  while p <= n
    total += (n - p + 1)
    break if p >= 1000000000000000
    p *= 1000
  end
  total
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countCommas(n: Long): Long = {
        var total: Long = 0
        var p: Long = 1000
        var keepGoing = true
        while (p <= n && keepGoing) {
            total += (n - p + 1)
            if (p >= 1000000000000000L) {
                keepGoing = false
            } else {
                p *= 1000
            }
        }
        total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_commas(n: i64) -> i64 {
        let mut total: i64 = 0;
        let mut threshold: i64 = 1000;
        while threshold <= n {
            total += n - threshold + 1;
            if threshold >= 1_000_000_000_000_000 {
                break;
            }
            threshold *= 1000;
        }
        total
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
  (let loop ([threshold 1000]
             [total 0])
    (if (<= threshold n)
        (loop (* threshold 1000) (+ total (+ (- n threshold) 1)))
        total)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec count_commas(N :: integer()) -> integer().
count_commas(N) ->
    do_count(N, 1000, 0).

do_count(N, Threshold, Total) when Threshold =< N ->
    do_count(N, Threshold * 1000, Total + (N - Threshold + 1));
do_count(_N, _Threshold, Total) ->
    Total.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_commas(n :: integer) :: integer
  def count_commas(n) do
    do_count(n, 1000, 0)
  end

  defp do_count(n, threshold, total) when threshold <= n do
    do_count(n, threshold * 1000, total + (n - threshold + 1))
  end

  defp do_count(_n, _threshold, total) do
    total
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(\log n) because the algorithm iterates through the powers of 1,000. Since $1,000^k$ grows exponentially, the total number of iterations is proportional to the number of digits in $n$ divided by 3. For $n = 10^{15}$, this involves only 5 iterations, making the algorithm extremely efficient.
- **Space Complexity:** O(1) because the algorithm only uses a fixed number of long integer variables to track the current tier and the accumulated sum, regardless of the size of $n$.
