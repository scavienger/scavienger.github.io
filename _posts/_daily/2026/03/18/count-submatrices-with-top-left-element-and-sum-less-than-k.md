---
layout: post
title: "Count Submatrices with Top-Left Element and Sum Less Than k"
date: 2026-03-18 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Matrix", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int countSubmatrices(vector<vector<int>>&\
        \ grid, int k) {\n        int m = grid.size();\n        int n = grid[0].size();\n\
        \        int count = 0;\n        for (int i = 0; i < m; ++i) {\n           \
        \ for (int j = 0; j < n; ++j) {\n                if (i > 0) grid[i][j] += grid[i\
        \ - 1][j];\n                if (j > 0) grid[i][j] += grid[i][j - 1];\n     \
        \           if (i > 0 && j > 0) grid[i][j] -= grid[i - 1][j - 1];\n        \
        \        if (grid[i][j] <= k) {\n                    count++;\n            \
        \    } else {\n                    break;\n                }\n            }\n\
        \        }\n        return count;\n    }\n};"
      java: "class Solution {\n    public int countSubmatrices(int[][] grid, int k)\
        \ {\n        int m = grid.length;\n        int n = grid[0].length;\n       \
        \ int count = 0;\n        for (int i = 0; i < m; i++) {\n            for (int\
        \ j = 0; j < n; j++) {\n                if (i > 0) grid[i][j] += grid[i - 1][j];\n\
        \                if (j > 0) grid[i][j] += grid[i][j - 1];\n                if\
        \ (i > 0 && j > 0) grid[i][j] -= grid[i - 1][j - 1];\n                if (grid[i][j]\
        \ <= k) {\n                    count++;\n                } else {\n        \
        \            break;\n                }\n            }\n        }\n        return\
        \ count;\n    }\n}"
      python: "class Solution(object):\n    def countSubmatrices(self, grid, k):\n \
        \       \"\"\"\n        :type grid: List[List[int]]\n        :type k: int\n\
        \        :rtype: int\n        \"\"\"\n        m = len(grid)\n        n = len(grid[0])\n\
        \        count = 0\n        for i in range(m):\n            for j in range(n):\n\
        \                if i > 0:\n                    grid[i][j] += grid[i-1][j]\n\
        \                if j > 0:\n                    grid[i][j] += grid[i][j-1]\n\
        \                if i > 0 and j > 0:\n                    grid[i][j] -= grid[i-1][j-1]\n\
        \                if grid[i][j] <= k:\n                    count += 1\n     \
        \           else:\n                    break\n        return count"
      python3: "class Solution:\n    def countSubmatrices(self, grid: List[List[int]],\
        \ k: int) -> int:\n        m, n = len(grid), len(grid[0])\n        count = 0\n\
        \        for i in range(m):\n            for j in range(n):\n              \
        \  if i > 0:\n                    grid[i][j] += grid[i-1][j]\n             \
        \   if j > 0:\n                    grid[i][j] += grid[i][j-1]\n            \
        \    if i > 0 and j > 0:\n                    grid[i][j] -= grid[i-1][j-1]\n\
        \                if grid[i][j] <= k:\n                    count += 1\n     \
        \           else:\n                    break\n        return count"
      c: "int countSubmatrices(int** grid, int gridSize, int* gridColSize, int k) {\n\
        \    int m = gridSize;\n    int n = gridColSize[0];\n    int count = 0;\n  \
        \  for (int i = 0; i < m; i++) {\n        for (int j = 0; j < n; j++) {\n  \
        \          if (i > 0) grid[i][j] += grid[i - 1][j];\n            if (j > 0)\
        \ grid[i][j] += grid[i][j - 1];\n            if (i > 0 && j > 0) grid[i][j]\
        \ -= grid[i - 1][j - 1];\n            if (grid[i][j] <= k) {\n             \
        \   count++;\n            } else {\n                break;\n            }\n\
        \        }\n    }\n    return count;\n}"
      csharp: "public class Solution {\n    public int CountSubmatrices(int[][] grid,\
        \ int k) {\n        int m = grid.Length;\n        int n = grid[0].Length;\n\
        \        int count = 0;\n        for (int i = 0; i < m; i++) {\n           \
        \ for (int j = 0; j < n; j++) {\n                if (i > 0) grid[i][j] += grid[i\
        \ - 1][j];\n                if (j > 0) grid[i][j] += grid[i][j - 1];\n     \
        \           if (i > 0 && j > 0) grid[i][j] -= grid[i - 1][j - 1];\n        \
        \        if (grid[i][j] <= k) {\n                    count++;\n            \
        \    } else {\n                    break;\n                }\n            }\n\
        \        }\n        return count;\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @param {number} k\n * @return\
        \ {number}\n */\nvar countSubmatrices = function(grid, k) {\n    const m = grid.length;\n\
        \    const n = grid[0].length;\n    let count = 0;\n    for (let i = 0; i <\
        \ m; i++) {\n        for (let j = 0; j < n; j++) {\n            if (i > 0) grid[i][j]\
        \ += grid[i - 1][j];\n            if (j > 0) grid[i][j] += grid[i][j - 1];\n\
        \            if (i > 0 && j > 0) grid[i][j] -= grid[i - 1][j - 1];\n       \
        \     if (grid[i][j] <= k) {\n                count++;\n            } else {\n\
        \                break;\n            }\n        }\n    }\n    return count;\n\
        };"
      typescript: "function countSubmatrices(grid: number[][], k: number): number {\n\
        \    const m = grid.length;\n    const n = grid[0].length;\n    let count =\
        \ 0;\n    const prefixSums = new Array(n).fill(0);\n    for (let i = 0; i <\
        \ m; i++) {\n        let rowSum = 0;\n        for (let j = 0; j < n; j++) {\n\
        \            rowSum += grid[i][j];\n            prefixSums[j] += rowSum;\n \
        \           if (prefixSums[j] <= k) {\n                count++;\n          \
        \  } else {\n                break;\n            }\n        }\n    }\n    return\
        \ count;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @param\
        \ Integer $k\n     * @return Integer\n     */\n    function countSubmatrices($grid,\
        \ $k) {\n        $m = count($grid);\n        $n = count($grid[0]);\n       \
        \ $count = 0;\n        $prefixSums = array_fill(0, $n, 0);\n        for ($i\
        \ = 0; $i < $m; $i++) {\n            $rowSum = 0;\n            for ($j = 0;\
        \ $j < $n; $j++) {\n                $rowSum += $grid[$i][$j];\n            \
        \    $prefixSums[$j] += $rowSum;\n                if ($prefixSums[$j] <= $k)\
        \ {\n                    $count++;\n                } else {\n             \
        \       break;\n                }\n            }\n        }\n        return\
        \ $count;\n    }\n}"
      swift: "class Solution {\n    func countSubmatrices(_ grid: [[Int]], _ k: Int)\
        \ -> Int {\n        let m = grid.count\n        let n = grid[0].count\n    \
        \    var count = 0\n        var prefixSums = [Int](repeating: 0, count: n)\n\
        \        for i in 0..<m {\n            var rowSum = 0\n            for j in\
        \ 0..<n {\n                rowSum += grid[i][j]\n                prefixSums[j]\
        \ += rowSum\n                if prefixSums[j] <= k {\n                    count\
        \ += 1\n                } else {\n                    break\n              \
        \  }\n            }\n        }\n        return count\n    }\n}"
      kotlin: "class Solution {\n    fun countSubmatrices(grid: Array<IntArray>, k:\
        \ Int): Int {\n        val m = grid.size\n        val n = grid[0].size\n   \
        \     var count = 0\n        val prefixSums = IntArray(n)\n        for (i in\
        \ 0 until m) {\n            var rowSum = 0\n            for (j in 0 until n)\
        \ {\n                rowSum += grid[i][j]\n                prefixSums[j] +=\
        \ rowSum\n                if (prefixSums[j] <= k) {\n                    count++\n\
        \                } else {\n                    break\n                }\n  \
        \          }\n        }\n        return count\n    }\n}"
      dart: "class Solution {\n  int countSubmatrices(List<List<int>> grid, int k) {\n\
        \    int m = grid.length;\n    int n = grid[0].length;\n    int count = 0;\n\
        \    List<int> prefixSums = List<int>.filled(n, 0);\n    for (int i = 0; i <\
        \ m; i++) {\n      int rowSum = 0;\n      for (int j = 0; j < n; j++) {\n  \
        \      rowSum += grid[i][j];\n        prefixSums[j] += rowSum;\n        if (prefixSums[j]\
        \ <= k) {\n          count++;\n        } else {\n          break;\n        }\n\
        \      }\n    }\n    return count;\n  }\n}"
      go: "func countSubmatrices(grid [][]int, k int) int {\n    m := len(grid)\n  \
        \  n := len(grid[0])\n    count := 0\n    prefixSums := make([]int, n)\n   \
        \ for i := 0; i < m; i++ {\n        rowSum := 0\n        for j := 0; j < n;\
        \ j++ {\n            rowSum += grid[i][j]\n            prefixSums[j] += rowSum\n\
        \            if prefixSums[j] <= k {\n                count++\n            }\
        \ else {\n                break\n            }\n        }\n    }\n    return\
        \ count\n}"
      ruby: "# @param {Integer[][]} grid\n# @param {Integer} k\n# @return {Integer}\n\
        def count_submatrices(grid, k)\n  m = grid.length\n  n = grid[0].length\n  count\
        \ = 0\n  above_sums = Array.new(n, 0)\n  grid.each do |row|\n    row_sum = 0\n\
        \    row.each_with_index do |val, j|\n      row_sum += val\n      above_sums[j]\
        \ += row_sum\n      count += 1 if above_sums[j] <= k\n    end\n  end\n  count\n\
        end"
      scala: "object Solution {\n  def countSubmatrices(grid: Array[Array[Int]], k:\
        \ Int): Int = {\n    val m = grid.length\n    val n = grid(0).length\n    val\
        \ aboveSums = new Array[Int](n)\n    var totalCount = 0\n    for (i <- 0 until\
        \ m) {\n      var rowSum = 0\n      for (j <- 0 until n) {\n        rowSum +=\
        \ grid(i)(j)\n        aboveSums(j) += rowSum\n        if (aboveSums(j) <= k)\
        \ {\n          totalCount += 1\n        }\n      }\n    }\n    totalCount\n\
        \  }\n}"
      rust: "impl Solution {\n    pub fn count_submatrices(grid: Vec<Vec<i32>>, k: i32)\
        \ -> i32 {\n        let m = grid.len();\n        let n = grid[0].len();\n  \
        \      let mut count = 0;\n        let mut above_sums = vec![0; n];\n      \
        \  for i in 0..m {\n            let mut row_sum = 0;\n            for j in 0..n\
        \ {\n                row_sum += grid[i][j];\n                above_sums[j] +=\
        \ row_sum;\n                if above_sums[j] <= k {\n                    count\
        \ += 1;\n                }\n            }\n        }\n        count\n    }\n\
        }"
      racket: "(define/contract (count-submatrices grid k)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer? exact-integer?)\n  (let* ([n (length (car grid))]\n       \
        \  [above-sums (make-vector n 0)]\n         [count 0])\n    (for ([row grid])\n\
        \      (let ([row-sum 0])\n        (for ([val row]\n              [j (in-range\
        \ n)])\n          (set! row-sum (+ row-sum val))\n          (let ([current-sum\
        \ (+ row-sum (vector-ref above-sums j))])\n            (vector-set! above-sums\
        \ j current-sum)\n            (when (<= current-sum k)\n              (set!\
        \ count (+ count 1)))))))\n    count))"
      erlang: "-spec count_submatrices(Grid :: [[integer()]], K :: integer()) -> integer().\n\
        count_submatrices(Grid, K) ->\n    N = length(hd(Grid)),\n    InitialAboveSums\
        \ = lists:duplicate(N, 0),\n    process_rows(Grid, K, InitialAboveSums, 0).\n\
        \nprocess_rows([], _K, _AboveSums, Acc) -> Acc;\nprocess_rows([Row | Rest],\
        \ K, AboveSums, Acc) ->\n    {NewAboveSums, RowCount} = process_row(Row, K,\
        \ AboveSums, 0, 0, []),\n    process_rows(Rest, K, lists:reverse(NewAboveSums),\
        \ Acc + RowCount).\n\nprocess_row([], _K, [], _RowSum, RowCount, NewAboveSums)\
        \ ->\n    {NewAboveSums, RowCount};\nprocess_row([Val | RowRest], K, [AboveVal\
        \ | AboveRest], RowSum, RowCount, NewAboveSums) ->\n    NewRowSum = RowSum +\
        \ Val,\n    CurrentSum = NewRowSum + AboveVal,\n    NewCount = if CurrentSum\
        \ =< K -> RowCount + 1; true -> RowCount end,\n    process_row(RowRest, K, AboveRest,\
        \ NewRowSum, NewCount, [CurrentSum | NewAboveSums])."
      elixir: "defmodule Solution do\n  @spec count_submatrices(grid :: [[integer]],\
        \ k :: integer) :: integer\n  def count_submatrices(grid, k) do\n    n = length(hd(grid))\n\
        \    initial_above_sums = List.duplicate(0, n)\n    process_rows(grid, k, initial_above_sums,\
        \ 0)\n  end\n\n  defp process_rows([], _k, _above_sums, acc), do: acc\n  defp\
        \ process_rows([row | rest], k, above_sums, acc) do\n    {new_above_sums, row_count}\
        \ = process_row(row, k, above_sums, 0, 0, [])\n    process_rows(rest, k, Enum.reverse(new_above_sums),\
        \ acc + row_count)\n  end\n\n  defp process_row([], _k, [], _row_sum, row_count,\
        \ new_above_sums) do\n    {new_above_sums, row_count}\n  end\n  defp process_row([val\
        \ | row_rest], k, [above_val | above_rest], row_sum, row_count, new_above_sums)\
        \ do\n    new_row_sum = row_sum + val\n    current_sum = new_row_sum + above_val\n\
        \    new_count = if current_sum <= k, do: row_count + 1, else: row_count\n \
        \   process_row(row_rest, k, above_rest, new_row_sum, new_count, [current_sum\
        \ | new_above_sums])\n  end\nend"
    approach: 'The problem asks for the count of submatrices starting at the top-left
      corner $(0,0)$ that have a sum less than or equal to $k$. Each such submatrix
      is uniquely determined by its bottom-right corner $(i, j)$. To calculate the sum
      of each submatrix efficiently, we use a 2D prefix sum algorithm. The sum of the
      submatrix ending at $(i, j)$, denoted as $S[i][j]$, can be calculated from previously
      computed sums using the relation $S[i][j] = \text{grid}[i][j] + S[i-1][j] + S[i][j-1]
      - S[i-1][j-1]$. This allows us to determine the sum of any top-left submatrix
      in constant time as we iterate through the grid.


      We iterate through the grid row by row and column by column, updating each cell
      with its 2D prefix sum. Since all elements in the grid are non-negative, the prefix
      sums are monotonically non-decreasing as we move right or down. This means that
      if $S[i][j]$ exceeds $k$, any submatrix ending further to the right in the same
      row ($S[i][j'']$ where $j'' > j$) will also exceed $k$. We use this observation
      to optimize by breaking out of the inner loop early when the sum exceeds $k$,
      and we increment a counter for every submatrix whose sum satisfies the condition.'
    time_complexity: O(m * n) where m is the number of rows and n is the number of columns.
      We visit every cell of the matrix at most once to calculate its prefix sum and
      check the condition.
    space_complexity: O(1) additional space if the prefix sum calculation is performed
      in-place within the original grid, or O(m * n) if a separate prefix sum matrix
      is created. Given the constraints and the nature of the recurrence, in-place modification
      is the most space-efficient.
    elapsed_time: 187.5318500995636
    model: gemini-3-flash-preview
    generated_at: '2026-03-18 01:30:45 '
