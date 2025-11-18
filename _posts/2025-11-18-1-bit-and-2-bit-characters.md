---
layout: post
title: 1-bit and 2-bit Characters
date: "2025-11-18 09:00:00 +0900"
categories: [LeetCode, Easy]
tags: ["Array"]
difficulty: Easy
leetcode_url: "https://leetcode.com/problems/1-bit-and-2-bit-characters/"
---
## Problem #717: 1-bit and 2-bit Characters

**Difficulty:** Easy

**Topics:** Array

## Problem Description

We have two special characters:

  * The first character can be represented by one bit `0`.
  * The second character can be represented by two bits (`10` or `11`).

Given a binary array `bits` that ends with `0`, return `true` if the last character must be a one-bit character.

**Example 1:**

``` Input: bits = [1,0,0] Output: true Explanation: The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character. ``` 

**Example 2:**

``` Input: bits = [1,1,1,0] Output: false Explanation: The only way to decode it is two-bit character and two-bit character. So the last character is not one-bit character. ``` 

**Constraints:**

  * `1 <= bits.length <= 1000`
  * `bits[i]` is either `0` or `1`.

## Hints

1. Keep track of where the next character starts.  At the end, you want to know if you started on the last bit.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details open>
<summary><strong>✨ Solution from gemini-2.5-flash</strong></summary>

### Approach

The problem asks us to determine if the last character in a given binary array `bits` (which is guaranteed to end with `0`) must be a one-bit character. We are given two types of special characters: a one-bit character represented by `0`, and a two-bit character represented by `10` or `11`. The key insight here is that the decoding of the `bits` array is unique and unambiguous from left to right. A `0` can only be a one-bit character, consuming one bit. A `1` can only be the start of a two-bit character (either `10` or `11`), consuming two bits.

Our approach is to simulate the decoding process by iterating through the `bits` array from left to right. We maintain a pointer, let's call it `i`, which represents the current index in the `bits` array from where the next character decoding should begin. We initialize `i` to `0`. In each step of our iteration, we examine the bit at `bits[i]`. If `bits[i]` is `0`, it means we've encountered a one-bit character, so we advance our pointer `i` by `1`. If `bits[i]` is `1`, it means we've encountered the start of a two-bit character, so we advance `i` by `2` (to account for both bits of this character). This process continues, greedily consuming characters from the beginning of the array.

The crucial aspect of this problem is to correctly interpret the ending condition and the final state of our pointer `i`. We are interested in whether the character *ending* at the very last position `n-1` (where `n` is the length of `bits`) is a one-bit character. To achieve this, we continue our decoding loop as long as `i` is less than `n - 1`. This loop condition ensures that we process all characters that *precede* the final bit `bits[n-1]`. The last bit itself, `bits[n-1]`, is explicitly excluded from being the *start* of a character handled within the loop, which allows us to check its status post-loop.

After the loop terminates, the value of `i` will provide the answer. There are two possible scenarios for `i` when the loop `while (i < n - 1)` finishes: 
1. If `i` is exactly `n - 1`: This means that after decoding all characters up to `bits[n-2]`, our pointer `i` landed precisely on the index `n - 1`. This implies that `bits[n-1]` itself is the beginning of the *last character* to be decoded. Since the problem statement guarantees that `bits[n-1]` is `0`, this character must be a one-bit character. In this scenario, we return `true`.
2. If `i` is `n`: This means that the last character decoded *inside the loop* was a two-bit character that started at `n - 2` and consumed both `bits[n-2]` and `bits[n-1]`. In this case, `bits[n-1]` was the second bit of a two-bit character, meaning the last character is *not* a one-bit character. In this scenario, we return `false`.
This greedy forward-scanning approach works reliably because the character encoding rules are deterministic, preventing any ambiguity or alternative valid decodings.

### Code

<div class="code-tabs">
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
#include <vector>

