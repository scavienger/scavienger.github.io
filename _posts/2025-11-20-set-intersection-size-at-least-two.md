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

You are given a 2D integer array `intervals` where `intervals[i] = [starti, endi]` represents all the integers from `starti` to `endi` inclusively.

A **containing set** is an array `nums` where each interval from `intervals` has **at least two** integers in `nums`.

  * For example, if `intervals = [[1,3], [3,7], [8,9]]`, then `[1,2,4,7,8,9]` and `[2,3,4,8,9]` are **containing sets**.

Return _the minimum possible size of a containing set_.

**Example 1:**

``` Input: intervals = [[1,3],[3,7],[8,9]] Output: 5 Explanation: let nums = [2, 3, 4, 8, 9]. It can be shown that there cannot be any containing array of size 4. ``` 

**Example 2:**

``` Input: intervals = [[1,3],[1,4],[2,5],[3,5]] Output: 3 Explanation: let nums = [2, 3, 4]. It can be shown that there cannot be any containing array of size 2. ``` 

**Example 3:**

``` Input: intervals = [[1,2],[2,3],[2,4],[4,5]] Output: 5 Explanation: let nums = [1, 2, 3, 4, 5]. It can be shown that there cannot be any containing array of size 4. ``` 

**Constraints:**

  * `1 <= intervals.length <= 3000`
  * `intervals[i].length == 2`
  * `0 <= starti < endi <= 108`

## ✨ AI-Generated Solution (gemini-2.5-flash)

### Approach

The problem asks for the minimum size of a 'containing set' of integers `nums` such that every given interval `[start_i, end_i]` has at least two integers from `nums` within its range. This is a classic greedy problem involving intervals. The core idea is to make choices that are locally optimal and also contribute optimally to satisfying future requirements.

Our greedy strategy relies on sorting the input `intervals`. The most effective sorting order for interval problems often involves sorting by end times. Specifically, we sort the intervals in ascending order of their `end_i` values. If two intervals have the same `end_i`, we sort them by their `start_i` values in descending order. The rationale for this tie-breaking rule is to process 'harder' or 'more constrained' intervals first. An interval with a larger `start_i` for a given `end_i` is 'harder' to satisfy because it offers a smaller valid range `[start_i, end_i]`. By processing it first, we ensure its needs are met, and the chosen points (which will be `end_i-1` and `end_i` or just `end_i`) are as far to the right as possible, maximizing their chances of covering other intervals that share the same `end_i` but have smaller `start_i` values.

After sorting, we iterate through the intervals. We maintain two variables, `p1` and `p2`, which represent the two largest integers we've added to our `nums` set so far (`p1 < p2`). Initially, `p1` and `p2` are set to values smaller than any possible interval start (e.g., -1). We also maintain `ans` to count the total number of integers in `nums`. For each interval `[s, e]` we process:

1.  **If `s > p2`**: This means neither `p1` nor `p2` are within the current interval `[s, e]`. We need to add two new integers to satisfy this interval. To maximize their usefulness for future intervals (which will have `end` values greater than or equal to `e`), we should pick the two largest possible integers within `[s, e]`, which are `e-1` and `e`. We update `ans` by adding 2, and set `p1 = e-1`, `p2 = e`.
2.  **Else if `s > p1`**: This means `p2` is within `[s, e]` (since `s <= p2` must be true), but `p1` is not. We only need to add one more integer. Again, for maximum future coverage, we pick the largest possible integer within `[s, e]` that isn't `p2`, which is `e`. We update `ans` by adding 1, and set `p1 = p2`, `p2 = e`.
3.  **Else (`s <= p1`)**: This implies both `p1` and `p2` are within `[s, e]` (because `p1 < p2`, and `s <= p1` ensures both are covered by `s`). This interval is already satisfied by previously chosen points, so we do nothing. The `ans`, `p1`, `p2` remain unchanged.

