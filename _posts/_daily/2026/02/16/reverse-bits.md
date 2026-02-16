---
layout: post
title: "Reverse Bits"
date: 2026-02-16 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Divide and Conquer", "Bit Manipulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/reverse-bits/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int reverseBits(int n) {\n        unsigned\
        \ int un = (unsigned int)n;\n        unsigned int res = 0;\n        for (int\
        \ i = 0; i < 32; i++) {\n            res = (res << 1) | (un & 1);\n        \
        \    un >>= 1;\n        }\n        return (int)res;\n    }\n};"
      java: "class Solution {\n    public int reverseBits(int n) {\n        int res\
        \ = 0;\n        for (int i = 0; i < 32; i++) {\n            res = (res << 1)\
        \ | (n & 1);\n            n >>>= 1;\n        }\n        return res;\n    }\n\
        }"
      python: "class Solution(object):\n    def reverseBits(self, n):\n        \"\"\"\
        \n        :type n: int\n        :rtype: int\n        \"\"\"\n        res = 0\n\
        \        for _ in range(32):\n            res = (res << 1) | (n & 1)\n     \
        \       n >>= 1\n        return res"
      python3: "class Solution:\n    def reverseBits(self, n: int) -> int:\n       \
        \ res = 0\n        for _ in range(32):\n            res = (res << 1) | (n &\
        \ 1)\n            n >>= 1\n        return res"
      c: "int reverseBits(int n) {\n    unsigned int un = (unsigned int)n;\n    unsigned\
        \ int res = 0;\n    for (int i = 0; i < 32; i++) {\n        res = (res << 1)\
        \ | (un & 1);\n        un >>= 1;\n    }\n    return (int)res;\n}"
      csharp: "public class Solution {\n    public int ReverseBits(int n) {\n      \
        \  uint un = (uint)n;\n        uint res = 0;\n        for (int i = 0; i < 32;\
        \ i++) {\n            res = (res << 1) | (un & 1);\n            un >>= 1;\n\
        \        }\n        return (int)res;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @return {number}\n */\nvar reverseBits\
        \ = function(n) {\n    let res = 0;\n    for (let i = 0; i < 32; i++) {\n  \
        \      res = (res << 1) | (n & 1);\n        n >>>= 1;\n    }\n    return res\
        \ >>> 0;\n};"
      typescript: "function reverseBits(n: number): number {\n    let res = 0;\n   \
        \ for (let i = 0; i < 32; i++) {\n        res = (res << 1) | (n & 1);\n    \
        \    n >>>= 1;\n    }\n    return res >>> 0;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @return Integer\n\
        \     */\n    function reverseBits($n) {\n        $res = 0;\n        for ($i\
        \ = 0; $i < 32; $i++) {\n            $res = ($res << 1) | ($n & 1);\n      \
        \      $n >>= 1;\n        }\n        return $res;\n    }\n}"
      swift: "class Solution {\n    func reverseBits(_ n: Int) -> Int {\n        var\
        \ res = 0\n        var num = n\n        for _ in 0..<32 {\n            res =\
        \ (res << 1) | (num & 1)\n            num >>= 1\n        }\n        return res\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun reverseBits(n: Int): Int {\n        var res\
        \ = 0\n        var num = n\n        for (i in 0 until 32) {\n            res\
        \ = (res shl 1) or (num and 1)\n            num = num ushr 1\n        }\n  \
        \      return res\n    }\n}"
      dart: "class Solution {\n  int reverseBits(int n) {\n    int res = 0;\n    for\
        \ (int i = 0; i < 32; i++) {\n      res = (res << 1) | (n & 1);\n      n >>=\
        \ 1;\n    }\n    return res & 0xFFFFFFFF;\n  }\n}"
      go: "func reverseBits(n int) int {\n    res := 0\n    for i := 0; i < 32; i++\
        \ {\n        res = (res << 1) | (n & 1)\n        n >>= 1\n    }\n    return\
        \ res\n}"
      ruby: "def reverse_bits(n)\n  res = 0\n  32.times do\n    res = (res << 1) | (n\
        \ & 1)\n    n >>= 1\n  end\n  res\nend"
      scala: "object Solution {\n  def reverseBits(n: Int): Int = {\n    var res = 0\n\
        \    var curr = n\n    for (_ <- 0 until 32) {\n      res = (res << 1) | (curr\
        \ & 1)\n      curr >>>= 1\n    }\n    res\n  }\n}"
      rust: "impl Solution {\n  pub fn reverse_bits(n: i32) -> i32 {\n    n.reverse_bits()\n\
        \  }\n}"
      racket: "(define/contract (reverse-bits n)\n  (-> exact-integer? exact-integer?)\n\
        \  (for/fold ([res 0]\n             [curr n]\n             #:result res)\n \
        \           ([i (in-range 32)])\n    (values (bitwise-ior (arithmetic-shift\
        \ res 1) (bitwise-and curr 1))\n            (arithmetic-shift curr -1))))"
      erlang: "-spec reverse_bits(N :: integer()) -> integer().\nreverse_bits(N) ->\n\
        \  reverse_bits_helper(N, 0, 32).\n\nreverse_bits_helper(_N, Res, 0) ->\n  Res;\n\
        reverse_bits_helper(N, Res, Count) ->\n  reverse_bits_helper(N bsr 1, (Res bsl\
        \ 1) bor (N band 1), Count - 1)."
      elixir: "defmodule Solution do\n  use Bitwise\n  @spec reverse_bits(n :: integer)\
        \ :: integer\n  def reverse_bits(n) do\n    {res, _} = Enum.reduce(0..31, {0,\
        \ n}, fn _, {res, curr} ->\n      {(res <<< 1) ||| (curr &&& 1), curr >>> 1}\n\
        \    end)\n    res\n  end\nend"
    approach: 'The algorithm reverses the bits of a 32-bit integer by iterating through
      all 32 bit positions from the least significant bit to the most significant bit.
      In each iteration, we shift our result variable to the left by one position to
      make room for the next bit. We then extract the current rightmost bit of the input
      number using a bitwise AND operation with 1 and combine it with the result using
      a bitwise OR operation. This effectively places the extracted bit at the new rightmost
      position of the result.


      To process the next bit, the input integer is shifted to the right in each step.
      For languages where integers are signed, it is crucial to use a logical right
      shift to ensure that zeros are filled in from the left rather than preserving
      the sign bit. After 32 such iterations, every bit from the original input has
      been moved to its corresponding mirrored position in the result, effectively reversing
      the bit sequence.'
    time_complexity: O(1). The algorithm always performs exactly 32 iterations, as the
      input is defined as a 32-bit integer. Since the number of operations is fixed
      and does not depend on the input magnitude, the execution time is constant.
    space_complexity: O(1). The solution only requires a few auxiliary variables to
      store the result and the loop counter, which take up a constant amount of memory
      regardless of the input.
    elapsed_time: 189.73777437210083
    model: gemini-3-flash-preview
    generated_at: '2026-02-16 01:28:20 '
