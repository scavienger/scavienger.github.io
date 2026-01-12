---
layout: post
title: "Minimum Time Visiting All Points"
date: 2026-01-12 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Math", "Geometry"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/minimum-time-visiting-all-points/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minTimeToVisitAllPoints(vector<vector<int>>&\
        \ points) {\n        int totalTime = 0;\n        for (int i = 0; i < points.size()\
        \ - 1; ++i) {\n            int x1 = points[i][0];\n            int y1 = points[i][1];\n\
        \            int x2 = points[i+1][0];\n            int y2 = points[i+1][1];\n\
        \n            int dx = abs(x2 - x1);\n            int dy = abs(y2 - y1);\n\n\
        \            totalTime += max(dx, dy);\n        }\n        return totalTime;\n\
        \    }\n};"
      java: "class Solution {\n    public int minTimeToVisitAllPoints(int[][] points)\
        \ {\n        int totalTime = 0;\n        for (int i = 0; i < points.length -\
        \ 1; ++i) {\n            int x1 = points[i][0];\n            int y1 = points[i][1];\n\
        \            int x2 = points[i+1][0];\n            int y2 = points[i+1][1];\n\
        \n            int dx = Math.abs(x2 - x1);\n            int dy = Math.abs(y2\
        \ - y1);\n\n            totalTime += Math.max(dx, dy);\n        }\n        return\
        \ totalTime;\n    }\n}"
      python: "class Solution(object):\n    def minTimeToVisitAllPoints(self, points):\n\
        \        \"\"\"\n        :type points: List[List[int]]\n        :rtype: int\n\
        \        \"\"\"\n        total_time = 0\n        for i in range(len(points)\
        \ - 1):\n            x1, y1 = points[i]\n            x2, y2 = points[i+1]\n\n\
        \            dx = abs(x2 - x1)\n            dy = abs(y2 - y1)\n\n          \
        \  total_time += max(dx, dy)\n        return total_time"
      python3: "class Solution:\n    def minTimeToVisitAllPoints(self, points: List[List[int]])\
        \ -> int:\n        total_time = 0\n        for i in range(len(points) - 1):\n\
        \            x1, y1 = points[i]\n            x2, y2 = points[i+1]\n\n      \
        \      dx = abs(x2 - x1)\n            dy = abs(y2 - y1)\n\n            total_time\
        \ += max(dx, dy)\n        return total_time"
      c: "int max(int a, int b) {\n    return (a > b) ? a : b;\n}\n\nint minTimeToVisitAllPoints(int**\
        \ points, int pointsSize, int* pointsColSize) {\n    int totalTime = 0;\n  \
        \  for (int i = 0; i < pointsSize - 1; ++i) {\n        int x1 = points[i][0];\n\
        \        int y1 = points[i][1];\n        int x2 = points[i+1][0];\n        int\
        \ y2 = points[i+1][1];\n\n        int dx = abs(x2 - x1);\n        int dy = abs(y2\
        \ - y1);\n\n        totalTime += max(dx, dy);\n    }\n    return totalTime;\n\
        }"
      csharp: "public class Solution {\n    public int MinTimeToVisitAllPoints(int[][]\
        \ points) {\n        int totalTime = 0;\n        for (int i = 0; i < points.Length\
        \ - 1; i++) {\n            int x1 = points[i][0];\n            int y1 = points[i][1];\n\
        \            int x2 = points[i+1][0];\n            int y2 = points[i+1][1];\n\
        \n            int dx = Math.Abs(x2 - x1);\n            int dy = Math.Abs(y2\
        \ - y1);\n\n            totalTime += Math.Max(dx, dy);\n        }\n        return\
        \ totalTime;\n    }\n}"
      javascript: "/**\n * @param {number[][]} points\n * @return {number}\n */\nvar\
        \ minTimeToVisitAllPoints = function(points) {\n    let totalTime = 0;\n   \
        \ for (let i = 0; i < points.length - 1; i++) {\n        let x1 = points[i][0];\n\
        \        let y1 = points[i][1];\n        let x2 = points[i+1][0];\n        let\
        \ y2 = points[i+1][1];\n\n        let dx = Math.abs(x2 - x1);\n        let dy\
        \ = Math.abs(y2 - y1);\n\n        totalTime += Math.max(dx, dy);\n    }\n  \
        \  return totalTime;\n};"
      typescript: "function minTimeToVisitAllPoints(points: number[][]): number {\n\
        \    let totalTime: number = 0;\n    for (let i = 0; i < points.length - 1;\
        \ i++) {\n        let x1: number = points[i][0];\n        let y1: number = points[i][1];\n\
        \        let x2: number = points[i+1][0];\n        let y2: number = points[i+1][1];\n\
        \n        let dx: number = Math.abs(x2 - x1);\n        let dy: number = Math.abs(y2\
        \ - y1);\n\n        totalTime += Math.max(dx, dy);\n    }\n    return totalTime;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $points\n     * @return\
        \ Integer\n     */\n    function minTimeToVisitAllPoints($points) {\n      \
        \  $totalTime = 0;\n        for ($i = 0; $i < count($points) - 1; $i++) {\n\
        \            $x1 = $points[$i][0];\n            $y1 = $points[$i][1];\n    \
        \        $x2 = $points[$i+1][0];\n            $y2 = $points[$i+1][1];\n\n  \
        \          $dx = abs($x2 - $x1);\n            $dy = abs($y2 - $y1);\n\n    \
        \        $totalTime += max($dx, $dy);\n        }\n        return $totalTime;\n\
        \    }\n}"
      swift: "class Solution {\n    func minTimeToVisitAllPoints(_ points: [[Int]])\
        \ -> Int {\n        var totalTime = 0\n        for i in 0..<points.count - 1\
        \ {\n            let x1 = points[i][0]\n            let y1 = points[i][1]\n\
        \            let x2 = points[i+1][0]\n            let y2 = points[i+1][1]\n\n\
        \            let dx = abs(x2 - x1)\n            let dy = abs(y2 - y1)\n\n  \
        \          totalTime += max(dx, dy)\n        }\n        return totalTime\n \
        \   }\n}"
      kotlin: "class Solution {\n    fun minTimeToVisitAllPoints(points: Array<IntArray>):\
        \ Int {\n        var totalTime = 0\n        for (i in 0 until points.size -\
        \ 1) {\n            val p1 = points[i]\n            val p2 = points[i+1]\n \
        \           val dx = Math.abs(p2[0] - p1[0])\n            val dy = Math.abs(p2[1]\
        \ - p1[1])\n            totalTime += Math.max(dx, dy)\n        }\n        return\
        \ totalTime\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int minTimeToVisitAllPoints(List<List<int>>\
        \ points) {\n    int totalTime = 0;\n    for (int i = 0; i < points.length -\
        \ 1; i++) {\n      List<int> p1 = points[i];\n      List<int> p2 = points[i+1];\n\
        \      int dx = (p2[0] - p1[0]).abs();\n      int dy = (p2[1] - p1[1]).abs();\n\
        \      totalTime += max(dx, dy);\n    }\n    return totalTime;\n  }\n}"
      go: "import \"math\"\n\nfunc minTimeToVisitAllPoints(points [][]int) int {\n \
        \   totalTime := 0\n    for i := 0; i < len(points) - 1; i++ {\n        p1 :=\
        \ points[i]\n        p2 := points[i+1]\n        dx := int(math.Abs(float64(p2[0]\
        \ - p1[0])))\n        dy := int(math.Abs(float64(p2[1] - p1[1])))\n        totalTime\
        \ += int(math.Max(float64(dx), float64(dy)))\n    }\n    return totalTime\n}"
      ruby: "# @param {Integer[][]} points\n# @return {Integer}\ndef min_time_to_visit_all_points(points)\n\
        \    total_time = 0\n    (0...points.length - 1).each do |i|\n        p1 = points[i]\n\
        \        p2 = points[i+1]\n        dx = (p2[0] - p1[0]).abs\n        dy = (p2[1]\
        \ - p1[1]).abs\n        total_time += [dx, dy].max\n    end\n    total_time\n\
        end"
      scala: "object Solution {\n    def minTimeToVisitAllPoints(points: Array[Array[Int]]):\
        \ Int = {\n        var totalTime = 0\n        for (i <- 0 until points.length\
        \ - 1) {\n            val p1 = points(i)\n            val p2 = points(i+1)\n\
        \            val dx = Math.abs(p2(0) - p1(0))\n            val dy = Math.abs(p2(1)\
        \ - p1(1))\n            totalTime += Math.max(dx, dy)\n        }\n        totalTime\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn min_time_to_visit_all_points(points: Vec<Vec<i32>>)\
        \ -> i32 {\n        let mut total_time = 0;\n        for i in 1..points.len()\
        \ {\n            let p1 = &points[i - 1];\n            let p2 = &points[i];\n\
        \            let dx = (p2[0] - p1[0]).abs();\n            let dy = (p2[1] -\
        \ p1[1]).abs();\n            total_time += dx.max(dy);\n        }\n        total_time\n\
        \    }\n}"
      racket: "(define/contract (min-time-to-visit-all-points points)\n  (-> (listof\
        \ (listof exact-integer?)) exact-integer?)\n  (if (<= (length points) 1)\n \
        \     0\n      (let loop ((prev-point (car points))\n                 (remaining-points\
        \ (cdr points))\n                 (total-time 0))\n        (if (empty? remaining-points)\n\
        \            total-time\n            (let* ((current-point (car remaining-points))\n\
        \                   (x1 (list-ref prev-point 0))\n                   (y1 (list-ref\
        \ prev-point 1))\n                   (x2 (list-ref current-point 0))\n     \
        \              (y2 (list-ref current-point 1))\n                   (dx (abs\
        \ (- x2 x1)))\n                   (dy (abs (- y2 y1))))\n              (loop\
        \ current-point\n                    (cdr remaining-points)\n              \
        \      (+ total-time (max dx dy))))))))"
      erlang: "-spec min_time_to_visit_all_points(Points :: [[integer()]]) -> integer().\n\
        min_time_to_visit_all_points(Points) ->\n    min_time_to_visit_all_points(Points,\
        \ 0).\n\nmin_time_to_visit_all_points([[X1, Y1], [X2, Y2] | Rest], Acc) ->\n\
        \    DX = abs(X2 - X1),\n    DY = abs(Y2 - Y1),\n    Time = max(DX, DY),\n \
        \   min_time_to_visit_all_points([[X2, Y2] | Rest], Acc + Time);\nmin_time_to_visit_all_points([_],\
        \ Acc) ->\n    Acc;\nmin_time_to_visit_all_points([], Acc) ->\n    Acc."
      elixir: "defmodule Solution do\n  @spec min_time_to_visit_all_points(points ::\
        \ [[integer]]) :: integer\n  def min_time_to_visit_all_points(points) do\n \
        \   do_min_time_to_visit_all_points(points, 0)\n  end\n\n  defp do_min_time_to_visit_all_points([[x1,\
        \ y1], [x2, y2] | rest], acc) do\n    dx = abs(x2 - x1)\n    dy = abs(y2 - y1)\n\
        \    time_segment = max(dx, dy)\n    do_min_time_to_visit_all_points([[x2, y2]\
        \ | rest], acc + time_segment)\n  end\n\n  defp do_min_time_to_visit_all_points([_],\
        \ acc), do: acc\n  defp do_min_time_to_visit_all_points([], acc), do: acc\n\
        end"
    approach: 'The problem requires finding the minimum time to visit a sequence of
      points on a 2D plane, where movement can be horizontal, vertical, or diagonal,
      each taking 1 second per unit. The key insight is that a diagonal move covers
      one unit horizontally and one unit vertically simultaneously, making it the most
      efficient way to reduce both coordinate differences. To travel from a point (x1,
      y1) to (x2, y2), we calculate the absolute differences in coordinates: dx = |x2
      - x1| and dy = |y2 - y1|. The maximum number of diagonal moves possible is min(dx,
      dy). After these diagonal moves, the remaining difference in one dimension (or
      both) will be max(dx, dy) - min(dx, dy), which must be covered by straight horizontal
      or vertical moves.


      Combining these, the total time to move between two points (x1, y1) and (x2, y2)
      is min(dx, dy) + (max(dx, dy) - min(dx, dy)), which simplifies to max(dx, dy).
      This is also known as the Chebyshev distance. To find the minimum total time to
      visit all points in the given order, we iterate through the list of points, calculating
      the Chebyshev distance between each consecutive pair of points and summing these
      individual travel times. The final sum represents the overall minimum time.'
    time_complexity: The algorithm iterates through the list of points once. For each
      of the n-1 pairs of consecutive points, it performs a constant number of arithmetic
      operations (subtraction, absolute value, and finding the maximum). Therefore,
      the time complexity is directly proportional to the number of points, N, making
      it O(N).
    space_complexity: The algorithm uses a few integer variables to store the current
      coordinates, their differences, and the running total time. It does not allocate
      any additional data structures that scale with the input size. Hence, the space
      complexity is constant, O(1), excluding the space required to store the input
      points themselves.
    elapsed_time: 59.09058475494385
    model: gemini-2.5-flash
    generated_at: '2026-01-12 01:13:51 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int minTimeToVisitAllPoints(vector<vector<int>>&\
        \ points) {\n        int time = 0;\n        for (int i = 1; i < points.size();\
        \ i++) {\n            time += max(abs(points[i][0] - points[i-1][0]), abs(points[i][1]\
        \ - points[i-1][1]));\n        }\n        return time;\n    }\n};"
      java: "class Solution {\n    public int minTimeToVisitAllPoints(int[][] points)\
        \ {\n        int time = 0;\n        for (int i = 1; i < points.length; i++)\
        \ {\n            time += Math.max(Math.abs(points[i][0] - points[i-1][0]), Math.abs(points[i][1]\
        \ - points[i-1][1]));\n        }\n        return time;\n    }\n}"
      python: "class Solution(object):\n    def minTimeToVisitAllPoints(self, points):\n\
        \        time = 0\n        for i in range(1, len(points)):\n            time\
        \ += max(abs(points[i][0] - points[i-1][0]), abs(points[i][1] - points[i-1][1]))\n\
        \        return time"
      python3: "class Solution:\n    def minTimeToVisitAllPoints(self, points: List[List[int]])\
        \ -> int:\n        time = 0\n        for i in range(1, len(points)):\n     \
        \       time += max(abs(points[i][0] - points[i-1][0]), abs(points[i][1] - points[i-1][1]))\n\
        \        return time"
      c: "int minTimeToVisitAllPoints(int** points, int pointsSize, int* pointsColSize)\
        \ {\n    int time = 0;\n    for (int i = 1; i < pointsSize; i++) {\n       \
        \ time += (abs(points[i][0] - points[i-1][0]) > abs(points[i][1] - points[i-1][1]))\
        \ ? abs(points[i][0] - points[i-1][0]) : abs(points[i][1] - points[i-1][1]);\n\
        \    }\n    return time;\n}"
      csharp: "public class Solution { \n    public int MinTimeToVisitAllPoints(int[][]\
        \ points) { \n        int time = 0; \n        for (int i = 0; i < points.Length\
        \ - 1; i++) { \n            int dx = Math.Abs(points[i + 1][0] - points[i][0]);\
        \ \n            int dy = Math.Abs(points[i + 1][1] - points[i][1]); \n     \
        \       time += Math.Max(dx, dy); \n        } \n        return time; \n    }\
        \ \n}"
      javascript: "var minTimeToVisitAllPoints = function(points) { \n    let time =\
        \ 0; \n    for (let i = 0; i < points.length - 1; i++) { \n        let dx =\
        \ Math.abs(points[i + 1][0] - points[i][0]); \n        let dy = Math.abs(points[i\
        \ + 1][1] - points[i][1]); \n        time += Math.max(dx, dy); \n    } \n  \
        \  return time; \n};"
      typescript: "function minTimeToVisitAllPoints(points: number[][]): number { \n\
        \    let time: number = 0; \n    for (let i: number = 0; i < points.length -\
        \ 1; i++) { \n        let dx: number = Math.abs(points[i + 1][0] - points[i][0]);\
        \ \n        let dy: number = Math.abs(points[i + 1][1] - points[i][1]); \n \
        \       time += Math.max(dx, dy); \n    } \n    return time; \n}"
      php: "class Solution { \n    function minTimeToVisitAllPoints($points) { \n  \
        \      $time = 0; \n        for ($i = 0; $i < count($points) - 1; $i++) { \n\
        \            $dx = abs($points[$i + 1][0] - $points[$i][0]); \n            $dy\
        \ = abs($points[$i + 1][1] - $points[$i][1]); \n            $time += max($dx,\
        \ $dy); \n        } \n        return $time; \n    } \n}"
      swift: "class Solution { \n    func minTimeToVisitAllPoints(_ points: [[Int]])\
        \ -> Int { \n        var time: Int = 0 \n        for i in 0..<points.count -\
        \ 1 { \n            let dx = abs(points[i + 1][0] - points[i][0]) \n       \
        \     let dy = abs(points[i + 1][1] - points[i][1]) \n            time += max(dx,\
        \ dy) \n        } \n        return time \n    } \n}"
      kotlin: "class Solution {\n    fun minTimeToVisitAllPoints(points: Array<IntArray>):\
        \ Int {\n        var time = 0\n        for (i in 0 until points.size - 1) {\n\
        \            val xDiff = Math.abs(points[i][0] - points[i + 1][0])\n       \
        \     val yDiff = Math.abs(points[i][1] - points[i + 1][1])\n            time\
        \ += Math.max(xDiff, yDiff)\n        }\n        return time\n    }\n}"
      dart: "class Solution {\n  int minTimeToVisitAllPoints(List<List<int>> points)\
        \ {\n    int time = 0;\n    for (int i = 0; i < points.length - 1; i++) {\n\
        \      int xDiff = (points[i][0] - points[i + 1][0]).abs();\n      int yDiff\
        \ = (points[i][1] - points[i + 1][1]).abs();\n      time += xDiff > yDiff ?\
        \ xDiff : yDiff;\n    }\n    return time;\n  }\n}"
      go: "func minTimeToVisitAllPoints(points [][]int) int {\n    time := 0\n    for\
        \ i := 0; i < len(points) - 1; i++ {\n        xDiff := abs(points[i][0] - points[i\
        \ + 1][0])\n        yDiff := abs(points[i][1] - points[i + 1][1])\n        time\
        \ += max(xDiff, yDiff)\n    }\n    return time\n}\n\nfunc abs(x int) int {\n\
        \    if x < 0 {\n        return -x\n    }\n    return x\n}\n\nfunc max(x, y\
        \ int) int {\n    if x > y {\n        return x\n    }\n    return y\n}"
      ruby: "def min_time_to_visit_all_points(points)\n    time = 0\n    (0...points.size\
        \ - 1).each do |i|\n        x_diff = (points[i][0] - points[i + 1][0]).abs\n\
        \        y_diff = (points[i][1] - points[i + 1][1]).abs\n        time += [x_diff,\
        \ y_diff].max\n    end\n    time\nend"
      scala: "object Solution {\n    def minTimeToVisitAllPoints(points: Array[Array[Int]]):\
        \ Int = {\n        var time = 0\n        for (i <- 0 until points.length - 1)\
        \ {\n            val xDiff = (points(i)(0) - points(i + 1)(0)).abs\n       \
        \     val yDiff = (points(i)(1) - points(i + 1)(1)).abs\n            time +=\
        \ xDiff.max(yDiff)\n        }\n        time\n    }\n}"
      rust: "impl Solution {\n    pub fn min_time_to_visit_all_points(points: Vec<Vec<i32>>)\
        \ -> i32 {\n        let mut total_time = 0;\n        for i in 0..points.len()\
        \ - 1 {\n            let x_diff = (points[i][0] - points[i + 1][0]).abs();\n\
        \            let y_diff = (points[i][1] - points[i + 1][1]).abs();\n       \
        \     total_time += x_diff.max(y_diff);\n        }\n        total_time\n   \
        \ }\n}"
      racket: "(define/contract (min-time-to-visit-all-points points)\n  (-> (listof\
        \ (listof exact-integer?)) exact-integer?)\n  (let loop ([points points] [total-time\
        \ 0])\n    (if (null? (cdr points))\n        total-time\n        (loop (cdr\
        \ points) (+ total-time (max (abs (- (caar points) (caadr points))) (abs (-\
        \ (cadar points) (cadadr points)))))))))"
      erlang: "min_time_to_visit_all_points(Points) ->\n  lists:foldl(fun ([X1, Y1],\
        \ [X2, Y2] = Point, Acc) ->\n                  Acc + max(abs(X1 - X2), abs(Y1\
        \ - Y2))\n              end, 0, Points)."
      elixir: "defmodule Solution do\n  @spec min_time_to_visit_all_points(points ::\
        \ [[integer]]) :: integer\n  def min_time_to_visit_all_points(points) do\n \
        \   Enum.reduce(points, 0, fn [x1, y1], acc ->\n      [x2, y2] = Enum.at(points,\
        \ Enum.find_index(points, fn point -> point == [x1, y1] end) + 1)\n      acc\
        \ + max(abs(x1 - x2), abs(y1 - y2))\n    end)\n  end\nend"
    approach: "The problem can be solved by iterating over each pair of consecutive\
      \ points and calculating the time it takes to move from one point to the next.\
      \ The key intuition is to move diagonally as much as possible and then move in\
      \ a straight line. This can be achieved by calculating the maximum of the absolute\
      \ differences in the x and y coordinates between the two points, which represents\
      \ the number of diagonal moves, and then adding any remaining moves in a straight\
      \ line. \nThe algorithm works by initializing a variable to store the total time\
      \ and then iterating over each pair of points. For each pair, it calculates the\
      \ time it takes to move from the first point to the second point and adds this\
      \ to the total time. The time it takes to move from one point to the next is calculated\
      \ as the maximum of the absolute differences in the x and y coordinates between\
      \ the two points, which represents the number of diagonal moves, and then adding\
      \ any remaining moves in a straight line."
    time_complexity: The time complexity of this solution is O(n), where n is the number
      of points. This is because the algorithm iterates over each pair of points once,
      and the operations performed for each pair take constant time. The space complexity
      is O(1), which means the space required does not change with the size of the input,
      making it very efficient for large inputs.
    space_complexity: The space complexity of this solution is O(1), which means the
      space required does not change with the size of the input. This is because the
      algorithm only uses a constant amount of space to store the total time and the
      current point, regardless of the number of points.
    elapsed_time: 7.678443431854248
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-12 01:14:14 '
---

