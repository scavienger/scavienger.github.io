---
layout: post
title: "Keep Multiplying Found Values by Two"
date: 2025-11-19 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Hash Table", "Sorting", "Simulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/keep-multiplying-found-values-by-two/
---

## Problem #2154: Keep Multiplying Found Values by Two

**Difficulty:** Easy

**Topics:** Array, Hash Table, Sorting, Simulation

## Problem Description

<p>You are given an array of integers <code>nums</code>. You are also given an integer <code>original</code> which is the first number that needs to be searched for in <code>nums</code>.</p>

<p>You then do the following steps:</p>

<ol>
	<li>If <code>original</code> is found in <code>nums</code>, <strong>multiply</strong> it by two (i.e., set <code>original = 2 * original</code>).</li>
	<li>Otherwise, <strong>stop</strong> the process.</li>
	<li><strong>Repeat</strong> this process with the new number as long as you keep finding the number.</li>
</ol>

<p>Return <em>the <strong>final</strong> value of </em><code>original</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,3,6,1,12], original = 3
<strong>Output:</strong> 24
<strong>Explanation:</strong> 
- 3 is found in nums. 3 is multiplied by 2 to obtain 6.
- 6 is found in nums. 6 is multiplied by 2 to obtain 12.
- 12 is found in nums. 12 is multiplied by 2 to obtain 24.
- 24 is not found in nums. Thus, 24 is returned.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,9], original = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong>
- 4 is not found in nums. Thus, 4 is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i], original &lt;= 1000</code></li>
</ul>


## Hints

1. Repeatedly iterate through the array and check if the current value of original is in the array.

2. If original is not found, stop and return its current value.

3. Otherwise, multiply original by 2 and repeat the process.

4. Use set data structure to check the existence faster.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-20 22:20:40 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to simulate a process where we start with an `original` integer and repeatedly check if this value exists within a given array `nums`. If it does, we multiply `original` by two. We continue this process until the current `original` value is no longer found in `nums`, at which point we return its final value.

To efficiently check for the existence of `original` in `nums`, a crucial step is to optimize the lookup operation. A naive approach would be to iterate through `nums` in each step of the process, which would lead to a linear search (O(N) time) for every check. Given that `original` might be multiplied a few times, and `nums.length` can be up to 1000, this could result in O(k*N) complexity, where 'k' is the number of times `original` is doubled. While `k` is small (logarithmic with respect to the maximum possible value in `nums`, roughly 10-11 times as `original` will exceed 1000 quickly), a more optimal approach exists.

The most efficient way to check for element existence is by using a hash set (or a similar hash-based collection like `unordered_set` in C++, `HashSet` in Java, `Set` in Python, or a boolean array/frequency map for fixed small range integers). We first preprocess the `nums` array by inserting all its elements into a hash set. This operation typically takes O(N) time on average. Once the hash set is populated, checking if an element exists within it takes O(1) time on average.

The algorithm then proceeds as follows:
1.  **Preprocessing:** Convert the input array `nums` into a hash set. This set will allow for fast O(1) average-time lookups.
2.  **Iterative Doubling:** Enter a loop that continues as long as `original` is found in the hash set.
    a.  Inside the loop, check if the current value of `original` is present in the hash set.
    b.  If `original` is found, update `original` by multiplying it by two (`original = original * 2`).
    c.  If `original` is not found, exit the loop.
3.  **Return Value:** Once the loop terminates, the current value of `original` is the final value that was not found in `nums` (or its doubled sequence). Return this value.

For languages like C, which lack a built-in hash set and where `nums[i]` and `original` are constrained to a small positive range (1 to 1000), an even more performant alternative to a generic hash set is a boolean frequency array. An array `bool present[1001]` can be used, where `present[val]` is true if `val` exists in `nums`. This provides guaranteed O(1) lookups and O(N) initialization time, with O(Max_Val) space, which is very suitable here.

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
    int findFinalValue(std::vector<int>& nums, int original) {
        std::unordered_set<int> numSet(nums.begin(), nums.end());

        while (numSet.count(original)) {
            original *= 2;
        }

        return original;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int findFinalValue(int[] nums, int original) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }

        while (numSet.contains(original)) {
            original *= 2;
        }

        return original;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        num_set = set(nums)

        while original in num_set:
            original *= 2

        return original
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        num_set = set(nums)

        while original in num_set:
            original *= 2

        return original
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <stdlib.h>

// Note: This solution uses a boolean array for presence checking,
// which is efficient given the constraint nums[i], original <= 1000.
// It avoids complex data structures not standard in competitive C setups.

int findFinalValue(int* nums, int numsSize, int original) {
    // Max value constraint is 1000, so we need indices up to 1000.
    // A size of 1001 covers indices 0 to 1000.
    bool present[1001] = {false}; 

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] >= 1 && nums[i] <= 1000) {
            present[nums[i]] = true;
        }
    }

    while (original <= 1000 && present[original]) {
        original *= 2;
    }

    return original;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Collections.Generic;

