---
layout: post
title: "Largest Submatrix With Rearrangements"
date: 2026-03-17 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Greedy", "Sorting", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/largest-submatrix-with-rearrangements/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int largestSubmatrix(vector<vector<int>>&\
        \ matrix) {\n        int m = matrix.size();\n        int n = matrix[0].size();\n\
        \        int maxArea = 0;\n        for (int i = 1; i < m; ++i) {\n         \
        \   for (int j = 0; j < n; ++j) {\n                if (matrix[i][j] == 1) {\n\
        \                    matrix[i][j] += matrix[i - 1][j];\n                }\n\
        \            }\n        }\n        for (int i = 0; i < m; ++i) {\n         \
        \   vector<int> row = matrix[i];\n            sort(row.begin(), row.end(), greater<int>());\n\
        \            for (int j = 0; j < n; ++j) {\n                maxArea = max(maxArea,\
        \ row[j] * (j + 1));\n            }\n        }\n        return maxArea;\n  \
        \  }\n};"
      java: "class Solution {\n    public int largestSubmatrix(int[][] matrix) {\n \
        \       int m = matrix.length;\n        int n = matrix[0].length;\n        for\
        \ (int i = 1; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n   \
        \             if (matrix[i][j] == 1) {\n                    matrix[i][j] +=\
        \ matrix[i - 1][j];\n                }\n            }\n        }\n        int\
        \ maxArea = 0;\n        for (int i = 0; i < m; i++) {\n            int[] row\
        \ = matrix[i].clone();\n            java.util.Arrays.sort(row);\n          \
        \  for (int j = 0; j < n; j++) {\n                maxArea = Math.max(maxArea,\
        \ row[j] * (n - j));\n            }\n        }\n        return maxArea;\n  \
        \  }\n}"
      python: "class Solution(object):\n    def largestSubmatrix(self, matrix):\n  \
        \      \"\"\"\n        :type matrix: List[List[int]]\n        :rtype: int\n\
        \        \"\"\"\n        m, n = len(matrix), len(matrix[0])\n        for i in\
        \ range(1, m):\n            for j in range(n):\n                if matrix[i][j]\
        \ == 1:\n                    matrix[i][j] += matrix[i-1][j]\n        res = 0\n\
        \        for i in range(m):\n            row = sorted(matrix[i], reverse=True)\n\
        \            for j in range(n):\n                res = max(res, row[j] * (j\
        \ + 1))\n        return res"
      python3: "class Solution:\n    def largestSubmatrix(self, matrix: List[List[int]])\
        \ -> int:\n        m, n = len(matrix), len(matrix[0])\n        for i in range(1,\
        \ m):\n            for j in range(n):\n                if matrix[i][j] == 1:\n\
        \                    matrix[i][j] += matrix[i - 1][j]\n        max_area = 0\n\
        \        for i in range(m):\n            sorted_row = sorted(matrix[i], reverse=True)\n\
        \            for j in range(n):\n                max_area = max(max_area, sorted_row[j]\
        \ * (j + 1))\n        return max_area"
      c: "int compare(const void* a, const void* b) {\n    return (*(int*)b - *(int*)a);\n\
        }\n\nint largestSubmatrix(int** matrix, int matrixSize, int* matrixColSize)\
        \ {\n    int m = matrixSize;\n    int n = matrixColSize[0];\n    for (int i\
        \ = 1; i < m; i++) {\n        for (int j = 0; j < n; j++) {\n            if\
        \ (matrix[i][j] == 1) {\n                matrix[i][j] += matrix[i - 1][j];\n\
        \            }\n        }\n    }\n    int maxArea = 0;\n    int* row = (int*)malloc(n\
        \ * sizeof(int));\n    for (int i = 0; i < m; i++) {\n        for (int j = 0;\
        \ j < n; j++) row[j] = matrix[i][j];\n        qsort(row, n, sizeof(int), compare);\n\
        \        for (int j = 0; j < n; j++) {\n            int area = row[j] * (j +\
        \ 1);\n            if (area > maxArea) maxArea = area;\n        }\n    }\n \
        \   free(row);\n    return maxArea;\n}"
      csharp: "public class Solution {\n    public int LargestSubmatrix(int[][] matrix)\
        \ {\n        int m = matrix.Length;\n        int n = matrix[0].Length;\n   \
        \     for (int i = 1; i < m; i++) {\n            for (int j = 0; j < n; j++)\
        \ {\n                if (matrix[i][j] == 1) {\n                    matrix[i][j]\
        \ += matrix[i - 1][j];\n                }\n            }\n        }\n      \
        \  int maxArea = 0;\n        for (int i = 0; i < m; i++) {\n            int[]\
        \ row = (int[])matrix[i].Clone();\n            Array.Sort(row);\n          \
        \  for (int j = 0; j < n; j++) {\n                maxArea = Math.Max(maxArea,\
        \ row[j] * (n - j));\n            }\n        }\n        return maxArea;\n  \
        \  }\n}"
      javascript: "/**\n * @param {number[][]} matrix\n * @return {number}\n */\nvar\
        \ largestSubmatrix = function(matrix) {\n    const m = matrix.length;\n    const\
        \ n = matrix[0].length;\n    for (let i = 1; i < m; i++) {\n        for (let\
        \ j = 0; j < n; j++) {\n            if (matrix[i][j] === 1) {\n            \
        \    matrix[i][j] += matrix[i - 1][j];\n            }\n        }\n    }\n  \
        \  let maxArea = 0;\n    for (let i = 0; i < m; i++) {\n        const row =\
        \ [...matrix[i]].sort((a, b) => b - a);\n        for (let j = 0; j < n; j++)\
        \ {\n            maxArea = Math.max(maxArea, row[j] * (j + 1));\n        }\n\
        \    }\n    return maxArea;\n};"
      typescript: "function largestSubmatrix(matrix: number[][]): number {\n    const\
        \ m = matrix.length;\n    const n = matrix[0].length;\n    for (let i = 1; i\
        \ < m; i++) {\n        for (let j = 0; j < n; j++) {\n            if (matrix[i][j]\
        \ === 1) {\n                matrix[i][j] += matrix[i - 1][j];\n            }\n\
        \        }\n    }\n    let maxArea = 0;\n    for (let i = 0; i < m; i++) {\n\
        \        const row = [...matrix[i]].sort((a, b) => b - a);\n        for (let\
        \ j = 0; j < n; j++) {\n            maxArea = Math.max(maxArea, row[j] * (j\
        \ + 1));\n        }\n    }\n    return maxArea;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $matrix\n     * @return\
        \ Integer\n     */\n    function largestSubmatrix($matrix) {\n        $m = count($matrix);\n\
        \        $n = count($matrix[0]);\n        for ($i = 1; $i < $m; $i++) {\n  \
        \          for ($j = 0; $j < $n; $j++) {\n                if ($matrix[$i][$j]\
        \ === 1) {\n                    $matrix[$i][$j] += $matrix[$i - 1][$j];\n  \
        \              }\n            }\n        }\n        $maxArea = 0;\n        for\
        \ ($i = 0; $i < $m; $i++) {\n            $row = $matrix[$i];\n            rsort($row);\n\
        \            for ($j = 0; $j < $n; $j++) {\n                $maxArea = max($maxArea,\
        \ $row[$j] * ($j + 1));\n            }\n        }\n        return $maxArea;\n\
        \    }\n}"
      swift: "class Solution {\n    func largestSubmatrix(_ matrix: [[Int]]) -> Int\
        \ {\n        var heights = matrix\n        let m = heights.count\n        let\
        \ n = heights[0].count\n        for i in 1..<m {\n            for j in 0..<n\
        \ {\n                if heights[i][j] == 1 {\n                    heights[i][j]\
        \ += heights[i - 1][j]\n                }\n            }\n        }\n      \
        \  var maxArea = 0\n        for i in 0..<m {\n            let sortedRow = heights[i].sorted(by:\
        \ >)\n            for j in 0..<n {\n                maxArea = max(maxArea, sortedRow[j]\
        \ * (j + 1))\n            }\n        }\n        return maxArea\n    }\n}"
      kotlin: "class Solution {\n    fun largestSubmatrix(matrix: Array<IntArray>):\
        \ Int {\n        val m = matrix.size\n        val n = matrix[0].size\n     \
        \   for (i in 1 until m) {\n            for (j in 0 until n) {\n           \
        \     if (matrix[i][j] == 1) {\n                    matrix[i][j] += matrix[i\
        \ - 1][j]\n                }\n            }\n        }\n        var maxArea\
        \ = 0\n        for (i in 0 until m) {\n            val sortedRow = matrix[i].sortedArrayDescending()\n\
        \            for (j in 0 until n) {\n                maxArea = Math.max(maxArea,\
        \ sortedRow[j] * (j + 1))\n            }\n        }\n        return maxArea\n\
        \    }\n}"
      dart: "class Solution {\n  int largestSubmatrix(List<List<int>> matrix) {\n  \
        \  int m = matrix.length;\n    int n = matrix[0].length;\n    for (int i = 1;\
        \ i < m; i++) {\n      for (int j = 0; j < n; j++) {\n        if (matrix[i][j]\
        \ == 1) {\n          matrix[i][j] += matrix[i - 1][j];\n        }\n      }\n\
        \    }\n    int maxArea = 0;\n    for (int i = 0; i < m; i++) {\n      List<int>\
        \ row = List<int>.from(matrix[i]);\n      row.sort((a, b) => b.compareTo(a));\n\
        \      for (int j = 0; j < n; j++) {\n        int area = row[j] * (j + 1);\n\
        \        if (area > maxArea) {\n          maxArea = area;\n        }\n     \
        \ }\n    }\n    return maxArea;\n  }\n}"
      go: "import \"sort\"\n\nfunc largestSubmatrix(matrix [][]int) int {\n\tm := len(matrix)\n\
        \tn := len(matrix[0])\n\tfor i := 1; i < m; i++ {\n\t\tfor j := 0; j < n; j++\
        \ {\n\t\t\tif matrix[i][j] == 1 {\n\t\t\t\tmatrix[i][j] += matrix[i-1][j]\n\t\
        \t\t}\n\t\t}\n\t}\n\tmaxArea := 0\n\tfor i := 0; i < m; i++ {\n\t\trow := make([]int,\
        \ n)\n\t\tcopy(row, matrix[i])\n\t\tsort.Ints(row)\n\t\tfor j := 0; j < n; j++\
        \ {\n\t\t\tarea := row[j] * (n - j)\n\t\t\tif area > maxArea {\n\t\t\t\tmaxArea\
        \ = area\n\t\t\t}\n\t\t}\n\t}\n\treturn maxArea\n}"
      ruby: "def largest_submatrix(matrix)\n  n = matrix[0].length\n  heights = Array.new(n,\
        \ 0)\n  max_area = 0\n  matrix.each do |row|\n    row.each_with_index do |val,\
        \ j|\n      heights[j] = (val == 1 ? heights[j] + 1 : 0)\n    end\n    sorted_heights\
        \ = heights.sort.reverse\n    sorted_heights.each_with_index do |h, k|\n   \
        \   area = h * (k + 1)\n      max_area = area if area > max_area\n    end\n\
        \  end\n  max_area\nend"
      scala: "object Solution {\n  def largestSubmatrix(matrix: Array[Array[Int]]):\
        \ Int = {\n    val m = matrix.length\n    val n = matrix(0).length\n    val\
        \ heights = Array.fill(n)(0)\n    var maxArea = 0\n    for (i <- 0 until m)\
        \ {\n      for (j <- 0 until n) {\n        if (matrix(i)(j) == 1) heights(j)\
        \ += 1\n        else heights(j) = 0\n      }\n      val sortedHeights = heights.sorted(Ordering.Int.reverse)\n\
        \      for (k <- 0 until n) {\n        maxArea = Math.max(maxArea, sortedHeights(k)\
        \ * (k + 1))\n      }\n    }\n    maxArea\n  }\n}"
      rust: "impl Solution {\n    pub fn largest_submatrix(matrix: Vec<Vec<i32>>) ->\
        \ i32 {\n        let m = matrix.len();\n        let n = matrix[0].len();\n \
        \       let mut heights = vec![0; n];\n        let mut max_area = 0;\n     \
        \   for row in matrix {\n            for j in 0..n {\n                if row[j]\
        \ == 1 {\n                    heights[j] += 1;\n                } else {\n \
        \                   heights[j] = 0;\n                }\n            }\n    \
        \        let mut sorted_heights = heights.clone();\n            sorted_heights.sort_unstable_by(|a,\
        \ b| b.cmp(a));\n            for (k, &h) in sorted_heights.iter().enumerate()\
        \ {\n                max_area = max_area.max(h * (k as i32 + 1));\n        \
        \    }\n        }\n        max_area\n    }\n}"
      racket: "(define/contract (largest-submatrix matrix)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer?)\n  (let* ([n (length (car matrix))]\n         [heights (make-vector\
        \ n 0)])\n    (foldl (lambda (row max-acc)\n             (for ([j (in-range\
        \ n)]\n                   [val row])\n               (vector-set! heights j\
        \ (if (= val 1) (+ (vector-ref heights j) 1) 0)))\n             (let* ([sorted-heights\
        \ (sort (vector->list heights) >)]\n                    [row-max (let loop ([hs\
        \ sorted-heights] [k 1] [curr-max 0])\n                               (if (null?\
        \ hs)\n                                   curr-max\n                       \
        \            (loop (cdr hs) (+ k 1) (max curr-max (* (car hs) k)))))])\n   \
        \            (max max-acc row-max)))\n           0\n           matrix)))"
      erlang: "-spec largest_submatrix(Matrix :: [[integer()]]) -> integer().\nlargest_submatrix(Matrix)\
        \ ->\n    N = length(hd(Matrix)),\n    Heights = lists:duplicate(N, 0),\n  \
        \  solve(Matrix, Heights, 0).\n\nsolve([], _, MaxArea) -> MaxArea;\nsolve([Row|Rest],\
        \ Heights, MaxArea) ->\n    NewHeights = lists:zipwith(fun(R, H) -> if R =:=\
        \ 1 -> H + 1; true -> 0 end end, Row, Heights),\n    SortedHeights = lists:sort(fun(A,\
        \ B) -> A > B end, NewHeights),\n    RowMax = calc_row_max(SortedHeights, 1,\
        \ 0),\n    solve(Rest, NewHeights, erlang:max(MaxArea, RowMax)).\n\ncalc_row_max([],\
        \ _, Max) -> Max;\ncalc_row_max([H|T], K, Max) ->\n    calc_row_max(T, K + 1,\
        \ erlang:max(Max, H * K))."
      elixir: "defmodule Solution do\n  @spec largest_submatrix(matrix :: [[integer]])\
        \ :: integer\n  def largest_submatrix(matrix) do\n    n = length(hd(matrix))\n\
        \    initial_heights = List.duplicate(0, n)\n\n    {_, max_area} = Enum.reduce(matrix,\
        \ {initial_heights, 0}, fn row, {heights, current_max} ->\n      new_heights\
        \ = Enum.zip_with(row, heights, fn r, h -> if r == 1, do: h + 1, else: 0 end)\n\
        \      row_max = new_heights\n        |> Enum.sort(:desc)\n        |> Enum.with_index(1)\n\
        \        |> Enum.reduce(0, fn {h, k}, acc -> max(acc, h * k) end)\n      {new_heights,\
        \ max(current_max, row_max)}\n    end)\n\n    max_area\n  end\nend"
    approach: 'The core strategy relies on treating each row as the base of a potential
      submatrix. First, we calculate the number of consecutive ones ending at each cell
      (i, j) by iterating through the matrix column-wise. If the current cell is ''1'',
      its height is the height of the cell above it plus one; if it is ''0'', the height
      resets to zero. This transforms each row into an array of heights representing
      vertical strips of ones terminating at that row.


      Since we are allowed to rearrange the columns in any order, we sort the heights
      calculated for each row in descending order. For a sorted row of heights h_1,
      h_2, ..., h_n, the largest submatrix ending at this row with width k will have
      a height equal to h_k. Thus, the area is calculated as h_k * k. By iterating through
      all rows and all possible widths k, we can determine the maximum submatrix area
      possible across the entire matrix.'
    time_complexity: O(m * n * log n), where m is the number of rows and n is the number
      of columns. Calculating the heights takes O(m * n), and sorting each of the m
      rows takes O(n log n).
    space_complexity: O(n) or O(m * n) depending on implementation. If we update the
      matrix in-place or use a single array to track heights, the auxiliary space is
      O(n) for the sorting step, excluding the input matrix storage.
    elapsed_time: 129.112731218338
    model: gemini-3-flash-preview
    generated_at: '2026-03-17 01:26:42 '
