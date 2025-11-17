---
layout: post
title: "Number of Substrings With Only 1s"
date: 2025-11-16 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Math", "String"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/number-of-substrings-with-only-1s/
---

## Problem #1513: Number of Substrings With Only 1s

**Difficulty:** Medium

**Topics:** Math, String

## Problem Description

Given a binary string `s`, return _the number of substrings with all characters_ `1` _'s_. Since the answer may be too large, return it modulo `109 + 7`.

**Example 1:**

``` Input: s = "0110111" Output: 9 Explanation: There are 9 substring in total with only 1's characters. "1" -> 5 times. "11" -> 3 times. "111" -> 1 time. ``` 

**Example 2:**

``` Input: s = "101" Output: 2 Explanation: Substring "1" is shown 2 times in s. ``` 

**Example 3:**

``` Input: s = "111111" Output: 21 Explanation: Each substring contains only 1's characters. ``` 

**Constraints:**

  * `1 <= s.length <= 105`
  * `s[i]` is either `'0'` or `'1'`.

## Hints

1. Count number of 1s in each consecutive-1 group. For a group with n consecutive 1s, the total contribution of it to the final answer is (n + 1) * n // 2.

## ✨ AI-Generated Solution (gemini-2.5-flash)

### Approach

The problem asks us to count the total number of substrings consisting only of '1's in a given binary string `s`. The result should be returned modulo `10^9 + 7`.

The core idea is to identify consecutive blocks of '1's. For any block of `n` consecutive '1's, say "11...1" (n times), the number of substrings with only '1's that can be formed from this block is the sum of integers from 1 to `n`. This is because we can form `n` substrings of length 1 ("1"), `n-1` substrings of length 2 ("11"), ..., and 1 substring of length `n` ("11...1"). The sum `1 + 2 + ... + n` is given by the formula `n * (n + 1) / 2`.

We can iterate through the input string `s` character by character. We maintain a `current_consecutive_ones` counter. When we encounter a '1', we increment this counter. When we encounter a '0' (or reach the end of the string), it signifies the end of a block of consecutive '1's. At this point:
1. We calculate the contribution of the just-ended block using the formula `current_consecutive_ones * (current_consecutive_ones + 1) / 2`.
2. We add this contribution to a running `total_substrings` count.
3. We reset `current_consecutive_ones` to 0 to start counting a new block.

It's important to perform the modulo operation (`% (10^9 + 7)`) after each addition to `total_substrings` to prevent integer overflow, as the sum can become very large. Also, the intermediate product `current_consecutive_ones * (current_consecutive_ones + 1)` can be up to `(10^5)^2 = 10^10`, which might exceed the capacity of a standard 32-bit integer. Therefore, `long` or `long long` (or equivalent arbitrary-precision types) should be used for `current_consecutive_ones` and `total_substrings` and the intermediate calculations to ensure correctness before applying the modulo.

After iterating through the entire string, there might be a trailing sequence of '1's (if the string ends with '1's). The algorithm correctly handles this by performing the contribution calculation one last time for any non-zero `current_consecutive_ones` count remaining after the loop finishes.

Example walk-through for `s = "0110111"`:
- `MOD = 10^9 + 7`, `total_substrings = 0`, `current_consecutive_ones = 0`
- `s[0] = '0'`: `current_consecutive_ones` is 0. No contribution. Reset `current_consecutive_ones` to 0.
- `s[1] = '1'`: `current_consecutive_ones` becomes 1.
- `s[2] = '1'`: `current_consecutive_ones` becomes 2.
- `s[3] = '0'`: End of a block of '1's. `current_consecutive_ones` is 2.
  - Contribution: `2 * (2 + 1) / 2 = 3`.
  - `total_substrings = (0 + 3) % MOD = 3`.
  - Reset `current_consecutive_ones` to 0.
- `s[4] = '1'`: `current_consecutive_ones` becomes 1.
- `s[5] = '1'`: `current_consecutive_ones` becomes 2.
- `s[6] = '1'`: `current_consecutive_ones` becomes 3.
- End of string: Remaining `current_consecutive_ones` is 3.
  - Contribution: `3 * (3 + 1) / 2 = 6`.
  - `total_substrings = (3 + 6) % MOD = 9`.
- Final result: 9.

### Code