## Problem #1266: Minimum Time Visiting All Points

**Difficulty:** Easy

**Topics:** Array, Math, Geometry

## Problem Description

<p>On a 2D plane, there are <code>n</code> points with integer coordinates <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>. Return <em>the <strong>minimum time</strong> in seconds to visit all the points in the order given by </em><code>points</code>.</p>

<p>You can move according to these rules:</p>

<ul>
	<li>In <code>1</code> second, you can either:

	<ul>
		<li>move vertically by one&nbsp;unit,</li>
		<li>move horizontally by one unit, or</li>
		<li>move diagonally <code>sqrt(2)</code> units (in other words, move one unit vertically then one unit horizontally in <code>1</code> second).</li>
	</ul>
	</li>
	<li>You have to visit the points in the same order as they appear in the array.</li>
	<li>You are allowed to pass through points that appear later in the order, but these do not count as visits.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/11/14/1626_example_1.PNG" style="width: 500px; height: 428px;" />
<pre>
<strong>Input:</strong> points = [[1,1],[3,4],[-1,0]]
<strong>Output:</strong> 7
<strong>Explanation: </strong>One optimal path is <strong>[1,1]</strong> -&gt; [2,2] -&gt; [3,3] -&gt; <strong>[3,4] </strong>-&gt; [2,3] -&gt; [1,2] -&gt; [0,1] -&gt; <strong>[-1,0]</strong>   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> points = [[3,2],[-2,2]]
<strong>Output:</strong> 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>points.length == n</code></li>
	<li><code>1 &lt;= n&nbsp;&lt;= 100</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-1000&nbsp;&lt;= points[i][0], points[i][1]&nbsp;&lt;= 1000</code></li>
