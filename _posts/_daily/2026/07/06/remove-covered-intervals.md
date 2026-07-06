---
layout: post
title: "Remove Covered Intervals"
date: 2026-07-06 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/remove-covered-intervals/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int removeCoveredIntervals(vector<vector<int>>&\
        \ intervals) {\n        sort(intervals.begin(), intervals.end(), [](const vector<int>&\
        \ a, const vector<int>& b) {\n            if (a[0] == b[0]) return a[1] > b[1];\n\
        \            return a[0] < b[0];\n        });\n\n        int count = 0;\n  \
        \      int max_end = 0;\n        for (const auto& interval : intervals) {\n\
        \            if (interval[1] > max_end) {\n                count++;\n      \
        \          max_end = interval[1];\n            }\n        }\n        return\
        \ count;\n    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public int removeCoveredIntervals(int[][]\
        \ intervals) {\n        Arrays.sort(intervals, (a, b) -> {\n            if (a[0]\
        \ == b[0]) return b[1] - a[1];\n            return a[0] - b[0];\n        });\n\
        \n        int count = 0;\n        int maxEnd = 0;\n        for (int[] interval\
        \ : intervals) {\n            if (interval[1] > maxEnd) {\n                count++;\n\
        \                maxEnd = interval[1];\n            }\n        }\n        return\
        \ count;\n    }\n}"
      python: "class Solution(object):\n    def removeCoveredIntervals(self, intervals):\n\
        \        \"\"\"\n        :type intervals: List[List[int]]\n        :rtype: int\n\
        \        \"\"\"\n        intervals.sort(key=lambda x: (x[0], -x[1]))\n     \
        \   count = 0\n        max_end = 0\n        for _, end in intervals:\n     \
        \       if end > max_end:\n                count += 1\n                max_end\
        \ = end\n        return count"
      python3: "class Solution:\n    def removeCoveredIntervals(self, intervals: List[List[int]])\
        \ -> int:\n        intervals.sort(key=lambda x: (x[0], -x[1]))\n        count\
        \ = 0\n        max_end = 0\n        for _, end in intervals:\n            if\
        \ end > max_end:\n                count += 1\n                max_end = end\n\
        \        return count"
      c: "#include <stdlib.h>\n\nint compareIntervals(const void* a, const void* b)\
        \ {\n    int* i1 = *(int**)a;\n    int* i2 = *(int**)b;\n    if (i1[0] != i2[0])\
        \ return i1[0] - i2[0];\n    return i2[1] - i1[1];\n}\n\nint removeCoveredIntervals(int**\
        \ intervals, int intervalsSize, int* intervalsColSize) {\n    if (intervalsSize\
        \ == 0) return 0;\n    qsort(intervals, intervalsSize, sizeof(int*), compareIntervals);\n\
        \n    int count = 0;\n    int max_end = 0;\n    for (int i = 0; i < intervalsSize;\
        \ i++) {\n        if (intervals[i][1] > max_end) {\n            count++;\n \
        \           max_end = intervals[i][1];\n        }\n    }\n    return count;\n\
        }"
      csharp: "public class Solution {\n    public int RemoveCoveredIntervals(int[][]\
        \ intervals) {\n        System.Array.Sort(intervals, (a, b) => {\n         \
        \   if (a[0] != b[0]) {\n                return a[0].CompareTo(b[0]);\n    \
        \        }\n            return b[1].CompareTo(a[1]);\n        });\n\n      \
        \  int count = 0;\n        int maxEnd = 0;\n        foreach (int[] interval\
        \ in intervals) {\n            if (interval[1] > maxEnd) {\n               \
        \ count++;\n                maxEnd = interval[1];\n            }\n        }\n\
        \        return count;\n    }\n}"
      javascript: "/**\n * @param {number[][]} intervals\n * @return {number}\n */\n\
        var removeCoveredIntervals = function(intervals) {\n    intervals.sort((a, b)\
        \ => {\n        if (a[0] !== b[0]) {\n            return a[0] - b[0];\n    \
        \    }\n        return b[1] - a[1];\n    });\n\n    let count = 0;\n    let\
        \ maxEnd = 0;\n    for (const interval of intervals) {\n        if (interval[1]\
        \ > maxEnd) {\n            count++;\n            maxEnd = interval[1];\n   \
        \     }\n    }\n    return count;\n};"
      typescript: "function removeCoveredIntervals(intervals: number[][]): number {\n\
        \    intervals.sort((a, b) => {\n        if (a[0] !== b[0]) {\n            return\
        \ a[0] - b[0];\n        }\n        return b[1] - a[1];\n    });\n\n    let count\
        \ = 0;\n    let maxEnd = 0;\n    for (const interval of intervals) {\n     \
        \   if (interval[1] > maxEnd) {\n            count++;\n            maxEnd =\
        \ interval[1];\n        }\n    }\n    return count;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $intervals\n    \
        \ * @return Integer\n     */\n    function removeCoveredIntervals($intervals)\
        \ {\n        usort($intervals, function($a, $b) {\n            if ($a[0] !=\
        \ $b[0]) {\n                return $a[0] - $b[0];\n            }\n         \
        \   return $b[1] - $a[1];\n        });\n\n        $count = 0;\n        $maxEnd\
        \ = 0;\n        foreach ($intervals as $interval) {\n            if ($interval[1]\
        \ > $maxEnd) {\n                $count++;\n                $maxEnd = $interval[1];\n\
        \            }\n        }\n        return $count;\n    }\n}"
      swift: "class Solution {\n    func removeCoveredIntervals(_ intervals: [[Int]])\
        \ -> Int {\n        let sortedIntervals = intervals.sorted { (a, b) -> Bool\
        \ in\n            if a[0] != b[0] {\n                return a[0] < b[0]\n  \
        \          } else {\n                return a[1] > b[1]\n            }\n   \
        \     }\n\n        var count = 0\n        var maxEnd = 0\n        for interval\
        \ in sortedIntervals {\n            if interval[1] > maxEnd {\n            \
        \    count += 1\n                maxEnd = interval[1]\n            }\n     \
        \   }\n        return count\n    }\n}"
      kotlin: "import java.util.Comparator\n\nclass Solution {\n    fun removeCoveredIntervals(intervals:\
        \ Array<IntArray>): Int {\n        intervals.sortWith(Comparator { a, b ->\n\
        \            if (a[0] == b[0]) b[1] - a[1] else a[0] - b[0]\n        })\n  \
        \      var count = 0\n        var maxEnd = 0\n        for (interval in intervals)\
        \ {\n            if (interval[1] > maxEnd) {\n                count++\n    \
        \            maxEnd = interval[1]\n            }\n        }\n        return\
        \ count\n    }\n}"
      dart: "class Solution {\n  int removeCoveredIntervals(List<List<int>> intervals)\
        \ {\n    intervals.sort((a, b) {\n      if (a[0] == b[0]) {\n        return\
        \ b[1].compareTo(a[1]);\n      } else {\n        return a[0].compareTo(b[0]);\n\
        \      }\n    });\n    int count = 0;\n    int maxEnd = 0;\n    for (var interval\
        \ in intervals) {\n      if (interval[1] > maxEnd) {\n        count++;\n   \
        \     maxEnd = interval[1];\n      }\n    }\n    return count;\n  }\n}"
      go: "import \"sort\"\n\nfunc removeCoveredIntervals(intervals [][]int) int {\n\
        \    sort.Slice(intervals, func(i, j int) bool {\n        if intervals[i][0]\
        \ == intervals[j][0] {\n            return intervals[i][1] > intervals[j][1]\n\
        \        }\n        return intervals[i][0] < intervals[j][0]\n    })\n    count\
        \ := 0\n    maxEnd := 0\n    for _, interval := range intervals {\n        if\
        \ interval[1] > maxEnd {\n            count++\n            maxEnd = interval[1]\n\
        \        }\n    }\n    return count\n}"
      ruby: "# @param {Integer[][]} intervals\n# @return {Integer}\ndef remove_covered_intervals(intervals)\n\
        \    intervals.sort! { |a, b| a[0] == b[0] ? b[1] <=> a[1] : a[0] <=> b[0] }\n\
        \    count = 0\n    max_end = 0\n    intervals.each do |interval|\n        if\
        \ interval[1] > max_end\n            count += 1\n            max_end = interval[1]\n\
        \        end\n    end\n    count\nend"
      scala: "object Solution {\n    def removeCoveredIntervals(intervals: Array[Array[Int]]):\
        \ Int = {\n        val sorted = intervals.sortWith((a, b) => {\n           \
        \ if (a(0) == b(0)) a(1) > b(1) else a(0) < b(0)\n        })\n        var count\
        \ = 0\n        var maxEnd = 0\n        for (interval <- sorted) {\n        \
        \    if (interval(1) > maxEnd) {\n                count += 1\n             \
        \   maxEnd = interval(1)\n            }\n        }\n        count\n    }\n}"
      rust: "impl Solution {\n    pub fn remove_covered_intervals(intervals: Vec<Vec<i32>>)\
        \ -> i32 {\n        let mut intervals = intervals;\n        intervals.sort_unstable_by(|a,\
        \ b| {\n            if a[0] == b[0] {\n                b[1].cmp(&a[1])\n   \
        \         } else {\n                a[0].cmp(&b[0])\n            }\n       \
        \ });\n\n        let mut count = 0;\n        let mut max_r = 0;\n        for\
        \ interval in intervals {\n            if interval[1] > max_r {\n          \
        \      count += 1;\n                max_r = interval[1];\n            }\n  \
        \      }\n        count\n    }\n}"
      racket: "(define/contract (remove-covered-intervals intervals)\n  (-> (listof\
        \ (listof exact-integer?)) exact-integer?)\n  (let* ([sorted (sort intervals\
        \ (lambda (a b) (if (= (car a) (car b)) (> (cadr a) (cadr b)) (< (car a) (car\
        \ b)))))])\n    (let loop ([rem sorted]\n               [max-r 0]\n        \
        \       [count 0])\n      (if (null? rem)\n          count\n          (let ([r\
        \ (cadr (car rem))])\n            (if (> r max-r)\n                (loop (cdr\
        \ rem) r (+ count 1))\n                (loop (cdr rem) max-r count)))))))"
      erlang: "-spec remove_covered_intervals(Intervals :: [[integer()]]) -> integer().\n\
        remove_covered_intervals(Intervals) ->\n  Sorted = lists:sort(fun([A1, A2],\
        \ [B1, B2]) ->\n                        if A1 < B1 -> true;\n              \
        \             A1 == B1 -> A2 >= B2;\n                           true -> false\n\
        \                        end\n                      end, Intervals),\n  count_rem(Sorted,\
        \ 0, 0).\n\ncount_rem([], _MaxR, Count) ->\n  Count;\ncount_rem([[_, R] | T],\
        \ MaxR, Count) ->\n  if R > MaxR -> count_rem(T, R, Count + 1);\n     true ->\
        \ count_rem(T, MaxR, Count)\n  end."
      elixir: "defmodule Solution do\n  @spec remove_covered_intervals(intervals ::\
        \ [[integer]]) :: integer\n  def remove_covered_intervals(intervals) do\n  \
        \  sorted = Enum.sort(intervals, fn [a1, a2], [b1, b2] ->\n      if a1 == b1\
        \ do\n        a2 >= b2\n      else\n        a1 < b1\n      end\n    end)\n\n\
        \    {final_count, _} = Enum.reduce(sorted, {0, 0}, fn [_, r], {acc_count, acc_max_r}\
        \ ->\n      if r > acc_max_r do\n        {acc_count + 1, r}\n      else\n  \
        \      {acc_count, acc_max_r}\n      end\n    end)\n    final_count\n  end\n\
        end"
    approach: The core strategy is to sort the intervals so that they can be processed
      in a single linear scan. We sort the intervals primarily by their starting point
      in ascending order. When two intervals have the same starting point, we sort them
      by their ending point in descending order. This ensures that for any two intervals
      with the same start, the larger one (which could potentially cover the other)
      comes first. After sorting, we iterate through the list and maintain the maximum
      end position seen so far.
    time_complexity: O(N log N) where N is the number of intervals. This complexity
      is dominated by the sorting step. The subsequent linear scan through the intervals
      to count the non-covered ones takes O(N) time.
    space_complexity: O(N) or O(log N) depending on the programming language and sorting
      implementation. For example, Python and Java use Timsort which requires O(N) auxiliary
      space, while C++'s std::sort typically uses O(log N) stack space for recursion.
    elapsed_time: 168.23123788833618
    model: gemini-3-flash-preview
    generated_at: '2026-07-06 02:31:41 '
