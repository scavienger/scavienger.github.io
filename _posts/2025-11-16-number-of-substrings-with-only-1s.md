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

## ✨ AI-Generated Solution (GEMINI)

### Approach

The problem asks us to count the total number of substrings consisting only of '1's in a given binary string `s`. Since the answer can be very large, we need to return it modulo `10^9 + 7`.

The core idea is to identify contiguous blocks of '1's. For any block of `n` consecutive '1's (e.g., "111" has `n=3`), the substrings with only '1's that can be formed from this block are:
- `n` substrings of length 1 ("1", "1", "1")
- `n-1` substrings of length 2 ("11", "11")
- ...
- `1` substring of length `n` ("111")

The total number of such substrings for a block of `n` consecutive '1's is the sum `1 + 2 + ... + n`, which is given by the triangular number formula: `n * (n + 1) / 2`.

Our approach will be to iterate through the string, keeping track of the current count of consecutive '1's. When we encounter a '0' or reach the end of the string, it signifies the end of a block of '1's. At this point:
1. We take the `current_ones` count, let's call it `n`.
2. We calculate its contribution to the total: `n * (n + 1) / 2`.
3. We add this contribution to our running total, applying the modulo `10^9 + 7` at each addition.
4. We reset `current_ones` to 0.

After iterating through the entire string, there might be a trailing block of '1's (if the string ends with '1's). We perform one final check for `current_ones > 0` and add its contribution to the total.

**Example Trace (`s = "0110111"`):**
- Initialize `total_count = 0`, `current_ones = 0`, `MOD = 10^9 + 7`.
- Iterate through `s`:
  - `s[0] = '0'`: `current_ones` is 0, no contribution. Reset `current_ones = 0`.
  - `s[1] = '1'`: `current_ones` becomes 1.
  - `s[2] = '1'`: `current_ones` becomes 2.
  - `s[3] = '0'`: Block ends. `n = current_ones = 2`. Contribution = `2 * (2 + 1) / 2 = 3`. `total_count = (0 + 3) % MOD = 3`. Reset `current_ones = 0`.
  - `s[4] = '1'`: `current_ones` becomes 1.
  - `s[5] = '1'`: `current_ones` becomes 2.
  - `s[6] = '1'`: `current_ones` becomes 3.
- End of loop.
- Final check: `current_ones` is 3. Contribution = `3 * (3 + 1) / 2 = 6`. `total_count = (3 + 6) % MOD = 9`.
- Return `9`.

Modulo operations should be applied carefully. The sum `total_count` should be modulo `MOD` after each addition. The intermediate `n * (n + 1) / 2` can be calculated first. For `n` up to `10^5`, `n * (n+1)` can be up to `10^{10}`, which requires 64-bit integers (`long` in Java/Go, `long long` in C++, Python handles automatically, JavaScript handles sufficiently) to prevent overflow before division, if applicable.

### Code

