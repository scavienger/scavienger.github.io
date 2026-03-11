---
layout: post
title: "Complement of Base 10 Integer"
date: 2026-03-11 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Bit Manipulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/complement-of-base-10-integer/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int bitwiseComplement(int n) {\n        if\
        \ (n == 0) return 1;\n        unsigned int mask = 1;\n        while (mask <\
        \ n) {\n            mask = (mask << 1) | 1;\n        }\n        return n ^ mask;\n\
        \    }\n};"
      java: "class Solution {\n    public int bitwiseComplement(int n) {\n        if\
        \ (n == 0) return 1;\n        int mask = 1;\n        while (mask < n) {\n  \
        \          mask = (mask << 1) | 1;\n        }\n        return n ^ mask;\n  \
        \  }\n}"
      python: "class Solution(object):\n    def bitwiseComplement(self, n):\n      \
        \  \"\"\"\n        :type n: int\n        :rtype: int\n        \"\"\"\n     \
        \   if n == 0: return 1\n        mask = 1\n        while mask < n:\n       \
        \     mask = (mask << 1) | 1\n        return n ^ mask"
      python3: "class Solution:\n    def bitwiseComplement(self, n: int) -> int:\n \
        \       if n == 0: return 1\n        mask = 1\n        while mask < n:\n   \
        \         mask = (mask << 1) | 1\n        return n ^ mask"
      c: "int bitwiseComplement(int n) {\n    if (n == 0) return 1;\n    unsigned int\
        \ mask = 1;\n    while (mask < n) {\n        mask = (mask << 1) | 1;\n    }\n\
        \    return n ^ (int)mask;\n}"
      csharp: "public class Solution {\n    public int BitwiseComplement(int n) {\n\
        \        if (n == 0) return 1;\n        int mask = 1;\n        while (mask <\
        \ n) {\n            mask = (mask << 1) | 1;\n        }\n        return n ^ mask;\n\
        \    }\n}"
      javascript: "/**\n * @param {number} n\n * @return {number}\n */\nvar bitwiseComplement\
        \ = function(n) {\n    if (n === 0) return 1;\n    let mask = 1;\n    while\
        \ (mask < n) {\n        mask = (mask << 1) | 1;\n    }\n    return n ^ mask;\n\
        };"
      typescript: "function bitwiseComplement(n: number): number {\n    if (n === 0)\
        \ return 1;\n    let mask = 1;\n    while (mask < n) {\n        mask = (mask\
        \ << 1) | 1;\n    }\n    return n ^ mask;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @return Integer\n\
        \     */\n    function bitwiseComplement($n) {\n        if ($n === 0) return\
        \ 1;\n        $mask = 1;\n        while ($mask < $n) {\n            $mask =\
        \ ($mask << 1) | 1;\n        }\n        return $n ^ $mask;\n    }\n}"
      swift: "class Solution {\n    func bitwiseComplement(_ n: Int) -> Int {\n    \
        \    if n == 0 { return 1 }\n        var mask = 1\n        while mask < n {\n\
        \            mask = (mask << 1) | 1\n        }\n        return n ^ mask\n  \
        \  }\n}"
      kotlin: "class Solution {\n    fun bitwiseComplement(n: Int): Int {\n        if\
        \ (n == 0) return 1\n        var mask = 1\n        while (mask < n) {\n    \
        \        mask = (mask shl 1) or 1\n        }\n        return n xor mask\n  \
        \  }\n}"
      dart: "class Solution {\n  int bitwiseComplement(int n) {\n    if (n == 0) return\
        \ 1;\n    int mask = 1;\n    while (mask < n) {\n      mask = (mask << 1) |\
        \ 1;\n    }\n    return n ^ mask;\n  }\n}"
      go: "func bitwiseComplement(n int) int {\n    if n == 0 {\n        return 1\n\
        \    }\n    mask := 1\n    for mask < n {\n        mask = (mask << 1) | 1\n\
        \    }\n    return n ^ mask\n}"
      ruby: "# @param {Integer} n\n# @return {Integer}\ndef bitwise_complement(n)\n\
        \  mask = 1\n  while mask < n\n    mask = (mask << 1) | 1\n  end\n  n ^ mask\n\
        end"
      scala: "object Solution {\n    def bitwiseComplement(n: Int): Int = {\n      \
        \  var mask = 1\n        while (mask < n) {\n            mask = (mask << 1)\
        \ | 1\n        }\n        n ^ mask\n    }\n}"
      rust: "impl Solution {\n    pub fn bitwise_complement(n: i32) -> i32 {\n     \
        \   let mut mask = 1;\n        while mask < n {\n            mask = (mask <<\
        \ 1) | 1;\n        }\n        n ^ mask\n    }\n}"
      racket: "(define/contract (bitwise-complement n)\n  (-> exact-integer? exact-integer?)\n\
        \  (let loop ([mask 1])\n    (if (< mask n)\n        (loop (bitwise-ior (arithmetic-shift\
        \ mask 1) 1))\n        (bitwise-xor n mask))))"
      erlang: "-spec bitwise_complement(N :: integer()) -> integer().\nbitwise_complement(N)\
        \ ->\n  find_mask(1, N) bxor N.\n\nfind_mask(Mask, N) when Mask < N ->\n  find_mask((Mask\
        \ bsl 1) bor 1, N);\nfind_mask(Mask, _) ->\n  Mask."
      elixir: "defmodule Solution do\n  @spec bitwise_complement(n :: integer) :: integer\n\
        \  def bitwise_complement(n) do\n    do_complement(1, n)\n  end\n\n  defp do_complement(mask,\
        \ n) when mask < n do\n    do_complement(Bitwise.bor(Bitwise.bsl(mask, 1), 1),\
        \ n)\n  end\n\n  defp do_complement(mask, n) do\n    Bitwise.bxor(n, mask)\n\
        \  end\nend"
    approach: 'To find the bitwise complement of a non-negative integer $n$, we need
      to flip every bit in its binary representation. The key intuition is that XORing
      a binary number with a bitmask of all ones (of the same bit length) will flip
      all its bits. For example, if $n = 5$ ($101_2$), we use a bitmask of $7$ ($111_2$).
      The result of $5 \oplus 7$ is $2$ ($010_2$), which is the desired complement.


      The algorithm handles the special case where $n = 0$ by returning 1, as its binary
      representation ''0'' has a complement of ''1''. For $n > 0$, we construct a bitmask
      by starting at 1 and repeatedly shifting left and ORing with 1 until the mask
      is greater than or equal to $n$. Since $n$ is at most $10^9$, which is less than
      $2^{30}$, this loop executes at most 30 times, ensuring the operation is extremely
      efficient.'
    time_complexity: O(log n) as the algorithm performs a number of iterations proportional
      to the number of bits in the integer n. Since $n < 10^9$, this is at most 30 iterations.
    space_complexity: O(1) because the algorithm only uses a constant amount of extra
      space for the bitmask variable, regardless of the input size.
    elapsed_time: 128.10880184173584
    model: gemini-3-flash-preview
    generated_at: '2026-03-11 01:20:51 '
