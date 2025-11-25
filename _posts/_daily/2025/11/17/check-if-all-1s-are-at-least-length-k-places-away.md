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

<p>Given an binary array <code>nums</code> and an integer <code>k</code>, return <code>true</code><em> if all </em><code>1</code><em>&#39;s are at least </em><code>k</code><em> places away from each other, otherwise return </em><code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/15/sample_1_1791.png" style="width: 428px; height: 181px;" />
<pre>
<strong>Input:</strong> nums = [1,0,0,0,1,0,0,1], k = 2
<strong>Output:</strong> true
<strong>Explanation:</strong> Each of the 1s are at least 2 places away from each other.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/15/sample_2_1791.png" style="width: 320px; height: 173px;" />
<pre>
<strong>Input:</strong> nums = [1,0,0,1,0,1], k = 2
<strong>Output:</strong> false
<strong>Explanation:</strong> The second 1 and third 1 are only one apart from each other.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= nums.length</code></li>
	<li><code>nums[i]</code> is <code>0</code> or <code>1</code></li>
</ul>


## Hints

1. Each time you find a number 1, check whether or not it is K or more places away from the next one. If it's not, return false.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-25 04:05:19 UTC)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to determine if all '1's in a binary array `nums` are separated by at least `k` places. This means that if we find a '1' at index `i` and the next '1' is at index `j`, then the number of '0's between them, which is `j - i - 1`, must be greater than or equal to `k`. If this condition is violated for any pair of consecutive '1's, we should return `false`; otherwise, if we iterate through the entire array and find no such violation, we return `true`.

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
{% raw %}
class Solution {
public:
    bool kLengthApart(std::vector<int>& nums, int k) {
        int lastOneIndex = -1;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) {
                if (lastOneIndex != -1) {
                    // Calculate the number of zeros between the current '1' and the previous '1'.
                    // If the distance (i - lastOneIndex) is 1, there are 0 zeros.
                    // If the distance is 2, there is 1 zero, etc.
                    // So, number of zeros = (current_index - previous_index - 1).
                    if ((i - lastOneIndex - 1) < k) {
                        return false;
                    }
                }
                lastOneIndex = i;
            }
        }

        return true;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        int lastOneIndex = -1;
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) {
                if (lastOneIndex != -1) {
                    // Calculate the number of zeros between the current '1' and the previous '1'.
                    // If the distance (i - lastOneIndex) is 1, there are 0 zeros.
                    // If the distance is 2, there is 1 zero, etc.
                    // So, number of zeros = (current_index - previous_index - 1).
                    if ((i - lastOneIndex - 1) < k) {
                        return false;
                    }
                }
                lastOneIndex = i;
            }
        }

        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        last_one_index = -1
        n = len(nums)

        for i in range(n):
            if nums[i] == 1:
                if last_one_index != -1:
                    # Calculate the number of zeros between the current '1' and the previous '1'.
                    # If the distance (i - last_one_index) is 1, there are 0 zeros.
                    # If the distance is 2, there is 1 zero, etc.
                    # So, number of zeros = (current_index - previous_index - 1).
                    if (i - last_one_index - 1) < k:
                        return False
                last_one_index = i

        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        last_one_index = -1
        n = len(nums)

        for i in range(n):
            if nums[i] == 1:
                if last_one_index != -1:
                    # Calculate the number of zeros between the current '1' and the previous '1'.
                    # If the distance (i - last_one_index) is 1, there are 0 zeros.
                    # If the distance is 2, there is 1 zero, etc.
                    # So, number of zeros = (current_index - previous_index - 1).
                    if (i - last_one_index - 1) < k:
                        return False
                last_one_index = i

        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <stddef.h> // For size_t

