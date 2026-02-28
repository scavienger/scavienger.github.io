---
layout: post
title: "Concatenation of Consecutive Binary Numbers"
date: 2026-02-28 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Math", "Bit Manipulation", "Simulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int concatenatedBinary(int n) {\n       \
        \ long long res = 0;\n        int MOD = 1000000007;\n        int length = 0;\n\
        \        for (int i = 1; i <= n; ++i) {\n            if ((i & (i - 1)) == 0)\
        \ {\n                length++;\n            }\n            res = ((res << length)\
        \ | i) % MOD;\n        }\n        return (int)res;\n    }\n};"
      java: "class Solution {\n    public int concatenatedBinary(int n) {\n        long\
        \ res = 0;\n        int MOD = 1000000007;\n        int length = 0;\n       \
        \ for (int i = 1; i <= n; i++) {\n            if ((i & (i - 1)) == 0) {\n  \
        \              length++;\n            }\n            res = ((res << length)\
        \ | i) % MOD;\n        }\n        return (int) res;\n    }\n}"
      python: "class Solution(object):\n    def concatenatedBinary(self, n):\n     \
        \   \"\"\"\n        :type n: int\n        :rtype: int\n        \"\"\"\n    \
        \    res = 0\n        MOD = 10**9 + 7\n        length = 0\n        for i in\
        \ xrange(1, n + 1):\n            if i & (i - 1) == 0:\n                length\
        \ += 1\n            res = ((res << length) | i) % MOD\n        return res"
      python3: "class Solution:\n    def concatenatedBinary(self, n: int) -> int:\n\
        \        res = 0\n        MOD = 10**9 + 7\n        length = 0\n        for i\
        \ in range(1, n + 1):\n            if i & (i - 1) == 0:\n                length\
        \ += 1\n            res = ((res << length) | i) % MOD\n        return res"
      c: "int concatenatedBinary(int n){\n    long long res = 0;\n    int MOD = 1000000007;\n\
        \    int length = 0;\n    for (int i = 1; i <= n; i++) {\n        if ((i & (i\
        \ - 1)) == 0) {\n            length++;\n        }\n        res = ((res << length)\
        \ | i) % MOD;\n    }\n    return (int)res;\n}"
      csharp: "public class Solution {\n    public int ConcatenatedBinary(int n) {\n\
        \        long res = 0;\n        int MOD = 1000000007;\n        int length =\
        \ 0;\n        for (int i = 1; i <= n; i++) {\n            if ((i & (i - 1))\
        \ == 0) {\n                length++;\n            }\n            res = ((res\
        \ << length) | (long)i) % MOD;\n        }\n        return (int)res;\n    }\n\
        }"
      javascript: "/**\n * @param {number} n\n * @return {number}\n */\nvar concatenatedBinary\
        \ = function(n) {\n    let res = BigInt(0);\n    const MOD = BigInt(1000000007);\n\
        \    let length = 0;\n    for (let i = 1; i <= n; i++) {\n        if ((i & (i\
        \ - 1)) === 0) {\n            length++;\n        }\n        res = ((res << BigInt(length))\
        \ | BigInt(i)) % MOD;\n    }\n    return Number(res);\n};"
      typescript: "function concatenatedBinary(n: number): number {\n  const MOD = BigInt(1000000007);\n\
        \  let res = BigInt(0);\n  let bitLength = 0;\n  for (let i = 1; i <= n; i++)\
        \ {\n    if ((i & (i - 1)) === 0) {\n      bitLength++;\n    }\n    res = ((res\
        \ << BigInt(bitLength)) + BigInt(i)) % MOD;\n  }\n  return Number(res);\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @return Integer\n\
        \     */\n    function concatenatedBinary($n) {\n        $MOD = 1000000007;\n\
        \        $res = 0;\n        $bitLength = 0;\n        for ($i = 1; $i <= $n;\
        \ $i++) {\n            if (($i & ($i - 1)) == 0) {\n                $bitLength++;\n\
        \            }\n            $res = (($res << $bitLength) + $i) % $MOD;\n   \
        \     }\n        return $res;\n    }\n}"
      swift: "class Solution {\n    func concatenatedBinary(_ n: Int) -> Int {\n   \
        \     let mod = 1_000_000_007\n        var res = 0\n        var bitLength =\
        \ 0\n        for i in 1...n {\n            if (i & (i - 1)) == 0 {\n       \
        \         bitLength += 1\n            }\n            res = ((res << bitLength)\
        \ + i) % mod\n        }\n        return res\n    }\n}"
      kotlin: "class Solution {\n    fun concatenatedBinary(n: Int): Int {\n       \
        \ val mod: Long = 1000000007\n        var res: Long = 0\n        var bitLength\
        \ = 0\n        for (i in 1..n) {\n            if ((i and (i - 1)) == 0) {\n\
        \                bitLength++\n            }\n            res = ((res shl bitLength)\
        \ + i.toLong()) % mod\n        }\n        return res.toInt()\n    }\n}"
      dart: "class Solution {\n  int concatenatedBinary(int n) {\n    int mod = 1000000007;\n\
        \    int res = 0;\n    int bitLength = 0;\n    for (int i = 1; i <= n; i++)\
        \ {\n      if ((i & (i - 1)) == 0) {\n        bitLength++;\n      }\n      res\
        \ = ((res << bitLength) + i) % mod;\n    }\n    return res;\n  }\n}"
      go: "func concatenatedBinary(n int) int {\n\tconst mod int64 = 1000000007\n\t\
        var res int64 = 0\n\tbitLength := 0\n\tfor i := 1; i <= n; i++ {\n\t\tif i&(i-1)\
        \ == 0 {\n\t\t\tbitLength++\n\t\t}\n\t\tres = ((res << bitLength) + int64(i))\
        \ % mod\n\t}\n\treturn int(res)\n}"
      ruby: "# @param {Integer} n\n# @return {Integer}\ndef concatenated_binary(n)\n\
        \  res = 0\n  len = 0\n  mod = 1_000_000_007\n  (1..n).each do |i|\n    len\
        \ += 1 if (i & (i - 1)) == 0\n    res = ((res << len) + i) % mod\n  end\n  res\n\
        end"
      scala: "object Solution {\n    def concatenatedBinary(n: Int): Int = {\n     \
        \   var res: Long = 0L\n        var len = 0\n        val mod = 1000000007\n\
        \        var i = 1\n        while (i <= n) {\n            if ((i & (i - 1))\
        \ == 0) len += 1\n            res = ((res << len) + i) % mod\n            i\
        \ += 1\n        }\n        res.toInt\n    }\n}"
      rust: "impl Solution {\n    pub fn concatenated_binary(n: i32) -> i32 {\n    \
        \    let mut res: i64 = 0;\n        let mut len: u32 = 0;\n        let mod_val:\
        \ i64 = 1_000_000_007;\n        for i in 1..=n {\n            if (i & (i - 1))\
        \ == 0 {\n                len += 1;\n            }\n            res = ((res\
        \ << len) + i as i64) % mod_val;\n        }\n        res as i32\n    }\n}"
      racket: "(define/contract (concatenated-binary n)\n  (-> exact-integer? exact-integer?)\n\
        \  (define MOD 1000000007)\n  (let loop ([i 1] [res 0] [len 0])\n    (if (>\
        \ i n)\n        res\n        (let* ([new-len (if (zero? (bitwise-and i (- i\
        \ 1))) (+ len 1) len)]\n               [new-res (modulo (+ (arithmetic-shift\
        \ res new-len) i) MOD)])\n          (loop (+ i 1) new-res new-len)))))"
      erlang: "-spec concatenated_binary(N :: integer()) -> integer().\nconcatenated_binary(N)\
        \ ->\n    concatenated_binary(1, N, 0, 0).\n\nconcatenated_binary(I, N, Res,\
        \ Len) when I > N ->\n    Res;\nconcatenated_binary(I, N, Res, Len) ->\n   \
        \ NewLen = case (I band (I - 1)) of\n        0 -> Len + 1;\n        _ -> Len\n\
        \    end,\n    NewRes = ((Res bsl NewLen) + I) rem 1000000007,\n    concatenated_binary(I\
        \ + 1, N, NewRes, NewLen)."
      elixir: "defmodule Solution do\n  import Bitwise\n  @spec concatenated_binary(n\
        \ :: integer) :: integer\n  def concatenated_binary(n) do\n    mod = 1_000_000_007\n\
        \    {res, _} = Enum.reduce(1..n, {0, 0}, fn i, {res, len} ->\n      new_len\
        \ = if (i &&& (i - 1)) == 0, do: len + 1, else: len\n      new_res = rem((res\
        \ <<< new_len) + i, mod)\n      {new_res, new_len}\n    end)\n    res\n  end\n\
        end"
    approach: 'To calculate the decimal value of the concatenated binary representations,
      we iterate through each number $i$ from 1 to $n$ and maintain a cumulative result.
      For each $i$, we shift the current cumulative result to the left by the number
      of bits required to represent $i$ and then add $i$ to the result using a bitwise
      OR operation. The modulo operation $10^9 + 7$ is applied at each step to keep
      the intermediate decimal value manageable and prevent numeric overflow.


      The bit length of the current number $i$ increases by one every time $i$ reaches
      a new power of 2 (i.e., 1, 2, 4, 8, etc.). We can efficiently detect these transition
      points using the bitwise expression $(i \text{ AND } (i - 1)) == 0$. This allows
      us to update the bit length counter in constant time throughout the loop, ensuring
      that the concatenation process accurately simulates appending the binary string
      of each number to the end of the total string.'
    time_complexity: O(n) because we iterate through the integers from 1 up to $n$ exactly
      once. In each iteration, we perform a few bitwise operations and a modulo operation,
      all of which take constant time for standard word-sized integers.
    space_complexity: O(1) because we only need a few variables to store the intermediate
      result and the current bit length. No additional data structures proportional
      to the size of $n$ are required.
    elapsed_time: 209.1889307498932
    model: gemini-3-flash-preview
    generated_at: '2026-02-28 01:18:13 '
