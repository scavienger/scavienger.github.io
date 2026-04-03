---
layout: post
title: "Maximum Walls Destroyed by Robots"
date: 2026-04-03 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Binary Search", "Dynamic Programming", "Sorting"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/maximum-walls-destroyed-by-robots/
ai_solutions:
  - solutions:
      cpp: '// Generation failed for C++

        // Reason: Parsing failed'
      java: '// Generation failed for Java

        // Reason: Parsing failed'
      python: '// Generation failed for Python

        // Reason: Parsing failed'
      python3: '// Generation failed for Python3

        // Reason: Parsing failed'
      c: '// Generation failed for C

        // Reason: Parsing failed'
      csharp: '// Generation failed for C#

        // Reason: Parsing failed'
      javascript: '// Generation failed for JavaScript

        // Reason: Parsing failed'
      typescript: "function maxWalls(robots: number[], distance: number[], walls: number[]):\
        \ number {\n    const n = robots.length;\n    const m = walls.length;\n    const\
        \ robotData = robots.map((p, i) => ({ p, d: distance[i] })).sort((a, b) => a.p\
        \ - b.p);\n    walls.sort((a, b) => a.p - b.p);\n\n    const lowerBound = (target:\
        \ number) => {\n        let l = 0, r = m;\n        while (l < r) {\n       \
        \     let mid = (l + r) >> 1;\n            if (walls[mid] < target) l = mid\
        \ + 1;\n            else r = mid;\n        }\n        return l;\n    };\n  \
        \  const upperBound = (target: number) => {\n        let l = 0, r = m;\n   \
        \     while (l < r) {\n            let mid = (l + r) >> 1;\n            if (walls[mid]\
        \ <= target) l = mid + 1;\n            else r = mid;\n        }\n        return\
        \ l;\n    };\n    const count = (s: number, e: number) => (s > e ? 0 : upperBound(e)\
        \ - lowerBound(s));\n\n    const dp = Array.from({ length: n }, () => [0, 0]);\n\
        \    for (let i = 0; i < n; i++) {\n        const x = robotData[i].p;\n    \
        \    const d = robotData[i].d;\n        const lb = i > 0 ? Math.max(robotData[i\
        \ - 1].p + 1, x - d) : x - d;\n        const rb = i < n - 1 ? Math.min(robotData[i\
        \ + 1].p - 1, x + d) : x + d;\n\n        const cL = count(lb, x);\n        const\
        \ cR = count(x, rb);\n\n        if (i === 0) {\n            dp[i][0] = cL;\n\
        \            dp[i][1] = cR;\n        } else {\n            const xPrev = robotData[i\
        \ - 1].p;\n            const dPrev = robotData[i - 1].d;\n            const\
        \ overlapRangeStart = Math.max(xPrev + 1, x - d);\n            const overlapRangeEnd\
        \ = Math.min(x - 1, xPrev + dPrev);\n            const overlap = count(overlapRangeStart,\
        \ overlapRangeEnd);\n\n            dp[i][0] = cL + Math.max(dp[i - 1][0], dp[i\
        \ - 1][1] - overlap);\n            dp[i][1] = cR + Math.max(dp[i - 1][0], dp[i\
        \ - 1][1]);\n        }\n    }\n    return Math.max(dp[n - 1][0], dp[n - 1][1]);\n\
        }"
      php: "class Solution {\n    function maxWalls($robots, $distance, $walls) {\n\
        \        $n = count($robots);\n        $robotData = [];\n        for ($i = 0;\
        \ $i < $n; $i++) $robotData[] = ['p' => $robots[$i], 'd' => $distance[$i]];\n\
        \        usort($robotData, fn($a, $b) => $a['p'] <=> $b['p']);\n        sort($walls);\n\
        \        $m = count($walls);\n\n        $lb_func = function($target) use ($walls,\
        \ $m) {\n            $l = 0; $r = $m;\n            while ($l < $r) {\n     \
        \           $mid = (int)(($l + $r) / 2);\n                if ($walls[$mid] <\
        \ $target) $l = $mid + 1; else $r = $mid;\n            }\n            return\
        \ $l;\n        };\n        $ub_func = function($target) use ($walls, $m) {\n\
        \            $l = 0; $r = $m;\n            while ($l < $r) {\n             \
        \   $mid = (int)(($l + $r) / 2);\n                if ($walls[$mid] <= $target)\
        \ $l = $mid + 1; else $r = $mid;\n            }\n            return $l;\n  \
        \      };\n        $count = function($s, $e) use ($lb_func, $ub_func) { \n \
        \           return ($s > $e) ? 0 : $ub_func($e) - $lb_func($s);\n        };\n\
        \n        $dp = array_fill(0, $n, [0, 0]);\n        for ($i = 0; $i < $n; $i++)\
        \ {\n            $x = $robotData[$i]['p']; $d = $robotData[$i]['d'];\n     \
        \       $cL = $count($i > 0 ? max($robotData[$i-1]['p'] + 1, $x - $d) : $x -\
        \ $d, $x);\n            $cR = $count($x, $i < $n - 1 ? min($robotData[$i+1]['p']\
        \ - 1, $x + $d) : $x + $d);\n            if ($i == 0) {\n                $dp[$i][0]\
        \ = $cL; $dp[$i][1] = $cR;\n            } else {\n                $overlap =\
        \ $count(max($robotData[$i-1]['p'] + 1, $x - $d), min($x - 1, $robotData[$i-1]['p']\
        \ + $robotData[$i-1]['d']));\n                $dp[$i][0] = $cL + max($dp[$i-1][0],\
        \ $dp[$i-1][1] - $overlap);\n                $dp[$i][1] = $cR + max($dp[$i-1][0],\
        \ $dp[$i-1][1]);\n            }\n        }\n        return max($dp[$n-1][0],\
        \ $dp[$n-1][1]);\n    }\n}"
      swift: "class Solution {\n    func maxWalls(_ robots: [Int], _ distance: [Int],\
        \ _ walls: [Int]) -> Int {\n        let n = robots.count\n        var robotData\
        \ = (0..<n).map { (p: robots[$it], d: distance[$it]) }.sorted { $0.p < $1.p\
        \ }\n        let sortedWalls = walls.sorted()\n\n        func lowerBound(_ target:\
        \ Int) -> Int {\n            var l = 0, r = sortedWalls.count\n            while\
        \ l < r {\n                let mid = (l + r) / 2\n                if sortedWalls[mid]\
        \ < target { l = mid + 1 } else { r = mid }\n            }\n            return\
        \ l\n        }\n        func upperBound(_ target: Int) -> Int {\n          \
        \  var l = 0, r = sortedWalls.count\n            while l < r {\n           \
        \     let mid = (l + r) / 2\n                if sortedWalls[mid] <= target {\
        \ l = mid + 1 } else { r = mid }\n            }\n            return l\n    \
        \    }\n        func count(_ s: Int, _ e: Int) -> Int {\n            return\
        \ s > e ? 0 : upperBound(e) - lowerBound(s)\n        }\n\n        var dp = Array(repeating:\
        \ [0, 0], count: n)\n        for i in 0..<n {\n            let x = robotData[i].p,\
        \ d = robotData[i].d\n            let cL = count(i > 0 ? max(robotData[i-1].p\
        \ + 1, x - d) : x - d, x)\n            let cR = count(x, i < n - 1 ? min(robotData[i+1].p\
        \ - 1, x + d) : x + d)\n\n            if i == 0 {\n                dp[i][0]\
        \ = cL\n                dp[i][1] = cR\n            } else {\n              \
        \  let overlap = count(max(robotData[i-1].p + 1, x - d), min(x - 1, robotData[i-1].p\
        \ + robotData[i-1].d))\n                dp[i][0] = cL + max(dp[i-1][0], dp[i-1][1]\
        \ - overlap)\n                dp[i][1] = cR + max(dp[i-1][0], dp[i-1][1])\n\
        \            }\n        }\n        return dp[n - 1].max() ?? 0\n    }\n}"
      kotlin: "class Solution {\n    fun maxWalls(robots: IntArray, distance: IntArray,\
        \ walls: IntArray): Int {\n        val n = robots.size\n        val robotData\
        \ = robots.indices.map { i -> i }.sortedBy { robots[it] }\n        val sortedWalls\
        \ = walls.sortedArray()\n\n        fun lowerBound(target: Int): Int {\n    \
        \        var l = 0; var r = sortedWalls.size\n            while (l < r) {\n\
        \                val mid = (l + r) / 2\n                if (sortedWalls[mid]\
        \ < target) l = mid + 1 else r = mid\n            }\n            return l\n\
        \        }\n        fun upperBound(target: Int): Int {\n            var l =\
        \ 0; var r = sortedWalls.size\n            while (l < r) {\n               \
        \ val mid = (l + r) / 2\n                if (sortedWalls[mid] <= target) l =\
        \ mid + 1 else r = mid\n            }\n            return l\n        }\n   \
        \     fun countWallsInRange(s: Int, e: Int) = if (s > e) 0 else upperBound(e)\
        \ - lowerBound(s)\n\n        val dp = Array(n) { IntArray(2) }\n        for\
        \ (i in 0 until n) {\n            val idx = robotData[i]\n            val x\
        \ = robots[idx]; val d = distance[idx]\n            val cL = countWallsInRange(if\
        \ (i > 0) maxOf(robots[robotData[i-1]] + 1, x - d) else x - d, x)\n        \
        \    val cR = countWallsInRange(x, if (i < n - 1) minOf(robots[robotData[i+1]]\
        \ - 1, x + d) else x + d)\n\n            if (i == 0) {\n                dp[i][0]\
        \ = cL\n                dp[i][1] = cR\n            } else {\n              \
        \  val xPrev = robots[robotData[i-1]]\n                val dPrev = distance[robotData[i-1]]\n\
        \                val overlap = countWallsInRange(maxOf(xPrev + 1, x - d), minOf(x\
        \ - 1, xPrev + dPrev))\n                dp[i][0] = cL + maxOf(dp[i-1][0], dp[i-1][1]\
        \ - overlap)\n                dp[i][1] = cR + maxOf(dp[i-1][0], dp[i-1][1])\n\
        \            }\n        }\n        return maxOf(dp[n-1][0], dp[n-1][1])\n  \
        \  }\n}"
      dart: "class Solution {\n  int maxWalls(List<int> robots, List<int> distance,\
        \ List<int> walls) {\n    int n = robots.length;\n    List<Map<String, int>>\
        \ robotData = [];\n    for (int i = 0; i < n; i++) robotData.add({'p': robots[i],\
        \ 'd': distance[i]});\n    robotData.sort((a, b) => a['p']!.compareTo(b['p']!));\n\
        \    walls.sort();\n\n    int lowerBound(int target) {\n      int l = 0, r =\
        \ walls.length;\n      while (l < r) {\n        int m = (l + r) ~/ 2;\n    \
        \    if (walls[m] < target) l = m + 1; else r = m;\n      }\n      return l;\n\
        \    }\n    int upperBound(int target) {\n      int l = 0, r = walls.length;\n\
        \      while (l < r) {\n        int m = (l + r) ~/ 2;\n        if (walls[m]\
        \ <= target) l = m + 1; else r = m;\n      }\n      return l;\n    }\n    int\
        \ countInRange(int s, int e) => (s > e) ? 0 : upperBound(e) - lowerBound(s);\n\
        \n    List<List<int>> dp = List.generate(n, (_) => [0, 0]);\n    for (int i\
        \ = 0; i < n; i++) {\n      int x = robotData[i]['p']!, d = robotData[i]['d']!;\n\
        \      int cL = countInRange(i > 0 ? (robotData[i - 1]['p']! + 1 > x - d ? robotData[i\
        \ - 1]['p']! + 1 : x - d) : x - d, x);\n      int cR = countInRange(x, i < n\
        \ - 1 ? (robotData[i + 1]['p']! - 1 < x + d ? robotData[i + 1]['p']! - 1 : x\
        \ + d) : x + d);\n\n      if (i == 0) {\n        dp[i][0] = cL; dp[i][1] = cR;\n\
        \      } else {\n        int prevP = robotData[i - 1]['p']!, prevD = robotData[i\
        \ - 1]['d']!;\n        int overlapStart = prevP + 1 > x - d ? prevP + 1 : x\
        \ - d;\n        int overlapEnd = x - 1 < prevP + prevD ? x - 1 : prevP + prevD;\n\
        \        int overlap = countInRange(overlapStart, overlapEnd);\n        dp[i][0]\
        \ = cL + (dp[i - 1][0] > dp[i - 1][1] - overlap ? dp[i - 1][0] : dp[i - 1][1]\
        \ - overlap);\n        dp[i][1] = cR + (dp[i - 1][0] > dp[i - 1][1] ? dp[i -\
        \ 1][0] : dp[i - 1][1]);\n      }\n    }\n    return dp[n - 1][0] > dp[n - 1][1]\
        \ ? dp[n - 1][0] : dp[n - 1][1];\n  }\n}"
      go: "func maxWalls(robots []int, distance []int, walls []int) int {\n    n :=\
        \ len(robots)\n    type Robot struct{ p, d int }\n    robotData := make([]Robot,\
        \ n)\n    for i := 0; i < n; i++ { robotData[i] = Robot{robots[i], distance[i]}\
        \ }\n    sort.Slice(robotData, func(i, j int) bool { return robotData[i].p <\
        \ robotData[j].p })\n    sort.Ints(walls)\n\n    countInRange := func(s, e int)\
        \ int {\n        if s > e { return 0 }\n        lb := sort.SearchInts(walls,\
        \ s)\n        ub := sort.Search(len(walls), func(i int) bool { return walls[i]\
        \ > e })\n        return ub - lb\n    }\n\n    dp := make([][2]int, n)\n   \
        \ for i := 0; i < n; i++ {\n        x, d := robotData[i].p, robotData[i].d\n\
        \        lBound := x - d\n        if i > 0 && robotData[i-1].p+1 > lBound {\
        \ lBound = robotData[i-1].p + 1 }\n        rBound := x + d\n        if i < n-1\
        \ && robotData[i+1].p-1 < rBound { rBound = robotData[i+1].p - 1 }\n\n     \
        \   cL, cR := countInRange(lBound, x), countInRange(x, rBound)\n        if i\
        \ == 0 {\n            dp[i][0], dp[i][1] = cL, cR\n        } else {\n      \
        \      oStart := x - d\n            if robotData[i-1].p+1 > oStart { oStart\
        \ = robotData[i-1].p + 1 }\n            oEnd := x - 1\n            if robotData[i-1].p+robotData[i-1].d\
        \ < oEnd { oEnd = robotData[i-1].p + robotData[i-1].d }\n            overlap\
        \ := countInRange(oStart, oEnd)\n\n            val0 := dp[i-1][0]; if dp[i-1][1]-overlap\
        \ > val0 { val0 = dp[i-1][1] - overlap }\n            val1 := dp[i-1][0]; if\
        \ dp[i-1][1] > val1 { val1 = dp[i-1][1] }\n            dp[i][0], dp[i][1] =\
        \ cL+val0, cR+val1\n        }\n    }\n    if dp[n-1][0] > dp[n-1][1] { return\
        \ dp[n-1][0] }; return dp[n-1][1]\n}"
      ruby: '// Generation failed for Ruby

        // Reason: Parsing failed'
      scala: '// Generation failed for Scala

        // Reason: Parsing failed'
      rust: '// Generation failed for Rust

        // Reason: Parsing failed'
      racket: '// Generation failed for Racket

        // Reason: Parsing failed'
      erlang: '// Generation failed for Erlang

        // Reason: Parsing failed'
      elixir: '// Generation failed for Elixir

        // Reason: Parsing failed'
    approach: To maximize the number of unique walls destroyed, we first sort both the
      robots (along with their firing distances) and the walls by their positions. For
      each robot $i$ at position $x_i$, its bullet can travel either left or right but
      is stopped by any adjacent robot. Thus, its potential ranges are $[\max(x_{i-1}
      + 1, x_i - d_i), x_i]$ if firing left, and $[x_i, \min(x_{i+1} - 1, x_i + d_i)]$
      if firing right. Using binary search on the sorted walls array, we can efficiently
      count the number of walls within these specific ranges for every robot.
    time_complexity: O(N log N + M log M + N log M) where N is the number of robots
      and M is the number of walls. Sorting robots takes O(N log N), sorting walls takes
      O(M log M), and the DP iterates N times, performing a constant number of binary
      searches O(log M) per step.
    space_complexity: O(N + M) to store the sorted robots, distances, walls, and the
      DP table.
    elapsed_time: 814.4292221069336
    model: gemini-3-flash-preview
    generated_at: '2026-04-03 04:57:57 '
