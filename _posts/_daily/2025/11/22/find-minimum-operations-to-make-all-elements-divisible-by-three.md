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

<p>You are given an integer array <code>nums</code>. In one operation, you can add or subtract 1 from <strong>any</strong> element of <code>nums</code>.</p>

<p>Return the <strong>minimum</strong> number of operations to make all elements of <code>nums</code> divisible by 3.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>All array elements can be made divisible by 3 using 3 operations:</p>

<ul>
	<li>Subtract 1 from 1.</li>
	<li>Add 1 to 2.</li>
	<li>Subtract 1 from 4.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,6,9]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>


## Hints

1. If `x % 3 != 0` we can always increment or decrement `x` such that we only need 1 operation.

2. Add `min(nums[i] % 3, 3 - (nums[i] % 3))` to the count of operations.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-25 02:41:18 UTC)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the minimum number of operations to make all elements in an integer array `nums` divisible by 3. An operation consists of adding or subtracting 1 from any element.

Let's consider a single element `x` from the array. We want to make `x` divisible by 3 using the minimum number of operations. If `x` is already divisible by 3 (i.e., `x % 3 == 0`), then 0 operations are needed for this element. If `x` is not divisible by 3, its remainder when divided by 3 can be either 1 or 2.

If `x % 3 == 1`, we can subtract 1 from `x` to make it divisible by 3 (e.g., `4 -> 3`). This takes 1 operation. We could also add 2 to `x` (e.g., `4 -> 6`), which takes 2 operations. The minimum is 1. If `x % 3 == 2`, we can add 1 to `x` to make it divisible by 3 (e.g., `2 -> 3`). This takes 1 operation. We could also subtract 2 from `x` (e.g., `2 -> 0`), which takes 2 operations. The minimum is 1. In summary, any number not divisible by 3 requires exactly 1 operation to become divisible by 3.

