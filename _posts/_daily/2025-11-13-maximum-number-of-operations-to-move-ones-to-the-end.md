---
layout: post
title: "Maximum Number of Operations to Move Ones to the End"
date: 2025-11-13 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Greedy", "Counting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/
---

## Problem #3228: Maximum Number of Operations to Move Ones to the End

**Difficulty:** Medium

**Topics:** String, Greedy, Counting

## Problem Description

<p>You are given a <span data-keyword="binary-string">binary string</span> <code>s</code>.</p>

<p>You can perform the following operation on the string <strong>any</strong> number of times:</p>

<ul>
	<li>Choose <strong>any</strong> index <code>i</code> from the string where <code>i + 1 &lt; s.length</code> such that <code>s[i] == &#39;1&#39;</code> and <code>s[i + 1] == &#39;0&#39;</code>.</li>
	<li>Move the character <code>s[i]</code> to the <strong>right</strong> until it reaches the end of the string or another <code>&#39;1&#39;</code>. For example, for <code>s = &quot;010010&quot;</code>, if we choose <code>i = 1</code>, the resulting string will be <code>s = &quot;0<strong><u>001</u></strong>10&quot;</code>.</li>
</ul>

<p>Return the <strong>maximum</strong> number of operations that you can perform.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;1001101&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>We can perform the following operations:</p>

<ul>
	<li>Choose index <code>i = 0</code>. The resulting string is <code>s = &quot;<u><strong>001</strong></u>1101&quot;</code>.</li>
	<li>Choose index <code>i = 4</code>. The resulting string is <code>s = &quot;0011<u><strong>01</strong></u>1&quot;</code>.</li>
	<li>Choose index <code>i = 3</code>. The resulting string is <code>s = &quot;001<strong><u>01</u></strong>11&quot;</code>.</li>
	<li>Choose index <code>i = 2</code>. The resulting string is <code>s = &quot;00<strong><u>01</u></strong>111&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;00111&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>


## Hints

1. It is optimal to perform the operation on the lowest index possible each time.

2. Traverse the string from left to right and perform the operation every time it is possible.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-20 10:45:59)</small>
</summary>

<div class="ai-solution-content">

{% raw %}

### Approach

The problem asks for the maximum number of operations to move all '1's to the end of a binary string. An operation consists of choosing an index `i` where `s[i] == '1'` and `s[i+1] == '0'`, and then moving `s[i]` to the right until it encounters another '1' or the end of the string. This entire movement counts as a single operation.

Let's analyze the nature of the operation. When `s[i] = '1'` moves past `s[i+1] = '0'`, `s[i]` effectively becomes '0', and the '1' reappears further to the right. The core insight comes from how this movement contributes to the total operations. Each '1' that moves is chosen from a position `i` where `s[i] == '1'` and `s[i+1] == '0'`. Once chosen, that specific `1` at that specific position `i` cannot be chosen again from `i` because `s[i]` becomes '0'. However, the same '1' can potentially be chosen again from its new position later.

The hints suggest a greedy approach: "It is optimal to perform the operation on the lowest index possible each time." and "Traverse the string from left to right and perform the operation every time it is possible." This implies a single-pass solution rather than an actual simulation that modifies the string, which would be too slow (`O(N^2)`).

Let's maintain a counter, `ones_count`, which represents the number of '1's encountered so far during our left-to-right scan. These `ones_count` '1's are conceptually to the left of our current position `i` and are 'active' in the sense that they are still '1's and could potentially move further right.

We iterate through the string `s` from index `0` to `N-1`:
1.  **If `s[i] == '1'`**: We increment `ones_count`. This '1' contributes to the pool of '1's that are currently to the left and might move past subsequent '0's.
2.  **If `s[i] == '0'`**: This '0' acts as a pivot. If there are any `ones_count` '1's to its left, they might be able to move past this `0`. The problem specifies that a '1' moves until it hits the *end of the string* or *another '1'*. This is crucial. If a `0` at index `i` is immediately followed by a `1` (i.e., `s[i+1] == '1'`) or if this `0` is the last character of the string (`i == N-1`), it signifies a 'boundary' where moving '1's would stop. In such a scenario, all `ones_count` '1's that are currently to the left of this `0` can perform one operation by moving past this `0` and stopping at the boundary. Therefore, we add `ones_count` to our `total_operations` count.

