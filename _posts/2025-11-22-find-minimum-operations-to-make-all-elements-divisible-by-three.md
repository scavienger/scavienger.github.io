---
layout: post
title: "Find Minimum Operations to Make All Elements Divisible by Three"
date: 2025-11-22 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Math"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
---

## Problem #3190: Find Minimum Operations to Make All Elements Divisible by Three

**Difficulty:** Easy

**Topics:** Array, Math

## Problem Description

You are given an integer array `nums`. In one operation, you can add or subtract 1 from **any** element of `nums`.

Return the **minimum** number of operations to make all elements of `nums` divisible by 3.

**Example 1:**

**Input:** nums = [1,2,3,4]

**Output:** 3

**Explanation:**

All array elements can be made divisible by 3 using 3 operations:

  * Subtract 1 from 1.
  * Add 1 to 2.
  * Subtract 1 from 4.

**Example 2:**

**Input:** nums = [3,6,9]

**Output:** 0

**Constraints:**

  * `1 <= nums.length <= 50`
  * `1 <= nums[i] <= 50`

## Hints

1. If `x % 3 != 0` we can always increment or decrement `x` such that we only need 1 operation.

2. Add `min(nums[i] % 3, 3 - (num[i] % 3))` to the count of operations.

## ✨ AI-Generated Solution (gemini-2.5-flash)

### Approach

The problem asks for the minimum number of operations to make all elements in an integer array `nums` divisible by 3. An operation consists of adding or subtracting 1 from any element. The key insight to solving this problem efficiently lies in determining the minimum operations for a single element to become divisible by 3, and then extending this logic to the entire array.

Let's consider an arbitrary element `x` from the `nums` array. We want to find the minimum number of operations to transform `x` into a number `y` such that `y` is divisible by 3 (i.e., `y % 3 == 0`). The number of operations is simply the absolute difference `|x - y|`. Since we want to minimize this difference, we should look for the closest multiple of 3 to `x`. There are two multiples of 3 that are closest to `x`: one that is less than or equal to `x`, and one that is greater than or equal to `x`. For example, if `x` is 4, the closest multiples of 3 are 3 and 6. If `x` is 5, they are 3 and 6. If `x` is 6, they are 6 itself.

We can analyze the number of operations needed for a single element `x` based on its remainder when divided by 3 (`x % 3`): 
1.  **If `x % 3 == 0`**: `x` is already divisible by 3. No operations are needed. The cost is 0.
2.  **If `x % 3 == 1`**: `x` is one more than a multiple of 3 (e.g., 1, 4, 7). To make it divisible by 3, we can either subtract 1 (e.g., `4 -> 3`), which takes 1 operation, or add 2 (e.g., `4 -> 6`), which takes 2 operations. The minimum is 1 operation.
3.  **If `x % 3 == 2`**: `x` is two more than a multiple of 3 (e.g., 2, 5, 8). To make it divisible by 3, we can either add 1 (e.g., `5 -> 6`), which takes 1 operation, or subtract 2 (e.g., `5 -> 3`), which takes 2 operations. The minimum is 1 operation.

Observing these cases, we can derive a general formula. The remainder `r = x % 3`. The operations needed are `r` (to subtract `r` and reach the previous multiple of 3) or `3 - r` (to add `3 - r` and reach the next multiple of 3). The minimum operations for `x` is `min(r, 3 - r)`. Let's test this formula: 
*   If `r = 0`: `min(0, 3 - 0) = min(0, 3) = 0`. Correct.
*   If `r = 1`: `min(1, 3 - 1) = min(1, 2) = 1`. Correct.
*   If `r = 2`: `min(2, 3 - 2) = min(2, 1) = 1`. Correct.
This formula elegantly covers all cases.

The overall strategy is straightforward: since operations on one element do not affect other elements in the array, the total minimum operations to make all elements divisible by 3 is simply the sum of the minimum operations required for each individual element. This is a greedy approach, and it works because the decision for each element is independent. We iterate through the array, calculate the minimum operations for each number using the `min(remainder, 3 - remainder)` formula, and accumulate these operations in a total counter. Finally, we return the accumulated total.

