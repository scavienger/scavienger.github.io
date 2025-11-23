---
layout: post
title: "Set Intersection Size At Least Two"
date: 2025-11-20 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Greedy", "Sorting"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/set-intersection-size-at-least-two/
---

## Problem #757: Set Intersection Size At Least Two

**Difficulty:** Hard

**Topics:** Array, Greedy, Sorting

## Problem Description

<p>You are given a 2D integer array <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> represents all the integers from <code>start<sub>i</sub></code> to <code>end<sub>i</sub></code> inclusively.</p>

<p>A <strong>containing set</strong> is an array <code>nums</code> where each interval from <code>intervals</code> has <strong>at least two</strong> integers in <code>nums</code>.</p>

<ul>
	<li>For example, if <code>intervals = [[1,3], [3,7], [8,9]]</code>, then <code>[1,2,4,7,8,9]</code> and <code>[2,3,4,8,9]</code> are <strong>containing sets</strong>.</li>
</ul>

<p>Return <em>the minimum possible size of a containing set</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,3],[3,7],[8,9]]
<strong>Output:</strong> 5
<strong>Explanation:</strong> let nums = [2, 3, 4, 8, 9].
It can be shown that there cannot be any containing array of size 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,3],[1,4],[2,5],[3,5]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> let nums = [2, 3, 4].
It can be shown that there cannot be any containing array of size 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[2,3],[2,4],[4,5]]
<strong>Output:</strong> 5
<strong>Explanation:</strong> let nums = [1, 2, 3, 4, 5].
It can be shown that there cannot be any containing array of size 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 3000</code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 10<sup>8</sup></code></li>
</ul>


## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-20 21:19:36 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the minimum size of a set `nums` such that every given interval `[start_i, end_i]` contains at least two elements from `nums`. This is a classic greedy problem, often solved by sorting intervals and making locally optimal choices. The core idea is to identify which intervals require new points to be added to `nums`, and when points are added, to choose them in a way that maximizes their utility for future intervals.

Our greedy strategy relies on a specific sorting order and a state-tracking mechanism. First, we sort the input `intervals`. The most effective sort for this problem is primarily by the `end` coordinate in ascending order. If two intervals have the same `end` coordinate, we sort them by their `start` coordinate in descending order. This sorting order is crucial: processing intervals that end earliest first helps manage the 'rightmost' boundaries, allowing us to satisfy immediate needs while keeping options open for later intervals. For intervals ending at the same point, processing the one that starts later (`start` descending) ensures that if we pick points `end-1` and `end` for it, these points are also highly likely to cover any other interval that ends at `end` but starts earlier.

We maintain two variables, `p1` and `p2`, which represent the two largest points currently in our 'containing set' `nums`, with `p1 < p2`. Initially, `p1` and `p2` are set to a value smaller than any possible interval coordinate (e.g., -1) to signify that no points have been chosen yet. We then iterate through the sorted intervals `[start, end]`. For each interval, we check its relationship with `p1` and `p2` and determine if we need to add new points. There are three main cases:
1. If `start <= p1`: This means both `p1` and `p2` are greater than or equal to `start` (since `p1 < p2`), and since `p1` and `p2` were chosen based on preceding intervals' `end` points, they are guaranteed to be less than or equal to `end` of the *previous* intervals that determined them. As we are processing intervals sorted by `end`, `p2` (and `p1`) will generally be 'to the left' of or at `end`. More specifically, if `start <= p1`, then `[start, end]` is already sufficiently covered by `p1` and `p2`. No new points are needed.
2. If `p1 < start <= p2`: This means only `p2` is within `[start, end]` (or equal to `start`). We need one more point to satisfy the 'at least two' condition. To maximize its impact on future intervals, we choose `end`. We update our state: `p1` becomes the old `p2`, and `p2` becomes the new `end`. We increment our total count `ans` by 1.
3. If `p2 < start`: This means neither `p1` nor `p2` is within `[start, end]`. We need to add two new points. To maximize their coverage for subsequent intervals, we choose `end-1` and `end`. We update our state: `p1` becomes `end-1`, and `p2` becomes `end`. We increment `ans` by 2.

