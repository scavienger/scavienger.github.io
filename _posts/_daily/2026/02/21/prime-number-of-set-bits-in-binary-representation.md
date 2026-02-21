---
layout: post
title: "Prime Number of Set Bits in Binary Representation"
date: 2026-02-21 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Math", "Bit Manipulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int countPrimeSetBits(int left, int right)\
        \ {\n        int ans = 0;\n        for (int i = left; i <= right; ++i) {\n \
        \           int bits = __builtin_popcount(i);\n            if ((665772 >> bits)\
        \ & 1) {\n                ans++;\n            }\n        }\n        return ans;\n\
        \    }\n};"
      java: "class Solution {\n    public int countPrimeSetBits(int left, int right)\
        \ {\n        int ans = 0;\n        for (int i = left; i <= right; i++) {\n \
        \           int bits = Integer.bitCount(i);\n            if (((1 << bits) &\
        \ 665772) != 0) {\n                ans++;\n            }\n        }\n      \
        \  return ans;\n    }\n}"
      python: "class Solution(object):\n    def countPrimeSetBits(self, left, right):\n\
        \        \"\"\"\n        :type left: int\n        :type right: int\n       \
        \ :rtype: int\n        \"\"\"\n        ans = 0\n        primes = {2, 3, 5, 7,\
        \ 11, 13, 17, 19}\n        for i in range(left, right + 1):\n            if\
        \ bin(i).count('1') in primes:\n                ans += 1\n        return ans"
      python3: "class Solution:\n    def countPrimeSetBits(self, left: int, right: int)\
        \ -> int:\n        ans = 0\n        primes = {2, 3, 5, 7, 11, 13, 17, 19}\n\
        \        for i in range(left, right + 1):\n            if bin(i).count('1')\
        \ in primes:\n                ans += 1\n        return ans"
      c: "int countPrimeSetBits(int left, int right) {\n    int ans = 0;\n    for (int\
        \ i = left; i <= right; i++) {\n        int bits = __builtin_popcount(i);\n\
        \        if ((665772 >> bits) & 1) {\n            ans++;\n        }\n    }\n\
        \    return ans;\n}"
      csharp: "public class Solution {\n    public int CountPrimeSetBits(int left, int\
        \ right) {\n        int ans = 0;\n        for (int i = left; i <= right; i++)\
        \ {\n            int bits = 0;\n            int n = i;\n            while (n\
        \ > 0) {\n                n &= (n - 1);\n                bits++;\n         \
        \   }\n            if (((1 << bits) & 665772) != 0) {\n                ans++;\n\
        \            }\n        }\n        return ans;\n    }\n}"
      javascript: "/**\n * @param {number} left\n * @param {number} right\n * @return\
        \ {number}\n */\nvar countPrimeSetBits = function(left, right) {\n    let ans\
        \ = 0;\n    const primeMask = 665772;\n    for (let i = left; i <= right; i++)\
        \ {\n        let bits = 0;\n        let n = i;\n        while (n > 0) {\n  \
        \          n &= (n - 1);\n            bits++;\n        }\n        if ((primeMask\
        \ >> bits) & 1) {\n            ans++;\n        }\n    }\n    return ans;\n};"
      typescript: "function countPrimeSetBits(left: number, right: number): number {\n\
        \    let count = 0;\n    const mask = 665772;\n    for (let i = left; i <= right;\
        \ i++) {\n        let bits = 0;\n        for (let n = i; n > 0; n &= (n - 1))\
        \ {\n            bits++;\n        }\n        if ((mask & (1 << bits)) !== 0)\
        \ {\n            count++;\n        }\n    }\n    return count;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $left\n     * @param\
        \ Integer $right\n     * @return Integer\n     */\n    function countPrimeSetBits($left,\
        \ $right) {\n        $count = 0;\n        $mask = 665772;\n        for ($i =\
        \ $left; $i <= $right; $i++) {\n            $bits = 0;\n            for ($n\
        \ = $i; $n > 0; $n &= ($n - 1)) {\n                $bits++;\n            }\n\
        \            if (($mask & (1 << $bits)) !== 0) {\n                $count++;\n\
        \            }\n        }\n        return $count;\n    }\n}"
      swift: "class Solution {\n    func countPrimeSetBits(_ left: Int, _ right: Int)\
        \ -> Int {\n        var count = 0\n        let mask = 665772\n        for i\
        \ in left...right {\n            let bits = i.nonzeroBitCount\n            if\
        \ (mask & (1 << bits)) != 0 {\n                count += 1\n            }\n \
        \       }\n        return count\n    }\n}"
      kotlin: "class Solution {\n    fun countPrimeSetBits(left: Int, right: Int): Int\
        \ {\n        var count = 0\n        val mask = 665772\n        for (i in left..right)\
        \ {\n            val bits = java.lang.Integer.bitCount(i)\n            if ((mask\
        \ and (1 shl bits)) != 0) {\n                count++\n            }\n      \
        \  }\n        return count\n    }\n}"
      dart: "class Solution {\n  int countPrimeSetBits(int left, int right) {\n    int\
        \ count = 0;\n    const mask = 665772;\n    for (int i = left; i <= right; i++)\
        \ {\n      int bits = 0;\n      for (int n = i; n > 0; n &= (n - 1)) {\n   \
        \     bits++;\n      }\n      if ((mask & (1 << bits)) != 0) {\n        count++;\n\
        \      }\n    }\n    return count;\n  }\n}"
      go: "func countPrimeSetBits(left int, right int) int {\n    count := 0\n    mask\
        \ := 665772\n    for i := left; i <= right; i++ {\n        bits := 0\n     \
        \   for n := i; n > 0; n &= (n - 1) {\n            bits++\n        }\n     \
        \   if (mask & (1 << bits)) != 0 {\n            count++\n        }\n    }\n\
        \    return count\n}"
      ruby: "def count_prime_set_bits(left, right)\n  primes = [2, 3, 5, 7, 11, 13,\
        \ 17, 19]\n  (left..right).count { |n| primes.include?(n.to_s(2).count('1'))\
        \ }\nend"
      scala: "object Solution {\n    def countPrimeSetBits(left: Int, right: Int): Int\
        \ = {\n        val primes = Set(2, 3, 5, 7, 11, 13, 17, 19)\n        (left to\
        \ right).count(n => primes.contains(java.lang.Integer.bitCount(n)))\n    }\n\
        }"
      rust: "impl Solution {\n    pub fn count_prime_set_bits(left: i32, right: i32)\
        \ -> i32 {\n        let primes = [2, 3, 5, 7, 11, 13, 17, 19];\n        (left..=right)\n\
        \            .filter(|&n| primes.contains(&(n.count_ones() as i32)))\n     \
        \       .count() as i32\n    }\n}"
      racket: "(define/contract (count-prime-set-bits left right)\n  (-> exact-integer?\
        \ exact-integer? exact-integer?)\n  (let ([primes '(2 3 5 7 11 13 17 19)])\n\
        \    (for/sum ([i (in-range left (add1 right))])\n      (if (member (integer-popcount\
        \ i) primes) 1 0))))"
      erlang: "count_prime_set_bits(Left, Right) ->\n  count_prime_set_bits(Left, Right,\
        \ 0).\n\ncount_prime_set_bits(Current, Right, Acc) when Current > Right ->\n\
        \  Acc;\ncount_prime_set_bits(Current, Right, Acc) ->\n  BC = bit_count(Current,\
        \ 0),\n  IsPrime = lists:member(BC, [2, 3, 5, 7, 11, 13, 17, 19]),\n  NewAcc\
        \ = if IsPrime -> Acc + 1; true -> Acc end,\n  count_prime_set_bits(Current\
        \ + 1, Right, NewAcc).\n\nbit_count(0, Count) -> Count;\nbit_count(N, Count)\
        \ -> bit_count(N bsr 1, Count + (N band 1))."
      elixir: "defmodule Solution do\n  @spec count_prime_set_bits(left :: integer,\
        \ right :: integer) :: integer\n  def count_prime_set_bits(left, right) do\n\
        \    primes = [2, 3, 5, 7, 11, 13, 17, 19]\n    Enum.count(left..right, fn n\
        \ ->\n      Integer.popcount(n) in primes\n    end)\n  end\nend"
    approach: 'The problem requires counting how many integers in a range [left, right]
      have a prime number of set bits (Hamming weight). Since the maximum possible value
      is 10^6, which is less than 2^20, any integer in this range will have at most
      19 set bits. We can pre-identify the prime numbers up to 19 as {2, 3, 5, 7, 11,
      13, 17, 19}. This small set allows for extremely fast lookups using a bitmask
      where the i-th bit is set if i is prime, specifically the decimal value 665772.


      We iterate through each integer from ''left'' to ''right'' and calculate its set
      bits count using built-in library functions like __builtin_popcount in C/C++ or
      Integer.bitCount in Java, or bit manipulation techniques like Brian Kernighan''s
      algorithm. If the resulting count is a bit position set in our prime mask (or
      exists in our prime set), we increment the final answer. The small range of the
      input (at most 10,001 integers) ensures that this approach is efficient and well
      within time limits.'
    time_complexity: O(N log M), where N is the number of integers in the range (up
      to 10^4) and M is the maximum value of the integers (up to 10^6). Calculating
      the set bits for each number takes O(log M) time, leading to an overall efficient
      linear scan of the range.
    space_complexity: O(1), as we only use a fixed bitmask or a small constant-sized
      set to store the prime numbers up to 19, and a few integer variables for counting.
    elapsed_time: 214.5078821182251
    model: gemini-3-flash-preview
    generated_at: '2026-02-21 01:23:20 '
