---
layout: post
title: "Smallest Integer Divisible by K"
date: 2025-11-25 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Hash Table", "Math"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/smallest-integer-divisible-by-k/
---

## Problem #1015: Smallest Integer Divisible by K

**Difficulty:** Medium

**Topics:** Hash Table, Math

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

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-25 01:03:41 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to find the length of the smallest positive integer `n` that consists solely of the digit '1' and is divisible by a given positive integer `k`. Since `n` can grow very large, we cannot construct it directly. Instead, we must use modular arithmetic to track the remainder of `n` when divided by `k`.

We can observe a recursive pattern for numbers consisting only of ones: `n_len = n_{len-1} * 10 + 1`, where `n_len` is the number with `len` ones. For example, `11 = 1 * 10 + 1`, and `111 = 11 * 10 + 1`. We can simulate this process iteratively. We start with a `remainder` of 0 and a `length` of 0. In each step, we increment `length`, update the `remainder` using the formula `(current_remainder * 10 + 1) % k`, and check if the `new_remainder` is 0. If it is, the current `length` is our answer.

A crucial optimization and correctness check involves the divisibility of `k`. If `k` is divisible by 2 or 5, no such `n` can exist. This is because any number composed entirely of ones (e.g., 1, 11, 111, ...) always ends in the digit '1'. A number ending in '1' cannot be divisible by 2 (as it must be even) nor by 5 (as it must end in '0' or '5'). Therefore, if `k % 2 == 0` or `k % 5 == 0`, we can immediately return -1. If `k` is not divisible by 2 or 5, it implies that `gcd(k, 10) = 1`, which guarantees that a solution exists.

