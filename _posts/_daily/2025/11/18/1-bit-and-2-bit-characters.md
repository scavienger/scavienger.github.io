---
layout: post
title: "1-bit and 2-bit Characters"
date: 2025-11-18 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/1-bit-and-2-bit-characters/
---

## Problem #717: 1-bit and 2-bit Characters

**Difficulty:** Easy

**Topics:** Array

## Problem Description

<p>We have two special characters:</p>

<ul>
	<li>The first character can be represented by one bit <code>0</code>.</li>
	<li>The second character can be represented by two bits (<code>10</code> or <code>11</code>).</li>
</ul>

<p>Given a binary array <code>bits</code> that ends with <code>0</code>, return <code>true</code> if the last character must be a one-bit character.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> bits = [1,0,0]
<strong>Output:</strong> true
<strong>Explanation:</strong> The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> bits = [1,1,1,0]
<strong>Output:</strong> false
<strong>Explanation:</strong> The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= bits.length &lt;= 1000</code></li>
	<li><code>bits[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>


## Hints

1. Keep track of where the next character starts.  At the end, you want to know if you started on the last bit.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-20 16:10:28 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to determine if the last character in a given binary array `bits` must be a one-bit character, given that the array always ends with a `0`. A one-bit character is represented by `0`, and a two-bit character is represented by `10` or `11`. This is essentially a decoding problem where we need to trace the parsing of the `bits` array.

Our strategy is to simulate the decoding process from the beginning of the `bits` array to its end. We maintain an index, let's call it `i`, which points to the start of the current character being decoded. We iterate through the array, advancing `i` based on the character type we encounter. If `bits[i]` is `0`, it signifies a one-bit character, and we advance `i` by `1`. If `bits[i]` is `1`, it signifies the start of a two-bit character (either `10` or `11`), and we advance `i` by `2` to consume both bits of that character.

The crucial insight for this problem lies in how we handle the very last character. The problem guarantees that `bits[bits.length - 1]` is `0`. This `0` could either be a standalone one-bit character, or it could be the second bit of a two-bit character (e.g., `10`). We need to determine which scenario *must* occur based on the preceding bits. We continue our simulation until `i` reaches or surpasses `bits.length - 1`. The loop condition `i < bits.length - 1` is key; it ensures we process all characters up to, but not including, the very last bit `bits[bits.length - 1]` itself. This allows us to check the state of `i` precisely when it's time to evaluate the last character.

After the loop finishes, we check the final value of `i`. If `i` is exactly equal to `bits.length - 1`, it means that our decoding process has successfully consumed all characters up to `bits.length - 2`, and the character starting at `bits.length - 1` (which is `0`) is a one-bit character. In this case, the last character must be a one-bit character, and we return `true`. If `i` is greater than `bits.length - 1` (which implies `i` is equal to `bits.length`, as `i` increments by 1 or 2), it means that the character starting at `i-2` (if `bits[i-2]` was `1`) or `i-1` (if `bits[i-1]` was `0`) consumed `bits[bits.length - 1]` as part of a two-bit character. Specifically, if `i` lands at `bits.length`, it implies the last character was a two-bit character whose second bit was `bits[bits.length - 1]`. Therefore, the last character is not a one-bit character, and we return `false`. This greedy approach works because the encoding rules are unambiguous and there's no backtracking required; a `0` always means a one-bit char, and a `1` always means a two-bit char starting there.

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
class Solution {
public:
    bool isOneBitCharacter(std::vector<int>& bits) {
        int i = 0;
        int n = bits.size();
        while (i < n - 1) {
            if (bits[i] == 0) {
                i += 1;
            } else { // bits[i] == 1
                i += 2;
            }
        }
        // If i lands exactly on n-1, it means the last character is a one-bit character (0).
        // If i jumps past n-1 (i.e., i == n), it means the last character (0) was part of a two-bit character.
        return i == n - 1;
    }
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int i = 0;
        int n = bits.length;
        while (i < n - 1) {
            if (bits[i] == 0) {
                i += 1;
            } else { // bits[i] == 1
                i += 2;
            }
        }
        // If i lands exactly on n-1, it means the last character is a one-bit character (0).
        // If i jumps past n-1 (i.e., i == n), it means the last character (0) was part of a two-bit character.
        return i == n - 1;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0
        n = len(bits)
        while i < n - 1:
            if bits[i] == 0:
                i += 1
            else:  # bits[i] == 1
                i += 2
        
        # If i lands exactly on n-1, it means the last character is a one-bit character (0).
        # If i jumps past n-1 (i.e., i == n), it means the last character (0) was part of a two-bit character.
        return i == n - 1
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0
        n = len(bits)
        while i < n - 1:
            if bits[i] == 0:
                i += 1
            else:  # bits[i] == 1
                i += 2
        
        # If i lands exactly on n-1, it means the last character is a one-bit character (0).
        # If i jumps past n-1 (i.e., i == n), it means the last character (0) was part of a two-bit character.
        return i == n - 1
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdbool.h>

bool isOneBitCharacter(int* bits, int bitsSize) {
    int i = 0;
    int n = bitsSize;
    while (i < n - 1) {
        if (bits[i] == 0) {
            i += 1;
        } else { // bits[i] == 1
            i += 2;
        }
    }
    // If i lands exactly on n-1, it means the last character is a one-bit character (0).
    // If i jumps past n-1 (i.e., i == n), it means the last character (0) was part of a two-bit character.
    return i == n - 1;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
public class Solution {
    public bool IsOneBitCharacter(int[] bits) {
        int i = 0;
        int n = bits.Length;
        while (i < n - 1) {
            if (bits[i] == 0) {
                i += 1;
            } else { // bits[i] == 1
                i += 2;
            }
        }
        // If i lands exactly on n-1, it means the last character is a one-bit character (0).
        // If i jumps past n-1 (i.e., i == n), it means the last character (0) was part of a two-bit character.
        return i == n - 1;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
/**
 * @param {number[]} bits
 * @return {boolean}
 */
var isOneBitCharacter = function(bits) {
    let i = 0;
    const n = bits.length;
    while (i < n - 1) {
        if (bits[i] === 0) {
            i += 1;
        } else { // bits[i] === 1
            i += 2;
        }
    }
    // If i lands exactly on n-1, it means the last character is a one-bit character (0).
    // If i jumps past n-1 (i.e., i === n), it means the last character (0) was part of a two-bit character.
    return i === n - 1;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function isOneBitCharacter(bits: number[]): boolean {
    let i: number = 0;
    const n: number = bits.length;
    while (i < n - 1) {
        if (bits[i] === 0) {
            i += 1;
        } else { // bits[i] === 1
            i += 2;
        }
    }
    // If i lands exactly on n-1, it means the last character is a one-bit character (0).
    // If i jumps past n-1 (i.e., i === n), it means the last character (0) was part of a two-bit character.
    return i === n - 1;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
class Solution {
    /**
     * @param Integer[] $bits
     * @return Boolean
     */
    function isOneBitCharacter($bits) {
        $i = 0;
        $n = count($bits);
        while ($i < $n - 1) {
            if ($bits[$i] == 0) {
                $i += 1;
            } else { // $bits[$i] == 1
                $i += 2;
            }
        }
        // If i lands exactly on n-1, it means the last character is a one-bit character (0).
        // If i jumps past n-1 (i.e., i == n), it means the last character (0) was part of a two-bit character.
        return $i == $n - 1;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution {
    func isOneBitCharacter(_ bits: [Int]) -> Bool {
        var i = 0
        let n = bits.count
        while i < n - 1 {
            if bits[i] == 0 {
                i += 1
            } else { // bits[i] == 1
                i += 2
            }
        }
        // If i lands exactly on n-1, it means the last character is a one-bit character (0).
        // If i jumps past n-1 (i.e., i == n), it means the last character (0) was part of a two-bit character.
        return i == n - 1
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution {
    fun isOneBitCharacter(bits: IntArray): Boolean {
        var i = 0
        val n = bits.size
        while (i < n - 1) {
            if (bits[i] == 0) {
                i += 1
            } else { // bits[i] == 1
                i += 2
            }
        }
        // If i lands exactly on n-1, it means the last character is a one-bit character (0).
        // If i jumps past n-1 (i.e., i == n), it means the last character (0) was part of a two-bit character.
        return i == n - 1
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
class Solution {
  bool isOneBitCharacter(List<int> bits) {
    int i = 0;
    int n = bits.length;
    while (i < n - 1) {
      if (bits[i] == 0) {
        i += 1;
      } else { // bits[i] == 1
        i += 2;
      }
    }
    // If i lands exactly on n-1, it means the last character is a one-bit character (0).
    // If i jumps past n-1 (i.e., i == n), it means the last character (0) was part of a two-bit character.
    return i == n - 1;
  }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
func isOneBitCharacter(bits []int) bool {
    i := 0
    n := len(bits)
    for i < n - 1 {
        if bits[i] == 0 {
            i += 1
        } else { // bits[i] == 1
            i += 2
        }
    }
    // If i lands exactly on n-1, it means the last character is a one-bit character (0).
    // If i jumps past n-1 (i.e., i == n), it means the last character (0) was part of a two-bit character.
    return i == n - 1
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
class Solution
    # @param {Integer[]} bits
    # @return {Boolean}
    def is_one_bit_character(bits)
        i = 0
        n = bits.length
        while i < n - 1
            if bits[i] == 0
                i += 1
            else # bits[i] == 1
                i += 2
            end
        end
        # If i lands exactly on n-1, it means the last character is a one-bit character (0).
        # If i jumps past n-1 (i.e., i == n), it means the last character (0) was part of a two-bit character.
        return i == n - 1
    end
end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {
    def isOneBitCharacter(bits: Array[Int]): Boolean = {
        var i = 0
        val n = bits.length
        while (i < n - 1) {
            if (bits(i) == 0) {
                i += 1
            } else { // bits(i) == 1
                i += 2
            }
        }
        // If i lands exactly on n-1, it means the last character is a one-bit character (0).
        // If i jumps past n-1 (i.e., i == n), it means the last character (0) was part of a two-bit character.
        i == n - 1
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution {
    pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
        let mut i = 0;
        let n = bits.len();
        while i < n - 1 {
            if bits[i] == 0 {
                i += 1;
            } else { // bits[i] == 1
                i += 2;
            }
        }
        // If i lands exactly on n-1, it means the last character is a one-bit character (0).
        // If i jumps past n-1 (i.e., i == n), it means the last character (0) was part of a two-bit character.
        i == n - 1
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket
(define/contract (is-one-bit-character bits) 
  (-> (listof exact-integer?) boolean?)
  (let* ((n (length bits))
         (i (let loop ((idx 0))
              (cond
                ((>= idx (- n 1)) idx) ; Stop when idx reaches or surpasses n-1
                ((zero? (list-ref bits idx)) (loop (+ idx 1)))
                (else (loop (+ idx 2)))))))
    (= i (- n 1))))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
-export([is_one_bit_character/1]).

is_one_bit_character(Bits) ->
    N = length(Bits),
    is_one_bit_character_recursive(Bits, 0, N).

is_one_bit_character_recursive(_Bits, I, N) when I >= N - 1 ->
    I == N - 1;
is_one_bit_character_recursive(Bits, I, N) ->
    case lists:nth(I + 1, Bits) of % Erlang lists are 1-indexed for nth
        0 -> is_one_bit_character_recursive(Bits, I + 1, N);
        1 -> is_one_bit_character_recursive(Bits, I + 2, N)
    end.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
  @spec is_one_bit_character(bits :: [integer]) :: boolean
  def is_one_bit_character(bits) do
    n = length(bits)
    is_one_bit_character_recursive(bits, 0, n)
  end

  defp is_one_bit_character_recursive(_bits, i, n) when i >= n - 1 do
    i == n - 1
  end

  defp is_one_bit_character_recursive(bits, i, n) do
    case Enum.at(bits, i) do
      0 -> is_one_bit_character_recursive(bits, i + 1, n)
      1 -> is_one_bit_character_recursive(bits, i + 2, n)
    end
  end
end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N)

- **Space Complexity:** O(1)

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-20 16:10:33 )</small>
</summary>

<div class="ai-solution-content">

### Approach


   The problem requires determining whether the last character in a binary array must be a one-bit character. 
   To solve this problem, we can use a simple iterative approach. We will iterate through the array from left to right, 
   keeping track of the current position. If we encounter a 0, we move one step forward. If we encounter a 1, 
   we move two steps forward because the next character is a two-bit character. 
   At the end of the iteration, if the current position is at the second last element, 
   it means the last character must be a one-bit character.

   The problem-solving strategy involves iterating through the array and keeping track of the current position. 
   We start at the beginning of the array and move forward based on the value of the current element. 
   If the current element is 0, we move one step forward. If the current element is 1, we move two steps forward. 
   This is because a 1 is always followed by another bit (either 0 or 1) to form a two-bit character. 
   By the end of the iteration, we should be at the second last element if the last character is a one-bit character.

   The algorithm logic is straightforward. We initialize a variable to keep track of the current position. 
   We then iterate through the array, updating the current position based on the value of the current element. 
   If the current element is 0, we increment the current position by 1. If the current element is 1, 
   we increment the current position by 2. After the iteration, we check if the current position is at the second last element. 
   If it is, we return True, indicating that the last character must be a one-bit character. Otherwise, we return False.

   For example, consider the array [1,0,0]. We start at the beginning of the array. 
   The first element is 1, so we move two steps forward to the third element. 
   The third element is 0, so we move one step forward to the fourth element. 
   However, since the array only has three elements, we are now at the end of the array. 
   Since we are at the second last element (the third element is the last element), 
   we return True, indicating that the last character must be a one-bit character.

   Another example is the array [1,1,1,0]. We start at the beginning of the array. 
   The first element is 1, so we move two steps forward to the third element. 
   The third element is 1, so we move two steps forward to the fifth element. 
   However, since the array only has four elements, we are now at the end of the array. 
   Since we are not at the second last element, we return False, indicating that the last character is not a one-bit character.
   

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
#include <vector>
       class Solution {
       public:
           bool isOneBitCharacter(std::vector<int>& bits) {
               int i = 0;
               while (i < bits.size() - 1) {
                   if (bits[i] == 0) {
                       i += 1;
                   } else {
                       i += 2;
                   }
               }
               return i == bits.size() - 1;
           }
       };
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
           public boolean isOneBitCharacter(int[] bits) {
               int i = 0;
               while (i < bits.length - 1) {
                   if (bits[i] == 0) {
                       i += 1;
                   } else {
                       i += 2;
                   }
               }
               return i == bits.length - 1;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
           def isOneBitCharacter(self, bits: list[int]) -> bool:
               i = 0
               while i < len(bits) - 1:
                   if bits[i] == 0:
                       i += 1
                   else:
                       i += 2
               return i == len(bits) - 1
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
           def isOneBitCharacter(self, bits: list[int]) -> bool:
               i = 0
               while i < len(bits) - 1:
                   if bits[i] == 0:
                       i += 1
                   else:
                       i += 2
               return i == len(bits) - 1
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdbool.h>
       bool isOneBitCharacter(int* bits, int bitsSize){
           int i = 0;
           while (i < bitsSize - 1) {
               if (bits[i] == 0) {
                   i += 1;
               } else {
                   i += 2;
               }
           }
           return i == bitsSize - 1;
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
public class Solution {
           public bool IsOneBitCharacter(int[] bits) {
               int i = 0;
               while (i < bits.Length - 1) {
                   if (bits[i] == 0) {
                       i += 1;
                   } else {
                       i += 2;
                   }
               }
               return i == bits.Length - 1;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
var isOneBitCharacter = function(bits) {
           let i = 0;
           while (i < bits.length - 1) {
               if (bits[i] == 0) {
                   i += 1;
               } else {
                   i += 2;
               }
           }
           return i == bits.length - 1;
       };
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function isOneBitCharacter(bits: number[]): boolean {
           let i: number = 0;
           while (i < bits.length - 1) {
               if (bits[i] == 0) {
                   i += 1;
               } else {
                   i += 2;
               }
           }
           return i == bits.length - 1;
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
class Solution {
           function isOneBitCharacter($bits) {
               $i = 0;
               while ($i < count($bits) - 1) {
                   if ($bits[$i] == 0) {
                       $i += 1;
                   } else {
                       $i += 2;
                   }
               }
               return $i == count($bits) - 1;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution {
           func isOneBitCharacter(_ bits: [Int]) -> Bool {
               var i = 0
               while i < bits.count - 1 {
                   if bits[i] == 0 {
                       i += 1
                   } else {
                       i += 2
                   }
               }
               return i == bits.count - 1
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution {
           fun isOneBitCharacter(bits: IntArray): Boolean {
               var i = 0
               while (i < bits.size - 1) {
                   if (bits[i] == 0) {
                       i += 1
                   } else {
                       i += 2
                   }
               }
               return i == bits.size - 1
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
class Solution {
           bool isOneBitCharacter(List<int> bits) {
               int i = 0;
               while (i < bits.length - 1) {
                   if (bits[i] == 0) {
                       i += 1;
                   } else {
                       i += 2;
                   }
               }
               return i == bits.length - 1;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
func isOneBitCharacter(bits []int) bool {
           i := 0
           for i < len(bits)-1 {
               if bits[i] == 0 {
                   i += 1
               } else {
                   i += 2
               }
           }
           return i == len(bits)-1
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
# @param {Integer[]} bits
       # @return {Boolean}
       def is_one_bit_character(bits)
           i = 0
           while i < bits.size - 1
               if bits[i] == 0
                   i += 1
               else
                   i += 2
               end
           end
           i == bits.size - 1
       end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {
           def isOneBitCharacter(bits: Array[Int]): Boolean = {
               var i = 0
               while (i < bits.length - 1) {
                   if (bits(i) == 0) {
                       i += 1
                   } else {
                       i += 2
                   }
               }
               i == bits.length - 1
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution {
           pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
               let mut i = 0;
               while i < bits.len() - 1 {
                   if bits[i] == 0 {
                       i += 1;
                   } else {
                       i += 2;
                   }
               }
               i == bits.len() - 1
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket
       (define (is-one-bit-character bits)
           (let loop ((i 0))
             (cond
               ((>= i (sub1 (length bits))) (= i (sub1 (length bits))))
               ((= (list-ref bits i) 0) (loop (add1 i)))
               (else (loop (+ i 2))))))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
       -export([is_one_bit_character/1]).
       is_one_bit_character(Bits) ->
           is_one_bit_character(Bits, 0).
       is_one_bit_character([0|T], I) ->
           is_one_bit_character(T, I + 1);
       is_one_bit_character([1,_|T], I) ->
           is_one_bit_character(T, I + 2);
       is_one_bit_character([], I) ->
           I == -1.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
           def is_one_bit_character(bits) do
               is_one_bit_character(bits, 0)
           end

           defp is_one_bit_character([0|t], i) do
               is_one_bit_character(t, i + 1)
           end

           defp is_one_bit_character([1, _|t], i) do
               is_one_bit_character(t, i + 2)
           end

           defp is_one_bit_character([], i) do
               i == length([]) - 1
           end
       end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** 
   The time complexity of the solution is O(n), where n is the number of elements in the array. 
   This is because we are iterating through the array once, and each operation (comparing the current element and updating the current position) takes constant time. 
   The space complexity is O(1), which means the space required does not change with the size of the input array, 
   making it very efficient in terms of memory usage.
   

- **Space Complexity:** 
   The space complexity of the solution is O(1), which means the space required does not change with the size of the input array. 
   This is because we are only using a constant amount of space to store the current position and the array itself, 
   making it very efficient in terms of memory usage.
   

</div>
</details>