</ul>


## Hints

1. To walk from point A to point B there will be an optimal strategy to walk ?

2. Advance in diagonal as possible then after that go in straight line.

3. Repeat the process until visiting all the points.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-12 01:13:51 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires finding the minimum time to visit a sequence of points on a 2D plane, where movement can be horizontal, vertical, or diagonal, each taking 1 second per unit. The key insight is that a diagonal move covers one unit horizontally and one unit vertically simultaneously, making it the most efficient way to reduce both coordinate differences. To travel from a point (x1, y1) to (x2, y2), we calculate the absolute differences in coordinates: dx = |x2 - x1| and dy = |y2 - y1|. The maximum number of diagonal moves possible is min(dx, dy). After these diagonal moves, the remaining difference in one dimension (or both) will be max(dx, dy) - min(dx, dy), which must be covered by straight horizontal or vertical moves.

Combining these, the total time to move between two points (x1, y1) and (x2, y2) is min(dx, dy) + (max(dx, dy) - min(dx, dy)), which simplifies to max(dx, dy). This is also known as the Chebyshev distance. To find the minimum total time to visit all points in the given order, we iterate through the list of points, calculating the Chebyshev distance between each consecutive pair of points and summing these individual travel times. The final sum represents the overall minimum time.

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
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int totalTime = 0;
        for (int i = 0; i < points.size() - 1; ++i) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            int x2 = points[i+1][0];
            int y2 = points[i+1][1];

            int dx = abs(x2 - x1);
            int dy = abs(y2 - y1);

            totalTime += max(dx, dy);
        }
        return totalTime;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int totalTime = 0;
        for (int i = 0; i < points.length - 1; ++i) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            int x2 = points[i+1][0];
            int y2 = points[i+1][1];

            int dx = Math.abs(x2 - x1);
            int dy = Math.abs(y2 - y1);

            totalTime += Math.max(dx, dy);
        }
        return totalTime;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total_time = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]

            dx = abs(x2 - x1)
            dy = abs(y2 - y1)

            total_time += max(dx, dy)
        return total_time
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]

            dx = abs(x2 - x1)
            dy = abs(y2 - y1)

            total_time += max(dx, dy)
        return total_time
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int max(int a, int b) {
    return (a > b) ? a : b;
}

