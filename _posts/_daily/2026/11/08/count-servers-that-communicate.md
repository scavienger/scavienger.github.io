---
layout: post
title: "Count Servers that Communicate"
date: 2026-11-08 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Depth-First Search", "Breadth-First Search", "Union-Find", "Matrix", "Counting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-servers-that-communicate/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int countServers(vector<vector<int>>& grid)\
        \ {\n        int m = grid.size();\n        int n = grid[0].size();\n       \
        \ vector<int> rows(m, 0), cols(n, 0);\n\n        for (int i = 0; i < m; ++i)\
        \ {\n            for (int j = 0; j < n; ++j) {\n                if (grid[i][j]\
        \ == 1) {\n                    ++rows[i];\n                    ++cols[j];\n\
        \                }\n            }\n        }\n\n        int count = 0;\n   \
        \     for (int i = 0; i < m; ++i) {\n            for (int j = 0; j < n; ++j)\
        \ {\n                if (grid[i][j] == 1 && (rows[i] > 1 || cols[j] > 1)) {\n\
        \                    ++count;\n                }\n            }\n        }\n\
        \        return count;\n    }\n};"
      java: "class Solution {\n    public int countServers(int[][] grid) {\n       \
        \ int m = grid.length;\n        int n = grid[0].length;\n        int[] rows\
        \ = new int[m];\n        int[] cols = new int[n];\n\n        for (int i = 0;\
        \ i < m; i++) {\n            for (int j = 0; j < n; j++) {\n               \
        \ if (grid[i][j] == 1) {\n                    rows[i]++;\n                 \
        \   cols[j]++;\n                }\n            }\n        }\n\n        int count\
        \ = 0;\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j\
        \ < n; j++) {\n                if (grid[i][j] == 1 && (rows[i] > 1 || cols[j]\
        \ > 1)) {\n                    count++;\n                }\n            }\n\
        \        }\n        return count;\n    }\n}"
      python: "class Solution(object):\n    def countServers(self, grid):\n        \"\
        \"\"\n        :type grid: List[List[int]]\n        :rtype: int\n        \"\"\
        \"\n        m = len(grid)\n        n = len(grid[0])\n        rows = [0] * m\n\
        \        cols = [0] * n\n\n        for i in range(m):\n            for j in\
        \ range(n):\n                if grid[i][j] == 1:\n                    rows[i]\
        \ += 1\n                    cols[j] += 1\n\n        count = 0\n        for i\
        \ in range(m):\n            for j in range(n):\n                if grid[i][j]\
        \ == 1 and (rows[i] > 1 or cols[j] > 1):\n                    count += 1\n \
        \       return count"
      python3: "class Solution:\n    def countServers(self, grid: list[list[int]]) ->\
        \ int:\n        m = len(grid)\n        n = len(grid[0])\n        rows = [0]\
        \ * m\n        cols = [0] * n\n\n        for i in range(m):\n            for\
        \ j in range(n):\n                if grid[i][j] == 1:\n                    rows[i]\
        \ += 1\n                    cols[j] += 1\n\n        count = 0\n        for i\
        \ in range(m):\n            for j in range(n):\n                if grid[i][j]\
        \ == 1 and (rows[i] > 1 or cols[j] > 1):\n                    count += 1\n \
        \       return count"
      c: "int countServers(int** grid, int gridSize, int* gridColSize) {\n    int n\
        \ = gridColSize[0];\n    int* rows = (int*)calloc(gridSize, sizeof(int));\n\
        \    int* cols = (int*)calloc(n, sizeof(int));\n\n    for (int i = 0; i < gridSize;\
        \ ++i) {\n        for (int j = 0; j < n; ++j) {\n            if (grid[i][j]\
        \ == 1) {\n                ++rows[i];\n                ++cols[j];\n        \
        \    }\n        }\n    }\n\n    int count = 0;\n    for (int i = 0; i < gridSize;\
        \ ++i) {\n        for (int j = 0; j < n; ++j) {\n            if (grid[i][j]\
        \ == 1 && (rows[i] > 1 || cols[j] > 1)) {\n                ++count;\n      \
        \      }\n        }\n    }\n\n    free(rows);\n    free(cols);\n    return count;\n\
        }"
      csharp: "public class Solution {\n    public int CountServers(int[][] grid) {\n\
        \        int m = grid.Length;\n        int n = grid[0].Length;\n        int[]\
        \ rows = new int[m];\n        int[] cols = new int[n];\n\n        for (int i\
        \ = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n          \
        \      if (grid[i][j] == 1) {\n                    rows[i]++;\n            \
        \        cols[j]++;\n                }\n            }\n        }\n\n       \
        \ int count = 0;\n        for (int i = 0; i < m; i++) {\n            for (int\
        \ j = 0; j < n; j++) {\n                if (grid[i][j] == 1 && (rows[i] > 1\
        \ || cols[j] > 1)) {\n                    count++;\n                }\n    \
        \        }\n        }\n        return count;\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @return {number}\n */\nvar countServers\
        \ = function(grid) {\n    const m = grid.length;\n    const n = grid[0].length;\n\
        \    const rows = Array(m).fill(0);\n    const cols = Array(n).fill(0);\n\n\
        \    for (let i = 0; i < m; i++) {\n        for (let j = 0; j < n; j++) {\n\
        \            if (grid[i][j] === 1) {\n                rows[i]++;\n         \
        \       cols[j]++;\n            }\n        }\n    }\n\n    let count = 0;\n\
        \    for (let i = 0; i < m; i++) {\n        for (let j = 0; j < n; j++) {\n\
        \            if (grid[i][j] === 1 && (rows[i] > 1 || cols[j] > 1)) {\n     \
        \           count++;\n            }\n        }\n    }\n    return count;\n};"
      typescript: "function countServers(grid: number[][]): number {\n    const m =\
        \ grid.length;\n    const n = grid[0].length;\n    const rows = Array(m).fill(0);\n\
        \    const cols = Array(n).fill(0);\n\n    for (let i = 0; i < m; i++) {\n \
        \       for (let j = 0; j < n; j++) {\n            if (grid[i][j] === 1) {\n\
        \                rows[i]++;\n                cols[j]++;\n            }\n   \
        \     }\n    }\n\n    let count = 0;\n    for (let i = 0; i < m; i++) {\n  \
        \      for (let j = 0; j < n; j++) {\n            if (grid[i][j] === 1 && (rows[i]\
        \ > 1 || cols[j] > 1)) {\n                count++;\n            }\n        }\n\
        \    }\n    return count;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @return\
        \ Integer\n     */\n    function countServers($grid) {\n        $m = count($grid);\n\
        \        $n = count($grid[0]);\n        $rows = array_fill(0, $m, 0);\n    \
        \    $cols = array_fill(0, $n, 0);\n\n        for ($i = 0; $i < $m; $i++) {\n\
        \            for ($j = 0; $j < $n; $j++) {\n                if ($grid[$i][$j]\
        \ === 1) {\n                    $rows[$i]++;\n                    $cols[$j]++;\n\
        \                }\n            }\n        }\n\n        $count = 0;\n      \
        \  for ($i = 0; $i < $m; $i++) {\n            for ($j = 0; $j < $n; $j++) {\n\
        \                if ($grid[$i][$j] === 1 && ($rows[$i] > 1 || $cols[$j] > 1))\
        \ {\n                    $count++;\n                }\n            }\n     \
        \   }\n        return $count;\n    }\n}"
      swift: "class Solution {\n    func countServers(_ grid: [[Int]]) -> Int {\n  \
        \      let m = grid.count\n        let n = grid[0].count\n        var rows =\
        \ Array(repeating: 0, count: m)\n        var cols = Array(repeating: 0, count:\
        \ n)\n\n        for i in 0..<m {\n            for j in 0..<n {\n           \
        \     if grid[i][j] == 1 {\n                    rows[i] += 1\n             \
        \       cols[j] += 1\n                }\n            }\n        }\n\n      \
        \  var count = 0\n        for i in 0..<m {\n            for j in 0..<n {\n \
        \               if grid[i][j] == 1 && (rows[i] > 1 || cols[j] > 1) {\n     \
        \               count += 1\n                }\n            }\n        }\n  \
        \      return count\n    }\n}"
      kotlin: "class Solution {\n    fun countServers(grid: Array<IntArray>): Int {\n\
        \        val m = grid.size\n        val n = grid[0].size\n        val rows =\
        \ IntArray(m)\n        val cols = IntArray(n)\n\n        for (i in 0 until m)\
        \ {\n            for (j in 0 until n) {\n                if (grid[i][j] == 1)\
        \ {\n                    rows[i]++\n                    cols[j]++\n        \
        \        }\n            }\n        }\n\n        var count = 0\n        for (i\
        \ in 0 until m) {\n            for (j in 0 until n) {\n                if (grid[i][j]\
        \ == 1 && (rows[i] > 1 || cols[j] > 1)) {\n                    count++\n   \
        \             }\n            }\n        }\n        return count\n    }\n}"
      dart: "class Solution {\n  int countServers(List<List<int>> grid) {\n    final\
        \ m = grid.length;\n    final n = grid[0].length;\n    final rows = List<int>.filled(m,\
        \ 0);\n    final cols = List<int>.filled(n, 0);\n\n    for (var i = 0; i < m;\
        \ i++) {\n      for (var j = 0; j < n; j++) {\n        if (grid[i][j] == 1)\
        \ {\n          rows[i]++;\n          cols[j]++;\n        }\n      }\n    }\n\
        \n    var count = 0;\n    for (var i = 0; i < m; i++) {\n      for (var j =\
        \ 0; j < n; j++) {\n        if (grid[i][j] == 1 && (rows[i] > 1 || cols[j] >\
        \ 1)) {\n          count++;\n        }\n      }\n    }\n    return count;\n\
        \  }\n}"
      go: "func countServers(grid [][]int) int {\n\tm := len(grid)\n\tn := len(grid[0])\n\
        \trows := make([]int, m)\n\tcols := make([]int, n)\n\n\tfor i := 0; i < m; i++\
        \ {\n\t\tfor j := 0; j < n; j++ {\n\t\t\tif grid[i][j] == 1 {\n\t\t\t\trows[i]++\n\
        \t\t\t\tcols[j]++\n\t\t\t}\n\t\t}\n\t}\n\n\tcount := 0\n\tfor i := 0; i < m;\
        \ i++ {\n\t\tfor j := 0; j < n; j++ {\n\t\t\tif grid[i][j] == 1 && (rows[i]\
        \ > 1 || cols[j] > 1) {\n\t\t\t\tcount++\n\t\t\t}\n\t\t}\n\t}\n\treturn count\n\
        }"
      ruby: "# @param {Integer[][]} grid\n# @return {Integer}\ndef count_servers(grid)\n\
        \  m = grid.length\n  n = grid[0].length\n  rows = Array.new(m, 0)\n  cols =\
        \ Array.new(n, 0)\n\n  m.times do |i|\n    n.times do |j|\n      if grid[i][j]\
        \ == 1\n        rows[i] += 1\n        cols[j] += 1\n      end\n    end\n  end\n\
        \n  count = 0\n  m.times do |i|\n    n.times do |j|\n      if grid[i][j] ==\
        \ 1 && (rows[i] > 1 || cols[j] > 1)\n        count += 1\n      end\n    end\n\
        \  end\n  count\nend"
      scala: "object Solution {\n    def countServers(grid: Array[Array[Int]]): Int\
        \ = {\n        val m = grid.length\n        val n = grid(0).length\n       \
        \ val rows = Array.fill(m)(0)\n        val cols = Array.fill(n)(0)\n\n     \
        \   for (i <- 0 until m) {\n            for (j <- 0 until n) {\n           \
        \     if (grid(i)(j) == 1) {\n                    rows(i) += 1\n           \
        \         cols(j) += 1\n                }\n            }\n        }\n\n    \
        \    var count = 0\n        for (i <- 0 until m) {\n            for (j <- 0\
        \ until n) {\n                if (grid(i)(j) == 1 && (rows(i) > 1 || cols(j)\
        \ > 1)) {\n                    count += 1\n                }\n            }\n\
        \        }\n        count\n    }\n}"
      rust: "impl Solution {\n    pub fn count_servers(grid: Vec<Vec<i32>>) -> i32 {\n\
        \        let m = grid.len();\n        let n = grid[0].len();\n        let mut\
        \ rows = vec![0; m];\n        let mut cols = vec![0; n];\n\n        for i in\
        \ 0..m {\n            for j in 0..n {\n                if grid[i][j] == 1 {\n\
        \                    rows[i] += 1;\n                    cols[j] += 1;\n    \
        \            }\n            }\n        }\n\n        let mut count = 0;\n   \
        \     for i in 0..m {\n            for j in 0..n {\n                if grid[i][j]\
        \ == 1 && (rows[i] > 1 || cols[j] > 1) {\n                    count += 1;\n\
        \                }\n            }\n        }\n        count\n    }\n}"
      racket: "(define/contract (count-servers grid)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer?)\n  (let* ([m (length grid)]\n         [n (length (car grid))]\n\
        \         [rows (make-vector m 0)]\n         [cols (make-vector n 0)])\n   \
        \ (for ([i (in-range m)])\n      (for ([j (in-range n)])\n        (when (= (list-ref\
        \ (list-ref grid i) j) 1)\n          (vector-set! rows i (add1 (vector-ref rows\
        \ i)))\n          (vector-set! cols j (add1 (vector-ref cols j)))))\n    (for*/sum\
        \ ([i (in-range m)]\n               [j (in-range n)])\n      (if (and (= (list-ref\
        \ (list-ref grid i) j) 1)\n               (or (> (vector-ref rows i) 1)\n  \
        \                 (> (vector-ref cols j) 1)))\n          1\n          0))))"
      erlang: "-spec count_servers(Grid :: [[integer()]]) -> integer().\ncount_servers(Grid)\
        \ ->\n  M = length(Grid),\n  N = length(hd(Grid)),\n  Rows = lists:duplicate(M,\
        \ 0),\n  Cols = lists:duplicate(N, 0),\n  {RowCounts, ColCounts} = lists:foldl(\n\
        \    fun({Row, I}, {RAcc, CAcc}) ->\n      lists:foldl(\n        fun({Cell,\
        \ J}, {RInner, CInner}) ->\n          case Cell of\n            1 ->\n     \
        \         {increment_at(I, RInner), increment_at(J, CInner)};\n            _\
        \ ->\n              {RInner, CInner}\n          end\n        end,\n        {RAcc,\
        \ CAcc},\n        lists:zip(Row, lists:seq(1, N))\n      )\n    end,\n    {Rows,\
        \ Cols},\n    lists:zip(Grid, lists:seq(1, M))\n  ),\n  lists:sum([\n    case\
        \ Cell =:= 1 andalso (lists:nth(I, RowCounts) > 1 orelse lists:nth(J, ColCounts)\
        \ > 1) of\n      true -> 1;\n      false -> 0\n    end\n    || {Row, I} <- lists:zip(Grid,\
        \ lists:seq(1, M)),\n       {Cell, J} <- lists:zip(Row, lists:seq(1, N))\n \
        \ ]).\n\nincrement_at(Index, List) ->\n  {Before, [Value | After]} = lists:split(Index\
        \ - 1, List),\n  Before ++ [Value + 1 | After]."
      elixir: "defmodule Solution do\n  @spec count_servers(grid :: [[integer]]) ::\
        \ integer\n  def count_servers(grid) do\n    m = length(grid)\n    n = length(hd(grid))\n\
        \n    {rows, cols} =\n      grid\n      |> Enum.with_index()\n      |> Enum.reduce({List.duplicate(0,\
        \ m), List.duplicate(0, n)}, fn {row, i}, {rows, cols} ->\n        row\n   \
        \     |> Enum.with_index()\n        |> Enum.reduce({rows, cols}, fn {cell, j},\
        \ {row_counts, col_counts} ->\n          if cell == 1 do\n            {List.update_at(row_counts,\
        \ i, &(&1 + 1)),\n             List.update_at(col_counts, j, &(&1 + 1))}\n \
        \         else\n            {row_counts, col_counts}\n          end\n      \
        \  end)\n      end)\n\n    grid\n    |> Enum.with_index()\n    |> Enum.reduce(0,\
        \ fn {row, i}, count ->\n      row\n      |> Enum.with_index()\n      |> Enum.reduce(count,\
        \ fn {cell, j}, acc ->\n        if cell == 1 and (Enum.at(rows, i) > 1 or Enum.at(cols,\
        \ j) > 1) do\n          acc + 1\n        else\n          acc\n        end\n\
        \      end)\n    end)\n  end\nend"
    approach: 'First, count the servers in each row and column. Then inspect every cell
      containing a server and include it if its row or column has more than one server.


      A server communicates with another server exactly when they share a row or column,
      so this counts every communicating server once and excludes isolated servers.'
    time_complexity: O(m * n), since the grid is traversed twice.
    space_complexity: O(m + n) for the row and column counts.
    elapsed_time: 92.63179469108582
    model: gpt-6-luna
    generated_at: '2026-11-12 23:44:20 '
