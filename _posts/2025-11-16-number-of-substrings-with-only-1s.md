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

## ⚡ AI-Generated Solution (llama-3.3-70b-versatile)

### Approach

Failed to parse AI response

### Code

<div class="code-tabs">
  <input type="radio" name="code-lang" id="lang-python">
  <div class="tab-labels">
    <label for="lang-python">Python</label>
  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
# Failed to parse response
# Raw output:
```json
{
  "approach": "To solve this problem, we can iterate through the string and count the number of consecutive 1s. For each group of consecutive 1s, we calculate the number of substrings using the formula (n + 1) * n // 2, where n is the number of consecutive 1s. We then add this to our total count. We use the modulo operator to prevent overflow and ensure the result is within the range of 10^9 + 7.",
  "time_complexity": "O(n) where n is the length of the string, because we are scanning
{% endhighlight %}

  </div>

</div>


### Complexity Analysis

- **Time Complexity:** N/A

- **Space Complexity:** N/A
