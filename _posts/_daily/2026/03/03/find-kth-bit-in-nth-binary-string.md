---
layout: post
title: "Find Kth Bit in Nth Binary String"
date: 2026-03-03 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Recursion", "Simulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    char findKthBit(int n, int k) {\n       \
        \ if (n == 1) return '0';\n        int mid = 1 << (n - 1);\n        if (k ==\
        \ mid) return '1';\n        if (k < mid) return findKthBit(n - 1, k);\n    \
        \    return findKthBit(n - 1, (1 << n) - k) == '0' ? '1' : '0';\n    }\n};"
      java: "class Solution {\n    public char findKthBit(int n, int k) {\n        if\
        \ (n == 1) return '0';\n        int mid = 1 << (n - 1);\n        if (k == mid)\
        \ return '1';\n        if (k < mid) return findKthBit(n - 1, k);\n        return\
        \ findKthBit(n - 1, (1 << n) - k) == '0' ? '1' : '0';\n    }\n}"
      python: "class Solution(object):\n    def findKthBit(self, n, k):\n        \"\"\
        \"\n        :type n: int\n        :type k: int\n        :rtype: str\n      \
        \  \"\"\"\n        if n == 1:\n            return \"0\"\n        mid = 1 <<\
        \ (n - 1)\n        if k == mid:\n            return \"1\"\n        if k < mid:\n\
        \            return self.findKthBit(n - 1, k)\n        res = self.findKthBit(n\
        \ - 1, (1 << n) - k)\n        return \"1\" if res == \"0\" else \"0\""
      python3: "class Solution:\n    def findKthBit(self, n: int, k: int) -> str:\n\
        \        if n == 1:\n            return \"0\"\n        mid = 1 << (n - 1)\n\
        \        if k == mid:\n            return \"1\"\n        if k < mid:\n     \
        \       return self.findKthBit(n - 1, k)\n        res = self.findKthBit(n -\
        \ 1, (1 << n) - k)\n        return \"1\" if res == \"0\" else \"0\""
      c: "char findKthBit(int n, int k) {\n    if (n == 1) return '0';\n    int mid\
        \ = 1 << (n - 1);\n    if (k == mid) return '1';\n    if (k < mid) return findKthBit(n\
        \ - 1, k);\n    return findKthBit(n - 1, (1 << n) - k) == '0' ? '1' : '0';\n\
        }"
      csharp: "public class Solution {\n    public char FindKthBit(int n, int k) {\n\
        \        if (n == 1) return '0';\n        int mid = 1 << (n - 1);\n        if\
        \ (k == mid) return '1';\n        if (k < mid) return FindKthBit(n - 1, k);\n\
        \        return FindKthBit(n - 1, (1 << n) - k) == '0' ? '1' : '0';\n    }\n\
        }"
      javascript: "/**\n * @param {number} n\n * @param {number} k\n * @return {character}\n\
        \ */\nvar findKthBit = function(n, k) {\n    if (n === 1) return \"0\";\n  \
        \  var mid = 1 << (n - 1);\n    if (k === mid) return \"1\";\n    if (k < mid)\
        \ return findKthBit(n - 1, k);\n    return findKthBit(n - 1, (1 << n) - k) ===\
        \ \"0\" ? \"1\" : \"0\";\n};"
      typescript: "function findKthBit(n: number, k: number): string {\n    if (n ===\
        \ 1) return \"0\";\n    const mid = 1 << (n - 1);\n    if (k === mid) return\
        \ \"1\";\n    if (k < mid) return findKthBit(n - 1, k);\n    return findKthBit(n\
        \ - 1, (1 << n) - k) === \"0\" ? \"1\" : \"0\";\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @param Integer\
        \ $k\n     * @return String\n     */\n    function findKthBit($n, $k) {\n  \
        \      if ($n == 1) return \"0\";\n        $mid = 1 << ($n - 1);\n        if\
        \ ($k == $mid) return \"1\";\n        if ($k < $mid) return $this->findKthBit($n\
        \ - 1, $k);\n        return $this->findKthBit($n - 1, (1 << $n) - $k) == \"\
        0\" ? \"1\" : \"0\";\n    }\n}"
      swift: "class Solution {\n    func findKthBit(_ n: Int, _ k: Int) -> Character\
        \ {\n        if n == 1 { return \"0\" }\n        let mid = 1 << (n - 1)\n  \
        \      if k == mid { return \"1\" }\n        if k < mid { return findKthBit(n\
        \ - 1, k) }\n        let bit = findKthBit(n - 1, (1 << n) - k)\n        return\
        \ bit == \"0\" ? \"1\" : \"0\"\n    }\n}"
      kotlin: "class Solution {\n    fun findKthBit(n: Int, k: Int): Char {\n      \
        \  if (n == 1) return '0'\n        val mid = 1 shl (n - 1)\n        return when\
        \ {\n            k == mid -> '1'\n            k < mid -> findKthBit(n - 1, k)\n\
        \            else -> if (findKthBit(n - 1, (1 shl n) - k) == '0') '1' else '0'\n\
        \        }\n    }\n}"
      dart: "class Solution {\n  String findKthBit(int n, int k) {\n    if (n == 1)\
        \ return \"0\";\n    int mid = 1 << (n - 1);\n    if (k == mid) return \"1\"\
        ;\n    if (k < mid) return findKthBit(n - 1, k);\n    return findKthBit(n -\
        \ 1, (1 << n) - k) == \"0\" ? \"1\" : \"0\";\n  }\n}"
      go: "func findKthBit(n int, k int) byte {\n    if n == 1 {\n        return '0'\n\
        \    }\n    mid := 1 << (n - 1)\n    if k == mid {\n        return '1'\n   \
        \ }\n    if k < mid {\n        return findKthBit(n-1, k)\n    }\n    bit :=\
        \ findKthBit(n-1, (1<<n)-k)\n    if bit == '0' {\n        return '1'\n    }\n\
        \    return '0'\n}"
      ruby: "def find_kth_bit(n, k)\n  return \"0\" if n == 1\n  mid = 1 << (n - 1)\n\
        \  return \"1\" if k == mid\n  if k < mid\n    find_kth_bit(n - 1, k)\n  else\n\
        \    res = find_kth_bit(n - 1, 2 * mid - k)\n    res == \"0\" ? \"1\" : \"0\"\
        \n  end\nend"
      scala: "object Solution {\n    def findKthBit(n: Int, k: Int): Char = {\n    \
        \    if (n == 1) return '0'\n        val mid = 1 << (n - 1)\n        if (k ==\
        \ mid) return '1'\n        if (k < mid) return findKthBit(n - 1, k)\n      \
        \  val res = findKthBit(n - 1, 2 * mid - k)\n        if (res == '0') '1' else\
        \ '0'\n    }\n}"
      rust: "impl Solution {\n    pub fn find_kth_bit(n: i32, k: i32) -> char {\n  \
        \      if n == 1 {\n            return '0';\n        }\n        let mid = 1\
        \ << (n - 1);\n        if k == mid {\n            return '1';\n        }\n \
        \       if k < mid {\n            return Self::find_kth_bit(n - 1, k);\n   \
        \     }\n        let res = Self::find_kth_bit(n - 1, 2 * mid - k);\n       \
        \ if res == '0' { '1' } else { '0' }\n    }\n}"
      racket: "(define/contract (find-kth-bit n k)\n  (-> exact-integer? exact-integer?\
        \ char?)\n  (cond\n    [(= n 1) #\\0]\n    [else\n     (let ([mid (expt 2 (-\
        \ n 1))])\n       (cond\n         [(= k mid) #\\1]\n         [(< k mid) (find-kth-bit\
        \ (- n 1) k)]\n         [else (if (char=? (find-kth-bit (- n 1) (- (* 2 mid)\
        \ k)) #\\0) #\\1 #\\0)]))]))"
      erlang: "-spec find_kth_bit(N :: integer(), K :: integer()) -> char().\nfind_kth_bit(N,\
        \ K) ->\n  if\n    N =:= 1 -> $0;\n    true ->\n      Mid = 1 bsl (N - 1),\n\
        \      if\n        K =:= Mid -> $1;\n        K < Mid -> find_kth_bit(N - 1,\
        \ K);\n        true ->\n          case find_kth_bit(N - 1, 2 * Mid - K) of\n\
        \            $0 -> $1;\n            $1 -> $0\n          end\n      end\n  end."
      elixir: "defmodule Solution do\n  @spec find_kth_bit(n :: integer, k :: integer)\
        \ :: char\n  def find_kth_bit(n, k) do\n    if n == 1 do\n      ?0\n    else\n\
        \      mid = round(:math.pow(2, n - 1))\n      cond do\n        k == mid ->\
        \ ?1\n        k < mid -> find_kth_bit(n - 1, k)\n        true ->\n         \
        \ if find_kth_bit(n - 1, 2 * mid - k) == ?0 do\n            ?1\n          else\n\
        \            ?0\n          end\n      end\n    end\n  end\nend"
    approach: 'The binary string sequence $S_n$ is constructed recursively where $S_n$
      consists of $S_{n-1}$, followed by a ''1'', and finally the reversed, inverted
      version of $S_{n-1}$. This structure reveals a middle bit at position $2^{n-1}$
      that is always ''1'' for $n > 1$. By comparing the target index $k$ with this
      middle position, we can determine the bit''s value without simulating the entire
      string construction.


      If $k$ is less than the middle index, the bit is identical to the $k$-th bit in
      $S_{n-1}$. If $k$ is exactly at the middle, the result is ''1''. If $k$ is greater
      than the middle, we map $k$ to its symmetric position in the first half using
      the formula $2^n - k$. The bit at $k$ is then the logical inversion of the bit
      at this symmetric position in $S_{n-1}$. This recursive reduction continues until
      the base case $S_1 = "0"$ is reached.'
    time_complexity: O(n) because each recursive call reduces the problem size by decreasing
      $n$ by 1. Since $n$ is at most 20, the recursion depth is small and each step
      involves only constant-time arithmetic operations.
    space_complexity: O(n) due to the recursive call stack. The maximum depth of the
      recursion is $n$, which requires proportional memory to store the execution context
      at each level.
    elapsed_time: 235.99595546722412
    model: gemini-3-flash-preview
    generated_at: '2026-03-03 01:29:41 '