The sequence of remainders `(1 % k), (11 % k), (111 % k), ...` will eventually repeat. Since there are only `k` possible remainders (0 to `k-1`), if we haven't found a remainder of 0 within `k` iterations, we must have encountered a repeated non-zero remainder. When `gcd(k, 10) = 1`, the sequence of remainders is purely periodic, meaning if a solution exists, it will be found within at most `k` steps. Thus, we can iterate up to `k` times. If `remainder` becomes 0, we return the current `length`. If the loop completes `k` iterations without `remainder` becoming 0, it indicates that no solution exists (though this scenario should ideally not be reached if the initial `k % 2` or `k % 5` check is performed and `k > 1`).

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
        for (int length = 1; length <= k; ++length) {
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
#include <stdio.h>

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
        for (int length = 1; length <= k; ++length) {
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
    for (let length = 1; length <= k; ++length) {
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

    let remainder: number = 0;
    for (let length: number = 1; length <= k; ++length) {
        remainder = (remainder * 10 + 1) % k;
        if (remainder === 0) {
            return length;
        }
    }

    return -1;
}
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
        for ($length = 1; $length <= $k; ++$length) {
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

    int remainder = 0;
    for (int length = 1; length <= k; ++length) {
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
package main

func smallestRepunitDivByK(k int) int {
    if k % 2 == 0 || k % 5 == 0 {
        return -1
    }

    remainder := 0
    for length := 1; length <= k; length++ {
        remainder = (remainder * 10 + 1) % k
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
def smallest_repun_it_div_by_k(k)
    if k % 2 == 0 || k % 5 == 0
        return -1
    end

    remainder = 0
    (1..k).each do |length|
        remainder = (remainder * 10 + 1) % k
        if remainder == 0
            return length
        end
    end

    return -1
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
    pub fn smallest_repun_it_div_by_k(k: i32) -> i32 {
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
#lang racket

(define (smallest-repun-it-div-by-k k)
  (if (or (= (modulo k 2) 0) (= (modulo k 5) 0))
      -1
      (let loop ((remainder 0) (length 1))
        (if (> length k)
            -1
            (let ((new-remainder (modulo (+ (* remainder 10) 1) k)))
              (if (= new-remainder 0)
                  length
                  (loop new-remainder (+ length 1))))))))

(define (smallestRepunitDivByK k)
  (smallest-repun-it-div-by-k k))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([smallest_repun_it_div_by_k/1]).

smallest_repun_it_div_by_k(K) ->
if
K rem 2 == 0; K rem 5 == 0 ->
-1;
true ->
smallest_repun_it_div_by_k_loop(K, 0, 1)
end.

smallest_repun_it_div_by_k_loop(K, Remainder, Length) when Length =< K ->
NewRemainder = (Remainder * 10 + 1) rem K,
if
NewRemainder == 0 ->
Length;
true ->
smallest_repun_it_div_by_k_loop(K, NewRemainder, Length + 1)
end;
smallest_repun_it_div_by_k_loop(_K, _Remainder, _Length) ->
-1.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec smallest_repun_it_div_by_k(k :: integer) :: integer
  def smallest_repun_it_div_by_k(k) do
    if rem(k, 2) == 0 or rem(k, 5) == 0 do
      -1
    else
      smallest_repun_it_div_by_k_loop(k, 0, 1)
    end
  end

  defp smallest_repun_it_div_by_k_loop(k, remainder, length) when length <= k do
    new_remainder = rem(remainder * 10 + 1, k)
    if new_remainder == 0 do
      length
    else
      smallest_repun_it_div_by_k_loop(k, new_remainder, length + 1)
    end
  end

  defp smallest_repun_it_div_by_k_loop(_k, _remainder, _length) do
    -1
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(k) with explanation

- **Space Complexity:** O(1) with explanation

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-25 01:03:45 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by using a mathematical approach. We need to find the smallest positive integer n that is divisible by k and only contains the digit 1. We can start by checking if k is divisible by 2 or 5. If it is, then there is no such n because any number consisting only of 1s will always be odd and will never end in 0 or 5. If k is not divisible by 2 or 5, then we can use the fact that 11111 = 1111 * 10 + 1 to find the remainder of n modulo k. We can keep adding 1 to the remainder until we get a remainder of 0, which means we have found the smallest n that is divisible by k.

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
#include <iostream>
class Solution {
public:
    int smallestRepunitDivByK(int k) {
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
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
public class Solution {
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
#include <stdio.h>
int smallestRepunitDivByK(int k) {
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
var smallestRepunitDivByK = function(k) {
    if (k % 2 == 0 || k % 5 == 0) {
        return -1;
    }
    let remainder = 0;
    for (let length = 1; length <= k; length++) {
        remainder = (remainder * 10 + 1) % k;
        if (remainder == 0) {
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
    if (k % 2 == 0 || k % 5 == 0) {
        return -1;
    }
    let remainder = 0;
    for (let length = 1; length <= k; length++) {
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

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
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

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func smallestRepunitDivByK(k int) int {
    if k % 2 == 0 || k % 5 == 0 {
        return -1
    }
    remainder := 0
    for length := 1; length <= k; length++ {
        remainder = (remainder * 10 + 1) % k
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
    if k % 2 == 0 || k % 5 == 0
        return -1
    end
    remainder = 0
    (1..k).each do |length|
        remainder = (remainder * 10 + 1) % k
        if remainder == 0
            return length
        end
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
                return length as i32;
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
#lang racket
  (define (smallestRepunitDivByK k)
      (if (or (= (remainder k 2) 0) (= (remainder k 5) 0))
          -1
          (let loop ((length 1) (remainder 0))
            (if (= remainder 0)
                length
                (loop (+ length 1) (remainder (+ (* remainder 10) 1) k))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
  -export([smallestRepunitDivByK/1]).
  smallestRepunitDivByK(K) ->
      if
          K rem 2 == 0 orelse K rem 5 == 0 ->
              -1;
          true ->
              loop(1, 0, K)
      end.
  loop(Length, Remainder, K) ->
      NewRemainder = (Remainder * 10 + 1) rem K,
      if
          NewRemainder == 0 ->
              Length;
          true ->
              loop(Length + 1, NewRemainder, K)
      end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  def smallest_repunit_div_by_k(k) do
      if rem(k, 2) == 0 || rem(k, 5) == 0 do
          -1
      else
          loop(1, 0, k)
      end
  end
  defp loop(length, remainder, k) do
      new_remainder = rem(remainder * 10 + 1, k)
      if new_remainder == 0 do
          length
      else
          loop(length + 1, new_remainder, k)
      end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(k) because in the worst-case scenario, we need to iterate k times to find the remainder of 0.

- **Space Complexity:** O(1) because we only need a constant amount of space to store the remainder and the length of n.

</div>
</details>
