---
layout: post
title: "Flip Square Submatrix Vertically"
date: 2026-03-21 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Two Pointers", "Matrix"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/flip-square-submatrix-vertically/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<vector<int>> reverseSubmatrix(vector<vector<int>>&\
        \ grid, int x, int y, int k) {\n        for (int i = 0; i < k / 2; ++i) {\n\
        \            int r1 = x + i;\n            int r2 = x + k - 1 - i;\n        \
        \    for (int j = 0; j < k; ++j) {\n                std::swap(grid[r1][y + j],\
        \ grid[r2][y + j]);\n            }\n        }\n        return grid;\n    }\n\
        };"
      java: "class Solution {\n    public int[][] reverseSubmatrix(int[][] grid, int\
        \ x, int y, int k) {\n        for (int i = 0; i < k / 2; i++) {\n          \
        \  int r1 = x + i;\n            int r2 = x + k - 1 - i;\n            for (int\
        \ j = 0; j < k; j++) {\n                int c = y + j;\n                int\
        \ temp = grid[r1][c];\n                grid[r1][c] = grid[r2][c];\n        \
        \        grid[r2][c] = temp;\n            }\n        }\n        return grid;\n\
        \    }\n}"
      python: "class Solution(object):\n    def reverseSubmatrix(self, grid, x, y, k):\n\
        \        \"\"\"\n        :type grid: List[List[int]]\n        :type x: int\n\
        \        :type y: int\n        :type k: int\n        :rtype: List[List[int]]\n\
        \        \"\"\"\n        for i in range(k / 2):\n            r1, r2 = x + i,\
        \ x + k - 1 - i\n            for j in range(y, y + k):\n                grid[r1][j],\
        \ grid[r2][j] = grid[r2][j], grid[r1][j]\n        return grid"
      python3: "class Solution:\n    def reverseSubmatrix(self, grid: List[List[int]],\
        \ x: int, y: int, k: int) -> List[List[int]]:\n        for i in range(k // 2):\n\
        \            r1, r2 = x + i, x + k - 1 - i\n            for j in range(y, y\
        \ + k):\n                grid[r1][j], grid[r2][j] = grid[r2][j], grid[r1][j]\n\
        \        return grid"
      c: "/**\n * Return an array of arrays of size *returnSize.\n * The sizes of the\
        \ arrays are returned as *returnColumnSizes array.\n * Note: Both returned array\
        \ and *columnSizes array must be malloced, assume caller calls free().\n */\n\
        int** reverseSubmatrix(int** grid, int gridSize, int* gridColSize, int x, int\
        \ y, int k, int* returnSize, int** returnColumnSizes) {\n    *returnSize = gridSize;\n\
        \    *returnColumnSizes = (int*)malloc(gridSize * sizeof(int));\n    int** result\
        \ = (int**)malloc(gridSize * sizeof(int*));\n    for (int i = 0; i < gridSize;\
        \ i++) {\n        (*returnColumnSizes)[i] = gridColSize[i];\n        result[i]\
        \ = (int*)malloc(gridColSize[i] * sizeof(int));\n        for (int j = 0; j <\
        \ gridColSize[i]; j++) {\n            result[i][j] = grid[i][j];\n        }\n\
        \    }\n    for (int i = 0; i < k / 2; i++) {\n        int r1 = x + i;\n   \
        \     int r2 = x + k - 1 - i;\n        for (int j = 0; j < k; j++) {\n     \
        \       int c = y + j;\n            int temp = result[r1][c];\n            result[r1][c]\
        \ = result[r2][c];\n            result[r2][c] = temp;\n        }\n    }\n  \
        \  return result;\n}"
      csharp: "public class Solution {\n    public int[][] ReverseSubmatrix(int[][]\
        \ grid, int x, int y, int k) {\n        for (int i = 0; i < k / 2; i++) {\n\
        \            int r1 = x + i;\n            int r2 = x + k - 1 - i;\n        \
        \    for (int j = 0; j < k; j++) {\n                int c = y + j;\n       \
        \         int temp = grid[r1][c];\n                grid[r1][c] = grid[r2][c];\n\
        \                grid[r2][c] = temp;\n            }\n        }\n        return\
        \ grid;\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @param {number} x\n * @param\
        \ {number} y\n * @param {number} k\n * @return {number[][]}\n */\nvar reverseSubmatrix\
        \ = function(grid, x, y, k) {\n    for (let i = 0; i < Math.floor(k / 2); i++)\
        \ {\n        let r1 = x + i;\n        let r2 = x + k - 1 - i;\n        for (let\
        \ j = 0; j < k; j++) {\n            let c = y + j;\n            let temp = grid[r1][c];\n\
        \            grid[r1][c] = grid[r2][c];\n            grid[r2][c] = temp;\n \
        \       }\n    }\n    return grid;\n};"
      typescript: "function reverseSubmatrix(grid: number[][], x: number, y: number,\
        \ k: number): number[][] {\n    let top = x;\n    let bottom = x + k - 1;\n\
        \    while (top < bottom) {\n        for (let j = y; j < y + k; j++) {\n   \
        \         const temp = grid[top][j];\n            grid[top][j] = grid[bottom][j];\n\
        \            grid[bottom][j] = temp;\n        }\n        top++;\n        bottom--;\n\
        \    }\n    return grid;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @param\
        \ Integer $x\n     * @param Integer $y\n     * @param Integer $k\n     * @return\
        \ Integer[][]\n     */\n    function reverseSubmatrix($grid, $x, $y, $k) {\n\
        \        $top = $x;\n        $bottom = $x + $k - 1;\n        while ($top < $bottom)\
        \ {\n            for ($j = $y; $j < $y + $k; $j++) {\n                $temp\
        \ = $grid[$top][$j];\n                $grid[$top][$j] = $grid[$bottom][$j];\n\
        \                $grid[$bottom][$j] = $temp;\n            }\n            $top++;\n\
        \            $bottom--;\n        }\n        return $grid;\n    }\n}"
      swift: "class Solution {\n    func reverseSubmatrix(_ grid: [[Int]], _ x: Int,\
        \ _ y: Int, _ k: Int) -> [[Int]] {\n        var res = grid\n        var top\
        \ = x\n        var bottom = x + k - 1\n        while top < bottom {\n      \
        \      for j in y..<(y + k) {\n                let temp = res[top][j]\n    \
        \            res[top][j] = res[bottom][j]\n                res[bottom][j] =\
        \ temp\n            }\n            top += 1\n            bottom -= 1\n     \
        \   }\n        return res\n    }\n}"
      kotlin: "class Solution {\n    fun reverseSubmatrix(grid: Array<IntArray>, x:\
        \ Int, y: Int, k: Int): Array<IntArray> {\n        var top = x\n        var\
        \ bottom = x + k - 1\n        while (top < bottom) {\n            for (j in\
        \ y until (y + k)) {\n                val temp = grid[top][j]\n            \
        \    grid[top][j] = grid[bottom][j]\n                grid[bottom][j] = temp\n\
        \            }\n            top++\n            bottom--\n        }\n       \
        \ return grid\n    }\n}"
      dart: "class Solution {\n  List<List<int>> reverseSubmatrix(List<List<int>> grid,\
        \ int x, int y, int k) {\n    int top = x;\n    int bottom = x + k - 1;\n  \
        \  while (top < bottom) {\n      for (int j = y; j < y + k; j++) {\n       \
        \ int temp = grid[top][j];\n        grid[top][j] = grid[bottom][j];\n      \
        \  grid[bottom][j] = temp;\n      }\n      top++;\n      bottom--;\n    }\n\
        \    return grid;\n  }\n}"
      go: "func reverseSubmatrix(grid [][]int, x int, y int, k int) [][]int {\n    top\
        \ := x\n    bottom := x + k - 1\n    for top < bottom {\n        for j := y;\
        \ j < y + k; j++ {\n            grid[top][j], grid[bottom][j] = grid[bottom][j],\
        \ grid[top][j]\n        }\n        top++\n        bottom--\n    }\n    return\
        \ grid\n}"
      ruby: "def reverse_submatrix(grid, x, y, k)\n  (0...(k / 2)).each do |i|\n   \
        \ r1 = x + i\n    r2 = x + k - 1 - i\n    (y...(y + k)).each do |j|\n      grid[r1][j],\
        \ grid[r2][j] = grid[r2][j], grid[r1][j]\n    end\n  end\n  grid\nend"
      scala: "object Solution {\n  def reverseSubmatrix(grid: Array[Array[Int]], x:\
        \ Int, y: Int, k: Int): Array[Array[Int]] = {\n    for (i <- 0 until k / 2)\
        \ {\n      val r1 = x + i\n      val r2 = x + k - 1 - i\n      for (j <- y until\
        \ y + k) {\n        val temp = grid(r1)(j)\n        grid(r1)(j) = grid(r2)(j)\n\
        \        grid(r2)(j) = temp\n      }\n    }\n    grid\n  }\n}"
      rust: "impl Solution {\n    pub fn reverse_submatrix(grid: Vec<Vec<i32>>, x: i32,\
        \ y: i32, k: i32) -> Vec<Vec<i32>> {\n        let mut grid = grid;\n       \
        \ let (ux, uy, uk) = (x as usize, y as usize, k as usize);\n        for i in\
        \ 0..(uk / 2) {\n            let r1 = ux + i;\n            let r2 = ux + uk\
        \ - 1 - i;\n            for j in uy..(uy + uk) {\n                let temp =\
        \ grid[r1][j];\n                grid[r1][j] = grid[r2][j];\n               \
        \ grid[r2][j] = temp;\n            }\n        }\n        grid\n    }\n}"
      racket: "(define/contract (reverse-submatrix grid x y k)\n  (-> (listof (listof\
        \ exact-integer?)) exact-integer? exact-integer? exact-integer? (listof (listof\
        \ exact-integer?)))\n  (let* ([grid-vec (list->vector (map list->vector grid))])\n\
        \    (for ([i (in-range (quotient k 2))])\n      (let* ([r1-idx (+ x i)]\n \
        \            [r2-idx (- (+ x k) i 1)]\n             [r1 (vector-ref grid-vec\
        \ r1-idx)]\n             [r2 (vector-ref grid-vec r2-idx)])\n        (for ([j\
        \ (in-range y (+ y k))])\n          (let ([v1 (vector-ref r1 j)]\n         \
        \       [v2 (vector-ref r2 j)])\n            (vector-set! r1 j v2)\n       \
        \     (vector-set! r2 j v1)))))\n    (map vector->list (vector->list grid-vec))))"
      erlang: "reverse_submatrix(Grid, X, Y, K) ->\n    Rows = list_to_tuple([list_to_tuple(R)\
        \ || R <- Grid]),\n    M = tuple_size(Rows),\n    FinalRows = flip_rows(Rows,\
        \ X, Y, K, 0),\n    [tuple_to_list(element(I, FinalRows)) || I <- lists:seq(1,\
        \ M)].\n\nflip_rows(Rows, X, Y, K, I) when I < K div 2 ->\n    R1Idx = X + I\
        \ + 1,\n    R2Idx = X + K - 1 - I + 1,\n    R1 = element(R1Idx, Rows),\n   \
        \ R2 = element(R2Idx, Rows),\n    {NewR1, NewR2} = swap_cols(R1, R2, Y, K, 0),\n\
        \    Rows1 = setelement(R1Idx, Rows, NewR1),\n    NewRows = setelement(R2Idx,\
        \ Rows1, NewR2),\n    flip_rows(NewRows, X, Y, K, I + 1);\nflip_rows(Rows, _,\
        \ _, _, _) -> Rows.\n\nswap_cols(R1, R2, Y, K, J) when J < K ->\n    CIdx =\
        \ Y + J + 1,\n    V1 = element(CIdx, R1),\n    V2 = element(CIdx, R2),\n   \
        \ NewR1 = setelement(CIdx, R1, V2),\n    NewR2 = setelement(CIdx, R2, V1),\n\
        \    swap_cols(NewR1, NewR2, Y, K, J + 1);\nswap_cols(R1, R2, _, _, _) -> {R1,\
        \ R2}."
      elixir: "defmodule Solution do\n  @spec reverse_submatrix(grid :: [[integer]],\
        \ x :: integer, y :: integer, k :: integer) :: [[integer]]\n  def reverse_submatrix(grid,\
        \ x, y, k) do\n    grid_tuple = grid |> Enum.map(&List.to_tuple/1) |> List.to_tuple()\n\
        \    num_flips = div(k, 2)\n    result_tuple = if num_flips > 0 do\n      Enum.reduce(0..(num_flips\
        \ - 1), grid_tuple, fn i, acc ->\n        r1_idx = x + i\n        r2_idx = x\
        \ + k - 1 - i\n        r1 = elem(acc, r1_idx)\n        r2 = elem(acc, r2_idx)\n\
        \        {new_r1, new_r2} = Enum.reduce(y..(y + k - 1), {r1, r2}, fn j, {acc_r1,\
        \ acc_r2} ->\n          v1 = elem(acc_r1, j)\n          v2 = elem(acc_r2, j)\n\
        \          {put_elem(acc_r1, j, v2), put_elem(acc_r2, j, v1)}\n        end)\n\
        \        acc |> put_elem(r1_idx, new_r1) |> put_elem(r2_idx, new_r2)\n     \
        \ end)\n    else\n      grid_tuple\n    end\n    result_tuple |> Tuple.to_list()\
        \ |> Enum.map(&Tuple.to_list/1)\n  end\nend"
    approach: 'To flip the square submatrix vertically, the algorithm targets the specific
      region defined by the top-left corner (x, y) and side length k. It employs a two-pointer
      approach along the vertical axis of this submatrix, iterating from the top row
      index x and bottom row index x + k - 1 toward the middle. For each pair of symmetric
      rows, it swaps the elements located in the columns ranging from y to y + k - 1,
      effectively reversing the row order within that specific sub-square.


      Since the transformation only affects elements within the boundaries [x, x + k
      - 1] and [y, y + k - 1], the rest of the grid remains unchanged. The swapping
      process is performed in-place for most languages, ensuring efficiency. The nested
      loop structure iterates through half of the submatrix rows and all of its columns,
      completing the vertical flip with a number of operations proportional to the area
      of the submatrix square.'
    time_complexity: O(k^2) where k is the side length of the square submatrix. The
      algorithm iterates through k/2 rows and k columns within the submatrix boundaries
      to perform swaps, resulting in O(k^2) total operations. The overall dimensions
      of the grid, m and n, do not affect the runtime beyond defining the submatrix
      limits.
    space_complexity: O(1) in most environments because the submatrix is flipped in-place
      within the existing memory. In the C implementation, the complexity is O(m * n)
      as the problem signature requires returning a newly allocated 2D array representing
      the modified grid.
    elapsed_time: 101.50705599784851
    model: gemini-3-flash-preview
    generated_at: '2026-03-21 01:20:32 '