public class Solution {
    public int FindFinalValue(int[] nums, int original) {
        HashSet<int> numSet = new HashSet<int>();
        foreach (int num in nums) {
            numSet.Add(num);
        }

        while (numSet.Contains(original)) {
            original *= 2;
        }

        return original;
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
 * @param {number} original
 * @return {number}
 */
var findFinalValue = function(nums, original) {
    const numSet = new Set(nums);

    while (numSet.has(original)) {
        original *= 2;
    }

    return original;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findFinalValue(nums: number[], original: number): number {
    const numSet: Set<number> = new Set(nums);

    while (numSet.has(original)) {
        original *= 2;
    }

    return original;
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
     * @param Integer $original
     * @return Integer
     */
    function findFinalValue($nums, $original) {
        // Using an associative array (hash map) for O(1) average lookup.
        // Flip values to keys for faster existence check with isset().
        $numMap = array_flip($nums);

        while (isset($numMap[$original])) {
            $original *= 2;
        }

        return $original;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {
    func findFinalValue(_ nums: [Int], _ original: Int) -> Int {
        var currentOriginal = original
        let numSet = Set(nums)

        while numSet.contains(currentOriginal) {
            currentOriginal *= 2
        }

        return currentOriginal
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun findFinalValue(nums: IntArray, original: Int): Int {
        var currentOriginal = original
        val numSet = nums.toSet()

        while (numSet.contains(currentOriginal)) {
            currentOriginal *= 2
        }

        return currentOriginal
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int findFinalValue(List<int> nums, int original) {
    final Set<int> numSet = nums.toSet();

    while (numSet.contains(original)) {
      original *= 2;
    }

    return original;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

func findFinalValue(nums []int, original int) int {
    numSet := make(map[int]bool)
    for _, num := range nums {
        numSet[num] = true
    }

    for numSet[original] {
        original *= 2
    }

    return original
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
  def find_final_value(nums, original)
    num_set = nums.to_set

    while num_set.include?(original)
      original *= 2
    end

    original
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def findFinalValue(nums: Array[Int], original: Int): Int = {
        var currentOriginal = original
        val numSet = nums.toSet

        while (numSet.contains(currentOriginal)) {
            currentOriginal *= 2
        }

        currentOriginal
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashSet;

impl Solution {
    pub fn find_final_value(nums: Vec<i32>, original: i32) -> i32 {
        let num_set: HashSet<i32> = nums.into_iter().collect();
        let mut current_original = original;

        while num_set.contains(&current_original) {
            current_original *= 2;
        }

        current_original
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
(define/contract (find-final-value nums original)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ([num-set (list->set nums)])
    (let loop ([current-original original])
      (if (set-member? num-set current-original)
          (loop (* current-original 2))
          current-original))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([find_final_value/2]).

find_final_value(Nums, Original) ->
    NumSet = sets:from_list(Nums),
    find_final_value_loop(NumSet, Original).

find_final_value_loop(NumSet, Original) ->
    case sets:is_element(Original, NumSet) of
        true ->
            find_final_value_loop(NumSet, Original * 2);
        false ->
            Original
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec find_final_value(nums :: [integer], original :: integer) :: integer
  def find_final_value(nums, original) do
    num_set = MapSet.new(nums)
    find_final_value_loop(num_set, original)
  end

  defp find_final_value_loop(num_set, original) do
    if MapSet.member?(num_set, original) do
      find_final_value_loop(num_set, original * 2)
    else
      original
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) on average. The initial step of converting `nums` into a hash set takes O(N) time, where N is `nums.length`. Each subsequent check for `original` in the hash set takes O(1) time on average. The loop for multiplying `original` runs at most `log2(MAX_VALUE)` times. Given that `original` starts at most 1000 and `nums[i]` are also at most 1000, `original` will exceed 1000 after roughly `log2(1000)` (approx. 10) doublings. So, the number of loop iterations (let's call it 'k') is very small, constant-like. Thus, the total time complexity is dominated by the O(N) hash set creation, making it O(N). For C solution using a boolean array, it's also O(N) for populating the boolean array.

- **Space Complexity:** O(N) on average. This space is primarily used to store the elements of `nums` in the hash set. In the worst case, all elements in `nums` are unique, requiring space proportional to N. For C solution using a boolean array, it's O(MAX_VALUE) where MAX_VALUE is 1000, which is effectively O(1) because 1000 is a constant, regardless of N.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-20 22:20:45 )</small>
</summary>

<div class="ai-solution-content">

### Approach


The problem requires us to find the final value of a given number 'original' after repeatedly multiplying it by 2 as long as it is found in the given array 'nums'. To solve this problem, we can follow these steps:

1. Initialize the variable 'original' with the given value.
2. Create a set from the given array 'nums' for efficient lookups.
3. Enter a loop where we check if 'original' is present in the set.
4. If 'original' is found, multiply it by 2 and continue the loop.
5. If 'original' is not found, break the loop and return the current value of 'original'.

This approach ensures that we keep multiplying 'original' by 2 as long as it is present in 'nums', and stop as soon as it is not found.

For example, if 'nums' is [5, 3, 6, 1, 12] and 'original' is 3, we will multiply 3 by 2 to get 6, then multiply 6 by 2 to get 12, and finally multiply 12 by 2 to get 24. Since 24 is not in 'nums', we will return 24 as the final value.

The time complexity of this approach is O(n) because in the worst case, we might need to multiply 'original' by 2 for each number in 'nums'. The space complexity is also O(n) because we are creating a set from 'nums' for efficient lookups.

We can implement this approach in various programming languages. Here are the implementations in 19 different languages:



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
    int findFinalValue(vector<int>& nums, int original) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        while (numSet.find(original) != numSet.end()) {
            original *= 2;
        }
        return original;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int findFinalValue(int[] nums, int original) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }
        while (numSet.contains(original)) {
            original *= 2;
        }
        return original;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_set = set(nums)
        while original in num_set:
            original *= 2
        return original
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_set = set(nums)
        while original in num_set:
            original *= 2
        return original
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>

int findFinalValue(int* nums, int numsSize, int original) {
    int* num_set = (int*)malloc(numsSize * sizeof(int));
    int num_set_size = 0;
    for (int i = 0; i < numsSize; i++) {
        int found = 0;
        for (int j = 0; j < num_set_size; j++) {
            if (num_set[j] == nums[i]) {
                found = 1;
                break;
            }
        }
        if (!found) {
            num_set[num_set_size++] = nums[i];
        }
    }
    while (1) {
        int found = 0;
        for (int i = 0; i < num_set_size; i++) {
            if (num_set[i] == original) {
                found = 1;
                break;
            }
        }
        if (!found) {
            break;
        }
        original *= 2;
    }
    free(num_set);
    return original;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int FindFinalValue(int[] nums, int original) {
        HashSet<int> numSet = new HashSet<int>(nums);
        while (numSet.Contains(original)) {
            original *= 2;
        }
        return original;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var findFinalValue = function(nums, original) {
    let numSet = new Set(nums);
    while (numSet.has(original)) {
        original *= 2;
    }
    return original;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findFinalValue(nums: number[], original: number): number {
    let numSet: Set<number> = new Set(nums);
    while (numSet.has(original)) {
        original *= 2;
    }
    return original;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function findFinalValue($nums, $original) {
        $numSet = array_unique($nums);
        while (in_array($original, $numSet)) {
            $original *= 2;
        }
        return $original;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func findFinalValue(_ nums: [Int], _ original: Int) -> Int {
        let numSet = Set(nums)
        var original = original
        while numSet.contains(original) {
            original *= 2
        }
        return original
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun findFinalValue(nums: IntArray, original: Int): Int {
        val numSet = nums.toSet()
        var original = original
        while (numSet.contains(original)) {
            original *= 2
        }
        return original
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int findFinalValue(List<int> nums, int original) {
        Set<int> numSet = Set.from(nums);
        while (numSet.contains(original)) {
            original *= 2;
        }
        return original;
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

func findFinalValue(nums []int, original int) int {
    numSet := make(map[int]bool)
    for _, num := range nums {
        numSet[num] = true
    }
    for numSet[original] {
        original *= 2
    }
    return original
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @param {Integer} original
# @return {Integer}
def find_final_value(nums, original)
    num_set = nums.to_set
    while num_set.include?(original)
        original *= 2
    end
    original
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def findFinalValue(nums: Array[Int], original: Int): Int = {
        val numSet = nums.toSet
        var originalVar = original
        while (numSet.contains(originalVar)) {
            originalVar *= 2
        }
        originalVar
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn find_final_value(nums: Vec<i32>, original: i32) -> i32 {
        let num_set: std::collections::HashSet<i32> = nums.into_iter().collect();
        let mut original = original;
        while num_set.contains(&original) {
            original *= 2;
        }
        original
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
(define (find-final-value nums original)
  (let loop ((original original))
    (if (member original nums)
        (loop (* original 2))
        original)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([findFinalValue/2]).

findFinalValue(Nums, Original) ->
    NumSet = sets:from_list(Nums),
    findFinalValue(NumSet, Original).

findFinalValue(NumSet, Original) ->
    case sets:is_element(Original, NumSet) of
        true ->
            findFinalValue(NumSet, Original * 2);
        false ->
            Original
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def findFinalValue(nums, original) do
        numSet = MapSet.new(nums)
        findFinalValue(numSet, original)
    end

    defp findFinalValue(numSet, original) do
        if MapSet.member?(numSet, original) do
            findFinalValue(numSet, original * 2)
        else
            original
        end
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the number of elements in the array 'nums'. This is because in the worst case, we might need to multiply 'original' by 2 for each number in 'nums'.

- **Space Complexity:** O(n) where n is the number of elements in the array 'nums'. This is because we are creating a set from 'nums' for efficient lookups.

</div>
</details>
