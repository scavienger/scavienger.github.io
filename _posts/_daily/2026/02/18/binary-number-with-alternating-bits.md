---
layout: post
title: "Binary Number with Alternating Bits"
date: 2026-02-18 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Bit Manipulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/binary-number-with-alternating-bits/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool hasAlternatingBits(int n) {\n      \
        \  long x = (long)n ^ (n >> 1);\n        return (x & (x + 1)) == 0;\n    }\n\
        };"
      java: "class Solution {\n    public boolean hasAlternatingBits(int n) {\n    \
        \    long x = (long)n ^ (n >> 1);\n        return (x & (x + 1)) == 0;\n    }\n\
        }"
      python: "class Solution(object):\n    def hasAlternatingBits(self, n):\n     \
        \   \"\"\"\n        :type n: int\n        :rtype: bool\n        \"\"\"\n   \
        \     x = n ^ (n >> 1)\n        return (x & (x + 1)) == 0"
      python3: "class Solution:\n    def hasAlternatingBits(self, n: int) -> bool:\n\
        \        x = n ^ (n >> 1)\n        return (x & (x + 1)) == 0"
      c: "bool hasAlternatingBits(int n) {\n    long x = (long)n ^ (n >> 1);\n    return\
        \ (x & (x + 1)) == 0;\n}"
      csharp: "public class Solution {\n    public bool HasAlternatingBits(int n) {\n\
        \        long x = (long)n ^ (n >> 1);\n        return (x & (x + 1)) == 0;\n\
        \    }\n}"
      javascript: "/**\n * @param {number} n\n * @return {boolean}\n */\nvar hasAlternatingBits\
        \ = function(n) {\n    let x = n ^ (n >>> 1);\n    return (x & (x + 1)) ===\
        \ 0;\n};"
      typescript: "function hasAlternatingBits(n: number): boolean {\n    const m =\
        \ n ^ (n >> 1);\n    return (m & (m + 1)) === 0;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @return Boolean\n\
        \     */\n    function hasAlternatingBits($n) {\n        $m = $n ^ ($n >> 1);\n\
        \        return ($m & ($m + 1)) == 0;\n    }\n}"
      swift: "class Solution {\n    func hasAlternatingBits(_ n: Int) -> Bool {\n  \
        \      let m = n ^ (n >> 1)\n        return (m & (m + 1)) == 0\n    }\n}"
      kotlin: "class Solution {\n    fun hasAlternatingBits(n: Int): Boolean {\n   \
        \     val m = n xor (n shr 1)\n        val mLong = m.toLong()\n        return\
        \ (mLong and (mLong + 1)) == 0L\n    }\n}"
      dart: "class Solution {\n  bool hasAlternatingBits(int n) {\n    int m = n ^ (n\
        \ >> 1);\n    return (m & (m + 1)) == 0;\n  }\n}"
      go: "func hasAlternatingBits(n int) bool {\n    m := n ^ (n >> 1)\n    return\
        \ (m & (m + 1)) == 0\n}"
      ruby: "# @param {Integer} n\n# @return {Boolean}\ndef has_alternating_bits(n)\n\
        \  m = n ^ (n >> 1)\n  (m & (m + 1)) == 0\nend"
      scala: "object Solution {\n    def hasAlternatingBits(n: Int): Boolean = {\n \
        \       val m = n.toLong ^ (n.toLong >> 1)\n        (m & (m + 1)) == 0\n   \
        \ }\n}"
      rust: "impl Solution {\n    pub fn has_alternating_bits(n: i32) -> bool {\n  \
        \      let m = (n as i64) ^ ((n as i64) >> 1);\n        (m & (m + 1)) == 0\n\
        \    }\n}"
      racket: "(define/contract (has-alternating-bits n)\n  (-> exact-integer? boolean?)\n\
        \  (let ([m (bitwise-xor n (arithmetic-shift n -1))])\n    (zero? (bitwise-and\
        \ m (+ m 1))))\n)"
      erlang: "-spec has_alternating_bits(N :: integer()) -> boolean().\nhas_alternating_bits(N)\
        \ ->\n  M = N bxor (N bsr 1),\n  (M band (M + 1)) =:= 0."
      elixir: "defmodule Solution do\n  @spec has_alternating_bits(n :: integer) ::\
        \ boolean\n  def has_alternating_bits(n) do\n    import Bitwise\n    m = n ^^^\
        \ (n >>> 1)\n    (m &&& (m + 1)) == 0\n  end\nend"
    approach: 'The problem can be solved by shifting the integer n right by one bit
      and performing an XOR operation with the original number. If n has alternating
      bits, the resulting value x will be a sequence of continuous 1s (e.g., if n is
      101, then 101 XOR 010 = 111). This happens because every bit at position i is
      guaranteed to be different from the bit at position i-1 in an alternating sequence.


      To verify if the resulting number x consists entirely of 1s, we can use the bitwise
      property that adding 1 to such a number results in a power of 2 where only the
      next higher bit is set (e.g., 111 + 1 = 1000). By performing a bitwise AND between
      x and x + 1, the result will be 0 if and only if x was a sequence of all 1s. This
      bitwise approach is extremely efficient and avoids the need for explicit loops
      or string conversions.'
    time_complexity: O(1). The bitwise operations are performed on fixed-width integers
      (at most 32 bits), which takes constant time regardless of the magnitude of the
      input integer n.
    space_complexity: O(1). The algorithm uses only a constant amount of auxiliary space
      to store intermediate bitwise results.
    elapsed_time: 114.37218046188354
    model: gemini-3-flash-preview
    generated_at: '2026-02-18 01:28:54 '