<div class="code-tabs">
  <input type="radio" name="code-lang" id="lang-python" checked>
  <input type="radio" name="code-lang" id="lang-java">
  <input type="radio" name="code-lang" id="lang-cpp">
  <input type="radio" name="code-lang" id="lang-javascript">
  <input type="radio" name="code-lang" id="lang-typescript">
  <input type="radio" name="code-lang" id="lang-go">
  <div class="tab-labels">
    <label for="lang-python">Python</label>
    <label for="lang-java">Java</label>
    <label for="lang-cpp">C++</label>
    <label for="lang-javascript">JS</label>
    <label for="lang-typescript">TS</label>
    <label for="lang-go">Go</label>
  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        total_count = 0
        current_ones = 0

        for char in s:
            if char == '1':
                current_ones += 1
            else:
                # Block of ones ended
                if current_ones > 0:
                    # Calculate sum of 1 to current_ones (n * (n + 1) / 2)
                    contribution = current_ones * (current_ones + 1) // 2
                    total_count = (total_count + contribution) % MOD
                current_ones = 0
        
        # After the loop, check for any trailing block of ones
        if current_ones > 0:
            contribution = current_ones * (current_ones + 1) // 2
            total_count = (total_count + contribution) % MOD
            
        return total_count
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
    public int numSub(String s) {
        final int MOD = 1_000_000_007;
        long totalCount = 0;
        long currentOnes = 0;

        for (char c : s.toCharArray()) {
            if (c == '1') {
                currentOnes++;
            } else {
                // Block of ones ended
                if (currentOnes > 0) {
                    // Calculate sum of 1 to currentOnes (n * (n + 1) / 2)
                    long contribution = currentOnes * (currentOnes + 1) / 2;
                    totalCount = (totalCount + contribution) % MOD;
                }
                currentOnes = 0;
            }
        }
        
        // After the loop, check for any trailing block of ones
        if (currentOnes > 0) {
            long contribution = currentOnes * (currentOnes + 1) / 2;
            totalCount = (totalCount + contribution) % MOD;
        }
            
        return (int)totalCount;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
#include <string>
#include <vector>

class Solution {
public:
    int numSub(std::string s) {
        const int MOD = 1e9 + 7;
        long long total_count = 0;
        long long current_ones = 0;

        for (char c : s) {
            if (c == '1') {
                current_ones++;
            } else {
                // Block of ones ended
                if (current_ones > 0) {
                    // Calculate sum of 1 to current_ones (n * (n + 1) / 2)
                    long long contribution = current_ones * (current_ones + 1) / 2;
                    total_count = (total_count + contribution) % MOD;
                }
                current_ones = 0;
            }
        }
        
        // After the loop, check for any trailing block of ones
        if (current_ones > 0) {
            long long contribution = current_ones * (current_ones + 1) / 2;
            total_count = (total_count + contribution) % MOD;
        }
            
        return static_cast<int>(total_count);
    }
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
/**
 * @param {string} s
 * @return {number}
 */
var numSub = function(s) {
    const MOD = 10**9 + 7;
    let totalCount = 0;
    let currentOnes = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') {
            currentOnes++;
        } else {
            // Block of ones ended
            if (currentOnes > 0) {
                // Calculate sum of 1 to currentOnes (n * (n + 1) / 2)
                // JavaScript numbers handle up to 2^53-1 accurately for integers
                // 10^5 * (10^5 + 1) / 2 is approximately 5 * 10^9, which fits.
                let contribution = currentOnes * (currentOnes + 1) / 2;
                totalCount = (totalCount + contribution) % MOD;
            }
            currentOnes = 0;
        }
    }
    
    // After the loop, check for any trailing block of ones
    if (currentOnes > 0) {
        let contribution = currentOnes * (currentOnes + 1) / 2;
        totalCount = (totalCount + contribution) % MOD;
    }
        
    return totalCount;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function numSub(s: string): number {
    const MOD = 10**9 + 7;
    let totalCount: number = 0;
    let currentOnes: number = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') {
            currentOnes++;
        } else {
            // Block of ones ended
            if (currentOnes > 0) {
                // Calculate sum of 1 to currentOnes (n * (n + 1) / 2)
                let contribution = currentOnes * (currentOnes + 1) / 2;
                totalCount = (totalCount + contribution) % MOD;
            }
            currentOnes = 0;
        }
    }
    
    // After the loop, check for any trailing block of ones
    if (currentOnes > 0) {
        let contribution = currentOnes * (currentOnes + 1) / 2;
        totalCount = (totalCount + contribution) % MOD;
    }
        
    return totalCount;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

import (
	"fmt"
)

func numSub(s string) int {
    const MOD = 1_000_000_007
    var totalCount int = 0
    var currentOnes int = 0

    for _, r := range s {
        if r == '1' {
            currentOnes++
        } else {
            // Block of ones ended
            if currentOnes > 0 {
                // Calculate sum of 1 to currentOnes (n * (n + 1) / 2)
                // Go's int type is typically 64-bit on most systems, sufficient for 10^5 * (10^5+1)
                contribution := currentOnes * (currentOnes + 1) / 2
                totalCount = (totalCount + contribution) % MOD
            }
            currentOnes = 0
        }
    }
    
    // After the loop, check for any trailing block of ones
    if currentOnes > 0 {
        contribution := currentOnes * (currentOnes + 1) / 2
        totalCount = (totalCount + contribution) % MOD
    }
        
    return totalCount
}
{% endhighlight %}

  </div>

</div>


### Complexity Analysis

- **Time Complexity:** O(N), where N is the length of the string `s`. We iterate through the string once, performing constant time operations for each character.

- **Space Complexity:** O(1), as we only use a few integer variables to store counts and the total, regardless of the input string's length.
