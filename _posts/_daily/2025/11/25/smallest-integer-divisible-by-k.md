---
layout: post
title: "Smallest Integer Divisible by K"
date: 2025-11-25 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Hash Table", "Math", "Pigeonhole Principle"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/smallest-integer-divisible-by-k/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int smallestRepunitDivByK(int k) {\n    \
        \    if (k % 2 == 0 || k % 5 == 0) {\n            return -1;\n        }\n\n\
        \        int remainder = 0;\n        for (int length = 1; length <= k; ++length)\
        \ {\n            remainder = (remainder * 10 + 1) % k;\n            if (remainder\
        \ == 0) {\n                return length;\n            }\n        }\n      \
        \  return -1;\n    }\n};"
      java: "class Solution {\n    public int smallestRepunitDivByK(int k) {\n     \
        \   if (k % 2 == 0 || k % 5 == 0) {\n            return -1;\n        }\n\n \
        \       int remainder = 0;\n        for (int length = 1; length <= k; length++)\
        \ {\n            remainder = (remainder * 10 + 1) % k;\n            if (remainder\
        \ == 0) {\n                return length;\n            }\n        }\n      \
        \  return -1;\n    }\n}"
      python: "class Solution(object):\n    def smallestRepunitDivByK(self, k):\n  \
        \      \"\"\"\n        :type k: int\n        :rtype: int\n        \"\"\"\n \
        \       if k % 2 == 0 or k % 5 == 0:\n            return -1\n\n        remainder\
        \ = 0\n        for length in range(1, k + 1):\n            remainder = (remainder\
        \ * 10 + 1) % k\n            if remainder == 0:\n                return length\n\
        \        return -1"
      python3: "class Solution:\n    def smallestRepunitDivByK(self, k: int) -> int:\n\
        \        if k % 2 == 0 or k % 5 == 0:\n            return -1\n\n        remainder\
        \ = 0\n        for length in range(1, k + 1):\n            remainder = (remainder\
        \ * 10 + 1) % k\n            if remainder == 0:\n                return length\n\
        \        return -1"
      c: "int smallestRepunitDivByK(int k) {\n    if (k % 2 == 0 || k % 5 == 0) {\n\
        \        return -1;\n    }\n\n    int remainder = 0;\n    for (int length =\
        \ 1; length <= k; ++length) {\n        remainder = (remainder * 10 + 1) % k;\n\
        \        if (remainder == 0) {\n            return length;\n        }\n    }\n\
        \    return -1;\n}"
      csharp: "public class Solution {\n    public int SmallestRepunitDivByK(int k)\
        \ {\n        if (k % 2 == 0 || k % 5 == 0) {\n            return -1;\n     \
        \   }\n\n        int remainder = 0;\n        for (int length = 1; length <=\
        \ k; length++) {\n            remainder = (remainder * 10 + 1) % k;\n      \
        \      if (remainder == 0) {\n                return length;\n            }\n\
        \        }\n\n        return -1;\n    }\n}"
      javascript: "/**\n * @param {number} k\n * @return {number}\n */\nvar smallestRepunitDivByK\
        \ = function(k) {\n    if (k % 2 === 0 || k % 5 === 0) {\n        return -1;\n\
        \    }\n\n    let remainder = 0;\n    for (let length = 1; length <= k; length++)\
        \ {\n        remainder = (remainder * 10 + 1) % k;\n        if (remainder ===\
        \ 0) {\n            return length;\n        }\n    }\n\n    return -1;\n};"
      typescript: "function smallestRepunitDivByK(k: number): number {\n    if (k %\
        \ 2 === 0 || k % 5 === 0) {\n        return -1;\n    }\n\n    let remainder\
        \ = 0;\n    for (let length = 1; length <= k; length++) {\n        remainder\
        \ = (remainder * 10 + 1) % k;\n        if (remainder === 0) {\n            return\
        \ length;\n        }\n    }\n\n    return -1;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $k\n     * @return Integer\n\
        \     */\n    function smallestRepunitDivByK($k) {\n        if ($k % 2 == 0\
        \ || $k % 5 == 0) {\n            return -1;\n        }\n\n        $remainder\
        \ = 0;\n        for ($length = 1; $length <= $k; $length++) {\n            $remainder\
        \ = ($remainder * 10 + 1) % $k;\n            if ($remainder == 0) {\n      \
        \          return $length;\n            }\n        }\n\n        return -1;\n\
        \    }\n}"
      swift: "class Solution {\n    func smallestRepunitDivByK(_ k: Int) -> Int {\n\
        \        if k % 2 == 0 || k % 5 == 0 {\n            return -1\n        }\n\n\
        \        var remainder = 0\n        for length in 1...k {\n            remainder\
        \ = (remainder * 10 + 1) % k\n            if remainder == 0 {\n            \
        \    return length\n            }\n        }\n\n        return -1\n    }\n}"
      kotlin: "class Solution {\n    fun smallestRepunitDivByK(k: Int): Int {\n    \
        \    if (k % 2 == 0 || k % 5 == 0) {\n            return -1\n        }\n\n \
        \       var remainder = 0\n        for (length in 1..k) {\n            remainder\
        \ = (remainder * 10 + 1) % k\n            if (remainder == 0) {\n          \
        \      return length\n            }\n        }\n        return -1\n    }\n}"
      dart: "class Solution {\n  int smallestRepunitDivByK(int k) {\n    if (k % 2 ==\
        \ 0 || k % 5 == 0) {\n      return -1;\n    }\n\n    var remainder = 0;\n  \
        \  for (var length = 1; length <= k; length++) {\n      remainder = (remainder\
        \ * 10 + 1) % k;\n      if (remainder == 0) {\n        return length;\n    \
        \  }\n    }\n    return -1;\n  }\n}"
      go: "func smallestRepunitDivByK(k int) int {\n\tif k%2 == 0 || k%5 == 0 {\n\t\t\
        return -1\n\t}\n\n\tremainder := 0\n\tfor length := 1; length <= k; length++\
        \ {\n\t\tremainder = (remainder*10 + 1) % k\n\t\tif remainder == 0 {\n\t\t\t\
        return length\n\t\t}\n\t}\n\treturn -1\n}"
      ruby: "# @param {Integer} k\n# @return {Integer}\ndef smallest_repunit_div_by_k(k)\n\
        \  return -1 if k % 2 == 0 || k % 5 == 0\n\n  remainder = 0\n  (1..k).each do\
        \ |length|\n    remainder = (remainder * 10 + 1) % k\n    return length if remainder\
        \ == 0\n  end\n  -1\nend"
      scala: "object Solution {\n    def smallestRepunitDivByK(k: Int): Int = {\n  \
        \      if (k % 2 == 0 || k % 5 == 0) {\n            return -1\n        }\n\n\
        \        var remainder = 0\n        for (length <- 1 to k) {\n            remainder\
        \ = (remainder * 10 + 1) % k\n            if (remainder == 0) {\n          \
        \      return length\n            }\n        }\n        -1\n    }\n}"
      rust: "impl Solution {\n    pub fn smallest_repunit_div_by_k(k: i32) -> i32 {\n\
        \        if k % 2 == 0 || k % 5 == 0 {\n            return -1;\n        }\n\n\
        \        let mut remainder = 0;\n        for length in 1..=k {\n           \
        \ remainder = (remainder * 10 + 1) % k;\n            if remainder == 0 {\n \
        \               return length;\n            }\n        }\n        -1\n    }\n\
        }"
      racket: "(define/contract (smallest-repunit-div-by-k k)\n  (-> exact-integer?\
        \ exact-integer?)\n  (if (or (= (remainder k 2) 0) (= (remainder k 5) 0))\n\
        \      -1\n      (let loop ([length 1] [rem 0])\n        (if (> length k)\n\
        \            -1\n            (let ([next-rem (remainder (+ (* rem 10) 1) k)])\n\
        \              (if (= next-rem 0)\n                  length\n              \
        \    (loop (+ length 1) next-rem)))))))"
      erlang: "-spec smallest_repunit_div_by_k(K :: integer()) -> integer().\nsmallest_repunit_div_by_k(K)\
        \ ->\n  case K rem 2 =:= 0 orelse K rem 5 =:= 0 of\n    true -> -1;\n    false\
        \ -> smallest_repunit_div_by_k(K, 1, 0)\n  end.\n\nsmallest_repunit_div_by_k(K,\
        \ Length, _) when Length > K ->\n  -1;\nsmallest_repunit_div_by_k(K, Length,\
        \ Remainder) ->\n  NextRemainder = (Remainder * 10 + 1) rem K,\n  case NextRemainder\
        \ of\n    0 -> Length;\n    _ -> smallest_repunit_div_by_k(K, Length + 1, NextRemainder)\n\
        \  end."
      elixir: "defmodule Solution do\n  @spec smallest_repunit_div_by_k(k :: integer)\
        \ :: integer\n  def smallest_repunit_div_by_k(k) do\n    if rem(k, 2) == 0 or\
        \ rem(k, 5) == 0 do\n      -1\n    else\n      search(k, 1, 0)\n    end\n  end\n\
        \n  defp search(k, length, _remainder) when length > k, do: -1\n\n  defp search(k,\
        \ length, remainder) do\n    next_remainder = rem(remainder * 10 + 1, k)\n\n\
        \    if next_remainder == 0 do\n      length\n    else\n      search(k, length\
        \ + 1, next_remainder)\n    end\n  end\nend"
    approach: 'A repunit can only be divisible by k if k is relatively prime to 10,
      since every repunit ends in 1. If k is divisible by 2 or 5, return -1.


      Otherwise, build each repunit remainder without constructing the number: update
      remainder = (remainder * 10 + 1) % k for lengths from 1 through k. A remainder
      of 0 gives the answer. Among k possible remainders, one must repeat within k steps;
      once it repeats, later remainders cycle, so no new zero can occur.'
    time_complexity: O(k), since at most k remainders are computed.
    space_complexity: O(1), since only the current remainder and length are stored.
    elapsed_time: 57.834251165390015
    model: gpt-6-luna
    generated_at: '2026-11-13 00:13:01 '
