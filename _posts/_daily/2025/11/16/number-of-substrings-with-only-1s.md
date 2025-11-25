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

<p>Given a binary string <code>s</code>, return <em>the number of substrings with all characters</em> <code>1</code><em>&#39;s</em>. Since the answer may be too large, return it modulo <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;0110111&quot;
<strong>Output:</strong> 9
<strong>Explanation:</strong> There are 9 substring in total with only 1&#39;s characters.
&quot;1&quot; -&gt; 5 times.
&quot;11&quot; -&gt; 3 times.
&quot;111&quot; -&gt; 1 time.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;101&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> Substring &quot;1&quot; is shown 2 times in s.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;111111&quot;
<strong>Output:</strong> 21
<strong>Explanation:</strong> Each substring contains only 1&#39;s characters.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>


## Hints

1. Count number of 1s in each consecutive-1 group. For a group with n consecutive 1s, the total contribution of it to the final answer is (n + 1) * n // 2.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-20 20:08:36 UTC)</small>
</summary>

<div class="ai-solution-content">

{% raw %}

### Approach

The problem asks us to count the total number of substrings within a given binary string `s` that consist solely of '1's. Since the total count can be very large, we need to return the result modulo `10^9 + 7`. 

The core insight to solve this problem efficiently comes from observing how many substrings composed entirely of '1's can be formed from a contiguous block of '1's. Consider a block of `n` consecutive '1's. For instance: 
- If `n=1` ("1"), there is 1 substring ("1"). 
- If `n=2` ("11"), there are 3 substrings ("1", "1", "11"). 
- If `n=3` ("111"), there are 6 substrings ("1", "1", "1", "11", "11", "111"). 
This pattern reveals that a block of `n` consecutive '1's contributes `1 + 2 + ... + n` substrings to the total count. This is the sum of the first `n` natural numbers, which can be calculated using the formula `n * (n + 1) / 2`. 

Our strategy is to iterate through the input string `s` character by character. We maintain a counter, `current_consecutive_ones`, which tracks the length of the current contiguous block of '1's. When we encounter a '1', we increment this counter. If we encounter a '0' (or reach the end of the string), it signifies the end of the current block of '1's. At this point, we calculate the contribution of this completed block using the formula `current_consecutive_ones * (current_consecutive_ones + 1) / 2` and add it to our running total, `total_substrings`. After processing a '0', we reset `current_consecutive_ones` to 0 to start counting a new potential block.