The `ones_count` is *not* decremented or reset when an operation occurs because the '1's that moved are still '1's; they merely shifted their positions to the right. They remain available to move past subsequent '0's if the conditions are met again.

Let's trace `s = "1001101"` with this logic:
-   Initialize `total_operations = 0`, `ones_count = 0`.
-   `i = 0, s[0] = '1'`: `ones_count` becomes `1`.
-   `i = 1, s[1] = '0'`: `s[i+1]` (`s[2]`) is `'0'`. Condition (`i == N-1` or `s[i+1] == '1'`) is false. No operations added.
-   `i = 2, s[2] = '0'`: `s[i+1]` (`s[3]`) is `'1'`. Condition is true. `ones_count` is `1`. `total_operations += 1`. `total_operations` becomes `1`. `ones_count` remains `1`.
    (This corresponds to the first `1` at `s[0]` moving past `s[1]` and `s[2]` to stop at `s[3]`, contributing 1 operation).
-   `i = 3, s[3] = '1'`: `ones_count` becomes `2`.
-   `i = 4, s[4] = '1'`: `ones_count` becomes `3`.
-   `i = 5, s[5] = '0'`: `s[i+1]` (`s[6]`) is `'1'`. Condition is true. `ones_count` is `3`. `total_operations += 3`. `total_operations` becomes `1 + 3 = 4`. `ones_count` remains `3`.
    (This corresponds to the three `1`s that are now conceptually to the left of `s[5]` moving past `s[5]` to stop at `s[6]`, contributing 3 operations. These three operations are: original `s[2]` (now `s[2]`) moves, original `s[3]` (now `s[3]`) moves, original `s[4]` (now `s[4]`) moves).
-   `i = 6, s[6] = '1'`: `ones_count` becomes `4`.

After iterating through the string, `total_operations` is `4`, which matches the example output. This logic correctly accounts for the cumulative effect of '1's moving rightwards past '0's, with each '1' contributing an operation every time it crosses a '0' that marks a 'boundary' (either another '1' or the end of the string).

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
#include <string>
#include <vector>

class Solution {
public:
    long long maxOperations(std::string s) {
        long long totalOperations = 0;
        long long onesCount = 0;
        int n = s.length();

        for (int i = 0; i < n; ++i) {
            if (s[i] == '1') {
                onesCount++;
            } else { // s[i] == '0'
                // An operation occurs if there are '1's to the left (onesCount > 0)
                // AND this '0' is followed by a '1' or is at the end of the string.
                // This condition signals a 'block jump' opportunity for available '1's.
                if (onesCount > 0 && (i + 1 == n || s[i + 1] == '1')) {
                    totalOperations += onesCount;
                }
            }
        }

        return totalOperations;
    }
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
    public long maxOperations(String s) {
        long totalOperations = 0;
        long onesCount = 0;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') {
                onesCount++;
            } else { // s.charAt(i) == '0'
                // An operation occurs if there are '1's to the left (onesCount > 0)
                // AND this '0' is followed by a '1' or is at the end of the string.
                // This condition signals a 'block jump' opportunity for available '1's.
                if (onesCount > 0 && (i + 1 == n || s.charAt(i + 1) == '1')) {
                    totalOperations += onesCount;
                }
            }
        }

        return totalOperations;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
    def maxOperations(self, s: str) -> int:
        total_operations = 0
        ones_count = 0
        n = len(s)

        for i in range(n):
            if s[i] == '1':
                ones_count += 1
            else: # s[i] == '0'
                # An operation occurs if there are '1's to the left (ones_count > 0)
                # AND this '0' is followed by a '1' or is at the end of the string.
                # This condition signals a 'block jump' opportunity for available '1's.
                if ones_count > 0 and (i + 1 == n or s[i + 1] == '1'):
                    total_operations += ones_count

        return total_operations
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
    def maxOperations(self, s: str) -> int:
        total_operations = 0
        ones_count = 0
        n = len(s)

        for i in range(n):
            if s[i] == '1':
                ones_count += 1
            else: # s[i] == '0'
                # An operation occurs if there are '1's to the left (ones_count > 0)
                # AND this '0' is followed by a '1' or is at the end of the string.
                # This condition signals a 'block jump' opportunity for available '1's.
                if ones_count > 0 and (i + 1 == n or s[i + 1] == '1'):
                    total_operations += ones_count

        return total_operations
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <string.h>