---

## Problem #3070: Count Submatrices with Top-Left Element and Sum Less Than k

**Difficulty:** Medium

**Topics:** Array, Matrix, Prefix Sum

## Problem Description

<p>You are given a <strong>0-indexed</strong> integer matrix <code>grid</code> and an integer <code>k</code>.</p>

<p>Return <em>the <strong>number</strong> of <span data-keyword="submatrix">submatrices</span> that contain the top-left element of the</em> <code>grid</code>, <em>and have a sum less than or equal to </em><code>k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/01/example1.png" style="padding: 10px; background: #fff; border-radius: .5rem;" />
<pre>
<strong>Input:</strong> grid = [[7,6,3],[6,6,1]], k = 18
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are only 4 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 18.</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/01/example21.png" style="padding: 10px; background: #fff; border-radius: .5rem;" />
<pre>
<strong>Input:</strong> grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
<strong>Output:</strong> 6
<strong>Explanation:</strong> There are only 6 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 20.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length </code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= n, m &lt;= 1000 </code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the count of submatrices starting at the top-left corner $(0,0)$ that have a sum less than or equal to $k$. Each such submatrix is uniquely determined by its bottom-right corner $(i, j)$. To calculate the sum of each submatrix efficiently, we use a 2D prefix sum algorithm. The sum of the submatrix ending at $(i, j)$, denoted as $S[i][j]$, can be calculated from previously computed sums using the relation $S[i][j] = \text{grid}[i][j] + S[i-1][j] + S[i][j-1] - S[i-1][j-1]$. This allows us to determine the sum of any top-left submatrix in constant time as we iterate through the grid.