---

## Problem #762: Prime Number of Set Bits in Binary Representation

**Difficulty:** Easy

**Topics:** Math, Bit Manipulation

## Problem Description

<p>Given two integers <code>left</code> and <code>right</code>, return <em>the <strong>count</strong> of numbers in the <strong>inclusive</strong> range </em><code>[left, right]</code><em> having a <strong>prime number of set bits</strong> in their binary representation</em>.</p>

<p>Recall that the <strong>number of set bits</strong> an integer has is the number of <code>1</code>&#39;s present when written in binary.</p>

<ul>
	<li>For example, <code>21</code> written in binary is <code>10101</code>, which has <code>3</code> set bits.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> left = 6, right = 10
<strong>Output:</strong> 4
<strong>Explanation:</strong>
6  -&gt; 110 (2 set bits, 2 is prime)
7  -&gt; 111 (3 set bits, 3 is prime)
8  -&gt; 1000 (1 set bit, 1 is not prime)
9  -&gt; 1001 (2 set bits, 2 is prime)
10 -&gt; 1010 (2 set bits, 2 is prime)
4 numbers have a prime number of set bits.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> left = 10, right = 15
<strong>Output:</strong> 5
<strong>Explanation:</strong>
10 -&gt; 1010 (2 set bits, 2 is prime)
11 -&gt; 1011 (3 set bits, 3 is prime)
12 -&gt; 1100 (2 set bits, 2 is prime)
13 -&gt; 1101 (3 set bits, 3 is prime)
14 -&gt; 1110 (3 set bits, 3 is prime)
15 -&gt; 1111 (4 set bits, 4 is not prime)
5 numbers have a prime number of set bits.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= left &lt;= right &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= right - left &lt;= 10<sup>4</sup></code></li>
</ul>


