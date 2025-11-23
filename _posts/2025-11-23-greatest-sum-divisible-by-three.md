---
layout: post
title: "Greatest Sum Divisible by Three"
date: 2025-11-23 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Dynamic Programming", "Greedy", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/greatest-sum-divisible-by-three/
---

## Problem #1262: Greatest Sum Divisible by Three

**Difficulty:** Medium

**Topics:** Array, Dynamic Programming, Greedy, Sorting

## Problem Description

Given an integer array `nums`, return _the**maximum possible sum** of elements of the array such that it is divisible by three_.

**Example 1:**

``` Input: nums = [3,6,5,1,8] Output: 18 Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3). ``` 

**Example 2:**

``` Input: nums = [4] Output: 0 Explanation: Since 4 is not divisible by 3, do not pick any number. ``` 

**Example 3:**

``` Input: nums = [1,2,3,4,4] Output: 12 Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3). ``` 

**Constraints:**

  * `1 <= nums.length <= 4 * 104`
  * `1 <= nums[i] <= 104`

## Hints

1. Represent the state as DP[pos][mod]: maximum possible sum starting in the position "pos" in the array where the current sum modulo 3 is equal to mod.

## ✨ AI-Generated Solution (gemini-2.5-flash)

### Approach

Failed to parse AI response

### Code

<div class="code-tabs">
  <input type="radio" name="code-lang" id="lang-python" checked>
  <div class="tab-labels">
    <label for="lang-python">Python</label>
  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
# Failed to parse response
# Raw output:
```json
{
  "approach": "The problem asks us to find the maximum possible sum of elements from a given integer array `nums` such that this sum is perfectly divisible by three. This is a classic dynamic programming problem where we need to keep track of sums based on their remainder when divided by three.\n\nWe define a dynamic programming array, `dp`, of size three. Each element `dp[i]` will store the maximum sum encountered so far that has a remainder of `i` when divided by 3. Specifically:\n-
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** N/A
- **Space Complexity:** N/A