class Solution {
public:
    bool isOneBitCharacter(std::vector<int>& bits) {
        int n = bits.size();
        int i = 0;
        while (i < n - 1) {
            if (bits[i] == 1) {
                // This is a two-bit character (10 or 11)
                i += 2;
            } else {
                // This is a one-bit character (0)
                i += 1;
            }
        }
        // After the loop, if i is exactly n - 1, it means the last character
        // started at n - 1. Since bits[n-1] is guaranteed to be 0,
        // it must be a one-bit character.
        // If i is n, it means the last character processed was a two-bit character
        // that consumed bits[n-2] and bits[n-1].
        return i == n - 1;
    }
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int n = bits.length;
        int i = 0;
        while (i < n - 1) {
            if (bits[i] == 1) {
                // This is a two-bit character (10 or 11)
                i += 2;
            } else {
                // This is a one-bit character (0)
                i += 1;
            }
        }
        // After the loop, if i is exactly n - 1, it means the last character
        // started at n - 1. Since bits[n-1] is guaranteed to be 0,
        // it must be a one-bit character.
        // If i is n, it means the last character processed was a two-bit character
        // that consumed bits[n-2] and bits[n-1].
        return i == n - 1;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        while i < n - 1:
            if bits[i] == 1:
                # This is a two-bit character (10 or 11)
                i += 2
            else:
                # This is a one-bit character (0)
                i += 1
        # After the loop, if i is exactly n - 1, it means the last character
        # started at n - 1. Since bits[n-1] is guaranteed to be 0,
        # it must be a one-bit character.
        # If i is n, it means the last character processed was a two-bit character
        # that consumed bits[n-2] and bits[n-1].
        return i == n - 1
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        while i < n - 1:
            if bits[i] == 1:
                # This is a two-bit character (10 or 11)
                i += 2
            else:
                # This is a one-bit character (0)
                i += 1
        # After the loop, if i is exactly n - 1, it means the last character
        # started at n - 1. Since bits[n-1] is guaranteed to be 0,
        # it must be a one-bit character.
        # If i is n, it means the last character processed was a two-bit character
        # that consumed bits[n-2] and bits[n-1].
        return i == n - 1
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdbool.h>

bool isOneBitCharacter(int* bits, int bitsSize) {
    int n = bitsSize;
    int i = 0;
    while (i < n - 1) {
        if (bits[i] == 1) {
            // This is a two-bit character (10 or 11)
            i += 2;
        } else {
            // This is a one-bit character (0)
            i += 1;
        }
    }
    // After the loop, if i is exactly n - 1, it means the last character
    // started at n - 1. Since bits[n-1] is guaranteed to be 0,
    // it must be a one-bit character.
    // If i is n, it means the last character processed was a two-bit character
    // that consumed bits[n-2] and bits[n-1].
    return i == n - 1;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
public class Solution {
    public bool IsOneBitCharacter(int[] bits) {
        int n = bits.Length;
        int i = 0;
        while (i < n - 1) {
            if (bits[i] == 1) {
                // This is a two-bit character (10 or 11)
                i += 2;
            } else {
                // This is a one-bit character (0)
                i += 1;
            }
        }
        // After the loop, if i is exactly n - 1, it means the last character
        // started at n - 1. Since bits[n-1] is guaranteed to be 0,
        // it must be a one-bit character.
        // If i is n, it means the last character processed was a two-bit character
        // that consumed bits[n-2] and bits[n-1].
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
    let n = bits.length;
    let i = 0;
    while (i < n - 1) {
        if (bits[i] === 1) {
            // This is a two-bit character (10 or 11)
            i += 2;
        } else {
            // This is a one-bit character (0)
            i += 1;
        }
    }
    // After the loop, if i is exactly n - 1, it means the last character
    // started at n - 1. Since bits[n-1] is guaranteed to be 0,
    // it must be a one-bit character.
    // If i is n, it means the last character processed was a two-bit character
    // that consumed bits[n-2] and bits[n-1].
    return i === n - 1;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function isOneBitCharacter(bits: number[]): boolean {
    let n: number = bits.length;
    let i: number = 0;
    while (i < n - 1) {
        if (bits[i] === 1) {
            // This is a two-bit character (10 or 11)
            i += 2;
        } else {
            // This is a one-bit character (0)
            i += 1;
        }
    }
    // After the loop, if i is exactly n - 1, it means the last character
    // started at n - 1. Since bits[n-1] is guaranteed to be 0,
    // it must be a one-bit character.
    // If i is n, it means the last character processed was a two-bit character
    // that consumed bits[n-2] and bits[n-1].
    return i === n - 1;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
<?php

class Solution {
    /**
     * @param Integer[] $bits
     * @return Boolean
     */
    function isOneBitCharacter($bits) {
        $n = count($bits);
        $i = 0;
        while ($i < $n - 1) {
            if ($bits[$i] == 1) {
                // This is a two-bit character (10 or 11)
                $i += 2;
            } else {
                // This is a one-bit character (0)
                $i += 1;
            }
        }
        // After the loop, if i is exactly n - 1, it means the last character
        // started at n - 1. Since bits[n-1] is guaranteed to be 0,
        // it must be a one-bit character.
        // If i is n, it means the last character processed was a two-bit character
        // that consumed bits[n-2] and bits[n-1].
        return $i == $n - 1;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution {
    func isOneBitCharacter(_ bits: [Int]) -> Bool {
        let n = bits.count
        var i = 0
        while i < n - 1 {
            if bits[i] == 1 {
                // This is a two-bit character (10 or 11)
                i += 2
            } else {
                // This is a one-bit character (0)
                i += 1
            }
        }
        // After the loop, if i is exactly n - 1, it means the last character
        // started at n - 1. Since bits[n-1] is guaranteed to be 0,
        // it must be a one-bit character.
        // If i is n, it means the last character processed was a two-bit character
        // that consumed bits[n-2] and bits[n-1].
        return i == n - 1
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution {
    fun isOneBitCharacter(bits: IntArray): Boolean {
        val n = bits.size
        var i = 0
        while (i < n - 1) {
            if (bits[i] == 1) {
                // This is a two-bit character (10 or 11)
                i += 2
            } else {
                // This is a one-bit character (0)
                i += 1
            }
        }
        // After the loop, if i is exactly n - 1, it means the last character
        // started at n - 1. Since bits[n-1] is guaranteed to be 0,
        // it must be a one-bit character.
        // If i is n, it means the last character processed was a two-bit character
        // that consumed bits[n-2] and bits[n-1].
        return i == n - 1
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
class Solution {
  bool isOneBitCharacter(List<int> bits) {
    int n = bits.length;
    int i = 0;
    while (i < n - 1) {
      if (bits[i] == 1) {
        // This is a two-bit character (10 or 11)
        i += 2;
      } else {
        // This is a one-bit character (0)
        i += 1;
      }
    }
    // After the loop, if i is exactly n - 1, it means the last character
    // started at n - 1. Since bits[n-1] is guaranteed to be 0,
    // it must be a one-bit character.
    // If i is n, it means the last character processed was a two-bit character
    // that consumed bits[n-2] and bits[n-1].
    return i == n - 1;
  }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

func isOneBitCharacter(bits []int) bool {
    n := len(bits)
    i := 0
    for i < n - 1 {
        if bits[i] == 1 {
            // This is a two-bit character (10 or 11)
            i += 2
        } else {
            // This is a one-bit character (0)
            i += 1
        }
    }
    // After the loop, if i is exactly n - 1, it means the last character
    // started at n - 1. Since bits[n-1] is guaranteed to be 0,
    // it must be a one-bit character.
    // If i is n, it means the last character processed was a two-bit character
    // that consumed bits[n-2] and bits[n-1].
    return i == n - 1
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
# @param {Integer[]} bits
# @return {Boolean}
def is_one_bit_character(bits)
    n = bits.length
    i = 0
    while i < n - 1
        if bits[i] == 1
            # This is a two-bit character (10 or 11)
            i += 2
        else
            # This is a one-bit character (0)
            i += 1
        end
    end
    # After the loop, if i is exactly n - 1, it means the last character
    # started at n - 1. Since bits[n-1] is guaranteed to be 0,
    # it must be a one-bit character.
    # If i is n, it means the last character processed was a two-bit character
    # that consumed bits[n-2] and bits[n-1].
    i == n - 1
end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {
    def isOneBitCharacter(bits: Array[Int]): Boolean = {
        val n = bits.length
        var i = 0
        while (i < n - 1) {
            if (bits(i) == 1) {
                // This is a two-bit character (10 or 11)
                i += 2
            } else {
                // This is a one-bit character (0)
                i += 1
            }
        }
        // After the loop, if i is exactly n - 1, it means the last character
        // started at n - 1. Since bits(n-1) is guaranteed to be 0,
        // it must be a one-bit character.
        // If i is n, it means the last character processed was a two-bit character
        // that consumed bits(n-2) and bits(n-1).
        i == n - 1
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution {
    pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
        let n = bits.len();
        let mut i = 0;
        while i < n - 1 {
            if bits[i] == 1 {
                // This is a two-bit character (10 or 11)
                i += 2;
            } else {
                // This is a one-bit character (0)
                i += 1;
            }
        }
        // After the loop, if i is exactly n - 1, it means the last character
        // started at n - 1. Since bits[n-1] is guaranteed to be 0,
        // it must be a one-bit character.
        // If i is n, it means the last character processed was a two-bit character
        // that consumed bits[n-2] and bits[n-1].
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
         (i (let loop ((k 0))
              (cond
                ((>= k (- n 1)) k) ; Stop before processing the last bit as a potential character start
                ((= (list-ref bits k) 1) (loop (+ k 2)))
                (else (loop (+ k 1)))))))
    ; After the loop, if i is exactly n - 1, it means the last character
    ; started at n - 1. Since bits[n-1] is guaranteed to be 0,
    ; it must be a one-bit character.
    ; If i is n, it means the last character processed was a two-bit character
    ; that consumed bits[n-2] and bits[n-1].
    (= i (- n 1))))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
-export([is_one_bit_character/1]).

-spec is_one_bit_character(Bits :: [integer()]) -> boolean().
is_one_bit_character(Bits) ->
    N = length(Bits),
    % `lists:nth` is 1-indexed, but our logic `I` is 0-indexed for array access.
    % So `lists:nth(I + 1, Bits)` gets the element at 0-indexed `I`.
    is_one_bit_character_recursive(Bits, 0, N).

is_one_bit_character_recursive(Bits, I, N) when I < N - 1 ->
    CharBit = lists:nth(I + 1, Bits),
    if
        CharBit == 1 ->
            is_one_bit_character_recursive(Bits, I + 2, N);
        true -> % CharBit == 0
            is_one_bit_character_recursive(Bits, I + 1, N)
    end;
is_one_bit_character_recursive(_Bits, I, N) ->
    % After the recursive calls, if I is exactly N - 1, it means the last character
    % started at N - 1. Since Bits[N-1] is guaranteed to be 0,
    % it must be a one-bit character.
    % If I is N, it means the last character processed was a two-bit character
    % that consumed Bits[N-2] and Bits[N-1].
    I == N - 1.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
  @spec is_one_bit_character(bits :: [integer]) :: boolean
  def is_one_bit_character(bits) do
    n = length(bits)
    i = decode_bits(bits, 0, n)

    # After the loop (recursive calls), if i is exactly n - 1, it means the last character
    # started at n - 1. Since bits[n-1] is guaranteed to be 0,
    # it must be a one-bit character.
    # If i is n, it means the last character processed was a two-bit character
    # that consumed bits[n-2] and bits[n-1].
    i == n - 1
  end

  defp decode_bits(bits, i, n) when i < n - 1 do
    current_bit = Enum.at(bits, i)
    if current_bit == 1 do
      decode_bits(bits, i + 2, n)
    else
      decode_bits(bits, i + 1, n)
    end
  end

  defp decode_bits(_bits, i, _n) do
    # Base case for recursion: i is no longer less than n - 1
    i
  end
end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) with explanation. The algorithm iterates through the `bits` array once. In each step of the `while` loop, the index `i` is incremented by either 1 (for a one-bit character) or 2 (for a two-bit character). Since `i` starts at 0 and goes up to at most `N` (where `N` is the length of the `bits` array), the loop runs a maximum of `N` iterations. Each operation inside the loop (array access, comparison, increment) takes constant time. Thus, the total time complexity is directly proportional to the length of the `bits` array, making it O(N).

- **Space Complexity:** O(1) with explanation. The algorithm uses a fixed amount of extra space, regardless of the input size. It only requires a single integer variable (`i`) to keep track of the current position in the array. No additional data structures are allocated that would scale with the input `N`. Therefore, the space complexity is O(1).

</details>


<details>
<summary><strong>⚡ Solution from llama-3.3-70b-versatile</strong></summary>

### Approach

The problem can be solved by iterating over the binary array from left to right and keeping track of the current position. If the current bit is 0, it means we have encountered a one-bit character, so we move to the next position. If the current bit is 1, it means we have encountered a two-bit character, so we move two positions forward. At the end, if we are at the second last position, it means the last character must be a one-bit character.

### Code

<div class="code-tabs">
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
class Solution {
     public:
         bool isOneBitCharacter(vector<int>& bits) {
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
             let mut i: usize = 0;
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
     is_one_bit_character([0 | Rest], I) ->
         is_one_bit_character(Rest, I + 1);
     is_one_bit_character([1, _ | Rest], I) ->
         is_one_bit_character(Rest, I + 2);
     is_one_bit_character([], I) ->
         I == length([]).
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
       def is_one_bit_character(bits) do
         is_one_bit_character(bits, 0)
       end

       defp is_one_bit_character([0 | rest], i) do
         is_one_bit_character(rest, i + 1)
       end

       defp is_one_bit_character([1, _ | rest], i) do
         is_one_bit_character(rest, i + 2)
       end

       defp is_one_bit_character([], i) do
         i == length([])
       end
     end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the binary array, because we are scanning the array once.

- **Space Complexity:** O(1) because we are using a constant amount of space to store the current position.

</details>
