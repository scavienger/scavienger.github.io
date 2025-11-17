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

## ✨ AI-Generated Solution (gemini-2.5-flash)

### Approach

The problem asks us to verify if every pair of '1's in a given binary array `nums` is separated by at least `k` '0's. We can solve this by iterating through the array once and keeping track of the index of the last encountered '1'.

1.  Initialize a variable, let's call it `last_one_index`, to `-1`. This sentinel value indicates that no '1' has been encountered yet.
2.  Iterate through the `nums` array with an index `i` from `0` to `nums.length - 1`.
3.  If `nums[i]` is `1`:
    a.  Check if `last_one_index` is not `-1`. This means we have encountered at least one '1' before the current one.
    b.  If it's not the first '1', calculate the number of '0's between the current '1' and the `last_one_index`. This distance is `i - last_one_index - 1`.
    c.  If this calculated distance is less than `k`, it means the condition is violated, so we immediately return `false`.
    d.  After the check (or if it was the first '1'), update `last_one_index` to the current index `i`.
4.  If the loop completes without returning `false`, it means all '1's are sufficiently far apart, so we return `true`.

Edge Cases:
*   If there are no '1's in the array, `last_one_index` will remain `-1` throughout the loop. No checks will be performed, and the function will correctly return `true`.
*   If there is only one '1', `last_one_index` will be updated once, but the condition `last_one_index != -1` will only be met when there's a *second* '1'. Thus, no checks will be performed, and the function will correctly return `true`.

### Code

<div class="code-tabs">
  <input type="radio" name="code-lang" id="lang-cpp" checked>
  <input type="radio" name="code-lang" id="lang-java">
  <input type="radio" name="code-lang" id="lang-python">
  <input type="radio" name="code-lang" id="lang-python3">
  <input type="radio" name="code-lang" id="lang-c">
  <input type="radio" name="code-lang" id="lang-csharp">
  <input type="radio" name="code-lang" id="lang-javascript">
  <input type="radio" name="code-lang" id="lang-typescript">
  <input type="radio" name="code-lang" id="lang-php">
  <input type="radio" name="code-lang" id="lang-swift">
  <input type="radio" name="code-lang" id="lang-kotlin">
  <input type="radio" name="code-lang" id="lang-dart">
  <input type="radio" name="code-lang" id="lang-go">
  <input type="radio" name="code-lang" id="lang-ruby">
  <input type="radio" name="code-lang" id="lang-scala">
  <input type="radio" name="code-lang" id="lang-rust">
  <input type="radio" name="code-lang" id="lang-racket">
  <input type="radio" name="code-lang" id="lang-erlang">
  <input type="radio" name="code-lang" id="lang-elixir">
  <div class="tab-labels">
    <label for="lang-cpp">C++</label>
    <label for="lang-java">Java</label>
    <label for="lang-python">Python</label>
    <label for="lang-python3">Python3</label>
    <label for="lang-c">C</label>
    <label for="lang-csharp">C#</label>
    <label for="lang-javascript">JavaScript</label>
    <label for="lang-typescript">TypeScript</label>
    <label for="lang-php">PHP</label>
    <label for="lang-swift">Swift</label>
    <label for="lang-kotlin">Kotlin</label>
    <label for="lang-dart">Dart</label>
    <label for="lang-go">Go</label>
    <label for="lang-ruby">Ruby</label>
    <label for="lang-scala">Scala</label>
    <label for="lang-rust">Rust</label>
    <label for="lang-racket">Racket</label>
    <label for="lang-erlang">Erlang</label>
    <label for="lang-elixir">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