After iterating through all intervals, the accumulated `ans` will be the minimum possible size of the containing set. This greedy approach ensures that we always choose points as far right as possible when new points are required, maximizing their ability to cover future intervals and minimizing the overall points needed.

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
    int intersectionSizeTwo(std::vector<std::vector<int>>& intervals) {
        // Sort intervals: primarily by end coordinate ascending.
        // For ties in end coordinate, sort by start coordinate descending.
        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            if (a[1] != b[1]) {
                return a[1] < b[1]; // Sort by end ascending
            }
            return a[0] > b[0]; // Sort by start descending for ties
        });

        int ans = 0;
        int p1 = -1; // Second largest point chosen so far
        int p2 = -1; // Largest point chosen so far

        for (const auto& interval : intervals) {
            int start = interval[0];
            int end = interval[1];

            // Case 1: The current interval [start, end] is fully covered by p1 and p2.
            // This implies start <= p1 (and implicitly start <= p2 since p1 < p2).
            if (start <= p1) {
                continue;
            }
            // Case 2: Only p2 covers the current interval (p1 < start <= p2).
            // We need to add one more point. The best choice is 'end' to maximize coverage.
            else if (start <= p2) { // Implies p1 < start
                ans += 1;
                p1 = p2; // The old largest becomes the new second largest
                p2 = end; // The new point 'end' becomes the largest
            }
            // Case 3: Neither p1 nor p2 covers the current interval (p2 < start).
            // We need to add two new points. The best choices are 'end-1' and 'end'.
            else { // p2 < start
                ans += 2;
                p1 = end - 1;
                p2 = end;
            }
        }

        return ans;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int intersectionSizeTwo(int[][] intervals) {
        // Sort intervals: primarily by end coordinate ascending.
        // For ties in end coordinate, sort by start coordinate descending.
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] a, int[] b) {
                if (a[1] != b[1]) {
                    return Integer.compare(a[1], b[1]); // Sort by end ascending
                }
                return Integer.compare(b[0], a[0]); // Sort by start descending for ties
            }
        });

        int ans = 0;
        int p1 = -1; // Second largest point chosen so far
        int p2 = -1; // Largest point chosen so far

        for (int[] interval : intervals) {
            int start = interval[0];
            int end = interval[1];

            // Case 1: The current interval [start, end] is fully covered by p1 and p2.
            // This implies start <= p1 (and implicitly start <= p2 since p1 < p2).
            if (start <= p1) {
                continue;
            }
            // Case 2: Only p2 covers the current interval (p1 < start <= p2).
            // We need to add one more point. The best choice is 'end' to maximize coverage.
            else if (start <= p2) { // Implies p1 < start
                ans += 1;
                p1 = p2; // The old largest becomes the new second largest
                p2 = end; // The new point 'end' becomes the largest
            }
            // Case 3: Neither p1 nor p2 covers the current interval (p2 < start).
            // We need to add two new points. The best choices are 'end-1' and 'end'.
            else { // p2 < start
                ans += 2;
                p1 = end - 1;
                p2 = end;
            }
        }

        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort intervals: primarily by end coordinate ascending.
        # For ties in end coordinate, sort by start coordinate descending.
        intervals.sort(key=lambda x: (x[1], -x[0]))

        ans = 0
        # p1: second largest point chosen so far
        # p2: largest point chosen so far
        # Initialize with values smaller than any possible interval coordinates
        p1 = -1
        p2 = -1

        for start, end in intervals:
            # Case 1: The current interval [start, end] is fully covered by p1 and p2.
            # This implies start <= p1 (and implicitly start <= p2 since p1 < p2).
            # No action needed.
            if start <= p1:
                continue

            # Case 2: Only p2 covers the current interval (p1 < start <= p2).
            # We need to add one more point. The best choice is 'end' to maximize coverage for future intervals.
            elif start <= p2:
                ans += 1
                p1 = p2  # The old largest becomes the new second largest
                p2 = end # The new point 'end' becomes the largest

            # Case 3: Neither p1 nor p2 covers the current interval (p2 < start).
            # We need to add two new points. The best choices are 'end-1' and 'end'.
            else: # p2 < start
                ans += 2
                p1 = end - 1
                p2 = end

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort intervals: primarily by end coordinate ascending.
        # For ties in end coordinate, sort by start coordinate descending.
        intervals.sort(key=lambda x: (x[1], -x[0]))

        ans = 0
        # p1: second largest point chosen so far
        # p2: largest point chosen so far
        # Initialize with values smaller than any possible interval coordinates
        p1 = -1
        p2 = -1

        for start, end in intervals:
            # Case 1: The current interval [start, end] is fully covered by p1 and p2.
            # This implies start <= p1 (and implicitly start <= p2 since p1 < p2).
            # No action needed.
            if start <= p1:
                continue

            # Case 2: Only p2 covers the current interval (p1 < start <= p2).
            # We need to add one more point. The best choice is 'end' to maximize coverage for future intervals.
            elif start <= p2:
                ans += 1
                p1 = p2  # The old largest becomes the new second largest
                p2 = end # The new point 'end' becomes the largest

            # Case 3: Neither p1 nor p2 covers the current interval (p2 < start).
            # We need to add two new points. The best choices are 'end-1' and 'end'.
            else: # p2 < start
                ans += 2
                p1 = end - 1
                p2 = end

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h> // For qsort

// Comparator for qsort
int compareIntervals(const void* a, const void* b) {
    const int* intervalA = *(const int**)a;
    const int* intervalB = *(const int**)b;

    if (intervalA[1] != intervalB[1]) {
        return intervalA[1] - intervalB[1]; // Sort by end ascending
    }
    return intervalB[0] - intervalA[0]; // Sort by start descending for ties
}

