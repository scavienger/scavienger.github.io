---
layout: post
title: "Increment Submatrices by One"
date: 2025-11-14 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Matrix", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/increment-submatrices-by-one/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<vector<int>> rangeAddQueries(int n,\
        \ vector<vector<int>>& queries) {\n        vector<vector<int>> mat(n, vector<int>(n\
        \ + 1, 0));\n        for (const auto& query : queries) {\n            int row1\
        \ = query[0];\n            int col1 = query[1];\n            int row2 = query[2];\n\
        \            int col2 = query[3];\n            for (int row = row1; row <= row2;\
        \ ++row) {\n                ++mat[row][col1];\n                --mat[row][col2\
        \ + 1];\n            }\n        }\n        for (int row = 0; row < n; ++row)\
        \ {\n            for (int col = 1; col < n; ++col) {\n                mat[row][col]\
        \ += mat[row][col - 1];\n            }\n            mat[row].resize(n);\n  \
        \      }\n        return mat;\n    }\n};"
      java: "class Solution {\n    public int[][] rangeAddQueries(int n, int[][] queries)\
        \ {\n        int[][] mat = new int[n][n + 1];\n        for (int[] query : queries)\
        \ {\n            int row1 = query[0];\n            int col1 = query[1];\n  \
        \          int row2 = query[2];\n            int col2 = query[3];\n        \
        \    for (int row = row1; row <= row2; row++) {\n                mat[row][col1]++;\n\
        \                mat[row][col2 + 1]--;\n            }\n        }\n        int[][]\
        \ result = new int[n][n];\n        for (int row = 0; row < n; row++) {\n   \
        \         int running = 0;\n            for (int col = 0; col < n; col++) {\n\
        \                running += mat[row][col];\n                result[row][col]\
        \ = running;\n            }\n        }\n        return result;\n    }\n}"
      python: "class Solution(object):\n    def rangeAddQueries(self, n, queries):\n\
        \        \"\"\"\n        :type n: int\n        :type queries: List[List[int]]\n\
        \        :rtype: List[List[int]]\n        \"\"\"\n        mat = [[0] * (n +\
        \ 1) for _ in range(n)]\n        for row1, col1, row2, col2 in queries:\n  \
        \          for row in range(row1, row2 + 1):\n                mat[row][col1]\
        \ += 1\n                mat[row][col2 + 1] -= 1\n        result = [[0] * n for\
        \ _ in range(n)]\n        for row in range(n):\n            running = 0\n  \
        \          for col in range(n):\n                running += mat[row][col]\n\
        \                result[row][col] = running\n        return result"
      python3: "class Solution:\n    def rangeAddQueries(self, n: int, queries: list[list[int]])\
        \ -> list[list[int]]:\n        mat = [[0] * (n + 1) for _ in range(n)]\n   \
        \     for row1, col1, row2, col2 in queries:\n            for row in range(row1,\
        \ row2 + 1):\n                mat[row][col1] += 1\n                mat[row][col2\
        \ + 1] -= 1\n        result = [[0] * n for _ in range(n)]\n        for row in\
        \ range(n):\n            running = 0\n            for col in range(n):\n   \
        \             running += mat[row][col]\n                result[row][col] = running\n\
        \        return result"
      c: "#include <stdlib.h>\n\nint** rangeAddQueries(int n, int** queries, int queriesSize,\
        \ int* queriesColSize, int* returnSize, int** returnColumnSizes) {\n    int**\
        \ mat = (int**)calloc(n, sizeof(int*));\n    for (int row = 0; row < n; row++)\
        \ {\n        mat[row] = (int*)calloc(n + 1, sizeof(int));\n    }\n    for (int\
        \ i = 0; i < queriesSize; i++) {\n        int row1 = queries[i][0];\n      \
        \  int col1 = queries[i][1];\n        int row2 = queries[i][2];\n        int\
        \ col2 = queries[i][3];\n        for (int row = row1; row <= row2; row++) {\n\
        \            mat[row][col1]++;\n            mat[row][col2 + 1]--;\n        }\n\
        \    }\n    int** result = (int**)malloc(n * sizeof(int*));\n    *returnColumnSizes\
        \ = (int*)malloc(n * sizeof(int));\n    for (int row = 0; row < n; row++) {\n\
        \        result[row] = (int*)malloc(n * sizeof(int));\n        (*returnColumnSizes)[row]\
        \ = n;\n        int running = 0;\n        for (int col = 0; col < n; col++)\
        \ {\n            running += mat[row][col];\n            result[row][col] = running;\n\
        \        }\n        free(mat[row]);\n    }\n    free(mat);\n    *returnSize\
        \ = n;\n    return result;\n}"
      csharp: "public class Solution {\n    public int[][] RangeAddQueries(int n, int[][]\
        \ queries) {\n        int[][] mat = new int[n][];\n        for (int row = 0;\
        \ row < n; row++) {\n            mat[row] = new int[n + 1];\n        }\n\n \
        \       foreach (int[] query in queries) {\n            int row1 = query[0];\n\
        \            int col1 = query[1];\n            int row2 = query[2];\n      \
        \      int col2 = query[3];\n\n            for (int row = row1; row <= row2;\
        \ row++) {\n                mat[row][col1]++;\n                mat[row][col2\
        \ + 1]--;\n            }\n        }\n\n        int[][] result = new int[n][];\n\
        \        for (int row = 0; row < n; row++) {\n            result[row] = new\
        \ int[n];\n            int running = 0;\n            for (int col = 0; col <\
        \ n; col++) {\n                running += mat[row][col];\n                result[row][col]\
        \ = running;\n            }\n        }\n\n        return result;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number[][]} queries\n * @return\
        \ {number[][]}\n */\nvar rangeAddQueries = function(n, queries) {\n    const\
        \ mat = Array.from({ length: n }, () => Array(n + 1).fill(0));\n\n    for (const\
        \ [row1, col1, row2, col2] of queries) {\n        for (let row = row1; row <=\
        \ row2; row++) {\n            mat[row][col1]++;\n            mat[row][col2 +\
        \ 1]--;\n        }\n    }\n\n    const result = Array.from({ length: n }, ()\
        \ => Array(n).fill(0));\n    for (let row = 0; row < n; row++) {\n        let\
        \ running = 0;\n        for (let col = 0; col < n; col++) {\n            running\
        \ += mat[row][col];\n            result[row][col] = running;\n        }\n  \
        \  }\n\n    return result;\n};"
      typescript: "function rangeAddQueries(n: number, queries: number[][]): number[][]\
        \ {\n    const mat: number[][] = Array.from({ length: n }, () => Array(n + 1).fill(0));\n\
        \n    for (const [row1, col1, row2, col2] of queries) {\n        for (let row\
        \ = row1; row <= row2; row++) {\n            mat[row][col1]++;\n           \
        \ mat[row][col2 + 1]--;\n        }\n    }\n\n    const result: number[][] =\
        \ Array.from({ length: n }, () => Array(n).fill(0));\n    for (let row = 0;\
        \ row < n; row++) {\n        let running = 0;\n        for (let col = 0; col\
        \ < n; col++) {\n            running += mat[row][col];\n            result[row][col]\
        \ = running;\n        }\n    }\n\n    return result;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @param Integer[][]\
        \ $queries\n     * @return Integer[][]\n     */\n    function rangeAddQueries($n,\
        \ $queries) {\n        $mat = array_fill(0, $n, array_fill(0, $n + 1, 0));\n\
        \n        foreach ($queries as $query) {\n            [$row1, $col1, $row2,\
        \ $col2] = $query;\n            for ($row = $row1; $row <= $row2; $row++) {\n\
        \                $mat[$row][$col1]++;\n                $mat[$row][$col2 + 1]--;\n\
        \            }\n        }\n\n        $result = array_fill(0, $n, array_fill(0,\
        \ $n, 0));\n        for ($row = 0; $row < $n; $row++) {\n            $running\
        \ = 0;\n            for ($col = 0; $col < $n; $col++) {\n                $running\
        \ += $mat[$row][$col];\n                $result[$row][$col] = $running;\n  \
        \          }\n        }\n\n        return $result;\n    }\n}"
      swift: "class Solution {\n    func rangeAddQueries(_ n: Int, _ queries: [[Int]])\
        \ -> [[Int]] {\n        var mat = Array(repeating: Array(repeating: 0, count:\
        \ n + 1), count: n)\n\n        for query in queries {\n            let row1\
        \ = query[0]\n            let col1 = query[1]\n            let row2 = query[2]\n\
        \            let col2 = query[3]\n\n            for row in row1...row2 {\n \
        \               mat[row][col1] += 1\n                mat[row][col2 + 1] -= 1\n\
        \            }\n        }\n\n        var result = Array(repeating: Array(repeating:\
        \ 0, count: n), count: n)\n        for row in 0..<n {\n            var running\
        \ = 0\n            for col in 0..<n {\n                running += mat[row][col]\n\
        \                result[row][col] = running\n            }\n        }\n\n  \
        \      return result\n    }\n}"
      kotlin: "class Solution {\n    fun rangeAddQueries(n: Int, queries: Array<IntArray>):\
        \ Array<IntArray> {\n        val diff = Array(n) { IntArray(n + 1) }\n     \
        \   for (query in queries) {\n            val row1 = query[0]\n            val\
        \ col1 = query[1]\n            val row2 = query[2]\n            val col2 = query[3]\n\
        \            for (row in row1..row2) {\n                diff[row][col1] += 1\n\
        \                diff[row][col2 + 1] -= 1\n            }\n        }\n      \
        \  val result = Array(n) { IntArray(n) }\n        for (row in 0 until n) {\n\
        \            var running = 0\n            for (col in 0 until n) {\n       \
        \         running += diff[row][col]\n                result[row][col] = running\n\
        \            }\n        }\n        return result\n    }\n}"
      dart: "class Solution {\n  List<List<int>> rangeAddQueries(int n, List<List<int>>\
        \ queries) {\n    final diff = List.generate(n, (_) => List<int>.filled(n +\
        \ 1, 0));\n    for (final query in queries) {\n      final row1 = query[0];\n\
        \      final col1 = query[1];\n      final row2 = query[2];\n      final col2\
        \ = query[3];\n      for (var row = row1; row <= row2; row++) {\n        diff[row][col1]\
        \ += 1;\n        diff[row][col2 + 1] -= 1;\n      }\n    }\n    final result\
        \ = List.generate(n, (_) => List<int>.filled(n, 0));\n    for (var row = 0;\
        \ row < n; row++) {\n      var running = 0;\n      for (var col = 0; col < n;\
        \ col++) {\n        running += diff[row][col];\n        result[row][col] = running;\n\
        \      }\n    }\n    return result;\n  }\n}"
      go: "func rangeAddQueries(n int, queries [][]int) [][]int {\n\tdiff := make([][]int,\
        \ n)\n\tfor row := range diff {\n\t\tdiff[row] = make([]int, n+1)\n\t}\n\tfor\
        \ _, query := range queries {\n\t\trow1, col1, row2, col2 := query[0], query[1],\
        \ query[2], query[3]\n\t\tfor row := row1; row <= row2; row++ {\n\t\t\tdiff[row][col1]++\n\
        \t\t\tdiff[row][col2+1]--\n\t\t}\n\t}\n\tresult := make([][]int, n)\n\tfor row\
        \ := 0; row < n; row++ {\n\t\tresult[row] = make([]int, n)\n\t\trunning := 0\n\
        \t\tfor col := 0; col < n; col++ {\n\t\t\trunning += diff[row][col]\n\t\t\t\
        result[row][col] = running\n\t\t}\n\t}\n\treturn result\n}"
      ruby: "# @param {Integer} n\n# @param {Integer[][]} queries\n# @return {Integer[][]}\n\
        def range_add_queries(n, queries)\n    diff = Array.new(n) { Array.new(n + 1,\
        \ 0) }\n    queries.each do |query|\n        row1, col1, row2, col2 = query\n\
        \        (row1..row2).each do |row|\n            diff[row][col1] += 1\n    \
        \        diff[row][col2 + 1] -= 1\n        end\n    end\n    result = Array.new(n)\
        \ { Array.new(n, 0) }\n    n.times do |row|\n        running = 0\n        n.times\
        \ do |col|\n            running += diff[row][col]\n            result[row][col]\
        \ = running\n        end\n    end\n    result\nend"
      scala: "object Solution {\n    def rangeAddQueries(n: Int, queries: Array[Array[Int]]):\
        \ Array[Array[Int]] = {\n        val diff = Array.fill(n, n + 1)(0)\n      \
        \  for (query <- queries) {\n            val row1 = query(0)\n            val\
        \ col1 = query(1)\n            val row2 = query(2)\n            val col2 = query(3)\n\
        \            for (row <- row1 to row2) {\n                diff(row)(col1) +=\
        \ 1\n                diff(row)(col2 + 1) -= 1\n            }\n        }\n  \
        \      val result = Array.fill(n, n)(0)\n        for (row <- 0 until n) {\n\
        \            var running = 0\n            for (col <- 0 until n) {\n       \
        \         running += diff(row)(col)\n                result(row)(col) = running\n\
        \            }\n        }\n        result\n    }\n}"
      rust: "impl Solution {\n    pub fn range_add_queries(n: i32, queries: Vec<Vec<i32>>)\
        \ -> Vec<Vec<i32>> {\n        let n = n as usize;\n        let mut diff = vec![vec![0;\
        \ n + 1]; n];\n\n        for query in queries {\n            let row1 = query[0]\
        \ as usize;\n            let col1 = query[1] as usize;\n            let row2\
        \ = query[2] as usize;\n            let col2 = query[3] as usize;\n\n      \
        \      for row in row1..=row2 {\n                diff[row][col1] += 1;\n   \
        \             diff[row][col2 + 1] -= 1;\n            }\n        }\n\n      \
        \  let mut result = vec![vec![0; n]; n];\n        for row in 0..n {\n      \
        \      let mut running = 0;\n            for col in 0..n {\n               \
        \ running += diff[row][col];\n                result[row][col] = running;\n\
        \            }\n        }\n\n        result\n    }\n}"
      racket: "(define/contract (range-add-queries n queries)\n  (-> exact-integer?\
        \ (listof (listof exact-integer?)) (listof (listof exact-integer?)))\n  (let\
        \ ([diff (build-vector n (lambda (_) (make-vector (add1 n) 0)))])\n    (for\
        \ ([query queries])\n      (define row1 (list-ref query 0))\n      (define col1\
        \ (list-ref query 1))\n      (define row2 (list-ref query 2))\n      (define\
        \ col2 (list-ref query 3))\n      (for ([row (in-range row1 (add1 row2))])\n\
        \        (vector-set! (vector-ref diff row) col1\n                     (add1\
        \ (vector-ref (vector-ref diff row) col1)))\n        (vector-set! (vector-ref\
        \ diff row) (add1 col2)\n                     (sub1 (vector-ref (vector-ref\
        \ diff row) (add1 col2)))))\n    (for/list ([row (in-range n)])\n      (define\
        \ running 0)\n      (for/list ([col (in-range n)])\n        (set! running (+\
        \ running (vector-ref (vector-ref diff row) col)))\n        running))))"
      erlang: "-spec range_add_queries(N :: integer(), Queries :: [[integer()]]) ->\
        \ [[integer()]].\nrange_add_queries(N, Queries) ->\n  Diff0 = [lists:duplicate(N\
        \ + 1, 0) || _ <- lists:seq(1, N)],\n  Diff = lists:foldl(\n    fun([Row1, Col1,\
        \ Row2, Col2], Acc) ->\n      lists:foldl(\n        fun(Row, Rows) ->\n    \
        \      Current = lists:nth(Row + 1, Rows),\n          Updated = update_at(Col2\
        \ + 2,\n            update_at(Col1 + 1, lists:nth(Col1 + 1, Current) + 1, Current),\n\
        \            lists:sublist(Current, Col2 + 1) ++ [lists:nth(Col2 + 2, Current)\
        \ - 1 | lists:nthtail(Col2 + 2, Current)]),\n          replace_at(Row + 1, Updated,\
        \ Rows)\n        end,\n        Acc,\n        lists:seq(Row1, Row2))\n    end,\n\
        \    Diff0,\n    Queries),\n  [row_prefix(lists:sublist(Row, N), 0, []) || Row\
        \ <- Diff].\n\nupdate_at(1, Value, [_ | Tail]) -> [Value | Tail];\nupdate_at(Index,\
        \ Value, [Head | Tail]) -> [Head | update_at(Index - 1, Value, Tail)].\n\nreplace_at(1,\
        \ Value, [_ | Tail]) -> [Value | Tail];\nreplace_at(Index, Value, [Head | Tail])\
        \ -> [Head | replace_at(Index - 1, Value, Tail)].\n\nrow_prefix([], _Running,\
        \ Acc) -> lists:reverse(Acc);\nrow_prefix([Value | Rest], Running, Acc) ->\n\
        \  Next = Running + Value,\n  row_prefix(Rest, Next, [Next | Acc])."
      elixir: "defmodule Solution do\n  @spec range_add_queries(n :: integer, queries\
        \ :: [[integer]]) :: [[integer]]\n  def range_add_queries(n, queries) do\n \
        \   diff = for _ <- 1..n, do: List.duplicate(0, n + 1)\n\n    diff =\n     \
        \ Enum.reduce(queries, diff, fn [row1, col1, row2, col2], rows ->\n        Enum.reduce(row1..row2,\
        \ rows, fn row, acc ->\n          current = Enum.at(acc, row)\n          current\
        \ = List.update_at(current, col1, &(&1 + 1))\n          current = List.update_at(current,\
        \ col2 + 1, &(&1 - 1))\n          List.replace_at(acc, row, current)\n     \
        \   end)\n      end)\n\n    Enum.map(diff, fn row ->\n      row\n      |> Enum.take(n)\n\
        \      |> Enum.scan(0, &(&1 + &2))\n    end)\n  end\nend"
    approach: 'Create an n by n difference matrix. For each query, add 1 at the left
      column and subtract 1 just after the right column for every affected row, so each
      query takes time proportional to its height. The extra column at index n records
      boundary updates safely.


      Then compute prefix sums across each row. The running sum at each cell gives the
      total number of queries that cover it, producing the final matrix.'
    time_complexity: O(n^2 + qn), where q is the number of queries. Each query updates
      at most n rows, and the final row-wise prefix sums visit all n^2 cells.
    space_complexity: O(n^2) for the difference matrix, which is also used to store
      the result.
    elapsed_time: 103.56173944473267
    model: gpt-6-luna
    generated_at: '2026-11-12 23:59:59 '
