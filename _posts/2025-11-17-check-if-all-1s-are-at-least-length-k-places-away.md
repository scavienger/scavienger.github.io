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

The problem asks us to determine if all '1's in a binary array `nums` are separated by at least `k` zeros. This means that for any two consecutive '1's in the array, say one at index `i` and the next one at index `j`, the number of elements (all of which must be zeros) between them, `j - i - 1`, must be greater than or equal to `k`.

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
```cpp
#include <vector>

class Solution {
public:
    bool kLengthApart(std::vector<int>& nums, int k) {
        int last_one_idx = -1; // Stores the index of the last encountered '1'. Initialized to -1 to signify no '1' has been seen yet.

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 1) {
                if (last_one_idx != -1) { // If this is not the first '1' we've seen
                    // Calculate the number of zeros between the current '1' at `i` and the last '1' at `last_one_idx`.
                    // This distance is `i - last_one_idx - 1`.
                    if (i - last_one_idx - 1 < k) {
                        return false; // The condition is violated: '1's are too close.
                    }
                }
                last_one_idx = i; // Update the index of the last encountered '1' to the current index.
            }
        }

        return true; // If the loop completes, all '1's are at least k places apart.
    }
};
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
```java
class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        int lastOneIdx = -1; // Stores the index of the last encountered '1'. Initialized to -1 to signify no '1' has been seen yet.

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                if (lastOneIdx != -1) { // If this is not the first '1' we've seen
                    // Calculate the number of zeros between the current '1' at `i` and the last '1' at `lastOneIdx`.
                    // This distance is `i - lastOneIdx - 1`.
                    if (i - lastOneIdx - 1 < k) {
                        return false; // The condition is violated: '1's are too close.
                    }
                }
                lastOneIdx = i; // Update the index of the last encountered '1' to the current index.
            }
        }

        return true; // If the loop completes, all '1's are at least k places apart.
    }
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
```python
from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one_idx = -1 # Stores the index of the last encountered '1'. Initialized to -1 to signify no '1' has been seen yet.

        for i in range(len(nums)):
            if nums[i] == 1:
                if last_one_idx != -1: # If this is not the first '1' we've seen
                    # Calculate the number of zeros between the current '1' at `i` and the last '1' at `last_one_idx`.
                    # This distance is `i - last_one_idx - 1`.
                    if i - last_one_idx - 1 < k:
                        return False # The condition is violated: '1's are too close.
                last_one_idx = i # Update the index of the last encountered '1' to the current index.

        return True # If the loop completes, all '1's are at least k places apart.
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
```python
from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one_idx = -1 # Stores the index of the last encountered '1'. Initialized to -1 to signify no '1' has been seen yet.

        for i in range(len(nums)):
            if nums[i] == 1:
                if last_one_idx != -1: # If this is not the first '1' we've seen
                    # Calculate the number of zeros between the current '1' at `i` and the last '1' at `last_one_idx`.
                    # This distance is `i - last_one_idx - 1`.
                    if i - last_one_idx - 1 < k:
                        return False # The condition is violated: '1's are too close.
                last_one_idx = i # Update the index of the last encountered '1' to the current index.

        return True # If the loop completes, all '1's are at least k places apart.
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
```c
#include <stdbool.h>
#include <stddef.h> // For size_t

bool kLengthApart(int* nums, int numsSize, int k) {
    int last_one_idx = -1; // Stores the index of the last encountered '1'. Initialized to -1 to signify no '1' has been seen yet.

    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 1) {
            if (last_one_idx != -1) { // If this is not the first '1' we've seen
                // Calculate the number of zeros between the current '1' at `i` and the last '1' at `last_one_idx`.
                // This distance is `i - last_one_idx - 1`.
                if (i - last_one_idx - 1 < k) {
                    return false; // The condition is violated: '1's are too close.
                }
            }
            last_one_idx = i; // Update the index of the last encountered '1' to the current index.
        }
    }

    return true; // If the loop completes, all '1's are at least k places apart.
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
```csharp
public class Solution {
    public bool KLengthApart(int[] nums, int k) {
        int lastOneIdx = -1; // Stores the index of the last encountered '1'. Initialized to -1 to signify no '1' has been seen yet.

        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 1) {
                if (lastOneIdx != -1) { // If this is not the first '1' we've seen
                    // Calculate the number of zeros between the current '1' at `i` and the last '1' at `lastOneIdx`.
                    // This distance is `i - lastOneIdx - 1`.
                    if (i - lastOneIdx - 1 < k) {
                        return false; // The condition is violated: '1's are too close.
                    }
                }
                lastOneIdx = i; // Update the index of the last encountered '1' to the current index.
            }
        }

        return true; // If the loop completes, all '1's are at least k places apart.
    }
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var kLengthApart = function(nums, k) {
    let lastOneIdx = -1; // Stores the index of the last encountered '1'. Initialized to -1 to signify no '1' has been seen yet.

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            if (lastOneIdx !== -1) { // If this is not the first '1' we've seen
                // Calculate the number of zeros between the current '1' at `i` and the last '1' at `lastOneIdx`.
                // This distance is `i - lastOneIdx - 1`.
                if (i - lastOneIdx - 1 < k) {
                    return false; // The condition is violated: '1's are too close.
                }
            }
            lastOneIdx = i; // Update the index of the last encountered '1' to the current index.
        }
    }

    return true; // If the loop completes, all '1's are at least k places apart.
};
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
```typescript
function kLengthApart(nums: number[], k: number): boolean {
    let lastOneIdx: number = -1; // Stores the index of the last encountered '1'. Initialized to -1 to signify no '1' has been seen yet.

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            if (lastOneIdx !== -1) { // If this is not the first '1' we've seen
                // Calculate the number of zeros between the current '1' at `i` and the last '1' at `lastOneIdx`.
                // This distance is `i - lastOneIdx - 1`.
                if (i - lastOneIdx - 1 < k) {
                    return false; // The condition is violated: '1's are too close.
                }
            }
            lastOneIdx = i; // Update the index of the last encountered '1' to the current index.
        }
    }

    return true; // If the loop completes, all '1's are at least k places apart.
};
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function kLengthApart($nums, $k) {
        $lastOneIdx = -1; // Stores the index of the last encountered '1'. Initialized to -1 to signify no '1' has been seen yet.

        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] === 1) {
                if ($lastOneIdx !== -1) { // If this is not the first '1' we've seen
                    // Calculate the number of zeros between the current '1' at `i` and the last '1' at `lastOneIdx`.
                    // This distance is `i - lastOneIdx - 1`.
                    if ($i - $lastOneIdx - 1 < $k) {
                        return false; // The condition is violated: '1's are too close.
                    }
                }
                $lastOneIdx = $i; // Update the index of the last encountered '1' to the current index.
            }
        }

        return true; // If the loop completes, all '1's are at least k places apart.
    }
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
```swift
class Solution {
    func kLengthApart(_ nums: [Int], _ k: Int) -> Bool {
        var lastOneIdx: Int = -1 // Stores the index of the last encountered '1'. Initialized to -1 to signify no '1' has been seen yet.

        for (i, num) in nums.enumerated() {
            if num == 1 {
                if lastOneIdx != -1 { // If this is not the first '1' we've seen
                    // Calculate the number of zeros between the current '1' at `i` and the last '1' at `lastOneIdx`.
                    // This distance is `i - lastOneIdx - 1`.
                    if i - lastOneIdx - 1 < k {
                        return false // The condition is violated: '1's are too close.
                    }
                }
                lastOneIdx = i // Update the index of the last encountered '1' to the current index.
            }
        }

        return true // If the loop completes, all '1's are at least k places apart.
    }
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
```kotlin
class Solution {
    fun kLengthApart(nums: IntArray, k: Int): Boolean {
        var lastOneIdx: Int = -1 // Stores the index of the last encountered '1'. Initialized to -1 to signify no '1' has been seen yet.

        for (i in nums.indices) {
            if (nums[i] == 1) {
                if (lastOneIdx != -1) { // If this is not the first '1' we've seen
                    // Calculate the number of zeros between the current '1' at `i` and the last '1' at `lastOneIdx`.
                    // This distance is `i - lastOneIdx - 1`.
                    if (i - lastOneIdx - 1 < k) {
                        return false // The condition is violated: '1's are too close.
                    }
                }
                lastOneIdx = i // Update the index of the last encountered '1' to the current index.
            }
        }

        return true // If the loop completes, all '1's are at least k places apart.
    }
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
```dart
class Solution {
  bool kLengthApart(List<int> nums, int k) {
    int lastOneIdx = -1; // Stores the index of the last encountered '1'. Initialized to -1 to signify no '1' has been seen yet.

    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == 1) {
        if (lastOneIdx != -1) { // If this is not the first '1' we've seen
          // Calculate the number of zeros between the current '1' at `i` and the last '1' at `lastOneIdx`.
          // This distance is `i - lastOneIdx - 1`.
          if (i - lastOneIdx - 1 < k) {
            return false; // The condition is violated: '1's are too close.
          }
        }
        lastOneIdx = i; // Update the index of the last encountered '1' to the current index.
      }
    }

