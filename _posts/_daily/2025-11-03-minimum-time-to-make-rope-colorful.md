---
layout: post
title: "Minimum Time to Make Rope Colorful"
date: 2025-11-03 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "String", "Dynamic Programming", "Greedy"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
---

## Problem #1578: Minimum Time to Make Rope Colorful

**Difficulty:** Medium

**Topics:** Array, String, Dynamic Programming, Greedy

## Problem Description

<p>Alice has <code>n</code> balloons arranged on a rope. You are given a <strong>0-indexed</strong> string <code>colors</code> where <code>colors[i]</code> is the color of the <code>i<sup>th</sup></code> balloon.</p>

<p>Alice wants the rope to be <strong>colorful</strong>. She does not want <strong>two consecutive balloons</strong> to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it <strong>colorful</strong>. You are given a <strong>0-indexed</strong> integer array <code>neededTime</code> where <code>neededTime[i]</code> is the time (in seconds) that Bob needs to remove the <code>i<sup>th</sup></code> balloon from the rope.</p>

<p>Return <em>the <strong>minimum time</strong> Bob needs to make the rope <strong>colorful</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/13/ballon1.jpg" style="width: 404px; height: 243px;" />
<pre>
<strong>Input:</strong> colors = &quot;abaac&quot;, neededTime = [1,2,3,4,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> In the above image, &#39;a&#39; is blue, &#39;b&#39; is red, and &#39;c&#39; is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/13/balloon2.jpg" style="width: 244px; height: 243px;" />
<pre>
<strong>Input:</strong> colors = &quot;abc&quot;, neededTime = [1,2,3]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The rope is already colorful. Bob does not need to remove any balloons from the rope.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/13/balloon3.jpg" style="width: 404px; height: 243px;" />
<pre>
<strong>Input:</strong> colors = &quot;aabaa&quot;, neededTime = [1,2,3,4,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Bob will remove the balloons at indices 0 and 4. Each balloons takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == colors.length == neededTime.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= neededTime[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>colors</code> contains only lowercase English letters.</li>
</ul>


## Hints

1. Maintain the running sum and max value for repeated letters.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-20 00:19:45)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to find the minimum time needed to make a rope 'colorful', meaning no two consecutive balloons have the same color. We are given the colors of `n` balloons and the time required to remove each balloon. If there are consecutive balloons of the same color, we must remove some of them until no two identical balloons are adjacent.

Consider a sequence of consecutive balloons of the same color, for example, `A A A` with removal times `t1, t2, t3`. To break this sequence and ensure no two 'A's are consecutive, we must remove at least `k-1` balloons if there are `k` identical consecutive balloons. For `A A A`, we must remove two 'A's, leaving only one. To minimize the total removal time for this block, we should always keep the balloon with the *highest* removal time within that block and remove all the others. The cost for this block would then be the sum of removal times for all balloons in the block minus the maximum removal time in that block.

This greedy strategy works because the decision for one block of identical balloons does not affect the optimal decision for another separate block of identical balloons. If we have `A A B C C C`, the optimal removals for `A A` are independent of the optimal removals for `C C C`. Our goal is to minimize the total time, so for each block of identical consecutive balloons, we apply this local optimum.

We can implement this strategy with a single pass through the `colors` string and `neededTime` array. We iterate through the balloons, keeping track of the maximum removal time encountered in the *current* consecutive block of identical colors. When we encounter a balloon `colors[i]` that is the same color as `colors[i-1]`, we know we have a conflict. We must remove one of these two. To minimize cost, we remove the one with the smaller `neededTime` between `neededTime[i]` and the `current_block_max_time` (which represents the cost of the balloon we've decided to keep from the previous elements of this same-colored block). We add this minimum cost to our `total_min_cost`. Then, we update `current_block_max_time` to be the maximum of the two times, because the balloon with the higher removal time is the one we effectively 'keep' to potentially face future conflicts within the same block.

If `colors[i]` is different from `colors[i-1]`, it signifies the start of a new block of colors. In this case, there's no immediate conflict with `colors[i-1]`, so we reset `current_block_max_time` to `neededTime[i]`, as this balloon is now the first (and currently only) balloon in its new block.

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
#include <string>
#include <vector>
#include <algorithm> // For std::min and std::max

class Solution {
public:
    int minCost(std::string colors, std::vector<int>& neededTime) {
        int n = colors.length();
        if (n < 2) {
            return 0;
        }

        int totalMinCost = 0;
        // currentBlockMaxTime stores the max cost of the balloon kept in the current consecutive block
        int currentBlockMaxTime = neededTime[0];

        // Iterate from the second balloon
        for (int i = 1; i < n; ++i) {
            // If the current balloon has the same color as the previous one
            if (colors[i] == colors[i-1]) {
                // We must remove one. Add the minimum of the two costs to totalMinCost.
                // currentBlockMaxTime already holds the maximum of previous elements in this block.
                totalMinCost += std::min(currentBlockMaxTime, neededTime[i]);
                // Update currentBlockMaxTime to keep the maximum cost balloon in the block.
                currentBlockMaxTime = std::max(currentBlockMaxTime, neededTime[i]);
            } else {
                // If colors are different, it's a new block. Reset currentBlockMaxTime.
                currentBlockMaxTime = neededTime[i];
            }
        }

        return totalMinCost;
    }
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
    public int minCost(String colors, int[] neededTime) {
        int n = colors.length();
        if (n < 2) {
            return 0;
        }

        int totalMinCost = 0;
        // currentBlockMaxTime stores the max cost of the balloon kept in the current consecutive block
        int currentBlockMaxTime = neededTime[0];

        // Iterate from the second balloon
        for (int i = 1; i < n; i++) {
            // If the current balloon has the same color as the previous one
            if (colors.charAt(i) == colors.charAt(i - 1)) {
                // We must remove one. Add the minimum of the two costs to totalMinCost.
                // currentBlockMaxTime already holds the maximum of previous elements in this block.
                totalMinCost += Math.min(currentBlockMaxTime, neededTime[i]);
                // Update currentBlockMaxTime to keep the maximum cost balloon in the block.
                currentBlockMaxTime = Math.max(currentBlockMaxTime, neededTime[i]);
            } else {
                // If colors are different, it's a new block. Reset currentBlockMaxTime.
                currentBlockMaxTime = neededTime[i];
            }
        }

        return totalMinCost;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        if n < 2:
            return 0

        total_min_cost = 0
        # current_block_max_time stores the max cost of the balloon kept in the current consecutive block
        current_block_max_time = neededTime[0]

        # Iterate from the second balloon
        for i in range(1, n):
            # If the current balloon has the same color as the previous one
            if colors[i] == colors[i-1]:
                # We must remove one. Add the minimum of the two costs to total_min_cost.
                # current_block_max_time already holds the maximum of previous elements in this block.
                total_min_cost += min(current_block_max_time, neededTime[i])
                # Update current_block_max_time to keep the maximum cost balloon in the block.
                current_block_max_time = max(current_block_max_time, neededTime[i])
            else:
                # If colors are different, it's a new block. Reset current_block_max_time.
                current_block_max_time = neededTime[i]

        return total_min_cost
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        if n < 2:
            return 0

        total_min_cost = 0
        # current_block_max_time stores the max cost of the balloon kept in the current consecutive block
        current_block_max_time = neededTime[0]

        # Iterate from the second balloon
        for i in range(1, n):
            # If the current balloon has the same color as the previous one
            if colors[i] == colors[i-1]:
                # We must remove one. Add the minimum of the two costs to total_min_cost.
                # current_block_max_time already holds the maximum of previous elements in this block.
                total_min_cost += min(current_block_max_time, neededTime[i])
                # Update current_block_max_time to keep the maximum cost balloon in the block.
                current_block_max_time = max(current_block_max_time, neededTime[i])
            else:
                # If colors are different, it's a new block. Reset current_block_max_time.
                current_block_max_time = neededTime[i]

        return total_min_cost
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <string.h> // For strlen

// Custom min/max functions for integers
int min(int a, int b) {
    return (a < b) ? a : b;
}

int max(int a, int b) {
    return (a > b) ? a : b;
}

int minCost(char * colors, int* neededTime, int neededTimeSize) {
    int n = neededTimeSize;
    if (n < 2) {
        return 0;
    }

    int totalMinCost = 0;
    // currentBlockMaxTime stores the max cost of the balloon kept in the current consecutive block
    int currentBlockMaxTime = neededTime[0];

    // Iterate from the second balloon
    for (int i = 1; i < n; i++) {
        // If the current balloon has the same color as the previous one
        if (colors[i] == colors[i-1]) {
            // We must remove one. Add the minimum of the two costs to totalMinCost.
            // currentBlockMaxTime already holds the maximum of previous elements in this block.
            totalMinCost += min(currentBlockMaxTime, neededTime[i]);
            // Update currentBlockMaxTime to keep the maximum cost balloon in the block.
            currentBlockMaxTime = max(currentBlockMaxTime, neededTime[i]);
        } else {
            // If colors are different, it's a new block. Reset currentBlockMaxTime.
            currentBlockMaxTime = neededTime[i];
        }
    }

    return totalMinCost;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
using System;

public class Solution {
    public int MinCost(string colors, int[] neededTime) {
        int n = colors.Length;
        if (n < 2) {
            return 0;
        }

        int totalMinCost = 0;
        // currentBlockMaxTime stores the max cost of the balloon kept in the current consecutive block
        int currentBlockMaxTime = neededTime[0];

        // Iterate from the second balloon
        for (int i = 1; i < n; i++) {
            // If the current balloon has the same color as the previous one
            if (colors[i] == colors[i - 1]) {
                // We must remove one. Add the minimum of the two costs to totalMinCost.
                // currentBlockMaxTime already holds the maximum of previous elements in this block.
                totalMinCost += Math.Min(currentBlockMaxTime, neededTime[i]);
                // Update currentBlockMaxTime to keep the maximum cost balloon in the block.
                currentBlockMaxTime = Math.Max(currentBlockMaxTime, neededTime[i]);
            } else {
                // If colors are different, it's a new block. Reset currentBlockMaxTime.
                currentBlockMaxTime = neededTime[i];
            }
        }

        return totalMinCost;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
/**
 * @param {string} colors
 * @param {number[]} neededTime
 * @return {number}
 */
var minCost = function(colors, neededTime) {
    const n = colors.length;
    if (n < 2) {
        return 0;
    }

    let totalMinCost = 0;
    // currentBlockMaxTime stores the max cost of the balloon kept in the current consecutive block
    let currentBlockMaxTime = neededTime[0];

    // Iterate from the second balloon
    for (let i = 1; i < n; i++) {
        // If the current balloon has the same color as the previous one
        if (colors[i] === colors[i - 1]) {
            // We must remove one. Add the minimum of the two costs to totalMinCost.
            // currentBlockMaxTime already holds the maximum of previous elements in this block.
            totalMinCost += Math.min(currentBlockMaxTime, neededTime[i]);
            // Update currentBlockMaxTime to keep the maximum cost balloon in the block.
            currentBlockMaxTime = Math.max(currentBlockMaxTime, neededTime[i]);
        } else {
            // If colors are different, it's a new block. Reset currentBlockMaxTime.
            currentBlockMaxTime = neededTime[i];
        }
    }

    return totalMinCost;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function minCost(colors: string, neededTime: number[]): number {
    const n = colors.length;
    if (n < 2) {
        return 0;
    }

    let totalMinCost: number = 0;
    // currentBlockMaxTime stores the max cost of the balloon kept in the current consecutive block
    let currentBlockMaxTime: number = neededTime[0];

    // Iterate from the second balloon
    for (let i = 1; i < n; i++) {
        // If the current balloon has the same color as the previous one
        if (colors[i] === colors[i - 1]) {
            // We must remove one. Add the minimum of the two costs to totalMinCost.
            // currentBlockMaxTime already holds the maximum of previous elements in this block.
            totalMinCost += Math.min(currentBlockMaxTime, neededTime[i]);
            // Update currentBlockMaxTime to keep the maximum cost balloon in the block.
            currentBlockMaxTime = Math.max(currentBlockMaxTime, neededTime[i]);
        } else {
            // If colors are different, it's a new block. Reset currentBlockMaxTime.
            currentBlockMaxTime = neededTime[i];
        }
    }

    return totalMinCost;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
class Solution {
    /**
     * @param String $colors
     * @param Integer[] $neededTime
     * @return Integer
     */
    function minCost($colors, $neededTime) {
        $n = strlen($colors);
        if ($n < 2) {
            return 0;
        }

        $totalMinCost = 0;
        // $currentBlockMaxTime stores the max cost of the balloon kept in the current consecutive block
        $currentBlockMaxTime = $neededTime[0];

        // Iterate from the second balloon
        for ($i = 1; $i < $n; $i++) {
            // If the current balloon has the same color as the previous one
            if ($colors[$i] == $colors[$i-1]) {
                // We must remove one. Add the minimum of the two costs to $totalMinCost.
                // $currentBlockMaxTime already holds the maximum of previous elements in this block.
                $totalMinCost += min($currentBlockMaxTime, $neededTime[$i]);
                // Update $currentBlockMaxTime to keep the maximum cost balloon in the block.
                $currentBlockMaxTime = max($currentBlockMaxTime, $neededTime[$i]);
            } else {
                // If colors are different, it's a new block. Reset $currentBlockMaxTime.
                $currentBlockMaxTime = $neededTime[$i];
            }
        }

        return $totalMinCost;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution {
    func minCost(_ colors: String, _ neededTime: [Int]) -> Int {
        let n = colors.count
        if n < 2 {
            return 0
        }

        var totalMinCost = 0
        // currentBlockMaxTime stores the max cost of the balloon kept in the current consecutive block
        var currentBlockMaxTime = neededTime[0]

        // Convert string to array of characters for O(1) character access
        let colorChars = Array(colors)

        // Iterate from the second balloon
        for i in 1..<n {
            // If the current balloon has the same color as the previous one
            if colorChars[i] == colorChars[i-1] {
                // We must remove one. Add the minimum of the two costs to totalMinCost.
                // currentBlockMaxTime already holds the maximum of previous elements in this block.
                totalMinCost += min(currentBlockMaxTime, neededTime[i])
                // Update currentBlockMaxTime to keep the maximum cost balloon in the block.
                currentBlockMaxTime = max(currentBlockMaxTime, neededTime[i])
            } else {
                // If colors are different, it's a new block. Reset currentBlockMaxTime.
                currentBlockMaxTime = neededTime[i]
            }
        }

        return totalMinCost
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution {
    fun minCost(colors: String, neededTime: IntArray): Int {
        val n = colors.length
        if (n < 2) {
            return 0
        }

        var totalMinCost = 0
        // currentBlockMaxTime stores the max cost of the balloon kept in the current consecutive block
        var currentBlockMaxTime = neededTime[0]

        // Iterate from the second balloon
        for (i in 1 until n) {
            // If the current balloon has the same color as the previous one
            if (colors[i] == colors[i - 1]) {
                // We must remove one. Add the minimum of the two costs to totalMinCost.
                // currentBlockMaxTime already holds the maximum of previous elements in this block.
                totalMinCost += minOf(currentBlockMaxTime, neededTime[i])
                // Update currentBlockMaxTime to keep the maximum cost balloon in the block.
                currentBlockMaxTime = maxOf(currentBlockMaxTime, neededTime[i])
            } else {
                // If colors are different, it's a new block. Reset currentBlockMaxTime.
                currentBlockMaxTime = neededTime[i]
            }
        }

        return totalMinCost
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
import 'dart:math';

class Solution {
  int minCost(String colors, List<int> neededTime) {
    int n = colors.length;
    if (n < 2) {
      return 0;
    }

    int totalMinCost = 0;
    // currentBlockMaxTime stores the max cost of the balloon kept in the current consecutive block
    int currentBlockMaxTime = neededTime[0];

    // Iterate from the second balloon
    for (int i = 1; i < n; i++) {
      // If the current balloon has the same color as the previous one
      if (colors[i] == colors[i - 1]) {
        // We must remove one. Add the minimum of the two costs to totalMinCost.
        // currentBlockMaxTime already holds the maximum of previous elements in this block.
        totalMinCost += min(currentBlockMaxTime, neededTime[i]);
        // Update currentBlockMaxTime to keep the maximum cost balloon in the block.
        currentBlockMaxTime = max(currentBlockMaxTime, neededTime[i]);
      } else {
        // If colors are different, it's a new block. Reset currentBlockMaxTime.
        currentBlockMaxTime = neededTime[i];
      }
    }

    return totalMinCost;
  }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

// Helper functions for int min/max if not using Go 1.21+ (which has built-in min/max for int)
func intMin(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func intMax(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func minCost(colors string, neededTime []int) int {
    n := len(colors)
    if n < 2 {
        return 0
    }

    totalMinCost := 0
    // currentBlockMaxTime stores the max cost of the balloon kept in the current consecutive block
    currentBlockMaxTime := neededTime[0]

    // Iterate from the second balloon
    for i := 1; i < n; i++ {
        // If the current balloon has the same color as the previous one
        if colors[i] == colors[i-1] {
            // We must remove one. Add the minimum of the two costs to totalMinCost.
            // currentBlockMaxTime already holds the maximum of previous elements in this block.
            totalMinCost += intMin(currentBlockMaxTime, neededTime[i])
            // Update currentBlockMaxTime to keep the maximum cost balloon in the block.
            currentBlockMaxTime = intMax(currentBlockMaxTime, neededTime[i])
        } else {
            // If colors are different, it's a new block. Reset currentBlockMaxTime.
            currentBlockMaxTime = neededTime[i]
        }
    }

    return totalMinCost
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
# @param {string} colors
# @param {integer[]} needed_time
# @return {integer}
def min_cost(colors, needed_time)
    n = colors.length
    return 0 if n < 2

    total_min_cost = 0
    # current_block_max_time stores the max cost of the balloon kept in the current consecutive block
    current_block_max_time = needed_time[0]

    # Iterate from the second balloon
    (1...n).each do |i|
        # If the current balloon has the same color as the previous one
        if colors[i] == colors[i-1]
            # We must remove one. Add the minimum of the two costs to total_min_cost.
            # current_block_max_time already holds the maximum of previous elements in this block.
            total_min_cost += [current_block_max_time, needed_time[i]].min
            # Update current_block_max_time to keep the maximum cost balloon in the block.
            current_block_max_time = [current_block_max_time, needed_time[i]].max
        else
            # If colors are different, it's a new block. Reset current_block_max_time.
            current_block_max_time = needed_time[i]
        end
    end

    total_min_cost
end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {
    def minCost(colors: String, neededTime: Array[Int]): Int = {
        val n = colors.length
        if (n < 2) {
            return 0
        }

        var totalMinCost = 0
        // currentBlockMaxTime stores the max cost of the balloon kept in the current consecutive block
        var currentBlockMaxTime = neededTime(0)

        // Iterate from the second balloon
        for (i <- 1 until n) {
            // If the current balloon has the same color as the previous one
            if (colors(i) == colors(i-1)) {
                // We must remove one. Add the minimum of the two costs to totalMinCost.
                // currentBlockMaxTime already holds the maximum of previous elements in this block.
                totalMinCost += math.min(currentBlockMaxTime, neededTime(i))
                // Update currentBlockMaxTime to keep the maximum cost balloon in the block.
                currentBlockMaxTime = math.max(currentBlockMaxTime, neededTime(i))
            } else {
                // If colors are different, it's a new block. Reset currentBlockMaxTime.
                currentBlockMaxTime = neededTime(i)
            }
        }

        totalMinCost
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution {
    pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
        let n = colors.len();
        if n < 2 {
            return 0;
        }

        let mut total_min_cost = 0;
        // current_block_max_time stores the max cost of the balloon kept in the current consecutive block
        let mut current_block_max_time = needed_time[0];

        // Accessing characters by index for a String is O(N) in Rust.
        // Convert to a byte slice for O(1) character (byte) access for ASCII strings.
        // Problem states 'colors contains only lowercase English letters', so ASCII bytes are fine.
        let colors_bytes = colors.as_bytes();

        // Iterate from the second balloon
        for i in 1..n {
            // If the current balloon has the same color as the previous one
            if colors_bytes[i] == colors_bytes[i - 1] {
                // We must remove one. Add the minimum of the two costs to total_min_cost.
                // current_block_max_time already holds the maximum of previous elements in this block.
                total_min_cost += std::cmp::min(current_block_max_time, needed_time[i]);
                // Update current_block_max_time to keep the maximum cost balloon in the block.
                current_block_max_time = std::cmp::max(current_block_max_time, needed_time[i]);
            } else {
                // If colors are different, it's a new block. Reset current_block_max_time.
                current_block_max_time = needed_time[i];
            }
        }

        total_min_cost
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket

(provide (contract-out
  [min-cost-colorful-rope (string? (listof integer?) . -> . integer?)]))

;; min-cost-colorful-rope : string? (listof integer?) -> integer?
;; Calculates the minimum time Bob needs to make the rope colorful.
;; The colors string contains 'n' balloons, and needed-time is a list of 'n' integers
;; representing the time to remove each balloon.
(define (min-cost-colorful-rope colors needed-time-list)
  (define n (string-length colors))
  (if (< n 2)
      0
      (let* ((needed-time-vec (list->vector needed-time-list))) ;; For O(1) neededTime access
        (let loop ((i 1)
                   (total-min-cost 0)
                   ;; current-block-max-time stores the max cost of the balloon kept in the current consecutive block
                   (current-block-max-time (vector-ref needed-time-vec 0)))
          (if (< i n)
              (if (char=? (string-ref colors i) (string-ref colors (- i 1)))
                  ;; If the current balloon has the same color as the previous one
                  (loop (+ i 1)
                        ;; We must remove one. Add the minimum of the two costs to total-min-cost.
                        ;; current-block-max-time already holds the maximum of previous elements in this block.
                        (+ total-min-cost (min current-block-max-time (vector-ref needed-time-vec i)))
                        ;; Update current-block-max-time to keep the maximum cost balloon in the block.
                        (max current-block-max-time (vector-ref needed-time-vec i)))
                  ;; If colors are different, it's a new block. Reset current-block-max-time.
                  (loop (+ i 1)
                        total-min-cost
                        (vector-ref needed-time-vec i)))
              total-min-cost)))))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
-export([min_cost/2]).

-spec min_cost(Colors :: string(), NeededTime :: [integer()]) -> integer().
min_cost(Colors, NeededTime) ->
    N = length(Colors),
    if N < 2 ->
        0;
    true ->
        % Initialize with the first element's needed time and color
        % Then iterate from the second element onwards.
        min_cost_impl(
            tl(Colors),     % Colors list starting from index 1
            tl(NeededTime), % neededTime list starting from index 1
            hd(NeededTime), % current_block_max_time, initialized with neededTime[0]
            hd(Colors),     % prev_char_code, initialized with colors[0]
            0               % total_min_cost
        )
    end.

min_cost_impl([], [], _CurrentBlockMaxTime, _PrevCharCode, TotalMinCost) ->
    TotalMinCost;
min_cost_impl([CurrentCharCode | RestColors], [CurrentTime | RestTimes], CurrentBlockMaxTime, PrevCharCode, TotalMinCost) ->
    if CurrentCharCode == PrevCharCode ->
        % We must remove one. Add the minimum of the two costs to TotalMinCost.
        % CurrentBlockMaxTime already holds the maximum of previous elements in this block.
        NewTotalMinCost = TotalMinCost + min(CurrentBlockMaxTime, CurrentTime),
        % Update CurrentBlockMaxTime to keep the maximum cost balloon in the block.
        NewCurrentBlockMaxTime = max(CurrentBlockMaxTime, CurrentTime),
        min_cost_impl(RestColors, RestTimes, NewCurrentBlockMaxTime, CurrentCharCode, NewTotalMinCost);
    true -> % CurrentCharCode /= PrevCharCode
        % If colors are different, it's a new block. Reset CurrentBlockMaxTime.
        min_cost_impl(RestColors, RestTimes, CurrentTime, CurrentCharCode, TotalMinCost)
    end.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
  @spec min_cost(colors :: String.t(), needed_time :: [integer()]) :: integer()
  def min_cost(colors, needed_time) do
    n = String.length(colors)

    if n < 2 do
      0
    else
      # Convert colors string to a list of character codes for easier head/tail operations
      colors_charlist = String.to_charlist(colors)

      # Initialize with the first element's needed time and color
      # Then iterate from the second element onwards.
      min_cost_impl(
        tl(colors_charlist), # Colors charcodes starting from index 1
        tl(needed_time),     # neededTime list starting from index 1
        hd(needed_time),     # current_block_max_time, initialized with neededTime[0]
        hd(colors_charlist), # prev_char_code, initialized with colors[0]
        0                    # total_min_cost
      )
    end
  end

  defp min_cost_impl([], [], _current_block_max_time, _prev_char_code, total_min_cost) do
    total_min_cost
  end

  defp min_cost_impl([current_char_code | rest_colors], [current_time | rest_times], current_block_max_time, prev_char_code, total_min_cost) do
    if current_char_code == prev_char_code do
      # We must remove one. Add the minimum of the two costs to total_min_cost.
      # current_block_max_time already holds the maximum of previous elements in this block.
      new_total_min_cost = total_min_cost + min(current_block_max_time, current_time)
      # Update current_block_max_time to keep the maximum cost balloon in the block.
      new_current_block_max_time = max(current_block_max_time, current_time)
      min_cost_impl(rest_colors, rest_times, new_current_block_max_time, current_char_code, new_total_min_cost)
    else
      # If colors are different, it's a new block. Reset current_block_max_time.
      min_cost_impl(rest_colors, rest_times, current_time, current_char_code, total_min_cost)
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
  <small class="solution-timestamp">(2025-11-20 00:19:52)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by iterating through the string of colors and the array of needed times simultaneously. We maintain a running sum of the time needed to remove balloons and a max value for the current group of repeated letters. When we encounter a new color, we update the total time by adding the sum of the times of the previous group minus the max time of the previous group, and then reset the sum and max for the new group. At the end, we add the sum of the times of the last group minus the max time of the last group to the total time. This approach ensures that we remove the minimum number of balloons to make the rope colorful.

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
           int minCost(string colors, vector<int>& neededTime) {
               int sum = 0, maxVal = 0, totalTime = 0;
               for (int i = 0; i < colors.size(); ++i) {
                   if (i > 0 && colors[i] != colors[i - 1]) {
                       totalTime += sum - maxVal;
                       sum = 0;
                       maxVal = 0;
                   }
                   sum += neededTime[i];
                   maxVal = max(maxVal, neededTime[i]);
               }
               totalTime += sum - maxVal;
               return totalTime;
           }
       };
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
           public int minCost(String colors, int[] neededTime) {
               int sum = 0, maxVal = 0, totalTime = 0;
               for (int i = 0; i < colors.length(); ++i) {
                   if (i > 0 && colors.charAt(i) != colors.charAt(i - 1)) {
                       totalTime += sum - maxVal;
                       sum = 0;
                       maxVal = 0;
                   }
                   sum += neededTime[i];
                   maxVal = Math.max(maxVal, neededTime[i]);
               }
               totalTime += sum - maxVal;
               return totalTime;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
           def minCost(self, colors: str, neededTime: list[int]) -> int:
               sumVal = 0
               maxVal = 0
               totalTime = 0
               for i in range(len(colors)):
                   if i > 0 and colors[i] != colors[i - 1]:
                       totalTime += sumVal - maxVal
                       sumVal = 0
                       maxVal = 0
                   sumVal += neededTime[i]
                   maxVal = max(maxVal, neededTime[i])
               totalTime += sumVal - maxVal
               return totalTime
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
           def minCost(self, colors: str, neededTime: list[int]) -> int:
               sumVal = 0
               maxVal = 0
               totalTime = 0
               for i in range(len(colors)):
                   if i > 0 and colors[i] != colors[i - 1]:
                       totalTime += sumVal - maxVal
                       sumVal = 0
                       maxVal = 0
                   sumVal += neededTime[i]
                   maxVal = max(maxVal, neededTime[i])
               totalTime += sumVal - maxVal
               return totalTime
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdio.h>
       #include <string.h>
       #include <stdlib.h>

       int compare(const void *a, const void *b) {
           return (*(int*)a - *(int*)b);
       }

       int minCost(char *colors, int* neededTime, int colorsSize) {
           int sum = 0, maxVal = 0, totalTime = 0;
           for (int i = 0; i < colorsSize; ++i) {
               if (i > 0 && colors[i] != colors[i - 1]) {
                   totalTime += sum - maxVal;
                   sum = 0;
                   maxVal = 0;
               }
               sum += neededTime[i];
               if (neededTime[i] > maxVal) {
                   maxVal = neededTime[i];
               }
           }
           totalTime += sum - maxVal;
           return totalTime;
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
public class Solution {
           public int MinCost(string colors, int[] neededTime) {
               int sum = 0, maxVal = 0, totalTime = 0;
               for (int i = 0; i < colors.Length; ++i) {
                   if (i > 0 && colors[i] != colors[i - 1]) {
                       totalTime += sum - maxVal;
                       sum = 0;
                       maxVal = 0;
                   }
                   sum += neededTime[i];
                   maxVal = Math.Max(maxVal, neededTime[i]);
               }
               totalTime += sum - maxVal;
               return totalTime;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
var minCost = function(colors, neededTime) {
           let sum = 0, maxVal = 0, totalTime = 0;
           for (let i = 0; i < colors.length; ++i) {
               if (i > 0 && colors[i] != colors[i - 1]) {
                   totalTime += sum - maxVal;
                   sum = 0;
                   maxVal = 0;
               }
               sum += neededTime[i];
               maxVal = Math.max(maxVal, neededTime[i]);
           }
           totalTime += sum - maxVal;
           return totalTime;
       };
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function minCost(colors: string, neededTime: number[]): number {
           let sum: number = 0, maxVal: number = 0, totalTime: number = 0;
           for (let i: number = 0; i < colors.length; ++i) {
               if (i > 0 && colors[i] != colors[i - 1]) {
                   totalTime += sum - maxVal;
                   sum = 0;
                   maxVal = 0;
               }
               sum += neededTime[i];
               maxVal = Math.max(maxVal, neededTime[i]);
           }
           totalTime += sum - maxVal;
           return totalTime;
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
class Solution {
           function minCost($colors, $neededTime) {
               $sum = 0;
               $maxVal = 0;
               $totalTime = 0;
               for ($i = 0; $i < strlen($colors); $i++) {
                   if ($i > 0 && $colors[$i] != $colors[$i - 1]) {
                       $totalTime += $sum - $maxVal;
                       $sum = 0;
                       $maxVal = 0;
                   }
                   $sum += $neededTime[$i];
                   $maxVal = max($maxVal, $neededTime[$i]);
               }
               $totalTime += $sum - $maxVal;
               return $totalTime;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution {
           func minCost(_ colors: String, _ neededTime: [Int]) -> Int {
               var sum = 0
               var maxVal = 0
               var totalTime = 0
               let colorsArray = Array(colors)
               for i in 0..<colorsArray.count {
                   if i > 0 && colorsArray[i] != colorsArray[i - 1] {
                       totalTime += sum - maxVal
                       sum = 0
                       maxVal = 0
                   }
                   sum += neededTime[i]
                   maxVal = max(maxVal, neededTime[i])
               }
               totalTime += sum - maxVal
               return totalTime
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution {
           fun minCost(colors: String, neededTime: IntArray): Int {
               var sum = 0
               var maxVal = 0
               var totalTime = 0
               for (i in colors.indices) {
                   if (i > 0 && colors[i] != colors[i - 1]) {
                       totalTime += sum - maxVal
                       sum = 0
                       maxVal = 0
                   }
                   sum += neededTime[i]
                   maxVal = maxOf(maxVal, neededTime[i])
               }
               totalTime += sum - maxVal
               return totalTime
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
class Solution {
           int minCost(String colors, List<int> neededTime) {
               int sum = 0;
               int maxVal = 0;
               int totalTime = 0;
               for (int i = 0; i < colors.length; i++) {
                   if (i > 0 && colors[i] != colors[i - 1]) {
                       totalTime += sum - maxVal;
                       sum = 0;
                       maxVal = 0;
                   }
                   sum += neededTime[i];
                   maxVal = max(maxVal, neededTime[i]);
               }
               totalTime += sum - maxVal;
               return totalTime;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

       import (
           "fmt"
       )

       func minCost(colors string, neededTime []int) int {
           sum := 0
           maxVal := 0
           totalTime := 0
           for i := 0; i < len(colors); i++ {
               if i > 0 && colors[i] != colors[i-1] {
                   totalTime += sum - maxVal
                   sum = 0
                   maxVal = 0
               }
               sum += neededTime[i]
               if neededTime[i] > maxVal {
                   maxVal = neededTime[i]
               }
           }
           totalTime += sum - maxVal
           return totalTime
       }

       func main() {
           fmt.Println(minCost("abaac", []int{1, 2, 3, 4, 5}))
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
# @param {String} colors
       # @param {Integer[]} needed_time
       # @return {Integer}
       def min_cost(colors, needed_time)
           sum = 0
           max_val = 0
           total_time = 0
           colors.chars.each_with_index do |color, i|
               if i > 0 && color != colors[i - 1]
                   total_time += sum - max_val
                   sum = 0
                   max_val = 0
               end
               sum += needed_time[i]
               max_val = [max_val, needed_time[i]].max
           end
           total_time += sum - max_val
           total_time
       end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {
           def minCost(colors: String, neededTime: Array[Int]): Int = {
               var sum = 0
               var maxVal = 0
               var totalTime = 0
               for (i <- colors.indices) {
                   if (i > 0 && colors(i) != colors(i - 1)) {
                       totalTime += sum - maxVal
                       sum = 0
                       maxVal = 0
                   }
                   sum += neededTime(i)
                   maxVal = max(maxVal, neededTime(i))
               }
               totalTime += sum - maxVal
               totalTime
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution {
           pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
               let mut sum = 0;
               let mut max_val = 0;
               let mut total_time = 0;
               let colors: Vec<char> = colors.chars().collect();
               for i in 0..colors.len() {
                   if i > 0 && colors[i] != colors[i - 1] {
                       total_time += sum - max_val;
                       sum = 0;
                       max_val = 0;
                   }
                   sum += needed_time[i];
                   max_val = max(max_val, needed_time[i]);
               }
               total_time += sum - max_val;
               total_time
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket
       (define (minCost colors neededTime)
           (define (helper colors neededTime sum maxVal totalTime)
               (cond
                   [(null? colors) (+ totalTime sum - maxVal)]
                   [(null? (cdr colors)) (+ totalTime sum - maxVal)]
                   [else
                       (let ([color (car colors)]
                             [time (car neededTime)])
                           (if (eq? color (cadr colors))
                               (helper (cdr colors) (cdr neededTime) (+ sum time) (max maxVal time) totalTime)
                               (helper (cdr colors) (cdr neededTime) 0 0 (+ totalTime sum - maxVal))))]))
           (helper (string->list colors) neededTime 0 0 0))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
       -export([minCost/2]).

       minCost(Colors, NeededTime) ->
           minCost(Colors, NeededTime, 0, 0, 0).

       minCost([], [], Sum, MaxVal, TotalTime) ->
           TotalTime + Sum - MaxVal;
       minCost([Color | Colors], [Time | NeededTime], Sum, MaxVal, TotalTime) ->
           case Colors of
               [] ->
                   TotalTime + Sum - MaxVal;
               [NextColor | _] ->
                   if Color =:= NextColor ->
                       minCost(Colors, NeededTime, Sum + Time, max(MaxVal, Time), TotalTime);
                   true ->
                       minCost(Colors, NeededTime, 0, 0, TotalTime + Sum - MaxVal)
           end.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
           def min_cost(colors, needed_time) do
               min_cost(colors, needed_time, 0, 0, 0)
           end

           defp min_cost([], [], sum, max_val, total_time) do
               total_time + sum - max_val
           end

           defp min_cost([color | colors], [time | needed_time], sum, max_val, total_time) do
               case colors do
                   [] ->
                       total_time + sum - max_val

                   [next_color | _] ->
                       if color == next_color do
                           min_cost(colors, needed_time, sum + time, max(max_val, time), total_time)
                       else
                           min_cost(colors, needed_time, 0, 0, total_time + sum - max_val)
               end
           end
       end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the number of balloons. This is because we are iterating through the string of colors and the array of needed times once.

- **Space Complexity:** O(1) because we are using a constant amount of space to store the sum, max, and total time.

</div>
</details>