---

## Problem #1680: Concatenation of Consecutive Binary Numbers

**Difficulty:** Medium

**Topics:** Math, Bit Manipulation, Simulation

## Problem Description

<p>Given an integer <code>n</code>, return <em>the <strong>decimal value</strong> of the binary string formed by concatenating the binary representations of </em><code>1</code><em> to </em><code>n</code><em> in order, <strong>modulo </strong></em><code>10<sup>9 </sup>+ 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
<strong>Explanation: </strong>&quot;1&quot; in binary corresponds to the decimal value 1. 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 27
<strong>Explanation: </strong>In binary, 1, 2, and 3 corresponds to &quot;1&quot;, &quot;10&quot;, and &quot;11&quot;.
After concatenating them, we have &quot;11011&quot;, which corresponds to the decimal value 27.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 12
<strong>Output:</strong> 505379714
<strong>Explanation</strong>: The concatenation results in &quot;1101110010111011110001001101010111100&quot;.
The decimal value of that is 118505380540.
After modulo 10<sup>9</sup> + 7, the result is 505379714.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Express the nth number value in a recursion formula and think about how we can do a fast evaluation.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To calculate the decimal value of the concatenated binary representations, we iterate through each number $i$ from 1 to $n$ and maintain a cumulative result. For each $i$, we shift the current cumulative result to the left by the number of bits required to represent $i$ and then add $i$ to the result using a bitwise OR operation. The modulo operation $10^9 + 7$ is applied at each step to keep the intermediate decimal value manageable and prevent numeric overflow.

