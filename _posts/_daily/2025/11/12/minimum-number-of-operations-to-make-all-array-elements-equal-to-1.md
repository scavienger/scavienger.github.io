---
layout: post
title: "Minimum Number of Operations to Make All Array Elements Equal to 1"
date: 2025-11-12 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Number Theory"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/
---

## Problem #2654: Minimum Number of Operations to Make All Array Elements Equal to 1

**Difficulty:** Medium

**Topics:** Array, Math, Number Theory

## Problem Description

<p>You are given a <strong>0-indexed</strong>&nbsp;array <code>nums</code> consisting of <strong>positive</strong> integers. You can do the following operation on the array <strong>any</strong> number of times:</p>

<ul>
	<li>Select an index <code>i</code> such that <code>0 &lt;= i &lt; n - 1</code> and replace either of&nbsp;<code>nums[i]</code> or <code>nums[i+1]</code> with their gcd value.</li>
</ul>

<p>Return <em>the <strong>minimum</strong> number of operations to make all elements of </em><code>nums</code><em> equal to </em><code>1</code>. If it is impossible, return <code>-1</code>.</p>

<p>The gcd of two integers is the greatest common divisor of the two integers.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,6,3,4]
<strong>Output:</strong> 4
<strong>Explanation:</strong> We can do the following operations:
- Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
- Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
- Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
- Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,10,6,14]
<strong>Output:</strong> -1
<strong>Explanation:</strong> It can be shown that it is impossible to make all the elements equal to 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## Hints

1. Note that if you have at least one occurrence of 1 in the array, then you can make all the other elements equal to 1 with one operation each.

2. Try finding the shortest subarray with a gcd equal to 1.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-23 00:16:11 )</small>
</summary>

<div class="ai-solution-content">

### Approach

First, count existing '1's. If any '1's are present, the minimum operations are `n - count_ones`. Otherwise, find the shortest subarray whose elements' greatest common divisor (GCD) is '1'. If such a subarray has length `L`, it takes `L-1` operations to make one of its elements '1'. Once a '1' is created, it takes `n-1` additional operations to make all other elements '1'. The total is `(L-1) + (n-1)`. If no subarray has a GCD of '1', it's impossible, return -1.

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
#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        int n = nums.size();

        int count_ones = 0;
        for (int x : nums) {
            if (x == 1) {
                count_ones++;
            }
        }

        if (count_ones > 0) {
            return n - count_ones;
        }

        int min_len_gcd_one = n + 1; 

        for (int i = 0; i < n; ++i) {
            int current_gcd = nums[i];
            for (int j = i + 1; j < n; ++j) {
                current_gcd = std::gcd(current_gcd, nums[j]);
                if (current_gcd == 1) {
                    min_len_gcd_one = std::min(min_len_gcd_one, j - i + 1);
                    break; 
                }
            }
        }

        if (min_len_gcd_one == n + 1) {
            return -1;
        }

        return (min_len_gcd_one - 1) + (n - 1);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.List;
import java.util.ArrayList;

