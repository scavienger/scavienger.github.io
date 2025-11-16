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

The core idea is to iterate through the string and keep track of consecutive '1's. When we encounter a '1', it extends the current sequence of consecutive '1's. Each '1' at the end of a sequence of `k` consecutive '1's (i.e., this '1' is the k-th '1' in the current block) contributes `k` new substrings that *end* at its current position:
1. The single '1' itself.
2. The '11' ending at this position (if `k >= 2`).
3. The '111' ending at this position (if `k >= 3`).
...and so on, up to the sequence of `k` '1's ending at this position.

For example, consider the string `s = "111"`:
- When we process the first `'1'` (at index 0): `current_consecutive_ones` becomes 1. This '1' forms one substring: "1". We add 1 to `total_substrings`.
- When we process the second `'1'` (at index 1): `current_consecutive_ones` becomes 2. This '1' forms two substrings ending at index 1: "1" and "11". We add 2 to `total_substrings`.
- When we process the third `'1'` (at index 2): `current_consecutive_ones` becomes 3. This '1' forms three substrings ending at index 2: "1", "11", and "111". We add 3 to `total_substrings`.

Thus, for "111", the total substrings would be 1 + 2 + 3 = 6. This is equivalent to summing the length of the current consecutive '1's block each time a '1' is encountered.

When we encounter a '0', it breaks any current sequence of '1's, so we reset `current_consecutive_ones` to 0.

**Algorithm:**
1. Initialize `total_substrings` to 0.
2. Initialize `current_consecutive_ones` to 0.
3. Define `MOD = 10^9 + 7`.
4. Iterate through each character `c` in the input string `s`:
   a. If `c` is `'1'`:
      i. Increment `current_consecutive_ones`.
      ii. Add the current `current_consecutive_ones` count to `total_substrings`. Perform modulo `MOD` after each addition to prevent overflow: `total_substrings = (total_substrings + current_consecutive_ones) % MOD`.
   b. If `c` is `'0'`:
      i. Reset `current_consecutive_ones` to 0.
5. After iterating through the entire string, `total_substrings` will hold the final count.
6. Return `total_substrings`.

This approach is efficient as it processes each character once and uses only a few variables.

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
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        total_substrings = 0
        current_consecutive_ones = 0

        for char in s:
            if char == '1':
                current_consecutive_ones += 1
                total_substrings = (total_substrings + current_consecutive_ones) % MOD
            else:
                current_consecutive_ones = 0
        
        return total_substrings
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
    public int numSub(String s) {
        long MOD = 1_000_000_007L; 
        long totalSubstrings = 0;
        int currentConsecutiveOnes = 0;

        for (char c : s.toCharArray()) {
            if (c == '1') {
                currentConsecutiveOnes++;
                totalSubstrings = (totalSubstrings + currentConsecutiveOnes) % MOD;
            } else {
                currentConsecutiveOnes = 0;
            }
        }

        return (int) totalSubstrings;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
class Solution {
public:
    int numSub(string s) {
        long long MOD = 1e9 + 7; 
        long long total_substrings = 0;
        int current_consecutive_ones = 0;

        for (char c : s) {
            if (c == '1') {
                current_consecutive_ones++;
                total_substrings = (total_substrings + current_consecutive_ones) % MOD;
            } else {
                current_consecutive_ones = 0;
            }
        }

        return (int) total_substrings;
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
    let totalSubstrings = 0;
    let currentConsecutiveOnes = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') {
            currentConsecutiveOnes++;
            totalSubstrings = (totalSubstrings + currentConsecutiveOnes) % MOD;
        } else {
            currentConsecutiveOnes = 0;
        }
    }

    return totalSubstrings;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function numSub(s: string): number {
    const MOD = 10**9 + 7;
    let totalSubstrings: number = 0;
    let currentConsecutiveOnes: number = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') {
            currentConsecutiveOnes++;
            totalSubstrings = (totalSubstrings + currentConsecutiveOnes) % MOD;
        } else {
            currentConsecutiveOnes = 0;
        }
    }

    return totalSubstrings;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

func numSub(s string) int {
	MOD := 1_000_000_007
	totalSubstrings := 0
	currentConsecutiveOnes := 0

	for _, r := range s {
		if r == '1' {
			currentConsecutiveOnes++
			totalSubstrings = (totalSubstrings + currentConsecutiveOnes) % MOD
		} else {
			currentConsecutiveOnes = 0
		}
	}

	return totalSubstrings
}
{% endhighlight %}

  </div>

</div>


### Complexity Analysis

- **Time Complexity:** O(N), where N is the length of the input string `s`. We iterate through the string exactly once, performing constant time operations for each character.

- **Space Complexity:** O(1), as we only use a few integer variables to store counts and the modulo constant, regardless of the input string's length.