long long maxOperations(char* s) {
    long long totalOperations = 0;
    long long onesCount = 0;
    int n = strlen(s);

    for (int i = 0; i < n; ++i) {
        if (s[i] == '1') {
            onesCount++;
        } else { // s[i] == '0'
            // An operation occurs if there are '1's to the left (onesCount > 0)
            // AND this '0' is followed by a '1' or is at the end of the string.
            // This condition signals a 'block jump' opportunity for available '1's.
            if (onesCount > 0 && (i + 1 == n || s[i + 1] == '1')) {
                totalOperations += onesCount;
            }
        }
    }

    return totalOperations;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
using System;

public class Solution {
    public long MaxOperations(string s) {
        long totalOperations = 0;
        long onesCount = 0;
        int n = s.Length;

        for (int i = 0; i < n; i++) {
            if (s[i] == '1') {
                onesCount++;
            } else { // s[i] == '0'
                // An operation occurs if there are '1's to the left (onesCount > 0)
                // AND this '0' is followed by a '1' or is at the end of the string.
                // This condition signals a 'block jump' opportunity for available '1's.
                if (onesCount > 0 && (i + 1 == n || s[i + 1] == '1')) {
                    totalOperations += onesCount;
                }
            }
        }

        return totalOperations;
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
var maxOperations = function(s) {
    let totalOperations = 0;
    let onesCount = 0;
    let n = s.length;

    for (let i = 0; i < n; i++) {
        if (s[i] === '1') {
            onesCount++;
        } else { // s[i] === '0'
            // An operation occurs if there are '1's to the left (onesCount > 0)
            // AND this '0' is followed by a '1' or is at the end of the string.
            // This condition signals a 'block jump' opportunity for available '1's.
            if (onesCount > 0 && (i + 1 === n || s[i + 1] === '1')) {
                totalOperations += onesCount;
            }
        }
    }

    return totalOperations;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function maxOperations(s: string): number {
    let totalOperations: number = 0;
    let onesCount: number = 0;
    const n: number = s.length;

    for (let i = 0; i < n; i++) {
        if (s[i] === '1') {
            onesCount++;
        } else { // s[i] === '0'
            // An operation occurs if there are '1's to the left (onesCount > 0)
            // AND this '0' is followed by a '1' or is at the end of the string.
            // This condition signals a 'block jump' opportunity for available '1's.
            if (onesCount > 0 && (i + 1 === n || s[i + 1] === '1')) {
                totalOperations += onesCount;
            }
        }
    }

    return totalOperations;
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
    function maxOperations($s) {
        $totalOperations = 0;
        $onesCount = 0;
        $n = strlen($s);

        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] == '1') {
                $onesCount++;
            } else { // $s[$i] == '0'
                // An operation occurs if there are '1's to the left (onesCount > 0)
                // AND this '0' is followed by a '1' or is at the end of the string.
                // This condition signals a 'block jump' opportunity for available '1's.
                if ($onesCount > 0 && ($i + 1 == $n || $s[$i + 1] == '1')) {
                    $totalOperations += $onesCount;
                }
            }
        }

        return $totalOperations;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution {
    func maxOperations(_ s: String) -> Int {
        var totalOperations: Int = 0
        var onesCount: Int = 0
        let n = s.count
        let sChars = Array(s)

        for i in 0..<n {
            if sChars[i] == "1" {
                onesCount += 1
            } else { // sChars[i] == '0'
                // An operation occurs if there are '1's to the left (onesCount > 0)
                // AND this '0' is followed by a '1' or is at the end of the string.
                // This condition signals a 'block jump' opportunity for available '1's.
                if onesCount > 0 && (i + 1 == n || sChars[i + 1] == "1") {
                    totalOperations += onesCount
                }
            }
        }

        return totalOperations
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution {
    fun maxOperations(s: String): Long {
        var totalOperations: Long = 0
        var onesCount: Long = 0
        val n = s.length

        for (i in 0 until n) {
            if (s[i] == '1') {
                onesCount++
            } else { // s[i] == '0'
                // An operation occurs if there are '1's to the left (onesCount > 0)
                // AND this '0' is followed by a '1' or is at the end of the string.
                // This condition signals a 'block jump' opportunity for available '1's.
                if (onesCount > 0 && (i + 1 == n || s[i + 1] == '1')) {
                    totalOperations += onesCount
                }
            }
        }

        return totalOperations
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
class Solution {
  int maxOperations(String s) {
    int totalOperations = 0;
    int onesCount = 0;
    int n = s.length;

    for (int i = 0; i < n; i++) {
      if (s[i] == '1') {
        onesCount++;
      } else { // s[i] == '0'
        // An operation occurs if there are '1's to the left (onesCount > 0)
        // AND this '0' is followed by a '1' or is at the end of the string.
        // This condition signals a 'block jump' opportunity for available '1's.
        if (onesCount > 0 && (i + 1 == n || s[i + 1] == '1')) {
          totalOperations += onesCount;
        }
      }
    }

    return totalOperations;
  }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

import (
	"string"
)

func maxOperations(s string) int64 {
    var totalOperations int64 = 0
    var onesCount int64 = 0
    n := len(s)

    for i := 0; i < n; i++ {
        if s[i] == '1' {
            onesCount++
        } else { // s[i] == '0'
            // An operation occurs if there are '1's to the left (onesCount > 0)
            // AND this '0' is followed by a '1' or is at the end of the string.
            // This condition signals a 'block jump' opportunity for available '1's.
            if onesCount > 0 && (i + 1 == n || s[i + 1] == '1') {
                totalOperations += onesCount
            }
        }
    }

    return totalOperations
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
# @param {String} s
# @return {Integer}
def max_operations(s)
    total_operations = 0
    ones_count = 0
    n = s.length

    (0...n).each do |i|
        if s[i] == '1'
            ones_count += 1
        else # s[i] == '0'
            # An operation occurs if there are '1's to the left (ones_count > 0)
            # AND this '0' is followed by a '1' or is at the end of the string.
            # This condition signals a 'block jump' opportunity for available '1's.
            if ones_count > 0 && (i + 1 == n || s[i + 1] == '1')
                total_operations += ones_count
            end
        end
    end

    return total_operations
end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {
    def maxOperations(s: String): Long = {
        var totalOperations: Long = 0
        var onesCount: Long = 0
        val n = s.length

        for (i <- 0 until n) {
            if (s(i) == '1') {
                onesCount += 1
            } else { // s(i) == '0'
                // An operation occurs if there are '1's to the left (onesCount > 0)
                // AND this '0' is followed by a '1' or is at the end of the string.
                // This condition signals a 'block jump' opportunity for available '1's.
                if (onesCount > 0 && (i + 1 == n || s(i + 1) == '1')) {
                    totalOperations += onesCount
                }
            }
        }

        totalOperations
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution {
    pub fn max_operations(s: String) -> i64 {
        let mut total_operations: i64 = 0;
        let mut ones_count: i64 = 0;
        let n = s.len();
        let s_chars: Vec<char> = s.chars().collect();

        for i in 0..n {
            if s_chars[i] == '1' {
                ones_count += 1;
            } else { // s_chars[i] == '0'
                // An operation occurs if there are '1's to the left (ones_count > 0)
                // AND this '0' is followed by a '1' or is at the end of the string.
                // This condition signals a 'block jump' opportunity for available '1's.
                if ones_count > 0 && (i + 1 == n || s_chars[i + 1] == '1') {
                    total_operations += ones_count;
                }
            }
        }

        total_operations
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
(define/contract (max-operations s)
  (-> string? integer?)
  (let* ((n (string-length s))
         (s-chars (string->list s))
         (total-operations 0)
         (ones-count 0))
    (for ([i (in-range n)])
      (let ((char (list-ref s-chars i)))
        (cond
          ((char?-> '1' char) (set! ones-count (+ ones-count 1)))
          ((char?-> '0' char)
           (when (and (> ones-count 0)
                      (or (= (+ i 1) n)
                          (char?-> '1' (list-ref s-chars (+ i 1)))))
             (set! total-operations (+ total-operations ones-count)))))))
    total-operations))

(define (char?-> c1 c2)
  (char=? c1 c2))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
-export([max_operations/1]).

%% @spec max_operations(S :: unicode:unicode_binary()) -> integer()
max_operations(S) ->
    N = byte_size(S),
    max_operations_recursive(S, N, 0, 0, 0).

max_operations_recursive(S, N, Index, OnesCount, TotalOperations) when Index < N ->
    Char = binary:at(S, Index),
    case Char of
        49 -> %% '1'
            max_operations_recursive(S, N, Index + 1, OnesCount + 1, TotalOperations);
        48 -> %% '0'
            ShouldAdd = (OnesCount > 0) andalso ((Index + 1 == N) orelse (binary:at(S, Index + 1) == 49)),
            NewTotalOperations = case ShouldAdd of
                true -> TotalOperations + OnesCount;
                false -> TotalOperations
            end,
            max_operations_recursive(S, N, Index + 1, OnesCount, NewTotalOperations)
    end;
max_operations_recursive(_S, _N, _Index, _OnesCount, TotalOperations) ->
    TotalOperations.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
  @spec max_operations(s :: String.t) :: integer
  def max_operations(s) do
    n = String.length(s)
    s_chars = String.to_charlist(s)

    do_max_operations(s_chars, n, 0, 0, 0)
  end

  defp do_max_operations(_s_chars, _n, index, ones_count, total_operations) when index >= _n do
    total_operations
  end

  defp do_max_operations(s_chars, n, index, ones_count, total_operations) do
    char = Enum.at(s_chars, index)

    case char do
      ?1 -> # '1'
        do_max_operations(s_chars, n, index + 1, ones_count + 1, total_operations)
      ?0 -> # '0'
        should_add = (ones_count > 0) and (index + 1 == n or Enum.at(s_chars, index + 1) == ?1)
        new_total_operations = if should_add, do: total_operations + ones_count, else: total_operations
        do_max_operations(s_chars, n, index + 1, ones_count, new_total_operations)
    end
  end
end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N), where N is the length of the string `s`. The algorithm iterates through the string exactly once. Each character is processed in constant time.

- **Space Complexity:** O(1). The algorithm uses a few integer variables (`total_operations`, `ones_count`, and loop counter `i`) regardless of the input string's length.

</div>
</details>


<hr class="ai-solution-separator">


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-20 10:46:07)</small>
</summary>

<div class="ai-solution-content">

{% raw %}

### Approach

The problem requires finding the maximum number of operations to move ones to the end of a binary string. The operation involves choosing an index where the current character is '1' and the next character is '0', then moving the '1' to the right until it reaches the end of the string or another '1'. To solve this problem, we can use a greedy approach where we always choose the leftmost index that satisfies the condition for the operation. This approach ensures that we maximize the number of operations because moving a '1' to the right as soon as possible allows for more opportunities to perform the operation later. We will iterate through the string from left to right, keeping track of the number of operations performed and the current state of the string after each operation.

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
class Solution {
       public:
           int maxOperations(string s) {
               int operations = 0;
               for (int i = 0; i < s.length() - 1; i++) {
                   if (s[i] == '1' && s[i + 1] == '0') {
                       operations++;
                       for (int j = i; j < s.length() - 1; j++) {
                           if (s[j] == '1' && s[j + 1] == '0') {
                               swap(s[j], s[j + 1]);
                           } else {
                               break;
                           }
                       }
                   }
               }
               return operations;
           }
       };
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
           public int maxOperations(String s) {
               int operations = 0;
               char[] chars = s.toCharArray();
               for (int i = 0; i < chars.length - 1; i++) {
                   if (chars[i] == '1' && chars[i + 1] == '0') {
                       operations++;
                       for (int j = i; j < chars.length - 1; j++) {
                           if (chars[j] == '1' && chars[j + 1] == '0') {
                               char temp = chars[j];
                               chars[j] = chars[j + 1];
                               chars[j + 1] = temp;
                           } else {
                               break;
                           }
                       }
                   }
               }
               return operations;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
           def maxOperations(self, s: str) -> int:
               operations = 0
               s = list(s)
               for i in range(len(s) - 1):
                   if s[i] == '1' and s[i + 1] == '0':
                       operations += 1
                       for j in range(i, len(s) - 1):
                           if s[j] == '1' and s[j + 1] == '0':
                               s[j], s[j + 1] = s[j + 1], s[j]
                           else:
                               break
               return operations
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
           def maxOperations(self, s: str) -> int:
               operations = 0
               s = list(s)
               for i in range(len(s) - 1):
                   if s[i] == '1' and s[i + 1] == '0':
                       operations += 1
                       for j in range(i, len(s) - 1):
                           if s[j] == '1' and s[j + 1] == '0':
                               s[j], s[j + 1] = s[j + 1], s[j]
                           else:
                               break
               return operations
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdio.h>
       #include <string.h>

       int maxOperations(char * s){
           int operations = 0;
           for (int i = 0; i < strlen(s) - 1; i++) {
               if (s[i] == '1' && s[i + 1] == '0') {
                   operations++;
                   for (int j = i; j < strlen(s) - 1; j++) {
                       if (s[j] == '1' && s[j + 1] == '0') {
                           char temp = s[j];
                           s[j] = s[j + 1];
                           s[j + 1] = temp;
                       } else {
                           break;
                       }
                   }
               }
           }
           return operations;
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
public class Solution {
           public int MaxOperations(string s) {
               int operations = 0;
               char[] chars = s.ToCharArray();
               for (int i = 0; i < chars.Length - 1; i++) {
                   if (chars[i] == '1' && chars[i + 1] == '0') {
                       operations++;
                       for (int j = i; j < chars.Length - 1; j++) {
                           if (chars[j] == '1' && chars[j + 1] == '0') {
                               char temp = chars[j];
                               chars[j] = chars[j + 1];
                               chars[j + 1] = temp;
                           } else {
                               break;
                           }
                       }
                   }
               }
               return operations;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
var maxOperations = function(s) {
           let operations = 0;
           s = s.split('');
           for (let i = 0; i < s.length - 1; i++) {
               if (s[i] == '1' && s[i + 1] == '0') {
                   operations++;
                   for (let j = i; j < s.length - 1; j++) {
                       if (s[j] == '1' && s[j + 1] == '0') {
                           [s[j], s[j + 1]] = [s[j + 1], s[j]];
                       } else {
                           break;
                       }
                   }
               }
           }
           return operations;
       };
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function maxOperations(s: string): number {
           let operations: number = 0;
           s = s.split('');
           for (let i: number = 0; i < s.length - 1; i++) {
               if (s[i] == '1' && s[i + 1] == '0') {
                   operations++;
                   for (let j: number = i; j < s.length - 1; j++) {
                       if (s[j] == '1' && s[j + 1] == '0') {
                           [s[j], s[j + 1]] = [s[j + 1], s[j]];
                       } else {
                           break;
                       }
                   }
               }
           }
           return operations;
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
class Solution {
           function maxOperations($s) {
               $operations = 0;
               $s = str_split($s);
               for ($i = 0; $i < count($s) - 1; $i++) {
                   if ($s[$i] == '1' && $s[$i + 1] == '0') {
                       $operations++;
                       for ($j = $i; $j < count($s) - 1; $j++) {
                           if ($s[$j] == '1' && $s[$j + 1] == '0') {
                               list($s[$j], $s[$j + 1]) = array($s[$j + 1], $s[$j]);
                           } else {
                               break;
                           }
                       }
                   }
               }
               return $operations;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution {
           func maxOperations(_ s: String) -> Int {
               var operations = 0
               var s = Array(s)
               for i in 0..<s.count - 1 {
                   if s[i] == "1" && s[i + 1] == "0" {
                       operations += 1
                       for j in stride(from: i, to: s.count - 1, by: 1) {
                           if s[j] == "1" && s[j + 1] == "0" {
                               let temp = s[j]
                               s[j] = s[j + 1]
                               s[j + 1] = temp
                           } else {
                               break
                           }
                       }
                   }
               }
               return operations
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution {
           fun maxOperations(s: String): Int {
               var operations = 0
               val s = s.toCharArray()
               for (i in 0 until s.size - 1) {
                   if (s[i] == '1' && s[i + 1] == '0') {
                       operations++
                       for (j in i until s.size - 1) {
                           if (s[j] == '1' && s[j + 1] == '0') {
                               val temp = s[j]
                               s[j] = s[j + 1]
                               s[j + 1] = temp
                           } else {
                               break
                           }
                       }
                   }
               }
               return operations
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
class Solution {
           int maxOperations(String s) {
               int operations = 0;
               List<String> sList = s.split('').toList();
               for (int i = 0; i < sList.length - 1; i++) {
                   if (sList[i] == '1' && sList[i + 1] == '0') {
                       operations++;
                       for (int j = i; j < sList.length - 1; j++) {
                           if (sList[j] == '1' && sList[j + 1] == '0') {
                               String temp = sList[j];
                               sList[j] = sList[j + 1];
                               sList[j + 1] = temp;
                           } else {
                               break;
                           }
                       }
                   }
               }
               return operations;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

       import (
           "fmt"
           "strings"
       )

       func maxOperations(s string) int {
           operations := 0
           sList := strings.Split(s, "")
           for i := 0; i < len(sList)-1; i++ {
               if sList[i] == "1" && sList[i+1] == "0" {
                   operations++
                   for j := i; j < len(sList)-1; j++ {
                       if sList[j] == "1" && sList[j+1] == "0" {
                           sList[j], sList[j+1] = sList[j+1], sList[j]
                       } else {
                           break
                       }
                   }
               }
           }
           return operations
       }

       func main() {
           fmt.Println(maxOperations("1001101"))
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
# @param {String} s
       # @return {Integer}
       def max_operations(s)
           operations = 0
           s = s.split('')
           (0...s.length - 1).each do |i|
               if s[i] == '1' && s[i + 1] == '0'
                   operations += 1
                   j = i
                   while j < s.length - 1
                       if s[j] == '1' && s[j + 1] == '0'
                           s[j], s[j + 1] = s[j + 1], s[j]
                       else
                           break
                       end
                       j += 1
                   end
               end
           end
           operations
       end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {
           def maxOperations(s: String): Int = {
               var operations = 0
               val sList = s.toCharArray
               for (i <- 0 until sList.length - 1) {
                   if (sList(i) == '1' && sList(i + 1) == '0') {
                       operations += 1
                       for (j <- i until sList.length - 1) {
                           if (sList(j) == '1' && sList(j + 1) == '0') {
                               val temp = sList(j)
                               sList(j) = sList(j + 1)
                               sList(j + 1) = temp
                           } else {
                               j
                           }
                       }
                   }
               }
               operations
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution {
           pub fn max_operations(s: String) -> i32 {
               let mut operations: i32 = 0;
               let mut s: Vec<char> = s.chars().collect();
               for i in 0..s.len() - 1 {
                   if s[i] == '1' && s[i + 1] == '0' {
                       operations += 1;
                       for j in i..s.len() - 1 {
                           if s[j] == '1' && s[j + 1] == '0' {
                               s.swap(j, j + 1);
                           } else {
                               break;
                           }
                       }
                   }
               }
               operations
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket

       (define (max-operations s)
         (let loop ((s (string->list s))
                    (i 0)
                    (operations 0))
           (cond
             ((>= i (sub1 (length s))) operations)
             ((and (eq? (list-ref s i) #\1)
                   (eq? (list-ref s (add1 i)) #\0))
              (loop (list-set! s i #\0)
                    i
                    (add1 operations)))
             (else (loop s (add1 i) operations)))))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
       -export([max_operations/1]).

       max_operations(S) ->
           max_operations(S, 0).

       max_operations([H1, H2 | T], Operations) ->
           case {H1, H2} of
               {1, 0} ->
                   NewT = move_one(T, [H2, H1]),
                   max_operations(NewT, Operations + 1);
               _ ->
                   max_operations([H2 | T], Operations)
           end;
       max_operations(_, Operations) ->
           Operations.

       move_one([H | T], Acc) ->
           case H of
               1 -> move_one(T, [0 | Acc]);
               _ -> lists:reverse([H | Acc], T)
           end;
       move_one([], Acc) ->
           lists:reverse(Acc).
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
           def max_operations(s) do
               operations = 0
               s = String.split(s, "")
               Enum.reduce(0..(length(s) - 2), operations, fn i, acc ->
                   if Enum.at(s, i) == "1" and Enum.at(s, i + 1) == "0" do
                       new_s = move_one(s, i)
                       acc + 1
                   else
                       acc
                   end
               end)
           end

           defp move_one(s, i) do
               new_s = List.update_at(s, i, fn _ -> Enum.at(s, i + 1) end)
               new_s = List.update_at(new_s, i + 1, fn _ -> Enum.at(s, i) end)
               new_s
           end
       end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the string. This is because in the worst case, we might need to iterate through the entire string for each operation, and there can be up to n operations (in the case where the string is all '1's except for the last character which is '0'). However, since we are iterating through the string and performing a constant amount of work for each character, the overall time complexity remains linear.

- **Space Complexity:** O(n) because in the worst case, we might need to store the entire string after each operation. However, if we consider the space used by the input and the output as not part of the space complexity, then the space complexity would be O(1) because we only use a constant amount of space to store the count of operations and the current index.

</div>
</details>