---

## Problem #3661: Maximum Walls Destroyed by Robots

**Difficulty:** Hard

**Topics:** Array, Binary Search, Dynamic Programming, Sorting

## Problem Description

<div data-docx-has-block-data="false" data-lark-html-role="root" data-page-id="Rax8d6clvoFeVtx7bzXcvkVynwf">
<div class="old-record-id-Y5dGdSKIMoNTttxGhHLccrpEnaf">There is an endless straight line populated with some robots and walls. You are given integer arrays <code>robots</code>, <code>distance</code>, and <code>walls</code>:</div>
</div>

<ul>
	<li><code>robots[i]</code> is the position of the <code>i<sup>th</sup></code> robot.</li>
	<li><code>distance[i]</code> is the <strong>maximum</strong> distance the <code>i<sup>th</sup></code> robot&#39;s bullet can travel.</li>
	<li><code>walls[j]</code> is the position of the <code>j<sup>th</sup></code> wall.</li>
</ul>

<p>Every robot has <strong>one</strong> bullet that can either fire to the left or the right <strong>at most </strong><code>distance[i]</code> meters.</p>

<p>A bullet destroys every wall in its path that lies within its range. Robots are fixed obstacles: if a bullet hits another robot before reaching a wall, it <strong>immediately stops</strong> at that robot and cannot continue.</p>

