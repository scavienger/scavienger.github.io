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

The problem asks us to determine if all '1's in a binary array `nums` are separated by at least `k` '0's. We can solve this by iterating through the array and keeping track of the index of the last encountered '1'.

1.  Initialize a variable, say `last_one_idx`, to -1. This value signifies that we haven't encountered any '1' yet.
2.  Iterate through the `nums` array from the beginning to the end, using an index `i`.
3.  When we encounter a `1` at the current index `i`:
    a.  Check if `last_one_idx` is not -1. If it's not -1, it means we have seen a '1' before. In this case, calculate the distance between the current '1' and the previous '1'. The number of elements *strictly between* the two '1's (which must all be '0's) is `(i - last_one_idx - 1)`. 
    b.  If this calculated distance `(i - last_one_idx - 1)` is less than `k`, it violates the condition. Therefore, we immediately return `false`.
    c.  After checking the distance (or if `last_one_idx` was -1, meaning this is the first '1'), update `last_one_idx` to the current index `i`.
4.  If the loop completes without returning `false`, it means all pairs of '1's satisfy the `k` distance requirement. In this case, return `true`.

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
import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one_idx = -1
        for i, num in enumerate(nums):
            if num == 1:
                if last_one_idx != -1:
                    # Calculate distance: current index - last_one_idx - 1
                    # This gives the number of zeros strictly between the two 1s.
                    if (i - last_one_idx - 1) < k:
                        return False
                last_one_idx = i
        return True
```

  </div>

  <div class="tab-panel" data-lang="java">

```java
class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        int lastOneIdx = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                if (lastOneIdx != -1) {
                    // Calculate distance: current index - last_one_idx - 1
                    // This gives the number of zeros strictly between the two 1s.
                    if ((i - lastOneIdx - 1) < k) {
                        return false;
                    }
                }
                lastOneIdx = i;
            }
        }
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
        int lastOneIdx = -1;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 1) {
                if (lastOneIdx != -1) {
                    // Calculate distance: current index - last_one_idx - 1
                    // This gives the number of zeros strictly between the two 1s.
                    if ((i - lastOneIdx - 1) < k) {
                        return false;
                    }
                }
                lastOneIdx = i;
            }
        }
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
    let lastOneIdx = -1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            if (lastOneIdx !== -1) {
                // Calculate distance: current index - last_one_idx - 1
                // This gives the number of zeros strictly between the two 1s.
                if ((i - lastOneIdx - 1) < k) {
                    return false;
                }
            }
            lastOneIdx = i;
        }
    }
    return true;
};
```

  </div>

  <div class="tab-panel" data-lang="typescript">

```typescript
function kLengthApart(nums: number[], k: number): boolean {
    let lastOneIdx: number = -1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            if (lastOneIdx !== -1) {
                // Calculate distance: current index - last_one_idx - 1
                // This gives the number of zeros strictly between the two 1s.
                if ((i - lastOneIdx - 1) < k) {
                    return false;
                }
            }
            lastOneIdx = i;
        }
    }
    return true;
}
```

  </div>

  <div class="tab-panel" data-lang="go">

```go
package main

func kLengthApart(nums []int, k int) bool {
    lastOneIdx := -1
    for i, num := range nums {
        if num == 1 {
            if lastOneIdx != -1 {
                // Calculate distance: current index - last_one_idx - 1
                // This gives the number of zeros strictly between the two 1s.
                if (i - lastOneIdx - 1) < k {
                    return false
                }
            }
            lastOneIdx = i
        }
    }
    return true
}
```

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)