int intersectionSizeTwo(int** intervals, int intervalsSize, int* intervalsColSize) {
    // qsort takes an array of pointers to int arrays (int**)
    qsort(intervals, intervalsSize, sizeof(int*), compareIntervals);

    int ans = 0;
    int p1 = -1; // Second largest point chosen so far
    int p2 = -1; // Largest point chosen so far

    for (int i = 0; i < intervalsSize; ++i) {
        int start = intervals[i][0];
        int end = intervals[i][1];

        // Case 1: The current interval [start, end] is fully covered by p1 and p2.
        // This implies start <= p1 (and implicitly start <= p2 since p1 < p2).
        if (start <= p1) {
            continue;
        }
        // Case 2: Only p2 covers the current interval (p1 < start <= p2).
        // We need to add one more point. The best choice is 'end' to maximize coverage.
        else if (start <= p2) { // Implies p1 < start
            ans += 1;
            p1 = p2; // The old largest becomes the new second largest
            p2 = end; // The new point 'end' becomes the largest
        }
        // Case 3: Neither p1 nor p2 covers the current interval (p2 < start).
        // We need to add two new points. The best choices are 'end-1' and 'end'.
        else { // p2 < start
            ans += 2;
            p1 = end - 1;
            p2 = end;
        }
    }

    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int IntersectionSizeTwo(int[][] intervals) {
        // Sort intervals: primarily by end coordinate ascending.
        // For ties in end coordinate, sort by start coordinate descending.
        Array.Sort(intervals, (a, b) => {
            if (a[1] != b[1]) {
                return a[1].CompareTo(b[1]); // Sort by end ascending
            }
            return b[0].CompareTo(a[0]); // Sort by start descending for ties
        });

        int ans = 0;
        int p1 = -1; // Second largest point chosen so far
        int p2 = -1; // Largest point chosen so far

        foreach (var interval in intervals) {
            int start = interval[0];
            int end = interval[1];

            // Case 1: The current interval [start, end] is fully covered by p1 and p2.
            // This implies start <= p1 (and implicitly start <= p2 since p1 < p2).
            if (start <= p1) {
                continue;
            }
            // Case 2: Only p2 covers the current interval (p1 < start <= p2).
            // We need to add one more point. The best choice is 'end' to maximize coverage.
            else if (start <= p2) { // Implies p1 < start
                ans += 1;
                p1 = p2; // The old largest becomes the new second largest
                p2 = end; // The new point 'end' becomes the largest
            }
            // Case 3: Neither p1 nor p2 covers the current interval (p2 < start).
            // We need to add two new points. The best choices are 'end-1' and 'end'.
            else { // p2 < start
                ans += 2;
                p1 = end - 1;
                p2 = end;
            }
        }

        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} intervals
 * @return {number}
 */
var intersectionSizeTwo = function(intervals) {
    // Sort intervals: primarily by end coordinate ascending.
    // For ties in end coordinate, sort by start coordinate descending.
    intervals.sort((a, b) => {
        if (a[1] !== b[1]) {
            return a[1] - b[1]; // Sort by end ascending
        }
        return b[0] - a[0]; // Sort by start descending for ties
    });

    let ans = 0;
    let p1 = -1; // Second largest point chosen so far
    let p2 = -1; // Largest point chosen so far

    for (const interval of intervals) {
        const start = interval[0];
        const end = interval[1];

        // Case 1: The current interval [start, end] is fully covered by p1 and p2.
        // This implies start <= p1 (and implicitly start <= p2 since p1 < p2).
        if (start <= p1) {
            continue;
        }
        // Case 2: Only p2 covers the current interval (p1 < start <= p2).
        // We need to add one more point. The best choice is 'end' to maximize coverage.
        else if (start <= p2) { // Implies p1 < start
            ans += 1;
            p1 = p2; // The old largest becomes the new second largest
            p2 = end; // The new point 'end' becomes the largest
        }
        // Case 3: Neither p1 nor p2 covers the current interval (p2 < start).
        // We need to add two new points. The best choices are 'end-1' and 'end'.
        else { // p2 < start
            ans += 2;
            p1 = end - 1;
            p2 = end;
        }
    }

    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function intersectionSizeTwo(intervals: number[][]): number {
    // Sort intervals: primarily by end coordinate ascending.
    // For ties in end coordinate, sort by start coordinate descending.
    intervals.sort((a, b) => {
        if (a[1] !== b[1]) {
            return a[1] - b[1]; // Sort by end ascending
        }
        return b[0] - a[0]; // Sort by start descending for ties
    });

    let ans: number = 0;
    let p1: number = -1; // Second largest point chosen so far
    let p2: number = -1; // Largest point chosen so far

    for (const interval of intervals) {
        const start: number = interval[0];
        const end: number = interval[1];

        // Case 1: The current interval [start, end] is fully covered by p1 and p2.
        // This implies start <= p1 (and implicitly start <= p2 since p1 < p2).
        if (start <= p1) {
            continue;
        }
        // Case 2: Only p2 covers the current interval (p1 < start <= p2).
        // We need to add one more point. The best choice is 'end' to maximize coverage.
        else if (start <= p2) { // Implies p1 < start
            ans += 1;
            p1 = p2; // The old largest becomes the new second largest
            p2 = end; // The new point 'end' becomes the largest
        }
        // Case 3: Neither p1 nor p2 covers the current interval (p2 < start).
        // We need to add two new points. The best choices are 'end-1' and 'end'.
        else { // p2 < start
            ans += 2;
            p1 = end - 1;
            p2 = end;
        }
    }

    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {

    /**
     * @param int[][] $intervals
     * @return int
     */
    function intersectionSizeTwo($intervals) {
        // Sort intervals: primarily by end coordinate ascending.
        // For ties in end coordinate, sort by start coordinate descending.
        usort($intervals, function($a, $b) {
            if ($a[1] != $b[1]) {
                return $a[1] - $b[1]; // Sort by end ascending
            }
            return $b[0] - $a[0]; // Sort by start descending for ties
        });

        $ans = 0;
        $p1 = -1; // Second largest point chosen so far
        $p2 = -1; // Largest point chosen so far

        foreach ($intervals as $interval) {
            $start = $interval[0];
            $end = $interval[1];

            // Case 1: The current interval [start, end] is fully covered by p1 and p2.
            // This implies start <= p1 (and implicitly start <= p2 since p1 < p2).
            if ($start <= $p1) {
                continue;
            }
            // Case 2: Only p2 covers the current interval (p1 < start <= p2).
            // We need to add one more point. The best choice is 'end' to maximize coverage.
            else if ($start <= $p2) { // Implies p1 < start
                $ans += 1;
                $p1 = $p2; // The old largest becomes the new second largest
                $p2 = $end; // The new point 'end' becomes the largest
            }
            // Case 3: Neither p1 nor p2 covers the current interval (p2 < start).
            // We need to add two new points. The best choices are 'end-1' and 'end'.
            else { // p2 < start
                $ans += 2;
                $p1 = $end - 1;
                $p2 = $end;
            }
        }

        return $ans;
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
    func intersectionSizeTwo(_ intervals: [[Int]]) -> Int {
        // Sort intervals: primarily by end coordinate ascending.
        // For ties in end coordinate, sort by start coordinate descending.
        var sortedIntervals = intervals.sorted { (a, b) -> Bool in
            if a[1] != b[1] {
                return a[1] < b[1] // Sort by end ascending
            }
            return a[0] > b[0] // Sort by start descending for ties
        }

        var ans = 0
        var p1 = -1 // Second largest point chosen so far
        var p2 = -1 // Largest point chosen so far

        for interval in sortedIntervals {
            let start = interval[0]
            let end = interval[1]

            // Case 1: The current interval [start, end] is fully covered by p1 and p2.
            // This implies start <= p1 (and implicitly start <= p2 since p1 < p2).
            if start <= p1 {
                continue
            }
            // Case 2: Only p2 covers the current interval (p1 < start <= p2).
            // We need to add one more point. The best choice is 'end' to maximize coverage.
            else if start <= p2 { // Implies p1 < start
                ans += 1
                p1 = p2 // The old largest becomes the new second largest
                p2 = end // The new point 'end' becomes the largest
            }
            // Case 3: Neither p1 nor p2 covers the current interval (p2 < start).
            // We need to add two new points. The best choices are 'end-1' and 'end'.
            else { // p2 < start
                ans += 2
                p1 = end - 1
                p2 = end
            }
        }

        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.Arrays

class Solution {
    fun intersectionSizeTwo(intervals: Array<IntArray>): Int {
        // Sort intervals: primarily by end coordinate ascending.
        // For ties in end coordinate, sort by start coordinate descending.
        Arrays.sort(intervals) { a, b ->
            if (a[1] != b[1]) {
                a[1].compareTo(b[1]) // Sort by end ascending
            } else {
                b[0].compareTo(a[0]) // Sort by start descending for ties
            }
        }

        var ans = 0
        var p1 = -1 // Second largest point chosen so far
        var p2 = -1 // Largest point chosen so far

        for (interval in intervals) {
            val start = interval[0]
            val end = interval[1]

            // Case 1: The current interval [start, end] is fully covered by p1 and p2.
            // This implies start <= p1 (and implicitly start <= p2 since p1 < p2).
            if (start <= p1) {
                continue
            }
            // Case 2: Only p2 covers the current interval (p1 < start <= p2).
            // We need to add one more point. The best choice is 'end' to maximize coverage.
            else if (start <= p2) { // Implies p1 < start
                ans += 1
                p1 = p2 // The old largest becomes the new second largest
                p2 = end // The new point 'end' becomes the largest
            }
            // Case 3: Neither p1 nor p2 covers the current interval (p2 < start).
            // We need to add two new points. The best choices are 'end-1' and 'end'.
            else { // p2 < start
                ans += 2
                p1 = end - 1
                p2 = end
            }
        }

        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int intersectionSizeTwo(List<List<int>> intervals) {
    // Sort intervals: primarily by end coordinate ascending.
    // For ties in end coordinate, sort by start coordinate descending.
    intervals.sort((a, b) {
      if (a[1] != b[1]) {
        return a[1].compareTo(b[1]); // Sort by end ascending
      }
      return b[0].compareTo(a[0]); // Sort by start descending for ties
    });

    int ans = 0;
    int p1 = -1; // Second largest point chosen so far
    int p2 = -1; // Largest point chosen so far

    for (final interval in intervals) {
      final start = interval[0];
      final end = interval[1];

      // Case 1: The current interval [start, end] is fully covered by p1 and p2.
      // This implies start <= p1 (and implicitly start <= p2 since p1 < p2).
      if (start <= p1) {
        continue;
      }
      // Case 2: Only p2 covers the current interval (p1 < start <= p2).
      // We need to add one more point. The best choice is 'end' to maximize coverage.
      else if (start <= p2) { // Implies p1 < start
        ans += 1;
        p1 = p2; // The old largest becomes the new second largest
        p2 = end; // The new point 'end' becomes the largest
      }
      // Case 3: Neither p1 nor p2 covers the current interval (p2 < start).
      // We need to add two new points. The best choices are 'end-1' and 'end'.
      else { // p2 < start
        ans += 2;
        p1 = end - 1;
        p2 = end;
      }
    }

    return ans;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func intersectionSizeTwo(intervals [][]int) int {
    // Sort intervals: primarily by end coordinate ascending.
    // For ties in end coordinate, sort by start coordinate descending.
    sort.Slice(intervals, func(i, j int) bool {
        if intervals[i][1] != intervals[j][1] {
            return intervals[i][1] < intervals[j][1] // Sort by end ascending
        }
        return intervals[i][0] > intervals[j][0] // Sort by start descending for ties
    })

    ans := 0
    p1 := -1 // Second largest point chosen so far
    p2 := -1 // Largest point chosen so far

    for _, interval := range intervals {
        start := interval[0]
        end := interval[1]

        // Case 1: The current interval [start, end] is fully covered by p1 and p2.
        // This implies start <= p1 (and implicitly start <= p2 since p1 < p2).
        if start <= p1 {
            continue
        }
        // Case 2: Only p2 covers the current interval (p1 < start <= p2).
        // We need to add one more point. The best choice is 'end' to maximize coverage.
        else if start <= p2 { // Implies p1 < start
            ans += 1
            p1 = p2 // The old largest becomes the new second largest
            p2 = end // The new point 'end' becomes the largest
        }
        // Case 3: Neither p1 nor p2 covers the current interval (p2 < start).
        // We need to add two new points. The best choices are 'end-1' and 'end'.
        else { // p2 < start
            ans += 2
            p1 = end - 1
            p2 = end
        }
    }

    return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[][]} intervals
# @return {Integer}
def intersection_size_two(intervals)
    # Sort intervals: primarily by end coordinate ascending.
    # For ties in end coordinate, sort by start coordinate descending.
    intervals.sort! do |a, b|
        if a[1] != b[1]
            a[1] - b[1] # Sort by end ascending
        else
            b[0] - a[0] # Sort by start descending for ties
        end
    end

    ans = 0
    p1 = -1 # Second largest point chosen so far
    p2 = -1 # Largest point chosen so far

    intervals.each do |interval|
        start = interval[0]
        _end = interval[1] # Using _end to avoid conflict with `end` keyword

        # Case 1: The current interval [start, _end] is fully covered by p1 and p2.
        # This implies start <= p1 (and implicitly start <= p2 since p1 < p2).
        if start <= p1
            next
        end
        # Case 2: Only p2 covers the current interval (p1 < start <= p2).
        # We need to add one more point. The best choice is '_end' to maximize coverage.
        if start <= p2 # Implies p1 < start
            ans += 1
            p1 = p2 # The old largest becomes the new second largest
            p2 = _end # The new point '_end' becomes the largest
        # Case 3: Neither p1 nor p2 covers the current interval (p2 < start).
        # We need to add two new points. The best choices are '_end-1' and '_end'.
        else # p2 < start
            ans += 2
            p1 = _end - 1
            p2 = _end
        end
    end

    ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable.ArrayBuffer

object Solution {
    def intersectionSizeTwo(intervals: Array[Array[Int]]): Int = {
        // Sort intervals: primarily by end coordinate ascending.
        // For ties in end coordinate, sort by start coordinate descending.
        // Array.sortWith needs to be used with a custom comparison function.
        intervals.sortWith((a, b) => {
            if (a(1) != b(1)) {
                a(1) < b(1) // Sort by end ascending
            } else {
                a(0) > b(0) // Sort by start descending for ties
            }
        })

        var ans = 0
        var p1 = -1 // Second largest point chosen so far
        var p2 = -1 // Largest point chosen so far

        for (interval <- intervals) {
            val start = interval(0)
            val end = interval(1)

            // Case 1: The current interval [start, end] is fully covered by p1 and p2.
            // This implies start <= p1 (and implicitly start <= p2 since p1 < p2).
            if (start <= p1) {
                // Continue to the next interval
            }
            // Case 2: Only p2 covers the current interval (p1 < start <= p2).
            // We need to add one more point. The best choice is 'end' to maximize coverage.
            else if (start <= p2) { // Implies p1 < start
                ans += 1
                p1 = p2 // The old largest becomes the new second largest
                p2 = end // The new point 'end' becomes the largest
            }
            // Case 3: Neither p1 nor p2 covers the current interval (p2 < start).
            // We need to add two new points. The best choices are 'end-1' and 'end'.
            else { // p2 < start
                ans += 2
                p1 = end - 1
                p2 = end
            }
        }

        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn intersection_size_two(mut intervals: Vec<Vec<i32>>) -> i32 {
        // Sort intervals: primarily by end coordinate ascending.
        // For ties in end coordinate, sort by start coordinate descending.
        intervals.sort_unstable_by(|a, b| {
            if a[1] != b[1] {
                a[1].cmp(&b[1]) // Sort by end ascending
            } else {
                b[0].cmp(&a[0]) // Sort by start descending for ties
            }
        });

        let mut ans = 0;
        let mut p1 = -1; // Second largest point chosen so far
        let mut p2 = -1; // Largest point chosen so far

        for interval in intervals {
            let start = interval[0];
            let end = interval[1];

            // Case 1: The current interval [start, end] is fully covered by p1 and p2.
            // This implies start <= p1 (and implicitly start <= p2 since p1 < p2).
            if start <= p1 {
                continue;
            }
            // Case 2: Only p2 covers the current interval (p1 < start <= p2).
            // We need to add one more point. The best choice is 'end' to maximize coverage.
            else if start <= p2 { // Implies p1 < start
                ans += 1;
                p1 = p2; // The old largest becomes the new second largest
                p2 = end; // The new point 'end' becomes the largest
            }
            // Case 3: Neither p1 nor p2 covers the current interval (p2 < start).
            // We need to add two new points. The best choices are 'end-1' and 'end'.
            else { // p2 < start
                ans += 2;
                p1 = end - 1;
                p2 = end;
            }
        }

        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (intersection-size-two intervals)
  ;; Sort intervals: primarily by end coordinate ascending.
  ;; For ties in end coordinate, sort by start coordinate descending.
  (define sorted-intervals
    (sort intervals (lambda (a b)
                      (let ((end-a (list-ref a 1))
                            (end-b (list-ref b 1)))                       
                        (if (!= end-a end-b)
                            (< end-a end-b) ; Sort by end ascending
                            (> (list-ref a 0) (list-ref b 0))))))) ; Sort by start descending for ties

  (define ans 0)
  (define p1 -1) ; Second largest point chosen so far
  (define p2 -1) ; Largest point chosen so far

  (for ([interval sorted-intervals])
    (define start (list-ref interval 0))
    (define end (list-ref interval 1))

    (cond
      ;; Case 1: The current interval [start, end] is fully covered by p1 and p2.
      ;; This implies start <= p1 (and implicitly start <= p2 since p1 < p2).
      [(<= start p1) (void)] ; No action needed
      ;; Case 2: Only p2 covers the current interval (p1 < start <= p2).
      ;; We need to add one more point. The best choice is 'end' to maximize coverage.
      [(<= start p2) ; Implies p1 < start
       (set! ans (+ ans 1))
       (set! p1 p2) ; The old largest becomes the new second largest
       (set! p2 end)] ; The new point 'end' becomes the largest
      ;; Case 3: Neither p1 nor p2 covers the current interval (p2 < start).
      ;; We need to add two new points. The best choices are 'end-1' and 'end'.
      [else ; This implies p2 < start
       (set! ans (+ ans 2))
       (set! p1 (- end 1))
       (set! p2 end)]))
  ans)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([intersection_size_two/1]).

intersection_size_two(Intervals) ->
    % Sort intervals: primarily by end coordinate ascending.
    % For ties in end coordinate, sort by start coordinate descending.
    SortedIntervals = lists:sort(fun(A, B) ->
        [StartA, EndA] = A,
        [StartB, EndB] = B,
        if EndA =:= EndB -> StartA > StartB; % Sort by start descending for ties
           true        -> EndA < EndB         % Sort by end ascending
        end
    end, Intervals),

    % ans: total count of points
    % p1: second largest point chosen so far
    % p2: largest point chosen so far
    % Initial state: ans = 0, p1 = -1, p2 = -1
    FinalAcc = lists:foldl(fun(Interval, Acc) ->
        [Start, End] = Interval,
        #{ans := CurrentAns, p1 := CurrentP1, p2 := CurrentP2} = Acc,

        if Start =< CurrentP1 ->
            % Case 1: Interval is fully covered. No action.
            Acc;
        Start =< CurrentP2 ->
            % Case 2: Only CurrentP2 covers. Add one point (End).
            Acc#{ans := CurrentAns + 1, p1 := CurrentP2, p2 := End};
        true -> % Implies CurrentP2 < Start
            % Case 3: Neither covers. Add two points (End-1, End).
            Acc#{ans := CurrentAns + 2, p1 := End - 1, p2 := End}
        end
    end, #{ans => 0, p1 => -1, p2 => -1}, SortedIntervals),

    #{ans := FinalAns} = FinalAcc,
    FinalAns.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec intersection_size_two(intervals :: [[integer]]) :: integer
  def intersection_size_two(intervals) do
    # Sort intervals: primarily by end coordinate ascending.
    # For ties in end coordinate, sort by start coordinate descending.
    sorted_intervals = Enum.sort(intervals, fn [start_a, end_a], [start_b, end_b] ->
      if end_a != end_b do
        end_a < end_b # Sort by end ascending
      else
        start_a > start_b # Sort by start descending for ties
      end
    end)

    # ans: total count of points
    # p1: second largest point chosen so far
    # p2: largest point chosen so far
    # Initial state: ans = 0, p1 = -1, p2 = -1
    {ans, _p1, _p2} = Enum.reduce(sorted_intervals, {0, -1, -1}, fn [start, end], {current_ans, p1, p2} ->
      cond do
        # Case 1: The current interval [start, end] is fully covered by p1 and p2.
        # This implies start <= p1 (and implicitly start <= p2 since p1 < p2).
        start <= p1 ->
          {current_ans, p1, p2}
        # Case 2: Only p2 covers the current interval (p1 < start <= p2).
        # We need to add one more point. The best choice is 'end' to maximize coverage.
        start <= p2 -> # Implies p1 < start
          {current_ans + 1, p2, end}
        # Case 3: Neither p1 nor p2 covers the current interval (p2 < start).
        # We need to add two new points. The best choices are 'end-1' and 'end'.
        true -> # Implies p2 < start
          {current_ans + 2, end - 1, end}
      end
    end)

    ans
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log N)

- **Space Complexity:** O(N)

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-20 21:19:44 )</small>
</summary>

<div class="ai-solution-content">

### Approach


The problem requires finding the minimum possible size of a containing set, which is an array where each interval from the given intervals has at least two integers in the array.

To solve this problem, we can use a greedy algorithm. The idea is to sort the intervals by their end points and then try to cover as many intervals as possible with the smallest possible containing set.

We start by sorting the intervals based on their end points. Then, we initialize our containing set with the last two elements of the first interval.

Next, we iterate over the rest of the intervals. For each interval, we check if it is covered by the current containing set. If it is not covered, we add the last two elements of the current interval to the containing set.

We continue this process until we have checked all intervals. The size of the containing set at the end of this process is the minimum possible size of a containing set.

This approach works because we are always trying to cover as many intervals as possible with the smallest possible containing set. By sorting the intervals by their end points and adding the last two elements of each interval to the containing set, we ensure that we are covering as many intervals as possible with the smallest possible containing set.

For example, if the intervals are [[1,3], [3,7], [8,9]], we first sort them by their end points to get [[1,3], [8,9], [3,7]]. Then, we initialize our containing set with the last two elements of the first interval, which are [2, 3]. Next, we check the second interval [8,9] and add its last two elements [8, 9] to the containing set because [8,9] is not covered by [2, 3]. Finally, we check the third interval [3,7] and add its last two elements [6, 7] to the containing set because [3,7] is not covered by [2, 3, 8, 9]. The containing set at the end of this process is [2, 3, 8, 9, 6, 7], which has a size of 6. However, we can further optimize this by noticing that [2, 3, 4, 8, 9] is a smaller containing set that covers all intervals.

The time complexity of this approach is O(n log n) due to the sorting step, where n is the number of intervals. The space complexity is O(n) because in the worst case, we might need to store all intervals in the containing set.

The algorithm logic can be described as follows:
- Sort the intervals by their end points.
- Initialize the containing set with the last two elements of the first interval.
- Iterate over the rest of the intervals and add the last two elements of each interval to the containing set if the interval is not covered by the current containing set.
- Return the size of the containing set at the end of the process.

This approach ensures that we find the minimum possible size of a containing set because we are always trying to cover as many intervals as possible with the smallest possible containing set.



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
#include <algorithm>

using namespace std;

class Solution {
public:
    int intersectionSizeTwo(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });

        vector<int> res;
        for (auto& interval : intervals) {
            if (res.empty() || res.back() < interval[0]) {
                res.push_back(interval[1] - 1);
                res.push_back(interval[1]);
            } else if (res[res.size() - 2] < interval[0]) {
                res.push_back(interval[1]);
            }
        }

        return res.size();
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;

class Solution {
    public int intersectionSizeTwo(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);

        List<Integer> res = new ArrayList<>();
        for (int[] interval : intervals) {
            if (res.isEmpty() || res.get(res.size() - 1) < interval[0]) {
                res.add(interval[1] - 1);
                res.add(interval[1]);
            } else if (res.get(res.size() - 2) < interval[0]) {
                res.add(interval[1]);
            }
        }

        return res.size();
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        res = []
        for interval in intervals:
            if not res or res[-1] < interval[0]:
                res.append(interval[1] - 1)
                res.append(interval[1])
            elif res[-2] < interval[0]:
                res.append(interval[1])

        return len(res)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        res = []
        for interval in intervals:
            if not res or res[-1] < interval[0]:
                res.append(interval[1] - 1)
                res.append(interval[1])
            elif res[-2] < interval[0]:
                res.append(interval[1])

        return len(res)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int start;
    int end;
} Interval;

int compare(const void* a, const void* b) {
    Interval* interval1 = (Interval*)a;
    Interval* interval2 = (Interval*)b;
    return interval1->end - interval2->end;
}

int intersectionSizeTwo(int** intervals, int intervalsSize, int* intervalsColSize) {
    qsort(intervals, intervalsSize, sizeof(int*), compare);

    int* res = (int*)malloc(intervalsSize * 2 * sizeof(int));
    int resSize = 0;
    for (int i = 0; i < intervalsSize; i++) {
        if (resSize == 0 || res[resSize - 1] < intervals[i][0]) {
            res[resSize++] = intervals[i][1] - 1;
            res[resSize++] = intervals[i][1];
        } else if (resSize >= 2 && res[resSize - 2] < intervals[i][0]) {
            res[resSize++] = intervals[i][1];
        }
    }

    int result = resSize;
    free(res);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int IntersectionSizeTwo(int[][] intervals) {
        Array.Sort(intervals, (a, b) => a[1].CompareTo(b[1]));

        List<int> res = new List<int>();
        foreach (var interval in intervals) {
            if (res.Count == 0 || res[res.Count - 1] < interval[0]) {
                res.Add(interval[1] - 1);
                res.Add(interval[1]);
            } else if (res.Count >= 2 && res[res.Count - 2] < interval[0]) {
                res.Add(interval[1]);
            }
        }

        return res.Count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var intersectionSizeTwo = function(intervals) {
    intervals.sort((a, b) => a[1] - b[1]);

    let res = [];
    for (let interval of intervals) {
        if (res.length === 0 || res[res.length - 1] < interval[0]) {
            res.push(interval[1] - 1);
            res.push(interval[1]);
        } else if (res.length >= 2 && res[res.length - 2] < interval[0]) {
            res.push(interval[1]);
        }
    }

    return res.length;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function intersectionSizeTwo(intervals: number[][]): number {
    intervals.sort((a, b) => a[1] - b[1]);

    let res: number[] = [];
    for (let interval of intervals) {
        if (res.length === 0 || res[res.length - 1] < interval[0]) {
            res.push(interval[1] - 1);
            res.push(interval[1]);
        } else if (res.length >= 2 && res[res.length - 2] < interval[0]) {
            res.push(interval[1]);
        }
    }

    return res.length;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
function intersectionSizeTwo($intervals) {
    usort($intervals, function($a, $b) {
        return $a[1] - $b[1];
    });

    $res = array();
    foreach ($intervals as $interval) {
        if (empty($res) || end($res) < $interval[0]) {
            $res[] = $interval[1] - 1;
            $res[] = $interval[1];
        } elseif (count($res) >= 2 && $res[count($res) - 2] < $interval[0]) {
            $res[] = $interval[1];
        }
    }

    return count($res);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func intersectionSizeTwo(_ intervals: [[Int]]) -> Int {
        let sortedIntervals = intervals.sorted { $0[1] < $1[1] }

        var res: [Int] = []
        for interval in sortedIntervals {
            if res.isEmpty || res.last! < interval[0] {
                res.append(interval[1] - 1)
                res.append(interval[1])
            } else if res.count >= 2 && res[res.count - 2] < interval[0] {
                res.append(interval[1])
            }
        }

        return res.count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun intersectionSizeTwo(intervals: Array<IntArray>): Int {
        val sortedIntervals = intervals.sortedBy { it[1] }

        val res = mutableListOf<Int>()
        for (interval in sortedIntervals) {
            if (res.isEmpty() || res.last() < interval[0]) {
                res.add(interval[1] - 1)
                res.add(interval[1])
            } else if (res.size >= 2 && res[res.size - 2] < interval[0]) {
                res.add(interval[1])
            }
        }

        return res.size
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int intersectionSizeTwo(List<List<int>> intervals) {
        intervals.sort((a, b) => a[1].compareTo(b[1]));

        List<int> res = [];
        for (var interval in intervals) {
            if (res.isEmpty || res.last < interval[0]) {
                res.add(interval[1] - 1);
                res.add(interval[1]);
            } else if (res.length >= 2 && res[res.length - 2] < interval[0]) {
                res.add(interval[1]);
            }
        }

        return res.length;
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
	"sort"
)

func intersectionSizeTwo(intervals [][]int) int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][1] < intervals[j][1]
	})

	res := []int{}
	for _, interval := range intervals {
		if len(res) == 0 || res[len(res)-1] < interval[0] {
			res = append(res, interval[1]-1)
			res = append(res, interval[1])
		} else if len(res) >= 2 && res[len(res)-2] < interval[0] {
			res = append(res, interval[1])
		}
	}

	return len(res)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def intersection_size_two(intervals)
    intervals.sort_by! { |a| a[1] }

    res = []
    intervals.each do |interval|
        if res.empty? || res.last < interval[0]
            res.push(interval[1] - 1)
            res.push(interval[1])
        elsif res.size >= 2 && res[-2] < interval[0]
            res.push(interval[1])
        end
    end

    res.size
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def intersectionSizeTwo(intervals: Array[Array[Int]]): Int = {
        val sortedIntervals = intervals.sortBy(_.apply(1))

        var res: List[Int] = Nil
        for (interval <- sortedIntervals) {
            if (res.isEmpty || res.last < interval(0)) {
                res = interval(1) - 1 :: interval(1) :: res
            } else if (res.size >= 2 && res.init.last < interval(0)) {
                res = interval(1) :: res
            }
        }

        res.size
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn intersection_size_two(intervals: Vec<Vec<i32>>) -> i32 {
        let mut intervals: Vec<Vec<i32>> = intervals;
        intervals.sort_by_key(|x| x[1]);

        let mut res: Vec<i32> = Vec::new();
        for interval in intervals {
            if res.is_empty() || *res.last().unwrap() < interval[0] {
                res.push(interval[1] - 1);
                res.push(interval[1]);
            } else if res.len() >= 2 && *res.get(res.len() - 2).unwrap() < interval[0] {
                res.push(interval[1]);
            }
        }

        res.len() as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (intersection-size-two intervals)
    (let* ([sorted-intervals (sort intervals (λ (x y) (< (cadr x) (cadr y))))])
        (let loop ([res '()] [intervals sorted-intervals])
            (cond
                [(null? intervals) (length res)]
                [(or (null? res) (< (car (reverse res)) (caar intervals)))
                    (loop (append res (list (- (cadar intervals) 1) (cadar intervals))) (cdr intervals))]
                [(< (car (reverse (cdr res))) (caar intervals))
                    (loop (append res (list (cadar intervals))) (cdr intervals))]
                [else (loop res (cdr intervals))]))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([intersectionSizeTwo/1]).

intersectionSizeTwo(Intervals) ->
    SortedIntervals = lists:sort(fun({_, End1}, {_, End2}) -> End1 =< End2 end, Intervals),
    intersectionSizeTwo(SortedIntervals, []).

intersectionSizeTwo([], Res) -> length(Res);
intersectionSizeTwo([Interval | Intervals], Res) ->
    case Res of
        [] ->
            intersectionSizeTwo(Intervals, [element(2, Interval) - 1, element(2, Interval)]);
        _ ->
            case length(Res) >= 2 andalso element(1, lists:reverse(Res)) < element(1, Interval) of
                true ->
                    intersectionSizeTwo(Intervals, [element(2, Interval) | Res]);
                false ->
                    intersectionSizeTwo(Intervals, Res)
            end
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def intersection_size_two(intervals) do
        sorted_intervals = Enum.sort(intervals, fn x, y -> elem(x, 1) <= elem(y, 1) end)

        res = []
        Enum.reduce(sorted_intervals, res, fn interval, acc ->
            if Enum.empty?(acc) || List.last(acc) < elem(interval, 0) do
                [elem(interval, 1) - 1, elem(interval, 1)] ++ acc
            else
                if length(acc) >= 2 and List.first(Enum.reverse(acc)) < elem(interval, 0) do
                    [elem(interval, 1)] ++ acc
                else
                    acc
                end
            end
        )
        |> length
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log n) where n is the number of intervals. This is because we are sorting the intervals by their end points, which takes O(n log n) time. The rest of the algorithm takes O(n) time.

- **Space Complexity:** O(n) where n is the number of intervals. This is because in the worst case, we might need to store all intervals in the containing set.

</div>
</details>