<p>Return the <strong>maximum</strong> number of <strong>unique</strong> walls that can be destroyed by the robots.</p>

<p>Notes:</p>

<ul>
	<li>A wall and a robot may share the same position; the wall can be destroyed by the robot at that position.</li>
	<li>Robots are not destroyed by bullets.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">robots = [4], distance = [3], walls = [1,10]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>robots[0] = 4</code> fires <strong>left</strong> with <code>distance[0] = 3</code>, covering <code>[1, 4]</code> and destroys <code>walls[0] = 1</code>.</li>
	<li>Thus, the answer is 1.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">robots = [10,2], distance = [5,1], walls = [5,2,7]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>robots[0] = 10</code> fires <strong>left</strong> with <code>distance[0] = 5</code>, covering <code>[5, 10]</code> and destroys <code>walls[0] = 5</code> and <code>walls[2] = 7</code>.</li>
	<li><code>robots[1] = 2</code> fires <strong>left</strong> with <code>distance[1] = 1</code>, covering <code>[1, 2]</code> and destroys <code>walls[1] = 2</code>.</li>
	<li>Thus, the answer is 3.</li>
</ul>
</div>
<strong class="example">Example 3:</strong>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">robots = [1,2], distance = [100,1], walls = [10]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>In this example, only <code>robots[0]</code> can reach the wall, but its shot to the <strong>right</strong> is blocked by <code>robots[1]</code>; thus the answer is 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= robots.length == distance.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= walls.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= robots[i], walls[j] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= distance[i] &lt;= 10<sup>5</sup></code></li>
	<li>All values in <code>robots</code> are <strong>unique</strong></li>
	<li>All values in <code>walls</code> are <strong>unique</strong></li>
