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

Given a binary string `s`, return _the number of substrings with all characters_ `1` _' s_. Since the answer may be too large, return it modulo `109 + 7`.

 

**Example 1:**
    
    
    **Input:** s = "0110111"
    **Output:** 9
    **Explanation:** There are 9 substring in total with only 1's characters.
    "1" -> 5 times.
    "11" -> 3 times.
    "111" -> 1 time.

**Example 2:**
    
    
    **Input:** s = "101"
    **Output:** 2
    **Explanation:** Substring "1" is shown 2 times in s.
    

**Example 3:**
    
    
    **Input:** s = "111111"
    **Output:** 21
    **Explanation:** Each substring contains only 1's characters.
    

 

**Constraints:**

  * `1 <= s.length <= 105`
  * `s[i]` is either `'0'` or `'1'`.

## Hints

1. Count number of 1s in each consecutive-1 group. For a group with n consecutive 1s, the total contribution of it to the final answer is (n + 1) * n // 2.

## ✨ AI-Generated Solution (GEMINI)

### Approach

The problem asks us to count the total number of substrings consisting only of '1's in a given binary string `s`. Since the answer can be very large, we need to return it modulo `10^9 + 7`.

The core idea is to recognize that substrings consisting only of '1's can only be formed from consecutive sequences of '1's. For example, in "0110111", the relevant parts are "11" and "111". The '0's act as delimiters, effectively breaking the string into segments of consecutive '1's.

Consider a continuous block of `n` '1's, for instance, "111" has `n=3`. The substrings entirely composed of '1's within this block are:
- "1" (length 1): appears `n` times.
- "11" (length 2): appears `n-1` times.
- ...
- "11...1" (length `n`): appears 1 time.

The total number of such substrings within a block of `n` consecutive '1's is the sum `n + (n-1) + ... + 1`. This sum is given by the formula for the sum of the first `n` natural numbers: `n * (n + 1) / 2`.

With this understanding, the algorithm is as follows:
1. Initialize `total_substrings` to 0 and `current_ones` to 0. `total_substrings` will store the final count, and `current_ones` will track the length of the current consecutive block of '1's being examined.
2. Define the modulo constant `MOD = 10^9 + 7`.
3. Iterate through each character `c` in the input string `s`:
   a. If `c` is '1', increment `current_ones`. This means the current block of '1's is extending.
   b. If `c` is '0', the current block of '1's is broken. At this point, `current_ones` holds the length of the block of '1's that just ended. Calculate its contribution to `total_substrings` using the formula `current_ones * (current_ones + 1) / 2`. Add this contribution to `total_substrings`, ensuring to take the modulo `MOD` at each addition to prevent overflow. After processing the block, reset `current_ones` to 0 to start counting a new potential block.
