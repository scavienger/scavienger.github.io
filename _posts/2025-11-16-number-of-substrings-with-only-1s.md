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

The problem asks us to count the total number of substrings consisting only of '1's in a given binary string `s`, returning the result modulo `10^9 + 7`. 

The core idea is to process the string and identify consecutive blocks of '1's. Any '0' character acts as a separator between such blocks.

Consider a contiguous block of `n` ones, for example, "11...1" (`n` times). The substrings consisting only of '1's that can be formed from this block are:
- `n` substrings of length 1 ("1")
- `n-1` substrings of length 2 ("11")
- ...
- `1` substring of length `n` ("1...1")

The total number of such substrings for a block of `n` consecutive '1's is the sum `n + (n-1) + ... + 1`. This sum is given by the arithmetic series formula: `n * (n + 1) / 2`.

**Algorithm:**
1. Initialize `total_count` to 0. This variable will store the cumulative sum of substrings, modulo `10^9 + 7`.
2. Initialize `current_consecutive_ones` to 0. This variable will keep track of the length of the current block of consecutive '1's being processed.
3. Define `MOD = 10^9 + 7`.
4. Iterate through each character `char_s` in the input string `s`:
   a. If `char_s` is '1', increment `current_consecutive_ones`.
   b. If `char_s` is '0', it signifies the end of a block of '1's (if `current_consecutive_ones > 0`). At this point, calculate the contribution of this finished block to the `total_count` using the formula `current_consecutive_ones * (current_consecutive_ones + 1) / 2`. Add this contribution to `total_count` and take the result modulo `MOD`. Then, reset `current_consecutive_ones` to 0 to start counting a new potential block.
5. After the loop finishes, there might be a trailing block of '1's (i.e., `s` ends with '1's). So, perform the same calculation for `current_consecutive_ones` one last time and add its contribution to `total_count` modulo `MOD`.
6. Return `total_count`.

**Example Walkthrough (`s = "0110111"`):**
- Initialize `total_count = 0`, `current_consecutive_ones = 0`.
- `s[0] = '0'`: `current_consecutive_ones` is 0. No contribution. Reset `current_consecutive_ones = 0`.
- `s[1] = '1'`: `current_consecutive_ones = 1`.
- `s[2] = '1'`: `current_consecutive_ones = 2`.
- `s[3] = '0'`: End of a block of 2 '1's. Contribution = `2 * (2 + 1) / 2 = 3`. `total_count = (0 + 3) % MOD = 3`. Reset `current_consecutive_ones = 0`.
- `s[4] = '1'`: `current_consecutive_ones = 1`.
- `s[5] = '1'`: `current_consecutive_ones = 2`.
- `s[6] = '1'`: `current_consecutive_ones = 3`.
- End of string. `current_consecutive_ones` is 3. Contribution = `3 * (3 + 1) / 2 = 6`. `total_count = (3 + 6) % MOD = 9`.
- Return `9`.