---

## Problem #1545: Find Kth Bit in Nth Binary String

**Difficulty:** Medium

**Topics:** String, Recursion, Simulation

## Problem Description

<p>Given two positive integers <code>n</code> and <code>k</code>, the binary string <code>S<sub>n</sub></code> is formed as follows:</p>

<ul>
	<li><code>S<sub>1</sub> = &quot;0&quot;</code></li>
	<li><code>S<sub>i</sub> = S<sub>i - 1</sub> + &quot;1&quot; + reverse(invert(S<sub>i - 1</sub>))</code> for <code>i &gt; 1</code></li>
</ul>

<p>Where <code>+</code> denotes the concatenation operation, <code>reverse(x)</code> returns the reversed string <code>x</code>, and <code>invert(x)</code> inverts all the bits in <code>x</code> (<code>0</code> changes to <code>1</code> and <code>1</code> changes to <code>0</code>).</p>

<p>For example, the first four strings in the above sequence are:</p>

<ul>
	<li><code>S<sub>1 </sub>= &quot;0&quot;</code></li>
	<li><code>S<sub>2 </sub>= &quot;0<strong>1</strong>1&quot;</code></li>
	<li><code>S<sub>3 </sub>= &quot;011<strong>1</strong>001&quot;</code></li>
	<li><code>S<sub>4</sub> = &quot;0111001<strong>1</strong>0110001&quot;</code></li>