The bit length of the current number $i$ increases by one every time $i$ reaches a new power of 2 (i.e., 1, 2, 4, 8, etc.). We can efficiently detect these transition points using the bitwise expression $(i \text{ AND } (i - 1)) == 0$. This allows us to update the bit length counter in constant time throughout the loop, ensuring that the concatenation process accurately simulates appending the binary string of each number to the end of the total string.

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
    int concatenatedBinary(int n) {
        long long res = 0;
        int MOD = 1000000007;
        int length = 0;
        for (int i = 1; i <= n; ++i) {
            if ((i & (i - 1)) == 0) {
                length++;
            }
            res = ((res << length) | i) % MOD;
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
    public int concatenatedBinary(int n) {
        long res = 0;
        int MOD = 1000000007;
        int length = 0;
        for (int i = 1; i <= n; i++) {
            if ((i & (i - 1)) == 0) {
                length++;
            }
            res = ((res << length) | i) % MOD;
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
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        MOD = 10**9 + 7
        length = 0
        for i in xrange(1, n + 1):
            if i & (i - 1) == 0:
                length += 1
            res = ((res << length) | i) % MOD
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = 0
        MOD = 10**9 + 7
        length = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                length += 1
            res = ((res << length) | i) % MOD
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int concatenatedBinary(int n){
    long long res = 0;
    int MOD = 1000000007;
    int length = 0;
    for (int i = 1; i <= n; i++) {
        if ((i & (i - 1)) == 0) {
            length++;
        }
        res = ((res << length) | i) % MOD;
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
    public int ConcatenatedBinary(int n) {
        long res = 0;
        int MOD = 1000000007;
        int length = 0;
        for (int i = 1; i <= n; i++) {
            if ((i & (i - 1)) == 0) {
                length++;
            }
            res = ((res << length) | (long)i) % MOD;
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
var concatenatedBinary = function(n) {
    let res = BigInt(0);
    const MOD = BigInt(1000000007);
    let length = 0;
    for (let i = 1; i <= n; i++) {
        if ((i & (i - 1)) === 0) {
            length++;
        }
        res = ((res << BigInt(length)) | BigInt(i)) % MOD;
    }
    return Number(res);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function concatenatedBinary(n: number): number {
  const MOD = BigInt(1000000007);
  let res = BigInt(0);
  let bitLength = 0;
  for (let i = 1; i <= n; i++) {
    if ((i & (i - 1)) === 0) {
      bitLength++;
    }
    res = ((res << BigInt(bitLength)) + BigInt(i)) % MOD;
  }
  return Number(res);
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
    function concatenatedBinary($n) {
        $MOD = 1000000007;
        $res = 0;
        $bitLength = 0;
        for ($i = 1; $i <= $n; $i++) {
            if (($i & ($i - 1)) == 0) {
                $bitLength++;
            }
            $res = (($res << $bitLength) + $i) % $MOD;
        }
        return $res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func concatenatedBinary(_ n: Int) -> Int {
        let mod = 1_000_000_007
        var res = 0
        var bitLength = 0
        for i in 1...n {
            if (i & (i - 1)) == 0 {
                bitLength += 1
            }
            res = ((res << bitLength) + i) % mod
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun concatenatedBinary(n: Int): Int {
        val mod: Long = 1000000007
        var res: Long = 0
        var bitLength = 0
        for (i in 1..n) {
            if ((i and (i - 1)) == 0) {
                bitLength++
            }
            res = ((res shl bitLength) + i.toLong()) % mod
        }
        return res.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int concatenatedBinary(int n) {
    int mod = 1000000007;
    int res = 0;
    int bitLength = 0;
    for (int i = 1; i <= n; i++) {
      if ((i & (i - 1)) == 0) {
        bitLength++;
      }
      res = ((res << bitLength) + i) % mod;
    }
    return res;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func concatenatedBinary(n int) int {
	const mod int64 = 1000000007
	var res int64 = 0
	bitLength := 0
	for i := 1; i <= n; i++ {
		if i&(i-1) == 0 {
			bitLength++
		}
		res = ((res << bitLength) + int64(i)) % mod
	}
	return int(res)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @return {Integer}
def concatenated_binary(n)
  res = 0
  len = 0
  mod = 1_000_000_007
  (1..n).each do |i|
    len += 1 if (i & (i - 1)) == 0
    res = ((res << len) + i) % mod
  end
  res
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def concatenatedBinary(n: Int): Int = {
        var res: Long = 0L
        var len = 0
        val mod = 1000000007
        var i = 1
        while (i <= n) {
            if ((i & (i - 1)) == 0) len += 1
            res = ((res << len) + i) % mod
            i += 1
        }
        res.toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn concatenated_binary(n: i32) -> i32 {
        let mut res: i64 = 0;
        let mut len: u32 = 0;
        let mod_val: i64 = 1_000_000_007;
        for i in 1..=n {
            if (i & (i - 1)) == 0 {
                len += 1;
            }
            res = ((res << len) + i as i64) % mod_val;
        }
        res as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (concatenated-binary n)
  (-> exact-integer? exact-integer?)
  (define MOD 1000000007)
  (let loop ([i 1] [res 0] [len 0])
    (if (> i n)
        res
        (let* ([new-len (if (zero? (bitwise-and i (- i 1))) (+ len 1) len)]
               [new-res (modulo (+ (arithmetic-shift res new-len) i) MOD)])
          (loop (+ i 1) new-res new-len)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec concatenated_binary(N :: integer()) -> integer().
concatenated_binary(N) ->
    concatenated_binary(1, N, 0, 0).

concatenated_binary(I, N, Res, Len) when I > N ->
    Res;
concatenated_binary(I, N, Res, Len) ->
    NewLen = case (I band (I - 1)) of
        0 -> Len + 1;
        _ -> Len
    end,
    NewRes = ((Res bsl NewLen) + I) rem 1000000007,
    concatenated_binary(I + 1, N, NewRes, NewLen).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  import Bitwise
  @spec concatenated_binary(n :: integer) :: integer
  def concatenated_binary(n) do
    mod = 1_000_000_007
    {res, _} = Enum.reduce(1..n, {0, 0}, fn i, {res, len} ->
      new_len = if (i &&& (i - 1)) == 0, do: len + 1, else: len
      new_res = rem((res <<< new_len) + i, mod)
      {new_res, new_len}
    end)
    res
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) because we iterate through the integers from 1 up to $n$ exactly once. In each iteration, we perform a few bitwise operations and a modulo operation, all of which take constant time for standard word-sized integers.
- **Space Complexity:** O(1) because we only need a few variables to store the intermediate result and the current bit length. No additional data structures proportional to the size of $n$ are required.