---

## Problem #2536: Increment Submatrices by One

**Difficulty:** Medium

**Topics:** Array, Matrix, Prefix Sum

## Problem Description

<p>You are given a positive integer <code>n</code>, indicating that we initially have an <code>n x n</code>&nbsp;<strong>0-indexed</strong> integer matrix <code>mat</code> filled with zeroes.</p>

<p>You are also given a 2D integer array <code>query</code>. For each <code>query[i] = [row1<sub>i</sub>, col1<sub>i</sub>, row2<sub>i</sub>, col2<sub>i</sub>]</code>, you should do the following operation:</p>

<ul>
	<li>Add <code>1</code> to <strong>every element</strong> in the submatrix with the <strong>top left</strong> corner <code>(row1<sub>i</sub>, col1<sub>i</sub>)</code> and the <strong>bottom right</strong> corner <code>(row2<sub>i</sub>, col2<sub>i</sub>)</code>. That is, add <code>1</code> to <code>mat[x][y]</code> for all <code>row1<sub>i</sub> &lt;= x &lt;= row2<sub>i</sub></code> and <code>col1<sub>i</sub> &lt;= y &lt;= col2<sub>i</sub></code>.</li>
</ul>

<p>Return<em> the matrix</em> <code>mat</code><em> after performing every query.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/11/24/p2example11.png" style="width: 531px; height: 121px;" />
<pre>
<strong>Input:</strong> n = 3, queries = [[1,1,2,2],[0,0,1,1]]
<strong>Output:</strong> [[1,1,0],[1,2,1],[0,1,1]]
<strong>Explanation:</strong> The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/11/24/p2example22.png" style="width: 261px; height: 82px;" />
<pre>
<strong>Input:</strong> n = 2, queries = [[0,0,1,1]]
<strong>Output:</strong> [[1,1],[1,1]]
<strong>Explanation:</strong> The diagram above shows the initial matrix and the matrix after the first query.
- In the first query we add 1 to every element in the matrix.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= row1<sub>i</sub> &lt;= row2<sub>i</sub> &lt; n</code></li>
	<li><code>0 &lt;= col1<sub>i</sub> &lt;= col2<sub>i</sub> &lt; n</code></li>
