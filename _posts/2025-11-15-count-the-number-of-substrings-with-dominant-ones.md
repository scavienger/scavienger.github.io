---
layout: post
title: "Count the Number of Substrings With Dominant Ones"
date: 2025-11-15 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Sliding Window", "Enumeration"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/
---

## Problem #3234: Count the Number of Substrings With Dominant Ones

**Difficulty:** Medium

**Topics:** String, Sliding Window, Enumeration

## Problem Description

You are given a binary string `s`.

Return the number of substrings with **dominant** ones.

A string has **dominant** ones if the number of ones in the string is **greater than or equal to** the **square** of the number of zeros in the string.

**Example 1:**

**Input:** s = "00011"

**Output:** 5

**Explanation:**

The substrings with dominant ones are shown in the table below.

``` i j s[i..j] Number of Zeros Number of Ones 3 3 1 0 1 4 4 1 0 1 2 3 01 1 1 3 4 11 0 2 2 4 011 1 2 ``` 

**Example 2:**

**Input:** s = "101101"

**Output:** 16

**Explanation:**

The substrings with **non-dominant** ones are shown in the table below.

Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.

``` i j s[i..j] Number of Zeros Number of Ones 1 1 0 1 0 4 4 0 1 0 1 4 0110 2 2 0 4 10110 2 3 1 5 01101 2 3 ``` 

**Constraints:**

  * `1 <= s.length <= 4 * 104`
  * `s` consists only of characters `'0'` and `'1'`.

## Hints

1. Let us fix the starting index <code>l</code> of the substring and count the number of indices <code>r</code> such that <code>l <= r</code> and the substring <code>s[l..r]</code> has dominant ones.

2. A substring with dominant ones has at most <code>sqrt(n)</code> zeros.

3. We cannot iterate over every <code>r</code> and check if the  <code>s[l..r]</code> has dominant ones. Instead, we iterate over the next <code>sqrt(n)</code> zeros to the left of <code>l</code> and count the number of substrings with dominant ones where the current zero is the rightmost zero of the substring.

## ✨ AI-Generated Solution (gemini-2.5-flash)

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
  "approach": "The problem asks us to count substrings with \"dominant ones\", meaning the number of ones (`num_ones`) is greater than or equal to the square of the number of zeros (`num_zeros`). That is, `num_ones >= num_zeros * num_zeros`.\n\nThe string length `N` can be up to `4 * 10^4`. A naive O(N^2) approach (checking all substrings) would be too slow (`(4 * 10^4)^2 = 1.6 * 10^9` operations).\n\nThe key observation, hinted in the problem description, is that any substring with do
{% endhighlight %}

  </div>

</div>


### Complexity Analysis

- **Time Complexity:** N/A

- **Space Complexity:** N/A
