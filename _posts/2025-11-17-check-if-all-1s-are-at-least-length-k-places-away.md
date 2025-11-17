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

The problem asks us to determine if all '1's in a binary array `nums` are separated by at least `k` '0's. This means that for any two consecutive '1's, the count of '0's between them must be greater than or equal to `k`.

We can solve this by iterating through the array once. We need to keep track of the index of the previously encountered '1'. Let's call this `last_one_idx`.

1.  Initialize `last_one_idx`. A good sentinel value is `-k - 1`. This choice simplifies the logic because when we encounter the very first '1' at index `i`, the calculated distance `i - last_one_idx - 1` will be `i - (-k - 1) - 1 = i + k`. Since `i >= 0`, this distance `i + k` will always be `>= k`. Therefore, the first '1' will never trigger a `false` condition, and we don't need a special check for the first '1' being the `last_one_idx`.

2.  Iterate through `nums` from index `i = 0` to `nums.length - 1`:
    a.  If `nums[i]` is `1`:
        i.  Calculate the number of '0's between the current '1' (at index `i`) and the previous '1' (at `last_one_idx`). This count is `i - last_one_idx - 1`.
        ii. If this count is less than `k` (i.e., `i - last_one_idx - 1 < k`), it means the '1's are not `k` places apart. In this case, we immediately return `false`.
        iii. Update `last_one_idx` to the current index `i`.

3.  If the loop completes without returning `false`, it means all pairs of '1's are at least `k` places apart. So, return `true`.

This approach ensures that every time a '1' is found, its distance from the preceding '1' is checked against `k`. If any pair violates the condition, we stop and return `false`. If all pairs satisfy it, we return `true`.

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
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # Initialize last_one_idx. Using -k-1 allows us to avoid a special check for the first '1'.
        # For the first '1' at index 'i', the distance i - (-k-1) - 1 = i + k, which is always >= k.
        last_one_idx = -k - 1
        
        for i, num in enumerate(nums):
            if num == 1:
                # Calculate the number of zeros between the current '1' and the last '1'.
                # This is (current_index - last_one_index) - 1.
                if i - last_one_idx - 1 < k:
                    return False
                last_one_idx = i
                
        return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        // Initialize lastOneIdx. Using -k-1 allows us to avoid a special check for the first '1'.
        // For the first '1' at index 'i', the distance i - (-k-1) - 1 = i + k, which is always >= k.
        int lastOneIdx = -k - 1;
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                // Calculate the number of zeros between the current '1' and the last '1'.
                // This is (current_index - last_one_index) - 1.
                if (i - lastOneIdx - 1 < k) {
                    return false;
                }
                lastOneIdx = i;
            }
        }
        
        return true;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
#include <vector> // Required for std::vector

class Solution {
public:
    bool kLengthApart(std::vector<int>& nums, int k) {
        // Initialize lastOneIdx. Using -k-1 allows us to avoid a special check for the first '1'.
        // For the first '1' at index 'i', the distance i - (-k-1) - 1 = i + k, which is always >= k.
        int lastOneIdx = -k - 1;
        
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 1) {
                // Calculate the number of zeros between the current '1' and the last '1'.
                // This is (current_index - last_one_index) - 1.
                if (i - lastOneIdx - 1 < k) {
                    return false;
                }
                lastOneIdx = i;
            }
        }
        
        return true;
    }
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var kLengthApart = function(nums, k) {
    // Initialize lastOneIdx. Using -k-1 allows us to avoid a special check for the first '1'.
    // For the first '1' at index 'i', the distance i - (-k-1) - 1 = i + k, which is always >= k.
    let lastOneIdx = -k - 1;
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            // Calculate the number of zeros between the current '1' and the last '1'.
            // This is (current_index - last_one_index) - 1.
            if (i - lastOneIdx - 1 < k) {
                return false;
            }
            lastOneIdx = i;
        }
    }
    
    return true;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function kLengthApart(nums: number[], k: number): boolean {
    // Initialize lastOneIdx. Using -k-1 allows us to avoid a special check for the first '1'.
    // For the first '1' at index 'i', the distance i - (-k-1) - 1 = i + k, which is always >= k.
    let lastOneIdx: number = -k - 1;
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            // Calculate the number of zeros between the current '1' and the last '1'.
            // This is (current_index - last_one_index) - 1.
            if (i - lastOneIdx - 1 < k) {
                return false;
            }
            lastOneIdx = i;
        }
    }
    
    return true;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

func kLengthApart(nums []int, k int) bool {
    // Initialize lastOneIdx. Using -k-1 allows us to avoid a special check for the first '1'.
    // For the first '1' at index 'i', the distance i - (-k-1) - 1 = i + k, which is always >= k.
    lastOneIdx := -k - 1
    
    for i, num := range nums {
        if num == 1 {
            // Calculate the number of zeros between the current '1' and the last '1'.
            // This is (current_index - last_one_index) - 1.
            if i - lastOneIdx - 1 < k {
                return false
            }
            lastOneIdx = i
        }
    }
    
    return true
}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N), where N is the length of the `nums` array. We iterate through the array exactly once, performing constant time operations (comparisons, arithmetic, assignments) for each element. Therefore, the time complexity is directly proportional to the size of the input array.
- **Space Complexity:** O(1). We use a fixed number of variables (`last_one_idx`, loop counter `i`, and current element `num`) regardless of the input array's size. No additional data structures are allocated that scale with the input.
