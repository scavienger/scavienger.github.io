---
layout: post
title: "Check If All 1's Are at Least Length K Places Away"
date: 2025-11-02 09:00:00 +0900
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

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details open>
<summary><strong>✨ Solution from gemini-2.5-flash</strong></summary>

### Approach

The problem requires us to check if every pair of '1's in a binary array `nums` is separated by at least `k` '0's. This means that if we find a '1' at index `i` and the next '1' is at index `j`, then the number of elements between them (`j - i - 1`) must be greater than or equal to `k`. If this condition is violated for any pair of '1's, we should return `false`.

We can solve this by iterating through the `nums` array once. We'll maintain a variable, let's call it `last_one_idx`, which stores the index of the most recently encountered '1'. Initially, `last_one_idx` can be set to a value indicating that no '1' has been found yet (e.g., -1).

As we iterate through the array from left to right:
1.  If we encounter a '0', we simply continue to the next element, as '0's do not affect the `last_one_idx` directly.
2.  If we encounter a '1' at the current index `i`:
    a.  If `last_one_idx` is not its initial 'no-one-found' value (i.e., `last_one_idx != -1`), it means we've encountered at least one '1' before. We then calculate the number of '0's between the current '1' and the `last_one_idx`. This count is `i - last_one_idx - 1`.
    b.  We check if this calculated distance (`i - last_one_idx - 1`) is less than `k`. If it is, the condition is violated, and we immediately return `false`.
    c.  Regardless of the distance check (or if it's the very first '1' encountered), we update `last_one_idx = i` to mark the current '1' as the most recently found '1'.

If we successfully iterate through the entire array without finding any violations (i.e., without returning `false`), it means all '1's satisfy the condition, so we return `true`.

### Code

<div class="code-tabs">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-cpp-gemini-2-5-flash" checked>
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-java-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python3-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-c-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-csharp-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-javascript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-typescript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-php-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-swift-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-kotlin-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-dart-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-go-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-ruby-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-scala-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-rust-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-racket-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-erlang-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-elixir-gemini-2-5-flash">
  <div class="tab-labels">
    <label for="lang-cpp-gemini-2-5-flash">C++</label>
    <label for="lang-java-gemini-2-5-flash">Java</label>
    <label for="lang-python-gemini-2-5-flash">Python</label>
    <label for="lang-python3-gemini-2-5-flash">Python3</label>
    <label for="lang-c-gemini-2-5-flash">C</label>
    <label for="lang-csharp-gemini-2-5-flash">C#</label>
    <label for="lang-javascript-gemini-2-5-flash">JavaScript</label>
    <label for="lang-typescript-gemini-2-5-flash">TypeScript</label>
    <label for="lang-php-gemini-2-5-flash">PHP</label>
    <label for="lang-swift-gemini-2-5-flash">Swift</label>
    <label for="lang-kotlin-gemini-2-5-flash">Kotlin</label>
    <label for="lang-dart-gemini-2-5-flash">Dart</label>
    <label for="lang-go-gemini-2-5-flash">Go</label>
    <label for="lang-ruby-gemini-2-5-flash">Ruby</label>
    <label for="lang-scala-gemini-2-5-flash">Scala</label>
    <label for="lang-rust-gemini-2-5-flash">Rust</label>
    <label for="lang-racket-gemini-2-5-flash">Racket</label>
    <label for="lang-erlang-gemini-2-5-flash">Erlang</label>
    <label for="lang-elixir-gemini-2-5-flash">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
class Solution {
public:
    bool kLengthApart(std::vector<int>& nums, int k) {
        int lastOneIdx = -1; // Initialize to -1 to signify no '1' found yet

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 1) {
                // If this is not the very first '1' encountered
                // and we've already found a previous '1' (lastOneIdx is not -1)
                if (lastOneIdx != -1) {
                    // Check if the number of zeros between current '1' and last '1' is less than k
                    if ((i - lastOneIdx - 1) < k) {
                        return false;
                    }
                }
                // Update the index of the last encountered '1'
                lastOneIdx = i;
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
        int lastOneIdx = -1; // Initialize to -1 to signify no '1' found yet

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                // If this is not the very first '1' encountered
                // and we've already found a previous '1' (lastOneIdx is not -1)
                if (lastOneIdx != -1) {
                    // Check if the number of zeros between current '1' and last '1' is less than k
                    if ((i - lastOneIdx - 1) < k) {
                        return false;
                    }
                }
                // Update the index of the last encountered '1'
                lastOneIdx = i;
            }
        }

        return true;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
import math
from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one_idx = -1 # Initialize to -1 to signify no '1' found yet

        for i, num in enumerate(nums):
            if num == 1:
                # If this is not the very first '1' encountered
                # and we've already found a previous '1' (last_one_idx is not -1)
                if last_one_idx != -1:
                    # Check if the number of zeros between current '1' and last '1' is less than k
                    if (i - last_one_idx - 1) < k:
                        return False
                # Update the index of the last encountered '1'
                last_one_idx = i

        return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
import math
from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one_idx = -1 # Initialize to -1 to signify no '1' found yet

        for i, num in enumerate(nums):
            if num == 1:
                # If this is not the very first '1' encountered
                # and we've already found a previous '1' (last_one_idx is not -1)
                if last_one_idx != -1:
                    # Check if the number of zeros between current '1' and last '1' is less than k
                    if (i - last_one_idx - 1) < k:
                        return False
                # Update the index of the last encountered '1'
                last_one_idx = i

        return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdbool.h>
#include <stddef.h> // For size_t

bool kLengthApart(int* nums, int numsSize, int k) {
    int lastOneIdx = -1; // Initialize to -1 to signify no '1' found yet

    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 1) {
            // If this is not the very first '1' encountered
            // and we've already found a previous '1' (lastOneIdx is not -1)
            if (lastOneIdx != -1) {
                // Check if the number of zeros between current '1' and last '1' is less than k
                if ((i - lastOneIdx - 1) < k) {
                    return false;
                }
            }
            // Update the index of the last encountered '1'
            lastOneIdx = i;
        }
    }

    return true;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