---

## Problem #190: Reverse Bits

**Difficulty:** Easy

**Topics:** Divide and Conquer, Bit Manipulation

## Problem Description

<p>Reverse bits of a given 32 bits signed integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 43261596</span></p>

<p><strong>Output:</strong> <span class="example-io">964176192</span></p>

<p><strong>Explanation:</strong></p>

<table>
	<tbody>
		<tr>
			<th>Integer</th>
			<th>Binary</th>
		</tr>
		<tr>
			<td>43261596</td>
			<td>00000010100101000001111010011100</td>
		</tr>
		<tr>
			<td>964176192</td>
			<td>00111001011110000010100101000000</td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2147483644</span></p>

<p><strong>Output:</strong> <span class="example-io">1073741822</span></p>

<p><strong>Explanation:</strong></p>

<table>
	<tbody>
		<tr>
			<th>Integer</th>
			<th>Binary</th>
		</tr>
		<tr>
			<td>2147483644</td>
			<td>01111111111111111111111111111100</td>
		</tr>
		<tr>
			<td>1073741822</td>
			<td>00111111111111111111111111111110</td>
		</tr>
	</tbody>
</table>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 2<sup>31</sup> - 2</code></li>
	<li><code>n</code> is even.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> If this function is called many times, how would you optimize it?</p>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm reverses the bits of a 32-bit integer by iterating through all 32 bit positions from the least significant bit to the most significant bit. In each iteration, we shift our result variable to the left by one position to make room for the next bit. We then extract the current rightmost bit of the input number using a bitwise AND operation with 1 and combine it with the result using a bitwise OR operation. This effectively places the extracted bit at the new rightmost position of the result.