---

## Problem #693: Binary Number with Alternating Bits

**Difficulty:** Easy

**Topics:** Bit Manipulation

## Problem Description

<p>Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> true
<strong>Explanation:</strong> The binary representation of 5 is: 101
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 7
<strong>Output:</strong> false
<strong>Explanation:</strong> The binary representation of 7 is: 111.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 11
<strong>Output:</strong> false
<strong>Explanation:</strong> The binary representation of 11 is: 1011.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be solved by shifting the integer n right by one bit and performing an XOR operation with the original number. If n has alternating bits, the resulting value x will be a sequence of continuous 1s (e.g., if n is 101, then 101 XOR 010 = 111). This happens because every bit at position i is guaranteed to be different from the bit at position i-1 in an alternating sequence.

To verify if the resulting number x consists entirely of 1s, we can use the bitwise property that adding 1 to such a number results in a power of 2 where only the next higher bit is set (e.g., 111 + 1 = 1000). By performing a bitwise AND between x and x + 1, the result will be 0 if and only if x was a sequence of all 1s. This bitwise approach is extremely efficient and avoids the need for explicit loops or string conversions.

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
    bool hasAlternatingBits(int n) {
        long x = (long)n ^ (n >> 1);
        return (x & (x + 1)) == 0;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean hasAlternatingBits(int n) {
        long x = (long)n ^ (n >> 1);
        return (x & (x + 1)) == 0;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool hasAlternatingBits(int n) {
    long x = (long)n ^ (n >> 1);
    return (x & (x + 1)) == 0;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool HasAlternatingBits(int n) {
        long x = (long)n ^ (n >> 1);
        return (x & (x + 1)) == 0;
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
 * @return {boolean}
 */
var hasAlternatingBits = function(n) {
    let x = n ^ (n >>> 1);
    return (x & (x + 1)) === 0;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function hasAlternatingBits(n: number): boolean {
    const m = n ^ (n >> 1);
    return (m & (m + 1)) === 0;
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
     * @return Boolean
     */
    function hasAlternatingBits($n) {
        $m = $n ^ ($n >> 1);
        return ($m & ($m + 1)) == 0;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func hasAlternatingBits(_ n: Int) -> Bool {
        let m = n ^ (n >> 1)
        return (m & (m + 1)) == 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun hasAlternatingBits(n: Int): Boolean {
        val m = n xor (n shr 1)
        val mLong = m.toLong()
        return (mLong and (mLong + 1)) == 0L
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool hasAlternatingBits(int n) {
    int m = n ^ (n >> 1);
    return (m & (m + 1)) == 0;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func hasAlternatingBits(n int) bool {
    m := n ^ (n >> 1)
    return (m & (m + 1)) == 0
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @return {Boolean}
def has_alternating_bits(n)
  m = n ^ (n >> 1)
  (m & (m + 1)) == 0
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def hasAlternatingBits(n: Int): Boolean = {
        val m = n.toLong ^ (n.toLong >> 1)
        (m & (m + 1)) == 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn has_alternating_bits(n: i32) -> bool {
        let m = (n as i64) ^ ((n as i64) >> 1);
        (m & (m + 1)) == 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (has-alternating-bits n)
  (-> exact-integer? boolean?)
  (let ([m (bitwise-xor n (arithmetic-shift n -1))])
    (zero? (bitwise-and m (+ m 1))))
)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec has_alternating_bits(N :: integer()) -> boolean().
has_alternating_bits(N) ->
  M = N bxor (N bsr 1),
  (M band (M + 1)) =:= 0.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec has_alternating_bits(n :: integer) :: boolean
  def has_alternating_bits(n) do
    import Bitwise
    m = n ^^^ (n >>> 1)
    (m &&& (m + 1)) == 0
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(1). The bitwise operations are performed on fixed-width integers (at most 32 bits), which takes constant time regardless of the magnitude of the input integer n.
- **Space Complexity:** O(1). The algorithm uses only a constant amount of auxiliary space to store intermediate bitwise results.
