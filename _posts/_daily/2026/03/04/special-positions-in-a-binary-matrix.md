---
layout: post
title: "Special Positions in a Binary Matrix"
date: 2026-03-04 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Matrix"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/special-positions-in-a-binary-matrix/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int numSpecial(vector<vector<int>>& mat)\
        \ {\n        int m = mat.size();\n        int n = mat[0].size();\n        vector<int>\
        \ rowCount(m, 0);\n        vector<int> colCount(n, 0);\n        for (int i =\
        \ 0; i < m; ++i) {\n            for (int j = 0; j < n; ++j) {\n            \
        \    if (mat[i][j] == 1) {\n                    rowCount[i]++;\n           \
        \         colCount[j]++;\n                }\n            }\n        }\n    \
        \    int ans = 0;\n        for (int i = 0; i < m; ++i) {\n            for (int\
        \ j = 0; j < n; ++j) {\n                if (mat[i][j] == 1 && rowCount[i] ==\
        \ 1 && colCount[j] == 1) {\n                    ans++;\n                }\n\
        \            }\n        }\n        return ans;\n    }\n};"
      java: "class Solution {\n    public int numSpecial(int[][] mat) {\n        int\
        \ m = mat.length;\n        int n = mat[0].length;\n        int[] rowCount =\
        \ new int[m];\n        int[] colCount = new int[n];\n        for (int i = 0;\
        \ i < m; i++) {\n            for (int j = 0; j < n; j++) {\n               \
        \ if (mat[i][j] == 1) {\n                    rowCount[i]++;\n              \
        \      colCount[j]++;\n                }\n            }\n        }\n       \
        \ int ans = 0;\n        for (int i = 0; i < m; i++) {\n            for (int\
        \ j = 0; j < n; j++) {\n                if (mat[i][j] == 1 && rowCount[i] ==\
        \ 1 && colCount[j] == 1) {\n                    ans++;\n                }\n\
        \            }\n        }\n        return ans;\n    }\n}"
      python: "class Solution(object):\n    def numSpecial(self, mat):\n        \"\"\
        \"\n        :type mat: List[List[int]]\n        :rtype: int\n        \"\"\"\n\
        \        m = len(mat)\n        n = len(mat[0])\n        rowCount = [0] * m\n\
        \        colCount = [0] * n\n        for i in range(m):\n            for j in\
        \ range(n):\n                if mat[i][j] == 1:\n                    rowCount[i]\
        \ += 1\n                    colCount[j] += 1\n        ans = 0\n        for i\
        \ in range(m):\n            for j in range(n):\n                if mat[i][j]\
        \ == 1 and rowCount[i] == 1 and colCount[j] == 1:\n                    ans +=\
        \ 1\n        return ans"
      python3: "class Solution:\n    def numSpecial(self, mat: List[List[int]]) -> int:\n\
        \        m = len(mat)\n        n = len(mat[0])\n        rowCount = [0] * m\n\
        \        colCount = [0] * n\n        for i in range(m):\n            for j in\
        \ range(n):\n                if mat[i][j] == 1:\n                    rowCount[i]\
        \ += 1\n                    colCount[j] += 1\n        ans = 0\n        for i\
        \ in range(m):\n            for j in range(n):\n                if mat[i][j]\
        \ == 1 and rowCount[i] == 1 and colCount[j] == 1:\n                    ans +=\
        \ 1\n        return ans"
      c: "int numSpecial(int** mat, int matSize, int* matColSize) {\n    int m = matSize;\n\
        \    int n = matColSize[0];\n    int* rowCount = (int*)calloc(m, sizeof(int));\n\
        \    int* colCount = (int*)calloc(n, sizeof(int));\n    for (int i = 0; i <\
        \ m; i++) {\n        for (int j = 0; j < n; j++) {\n            if (mat[i][j]\
        \ == 1) {\n                rowCount[i]++;\n                colCount[j]++;\n\
        \            }\n        }\n    }\n    int ans = 0;\n    for (int i = 0; i <\
        \ m; i++) {\n        for (int j = 0; j < n; j++) {\n            if (mat[i][j]\
        \ == 1 && rowCount[i] == 1 && colCount[j] == 1) {\n                ans++;\n\
        \            }\n        }\n    }\n    free(rowCount);\n    free(colCount);\n\
        \    return ans;\n}"
      csharp: "public class Solution {\n    public int NumSpecial(int[][] mat) {\n \
        \       int m = mat.Length;\n        int n = mat[0].Length;\n        int[] rowCount\
        \ = new int[m];\n        int[] colCount = new int[n];\n        for (int i =\
        \ 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n            \
        \    if (mat[i][j] == 1) {\n                    rowCount[i]++;\n           \
        \         colCount[j]++;\n                }\n            }\n        }\n    \
        \    int ans = 0;\n        for (int i = 0; i < m; i++) {\n            for (int\
        \ j = 0; j < n; j++) {\n                if (mat[i][j] == 1 && rowCount[i] ==\
        \ 1 && colCount[j] == 1) {\n                    ans++;\n                }\n\
        \            }\n        }\n        return ans;\n    }\n}"
      javascript: "/**\n * @param {number[][]} mat\n * @return {number}\n */\nvar numSpecial\
        \ = function(mat) {\n    const m = mat.length;\n    const n = mat[0].length;\n\
        \    const rowCount = new Array(m).fill(0);\n    const colCount = new Array(n).fill(0);\n\
        \    for (let i = 0; i < m; i++) {\n        for (let j = 0; j < n; j++) {\n\
        \            if (mat[i][j] === 1) {\n                rowCount[i]++;\n      \
        \          colCount[j]++;\n            }\n        }\n    }\n    let ans = 0;\n\
        \    for (let i = 0; i < m; i++) {\n        for (let j = 0; j < n; j++) {\n\
        \            if (mat[i][j] === 1 && rowCount[i] === 1 && colCount[j] === 1)\
        \ {\n                ans++;\n            }\n        }\n    }\n    return ans;\n\
        };"
      typescript: "function numSpecial(mat: number[][]): number {\n    const m = mat.length;\n\
        \    const n = mat[0].length;\n    const rowCount = new Array(m).fill(0);\n\
        \    const colCount = new Array(n).fill(0);\n    for (let i = 0; i < m; i++)\
        \ {\n        for (let j = 0; j < n; j++) {\n            if (mat[i][j] === 1)\
        \ {\n                rowCount[i]++;\n                colCount[j]++;\n      \
        \      }\n        }\n    }\n    let res = 0;\n    for (let i = 0; i < m; i++)\
        \ {\n        for (let j = 0; j < n; j++) {\n            if (mat[i][j] === 1\
        \ && rowCount[i] === 1 && colCount[j] === 1) {\n                res++;\n   \
        \         }\n        }\n    }\n    return res;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $mat\n     * @return\
        \ Integer\n     */\n    function numSpecial($mat) {\n        $m = count($mat);\n\
        \        $n = count($mat[0]);\n        $rowCount = array_fill(0, $m, 0);\n \
        \       $colCount = array_fill(0, $n, 0);\n        for ($i = 0; $i < $m; $i++)\
        \ {\n            for ($j = 0; $j < $n; $j++) {\n                if ($mat[$i][$j]\
        \ == 1) {\n                    $rowCount[$i]++;\n                    $colCount[$j]++;\n\
        \                }\n            }\n        }\n        $res = 0;\n        for\
        \ ($i = 0; $i < $m; $i++) {\n            for ($j = 0; $j < $n; $j++) {\n   \
        \             if ($mat[$i][$j] == 1 && $rowCount[$i] == 1 && $colCount[$j] ==\
        \ 1) {\n                    $res++;\n                }\n            }\n    \
        \    }\n        return $res;\n    }\n}"
      swift: "class Solution {\n    func numSpecial(_ mat: [[Int]]) -> Int {\n     \
        \   let m = mat.count\n        let n = mat[0].count\n        var rowCount =\
        \ Array(repeating: 0, count: m)\n        var colCount = Array(repeating: 0,\
        \ count: n)\n        for i in 0..<m {\n            for j in 0..<n {\n      \
        \          if mat[i][j] == 1 {\n                    rowCount[i] += 1\n     \
        \               colCount[j] += 1\n                }\n            }\n       \
        \ }\n        var res = 0\n        for i in 0..<m {\n            for j in 0..<n\
        \ {\n                if mat[i][j] == 1 && rowCount[i] == 1 && colCount[j] ==\
        \ 1 {\n                    res += 1\n                }\n            }\n    \
        \    }\n        return res\n    }\n}"
      kotlin: "class Solution {\n    fun numSpecial(mat: Array<IntArray>): Int {\n \
        \       val m = mat.size\n        val n = mat[0].size\n        val rowCount\
        \ = IntArray(m)\n        val colCount = IntArray(n)\n        for (i in 0 until\
        \ m) {\n            for (j in 0 until n) {\n                if (mat[i][j] ==\
        \ 1) {\n                    rowCount[i]++\n                    colCount[j]++\n\
        \                }\n            }\n        }\n        var res = 0\n        for\
        \ (i in 0 until m) {\n            for (j in 0 until n) {\n                if\
        \ (mat[i][j] == 1 && rowCount[i] == 1 && colCount[j] == 1) {\n             \
        \       res++\n                }\n            }\n        }\n        return res\n\
        \    }\n}"
      dart: "class Solution {\n  int numSpecial(List<List<int>> mat) {\n    int m =\
        \ mat.length;\n    int n = mat[0].length;\n    List<int> rowCount = List.filled(m,\
        \ 0);\n    List<int> colCount = List.filled(n, 0);\n    for (int i = 0; i <\
        \ m; i++) {\n      for (int j = 0; j < n; j++) {\n        if (mat[i][j] == 1)\
        \ {\n          rowCount[i]++;\n          colCount[j]++;\n        }\n      }\n\
        \    }\n    int res = 0;\n    for (int i = 0; i < m; i++) {\n      for (int\
        \ j = 0; j < n; j++) {\n        if (mat[i][j] == 1 && rowCount[i] == 1 && colCount[j]\
        \ == 1) {\n          res++;\n        }\n      }\n    }\n    return res;\n  }\n\
        }"
      go: "func numSpecial(mat [][]int) int {\n    m := len(mat)\n    n := len(mat[0])\n\
        \    rowCount := make([]int, m)\n    colCount := make([]int, n)\n    for i :=\
        \ 0; i < m; i++ {\n        for j := 0; j < n; j++ {\n            if mat[i][j]\
        \ == 1 {\n                rowCount[i]++\n                colCount[j]++\n   \
        \         }\n        }\n    }\n    res := 0\n    for i := 0; i < m; i++ {\n\
        \        for j := 0; j < n; j++ {\n            if mat[i][j] == 1 && rowCount[i]\
        \ == 1 && colCount[j] == 1 {\n                res++\n            }\n       \
        \ }\n    }\n    return res\n}"
      ruby: "def num_special(mat)\n  m = mat.length\n  n = mat[0].length\n  row_sums\
        \ = Array.new(m, 0)\n  col_sums = Array.new(n, 0)\n  m.times do |i|\n    n.times\
        \ do |j|\n      if mat[i][j] == 1\n        row_sums[i] += 1\n        col_sums[j]\
        \ += 1\n      end\n    end\n  end\n  count = 0\n  m.times do |i|\n    n.times\
        \ do |j|\n      if mat[i][j] == 1 && row_sums[i] == 1 && col_sums[j] == 1\n\
        \        count += 1\n      end\n    end\n  end\n  count\nend"
      scala: "object Solution {\n    def numSpecial(mat: Array[Array[Int]]): Int = {\n\
        \        val m = mat.length\n        val n = mat(0).length\n        val rowSums\
        \ = new Array[Int](m)\n        val colSums = new Array[Int](n)\n        for\
        \ (i <- 0 until m; j <- 0 until n) {\n            if (mat(i)(j) == 1) {\n  \
        \              rowSums(i) += 1\n                colSums(j) += 1\n          \
        \  }\n        }\n        var count = 0\n        for (i <- 0 until m; j <- 0\
        \ until n) {\n            if (mat(i)(j) == 1 && rowSums(i) == 1 && colSums(j)\
        \ == 1) {\n                count += 1\n            }\n        }\n        count\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn num_special(mat: Vec<Vec<i32>>) -> i32 {\n\
        \        let m = mat.len();\n        let n = mat[0].len();\n        let mut\
        \ row_sums = vec![0; m];\n        let mut col_sums = vec![0; n];\n        for\
        \ i in 0..m {\n            for j in 0..n {\n                if mat[i][j] ==\
        \ 1 {\n                    row_sums[i] += 1;\n                    col_sums[j]\
        \ += 1;\n                }\n            }\n        }\n        let mut count\
        \ = 0;\n        for i in 0..m {\n            for j in 0..n {\n             \
        \   if mat[i][j] == 1 && row_sums[i] == 1 && col_sums[j] == 1 {\n          \
        \          count += 1;\n                }\n            }\n        }\n      \
        \  count\n    }\n}"
      racket: "(define/contract (num-special mat)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer?)\n  (let* ([m (length mat)]\n         [n (length (car mat))]\n\
        \         [row-sums (make-vector m 0)]\n         [col-sums (make-vector n 0)])\n\
        \    (for ([row (in-list mat)] [i (in-naturals)])\n      (for ([val (in-list\
        \ row)] [j (in-naturals)])\n        (when (= val 1)\n          (vector-set!\
        \ row-sums i (+ (vector-ref row-sums i) 1))\n          (vector-set! col-sums\
        \ j (+ (vector-ref col-sums j) 1)))))\n    (for/sum ([row (in-list mat)] [i\
        \ (in-naturals)])\n      (for/sum ([val (in-list row)] [j (in-naturals)])\n\
        \        (if (and (= val 1)\n                 (= (vector-ref row-sums i) 1)\n\
        \                 (= (vector-ref col-sums j) 1))\n            1\n          \
        \  0)))))"
      erlang: "-spec num_special(Mat :: [[integer()]]) -> integer().\nnum_special(Mat)\
        \ ->\n    RowSums = [lists:sum(Row) || Row <- Mat],\n    ColSums = [lists:sum(Col)\
        \ || Col <- transpose(Mat)],\n    check_rows(Mat, RowSums, ColSums, 0).\n\n\
        transpose([[]|_]) -> [];\ntranspose(M) ->\n    [lists:map(fun(R) -> hd(R) end,\
        \ M) | transpose(lists:map(fun(R) -> tl(R) end, M))].\n\ncheck_rows([], [],\
        \ _, Total) -> Total;\ncheck_rows([Row|RRest], [RS|RSRest], ColSums, Total)\
        \ ->\n    check_rows(RRest, RSRest, ColSums, Total + check_cols(Row, RS, ColSums,\
        \ 0)).\n\ncheck_cols([], _, [], RowTotal) -> RowTotal;\ncheck_cols([1|CRest],\
        \ 1, [1|CSRest], RowTotal) ->\n    check_cols(CRest, 1, CSRest, RowTotal + 1);\n\
        check_cols([_|CRest], RS, [_|CSRest], RowTotal) ->\n    check_cols(CRest, RS,\
        \ CSRest, RowTotal)."
      elixir: "defmodule Solution do\n  @spec num_special(mat :: [[integer]]) :: integer\n\
        \  def num_special(mat) do\n    row_sums = Enum.map(mat, &Enum.sum/1)\n    col_sums\
        \ = mat\n               |> Enum.zip()\n               |> Enum.map(fn t -> Tuple.to_list(t)\
        \ |> Enum.sum() end)\n\n    row_sums_tuple = List.to_tuple(row_sums)\n    col_sums_tuple\
        \ = List.to_tuple(col_sums)\n\n    mat\n    |> Enum.with_index()\n    |> Enum.reduce(0,\
        \ fn {row, i}, acc ->\n      row_sum = elem(row_sums_tuple, i)\n      row\n\
        \      |> Enum.with_index()\n      |> Enum.reduce(acc, fn {val, j}, inner_acc\
        \ ->\n        col_sum = elem(col_sums_tuple, j)\n        if val == 1 and row_sum\
        \ == 1 and col_sum == 1 do\n          inner_acc + 1\n        else\n        \
        \  inner_acc\n        end\n      end)\n    end)\n  end\nend"
    approach: 'The algorithm identifies special positions by pre-calculating the number
      of ''1''s in each row and each column. We iterate through the matrix once, maintaining
      two arrays: ''rowCount'' of size m and ''colCount'' of size n. For every cell
      (i, j) that contains a 1, we increment rowCount[i] and colCount[j]. This allows
      us to determine in constant time how many ones exist in any given row or column.


      In the second pass, we iterate through the matrix again. For each position (i,
      j), if the value is 1 and both rowCount[i] and colCount[j] are exactly 1, it means
      that the current 1 is the only 1 in its row and the only 1 in its column. We increment
      a counter for every such occurrence found and return the final count as the result.'
    time_complexity: 'O(m * n), where m is the number of rows and n is the number of
      columns. We traverse the entire matrix twice: once to count the occurrences in
      rows and columns, and once to check the special condition for each cell.'
    space_complexity: O(m + n) because we use two auxiliary arrays to store the sums
      of each row and each column.
    elapsed_time: 85.42603516578674
    model: gemini-3-flash-preview
    generated_at: '2026-03-04 01:22:07 '