---

## Problem #1009: Complement of Base 10 Integer

**Difficulty:** Easy

**Topics:** Bit Manipulation

## Problem Description

<p>The <strong>complement</strong> of an integer is the integer you get when you flip all the <code>0</code>&#39;s to <code>1</code>&#39;s and all the <code>1</code>&#39;s to <code>0</code>&#39;s in its binary representation.</p>

<ul>
	<li>For example, The integer <code>5</code> is <code>&quot;101&quot;</code> in binary and its <strong>complement</strong> is <code>&quot;010&quot;</code> which is the integer <code>2</code>.</li>
</ul>

<p>Given an integer <code>n</code>, return <em>its complement</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> 5 is &quot;101&quot; in binary, with complement &quot;010&quot; in binary, which is 2 in base-10.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 7
<strong>Output:</strong> 0
<strong>Explanation:</strong> 7 is &quot;111&quot; in binary, with complement &quot;000&quot; in binary, which is 0 in base-10.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 5
<strong>Explanation:</strong> 10 is &quot;1010&quot; in binary, with complement &quot;0101&quot; in binary, which is 5 in base-10.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt; 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as 476: <a href="https://leetcode.com/problems/number-complement/" target="_blank">https://leetcode.com/problems/number-complement/</a></p>


## Hints

1. A binary number plus its complement will equal 111....111 in binary.  Also, N = 0 is a corner case.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To find the bitwise complement of a non-negative integer $n$, we need to flip every bit in its binary representation. The key intuition is that XORing a binary number with a bitmask of all ones (of the same bit length) will flip all its bits. For example, if $n = 5$ ($101_2$), we use a bitmask of $7$ ($111_2$). The result of $5 \oplus 7$ is $2$ ($010_2$), which is the desired complement.