---

## Problem #1267: Count Servers that Communicate

**Difficulty:** Medium

**Topics:** Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix, Counting

## Problem Description

<p>You are given a map of a server center, represented as a <code>m * n</code> integer matrix&nbsp;<code>grid</code>, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.<br />
<br />
Return the number of servers&nbsp;that communicate with any other server.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/11/14/untitled-diagram-6.jpg" style="width: 202px; height: 203px;" /></p>

<pre>
<strong>Input:</strong> grid = [[1,0],[0,1]]
<strong>Output:</strong> 0
<b>Explanation:</b>&nbsp;No servers can communicate with others.</pre>

<p><strong class="example">Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/11/13/untitled-diagram-4.jpg" style="width: 203px; height: 203px;" /></strong></p>

<pre>
<strong>Input:</strong> grid = [[1,0],[1,1]]
<strong>Output:</strong> 3
<b>Explanation:</b>&nbsp;All three servers can communicate with at least one other server.
</pre>

<p><strong class="example">Example 3:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/11/14/untitled-diagram-1-3.jpg" style="width: 443px; height: 443px;" /></p>

<pre>
<strong>Input:</strong> grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
<strong>Output:</strong> 4
<b>Explanation:</b>&nbsp;The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can&#39;t communicate with any other server.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m &lt;= 250</code></li>
	<li><code>1 &lt;= n &lt;= 250</code></li>
	<li><code>grid[i][j] == 0 or 1</code></li>