Let's walk through Example 1: `nums = [1, 2, 3, 4]`
1. Initialize `total_operations = 0`.
2. For `num = 1`: `remainder = 1 % 3 = 1`. Operations needed = `min(1, 3 - 1) = min(1, 2) = 1`. `total_operations = 0 + 1 = 1`.
3. For `num = 2`: `remainder = 2 % 3 = 2`. Operations needed = `min(2, 3 - 2) = min(2, 1) = 1`. `total_operations = 1 + 1 = 2`.
4. For `num = 3`: `remainder = 3 % 3 = 0`. Operations needed = `min(0, 3 - 0) = min(0, 3) = 0`. `total_operations = 2 + 0 = 2`.
5. For `num = 4`: `remainder = 4 % 3 = 1`. Operations needed = `min(1, 3 - 1) = min(1, 2) = 1`. `total_operations = 2 + 1 = 3`.
After iterating through all elements, the final `total_operations` is 3, which matches the example output.

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
    int minimumOperations(std::vector<int>& nums) {
        int operations = 0;
        for (int num : nums) {
            int remainder = num % 3;
            operations += std::min(remainder, 3 - remainder);
        }
        return operations;
    }
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
import java.util.List;
import java.lang.Math;

class Solution {
    public int minimumOperations(List<Integer> nums) {
        int operations = 0;
        for (int num : nums) {
            int remainder = num % 3;
            operations += Math.min(remainder, 3 - remainder);
        }
        return operations;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
import math

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        for num in nums:
            remainder = num % 3
            operations += min(remainder, 3 - remainder)
        return operations
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
import math

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        for num in nums:
            remainder = num % 3
            operations += min(remainder, 3 - remainder)
        return operations
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdio.h>
#include <stdlib.h> // Required for min function if custom one not used

// Custom min function for integers, as math.h min works with doubles
int min_int(int a, int b) {
    return (a < b) ? a : b;
}

int minimumOperations(int* nums, int numsSize) {
    int operations = 0;
    for (int i = 0; i < numsSize; i++) {
        int num = nums[i];
        int remainder = num % 3;
        operations += min_int(remainder, 3 - remainder);
    }
    return operations;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumOperations(IList<int> nums) {
        int operations = 0;
        foreach (int num in nums) {
            int remainder = num % 3;
            operations += Math.Min(remainder, 3 - remainder);
        }
        return operations;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function(nums) {
    let operations = 0;
    for (const num of nums) {
        const remainder = num % 3;
        operations += Math.min(remainder, 3 - remainder);
    }
    return operations;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function minimumOperations(nums: number[]): number {
    let operations: number = 0;
    for (const num of nums) {
        const remainder: number = num % 3;
        operations += Math.min(remainder, 3 - remainder);
    }
    return operations;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
<?php

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumOperations($nums) {
        $operations = 0;
        foreach ($nums as $num) {
            $remainder = $num % 3;
            $operations += min($remainder, 3 - $remainder);
        }
        return $operations;
    }
}

?>
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
import Foundation

class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        var operations = 0
        for num in nums {
            let remainder = num % 3
            operations += min(remainder, 3 - remainder)
        }
        return operations
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution {
    fun minimumOperations(nums: List<Int>): Int {
        var operations = 0
        for (num in nums) {
            val remainder = num % 3
            operations += minOf(remainder, 3 - remainder)
        }
        return operations
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
import 'dart:math';

class Solution {
  int minimumOperations(List<int> nums) {
    int operations = 0;
    for (int num in nums) {
      int remainder = num % 3;
      operations += min(remainder, 3 - remainder);
    }
    return operations;
  }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

import (
	"math"
)

func minimumOperations(nums []int) int {
    operations := 0
    for _, num := range nums {
        remainder := num % 3
        operations += int(math.Min(float64(remainder), float64(3 - remainder)))
    }
    return operations
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
    operations = 0
    nums.each do |num|
        remainder = num % 3
        operations += [remainder, 3 - remainder].min
    end
    operations
end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {
    def minimumOperations(nums: List[Int]): Int = {
        var operations = 0
        for (num <- nums) {
            val remainder = num % 3
            operations += Math.min(remainder, 3 - remainder)
        }
        operations
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let mut operations = 0;
        for num in nums {
            let remainder = num % 3;
            operations += std::cmp::min(remainder, 3 - remainder);
        }
        operations
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket

(define (minimum-operations nums)
  (define operations 0)
  (for ([num nums])
    (define remainder (modulo num 3))
    (set! operations (+ operations (min remainder (- 3 remainder)))))
  operations)

(provide (rename-out [minimum-operations minimumOperations]))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-spec minimum_operations(Nums :: [integer()]) -> integer().
minimum_operations(Nums) ->
    lists:foldl(fun(Num, Acc) ->
        Remainder = Num rem 3,
        Acc + min(Remainder, 3 - Remainder)
    end, 0, Nums).
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
  @spec minimum_operations(nums :: [integer]) :: integer
  def minimum_operations(nums) do
    Enum.reduce(nums, 0, fn num, acc ->
      remainder = rem(num, 3)
      acc + min(remainder, 3 - remainder)
    end)
  end
end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)