After iterating through the entire string, there might be a final block of '1's if the string ends with one or more '1's. Therefore, we perform one last calculation and addition for any remaining `current_consecutive_ones`. All additions to `total_substrings` must be done modulo `10^9 + 7` to prevent integer overflow and ensure the final result is within the required range. For languages with fixed-size integers (like C++, Java, C#), it's important to use 64-bit integer types (e.g., `long long` in C++, `long` in Java/C#) for `current_consecutive_ones` and `total_substrings` during intermediate calculations, as `n * (n + 1) / 2` can exceed the maximum value of a 32-bit integer if `n` is large (e.g., `10^5`). Python, JavaScript, PHP, Ruby, etc., handle large integers automatically.

{% endraw %}

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
    int numSub(std::string s) {
        long long total_substrings = 0;
        long long current_consecutive_ones = 0;
        long long MOD = 1e9 + 7;

        for (char c : s) {
            if (c == '1') {
                current_consecutive_ones++;
            } else {
                // Block of '1's ended. Calculate its contribution.
                // sum = n * (n + 1) / 2
                total_substrings = (total_substrings + (current_consecutive_ones * (current_consecutive_ones + 1) / 2)) % MOD;
                current_consecutive_ones = 0;
            }
        }

        // After the loop, add the contribution of any trailing block of '1's
        total_substrings = (total_substrings + (current_consecutive_ones * (current_consecutive_ones + 1) / 2)) % MOD;

        return static_cast<int>(total_substrings);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int numSub(String s) {
        long totalSubstrings = 0;
        long currentConsecutiveOnes = 0;
        long MOD = 1_000_000_007;

        for (char c : s.toCharArray()) {
            if (c == '1') {
                currentConsecutiveOnes++;
            } else {
                // Block of '1's ended. Calculate its contribution.
                // sum = n * (n + 1) / 2
                totalSubstrings = (totalSubstrings + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD;
                currentConsecutiveOnes = 0;
            }
        }

        // After the loop, add the contribution of any trailing block of '1's
        totalSubstrings = (totalSubstrings + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD;

        return (int)totalSubstrings;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def numSub(self, s: str) -> int:
        total_substrings = 0
        current_consecutive_ones = 0
        MOD = 10**9 + 7

        for char in s:
            if char == '1':
                current_consecutive_ones += 1
            else:
                # Block of '1's ended. Calculate its contribution.
                # sum = n * (n + 1) / 2
                total_substrings = (total_substrings + (current_consecutive_ones * (current_consecutive_ones + 1) // 2)) % MOD
                current_consecutive_ones = 0

        # After the loop, add the contribution of any trailing block of '1's
        total_substrings = (total_substrings + (current_consecutive_ones * (current_consecutive_ones + 1) // 2)) % MOD

        return total_substrings
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numSub(self, s: str) -> int:
        total_substrings = 0
        current_consecutive_ones = 0
        MOD = 10**9 + 7

        for char in s:
            if char == '1':
                current_consecutive_ones += 1
            else:
                # Block of '1's ended. Calculate its contribution.
                # sum = n * (n + 1) / 2
                total_substrings = (total_substrings + (current_consecutive_ones * (current_consecutive_ones + 1) // 2)) % MOD
                current_consecutive_ones = 0

        # After the loop, add the contribution of any trailing block of '1's
        total_substrings = (total_substrings + (current_consecutive_ones * (current_consecutive_ones + 1) // 2)) % MOD

        return total_substrings
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>

// Assuming the input string s is passed as a char* and its length is known.
// For LeetCode, it's typically within a function like `int numSub(char* s)`.
// Need to define it within the context of a solution structure if submitting to LeetCode, 
// or just the function if testing locally.

int numSub(char* s) {
    long long total_substrings = 0;
    long long current_consecutive_ones = 0;
    long long MOD = 1000000007;
    int i = 0;

    while (s[i] != '\0') {
        if (s[i] == '1') {
            current_consecutive_ones++;
        } else {
            // Block of '1's ended. Calculate its contribution.
            // sum = n * (n + 1) / 2
            total_substrings = (total_substrings + (current_consecutive_ones * (current_consecutive_ones + 1) / 2)) % MOD;
            current_consecutive_ones = 0;
        }
        i++;
    }

    // After the loop, add the contribution of any trailing block of '1's
    total_substrings = (total_substrings + (current_consecutive_ones * (current_consecutive_ones + 1) / 2)) % MOD;

    return (int)total_substrings;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int NumSub(string s) {
        long totalSubstrings = 0;
        long currentConsecutiveOnes = 0;
        long MOD = 1_000_000_007;

        foreach (char c in s) {
            if (c == '1') {
                currentConsecutiveOnes++;
            } else {
                // Block of '1's ended. Calculate its contribution.
                // sum = n * (n + 1) / 2
                totalSubstrings = (totalSubstrings + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD;
                currentConsecutiveOnes = 0;
            }
        }

        // After the loop, add the contribution of any trailing block of '1's
        totalSubstrings = (totalSubstrings + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD;

        return (int)totalSubstrings;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} s
 * @return {number}
 */
var numSub = function(s) {
    let totalSubstrings = 0;
    let currentConsecutiveOnes = 0;
    const MOD = 10**9 + 7;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') {
            currentConsecutiveOnes++;
        } else {
            // Block of '1's ended. Calculate its contribution.
            // sum = n * (n + 1) / 2
            totalSubstrings = (totalSubstrings + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD;
            currentConsecutiveOnes = 0;
        }
    }

    // After the loop, add the contribution of any trailing block of '1's
    totalSubstrings = (totalSubstrings + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD;

    return totalSubstrings;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numSub(s: string): number {
    let totalSubstrings: number = 0;
    let currentConsecutiveOnes: number = 0;
    const MOD: number = 10**9 + 7;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') {
            currentConsecutiveOnes++;
        } else {
            // Block of '1's ended. Calculate its contribution.
            // sum = n * (n + 1) / 2
            totalSubstrings = (totalSubstrings + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD;
            currentConsecutiveOnes = 0;
        }
    }

    // After the loop, add the contribution of any trailing block of '1's
    totalSubstrings = (totalSubstrings + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD;

    return totalSubstrings;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function numSub($s) {
        $totalSubstrings = 0;
        $currentConsecutiveOnes = 0;
        $MOD = 10**9 + 7;

        $length = strlen($s);
        for ($i = 0; $i < $length; $i++) {
            if ($s[$i] === '1') {
                $currentConsecutiveOnes++;
            } else {
                // Block of '1's ended. Calculate its contribution.
                // sum = n * (n + 1) / 2
                $contribution = ($currentConsecutiveOnes * ($currentConsecutiveOnes + 1) / 2);
                $totalSubstrings = ($totalSubstrings + $contribution) % $MOD;
                $currentConsecutiveOnes = 0;
            }
        }

        // After the loop, add the contribution of any trailing block of '1's
        $contribution = ($currentConsecutiveOnes * ($currentConsecutiveOnes + 1) / 2);
        $totalSubstrings = ($totalSubstrings + $contribution) % $MOD;

        return $totalSubstrings;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func numSub(_ s: String) -> Int {
        var totalSubstrings: Int = 0
        var currentConsecutiveOnes: Int = 0
        let MOD: Int = 1_000_000_007

        for char in s {
            if char == "1" {
                currentConsecutiveOnes += 1
            } else {
                // Block of '1's ended. Calculate its contribution.
                // sum = n * (n + 1) / 2
                totalSubstrings = (totalSubstrings + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD
                currentConsecutiveOnes = 0
            }
        }

        // After the loop, add the contribution of any trailing block of '1's
        totalSubstrings = (totalSubstrings + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD

        return totalSubstrings
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun numSub(s: String): Int {
        var totalSubstrings: Long = 0
        var currentConsecutiveOnes: Long = 0
        val MOD: Long = 1_000_000_007

        for (char in s) {
            if (char == '1') {
                currentConsecutiveOnes++
            } else {
                // Block of '1's ended. Calculate its contribution.
                // sum = n * (n + 1) / 2
                totalSubstrings = (totalSubstrings + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD
                currentConsecutiveOnes = 0
            }
        }

        // After the loop, add the contribution of any trailing block of '1's
        totalSubstrings = (totalSubstrings + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD

        return totalSubstrings.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int numSub(String s) {
    int totalSubstrings = 0;
    int currentConsecutiveOnes = 0;
    final int MOD = 1000000007;

    for (int i = 0; i < s.length; i++) {
      if (s[i] == '1') {
        currentConsecutiveOnes++;
      } else {
        // Block of '1's ended. Calculate its contribution.
        // sum = n * (n + 1) / 2
        totalSubstrings = (totalSubstrings + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) ~/ 2)) % MOD;
        currentConsecutiveOnes = 0;
      }
    }

    // After the loop, add the contribution of any trailing block of '1's
    totalSubstrings = (totalSubstrings + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) ~/ 2)) % MOD;

    return totalSubstrings;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func numSub(s string) int {
    var totalSubstrings int = 0
    var currentConsecutiveOnes int = 0
    const MOD int = 1e9 + 7

    for _, char := range s {
        if char == '1' {
            currentConsecutiveOnes++
        } else {
            // Block of '1's ended. Calculate its contribution.
            // sum = n * (n + 1) / 2
            totalSubstrings = (totalSubstrings + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD
            currentConsecutiveOnes = 0
        }
    }

    // After the loop, add the contribution of any trailing block of '1's
    totalSubstrings = (totalSubstrings + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD

    return totalSubstrings
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    /**
     * @param {string} s
     * @return {number}
     */
    def numSub(s)
        total_substrings = 0
        current_consecutive_ones = 0
        mod = 10**9 + 7

        s.each_char do |char|
            if char == '1'
                current_consecutive_ones += 1
            else
                # Block of '1's ended. Calculate its contribution.
                # sum = n * (n + 1) / 2
                total_substrings = (total_substrings + (current_consecutive_ones * (current_consecutive_ones + 1) / 2)) % mod
                current_consecutive_ones = 0
            end
        end

        # After the loop, add the contribution of any trailing block of '1's
        total_substrings = (total_substrings + (current_consecutive_ones * (current_consecutive_ones + 1) / 2)) % mod

        return total_substrings
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def numSub(s: String): Int = {
        var totalSubstrings: Long = 0
        var currentConsecutiveOnes: Long = 0
        val MOD: Long = 1_000_000_007

        for (char <- s) {
            if (char == '1') {
                currentConsecutiveOnes += 1
            } else {
                // Block of '1's ended. Calculate its contribution.
                // sum = n * (n + 1) / 2
                totalSubstrings = (totalSubstrings + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD
                currentConsecutiveOnes = 0
            }
        }

        // After the loop, add the contribution of any trailing block of '1's
        totalSubstrings = (totalSubstrings + (currentConsecutiveOnes * (currentConsecutiveOnes + 1) / 2)) % MOD

        totalSubstrings.toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn num_sub(s: String) -> i32 {
        let mut total_substrings: i64 = 0;
        let mut current_consecutive_ones: i64 = 0;
        let mod_val: i64 = 1_000_000_007;

        for char_val in s.chars() {
            if char_val == '1' {
                current_consecutive_ones += 1;
            } else {
                // Block of '1's ended. Calculate its contribution.
                // sum = n * (n + 1) / 2
                total_substrings = (total_substrings + (current_consecutive_ones * (current_consecutive_ones + 1) / 2)) % mod_val;
                current_consecutive_ones = 0;
            }
        }

        // After the loop, add the contribution of any trailing block of '1's
        total_substrings = (total_substrings + (current_consecutive_ones * (current_consecutive_ones + 1) / 2)) % mod_val;

        total_substrings as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (num-sub s)
  (define mod 1000000007)
  (define total-substrings 0)
  (define current-consecutive-ones 0)

  (for ([char (string->list s)])
    (if (char=? char #\1)
        (set! current-consecutive-ones (+ current-consecutive-ones 1))
        (begin
          ; Block of '1's ended. Calculate its contribution.
          ; sum = n * (n + 1) / 2
          (set! total-substrings (modulo (+ total-substrings (quotient (* current-consecutive-ones (+ current-consecutive-ones 1)) 2)) mod))
          (set! current-consecutive-ones 0))))

  ; After the loop, add the contribution of any trailing block of '1's
  (set! total-substrings (modulo (+ total-substrings (quotient (* current-consecutive-ones (+ current-consecutive-ones 1)) 2)) mod))

  total-substrings)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([num_sub/1]).

num_sub(S) ->
    Mod = 1000000007,
    {\f(Char, {TotalSubstrings, CurrentConsecutiveOnes}) ->
        if
            Char == $1 ->
                {TotalSubstrings, CurrentConsecutiveOnes + 1};
            true ->
                Contribution = (CurrentConsecutiveOnes * (CurrentConsecutiveOnes + 1) div 2),
                { (TotalSubstrings + Contribution) rem Mod, 0}
        end
    end, S, {0, 0}) \}.
    (fun({Total, Current}) ->
        Contribution = (Current * (Current + 1) div 2),
        (Total + Contribution) rem Mod
    end).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec num_sub(s :: String.t) :: integer
  def num_sub(s) do
    mod = 1_000_000_007

    {total_substrings, current_consecutive_ones} = 
      Enum.reduce(String.graphemes(s), {0, 0}, fn char, {total, current} ->
        if char == "1" do
          {total, current + 1}
        else
          # Block of '1's ended. Calculate its contribution.
          # sum = n * (n + 1) / 2
          contribution = (current * (current + 1)) |> div(2)
          {rem(total + contribution, mod), 0}
        end
      end)

    # After the loop, add the contribution of any trailing block of '1's
    contribution = (current_consecutive_ones * (current_consecutive_ones + 1)) |> div(2)
    rem(total_substrings + contribution, mod)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N)

- **Space Complexity:** O(1)

</div>
</details>


<hr class="ai-solution-separator">


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-20 20:08:44 UTC)</small>
</summary>

<div class="ai-solution-content">

{% raw %}

### Approach

The problem can be solved by counting the number of consecutive 1s in the binary string and then calculating the total number of substrings that can be formed from these consecutive 1s. We will iterate over the string and whenever we encounter a '1', we will increment a counter. If we encounter a '0', we will calculate the total number of substrings that can be formed from the previous consecutive 1s and add it to the total count. We will use the formula (n + 1) * n // 2 to calculate the total number of substrings for each group of consecutive 1s, where n is the number of consecutive 1s. This formula is derived from the fact that for a group of n consecutive 1s, we can form n substrings of length 1, n-1 substrings of length 2, n-2 substrings of length 3, and so on, until 1 substring of length n. The sum of the first n natural numbers is given by the formula n * (n + 1) // 2, which is used to calculate the total number of substrings for each group of consecutive 1s.

The time complexity of this approach is O(n), where n is the length of the binary string, because we are iterating over the string once. The space complexity is O(1), because we are using a constant amount of space to store the count of consecutive 1s and the total count of substrings.

We will also handle the case where the string ends with one or more '1's, by calculating the total number of substrings for the last group of consecutive 1s after the loop ends.

We will use the modulo operator to ensure that the total count of substrings does not exceed the maximum limit of 10^9 + 7.

{% endraw %}

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
class Solution {
public:
    int numSub(string s) {
        int MOD = 1e9 + 7;
        int count = 0;
        int total = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '1') {
                count++;
            } else {
                total = (total + (count + 1) * count / 2) % MOD;
                count = 0;
            }
        }
        total = (total + (count + 1) * count / 2) % MOD;
        return total;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
public class Solution {
    public int numSub(String s) {
        int MOD = (int)1e9 + 7;
        int count = 0;
        int total = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                count++;
            } else {
                total = (total + (count + 1) * count / 2) % MOD;
                count = 0;
            }
        }
        total = (total + (count + 1) * count / 2) % MOD;
        return total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        total = 0
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            else:
                total = (total + (count + 1) * count // 2) % MOD
                count = 0
        total = (total + (count + 1) * count // 2) % MOD
        return total
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        total = 0
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            else:
                total = (total + (count + 1) * count // 2) % MOD
                count = 0
        total = (total + (count + 1) * count // 2) % MOD
        return total
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <string.h>

int numSub(char * s) {
    int MOD = 1e9 + 7;
    int count = 0;
    int total = 0;
    for (int i = 0; i < strlen(s); i++) {
        if (s[i] == '1') {
            count++;
        } else {
            total = (total + (count + 1) * count / 2) % MOD;
            count = 0;
        }
    }
    total = (total + (count + 1) * count / 2) % MOD;
    return total;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int NumSub(string s) {
        int MOD = (int)1e9 + 7;
        int count = 0;
        int total = 0;
        for (int i = 0; i < s.Length; i++) {
            if (s[i] == '1') {
                count++;
            } else {
                total = (total + (count + 1) * count / 2) % MOD;
                count = 0;
            }
        }
        total = (total + (count + 1) * count / 2) % MOD;
        return total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var numSub = function(s) {
    let MOD = 1e9 + 7;
    let count = 0;
    let total = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') {
            count++;
        } else {
            total = (total + (count + 1) * count / 2) % MOD;
            count = 0;
        }
    }
    total = (total + (count + 1) * count / 2) % MOD;
    return total;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numSub(s: string): number {
    let MOD: number = 1e9 + 7;
    let count: number = 0;
    let total: number = 0;
    for (let i: number = 0; i < s.length; i++) {
        if (s[i] === '1') {
            count++;
        } else {
            total = (total + (count + 1) * count / 2) % MOD;
            count = 0;
        }
    }
    total = (total + (count + 1) * count / 2) % MOD;
    return total;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function numSub($s) {
        $MOD = 1e9 + 7;
        $count = 0;
        $total = 0;
        for ($i = 0; $i < strlen($s); $i++) {
            if ($s[$i] == '1') {
                $count++;
            } else {
                $total = ($total + (int)(($count + 1) * $count / 2)) % $MOD;
                $count = 0;
            }
        }
        $total = ($total + (int)(($count + 1) * $count / 2)) % $MOD;
        return $total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func numSub(_ s: String) -> Int {
        let MOD: Int = Int(1e9) + 7
        var count: Int = 0
        var total: Int = 0
        for i in s.indices {
            if s[i] == "1" {
                count += 1
            } else {
                total = (total + (count + 1) * count / 2) % MOD
                count = 0
            }
        }
        total = (total + (count + 1) * count / 2) % MOD
        return total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun numSub(s: String): Int {
        val MOD: Int = (1e9 + 7).toInt()
        var count: Int = 0
        var total: Int = 0
        for (i in s.indices) {
            if (s[i] == '1') {
                count++
            } else {
                total = (total + (count + 1) * count / 2) % MOD
                count = 0
            }
        }
        total = (total + (count + 1) * count / 2) % MOD
        return total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int numSub(String s) {
        int MOD = (1e9 + 7).toInt();
        int count = 0;
        int total = 0;
        for (int i = 0; i < s.length; i++) {
            if (s[i] == '1') {
                count++;
            } else {
                total = (total + (count + 1) * count ~/ 2) % MOD;
                count = 0;
            }
        }
        total = (total + (count + 1) * count ~/ 2) % MOD;
        return total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import (
    "fmt"
)

type Solution struct{}

func (s Solution) numSub(sStr string) int {
    MOD := int(1e9 + 7)
    count := 0
    total := 0
    for i := range sStr {
        if sStr[i] == '1' {
            count++
        } else {
            total = (total + (count+1)*count/2) % MOD
            count = 0
        }
    }
    total = (total + (count+1)*count/2) % MOD
    return total
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def num_sub(s)
        MOD = 1e9.to_i + 7
        count = 0
        total = 0
        s.each_char do |c|
            if c == '1'
                count += 1
            else
                total = (total + (count + 1) * count / 2) % MOD
                count = 0
            end
        end
        total = (total + (count + 1) * count / 2) % MOD
        total
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def numSub(s: String): Int = {
        val MOD: Int = (1e9 + 7).toInt
        var count: Int = 0
        var total: Int = 0
        for (i <- s.indices) {
            if (s(i) == '1') {
                count += 1
            } else {
                total = (total + (count + 1) * count / 2) % MOD
                count = 0
            }
        }
        total = (total + (count + 1) * count / 2) % MOD
        total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
struct Solution;

impl Solution {
    pub fn num_sub(s: String) -> i32 {
        let MOD: i64 = 1e9 as i64 + 7;
        let mut count: i64 = 0;
        let mut total: i64 = 0;
        for c in s.chars() {
            if c == '1' {
                count += 1;
            } else {
                total = (total + (count + 1) * count / 2) % MOD;
                count = 0;
            }
        }
        total = (total + (count + 1) * count / 2) % MOD;
        total as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (num-sub s)
    (let (
        (MOD 1000000007)
        (count 0)
        (total 0))
        (for-each
            (lambda (c)
                (if (equal? c #\1)
                    (set! count (+ count 1))
                    (begin
                        (set! total (modulo (+ total (/ (* (+ count 1) count) 2)) MOD))
                        (set! count 0))))
            (string->list s))
        (set! total (modulo (+ total (/ (* (+ count 1) count) 2)) MOD))
        total))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([num_sub/1]).

num_sub(S) ->
    MOD = 1000000007,
    num_sub(S, 0, 0, MOD).

num_sub([], Count, Total, MOD) ->
    (Total + (Count + 1) * Count div 2) rem MOD;
num_sub([H|T], Count, Total, MOD) when H == $1 ->
    num_sub(T, Count + 1, Total, MOD);
num_sub([H|T], Count, Total, MOD) ->
    NewTotal = (Total + (Count + 1) * Count div 2) rem MOD,
    num_sub(T, 0, NewTotal, MOD).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def num_sub(s) do
        MOD = 1_000_000_007
        num_sub(s, 0, 0, MOD)
    end

    defp num_sub([], count, total, MOD) do
        (total + (count + 1) * count div 2) rem MOD
    end

    defp num_sub([h|t], count, total, MOD) when h == ?1 do
        num_sub(t, count + 1, total, MOD)
    end

    defp num_sub([h|t], count, total, MOD) do
        new_total = (total + (count + 1) * count div 2) rem MOD
        num_sub(t, 0, new_total, MOD)
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the binary string, because we are iterating over the string once.

- **Space Complexity:** O(1) because we are using a constant amount of space to store the count of consecutive 1s and the total count of substrings.

</div>
</details>
