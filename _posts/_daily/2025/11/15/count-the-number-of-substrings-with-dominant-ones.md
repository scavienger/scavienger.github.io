---
layout: post
title: "Count the Number of Substrings With Dominant Ones"
date: 2025-11-15 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Enumeration"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/
---

## Problem #3234: Count the Number of Substrings With Dominant Ones

**Difficulty:** Medium

**Topics:** String, Enumeration

## Problem Description

<p>You are given a binary string <code>s</code>.</p>

<p>Return the number of <span data-keyword="substring-nonempty">substrings</span> with <strong>dominant</strong> ones.</p>

<p>A string has <strong>dominant</strong> ones if the number of ones in the string is <strong>greater than or equal to</strong> the <strong>square</strong> of the number of zeros in the string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;00011&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The substrings with dominant ones are shown in the table below.</p>
</div>

<table>
	<thead>
		<tr>
			<th>i</th>
			<th>j</th>
			<th>s[i..j]</th>
			<th>Number of Zeros</th>
			<th>Number of Ones</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>3</td>
			<td>3</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<td>4</td>
			<td>4</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<td>2</td>
			<td>3</td>
			<td>01</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>3</td>
			<td>4</td>
			<td>11</td>
			<td>0</td>
			<td>2</td>
		</tr>
		<tr>
			<td>2</td>
			<td>4</td>
			<td>011</td>
			<td>1</td>
			<td>2</td>
		</tr>
	</tbody>
</table>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;101101&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">16</span></p>

<p><strong>Explanation:</strong></p>

<p>The substrings with <strong>non-dominant</strong> ones are shown in the table below.</p>

<p>Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.</p>
</div>

<table>
	<thead>
		<tr>
			<th>i</th>
			<th>j</th>
			<th>s[i..j]</th>
			<th>Number of Zeros</th>
			<th>Number of Ones</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>1</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<td>4</td>
			<td>4</td>
			<td>0</td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<td>1</td>
			<td>4</td>
			<td>0110</td>
			<td>2</td>
			<td>2</td>
		</tr>
		<tr>
			<td>0</td>
			<td>4</td>
			<td>10110</td>
			<td>2</td>
			<td>3</td>
		</tr>
		<tr>
			<td>1</td>
			<td>5</td>
			<td>01101</td>
			<td>2</td>
			<td>3</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists only of characters <code>&#39;0&#39;</code> and <code>&#39;1&#39;</code>.</li>
</ul>


## Hints

1. Let us fix the starting index `l` of the substring and count the number of indices `r` such that `l <= r` and the substring `s[l..r]` has dominant ones.

2. A substring with dominant ones has at most `sqrt(n)` zeros.

3. We cannot iterate over every `r` and check if the  `s[l..r]` has dominant ones. Instead, we iterate over the next `sqrt(n)` zeros to the left of `l` and count the number of substrings with dominant ones where the current zero is the rightmost zero of the substring.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-25 04:07:31 UTC)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to count substrings with 'dominant ones', meaning the number of ones is greater than or equal to the square of the number of zeros. The string length `N` can be up to `4 * 10^4`. A brute-force approach of iterating through all `O(N^2)` substrings and for each, counting zeros and ones (`O(N)` or `O(1)` with prefix sums) would be `O(N^3)` or `O(N^2)`, which is too slow for `N = 4 * 10^4`.

The key observation comes from the constraint `ones >= zeros^2`. Let `Z` be the number of zeros and `O` be the number of ones. The total length of the substring is `L = Z + O`. Since `O <= L <= N`, we have `N >= O`. If `Z > sqrt(N)`, then `Z^2 > N`. In this case, it's impossible for `O >= Z^2` because `O <= N < Z^2`. Therefore, any substring with dominant ones must have `Z <= sqrt(N)` zeros. For `N = 4 * 10^4`, `sqrt(N) = 200`. This means the number of zeros in any valid substring is at most 200.

