---
layout: post
title: "Check If All 1's Are at Least Length K Places Away"
date: 2025-11-17 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
---

## Problem #1437: Check If All 1's Are at Least Length K Places Away

**Difficulty:** Easy

**Topics:** Array

## Problem Description

Given an binary array `nums` and an integer `k`, return `true` _if all_`1` _'s are at least_`k` _places away from each other, otherwise return_`false`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/04/15/sample_1_1791.png)

``` Input: nums = [1,0,0,0,1,0,0,1], k = 2 Output: true Explanation: Each of the 1s are at least 2 places away from each other. ``` 

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/04/15/sample_2_1791.png)

``` Input: nums = [1,0,0,1,0,1], k = 2 Output: false Explanation: The second 1 and third 1 are only one apart from each other. ``` 

**Constraints:**

  * `1 <= nums.length <= 105`
  * `0 <= k <= nums.length`
  * `nums[i]` is `0` or `1`

### Illustrations

![](https://assets.leetcode.com/uploads/2020/04/15/sample_1_1791.png)

![](https://assets.leetcode.com/uploads/2020/04/15/sample_2_1791.png)

## Hints

1. Each time you find a number 1, check whether or not it is K or more places away from the next one. If it's not, return false.

## ⚡ AI-Generated Solution (GROQ)

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
  "approach": "The approach is to iterate over the given binary array `nums` and keep track of the last seen 1. If the distance between the current 1 and the last seen 1 is less than `k`, return False. If the iteration completes without finding any such pair, return True.",
  "time_complexity": "O(n) where n is the length of the array `nums`, because we are doing a single pass through the array.",
  "space_complexity": "O(1) because we are using a constant amount of space to store the
{% endhighlight %}

  </div>

</div>


### Complexity Analysis

- **Time Complexity:** N/A

- **Space Complexity:** N/A