4. After the loop finishes, there might be a remaining block of '1's at the very end of the string (if the string doesn't end with a '0'). Perform the same calculation for this final `current_ones` count and add it to `total_substrings`, again taking the modulo.
5. Return `total_substrings`.

**Important Note on Integer Overflow:** The maximum length of `s` is `10^5`. If a string consists of `10^5` '1's, `n` would be `10^5`. The contribution `n * (n + 1) / 2` would be approximately `(10^5)^2 / 2 = 5 * 10^9`. This value exceeds the maximum capacity of a standard 32-bit signed integer (approximately `2 * 10^9`). Therefore, for languages like Java, C++, and Go, `total_substrings` and the intermediate calculation for `contribution` must use 64-bit integers (`long` in Java, `long long` in C++, `int64` in Go). Python handles large integers automatically. JavaScript numbers can lose precision for integers larger than `2^53 - 1`, so `BigInt` should be used for the contribution calculation in JavaScript/TypeScript.

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
    <label for="lang-javascript">JavaScript</label>
    <label for="lang-typescript">TypeScript</label>
    <label for="lang-go">Go</label>
  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
import math

class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        total_substrings = 0
        current_ones = 0
        
        for char in s:
            if char == '1':
                current_ones += 1
            else:
                # If a '0' is encountered, the current block of '1's ends.
                # Calculate its contribution: n * (n + 1) // 2
                # Python handles large integers automatically, so no special BigInt needed.
                contribution = current_ones * (current_ones + 1) // 2
                total_substrings = (total_substrings + contribution) % MOD
                current_ones = 0 # Reset count for the next block
        
        # After the loop, there might be a pending block of '1's at the end of the string
        contribution = current_ones * (current_ones + 1) // 2
        total_substrings = (total_substrings + contribution) % MOD
        
        return total_substrings
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
    public int numSub(String s) {
        final int MOD = 1_000_000_007; // 10^9 + 7
        long totalSubstrings = 0; // Use long to accumulate sum before modulo
        int currentOnes = 0;
        
        for (char c : s.toCharArray()) {
            if (c == '1') {
                currentOnes++;
            } else {
                // If a '0' is encountered, the current block of '1's ends.
                // Calculate its contribution: n * (n + 1) / 2
                // Cast to long before multiplication to prevent overflow for n*(n+1)
                long n = currentOnes;
                long contribution = n * (n + 1) / 2;
                totalSubstrings = (totalSubstrings + contribution) % MOD;
                currentOnes = 0; // Reset count for the next block
            }
        }
        
        // After the loop, there might be a pending block of '1's at the end of the string
        long n = currentOnes;
        long contribution = n * (n + 1) / 2;
        totalSubstrings = (totalSubstrings + contribution) % MOD;
        
        return (int) totalSubstrings; // Result fits in int because of modulo
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
        const int MOD = 1e9 + 7; // 10^9 + 7
        long long totalSubstrings = 0; // Use long long to accumulate sum before modulo
        int currentOnes = 0;
        
        for (char c : s) {
            if (c == '1') {
                currentOnes++;
            } else {
                // If a '0' is encountered, the current block of '1's ends.
                // Calculate its contribution: n * (n + 1) / 2
                // Cast to long long before multiplication to prevent overflow for n*(n+1)
                long long n = currentOnes;
                long long contribution = n * (n + 1) / 2;
                totalSubstrings = (totalSubstrings + contribution) % MOD;
                currentOnes = 0; // Reset count for the next block
            }
        }
        
        // After the loop, there might be a pending block of '1's at the end of the string
        long long n = currentOnes;
        long long contribution = n * (n + 1) / 2;
        totalSubstrings = (totalSubstrings + contribution) % MOD;
        
        return static_cast<int>(totalSubstrings); // Result fits in int because of modulo
    }
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
class Solution {
    numSub(s) {
        const MOD = 1_000_000_007; // 10^9 + 7
        let totalSubstrings = 0;
        let currentOnes = 0;
        
        for (let i = 0; i < s.length; i++) {
            if (s[i] === '1') {
                currentOnes++;
            } else {
                // Calculate contribution for the completed block of '1's
                // Use BigInt for calculation involving n*(n+1) to avoid precision loss,
                // then convert back to Number for addition to totalSubstrings.
                const nBigInt = BigInt(currentOnes);
                const contributionBigInt = (nBigInt * (nBigInt + 1n)) / 2n;
                totalSubstrings = (totalSubstrings + Number(contributionBigInt % BigInt(MOD))) % MOD;
                currentOnes = 0; // Reset count
            }
        }
        
        // Handle any pending block of '1's at the end
        const nBigInt = BigInt(currentOnes);
        const contributionBigInt = (nBigInt * (nBigInt + 1n)) / 2n;
        totalSubstrings = (totalSubstrings + Number(contributionBigInt % BigInt(MOD))) % MOD;
        
        return totalSubstrings;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
class Solution {
    numSub(s: string): number {
        const MOD = 1_000_000_007; // 10^9 + 7
        let totalSubstrings: number = 0;
        let currentOnes: number = 0;
        
        for (let i = 0; i < s.length; i++) {
            if (s[i] === '1') {
                currentOnes++;
            } else {
                // Calculate contribution for the completed block of '1's
                // Use BigInt for calculation involving n*(n+1) to avoid precision loss,
                // then convert back to Number for addition to totalSubstrings.
                const nBigInt = BigInt(currentOnes);
                const contributionBigInt = (nBigInt * (nBigInt + 1n)) / 2n;
                totalSubstrings = (totalSubstrings + Number(contributionBigInt % BigInt(MOD))) % MOD;
                currentOnes = 0; // Reset count
            }
        }
        
        // Handle any pending block of '1's at the end
        const nBigInt = BigInt(currentOnes);
        const contributionBigInt = (nBigInt * (nBigInt + 1n)) / 2n;
        totalSubstrings = (totalSubstrings + Number(contributionBigInt % BigInt(MOD))) % MOD;
        
        return totalSubstrings;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

import "fmt"

func numSub(s string) int {
    const MOD int = 1_000_000_007 // 10^9 + 7
    totalSubstrings := 0
    currentOnes := 0
    
    for _, char := range s {
        if char == '1' {
            currentOnes++
        } else {
            // If a '0' is encountered, the current block of '1's ends.
            // Calculate its contribution: n * (n + 1) / 2
            // Cast to int64 before multiplication to prevent overflow for n*(n+1)
            // contribution should be calculated modulo MOD as well before adding
            n := int64(currentOnes)
            contribution := (n * (n + 1) / 2) % int64(MOD)
            totalSubstrings = (totalSubstrings + int(contribution)) % MOD
            currentOnes = 0 // Reset count for the next block
        }
    }
    
    // After the loop, there might be a pending block of '1's at the end of the string
    n := int64(currentOnes)
    contribution := (n * (n + 1) / 2) % int64(MOD)
    totalSubstrings = (totalSubstrings + int(contribution)) % MOD
    
    return totalSubstrings
}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N), where N is the length of the input string `s`. We iterate through the string exactly once. Each character processing (incrementing a counter, calculating a sum, and performing modulo) takes constant time.
- **Space Complexity:** O(1). We use a few constant extra variables (`total_substrings`, `current_ones`, and `MOD`) regardless of the input string's length. This does not count the space for the input string itself.