---

## Problem #1727: Largest Submatrix With Rearrangements

**Difficulty:** Medium

**Topics:** Array, Greedy, Sorting, Matrix

## Problem Description

<p>You are given a binary matrix <code>matrix</code> of size <code>m x n</code>, and you are allowed to rearrange the <strong>columns</strong> of the <code>matrix</code> in any order.</p>

<p>Return <em>the area of the largest submatrix within </em><code>matrix</code><em> where <strong>every</strong> element of the submatrix is </em><code>1</code><em> after reordering the columns optimally.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/29/screenshot-2020-12-30-at-40536-pm.png" style="width: 500px; height: 240px;" />
<pre>
<strong>Input:</strong> matrix = [[0,0,1],[1,1,1],[1,0,1]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/29/screenshot-2020-12-30-at-40852-pm.png" style="width: 500px; height: 62px;" />
<pre>
<strong>Input:</strong> matrix = [[1,0,1,0,1]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[1,1,0],[1,0,1]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>matrix[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>


## Hints

1. For each column, find the number of consecutive ones ending at each position.

2. For each row, sort the cumulative ones in non-increasing order and "fit" the largest submatrix.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core strategy relies on treating each row as the base of a potential submatrix. First, we calculate the number of consecutive ones ending at each cell (i, j) by iterating through the matrix column-wise. If the current cell is '1', its height is the height of the cell above it plus one; if it is '0', the height resets to zero. This transforms each row into an array of heights representing vertical strips of ones terminating at that row.

Since we are allowed to rearrange the columns in any order, we sort the heights calculated for each row in descending order. For a sorted row of heights h_1, h_2, ..., h_n, the largest submatrix ending at this row with width k will have a height equal to h_k. Thus, the area is calculated as h_k * k. By iterating through all rows and all possible widths k, we can determine the maximum submatrix area possible across the entire matrix.

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
    int largestSubmatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        int maxArea = 0;
        for (int i = 1; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == 1) {
                    matrix[i][j] += matrix[i - 1][j];
                }
            }
        }
        for (int i = 0; i < m; ++i) {
            vector<int> row = matrix[i];
            sort(row.begin(), row.end(), greater<int>());
            for (int j = 0; j < n; ++j) {
                maxArea = max(maxArea, row[j] * (j + 1));
            }
        }
        return maxArea;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int largestSubmatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        for (int i = 1; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 1) {
                    matrix[i][j] += matrix[i - 1][j];
                }
            }
        }
        int maxArea = 0;
        for (int i = 0; i < m; i++) {
            int[] row = matrix[i].clone();
            java.util.Arrays.sort(row);
            for (int j = 0; j < n; j++) {
                maxArea = Math.max(maxArea, row[j] * (n - j));
            }
        }
        return maxArea;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        res = 0
        for i in range(m):
            row = sorted(matrix[i], reverse=True)
            for j in range(n):
                res = max(res, row[j] * (j + 1))
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]
        max_area = 0
        for i in range(m):
            sorted_row = sorted(matrix[i], reverse=True)
            for j in range(n):
                max_area = max(max_area, sorted_row[j] * (j + 1))
        return max_area
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int compare(const void* a, const void* b) {
    return (*(int*)b - *(int*)a);
}

