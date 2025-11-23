---
layout: post
title: "Minimum One Bit Operations to Make Integers Zero"
date: 2025-11-08 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Dynamic Programming", "Bit Manipulation", "Memoization"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/
---

## Problem #1611: Minimum One Bit Operations to Make Integers Zero

**Difficulty:** Hard

**Topics:** Dynamic Programming, Bit Manipulation, Memoization

## Problem Description

<p>Given an integer <code>n</code>, you must transform it into <code>0</code> using the following operations any number of times:</p>

<ul>
	<li>Change the rightmost (<code>0<sup>th</sup></code>) bit in the binary representation of <code>n</code>.</li>
	<li>Change the <code>i<sup>th</sup></code> bit in the binary representation of <code>n</code> if the <code>(i-1)<sup>th</sup></code> bit is set to <code>1</code> and the <code>(i-2)<sup>th</sup></code> through <code>0<sup>th</sup></code> bits are set to <code>0</code>.</li>
</ul>

<p>Return <em>the minimum number of operations to transform </em><code>n</code><em> into </em><code>0</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> The binary representation of 3 is &quot;11&quot;.
&quot;<u>1</u>1&quot; -&gt; &quot;<u>0</u>1&quot; with the 2<sup>nd</sup> operation since the 0<sup>th</sup> bit is 1.
&quot;0<u>1</u>&quot; -&gt; &quot;0<u>0</u>&quot; with the 1<sup>st</sup> operation.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> 4
<strong>Explanation:</strong> The binary representation of 6 is &quot;110&quot;.
&quot;<u>1</u>10&quot; -&gt; &quot;<u>0</u>10&quot; with the 2<sup>nd</sup> operation since the 1<sup>st</sup> bit is 1 and 0<sup>th</sup> through 0<sup>th</sup> bits are 0.
&quot;01<u>0</u>&quot; -&gt; &quot;01<u>1</u>&quot; with the 1<sup>st</sup> operation.
&quot;0<u>1</u>1&quot; -&gt; &quot;0<u>0</u>1&quot; with the 2<sup>nd</sup> operation since the 0<sup>th</sup> bit is 1.
&quot;00<u>1</u>&quot; -&gt; &quot;00<u>0</u>&quot; with the 1<sup>st</sup> operation.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. The fastest way to convert n to zero is to remove all set bits starting from the leftmost one. Try some simple examples to learn the rule of how many steps are needed to remove one set bit.