---

## Problem #1288: Remove Covered Intervals

**Difficulty:** Medium

**Topics:** Array, Sorting

## Problem Description

<p>Given an array <code>intervals</code> where <code>intervals[i] = [l<sub>i</sub>, r<sub>i</sub>]</code> represent the interval <code>[l<sub>i</sub>, r<sub>i</sub>)</code>, remove all intervals that are covered by another interval in the list.</p>

<p>The interval <code>[a, b)</code> is covered by the interval <code>[c, d)</code> if and only if <code>c &lt;= a</code> and <code>b &lt;= d</code>.</p>

<p>Return <em>the number of remaining intervals</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,4],[3,6],[2,8]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Interval [3,6] is covered by [2,8], therefore it is removed.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,4],[2,3]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 1000</code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= l<sub>i</sub> &lt; r<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li>All the given intervals are <strong>unique</strong>.</li>
</ul>


## Hints

1. How to check if an interval is covered by another?

2. Compare each interval to all others and check if it is covered by any interval.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core strategy is to sort the intervals so that they can be processed in a single linear scan. We sort the intervals primarily by their starting point in ascending order. When two intervals have the same starting point, we sort them by their ending point in descending order. This ensures that for any two intervals with the same start, the larger one (which could potentially cover the other) comes first. After sorting, we iterate through the list and maintain the maximum end position seen so far.