</ul>


## Hints

1. Sort both the robots and walls arrays. This will help in efficiently processing positions and performing range queries.

2. Each robot can shoot either left or right. However, if a robot fires and another robot is in its path, the bullet stops. You need to use the positions of neighboring robots to limit the shooting range.

3. Use binary search (lower_bound and upper_bound) to count how many walls fall within a certain range.

4. You can use dynamic programming to keep track of the maximum number of walls destroyed so far, depending on the direction the previous robot shot.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To maximize the number of unique walls destroyed, we first sort both the robots (along with their firing distances) and the walls by their positions. For each robot $i$ at position $x_i$, its bullet can travel either left or right but is stopped by any adjacent robot. Thus, its potential ranges are $[\max(x_{i-1} + 1, x_i - d_i), x_i]$ if firing left, and $[x_i, \min(x_{i+1} - 1, x_i + d_i)]$ if firing right. Using binary search on the sorted walls array, we can efficiently count the number of walls within these specific ranges for every robot.

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
// Generation failed for C++
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Generation failed for C#
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Generation failed for JavaScript
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxWalls(robots: number[], distance: number[], walls: number[]): number {
    const n = robots.length;
    const m = walls.length;
    const robotData = robots.map((p, i) => ({ p, d: distance[i] })).sort((a, b) => a.p - b.p);
    walls.sort((a, b) => a.p - b.p);

    const lowerBound = (target: number) => {
        let l = 0, r = m;
        while (l < r) {
            let mid = (l + r) >> 1;
            if (walls[mid] < target) l = mid + 1;
            else r = mid;
        }
        return l;
    };
    const upperBound = (target: number) => {
        let l = 0, r = m;
        while (l < r) {
            let mid = (l + r) >> 1;
            if (walls[mid] <= target) l = mid + 1;
            else r = mid;
        }
        return l;
    };
    const count = (s: number, e: number) => (s > e ? 0 : upperBound(e) - lowerBound(s));

    const dp = Array.from({ length: n }, () => [0, 0]);
    for (let i = 0; i < n; i++) {
        const x = robotData[i].p;
        const d = robotData[i].d;
        const lb = i > 0 ? Math.max(robotData[i - 1].p + 1, x - d) : x - d;
        const rb = i < n - 1 ? Math.min(robotData[i + 1].p - 1, x + d) : x + d;

        const cL = count(lb, x);
        const cR = count(x, rb);

        if (i === 0) {
            dp[i][0] = cL;
            dp[i][1] = cR;
        } else {
            const xPrev = robotData[i - 1].p;
            const dPrev = robotData[i - 1].d;
            const overlapRangeStart = Math.max(xPrev + 1, x - d);
            const overlapRangeEnd = Math.min(x - 1, xPrev + dPrev);
            const overlap = count(overlapRangeStart, overlapRangeEnd);

            dp[i][0] = cL + Math.max(dp[i - 1][0], dp[i - 1][1] - overlap);
            dp[i][1] = cR + Math.max(dp[i - 1][0], dp[i - 1][1]);
        }
    }
    return Math.max(dp[n - 1][0], dp[n - 1][1]);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function maxWalls($robots, $distance, $walls) {
        $n = count($robots);
        $robotData = [];
        for ($i = 0; $i < $n; $i++) $robotData[] = ['p' => $robots[$i], 'd' => $distance[$i]];
        usort($robotData, fn($a, $b) => $a['p'] <=> $b['p']);
        sort($walls);
        $m = count($walls);

        $lb_func = function($target) use ($walls, $m) {
            $l = 0; $r = $m;
            while ($l < $r) {
                $mid = (int)(($l + $r) / 2);
                if ($walls[$mid] < $target) $l = $mid + 1; else $r = $mid;
            }
            return $l;
        };
        $ub_func = function($target) use ($walls, $m) {
            $l = 0; $r = $m;
            while ($l < $r) {
                $mid = (int)(($l + $r) / 2);
                if ($walls[$mid] <= $target) $l = $mid + 1; else $r = $mid;
            }
            return $l;
        };
        $count = function($s, $e) use ($lb_func, $ub_func) { 
            return ($s > $e) ? 0 : $ub_func($e) - $lb_func($s);
        };

        $dp = array_fill(0, $n, [0, 0]);
        for ($i = 0; $i < $n; $i++) {
            $x = $robotData[$i]['p']; $d = $robotData[$i]['d'];
            $cL = $count($i > 0 ? max($robotData[$i-1]['p'] + 1, $x - $d) : $x - $d, $x);
            $cR = $count($x, $i < $n - 1 ? min($robotData[$i+1]['p'] - 1, $x + $d) : $x + $d);
            if ($i == 0) {
                $dp[$i][0] = $cL; $dp[$i][1] = $cR;
            } else {
                $overlap = $count(max($robotData[$i-1]['p'] + 1, $x - $d), min($x - 1, $robotData[$i-1]['p'] + $robotData[$i-1]['d']));
                $dp[$i][0] = $cL + max($dp[$i-1][0], $dp[$i-1][1] - $overlap);
                $dp[$i][1] = $cR + max($dp[$i-1][0], $dp[$i-1][1]);
            }
        }
        return max($dp[$n-1][0], $dp[$n-1][1]);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxWalls(_ robots: [Int], _ distance: [Int], _ walls: [Int]) -> Int {
        let n = robots.count
        var robotData = (0..<n).map { (p: robots[$it], d: distance[$it]) }.sorted { $0.p < $1.p }
        let sortedWalls = walls.sorted()

        func lowerBound(_ target: Int) -> Int {
            var l = 0, r = sortedWalls.count
            while l < r {
                let mid = (l + r) / 2
                if sortedWalls[mid] < target { l = mid + 1 } else { r = mid }
            }
            return l
        }
        func upperBound(_ target: Int) -> Int {
            var l = 0, r = sortedWalls.count
            while l < r {
                let mid = (l + r) / 2
                if sortedWalls[mid] <= target { l = mid + 1 } else { r = mid }
            }
            return l
        }
        func count(_ s: Int, _ e: Int) -> Int {
            return s > e ? 0 : upperBound(e) - lowerBound(s)
        }

        var dp = Array(repeating: [0, 0], count: n)
        for i in 0..<n {
            let x = robotData[i].p, d = robotData[i].d
            let cL = count(i > 0 ? max(robotData[i-1].p + 1, x - d) : x - d, x)
            let cR = count(x, i < n - 1 ? min(robotData[i+1].p - 1, x + d) : x + d)

            if i == 0 {
                dp[i][0] = cL
                dp[i][1] = cR
            } else {
                let overlap = count(max(robotData[i-1].p + 1, x - d), min(x - 1, robotData[i-1].p + robotData[i-1].d))
                dp[i][0] = cL + max(dp[i-1][0], dp[i-1][1] - overlap)
                dp[i][1] = cR + max(dp[i-1][0], dp[i-1][1])
            }
        }
        return dp[n - 1].max() ?? 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxWalls(robots: IntArray, distance: IntArray, walls: IntArray): Int {
        val n = robots.size
        val robotData = robots.indices.map { i -> i }.sortedBy { robots[it] }
        val sortedWalls = walls.sortedArray()

        fun lowerBound(target: Int): Int {
            var l = 0; var r = sortedWalls.size
            while (l < r) {
                val mid = (l + r) / 2
                if (sortedWalls[mid] < target) l = mid + 1 else r = mid
            }
            return l
        }
        fun upperBound(target: Int): Int {
            var l = 0; var r = sortedWalls.size
            while (l < r) {
                val mid = (l + r) / 2
                if (sortedWalls[mid] <= target) l = mid + 1 else r = mid
            }
            return l
        }
        fun countWallsInRange(s: Int, e: Int) = if (s > e) 0 else upperBound(e) - lowerBound(s)

        val dp = Array(n) { IntArray(2) }
        for (i in 0 until n) {
            val idx = robotData[i]
            val x = robots[idx]; val d = distance[idx]
            val cL = countWallsInRange(if (i > 0) maxOf(robots[robotData[i-1]] + 1, x - d) else x - d, x)
            val cR = countWallsInRange(x, if (i < n - 1) minOf(robots[robotData[i+1]] - 1, x + d) else x + d)

            if (i == 0) {
                dp[i][0] = cL
                dp[i][1] = cR
            } else {
                val xPrev = robots[robotData[i-1]]
                val dPrev = distance[robotData[i-1]]
                val overlap = countWallsInRange(maxOf(xPrev + 1, x - d), minOf(x - 1, xPrev + dPrev))
                dp[i][0] = cL + maxOf(dp[i-1][0], dp[i-1][1] - overlap)
                dp[i][1] = cR + maxOf(dp[i-1][0], dp[i-1][1])
            }
        }
        return maxOf(dp[n-1][0], dp[n-1][1])
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxWalls(List<int> robots, List<int> distance, List<int> walls) {
    int n = robots.length;
    List<Map<String, int>> robotData = [];
    for (int i = 0; i < n; i++) robotData.add({'p': robots[i], 'd': distance[i]});
    robotData.sort((a, b) => a['p']!.compareTo(b['p']!));
    walls.sort();

    int lowerBound(int target) {
      int l = 0, r = walls.length;
      while (l < r) {
        int m = (l + r) ~/ 2;
        if (walls[m] < target) l = m + 1; else r = m;
      }
      return l;
    }
    int upperBound(int target) {
      int l = 0, r = walls.length;
      while (l < r) {
        int m = (l + r) ~/ 2;
        if (walls[m] <= target) l = m + 1; else r = m;
      }
      return l;
    }
    int countInRange(int s, int e) => (s > e) ? 0 : upperBound(e) - lowerBound(s);

    List<List<int>> dp = List.generate(n, (_) => [0, 0]);
    for (int i = 0; i < n; i++) {
      int x = robotData[i]['p']!, d = robotData[i]['d']!;
      int cL = countInRange(i > 0 ? (robotData[i - 1]['p']! + 1 > x - d ? robotData[i - 1]['p']! + 1 : x - d) : x - d, x);
      int cR = countInRange(x, i < n - 1 ? (robotData[i + 1]['p']! - 1 < x + d ? robotData[i + 1]['p']! - 1 : x + d) : x + d);

      if (i == 0) {
        dp[i][0] = cL; dp[i][1] = cR;
      } else {
        int prevP = robotData[i - 1]['p']!, prevD = robotData[i - 1]['d']!;
        int overlapStart = prevP + 1 > x - d ? prevP + 1 : x - d;
        int overlapEnd = x - 1 < prevP + prevD ? x - 1 : prevP + prevD;
        int overlap = countInRange(overlapStart, overlapEnd);
        dp[i][0] = cL + (dp[i - 1][0] > dp[i - 1][1] - overlap ? dp[i - 1][0] : dp[i - 1][1] - overlap);
        dp[i][1] = cR + (dp[i - 1][0] > dp[i - 1][1] ? dp[i - 1][0] : dp[i - 1][1]);
      }
    }
    return dp[n - 1][0] > dp[n - 1][1] ? dp[n - 1][0] : dp[n - 1][1];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxWalls(robots []int, distance []int, walls []int) int {
    n := len(robots)
    type Robot struct{ p, d int }
    robotData := make([]Robot, n)
    for i := 0; i < n; i++ { robotData[i] = Robot{robots[i], distance[i]} }
    sort.Slice(robotData, func(i, j int) bool { return robotData[i].p < robotData[j].p })
    sort.Ints(walls)

    countInRange := func(s, e int) int {
        if s > e { return 0 }
        lb := sort.SearchInts(walls, s)
        ub := sort.Search(len(walls), func(i int) bool { return walls[i] > e })
        return ub - lb
    }

    dp := make([][2]int, n)
    for i := 0; i < n; i++ {
        x, d := robotData[i].p, robotData[i].d
        lBound := x - d
        if i > 0 && robotData[i-1].p+1 > lBound { lBound = robotData[i-1].p + 1 }
        rBound := x + d
        if i < n-1 && robotData[i+1].p-1 < rBound { rBound = robotData[i+1].p - 1 }

        cL, cR := countInRange(lBound, x), countInRange(x, rBound)
        if i == 0 {
            dp[i][0], dp[i][1] = cL, cR
        } else {
            oStart := x - d
            if robotData[i-1].p+1 > oStart { oStart = robotData[i-1].p + 1 }
            oEnd := x - 1
            if robotData[i-1].p+robotData[i-1].d < oEnd { oEnd = robotData[i-1].p + robotData[i-1].d }
            overlap := countInRange(oStart, oEnd)

            val0 := dp[i-1][0]; if dp[i-1][1]-overlap > val0 { val0 = dp[i-1][1] - overlap }
            val1 := dp[i-1][0]; if dp[i-1][1] > val1 { val1 = dp[i-1][1] }
            dp[i][0], dp[i][1] = cL+val0, cR+val1
        }
    }
    if dp[n-1][0] > dp[n-1][1] { return dp[n-1][0] }; return dp[n-1][1]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
// Generation failed for Ruby
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
// Generation failed for Scala
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
// Generation failed for Rust
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
// Generation failed for Racket
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
// Generation failed for Erlang
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
// Generation failed for Elixir
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log N + M log M + N log M) where N is the number of robots and M is the number of walls. Sorting robots takes O(N log N), sorting walls takes O(M log M), and the DP iterates N times, performing a constant number of binary searches O(log M) per step.
- **Space Complexity:** O(N + M) to store the sorted robots, distances, walls, and the DP table.