<div class="code-tabs">
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
class Solution {
public:
    int numSub(std::string s) {
        long long MOD = 1e9 + 7;
        long long totalSubstrings = 0;
        long long currentConsecutiveOnes = 0;

        for (char c : s) {
            if (c == '1') {
                currentConsecutiveOnes++;
            } else {
                totalSubstrings = (totalSubstrings + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD;
                currentConsecutiveOnes = 0;
            }
        }
        
        // Add contributions from any trailing ones
        totalSubstrings = (totalSubstrings + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD;
        
        return static_cast<int>(totalSubstrings);
    }
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
    public int numSub(String s) {
        long MOD = 1_000_000_007;
        long totalSubstrings = 0;
        long currentConsecutiveOnes = 0;

        for (char c : s.toCharArray()) {
            if (c == '1') {
                currentConsecutiveOnes++;
            } else {
                totalSubstrings = (totalSubstrings + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD;
                currentConsecutiveOnes = 0;
            }
        }
        
        // Add contributions from any trailing ones
        totalSubstrings = (totalSubstrings + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD;
        
        return (int) totalSubstrings;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        total_substrings = 0
        current_consecutive_ones = 0

        for char in s:
            if char == '1':
                current_consecutive_ones += 1
            else:
                total_substrings = (total_substrings + current_consecutive_ones * (current_consecutive_ones + 1) // 2) % MOD
                current_consecutive_ones = 0
        
        # Add contributions from any trailing ones
        total_substrings = (total_substrings + current_consecutive_ones * (current_consecutive_ones + 1) // 2) % MOD
        
        return total_substrings
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        total_substrings = 0
        current_consecutive_ones = 0

        for char in s:
            if char == '1':
                current_consecutive_ones += 1
            else:
                total_substrings = (total_substrings + current_consecutive_ones * (current_consecutive_ones + 1) // 2) % MOD
                current_consecutive_ones = 0
        
        # Add contributions from any trailing ones
        total_substrings = (total_substrings + current_consecutive_ones * (current_consecutive_ones + 1) // 2) % MOD
        
        return total_substrings
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <string.h> // For strlen

int numSub(char * s){
    long long MOD = 1000000007;
    long long totalSubstrings = 0;
    long long currentConsecutiveOnes = 0;
    
    int len = strlen(s);
    for (int i = 0; i < len; i++) {
        if (s[i] == '1') {
            currentConsecutiveOnes++;
        } else {
            totalSubstrings = (totalSubstrings + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD;
            currentConsecutiveOnes = 0;
        }
    }
    
    // Add contributions from any trailing ones
    totalSubstrings = (totalSubstrings + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD;
    
    return (int) totalSubstrings;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
public class Solution {
    public int NumSub(string s) {
        long MOD = 1_000_000_007;
        long totalSubstrings = 0;
        long currentConsecutiveOnes = 0;

        foreach (char c in s) {
            if (c == '1') {
                currentConsecutiveOnes++;
            } else {
                totalSubstrings = (totalSubstrings + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD;
                currentConsecutiveOnes = 0;
            }
        }
        
        // Add contributions from any trailing ones
        totalSubstrings = (totalSubstrings + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD;
        
        return (int) totalSubstrings;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
/**
 * @param {string} s
 * @return {number}
 */
var numSub = function(s) {
    const MOD = 1_000_000_007;
    let totalSubstrings = 0;
    let currentConsecutiveOnes = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') {
            currentConsecutiveOnes++;
        } else {
            // Use BigInt for intermediate product to prevent overflow in JavaScript Number type.
            let contribution = (BigInt(currentConsecutiveOnes) * BigInt(currentConsecutiveOnes + 1) / 2n);
            totalSubstrings = (totalSubstrings + Number(contribution % BigInt(MOD))) % MOD;
            currentConsecutiveOnes = 0;
        }
    }
    
    // Add contributions from any trailing ones
    let contribution = (BigInt(currentConsecutiveOnes) * BigInt(currentConsecutiveOnes + 1) / 2n);
    totalSubstrings = (totalSubstrings + Number(contribution % BigInt(MOD))) % MOD;
    
    return totalSubstrings;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function numSub(s: string): number {
    const MOD: number = 1_000_000_007;
    let totalSubstrings: number = 0;
    let currentConsecutiveOnes: number = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') {
            currentConsecutiveOnes++;
        } else {
            // Use BigInt for intermediate product to prevent overflow in JavaScript Number type.
            let contribution = (BigInt(currentConsecutiveOnes) * BigInt(currentConsecutiveOnes + 1) / 2n);
            totalSubstrings = (totalSubstrings + Number(contribution % BigInt(MOD))) % MOD;
            currentConsecutiveOnes = 0;
        }
    }
    
    // Add contributions from any trailing ones
    let contribution = (BigInt(currentConsecutiveOnes) * BigInt(currentConsecutiveOnes + 1) / 2n);
    totalSubstrings = (totalSubstrings + Number(contribution % BigInt(MOD))) % MOD;
    
    return totalSubstrings;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numSub($s) {
        $MOD = 1000000007;
        $totalSubstrings = 0;
        $currentConsecutiveOnes = 0;

        for ($i = 0; $i < strlen($s); $i++) {
            if ($s[$i] == '1') {
                $currentConsecutiveOnes++;
            } else {
                // PHP integers automatically handle large numbers on 64-bit systems.
                $contribution = (int)(($currentConsecutiveOnes * ($currentConsecutiveOnes + 1)) / 2);
                $totalSubstrings = ($totalSubstrings + $contribution) % $MOD;
                $currentConsecutiveOnes = 0;
            }
        }
        
        // Add contributions from any trailing ones
        $contribution = (int)(($currentConsecutiveOnes * ($currentConsecutiveOnes + 1)) / 2);
        $totalSubstrings = ($totalSubstrings + $contribution) % $MOD;
        
        return $totalSubstrings;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution {
    func numSub(_ s: String) -> Int {
        let MOD: Int = 1_000_000_007
        var totalSubstrings: Int = 0
        var currentConsecutiveOnes: Int = 0

        for char in s {
            if char == "1" {
                currentConsecutiveOnes += 1
            } else {
                let n = currentConsecutiveOnes
                // Swift's Int is typically 64-bit on modern platforms, handling intermediate product 10^10 correctly.
                let contribution = n * (n + 1) / 2
                totalSubstrings = (totalSubstrings + contribution) % MOD
                currentConsecutiveOnes = 0
            }
        }
        
        // Add contributions from any trailing ones
        let n = currentConsecutiveOnes
        let contribution = n * (n + 1) / 2
        totalSubstrings = (totalSubstrings + contribution) % MOD
        
        return totalSubstrings
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution {
    fun numSub(s: String): Int {
        val MOD = 1_000_000_007L // Use Long for modulo constant
        var totalSubstrings: Long = 0L
        var currentConsecutiveOnes: Long = 0L // Use Long for count

        for (char in s) {
            if (char == '1') {
                currentConsecutiveOnes++
            } else {
                totalSubstrings = (totalSubstrings + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD
                currentConsecutiveOnes = 0L
            }
        }
        
        // Add contributions from any trailing ones
        totalSubstrings = (totalSubstrings + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD
        
        return totalSubstrings.toInt()
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
class Solution {
  int numSub(String s) {
    final int MOD = 1_000_000_007;
    int totalSubstrings = 0;
    int currentConsecutiveOnes = 0;

    for (int i = 0; i < s.length; i++) {
      if (s[i] == '1') {
        currentConsecutiveOnes++;
      } else {
        // Dart integers (int) have arbitrary precision on the web (JavaScript),
        // and are 64-bit signed integers on native platforms. This handles large products.
        totalSubstrings = (totalSubstrings + currentConsecutiveOnes * (currentConsecutiveOnes + 1) ~/ 2) % MOD;
        currentConsecutiveOnes = 0;
      }
    }
    
    // Add contributions from any trailing ones
    totalSubstrings = (totalSubstrings + currentConsecutiveOnes * (currentConsecutiveOnes + 1) ~/ 2) % MOD;
    
    return totalSubstrings;
  }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

func numSub(s string) int {
    const MOD = 1_000_000_007
    totalSubstrings := 0
    currentConsecutiveOnes := 0

    for _, char := range s { // range iterates over unicode runes, which is fine for ASCII '0' and '1'
        if char == '1' {
            currentConsecutiveOnes++
        } else {
            // currentConsecutiveOnes can be up to 10^5, product can be 10^10.
            // Use int64 for intermediate calculation to prevent overflow before modulo.
            contribution := int64(currentConsecutiveOnes) * int64(currentConsecutiveOnes + 1) / 2
            totalSubstrings = (totalSubstrings + int(contribution % MOD)) % MOD
            currentConsecutiveOnes = 0
        }
    }
    
    // Add contributions from any trailing ones
    contribution := int64(currentConsecutiveOnes) * int64(currentConsecutiveOnes + 1) / 2
    totalSubstrings = (totalSubstrings + int(contribution % MOD)) % MOD
    
    return totalSubstrings
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
class Solution
    def numSub(s)
        mod = 1_000_000_007
        total_substrings = 0
        current_consecutive_ones = 0

        # Ruby handles arbitrary precision integers, so no overflow concerns.
        s.each_char do |char|
            if char == '1'
                current_consecutive_ones += 1
            else
                contribution = current_consecutive_ones * (current_consecutive_ones + 1) / 2
                total_substrings = (total_substrings + contribution) % mod
                current_consecutive_ones = 0
            end
        end
        
        # Add contributions from any trailing ones
        contribution = current_consecutive_ones * (current_consecutive_ones + 1) / 2
        total_substrings = (total_substrings + contribution) % mod
        
        total_substrings
    end
end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {
    def numSub(s: String): Int = {
        val MOD: Long = 1_000_000_007L
        var totalSubstrings: Long = 0L
        var currentConsecutiveOnes: Long = 0L

        for (char <- s) {
            if (char == '1') {
                currentConsecutiveOnes += 1
            } else {
                totalSubstrings = (totalSubstrings + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD
                currentConsecutiveOnes = 0L
            }
        }
        
        // Add contributions from any trailing ones
        totalSubstrings = (totalSubstrings + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD
        
        totalSubstrings.toInt
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution {
    pub fn num_sub(s: String) -> i32 {
        let modulo: i64 = 1_000_000_007;
        let mut total_substrings: i64 = 0;
        let mut current_consecutive_ones: i64 = 0;

        for char_code in s.as_bytes() { // Iterate over bytes for ASCII chars '0' and '1'
            if *char_code == b'1' {
                current_consecutive_ones += 1;
            } else {
                // current_consecutive_ones can be up to 10^5, product can be 10^10.
                // i64 handles this intermediate product before modulo.
                let contribution = current_consecutive_ones * (current_consecutive_ones + 1) / 2;
                total_substrings = (total_substrings + contribution) % modulo;
                current_consecutive_ones = 0;
            }
        }
        
        // Add contributions from any trailing ones
        let contribution = current_consecutive_ones * (current_consecutive_ones + 1) / 2;
        total_substrings = (total_substrings + contribution) % modulo;
        
        total_substrings as i32
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket

(define (num-sub s)
  (define MOD 1000000007)
  (define total-substrings 0)
  (define current-consecutive-ones 0)

  (for ([char (string->list s)])
    (if (char=? char #\1)
        (set! current-consecutive-ones (+ current-consecutive-ones 1))
        (begin
          (set! total-substrings
                (modulo (+ total-substrings
                           (quotient (* current-consecutive-ones (+ current-consecutive-ones 1)) 2))
                        MOD))
          (set! current-consecutive-ones 0))))

  ;; Add contributions from any trailing ones
  (set! total-substrings
        (modulo (+ total-substrings
                   (quotient (* current-consecutive-ones (+ current-consecutive-ones 1)) 2))
                MOD))
  
  total-substrings)
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
-export([num_sub/1]).

num_sub(S) ->
    MOD = 1000000007,
    {TotalSubstrings, CurrentConsecutiveOnes} = lists:foldl(
        fun(Char, {AccTotal, AccOnes}) ->
            case Char of
                $1 ->
                    {AccTotal, AccOnes + 1};
                $0 ->
                    % Erlang integers have arbitrary precision, no overflow concerns.
                    Contribution = (AccOnes * (AccOnes + 1) div 2),
                    {(AccTotal + Contribution) rem MOD, 0}
            end
        end,
        {0, 0},
        S
    ),
    % Add contributions from any trailing ones
    Contribution = (CurrentConsecutiveOnes * (CurrentConsecutiveOnes + 1) div 2),
    (TotalSubstrings + Contribution) rem MOD.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
  @spec num_sub(s :: String.t) :: integer
  def num_sub(s) do
    mod = 1_000_000_007
    
    # Elixir integers have arbitrary precision, no overflow concerns.
    {total_substrings, current_consecutive_ones} = 
      String.graphemes(s) # Or String.to_charlist(s) for ASCII '0' and '1'
      |> Enum.reduce({0, 0}, fn
        "1", {acc_total, acc_ones} ->
          {acc_total, acc_ones + 1}
        "0", {acc_total, acc_ones} ->
          contribution = div(acc_ones * (acc_ones + 1), 2)
          {rem(acc_total + contribution, mod), 0}
        _, acc -> acc # Should not be reached with valid binary string input
      end)
    
    # Add contributions from any trailing ones
    contribution = div(current_consecutive_ones * (current_consecutive_ones + 1), 2)
    rem(total_substrings + contribution, mod)
  end
end
{% endhighlight %}

  </div>

</div>


### Complexity Analysis

- **Time Complexity:** O(N)

- **Space Complexity:** O(1)
