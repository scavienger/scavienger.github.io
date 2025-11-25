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
  <small class="solution-timestamp">(2025-11-23 07:32:30 UTC)</small>
</summary>

<div class="ai-solution-content">

### Approach

Iterate through the balloons, keeping track of the sum of removal times and the maximum removal time for the current consecutive block of same-colored balloons. When a block of identical colors ends, add the sum of times for that block minus its maximum time to the total cost, effectively removing all but the most expensive balloon in that block.

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
    int minCost(std::string colors, std::vector<int>& neededTime) {
        int n = colors.length();
        if (n == 0) {
            return 0;
        }

        int total_cost = 0;
        int current_sum_time = neededTime[0];
        int current_max_time = neededTime[0];

        for (int i = 1; i < n; ++i) {
            if (colors[i] == colors[i-1]) {
                current_sum_time += neededTime[i];
                current_max_time = std::max(current_max_time, neededTime[i]);
            } else {
                total_cost += current_sum_time - current_max_time;
                current_sum_time = neededTime[i];
                current_max_time = neededTime[i];
            }
        }

        total_cost += current_sum_time - current_max_time;
        return total_cost;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.List;

class Solution {
    public int minCost(String colors, int[] neededTime) {
        int n = colors.length();
        if (n == 0) {
            return 0;
        }

        int totalCost = 0;
        int currentSumTime = neededTime[0];
        int currentMaxTime = neededTime[0];

        for (int i = 1; i < n; ++i) {
            if (colors.charAt(i) == colors.charAt(i-1)) {
                currentSumTime += neededTime[i];
                currentMaxTime = Math.max(currentMaxTime, neededTime[i]);
            } else {
                totalCost += currentSumTime - currentMaxTime;
                currentSumTime = neededTime[i];
                currentMaxTime = neededTime[i];
            }
        }

        totalCost += currentSumTime - currentMaxTime;
        return totalCost;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        if n == 0:
            return 0

        total_cost = 0
        current_sum_time = neededTime[0]
        current_max_time = neededTime[0]

        for i in range(1, n):
            if colors[i] == colors[i-1]:
                current_sum_time += neededTime[i]
                current_max_time = max(current_max_time, neededTime[i])
            else:
                total_cost += current_sum_time - current_max_time
                current_sum_time = neededTime[i]
                current_max_time = neededTime[i]

        total_cost += current_sum_time - current_max_time
        return total_cost
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        if n == 0:
            return 0

        total_cost = 0
        current_sum_time = neededTime[0]
        current_max_time = neededTime[0]

        for i in range(1, n):
            if colors[i] == colors[i-1]:
                current_sum_time += neededTime[i]
                current_max_time = max(current_max_time, neededTime[i])
            else:
                total_cost += current_sum_time - current_max_time
                current_sum_time = neededTime[i]
                current_max_time = neededTime[i]

        total_cost += current_sum_time - current_max_time
        return total_cost
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>
#include <stdlib.h>

int minCost(char * colors, int* neededTime, int neededTimeSize){
    int n = neededTimeSize;
    if (n == 0) {
        return 0;
    }

    int totalCost = 0;
    int currentSumTime = neededTime[0];
    int currentMaxTime = neededTime[0];

    for (int i = 1; i < n; ++i) {
        if (colors[i] == colors[i-1]) {
            currentSumTime += neededTime[i];
            currentMaxTime = (currentMaxTime > neededTime[i]) ? currentMaxTime : neededTime[i];
        } else {
            totalCost += currentSumTime - currentMaxTime;
            currentSumTime = neededTime[i];
            currentMaxTime = neededTime[i];
        }
    }

    totalCost += currentSumTime - currentMaxTime;
    return totalCost;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;

public class Solution {
    public int MinCost(string colors, int[] neededTime) {
        int n = colors.Length;
        if (n == 0) {
            return 0;
        }

        int totalCost = 0;
        int currentSumTime = neededTime[0];
        int currentMaxTime = neededTime[0];

        for (int i = 1; i < n; ++i) {
            if (colors[i] == colors[i-1]) {
                currentSumTime += neededTime[i];
                currentMaxTime = Math.Max(currentMaxTime, neededTime[i]);
            } else {
                totalCost += currentSumTime - currentMaxTime;
                currentSumTime = neededTime[i];
                currentMaxTime = neededTime[i];
            }
        }

        totalCost += currentSumTime - currentMaxTime;
        return totalCost;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} colors
 * @param {number[]} neededTime
 * @return {number}
 */
var minCost = function(colors, neededTime) {
    const n = colors.length;
    if (n === 0) {
        return 0;
    }

    let totalCost = 0;
    let currentSumTime = neededTime[0];
    let currentMaxTime = neededTime[0];

    for (let i = 1; i < n; ++i) {
        if (colors[i] === colors[i-1]) {
            currentSumTime += neededTime[i];
            currentMaxTime = Math.max(currentMaxTime, neededTime[i]);
        } else {
            totalCost += currentSumTime - currentMaxTime;
            currentSumTime = neededTime[i];
            currentMaxTime = neededTime[i];
        }
    }

    totalCost += currentSumTime - currentMaxTime;
    return totalCost;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minCost(colors: string, neededTime: number[]): number {
    const n = colors.length;
    if (n === 0) {
        return 0;
    }

    let totalCost: number = 0;
    let currentSumTime: number = neededTime[0];
    let currentMaxTime: number = neededTime[0];

    for (let i = 1; i < n; ++i) {
        if (colors[i] === colors[i-1]) {
            currentSumTime += neededTime[i];
            currentMaxTime = Math.max(currentMaxTime, neededTime[i]);
        } else {
            totalCost += currentSumTime - currentMaxTime;
            currentSumTime = neededTime[i];
            currentMaxTime = neededTime[i];
        }
    }

    totalCost += currentSumTime - currentMaxTime;
    return totalCost;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {

    /**
     * @param String $colors
     * @param Integer[] $neededTime
     * @return Integer
     */
    function minCost($colors, $neededTime) {
        $n = strlen($colors);
        if ($n === 0) {
            return 0;
        }

        $totalCost = 0;
        $currentSumTime = $neededTime[0];
        $currentMaxTime = $neededTime[0];

        for ($i = 1; $i < $n; ++$i) {
            if ($colors[$i] === $colors[$i-1]) {
                $currentSumTime += $neededTime[$i];
                $currentMaxTime = max($currentMaxTime, $neededTime[$i]);
            } else {
                $totalCost += $currentSumTime - $currentMaxTime;
                $currentSumTime = $neededTime[$i];
                $currentMaxTime = $neededTime[$i];
            }
        }

        $totalCost += $currentSumTime - $currentMaxTime;
        return $totalCost;
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
    func minCost(_ colors: String, _ neededTime: [Int]) -> Int {
        let n = colors.count
        if n == 0 {
            return 0
        }

        var totalCost = 0
        var currentSumTime = neededTime[0]
        var currentMaxTime = neededTime[0]

        let colorChars = Array(colors)

        for i in 1..<n {
            if colorChars[i] == colorChars[i-1] {
                currentSumTime += neededTime[i]
                currentMaxTime = max(currentMaxTime, neededTime[i])
            } else {
                totalCost += currentSumTime - currentMaxTime
                currentSumTime = neededTime[i]
                currentMaxTime = neededTime[i]
            }
        }

        totalCost += currentSumTime - currentMaxTime
        return totalCost
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minCost(colors: String, neededTime: IntArray): Int {
        val n = colors.length
        if (n == 0) {
            return 0
        }

        var totalCost = 0
        var currentSumTime = neededTime[0]
        var currentMaxTime = neededTime[0]

        for (i in 1 until n) {
            if (colors[i] == colors[i-1]) {
                currentSumTime += neededTime[i]
                currentMaxTime = maxOf(currentMaxTime, neededTime[i])
            } else {
                totalCost += currentSumTime - currentMaxTime
                currentSumTime = neededTime[i]
                currentMaxTime = neededTime[i]
            }
        }

        totalCost += currentSumTime - currentMaxTime
        return totalCost
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
  int minCost(String colors, List<int> neededTime) {
    final int n = colors.length;
    if (n == 0) {
      return 0;
    }

    int totalCost = 0;
    int currentSumTime = neededTime[0];
    int currentMaxTime = neededTime[0];

    for (int i = 1; i < n; ++i) {
      if (colors[i] == colors[i-1]) {
        currentSumTime += neededTime[i];
        currentMaxTime = max(currentMaxTime, neededTime[i]);
      } else {
        totalCost += currentSumTime - currentMaxTime;
        currentSumTime = neededTime[i];
        currentMaxTime = neededTime[i];
      }
    }

    totalCost += currentSumTime - currentMaxTime;
    return totalCost;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func minCost(colors string, neededTime []int) int {
    n := len(colors)
    if n == 0 {
        return 0
    }

    totalCost := 0
    currentSumTime := neededTime[0]
    currentMaxTime := neededTime[0]

    for i := 1; i < n; i++ {
        if colors[i] == colors[i-1] {
            currentSumTime += neededTime[i]
            currentMaxTime = max(currentMaxTime, neededTime[i])
        } else {
            totalCost += currentSumTime - currentMaxTime
            currentSumTime = neededTime[i]
            currentMaxTime = neededTime[i];
        }
    }

    totalCost += currentSumTime - currentMaxTime
    return totalCost
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} colors
# @param {Integer[]} needed_time
# @return {Integer}
def min_cost(colors, needed_time)
    n = colors.length
    return 0 if n == 0

    total_cost = 0
    current_sum_time = needed_time[0]
    current_max_time = needed_time[0]

    (1...n).each do |i|
        if colors[i] == colors[i-1]
            current_sum_time += needed_time[i]
            current_max_time = [current_max_time, needed_time[i]].max
        else
            total_cost += current_sum_time - current_max_time
            current_sum_time = needed_time[i]
            current_max_time = needed_time[i]
        end
    end

    total_cost += current_sum_time - current_max_time
    return total_cost
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minCost(colors: String, neededTime: Array[Int]): Int = {
        val n = colors.length
        if (n == 0) {
            return 0
        }

        var totalCost = 0
        var currentSumTime = neededTime(0)
        var currentMaxTime = neededTime(0)

        for (i <- 1 until n) {
            if (colors(i) == colors(i-1)) {
                currentSumTime += neededTime(i)
                currentMaxTime = currentMaxTime.max(neededTime(i))
            } else {
                totalCost += currentSumTime - currentMaxTime
                currentSumTime = neededTime(i)
                currentMaxTime = neededTime(i)
            }
        }

        totalCost += currentSumTime - currentMaxTime
        return totalCost
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
        let n = colors.len();
        if n == 0 {
            return 0;
        }

        let mut total_cost = 0;
        let mut current_sum_time = needed_time[0];
        let mut current_max_time = needed_time[0];

        let colors_chars: Vec<char> = colors.chars().collect();

        for i in 1..n {
            if colors_chars[i] == colors_chars[i-1] {
                current_sum_time += needed_time[i];
                current_max_time = current_max_time.max(needed_time[i]);
            } else {
                total_cost += current_sum_time - current_max_time;
                current_sum_time = needed_time[i];
                current_max_time = needed_time[i];
            }
        }

        total_cost += current_sum_time - current_max_time;
        return total_cost;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (min-cost colors needed-time)
  (let* ([n (string-length colors)]
         [total-cost 0]
         [current-sum-time 0]
         [current-max-time 0])
    (when (> n 0)
      (set! current-sum-time (vector-ref needed-time 0))
      (set! current-max-time (vector-ref needed-time 0))

      (for ([i (in-range 1 n)])
        (if (char=? (string-ref colors i) (string-ref colors (- i 1)))
            (begin
              (set! current-sum-time (+ current-sum-time (vector-ref needed-time i)))
              (set! current-max-time (max current-max-time (vector-ref needed-time i))))
            (begin
              (set! total-cost (+ total-cost (- current-sum-time current-max-time)))
              (set! current-sum-time (vector-ref needed-time i))
              (set! current-max-time (vector-ref needed-time i))))))

    (when (> n 0) 
      (set! total-cost (+ total-cost (- current-sum-time current-max-time))))

    total-cost))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([min_cost/2]).

min_cost(Colors, NeededTime) ->
    N = length(Colors),
    case N of
        0 -> 0;
        _ ->
            ColorsList = string:to_list(Colors),
            min_cost_helper(tl(ColorsList), tl(NeededTime), hd(ColorsList), 0, hd(NeededTime), hd(NeededTime))
    end.

min_cost_helper([], [], _PrevColor, TotalCost, CurrentSumTime, CurrentMaxTime) ->
    TotalCost + (CurrentSumTime - CurrentMaxTime);
min_cost_helper([Color | RestColors], [Time | RestNeededTime], PrevColor, AccTotalCost, AccCurrentSumTime, AccCurrentMaxTime) ->
    if Color == PrevColor ->
        NewCurrentSumTime = AccCurrentSumTime + Time,
        NewCurrentMaxTime = max(AccCurrentMaxTime, Time),
        min_cost_helper(RestColors, RestNeededTime, Color, AccTotalCost, NewCurrentSumTime, NewCurrentMaxTime);
    true ->
        NewTotalCost = AccTotalCost + (AccCurrentSumTime - AccCurrentMaxTime),
        min_cost_helper(RestColors, RestNeededTime, Color, NewTotalCost, Time, Time)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_cost(colors :: String.t, needed_time :: [integer]) :: integer
  def min_cost(colors, needed_time) do
    n = String.length(colors)
    if n == 0 do
      0
    else
      colors_list = String.to_charlist(colors)

      initial_state = {0, hd(needed_time), hd(needed_time), hd(colors_list)}

      {final_total_cost, final_current_sum_time, final_current_max_time, _} = 
        Enum.zip(tl(colors_list), tl(needed_time))
        |> Enum.reduce(initial_state, fn {char, time}, {acc_total_cost, acc_sum_time, acc_max_time, prev_char} ->
          if char == prev_char do
            {acc_total_cost, acc_sum_time + time, max(acc_max_time, time), char}
          else
            {acc_total_cost + (acc_sum_time - acc_max_time), time, time, char}
          end
        end)

      final_total_cost + (final_current_sum_time - final_current_max_time)
    end
  end

  defp max(a, b), do: if a > b, do: a, else: b
end
{% endraw %}
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
  <small class="solution-timestamp">(2025-11-23 07:32:37 UTC)</small>
</summary>

<div class="ai-solution-content">

### Approach

The approach is to iterate through the string of colors and whenever a sequence of the same color is found, calculate the total time needed to remove balloons of that color and subtract the maximum time from it. This is because we want to keep the balloon with the maximum time and remove the rest.

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
#include <iostream>
#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int res = 0;
        for (int i = 0; i < colors.size();) {
            int j = i + 1;
            int sum = neededTime[i];
            int mx = neededTime[i];
            while (j < colors.size() && colors[j] == colors[i]) {
                sum += neededTime[j];
                mx = max(mx, neededTime[j]);
                j++;
            }
            if (j - i > 1) res += sum - mx;
            i = j;
        }
        return res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minCost(String colors, int[] neededTime) {
        int res = 0;
        for (int i = 0; i < colors.length();) {
            int j = i + 1;
            int sum = neededTime[i];
            int mx = neededTime[i];
            while (j < colors.length() && colors.charAt(j) == colors.charAt(i)) {
                sum += neededTime[j];
                mx = Math.max(mx, neededTime[j]);
                j++;
            }
            if (j - i > 1) res += sum - mx;
            i = j;
        }
        return res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        res = 0
        i = 0
        while i < len(colors):
            j = i + 1
            sum_val = neededTime[i]
            mx = neededTime[i]
            while j < len(colors) and colors[j] == colors[i]:
                sum_val += neededTime[j]
                mx = max(mx, neededTime[j])
                j += 1
            if j - i > 1: res += sum_val - mx
            i = j
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        res = 0
        i = 0
        while i < len(colors):
            j = i + 1
            sum_val = neededTime[i]
            mx = neededTime[i]
            while j < len(colors) and colors[j] == colors[i]:
                sum_val += neededTime[j]
                mx = max(mx, neededTime[j])
                j += 1
            if j - i > 1: res += sum_val - mx
            i = j
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <string.h>
int minCost(char * colors, int* neededTime, int colorsSize){
    int res = 0;
    int i = 0;
    while (i < colorsSize) {
        int j = i + 1;
        int sum = neededTime[i];
        int mx = neededTime[i];
        while (j < colorsSize && colors[j] == colors[i]) {
            sum += neededTime[j];
            mx = (mx > neededTime[j]) ? mx : neededTime[j];
            j++;
        }
        if (j - i > 1) res += sum - mx;
        i = j;
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinCost(string colors, int[] neededTime) {
        int res = 0;
        int i = 0;
        while (i < colors.Length) {
            int j = i + 1;
            int sum = neededTime[i];
            int mx = neededTime[i];
            while (j < colors.Length && colors[j] == colors[i]) {
                sum += neededTime[j];
                mx = Math.Max(mx, neededTime[j]);
                j++;
            }
            if (j - i > 1) res += sum - mx;
            i = j;
        }
        return res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var minCost = function(colors, neededTime) {
    let res = 0;
    let i = 0;
    while (i < colors.length) {
        let j = i + 1;
        let sum = neededTime[i];
        let mx = neededTime[i];
        while (j < colors.length && colors[j] == colors[i]) {
            sum += neededTime[j];
            mx = Math.max(mx, neededTime[j]);
            j++;
        }
        if (j - i > 1) res += sum - mx;
        i = j;
    }
    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minCost(colors: string, neededTime: number[]): number {
    let res: number = 0;
    let i: number = 0;
    while (i < colors.length) {
        let j: number = i + 1;
        let sum: number = neededTime[i];
        let mx: number = neededTime[i];
        while (j < colors.length && colors[j] == colors[i]) {
            sum += neededTime[j];
            mx = Math.max(mx, neededTime[j]);
            j++;
        }
        if (j - i > 1) res += sum - mx;
        i = j;
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function minCost($colors, $neededTime) {
        $res = 0;
        $i = 0;
        while ($i < strlen($colors)) {
            $j = $i + 1;
            $sum = $neededTime[$i];
            $mx = $neededTime[$i];
            while ($j < strlen($colors) && $colors[$j] == $colors[$i]) {
                $sum += $neededTime[$j];
                $mx = max($mx, $neededTime[$j]);
                $j++;
            }
            if ($j - $i > 1) $res += $sum - $mx;
            $i = $j;
        }
        return $res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minCost(_ colors: String, _ neededTime: [Int]) -> Int {
        var res = 0
        var i = 0
        while i < colors.count {
            var j = i + 1
            var sum = neededTime[i]
            var mx = neededTime[i]
            while j < colors.count && String(colors[colors.index(colors.startIndex, offsetBy: j)]) == String(colors[colors.index(colors.startIndex, offsetBy: i)]) {
                sum += neededTime[j]
                mx = max(mx, neededTime[j])
                j += 1
            }
            if j - i > 1 { res += sum - mx }
            i = j
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minCost(colors: String, neededTime: IntArray): Int {
        var res = 0
        var i = 0
        while (i < colors.length) {
            var j = i + 1
            var sum = neededTime[i]
            var mx = neededTime[i]
            while (j < colors.length && colors[j] == colors[i]) {
                sum += neededTime[j]
                mx = maxOf(mx, neededTime[j])
                j++
            }
            if (j - i > 1) res += sum - mx
            i = j
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minCost(String colors, List<int> neededTime) {
      int res = 0;
      int i = 0;
      while (i < colors.length) {
          int j = i + 1;
          int sum = neededTime[i];
          int mx = neededTime[i];
          while (j < colors.length && colors[j] == colors[i]) {
              sum += neededTime[j];
              mx = max(mx, neededTime[j]);
              j++;
          }
          if (j - i > 1) res += sum - mx;
          i = j;
      }
      return res;
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
func minCost(colors string, neededTime []int) int {
    res := 0
    i := 0
    for i < len(colors) {
        j := i + 1
        sum := neededTime[i]
        mx := neededTime[i]
        for j < len(colors) && colors[j] == colors[i] {
            sum += neededTime[j]
            if neededTime[j] > mx {
                mx = neededTime[j]
            }
            j++
        }
        if j-i > 1 {
            res += sum - mx
        }
        i = j
    }
    return res
}
func main() {
    fmt.Println(minCost("abaac", []int{1, 2, 3, 4, 5}))
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} colors
# @param {Integer[]} needed_time
# @return {Integer}
def min_cost(colors, needed_time)
    res = 0
    i = 0
    while i < colors.size
        j = i + 1
        sum = needed_time[i]
        mx = needed_time[i]
        while j < colors.size && colors[j] == colors[i]
            sum += needed_time[j]
            mx = [mx, needed_time[j]].max
            j += 1
        end
        res += sum - mx if j - i > 1
        i = j
    end
    res
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minCost(colors: String, neededTime: Array[Int]): Int = {
        var res = 0
        var i = 0
        while (i < colors.length) {
            var j = i + 1
            var sum = neededTime(i)
            var mx = neededTime(i)
            while (j < colors.length && colors(j) == colors(i)) {
                sum += neededTime(j)
                mx = Math.max(mx, neededTime(j))
                j += 1
            }
            if (j - i > 1) res += sum - mx
            i = j
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut i = 0;
        while i < colors.len() {
            let mut j = i + 1;
            let mut sum = needed_time[i];
            let mut mx = needed_time[i];
            while j < colors.len() && colors.as_bytes()[j] == colors.as_bytes()[i] {
                sum += needed_time[j];
                mx = mx.max(needed_time[j]);
                j += 1;
            }
            if j - i > 1 {
                res += sum - mx;
            }
            i = j;
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
(define (minCost colors neededTime)
    (let loop ((i 0) (res 0))
        (cond
            [(>= i (string-length colors)) res]
            [else
                (let* ((j (+ i 1))
                       (sum (list-ref neededTime i))
                       (mx (list-ref neededTime i)))
                    (let loop2 ((j j) (sum sum) (mx mx))
                        (cond
                            [(>= j (string-length colors)) (loop (+ i 1) (+ res (- sum mx)))]
                            [(eq? (string-ref colors i) (string-ref colors j))
                                (loop2 (+ j 1) (+ sum (list-ref neededTime j)) (max mx (list-ref neededTime j)))]
                            [else (loop (+ i 1) res)]))))])))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([minCost/2]).
minCost(Colors, NeededTime) ->
    minCost(Colors, NeededTime, 0, 0).
minCost([], _, Res, _) ->
    Res;
minCost([C | Cs], [T | Ts], Res, I) ->
    {J, Sum, Mx} = loop(Cs, Ts, I + 1, T, T, C),
    minCost(lists:sublist(Cs, J - I), lists:sublist(Ts, J - I), Res + Sum - Mx, J).
loop([], [], J, Sum, Mx, _) ->
    {J, Sum, Mx};
loop([C | Cs], [T | Ts], I, Sum, Mx, C0) ->
    case C of
        C0 ->
            loop(Cs, Ts, I + 1, Sum + T, max(Mx, T), C0);
        _ ->
            {I, Sum, Mx}
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  def min_cost(colors, needed_time) do
      min_cost(colors, needed_time, 0, 0)
  end
  defp min_cost([], _, res, _), do: res
  defp min_cost([c | cs], [t | ts], res, i) do
      {j, sum, mx} = loop(cs, ts, i + 1, t, t, c)
      min_cost(Enum.slice(cs, j - i..-1), Enum.slice(ts, j - i..-1), res + sum - mx, j)
  end
  defp loop([], [], j, sum, mx, _), do: {j, sum, mx}
  defp loop([c | cs], [t | ts], i, sum, mx, c0) do
      case c do
          ^c0 -> loop(cs, ts, i + 1, sum + t, max(mx, t), c0)
          _ -> {i, sum, mx}
      end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n)

- **Space Complexity:** O(1)

</div>
</details>
