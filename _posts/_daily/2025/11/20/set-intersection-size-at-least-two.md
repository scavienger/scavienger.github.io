---
layout: post
title: "Set Intersection Size At Least Two"
date: 2025-11-20 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Greedy", "Sorting"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/set-intersection-size-at-least-two/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int intersectionSizeTwo(vector<vector<int>>&\
        \ intervals) {\n        sort(intervals.begin(), intervals.end(), [](const vector<int>&\
        \ a, const vector<int>& b) {\n            if (a[1] != b[1]) return a[1] < b[1];\n\
        \            return a[0] > b[0];\n        });\n\n        int count = 0;\n  \
        \      int secondLargest = -1;\n        int largest = -1;\n\n        for (const\
        \ auto& interval : intervals) {\n            int start = interval[0];\n    \
        \        int end = interval[1];\n            int contained = 0;\n\n        \
        \    if (secondLargest >= start) ++contained;\n            if (largest >= start)\
        \ ++contained;\n\n            if (contained == 0) {\n                count +=\
        \ 2;\n                secondLargest = end - 1;\n                largest = end;\n\
        \            } else if (contained == 1) {\n                ++count;\n      \
        \          if (largest < start) {\n                    secondLargest = largest;\n\
        \                    largest = end;\n                } else {\n            \
        \        secondLargest = end;\n                }\n            }\n        }\n\
        \n        return count;\n    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public int intersectionSizeTwo(int[][]\
        \ intervals) {\n        Arrays.sort(intervals, (a, b) -> {\n            if (a[1]\
        \ != b[1]) return Integer.compare(a[1], b[1]);\n            return Integer.compare(b[0],\
        \ a[0]);\n        });\n\n        int count = 0;\n        int secondLargest =\
        \ -1;\n        int largest = -1;\n\n        for (int[] interval : intervals)\
        \ {\n            int start = interval[0];\n            int end = interval[1];\n\
        \            int contained = 0;\n\n            if (secondLargest >= start) ++contained;\n\
        \            if (largest >= start) ++contained;\n\n            if (contained\
        \ == 0) {\n                count += 2;\n                secondLargest = end\
        \ - 1;\n                largest = end;\n            } else if (contained ==\
        \ 1) {\n                ++count;\n                if (largest < start) {\n \
        \                   secondLargest = largest;\n                    largest =\
        \ end;\n                } else {\n                    secondLargest = end;\n\
        \                }\n            }\n        }\n\n        return count;\n    }\n\
        }"
      python: "class Solution(object):\n    def intersectionSizeTwo(self, intervals):\n\
        \        \"\"\"\n        :type intervals: List[List[int]]\n        :rtype: int\n\
        \        \"\"\"\n        intervals.sort(key=lambda interval: (interval[1], -interval[0]))\n\
        \n        count = 0\n        second_largest = -1\n        largest = -1\n\n \
        \       for start, end in intervals:\n            contained = int(second_largest\
        \ >= start) + int(largest >= start)\n\n            if contained == 0:\n    \
        \            count += 2\n                second_largest = end - 1\n        \
        \        largest = end\n            elif contained == 1:\n                count\
        \ += 1\n                if largest < start:\n                    second_largest\
        \ = largest\n                    largest = end\n                else:\n    \
        \                second_largest = end\n\n        return count"
      python3: "class Solution:\n    def intersectionSizeTwo(self, intervals: list[list[int]])\
        \ -> int:\n        intervals.sort(key=lambda interval: (interval[1], -interval[0]))\n\
        \n        count = 0\n        second_largest = -1\n        largest = -1\n\n \
        \       for start, end in intervals:\n            contained = int(second_largest\
        \ >= start) + int(largest >= start)\n\n            if contained == 0:\n    \
        \            count += 2\n                second_largest = end - 1\n        \
        \        largest = end\n            elif contained == 1:\n                count\
        \ += 1\n                if largest < start:\n                    second_largest\
        \ = largest\n                    largest = end\n                else:\n    \
        \                second_largest = end\n\n        return count"
      c: "#include <stdlib.h>\n\nstatic int compareIntervals(const void* first, const\
        \ void* second) {\n    const int* a = *(const int**)first;\n    const int* b\
        \ = *(const int**)second;\n\n    if (a[1] < b[1]) return -1;\n    if (a[1] >\
        \ b[1]) return 1;\n    if (a[0] > b[0]) return -1;\n    if (a[0] < b[0]) return\
        \ 1;\n    return 0;\n}\n\nint intersectionSizeTwo(int** intervals, int intervalsSize,\
        \ int* intervalsColSize) {\n    qsort(intervals, intervalsSize, sizeof(int*),\
        \ compareIntervals);\n\n    int count = 0;\n    int secondLargest = -1;\n  \
        \  int largest = -1;\n\n    for (int i = 0; i < intervalsSize; i++) {\n    \
        \    int start = intervals[i][0];\n        int end = intervals[i][1];\n    \
        \    int contained = (secondLargest >= start) + (largest >= start);\n\n    \
        \    if (contained == 0) {\n            count += 2;\n            secondLargest\
        \ = end - 1;\n            largest = end;\n        } else if (contained == 1)\
        \ {\n            count++;\n            if (largest < start) {\n            \
        \    secondLargest = largest;\n                largest = end;\n            }\
        \ else {\n                secondLargest = end;\n            }\n        }\n \
        \   }\n\n    return count;\n}"
      csharp: "public class Solution {\n    public int IntersectionSizeTwo(int[][] intervals)\
        \ {\n        System.Array.Sort(intervals, (a, b) => {\n            int endComparison\
        \ = a[1].CompareTo(b[1]);\n            if (endComparison != 0) return endComparison;\n\
        \            return b[0].CompareTo(a[0]);\n        });\n\n        int count\
        \ = 0;\n        int secondLargest = -1;\n        int largest = -1;\n\n     \
        \   foreach (int[] interval in intervals) {\n            int start = interval[0];\n\
        \            int end = interval[1];\n            int contained = (secondLargest\
        \ >= start ? 1 : 0) + (largest >= start ? 1 : 0);\n\n            if (contained\
        \ == 0) {\n                count += 2;\n                secondLargest = end\
        \ - 1;\n                largest = end;\n            } else if (contained ==\
        \ 1) {\n                count++;\n                if (largest < start) {\n \
        \                   secondLargest = largest;\n                    largest =\
        \ end;\n                } else {\n                    secondLargest = end;\n\
        \                }\n            }\n        }\n\n        return count;\n    }\n\
        }"
      javascript: "/**\n * @param {number[][]} intervals\n * @return {number}\n */\n\
        var intersectionSizeTwo = function(intervals) {\n    intervals.sort((a, b) =>\
        \ a[1] - b[1] || b[0] - a[0]);\n\n    let count = 0;\n    let secondLargest\
        \ = -1;\n    let largest = -1;\n\n    for (const [start, end] of intervals)\
        \ {\n        const contained = (secondLargest >= start ? 1 : 0) + (largest >=\
        \ start ? 1 : 0);\n\n        if (contained === 0) {\n            count += 2;\n\
        \            secondLargest = end - 1;\n            largest = end;\n        }\
        \ else if (contained === 1) {\n            count++;\n            if (largest\
        \ < start) {\n                secondLargest = largest;\n                largest\
        \ = end;\n            } else {\n                secondLargest = end;\n     \
        \       }\n        }\n    }\n\n    return count;\n};"
      typescript: "function intersectionSizeTwo(intervals: number[][]): number {\n \
        \   intervals.sort((a, b) => a[1] - b[1] || b[0] - a[0]);\n\n    let count =\
        \ 0;\n    let secondLargest = -1;\n    let largest = -1;\n\n    for (const [start,\
        \ end] of intervals) {\n        const contained = Number(secondLargest >= start)\
        \ + Number(largest >= start);\n\n        if (contained === 0) {\n          \
        \  count += 2;\n            secondLargest = end - 1;\n            largest =\
        \ end;\n        } else if (contained === 1) {\n            count += 1;\n   \
        \         if (largest < start) {\n                secondLargest = largest;\n\
        \                largest = end;\n            } else {\n                secondLargest\
        \ = end;\n            }\n        }\n    }\n\n    return count;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $intervals\n    \
        \ * @return Integer\n     */\n    function intersectionSizeTwo($intervals) {\n\
        \        usort($intervals, function ($a, $b) {\n            if ($a[1] === $b[1])\
        \ {\n                return $b[0] <=> $a[0];\n            }\n            return\
        \ $a[1] <=> $b[1];\n        });\n\n        $count = 0;\n        $secondLargest\
        \ = -1;\n        $largest = -1;\n\n        foreach ($intervals as $interval)\
        \ {\n            [$start, $end] = $interval;\n            $contained = (int)($secondLargest\
        \ >= $start) + (int)($largest >= $start);\n\n            if ($contained ===\
        \ 0) {\n                $count += 2;\n                $secondLargest = $end\
        \ - 1;\n                $largest = $end;\n            } elseif ($contained ===\
        \ 1) {\n                $count++;\n                if ($largest < $start) {\n\
        \                    $secondLargest = $largest;\n                    $largest\
        \ = $end;\n                } else {\n                    $secondLargest = $end;\n\
        \                }\n            }\n        }\n\n        return $count;\n   \
        \ }\n}"
      swift: "class Solution {\n    func intersectionSizeTwo(_ intervals: [[Int]]) ->\
        \ Int {\n        let sortedIntervals = intervals.sorted {\n            if $0[1]\
        \ == $1[1] {\n                return $0[0] > $1[0]\n            }\n        \
        \    return $0[1] < $1[1]\n        }\n\n        var count = 0\n        var secondLargest\
        \ = -1\n        var largest = -1\n\n        for interval in sortedIntervals\
        \ {\n            let start = interval[0]\n            let end = interval[1]\n\
        \            let contained = (secondLargest >= start ? 1 : 0) + (largest >=\
        \ start ? 1 : 0)\n\n            if contained == 0 {\n                count +=\
        \ 2\n                secondLargest = end - 1\n                largest = end\n\
        \            } else if contained == 1 {\n                count += 1\n      \
        \          if largest < start {\n                    secondLargest = largest\n\
        \                    largest = end\n                } else {\n             \
        \       secondLargest = end\n                }\n            }\n        }\n\n\
        \        return count\n    }\n}"
      kotlin: "class Solution {\n    fun intersectionSizeTwo(intervals: Array<IntArray>):\
        \ Int {\n        intervals.sortWith(compareBy<IntArray> { it[1] }.thenByDescending\
        \ { it[0] })\n\n        var count = 0\n        var secondLargest = -1\n    \
        \    var largest = -1\n\n        for (interval in intervals) {\n           \
        \ val start = interval[0]\n            val end = interval[1]\n            val\
        \ contained = (if (secondLargest >= start) 1 else 0) + (if (largest >= start)\
        \ 1 else 0)\n\n            if (contained == 0) {\n                count += 2\n\
        \                secondLargest = end - 1\n                largest = end\n  \
        \          } else if (contained == 1) {\n                count++\n         \
        \       if (largest < start) {\n                    secondLargest = largest\n\
        \                    largest = end\n                } else {\n             \
        \       secondLargest = end\n                }\n            }\n        }\n\n\
        \        return count\n    }\n}"
      dart: "class Solution {\n  int intersectionSizeTwo(List<List<int>> intervals)\
        \ {\n    intervals.sort((a, b) {\n      final endComparison = a[1].compareTo(b[1]);\n\
        \      if (endComparison != 0) return endComparison;\n      return b[0].compareTo(a[0]);\n\
        \    });\n\n    var count = 0;\n    var secondLargest = -1;\n    var largest\
        \ = -1;\n\n    for (final interval in intervals) {\n      final start = interval[0];\n\
        \      final end = interval[1];\n      final contained = (secondLargest >= start\
        \ ? 1 : 0) +\n          (largest >= start ? 1 : 0);\n\n      if (contained ==\
        \ 0) {\n        count += 2;\n        secondLargest = end - 1;\n        largest\
        \ = end;\n      } else if (contained == 1) {\n        count += 1;\n        if\
        \ (largest < start) {\n          secondLargest = largest;\n          largest\
        \ = end;\n        } else {\n          secondLargest = end;\n        }\n    \
        \  }\n    }\n\n    return count;\n  }\n}"
      go: "func intersectionSizeTwo(intervals [][]int) int {\n\tsort.Slice(intervals,\
        \ func(i, j int) bool {\n\t\tif intervals[i][1] != intervals[j][1] {\n\t\t\t\
        return intervals[i][1] < intervals[j][1]\n\t\t}\n\t\treturn intervals[i][0]\
        \ > intervals[j][0]\n\t})\n\n\tcount := 0\n\tsecondLargest := -1\n\tlargest\
        \ := -1\n\n\tfor _, interval := range intervals {\n\t\tstart, end := interval[0],\
        \ interval[1]\n\t\tcontained := 0\n\t\tif secondLargest >= start {\n\t\t\tcontained++\n\
        \t\t}\n\t\tif largest >= start {\n\t\t\tcontained++\n\t\t}\n\n\t\tif contained\
        \ == 0 {\n\t\t\tcount += 2\n\t\t\tsecondLargest = end - 1\n\t\t\tlargest = end\n\
        \t\t} else if contained == 1 {\n\t\t\tcount++\n\t\t\tif largest < start {\n\t\
        \t\t\tsecondLargest = largest\n\t\t\t\tlargest = end\n\t\t\t} else {\n\t\t\t\
        \tsecondLargest = end\n\t\t\t}\n\t\t}\n\t}\n\n\treturn count\n}"
      ruby: "# @param {Integer[][]} intervals\n# @return {Integer}\ndef intersection_size_two(intervals)\n\
        \  intervals.sort_by! { |interval| [interval[1], -interval[0]] }\n\n  count\
        \ = 0\n  second_largest = -1\n  largest = -1\n\n  intervals.each do |start,\
        \ finish|\n    contained = (second_largest >= start ? 1 : 0) + (largest >= start\
        \ ? 1 : 0)\n\n    if contained == 0\n      count += 2\n      second_largest\
        \ = finish - 1\n      largest = finish\n    elsif contained == 1\n      count\
        \ += 1\n      if largest < start\n        second_largest = largest\n       \
        \ largest = finish\n      else\n        second_largest = finish\n      end\n\
        \    end\n  end\n\n  count\nend"
      scala: "object Solution {\n    def intersectionSizeTwo(intervals: Array[Array[Int]]):\
        \ Int = {\n        scala.util.Sorting.stableSort(intervals, (a: Array[Int],\
        \ b: Array[Int]) => {\n            if (a(1) != b(1)) a(1) < b(1) else a(0) >\
        \ b(0)\n        })\n\n        var count = 0\n        var secondLargest = -1\n\
        \        var largest = -1\n\n        for (interval <- intervals) {\n       \
        \     val start = interval(0)\n            val end = interval(1)\n         \
        \   val contained = (if (secondLargest >= start) 1 else 0) +\n             \
        \   (if (largest >= start) 1 else 0)\n\n            if (contained == 0) {\n\
        \                count += 2\n                secondLargest = end - 1\n     \
        \           largest = end\n            } else if (contained == 1) {\n      \
        \          count += 1\n                if (largest < start) {\n            \
        \        secondLargest = largest\n                    largest = end\n      \
        \          } else {\n                    secondLargest = end\n             \
        \   }\n            }\n        }\n\n        count\n    }\n}"
      rust: "impl Solution {\n    pub fn intersection_size_two(mut intervals: Vec<Vec<i32>>)\
        \ -> i32 {\n        intervals.sort_by(|a, b| a[1].cmp(&b[1]).then_with(|| b[0].cmp(&a[0])));\n\
        \n        let mut count = 0;\n        let mut second_largest = -1;\n       \
        \ let mut largest = -1;\n\n        for interval in intervals {\n           \
        \ let start = interval[0];\n            let end = interval[1];\n           \
        \ let contained = i32::from(second_largest >= start) + i32::from(largest >=\
        \ start);\n\n            if contained == 0 {\n                count += 2;\n\
        \                second_largest = end - 1;\n                largest = end;\n\
        \            } else if contained == 1 {\n                count += 1;\n     \
        \           if largest < start {\n                    second_largest = largest;\n\
        \                    largest = end;\n                } else {\n            \
        \        second_largest = end;\n                }\n            }\n        }\n\
        \n        count\n    }\n}"
      racket: "(define/contract (intersection-size-two intervals)\n  (-> (listof (listof\
        \ exact-integer?)) exact-integer?)\n  (define sorted-intervals\n    (sort intervals\n\
        \          (lambda (a b)\n            (or (< (second a) (second b))\n      \
        \          (and (= (second a) (second b))\n                     (> (first a)\
        \ (first b)))))))\n  (let loop ([remaining sorted-intervals]\n             [count\
        \ 0]\n             [second-largest -1]\n             [largest -1])\n    (if\
        \ (null? remaining)\n        count\n        (let* ([interval (car remaining)]\n\
        \               [start (first interval)]\n               [end (second interval)]\n\
        \               [contained (+ (if (>= second-largest start) 1 0)\n         \
        \                    (if (>= largest start) 1 0))])\n          (cond\n     \
        \       [(= contained 0)\n             (loop (cdr remaining) (+ count 2) (-\
        \ end 1) end)]\n            [(= contained 1)\n             (if (< largest start)\n\
        \                 (loop (cdr remaining) (+ count 1) largest end)\n         \
        \        (loop (cdr remaining) (+ count 1) end largest))]\n            [else\n\
        \             (loop (cdr remaining) count second-largest largest)])))))"
      erlang: "-spec intersection_size_two(Intervals :: [[integer()]]) -> integer().\n\
        intersection_size_two(Intervals) ->\n  Sorted = lists:sort(\n    fun([StartA,\
        \ EndA], [StartB, EndB]) ->\n      EndA < EndB orelse (EndA =:= EndB andalso\
        \ StartA > StartB)\n    end,\n    Intervals\n  ),\n  intersection_size_two_loop(Sorted,\
        \ 0, -1, -1).\n\nintersection_size_two_loop([], Count, _SecondLargest, _Largest)\
        \ ->\n  Count;\nintersection_size_two_loop([[Start, End] | Rest], Count, SecondLargest,\
        \ Largest) ->\n  Contained = (if SecondLargest >= Start -> 1; true -> 0 end)\
        \ +\n              (if Largest >= Start -> 1; true -> 0 end),\n  case Contained\
        \ of\n    0 -> intersection_size_two_loop(Rest, Count + 2, End - 1, End);\n\
        \    1 when Largest < Start -> intersection_size_two_loop(Rest, Count + 1, Largest,\
        \ End);\n    1 -> intersection_size_two_loop(Rest, Count + 1, End, Largest);\n\
        \    _ -> intersection_size_two_loop(Rest, Count, SecondLargest, Largest)\n\
        \  end."
      elixir: "defmodule Solution do\n  @spec intersection_size_two(intervals :: [[integer]])\
        \ :: integer\n  def intersection_size_two(intervals) do\n    sorted_intervals\
        \ =\n      Enum.sort_by(intervals, fn [start, ending] -> {ending, -start} end)\n\
        \n    process(sorted_intervals, 0, -1, -1)\n  end\n\n  defp process([], count,\
        \ _second_largest, _largest), do: count\n\n  defp process([[start, ending] |\
        \ rest], count, second_largest, largest) do\n    contained =\n      (if second_largest\
        \ >= start, do: 1, else: 0) +\n        (if largest >= start, do: 1, else: 0)\n\
        \n    case contained do\n      0 -> process(rest, count + 2, ending - 1, ending)\n\
        \      1 when largest < start -> process(rest, count + 1, largest, ending)\n\
        \      1 -> process(rest, count + 1, ending, largest)\n      _ -> process(rest,\
        \ count, second_largest, largest)\n    end\n  end\nend"
    approach: 'Sort the intervals by increasing end; for equal ends, sort by decreasing
      start. This processes tighter intervals before wider ones that share an endpoint.


      Track the two largest selected integers, a and b. For each interval, count how
      many of them it already contains. If it contains fewer than two, greedily add
      the missing integers at the interval''s right endpoint, choosing the largest available
      values. These choices are optimal because they are most likely to satisfy later
      intervals, whose endpoints are no smaller.'
    time_complexity: O(n log n), due to sorting the n intervals; the greedy scan takes
      O(n).
    space_complexity: O(1) auxiliary space beyond the storage used by the sorting implementation.
    elapsed_time: 111.93393731117249
    model: gpt-6-luna
    generated_at: '2026-11-13 00:07:42 '
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


## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

Sort the intervals by increasing end; for equal ends, sort by decreasing start. This processes tighter intervals before wider ones that share an endpoint.

Track the two largest selected integers, a and b. For each interval, count how many of them it already contains. If it contains fewer than two, greedily add the missing integers at the interval's right endpoint, choosing the largest available values. These choices are optimal because they are most likely to satisfy later intervals, whose endpoints are no smaller.

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
    int intersectionSizeTwo(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            if (a[1] != b[1]) return a[1] < b[1];
            return a[0] > b[0];
        });

        int count = 0;
        int secondLargest = -1;
        int largest = -1;

        for (const auto& interval : intervals) {
            int start = interval[0];
            int end = interval[1];
            int contained = 0;

            if (secondLargest >= start) ++contained;
            if (largest >= start) ++contained;

            if (contained == 0) {
                count += 2;
                secondLargest = end - 1;
                largest = end;
            } else if (contained == 1) {
                ++count;
                if (largest < start) {
                    secondLargest = largest;
                    largest = end;
                } else {
                    secondLargest = end;
                }
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
    public int intersectionSizeTwo(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            if (a[1] != b[1]) return Integer.compare(a[1], b[1]);
            return Integer.compare(b[0], a[0]);
        });

        int count = 0;
        int secondLargest = -1;
        int largest = -1;

        for (int[] interval : intervals) {
            int start = interval[0];
            int end = interval[1];
            int contained = 0;

            if (secondLargest >= start) ++contained;
            if (largest >= start) ++contained;

            if (contained == 0) {
                count += 2;
                secondLargest = end - 1;
                largest = end;
            } else if (contained == 1) {
                ++count;
                if (largest < start) {
                    secondLargest = largest;
                    largest = end;
                } else {
                    secondLargest = end;
                }
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
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda interval: (interval[1], -interval[0]))

        count = 0
        second_largest = -1
        largest = -1

        for start, end in intervals:
            contained = int(second_largest >= start) + int(largest >= start)

            if contained == 0:
                count += 2
                second_largest = end - 1
                largest = end
            elif contained == 1:
                count += 1
                if largest < start:
                    second_largest = largest
                    largest = end
                else:
                    second_largest = end

        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[1], -interval[0]))

        count = 0
        second_largest = -1
        largest = -1

        for start, end in intervals:
            contained = int(second_largest >= start) + int(largest >= start)

            if contained == 0:
                count += 2
                second_largest = end - 1
                largest = end
            elif contained == 1:
                count += 1
                if largest < start:
                    second_largest = largest
                    largest = end
                else:
                    second_largest = end

        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