    return true; // If the loop completes, all '1's are at least k places apart.
  }
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
```go
package main

func kLengthApart(nums []int, k int) bool {
    lastOneIdx := -1 // Stores the index of the last encountered '1'. Initialized to -1 to signify no '1' has been seen yet.

    for i := 0; i < len(nums); i++ {
        if nums[i] == 1 {
            if lastOneIdx != -1 { // If this is not the first '1' we've seen
                // Calculate the number of zeros between the current '1' at `i` and the last '1' at `lastOneIdx`.
                // This distance is `i - lastOneIdx - 1`.
                if i - lastOneIdx - 1 < k {
                    return false // The condition is violated: '1's are too close.
                }
            }
            lastOneIdx = i // Update the index of the last encountered '1' to the current index.
        }
    }

    return true // If the loop completes, all '1's are at least k places apart.
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def k_length_apart(nums, k)
    last_one_idx = -1 # Stores the index of the last encountered '1'. Initialized to -1 to signify no '1' has been seen yet.

    nums.each_with_index do |num, i|
        if num == 1
            if last_one_idx != -1 # If this is not the first '1' we've seen
                # Calculate the number of zeros between the current '1' at `i` and the last '1' at `last_one_idx`.
                # This distance is `i - last_one_idx - 1`.
                if i - last_one_idx - 1 < k
                    return false # The condition is violated: '1's are too close.
                end
            end
            last_one_idx = i # Update the index of the last encountered '1' to the current index.
        end
    end

    true # If the loop completes, all '1's are at least k places apart.
end
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
```scala
object Solution {
    def kLengthApart(nums: Array[Int], k: Int): Boolean = {
        var lastOneIdx: Int = -1 // Stores the index of the last encountered '1'. Initialized to -1 to signify no '1' has been seen yet.

        for (i <- nums.indices) {
            if (nums(i) == 1) {
                if (lastOneIdx != -1) { // If this is not the first '1' we've seen
                    // Calculate the number of zeros between the current '1' at `i` and the last '1' at `lastOneIdx`.
                    // This distance is `i - lastOneIdx - 1`.
                    if (i - lastOneIdx - 1 < k) {
                        return false // The condition is violated: '1's are too close.
                    }
                }
                lastOneIdx = i // Update the index of the last encountered '1' to the current index.
            }
        }

        true // If the loop completes, all '1's are at least k places apart.
    }
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
```rust
impl Solution {
    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
        let mut last_one_idx: i32 = -1; // Stores the index of the last encountered '1'. Initialized to -1 to signify no '1' has been seen yet.

        for (i, &num) in nums.iter().enumerate() {
            if num == 1 {
                if last_one_idx != -1 { // If this is not the first '1' we've seen
                    // Calculate the number of zeros between the current '1' at `i` and the last '1' at `last_one_idx`.
                    // This distance is `i - last_one_idx - 1`.
                    if (i as i32) - last_one_idx - 1 < k {
                        return false; // The condition is violated: '1's are too close.
                    }
                }
                last_one_idx = i as i32; // Update the index of the last encountered '1' to the current index.
            }
        }

        true // If the loop completes, all '1's are at least k places apart.
    }
}
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
```racket
#lang racket

(provide (rename-out [k-length-apart solution]))

; The function `k-length-apart` checks if all '1's in a list `nums` are separated by at least `k` zeros.
; It uses a helper loop that maintains the current index (`idx`) and the index of the last seen '1' (`last-one-idx`).
(define (k-length-apart nums k)
  (let loop ([idx 0] [last-one-idx -1] [nums-rest nums])
    (cond
      [(empty? nums-rest) #true] ; If we've processed all elements, all '1's are sufficiently apart.
      [(equal? (car nums-rest) 1) ; If the current element is a '1'
       (if (and (not (= last-one-idx -1)) (< (- idx last-one-idx 1) k))
           #false ; Condition violated: current '1' is too close to the previous '1'.
           (loop (+ idx 1) idx (cdr nums-rest))) ; Continue, updating last-one-idx to current index.
      [else ; If the current element is a '0'
       (loop (+ idx 1) last-one-idx (cdr nums-rest))])))
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
```erlang
-module(solution).
-export([k_length_apart/2]).

%% @doc `k_length_apart(Nums, K)` returns `true` if all `1`'s are at least `K` places away from each other, otherwise returns `false`.
-spec k_length_apart(Nums :: [0 | 1], K :: integer()) -> boolean().
k_length_apart(Nums, K) ->
    % Start the recursive helper with initial index 0 and last_one_idx -1 (meaning no '1' seen yet).
    k_length_apart_impl(Nums, K, 0, -1).

% Base case: If the list is empty, all '1's found so far (if any) have satisfied the condition.
k_length_apart_impl([], _K, _Idx, _LastOneIdx) ->
    true;
% Recursive case: Current element is '1'.
k_length_apart_impl([H | T], K, Idx, LastOneIdx) when H == 1 ->
    if
        LastOneIdx =/= -1 andalso (Idx - LastOneIdx - 1) < K ->
            % Condition violated: the current '1' is too close to the previous '1'.
            false;
        true ->
            % Condition satisfied for this pair, or this is the first '1'. Continue recursion.
            k_length_apart_impl(T, K, Idx + 1, Idx) % Update LastOneIdx to the current index.
    end;
% Recursive case: Current element is '0'.
k_length_apart_impl([_H | T], K, Idx, LastOneIdx) ->
    % Current element is '0', so no change to LastOneIdx. Continue recursion.
    k_length_apart_impl(T, K, Idx + 1, LastOneIdx).
```
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
```elixir
defmodule Solution do
  @spec k_length_apart(nums :: [integer], k :: integer) :: boolean
  def k_length_apart(nums, k) do
    # Start the recursive helper with initial index 0 and last_one_idx -1 (meaning no '1' seen yet).
    do_k_length_apart(nums, k, 0, -1)
  end

  # Base case: If the list is empty, all '1's found so far (if any) have satisfied the condition.
  defp do_k_length_apart([], _k, _idx, _last_one_idx), do: true

  # Recursive case: Current element is '1'.
  defp do_k_length_apart([1 | rest], k, idx, last_one_idx) do
    if last_one_idx != -1 && (idx - last_one_idx - 1) < k do
      # Condition violated: the current '1' is too close to the previous '1'.
      false
    else
      # Condition satisfied for this pair, or this is the first '1'. Continue recursion.
      do_k_length_apart(rest, k, idx + 1, idx) # Update last_one_idx to the current index.
    end
  end

  # Recursive case: Current element is '0'.
  defp do_k_length_apart([_ | rest], k, idx, last_one_idx) do
    # Current element is '0', so no change to last_one_idx. Continue recursion.
    do_k_length_apart(rest, k, idx + 1, last_one_idx)
  end
end
```
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N), where N is the length of the `nums` array. We iterate through the array exactly once from start to end. For each element, we perform a constant number of operations (comparison, arithmetic, assignment).
- **Space Complexity:** O(1). We use a constant amount of extra space to store a few variables such as `last_one_idx` (to keep track of the index of the previously found '1') and the loop counter `i`.