---

## Problem #3643: Flip Square Submatrix Vertically

**Difficulty:** Easy

**Topics:** Array, Two Pointers, Matrix

## Problem Description

<p>You are given an <code>m x n</code> integer matrix <code>grid</code>, and three integers <code>x</code>, <code>y</code>, and <code>k</code>.</p>

<p>The integers <code>x</code> and <code>y</code> represent the row and column indices of the <strong>top-left</strong> corner of a <strong>square</strong> submatrix and the integer <code>k</code> represents the size (side length) of the square submatrix.</p>

<p>Your task is to flip the submatrix by reversing the order of its rows vertically.</p>

<p>Return the updated matrix.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2025/07/20/gridexmdrawio.png" style="width: 300px; height: 116px;" />
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = </span>[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]<span class="example-io">, x = 1, y = 0, k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">[[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]</span></p>

<p><strong>Explanation:</strong></p>

<p>The diagram above shows the grid before and after the transformation.</p>
</div>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2025/07/20/gridexm2drawio.png" style="width: 350px; height: 68px;" />​​​​​​​
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[3,4,2,3],[2,3,4,2]], x = 0, y = 2, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[[3,4,4,2],[2,3,2,3]]</span></p>

<p><strong>Explanation:</strong></p>

<p>The diagram above shows the grid before and after the transformation.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 100</code></li>
	<li><code>0 &lt;= x &lt; m</code></li>
	<li><code>0 &lt;= y &lt; n</code></li>
	<li><code>1 &lt;= k &lt;= min(m - x, n - y)</code></li>