int largestSubmatrix(int** matrix, int matrixSize, int* matrixColSize) {
    int m = matrixSize;
    int n = matrixColSize[0];
    for (int i = 1; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] == 1) {
                matrix[i][j] += matrix[i - 1][j];
            }
        }
    }
    int maxArea = 0;
    int* row = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) row[j] = matrix[i][j];
        qsort(row, n, sizeof(int), compare);
        for (int j = 0; j < n; j++) {
            int area = row[j] * (j + 1);
            if (area > maxArea) maxArea = area;
        }
    }
    free(row);
    return maxArea;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int LargestSubmatrix(int[][] matrix) {
        int m = matrix.Length;
        int n = matrix[0].Length;
        for (int i = 1; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 1) {
                    matrix[i][j] += matrix[i - 1][j];
                }
            }
        }
        int maxArea = 0;
        for (int i = 0; i < m; i++) {
            int[] row = (int[])matrix[i].Clone();
            Array.Sort(row);
            for (int j = 0; j < n; j++) {
                maxArea = Math.Max(maxArea, row[j] * (n - j));
            }
        }
        return maxArea;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} matrix
 * @return {number}
 */
var largestSubmatrix = function(matrix) {
    const m = matrix.length;
    const n = matrix[0].length;
    for (let i = 1; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (matrix[i][j] === 1) {
                matrix[i][j] += matrix[i - 1][j];
            }
        }
    }
    let maxArea = 0;
    for (let i = 0; i < m; i++) {
        const row = [...matrix[i]].sort((a, b) => b - a);
        for (let j = 0; j < n; j++) {
            maxArea = Math.max(maxArea, row[j] * (j + 1));
        }
    }
    return maxArea;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function largestSubmatrix(matrix: number[][]): number {
    const m = matrix.length;
    const n = matrix[0].length;
    for (let i = 1; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (matrix[i][j] === 1) {
                matrix[i][j] += matrix[i - 1][j];
            }
        }
    }
    let maxArea = 0;
    for (let i = 0; i < m; i++) {
        const row = [...matrix[i]].sort((a, b) => b - a);
        for (let j = 0; j < n; j++) {
            maxArea = Math.max(maxArea, row[j] * (j + 1));
        }
    }
    return maxArea;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function largestSubmatrix($matrix) {
        $m = count($matrix);
        $n = count($matrix[0]);
        for ($i = 1; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($matrix[$i][$j] === 1) {
                    $matrix[$i][$j] += $matrix[$i - 1][$j];
                }
            }
        }
        $maxArea = 0;
        for ($i = 0; $i < $m; $i++) {
            $row = $matrix[$i];
            rsort($row);
            for ($j = 0; $j < $n; $j++) {
                $maxArea = max($maxArea, $row[$j] * ($j + 1));
            }
        }
        return $maxArea;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func largestSubmatrix(_ matrix: [[Int]]) -> Int {
        var heights = matrix
        let m = heights.count
        let n = heights[0].count
        for i in 1..<m {
            for j in 0..<n {
                if heights[i][j] == 1 {
                    heights[i][j] += heights[i - 1][j]
                }
            }
        }
        var maxArea = 0
        for i in 0..<m {
            let sortedRow = heights[i].sorted(by: >)
            for j in 0..<n {
                maxArea = max(maxArea, sortedRow[j] * (j + 1))
            }
        }
        return maxArea
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun largestSubmatrix(matrix: Array<IntArray>): Int {
        val m = matrix.size
        val n = matrix[0].size
        for (i in 1 until m) {
            for (j in 0 until n) {
                if (matrix[i][j] == 1) {
                    matrix[i][j] += matrix[i - 1][j]
                }
            }
        }
        var maxArea = 0
        for (i in 0 until m) {
            val sortedRow = matrix[i].sortedArrayDescending()
            for (j in 0 until n) {
                maxArea = Math.max(maxArea, sortedRow[j] * (j + 1))
            }
        }
        return maxArea
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int largestSubmatrix(List<List<int>> matrix) {
    int m = matrix.length;
    int n = matrix[0].length;
    for (int i = 1; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (matrix[i][j] == 1) {
          matrix[i][j] += matrix[i - 1][j];
        }
      }
    }
    int maxArea = 0;
    for (int i = 0; i < m; i++) {
      List<int> row = List<int>.from(matrix[i]);
      row.sort((a, b) => b.compareTo(a));
      for (int j = 0; j < n; j++) {
        int area = row[j] * (j + 1);
        if (area > maxArea) {
          maxArea = area;
        }
      }
    }
    return maxArea;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func largestSubmatrix(matrix [][]int) int {
	m := len(matrix)
	n := len(matrix[0])
	for i := 1; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == 1 {
				matrix[i][j] += matrix[i-1][j]
			}
		}
	}
	maxArea := 0
	for i := 0; i < m; i++ {
		row := make([]int, n)
		copy(row, matrix[i])
		sort.Ints(row)
		for j := 0; j < n; j++ {
			area := row[j] * (n - j)
			if area > maxArea {
				maxArea = area
			}
		}
	}
	return maxArea
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def largest_submatrix(matrix)
  n = matrix[0].length
  heights = Array.new(n, 0)
  max_area = 0
  matrix.each do |row|
    row.each_with_index do |val, j|
      heights[j] = (val == 1 ? heights[j] + 1 : 0)
    end
    sorted_heights = heights.sort.reverse
    sorted_heights.each_with_index do |h, k|
      area = h * (k + 1)
      max_area = area if area > max_area
    end
  end
  max_area
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def largestSubmatrix(matrix: Array[Array[Int]]): Int = {
    val m = matrix.length
    val n = matrix(0).length
    val heights = Array.fill(n)(0)
    var maxArea = 0
    for (i <- 0 until m) {
      for (j <- 0 until n) {
        if (matrix(i)(j) == 1) heights(j) += 1
        else heights(j) = 0
      }
      val sortedHeights = heights.sorted(Ordering.Int.reverse)
      for (k <- 0 until n) {
        maxArea = Math.max(maxArea, sortedHeights(k) * (k + 1))
      }
    }
    maxArea
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn largest_submatrix(matrix: Vec<Vec<i32>>) -> i32 {
        let m = matrix.len();
        let n = matrix[0].len();
        let mut heights = vec![0; n];
        let mut max_area = 0;
        for row in matrix {
            for j in 0..n {
                if row[j] == 1 {
                    heights[j] += 1;
                } else {
                    heights[j] = 0;
                }
            }
            let mut sorted_heights = heights.clone();
            sorted_heights.sort_unstable_by(|a, b| b.cmp(a));
            for (k, &h) in sorted_heights.iter().enumerate() {
                max_area = max_area.max(h * (k as i32 + 1));
            }
        }
        max_area
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (largest-submatrix matrix)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([n (length (car matrix))]
         [heights (make-vector n 0)])
    (foldl (lambda (row max-acc)
             (for ([j (in-range n)]
                   [val row])
               (vector-set! heights j (if (= val 1) (+ (vector-ref heights j) 1) 0)))
             (let* ([sorted-heights (sort (vector->list heights) >)]
                    [row-max (let loop ([hs sorted-heights] [k 1] [curr-max 0])
                               (if (null? hs)
                                   curr-max
                                   (loop (cdr hs) (+ k 1) (max curr-max (* (car hs) k)))))])
               (max max-acc row-max)))
           0
           matrix)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec largest_submatrix(Matrix :: [[integer()]]) -> integer().
largest_submatrix(Matrix) ->
    N = length(hd(Matrix)),
    Heights = lists:duplicate(N, 0),
    solve(Matrix, Heights, 0).

solve([], _, MaxArea) -> MaxArea;
solve([Row|Rest], Heights, MaxArea) ->
    NewHeights = lists:zipwith(fun(R, H) -> if R =:= 1 -> H + 1; true -> 0 end end, Row, Heights),
    SortedHeights = lists:sort(fun(A, B) -> A > B end, NewHeights),
    RowMax = calc_row_max(SortedHeights, 1, 0),
    solve(Rest, NewHeights, erlang:max(MaxArea, RowMax)).

calc_row_max([], _, Max) -> Max;
calc_row_max([H|T], K, Max) ->
    calc_row_max(T, K + 1, erlang:max(Max, H * K)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec largest_submatrix(matrix :: [[integer]]) :: integer
  def largest_submatrix(matrix) do
    n = length(hd(matrix))
    initial_heights = List.duplicate(0, n)

    {_, max_area} = Enum.reduce(matrix, {initial_heights, 0}, fn row, {heights, current_max} ->
      new_heights = Enum.zip_with(row, heights, fn r, h -> if r == 1, do: h + 1, else: 0 end)
      row_max = new_heights
        |> Enum.sort(:desc)
        |> Enum.with_index(1)
        |> Enum.reduce(0, fn {h, k}, acc -> max(acc, h * k) end)
      {new_heights, max(current_max, row_max)}
    end)

    max_area
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m * n * log n), where m is the number of rows and n is the number of columns. Calculating the heights takes O(m * n), and sorting each of the m rows takes O(n log n).
- **Space Complexity:** O(n) or O(m * n) depending on implementation. If we update the matrix in-place or use a single array to track heights, the auxiliary space is O(n) for the sorting step, excluding the input matrix storage.
