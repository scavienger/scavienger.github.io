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

The problem asks us to verify if every pair of '1's in a binary array `nums` is separated by at least `k` '0's. This means the distance between the indices of any two consecutive '1's must be at least `k + 1`. If we find a '1' at index `i` and the immediately preceding '1' was at `last_one_idx`, then the number of '0's between them is `i - last_one_idx - 1`. This value must be greater than or equal to `k` for the condition to hold.

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
        int last_one_idx = -k - 1; // Initialize to a value that makes the first check always pass

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 1) {
                // If the distance (number of zeros + 1) is less than k + 1
                // or equivalently, number of zeros is less than k
                if (i - last_one_idx - 1 < k) {
                    return false;
                }
                last_one_idx = i;
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
        int lastOneIdx = -k - 1; // Initialize to a value that makes the first check always pass

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                // If the number of zeros between current '1' and last '1' is less than k
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

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one_idx = -k - 1 # Initialize to a value that makes the first check always pass

        for i in range(len(nums)):
            if nums[i] == 1:
                # If the number of zeros between current '1' and last '1' is less than k
                if (i - last_one_idx - 1) < k:
                    return False
                last_one_idx = i

        return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one_idx = -k - 1 # Initialize to a value that makes the first check always pass

        for i in range(len(nums)):
            if nums[i] == 1:
                # If the number of zeros between current '1' and last '1' is less than k
                if (i - last_one_idx - 1) < k:
                    return False
                last_one_idx = i

        return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdbool.h>
#include <stddef.h>

bool kLengthApart(int* nums, int numsSize, int k) {
    int last_one_idx = -k - 1; // Initialize to a value that makes the first check always pass

    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 1) {
            // If the number of zeros between current '1' and last '1' is less than k
            if (i - last_one_idx - 1 < k) {
                return false;
            }
            last_one_idx = i;
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
        int lastOneIdx = -k - 1; // Initialize to a value that makes the first check always pass

        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 1) {
                // If the number of zeros between current '1' and last '1' is less than k
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

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var kLengthApart = function(nums, k) {
    let lastOneIdx = -k - 1; // Initialize to a value that makes the first check always pass

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            // If the number of zeros between current '1' and last '1' is less than k
            if ((i - lastOneIdx - 1) < k) {
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
    let lastOneIdx: number = -k - 1; // Initialize to a value that makes the first check always pass

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            // If the number of zeros between current '1' and last '1' is less than k
            if ((i - lastOneIdx - 1) < k) {
                return false;
            }
            lastOneIdx = i;
        }
    }

    return true;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function kLengthApart($nums, $k) {
        $lastOneIdx = -$k - 1; // Initialize to a value that makes the first check always pass

        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] === 1) {
                // If the number of zeros between current '1' and last '1' is less than k
                if (($i - $lastOneIdx - 1) < $k) {
                    return false;
                }
                $lastOneIdx = $i;
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
        var lastOneIdx = -k - 1 // Initialize to a value that makes the first check always pass

        for (i, num) in nums.enumerated() {
            if num == 1 {
                // If the number of zeros between current '1' and last '1' is less than k
                if (i - lastOneIdx - 1) < k {
                    return false
                }
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
        var lastOneIdx = -k - 1 // Initialize to a value that makes the first check always pass

        for (i in nums.indices) {
            if (nums[i] == 1) {
                // If the number of zeros between current '1' and last '1' is less than k
                if (i - lastOneIdx - 1 < k) {
                    return false
                }
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
    int lastOneIdx = -k - 1; // Initialize to a value that makes the first check always pass

    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == 1) {
        // If the number of zeros between current '1' and last '1' is less than k
        if ((i - lastOneIdx - 1) < k) {
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

  <div class="tab-panel" data-lang="go">

{% highlight go %}
func kLengthApart(nums []int, k int) bool {
    lastOneIdx := -k - 1 // Initialize to a value that makes the first check always pass

    for i, num := range nums {
        if num == 1 {
            // If the number of zeros between current '1' and last '1' is less than k
            if (i - lastOneIdx - 1) < k {
                return false
            }
            lastOneIdx = i
        }
    }

    return true
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
class Solution
    /**
     * @param {Integer[]} nums
     * @param {Integer} k
     * @return {Boolean}
     */
    def k_length_apart(nums, k)
        last_one_idx = -k - 1 # Initialize to a value that makes the first check always pass

        nums.each_with_index do |num, i|
            if num == 1
                # If the number of zeros between current '1' and last '1' is less than k
                if (i - last_one_idx - 1) < k
                    return false
                end
                last_one_idx = i
            end
        end

        true
    end
end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {
    def kLengthApart(nums: Array[Int], k: Int): Boolean = {
        var lastOneIdx = -k - 1 // Initialize to a value that makes the first check always pass

        for (i <- nums.indices) {
            if (nums(i) == 1) {
                // If the number of zeros between current '1' and last '1' is less than k
                if ((i - lastOneIdx - 1) < k) {
                    return false
                }
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
        let mut last_one_idx: i32 = -k - 1; // Initialize to a value that makes the first check always pass

        for (i, &num) in nums.iter().enumerate() {
            if num == 1 {
                // If the number of zeros between current '1' and last '1' is less than k
                // (i as i32) is needed for type consistency with last_one_idx and k
                if ((i as i32) - last_one_idx - 1) < k {
                    return false;
                }
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
(provide (rename-out [k-length-apart solution]))

(define (k-length-apart nums k)
  (let loop ((idx 0) (last-one-idx (- 0 k 1))) ;; Initialize last-one-idx to -k-1
    (if (>= idx (vector-length nums))
        #t ;; Reached end, all good
        (let ((val (vector-ref nums idx)))
          (if (= val 1)
              (if (< (- idx last-one-idx 1) k)
                  #f ;; Condition violated
                  (loop (+ idx 1) idx)) ;; Update last-one-idx to current idx
              (loop (+ idx 1) last-one-idx)))))) ;; Move to next, last-one-idx unchanged
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
-export([k_length_apart/2]).

k_length_apart(Nums, K) ->
    % Nums: list of integers (0 or 1)
    % K: integer
    % Initialize last_one_idx to -K - 1 to ensure the first '1' found passes the distance check.
    k_length_apart_recursive(Nums, K, 0, -K - 1).

k_length_apart_recursive([], _K, _Idx, _LastOneIdx) ->
    true;
k_length_apart_recursive([0 | T], K, Idx, LastOneIdx) ->
    % If current element is 0, just move to the next, last_one_idx remains unchanged.
    k_length_apart_recursive(T, K, Idx + 1, LastOneIdx);
k_length_apart_recursive([1 | T], K, Idx, LastOneIdx) ->
    % If current element is 1, check the distance.
    % The number of zeros between the current '1' and the last '1' is (Idx - LastOneIdx - 1).
    % This must be >= K.
    IfConditionViolated = (Idx - LastOneIdx - 1) < K,
    if IfConditionViolated ->
            false; % Condition violated, return false.
       true ->
            % Condition met, update last_one_idx to current Idx and continue.
            k_length_apart_recursive(T, K, Idx + 1, Idx)
    end.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
  @spec k_length_apart(nums :: [integer], k :: integer) :: boolean
  def k_length_apart(nums, k) do
    # Initialize last_one_idx to -k - 1 to ensure the first '1' found passes the distance check.
    do_k_length_apart(nums, k, 0, -k - 1)
  end

  defp do_k_length_apart([], _k, _idx, _last_one_idx), do: true

  defp do_k_length_apart([0 | rest], k, idx, last_one_idx) do
    # If current element is 0, just move to the next, last_one_idx remains unchanged.
    do_k_length_apart(rest, k, idx + 1, last_one_idx)
  end

  defp do_k_length_apart([1 | rest], k, idx, last_one_idx) do
    # If current element is 1, check the distance.
    # The number of zeros between the current '1' and the last '1' is (idx - last_one_idx - 1).
    # This must be >= k.
    if idx - last_one_idx - 1 < k do
      false # Condition violated, return false.
    else
      # Condition met, update last_one_idx to current idx and continue.
      do_k_length_apart(rest, k, idx + 1, idx)
    end
  end
end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)
