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

## ✨ AI-Generated Solution (GEMINI)

### Approach

The problem asks us to determine if all '1's in a given binary array `nums` are separated by at least `k` zeros. This means if we find a '1' at index `i` and the next '1' is at index `j`, then the number of zeros between them (which is `j - i - 1`) must be greater than or equal to `k`. Equivalently, the distance between their indices, `j - i`, must be strictly greater than `k` (i.e., `j - i > k`).

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

```python
import math
from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # Initialize last_one_idx. A value like -k - 1 ensures that the
        # first '1' encountered in the array will always satisfy the
        # distance condition, as (first_idx - (-k - 1) - 1) = first_idx + k >= k.
        last_one_idx = -k - 1
        
        for i, num in enumerate(nums):
            if num == 1:
                # Calculate the number of zeros between the current '1' and the last '1'.
                # If the current '1' is at index 'i' and the previous '1' was at 'last_one_idx',
                # the number of elements between them is i - last_one_idx - 1.
                # If this count is less than k, the condition is violated.
                if i - last_one_idx - 1 < k:
                    return False
                # Update the index of the last seen '1'.
                last_one_idx = i
                
        # If the loop completes, it means all '1's satisfied the distance requirement.
        return True
```

  </div>

  <div class="tab-panel" data-lang="java">

```java
class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        // Initialize lastOneIdx. A value like -k - 1 ensures that the
        // first '1' encountered in the array will always satisfy the
        // distance condition, as (firstIdx - (-k - 1) - 1) = firstIdx + k >= k.
        int lastOneIdx = -k - 1;
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                // Calculate the number of zeros between the current '1' and the last '1'.
                // If the current '1' is at index 'i' and the previous '1' was at 'lastOneIdx',
                // the number of elements between them is i - lastOneIdx - 1.
                // If this count is less than k, the condition is violated.
                if (i - lastOneIdx - 1 < k) {
                    return false;
                }
                // Update the index of the last seen '1'.
                lastOneIdx = i;
            }
        }
        
        // If the loop completes, it means all '1's satisfied the distance requirement.
        return true;
    }
}
```

  </div>

  <div class="tab-panel" data-lang="cpp">

```cpp
#include <vector>

class Solution {
public:
    bool kLengthApart(std::vector<int>& nums, int k) {
        // Initialize lastOneIdx. A value like -k - 1 ensures that the
        // first '1' encountered in the array will always satisfy the
        // distance condition, as (first_idx - (-k - 1) - 1) = first_idx + k >= k.
        int lastOneIdx = -k - 1;
        
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 1) {
                // Calculate the number of zeros between the current '1' and the last '1'.
                // If the current '1' is at index 'i' and the previous '1' was at 'lastOneIdx',
                // the number of elements between them is i - lastOneIdx - 1.
                // If this count is less than k, the condition is violated.
                if (i - lastOneIdx - 1 < k) {
                    return false;
                }
                // Update the index of the last seen '1'.
                lastOneIdx = i;
            }
        }
        
        // If the loop completes, it means all '1's satisfied the distance requirement.
        return true;
    }
};
```

  </div>

  <div class="tab-panel" data-lang="javascript">

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var kLengthApart = function(nums, k) {
    // Initialize lastOneIdx. A value like -k - 1 ensures that the
    // first '1' encountered in the array will always satisfy the
    // distance condition, as (firstIdx - (-k - 1) - 1) = firstIdx + k >= k.
    let lastOneIdx = -k - 1;
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            // Calculate the number of zeros between the current '1' and the last '1'.
            // If the current '1' is at index 'i' and the previous '1' was at 'lastOneIdx',
            // the number of elements between them is i - lastOneIdx - 1.
            // If this count is less than k, the condition is violated.
            if (i - lastOneIdx - 1 < k) {
                return false;
            }
            // Update the index of the last seen '1'.
            lastOneIdx = i;
        }
    }
    
    // If the loop completes, it means all '1's satisfied the distance requirement.
    return true;
};
```

  </div>

  <div class="tab-panel" data-lang="typescript">

```typescript
function kLengthApart(nums: number[], k: number): boolean {
    // Initialize lastOneIdx. A value like -k - 1 ensures that the
    // first '1' encountered in the array will always satisfy the
    // distance condition, as (firstIdx - (-k - 1) - 1) = firstIdx + k >= k.
    let lastOneIdx: number = -k - 1;
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            // Calculate the number of zeros between the current '1' and the last '1'.
            // If the current '1' is at index 'i' and the previous '1' was at 'lastOneIdx',
            // the number of elements between them is i - lastOneIdx - 1.
            // If this count is less than k, the condition is violated.
            if (i - lastOneIdx - 1 < k) {
                return false;
            }
            // Update the index of the last seen '1'.
            lastOneIdx = i;
        }
    }
    
    // If the loop completes, it means all '1's satisfied the distance requirement.
    return true;
}
```

  </div>

  <div class="tab-panel" data-lang="go">

```go
func kLengthApart(nums []int, k int) bool {
    // Initialize lastOneIdx. A value like -k - 1 ensures that the
    // first '1' encountered in the array will always satisfy the
    // distance condition, as (firstIdx - (-k - 1) - 1) = firstIdx + k >= k.
    lastOneIdx := -k - 1
    
    for i := 0; i < len(nums); i++ {
        if nums[i] == 1 {
            // Calculate the number of zeros between the current '1' and the last '1'.
            // If the current '1' is at index 'i' and the previous '1' was at 'lastOneIdx',
            // the number of elements between them is i - lastOneIdx - 1.
            // If this count is less than k, the condition is violated.
            if i - lastOneIdx - 1 < k {
                return false
            }
            // Update the index of the last seen '1'.
            lastOneIdx = i
        }
    }
    
    // If the loop completes, it means all '1's satisfied the distance requirement.
    return true
}
```

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)