## Hints

1. Write a helper function to count the number of set bits in a number, then check whether the number of set bits is 2, 3, 5, 7, 11, 13, 17 or 19.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem requires counting how many integers in a range [left, right] have a prime number of set bits (Hamming weight). Since the maximum possible value is 10^6, which is less than 2^20, any integer in this range will have at most 19 set bits. We can pre-identify the prime numbers up to 19 as {2, 3, 5, 7, 11, 13, 17, 19}. This small set allows for extremely fast lookups using a bitmask where the i-th bit is set if i is prime, specifically the decimal value 665772.

We iterate through each integer from 'left' to 'right' and calculate its set bits count using built-in library functions like __builtin_popcount in C/C++ or Integer.bitCount in Java, or bit manipulation techniques like Brian Kernighan's algorithm. If the resulting count is a bit position set in our prime mask (or exists in our prime set), we increment the final answer. The small range of the input (at most 10,001 integers) ensures that this approach is efficient and well within time limits.

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
    int countPrimeSetBits(int left, int right) {
        int ans = 0;
        for (int i = left; i <= right; ++i) {
            int bits = __builtin_popcount(i);
            if ((665772 >> bits) & 1) {
                ans++;
            }
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
    public int countPrimeSetBits(int left, int right) {
        int ans = 0;
        for (int i = left; i <= right; i++) {
            int bits = Integer.bitCount(i);
            if (((1 << bits) & 665772) != 0) {
                ans++;
            }
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
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        ans = 0
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        for i in range(left, right + 1):
            if bin(i).count('1') in primes:
                ans += 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        for i in range(left, right + 1):
            if bin(i).count('1') in primes:
                ans += 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countPrimeSetBits(int left, int right) {
    int ans = 0;
    for (int i = left; i <= right; i++) {
        int bits = __builtin_popcount(i);
        if ((665772 >> bits) & 1) {
            ans++;
        }
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
    public int CountPrimeSetBits(int left, int right) {
        int ans = 0;
        for (int i = left; i <= right; i++) {
            int bits = 0;
            int n = i;
            while (n > 0) {
                n &= (n - 1);
                bits++;
            }
            if (((1 << bits) & 665772) != 0) {
                ans++;
            }
        }
        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var countPrimeSetBits = function(left, right) {
    let ans = 0;
    const primeMask = 665772;
    for (let i = left; i <= right; i++) {
        let bits = 0;
        let n = i;
        while (n > 0) {
            n &= (n - 1);
            bits++;
        }
        if ((primeMask >> bits) & 1) {
            ans++;
        }
    }
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countPrimeSetBits(left: number, right: number): number {
    let count = 0;
    const mask = 665772;
    for (let i = left; i <= right; i++) {
        let bits = 0;
        for (let n = i; n > 0; n &= (n - 1)) {
            bits++;
        }
        if ((mask & (1 << bits)) !== 0) {
            count++;
        }
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $left
     * @param Integer $right
     * @return Integer
     */
    function countPrimeSetBits($left, $right) {
        $count = 0;
        $mask = 665772;
        for ($i = $left; $i <= $right; $i++) {
            $bits = 0;
            for ($n = $i; $n > 0; $n &= ($n - 1)) {
                $bits++;
            }
            if (($mask & (1 << $bits)) !== 0) {
                $count++;
            }
        }
        return $count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countPrimeSetBits(_ left: Int, _ right: Int) -> Int {
        var count = 0
        let mask = 665772
        for i in left...right {
            let bits = i.nonzeroBitCount
            if (mask & (1 << bits)) != 0 {
                count += 1
            }
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countPrimeSetBits(left: Int, right: Int): Int {
        var count = 0
        val mask = 665772
        for (i in left..right) {
            val bits = java.lang.Integer.bitCount(i)
            if ((mask and (1 shl bits)) != 0) {
                count++
            }
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int countPrimeSetBits(int left, int right) {
    int count = 0;
    const mask = 665772;
    for (int i = left; i <= right; i++) {
      int bits = 0;
      for (int n = i; n > 0; n &= (n - 1)) {
        bits++;
      }
      if ((mask & (1 << bits)) != 0) {
        count++;
      }
    }
    return count;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func countPrimeSetBits(left int, right int) int {
    count := 0
    mask := 665772
    for i := left; i <= right; i++ {
        bits := 0
        for n := i; n > 0; n &= (n - 1) {
            bits++
        }
        if (mask & (1 << bits)) != 0 {
            count++
        }
    }
    return count
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def count_prime_set_bits(left, right)
  primes = [2, 3, 5, 7, 11, 13, 17, 19]
  (left..right).count { |n| primes.include?(n.to_s(2).count('1')) }
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countPrimeSetBits(left: Int, right: Int): Int = {
        val primes = Set(2, 3, 5, 7, 11, 13, 17, 19)
        (left to right).count(n => primes.contains(java.lang.Integer.bitCount(n)))
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_prime_set_bits(left: i32, right: i32) -> i32 {
        let primes = [2, 3, 5, 7, 11, 13, 17, 19];
        (left..=right)
            .filter(|&n| primes.contains(&(n.count_ones() as i32)))
            .count() as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (count-prime-set-bits left right)
  (-> exact-integer? exact-integer? exact-integer?)
  (let ([primes '(2 3 5 7 11 13 17 19)])
    (for/sum ([i (in-range left (add1 right))])
      (if (member (integer-popcount i) primes) 1 0))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
count_prime_set_bits(Left, Right) ->
  count_prime_set_bits(Left, Right, 0).

count_prime_set_bits(Current, Right, Acc) when Current > Right ->
  Acc;
count_prime_set_bits(Current, Right, Acc) ->
  BC = bit_count(Current, 0),
  IsPrime = lists:member(BC, [2, 3, 5, 7, 11, 13, 17, 19]),
  NewAcc = if IsPrime -> Acc + 1; true -> Acc end,
  count_prime_set_bits(Current + 1, Right, NewAcc).

bit_count(0, Count) -> Count;
bit_count(N, Count) -> bit_count(N bsr 1, Count + (N band 1)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_prime_set_bits(left :: integer, right :: integer) :: integer
  def count_prime_set_bits(left, right) do
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    Enum.count(left..right, fn n ->
      Integer.popcount(n) in primes
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log M), where N is the number of integers in the range (up to 10^4) and M is the maximum value of the integers (up to 10^6). Calculating the set bits for each number takes O(log M) time, leading to an overall efficient linear scan of the range.
- **Space Complexity:** O(1), as we only use a fixed bitmask or a small constant-sized set to store the prime numbers up to 19, and a few integer variables for counting.