using System;

public class Solution {
    public bool KLengthApart(int[] nums, int k) {
        int lastOneIdx = -1; // Initialize to -1 to signify no '1' found yet

        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 1) {
                // If this is not the very first '1' encountered
                // and we've already found a previous '1' (lastOneIdx is not -1)
                if (lastOneIdx != -1) {
                    // Check if the number of zeros between current '1' and last '1' is less than k
                    if ((i - lastOneIdx - 1) < k) {
                        return false;
                    }
                }
                // Update the index of the last encountered '1'
                lastOneIdx = i;
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
    let lastOneIdx = -1; // Initialize to -1 to signify no '1' found yet

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            // If this is not the very first '1' encountered
            // and we've already found a previous '1' (lastOneIdx is not -1)
            if (lastOneIdx !== -1) {
                // Check if the number of zeros between current '1' and last '1' is less than k
                if ((i - lastOneIdx - 1) < k) {
                    return false;
                }
            }
            // Update the index of the last encountered '1'
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
    let lastOneIdx: number = -1; // Initialize to -1 to signify no '1' found yet

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            // If this is not the very first '1' encountered
            // and we've already found a previous '1' (lastOneIdx is not -1)
            if (lastOneIdx !== -1) {
                // Check if the number of zeros between current '1' and last '1' is less than k
                if ((i - lastOneIdx - 1) < k) {
                    return false;
                }
            }
            // Update the index of the last encountered '1'
            lastOneIdx = i;
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
        $lastOneIdx = -1; // Initialize to -1 to signify no '1' found yet

        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] === 1) {
                // If this is not the very first '1' encountered
                // and we've already found a previous '1' ($lastOneIdx is not -1)
                if ($lastOneIdx !== -1) {
                    // Check if the number of zeros between current '1' and last '1' is less than k
                    if (($i - $lastOneIdx - 1) < $k) {
                        return false;
                    }
                }
                // Update the index of the last encountered '1'
                $lastOneIdx = $i;
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
        var lastOneIdx: Int = -1 // Initialize to -1 to signify no '1' found yet

        for (i, num) in nums.enumerated() {
            if num == 1 {
                // If this is not the very first '1' encountered
                // and we've already found a previous '1' (lastOneIdx is not -1)
                if lastOneIdx != -1 {
                    // Check if the number of zeros between current '1' and last '1' is less than k
                    if (i - lastOneIdx - 1) < k {
                        return false
                    }
                }
                // Update the index of the last encountered '1'
                lastOneIdx = i
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
        var lastOneIdx: Int = -1 // Initialize to -1 to signify no '1' found yet

        for (i in nums.indices) {
            if (nums[i] == 1) {
                // If this is not the very first '1' encountered
                // and we've already found a previous '1' (lastOneIdx is not -1)
                if (lastOneIdx != -1) {
                    // Check if the number of zeros between current '1' and last '1' is less than k
                    if ((i - lastOneIdx - 1) < k) {
                        return false
                    }
                }
                // Update the index of the last encountered '1'
                lastOneIdx = i
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
    int lastOneIdx = -1; // Initialize to -1 to signify no '1' found yet

    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == 1) {
        // If this is not the very first '1' encountered
        // and we've already found a previous '1' (lastOneIdx is not -1)
        if (lastOneIdx != -1) {
          // Check if the number of zeros between current '1' and last '1' is less than k
          if ((i - lastOneIdx - 1) < k) {
            return false;
          }
        }
        // Update the index of the last encountered '1'
        lastOneIdx = i;
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
    lastOneIdx := -1 // Initialize to -1 to signify no '1' found yet

    for i, num := range nums {
        if num == 1 {
            // If this is not the very first '1' encountered
            // and we've already found a previous '1' (lastOneIdx is not -1)
            if lastOneIdx != -1 { 
                // Check if the number of zeros between current '1' and last '1' is less than k
                if (i - lastOneIdx - 1) < k {
                    return false
                }
            }
            // Update the index of the last encountered '1'
            lastOneIdx = i
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
    last_one_idx = -1 # Initialize to -1 to signify no '1' found yet

    nums.each_with_index do |num, i|
        if num == 1
            # If this is not the very first '1' encountered
            # and we've already found a previous '1' (last_one_idx is not -1)
            if last_one_idx != -1
                # Check if the number of zeros between current '1' and last '1' is less than k
                if (i - last_one_idx - 1) < k
                    return false
                end
            end
            # Update the index of the last encountered '1'
            last_one_idx = i
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
        var lastOneIdx: Int = -1 // Initialize to -1 to signify no '1' found yet

        for (i <- nums.indices) {
            if (nums(i) == 1) {
                // If this is not the very first '1' encountered
                // and we've already found a previous '1' (lastOneIdx is not -1)
                if (lastOneIdx != -1) {
                    // Check if the number of zeros between current '1' and last '1' is less than k
                    if ((i - lastOneIdx - 1) < k) {
                        return false
                    }
                }
                // Update the index of the last encountered '1'
                lastOneIdx = i
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
        let mut last_one_idx: i32 = -1; // Initialize to -1 to signify no '1' found yet

        for (i, &num) in nums.iter().enumerate() {
            if num == 1 {
                // If this is not the very first '1' encountered
                // and we've already found a previous '1' (last_one_idx is not -1)
                if last_one_idx != -1 {
                    // Check if the number of zeros between current '1' and last '1' is less than k
                    // Convert i to i32 for arithmetic consistency
                    if ((i as i32) - last_one_idx - 1) < k {
                        return false;
                    }
                }
                // Update the index of the last encountered '1'
                last_one_idx = i as i32;
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

(define (k-length-apart nums k)
  ;; Helper function to process each element and update state
  ;; State is a list: (ok? last-one-idx)
  ;; ok?: boolean, true if all conditions met so far
  ;; last-one-idx: integer, index of the last '1' found, -1 if no '1' found yet
  (define (process-element acc current-idx num)
    (match acc
      ;; If already failed, propagate the failure state
      [(list #f _) (list #f -1)]

      ;; If still OK, process the current number
      [(list #t last-one-idx)
       (if (= num 1)
           (if (= last-one-idx -1)
               ;; First '1' found, update last-one-idx
               (list #t current-idx)
               ;; Subsequent '1' found, check distance
               (let ([zeros-between (- current-idx last-one-idx 1)])
                 (if (< zeros-between k)
                     ;; Condition violated
                     (list #f -1)
                     ;; Condition met, update last-one-idx
                     (list #t current-idx))))
           ;; Current num is '0', no change to state
           (list #t last-one-idx))]))) 

  ;; Use for/fold to iterate and carry state
  (let ([final-state (for/fold ([acc (list #t -1)]) ; Initial accumulator: (true, no_one_found_yet)
                               ((num (in-list nums))
                                (current-idx (in-naturals))) ; Generate indices 0, 1, ...
                       (process-element acc current-idx num))])
    ;; The result is the boolean part of the final state
    (car final-state)))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
-export([k_length_apart/2]).

k_length_apart(Nums, K) ->
    %% Start recursive process with initial state:
    %% LastOneIdx = -1 (no '1' found yet)
    %% CurrentIdx = 0 (start from the first element)
    k_length_apart_recursive(Nums, K, -1, 0).

%% k_length_apart_recursive(RemainingNums, K, LastOneIdx, CurrentIdx)
%% RemainingNums: The rest of the list to process
%% K: The required minimum distance
%% LastOneIdx: Index of the previously found '1'
%% CurrentIdx: The current index being processed
k_length_apart_recursive([], _K, _LastOneIdx, _CurrentIdx) ->
    true; %% All '1's checked, all conditions met
k_length_apart_recursive([Num | Rest], K, LastOneIdx, CurrentIdx) ->
    if
        Num == 1 ->
            if
                LastOneIdx == -1 ->
                    %% This is the first '1' encountered, just update LastOneIdx
                    k_length_apart_recursive(Rest, K, CurrentIdx, CurrentIdx + 1);
                true ->
                    %% A subsequent '1' is found, check the distance to the last '1'
                    ZerosBetween = CurrentIdx - LastOneIdx - 1,
                    if
                        ZerosBetween < K ->
                            false; %% Condition violated, return false immediately
                        true ->
                            %% Condition met, continue and update LastOneIdx
                            k_length_apart_recursive(Rest, K, CurrentIdx, CurrentIdx + 1)
                    end
            end;
        true -> %% Num == 0
            %% Current number is '0', continue with existing state (LastOneIdx unchanged)
            k_length_apart_recursive(Rest, K, LastOneIdx, CurrentIdx + 1)
    end.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
  @spec k_length_apart(nums :: [integer], k :: integer) :: boolean
  def k_length_apart(nums, k) do
    # The state for Enum.reduce will be a tuple: {ok_so_far, last_one_idx}
    # ok_so_far: true if all conditions met up to the current element, false otherwise
    # last_one_idx: The index of the most recently found '1', or -1 if none found yet.
    initial_state = {true, -1}

    {final_ok, _} =
      Enum.reduce(Enum.with_index(nums), initial_state, fn
        # Case 1: Current element is '1' and it's the first '1' encountered
        {1, current_idx}, {true, -1} ->
          {true, current_idx}

        # Case 2: Current element is '1' and a previous '1' was found
        {1, current_idx}, {true, last_one_idx} ->
          # Calculate the number of zeros between the current '1' and the last '1'
          zeros_between = current_idx - last_one_idx - 1

          if zeros_between < k do
            # Condition violated, set ok_so_far to false and propagate failure
            {false, -1}
          else
            # Condition met, update last_one_idx for the next iteration
            {true, current_idx}
          end

        # Case 3: Current element is '0', or previous condition already failed (propagate failure)
        {_num, _idx}, {ok_so_far, last_one_idx} ->
          # If it's a '0', state remains unchanged. If already failed, propagate.
          {ok_so_far, last_one_idx}
      end)

    # The final result is the 'ok_so_far' boolean from the final state
    final_ok
  end
end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N), where `N` is the length of the `nums` array. We iterate through the array exactly once, performing constant-time operations for each element.

- **Space Complexity:** O(1) auxiliary space. We only use a few constant-space variables (like `last_one_idx` and a loop counter) regardless of the input size.

</details>


<details>
<summary><strong>⚡ Solution from llama-3.3-70b-versatile</strong></summary>

### Approach

The approach to solve this problem is to iterate over the given binary array and check the distance between each pair of 1's. If the distance between any two 1's is less than k, return false. Otherwise, return true.

### Code

<div class="code-tabs">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-cpp-llama-3-3-70b-versatile" checked>
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-java-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python3-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-c-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-csharp-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-javascript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-typescript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-php-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-swift-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-kotlin-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-dart-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-go-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-ruby-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-scala-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-rust-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-racket-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-erlang-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-elixir-llama-3-3-70b-versatile">
  <div class="tab-labels">
    <label for="lang-cpp-llama-3-3-70b-versatile">C++</label>
    <label for="lang-java-llama-3-3-70b-versatile">Java</label>
    <label for="lang-python-llama-3-3-70b-versatile">Python</label>
    <label for="lang-python3-llama-3-3-70b-versatile">Python3</label>
    <label for="lang-c-llama-3-3-70b-versatile">C</label>
    <label for="lang-csharp-llama-3-3-70b-versatile">C#</label>
    <label for="lang-javascript-llama-3-3-70b-versatile">JavaScript</label>
    <label for="lang-typescript-llama-3-3-70b-versatile">TypeScript</label>
    <label for="lang-php-llama-3-3-70b-versatile">PHP</label>
    <label for="lang-swift-llama-3-3-70b-versatile">Swift</label>
    <label for="lang-kotlin-llama-3-3-70b-versatile">Kotlin</label>
    <label for="lang-dart-llama-3-3-70b-versatile">Dart</label>
    <label for="lang-go-llama-3-3-70b-versatile">Go</label>
    <label for="lang-ruby-llama-3-3-70b-versatile">Ruby</label>
    <label for="lang-scala-llama-3-3-70b-versatile">Scala</label>
    <label for="lang-rust-llama-3-3-70b-versatile">Rust</label>
    <label for="lang-racket-llama-3-3-70b-versatile">Racket</label>
    <label for="lang-erlang-llama-3-3-70b-versatile">Erlang</label>
    <label for="lang-elixir-llama-3-3-70b-versatile">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
#include <vector>
         class Solution {
         public:
             bool kLengthApart(std::vector<int>& nums, int k) {
                 int prev = -1;
                 for (int i = 0; i < nums.size(); i++) {
                     if (nums[i] == 1) {
                         if (prev != -1 && i - prev <= k) {
                             return false;
                         }
                         prev = i;
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
                 int prev = -1;
                 for (int i = 0; i < nums.length; i++) {
                     if (nums[i] == 1) {
                         if (prev != -1 && i - prev <= k) {
                             return false;
                         }
                         prev = i;
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
             def kLengthApart(self, nums: list[int], k: int) -> bool:
                 prev = -1
                 for i, num in enumerate(nums):
                     if num == 1:
                         if prev != -1 and i - prev <= k:
                             return False
                         prev = i
                 return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
             def kLengthApart(self, nums: list[int], k: int) -> bool:
                 prev = -1
                 for i, num in enumerate(nums):
                     if num == 1:
                         if prev != -1 and i - prev <= k:
                             return False
                         prev = i
                 return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdbool.h>
         bool kLengthApart(int* nums, int numsSize, int k) {
             int prev = -1;
             for (int i = 0; i < numsSize; i++) {
                 if (nums[i] == 1) {
                     if (prev != -1 && i - prev <= k) {
                         return false;
                     }
                     prev = i;
                 }
             }
             return true;
         }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
public class Solution {
             public bool KLengthApart(int[] nums, int k) {
                 int prev = -1;
                 for (int i = 0; i < nums.Length; i++) {
                     if (nums[i] == 1) {
                         if (prev != -1 && i - prev <= k) {
                             return false;
                         }
                         prev = i;
                     }
                 }
                 return true;
             }
         }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
var kLengthApart = function(nums, k) {
             let prev = -1;
             for (let i = 0; i < nums.length; i++) {
                 if (nums[i] == 1) {
                     if (prev != -1 && i - prev <= k) {
                         return false;
                     }
                     prev = i;
                 }
             }
             return true;
         };
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function kLengthApart(nums: number[], k: number): boolean {
             let prev: number = -1;
             for (let i: number = 0; i < nums.length; i++) {
                 if (nums[i] == 1) {
                     if (prev != -1 && i - prev <= k) {
                         return false;
                     }
                     prev = i;
                 }
             }
             return true;
         }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
class Solution {
             function kLengthApart($nums, $k) {
                 $prev = -1;
                 for ($i = 0; $i < count($nums); $i++) {
                     if ($nums[$i] == 1) {
                         if ($prev != -1 && $i - $prev <= $k) {
                             return false;
                         }
                         $prev = $i;
                     }
                 }
                 return true;
             }
         }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution {
             func kLengthApart(_ nums: [Int], _ k: Int) -> Bool {
                 var prev: Int = -1
                 for (i, num) in nums.enumerated() {
                     if num == 1 {
                         if prev != -1 && i - prev <= k {
                             return false
                         }
                         prev = i
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
                 var prev: Int = -1
                 for (i in nums.indices) {
                     if (nums[i] == 1) {
                         if (prev != -1 && i - prev <= k) {
                             return false
                         }
                         prev = i
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
                 int prev = -1;
                 for (int i = 0; i < nums.length; i++) {
                     if (nums[i] == 1) {
                         if (prev != -1 && i - prev <= k) {
                             return false;
                         }
                         prev = i;
                     }
                 }
                 return true;
             }
         }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
func kLengthApart(nums []int, k int) bool {
             prev := -1
             for i, num := range nums {
                 if num == 1 {
                     if prev != -1 && i-prev <= k {
                         return false
                     }
                     prev = i
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
             prev = -1
             nums.each_with_index do |num, i|
                 if num == 1
                     if prev != -1 && i - prev <= k
                         return false
                     end
                     prev = i
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
                 var prev: Int = -1
                 for (i <- nums.indices) {
                     if (nums(i) == 1) {
                         if (prev != -1 && i - prev <= k) {
                             return false
                         }
                         prev = i
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
                 let mut prev: i32 = -1;
                 for (i, &num) in nums.iter().enumerate() {
                     if num == 1 {
                         if prev != -1 && i as i32 - prev <= k {
                             return false;
                         }
                         prev = i as i32;
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
         (define (k-length-apart nums k)
             (let loop ((nums nums) (prev -1))
                 (cond
                   ((null? nums) #t)
                   ((= (car nums) 1)
                    (if (and (not (= prev -1)) (<= (- (length nums) prev) k))
                        #f
                        (loop (cdr nums) (length nums))))
                   (else (loop (cdr nums) prev)))))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
         -export([k_length_apart/2]).
         k_length_apart(Nums, K) ->
             k_length_apart(Nums, K, -1).
         k_length_apart([], _, _) ->
             true;
         k_length_apart([1 | T], K, -1) ->
             k_length_apart(T, K, 0);
         k_length_apart([1 | T], K, Prev) ->
             if
                 Prev + K >= length([1 | T]) ->
                     false;
                 true ->
                     k_length_apart(T, K, 0)
             end;
         k_length_apart([_ | T], K, Prev) ->
             k_length_apart(T, K, Prev).
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
             def k_length_apart(nums, k) do
                 k_length_apart(nums, k, -1)
             end

             defp k_length_apart([], _, _), do: true
             defp k_length_apart([1 | t], k, -1), do: k_length_apart(t, k, 0)
             defp k_length_apart([1 | t], k, prev) when prev + k >= length([1 | t]), do: false
             defp k_length_apart([1 | t], k, _), do: k_length_apart(t, k, 0)
             defp k_length_apart([_ | t], k, prev), do: k_length_apart(t, k, prev)
         end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the binary array, because we are scanning the array once.

- **Space Complexity:** O(1) because we are using a constant amount of space to store the previous index of 1.

</details>