### Code

<div class="code-tabs" markdown="0">
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
{% raw %}
class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            if (a[0] == b[0]) return a[1] > b[1];
            return a[0] < b[0];
        });

        int count = 0;
        int max_end = 0;
        for (const auto& interval : intervals) {
            if (interval[1] > max_end) {
                count++;
                max_end = interval[1];
            }
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

class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            if (a[0] == b[0]) return b[1] - a[1];
            return a[0] - b[0];
        });

        int count = 0;
        int maxEnd = 0;
        for (int[] interval : intervals) {
            if (interval[1] > maxEnd) {
                count++;
                maxEnd = interval[1];
            }
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
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        max_end = 0
        for _, end in intervals:
            if end > max_end:
                count += 1
                max_end = end
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        max_end = 0
        for _, end in intervals:
            if end > max_end:
                count += 1
                max_end = end
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int compareIntervals(const void* a, const void* b) {
    int* i1 = *(int**)a;
    int* i2 = *(int**)b;
    if (i1[0] != i2[0]) return i1[0] - i2[0];
    return i2[1] - i1[1];
}

int removeCoveredIntervals(int** intervals, int intervalsSize, int* intervalsColSize) {
    if (intervalsSize == 0) return 0;
    qsort(intervals, intervalsSize, sizeof(int*), compareIntervals);

    int count = 0;
    int max_end = 0;
    for (int i = 0; i < intervalsSize; i++) {
        if (intervals[i][1] > max_end) {
            count++;
            max_end = intervals[i][1];
        }
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int RemoveCoveredIntervals(int[][] intervals) {
        System.Array.Sort(intervals, (a, b) => {
            if (a[0] != b[0]) {
                return a[0].CompareTo(b[0]);
            }
            return b[1].CompareTo(a[1]);
        });

        int count = 0;
        int maxEnd = 0;
        foreach (int[] interval in intervals) {
            if (interval[1] > maxEnd) {
                count++;
                maxEnd = interval[1];
            }
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
var removeCoveredIntervals = function(intervals) {
    intervals.sort((a, b) => {
        if (a[0] !== b[0]) {
            return a[0] - b[0];
        }
        return b[1] - a[1];
    });

    let count = 0;
    let maxEnd = 0;
    for (const interval of intervals) {
        if (interval[1] > maxEnd) {
            count++;
            maxEnd = interval[1];
        }
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function removeCoveredIntervals(intervals: number[][]): number {
    intervals.sort((a, b) => {
        if (a[0] !== b[0]) {
            return a[0] - b[0];
        }
        return b[1] - a[1];
    });

    let count = 0;
    let maxEnd = 0;
    for (const interval of intervals) {
        if (interval[1] > maxEnd) {
            count++;
            maxEnd = interval[1];
        }
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[][] $intervals
     * @return Integer
     */
    function removeCoveredIntervals($intervals) {
        usort($intervals, function($a, $b) {
            if ($a[0] != $b[0]) {
                return $a[0] - $b[0];
            }
            return $b[1] - $a[1];
        });

        $count = 0;
        $maxEnd = 0;
        foreach ($intervals as $interval) {
            if ($interval[1] > $maxEnd) {
                $count++;
                $maxEnd = $interval[1];
            }
        }
        return $count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func removeCoveredIntervals(_ intervals: [[Int]]) -> Int {
        let sortedIntervals = intervals.sorted { (a, b) -> Bool in
            if a[0] != b[0] {
                return a[0] < b[0]
            } else {
                return a[1] > b[1]
            }
        }

        var count = 0
        var maxEnd = 0
        for interval in sortedIntervals {
            if interval[1] > maxEnd {
                count += 1
                maxEnd = interval[1]
            }
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
import java.util.Comparator

class Solution {
    fun removeCoveredIntervals(intervals: Array<IntArray>): Int {
        intervals.sortWith(Comparator { a, b ->
            if (a[0] == b[0]) b[1] - a[1] else a[0] - b[0]
        })
        var count = 0
        var maxEnd = 0
        for (interval in intervals) {
            if (interval[1] > maxEnd) {
                count++
                maxEnd = interval[1]
            }
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
  int removeCoveredIntervals(List<List<int>> intervals) {
    intervals.sort((a, b) {
      if (a[0] == b[0]) {
        return b[1].compareTo(a[1]);
      } else {
        return a[0].compareTo(b[0]);
      }
    });
    int count = 0;
    int maxEnd = 0;
    for (var interval in intervals) {
      if (interval[1] > maxEnd) {
        count++;
        maxEnd = interval[1];
      }
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

func removeCoveredIntervals(intervals [][]int) int {
    sort.Slice(intervals, func(i, j int) bool {
        if intervals[i][0] == intervals[j][0] {
            return intervals[i][1] > intervals[j][1]
        }
        return intervals[i][0] < intervals[j][0]
    })
    count := 0
    maxEnd := 0
    for _, interval := range intervals {
        if interval[1] > maxEnd {
            count++
            maxEnd = interval[1]
        }
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
def remove_covered_intervals(intervals)
    intervals.sort! { |a, b| a[0] == b[0] ? b[1] <=> a[1] : a[0] <=> b[0] }
    count = 0
    max_end = 0
    intervals.each do |interval|
        if interval[1] > max_end
            count += 1
            max_end = interval[1]
        end
    end
    count
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def removeCoveredIntervals(intervals: Array[Array[Int]]): Int = {
        val sorted = intervals.sortWith((a, b) => {
            if (a(0) == b(0)) a(1) > b(1) else a(0) < b(0)
        })
        var count = 0
        var maxEnd = 0
        for (interval <- sorted) {
            if (interval(1) > maxEnd) {
                count += 1
                maxEnd = interval(1)
            }
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
    pub fn remove_covered_intervals(intervals: Vec<Vec<i32>>) -> i32 {
        let mut intervals = intervals;
        intervals.sort_unstable_by(|a, b| {
            if a[0] == b[0] {
                b[1].cmp(&a[1])
            } else {
                a[0].cmp(&b[0])
            }
        });

        let mut count = 0;
        let mut max_r = 0;
        for interval in intervals {
            if interval[1] > max_r {
                count += 1;
                max_r = interval[1];
            }
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
(define/contract (remove-covered-intervals intervals)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([sorted (sort intervals (lambda (a b) (if (= (car a) (car b)) (> (cadr a) (cadr b)) (< (car a) (car b)))))])
    (let loop ([rem sorted]
               [max-r 0]
               [count 0])
      (if (null? rem)
          count
          (let ([r (cadr (car rem))])
            (if (> r max-r)
                (loop (cdr rem) r (+ count 1))
                (loop (cdr rem) max-r count)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec remove_covered_intervals(Intervals :: [[integer()]]) -> integer().
remove_covered_intervals(Intervals) ->
  Sorted = lists:sort(fun([A1, A2], [B1, B2]) ->
                        if A1 < B1 -> true;
                           A1 == B1 -> A2 >= B2;
                           true -> false
                        end
                      end, Intervals),
  count_rem(Sorted, 0, 0).

count_rem([], _MaxR, Count) ->
  Count;
count_rem([[_, R] | T], MaxR, Count) ->
  if R > MaxR -> count_rem(T, R, Count + 1);
     true -> count_rem(T, MaxR, Count)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec remove_covered_intervals(intervals :: [[integer]]) :: integer
  def remove_covered_intervals(intervals) do
    sorted = Enum.sort(intervals, fn [a1, a2], [b1, b2] ->
      if a1 == b1 do
        a2 >= b2
      else
        a1 < b1
      end
    end)

    {final_count, _} = Enum.reduce(sorted, {0, 0}, fn [_, r], {acc_count, acc_max_r} ->
      if r > acc_max_r do
        {acc_count + 1, r}
      else
        {acc_count, acc_max_r}
      end
    end)
    final_count
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log N) where N is the number of intervals. This complexity is dominated by the sorting step. The subsequent linear scan through the intervals to count the non-covered ones takes O(N) time.
- **Space Complexity:** O(N) or O(log N) depending on the programming language and sorting implementation. For example, Python and Java use Timsort which requires O(N) auxiliary space, while C++'s std::sort typically uses O(log N) stack space for recursion.
