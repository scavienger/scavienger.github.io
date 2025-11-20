---
layout: post
title: Check If All 1's Are at Least Length K Places Away
date: "2025-11-17 09:00:00 +0900"
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
  <small class="solution-timestamp">(2025-11-19 22:26:55)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to determine if all '1's in a given binary array `nums` are separated by at least `k` positions. More specifically, if we encounter a '1' at index `i` and the next '1' is at index `j` (where `j > i`), then the number of zeros between them, which is `j - i - 1`, must be greater than or equal to `k`. This condition can be mathematically expressed as `j - i - 1 >= k`, which simplifies to `j - i >= k + 1`. This means the distance in terms of indices between any two consecutive '1's must be at least `k + 1`.

The core strategy to solve this is to iterate through the array once, keeping track of the index of the most recently encountered '1'. When a new '1' is found, we compare its current index to the index of the previous '1' to ensure they are sufficiently far apart. If at any point we find two '1's that violate this distance requirement, we can immediately conclude that the condition is not met and return `false`. If we successfully traverse the entire array without finding any such violation, it implies all '1's are properly separated, and we return `true`.

To implement this, we initialize a variable, let's call it `lastOneIndex`, to a value that ensures the first '1' encountered will always satisfy the distance condition. A suitable initial value is `-(k + 1)`. For instance, if `k=2`, `lastOneIndex` starts at `-3`. When the first '1' is found at index `i`, the difference `i - lastOneIndex` will be `i - (-(k + 1)) = i + k + 1`. Since `k` is non-negative and `i` is also non-negative, `i + k + 1` will always be greater than or equal to `k + 1`, thus passing the initial check for the first '1'. As we iterate through the `nums` array, if we encounter `nums[i] == 1`:
1. We calculate the difference `i - lastOneIndex`. This represents the total number of positions between the current '1' and the last '1' (inclusive of both '1's).
2. We then check if this difference `i - lastOneIndex` is less than or equal to `k`. If it is, it means the '1's are too close (i.e., `j - i < k + 1`, or `j - i - 1 < k`). In this case, the condition is violated, and we immediately return `false`.
3. Otherwise (if the difference `i - lastOneIndex` is greater than `k`), the '1's are sufficiently far apart. We then update `lastOneIndex` to `i` to mark the current '1' as the new reference point for subsequent checks.
If `nums[i]` is '0', we simply continue to the next element, as zeros only contribute to the distance and don't trigger checks directly. If the loop completes without returning `false`, it means all '1's satisfy the condition, and we return `true`.