To process the next bit, the input integer is shifted to the right in each step. For languages where integers are signed, it is crucial to use a logical right shift to ensure that zeros are filled in from the left rather than preserving the sign bit. After 32 such iterations, every bit from the original input has been moved to its corresponding mirrored position in the result, effectively reversing the bit sequence.

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
    int reverseBits(int n) {
        unsigned int un = (unsigned int)n;
        unsigned int res = 0;
        for (int i = 0; i < 32; i++) {
            res = (res << 1) | (un & 1);
            un >>= 1;
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
    public int reverseBits(int n) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            res = (res << 1) | (n & 1);
            n >>>= 1;
        }
        return res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int reverseBits(int n) {
    unsigned int un = (unsigned int)n;
    unsigned int res = 0;
    for (int i = 0; i < 32; i++) {
        res = (res << 1) | (un & 1);
        un >>= 1;
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
    public int ReverseBits(int n) {
        uint un = (uint)n;
        uint res = 0;
        for (int i = 0; i < 32; i++) {
            res = (res << 1) | (un & 1);
            un >>= 1;
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
var reverseBits = function(n) {
    let res = 0;
    for (let i = 0; i < 32; i++) {
        res = (res << 1) | (n & 1);
        n >>>= 1;
    }
    return res >>> 0;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function reverseBits(n: number): number {
    let res = 0;
    for (let i = 0; i < 32; i++) {
        res = (res << 1) | (n & 1);
        n >>>= 1;
    }
    return res >>> 0;
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
    function reverseBits($n) {
        $res = 0;
        for ($i = 0; $i < 32; $i++) {
            $res = ($res << 1) | ($n & 1);
            $n >>= 1;
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
    func reverseBits(_ n: Int) -> Int {
        var res = 0
        var num = n
        for _ in 0..<32 {
            res = (res << 1) | (num & 1)
            num >>= 1
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
    fun reverseBits(n: Int): Int {
        var res = 0
        var num = n
        for (i in 0 until 32) {
            res = (res shl 1) or (num and 1)
            num = num ushr 1
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int reverseBits(int n) {
    int res = 0;
    for (int i = 0; i < 32; i++) {
      res = (res << 1) | (n & 1);
      n >>= 1;
    }
    return res & 0xFFFFFFFF;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func reverseBits(n int) int {
    res := 0
    for i := 0; i < 32; i++ {
        res = (res << 1) | (n & 1)
        n >>= 1
    }
    return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def reverse_bits(n)
  res = 0
  32.times do
    res = (res << 1) | (n & 1)
    n >>= 1
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
  def reverseBits(n: Int): Int = {
    var res = 0
    var curr = n
    for (_ <- 0 until 32) {
      res = (res << 1) | (curr & 1)
      curr >>>= 1
    }
    res
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
  pub fn reverse_bits(n: i32) -> i32 {
    n.reverse_bits()
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (reverse-bits n)
  (-> exact-integer? exact-integer?)
  (for/fold ([res 0]
             [curr n]
             #:result res)
            ([i (in-range 32)])
    (values (bitwise-ior (arithmetic-shift res 1) (bitwise-and curr 1))
            (arithmetic-shift curr -1))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec reverse_bits(N :: integer()) -> integer().
reverse_bits(N) ->
  reverse_bits_helper(N, 0, 32).

reverse_bits_helper(_N, Res, 0) ->
  Res;
reverse_bits_helper(N, Res, Count) ->
  reverse_bits_helper(N bsr 1, (Res bsl 1) bor (N band 1), Count - 1).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  use Bitwise
  @spec reverse_bits(n :: integer) :: integer
  def reverse_bits(n) do
    {res, _} = Enum.reduce(0..31, {0, n}, fn _, {res, curr} ->
      {(res <<< 1) ||| (curr &&& 1), curr >>> 1}
    end)
    res
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(1). The algorithm always performs exactly 32 iterations, as the input is defined as a 32-bit integer. Since the number of operations is fixed and does not depend on the input magnitude, the execution time is constant.
- **Space Complexity:** O(1). The solution only requires a few auxiliary variables to store the result and the loop counter, which take up a constant amount of memory regardless of the input.