</ul>


## Hints

1. Use two pointers at the block's top and bottom rows and swap their `k` columns pairwise until the pointers meet.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To flip the square submatrix vertically, the algorithm targets the specific region defined by the top-left corner (x, y) and side length k. It employs a two-pointer approach along the vertical axis of this submatrix, iterating from the top row index x and bottom row index x + k - 1 toward the middle. For each pair of symmetric rows, it swaps the elements located in the columns ranging from y to y + k - 1, effectively reversing the row order within that specific sub-square.

Since the transformation only affects elements within the boundaries [x, x + k - 1] and [y, y + k - 1], the rest of the grid remains unchanged. The swapping process is performed in-place for most languages, ensuring efficiency. The nested loop structure iterates through half of the submatrix rows and all of its columns, completing the vertical flip with a number of operations proportional to the area of the submatrix square.

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
    vector<vector<int>> reverseSubmatrix(vector<vector<int>>& grid, int x, int y, int k) {
        for (int i = 0; i < k / 2; ++i) {
            int r1 = x + i;
            int r2 = x + k - 1 - i;
            for (int j = 0; j < k; ++j) {
                std::swap(grid[r1][y + j], grid[r2][y + j]);
            }
        }
        return grid;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int[][] reverseSubmatrix(int[][] grid, int x, int y, int k) {
        for (int i = 0; i < k / 2; i++) {
            int r1 = x + i;
            int r2 = x + k - 1 - i;
            for (int j = 0; j < k; j++) {
                int c = y + j;
                int temp = grid[r1][c];
                grid[r1][c] = grid[r2][c];
                grid[r2][c] = temp;
            }
        }
        return grid;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :type k: int
        :rtype: List[List[int]]
        """
        for i in range(k / 2):
            r1, r2 = x + i, x + k - 1 - i
            for j in range(y, y + k):
                grid[r1][j], grid[r2][j] = grid[r2][j], grid[r1][j]
        return grid
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k // 2):
            r1, r2 = x + i, x + k - 1 - i
            for j in range(y, y + k):
                grid[r1][j], grid[r2][j] = grid[r2][j], grid[r1][j]
        return grid
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** reverseSubmatrix(int** grid, int gridSize, int* gridColSize, int x, int y, int k, int* returnSize, int** returnColumnSizes) {
    *returnSize = gridSize;
    *returnColumnSizes = (int*)malloc(gridSize * sizeof(int));
    int** result = (int**)malloc(gridSize * sizeof(int*));
    for (int i = 0; i < gridSize; i++) {
        (*returnColumnSizes)[i] = gridColSize[i];
        result[i] = (int*)malloc(gridColSize[i] * sizeof(int));
        for (int j = 0; j < gridColSize[i]; j++) {
            result[i][j] = grid[i][j];
        }
    }
    for (int i = 0; i < k / 2; i++) {
        int r1 = x + i;
        int r2 = x + k - 1 - i;
        for (int j = 0; j < k; j++) {
            int c = y + j;
            int temp = result[r1][c];
            result[r1][c] = result[r2][c];
            result[r2][c] = temp;
        }
    }
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[][] ReverseSubmatrix(int[][] grid, int x, int y, int k) {
        for (int i = 0; i < k / 2; i++) {
            int r1 = x + i;
            int r2 = x + k - 1 - i;
            for (int j = 0; j < k; j++) {
                int c = y + j;
                int temp = grid[r1][c];
                grid[r1][c] = grid[r2][c];
                grid[r2][c] = temp;
            }
        }
        return grid;
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
 * @param {number} x
 * @param {number} y
 * @param {number} k
 * @return {number[][]}
 */
var reverseSubmatrix = function(grid, x, y, k) {
    for (let i = 0; i < Math.floor(k / 2); i++) {
        let r1 = x + i;
        let r2 = x + k - 1 - i;
        for (let j = 0; j < k; j++) {
            let c = y + j;
            let temp = grid[r1][c];
            grid[r1][c] = grid[r2][c];
            grid[r2][c] = temp;
        }
    }
    return grid;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function reverseSubmatrix(grid: number[][], x: number, y: number, k: number): number[][] {
    let top = x;
    let bottom = x + k - 1;
    while (top < bottom) {
        for (let j = y; j < y + k; j++) {
            const temp = grid[top][j];
            grid[top][j] = grid[bottom][j];
            grid[bottom][j] = temp;
        }
        top++;
        bottom--;
    }
    return grid;
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
     * @param Integer $x
     * @param Integer $y
     * @param Integer $k
     * @return Integer[][]
     */
    function reverseSubmatrix($grid, $x, $y, $k) {
        $top = $x;
        $bottom = $x + $k - 1;
        while ($top < $bottom) {
            for ($j = $y; $j < $y + $k; $j++) {
                $temp = $grid[$top][$j];
                $grid[$top][$j] = $grid[$bottom][$j];
                $grid[$bottom][$j] = $temp;
            }
            $top++;
            $bottom--;
        }
        return $grid;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func reverseSubmatrix(_ grid: [[Int]], _ x: Int, _ y: Int, _ k: Int) -> [[Int]] {
        var res = grid
        var top = x
        var bottom = x + k - 1
        while top < bottom {
            for j in y..<(y + k) {
                let temp = res[top][j]
                res[top][j] = res[bottom][j]
                res[bottom][j] = temp
            }
            top += 1
            bottom -= 1
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
    fun reverseSubmatrix(grid: Array<IntArray>, x: Int, y: Int, k: Int): Array<IntArray> {
        var top = x
        var bottom = x + k - 1
        while (top < bottom) {
            for (j in y until (y + k)) {
                val temp = grid[top][j]
                grid[top][j] = grid[bottom][j]
                grid[bottom][j] = temp
            }
            top++
            bottom--
        }
        return grid
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<List<int>> reverseSubmatrix(List<List<int>> grid, int x, int y, int k) {
    int top = x;
    int bottom = x + k - 1;
    while (top < bottom) {
      for (int j = y; j < y + k; j++) {
        int temp = grid[top][j];
        grid[top][j] = grid[bottom][j];
        grid[bottom][j] = temp;
      }
      top++;
      bottom--;
    }
    return grid;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func reverseSubmatrix(grid [][]int, x int, y int, k int) [][]int {
    top := x
    bottom := x + k - 1
    for top < bottom {
        for j := y; j < y + k; j++ {
            grid[top][j], grid[bottom][j] = grid[bottom][j], grid[top][j]
        }
        top++
        bottom--
    }
    return grid
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def reverse_submatrix(grid, x, y, k)
  (0...(k / 2)).each do |i|
    r1 = x + i
    r2 = x + k - 1 - i
    (y...(y + k)).each do |j|
      grid[r1][j], grid[r2][j] = grid[r2][j], grid[r1][j]
    end
  end
  grid
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def reverseSubmatrix(grid: Array[Array[Int]], x: Int, y: Int, k: Int): Array[Array[Int]] = {
    for (i <- 0 until k / 2) {
      val r1 = x + i
      val r2 = x + k - 1 - i
      for (j <- y until y + k) {
        val temp = grid(r1)(j)
        grid(r1)(j) = grid(r2)(j)
        grid(r2)(j) = temp
      }
    }
    grid
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn reverse_submatrix(grid: Vec<Vec<i32>>, x: i32, y: i32, k: i32) -> Vec<Vec<i32>> {
        let mut grid = grid;
        let (ux, uy, uk) = (x as usize, y as usize, k as usize);
        for i in 0..(uk / 2) {
            let r1 = ux + i;
            let r2 = ux + uk - 1 - i;
            for j in uy..(uy + uk) {
                let temp = grid[r1][j];
                grid[r1][j] = grid[r2][j];
                grid[r2][j] = temp;
            }
        }
        grid
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (reverse-submatrix grid x y k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer? (listof (listof exact-integer?)))
  (let* ([grid-vec (list->vector (map list->vector grid))])
    (for ([i (in-range (quotient k 2))])
      (let* ([r1-idx (+ x i)]
             [r2-idx (- (+ x k) i 1)]
             [r1 (vector-ref grid-vec r1-idx)]
             [r2 (vector-ref grid-vec r2-idx)])
        (for ([j (in-range y (+ y k))])
          (let ([v1 (vector-ref r1 j)]
                [v2 (vector-ref r2 j)])
            (vector-set! r1 j v2)
            (vector-set! r2 j v1)))))
    (map vector->list (vector->list grid-vec))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
reverse_submatrix(Grid, X, Y, K) ->
    Rows = list_to_tuple([list_to_tuple(R) || R <- Grid]),
    M = tuple_size(Rows),
    FinalRows = flip_rows(Rows, X, Y, K, 0),
    [tuple_to_list(element(I, FinalRows)) || I <- lists:seq(1, M)].

flip_rows(Rows, X, Y, K, I) when I < K div 2 ->
    R1Idx = X + I + 1,
    R2Idx = X + K - 1 - I + 1,
    R1 = element(R1Idx, Rows),
    R2 = element(R2Idx, Rows),
    {NewR1, NewR2} = swap_cols(R1, R2, Y, K, 0),
    Rows1 = setelement(R1Idx, Rows, NewR1),
    NewRows = setelement(R2Idx, Rows1, NewR2),
    flip_rows(NewRows, X, Y, K, I + 1);
flip_rows(Rows, _, _, _, _) -> Rows.

swap_cols(R1, R2, Y, K, J) when J < K ->
    CIdx = Y + J + 1,
    V1 = element(CIdx, R1),
    V2 = element(CIdx, R2),
    NewR1 = setelement(CIdx, R1, V2),
    NewR2 = setelement(CIdx, R2, V1),
    swap_cols(NewR1, NewR2, Y, K, J + 1);
swap_cols(R1, R2, _, _, _) -> {R1, R2}.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec reverse_submatrix(grid :: [[integer]], x :: integer, y :: integer, k :: integer) :: [[integer]]
  def reverse_submatrix(grid, x, y, k) do
    grid_tuple = grid |> Enum.map(&List.to_tuple/1) |> List.to_tuple()
    num_flips = div(k, 2)
    result_tuple = if num_flips > 0 do
      Enum.reduce(0..(num_flips - 1), grid_tuple, fn i, acc ->
        r1_idx = x + i
        r2_idx = x + k - 1 - i
        r1 = elem(acc, r1_idx)
        r2 = elem(acc, r2_idx)
        {new_r1, new_r2} = Enum.reduce(y..(y + k - 1), {r1, r2}, fn j, {acc_r1, acc_r2} ->
          v1 = elem(acc_r1, j)
          v2 = elem(acc_r2, j)
          {put_elem(acc_r1, j, v2), put_elem(acc_r2, j, v1)}
        end)
        acc |> put_elem(r1_idx, new_r1) |> put_elem(r2_idx, new_r2)
      end)
    else
      grid_tuple
    end
    result_tuple |> Tuple.to_list() |> Enum.map(&Tuple.to_list/1)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(k^2) where k is the side length of the square submatrix. The algorithm iterates through k/2 rows and k columns within the submatrix boundaries to perform swaps, resulting in O(k^2) total operations. The overall dimensions of the grid, m and n, do not affect the runtime beyond defining the submatrix limits.
- **Space Complexity:** O(1) in most environments because the submatrix is flipped in-place within the existing memory. In the C implementation, the complexity is O(m * n) as the problem signature requires returning a newly allocated 2D array representing the modified grid.
