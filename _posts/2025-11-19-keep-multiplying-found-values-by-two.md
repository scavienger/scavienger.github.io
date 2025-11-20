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

You are given an array of integers `nums`. You are also given an integer `original` which is the first number that needs to be searched for in `nums`.

You then do the following steps:

  1. If `original` is found in `nums`, **multiply** it by two (i.e., set `original = 2 * original`).
  2. Otherwise, **stop** the process.
  3. **Repeat** this process with the new number as long as you keep finding the number.

Return _the**final** value of _`original`.

**Example 1:**

``` Input: nums = [5,3,6,1,12], original = 3 Output: 24 Explanation: \- 3 is found in nums. 3 is multiplied by 2 to obtain 6. \- 6 is found in nums. 6 is multiplied by 2 to obtain 12. \- 12 is found in nums. 12 is multiplied by 2 to obtain 24. \- 24 is not found in nums. Thus, 24 is returned. ``` 

**Example 2:**

``` Input: nums = [2,7,9], original = 4 Output: 4 Explanation: \- 4 is not found in nums. Thus, 4 is returned. ``` 

**Constraints:**

  * `1 <= nums.length <= 1000`
  * `1 <= nums[i], original <= 1000`

## Hints

1. Repeatedly iterate through the array and check if the current value of original is in the array.

2. If original is not found, stop and return its current value.

3. Otherwise, multiply original by 2 and repeat the process.

4. Use set data structure to check the existence faster.

## ✨ AI-Generated Solution (gemini-2.5-flash)

### Approach

The problem asks us to start with an integer `original` and repeatedly check if this value exists within a given array `nums`. If it does, we double `original` and repeat the process. If `original` is not found in `nums`, we stop and return its current value.

To efficiently check for the existence of `original` in `nums` repeatedly, a crucial optimization is to convert the input array `nums` into a hash set (or a similar data structure like `HashSet` in Java/C#, `set` in Python, `unordered_set` in C++). A hash set allows for average O(1) time complexity for lookup operations, which is significantly faster than searching through an array, which would take O(N) time for each lookup. Given that we might perform multiple lookups, this optimization is very beneficial.

First, we initialize a hash set by iterating through the `nums` array and adding each element to the set. This step takes O(N) time on average, where N is the number of elements in `nums`. After the set is populated, we enter a `while` loop. The condition for this loop is whether the current `original` value is present in our hash set. As long as `original` is found in the set:
  1. We update `original` by multiplying it by two (`original = original * 2`).
  2. The loop then re-evaluates its condition with the new, doubled `original` value.

If `original` is not found in the hash set, the loop condition becomes false, and the loop terminates. At this point, the current value of `original` is the final value we need to return. The problem constraints state that `nums[i]` and `original` are at most 1000. This implies that once `original` exceeds 1000 (e.g., becomes 1024 after doubling), it can no longer be found in `nums`. Therefore, the `while` loop will execute a relatively small number of times (at most around `log2(2 * 1000)`, which is approximately 11 times if `original` starts at 1), making each lookup extremely fast and the overall process efficient.

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
    int findFinalValue(std::vector<int>& nums, int original) {
        std::unordered_set<int> num_set(nums.begin(), nums.end());
        
        while (num_set.count(original)) {
            original *= 2;
        }
        
        return original;
    }
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        num_set = set(nums)
        
        while original in num_set:
            original *= 2
            
        return original
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        num_set = set(nums)
        
        while original in num_set:
            original *= 2
            
        return original
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdbool.h>
#include <stdlib.h>

// For C, given there's no built-in hash set, and N is small (1000),
// a linear scan for each check is acceptable. The number of doublings is small (logK).
// Thus, O(N * logK) is okay.
int findFinalValue(int* nums, int numsSize, int original) {
    while (true) {
        bool found = false;
        for (int i = 0; i < numsSize; i++) {
            if (nums[i] == original) {
                found = true;
                break;
            }
        }

        if (found) {
            original *= 2;
        } else {
            break;
        }
    }
    return original;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
using System.Collections.Generic;

public class Solution {
    public int FindFinalValue(int[] nums, int original) {
        HashSet<int> numSet = new HashSet<int>(nums);
        
        while (numSet.Contains(original)) {
            original *= 2;
        }
        
        return original;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function findFinalValue(nums: number[], original: number): number {
    const numSet: Set<number> = new Set(nums);
    
    while (numSet.has(original)) {
        original *= 2;
    }
    
    return original;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $original
     * @return Integer
     */
    function findFinalValue($nums, $original) {
        // Using array_flip to create a hash map for O(1) average lookup
        // The keys will be the unique numbers from $nums, values can be anything (e.g., true).
        $numMap = array_flip($nums);
        
        while (isset($numMap[$original])) {
            $original *= 2;
        }
        
        return $original;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
class Solution {
  int findFinalValue(List<int> nums, int original) {
    final numSet = nums.toSet();
    
    while (numSet.contains(original)) {
      original *= 2;
    }
    
    return original;
  }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

func findFinalValue(nums []int, original int) int {
    numSet := make(map[int]struct{})
    for _, num := range nums {
        numSet[num] = struct{}{}
    }
    
    for {
        _, found := numSet[original]
        if found {
            original *= 2
        } else {
            break
        }
    }
    
    return original
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
require 'set'

# @param {Integer[]} nums
# @param {Integer} original
# @return {Integer}
def find_final_value(nums, original)
    num_set = nums.to_set
    
    while num_set.include?(original)
        original *= 2
    end
    
    return original
end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket

(define (find-final-value nums original)
  (define num-hash (make-hash))
  (for-each (lambda (n) (hash-set! num-hash n #t)) nums)

  (let loop ((current-original original))
    (if (hash-has-key? num-hash current-original)
        (loop (* current-original 2))
        current-original)))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
-export([find_final_value/2]).

find_final_value(Nums, Original) ->
    Set = sets:from_list(Nums),
    find_final_value_loop(Set, Original).

find_final_value_loop(Set, Original) ->
    case sets:is_element(Original, Set) of
        true ->
            find_final_value_loop(Set, Original * 2);
        false ->
            Original
    end.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
  @spec find_final_value(nums :: [integer], original :: integer) :: integer
  def find_final_value(nums, original) do
    num_set = MapSet.new(nums)
    
    find_final_value_loop(num_set, original)
  end

  defp find_final_value_loop(num_set, current_original) do
    if MapSet.member?(num_set, current_original) do
      find_final_value_loop(num_set, current_original * 2)
    else
      current_original
    end
  end
end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(N)
