---
layout: post
title: Check If All 1's Are at Least Length K Places Away
date: "2025-11-02 09:00:00 +0900"
categories: [LeetCode, Easy]
tags: ["Array"]
difficulty: Easy
leetcode_url: "https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/"
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


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-19 22:39:13)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to determine if all occurrences of the digit '1' in a given binary array `nums` are separated by at least `k` places. This means if we find a '1' at index `i` and the very next '1' (to its right) at index `j`, there must be at least `k` zeros between them. In other words, the count of elements between index `i` and `j`, excluding `nums[i]` and `nums[j]`, must be greater than or equal to `k`. Mathematically, this implies `j - i - 1 >= k`, which can be rearranged to `j - i >= k + 1` (the distance between their indices must be at least `k+1`).

The most efficient way to solve this is to traverse the array once, keeping track of the index of the last '1' encountered. We can initialize a variable, let's call it `last_one_index`, to a sentinel value like -1 to signify that we haven't found any '1's yet. As we iterate through the `nums` array, whenever we encounter a '1', we perform a check. If `last_one_index` is not -1, it means we have previously seen a '1'. At this point, we calculate the number of zeros between the current '1' and the previous '1'. This count is `current_index - last_one_index - 1`.

If this calculated count of zeros is less than `k`, it means the condition is violated, and we can immediately return `false`. If the condition holds (i.e., `current_index - last_one_index - 1 >= k`), or if `last_one_index` was -1 (meaning this is the first '1' we've encountered), we update `last_one_index` to the `current_index`. We continue this process for the entire array. If the loop completes without returning `false`, it implies that all pairs of '1's satisfy the `k`-length apart condition, and we can confidently return `true`.

Consider a few edge cases: If `nums` contains no '1's or only one '1', `last_one_index` will either remain -1 or be updated only once, so the distance check `if (last_one_index != -1)` will never evaluate to true for a subsequent '1' to trigger a `false` return. In these scenarios, the loop finishes, and `true` is correctly returned, as there are no '1's to violate the condition. If `k` is 0, the condition `i - last_one_index - 1 < 0` would mean `i - last_one_index < 1`. This implies that `1`s can be adjacent (e.g., `[1,1]`), which is consistent with being 'at least 0 places away'. The algorithm correctly handles this by returning `true` for `[1,1], k=0`.

### Code

<div class="code-tabs" markdown="0">
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
        int lastOneIndex = -1;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 1) {
                if (lastOneIndex != -1) {
                    // Check if the number of zeros between current 1 and last 1 is less than k
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
                    // Check if the number of zeros between current 1 and last 1 is less than k
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
                    # Check if the number of zeros between current 1 and last 1 is less than k
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
                    # Check if the number of zeros between current 1 and last 1 is less than k
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
                // Check if the number of zeros between current 1 and last 1 is less than k
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

public class Solution {
    public bool KLengthApart(int[] nums, int k) {
        int lastOneIndex = -1;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 1) {
                if (lastOneIndex != -1) {
                    // Check if the number of zeros between current 1 and last 1 is less than k
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
                // Check if the number of zeros between current 1 and last 1 is less than k
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
                // Check if the number of zeros between current 1 and last 1 is less than k
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
                    // Check if the number of zeros between current 1 and last 1 is less than k
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
        var lastOneIndex = -1
        for i in 0..<nums.count {
            if nums[i] == 1 {
                if lastOneIndex != -1 {
                    // Check if the number of zeros between current 1 and last 1 is less than k
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
        var lastOneIndex = -1
        for (i in nums.indices) {
            if (nums[i] == 1) {
                if (lastOneIndex != -1) {
                    // Check if the number of zeros between current 1 and last 1 is less than k
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
          // Check if the number of zeros between current 1 and last 1 is less than k
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
                // Check if the number of zeros between current 1 and last 1 is less than k
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
                # Check if the number of zeros between current 1 and last 1 is less than k
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
        var lastOneIndex = -1
        for (i <- nums.indices) {
            if (nums(i) == 1) {
                if (lastOneIndex != -1) {
                    // Check if the number of zeros between current 1 and last 1 is less than k
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
                    // Check if the number of zeros between current 1 and last 1 is less than k
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

(provide (rename-out [k-length-apart-impl kLengthApart]))

;; LeetCode's Python template suggests List[int], implying array-like access.
;; For Racket, we'll use a vector for efficient indexed access (O(1)).
;; The input 'nums' might be a list, so we'd typically convert it if direct indexing is needed.
;; Assuming 'nums' is passed as a list, convert to vector for internal processing.
(define (k-length-apart-impl nums-list k)
  (let ([nums (list->vector nums-list)]) ; Convert list to vector for array-like access
    (let loop ((i 0) (last-one-index -1))
      (cond
        ((= i (vector-length nums)) #t) ; Reached end of array, all checks passed
        ((= (vector-ref nums i) 1)
         (if (not (= last-one-index -1))
             (if (< (- i last-one-index 1) k)
                 #f ; Condition violated: less than k zeros between 1s
                 (loop (+ i 1) i)) ; Condition met, update last-one-index and continue
             (loop (+ i 1) i))) ; First '1', just update last-one-index and continue
        (else ; nums[i] is 0
         (loop (+ i 1) last-one-index)))))) ; Continue with same last-one-index
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
-export([k_length_apart/2]).

k_length_apart(Nums, K) ->
    % Helper function for list iteration using head/tail recursion
    k_length_apart_list(Nums, K, -1, 0).

k_length_apart_list([], _K, _LastOneIndex, _CurrentIndex) ->
    true; % Reached end of the list, all checks passed
k_length_apart_list([Head|Tail], K, LastOneIndex, CurrentIndex) ->
    case Head of
        1 ->
            if LastOneIndex =/= -1 ->
                % Calculate number of zeros between current 1 and last 1
                Dist = CurrentIndex - LastOneIndex - 1,
                if Dist < K ->
                    false; % Condition violated
                true ->
                    % Condition met, update last_one_index and continue
                    k_length_apart_list(Tail, K, CurrentIndex, CurrentIndex + 1)
                end;
            true -> % First '1', just update last_one_index and continue
                k_length_apart_list(Tail, K, CurrentIndex, CurrentIndex + 1)
            end;
        0 ->
            % Current element is 0, continue with same last_one_index
            k_length_apart_list(Tail, K, LastOneIndex, CurrentIndex + 1)
    end.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
  @spec k_length_apart(nums :: [integer], k :: integer) :: boolean
  def k_length_apart(nums, k) do
    # Helper function for list iteration using head/tail recursion
    do_k_length_apart(nums, k, -1, 0)
  end

  defp do_k_length_apart([], _k, _last_one_index, _current_index) do
    true # Reached end of the list, all checks passed
  end

  defp do_k_length_apart([head | tail], k, last_one_index, current_index) do
    case head do
      1 ->
        if last_one_index != -1 do
          # Calculate number of zeros between current 1 and last 1
          dist = current_index - last_one_index - 1
          if dist < k do
            false # Condition violated
          else
            # Condition met, update last_one_index and continue
            do_k_length_apart(tail, k, current_index, current_index + 1)
          end
        else
          # First '1', just update last_one_index and continue
          do_k_length_apart(tail, k, current_index, current_index + 1)
        end
      0 ->
        # Current element is 0, continue with same last_one_index
        do_k_length_apart(tail, k, last_one_index, current_index + 1)
    end
  end
end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N)

- **Space Complexity:** O(1)

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-19 22:39:18)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by iterating through the given binary array and checking the distance between each pair of 1's. We can use a variable to keep track of the position of the last 1 we encountered. If we find a new 1 and the distance between it and the last 1 is less than k, we return false. If we finish iterating through the array without finding any 1's that are too close together, we return true.

### Code

<div class="code-tabs" markdown="0">
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
class Solution {
       public:
           bool kLengthApart(vector<int>& nums, int k) {
               int lastOne = -1;
               for (int i = 0; i < nums.size(); i++) {
                   if (nums[i] == 1) {
                       if (lastOne != -1 && i - lastOne - 1 < k) {
                           return false;
                       }
                       lastOne = i;
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
               int lastOne = -1;
               for (int i = 0; i < nums.length; i++) {
                   if (nums[i] == 1) {
                       if (lastOne != -1 && i - lastOne - 1 < k) {
                           return false;
                       }
                       lastOne = i;
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
               last_one = -1
               for i, num in enumerate(nums):
                   if num == 1:
                       if last_one != -1 and i - last_one - 1 < k:
                           return False
                       last_one = i
               return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
           def kLengthApart(self, nums: list[int], k: int) -> bool:
               last_one = -1
               for i, num in enumerate(nums):
                   if num == 1:
                       if last_one != -1 and i - last_one - 1 < k:
                           return False
                       last_one = i
               return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdbool.h>
       bool kLengthApart(int* nums, int numsSize, int k) {
           int lastOne = -1;
           for (int i = 0; i < numsSize; i++) {
               if (nums[i] == 1) {
                   if (lastOne != -1 && i - lastOne - 1 < k) {
                       return false;
                   }
                   lastOne = i;
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
               int lastOne = -1;
               for (int i = 0; i < nums.Length; i++) {
                   if (nums[i] == 1) {
                       if (lastOne != -1 && i - lastOne - 1 < k) {
                           return false;
                       }
                       lastOne = i;
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
           let lastOne = -1;
           for (let i = 0; i < nums.length; i++) {
               if (nums[i] == 1) {
                   if (lastOne != -1 && i - lastOne - 1 < k) {
                       return false;
                   }
                   lastOne = i;
               }
           }
           return true;
       };
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function kLengthApart(nums: number[], k: number): boolean {
           let lastOne: number = -1;
           for (let i: number = 0; i < nums.length; i++) {
               if (nums[i] == 1) {
                   if (lastOne != -1 && i - lastOne - 1 < k) {
                       return false;
                   }
                   lastOne = i;
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
               $lastOne = -1;
               for ($i = 0; $i < count($nums); $i++) {
                   if ($nums[$i] == 1) {
                       if ($lastOne != -1 && $i - $lastOne - 1 < $k) {
                           return false;
                       }
                       $lastOne = $i;
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
               var lastOne = -1
               for (i, num) in nums.enumerated() {
                   if num == 1 {
                       if lastOne != -1 && i - lastOne - 1 < k {
                           return false
                       }
                       lastOne = i
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
               var lastOne = -1
               for (i in nums.indices) {
                   if (nums[i] == 1) {
                       if (lastOne != -1 && i - lastOne - 1 < k) {
                           return false
                       }
                       lastOne = i
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
               int lastOne = -1;
               for (int i = 0; i < nums.length; i++) {
                   if (nums[i] == 1) {
                       if (lastOne != -1 && i - lastOne - 1 < k) {
                           return false;
                       }
                       lastOne = i;
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
           lastOne := -1
           for i, num := range nums {
               if num == 1 {
                   if lastOne != -1 && i-lastOne-1 < k {
                       return false
                   }
                   lastOne = i
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
           last_one = -1
           nums.each_with_index do |num, i|
               if num == 1
                   if last_one != -1 && i - last_one - 1 < k
                       return false
                   end
                   last_one = i
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
               var lastOne = -1
               for (i <- nums.indices) {
                   if (nums(i) == 1) {
                       if (lastOne != -1 && i - lastOne - 1 < k) {
                           return false
                       }
                       lastOne = i
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
               let mut last_one = -1;
               for (i, &num) in nums.iter().enumerate() {
                   if num == 1 {
                       if last_one != -1 && i as i32 - last_one - 1 < k {
                           return false;
                       }
                       last_one = i as i32;
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
           (let loop ([nums nums] [last-one -1])
             (cond
               [(null? nums) #t]
               [(= (car nums) 1)
                (if (and (not (= last-one -1)) (< (- (length nums) last-one) k))
                    #f
                    (loop (cdr nums) (length nums)))]
               [else (loop (cdr nums) last-one)])))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
       -export([k_length_apart/2]).
       k_length_apart(Nums, K) ->
           k_length_apart(Nums, K, -1).
       k_length_apart([], _K, _LastOne) ->
           true;
       k_length_apart([1|T], K, -1) ->
           k_length_apart(T, K, 0);
       k_length_apart([1|T], K, LastOne) ->
           case (0 - LastOne) - 1 < K of
               true -> false;
               false -> k_length_apart(T, K, 0)
           end;
       k_length_apart([_|T], K, LastOne) ->
           k_length_apart(T, K, LastOne).
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
           def k_length_apart(nums, k) do
               k_length_apart(nums, k, -1)
           end
           defp k_length_apart([], _k, _last_one), do: true
           defp k_length_apart([1|t], k, -1), do: k_length_apart(t, k, 0)
           defp k_length_apart([1|t], k, last_one) do
               if 0 - last_one - 1 < k do
                   false
               else
                   k_length_apart(t, k, 0)
               end
           end
           defp k_length_apart([_|t], k, last_one), do: k_length_apart(t, k, last_one)
       end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the input array, because we are doing a constant amount of work for each element in the array.

- **Space Complexity:** O(1) because we are using a constant amount of space to store our variables, regardless of the size of the input array.

</div>
</details>
