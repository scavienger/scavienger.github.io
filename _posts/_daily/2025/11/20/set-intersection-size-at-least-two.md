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
  <small class="solution-timestamp">(2025-11-24 07:25:49 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the minimum size of a set of integers `nums` such that every given interval `[start_i, end_i]` contains at least two integers from `nums`. This is a classic greedy problem that can be solved by carefully sorting the intervals and iterating through them, making locally optimal choices.

The core idea of the greedy strategy is to process intervals in an order that allows us to make decisions that benefit future intervals as much as possible. We sort the intervals primarily by their `end_i` in ascending order. This ensures that when we consider an interval, it has the smallest possible `end_i` among the remaining intervals, allowing us to 'finish' intervals quickly. For intervals with the same `end_i`, we sort them by their `start_i` in descending order. This tie-breaking rule is crucial: by processing intervals with larger `start_i` first (among those ending at the same point), we are forced to pick points that are further to the right. These rightmost points are then more likely to cover subsequent intervals (which might have smaller `start_i` but the same `end_i`, or larger `end_i`).

We maintain two variables, `p1` and `p2`, representing the two largest points currently in our `nums` set that are relevant to the current interval being processed. `p1` is the second largest point, and `p2` is the largest. Initially, `p1` and `p2` are set to values smaller than any possible interval start (e.g., -1). For each interval `[start, end]` in the sorted list, we check how many of `p1` and `p2` fall within `[start, end]`. If neither `p1` nor `p2` is in `[start, end]` (i.e., `start > p2`), we must add two new points. To maximize their utility for future intervals, we choose `end - 1` and `end`. If only `p2` is in `[start, end]` (i.e., `start > p1` but `start <= p2`), we need one more point, so we add `end`. The new `p1` becomes the old `p2`, and the new `p2` becomes `end`. If both `p1` and `p2` are in `[start, end]` (i.e., `start <= p1`), the interval is already covered, and we add no new points. We increment our total count of points accordingly in each case.

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
        // Sort intervals: by end_i ascending, then by start_i descending
        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            if (a[1] != b[1]) {
                return a[1] < b[1];
            }
            return a[0] > b[0]; // For ties in end_i, sort by start_i descending
        });

        int count = 0;
        // last_two_points stores the two largest points chosen so far
        // p1 is the second largest, p2 is the largest
        // Initialize with values smaller than any possible interval start
        int p1 = -1, p2 = -1; 

        for (const auto& interval : intervals) {
            int start = interval[0];
            int end = interval[1];

            if (start > p2) {
                // Case 1: No points from last_two_points are in the current interval.
                // We need to add two new points. To maximize their utility for future intervals,
                // pick the largest possible points within [start, end], which are end-1 and end.
                count += 2;
                p1 = end - 1;
                p2 = end;
            } else if (start > p1) {
                // Case 2: Only one point (p2) from last_two_points is in the current interval.
                // We need to add one more point. To maximize its utility, pick 'end'.
                count += 1;
                // The new two largest points are p2 and end.
                p1 = p2;
                p2 = end;
            }
            // Case 3: Both p1 and p2 are in the current interval (start <= p1).
            // This interval is already covered. No new points needed.
            // p1 and p2 remain unchanged.
        }

        return count;
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
// Sort intervals: by end_i ascending, then by start_i descending
Arrays.sort(intervals, new Comparator<int[]>() {
    @Override
    public int compare(int[] a, int[] b) {
        if (a[1] != b[1]) {
            return a[1] - b[1];
        }
        return b[0] - a[0]; // For ties in end_i, sort by start_i descending
    }
});

int count = 0;
// last_two_points stores the two largest points chosen so far
// p1 is the second largest, p2 is the largest
// Initialize with values smaller than any possible interval start
int p1 = -1, p2 = -1; 

for (int[] interval : intervals) {
    int start = interval[0];
    int end = interval[1];

    if (start > p2) {
        // Case 1: No points from last_two_points are in the current interval.
        // We need to add two new points. To maximize their utility for future intervals,
        // pick the largest possible points within [start, end], which are end-1 and end.
        count += 2;
        p1 = end - 1;
        p2 = end;
    } else if (start > p1) {
        // Case 2: Only one point (p2) from last_two_points is in the current interval.
        // We need to add one more point. To maximize its utility, pick 'end'.
        count += 1;
        // The new two largest points are p2 and end.
        p1 = p2;
        p2 = end;
    }
    // Case 3: Both p1 and p2 are in the current interval (start <= p1).
    // This interval is already covered. No new points needed.
    // p1 and p2 remain unchanged.
}