Since operations on one element do not affect other elements, we can calculate the minimum operations for each element independently and sum them up. The overall strategy is to iterate through the `nums` array, and for each number, check if it is divisible by 3. If it is not, we increment a counter for the total operations. Finally, we return the accumulated count.

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
    int minimumOperations(std::vector<int>& nums) {
        int operations = 0;
        for (int num : nums) {
            if (num % 3 != 0) {
                operations++;
            }
        }
        return operations;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minimumOperations(int[] nums) {
        int operations = 0;
        for (int num : nums) {
            if (num % 3 != 0) {
                operations++;
            }
        }
        return operations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        operations = 0
        for num in nums:
            if num % 3 != 0:
                operations += 1
        return operations
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        operations = 0
        for num in nums:
            if num % 3 != 0:
                operations += 1
        return operations
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minimumOperations(int* nums, int numsSize) {
    int operations = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] % 3 != 0) {
            operations++;
        }
    }
    return operations;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinimumOperations(int[] nums) {
        int operations = 0;
        foreach (int num in nums) {
            if (num % 3 != 0) {
                operations++;
            }
        }
        return operations;
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
 * @return {number}
 */
var minimumOperations = function(nums) {
    let operations = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] % 3 !== 0) {
            operations++;
        }
    }
    return operations;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumOperations(nums: number[]): number {
    let operations: number = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] % 3 !== 0) {
            operations++;
        }
    }
    return operations;
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
     * @return Integer
     */
    function minimumOperations($nums) {
        $operations = 0;
        foreach ($nums as $num) {
            if ($num % 3 != 0) {
                $operations++;
            }
        }
        return $operations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        var operations = 0
        for num in nums {
            if num % 3 != 0 {
                operations += 1
            }
        }
        return operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumOperations(nums: IntArray): Int {
        var operations = 0
        for (num in nums) {
            if (num % 3 != 0) {
                operations++
            }
        }
        return operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumOperations(List<int> nums) {
    int operations = 0;
    for (int num in nums) {
      if (num % 3 != 0) {
        operations++;
      }
    }
    return operations;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumOperations(nums []int) int {
    operations := 0
    for _, num := range nums {
        if num % 3 != 0 {
            operations++
        }
    }
    return operations
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    # @param {Integer[]} nums
    # @return {Integer}
    def minimum_operations(nums)
        operations = 0
        nums.each do |num|
            if num % 3 != 0
                operations += 1
            end
        end
        operations
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumOperations(nums: Array[Int]): Int = {
        var operations = 0
        for (num <- nums) {
            if (num % 3 != 0) {
                operations += 1
            }
        }
        operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let mut operations = 0;
        for num in nums {
            if num % 3 != 0 {
                operations += 1;
            }
        }
        operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
(provide (contract-out [minimum-operations (-> (listof exact-integer?) exact-integer?)]))

(define (minimum-operations nums)
  (foldl (lambda (num acc)
           (if (= (modulo num 3) 0)
               acc
               (+ acc 1)))
         0
         nums))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_operations(Nums :: [integer()]) -> integer().
minimum_operations(Nums) ->
    lists:foldl(fun(Num, Acc) ->
                    case Num rem 3 of
                        0 -> Acc;
                        _ -> Acc + 1
                    end
                end, 0, Nums).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_operations(nums :: [integer]) :: integer
  def minimum_operations(nums) do
    Enum.reduce(nums, 0, fn num, acc ->
      if rem(num, 3) == 0 do
        acc
      else
        acc + 1
      end
    end)
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
  <small class="solution-timestamp">(2025-11-25 02:41:23 UTC)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires finding the minimum number of operations to make all elements of the given array divisible by 3. The approach involves iterating through each element in the array and calculating the minimum number of operations required to make it divisible by 3. This can be achieved by using the modulo operator to find the remainder of the element when divided by 3. If the remainder is not 0, we can either add or subtract the remainder from the element to make it divisible by 3. The minimum number of operations is the minimum of the remainder and 3 minus the remainder. We sum up these minimum operations for all elements to get the total minimum number of operations. 
The algorithm logic is straightforward and involves a single pass through the array, making it efficient for large inputs. 
The time complexity of this approach is O(n), where n is the number of elements in the array, because we are iterating through the array once. The space complexity is O(1), because we are not using any additional space that scales with the input size.

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
#include <vector>
#include <algorithm>

class Solution {
public:
    int minimumOperations(std::vector<int>& nums) {
        int operations = 0;
        for (int num : nums) {
            int remainder = num % 3;
            if (remainder != 0) {
                operations += std::min(remainder, 3 - remainder);
            }
        }
        return operations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;

public class Solution {
    public int minimumOperations(int[] nums) {
        int operations = 0;
        for (int num : nums) {
            int remainder = num % 3;
            if (remainder != 0) {
                operations += Math.min(remainder, 3 - remainder);
            }
        }
        return operations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        operations = 0
        for num in nums:
            remainder = num % 3
            if remainder != 0:
                operations += min(remainder, 3 - remainder)
        return operations
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        operations = 0
        for num in nums:
            remainder = num % 3
            if remainder != 0:
                operations += min(remainder, 3 - remainder)
        return operations
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>

int minimumOperations(int* nums, int numsSize) {
    int operations = 0;
    for (int i = 0; i < numsSize; i++) {
        int remainder = nums[i] % 3;
        if (remainder != 0) {
            operations += (remainder <= 3 - remainder) ? remainder : 3 - remainder;
        }
    }
    return operations;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int MinimumOperations(int[] nums) {
        int operations = 0;
        foreach (int num in nums) {
            int remainder = num % 3;
            if (remainder != 0) {
                operations += Math.Min(remainder, 3 - remainder);
            }
        }
        return operations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var minimumOperations = function(nums) {
    let operations = 0;
    for (let num of nums) {
        let remainder = num % 3;
        if (remainder != 0) {
            operations += Math.min(remainder, 3 - remainder);
        }
    }
    return operations;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumOperations(nums: number[]): number {
    let operations: number = 0;
    for (let num of nums) {
        let remainder: number = num % 3;
        if (remainder != 0) {
            operations += Math.min(remainder, 3 - remainder);
        }
    }
    return operations;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function minimumOperations($nums) {
        $operations = 0;
        foreach ($nums as $num) {
            $remainder = $num % 3;
            if ($remainder != 0) {
                $operations += min($remainder, 3 - $remainder);
            }
        }
        return $operations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        var operations: Int = 0
        for num in nums {
            let remainder = num % 3
            if remainder != 0 {
                operations += min(remainder, 3 - remainder)
            }
        }
        return operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumOperations(nums: IntArray): Int {
        var operations = 0
        for (num in nums) {
            val remainder = num % 3
            if (remainder != 0) {
                operations += minOf(remainder, 3 - remainder)
            }
        }
        return operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int minimumOperations(List<int> nums) {
        int operations = 0;
        for (int num in nums) {
            int remainder = num % 3;
            if (remainder != 0) {
                operations += remainder <= 3 - remainder ? remainder : 3 - remainder;
            }
        }
        return operations;
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

func minimumOperations(nums []int) int {
    operations := 0
    for _, num := range nums {
        remainder := num % 3
        if remainder != 0 {
            if remainder <= 3-remainder {
                operations += remainder
            } else {
                operations += 3 - remainder
            }
        }
    }
    return operations
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def minimum_operations(nums)
    operations = 0
    nums.each do |num|
        remainder = num % 3
        if remainder != 0
            operations += [remainder, 3 - remainder].min
        end
    end
    operations
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumOperations(nums: Array[Int]): Int = {
        nums.foldLeft(0) { case (operations, num) =>
            val remainder = num % 3
            if (remainder != 0) operations + remainder.min(3 - remainder)
            else operations
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let mut operations: i32 = 0;
        for num in nums {
            let remainder = num % 3;
            if remainder != 0 {
                operations += remainder.min(3 - remainder);
            }
        }
        operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
(define (minimum-operations nums)
    (let loop ((nums nums) (operations 0))
        (if (null? nums)
            operations
            (let ((remainder (modulo (car nums) 3)))
                (loop (cdr nums) (+ operations (if (zero? remainder) 0 (min remainder (- 3 remainder))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([minimum_operations/1]).

minimum_operations(Nums) ->
    lists:foldl(fun(X, Acc) ->
        Remainder = X rem 3,
        if Remainder =:= 0 -> Acc;
        true -> Acc + min(Remainder, 3 - Remainder)
        end
    end, 0, Nums).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def minimum_operations(nums) do
        Enum.reduce(nums, 0, fn num, acc ->
            remainder = rem(num, 3)
            if remainder != 0 do
                acc + min(remainder, 3 - remainder)
            else
                acc
            end
        end)
    end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the number of elements in the array, because we are iterating through the array once.

- **Space Complexity:** O(1) because we are not using any additional space that scales with the input size.

</div>
</details>