For example, consider `nums = [1,0,0,1,0,1]` and `k = 2`. `lastOneIndex` starts at `-(2+1) = -3`.
- At `i=0`, `nums[0]=1`: `0 - (-3) = 3`. `3 <= 2` is false. Update `lastOneIndex = 0`.
- At `i=1`, `nums[1]=0`: continue.
- At `i=2`, `nums[2]=0`: continue.
- At `i=3`, `nums[3]=1`: `3 - 0 = 3`. `3 <= 2` is false. Update `lastOneIndex = 3`.
- At `i=4`, `nums[4]=0`: continue.
- At `i=5`, `nums[5]=1`: `5 - 3 = 2`. `2 <= 2` is true. The condition is violated! Return `false`.
This approach correctly handles cases with no '1's (the loop finishes, returns true), arrays with only one '1' (the loop finishes, returns true), and ensures that `k=0` correctly identifies `1,1` as separated by 0 zeros (since `j - i - 1 >= 0` is `1-0-1 >= 0`, meaning `0 >= 0` which is true, so `1,1` would be valid for `k=0`). The logic `i - lastOneIndex > k` (or its negation `i - lastOneIndex <= k` for returning false) robustly captures the requirement.

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
        int lastOneIndex = -k - 1;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 1) {
                if (i - lastOneIndex <= k) {
                    return false;
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
        int lastOneIndex = -k - 1;
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] == 1) {
                if (i - lastOneIndex <= k) {
                    return false;
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
        last_one_index = -k - 1
        for i, num in enumerate(nums):
            if num == 1:
                if i - last_one_index <= k:
                    return False
                last_one_index = i
        return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one_index = -k - 1
        for i, num in enumerate(nums):
            if num == 1:
                if i - last_one_index <= k:
                    return False
                last_one_index = i
        return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdbool.h>
#include <stddef.h>

bool kLengthApart(int* nums, int numsSize, int k) {
    int lastOneIndex = -k - 1;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 1) {
            if (i - lastOneIndex <= k) {
                return false;
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
public class Solution {
    public bool KLengthApart(int[] nums, int k) {
        int lastOneIndex = -k - 1;
        for (int i = 0; i < nums.Length; ++i) {
            if (nums[i] == 1) {
                if (i - lastOneIndex <= k) {
                    return false;
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
    let lastOneIndex = -k - 1;
    for (let i = 0; i < nums.length; ++i) {
        if (nums[i] === 1) {
            if (i - lastOneIndex <= k) {
                return false;
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
    let lastOneIndex: number = -k - 1;
    for (let i = 0; i < nums.length; ++i) {
        if (nums[i] === 1) {
            if (i - lastOneIndex <= k) {
                return false;
            }
            lastOneIndex = i;
        }
    }
    return true;
}
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
        $lastOneIndex = -$k - 1;
        for ($i = 0; $i < count($nums); ++$i) {
            if ($nums[$i] === 1) {
                if ($i - $lastOneIndex <= $k) {
                    return false;
                }
                $lastOneIndex = $i;
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
        var lastOneIndex = -k - 1
        for (i, num) in nums.enumerated() {
            if num == 1 {
                if i - lastOneIndex <= k {
                    return false
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
        var lastOneIndex = -k - 1
        for (i in nums.indices) {
            if (nums[i] == 1) {
                if (i - lastOneIndex <= k) {
                    return false
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
    int lastOneIndex = -k - 1;
    for (int i = 0; i < nums.length; ++i) {
      if (nums[i] == 1) {
        if (i - lastOneIndex <= k) {
          return false;
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
func kLengthApart(nums []int, k int) bool {
    lastOneIndex := -k - 1
    for i, num := range nums {
        if num == 1 {
            if i - lastOneIndex <= k {
                return false
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
class Solution
    # @param {Integer[]} nums
    # @param {Integer} k
    # @return {Boolean}
    def k_length_apart(nums, k)
        last_one_index = -k - 1
        nums.each_with_index do |num, i|
            if num == 1
                if i - last_one_index <= k
                    return false
                end
                last_one_index = i
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
        var lastOneIndex: Int = -k - 1
        for (i <- nums.indices) {
            if (nums(i) == 1) {
                if (i - lastOneIndex <= k) {
                    return false
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
        let mut last_one_index: i32 = -k - 1;
        for (i, &num) in nums.iter().enumerate() {
            if num == 1 {
                if (i as i32) - last_one_index <= k {
                    return false;
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
(define (k-length-apart nums k)
  (let loop ((idx 0) (last-one-idx (- (+ k 1))))
    (cond
      [(>= idx (vector-length nums)) #true] ; Reached end, all good
      [(equal? (vector-ref nums idx) 1)
       (if (<= (- idx last-one-idx) k)
           #false ; Condition violated
           (loop (+ idx 1) idx))] ; Update last-one-idx and continue
      [else ; current element is 0
       (loop (+ idx 1) last-one-idx)]))) ; Continue with same last-one-idx
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
-export([k_length_apart/2]).

k_length_apart(Nums, K) ->
    k_length_apart(Nums, K, -K - 1, 0).

k_length_apart([], _K, _LastOneIndex, _Idx) ->
    true;

k_length_apart([H|T], K, LastOneIndex, Idx) when H == 1 ->
    case Idx - LastOneIndex =< K of
        true -> false;
        false -> k_length_apart(T, K, Idx, Idx + 1)
    end;

k_length_apart([_H|T], K, LastOneIndex, Idx) ->
    k_length_apart(T, K, LastOneIndex, Idx + 1).
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
  @spec k_length_apart(nums :: [integer], k :: integer) :: boolean
  def k_length_apart(nums, k) do
    do_k_length_apart(nums, k, -k - 1, 0)
  end

  defp do_k_length_apart([], _k, _last_one_index, _idx), do: true
  defp do_k_length_apart([1 | rest], k, last_one_index, idx) do
    if idx - last_one_index <= k do
      false
    else
      do_k_length_apart(rest, k, idx, idx + 1)
    end
  end
  defp do_k_length_apart([0 | rest], k, last_one_index, idx) do
    do_k_length_apart(rest, k, last_one_index, idx + 1)
  end
end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the length of the `nums` array. The algorithm iterates through the array exactly once, performing a constant number of operations (comparison, subtraction, assignment) for each element. Therefore, the execution time grows linearly with the size of the input array.

- **Space Complexity:** O(1). The algorithm uses a fixed number of auxiliary variables (`lastOneIndex`, loop counter `i`, `k`) regardless of the input array's size. No additional data structures are created that scale with N. Thus, the space complexity is constant.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-19 22:27:01)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires checking if all 1's in a binary array are at least k places away from each other. To solve this problem, we can use a simple iterative approach where we keep track of the position of the last seen 1 and check if the distance between the current 1 and the last seen 1 is at least k.

The problem-solving strategy involves iterating over the array and checking each element. If the current element is 1, we check if it is at least k places away from the last seen 1. If it is not, we return false. If it is, we update the position of the last seen 1.

The algorithm logic can be broken down into the following steps:
1. Initialize a variable to store the position of the last seen 1. This variable will be used to keep track of the position of the last seen 1.
2. Iterate over the array. For each element, check if it is 1.
3. If the current element is 1, check if it is at least k places away from the last seen 1. If it is not, return false.
4. If the current element is 1 and it is at least k places away from the last seen 1, update the position of the last seen 1.
5. If we have iterated over the entire array and have not returned false, return true.

This approach ensures that we check all 1's in the array and return false as soon as we find a pair of 1's that are not at least k places away from each other.

For example, if we have the array [1,0,0,0,1,0,0,1] and k = 2, we will return true because all 1's are at least 2 places away from each other. However, if we have the array [1,0,0,1,0,1] and k = 2, we will return false because the second 1 and the third 1 are only one apart from each other.

In terms of time complexity, this approach has a time complexity of O(n), where n is the length of the array. This is because we are iterating over the array once. The space complexity is O(1), which means the space required does not change with the size of the input array, making it very efficient.

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
// C++ solution
class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int lastSeen = -1;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 1) {
                if (lastSeen != -1 && i - lastSeen - 1 < k) {
                    return false;
                }
                lastSeen = i;
            }
        }
        return true;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
// Java solution
class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        int lastSeen = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                if (lastSeen != -1 && i - lastSeen - 1 < k) {
                    return false;
                }
                lastSeen = i;
            }
        }
        return true;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
# Python solution
class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        last_seen = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if last_seen != -1 and i - last_seen - 1 < k:
                    return False
                last_seen = i
        return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
# Python3 solution
class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        last_seen = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if last_seen != -1 and i - last_seen - 1 < k:
                    return False
                last_seen = i
        return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
// C solution
#include <stdbool.h>

bool kLengthApart(int* nums, int numsSize, int k) {
    int lastSeen = -1;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 1) {
            if (lastSeen != -1 && i - lastSeen - 1 < k) {
                return false;
            }
            lastSeen = i;
        }
    }
    return true;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
// C# solution
public class Solution {
    public bool KLengthApart(int[] nums, int k) {
        int lastSeen = -1;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 1) {
                if (lastSeen != -1 && i - lastSeen - 1 < k) {
                    return false;
                }
                lastSeen = i;
            }
        }
        return true;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
// JavaScript solution
var kLengthApart = function(nums, k) {
    let lastSeen = -1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] == 1) {
            if (lastSeen != -1 && i - lastSeen - 1 < k) {
                return false;
            }
            lastSeen = i;
        }
    }
    return true;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
// TypeScript solution
function kLengthApart(nums: number[], k: number): boolean {
    let lastSeen: number = -1;
    for (let i: number = 0; i < nums.length; i++) {
        if (nums[i] == 1) {
            if (lastSeen != -1 && i - lastSeen - 1 < k) {
                return false;
            }
            lastSeen = i;
        }
    }
    return true;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
// PHP solution
class Solution {
    function kLengthApart($nums, $k) {
        $lastSeen = -1;
        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] == 1) {
                if ($lastSeen != -1 && $i - $lastSeen - 1 < $k) {
                    return false;
                }
                $lastSeen = $i;
            }
        }
        return true;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
// Swift solution
class Solution {
    func kLengthApart(_ nums: [Int], _ k: Int) -> Bool {
        var lastSeen = -1
        for (i, num) in nums.enumerated() {
            if num == 1 {
                if lastSeen != -1 && i - lastSeen - 1 < k {
                    return false
                }
                lastSeen = i
            }
        }
        return true
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
// Kotlin solution
class Solution {
    fun kLengthApart(nums: IntArray, k: Int): Boolean {
        var lastSeen = -1
        for (i in nums.indices) {
            if (nums[i] == 1) {
                if (lastSeen != -1 && i - lastSeen - 1 < k) {
                    return false
                }
                lastSeen = i
            }
        }
        return true
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
// Dart solution
class Solution {
    bool kLengthApart(List<int> nums, int k) {
        int lastSeen = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                if (lastSeen != -1 && i - lastSeen - 1 < k) {
                    return false;
                }
                lastSeen = i;
            }
        }
        return true;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
// Go solution
func kLengthApart(nums []int, k int) bool {
    lastSeen := -1
    for i, num := range nums {
        if num == 1 {
            if lastSeen != -1 && i-lastSeen-1 < k {
                return false
            }
            lastSeen = i
        }
    }
    return true
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
# Ruby solution
def k_length_apart(nums, k)
    last_seen = -1
    nums.each_with_index do |num, i|
        if num == 1
            if last_seen != -1 && i - last_seen - 1 < k
                return false
            end
            last_seen = i
        end
    end
    true
end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
// Scala solution
object Solution {
    def kLengthApart(nums: Array[Int], k: Int): Boolean = {
        var lastSeen = -1
        for (i <- nums.indices) {
            if (nums(i) == 1) {
                if (lastSeen != -1 && i - lastSeen - 1 < k) {
                    return false
                }
                lastSeen = i
            }
        }
        true
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
// Rust solution
impl Solution {
    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
        let mut last_seen = -1;
        for (i, &num) in nums.iter().enumerate() {
            if num == 1 {
                if last_seen != -1 && i as i32 - last_seen - 1 < k {
                    return false;
                }
                last_seen = i as i32;
            }
        }
        true
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
# Racket solution
(define (k-length-apart nums k)
    (let loop ((nums nums) (last-seen -1))
        (cond
            ((null? nums) #t)
            ((= (car nums) 1)
                (if (and (not (= last-seen -1)) (< (- (length nums) last-seen) k))
                    #f
                    (loop (cdr nums) (length nums))))
            (else (loop (cdr nums) last-seen)))))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
% Erlang solution
-module(s).
-export([kLengthApart/2]).
kLengthApart([H|T], K) ->
    kLengthApart(H, T, K, -1).
kLengthApart(_, [], _, _) -> true;
kLengthApart(1, T, K, LastSeen) ->
    case LastSeen of
        -1 -> kLengthApart(1, T, K, length(T));
        _ ->
            case length(T) - LastSeen - 1 < K of
                true -> false;
                _ -> kLengthApart(1, T, K, length(T))
            end
    end;
kLengthApart(_, [H|T], K, LastSeen) -> kLengthApart(H, T, K, LastSeen).
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
# Elixir solution
defmodule Solution do
    def k_length_apart(nums, k) do
        k_length_apart(nums, k, -1)
    end

    defp k_length_apart([], _, _), do: true
    defp k_length_apart([1|t], k, last_seen) do
        if last_seen != -1 && length(t) - last_seen - 1 < k do
            false
        else
            k_length_apart(t, k, length(t))
        end
    end
    defp k_length_apart([_|t], k, last_seen), do: k_length_apart(t, k, last_seen)
end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the array, because we are iterating over the array once.

- **Space Complexity:** O(1) because the space required does not change with the size of the input array.

</div>
</details>