By always picking the rightmost points `e-1` and `e` (or just `e`), we ensure that these points are available for the maximum number of subsequent intervals possible (due to the `end` ascending sort). The descending `start` tie-breaker handles overlapping intervals with the same end efficiently. This greedy strategy guarantees the minimum possible size for `nums`.

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
    int intersectionSizeTwo(std::vector<std::vector<int>>& intervals) {
        // Sort intervals: by end ascending, then by start descending
        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            if (a[1] != b[1]) {
                return a[1] < b[1]; // Sort by end ascending
            }
            return a[0] > b[0]; // Sort by start descending
        });

        int ans = 0;
        int p1 = -1; // Smallest of the two largest chosen points
        int p2 = -1; // Largest of the two largest chosen points

        for (const auto& interval : intervals) {
            int s = interval[0];
            int e = interval[1];

            if (s > p2) {
                // Case 1: Neither p1 nor p2 cover the current interval [s, e].
                // We need to add two points. Choose e-1 and e for maximum future coverage.
                ans += 2;
                p1 = e - 1;
                p2 = e;
            } else if (s > p1) {
                // Case 2: Only p2 covers the current interval [s, e] (i.e., s <= p2 but s > p1).
                // We need to add one more point. Choose e for maximum future coverage.
                ans += 1;
                p1 = p2; // Old p2 becomes new p1
                p2 = e;   // New point is e
            }
            // Case 3: s <= p1. Both p1 and p2 cover the current interval [s, e].
            // Do nothing, this interval is already satisfied.
        }

        return ans;
    }
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int intersectionSizeTwo(int[][] intervals) {
        // Sort intervals: by end ascending, then by start descending
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] a, int[] b) {
                if (a[1] != b[1]) {
                    return Integer.compare(a[1], b[1]); // Sort by end ascending
                }
                return Integer.compare(b[0], a[0]); // Sort by start descending
            }
        });

        int ans = 0;
        int p1 = -1; // Smallest of the two largest chosen points
        int p2 = -1; // Largest of the two largest chosen points

        for (int[] interval : intervals) {
            int s = interval[0];
            int e = interval[1];

            if (s > p2) {
                // Case 1: Neither p1 nor p2 cover the current interval [s, e].
                // We need to add two points. Choose e-1 and e for maximum future coverage.
                ans += 2;
                p1 = e - 1;
                p2 = e;
            } else if (s > p1) {
                // Case 2: Only p2 covers the current interval [s, e] (i.e., s <= p2 but s > p1).
                // We need to add one more point. Choose e for maximum future coverage.
                ans += 1;
                p1 = p2; // Old p2 becomes new p1
                p2 = e;   // New point is e
            }
            // Case 3: s <= p1. Both p1 and p2 cover the current interval [s, e].
            // Do nothing, this interval is already satisfied.
        }

        return ans;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
import collections

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort intervals: by end ascending, then by start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))

        ans = 0
        p1 = -1  # Smallest of the two largest chosen points
        p2 = -1  # Largest of the two largest chosen points

        for s, e in intervals:
            if s > p2:
                # Case 1: Neither p1 nor p2 cover the current interval [s, e].
                # We need to add two points. Choose e-1 and e for maximum future coverage.
                ans += 2
                p1 = e - 1
                p2 = e
            elif s > p1:
                # Case 2: Only p2 covers the current interval [s, e] (i.e., s <= p2 but s > p1).
                # We need to add one more point. Choose e for maximum future coverage.
                ans += 1
                p1 = p2  # Old p2 becomes new p1
                p2 = e   # New point is e
            # Case 3: s <= p1. Both p1 and p2 cover the current interval [s, e].
            # Do nothing, this interval is already satisfied.

        return ans
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
import collections

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort intervals: by end ascending, then by start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))

        ans = 0
        p1 = -1  # Smallest of the two largest chosen points
        p2 = -1  # Largest of the two largest chosen points

        for s, e in intervals:
            if s > p2:
                # Case 1: Neither p1 nor p2 cover the current interval [s, e].
                # We need to add two points. Choose e-1 and e for maximum future coverage.
                ans += 2
                p1 = e - 1
                p2 = e
            elif s > p1:
                # Case 2: Only p2 covers the current interval [s, e] (i.e., s <= p2 but s > p1).
                # We need to add one more point. Choose e for maximum future coverage.
                ans += 1
                p1 = p2  # Old p2 becomes new p1
                p2 = e   # New point is e
            # Case 3: s <= p1. Both p1 and p2 cover the current interval [s, e].
            # Do nothing, this interval is already satisfied.

        return ans
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdlib.h> // For qsort

// Define a struct for intervals to make it easier to pass around
typedef struct {
    int start;
    int end;
} Interval;