</ul>

<p>Return <em>the</em> <code>k<sup>th</sup></code> <em>bit</em> <em>in</em> <code>S<sub>n</sub></code>. It is guaranteed that <code>k</code> is valid for the given <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3, k = 1
<strong>Output:</strong> &quot;0&quot;
<strong>Explanation:</strong> S<sub>3</sub> is &quot;<strong><u>0</u></strong>111001&quot;.
The 1<sup>st</sup> bit is &quot;0&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 4, k = 11
<strong>Output:</strong> &quot;1&quot;
<strong>Explanation:</strong> S<sub>4</sub> is &quot;0111001101<strong><u>1</u></strong>0001&quot;.
The 11<sup>th</sup> bit is &quot;1&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>1 &lt;= k &lt;= 2<sup>n</sup> - 1</code></li>
</ul>


## Hints

1. Since n is small, we can simply simulate the process of constructing S1 to Sn.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The binary string sequence $S_n$ is constructed recursively where $S_n$ consists of $S_{n-1}$, followed by a '1', and finally the reversed, inverted version of $S_{n-1}$. This structure reveals a middle bit at position $2^{n-1}$ that is always '1' for $n > 1$. By comparing the target index $k$ with this middle position, we can determine the bit's value without simulating the entire string construction.

If $k$ is less than the middle index, the bit is identical to the $k$-th bit in $S_{n-1}$. If $k$ is exactly at the middle, the result is '1'. If $k$ is greater than the middle, we map $k$ to its symmetric position in the first half using the formula $2^n - k$. The bit at $k$ is then the logical inversion of the bit at this symmetric position in $S_{n-1}$. This recursive reduction continues until the base case $S_1 = "0"$ is reached.

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
    char findKthBit(int n, int k) {
        if (n == 1) return '0';
        int mid = 1 << (n - 1);
        if (k == mid) return '1';
        if (k < mid) return findKthBit(n - 1, k);
        return findKthBit(n - 1, (1 << n) - k) == '0' ? '1' : '0';
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public char findKthBit(int n, int k) {
        if (n == 1) return '0';
        int mid = 1 << (n - 1);
        if (k == mid) return '1';
        if (k < mid) return findKthBit(n - 1, k);
        return findKthBit(n - 1, (1 << n) - k) == '0' ? '1' : '0';
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return "0"
        mid = 1 << (n - 1)
        if k == mid:
            return "1"
        if k < mid:
            return self.findKthBit(n - 1, k)
        res = self.findKthBit(n - 1, (1 << n) - k)
        return "1" if res == "0" else "0"
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        mid = 1 << (n - 1)
        if k == mid:
            return "1"
        if k < mid:
            return self.findKthBit(n - 1, k)
        res = self.findKthBit(n - 1, (1 << n) - k)
        return "1" if res == "0" else "0"
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
char findKthBit(int n, int k) {
    if (n == 1) return '0';
    int mid = 1 << (n - 1);
    if (k == mid) return '1';
    if (k < mid) return findKthBit(n - 1, k);
    return findKthBit(n - 1, (1 << n) - k) == '0' ? '1' : '0';
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public char FindKthBit(int n, int k) {
        if (n == 1) return '0';
        int mid = 1 << (n - 1);
        if (k == mid) return '1';
        if (k < mid) return FindKthBit(n - 1, k);
        return FindKthBit(n - 1, (1 << n) - k) == '0' ? '1' : '0';
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
 * @param {number} k
 * @return {character}
 */
var findKthBit = function(n, k) {
    if (n === 1) return "0";
    var mid = 1 << (n - 1);
    if (k === mid) return "1";
    if (k < mid) return findKthBit(n - 1, k);
    return findKthBit(n - 1, (1 << n) - k) === "0" ? "1" : "0";
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findKthBit(n: number, k: number): string {
    if (n === 1) return "0";
    const mid = 1 << (n - 1);
    if (k === mid) return "1";
    if (k < mid) return findKthBit(n - 1, k);
    return findKthBit(n - 1, (1 << n) - k) === "0" ? "1" : "0";
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
     * @param Integer $k
     * @return String
     */
    function findKthBit($n, $k) {
        if ($n == 1) return "0";
        $mid = 1 << ($n - 1);
        if ($k == $mid) return "1";
        if ($k < $mid) return $this->findKthBit($n - 1, $k);
        return $this->findKthBit($n - 1, (1 << $n) - $k) == "0" ? "1" : "0";
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func findKthBit(_ n: Int, _ k: Int) -> Character {
        if n == 1 { return "0" }
        let mid = 1 << (n - 1)
        if k == mid { return "1" }
        if k < mid { return findKthBit(n - 1, k) }
        let bit = findKthBit(n - 1, (1 << n) - k)
        return bit == "0" ? "1" : "0"
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun findKthBit(n: Int, k: Int): Char {
        if (n == 1) return '0'
        val mid = 1 shl (n - 1)
        return when {
            k == mid -> '1'
            k < mid -> findKthBit(n - 1, k)
            else -> if (findKthBit(n - 1, (1 shl n) - k) == '0') '1' else '0'
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String findKthBit(int n, int k) {
    if (n == 1) return "0";
    int mid = 1 << (n - 1);
    if (k == mid) return "1";
    if (k < mid) return findKthBit(n - 1, k);
    return findKthBit(n - 1, (1 << n) - k) == "0" ? "1" : "0";
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func findKthBit(n int, k int) byte {
    if n == 1 {
        return '0'
    }
    mid := 1 << (n - 1)
    if k == mid {
        return '1'
    }
    if k < mid {
        return findKthBit(n-1, k)
    }
    bit := findKthBit(n-1, (1<<n)-k)
    if bit == '0' {
        return '1'
    }
    return '0'
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def find_kth_bit(n, k)
  return "0" if n == 1
  mid = 1 << (n - 1)
  return "1" if k == mid
  if k < mid
    find_kth_bit(n - 1, k)
  else
    res = find_kth_bit(n - 1, 2 * mid - k)
    res == "0" ? "1" : "0"
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def findKthBit(n: Int, k: Int): Char = {
        if (n == 1) return '0'
        val mid = 1 << (n - 1)
        if (k == mid) return '1'
        if (k < mid) return findKthBit(n - 1, k)
        val res = findKthBit(n - 1, 2 * mid - k)
        if (res == '0') '1' else '0'
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn find_kth_bit(n: i32, k: i32) -> char {
        if n == 1 {
            return '0';
        }
        let mid = 1 << (n - 1);
        if k == mid {
            return '1';
        }
        if k < mid {
            return Self::find_kth_bit(n - 1, k);
        }
        let res = Self::find_kth_bit(n - 1, 2 * mid - k);
        if res == '0' { '1' } else { '0' }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (find-kth-bit n k)
  (-> exact-integer? exact-integer? char?)
  (cond
    [(= n 1) #\0]
    [else
     (let ([mid (expt 2 (- n 1))])
       (cond
         [(= k mid) #\1]
         [(< k mid) (find-kth-bit (- n 1) k)]
         [else (if (char=? (find-kth-bit (- n 1) (- (* 2 mid) k)) #\0) #\1 #\0)]))]))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec find_kth_bit(N :: integer(), K :: integer()) -> char().
find_kth_bit(N, K) ->
  if
    N =:= 1 -> $0;
    true ->
      Mid = 1 bsl (N - 1),
      if
        K =:= Mid -> $1;
        K < Mid -> find_kth_bit(N - 1, K);
        true ->
          case find_kth_bit(N - 1, 2 * Mid - K) of
            $0 -> $1;
            $1 -> $0
          end
      end
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec find_kth_bit(n :: integer, k :: integer) :: char
  def find_kth_bit(n, k) do
    if n == 1 do
      ?0
    else
      mid = round(:math.pow(2, n - 1))
      cond do
        k == mid -> ?1
        k < mid -> find_kth_bit(n - 1, k)
        true ->
          if find_kth_bit(n - 1, 2 * mid - k) == ?0 do
            ?1
          else
            ?0
          end
      end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) because each recursive call reduces the problem size by decreasing $n$ by 1. Since $n$ is at most 20, the recursion depth is small and each step involves only constant-time arithmetic operations.
- **Space Complexity:** O(n) due to the recursive call stack. The maximum depth of the recursion is $n$, which requires proportional memory to store the execution context at each level.