return count;
}
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import collections
from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort intervals: by end_i ascending, then by start_i descending
        intervals.sort(key=lambda x: (x[1], -x[0]))

        count = 0
        # last_two_points stores the two largest points chosen so far
        # p1 is the second largest, p2 is the largest
        # Initialize with values smaller than any possible interval start
        p1, p2 = -1, -1 

        for start, end in intervals:
            if start > p2:
                # Case 1: No points from last_two_points are in the current interval.
                # We need to add two new points. To maximize their utility for future intervals,
                # pick the largest possible points within [start, end], which are end-1 and end.
                count += 2
                p1 = end - 1
                p2 = end
            elif start > p1:
                # Case 2: Only one point (p2) from last_two_points is in the current interval.
                # We need to add one more point. To maximize its utility, pick 'end'.
                count += 1
                # The new two largest points are p2 and end.
                p1 = p2
                p2 = end
            # Case 3: Both p1 and p2 are in the current interval (start <= p1).
            # This interval is already covered. No new points needed.
            # p1 and p2 remain unchanged.

        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections
from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort intervals: by end_i ascending, then by start_i descending
        intervals.sort(key=lambda x: (x[1], -x[0]))

        count = 0
        # last_two_points stores the two largest points chosen so far
        # p1 is the second largest, p2 is the largest
        # Initialize with values smaller than any possible interval start
        p1, p2 = -1, -1 

        for start, end in intervals:
            if start > p2:
                # Case 1: No points from last_two_points are in the current interval.
                # We need to add two new points. To maximize their utility for future intervals,
                # pick the largest possible points within [start, end], which are end-1 and end.
                count += 2
                p1 = end - 1;
                p2 = end;
            elif start > p1:
                # Case 2: Only one point (p2) from last_two_points is in the current interval.
                # We need to add one more point. To maximize its utility, pick 'end'.
                count += 1;
                # The new two largest points are p2 and end.
                p1 = p2;
                p2 = end;
            # Case 3: Both p1 and p2 are in the current interval (start <= p1).
            # This interval is already covered. No new points needed.
            # p1 and p2 remain unchanged.

        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h> // For qsort

// Comparison function for qsort
int compareIntervals(const void* a, const void* b) {
    const int* intervalA = *(const int**)a;
    const int* intervalB = *(const int**)b;

    // Sort by end_i ascending
    if (intervalA[1] != intervalB[1]) {
        return intervalA[1] - intervalB[1];
    }
    // For ties in end_i, sort by start_i descending
    return intervalB[0] - intervalA[0];
}