The algorithm handles the special case where $n = 0$ by returning 1, as its binary representation '0' has a complement of '1'. For $n > 0$, we construct a bitmask by starting at 1 and repeatedly shifting left and ORing with 1 until the mask is greater than or equal to $n$. Since $n$ is at most $10^9$, which is less than $2^{30}$, this loop executes at most 30 times, ensuring the operation is extremely efficient.

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
    int bitwiseComplement(int n) {
        if (n == 0) return 1;
        unsigned int mask = 1;
        while (mask < n) {
            mask = (mask << 1) | 1;
        }
        return n ^ mask;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int bitwiseComplement(int n) {
        if (n == 0) return 1;
        int mask = 1;
        while (mask < n) {
            mask = (mask << 1) | 1;
        }
        return n ^ mask;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        mask = 1
        while mask < n:
            mask = (mask << 1) | 1
        return n ^ mask
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        mask = 1
        while mask < n:
            mask = (mask << 1) | 1
        return n ^ mask
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int bitwiseComplement(int n) {
    if (n == 0) return 1;
    unsigned int mask = 1;
    while (mask < n) {
        mask = (mask << 1) | 1;
    }
    return n ^ (int)mask;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int BitwiseComplement(int n) {
        if (n == 0) return 1;
        int mask = 1;
        while (mask < n) {
            mask = (mask << 1) | 1;
        }
        return n ^ mask;
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
var bitwiseComplement = function(n) {
    if (n === 0) return 1;
    let mask = 1;
    while (mask < n) {
        mask = (mask << 1) | 1;
    }
    return n ^ mask;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function bitwiseComplement(n: number): number {
    if (n === 0) return 1;
    let mask = 1;
    while (mask < n) {
        mask = (mask << 1) | 1;
    }
    return n ^ mask;
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
    function bitwiseComplement($n) {
        if ($n === 0) return 1;
        $mask = 1;
        while ($mask < $n) {
            $mask = ($mask << 1) | 1;
        }
        return $n ^ $mask;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func bitwiseComplement(_ n: Int) -> Int {
        if n == 0 { return 1 }
        var mask = 1
        while mask < n {
            mask = (mask << 1) | 1
        }
        return n ^ mask
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun bitwiseComplement(n: Int): Int {
        if (n == 0) return 1
        var mask = 1
        while (mask < n) {
            mask = (mask shl 1) or 1
        }
        return n xor mask
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int bitwiseComplement(int n) {
    if (n == 0) return 1;
    int mask = 1;
    while (mask < n) {
      mask = (mask << 1) | 1;
    }
    return n ^ mask;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func bitwiseComplement(n int) int {
    if n == 0 {
        return 1
    }
    mask := 1
    for mask < n {
        mask = (mask << 1) | 1
    }
    return n ^ mask
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @return {Integer}
def bitwise_complement(n)
  mask = 1
  while mask < n
    mask = (mask << 1) | 1
  end
  n ^ mask
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def bitwiseComplement(n: Int): Int = {
        var mask = 1
        while (mask < n) {
            mask = (mask << 1) | 1
        }
        n ^ mask
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn bitwise_complement(n: i32) -> i32 {
        let mut mask = 1;
        while mask < n {
            mask = (mask << 1) | 1;
        }
        n ^ mask
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (bitwise-complement n)
  (-> exact-integer? exact-integer?)
  (let loop ([mask 1])
    (if (< mask n)
        (loop (bitwise-ior (arithmetic-shift mask 1) 1))
        (bitwise-xor n mask))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec bitwise_complement(N :: integer()) -> integer().
bitwise_complement(N) ->
  find_mask(1, N) bxor N.

find_mask(Mask, N) when Mask < N ->
  find_mask((Mask bsl 1) bor 1, N);
find_mask(Mask, _) ->
  Mask.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec bitwise_complement(n :: integer) :: integer
  def bitwise_complement(n) do
    do_complement(1, n)
  end

  defp do_complement(mask, n) when mask < n do
    do_complement(Bitwise.bor(Bitwise.bsl(mask, 1), 1), n)
  end

  defp do_complement(mask, n) do
    Bitwise.bxor(n, mask)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(log n) as the algorithm performs a number of iterations proportional to the number of bits in the integer n. Since $n < 10^9$, this is at most 30 iterations.
- **Space Complexity:** O(1) because the algorithm only uses a constant amount of extra space for the bitmask variable, regardless of the input size.