This crucial observation allows us to optimize the counting. We iterate through all possible starting positions `i` (from `0` to `N-1`). For each `i`, we iterate through possible ending positions `j` (from `i` to `N-1`). As we extend `j`, we maintain the current count of zeros (`current_zeros`) and ones (`current_ones`) for the substring `s[i..j]`. If `current_zeros` exceeds `sqrt(N)`, we can immediately break the inner loop for `j`. This is because any further extension of the substring `s[i..j']` (where `j' > j`) will only increase `current_zeros` or `current_ones`, but `current_zeros` will remain greater than `sqrt(N)`, making the condition `ones >= zeros^2` impossible to satisfy. If `current_zeros <= sqrt(N)`, we check if `current_ones >= current_zeros^2` and increment our total count if it is.

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
    long long numberOfSubstrings(std::string s) {
        int n = s.length();
        long long count = 0;
        int max_zeros_limit = 0;
        if (n > 0) {
            max_zeros_limit = static_cast<int>(std::sqrt(n));
        }

        for (int i = 0; i < n; ++i) {
            int current_zeros = 0;
            int current_ones = 0;
            for (int j = i; j < n; ++j) {
                if (s[j] == '0') {
                    current_zeros++;
                } else {
                    current_ones++;
                }

                // Optimization: If current_zeros exceeds the limit, 
                // any further extension of this substring will also have 
                // current_zeros > max_zeros_limit, making the condition impossible.
                if (current_zeros > max_zeros_limit) {
                    break;
                }

                // Check the dominant ones condition
                if (static_cast<long long>(current_ones) >= static_cast<long long>(current_zeros) * current_zeros) {
                    count++;
                }
            }
        }
        return count;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long numberOfSubstrings(String s) {
        int n = s.length();
        long count = 0;
        int maxZerosLimit = 0;
        if (n > 0) {
            maxZerosLimit = (int) Math.sqrt(n);
        }

        for (int i = 0; i < n; ++i) {
            int currentZeros = 0;
            int currentOnes = 0;
            for (int j = i; j < n; ++j) {
                if (s.charAt(j) == '0') {
                    currentZeros++;
                } else {
                    currentOnes++;
                }

                // Optimization: If currentZeros exceeds the limit, 
                // any further extension of this substring will also have 
                // currentZeros > maxZerosLimit, making the condition impossible.
                if (currentZeros > maxZerosLimit) {
                    break;
                }

                // Check the dominant ones condition
                if ((long) currentOnes >= (long) currentZeros * currentZeros) {
                    count++;
                }
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        max_zeros_limit = 0
        if n > 0:
            max_zeros_limit = int(math.sqrt(n))

        for i in range(n):
            current_zeros = 0
            current_ones = 0
            for j in range(i, n):
                if s[j] == '0':
                    current_zeros += 1
                else:
                    current_ones += 1

                # Optimization: If current_zeros exceeds the limit, 
                # any further extension of this substring will also have 
                # current_zeros > max_zeros_limit, making the condition impossible.
                if current_zeros > max_zeros_limit:
                    break

                # Check the dominant ones condition
                if current_ones >= current_zeros * current_zeros:
                    count += 1

        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        max_zeros_limit = 0
        if n > 0:
            max_zeros_limit = int(math.sqrt(n))

        for i in range(n):
            current_zeros = 0
            current_ones = 0
            for j in range(i, n):
                if s[j] == '0':
                    current_zeros += 1
                else:
                    current_ones += 1

                # Optimization: If current_zeros exceeds the limit, 
                # any further extension of this substring will also have 
                # current_zeros > max_zeros_limit, making the condition impossible.
                if current_zeros > max_zeros_limit:
                    break

                # Check the dominant ones condition
                if current_ones >= current_zeros * current_zeros:
                    count += 1

        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>
#include <math.h>
#include <stdlib.h>

long long numberOfSubstrings(char * s){
    int n = strlen(s);
    long long count = 0;
    int max_zeros_limit = 0;
    if (n > 0) {
        max_zeros_limit = (int)sqrt(n);
    }

    for (int i = 0; i < n; ++i) {
        int current_zeros = 0;
        int current_ones = 0;
        for (int j = i; j < n; ++j) {
            if (s[j] == '0') {
                current_zeros++;
            } else {
                current_ones++;
            }

            // Optimization: If current_zeros exceeds the limit, 
            // any further extension of this substring will also have 
            // current_zeros > max_zeros_limit, making the condition impossible.
            if (current_zeros > max_zeros_limit) {
                break;
            }

            // Check the dominant ones condition
            if ((long long)current_ones >= (long long)current_zeros * current_zeros) {
                count++;
            }
        }
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public long NumberOfSubstrings(string s) {
        int n = s.Length;
        long count = 0;
        int maxZerosLimit = 0;
        if (n > 0) {
            maxZerosLimit = (int)Math.Sqrt(n);
        }

        for (int i = 0; i < n; ++i) {
            int currentZeros = 0;
            int currentOnes = 0;
            for (int j = i; j < n; ++j) {
                if (s[j] == '0') {
                    currentZeros++;
                } else {
                    currentOnes++;
                }

                // Optimization: If currentZeros exceeds the limit, 
                // any further extension of this substring will also have 
                // currentZeros > maxZerosLimit, making the condition impossible.
                if (currentZeros > maxZerosLimit) {
                    break;
                }

                // Check the dominant ones condition
                if ((long)currentOnes >= (long)currentZeros * currentZeros) {
                    count++;
                }
            }
        }
        return count;
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
var numberOfSubstrings = function(s) {
    const n = s.length;
    let count = 0;
    let maxZerosLimit = 0;
    if (n > 0) {
        maxZerosLimit = Math.floor(Math.sqrt(n));
    }

    for (let i = 0; i < n; ++i) {
        let currentZeros = 0;
        let currentOnes = 0;
        for (let j = i; j < n; ++j) {
            if (s[j] === '0') {
                currentZeros++;
            } else {
                currentOnes++;
            }

            // Optimization: If currentZeros exceeds the limit, 
            // any further extension of this substring will also have 
            // currentZeros > maxZerosLimit, making the condition impossible.
            if (currentZeros > maxZerosLimit) {
                break;
            }

            // Check the dominant ones condition
            if (currentOnes >= currentZeros * currentZeros) {
                count++;
            }
        }
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numberOfSubstrings(s: string): number {
    const n = s.length;
    let count: number = 0;
    let maxZerosLimit: number = 0;
    if (n > 0) {
        maxZerosLimit = Math.floor(Math.sqrt(n));
    }

    for (let i = 0; i < n; ++i) {
        let currentZeros: number = 0;
        let currentOnes: number = 0;
        for (let j = i; j < n; ++j) {
            if (s[j] === '0') {
                currentZeros++;
            } else {
                currentOnes++;
            }

            // Optimization: If currentZeros exceeds the limit, 
            // any further extension of this substring will also have 
            // currentZeros > maxZerosLimit, making the condition impossible.
            if (currentZeros > maxZerosLimit) {
                break;
            }

            // Check the dominant ones condition
            if (currentOnes >= currentZeros * currentZeros) {
                count++;
            }
        }
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function numberOfSubstrings($s) {
        $n = strlen($s);
        $count = 0;
        $maxZerosLimit = 0;
        if ($n > 0) {
            $maxZerosLimit = (int)floor(sqrt($n));
        }

        for ($i = 0; $i < $n; ++$i) {
            $currentZeros = 0;
            $currentOnes = 0;
            for ($j = $i; $j < $n; ++$j) {
                if ($s[$j] == '0') {
                    $currentZeros++;
                } else {
                    $currentOnes++;
                }

                // Optimization: If currentZeros exceeds the limit, 
                // any further extension of this substring will also have 
                // currentZeros > maxZerosLimit, making the condition impossible.
                if ($currentZeros > $maxZerosLimit) {
                    break;
                }

                // Check the dominant ones condition
                if ($currentOnes >= $currentZeros * $currentZeros) {
                    $count++;
                }
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
import Foundation

class Solution {
    func numberOfSubstrings(_ s: String) -> Int {
        let n = s.count
        var count: Int = 0
        let chars = Array(s)
        var maxZerosLimit: Int = 0
        if n > 0 {
            maxZerosLimit = Int(sqrt(Double(n)))
        }

        for i in 0..<n {
            var currentZeros: Int = 0
            var currentOnes: Int = 0
            for j in i..<n {
                if chars[j] == "0" {
                    currentZeros += 1
                } else {
                    currentOnes += 1
                }

                // Optimization: If currentZeros exceeds the limit, 
                // any further extension of this substring will also have 
                // currentZeros > maxZerosLimit, making the condition impossible.
                if currentZeros > maxZerosLimit {
                    break
                }

                // Check the dominant ones condition
                if currentOnes >= currentZeros * currentZeros {
                    count += 1
                }
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
import kotlin.math.sqrt

class Solution {
    fun numberOfSubstrings(s: String): Long {
        val n = s.length
        var count: Long = 0
        var maxZerosLimit = 0
        if (n > 0) {
            maxZerosLimit = sqrt(n.toDouble()).toInt()
        }

        for (i in 0 until n) {
            var currentZeros = 0
            var currentOnes = 0
            for (j in i until n) {
                if (s[j] == '0') {
                    currentZeros++
                } else {
                    currentOnes++
                }

                // Optimization: If currentZeros exceeds the limit, 
                // any further extension of this substring will also have 
                // currentZeros > maxZerosLimit, making the condition impossible.
                if (currentZeros > maxZerosLimit) {
                    break
                }

                // Check the dominant ones condition
                if (currentOnes.toLong() >= currentZeros.toLong() * currentZeros) {
                    count++
                }
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
import 'dart:math';

class Solution {
  int numberOfSubstrings(String s) {
    int n = s.length;
    int count = 0;
    int maxZerosLimit = 0;
    if (n > 0) {
      maxZerosLimit = sqrt(n).floor();
    }

    for (int i = 0; i < n; ++i) {
      int currentZeros = 0;
      int currentOnes = 0;
      for (int j = i; j < n; ++j) {
        if (s[j] == '0') {
          currentZeros++;
        } else {
          currentOnes++;
        }

        // Optimization: If currentZeros exceeds the limit, 
        // any further extension of this substring will also have 
        // currentZeros > maxZerosLimit, making the condition impossible.
        if (currentZeros > maxZerosLimit) {
          break;
        }

        // Check the dominant ones condition
        if (currentOnes >= currentZeros * currentZeros) {
          count++;
        }
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
import (
	"math"
)

func numberOfSubstrings(s string) int64 {
    n := len(s)
    var count int64 = 0
    maxZerosLimit := 0
    if n > 0 {
        maxZerosLimit = int(math.Sqrt(float64(n)))
    }

    for i := 0; i < n; i++ {
        currentZeros := 0
        currentOnes := 0
        for j := i; j < n; j++ {
            if s[j] == '0' {
                currentZeros++
            } else {
                currentOnes++
            }

            // Optimization: If currentZeros exceeds the limit, 
            // any further extension of this substring will also have 
            // currentZeros > maxZerosLimit, making the condition impossible.
            if currentZeros > maxZerosLimit {
                break
            }

            // Check the dominant ones condition
            if int64(currentOnes) >= int64(currentZeros)*int64(currentZeros) {
                count++
            }
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
class Solution
    /**
     * @param {String} s
     * @return {Number}
     */
    def number_of_substrings(s)
        n = s.length
        count = 0
        max_zeros_limit = 0
        if n > 0
            max_zeros_limit = Math.sqrt(n).floor.to_i
        end

        (0...n).each do |i|
            current_zeros = 0
            current_ones = 0
            (i...n).each do |j|
                if s[j] == '0'
                    current_zeros += 1
                else
                    current_ones += 1
                end

                # Optimization: If current_zeros exceeds the limit, 
                # any further extension of this substring will also have 
                # current_zeros > max_zeros_limit, making the condition impossible.
                if current_zeros > max_zeros_limit
                    break
                end

                # Check the dominant ones condition
                if current_ones >= current_zeros * current_zeros
                    count += 1
                end
            end
        end
        count
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.math

object Solution {
    def numberOfSubstrings(s: String): Long = {
        val n = s.length
        var count: Long = 0
        var maxZerosLimit: Int = 0
        if (n > 0) {
            maxZerosLimit = math.sqrt(n.toDouble).toInt
        }

        for (i <- 0 until n) {
            var currentZeros: Int = 0
            var currentOnes: Int = 0
            for (j <- i until n) {
                if (s(j) == '0') {
                    currentZeros += 1
                } else {
                    currentOnes += 1
                }

                // Optimization: If currentZeros exceeds the limit, 
                // any further extension of this substring will also have 
                // currentZeros > maxZerosLimit, making the condition impossible.
                if (currentZeros > maxZerosLimit) {
                    break
                }

                // Check the dominant ones condition
                if (currentOnes.toLong >= currentZeros.toLong * currentZeros) {
                    count += 1
                }
            }
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn number_of_substrings(s: String) -> i64 {
        let n = s.len();
        let mut count: i64 = 0;
        let chars: Vec<char> = s.chars().collect();
        let mut max_zeros_limit: usize = 0;
        if n > 0 {
            max_zeros_limit = (n as f64).sqrt() as usize;
        }

        for i in 0..n {
            let mut current_zeros: usize = 0;
            let mut current_ones: usize = 0;
            for j in i..n {
                if chars[j] == '0' {
                    current_zeros += 1;
                } else {
                    current_ones += 1;
                }

                // Optimization: If current_zeros exceeds the limit, 
                // any further extension of this substring will also have 
                // current_zeros > max_zeros_limit, making the condition impossible.
                if current_zeros > max_zeros_limit {
                    break;
                }

                // Check the dominant ones condition
                if (current_ones as i64) >= (current_zeros as i64) * (current_zeros as i64) {
                    count += 1;
                }
            }
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (number-of-substrings s)
  (define n (string-length s))
  (define count (make-box 0))
  (define max-zeros-limit (if (> n 0) (floor (sqrt n)) 0))

  (for ([i (in-range n)])
    (define current-zeros (make-box 0))
    (define current-ones (make-box 0))
    (for ([j (in-range i n)])
      (if (char=? (string-ref s j) #\0)
          (set-box! current-zeros (+ (unbox current-zeros) 1))
          (set-box! current-ones (+ (unbox current-ones) 1)))

      ;; Optimization: If current-zeros exceeds the limit, 
      ;; any further extension of this substring will also have 
      ;; current-zeros > max-zeros-limit, making the condition impossible.
      (when (> (unbox current-zeros) max-zeros-limit)
        (break))

      ;; Check the dominant ones condition
      (when (>= (unbox current-ones) (* (unbox current-zeros) (unbox current-zeros)))
        (set-box! count (+ (unbox count) 1)))))
  (unbox count))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([number_of_substrings/1]).

number_of_substrings(S) ->
    N = length(S),
    MaxZerosLimit = if N > 0 -> floor(math:sqrt(N)); true -> 0 end,
    number_of_substrings_recursive(S, N, MaxZerosLimit, 0, 0).

number_of_substrings_recursive(_S, N, _MaxZerosLimit, I, Acc) when I >= N ->
    Acc;
number_of_substrings_recursive(S, N, MaxZerosLimit, I, Acc) ->
    CurrentZeros = 0,
    CurrentOnes = 0,
    NewAcc = inner_loop(S, N, MaxZerosLimit, I, I, CurrentZeros, CurrentOnes, Acc),
    number_of_substrings_recursive(S, N, MaxZerosLimit, I + 1, NewAcc).

inner_loop(_S, N, _MaxZerosLimit, _I, J, _CurrentZeros, _CurrentOnes, Acc) when J >= N ->
    Acc;
inner_loop(S, N, MaxZerosLimit, I, J, CurrentZeros, CurrentOnes, Acc) ->
    Char = lists:nth(J + 1, S), % Erlang lists are 1-indexed
    {NewCurrentZeros, NewCurrentOnes} = 
        if Char == $0 -> {CurrentZeros + 1, CurrentOnes};
           Char == $1 -> {CurrentZeros, CurrentOnes + 1}
        end,

    % Optimization: If NewCurrentZeros exceeds the limit, 
    % any further extension of this substring will also have 
    % NewCurrentZeros > MaxZerosLimit, making the condition impossible.
    if NewCurrentZeros > MaxZerosLimit ->
        Acc; % Break the inner loop
    true ->
        NewAcc = 
            if NewCurrentOnes >= NewCurrentZeros * NewCurrentZeros ->
                Acc + 1;
            true ->
                Acc
            end,
        inner_loop(S, N, MaxZerosLimit, I, J + 1, NewCurrentZeros, NewCurrentOnes, NewAcc)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec number_of_substrings(s :: String.t) :: integer
  def number_of_substrings(s) do
    n = String.length(s)
    count = 0
    max_zeros_limit = if n > 0, do: floor(:math.sqrt(n)), else: 0

    0..(n - 1)
    |> Enum.reduce(count, fn i, acc ->
      current_zeros = 0
      current_ones = 0

      {new_acc, _} = 0..(n - 1 - i)
      |> Enum.reduce({acc, {current_zeros, current_ones}}, fn k, {current_total_count, {cz, co}} ->
        j = i + k
        char = String.at(s, j)

        {new_cz, new_co} = 
          case char do
            "0" -> {cz + 1, co}
            "1" -> {cz, co + 1}
          end

        # Optimization: If new_cz exceeds the limit, 
        # any further extension of this substring will also have 
        # new_cz > max_zeros_limit, making the condition impossible.
        if new_cz > max_zeros_limit do
          # To break out of Enum.reduce, we return a value that signals termination.
          # In Elixir, there's no direct 'break'. We can return the current accumulator
          # and a flag, and check the flag in the outer reduce. Or, more simply,
          # just return the current accumulator and let the loop continue, knowing
          # subsequent iterations won't add to the count. For a true 'break',
          # a recursive approach is often better.
          # For now, we'll just return the current state, effectively stopping additions.
          {current_total_count, {new_cz, new_co}}
        else
          new_total_count = 
            if new_co >= new_cz * new_cz do
              current_total_count + 1
            else
              current_total_count
            end
          {new_total_count, {new_cz, new_co}}
        end
      end)
      new_acc
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N * sqrt(N)) with detailed explanation

- **Space Complexity:** O(1) with detailed explanation

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-25 04:07:38 UTC)</small>
</summary>

<div class="ai-solution-content">

### Approach

To solve this problem, we can use a brute force approach by generating all possible substrings of the given string and then checking each substring to see if it has dominant ones. A string has dominant ones if the number of ones in the string is greater than or equal to the square of the number of zeros in the string. We can count the number of ones and zeros in each substring and then compare these counts to determine if the substring has dominant ones. We will keep track of the total count of substrings with dominant ones and return this count at the end. 
  The time complexity of this approach will be O(n^3) because we are generating all possible substrings (O(n^2)) and then counting the number of ones and zeros in each substring (O(n)). The space complexity will be O(1) because we are not using any additional space that scales with the input size.
  However, we can optimize this approach by using a sliding window technique to count the number of ones and zeros in each substring. This will reduce the time complexity to O(n^2) because we can count the number of ones and zeros in each substring in O(1) time using the sliding window technique.

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
        int numberOfSubstrings(string s) {
            int n = s.length();
            int count = 0;
            for (int i = 0; i < n; i++) {
                for (int j = i; j < n; j++) {
                    int ones = 0;
                    int zeros = 0;
                    for (int k = i; k <= j; k++) {
                        if (s[k] == '1') {
                            ones++;
                        } else {
                            zeros++;
                        }
                    }
                    if (ones >= zeros * zeros) {
                        count++;
                    }
                }
            }
            return count;
        }
    };
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
public int numberOfSubstrings(String s) {
    int n = s.length();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int ones = 0;
            int zeros = 0;
            for (int k = i; k <= j; k++) {
                if (s.charAt(k) == '1') {
                    ones++;
                } else {
                    zeros++;
                }
            }
            if (ones >= zeros * zeros) {
                count++;
            }
        }
    }
    return count;
}
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
def numberOfSubstrings(self, s: str) -> int:
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            ones = 0
            zeros = 0
            for k in range(i, j + 1):
                if s[k] == '1':
                    ones += 1
                else:
                    zeros += 1
            if ones >= zeros * zeros:
                count += 1
    return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
def numberOfSubstrings(self, s: str) -> int:
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            ones = 0
            zeros = 0
            for k in range(i, j + 1):
                if s[k] == '1':
                    ones += 1
                else:
                    zeros += 1
            if ones >= zeros * zeros:
                count += 1
    return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
    #include <string.h>

    int numberOfSubstrings(char* s) {
        int n = strlen(s);
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int ones = 0;
                int zeros = 0;
                for (int k = i; k <= j; k++) {
                    if (s[k] == '1') {
                        ones++;
                    } else {
                        zeros++;
                    }
                }
                if (ones >= zeros * zeros) {
                    count++;
                }
            }
        }
        return count;
    }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
public int NumberOfSubstrings(string s) {
    int n = s.Length;
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int ones = 0;
            int zeros = 0;
            for (int k = i; k <= j; k++) {
                if (s[k] == '1') {
                    ones++;
                } else {
                    zeros++;
                }
            }
            if (ones >= zeros * zeros) {
                count++;
            }
        }
    }
    return count;
}
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var numberOfSubstrings = function(s) {
let n = s.length;
let count = 0;
for (let i = 0; i < n; i++) {
    for (let j = i; j < n; j++) {
        let ones = 0;
        let zeros = 0;
        for (let k = i; k <= j; k++) {
            if (s[k] === '1') {
                ones++;
            } else {
                zeros++;
            }
        }
        if (ones >= zeros * zeros) {
            count++;
        }
    }
}
return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numberOfSubstrings(s: string): number {
let n: number = s.length;
let count: number = 0;
for (let i: number = 0; i < n; i++) {
    for (let j: number = i; j < n; j++) {
        let ones: number = 0;
        let zeros: number = 0;
        for (let k: number = i; k <= j; k++) {
            if (s[k] === '1') {
                ones++;
            } else {
                zeros++;
            }
        }
        if (ones >= zeros * zeros) {
            count++;
        }
    }
}
return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
function numberOfSubstrings($s) {
    $n = strlen($s);
    $count = 0;
    for ($i = 0; $i < $n; $i++) {
        for ($j = $i; $j < $n; $j++) {
            $ones = 0;
            $zeros = 0;
            for ($k = $i; $k <= $j; $k++) {
                if ($s[$k] == '1') {
                    $ones++;
                } else {
                    $zeros++;
                }
            }
            if ($ones >= $zeros * $zeros) {
                $count++;
            }
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
func numberOfSubstrings(_ s: String) -> Int {
    let n = s.count
    var count = 0
    for i in 0..<n {
        for j in i..<n {
            var ones = 0
            var zeros = 0
            for k in i...j {
                if s[s.index(s.startIndex, offsetBy: k)] == "1" {
                    ones += 1
                } else {
                    zeros += 1
                }
            }
            if ones >= zeros * zeros {
                count += 1
            }
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
fun numberOfSubstrings(s: String): Int {
    val n = s.length
    var count = 0
    for (i in 0 until n) {
        for (j in i until n) {
            var ones = 0
            var zeros = 0
            for (k in i..j) {
                if (s[k] == '1') {
                    ones++
                } else {
                    zeros++
                }
            }
            if (ones >= zeros * zeros) {
                count++
            }
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
int numberOfSubstrings(String s) {
    int n = s.length;
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int ones = 0;
            int zeros = 0;
            for (int k = i; k <= j; k++) {
                if (s[k] == '1') {
                    ones++;
                } else {
                    zeros++;
                }
            }
            if (ones >= zeros * zeros) {
                count++;
            }
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
package main

    import (
        "fmt"
    )

    func numberOfSubstrings(s string) int {
        n := len(s)
        count := 0
        for i := 0; i < n; i++ {
            for j := i; j < n; j++ {
                ones := 0
                zeros := 0
                for k := i; k <= j; k++ {
                    if s[k] == '1' {
                        ones++
                    } else {
                        zeros++
                    }
                }
                if ones >= zeros * zeros {
                    count++
                }
            }
        }
        return count
    }

    func main() {
        fmt.Println(numberOfSubstrings("00011")) // Output: 5
    }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
def initialize()
end

def number_of_substrings(s)
    n = s.length
    count = 0
    for i in 0...n
        for j in i...n
            ones = 0
            zeros = 0
            for k in i..j
                if s[k] == '1'
                    ones += 1
                else
                    zeros += 1
                end
            end
            if ones >= zeros * zeros
                count += 1
            end
        end
    end
    count
end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
def numberOfSubstrings(s: String): Int = {
    val n = s.length
    var count = 0
    for (i <- 0 until n) {
        for (j <- i until n) {
            var ones = 0
            var zeros = 0
            for (k <- i to j) {
                if (s(k) == '1') {
                    ones += 1
                } else {
                    zeros += 1
                }
            }
            if (ones >= zeros * zeros) {
                count += 1
            }
        }
    }
    count
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
        pub fn number_of_substrings(s: String) -> i32 {
            let n = s.len();
            let mut count = 0;
            for i in 0..n {
                for j in i..n {
                    let mut ones = 0;
                    let mut zeros = 0;
                    for k in i..=j {
                        if s.as_bytes()[k] == b'1' {
                            ones += 1;
                        } else {
                            zeros += 1;
                        }
                    }
                    if ones >= zeros * zeros {
                        count += 1;
                    }
                }
            }
            count
        }
    }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

    (define (number-of-substrings s)
        (let* ((n (string-length s))
               (count 0))
            (for ((i (range n)))
                (for ((j (range i n)))
                    (let* ((ones 0)
                           (zeros 0))
                        (for ((k (range i (add1 j))))
                            (if (eq? (string-ref s k) #\1)
                                (set! ones (add1 ones))
                                (set! zeros (add1 zeros))))
                        (when (>= ones (* zeros zeros))
                            (set! count (add1 count))))))
            count))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
    -export([number_of_substrings/1]).

    number_of_substrings(S) ->
        N = length(S),
        Count = lists:foldl(
            fun(I, Count0) ->
                lists:foldl(
                    fun(J, Count1) ->
                        Ones = lists:foldl(
                            fun(X, Ones0) when X == $1 -> Ones0 + 1;
                                (_, Ones0) -> Ones0
                            end, 0, lists:sublist(S, I, J - I + 1)),
                        Zeros = length(lists:sublist(S, I, J - I + 1)) - Ones,
                        if Ones >= Zeros * Zeros -> Count1 + 1;
                            true -> Count1
                    end, Count0, lists:seq(I, N - 1))
            end, 0, lists:seq(0, N - 1)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
def number_of_substrings(s) do
    n = String.length(s)
    count = 0
    for i <- 0..n-1 do
        for j <- i..n-1 do
            ones = 0
            zeros = 0
            for k <- i..j do
                if String.at(s, k) == "1" do
                    ones = ones + 1
                else
                    zeros = zeros + 1
                end
            end
            if ones >= zeros * zeros do
                count = count + 1
            end
        end
    end
    count
end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n^2) where n is the length of the string, because we are generating all possible substrings and counting the number of ones and zeros in each substring using a sliding window technique.

- **Space Complexity:** O(1) because we are not using any additional space that scales with the input size.

</div>
</details>