int intersectionSizeTwo(int** intervals, int intervalsSize, int* intervalsColSize) {
    // Sort intervals: by end_i ascending, then by start_i descending
    qsort(intervals, intervalsSize, sizeof(int*), compareIntervals);

    int count = 0;
    // last_two_points stores the two largest points chosen so far
    // p1 is the second largest, p2 is the largest
    // Initialize with values smaller than any possible interval start
    int p1 = -1, p2 = -1; 

    for (int i = 0; i < intervalsSize; ++i) {
        int start = intervals[i][0];
        int end = intervals[i][1];

        if (start > p2) {
            // Case 1: No points from last_two_points are in the current interval.
            // We need to add two new points. To maximize their utility for future intervals,
            // pick the largest possible points within [start, end], which are end-1 and end.
            count += 2;
            p1 = end - 1;
            p2 = end;
        } else if (start > p1) {
            // Case 2: Only one point (p2) from last_two_points is in the current interval.
            // We need to add one more point. To maximize its utility, pick 'end'.
            count += 1;
            // The new two largest points are p2 and end.
            p1 = p2;
            p2 = end;
        }
        // Case 3: Both p1 and p2 are in the current interval (start <= p1).
        // This interval is already covered. No new points needed.
        // p1 and p2 remain unchanged.
    }

    return count;
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
    public int IntersectionSizeTwo(int[][] intervals) {
        // Sort intervals: by end_i ascending, then by start_i descending
        Array.Sort(intervals, (a, b) => {
            if (a[1] != b[1]) {
                return a[1].CompareTo(b[1]);
            }
            return b[0].CompareTo(a[0]); // For ties in end_i, sort by start_i descending
        });

        int count = 0;
        // last_two_points stores the two largest points chosen so far
        // p1 is the second largest, p2 is the largest
        // Initialize with values smaller than any possible interval start
        int p1 = -1, p2 = -1; 

        foreach (int[] interval in intervals) {
            int start = interval[0];
            int end = interval[1];

            if (start > p2) {
                // Case 1: No points from last_two_points are in the current interval.
                // We need to add two new points. To maximize their utility for future intervals,
                // pick the largest possible points within [start, end], which are end-1 and end.
                count += 2;
                p1 = end - 1;
                p2 = end;
            } else if (start > p1) {
                // Case 2: Only one point (p2) from last_two_points is in the current interval.
                // We need to add one more point. To maximize its utility, pick 'end'.
                count += 1;
                // The new two largest points are p2 and end.
                p1 = p2;
                p2 = end;
            }
            // Case 3: Both p1 and p2 are in the current interval (start <= p1).
            // This interval is already covered. No new points needed.
            // p1 and p2 remain unchanged.
        }

        return count;
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
    // Sort intervals: by end_i ascending, then by start_i descending
    intervals.sort((a, b) => {
        if (a[1] !== b[1]) {
            return a[1] - b[1];
        }
        return b[0] - a[0]; // For ties in end_i, sort by start_i descending
    });

    let count = 0;
    // last_two_points stores the two largest points chosen so far
    // p1 is the second largest, p2 is the largest
    // Initialize with values smaller than any possible interval start
    let p1 = -1, p2 = -1; 

    for (const interval of intervals) {
        const start = interval[0];
        const end = interval[1];

        if (start > p2) {
            // Case 1: No points from last_two_points are in the current interval.
            // We need to add two new points. To maximize their utility for future intervals,
            // pick the largest possible points within [start, end], which are end-1 and end.
            count += 2;
            p1 = end - 1;
            p2 = end;
        } else if (start > p1) {
            // Case 2: Only one point (p2) from last_two_points is in the current interval.
            // We need to add one more point. To maximize its utility, pick 'end'.
            count += 1;
            // The new two largest points are p2 and end.
            p1 = p2;
            p2 = end;
        }
        // Case 3: Both p1 and p2 are in the current interval (start <= p1).
        // This interval is already covered. No new points needed.
        // p1 and p2 remain unchanged.
    }

    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function intersectionSizeTwo(intervals: number[][]): number {
    // Sort intervals: by end_i ascending, then by start_i descending
    intervals.sort((a, b) => {
        if (a[1] !== b[1]) {
            return a[1] - b[1];
        }
        return b[0] - a[0]; // For ties in end_i, sort by start_i descending
    });

    let count: number = 0;
    // last_two_points stores the two largest points chosen so far
    // p1 is the second largest, p2 is the largest
    // Initialize with values smaller than any possible interval start
    let p1: number = -1, p2: number = -1; 

    for (const interval of intervals) {
        const start: number = interval[0];
        const end: number = interval[1];

        if (start > p2) {
            // Case 1: No points from last_two_points are in the current interval.
            // We need to add two new points. To maximize their utility for future intervals,
            // pick the largest possible points within [start, end], which are end-1 and end.
            count += 2;
            p1 = end - 1;
            p2 = end;
        } else if (start > p1) {
            // Case 2: Only one point (p2) from last_two_points is in the current interval.
            // We need to add one more point. To maximize its utility, pick 'end'.
            count += 1;
            // The new two largest points are p2 and end.
            p1 = p2;
            p2 = end;
        }
        // Case 3: Both p1 and p2 are in the current interval (start <= p1).
        // This interval is already covered. No new points needed.
        // p1 and p2 remain unchanged.
    }

    return count;
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
    function intersectionSizeTwo(array $intervals): int {
        // Sort intervals: by end_i ascending, then by start_i descending
        usort($intervals, function($a, $b) {
            if ($a[1] != $b[1]) {
                return $a[1] <=> $b[1];
            }
            return $b[0] <=> $a[0]; // For ties in end_i, sort by start_i descending
        });

        $count = 0;
        // last_two_points stores the two largest points chosen so far
        // p1 is the second largest, p2 is the largest
        // Initialize with values smaller than any possible interval start
        $p1 = -1;
        $p2 = -1; 

        foreach ($intervals as $interval) {
            $start = $interval[0];
            $end = $interval[1];

            if ($start > $p2) {
                // Case 1: No points from last_two_points are in the current interval.
                // We need to add two new points. To maximize their utility for future intervals,
                // pick the largest possible points within [start, end], which are end-1 and end.
                $count += 2;
                $p1 = $end - 1;
                $p2 = $end;
            } elseif ($start > $p1) {
                // Case 2: Only one point (p2) from last_two_points is in the current interval.
                // We need to add one more point. To maximize its utility, pick 'end'.
                $count += 1;
                // The new two largest points are p2 and end.
                $p1 = $p2;
                $p2 = $end;
            }
            // Case 3: Both p1 and p2 are in the current interval (start <= p1).
            // This interval is already covered. No new points needed.
            // p1 and p2 remain unchanged.
        }

        return $count;
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
    func intersectionSizeTwo(_ intervals: [[Int]]) -> Int {
        // Sort intervals: by end_i ascending, then by start_i descending
        var sortedIntervals = intervals.sorted { (a, b) -> Bool in
            if a[1] != b[1] {
                return a[1] < b[1]
            }
            return a[0] > b[0] // For ties in end_i, sort by start_i descending
        }

        var count = 0
        // last_two_points stores the two largest points chosen so far
        // p1 is the second largest, p2 is the largest
        // Initialize with values smaller than any possible interval start
        var p1 = -1, p2 = -1 

        for interval in sortedIntervals {
            let start = interval[0]
            let end = interval[1]

            if start > p2 {
                // Case 1: No points from last_two_points are in the current interval.
                // We need to add two new points. To maximize their utility for future intervals,
                // pick the largest possible points within [start, end], which are end-1 and end.
                count += 2
                p1 = end - 1
                p2 = end
            } else if start > p1 {
                // Case 2: Only one point (p2) from last_two_points is in the current interval.
                // We need to add one more point. To maximize its utility, pick 'end'.
                count += 1
                // The new two largest points are p2 and end.
                p1 = p2
                p2 = end
            }
            // Case 3: Both p1 and p2 are in the current interval (start <= p1).
            // This interval is already covered. No new points needed.
            // p1 and p2 remain unchanged.
        }

        return count
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
        // Sort intervals: by end_i ascending, then by start_i descending
        intervals.sortWith(Comparator { a, b ->
            if (a[1] != b[1]) {
                a[1].compareTo(b[1])
            } else {
                b[0].compareTo(a[0]) // For ties in end_i, sort by start_i descending
            }
        })

        var count = 0
        // last_two_points stores the two largest points chosen so far
        // p1 is the second largest, p2 is the largest
        // Initialize with values smaller than any possible interval start
        var p1 = -1
        var p2 = -1 

        for (interval in intervals) {
            val start = interval[0]
            val end = interval[1]

            if (start > p2) {
                // Case 1: No points from last_two_points are in the current interval.
                // We need to add two new points. To maximize their utility for future intervals,
                // pick the largest possible points within [start, end], which are end-1 and end.
                count += 2
                p1 = end - 1
                p2 = end
            } else if (start > p1) {
                // Case 2: Only one point (p2) from last_two_points is in the current interval.
                // We need to add one more point. To maximize its utility, pick 'end'.
                count += 1
                // The new two largest points are p2 and end.
                p1 = p2
                p2 = end
            }
            // Case 3: Both p1 and p2 are in the current interval (start <= p1).
            // This interval is already covered. No new points needed.
            // p1 and p2 remain unchanged.
        }

        return count
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
    // Sort intervals: by end_i ascending, then by start_i descending
    intervals.sort((a, b) {
      if (a[1] != b[1]) {
        return a[1].compareTo(b[1]);
      }
      return b[0].compareTo(a[0]); // For ties in end_i, sort by start_i descending
    });

    int count = 0;
    // last_two_points stores the two largest points chosen so far
    // p1 is the second largest, p2 is the largest
    // Initialize with values smaller than any possible interval start
    int p1 = -1, p2 = -1; 

    for (final interval in intervals) {
      final int start = interval[0];
      final int end = interval[1];

      if (start > p2) {
        // Case 1: No points from last_two_points are in the current interval.
        // We need to add two new points. To maximize their utility for future intervals,
        // pick the largest possible points within [start, end], which are end-1 and end.
        count += 2;
        p1 = end - 1;
        p2 = end;
      } else if (start > p1) {
        // Case 2: Only one point (p2) from last_two_points is in the current interval.
        // We need to add one more point. To maximize its utility, pick 'end'.
        count += 1;
        // The new two largest points are p2 and end.
        p1 = p2;
        p2 = end;
      }
      // Case 3: Both p1 and p2 are in the current interval (start <= p1).
      // This interval is already covered. No new points needed.
      // p1 and p2 remain unchanged.
    }

    return count;
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
    // Sort intervals: by end_i ascending, then by start_i descending
    sort.Slice(intervals, func(i, j int) bool {
        if intervals[i][1] != intervals[j][1] {
            return intervals[i][1] < intervals[j][1]
        }
        return intervals[i][0] > intervals[j][0] // For ties in end_i, sort by start_i descending
    })

    count := 0
    // last_two_points stores the two largest points chosen so far
    // p1 is the second largest, p2 is the largest
    // Initialize with values smaller than any possible interval start
    p1, p2 := -1, -1 

    for _, interval := range intervals {
        start := interval[0]
        end := interval[1]

        if start > p2 {
            // Case 1: No points from last_two_points are in the current interval.
            // We need to add two new points. To maximize their utility for future intervals,
            // pick the largest possible points within [start, end], which are end-1 and end.
            count += 2
            p1 = end - 1
            p2 = end
        } else if start > p1 {
            // Case 2: Only one point (p2) from last_two_points is in the current interval.
            // We need to add one more point. To maximize its utility, pick 'end'.
            count += 1
            // The new two largest points are p2 and end.
            p1 = p2
            p2 = end
        }
        // Case 3: Both p1 and p2 are in the current interval (start <= p1).
        // This interval is already covered. No new points needed.
        // p1 and p2 remain unchanged.
    }

    return count
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
    # Sort intervals: by end_i ascending, then by start_i descending
    intervals.sort_by! { |a| [a[1], -a[0]] }

    count = 0
    # last_two_points stores the two largest points chosen so far
    # p1 is the second largest, p2 is the largest
    # Initialize with values smaller than any possible interval start
    p1, p2 = -1, -1 

    intervals.each do |interval|
        start = interval[0]
        _end = interval[1] # Use _end to avoid conflict with Ruby's 'end' keyword

        if start > p2
            # Case 1: No points from last_two_points are in the current interval.
            # We need to add two new points. To maximize their utility for future intervals,
            # pick the largest possible points within [start, _end], which are _end-1 and _end.
            count += 2
            p1 = _end - 1
            p2 = _end
        elsif start > p1
            # Case 2: Only one point (p2) from last_two_points is in the current interval.
            # We need to add one more point. To maximize its utility, pick '_end'.
            count += 1
            # The new two largest points are p2 and _end.
            p1 = p2
            p2 = _end
        end
        # Case 3: Both p1 and p2 are in the current interval (start <= p1).
        # This interval is already covered. No new points needed.
        # p1 and p2 remain unchanged.
    end

    return count
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
        // Sort intervals: by end_i ascending, then by start_i descending
        val sortedIntervals = intervals.sortBy(interval => (interval(1), -interval(0)))

        var count = 0
        // last_two_points stores the two largest points chosen so far
        // p1 is the second largest, p2 is the largest
        // Initialize with values smaller than any possible interval start
        var p1 = -1
        var p2 = -1 

        for (interval <- sortedIntervals) {
            val start = interval(0)
            val end = interval(1)

            if (start > p2) {
                // Case 1: No points from last_two_points are in the current interval.
                // We need to add two new points. To maximize their utility for future intervals,
                // pick the largest possible points within [start, end], which are end-1 and end.
                count += 2
                p1 = end - 1
                p2 = end
            } else if (start > p1) {
                // Case 2: Only one point (p2) from last_two_points is in the current interval.
                // We need to add one more point. To maximize its utility, pick 'end'.
                count += 1
                // The new two largest points are p2 and end.
                p1 = p2
                p2 = end
            }
            // Case 3: Both p1 and p2 are in the current interval (start <= p1).
            // This interval is already covered. No new points needed.
            // p1 and p2 remain unchanged.
        }

        count
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
        // Sort intervals: by end_i ascending, then by start_i descending
        intervals.sort_by(|a, b| {
            if a[1] != b[1] {
                a[1].cmp(&b[1])
            } else {
                b[0].cmp(&a[0]) // For ties in end_i, sort by start_i descending
            }
        });

        let mut count = 0;
        // last_two_points stores the two largest points chosen so far
        // p1 is the second largest, p2 is the largest
        // Initialize with values smaller than any possible interval start
        let mut p1 = -1;
        let mut p2 = -1; 

        for interval in intervals {
            let start = interval[0];
            let end = interval[1];

            if start > p2 {
                // Case 1: No points from last_two_points are in the current interval.
                // We need to add two new points. To maximize their utility for future intervals,
                // pick the largest possible points within [start, end], which are end-1 and end.
                count += 2;
                p1 = end - 1;
                p2 = end;
            } else if start > p1 {
                // Case 2: Only one point (p2) from last_two_points is in the current interval.
                // We need to add one more point. To maximize its utility, pick 'end'.
                count += 1;
                // The new two largest points are p2 and end.
                p1 = p2;
                p2 = end;
            }
            // Case 3: Both p1 and p2 are in the current interval (start <= p1).
            // This interval is already covered. No new points needed.
            // p1 and p2 remain unchanged.
        }

        count
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
  ;; Sort intervals: by end_i ascending, then by start_i descending
  (define sorted-intervals
    (sort intervals
          (lambda (a b)
            (let ((end-a (second a))
                  (end-b (second b))) 
              (if (not (= end-a end-b))
                  (< end-a end-b)
                  (> (first a) (first b))))))) ; For ties in end_i, sort by start_i descending

  (define count (make-box 0))
  ;; last_two_points stores the two largest points chosen so far
  ;; p1 is the second largest, p2 is the largest
  ;; Initialize with values smaller than any possible interval start
  (define p1 (make-box -1))
  (define p2 (make-box -1))

  (for-each
   (lambda (interval)
     (let ((start (first interval))
           (end (second interval)))
       (cond
         ((> start (unbox p2))
          ;; Case 1: No points from last_two_points are in the current interval.
          ;; We need to add two new points. To maximize their utility for future intervals,
          ;; pick the largest possible points within [start, end], which are end-1 and end.
          (set-box! count (+ (unbox count) 2))
          (set-box! p1 (- end 1))
          (set-box! p2 end))
         ((> start (unbox p1))
          ;; Case 2: Only one point (p2) from last_two_points is in the current interval.
          ;; We need to add one more point. To maximize its utility, pick 'end'.
          (set-box! count (+ (unbox count) 1))
          ;; The new two largest points are p2 and end.
          (set-box! p1 (unbox p2))
          (set-box! p2 end)))))
   sorted-intervals)

  (unbox count))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([intersection_size_two/1]).

intersection_size_two(Intervals) ->
    % Sort intervals: by end_i ascending, then by start_i descending
    SortedIntervals = lists:sort(fun(A, B) ->
                                     EndA = lists:nth(2, A), % A[1]
                                     EndB = lists:nth(2, B), % B[1]
                                     if EndA =/= EndB ->
                                            EndA < EndB;
                                        true ->
                                            lists:nth(1, A) > lists:nth(1, B) % A[0] > B[0]
                                     end
                                 end, Intervals),

    % Use a helper function to iterate and maintain state
    intersection_size_two_helper(SortedIntervals, 0, -1, -1).

intersection_size_two_helper([], Count, _P1, _P2) ->
    Count;
intersection_size_two_helper([H|T], Count, P1, P2) ->
    Start = lists:nth(1, H), % H[0]
    End = lists:nth(2, H),   % H[1]

    if Start > P2 ->
        % Case 1: No points from last_two_points are in the current interval.
        % We need to add two new points. To maximize their utility for future intervals,
        % pick the largest possible points within [Start, End], which are End-1 and End.
        intersection_size_two_helper(T, Count + 2, End - 1, End);
    Start > P1 ->
        % Case 2: Only one point (P2) from last_two_points is in the current interval.
        % We need to add one more point. To maximize its utility, pick 'End'.
        intersection_size_two_helper(T, Count + 1, P2, End);
    true ->
        % Case 3: Both P1 and P2 are in the current interval (Start <= P1).
        % This interval is already covered. No new points needed.
        intersection_size_two_helper(T, Count, P1, P2)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec intersection_size_two(intervals :: [[integer]]) :: integer
  def intersection_size_two(intervals) do
    # Sort intervals: by end_i ascending, then by start_i descending
    sorted_intervals =
      Enum.sort(intervals, fn a, b ->
        end_a = Enum.at(a, 1)
        end_b = Enum.at(b, 1)

        if end_a != end_b do
          end_a < end_b
        else
          Enum.at(a, 0) > Enum.at(b, 0) # For ties in end_i, sort by start_i descending
        end
      end)

    # Use a helper function to iterate and maintain state
    intersection_size_two_helper(sorted_intervals, 0, -1, -1)
  end

  defp intersection_size_two_helper([], count, _p1, _p2), do: count
  defp intersection_size_two_helper([h | t], count, p1, p2) do
    start = Enum.at(h, 0)
    _end = Enum.at(h, 1) # Use _end to avoid conflict with Elixir's 'end' keyword

    cond do
      start > p2 ->
        # Case 1: No points from last_two_points are in the current interval.
        # We need to add two new points. To maximize their utility for future intervals,
        # pick the largest possible points within [start, _end], which are _end-1 and _end.
        intersection_size_two_helper(t, count + 2, _end - 1, _end)
      start > p1 ->
        # Case 2: Only one point (p2) from last_two_points is in the current interval.
        # We need to add one more point. To maximize its utility, pick '_end'.
        intersection_size_two_helper(t, count + 1, p2, _end)
      true ->
        # Case 3: Both p1 and p2 are in the current interval (start <= p1).
        # This interval is already covered. No new points needed.
        intersection_size_two_helper(t, count, p1, p2)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log N) with explanation

- **Space Complexity:** O(N) with explanation

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-24 07:25:55 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by first sorting the intervals based on their end points. Then, we initialize an empty set to store the result. We iterate over the sorted intervals and for each interval, we check if it has at least two elements in the result set. If not, we add the last two elements of the interval to the result set. This approach ensures that each interval has at least two elements in the result set, thus satisfying the condition of a containing set.

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
#include <set>
#include <algorithm>

class Solution {
public:
    int intersectionSizeTwo(std::vector<std::vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[1] < b[1];
        });

        std::set<int> result;
        for (const auto& interval : intervals) {
            if (result.lower_bound(interval[0]) == result.end() || *result.lower_bound(interval[0]) > interval[1] - 1) {
                result.insert(interval[1] - 1);
                result.insert(interval[1]);
            }
        }

        return result.size();
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

        Set<Integer> result = new TreeSet<>();
        for (int[] interval : intervals) {
            if (result.lower(interval[0]) == null || result.lower(interval[0]) > interval[1] - 1) {
                result.add(interval[1] - 1);
                result.add(interval[1]);
            }
        }

        return result.size();
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

        result = set()
        for start, end in intervals:
            if not any(start <= num <= end - 1 for num in result):
                result.add(end - 1)
                result.add(end)

        return len(result)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        result = set()
        for start, end in intervals:
            if not any(start <= num <= end - 1 for num in result):
                result.add(end - 1)
                result.add(end)

        return len(result)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    int *interval1 = (int *)a;
    int *interval2 = (int *)b;
    return interval1[1] - interval2[1];
}

int intersectionSizeTwo(int **intervals, int intervalsSize, int *intervalsColSize) {
    qsort(intervals, intervalsSize, sizeof(int *), compare);

    int *result = (int *)malloc(intervalsSize * 2 * sizeof(int));
    int resultSize = 0;
    for (int i = 0; i < intervalsSize; i++) {
        if (resultSize == 0 || result[resultSize - 1] < intervals[i][0]) {
            result[resultSize++] = intervals[i][1] - 1;
            result[resultSize++] = intervals[i][1];
        } else if (result[resultSize - 1] < intervals[i][1] - 1) {
            result[resultSize++] = intervals[i][1];
        }
    }

    return resultSize;
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

class Solution {
    public int IntersectionSizeTwo(int[][] intervals) {
        Array.Sort(intervals, (a, b) => a[1].CompareTo(b[1]));

        var result = new SortedSet<int>();
        foreach (var interval in intervals) {
            if (!result.Any(num => interval[0] <= num && num <= interval[1] - 1)) {
                result.Add(interval[1] - 1);
                result.Add(interval[1]);
            }
        }

        return result.Count;
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

    var result = new Set();
    for (var i = 0; i < intervals.length; i++) {
        if (!Array.from(result).some(num => intervals[i][0] <= num && num <= intervals[i][1] - 1)) {
            result.add(intervals[i][1] - 1);
            result.add(intervals[i][1]);
        }
    }

    return result.size;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function intersectionSizeTwo(intervals: number[][]): number {
    intervals.sort((a, b) => a[1] - b[1]);

    var result: Set<number> = new Set();
    for (var i = 0; i < intervals.length; i++) {
        if (!Array.from(result).some(num => intervals[i][0] <= num && num <= intervals[i][1] - 1)) {
            result.add(intervals[i][1] - 1);
            result.add(intervals[i][1]);
        }
    }

    return result.size;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function intersectionSizeTwo($intervals) {
        usort($intervals, function($a, $b) {
            return $a[1] - $b[1];
        });

        $result = array();
        foreach ($intervals as $interval) {
            if (!in_array($interval[0], $result) && !in_array($interval[1] - 1, $result)) {
                $result[] = $interval[1] - 1;
                $result[] = $interval[1];
            }
        }

        return count($result);
    }
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

        var result: Set<Int> = []
        for interval in sortedIntervals {
            if !result.contains(where: { interval[0] <= $0 && $0 <= interval[1] - 1 }) {
                result.insert(interval[1] - 1)
                result.insert(interval[1])
            }
        }

        return result.count
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

        val result = mutableSetOf<Int>()
        for (interval in sortedIntervals) {
            if (!result.any { interval[0] <= it && it <= interval[1] - 1 }) {
                result.add(interval[1] - 1)
                result.add(interval[1])
            }
        }

        return result.size
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

      var result = <int>{};
      for (var interval in intervals) {
          if (!result.any((num) => interval[0] <= num && num <= interval[1] - 1)) {
              result.add(interval[1] - 1);
              result.add(interval[1]);
          }
      }

      return result.length;
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
    "sort"
    "fmt"
)

func intersectionSizeTwo(intervals [][]int) int {
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][1] < intervals[j][1]
    })

    result := make(map[int]bool)
    for _, interval := range intervals {
        if !hasTwoElements(result, interval[0], interval[1]) {
            result[interval[1]-1] = true
            result[interval[1]] = true
        }
    }

    return len(result)
}

func hasTwoElements(result map[int]bool, start, end int) bool {
    count := 0
    for num := start; num <= end; num++ {
        if result[num] {
            count++
        }
        if count >= 2 {
            return true
        }
    }
    return false
}

func len(m map[int]bool) int {
    return len(m)
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
    intervals.sort_by! { |a| a[1] }

    result = Set.new
    intervals.each do |interval|
        if !result.any? { |num| interval[0] <= num && num <= interval[1] - 1 }
            result.add(interval[1] - 1)
            result.add(interval[1])
        end
    end

    result.size
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

        var result = Set[Int]()
        for (interval <- sortedIntervals) {
            if (!result.exists(num => interval(0) <= num && num <= interval(1) - 1)) {
                result += interval(1) - 1
                result += interval(1)
            }
        }

        result.size
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
        intervals.sort_unstable_by_key(|x| x[1]);

        let mut result: std::collections::HashSet<i32> = std::collections::HashSet::new();
        for interval in intervals {
            if !result.iter().any(|&num| interval[0] <= num && num <= interval[1] - 1) {
                result.insert(interval[1] - 1);
                result.insert(interval[1]);
            }
        }

        result.len() as i32
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
    (define sorted-intervals (sort intervals (lambda (x y) (< (cadr x) (cadr y)))))
    (define result (set))

    (for-each
        (lambda (interval)
            (unless (exists? (lambda (num) (and (>= num (car interval)) (<= num (- (cadr interval) 1)))) result)
            (set! result (set-add result (- (cadr interval) 1)))
            (set! result (set-add result (cadr interval)))))
        sorted-intervals)

    (set-count result))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).

-export([intersection_size_two/1]).

intersection_size_two(Intervals) ->
    SortedIntervals = lists:sort(fun({_, End1}, {_, End2}) -> End1 =< End2 end, Intervals),
    Result = sets:new(),
    lists:foldl(fun({Start, End}, Set) ->
                        case sets:filter(fun(Num) -> Start =< Num andalso Num =< End - 1 end, Set) of
                            [] ->
                                sets:add_element(End - 1, sets:add_element(End, Set));
                            _ -> Set
                        end
                end, Result, SortedIntervals),
    sets:size(Result).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  def intersection_size_two(intervals) do
      sorted_intervals = Enum.sort(intervals, fn x, y -> Enum.at(x, 1) <= Enum.at(y, 1) end)
      result = MapSet.new()

      Enum.reduce(sorted_intervals, result, fn interval, set ->
          if !Enum.any?(MapSet.to_list(set), fn num -> Enum.at(interval, 0) <= num && num <= Enum.at(interval, 1) - 1 end) do
              MapSet.put(Enum.at(interval, 1) - 1, MapSet.put(Enum.at(interval, 1), set))
          else
              set
          end
      end)
      |> MapSet.size()
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log n) due to the sorting of intervals, where n is the number of intervals. The subsequent for loop runs in O(n) time, but it is dominated by the sorting operation.

- **Space Complexity:** O(n) for storing the result set, where n is the number of intervals. In the worst case, we might need to store all the end points of the intervals in the result set.

</div>
</details>