static int compareIntervals(const void* first, const void* second) {
    const int* a = *(const int**)first;
    const int* b = *(const int**)second;

    if (a[1] < b[1]) return -1;
    if (a[1] > b[1]) return 1;
    if (a[0] > b[0]) return -1;
    if (a[0] < b[0]) return 1;
    return 0;
}

int intersectionSizeTwo(int** intervals, int intervalsSize, int* intervalsColSize) {
    qsort(intervals, intervalsSize, sizeof(int*), compareIntervals);

    int count = 0;
    int secondLargest = -1;
    int largest = -1;

    for (int i = 0; i < intervalsSize; i++) {
        int start = intervals[i][0];
        int end = intervals[i][1];
        int contained = (secondLargest >= start) + (largest >= start);

        if (contained == 0) {
            count += 2;
            secondLargest = end - 1;
            largest = end;
        } else if (contained == 1) {
            count++;
            if (largest < start) {
                secondLargest = largest;
                largest = end;
            } else {
                secondLargest = end;
            }
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
    public int IntersectionSizeTwo(int[][] intervals) {
        System.Array.Sort(intervals, (a, b) => {
            int endComparison = a[1].CompareTo(b[1]);
            if (endComparison != 0) return endComparison;
            return b[0].CompareTo(a[0]);
        });

        int count = 0;
        int secondLargest = -1;
        int largest = -1;

        foreach (int[] interval in intervals) {
            int start = interval[0];
            int end = interval[1];
            int contained = (secondLargest >= start ? 1 : 0) + (largest >= start ? 1 : 0);

            if (contained == 0) {
                count += 2;
                secondLargest = end - 1;
                largest = end;
            } else if (contained == 1) {
                count++;
                if (largest < start) {
                    secondLargest = largest;
                    largest = end;
                } else {
                    secondLargest = end;
                }
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
var intersectionSizeTwo = function(intervals) {
    intervals.sort((a, b) => a[1] - b[1] || b[0] - a[0]);

    let count = 0;
    let secondLargest = -1;
    let largest = -1;

    for (const [start, end] of intervals) {
        const contained = (secondLargest >= start ? 1 : 0) + (largest >= start ? 1 : 0);

        if (contained === 0) {
            count += 2;
            secondLargest = end - 1;
            largest = end;
        } else if (contained === 1) {
            count++;
            if (largest < start) {
                secondLargest = largest;
                largest = end;
            } else {
                secondLargest = end;
            }
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
function intersectionSizeTwo(intervals: number[][]): number {
    intervals.sort((a, b) => a[1] - b[1] || b[0] - a[0]);

    let count = 0;
    let secondLargest = -1;
    let largest = -1;

    for (const [start, end] of intervals) {
        const contained = Number(secondLargest >= start) + Number(largest >= start);

        if (contained === 0) {
            count += 2;
            secondLargest = end - 1;
            largest = end;
        } else if (contained === 1) {
            count += 1;
            if (largest < start) {
                secondLargest = largest;
                largest = end;
            } else {
                secondLargest = end;
            }
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
    function intersectionSizeTwo($intervals) {
        usort($intervals, function ($a, $b) {
            if ($a[1] === $b[1]) {
                return $b[0] <=> $a[0];
            }
            return $a[1] <=> $b[1];
        });

        $count = 0;
        $secondLargest = -1;
        $largest = -1;

        foreach ($intervals as $interval) {
            [$start, $end] = $interval;
            $contained = (int)($secondLargest >= $start) + (int)($largest >= $start);

            if ($contained === 0) {
                $count += 2;
                $secondLargest = $end - 1;
                $largest = $end;
            } elseif ($contained === 1) {
                $count++;
                if ($largest < $start) {
                    $secondLargest = $largest;
                    $largest = $end;
                } else {
                    $secondLargest = $end;
                }
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
    func intersectionSizeTwo(_ intervals: [[Int]]) -> Int {
        let sortedIntervals = intervals.sorted {
            if $0[1] == $1[1] {
                return $0[0] > $1[0]
            }
            return $0[1] < $1[1]
        }

        var count = 0
        var secondLargest = -1
        var largest = -1

        for interval in sortedIntervals {
            let start = interval[0]
            let end = interval[1]
            let contained = (secondLargest >= start ? 1 : 0) + (largest >= start ? 1 : 0)

            if contained == 0 {
                count += 2
                secondLargest = end - 1
                largest = end
            } else if contained == 1 {
                count += 1
                if largest < start {
                    secondLargest = largest
                    largest = end
                } else {
                    secondLargest = end
                }
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
class Solution {
    fun intersectionSizeTwo(intervals: Array<IntArray>): Int {
        intervals.sortWith(compareBy<IntArray> { it[1] }.thenByDescending { it[0] })

        var count = 0
        var secondLargest = -1
        var largest = -1

        for (interval in intervals) {
            val start = interval[0]
            val end = interval[1]
            val contained = (if (secondLargest >= start) 1 else 0) + (if (largest >= start) 1 else 0)

            if (contained == 0) {
                count += 2
                secondLargest = end - 1
                largest = end
            } else if (contained == 1) {
                count++
                if (largest < start) {
                    secondLargest = largest
                    largest = end
                } else {
                    secondLargest = end
                }
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
  int intersectionSizeTwo(List<List<int>> intervals) {
    intervals.sort((a, b) {
      final endComparison = a[1].compareTo(b[1]);
      if (endComparison != 0) return endComparison;
      return b[0].compareTo(a[0]);
    });

    var count = 0;
    var secondLargest = -1;
    var largest = -1;

    for (final interval in intervals) {
      final start = interval[0];
      final end = interval[1];
      final contained = (secondLargest >= start ? 1 : 0) +
          (largest >= start ? 1 : 0);

      if (contained == 0) {
        count += 2;
        secondLargest = end - 1;
        largest = end;
      } else if (contained == 1) {
        count += 1;
        if (largest < start) {
          secondLargest = largest;
          largest = end;
        } else {
          secondLargest = end;
        }
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
func intersectionSizeTwo(intervals [][]int) int {
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][1] != intervals[j][1] {
			return intervals[i][1] < intervals[j][1]
		}
		return intervals[i][0] > intervals[j][0]
	})

	count := 0
	secondLargest := -1
	largest := -1

	for _, interval := range intervals {
		start, end := interval[0], interval[1]
		contained := 0
		if secondLargest >= start {
			contained++
		}
		if largest >= start {
			contained++
		}

		if contained == 0 {
			count += 2
			secondLargest = end - 1
			largest = end
		} else if contained == 1 {
			count++
			if largest < start {
				secondLargest = largest
				largest = end
			} else {
				secondLargest = end
			}
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
def intersection_size_two(intervals)
  intervals.sort_by! { |interval| [interval[1], -interval[0]] }

  count = 0
  second_largest = -1
  largest = -1

  intervals.each do |start, finish|
    contained = (second_largest >= start ? 1 : 0) + (largest >= start ? 1 : 0)

    if contained == 0
      count += 2
      second_largest = finish - 1
      largest = finish
    elsif contained == 1
      count += 1
      if largest < start
        second_largest = largest
        largest = finish
      else
        second_largest = finish
      end
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
    def intersectionSizeTwo(intervals: Array[Array[Int]]): Int = {
        scala.util.Sorting.stableSort(intervals, (a: Array[Int], b: Array[Int]) => {
            if (a(1) != b(1)) a(1) < b(1) else a(0) > b(0)
        })

        var count = 0
        var secondLargest = -1
        var largest = -1

        for (interval <- intervals) {
            val start = interval(0)
            val end = interval(1)
            val contained = (if (secondLargest >= start) 1 else 0) +
                (if (largest >= start) 1 else 0)

            if (contained == 0) {
                count += 2
                secondLargest = end - 1
                largest = end
            } else if (contained == 1) {
                count += 1
                if (largest < start) {
                    secondLargest = largest
                    largest = end
                } else {
                    secondLargest = end
                }
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
    pub fn intersection_size_two(mut intervals: Vec<Vec<i32>>) -> i32 {
        intervals.sort_by(|a, b| a[1].cmp(&b[1]).then_with(|| b[0].cmp(&a[0])));

        let mut count = 0;
        let mut second_largest = -1;
        let mut largest = -1;

        for interval in intervals {
            let start = interval[0];
            let end = interval[1];
            let contained = i32::from(second_largest >= start) + i32::from(largest >= start);

            if contained == 0 {
                count += 2;
                second_largest = end - 1;
                largest = end;
            } else if contained == 1 {
                count += 1;
                if largest < start {
                    second_largest = largest;
                    largest = end;
                } else {
                    second_largest = end;
                }
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
(define/contract (intersection-size-two intervals)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (define sorted-intervals
    (sort intervals
          (lambda (a b)
            (or (< (second a) (second b))
                (and (= (second a) (second b))
                     (> (first a) (first b)))))))
  (let loop ([remaining sorted-intervals]
             [count 0]
             [second-largest -1]
             [largest -1])
    (if (null? remaining)
        count
        (let* ([interval (car remaining)]
               [start (first interval)]
               [end (second interval)]
               [contained (+ (if (>= second-largest start) 1 0)
                             (if (>= largest start) 1 0))])
          (cond
            [(= contained 0)
             (loop (cdr remaining) (+ count 2) (- end 1) end)]
            [(= contained 1)
             (if (< largest start)
                 (loop (cdr remaining) (+ count 1) largest end)
                 (loop (cdr remaining) (+ count 1) end largest))]
            [else
             (loop (cdr remaining) count second-largest largest)])))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec intersection_size_two(Intervals :: [[integer()]]) -> integer().
intersection_size_two(Intervals) ->
  Sorted = lists:sort(
    fun([StartA, EndA], [StartB, EndB]) ->
      EndA < EndB orelse (EndA =:= EndB andalso StartA > StartB)
    end,
    Intervals
  ),
  intersection_size_two_loop(Sorted, 0, -1, -1).

intersection_size_two_loop([], Count, _SecondLargest, _Largest) ->
  Count;
intersection_size_two_loop([[Start, End] | Rest], Count, SecondLargest, Largest) ->
  Contained = (if SecondLargest >= Start -> 1; true -> 0 end) +
              (if Largest >= Start -> 1; true -> 0 end),
  case Contained of
    0 -> intersection_size_two_loop(Rest, Count + 2, End - 1, End);
    1 when Largest < Start -> intersection_size_two_loop(Rest, Count + 1, Largest, End);
    1 -> intersection_size_two_loop(Rest, Count + 1, End, Largest);
    _ -> intersection_size_two_loop(Rest, Count, SecondLargest, Largest)
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
    sorted_intervals =
      Enum.sort_by(intervals, fn [start, ending] -> {ending, -start} end)

    process(sorted_intervals, 0, -1, -1)
  end

  defp process([], count, _second_largest, _largest), do: count

  defp process([[start, ending] | rest], count, second_largest, largest) do
    contained =
      (if second_largest >= start, do: 1, else: 0) +
        (if largest >= start, do: 1, else: 0)

    case contained do
      0 -> process(rest, count + 2, ending - 1, ending)
      1 when largest < start -> process(rest, count + 1, largest, ending)
      1 -> process(rest, count + 1, ending, largest)
      _ -> process(rest, count, second_largest, largest)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log n), due to sorting the n intervals; the greedy scan takes O(n).
- **Space Complexity:** O(1) auxiliary space beyond the storage used by the sorting implementation.