bool kLengthApart(int* nums, int numsSize, int k) {
    int lastOneIndex = -1;

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 1) {
            if (lastOneIndex != -1) {
                // Calculate the number of zeros between the current '1' and the previous '1'.
                // If the distance (i - lastOneIndex) is 1, there are 0 zeros.
                // If the distance is 2, there is 1 zero, etc.
                // So, number of zeros = (current_index - previous_index - 1).
                if ((i - lastOneIndex - 1) < k) {
                    return false;
                }
            }
            lastOneIndex = i;
        }
    }

    return true;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool KLengthApart(int[] nums, int k) {
        int lastOneIndex = -1;
        int n = nums.Length;

        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) {
                if (lastOneIndex != -1) {
                    // Calculate the number of zeros between the current '1' and the previous '1'.
                    // If the distance (i - lastOneIndex) is 1, there are 0 zeros.
                    // If the distance is 2, there is 1 zero, etc.
                    // So, number of zeros = (current_index - previous_index - 1).
                    if ((i - lastOneIndex - 1) < k) {
                        return false;
                    }
                }
                lastOneIndex = i;
            }
        }

        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var kLengthApart = function(nums, k) {
    let lastOneIndex = -1;
    const n = nums.length;

    for (let i = 0; i < n; i++) {
        if (nums[i] === 1) {
            if (lastOneIndex !== -1) {
                // Calculate the number of zeros between the current '1' and the previous '1'.
                // If the distance (i - lastOneIndex) is 1, there are 0 zeros.
                // If the distance is 2, there is 1 zero, etc.
                // So, number of zeros = (current_index - previous_index - 1).
                if ((i - lastOneIndex - 1) < k) {
                    return false;
                }
            }
            lastOneIndex = i;
        }
    }

    return true;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function kLengthApart(nums: number[], k: number): boolean {
    let lastOneIndex: number = -1;
    const n: number = nums.length;

    for (let i = 0; i < n; i++) {
        if (nums[i] === 1) {
            if (lastOneIndex !== -1) {
                // Calculate the number of zeros between the current '1' and the previous '1'.
                // If the distance (i - lastOneIndex) is 1, there are 0 zeros.
                // If the distance is 2, there is 1 zero, etc.
                // So, number of zeros = (current_index - previous_index - 1).
                if ((i - lastOneIndex - 1) < k) {
                    return false;
                }
            }
            lastOneIndex = i;
        }
    }

    return true;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function kLengthApart($nums, $k) {
        $lastOneIndex = -1;
        $n = count($nums);

        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] === 1) {
                if ($lastOneIndex !== -1) {
                    // Calculate the number of zeros between the current '1' and the previous '1'.
                    // If the distance (i - $lastOneIndex) is 1, there are 0 zeros.
                    // If the distance is 2, there is 1 zero, etc.
                    // So, number of zeros = (current_index - previous_index - 1).
                    if (($i - $lastOneIndex - 1) < $k) {
                        return false;
                    }
                }
                $lastOneIndex = $i;
            }
        }

        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func kLengthApart(_ nums: [Int], _ k: Int) -> Bool {
        var lastOneIndex: Int = -1
        let n = nums.count

        for i in 0..<n {
            if nums[i] == 1 {
                if lastOneIndex != -1 {
                    // Calculate the number of zeros between the current '1' and the previous '1'.
                    // If the distance (i - lastOneIndex) is 1, there are 0 zeros.
                    // If the distance is 2, there is 1 zero, etc.
                    // So, number of zeros = (current_index - previous_index - 1).
                    if (i - lastOneIndex - 1) < k {
                        return false
                    }
                }
                lastOneIndex = i
            }
        }

        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun kLengthApart(nums: IntArray, k: Int): Boolean {
        var lastOneIndex = -1
        val n = nums.size

        for (i in 0 until n) {
            if (nums[i] == 1) {
                if (lastOneIndex != -1) {
                    // Calculate the number of zeros between the current '1' and the previous '1'.
                    // If the distance (i - lastOneIndex) is 1, there are 0 zeros.
                    // If the distance is 2, there is 1 zero, etc.
                    // So, number of zeros = (current_index - previous_index - 1).
                    if ((i - lastOneIndex - 1) < k) {
                        return false
                    }
                }
                lastOneIndex = i
            }
        }

        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool kLengthApart(List<int> nums, int k) {
    int lastOneIndex = -1;
    int n = nums.length;

    for (int i = 0; i < n; i++) {
      if (nums[i] == 1) {
        if (lastOneIndex != -1) {
          // Calculate the number of zeros between the current '1' and the previous '1'.
          // If the distance (i - lastOneIndex) is 1, there are 0 zeros.
          // If the distance is 2, there is 1 zero, etc.
          // So, number of zeros = (current_index - previous_index - 1).
          if ((i - lastOneIndex - 1) < k) {
            return false;
          }
        }
        lastOneIndex = i;
      }
    }

    return true;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

func kLengthApart(nums []int, k int) bool {
    lastOneIndex := -1
    n := len(nums)

    for i := 0; i < n; i++ {
        if nums[i] == 1 {
            if lastOneIndex != -1 {
                // Calculate the number of zeros between the current '1' and the previous '1'.
                // If the distance (i - lastOneIndex) is 1, there are 0 zeros.
                // If the distance is 2, there is 1 zero, etc.
                // So, number of zeros = (current_index - previous_index - 1).
                if (i - lastOneIndex - 1) < k {
                    return false
                }
            }
            lastOneIndex = i
        }
    }

    return true
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def k_length_apart(nums, k)
    last_one_index = -1
    n = nums.length

    (0...n).each do |i|
        if nums[i] == 1
            if last_one_index != -1
                # Calculate the number of zeros between the current '1' and the previous '1'.
                # If the distance (i - last_one_index) is 1, there are 0 zeros.
                # If the distance is 2, there is 1 zero, etc.
                # So, number of zeros = (current_index - previous_index - 1).
                if (i - last_one_index - 1) < k
                    return false
                end
            end
            last_one_index = i
        end
    end

    return true
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def kLengthApart(nums: Array[Int], k: Int): Boolean = {
        var lastOneIndex: Int = -1
        val n = nums.length

        for (i <- 0 until n) {
            if (nums(i) == 1) {
                if (lastOneIndex != -1) {
                    // Calculate the number of zeros between the current '1' and the previous '1'.
                    // If the distance (i - lastOneIndex) is 1, there are 0 zeros.
                    // If the distance is 2, there is 1 zero, etc.
                    // So, number of zeros = (current_index - previous_index - 1).
                    if ((i - lastOneIndex - 1) < k) {
                        return false
                    }
                }
                lastOneIndex = i
            }
        }

        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
        let mut last_one_index: i32 = -1;
        let n = nums.len() as i32;

        for i in 0..n {
            if nums[i as usize] == 1 {
                if last_one_index != -1 {
                    // Calculate the number of zeros between the current '1' and the previous '1'.
                    // If the distance (i - last_one_index) is 1, there are 0 zeros.
                    // If the distance is 2, there is 1 zero, etc.
                    // So, number of zeros = (current_index - previous_index - 1).
                    if (i - last_one_index - 1) < k {
                        return false;
                    }
                }
                last_one_index = i;
            }
        }

        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (k-length-apart nums k)
  (let loop ((i 0) (last-one-index -1))
    (cond
      ((= i (vector-length nums)) #t) ; Reached end, all good
      ((= (vector-ref nums i) 1)
       (if (and (not (= last-one-index -1))
                (< (- i last-one-index 1) k))
           #f ; Condition violated
           (loop (+ i 1) i))) ; Update last-one-index
      (else
       (loop (+ i 1) last-one-index))))) ; Continue with same last-one-index
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([k_length_apart/2]).

k_length_apart(Nums, K) ->
    k_length_apart_recursive(Nums, K, -1, 0, length(Nums)).

k_length_apart_recursive(_Nums, _K, _LastOneIndex, Index, N) when Index == N ->
    true;
k_length_apart_recursive(Nums, K, LastOneIndex, Index, N) ->
    case lists:nth(Index + 1, Nums) of % Erlang lists are 1-indexed for lists:nth
        1 ->
            if LastOneIndex =/= -1 ->
                % Calculate the number of zeros between the current '1' and the previous '1'.
                % So, number of zeros = (current_index - previous_index - 1).
                if (Index - LastOneIndex - 1) < K ->
                    false;
                true ->
                    k_length_apart_recursive(Nums, K, Index, Index + 1, N)
                end;
            true ->
                k_length_apart_recursive(Nums, K, Index, Index + 1, N)
            end;
        0 ->
            k_length_apart_recursive(Nums, K, LastOneIndex, Index + 1, N)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec k_length_apart(nums :: [integer], k :: integer) :: boolean
  def k_length_apart(nums, k) do
    do_k_length_apart(nums, k, -1, 0)
  end

  defp do_k_length_apart([], _k, _last_one_index, _current_index), do: true
  defp do_k_length_apart([head | tail], k, last_one_index, current_index) do
    if head == 1 do
      if last_one_index != -1 and (current_index - last_one_index - 1) < k do
        false
      else
        do_k_length_apart(tail, k, current_index, current_index + 1)
      end
    else
      do_k_length_apart(tail, k, last_one_index, current_index + 1)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) with detailed explanation

- **Space Complexity:** O(1) with detailed explanation

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-25 04:05:23 UTC)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by iterating through the given binary array and checking the distance between each pair of 1's. We can initialize a variable to store the index of the last seen 1. Then, we iterate through the array, and whenever we encounter a 1, we check if the distance between the current index and the last seen index is at least k. If it's not, we return false. If we finish iterating through the array without returning false, we return true. This approach ensures that all 1's are at least k places away from each other.

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
{% raw %}
class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int lastSeen = -1;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 1) {
                if (lastSeen != -1 && i - lastSeen <= k) {
                    return false;
                }
                lastSeen = i;
            }
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        int lastSeen = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                if (lastSeen != -1 && i - lastSeen <= k) {
                    return false;
                }
                lastSeen = i;
            }
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        last_seen = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if last_seen != -1 and i - last_seen <= k:
                    return False
                last_seen = i
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        last_seen = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if last_seen != -1 and i - last_seen <= k:
                    return False
                last_seen = i
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>

bool kLengthApart(int* nums, int numsSize, int k) {
    int lastSeen = -1;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 1) {
            if (lastSeen != -1 && i - lastSeen <= k) {
                return false;
            }
            lastSeen = i;
        }
    }
    return true;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool KLengthApart(int[] nums, int k) {
        int lastSeen = -1;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 1) {
                if (lastSeen != -1 && i - lastSeen <= k) {
                    return false;
                }
                lastSeen = i;
            }
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var kLengthApart = function(nums, k) {
    let lastSeen = -1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] == 1) {
            if (lastSeen != -1 && i - lastSeen <= k) {
                return false;
            }
            lastSeen = i;
        }
    }
    return true;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function kLengthApart(nums: number[], k: number): boolean {
    let lastSeen: number = -1;
    for (let i: number = 0; i < nums.length; i++) {
        if (nums[i] == 1) {
            if (lastSeen != -1 && i - lastSeen <= k) {
                return false;
            }
            lastSeen = i;
        }
    }
    return true;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function kLengthApart($nums, $k) {
        $lastSeen = -1;
        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] == 1) {
                if ($lastSeen != -1 && $i - $lastSeen <= $k) {
                    return false;
                }
                $lastSeen = $i;
            }
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func kLengthApart(_ nums: [Int], _ k: Int) -> Bool {
        var lastSeen = -1
        for (i, num) in nums.enumerated() {
            if num == 1 {
                if lastSeen != -1 && i - lastSeen <= k {
                    return false
                }
                lastSeen = i
            }
        }
        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun kLengthApart(nums: IntArray, k: Int): Boolean {
        var lastSeen = -1
        for (i in nums.indices) {
            if (nums[i] == 1) {
                if (lastSeen != -1 && i - lastSeen <= k) {
                    return false
                }
                lastSeen = i
            }
        }
        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    bool kLengthApart(List<int> nums, int k) {
        int lastSeen = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                if (lastSeen != -1 && i - lastSeen <= k) {
                    return false;
                }
                lastSeen = i;
            }
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import (
    "fmt"
)

func kLengthApart(nums []int, k int) bool {
    lastSeen := -1
    for i, num := range nums {
        if num == 1 {
            if lastSeen != -1 && i-lastSeen <= k {
                return false
            }
            lastSeen = i
        }
    }
    return true
}

func main() {
    nums := []int{1, 0, 0, 0, 1, 0, 0, 1}
    k := 2
    fmt.Println(kLengthApart(nums, k))
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def k_length_apart(nums, k)
    last_seen = -1
    nums.each_with_index do |num, i|
        if num == 1
            if last_seen != -1 && i - last_seen <= k
                return false
            end
            last_seen = i
        end
    end
    true
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def kLengthApart(nums: Array[Int], k: Int): Boolean = {
        var lastSeen = -1
        for (i <- nums.indices) {
            if (nums(i) == 1) {
                if (lastSeen != -1 && i - lastSeen <= k) {
                    return false
                }
                lastSeen = i
            }
        }
        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
        let mut last_seen = -1;
        for (i, &num) in nums.iter().enumerate() {
            if num == 1 {
                if last_seen != -1 && i as i32 - last_seen <= k {
                    return false;
                }
                last_seen = i as i32;
            }
        }
        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (k-length-apart nums k)
  (let loop ([nums nums] [last-seen -1])
    (cond
      [(null? nums) #t]
      [(= (car nums) 1)
       (if (and (not (= last-seen -1)) (<= (- (length nums) last-seen) k))
           #f
           (loop (cdr nums) (- (length nums))))]
      [else (loop (cdr nums) last-seen)])))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([k_length_apart/2]).

k_length_apart(Nums, K) ->
    k_length_apart(Nums, K, -1).

k_length_apart([1 | T], K, LastSeen) ->
    case LastSeen of
        -1 -> k_length_apart(T, K, 0);
        _ ->
            case length(T) - LastSeen =< K of
                true -> false;
                false -> k_length_apart(T, K, 0)
            end
    end;
k_length_apart([_ | T], K, LastSeen) ->
    k_length_apart(T, K, LastSeen);
k_length_apart([], _, _) ->
    true.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  def k_length_apart(nums, k) do
    k_length_apart(nums, k, -1)
  end

  defp k_length_apart([1 | t], k, last_seen) do
    case last_seen do
      -1 -> k_length_apart(t, k, 0)
      _ ->
        if length(t) - last_seen <= k do
          false
        else
          k_length_apart(t, k, 0)
        end
    end
  end

  defp k_length_apart([_ | t], k, last_seen) do
    k_length_apart(t, k, last_seen)
  end

  defp k_length_apart([], _, _) do
    true
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the input array, because we are doing a single pass through the array.

- **Space Complexity:** O(1) because we are using a constant amount of space to store the index of the last seen 1.

</div>
</details>