---

## Problem #1582: Special Positions in a Binary Matrix

**Difficulty:** Easy

**Topics:** Array, Matrix

## Problem Description

<p>Given an <code>m x n</code> binary matrix <code>mat</code>, return <em>the number of special positions in </em><code>mat</code><em>.</em></p>

<p>A position <code>(i, j)</code> is called <strong>special</strong> if <code>mat[i][j] == 1</code> and all other elements in row <code>i</code> and column <code>j</code> are <code>0</code> (rows and columns are <strong>0-indexed</strong>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/23/special1.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>Input:</strong> mat = [[1,0,0],[0,0,1],[1,0,0]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/special-grid.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>Input:</strong> mat = [[1,0,0],[0,1,0],[0,0,1]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> (0, 0), (1, 1) and (2, 2) are special positions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>mat[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>


## Hints

1. Keep track of 1s in each row and in each column. Then while iterating over matrix, if the current position is 1 and current row as well as current column contains exactly one occurrence of 1.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm identifies special positions by pre-calculating the number of '1's in each row and each column. We iterate through the matrix once, maintaining two arrays: 'rowCount' of size m and 'colCount' of size n. For every cell (i, j) that contains a 1, we increment rowCount[i] and colCount[j]. This allows us to determine in constant time how many ones exist in any given row or column.

In the second pass, we iterate through the matrix again. For each position (i, j), if the value is 1 and both rowCount[i] and colCount[j] are exactly 1, it means that the current 1 is the only 1 in its row and the only 1 in its column. We increment a counter for every such occurrence found and return the final count as the result.

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
    int numSpecial(vector<vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        vector<int> rowCount(m, 0);
        vector<int> colCount(n, 0);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] == 1) {
                    rowCount[i]++;
                    colCount[j]++;
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] == 1 && rowCount[i] == 1 && colCount[j] == 1) {
                    ans++;
                }
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
class Solution {
    public int numSpecial(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int[] rowCount = new int[m];
        int[] colCount = new int[n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1) {
                    rowCount[i]++;
                    colCount[j]++;
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1 && rowCount[i] == 1 && colCount[j] == 1) {
                    ans++;
                }
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
class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])
        rowCount = [0] * m
        colCount = [0] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    rowCount[i] += 1
                    colCount[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rowCount[i] == 1 and colCount[j] == 1:
                    ans += 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rowCount = [0] * m
        colCount = [0] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    rowCount[i] += 1
                    colCount[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rowCount[i] == 1 and colCount[j] == 1:
                    ans += 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int numSpecial(int** mat, int matSize, int* matColSize) {
    int m = matSize;
    int n = matColSize[0];
    int* rowCount = (int*)calloc(m, sizeof(int));
    int* colCount = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (mat[i][j] == 1) {
                rowCount[i]++;
                colCount[j]++;
            }
        }
    }
    int ans = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (mat[i][j] == 1 && rowCount[i] == 1 && colCount[j] == 1) {
                ans++;
            }
        }
    }
    free(rowCount);
    free(colCount);
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int NumSpecial(int[][] mat) {
        int m = mat.Length;
        int n = mat[0].Length;
        int[] rowCount = new int[m];
        int[] colCount = new int[n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1) {
                    rowCount[i]++;
                    colCount[j]++;
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1 && rowCount[i] == 1 && colCount[j] == 1) {
                    ans++;
                }
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
 * @param {number[][]} mat
 * @return {number}
 */
var numSpecial = function(mat) {
    const m = mat.length;
    const n = mat[0].length;
    const rowCount = new Array(m).fill(0);
    const colCount = new Array(n).fill(0);
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (mat[i][j] === 1) {
                rowCount[i]++;
                colCount[j]++;
            }
        }
    }
    let ans = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (mat[i][j] === 1 && rowCount[i] === 1 && colCount[j] === 1) {
                ans++;
            }
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
function numSpecial(mat: number[][]): number {
    const m = mat.length;
    const n = mat[0].length;
    const rowCount = new Array(m).fill(0);
    const colCount = new Array(n).fill(0);
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (mat[i][j] === 1) {
                rowCount[i]++;
                colCount[j]++;
            }
        }
    }
    let res = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (mat[i][j] === 1 && rowCount[i] === 1 && colCount[j] === 1) {
                res++;
            }
        }
    }
    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function numSpecial($mat) {
        $m = count($mat);
        $n = count($mat[0]);
        $rowCount = array_fill(0, $m, 0);
        $colCount = array_fill(0, $n, 0);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($mat[$i][$j] == 1) {
                    $rowCount[$i]++;
                    $colCount[$j]++;
                }
            }
        }
        $res = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($mat[$i][$j] == 1 && $rowCount[$i] == 1 && $colCount[$j] == 1) {
                    $res++;
                }
            }
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
    func numSpecial(_ mat: [[Int]]) -> Int {
        let m = mat.count
        let n = mat[0].count
        var rowCount = Array(repeating: 0, count: m)
        var colCount = Array(repeating: 0, count: n)
        for i in 0..<m {
            for j in 0..<n {
                if mat[i][j] == 1 {
                    rowCount[i] += 1
                    colCount[j] += 1
                }
            }
        }
        var res = 0
        for i in 0..<m {
            for j in 0..<n {
                if mat[i][j] == 1 && rowCount[i] == 1 && colCount[j] == 1 {
                    res += 1
                }
            }
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
    fun numSpecial(mat: Array<IntArray>): Int {
        val m = mat.size
        val n = mat[0].size
        val rowCount = IntArray(m)
        val colCount = IntArray(n)
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (mat[i][j] == 1) {
                    rowCount[i]++
                    colCount[j]++
                }
            }
        }
        var res = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (mat[i][j] == 1 && rowCount[i] == 1 && colCount[j] == 1) {
                    res++
                }
            }
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
  int numSpecial(List<List<int>> mat) {
    int m = mat.length;
    int n = mat[0].length;
    List<int> rowCount = List.filled(m, 0);
    List<int> colCount = List.filled(n, 0);
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (mat[i][j] == 1) {
          rowCount[i]++;
          colCount[j]++;
        }
      }
    }
    int res = 0;
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (mat[i][j] == 1 && rowCount[i] == 1 && colCount[j] == 1) {
          res++;
        }
      }
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
func numSpecial(mat [][]int) int {
    m := len(mat)
    n := len(mat[0])
    rowCount := make([]int, m)
    colCount := make([]int, n)
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if mat[i][j] == 1 {
                rowCount[i]++
                colCount[j]++
            }
        }
    }
    res := 0
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if mat[i][j] == 1 && rowCount[i] == 1 && colCount[j] == 1 {
                res++
            }
        }
    }
    return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def num_special(mat)
  m = mat.length
  n = mat[0].length
  row_sums = Array.new(m, 0)
  col_sums = Array.new(n, 0)
  m.times do |i|
    n.times do |j|
      if mat[i][j] == 1
        row_sums[i] += 1
        col_sums[j] += 1
      end
    end
  end
  count = 0
  m.times do |i|
    n.times do |j|
      if mat[i][j] == 1 && row_sums[i] == 1 && col_sums[j] == 1
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
    def numSpecial(mat: Array[Array[Int]]): Int = {
        val m = mat.length
        val n = mat(0).length
        val rowSums = new Array[Int](m)
        val colSums = new Array[Int](n)
        for (i <- 0 until m; j <- 0 until n) {
            if (mat(i)(j) == 1) {
                rowSums(i) += 1
                colSums(j) += 1
            }
        }
        var count = 0
        for (i <- 0 until m; j <- 0 until n) {
            if (mat(i)(j) == 1 && rowSums(i) == 1 && colSums(j) == 1) {
                count += 1
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
    pub fn num_special(mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len();
        let n = mat[0].len();
        let mut row_sums = vec![0; m];
        let mut col_sums = vec![0; n];
        for i in 0..m {
            for j in 0..n {
                if mat[i][j] == 1 {
                    row_sums[i] += 1;
                    col_sums[j] += 1;
                }
            }
        }
        let mut count = 0;
        for i in 0..m {
            for j in 0..n {
                if mat[i][j] == 1 && row_sums[i] == 1 && col_sums[j] == 1 {
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
(define/contract (num-special mat)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([m (length mat)]
         [n (length (car mat))]
         [row-sums (make-vector m 0)]
         [col-sums (make-vector n 0)])
    (for ([row (in-list mat)] [i (in-naturals)])
      (for ([val (in-list row)] [j (in-naturals)])
        (when (= val 1)
          (vector-set! row-sums i (+ (vector-ref row-sums i) 1))
          (vector-set! col-sums j (+ (vector-ref col-sums j) 1)))))
    (for/sum ([row (in-list mat)] [i (in-naturals)])
      (for/sum ([val (in-list row)] [j (in-naturals)])
        (if (and (= val 1)
                 (= (vector-ref row-sums i) 1)
                 (= (vector-ref col-sums j) 1))
            1
            0)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec num_special(Mat :: [[integer()]]) -> integer().
num_special(Mat) ->
    RowSums = [lists:sum(Row) || Row <- Mat],
    ColSums = [lists:sum(Col) || Col <- transpose(Mat)],
    check_rows(Mat, RowSums, ColSums, 0).

transpose([[]|_]) -> [];
transpose(M) ->
    [lists:map(fun(R) -> hd(R) end, M) | transpose(lists:map(fun(R) -> tl(R) end, M))].

check_rows([], [], _, Total) -> Total;
check_rows([Row|RRest], [RS|RSRest], ColSums, Total) ->
    check_rows(RRest, RSRest, ColSums, Total + check_cols(Row, RS, ColSums, 0)).

check_cols([], _, [], RowTotal) -> RowTotal;
check_cols([1|CRest], 1, [1|CSRest], RowTotal) ->
    check_cols(CRest, 1, CSRest, RowTotal + 1);
check_cols([_|CRest], RS, [_|CSRest], RowTotal) ->
    check_cols(CRest, RS, CSRest, RowTotal).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec num_special(mat :: [[integer]]) :: integer
  def num_special(mat) do
    row_sums = Enum.map(mat, &Enum.sum/1)
    col_sums = mat
               |> Enum.zip()
               |> Enum.map(fn t -> Tuple.to_list(t) |> Enum.sum() end)

    row_sums_tuple = List.to_tuple(row_sums)
    col_sums_tuple = List.to_tuple(col_sums)

    mat
    |> Enum.with_index()
    |> Enum.reduce(0, fn {row, i}, acc ->
      row_sum = elem(row_sums_tuple, i)
      row
      |> Enum.with_index()
      |> Enum.reduce(acc, fn {val, j}, inner_acc ->
        col_sum = elem(col_sums_tuple, j)
        if val == 1 and row_sum == 1 and col_sum == 1 do
          inner_acc + 1
        else
          inner_acc
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

- **Time Complexity:** O(m * n), where m is the number of rows and n is the number of columns. We traverse the entire matrix twice: once to count the occurrences in rows and columns, and once to check the special condition for each cell.
- **Space Complexity:** O(m + n) because we use two auxiliary arrays to store the sums of each row and each column.