The intermediate product `current_consecutive_ones * (current_consecutive_ones + 1)` can be up to `10^5 * (10^5 + 1) \approx 10^{10}`, which requires a 64-bit integer type (like `long long` in C++ or `long` in Java/C#) to avoid overflow before the division by 2. The result of the division, `n * (n+1) / 2`, will then be taken modulo `MOD` to keep the `total_count` within bounds.

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
```cpp
#include <string>
#include <iostream>

class Solution {
public:
    int numSub(std::string s) {
        long long total_count = 0;
        long long current_consecutive_ones = 0;
        long long MOD = 1e9 + 7;

        for (char c : s) {
            if (c == '1') {
                current_consecutive_ones++;
            } else {
                // End of a block of '1's
                // Add the sum 1 + 2 + ... + current_consecutive_ones
                total_count = (total_count + (current_consecutive_ones * (current_consecutive_ones + 1) / 2)) % MOD;
                current_consecutive_ones = 0;
            }
        }

        // Add the contribution of any trailing block of '1's
        total_count = (total_count + (current_consecutive_ones * (current_consecutive_ones + 1) / 2)) % MOD;

        return static_cast<int>(total_count);
    }
};
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
```java
class Solution {
    public int numSub(String s) {
        long totalCount = 0;
        long currentConsecutiveOnes = 0;
        long MOD = 1_000_000_007;

        for (char c : s.toCharArray()) {
            if (c == '1') {
                currentConsecutiveOnes++;
            } else {
                // End of a block of '1's
                // Add the sum 1 + 2 + ... + currentConsecutiveOnes
                totalCount = (totalCount + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD;
                currentConsecutiveOnes = 0;
            }
        }

        // Add the contribution of any trailing block of '1's
        totalCount = (totalCount + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD;

        return (int) totalCount;
    }
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
```python
class Solution:
    def numSub(self, s: str) -> int:
        total_count = 0
        current_consecutive_ones = 0
        MOD = 10**9 + 7

        for char_s in s:
            if char_s == '1':
                current_consecutive_ones += 1
            else:
                # End of a block of '1's
                # Add the sum 1 + 2 + ... + current_consecutive_ones
                total_count = (total_count + current_consecutive_ones * (current_consecutive_ones + 1) // 2) % MOD
                current_consecutive_ones = 0
        
        # Add the contribution of any trailing block of '1's
        total_count = (total_count + current_consecutive_ones * (current_consecutive_ones + 1) // 2) % MOD

        return total_count
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
```python
class Solution:
    def numSub(self, s: str) -> int:
        total_count = 0
        current_consecutive_ones = 0
        MOD = 10**9 + 7

        for char_s in s:
            if char_s == '1':
                current_consecutive_ones += 1
            else:
                # End of a block of '1's
                # Add the sum 1 + 2 + ... + current_consecutive_ones
                total_count = (total_count + current_consecutive_ones * (current_consecutive_ones + 1) // 2) % MOD
                current_consecutive_ones = 0
        
        # Add the contribution of any trailing block of '1's
        total_count = (total_count + current_consecutive_ones * (current_consecutive_ones + 1) // 2) % MOD

        return total_count
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
```c
#include <string.h>

int numSub(char* s) {
    long long total_count = 0;
    long long current_consecutive_ones = 0;
    long long MOD = 1e9 + 7;

    int len = strlen(s);
    for (int i = 0; i < len; i++) {
        if (s[i] == '1') {
            current_consecutive_ones++;
        } else {
            // End of a block of '1's
            // Add the sum 1 + 2 + ... + current_consecutive_ones
            total_count = (total_count + (current_consecutive_ones * (current_consecutive_ones + 1) / 2)) % MOD;
            current_consecutive_ones = 0;
        }
    }

    // Add the contribution of any trailing block of '1's
    total_count = (total_count + (current_consecutive_ones * (current_consecutive_ones + 1) / 2)) % MOD;

    return (int) total_count;
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
```csharp
using System;

public class Solution {
    public int NumSub(string s) {
        long totalCount = 0;
        long currentConsecutiveOnes = 0;
        long MOD = 1_000_000_007;

        foreach (char c in s) {
            if (c == '1') {
                currentConsecutiveOnes++;
            } else {
                // End of a block of '1's
                // Add the sum 1 + 2 + ... + currentConsecutiveOnes
                totalCount = (totalCount + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD;
                currentConsecutiveOnes = 0;
            }
        }

        // Add the contribution of any trailing block of '1's
        totalCount = (totalCount + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD;

        return (int) totalCount;
    }
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numSub = function(s) {
    let totalCount = 0;
    let currentConsecutiveOnes = 0;
    const MOD = 1_000_000_007;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') {
            currentConsecutiveOnes++;
        } else {
            // End of a block of '1's
            // Add the sum 1 + 2 + ... + currentConsecutiveOnes
            totalCount = (totalCount + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD;
            currentConsecutiveOnes = 0;
        }
    }

    // Add the contribution of any trailing block of '1's
    totalCount = (totalCount + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD;

    return totalCount;
};
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
```typescript
function numSub(s: string): number {
    let totalCount: number = 0;
    let currentConsecutiveOnes: number = 0;
    const MOD: number = 1_000_000_007;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') {
            currentConsecutiveOnes++;
        } else {
            // End of a block of '1's
            // Add the sum 1 + 2 + ... + currentConsecutiveOnes
            totalCount = (totalCount + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD;
            currentConsecutiveOnes = 0;
        }
    }

    // Add the contribution of any trailing block of '1's
    totalCount = (totalCount + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD;

    return totalCount;
};
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numSub($s) {
        $totalCount = 0;
        $currentConsecutiveOnes = 0;
        $MOD = 1_000_000_007;

        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === '1') {
                $currentConsecutiveOnes++;
            } else {
                // End of a block of '1's
                // Add the sum 1 + 2 + ... + currentConsecutiveOnes
                $totalCount = ($totalCount + $currentConsecutiveOnes * ($currentConsecutiveOnes + 1) / 2) % $MOD;
                $currentConsecutiveOnes = 0;
            }
        }

        // Add the contribution of any trailing block of '1's
        $totalCount = ($totalCount + $currentConsecutiveOnes * ($currentConsecutiveOnes + 1) / 2) % $MOD;

        return $totalCount;
    }
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
```swift
class Solution {
    func numSub(_ s: String) -> Int {
        var totalCount: Int = 0
        var currentConsecutiveOnes: Int = 0
        let MOD: Int = 1_000_000_007

        for char in s {
            if char == "1" {
                currentConsecutiveOnes += 1
            } else {
                // End of a block of '1's
                // Add the sum 1 + 2 + ... + currentConsecutiveOnes
                totalCount = (totalCount + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD
                currentConsecutiveOnes = 0
            }
        }

        // Add the contribution of any trailing block of '1's
        totalCount = (totalCount + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD

        return totalCount
    }
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
```kotlin
class Solution {
    fun numSub(s: String): Int {
        var totalCount: Long = 0
        var currentConsecutiveOnes: Long = 0
        val MOD: Long = 1_000_000_007

        for (char in s) {
            if (char == '1') {
                currentConsecutiveOnes++
            } else {
                // End of a block of '1's
                // Add the sum 1 + 2 + ... + currentConsecutiveOnes
                totalCount = (totalCount + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD
                currentConsecutiveOnes = 0
            }
        }

        // Add the contribution of any trailing block of '1's
        totalCount = (totalCount + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD

        return totalCount.toInt()
    }
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
```dart
class Solution {
  int numSub(String s) {
    int totalCount = 0;
    int currentConsecutiveOnes = 0;
    final int MOD = 1000000007;

    for (int i = 0; i < s.length; i++) {
      if (s[i] == '1') {
        currentConsecutiveOnes++;
      } else {
        // End of a block of '1's
        // Add the sum 1 + 2 + ... + currentConsecutiveOnes
        totalCount = (totalCount + currentConsecutiveOnes * (currentConsecutiveOnes + 1) ~/ 2) % MOD;
        currentConsecutiveOnes = 0;
      }
    }

    // Add the contribution of any trailing block of '1's
    totalCount = (totalCount + currentConsecutiveOnes * (currentConsecutiveOnes + 1) ~/ 2) % MOD;

    return totalCount;
  }
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
```go
package main

import "fmt"

func numSub(s string) int {
    var totalCount int = 0
    var currentConsecutiveOnes int = 0
    var MOD int = 1_000_000_007

    for _, char := range s {
        if char == '1' {
            currentConsecutiveOnes++
        } else {
            // End of a block of '1's
            // Add the sum 1 + 2 + ... + currentConsecutiveOnes
            totalCount = (totalCount + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD
            currentConsecutiveOnes = 0
        }
    }

    // Add the contribution of any trailing block of '1's
    totalCount = (totalCount + currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2) % MOD

    return totalCount
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
```ruby
# @param {String} s
# @return {Integer}
def num_sub(s)
    total_count = 0
    current_consecutive_ones = 0
    mod = 1_000_000_007

    s.each_char do |char_s|
        if char_s == '1'
            current_consecutive_ones += 1
        else
            # End of a block of '1's
            # Add the sum 1 + 2 + ... + current_consecutive_ones
            total_count = (total_count + current_consecutive_ones * (current_consecutive_ones + 1) / 2) % mod
            current_consecutive_ones = 0
        end
    end

    # Add the contribution of any trailing block of '1's
    total_count = (total_count + current_consecutive_ones * (current_consecutive_ones + 1) / 2) % mod

    total_count
end
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
```scala
object Solution {
    def numSub(s: String): Int = {
        var totalCount: Long = 0
        var currentConsecutiveOnes: Long = 0
        val MOD: Long = 1_000_000_007

        for (char <- s) {
            if (char == '1') {
                currentConsecutiveOnes += 1
            } else {
                // End of a block of '1's
                // Add the sum 1 + 2 + ... + currentConsecutiveOnes
                totalCount = (totalCount + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD
                currentConsecutiveOnes = 0
            }
        }

        // Add the contribution of any trailing block of '1's
        totalCount = (totalCount + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD

        totalCount.toInt
    }
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
```rust
impl Solution {
    pub fn num_sub(s: String) -> i32 {
        let mut total_count: i64 = 0;
        let mut current_consecutive_ones: i64 = 0;
        let modular: i64 = 1_000_000_007;

        for c in s.chars() {
            if c == '1' {
                current_consecutive_ones += 1;
            } else {
                // End of a block of '1's
                // Add the sum 1 + 2 + ... + current_consecutive_ones
                total_count = (total_count + (current_consecutive_ones * (current_consecutive_ones + 1) / 2)) % modular;
                current_consecutive_ones = 0;
            }
        }

        // Add the contribution of any trailing block of '1's
        total_count = (total_count + (current_consecutive_ones * (current_consecutive_ones + 1) / 2)) % modular;

        total_count as i32
    }
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
```racket
#lang racket

(define (num-sub s)
  (define mod 1000000007)
  (define total-count 0)
  (define current-consecutive-ones 0)

  (for ([char (string->list s)])
    (when (char=? char #\1)
      (set! current-consecutive-ones (+ current-consecutive-ones 1)))
    (when (char=? char #\0)
      (set! total-count (modulo (+ total-count (quotient (* current-consecutive-ones (+ current-consecutive-ones 1)) 2)) mod))
      (set! current-consecutive-ones 0)))

  ; Add the contribution of any trailing block of '1's
  (set! total-count (modulo (+ total-count (quotient (* current-consecutive-ones (+ current-consecutive-ones 1)) 2)) mod))

  total-count)

(provide num-sub)

; Example usage (for testing, not part of LeetCode submission)
; (module+ test
;   (require rackunit)
;   (check-equal? (num-sub "0110111") 9)
;   (check-equal? (num-sub "101") 2)
;   (check-equal? (num-sub "111111") 21)
;   (check-equal? (num-sub "000") 0)
;   (check-equal? (num-sub "1") 1))
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
```erlang
-module(solution).
-export([num_sub/1]).

num_sub(S) ->
    MOD = 1000000007,
    {TotalCount, CurrentConsecutiveOnes} = lists:foldl(
        fun(Char, {AccTotal, AccCurrent}) ->
            case Char of
                $1 ->
                    {AccTotal, AccCurrent + 1};
                $0 ->
                    Contribution = (AccCurrent * (AccCurrent + 1) div 2),
                    {(AccTotal + Contribution) rem MOD, 0}
            end
        end,
        {0, 0},
        S
    ),
    FinalContribution = (CurrentConsecutiveOnes * (CurrentConsecutiveOnes + 1) div 2),
    (TotalCount + FinalContribution) rem MOD.
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
```elixir
defmodule Solution do
  @spec num_sub(s :: String.t) :: integer
  def num_sub(s) do
    mod = 1_000_000_007

    {total_count, current_consecutive_ones} = Enum.reduce(String.graphemes(s), {0, 0}, fn
      "1", {acc_total, acc_current} ->
        {acc_total, acc_current + 1}
      "0", {acc_total, acc_current} ->
        contribution = div(acc_current * (acc_current + 1), 2)
        {rem(acc_total + contribution, mod), 0}
    end)

    # Add the contribution of any trailing block of '1's
    final_contribution = div(current_consecutive_ones * (current_consecutive_ones + 1), 2)
    rem(total_count + final_contribution, mod)
  end
end
```
{% endhighlight %}

  </div>

</div>


### Complexity Analysis

- **Time Complexity:** O(N)

- **Space Complexity:** O(1)
