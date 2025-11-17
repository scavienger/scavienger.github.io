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

The problem asks us to count the total number of substrings consisting only of '1's in a given binary string `s`, returning the result modulo `10^9 + 7`. 

The core insight comes from observing how many '1'-only substrings can be formed from a contiguous block of `n` '1's. For example, if we have a block "111" (where `n=3`):
- '1' appears 3 times
- '11' appears 2 times
- '111' appears 1 time
The total count is 3 + 2 + 1 = 6.

This is the sum of the first `n` natural numbers, which can be calculated using the formula for triangular numbers: `n * (n + 1) / 2`.

Our approach is to iterate through the string and identify consecutive blocks of '1's. Whenever we encounter a '0' or reach the end of the string, it signifies the end of a block of consecutive '1's. At this point, we calculate the contribution of that block to the total count using the formula `n * (n + 1) / 2`, where `n` is the length of the current block of '1's. We then add this contribution to our running total, applying the modulo operation at each addition to prevent integer overflow.

**Algorithm:**
1.  Initialize `total_count = 0` and `current_consecutive_ones = 0`. Set `MOD = 10^9 + 7`.
2.  Iterate through each character `char` in the input string `s`:
    a.  If `char` is `'1'`, increment `current_consecutive_ones`.
    b.  If `char` is `'0'`:
        i.  This indicates the end of a block of '1's. Calculate its contribution: `contribution = (current_consecutive_ones * (current_consecutive_ones + 1)) / 2`.
        ii. Add this `contribution` to `total_count`, ensuring to take the result modulo `MOD`: `total_count = (total_count + contribution) % MOD`.
        iii. Reset `current_consecutive_ones` to 0.
3.  After the loop finishes, there might be a pending block of '1's if the string ends with '1's (e.g., `s = "011"`). Perform the contribution calculation one last time for any remaining `current_consecutive_ones` and add it to `total_count` modulo `MOD`.
4.  Return `total_count`.

