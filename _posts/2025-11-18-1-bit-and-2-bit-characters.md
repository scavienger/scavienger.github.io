---
layout: post
title: "1-bit and 2-bit Characters"
date: 2025-11-18 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/1-bit-and-2-bit-characters/
---

## Problem #717: 1-bit and 2-bit Characters

**Difficulty:** Easy

**Topics:** Array

## Problem Description

We have two special characters:

  * The first character can be represented by one bit `0`.
  * The second character can be represented by two bits (`10` or `11`).

Given a binary array `bits` that ends with `0`, return `true` if the last character must be a one-bit character.

**Example 1:**

``` Input: bits = [1,0,0] Output: true Explanation: The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character. ``` 

**Example 2:**

``` Input: bits = [1,1,1,0] Output: false Explanation: The only way to decode it is two-bit character and two-bit character. So the last character is not one-bit character. ``` 

**Constraints:**

  * `1 <= bits.length <= 1000`
  * `bits[i]` is either `0` or `1`.

## Hints

1. Keep track of where the next character starts.  At the end, you want to know if you started on the last bit.

## Solution

### Approach

TODO: Add solution approach here.

### Code

```python
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
```

### Complexity Analysis

- **Time Complexity:** O(?)

- **Space Complexity:** O(?)