class Solution {
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public int minOperations(int[] nums) {
        int n = nums.length;

        int count_ones = 0;
        for (int x : nums) {
            if (x == 1) {
                count_ones++;
            }
        }

        if (count_ones > 0) {
            return n - count_ones;
        }

        int min_len_gcd_one = n + 1; 

        for (int i = 0; i < n; ++i) {
            int current_gcd = nums[i];
            for (int j = i + 1; j < n; ++j) {
                current_gcd = gcd(current_gcd, nums[j]);
                if (current_gcd == 1) {
                    min_len_gcd_one = Math.min(min_len_gcd_one, j - i + 1);
                    break; 
                }
            }
        }

        if (min_len_gcd_one == n + 1) {
            return -1;
        }

        return (min_len_gcd_one - 1) + (n - 1);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import math

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        count_ones = nums.count(1)

        if count_ones > 0:
            return n - count_ones

        min_len_gcd_one = float('inf')

        for i in range(n):
            current_gcd = nums[i]
            for j in range(i + 1, n):
                current_gcd = math.gcd(current_gcd, nums[j])
                if current_gcd == 1:
                    min_len_gcd_one = min(min_len_gcd_one, j - i + 1)
                    break

        if min_len_gcd_one == float('inf'):
            return -1

        return (min_len_gcd_one - 1) + (n - 1)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import math

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        count_ones = nums.count(1)

        if count_ones > 0:
            return n - count_ones

        min_len_gcd_one = float('inf')

        for i in range(n):
            current_gcd = nums[i]
            for j in range(i + 1, n):
                current_gcd = math.gcd(current_gcd, nums[j])
                if current_gcd == 1:
                    min_len_gcd_one = min(min_len_gcd_one, j - i + 1)
                    break

        if min_len_gcd_one == float('inf'):
            return -1

        return (min_len_gcd_one - 1) + (n - 1)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int minOperations(int* nums, int numsSize) {
    int n = numsSize;

    int count_ones = 0;
    for (int i = 0; i < n; ++i) {
        if (nums[i] == 1) {
            count_ones++;
        }
    }

    if (count_ones > 0) {
        return n - count_ones;
    }

    int min_len_gcd_one = n + 1; 

    for (int i = 0; i < n; ++i) {
        int current_gcd = nums[i];
        for (int j = i + 1; j < n; ++j) {
            current_gcd = gcd(current_gcd, nums[j]);
            if (current_gcd == 1) {
                min_len_gcd_one = (min_len_gcd_one < (j - i + 1)) ? min_len_gcd_one : (j - i + 1);
                break; 
            }
        }
    }

    if (min_len_gcd_one == n + 1) {
        return -1;
    }

    return (min_len_gcd_one - 1) + (n - 1);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Linq;

public class Solution {
    private int Gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public int MinOperations(int[] nums) {
        int n = nums.Length;

        int countOnes = 0;
        foreach (int x in nums) {
            if (x == 1) {
                countOnes++;
            }
        }

        if (countOnes > 0) {
            return n - countOnes;
        }

        int minLenGcdOne = n + 1; 

        for (int i = 0; i < n; ++i) {
            int currentGcd = nums[i];
            for (int j = i + 1; j < n; ++j) {
                currentGcd = Gcd(currentGcd, nums[j]);
                if (currentGcd == 1) {
                    minLenGcdOne = Math.Min(minLenGcdOne, j - i + 1);
                    break; 
                }
            }
        }

        if (minLenGcdOne == n + 1) {
            return -1;
        }

        return (minLenGcdOne - 1) + (n - 1);
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
var minOperations = function(nums) {
    const n = nums.length;

    const gcd = (a, b) => {
        while (b !== 0) {
            let temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    let countOnes = 0;
    for (const x of nums) {
        if (x === 1) {
            countOnes++;
        }
    }

    if (countOnes > 0) {
        return n - countOnes;
    }

    let minLenGcdOne = n + 1; 

    for (let i = 0; i < n; ++i) {
        let currentGcd = nums[i];
        for (let j = i + 1; j < n; ++j) {
            currentGcd = gcd(currentGcd, nums[j]);
            if (currentGcd === 1) {
                minLenGcdOne = Math.min(minLenGcdOne, j - i + 1);
                break; 
            }
        }
    }

    if (minLenGcdOne === n + 1) {
        return -1;
    }

    return (minLenGcdOne - 1) + (n - 1);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minOperations(nums: number[]): number {
    const n = nums.length;

    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            let temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    let countOnes = 0;
    for (const x of nums) {
        if (x === 1) {
            countOnes++;
        }
    }

    if (countOnes > 0) {
        return n - countOnes;
    }

    let minLenGcdOne = n + 1; 

    for (let i = 0; i < n; ++i) {
        let currentGcd = nums[i];
        for (let j = i + 1; j < n; ++j) {
            currentGcd = gcd(currentGcd, nums[j]);
            if (currentGcd === 1) {
                minLenGcdOne = Math.min(minLenGcdOne, j - i + 1);
                break; 
            }
        }
    }

    if (minLenGcdOne === n + 1) {
        return -1;
    }

    return (minLenGcdOne - 1) + (n - 1);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {

    private function gcd(int $a, int $b): int {
        while ($b !== 0) {
            $temp = $b;
            $b = $a % $b;
            $a = $temp;
        }
        return $a;
    }

    /**
     * @param int[] $nums
     * @return int
     */
    function minOperations(array $nums): int {
        $n = count($nums);

        $countOnes = 0;
        foreach ($nums as $x) {
            if ($x === 1) {
                $countOnes++;
            }
        }

        if ($countOnes > 0) {
            return $n - $countOnes;
        }

        $minLenGcdOne = $n + 1; 

        for ($i = 0; $i < $n; ++$i) {
            $currentGcd = $nums[$i];
            for ($j = $i + 1; $j < $n; ++$j) {
                $currentGcd = $this->gcd($currentGcd, $nums[$j]);
                if ($currentGcd === 1) {
                    $minLenGcdOne = min($minLenGcdOne, $j - $i + 1);
                    break; 
                }
            }
        }

        if ($minLenGcdOne === $n + 1) {
            return -1;
        }

        return ($minLenGcdOne - 1) + ($n - 1);
    }
}
?>
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {
    private func gcd(_ a: Int, _ b: Int) -> Int {
        var a = a
        var b = b
        while b != 0 {
            let temp = b
            b = a % b
            a = temp
        }
        return a
    }

    func minOperations(_ nums: [Int]) -> Int {
        let n = nums.count

        var countOnes = 0
        for x in nums {
            if x == 1 {
                countOnes += 1
            }
        }

        if countOnes > 0 {
            return n - countOnes
        }

        var minLenGcdOne = n + 1 

        for i in 0..<n {
            var currentGcd = nums[i]
            for j in (i + 1)..<n {
                currentGcd = gcd(currentGcd, nums[j])
                if currentGcd == 1 {
                    minLenGcdOne = min(minLenGcdOne, j - i + 1)
                    break 
                }
            }
        }

        if minLenGcdOne == n + 1 {
            return -1
        }

        return (minLenGcdOne - 1) + (n - 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import kotlin.math.min

class Solution {
    private fun gcd(a: Int, b: Int): Int {
        var a = a
        var b = b
        while (b != 0) {
            val temp = b
            b = a % b
            a = temp
        }
        return a
    }

    fun minOperations(nums: IntArray): Int {
        val n = nums.size

        var countOnes = 0
        for (x in nums) {
            if (x == 1) {
                countOnes++
            }
        }

        if (countOnes > 0) {
            return n - countOnes
        }

        var minLenGcdOne = n + 1 

        for (i in 0 until n) {
            var currentGcd = nums[i]
            for (j in i + 1 until n) {
                currentGcd = gcd(currentGcd, nums[j])
                if (currentGcd == 1) {
                    minLenGcdOne = min(minLenGcdOne, j - i + 1)
                    break 
                }
            }
        }

        if (minLenGcdOne == n + 1) {
            return -1
        }

        return (minLenGcdOne - 1) + (n - 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:math';

class Solution {
  int _gcd(int a, int b) {
    while (b != 0) {
      int temp = b;
      b = a % b;
      a = temp;
    }
    return a;
  }

  int minOperations(List<int> nums) {
    final n = nums.length;

    int countOnes = 0;
    for (final x in nums) {
      if (x == 1) {
        countOnes++;
      }
    }

    if (countOnes > 0) {
      return n - countOnes;
    }

    int minLenGcdOne = n + 1; 

    for (int i = 0; i < n; ++i) {
      int currentGcd = nums[i];
      for (int j = i + 1; j < n; ++j) {
        currentGcd = _gcd(currentGcd, nums[j]);
        if (currentGcd == 1) {
          minLenGcdOne = min(minLenGcdOne, j - i + 1);
          break; 
        }
      }
    }

    if (minLenGcdOne == n + 1) {
      return -1;
    }

    return (minLenGcdOne - 1) + (n - 1);
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
	"math"
)

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func minOperations(nums []int) int {
    n := len(nums)

    countOnes := 0
    for _, x := range nums {
        if x == 1 {
            countOnes++
        }
    }

    if countOnes > 0 {
        return n - countOnes
    }

    minLenGcdOne := n + 1 

    for i := 0; i < n; i++ {
        currentGcd := nums[i]
        for j := i + 1; j < n; j++ {
            currentGcd = gcd(currentGcd, nums[j])
            if currentGcd == 1 {
                minLenGcdOne = int(math.Min(float64(minLenGcdOne), float64(j - i + 1)))
                break 
            }
        }
    }

    if minLenGcdOne == n + 1 {
        return -1
    }

    return (minLenGcdOne - 1) + (n - 1)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def min_operations(nums)
        n = nums.length

        count_ones = nums.count(1)

        if count_ones > 0
            return n - count_ones
        end

        min_len_gcd_one = n + 1 

        (0...n).each do |i|
            current_gcd = nums[i]
            (i + 1...n).each do |j|
                current_gcd = current_gcd.gcd(nums[j])
                if current_gcd == 1
                    min_len_gcd_one = [min_len_gcd_one, j - i + 1].min
                    break 
                end
            end
        end

        if min_len_gcd_one == n + 1
            return -1
        end

        return (min_len_gcd_one - 1) + (n - 1)
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.annotation.tailrec
import scala.math.min

object Solution {
    @tailrec
    private def gcd(a: Int, b: Int): Int = {
        if (b == 0) a
        else gcd(b, a % b)
    }

    def minOperations(nums: Array[Int]): Int = {
        val n = nums.length

        val countOnes = nums.count(_ == 1)

        if (countOnes > 0) {
            return n - countOnes
        }

        var minLenGcdOne = n + 1 

        for (i <- 0 until n) {
            var currentGcd = nums(i)
            for (j <- i + 1 until n) {
                currentGcd = gcd(currentGcd, nums(j))
                if (currentGcd == 1) {
                    minLenGcdOne = min(minLenGcdOne, j - i + 1)
                    break 
                }
            }
        }

        if (minLenGcdOne == n + 1) {
            return -1
        }

        (minLenGcdOne - 1) + (n - 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    fn gcd(mut a: i32, mut b: i32) -> i32 {
        while b != 0 {
            let temp = b;
            b = a % b;
            a = temp;
        }
        a
    }

    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;

        let mut count_ones = 0;
        for &x in nums.iter() {
            if x == 1 {
                count_ones += 1;
            }
        }

        if count_ones > 0 {
            return n - count_ones;
        }

        let mut min_len_gcd_one = n + 1; 

        for i in 0..n as usize {
            let mut current_gcd = nums[i];
            for j in (i + 1)..n as usize {
                current_gcd = Solution::gcd(current_gcd, nums[j]);
                if current_gcd == 1 {
                    min_len_gcd_one = std::cmp::min(min_len_gcd_one, (j - i + 1) as i32);
                    break; 
                }
            }
        }

        if min_len_gcd_one == n + 1 {
            return -1;
        }

        (min_len_gcd_one - 1) + (n - 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (min-operations nums)
  (define n (vector-length nums))

  (define (count-ones)
    (for/sum ([x (in-vector nums)])
      (if (= x 1) 1 0)))

  (define count-ones-val (count-ones))

  (if (> count-ones-val 0)
      (- n count-ones-val)
      (let ([actual-min-len-gcd-one
             (for/fold ([min-len (+ n 1)])
                       ([i (in-range n)])
               (let ([current-gcd-val (vector-ref nums i)])
                 (for/fold ([inner-min-len min-len])
                           ([j (in-range (+ i 1) n)] #:break (= current-gcd-val 1))
                   (set! current-gcd-val (gcd current-gcd-val (vector-ref nums j)))
                   (if (= current-gcd-val 1)
                       (min inner-min-len (+ (- j i) 1))
                       inner-min-len))))])

        (if (= actual-min-len-gcd-one (+ n 1))
            -1
            (+ (- actual-min-len-gcd-one 1) (- n 1))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([min_operations/1]).

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).

min_operations(Nums) ->
    N = length(Nums),

    CountOnes = lists:sum([1 || X <- Nums, X == 1]),

    if CountOnes > 0 ->
        N - CountOnes;
    true ->
        MinLenGcdOne = find_min_len_gcd_one(Nums, N),

        if MinLenGcdOne == N + 1 ->
            -1;
        true ->
            (MinLenGcdOne - 1) + (N - 1)
        end
    end.

find_min_len_gcd_one(Nums, N) ->
    find_min_len_gcd_one_outer(0, N, Nums, N + 1).

find_min_len_gcd_one_outer(I, N, Nums, AccMinLen) when I < N ->
    CurrentGcd = lists:nth(I + 1, Nums), % Nth is 1-indexed
    MinLenForI = find_min_len_gcd_one_inner(I + 1, N, Nums, CurrentGcd, I),
    find_min_len_gcd_one_outer(I + 1, N, Nums, min(AccMinLen, MinLenForI));
find_min_len_gcd_one_outer(_, _, _, AccMinLen) ->
    AccMinLen.

find_min_len_gcd_one_inner(J, N, Nums, CurrentGcd, I) when J < N ->
    NewGcd = gcd(CurrentGcd, lists:nth(J + 1, Nums)),
    if NewGcd == 1 ->
        J - I + 1; % Found 1, this is the shortest for this I, return it
    true ->
        find_min_len_gcd_one_inner(J + 1, N, Nums, NewGcd, I)
    end;
find_min_len_gcd_one_inner(_, _, _, _, _) ->
    N + 1. % No GCD 1 found for this I
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  defp gcd(a, 0), do: a
  defp gcd(a, b), do: gcd(b, rem(a, b))

  def min_operations(nums) do
    n = length(nums)

    count_ones = Enum.count(nums, fn x -> x == 1 end)

    if count_ones > 0 do
      n - count_ones
    else
      min_len_gcd_one = find_min_len_gcd_one(nums, n)

      if min_len_gcd_one == n + 1 do
        -1
      else
        (min_len_gcd_one - 1) + (n - 1)
      end
    end
  end

  defp find_min_len_gcd_one(nums, n) do
    find_min_len_gcd_one_outer(0, n, nums, n + 1)
  end

  defp find_min_len_gcd_one_outer(i, n, nums, acc_min_len) when i < n do
    current_gcd = Enum.at(nums, i)
    min_len_for_i = find_min_len_gcd_one_inner(i + 1, n, nums, current_gcd, i)
    find_min_len_gcd_one_outer(i + 1, n, nums, min(acc_min_len, min_len_for_i))
  end
  defp find_min_len_gcd_one_outer(_i, _n, _nums, acc_min_len), do: acc_min_len

  defp find_min_len_gcd_one_inner(j, n, nums, current_gcd, i) when j < n do
    new_gcd = gcd(current_gcd, Enum.at(nums, j))
    if new_gcd == 1 do
      j - i + 1 # Found 1, this is the shortest for this I, return it
    else
      find_min_len_gcd_one_inner(j + 1, n, nums, new_gcd, i)
    end
  end
  defp find_min_len_gcd_one_inner(_j, _n, _nums, _current_gcd, _i), do: n + 1 # No GCD 1 found for this I
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N^2 * log(max_val))

- **Space Complexity:** O(1)

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-23 00:16:27 )</small>
</summary>

<div class="ai-solution-content">

### Approach

No approach provided

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
// Generation failed for C++
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Generation failed for C#
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Generation failed for JavaScript
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
// Generation failed for TypeScript
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
// Generation failed for PHP
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
// Generation failed for Swift
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
// Generation failed for Kotlin
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
// Generation failed for Dart
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
// Generation failed for Go
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
// Generation failed for Ruby
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
// Generation failed for Scala
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
// Generation failed for Rust
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
// Generation failed for Racket
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
// Generation failed for Erlang
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
// Generation failed for Elixir
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** N/A

- **Space Complexity:** N/A

</div>
</details>