We iterate through the grid row by row and column by column, updating each cell with its 2D prefix sum. Since all elements in the grid are non-negative, the prefix sums are monotonically non-decreasing as we move right or down. This means that if $S[i][j]$ exceeds $k$, any submatrix ending further to the right in the same row ($S[i][j']$ where $j' > j$) will also exceed $k$. We use this observation to optimize by breaking out of the inner loop early when the sum exceeds $k$, and we increment a counter for every submatrix whose sum satisfies the condition.

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
    int countSubmatrices(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        int count = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i > 0) grid[i][j] += grid[i - 1][j];
                if (j > 0) grid[i][j] += grid[i][j - 1];
                if (i > 0 && j > 0) grid[i][j] -= grid[i - 1][j - 1];
                if (grid[i][j] <= k) {
                    count++;
                } else {
                    break;
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
    public int countSubmatrices(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i > 0) grid[i][j] += grid[i - 1][j];
                if (j > 0) grid[i][j] += grid[i][j - 1];
                if (i > 0 && j > 0) grid[i][j] -= grid[i - 1][j - 1];
                if (grid[i][j] <= k) {
                    count++;
                } else {
                    break;
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
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if i > 0:
                    grid[i][j] += grid[i-1][j]
                if j > 0:
                    grid[i][j] += grid[i][j-1]
                if i > 0 and j > 0:
                    grid[i][j] -= grid[i-1][j-1]
                if grid[i][j] <= k:
                    count += 1
                else:
                    break
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if i > 0:
                    grid[i][j] += grid[i-1][j]
                if j > 0:
                    grid[i][j] += grid[i][j-1]
                if i > 0 and j > 0:
                    grid[i][j] -= grid[i-1][j-1]
                if grid[i][j] <= k:
                    count += 1
                else:
                    break
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countSubmatrices(int** grid, int gridSize, int* gridColSize, int k) {
    int m = gridSize;
    int n = gridColSize[0];
    int count = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (i > 0) grid[i][j] += grid[i - 1][j];
            if (j > 0) grid[i][j] += grid[i][j - 1];
            if (i > 0 && j > 0) grid[i][j] -= grid[i - 1][j - 1];
            if (grid[i][j] <= k) {
                count++;
            } else {
                break;
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
    public int CountSubmatrices(int[][] grid, int k) {
        int m = grid.Length;
        int n = grid[0].Length;
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i > 0) grid[i][j] += grid[i - 1][j];
                if (j > 0) grid[i][j] += grid[i][j - 1];
                if (i > 0 && j > 0) grid[i][j] -= grid[i - 1][j - 1];
                if (grid[i][j] <= k) {
                    count++;
                } else {
                    break;
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
 * @param {number} k
 * @return {number}
 */
var countSubmatrices = function(grid, k) {
    const m = grid.length;
    const n = grid[0].length;
    let count = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i > 0) grid[i][j] += grid[i - 1][j];
            if (j > 0) grid[i][j] += grid[i][j - 1];
            if (i > 0 && j > 0) grid[i][j] -= grid[i - 1][j - 1];
            if (grid[i][j] <= k) {
                count++;
            } else {
                break;
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
function countSubmatrices(grid: number[][], k: number): number {
    const m = grid.length;
    const n = grid[0].length;
    let count = 0;
    const prefixSums = new Array(n).fill(0);
    for (let i = 0; i < m; i++) {
        let rowSum = 0;
        for (let j = 0; j < n; j++) {
            rowSum += grid[i][j];
            prefixSums[j] += rowSum;
            if (prefixSums[j] <= k) {
                count++;
            } else {
                break;
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
     * @param Integer $k
     * @return Integer
     */
    function countSubmatrices($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $count = 0;
        $prefixSums = array_fill(0, $n, 0);
        for ($i = 0; $i < $m; $i++) {
            $rowSum = 0;
            for ($j = 0; $j < $n; $j++) {
                $rowSum += $grid[$i][$j];
                $prefixSums[$j] += $rowSum;
                if ($prefixSums[$j] <= $k) {
                    $count++;
                } else {
                    break;
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
    func countSubmatrices(_ grid: [[Int]], _ k: Int) -> Int {
        let m = grid.count
        let n = grid[0].count
        var count = 0
        var prefixSums = [Int](repeating: 0, count: n)
        for i in 0..<m {
            var rowSum = 0
            for j in 0..<n {
                rowSum += grid[i][j]
                prefixSums[j] += rowSum
                if prefixSums[j] <= k {
                    count += 1
                } else {
                    break
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
    fun countSubmatrices(grid: Array<IntArray>, k: Int): Int {
        val m = grid.size
        val n = grid[0].size
        var count = 0
        val prefixSums = IntArray(n)
        for (i in 0 until m) {
            var rowSum = 0
            for (j in 0 until n) {
                rowSum += grid[i][j]
                prefixSums[j] += rowSum
                if (prefixSums[j] <= k) {
                    count++
                } else {
                    break
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
  int countSubmatrices(List<List<int>> grid, int k) {
    int m = grid.length;
    int n = grid[0].length;
    int count = 0;
    List<int> prefixSums = List<int>.filled(n, 0);
    for (int i = 0; i < m; i++) {
      int rowSum = 0;
      for (int j = 0; j < n; j++) {
        rowSum += grid[i][j];
        prefixSums[j] += rowSum;
        if (prefixSums[j] <= k) {
          count++;
        } else {
          break;
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
func countSubmatrices(grid [][]int, k int) int {
    m := len(grid)
    n := len(grid[0])
    count := 0
    prefixSums := make([]int, n)
    for i := 0; i < m; i++ {
        rowSum := 0
        for j := 0; j < n; j++ {
            rowSum += grid[i][j]
            prefixSums[j] += rowSum
            if prefixSums[j] <= k {
                count++
            } else {
                break
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
# @param {Integer} k
# @return {Integer}
def count_submatrices(grid, k)
  m = grid.length
  n = grid[0].length
  count = 0
  above_sums = Array.new(n, 0)
  grid.each do |row|
    row_sum = 0
    row.each_with_index do |val, j|
      row_sum += val
      above_sums[j] += row_sum
      count += 1 if above_sums[j] <= k
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
  def countSubmatrices(grid: Array[Array[Int]], k: Int): Int = {
    val m = grid.length
    val n = grid(0).length
    val aboveSums = new Array[Int](n)
    var totalCount = 0
    for (i <- 0 until m) {
      var rowSum = 0
      for (j <- 0 until n) {
        rowSum += grid(i)(j)
        aboveSums(j) += rowSum
        if (aboveSums(j) <= k) {
          totalCount += 1
        }
      }
    }
    totalCount
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_submatrices(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut count = 0;
        let mut above_sums = vec![0; n];
        for i in 0..m {
            let mut row_sum = 0;
            for j in 0..n {
                row_sum += grid[i][j];
                above_sums[j] += row_sum;
                if above_sums[j] <= k {
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
(define/contract (count-submatrices grid k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ([n (length (car grid))]
         [above-sums (make-vector n 0)]
         [count 0])
    (for ([row grid])
      (let ([row-sum 0])
        (for ([val row]
              [j (in-range n)])
          (set! row-sum (+ row-sum val))
          (let ([current-sum (+ row-sum (vector-ref above-sums j))])
            (vector-set! above-sums j current-sum)
            (when (<= current-sum k)
              (set! count (+ count 1)))))))
    count))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec count_submatrices(Grid :: [[integer()]], K :: integer()) -> integer().
count_submatrices(Grid, K) ->
    N = length(hd(Grid)),
    InitialAboveSums = lists:duplicate(N, 0),
    process_rows(Grid, K, InitialAboveSums, 0).

process_rows([], _K, _AboveSums, Acc) -> Acc;
process_rows([Row | Rest], K, AboveSums, Acc) ->
    {NewAboveSums, RowCount} = process_row(Row, K, AboveSums, 0, 0, []),
    process_rows(Rest, K, lists:reverse(NewAboveSums), Acc + RowCount).

process_row([], _K, [], _RowSum, RowCount, NewAboveSums) ->
    {NewAboveSums, RowCount};
process_row([Val | RowRest], K, [AboveVal | AboveRest], RowSum, RowCount, NewAboveSums) ->
    NewRowSum = RowSum + Val,
    CurrentSum = NewRowSum + AboveVal,
    NewCount = if CurrentSum =< K -> RowCount + 1; true -> RowCount end,
    process_row(RowRest, K, AboveRest, NewRowSum, NewCount, [CurrentSum | NewAboveSums]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_submatrices(grid :: [[integer]], k :: integer) :: integer
  def count_submatrices(grid, k) do
    n = length(hd(grid))
    initial_above_sums = List.duplicate(0, n)
    process_rows(grid, k, initial_above_sums, 0)
  end

  defp process_rows([], _k, _above_sums, acc), do: acc
  defp process_rows([row | rest], k, above_sums, acc) do
    {new_above_sums, row_count} = process_row(row, k, above_sums, 0, 0, [])
    process_rows(rest, k, Enum.reverse(new_above_sums), acc + row_count)
  end

  defp process_row([], _k, [], _row_sum, row_count, new_above_sums) do
    {new_above_sums, row_count}
  end
  defp process_row([val | row_rest], k, [above_val | above_rest], row_sum, row_count, new_above_sums) do
    new_row_sum = row_sum + val
    current_sum = new_row_sum + above_val
    new_count = if current_sum <= k, do: row_count + 1, else: row_count
    process_row(row_rest, k, above_rest, new_row_sum, new_count, [current_sum | new_above_sums])
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m * n) where m is the number of rows and n is the number of columns. We visit every cell of the matrix at most once to calculate its prefix sum and check the condition.
- **Space Complexity:** O(1) additional space if the prefix sum calculation is performed in-place within the original grid, or O(m * n) if a separate prefix sum matrix is created. Given the constraints and the nature of the recurrence, in-place modification is the most space-efficient.