int minTimeToVisitAllPoints(int** points, int pointsSize, int* pointsColSize) {
    int totalTime = 0;
    for (int i = 0; i < pointsSize - 1; ++i) {
        int x1 = points[i][0];
        int y1 = points[i][1];
        int x2 = points[i+1][0];
        int y2 = points[i+1][1];

        int dx = abs(x2 - x1);
        int dy = abs(y2 - y1);

        totalTime += max(dx, dy);
    }
    return totalTime;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinTimeToVisitAllPoints(int[][] points) {
        int totalTime = 0;
        for (int i = 0; i < points.Length - 1; i++) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            int x2 = points[i+1][0];
            int y2 = points[i+1][1];

            int dx = Math.Abs(x2 - x1);
            int dy = Math.Abs(y2 - y1);

            totalTime += Math.Max(dx, dy);
        }
        return totalTime;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} points
 * @return {number}
 */
var minTimeToVisitAllPoints = function(points) {
    let totalTime = 0;
    for (let i = 0; i < points.length - 1; i++) {
        let x1 = points[i][0];
        let y1 = points[i][1];
        let x2 = points[i+1][0];
        let y2 = points[i+1][1];

        let dx = Math.abs(x2 - x1);
        let dy = Math.abs(y2 - y1);

        totalTime += Math.max(dx, dy);
    }
    return totalTime;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minTimeToVisitAllPoints(points: number[][]): number {
    let totalTime: number = 0;
    for (let i = 0; i < points.length - 1; i++) {
        let x1: number = points[i][0];
        let y1: number = points[i][1];
        let x2: number = points[i+1][0];
        let y2: number = points[i+1][1];

        let dx: number = Math.abs(x2 - x1);
        let dy: number = Math.abs(y2 - y1);

        totalTime += Math.max(dx, dy);
    }
    return totalTime;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function minTimeToVisitAllPoints($points) {
        $totalTime = 0;
        for ($i = 0; $i < count($points) - 1; $i++) {
            $x1 = $points[$i][0];
            $y1 = $points[$i][1];
            $x2 = $points[$i+1][0];
            $y2 = $points[$i+1][1];

            $dx = abs($x2 - $x1);
            $dy = abs($y2 - $y1);

            $totalTime += max($dx, $dy);
        }
        return $totalTime;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minTimeToVisitAllPoints(_ points: [[Int]]) -> Int {
        var totalTime = 0
        for i in 0..<points.count - 1 {
            let x1 = points[i][0]
            let y1 = points[i][1]
            let x2 = points[i+1][0]
            let y2 = points[i+1][1]

            let dx = abs(x2 - x1)
            let dy = abs(y2 - y1)

            totalTime += max(dx, dy)
        }
        return totalTime
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minTimeToVisitAllPoints(points: Array<IntArray>): Int {
        var totalTime = 0
        for (i in 0 until points.size - 1) {
            val p1 = points[i]
            val p2 = points[i+1]
            val dx = Math.abs(p2[0] - p1[0])
            val dy = Math.abs(p2[1] - p1[1])
            totalTime += Math.max(dx, dy)
        }
        return totalTime
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
  int minTimeToVisitAllPoints(List<List<int>> points) {
    int totalTime = 0;
    for (int i = 0; i < points.length - 1; i++) {
      List<int> p1 = points[i];
      List<int> p2 = points[i+1];
      int dx = (p2[0] - p1[0]).abs();
      int dy = (p2[1] - p1[1]).abs();
      totalTime += max(dx, dy);
    }
    return totalTime;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "math"

func minTimeToVisitAllPoints(points [][]int) int {
    totalTime := 0
    for i := 0; i < len(points) - 1; i++ {
        p1 := points[i]
        p2 := points[i+1]
        dx := int(math.Abs(float64(p2[0] - p1[0])))
        dy := int(math.Abs(float64(p2[1] - p1[1])))
        totalTime += int(math.Max(float64(dx), float64(dy)))
    }
    return totalTime
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[][]} points
# @return {Integer}
def min_time_to_visit_all_points(points)
    total_time = 0
    (0...points.length - 1).each do |i|
        p1 = points[i]
        p2 = points[i+1]
        dx = (p2[0] - p1[0]).abs
        dy = (p2[1] - p1[1]).abs
        total_time += [dx, dy].max
    end
    total_time
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minTimeToVisitAllPoints(points: Array[Array[Int]]): Int = {
        var totalTime = 0
        for (i <- 0 until points.length - 1) {
            val p1 = points(i)
            val p2 = points(i+1)
            val dx = Math.abs(p2(0) - p1(0))
            val dy = Math.abs(p2(1) - p1(1))
            totalTime += Math.max(dx, dy)
        }
        totalTime
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_time_to_visit_all_points(points: Vec<Vec<i32>>) -> i32 {
        let mut total_time = 0;
        for i in 1..points.len() {
            let p1 = &points[i - 1];
            let p2 = &points[i];
            let dx = (p2[0] - p1[0]).abs();
            let dy = (p2[1] - p1[1]).abs();
            total_time += dx.max(dy);
        }
        total_time
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-time-to-visit-all-points points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (if (<= (length points) 1)
      0
      (let loop ((prev-point (car points))
                 (remaining-points (cdr points))
                 (total-time 0))
        (if (empty? remaining-points)
            total-time
            (let* ((current-point (car remaining-points))
                   (x1 (list-ref prev-point 0))
                   (y1 (list-ref prev-point 1))
                   (x2 (list-ref current-point 0))
                   (y2 (list-ref current-point 1))
                   (dx (abs (- x2 x1)))
                   (dy (abs (- y2 y1))))
              (loop current-point
                    (cdr remaining-points)
                    (+ total-time (max dx dy))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_time_to_visit_all_points(Points :: [[integer()]]) -> integer().
min_time_to_visit_all_points(Points) ->
    min_time_to_visit_all_points(Points, 0).

min_time_to_visit_all_points([[X1, Y1], [X2, Y2] | Rest], Acc) ->
    DX = abs(X2 - X1),
    DY = abs(Y2 - Y1),
    Time = max(DX, DY),
    min_time_to_visit_all_points([[X2, Y2] | Rest], Acc + Time);
min_time_to_visit_all_points([_], Acc) ->
    Acc;
min_time_to_visit_all_points([], Acc) ->
    Acc.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_time_to_visit_all_points(points :: [[integer]]) :: integer
  def min_time_to_visit_all_points(points) do
    do_min_time_to_visit_all_points(points, 0)
  end

  defp do_min_time_to_visit_all_points([[x1, y1], [x2, y2] | rest], acc) do
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    time_segment = max(dx, dy)
    do_min_time_to_visit_all_points([[x2, y2] | rest], acc + time_segment)
  end

  defp do_min_time_to_visit_all_points([_], acc), do: acc
  defp do_min_time_to_visit_all_points([], acc), do: acc
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The algorithm iterates through the list of points once. For each of the n-1 pairs of consecutive points, it performs a constant number of arithmetic operations (subtraction, absolute value, and finding the maximum). Therefore, the time complexity is directly proportional to the number of points, N, making it O(N).

- **Space Complexity:** The algorithm uses a few integer variables to store the current coordinates, their differences, and the running total time. It does not allocate any additional data structures that scale with the input size. Hence, the space complexity is constant, O(1), excluding the space required to store the input points themselves.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-12 01:14:14 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by iterating over each pair of consecutive points and calculating the time it takes to move from one point to the next. The key intuition is to move diagonally as much as possible and then move in a straight line. This can be achieved by calculating the maximum of the absolute differences in the x and y coordinates between the two points, which represents the number of diagonal moves, and then adding any remaining moves in a straight line. 
The algorithm works by initializing a variable to store the total time and then iterating over each pair of points. For each pair, it calculates the time it takes to move from the first point to the second point and adds this to the total time. The time it takes to move from one point to the next is calculated as the maximum of the absolute differences in the x and y coordinates between the two points, which represents the number of diagonal moves, and then adding any remaining moves in a straight line.

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
class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int time = 0;
        for (int i = 1; i < points.size(); i++) {
            time += max(abs(points[i][0] - points[i-1][0]), abs(points[i][1] - points[i-1][1]));
        }
        return time;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int time = 0;
        for (int i = 1; i < points.length; i++) {
            time += Math.max(Math.abs(points[i][0] - points[i-1][0]), Math.abs(points[i][1] - points[i-1][1]));
        }
        return time;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        time = 0
        for i in range(1, len(points)):
            time += max(abs(points[i][0] - points[i-1][0]), abs(points[i][1] - points[i-1][1]))
        return time
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(1, len(points)):
            time += max(abs(points[i][0] - points[i-1][0]), abs(points[i][1] - points[i-1][1]))
        return time
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minTimeToVisitAllPoints(int** points, int pointsSize, int* pointsColSize) {
    int time = 0;
    for (int i = 1; i < pointsSize; i++) {
        time += (abs(points[i][0] - points[i-1][0]) > abs(points[i][1] - points[i-1][1])) ? abs(points[i][0] - points[i-1][0]) : abs(points[i][1] - points[i-1][1]);
    }
    return time;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution { 
    public int MinTimeToVisitAllPoints(int[][] points) { 
        int time = 0; 
        for (int i = 0; i < points.Length - 1; i++) { 
            int dx = Math.Abs(points[i + 1][0] - points[i][0]); 
            int dy = Math.Abs(points[i + 1][1] - points[i][1]); 
            time += Math.Max(dx, dy); 
        } 
        return time; 
    } 
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var minTimeToVisitAllPoints = function(points) { 
    let time = 0; 
    for (let i = 0; i < points.length - 1; i++) { 
        let dx = Math.abs(points[i + 1][0] - points[i][0]); 
        let dy = Math.abs(points[i + 1][1] - points[i][1]); 
        time += Math.max(dx, dy); 
    } 
    return time; 
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minTimeToVisitAllPoints(points: number[][]): number { 
    let time: number = 0; 
    for (let i: number = 0; i < points.length - 1; i++) { 
        let dx: number = Math.abs(points[i + 1][0] - points[i][0]); 
        let dy: number = Math.abs(points[i + 1][1] - points[i][1]); 
        time += Math.max(dx, dy); 
    } 
    return time; 
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution { 
    function minTimeToVisitAllPoints($points) { 
        $time = 0; 
        for ($i = 0; $i < count($points) - 1; $i++) { 
            $dx = abs($points[$i + 1][0] - $points[$i][0]); 
            $dy = abs($points[$i + 1][1] - $points[$i][1]); 
            $time += max($dx, $dy); 
        } 
        return $time; 
    } 
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution { 
    func minTimeToVisitAllPoints(_ points: [[Int]]) -> Int { 
        var time: Int = 0 
        for i in 0..<points.count - 1 { 
            let dx = abs(points[i + 1][0] - points[i][0]) 
            let dy = abs(points[i + 1][1] - points[i][1]) 
            time += max(dx, dy) 
        } 
        return time 
    } 
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minTimeToVisitAllPoints(points: Array<IntArray>): Int {
        var time = 0
        for (i in 0 until points.size - 1) {
            val xDiff = Math.abs(points[i][0] - points[i + 1][0])
            val yDiff = Math.abs(points[i][1] - points[i + 1][1])
            time += Math.max(xDiff, yDiff)
        }
        return time
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minTimeToVisitAllPoints(List<List<int>> points) {
    int time = 0;
    for (int i = 0; i < points.length - 1; i++) {
      int xDiff = (points[i][0] - points[i + 1][0]).abs();
      int yDiff = (points[i][1] - points[i + 1][1]).abs();
      time += xDiff > yDiff ? xDiff : yDiff;
    }
    return time;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minTimeToVisitAllPoints(points [][]int) int {
    time := 0
    for i := 0; i < len(points) - 1; i++ {
        xDiff := abs(points[i][0] - points[i + 1][0])
        yDiff := abs(points[i][1] - points[i + 1][1])
        time += max(xDiff, yDiff)
    }
    return time
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def min_time_to_visit_all_points(points)
    time = 0
    (0...points.size - 1).each do |i|
        x_diff = (points[i][0] - points[i + 1][0]).abs
        y_diff = (points[i][1] - points[i + 1][1]).abs
        time += [x_diff, y_diff].max
    end
    time
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minTimeToVisitAllPoints(points: Array[Array[Int]]): Int = {
        var time = 0
        for (i <- 0 until points.length - 1) {
            val xDiff = (points(i)(0) - points(i + 1)(0)).abs
            val yDiff = (points(i)(1) - points(i + 1)(1)).abs
            time += xDiff.max(yDiff)
        }
        time
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_time_to_visit_all_points(points: Vec<Vec<i32>>) -> i32 {
        let mut total_time = 0;
        for i in 0..points.len() - 1 {
            let x_diff = (points[i][0] - points[i + 1][0]).abs();
            let y_diff = (points[i][1] - points[i + 1][1]).abs();
            total_time += x_diff.max(y_diff);
        }
        total_time
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-time-to-visit-all-points points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let loop ([points points] [total-time 0])
    (if (null? (cdr points))
        total-time
        (loop (cdr points) (+ total-time (max (abs (- (caar points) (caadr points))) (abs (- (cadar points) (cadadr points)))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
min_time_to_visit_all_points(Points) ->
  lists:foldl(fun ([X1, Y1], [X2, Y2] = Point, Acc) ->
                  Acc + max(abs(X1 - X2), abs(Y1 - Y2))
              end, 0, Points).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_time_to_visit_all_points(points :: [[integer]]) :: integer
  def min_time_to_visit_all_points(points) do
    Enum.reduce(points, 0, fn [x1, y1], acc ->
      [x2, y2] = Enum.at(points, Enum.find_index(points, fn point -> point == [x1, y1] end) + 1)
      acc + max(abs(x1 - x2), abs(y1 - y2))
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n), where n is the number of points. This is because the algorithm iterates over each pair of points once, and the operations performed for each pair take constant time. The space complexity is O(1), which means the space required does not change with the size of the input, making it very efficient for large inputs.

- **Space Complexity:** The space complexity of this solution is O(1), which means the space required does not change with the size of the input. This is because the algorithm only uses a constant amount of space to store the total time and the current point, regardless of the number of points.

</div>
</details>