**Example: s = "0110111"**
- Initialize `total_count = 0`, `current_consecutive_ones = 0`.
- `s[0] = '0'`: `current_consecutive_ones` is 0. No contribution. Reset `current_consecutive_ones = 0`.
- `s[1] = '1'`: `current_consecutive_ones = 1`.
- `s[2] = '1'`: `current_consecutive_ones = 2`.
- `s[3] = '0'`: End of block "11". `n = 2`. Contribution = `(2 * 3) / 2 = 3`. `total_count = (0 + 3) % MOD = 3`. Reset `current_consecutive_ones = 0`.
- `s[4] = '1'`: `current_consecutive_ones = 1`.
- `s[5] = '1'`: `current_consecutive_ones = 2`.
- `s[6] = '1'`: `current_consecutive_ones = 3`.
- End of string. Remaining block "111". `n = 3`. Contribution = `(3 * 4) / 2 = 6`. `total_count = (3 + 6) % MOD = 9`.
- Return 9.

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
        current_consecutive_ones = 0

        for char in s:
            if char == '1':
                current_consecutive_ones += 1
            else:
                # End of a block of ones, calculate contribution
                # sum of 1 to n is n * (n + 1) / 2
                # Python handles large integers automatically, so no explicit casting needed.
                total_count = (total_count + (current_consecutive_ones * (current_consecutive_ones + 1)) // 2) % MOD
                current_consecutive_ones = 0
        
        # After loop, handle any remaining consecutive ones at the end of the string
        total_count = (total_count + (current_consecutive_ones * (current_consecutive_ones + 1)) // 2) % MOD
        
        return total_count
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
    public int numSub(String s) {
        long MOD = 1_000_000_007; // Using long for MOD is good practice though int value fits in int.
        long totalCount = 0; // Use long to ensure intermediate sums don't overflow before modulo
        int currentConsecutiveOnes = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                currentConsecutiveOnes++;
            } else {
                // End of a block of ones, calculate contribution
                // sum of 1 to n is n * (n + 1) / 2
                // Cast currentConsecutiveOnes to long for multiplication to prevent overflow.
                long n = currentConsecutiveOnes; 
                totalCount = (totalCount + (n * (n + 1)) / 2) % MOD;
                currentConsecutiveOnes = 0;
            }
        }
        
        // After loop, handle any remaining consecutive ones at the end of the string
        long n = currentConsecutiveOnes; // Cast currentConsecutiveOnes to long
        totalCount = (totalCount + (n * (n + 1)) / 2) % MOD;
        
        return (int) totalCount; // Cast the final result back to int
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
#include <string>

class Solution {
public:
    int numSub(std::string s) {
        long long MOD = 1000000007LL; // Use LL suffix for long long literal
        long long totalCount = 0; // Use long long for total count to prevent overflow before modulo
        int currentConsecutiveOnes = 0;

        for (char c : s) {
            if (c == '1') {
                currentConsecutiveOnes++;
            } else {
                // End of a block of ones, calculate contribution
                // sum of 1 to n is n * (n + 1) / 2
                // Cast currentConsecutiveOnes to long long for multiplication to prevent overflow.
                long long n = currentConsecutiveOnes; 
                totalCount = (totalCount + (n * (n + 1)) / 2) % MOD;
                currentConsecutiveOnes = 0;
            }
        }
        
        // After loop, handle any remaining consecutive ones at the end of the string
        long long n = currentConsecutiveOnes; // Cast currentConsecutiveOnes to long long
        totalCount = (totalCount + (n * (n + 1)) / 2) % MOD;
        
        return static_cast<int>(totalCount); // Cast the final result back to int
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
    let currentConsecutiveOnes = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') {
            currentConsecutiveOnes++;
        } else {
            // End of a block of ones, calculate contribution
            // sum of 1 to n is n * (n + 1) / 2
            // JavaScript numbers handle large integers up to 2^53 - 1 precisely,
            // which is sufficient for n*(n+1)/2 where n <= 10^5.
            const n = currentConsecutiveOnes;
            totalCount = (totalCount + (n * (n + 1)) / 2) % MOD;
            currentConsecutiveOnes = 0;
        }
    }
    
    // After loop, handle any remaining consecutive ones at the end of the string
    const n = currentConsecutiveOnes;
    totalCount = (totalCount + (n * (n + 1)) / 2) % MOD;
    
    return totalCount;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function numSub(s: string): number {
    const MOD = 10**9 + 7;
    let totalCount: number = 0;
    let currentConsecutiveOnes: number = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') {
            currentConsecutiveOnes++;
        } else {
            // End of a block of ones, calculate contribution
            // sum of 1 to n is n * (n + 1) / 2
            // TypeScript/JavaScript numbers handle large integers up to 2^53 - 1 precisely,
            // which is sufficient for n*(n+1)/2 where n <= 10^5.
            const n: number = currentConsecutiveOnes;
            totalCount = (totalCount + (n * (n + 1)) / 2) % MOD;
            currentConsecutiveOnes = 0;
        }
    }
    
    // After loop, handle any remaining consecutive ones at the end of the string
    const n: number = currentConsecutiveOnes;
    totalCount = (totalCount + (n * (n + 1)) / 2) % MOD;
    
    return totalCount;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

func numSub(s string) int {
    var MOD int = 1_000_000_007
    var totalCount int = 0 // totalCount will not exceed MOD, so int is sufficient after modulo.
    var currentConsecutiveOnes int = 0

    for i := 0; i < len(s); i++ {
        if s[i] == '1' { // Character comparison is done with byte values in Go strings
            currentConsecutiveOnes++
        } else {
            // End of a block of ones, calculate contribution
            // sum of 1 to n is n * (n + 1) / 2
            // Must cast currentConsecutiveOnes to int64 for multiplication
            // to prevent overflow before division, as n*(n+1) can exceed max int32.
            n := int64(currentConsecutiveOnes) 
            contribution := (n * (n + 1)) / 2
            totalCount = (totalCount + int(contribution)) % MOD // Cast back to int for totalCount
            currentConsecutiveOnes = 0
        }
    }
    
    // After loop, handle any remaining consecutive ones at the end of the string
    n := int64(currentConsecutiveOnes)
    contribution := (n * (n + 1)) / 2
    totalCount = (totalCount + int(contribution)) % MOD
    
    return totalCount
}
{% endhighlight %}

  </div>

</div>


### Complexity Analysis

- **Time Complexity:** O(N)

- **Space Complexity:** O(1)