</ul>


## Hints

1. Imagine each row as a separate array. Instead of updating the whole submatrix together, we can use prefix sum to update each row separately.

2. For each query, iterate over the rows i in the range [row1, row2] and add 1 to prefix sum S[i][col1], and subtract 1 from S[i][col2 + 1].

3. After doing this operation for all the queries, update each row separately with S[i][j] = S[i][j] + S[i][j - 1].

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

Create an n by n difference matrix. For each query, add 1 at the left column and subtract 1 just after the right column for every affected row, so each query takes time proportional to its height. The extra column at index n records boundary updates safely.

Then compute prefix sums across each row. The running sum at each cell gives the total number of queries that cover it, producing the final matrix.

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
    vector<vector<int>> rangeAddQueries(int n, vector<vector<int>>& queries) {
        vector<vector<int>> mat(n, vector<int>(n + 1, 0));
        for (const auto& query : queries) {
            int row1 = query[0];
            int col1 = query[1];
            int row2 = query[2];
            int col2 = query[3];
            for (int row = row1; row <= row2; ++row) {
                ++mat[row][col1];
                --mat[row][col2 + 1];
            }
        }
        for (int row = 0; row < n; ++row) {
            for (int col = 1; col < n; ++col) {
                mat[row][col] += mat[row][col - 1];
            }
            mat[row].resize(n);
        }
        return mat;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int[][] rangeAddQueries(int n, int[][] queries) {
        int[][] mat = new int[n][n + 1];
        for (int[] query : queries) {
            int row1 = query[0];
            int col1 = query[1];
            int row2 = query[2];
            int col2 = query[3];
            for (int row = row1; row <= row2; row++) {
                mat[row][col1]++;
                mat[row][col2 + 1]--;
            }
        }
        int[][] result = new int[n][n];
        for (int row = 0; row < n; row++) {
            int running = 0;
            for (int col = 0; col < n; col++) {
                running += mat[row][col];
                result[row][col] = running;
            }
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def rangeAddQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """
        mat = [[0] * (n + 1) for _ in range(n)]
        for row1, col1, row2, col2 in queries:
            for row in range(row1, row2 + 1):
                mat[row][col1] += 1
                mat[row][col2 + 1] -= 1
        result = [[0] * n for _ in range(n)]
        for row in range(n):
            running = 0
            for col in range(n):
                running += mat[row][col]
                result[row][col] = running
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        mat = [[0] * (n + 1) for _ in range(n)]
        for row1, col1, row2, col2 in queries:
            for row in range(row1, row2 + 1):
                mat[row][col1] += 1
                mat[row][col2 + 1] -= 1
        result = [[0] * n for _ in range(n)]
        for row in range(n):
            running = 0
            for col in range(n):
                running += mat[row][col]
                result[row][col] = running
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int** rangeAddQueries(int n, int** queries, int queriesSize, int* queriesColSize, int* returnSize, int** returnColumnSizes) {
    int** mat = (int**)calloc(n, sizeof(int*));
    for (int row = 0; row < n; row++) {
        mat[row] = (int*)calloc(n + 1, sizeof(int));
    }
    for (int i = 0; i < queriesSize; i++) {
        int row1 = queries[i][0];
        int col1 = queries[i][1];
        int row2 = queries[i][2];
        int col2 = queries[i][3];
        for (int row = row1; row <= row2; row++) {
            mat[row][col1]++;
            mat[row][col2 + 1]--;
        }
    }
    int** result = (int**)malloc(n * sizeof(int*));
    *returnColumnSizes = (int*)malloc(n * sizeof(int));
    for (int row = 0; row < n; row++) {
        result[row] = (int*)malloc(n * sizeof(int));
        (*returnColumnSizes)[row] = n;
        int running = 0;
        for (int col = 0; col < n; col++) {
            running += mat[row][col];
            result[row][col] = running;
        }
        free(mat[row]);
    }
    free(mat);
    *returnSize = n;
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[][] RangeAddQueries(int n, int[][] queries) {
        int[][] mat = new int[n][];
        for (int row = 0; row < n; row++) {
            mat[row] = new int[n + 1];
        }

        foreach (int[] query in queries) {
            int row1 = query[0];
            int col1 = query[1];
            int row2 = query[2];
            int col2 = query[3];

            for (int row = row1; row <= row2; row++) {
                mat[row][col1]++;
                mat[row][col2 + 1]--;
            }
        }

        int[][] result = new int[n][];
        for (int row = 0; row < n; row++) {
            result[row] = new int[n];
            int running = 0;
            for (int col = 0; col < n; col++) {
                running += mat[row][col];
                result[row][col] = running;
            }
        }

        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[][]}
 */
var rangeAddQueries = function(n, queries) {
    const mat = Array.from({ length: n }, () => Array(n + 1).fill(0));

    for (const [row1, col1, row2, col2] of queries) {
        for (let row = row1; row <= row2; row++) {
            mat[row][col1]++;
            mat[row][col2 + 1]--;
        }
    }

    const result = Array.from({ length: n }, () => Array(n).fill(0));
    for (let row = 0; row < n; row++) {
        let running = 0;
        for (let col = 0; col < n; col++) {
            running += mat[row][col];
            result[row][col] = running;
        }
    }

    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function rangeAddQueries(n: number, queries: number[][]): number[][] {
    const mat: number[][] = Array.from({ length: n }, () => Array(n + 1).fill(0));

    for (const [row1, col1, row2, col2] of queries) {
        for (let row = row1; row <= row2; row++) {
            mat[row][col1]++;
            mat[row][col2 + 1]--;
        }
    }

    const result: number[][] = Array.from({ length: n }, () => Array(n).fill(0));
    for (let row = 0; row < n; row++) {
        let running = 0;
        for (let col = 0; col < n; col++) {
            running += mat[row][col];
            result[row][col] = running;
        }
    }

    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $queries
     * @return Integer[][]
     */
    function rangeAddQueries($n, $queries) {
        $mat = array_fill(0, $n, array_fill(0, $n + 1, 0));

        foreach ($queries as $query) {
            [$row1, $col1, $row2, $col2] = $query;
            for ($row = $row1; $row <= $row2; $row++) {
                $mat[$row][$col1]++;
                $mat[$row][$col2 + 1]--;
            }
        }

        $result = array_fill(0, $n, array_fill(0, $n, 0));
        for ($row = 0; $row < $n; $row++) {
            $running = 0;
            for ($col = 0; $col < $n; $col++) {
                $running += $mat[$row][$col];
                $result[$row][$col] = $running;
            }
        }

        return $result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func rangeAddQueries(_ n: Int, _ queries: [[Int]]) -> [[Int]] {
        var mat = Array(repeating: Array(repeating: 0, count: n + 1), count: n)

        for query in queries {
            let row1 = query[0]
            let col1 = query[1]
            let row2 = query[2]
            let col2 = query[3]

            for row in row1...row2 {
                mat[row][col1] += 1
                mat[row][col2 + 1] -= 1
            }
        }

        var result = Array(repeating: Array(repeating: 0, count: n), count: n)
        for row in 0..<n {
            var running = 0
            for col in 0..<n {
                running += mat[row][col]
                result[row][col] = running
            }
        }

        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun rangeAddQueries(n: Int, queries: Array<IntArray>): Array<IntArray> {
        val diff = Array(n) { IntArray(n + 1) }
        for (query in queries) {
            val row1 = query[0]
            val col1 = query[1]
            val row2 = query[2]
            val col2 = query[3]
            for (row in row1..row2) {
                diff[row][col1] += 1
                diff[row][col2 + 1] -= 1
            }
        }
        val result = Array(n) { IntArray(n) }
        for (row in 0 until n) {
            var running = 0
            for (col in 0 until n) {
                running += diff[row][col]
                result[row][col] = running
            }
        }
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<List<int>> rangeAddQueries(int n, List<List<int>> queries) {
    final diff = List.generate(n, (_) => List<int>.filled(n + 1, 0));
    for (final query in queries) {
      final row1 = query[0];
      final col1 = query[1];
      final row2 = query[2];
      final col2 = query[3];
      for (var row = row1; row <= row2; row++) {
        diff[row][col1] += 1;
        diff[row][col2 + 1] -= 1;
      }
    }
    final result = List.generate(n, (_) => List<int>.filled(n, 0));
    for (var row = 0; row < n; row++) {
      var running = 0;
      for (var col = 0; col < n; col++) {
        running += diff[row][col];
        result[row][col] = running;
      }
    }
    return result;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func rangeAddQueries(n int, queries [][]int) [][]int {
	diff := make([][]int, n)
	for row := range diff {
		diff[row] = make([]int, n+1)
	}
	for _, query := range queries {
		row1, col1, row2, col2 := query[0], query[1], query[2], query[3]
		for row := row1; row <= row2; row++ {
			diff[row][col1]++
			diff[row][col2+1]--
		}
	}
	result := make([][]int, n)
	for row := 0; row < n; row++ {
		result[row] = make([]int, n)
		running := 0
		for col := 0; col < n; col++ {
			running += diff[row][col]
			result[row][col] = running
		}
	}
	return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[][]}
def range_add_queries(n, queries)
    diff = Array.new(n) { Array.new(n + 1, 0) }
    queries.each do |query|
        row1, col1, row2, col2 = query
        (row1..row2).each do |row|
            diff[row][col1] += 1
            diff[row][col2 + 1] -= 1
        end
    end
    result = Array.new(n) { Array.new(n, 0) }
    n.times do |row|
        running = 0
        n.times do |col|
            running += diff[row][col]
            result[row][col] = running
        end
    end
    result
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def rangeAddQueries(n: Int, queries: Array[Array[Int]]): Array[Array[Int]] = {
        val diff = Array.fill(n, n + 1)(0)
        for (query <- queries) {
            val row1 = query(0)
            val col1 = query(1)
            val row2 = query(2)
            val col2 = query(3)
            for (row <- row1 to row2) {
                diff(row)(col1) += 1
                diff(row)(col2 + 1) -= 1
            }
        }
        val result = Array.fill(n, n)(0)
        for (row <- 0 until n) {
            var running = 0
            for (col <- 0 until n) {
                running += diff(row)(col)
                result(row)(col) = running
            }
        }
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn range_add_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut diff = vec![vec![0; n + 1]; n];

        for query in queries {
            let row1 = query[0] as usize;
            let col1 = query[1] as usize;
            let row2 = query[2] as usize;
            let col2 = query[3] as usize;

            for row in row1..=row2 {
                diff[row][col1] += 1;
                diff[row][col2 + 1] -= 1;
            }
        }

        let mut result = vec![vec![0; n]; n];
        for row in 0..n {
            let mut running = 0;
            for col in 0..n {
                running += diff[row][col];
                result[row][col] = running;
            }
        }

        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (range-add-queries n queries)
  (-> exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let ([diff (build-vector n (lambda (_) (make-vector (add1 n) 0)))])
    (for ([query queries])
      (define row1 (list-ref query 0))
      (define col1 (list-ref query 1))
      (define row2 (list-ref query 2))
      (define col2 (list-ref query 3))
      (for ([row (in-range row1 (add1 row2))])
        (vector-set! (vector-ref diff row) col1
                     (add1 (vector-ref (vector-ref diff row) col1)))
        (vector-set! (vector-ref diff row) (add1 col2)
                     (sub1 (vector-ref (vector-ref diff row) (add1 col2)))))
    (for/list ([row (in-range n)])
      (define running 0)
      (for/list ([col (in-range n)])
        (set! running (+ running (vector-ref (vector-ref diff row) col)))
        running))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec range_add_queries(N :: integer(), Queries :: [[integer()]]) -> [[integer()]].
range_add_queries(N, Queries) ->
  Diff0 = [lists:duplicate(N + 1, 0) || _ <- lists:seq(1, N)],
  Diff = lists:foldl(
    fun([Row1, Col1, Row2, Col2], Acc) ->
      lists:foldl(
        fun(Row, Rows) ->
          Current = lists:nth(Row + 1, Rows),
          Updated = update_at(Col2 + 2,
            update_at(Col1 + 1, lists:nth(Col1 + 1, Current) + 1, Current),
            lists:sublist(Current, Col2 + 1) ++ [lists:nth(Col2 + 2, Current) - 1 | lists:nthtail(Col2 + 2, Current)]),
          replace_at(Row + 1, Updated, Rows)
        end,
        Acc,
        lists:seq(Row1, Row2))
    end,
    Diff0,
    Queries),
  [row_prefix(lists:sublist(Row, N), 0, []) || Row <- Diff].

update_at(1, Value, [_ | Tail]) -> [Value | Tail];
update_at(Index, Value, [Head | Tail]) -> [Head | update_at(Index - 1, Value, Tail)].

replace_at(1, Value, [_ | Tail]) -> [Value | Tail];
replace_at(Index, Value, [Head | Tail]) -> [Head | replace_at(Index - 1, Value, Tail)].

row_prefix([], _Running, Acc) -> lists:reverse(Acc);
row_prefix([Value | Rest], Running, Acc) ->
  Next = Running + Value,
  row_prefix(Rest, Next, [Next | Acc]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec range_add_queries(n :: integer, queries :: [[integer]]) :: [[integer]]
  def range_add_queries(n, queries) do
    diff = for _ <- 1..n, do: List.duplicate(0, n + 1)

    diff =
      Enum.reduce(queries, diff, fn [row1, col1, row2, col2], rows ->
        Enum.reduce(row1..row2, rows, fn row, acc ->
          current = Enum.at(acc, row)
          current = List.update_at(current, col1, &(&1 + 1))
          current = List.update_at(current, col2 + 1, &(&1 - 1))
          List.replace_at(acc, row, current)
        end)
      end)

    Enum.map(diff, fn row ->
      row
      |> Enum.take(n)
      |> Enum.scan(0, &(&1 + &2))
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n^2 + qn), where q is the number of queries. Each query updates at most n rows, and the final row-wise prefix sums visit all n^2 cells.
- **Space Complexity:** O(n^2) for the difference matrix, which is also used to store the result.