2. consider n=2^k case first, then solve for all n.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-23 00:02:17 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The given operations define transitions between numbers in a reflected binary Gray code sequence. The problem asks for the minimum operations to transform 'n' to '0', which is equivalent to finding the index 'k' such that 'n' is the 'k'-th Gray code number (starting from '0'). This 'k' is computed by the inverse Gray code mapping: B(n) = n ^ (n >> 1) ^ (n >> 2) ^ ...

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-cpp-gemini-2-5-flash" checked>
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-java-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python3-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-c-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-csharp-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-javascript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-typescript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-php-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-swift-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-kotlin-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-dart-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-go-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-ruby-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-scala-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-rust-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-racket-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-erlang-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-elixir-gemini-2-5-flash">
  <div class="tab-labels">
    <label for="lang-cpp-gemini-2-5-flash">C++</label>
    <label for="lang-java-gemini-2-5-flash">Java</label>
    <label for="lang-python-gemini-2-5-flash">Python</label>
    <label for="lang-python3-gemini-2-5-flash">Python3</label>
    <label for="lang-c-gemini-2-5-flash">C</label>
    <label for="lang-csharp-gemini-2-5-flash">C#</label>
    <label for="lang-javascript-gemini-2-5-flash">JavaScript</label>
    <label for="lang-typescript-gemini-2-5-flash">TypeScript</label>
    <label for="lang-php-gemini-2-5-flash">PHP</label>
    <label for="lang-swift-gemini-2-5-flash">Swift</label>
    <label for="lang-kotlin-gemini-2-5-flash">Kotlin</label>
    <label for="lang-dart-gemini-2-5-flash">Dart</label>
    <label for="lang-go-gemini-2-5-flash">Go</label>
    <label for="lang-ruby-gemini-2-5-flash">Ruby</label>
    <label for="lang-scala-gemini-2-5-flash">Scala</label>
    <label for="lang-rust-gemini-2-5-flash">Rust</label>
    <label for="lang-racket-gemini-2-5-flash">Racket</label>
    <label for="lang-erlang-gemini-2-5-flash">Erlang</label>
    <label for="lang-elixir-gemini-2-5-flash">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    int minimumOneBitOperations(int n) {
        int res = n;
        n >>= 1;
        while (n > 0) {
            res ^= n;
            n >>= 1;
        }
        return res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minimumOneBitOperations(int n) {
        int res = n;
        n >>= 1;
        while (n > 0) {
            res ^= n;
            n >>= 1;
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
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = n
        n >>= 1
        while n > 0:
            res ^= n
            n >>= 1
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = n
        n >>= 1
        while n > 0:
            res ^= n
            n >>= 1
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>

int minimumOneBitOperations(int n) {
    int res = n;
    n >>= 1;
    while (n > 0) {
        res ^= n;
        n >>= 1;
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinimumOneBitOperations(int n) {
        int res = n;
        n >>= 1;
        while (n > 0) {
            res ^= n;
            n >>= 1;
        }
        return res;
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
var minimumOneBitOperations = function(n) {
    let res = n;
    n >>= 1;
    while (n > 0) {
        res ^= n;
        n >>= 1;
    }
    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumOneBitOperations(n: number): number {
    let res = n;
    n >>= 1;
    while (n > 0) {
        res ^= n;
        n >>= 1;
    }
    return res;
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
    function minimumOneBitOperations($n) {
        $res = $n;
        $n >>= 1;
        while ($n > 0) {
            $res ^= $n;
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
    func minimumOneBitOperations(_ n: Int) -> Int {
        var res = n
        var currentN = n >> 1
        while currentN > 0 {
            res ^= currentN
            currentN >>= 1
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
    fun minimumOneBitOperations(n: Int): Int {
        var res = n
        var currentN = n shr 1
        while (currentN > 0) {
            res = res xor currentN
            currentN = currentN shr 1
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
  int minimumOneBitOperations(int n) {
    int res = n;
    n >>= 1;
    while (n > 0) {
      res ^= n;
      n >>= 1;
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
func minimumOneBitOperations(n int) int {
    res := n
    n >>= 1
    for n > 0 {
        res ^= n
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
def minimum_one_bit_operations(n)
    res = n
    n >>= 1
    while n > 0
        res ^= n
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
    def minimumOneBitOperations(n: Int): Int = {
        var res = n
        var currentN = n >>> 1
        while (currentN > 0) {
            res ^= currentN
            currentN >>>= 1
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
    pub fn minimum_one_bit_operations(n: i32) -> i32 {
        let mut res = n;
        let mut current_n = n >> 1;
        while current_n > 0 {
            res ^= current_n;
            current_n >>= 1;
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
(define/contract (minimum-one-bit-operations n)
  (-> exact-integer? exact-integer?)
  (let loop ((current-n (arithmetic-shift n -1)) (res n))
    (if (> current-n 0)
        (loop (arithmetic-shift current-n -1) (bitwise-xor res current-n))
        res)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_one_bit_operations(N :: integer()) -> integer().
minimum_one_bit_operations(N) ->
    minimum_one_bit_operations_impl(N bsr 1, N).

minimum_one_bit_operations_impl(0, Res) -> Res;
minimum_one_bit_operations_impl(CurrentN, Res) ->
    minimum_one_bit_operations_impl(CurrentN bsr 1, Res bxor CurrentN).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_one_bit_operations(n :: integer) :: integer
  def minimum_one_bit_operations(n) do
    do_minimum_one_bit_operations(n >>> 1, n)
  end

  defp do_minimum_one_bit_operations(0, res), do: res
  defp do_minimum_one_bit_operations(current_n, res) do
    do_minimum_one_bit_operations(current_n >>> 1, res ^ current_n)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(log n)

- **Space Complexity:** O(1)

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-23 00:02:17 )</small>
</summary>

<div class="ai-solution-content">

### Approach

No approach provided

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-cpp-llama-3-3-70b-versatile" checked>
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-java-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python3-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-c-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-csharp-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-javascript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-typescript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-php-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-swift-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-kotlin-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-dart-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-go-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-ruby-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-scala-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-rust-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-racket-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-erlang-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-elixir-llama-3-3-70b-versatile">
  <div class="tab-labels">
    <label for="lang-cpp-llama-3-3-70b-versatile">C++</label>
    <label for="lang-java-llama-3-3-70b-versatile">Java</label>
    <label for="lang-python-llama-3-3-70b-versatile">Python</label>
    <label for="lang-python3-llama-3-3-70b-versatile">Python3</label>
    <label for="lang-c-llama-3-3-70b-versatile">C</label>
    <label for="lang-csharp-llama-3-3-70b-versatile">C#</label>
    <label for="lang-javascript-llama-3-3-70b-versatile">JavaScript</label>
    <label for="lang-typescript-llama-3-3-70b-versatile">TypeScript</label>
    <label for="lang-php-llama-3-3-70b-versatile">PHP</label>
    <label for="lang-swift-llama-3-3-70b-versatile">Swift</label>
    <label for="lang-kotlin-llama-3-3-70b-versatile">Kotlin</label>
    <label for="lang-dart-llama-3-3-70b-versatile">Dart</label>
    <label for="lang-go-llama-3-3-70b-versatile">Go</label>
    <label for="lang-ruby-llama-3-3-70b-versatile">Ruby</label>
    <label for="lang-scala-llama-3-3-70b-versatile">Scala</label>
    <label for="lang-rust-llama-3-3-70b-versatile">Rust</label>
    <label for="lang-racket-llama-3-3-70b-versatile">Racket</label>
    <label for="lang-erlang-llama-3-3-70b-versatile">Erlang</label>
    <label for="lang-elixir-llama-3-3-70b-versatile">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
// Generation failed for C++
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Generation failed for C#
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Generation failed for JavaScript
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
// Generation failed for TypeScript
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
// Generation failed for PHP
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
// Generation failed for Swift
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
// Generation failed for Kotlin
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
// Generation failed for Dart
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
// Generation failed for Go
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
// Generation failed for Ruby
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
// Generation failed for Scala
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
// Generation failed for Rust
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
// Generation failed for Racket
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
// Generation failed for Erlang
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
// Generation failed for Elixir
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** N/A

- **Space Complexity:** N/A

</div>
</details>