</ul>


## Hints

1. Store number of computer in each row and column.

2. Count all servers that are not isolated.

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

First, count the servers in each row and column. Then inspect every cell containing a server and include it if its row or column has more than one server.

A server communicates with another server exactly when they share a row or column, so this counts every communicating server once and excludes isolated servers.

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
    int countServers(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<int> rows(m, 0), cols(n, 0);

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    ++rows[i];
                    ++cols[j];
                }
            }
        }

        int count = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1 && (rows[i] > 1 || cols[j] > 1)) {
                    ++count;
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
class Solution {
    public int countServers(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] rows = new int[m];
        int[] cols = new int[n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    rows[i]++;
                    cols[j]++;
                }
            }
        }

        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 && (rows[i] > 1 || cols[j] > 1)) {
                    count++;
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
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        rows = [0] * m
        cols = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rows = [0] * m
        cols = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countServers(int** grid, int gridSize, int* gridColSize) {
    int n = gridColSize[0];
    int* rows = (int*)calloc(gridSize, sizeof(int));
    int* cols = (int*)calloc(n, sizeof(int));

    for (int i = 0; i < gridSize; ++i) {
        for (int j = 0; j < n; ++j) {
            if (grid[i][j] == 1) {
                ++rows[i];
                ++cols[j];
            }
        }
    }

    int count = 0;
    for (int i = 0; i < gridSize; ++i) {
        for (int j = 0; j < n; ++j) {
            if (grid[i][j] == 1 && (rows[i] > 1 || cols[j] > 1)) {
                ++count;
            }
        }
    }

    free(rows);
    free(cols);
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountServers(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int[] rows = new int[m];
        int[] cols = new int[n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    rows[i]++;
                    cols[j]++;
                }
            }
        }

        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 && (rows[i] > 1 || cols[j] > 1)) {
                    count++;
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
 * @param {number[][]} grid
 * @return {number}
 */
var countServers = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const rows = Array(m).fill(0);
    const cols = Array(n).fill(0);

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                rows[i]++;
                cols[j]++;
            }
        }
    }

    let count = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1 && (rows[i] > 1 || cols[j] > 1)) {
                count++;
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
function countServers(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const rows = Array(m).fill(0);
    const cols = Array(n).fill(0);

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                rows[i]++;
                cols[j]++;
            }
        }
    }

    let count = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1 && (rows[i] > 1 || cols[j] > 1)) {
                count++;
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
     * @param Integer[][] $grid
     * @return Integer
     */
    function countServers($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $rows = array_fill(0, $m, 0);
        $cols = array_fill(0, $n, 0);

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] === 1) {
                    $rows[$i]++;
                    $cols[$j]++;
                }
            }
        }

        $count = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] === 1 && ($rows[$i] > 1 || $cols[$j] > 1)) {
                    $count++;
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
    func countServers(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var rows = Array(repeating: 0, count: m)
        var cols = Array(repeating: 0, count: n)

        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == 1 {
                    rows[i] += 1
                    cols[j] += 1
                }
            }
        }

        var count = 0
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == 1 && (rows[i] > 1 || cols[j] > 1) {
                    count += 1
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
    fun countServers(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val rows = IntArray(m)
        val cols = IntArray(n)

        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == 1) {
                    rows[i]++
                    cols[j]++
                }
            }
        }

        var count = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == 1 && (rows[i] > 1 || cols[j] > 1)) {
                    count++
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
  int countServers(List<List<int>> grid) {
    final m = grid.length;
    final n = grid[0].length;
    final rows = List<int>.filled(m, 0);
    final cols = List<int>.filled(n, 0);

    for (var i = 0; i < m; i++) {
      for (var j = 0; j < n; j++) {
        if (grid[i][j] == 1) {
          rows[i]++;
          cols[j]++;
        }
      }
    }

    var count = 0;
    for (var i = 0; i < m; i++) {
      for (var j = 0; j < n; j++) {
        if (grid[i][j] == 1 && (rows[i] > 1 || cols[j] > 1)) {
          count++;
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
func countServers(grid [][]int) int {
	m := len(grid)
	n := len(grid[0])
	rows := make([]int, m)
	cols := make([]int, n)

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				rows[i]++
				cols[j]++
			}
		}
	}

	count := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 && (rows[i] > 1 || cols[j] > 1) {
				count++
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
# @param {Integer[][]} grid
# @return {Integer}
def count_servers(grid)
  m = grid.length
  n = grid[0].length
  rows = Array.new(m, 0)
  cols = Array.new(n, 0)

  m.times do |i|
    n.times do |j|
      if grid[i][j] == 1
        rows[i] += 1
        cols[j] += 1
      end
    end
  end

  count = 0
  m.times do |i|
    n.times do |j|
      if grid[i][j] == 1 && (rows[i] > 1 || cols[j] > 1)
        count += 1
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
    def countServers(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        val n = grid(0).length
        val rows = Array.fill(m)(0)
        val cols = Array.fill(n)(0)

        for (i <- 0 until m) {
            for (j <- 0 until n) {
                if (grid(i)(j) == 1) {
                    rows(i) += 1
                    cols(j) += 1
                }
            }
        }

        var count = 0
        for (i <- 0 until m) {
            for (j <- 0 until n) {
                if (grid(i)(j) == 1 && (rows(i) > 1 || cols(j) > 1)) {
                    count += 1
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
    pub fn count_servers(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut rows = vec![0; m];
        let mut cols = vec![0; n];

        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    rows[i] += 1;
                    cols[j] += 1;
                }
            }
        }

        let mut count = 0;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 && (rows[i] > 1 || cols[j] > 1) {
                    count += 1;
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
(define/contract (count-servers grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([m (length grid)]
         [n (length (car grid))]
         [rows (make-vector m 0)]
         [cols (make-vector n 0)])
    (for ([i (in-range m)])
      (for ([j (in-range n)])
        (when (= (list-ref (list-ref grid i) j) 1)
          (vector-set! rows i (add1 (vector-ref rows i)))
          (vector-set! cols j (add1 (vector-ref cols j)))))
    (for*/sum ([i (in-range m)]
               [j (in-range n)])
      (if (and (= (list-ref (list-ref grid i) j) 1)
               (or (> (vector-ref rows i) 1)
                   (> (vector-ref cols j) 1)))
          1
          0))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec count_servers(Grid :: [[integer()]]) -> integer().
count_servers(Grid) ->
  M = length(Grid),
  N = length(hd(Grid)),
  Rows = lists:duplicate(M, 0),
  Cols = lists:duplicate(N, 0),
  {RowCounts, ColCounts} = lists:foldl(
    fun({Row, I}, {RAcc, CAcc}) ->
      lists:foldl(
        fun({Cell, J}, {RInner, CInner}) ->
          case Cell of
            1 ->
              {increment_at(I, RInner), increment_at(J, CInner)};
            _ ->
              {RInner, CInner}
          end
        end,
        {RAcc, CAcc},
        lists:zip(Row, lists:seq(1, N))
      )
    end,
    {Rows, Cols},
    lists:zip(Grid, lists:seq(1, M))
  ),
  lists:sum([
    case Cell =:= 1 andalso (lists:nth(I, RowCounts) > 1 orelse lists:nth(J, ColCounts) > 1) of
      true -> 1;
      false -> 0
    end
    || {Row, I} <- lists:zip(Grid, lists:seq(1, M)),
       {Cell, J} <- lists:zip(Row, lists:seq(1, N))
  ]).

increment_at(Index, List) ->
  {Before, [Value | After]} = lists:split(Index - 1, List),
  Before ++ [Value + 1 | After].
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_servers(grid :: [[integer]]) :: integer
  def count_servers(grid) do
    m = length(grid)
    n = length(hd(grid))

    {rows, cols} =
      grid
      |> Enum.with_index()
      |> Enum.reduce({List.duplicate(0, m), List.duplicate(0, n)}, fn {row, i}, {rows, cols} ->
        row
        |> Enum.with_index()
        |> Enum.reduce({rows, cols}, fn {cell, j}, {row_counts, col_counts} ->
          if cell == 1 do
            {List.update_at(row_counts, i, &(&1 + 1)),
             List.update_at(col_counts, j, &(&1 + 1))}
          else
            {row_counts, col_counts}
          end
        end)
      end)

    grid
    |> Enum.with_index()
    |> Enum.reduce(0, fn {row, i}, count ->
      row
      |> Enum.with_index()
      |> Enum.reduce(count, fn {cell, j}, acc ->
        if cell == 1 and (Enum.at(rows, i) > 1 or Enum.at(cols, j) > 1) do
          acc + 1
        else
          acc
        end
      end)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m * n), since the grid is traversed twice.
- **Space Complexity:** O(m + n) for the row and column counts.