---

## Problem #1015: Smallest Integer Divisible by K

**Difficulty:** Medium

**Topics:** Hash Table, Math, Pigeonhole Principle

## Problem Description

<p>Given a positive integer <code>k</code>, you need to find the <strong>length</strong> of the <strong>smallest</strong> positive integer <code>n</code> such that <code>n</code> is divisible by <code>k</code>, and <code>n</code> only contains the digit <code>1</code>.</p>

<p>Return <em>the <strong>length</strong> of </em><code>n</code>. If there is no such <code>n</code>, return -1.</p>

<p><strong>Note:</strong> <code>n</code> may not fit in a 64-bit signed integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> k = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> The smallest answer is n = 1, which has length 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> k = 2
<strong>Output:</strong> -1
<strong>Explanation:</strong> There is no such positive integer n divisible by 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The smallest answer is n = 111, which has length 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. 11111 = 1111 * 10 + 1
We only need to store remainders modulo K.

2. If we never get a remainder of 0, why would that happen, and how would we know that?

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

A repunit can only be divisible by k if k is relatively prime to 10, since every repunit ends in 1. If k is divisible by 2 or 5, return -1.

Otherwise, build each repunit remainder without constructing the number: update remainder = (remainder * 10 + 1) % k for lengths from 1 through k. A remainder of 0 gives the answer. Among k possible remainders, one must repeat within k steps; once it repeats, later remainders cycle, so no new zero can occur.

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
    int smallestRepunitDivByK(int k) {
        if (k % 2 == 0 || k % 5 == 0) {
            return -1;
        }

        int remainder = 0;
        for (int length = 1; length <= k; ++length) {
            remainder = (remainder * 10 + 1) % k;
            if (remainder == 0) {
                return length;
            }
        }
        return -1;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int smallestRepunitDivByK(int k) {
        if (k % 2 == 0 || k % 5 == 0) {
            return -1;
        }

        int remainder = 0;
        for (int length = 1; length <= k; length++) {
            remainder = (remainder * 10 + 1) % k;
            if (remainder == 0) {
                return length;
            }
        }
        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length
        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length
        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int smallestRepunitDivByK(int k) {
    if (k % 2 == 0 || k % 5 == 0) {
        return -1;
    }

    int remainder = 0;
    for (int length = 1; length <= k; ++length) {
        remainder = (remainder * 10 + 1) % k;
        if (remainder == 0) {
            return length;
        }
    }
    return -1;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int SmallestRepunitDivByK(int k) {
        if (k % 2 == 0 || k % 5 == 0) {
            return -1;
        }

        int remainder = 0;
        for (int length = 1; length <= k; length++) {
            remainder = (remainder * 10 + 1) % k;
            if (remainder == 0) {
                return length;
            }
        }

        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} k
 * @return {number}
 */
var smallestRepunitDivByK = function(k) {
    if (k % 2 === 0 || k % 5 === 0) {
        return -1;
    }

    let remainder = 0;
    for (let length = 1; length <= k; length++) {
        remainder = (remainder * 10 + 1) % k;
        if (remainder === 0) {
            return length;
        }
    }

    return -1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function smallestRepunitDivByK(k: number): number {
    if (k % 2 === 0 || k % 5 === 0) {
        return -1;
    }

    let remainder = 0;
    for (let length = 1; length <= k; length++) {
        remainder = (remainder * 10 + 1) % k;
        if (remainder === 0) {
            return length;
        }
    }

    return -1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $k
     * @return Integer
     */
    function smallestRepunitDivByK($k) {
        if ($k % 2 == 0 || $k % 5 == 0) {
            return -1;
        }

        $remainder = 0;
        for ($length = 1; $length <= $k; $length++) {
            $remainder = ($remainder * 10 + 1) % $k;
            if ($remainder == 0) {
                return $length;
            }
        }

        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func smallestRepunitDivByK(_ k: Int) -> Int {
        if k % 2 == 0 || k % 5 == 0 {
            return -1
        }

        var remainder = 0
        for length in 1...k {
            remainder = (remainder * 10 + 1) % k
            if remainder == 0 {
                return length
            }
        }

        return -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun smallestRepunitDivByK(k: Int): Int {
        if (k % 2 == 0 || k % 5 == 0) {
            return -1
        }

        var remainder = 0
        for (length in 1..k) {
            remainder = (remainder * 10 + 1) % k
            if (remainder == 0) {
                return length
            }
        }
        return -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int smallestRepunitDivByK(int k) {
    if (k % 2 == 0 || k % 5 == 0) {
      return -1;
    }

    var remainder = 0;
    for (var length = 1; length <= k; length++) {
      remainder = (remainder * 10 + 1) % k;
      if (remainder == 0) {
        return length;
      }
    }
    return -1;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func smallestRepunitDivByK(k int) int {
	if k%2 == 0 || k%5 == 0 {
		return -1
	}

	remainder := 0
	for length := 1; length <= k; length++ {
		remainder = (remainder*10 + 1) % k
		if remainder == 0 {
			return length
		}
	}
	return -1
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} k
# @return {Integer}
def smallest_repunit_div_by_k(k)
  return -1 if k % 2 == 0 || k % 5 == 0

  remainder = 0
  (1..k).each do |length|
    remainder = (remainder * 10 + 1) % k
    return length if remainder == 0
  end
  -1
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def smallestRepunitDivByK(k: Int): Int = {
        if (k % 2 == 0 || k % 5 == 0) {
            return -1
        }

        var remainder = 0
        for (length <- 1 to k) {
            remainder = (remainder * 10 + 1) % k
            if (remainder == 0) {
                return length
            }
        }
        -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn smallest_repunit_div_by_k(k: i32) -> i32 {
        if k % 2 == 0 || k % 5 == 0 {
            return -1;
        }

        let mut remainder = 0;
        for length in 1..=k {
            remainder = (remainder * 10 + 1) % k;
            if remainder == 0 {
                return length;
            }
        }
        -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (smallest-repunit-div-by-k k)
  (-> exact-integer? exact-integer?)
  (if (or (= (remainder k 2) 0) (= (remainder k 5) 0))
      -1
      (let loop ([length 1] [rem 0])
        (if (> length k)
            -1
            (let ([next-rem (remainder (+ (* rem 10) 1) k)])
              (if (= next-rem 0)
                  length
                  (loop (+ length 1) next-rem)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec smallest_repunit_div_by_k(K :: integer()) -> integer().
smallest_repunit_div_by_k(K) ->
  case K rem 2 =:= 0 orelse K rem 5 =:= 0 of
    true -> -1;
    false -> smallest_repunit_div_by_k(K, 1, 0)
  end.

smallest_repunit_div_by_k(K, Length, _) when Length > K ->
  -1;
smallest_repunit_div_by_k(K, Length, Remainder) ->
  NextRemainder = (Remainder * 10 + 1) rem K,
  case NextRemainder of
    0 -> Length;
    _ -> smallest_repunit_div_by_k(K, Length + 1, NextRemainder)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec smallest_repunit_div_by_k(k :: integer) :: integer
  def smallest_repunit_div_by_k(k) do
    if rem(k, 2) == 0 or rem(k, 5) == 0 do
      -1
    else
      search(k, 1, 0)
    end
  end

  defp search(k, length, _remainder) when length > k, do: -1

  defp search(k, length, remainder) do
    next_remainder = rem(remainder * 10 + 1, k)

    if next_remainder == 0 do
      length
    else
      search(k, length + 1, next_remainder)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(k), since at most k remainders are computed.
- **Space Complexity:** O(1), since only the current remainder and length are stored.