// Comparison function for qsort
int compareIntervals(const void* a, const void* b) {
    Interval* intervalA = (Interval*)a;
    Interval* intervalB = (Interval*)b;

    if (intervalA->end != intervalB->end) {
        return intervalA->end - intervalB->end; // Sort by end ascending
    }
    return intervalB->start - intervalA->start; // Sort by start descending
}

int intersectionSizeTwo(int** intervals, int intervalsSize, int* intervalsColSize) {
    // Convert int** to Interval* array for easier sorting with qsort
    // Note: intervalsColSize is typically 2 for all sub-arrays, so we can ignore it after validation.
    Interval* intervalStructs = (Interval*)malloc(intervalsSize * sizeof(Interval));
    if (intervalStructs == NULL) {
        // Handle allocation error
        return -1; // Or throw an error, depending on error handling strategy
    }

    for (int i = 0; i < intervalsSize; i++) {
        intervalStructs[i].start = intervals[i][0];
        intervalStructs[i].end = intervals[i][1];
    }

    // Sort intervals: by end ascending, then by start descending
    qsort(intervalStructs, intervalsSize, sizeof(Interval), compareIntervals);

    int ans = 0;
    int p1 = -1; // Smallest of the two largest chosen points
    int p2 = -1; // Largest of the two largest chosen points

    for (int i = 0; i < intervalsSize; i++) {
        int s = intervalStructs[i].start;
        int e = intervalStructs[i].end;

        if (s > p2) {
            // Case 1: Neither p1 nor p2 cover the current interval [s, e].
            // We need to add two points. Choose e-1 and e for maximum future coverage.
            ans += 2;
            p1 = e - 1;
            p2 = e;
        } else if (s > p1) {
            // Case 2: Only p2 covers the current interval [s, e] (i.e., s <= p2 but s > p1).
            // We need to add one more point. Choose e for maximum future coverage.
            ans += 1;
            p1 = p2; // Old p2 becomes new p1
            p2 = e;   // New point is e
        }
        // Case 3: s <= p1. Both p1 and p2 cover the current interval [s, e].
        // Do nothing, this interval is already satisfied.
    }

    free(intervalStructs); // Free the dynamically allocated memory
    return ans;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int IntersectionSizeTwo(int[][] intervals) {
        // Sort intervals: by end ascending, then by start descending
        Array.Sort(intervals, (a, b) => {
            if (a[1] != b[1]) {
                return a[1].CompareTo(b[1]); // Sort by end ascending
            }
            return b[0].CompareTo(a[0]); // Sort by start descending
        });

        int ans = 0;
        int p1 = -1; // Smallest of the two largest chosen points
        int p2 = -1; // Largest of the two largest chosen points

        foreach (int[] interval in intervals) {
            int s = interval[0];
            int e = interval[1];

            if (s > p2) {
                // Case 1: Neither p1 nor p2 cover the current interval [s, e].
                // We need to add two points. Choose e-1 and e for maximum future coverage.
                ans += 2;
                p1 = e - 1;
                p2 = e;
            } else if (s > p1) {
                // Case 2: Only p2 covers the current interval [s, e] (i.e., s <= p2 but s > p1).
                // We need to add one more point. Choose e for maximum future coverage.
                ans += 1;
                p1 = p2; // Old p2 becomes new p1
                p2 = e;   // New point is e
            }
            // Case 3: s <= p1. Both p1 and p2 cover the current interval [s, e].
            // Do nothing, this interval is already satisfied.
        }

        return ans;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
/**
 * @param {number[][]} intervals
 * @return {number}
 */
var intersectionSizeTwo = function(intervals) {
    // Sort intervals: by end ascending, then by start descending
    intervals.sort((a, b) => {
        if (a[1] !== b[1]) {
            return a[1] - b[1]; // Sort by end ascending
        }
        return b[0] - a[0]; // Sort by start descending
    });

    let ans = 0;
    let p1 = -1; // Smallest of the two largest chosen points
    let p2 = -1; // Largest of the two largest chosen points

    for (const interval of intervals) {
        const s = interval[0];
        const e = interval[1];

        if (s > p2) {
            // Case 1: Neither p1 nor p2 cover the current interval [s, e].
            // We need to add two points. Choose e-1 and e for maximum future coverage.
            ans += 2;
            p1 = e - 1;
            p2 = e;
        } else if (s > p1) {
            // Case 2: Only p2 covers the current interval [s, e] (i.e., s <= p2 but s > p1).
            // We need to add one more point. Choose e for maximum future coverage.
            ans += 1;
            p1 = p2; // Old p2 becomes new p1
            p2 = e;   // New point is e
        }
        // Case 3: s <= p1. Both p1 and p2 cover the current interval [s, e].
        // Do nothing, this interval is already satisfied.
    }

    return ans;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function intersectionSizeTwo(intervals: number[][]): number {
    // Sort intervals: by end ascending, then by start descending
    intervals.sort((a: number[], b: number[]) => {
        if (a[1] !== b[1]) {
            return a[1] - b[1]; // Sort by end ascending
        }
        return b[0] - a[0]; // Sort by start descending
    });

    let ans: number = 0;
    let p1: number = -1; // Smallest of the two largest chosen points
    let p2: number = -1; // Largest of the two largest chosen points

    for (const interval of intervals) {
        const s: number = interval[0];
        const e: number = interval[1];

        if (s > p2) {
            // Case 1: Neither p1 nor p2 cover the current interval [s, e].
            // We need to add two points. Choose e-1 and e for maximum future coverage.
            ans += 2;
            p1 = e - 1;
            p2 = e;
        } else if (s > p1) {
            // Case 2: Only p2 covers the current interval [s, e] (i.e., s <= p2 but s > p1).
            // We need to add one more point. Choose e for maximum future coverage.
            ans += 1;
            p1 = p2; // Old p2 becomes new p1
            p2 = e;   // New point is e
        }
        // Case 3: s <= p1. Both p1 and p2 cover the current interval [s, e].
        // Do nothing, this interval is already satisfied.
    }

    return ans;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
<?php

class Solution {

    /**
     * @param int[][] $intervals
     * @return int
     */
    function intersectionSizeTwo(array $intervals): int {
        // Sort intervals: by end ascending, then by start descending
        usort($intervals, function($a, $b) {
            if ($a[1] !== $b[1]) {
                return $a[1] <=> $b[1]; // Sort by end ascending
            }
            return $b[0] <=> $a[0]; // Sort by start descending
        });

        $ans = 0;
        $p1 = -1; // Smallest of the two largest chosen points
        $p2 = -1; // Largest of the two largest chosen points

        foreach ($intervals as $interval) {
            $s = $interval[0];
            $e = $interval[1];

            if ($s > $p2) {
                // Case 1: Neither p1 nor p2 cover the current interval [s, e].
                // We need to add two points. Choose e-1 and e for maximum future coverage.
                $ans += 2;
                $p1 = $e - 1;
                $p2 = $e;
            } elseif ($s > $p1) {
                // Case 2: Only p2 covers the current interval [s, e] (i.e., s <= p2 but s > p1).
                // We need to add one more point. Choose e for maximum future coverage.
                $ans += 1;
                $p1 = $p2; // Old p2 becomes new p1
                $p2 = $e;   // New point is e
            }
            // Case 3: s <= p1. Both p1 and p2 cover the current interval [s, e].
            // Do nothing, this interval is already satisfied.
        }

        return $ans;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution {
    func intersectionSizeTwo(_ intervals: [[Int]]) -> Int {
        // Sort intervals: by end ascending, then by start descending
        let sortedIntervals = intervals.sorted { (a, b) -> Bool in
            if a[1] != b[1] {
                return a[1] < b[1] // Sort by end ascending
            }
            return a[0] > b[0] // Sort by start descending
        }

        var ans = 0
        var p1 = -1 // Smallest of the two largest chosen points
        var p2 = -1 // Largest of the two largest chosen points

        for interval in sortedIntervals {
            let s = interval[0]
            let e = interval[1]

            if s > p2 {
                // Case 1: Neither p1 nor p2 cover the current interval [s, e].
                // We need to add two points. Choose e-1 and e for maximum future coverage.
                ans += 2
                p1 = e - 1
                p2 = e
            } else if s > p1 {
                // Case 2: Only p2 covers the current interval [s, e] (i.e., s <= p2 but s > p1).
                // We need to add one more point. Choose e for maximum future coverage.
                ans += 1
                p1 = p2 // Old p2 becomes new p1
                p2 = e   // New point is e
            }
            // Case 3: s <= p1. Both p1 and p2 cover the current interval [s, e].
            // Do nothing, this interval is already satisfied.
        }

        return ans
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
import java.util.Arrays

class Solution {
    fun intersectionSizeTwo(intervals: Array<IntArray>): Int {
        // Sort intervals: by end ascending, then by start descending
        intervals.sortWith(Comparator { a, b ->
            if (a[1] != b[1]) {
                a[1].compareTo(b[1]) // Sort by end ascending
            } else {
                b[0].compareTo(a[0]) // Sort by start descending
            }
        })

        var ans = 0
        var p1 = -1 // Smallest of the two largest chosen points
        var p2 = -1 // Largest of the two largest chosen points

        for (interval in intervals) {
            val s = interval[0]
            val e = interval[1]

            if (s > p2) {
                // Case 1: Neither p1 nor p2 cover the current interval [s, e].
                // We need to add two points. Choose e-1 and e for maximum future coverage.
                ans += 2
                p1 = e - 1
                p2 = e
            } else if (s > p1) {
                // Case 2: Only p2 covers the current interval [s, e] (i.e., s <= p2 but s > p1).
                // We need to add one more point. Choose e for maximum future coverage.
                ans += 1;
                p1 = p2 // Old p2 becomes new p1
                p2 = e   // New point is e
            }
            // Case 3: s <= p1. Both p1 and p2 cover the current interval [s, e].
            // Do nothing, this interval is already satisfied.
        }

        return ans
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
class Solution {
  int intersectionSizeTwo(List<List<int>> intervals) {
    // Sort intervals: by end ascending, then by start descending
    intervals.sort((a, b) {
      if (a[1] != b[1]) {
        return a[1].compareTo(b[1]); // Sort by end ascending
      }
      return b[0].compareTo(a[0]); // Sort by start descending
    });

    int ans = 0;
    int p1 = -1; // Smallest of the two largest chosen points
    int p2 = -1; // Largest of the two largest chosen points

    for (final interval in intervals) {
      final s = interval[0];
      final e = interval[1];

      if (s > p2) {
        // Case 1: Neither p1 nor p2 cover the current interval [s, e].
        // We need to add two points. Choose e-1 and e for maximum future coverage.
        ans += 2;
        p1 = e - 1;
        p2 = e;
      } else if (s > p1) {
        // Case 2: Only p2 covers the current interval [s, e] (i.e., s <= p2 but s > p1).
        // We need to add one more point. Choose e for maximum future coverage.
        ans += 1;
        p1 = p2; // Old p2 becomes new p1
        p2 = e;   // New point is e
      }
      // Case 3: s <= p1. Both p1 and p2 cover the current interval [s, e].
      // Do nothing, this interval is already satisfied.
    }

    return ans;
  }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
import "sort"

func intersectionSizeTwo(intervals [][]int) int {
    // Sort intervals: by end ascending, then by start descending
    sort.Slice(intervals, func(i, j int) bool {
        if intervals[i][1] != intervals[j][1] {
            return intervals[i][1] < intervals[j][1] // Sort by end ascending
        }
        return intervals[i][0] > intervals[j][0] // Sort by start descending
    })

    ans := 0
    p1 := -1 // Smallest of the two largest chosen points
    p2 := -1 // Largest of the two largest chosen points

    for _, interval := range intervals {
        s := interval[0]
        e := interval[1]

        if s > p2 {
            // Case 1: Neither p1 nor p2 cover the current interval [s, e].
            // We need to add two points. Choose e-1 and e for maximum future coverage.
            ans += 2
            p1 = e - 1
            p2 = e
        } else if s > p1 {
            // Case 2: Only p2 covers the current interval [s, e] (i.e., s <= p2 but s > p1).
            // We need to add one more point. Choose e for maximum future coverage.
            ans += 1;
            p1 = p2 // Old p2 becomes new p1
            p2 = e   // New point is e
        }
        // Case 3: s <= p1. Both p1 and p2 cover the current interval [s, e].
        // Do nothing, this interval is already satisfied.
    }

    return ans
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
# @param {Integer[][]} intervals
# @return {Integer}
def intersection_size_two(intervals)
    # Sort intervals: by end ascending, then by start descending
    intervals.sort! do |a, b|
        if a[1] != b[1]
            a[1] <=> b[1] # Sort by end ascending
        else
            b[0] <=> a[0] # Sort by start descending
        end
    end

    ans = 0
    p1 = -1 # Smallest of the two largest chosen points
    p2 = -1 # Largest of the two largest chosen points

    intervals.each do |interval|
        s = interval[0]
        e = interval[1]

        if s > p2
            # Case 1: Neither p1 nor p2 cover the current interval [s, e].
            # We need to add two points. Choose e-1 and e for maximum future coverage.
            ans += 2
            p1 = e - 1
            p2 = e
        elsif s > p1
            # Case 2: Only p2 covers the current interval [s, e] (i.e., s <= p2 but s > p1).
            # We need to add one more point. Choose e for maximum future coverage.
            ans += 1
            p1 = p2 # Old p2 becomes new p1
            p2 = e   # New point is e
        end
        # Case 3: s <= p1. Both p1 and p2 cover the current interval [s, e].
        # Do nothing, this interval is already satisfied.
    end

    ans
end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
import scala.collection.mutable.ArrayBuffer

object Solution {
    def intersectionSizeTwo(intervals: Array[Array[Int]]): Int = {
        // Sort intervals: by end ascending, then by start descending
        // Scala's sortWith needs to be careful with comparison function for stability
        // Here, a[1] < b[1] handles end ascending, a[0] > b[0] handles start descending
        val sortedIntervals = intervals.sortWith { (a, b) =>
            if (a(1) != b(1)) a(1) < b(1)
            else a(0) > b(0)
        }

        var ans = 0
        var p1 = -1 // Smallest of the two largest chosen points
        var p2 = -1 // Largest of the two largest chosen points

        for (interval <- sortedIntervals) {
            val s = interval(0)
            val e = interval(1)

            if (s > p2) {
                // Case 1: Neither p1 nor p2 cover the current interval [s, e].
                // We need to add two points. Choose e-1 and e for maximum future coverage.
                ans += 2
                p1 = e - 1
                p2 = e
            } else if (s > p1) {
                // Case 2: Only p2 covers the current interval [s, e] (i.e., s <= p2 but s > p1).
                // We need to add one more point. Choose e for maximum future coverage.
                ans += 1;
                p1 = p2 // Old p2 becomes new p1
                p2 = e   // New point is e
            }
            // Case 3: s <= p1. Both p1 and p2 cover the current interval [s, e].
            // Do nothing, this interval is already satisfied.
        }

        ans
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution {
    pub fn intersection_size_two(mut intervals: Vec<Vec<i32>>) -> i32 {
        // Sort intervals: by end ascending, then by start descending
        intervals.sort_by(|a, b| {
            if a[1] != b[1] {
                a[1].cmp(&b[1]) // Sort by end ascending
            } else {
                b[0].cmp(&a[0]) // Sort by start descending
            }
        });

        let mut ans = 0;
        let mut p1 = -1; // Smallest of the two largest chosen points
        let mut p2 = -1; // Largest of the two largest chosen points

        for interval in intervals {
            let s = interval[0];
            let e = interval[1];

            if s > p2 {
                // Case 1: Neither p1 nor p2 cover the current interval [s, e].
                // We need to add two points. Choose e-1 and e for maximum future coverage.
                ans += 2;
                p1 = e - 1;
                p2 = e;
            } else if s > p1 {
                // Case 2: Only p2 covers the current interval [s, e] (i.e., s <= p2 but s > p1).
                // We need to add one more point. Choose e for maximum future coverage.
                ans += 1;
                p1 = p2; // Old p2 becomes new p1
                p2 = e;   // New point is e
            }
            // Case 3: s <= p1. Both p1 and p2 cover the current interval [s, e].
            // Do nothing, this interval is already satisfied.
        }

        ans
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket

(define (intersection-size-two intervals)
  ;; Sort intervals: by end ascending, then by start descending
  (define sorted-intervals
    (sort intervals
          (lambda (a b)
            (let ((end-a (list-ref a 1))
                  (end-b (list-ref b 1)))
              (if (not (= end-a end-b))
                  (< end-a end-b) ; Sort by end ascending
                  (> (list-ref a 0) (list-ref b 0))))))) ; Sort by start descending

  (define ans 0)
  (define p1 -1) ; Smallest of the two largest chosen points
  (define p2 -1) ; Largest of the two largest chosen points

  (for ([interval sorted-intervals])
    (define s (list-ref interval 0))
    (define e (list-ref interval 1))

    (when (> s p2)
      ;; Case 1: Neither p1 nor p2 cover the current interval [s, e].
      ;; We need to add two points. Choose e-1 and e for maximum future coverage.
      (set! ans (+ ans 2))
      (set! p1 (- e 1))
      (set! p2 e))
    (when (and (<= s p2) (> s p1))
      ;; Case 2: Only p2 covers the current interval [s, e] (i.e., s <= p2 but s > p1).
      ;; We need to add one more point. Choose e for maximum future coverage.
      (set! ans (+ ans 1))
      (set! p1 p2) ; Old p2 becomes new p1
      (set! p2 e)))
    ;; Case 3: s <= p1. Both p1 and p2 cover the current interval [s, e].
    ;; Do nothing, this interval is already satisfied.

  ans)
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
-export([intersection_size_two/1]).

intersection_size_two(Intervals) ->
    % Sort intervals: by end ascending, then by start descending
    SortedIntervals = lists:sort(fun(A, B) ->
                                     E_A = element(2, A),
                                     E_B = element(2, B),
                                     S_A = element(1, A),
                                     S_B = element(1, B),
                                     if E_A =/= E_B -> E_A < E_B;
                                        true -> S_A > S_B % Tie-break: start descending
                                     end
                                 end, Intervals),

    intersection_size_two_inner(SortedIntervals, 0, -1, -1).

intersection_size_two_inner([], Ans, _P1, _P2) -> Ans;
intersection_size_two_inner([[S, E] | Rest], Ans, P1, P2) ->
    NewAns = Ans,
    NewP1 = P1,
    NewP2 = P2,

    {UpdatedAns, UpdatedP1, UpdatedP2} =
        if S > NewP2 ->
            % Case 1: Neither P1 nor P2 cover the current interval [S, E].
            % We need to add two points. Choose E-1 and E for maximum future coverage.
            {NewAns + 2, E - 1, E};
        S > NewP1 ->
            % Case 2: Only P2 covers the current interval [S, E] (i.e., S <= P2 but S > P1).
            % We need to add one more point. Choose E for maximum future coverage.
            {NewAns + 1, NewP2, E};
        true ->
            % Case 3: S <= P1. Both P1 and P2 cover the current interval [S, E].
            % Do nothing, this interval is already satisfied.
            {NewAns, NewP1, NewP2}
        end,
    
    intersection_size_two_inner(Rest, UpdatedAns, UpdatedP1, UpdatedP2).
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
  @spec intersection_size_two(intervals :: [[integer]]) :: integer
  def intersection_size_two(intervals) do
    # Sort intervals: by end ascending, then by start descending
    sorted_intervals = 
      Enum.sort(intervals, fn [s1, e1], [s2, e2] ->
        cond do
          e1 != e2 -> e1 < e2  # Sort by end ascending
          true -> s1 > s2      # Sort by start descending
        end
      end)

    do_intersection_size_two(sorted_intervals, 0, -1, -1)
  end

  defp do_intersection_size_two([], ans, _p1, _p2), do: ans
  defp do_intersection_size_two([[s, e] | rest], ans, p1, p2) do
    {new_ans, new_p1, new_p2} =
      cond do
        s > p2 ->
          # Case 1: Neither p1 nor p2 cover the current interval [s, e].
          # We need to add two points. Choose e-1 and e for maximum future coverage.
          {ans + 2, e - 1, e}
        s > p1 ->
          # Case 2: Only p2 covers the current interval [s, e] (i.e., s <= p2 but s > p1).
          # We need to add one more point. Choose e for maximum future coverage.
          {ans + 1, p2, e}
        true ->
          # Case 3: s <= p1. Both p1 and p2 cover the current interval [s, e].
          # Do nothing, this interval is already satisfied.
          {ans, p1, p2}
      end

    do_intersection_size_two(rest, new_ans, new_p1, new_p2)
  end
end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log N) with explanation
- **Space Complexity:** O(N) with explanation