class Solution {
public:
    bool kLengthApart(std::vector<int>& nums, int k) {
        int lastOneIndex = -1;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 1) {
                if (lastOneIndex != -1) {
                    // Calculate the number of zeros between the current '1' and the last '1'
                    // i is current index, lastOneIndex is previous '1' index.
                    // Distance in elements is i - lastOneIndex.
                    // Number of zeros is (i - lastOneIndex) - 1.
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

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        int lastOneIndex = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                if (lastOneIndex != -1) {
                    // Calculate the number of zeros between the current '1' and the last '1'
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

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one_index = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if last_one_index != -1:
                    # Calculate the number of zeros between the current '1' and the last '1'
                    if i - last_one_index - 1 < k:
                        return False
                last_one_index = i
        return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one_index = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if last_one_index != -1:
                    # Calculate the number of zeros between the current '1' and the last '1'
                    if i - last_one_index - 1 < k:
                        return False
                last_one_index = i
        return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdbool.h>
#include <stddef.h> // For size_t

bool kLengthApart(int* nums, int numsSize, int k) {
    int lastOneIndex = -1;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 1) {
            if (lastOneIndex != -1) {
                // Calculate the number of zeros between the current '1' and the last '1'
                if (i - lastOneIndex - 1 < k) {
                    return false;
                }
            }
            lastOneIndex = i;
        }
    }
    return true;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
using System;
using System.Collections.Generic;

public class Solution {
    public bool KLengthApart(int[] nums, int k) {
        int lastOneIndex = -1;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 1) {
                if (lastOneIndex != -1) {
                    // Calculate the number of zeros between the current '1' and the last '1'
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
                // Calculate the number of zeros between the current '1' and the last '1'
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
                // Calculate the number of zeros between the current '1' and the last '1'
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

  <div class="tab-panel" data-lang="php">

{% highlight php %}
<?php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function kLengthApart($nums, $k) {
        $lastOneIndex = -1;
        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] === 1) {
                if ($lastOneIndex !== -1) {
                    // Calculate the number of zeros between the current '1' and the last '1'
                    if ($i - $lastOneIndex - 1 < $k) {
                        return false;
                    }
                }
                $lastOneIndex = $i;
            }
        }
        return true;
    }
}
?>
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution {
    func kLengthApart(_ nums: [Int], _ k: Int) -> Bool {
        var lastOneIndex: Int = -1
        for i in 0..<nums.count {
            if nums[i] == 1 {
                if lastOneIndex != -1 {
                    // Calculate the number of zeros between the current '1' and the last '1'
                    if i - lastOneIndex - 1 < k {
                        return false
                    }
                }
                lastOneIndex = i
            }
        }
        return true
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution {
    fun kLengthApart(nums: IntArray, k: Int): Boolean {
        var lastOneIndex: Int = -1
        for (i in nums.indices) {
            if (nums[i] == 1) {
                if (lastOneIndex != -1) {
                    // Calculate the number of zeros between the current '1' and the last '1'
                    if (i - lastOneIndex - 1 < k) {
                        return false
                    }
                }
                lastOneIndex = i
            }
        }
        return true
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
class Solution {
    bool kLengthApart(List<int> nums, int k) {
        int lastOneIndex = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                if (lastOneIndex != -1) {
                    // Calculate the number of zeros between the current '1' and the last '1'
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

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

func kLengthApart(nums []int, k int) bool {
    lastOneIndex := -1
    for i := 0; i < len(nums); i++ {
        if nums[i] == 1 {
            if lastOneIndex != -1 {
                // Calculate the number of zeros between the current '1' and the last '1'
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

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def k_length_apart(nums, k)
    last_one_index = -1
    nums.each_with_index do |num, i|
        if num == 1
            if last_one_index != -1
                # Calculate the number of zeros between the current '1' and the last '1'
                if i - last_one_index - 1 < k
                    return false
                end
            end
            last_one_index = i
        end
    end
    true
end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {
    def kLengthApart(nums: Array[Int], k: Int): Boolean = {
        var lastOneIndex: Int = -1
        for (i <- nums.indices) {
            if (nums(i) == 1) {
                if (lastOneIndex != -1) {
                    // Calculate the number of zeros between the current '1' and the last '1'
                    if (i - lastOneIndex - 1 < k) {
                        return false
                    }
                }
                lastOneIndex = i
            }
        }
        true
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution {
    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
        let mut last_one_index: i32 = -1;
        for (i, &num) in nums.iter().enumerate() {
            if num == 1 {
                if last_one_index != -1 {
                    // Calculate the number of zeros between the current '1' and the last '1'
                    if (i as i32) - last_one_index - 1 < k {
                        return false;
                    }
                }
                last_one_index = i as i32;
            }
        }
        true
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket

(define (kLengthApart nums k)
  (let loop ((current-nums nums)
             (dist -1)) ; Tracks distance (number of zeros) from last 1. -1 means no 1 seen yet.
    (cond
      ((empty? current-nums) #t) ; Reached end of list, all checks passed
      ((= (car current-nums) 1)
       (if (and (not (= dist -1)) ; If it's not the very first '1'
                (< dist k))      ; And the calculated distance (number of zeros) is too small
           #f                    ; Then it's a violation, return false
           (loop (cdr current-nums) 0))) ; Else, reset distance for next '1' to 0
      (else ; Current element is 0
       (loop (cdr current-nums)
             (if (= dist -1)
                 -1              ; Still haven't seen the first '1', maintain -1 state
                 (+ dist 1))))))) ; Increment distance if a '1' has been seen previously
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
-export([kLengthApart/2]).

kLengthApart(Nums, K) ->
    % ZerosCount: 
    % -1 if no '1' has been encountered yet.
    % 0 if the immediately previous element was a '1'.
    % N (N > 0) if N zeros have been encountered since the last '1'.
    kLengthApart_impl(Nums, K, -1).

kLengthApart_impl([], _K, _ZerosCount) ->
    true;
kLengthApart_impl([Num | Rest], K, ZerosCount) ->
    case Num of
        1 ->
            case ZerosCount of
                -1 -> % First '1' encountered, reset count for future zeros
                    kLengthApart_impl(Rest, K, 0);
                _ when ZerosCount < K -> % Subsequent '1', but distance (zeros_count) is too small
                    false;
                _ -> % Subsequent '1', distance is sufficient
                    kLengthApart_impl(Rest, K, 0) % Reset count for future zeros
            end;
        0 ->
            case ZerosCount of
                -1 -> % Still no '1' encountered, keep -1 state
                    kLengthApart_impl(Rest, K, -1);
                _ -> % '1' has been encountered, increment zero count
                    kLengthApart_impl(Rest, K, ZerosCount + 1)
            end
    end.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
  @spec k_length_apart(nums :: [integer], k :: integer) :: boolean
  def k_length_apart(nums, k) do
    # ZerosCount:
    # -1 if no '1' has been encountered yet.
    # 0 if the immediately previous element was a '1'.
    # N (N > 0) if N zeros have been encountered since the last '1'.
    k_length_apart_impl(nums, k, -1)
  end

  defp k_length_apart_impl([], _k, _zeros_count), do: true
  defp k_length_apart_impl([num | rest], k, zeros_count) do
    case num do
      1 ->
        case zeros_count do
          -1 -> # First '1' encountered, reset count for future zeros
            k_length_apart_impl(rest, k, 0)
          _ when zeros_count < k -> # Subsequent '1', but distance (zeros_count) is too small
            false
          _ -> # Subsequent '1', distance is sufficient
            k_length_apart_impl(rest, k, 0) # Reset count for future zeros
        end
      0 ->
        case zeros_count do
          -1 -> # Still no '1' encountered, keep -1 state
            k_length_apart_impl(rest, k, -1)
          _ -> # '1' has been encountered, increment zero count
            k_length_apart_impl(rest, k, zeros_count + 1)
        end
    end
  end
end
{% endhighlight %}

  </div>

</div>


### Complexity Analysis

- **Time Complexity:** O(N)

- **Space Complexity:** O(1)
