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

The problem asks us to determine if all '1's in a binary array `nums` are separated by at least `k` zeros. We can solve this by iterating through the array and keeping track of the index of the most recently encountered '1'.

1.  Initialize a variable `last_one_index` to a sentinel value (e.g., -1) to indicate that no '1' has been found yet.
2.  Iterate through the `nums` array from left to right, using an index `i`.
3.  If the current element `nums[i]` is a '1':
    a.  Check if `last_one_index` is not its sentinel value (meaning this is not the first '1' we've encountered).
    b.  If it's not the first '1', calculate the number of zeros between the current '1' and the `last_one_index`. This distance is `i - last_one_index - 1`. (e.g., if '1' is at index 0 and next '1' is at index 3, `3 - 0 - 1 = 2` zeros in between).
    c.  If this calculated distance is less than `k`, it means the condition is violated, so we immediately return `false`.
    d.  After checking (or if it's the first '1'), update `last_one_index` to the current index `i`.
4.  If the loop completes without returning `false`, it means all pairs of '1's satisfy the `k` distance requirement, so we return `true`.

This approach handles edge cases such as an array with no '1's, only one '1', or `k=0` correctly. For `k=0`, any distance is valid (including zero zeros between ones), and `i - last_one_index - 1 < 0` will never be true because `i - last_one_index - 1` will always be at least 0 if there are two distinct '1's.

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
        last_one_index = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if last_one_index != -1:
                    # Found a subsequent '1'
                    # Calculate the number of zeros between the current '1' and the last '1'
                    # Distance is (current_index - last_one_index) - 1
                    if i - last_one_index - 1 < k:
                        return False
                last_one_index = i
        return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        int lastOneIndex = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                if (lastOneIndex != -1) {
                    // Found a subsequent '1'
                    // Calculate the number of zeros between the current '1' and the last '1'
                    // Distance is (current_index - last_one_index) - 1
                    if (i - lastOneIndex - 1 < k) {
                        return false;
                    }
                }
                lastOneIndex = i;
            }
        }
        return true;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
#include <vector>

class Solution {
public:
    bool kLengthApart(std::vector<int>& nums, int k) {
        int lastOneIndex = -1;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 1) {
                if (lastOneIndex != -1) {
                    // Found a subsequent '1'
                    // Calculate the number of zeros between the current '1' and the last '1'
                    // Distance is (current_index - last_one_index) - 1
                    if (i - lastOneIndex - 1 < k) {
                        return false;
                    }
                }
                lastOneIndex = i;
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
    let lastOneIndex = -1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            if (lastOneIndex !== -1) {
                // Found a subsequent '1'
                // Calculate the number of zeros between the current '1' and the last '1'
                // Distance is (current_index - last_one_index) - 1
                if (i - lastOneIndex - 1 < k) {
                    return false;
                }
            }
            lastOneIndex = i;
        }
    }
    return true;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function kLengthApart(nums: number[], k: number): boolean {
    let lastOneIndex: number = -1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            if (lastOneIndex !== -1) {
                // Found a subsequent '1'
                // Calculate the number of zeros between the current '1' and the last '1'
                // Distance is (current_index - last_one_index) - 1
                if (i - lastOneIndex - 1 < k) {
                    return false;
                }
            }
            lastOneIndex = i;
        }
    }
    return true;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
func kLengthApart(nums []int, k int) bool {
    lastOneIndex := -1
    for i := 0; i < len(nums); i++ {
        if nums[i] == 1 {
            if lastOneIndex != -1 {
                // Found a subsequent '1'
                // Calculate the number of zeros between the current '1' and the last '1'
                // Distance is (current_index - last_one_index) - 1
                if i - lastOneIndex - 1 < k {
                    return false
                }
            }
            lastOneIndex = i
        }
    }
    return true
}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)
