---
layout: post
title: "Shift 2D Grid"
date: 2026-07-20 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Matrix", "Simulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/shift-2d-grid/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<vector<int>> shiftGrid(vector<vector<int>>&\
        \ grid, int k) {\n        int m = grid.size();\n        int n = grid[0].size();\n\
        \        int total = m * n;\n        k %= total;\n        vector<vector<int>>\
        \ res(m, vector<int>(n));\n        for (int i = 0; i < m; ++i) {\n         \
        \   for (int j = 0; j < n; ++j) {\n                int oldIdx = i * n + j;\n\
        \                int newIdx = (oldIdx + k) % total;\n                res[newIdx\
        \ / n][newIdx % n] = grid[i][j];\n            }\n        }\n        return res;\n\
        \    }\n};"
      java: "class Solution {\n    public List<List<Integer>> shiftGrid(int[][] grid,\
        \ int k) {\n        int m = grid.length;\n        int n = grid[0].length;\n\
        \        int total = m * n;\n        k %= total;\n        int[][] temp = new\
        \ int[m][n];\n        for (int i = 0; i < m; i++) {\n            for (int j\
        \ = 0; j < n; j++) {\n                int index = (i * n + j + k) % total;\n\
        \                temp[index / n][index % n] = grid[i][j];\n            }\n \
        \       }\n        List<List<Integer>> result = new ArrayList<>();\n       \
        \ for (int i = 0; i < m; i++) {\n            List<Integer> row = new ArrayList<>();\n\
        \            for (int j = 0; j < n; j++) {\n                row.add(temp[i][j]);\n\
        \            }\n            result.add(row);\n        }\n        return result;\n\
        \    }\n}"
      python: "class Solution(object):\n    def shiftGrid(self, grid, k):\n        \"\
        \"\"\n        :type grid: List[List[int]]\n        :type k: int\n        :rtype:\
        \ List[List[int]]\n        \"\"\"\n        m = len(grid)\n        n = len(grid[0])\n\
        \        total = m * n\n        k %= total\n        res = [[0] * n for _ in\
        \ range(m)]\n        for i in range(m):\n            for j in range(n):\n  \
        \              old_idx = i * n + j\n                new_idx = (old_idx + k)\
        \ % total\n                res[new_idx // n][new_idx % n] = grid[i][j]\n   \
        \     return res"
      python3: "class Solution:\n    def shiftGrid(self, grid: List[List[int]], k: int)\
        \ -> List[List[int]]:\n        m, n = len(grid), len(grid[0])\n        total\
        \ = m * n\n        k %= total\n        res = [[0] * n for _ in range(m)]\n \
        \       for i in range(m):\n            for j in range(n):\n               \
        \ old_idx = i * n + j\n                new_idx = (old_idx + k) % total\n   \
        \             res[new_idx // n][new_idx % n] = grid[i][j]\n        return res"
      c: "/**\n * Return an array of arrays of size *returnSize.\n * The sizes of the\
        \ arrays are returned as *returnColumnSizes array.\n * Note: Both returned array\
        \ and *columnSizes array must be malloced, assume caller calls free().\n */\n\
        int** shiftGrid(int** grid, int gridSize, int* gridColSize, int k, int* returnSize,\
        \ int** returnColumnSizes) {\n    int m = gridSize;\n    int n = gridColSize[0];\n\
        \    int total = m * n;\n    k %= total;\n    int** res = (int**)malloc(m *\
        \ sizeof(int*));\n    *returnColumnSizes = (int*)malloc(m * sizeof(int));\n\
        \    *returnSize = m;\n    for (int i = 0; i < m; i++) {\n        res[i] = (int*)malloc(n\
        \ * sizeof(int));\n        (*returnColumnSizes)[i] = n;\n    }\n    for (int\
        \ i = 0; i < m; i++) {\n        for (int j = 0; j < n; j++) {\n            int\
        \ oldIdx = i * n + j;\n            int newIdx = (oldIdx + k) % total;\n    \
        \        res[newIdx / n][newIdx % n] = grid[i][j];\n        }\n    }\n    return\
        \ res;\n}"
      csharp: "public class Solution {\n    public IList<IList<int>> ShiftGrid(int[][]\
        \ grid, int k) {\n        int m = grid.Length;\n        int n = grid[0].Length;\n\
        \        int total = m * n;\n        k %= total;\n        int[][] temp = new\
        \ int[m][];\n        for (int i = 0; i < m; i++) {\n            temp[i] = new\
        \ int[n];\n        }\n        for (int i = 0; i < m; i++) {\n            for\
        \ (int j = 0; j < n; j++) {\n                int index = (i * n + j + k) % total;\n\
        \                temp[index / n][index % n] = grid[i][j];\n            }\n \
        \       }\n        IList<IList<int>> result = new List<IList<int>>();\n    \
        \    for (int i = 0; i < m; i++) {\n            result.Add(new List<int>(temp[i]));\n\
        \        }\n        return result;\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @param {number} k\n * @return\
        \ {number[][]}\n */\nvar shiftGrid = function(grid, k) {\n    const m = grid.length;\n\
        \    const n = grid[0].length;\n    const total = m * n;\n    k %= total;\n\
        \    const res = Array.from({ length: m }, () => Array(n).fill(0));\n    for\
        \ (let i = 0; i < m; i++) {\n        for (let j = 0; j < n; j++) {\n       \
        \     let oldIdx = i * n + j;\n            let newIdx = (oldIdx + k) % total;\n\
        \            res[Math.floor(newIdx / n)][newIdx % n] = grid[i][j];\n       \
        \ }\n    }\n    return res;\n};"
      typescript: "function shiftGrid(grid: number[][], k: number): number[][] {\n \
        \   const m = grid.length;\n    const n = grid[0].length;\n    const total =\
        \ m * n;\n    const shift = k % total;\n    const result: number[][] = Array.from({\
        \ length: m }, () => new Array(n).fill(0));\n\n    for (let i = 0; i < m; i++)\
        \ {\n        for (let j = 0; j < n; j++) {\n            const flatIdx = (i *\
        \ n + j + shift) % total;\n            const newR = Math.floor(flatIdx / n);\n\
        \            const newC = flatIdx % n;\n            result[newR][newC] = grid[i][j];\n\
        \        }\n    }\n    return result;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @param\
        \ Integer $k\n     * @return Integer[][]\n     */\n    function shiftGrid($grid,\
        \ $k) {\n        $m = count($grid);\n        $n = count($grid[0]);\n       \
        \ $total = $m * $n;\n        $shift = $k % $total;\n        $result = [];\n\
        \        for ($i = 0; $i < $m; $i++) {\n            $result[$i] = array_fill(0,\
        \ $n, 0);\n        }\n\n        for ($i = 0; $i < $m; $i++) {\n            for\
        \ ($j = 0; $j < $n; $j++) {\n                $flatIdx = ($i * $n + $j + $shift)\
        \ % $total;\n                $newR = (int)($flatIdx / $n);\n               \
        \ $newC = $flatIdx % $n;\n                $result[$newR][$newC] = $grid[$i][$j];\n\
        \            }\n        }\n        return $result;\n    }\n}"
      swift: "class Solution {\n    func shiftGrid(_ grid: [[Int]], _ k: Int) -> [[Int]]\
        \ {\n        let m = grid.count\n        let n = grid[0].count\n        let\
        \ total = m * n\n        let shift = k % total\n        var result = Array(repeating:\
        \ Array(repeating: 0, count: n), count: m)\n\n        for i in 0..<m {\n   \
        \         for j in 0..<n {\n                let flatIdx = (i * n + j + shift)\
        \ % total\n                let newR = flatIdx / n\n                let newC\
        \ = flatIdx % n\n                result[newR][newC] = grid[i][j]\n         \
        \   }\n        }\n        return result\n    }\n}"
      kotlin: "class Solution {\n    fun shiftGrid(grid: Array<IntArray>, k: Int): List<List<Int>>\
        \ {\n        val m = grid.size\n        val n = grid[0].size\n        val total\
        \ = m * n\n        val shift = k % total\n        val result = Array(m) { IntArray(n)\
        \ }\n\n        for (i in 0 until m) {\n            for (j in 0 until n) {\n\
        \                val flatIdx = (i * n + j + shift) % total\n               \
        \ val newR = flatIdx / n\n                val newC = flatIdx % n\n         \
        \       result[newR][newC] = grid[i][j]\n            }\n        }\n\n      \
        \  return result.map { it.toList() }\n    }\n}"
      dart: "class Solution {\n  List<List<int>> shiftGrid(List<List<int>> grid, int\
        \ k) {\n    int m = grid.length;\n    int n = grid[0].length;\n    int total\
        \ = m * n;\n    int shift = k % total;\n    List<List<int>> result = List.generate(m,\
        \ (_) => List<int>.filled(n, 0));\n\n    for (int i = 0; i < m; i++) {\n   \
        \   for (int j = 0; j < n; j++) {\n        int flatIdx = (i * n + j + shift)\
        \ % total;\n        int newR = flatIdx ~/ n;\n        int newC = flatIdx % n;\n\
        \        result[newR][newC] = grid[i][j];\n      }\n    }\n    return result;\n\
        \  }\n}"
      go: "func shiftGrid(grid [][]int, k int) [][]int {\n    m := len(grid)\n    n\
        \ := len(grid[0])\n    total := m * n\n    shift := k % total\n\n    result\
        \ := make([][]int, m)\n    for i := range result {\n        result[i] = make([]int,\
        \ n)\n    }\n\n    for i := 0; i < m; i++ {\n        for j := 0; j < n; j++\
        \ {\n            flatIdx := (i*n + j + shift) % total\n            newR := flatIdx\
        \ / n\n            newC := flatIdx % n\n            result[newR][newC] = grid[i][j]\n\
        \        }\n    }\n    return result\n}"
      ruby: "def shift_grid(grid, k)\n  m = grid.length\n  n = grid[0].length\n  size\
        \ = m * n\n  k %= size\n  return grid if k == 0\n\n  flat = grid.flatten\n \
        \ rotated = flat.rotate(-k)\n  rotated.each_slice(n).to_a\nend"
      scala: "object Solution {\n    def shiftGrid(grid: Array[Array[Int]], k: Int):\
        \ List[List[Int]] = {\n        val m = grid.length\n        val n = grid(0).length\n\
        \        val size = m * n\n        val s = k % size\n        val flat = grid.flatten\n\
        \        val result = new Array[Int](size)\n\n        for (i <- 0 until size)\
        \ {\n            result((i + s) % size) = flat(i)\n        }\n\n        result.grouped(n).map(_.toList).toList\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn shift_grid(grid: Vec<Vec<i32>>, k: i32) ->\
        \ Vec<Vec<i32>> {\n        let m = grid.len();\n        let n = grid[0].len();\n\
        \        let size = m * n;\n        let k = (k as usize) % size;\n\n       \
        \ if k == 0 {\n            return grid;\n        }\n\n        let mut flat:\
        \ Vec<i32> = grid.into_iter().flatten().collect();\n        flat.rotate_right(k);\n\
        \n        flat.chunks(n)\n            .map(|chunk| chunk.to_vec())\n       \
        \     .collect()\n    }\n}"
      racket: "(define/contract (shift-grid grid k)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer? (listof (listof exact-integer?)))\n  (let* ([m (length grid)]\n\
        \         [n (length (car grid))]\n         [size (* m n)]\n         [s (modulo\
        \ k size)])\n    (if (zero? s)\n        grid\n        (let* ([flat (flatten\
        \ grid)]\n               [pos (- size s)]\n               [prefix (take flat\
        \ pos)]\n               [suffix (drop flat pos)]\n               [rotated (append\
        \ suffix prefix)])\n          (let loop ([lst rotated])\n            (if (null?\
        \ lst)\n                '()\n                (cons (take lst n) (loop (drop\
        \ lst n)))))))))"
      erlang: "-spec shift_grid(Grid :: [[integer()]], K :: integer()) -> [[integer()]].\n\
        shift_grid(Grid, K) ->\n  M = length(Grid),\n  N = length(hd(Grid)),\n  Size\
        \ = M * N,\n  Shift = K rem Size,\n  Flat = lists:flatten(Grid),\n  Rotated\
        \ = if \n    Shift == 0 -> Flat;\n    true ->\n      {Prefix, Suffix} = lists:split(Size\
        \ - Shift, Flat),\n      Suffix ++ Prefix\n  end,\n  chunk(Rotated, N).\n\n\
        chunk([], _) -> [];\nchunk(List, N) ->\n  {Chunk, Rest} = lists:split(N, List),\n\
        \  [Chunk | chunk(Rest, N)]."
      elixir: "defmodule Solution do\n  @spec shift_grid(grid :: [[integer]], k :: integer)\
        \ :: [[integer]]\n  def shift_grid(grid, k) do\n    m = length(grid)\n    n\
        \ = length(hd(grid))\n    size = m * n\n    shift = rem(k, size)\n    if shift\
        \ == 0 do\n      grid\n    else\n      flat = List.flatten(grid)\n      {prefix,\
        \ suffix} = Enum.split(flat, size - shift)\n      (suffix ++ prefix)\n     \
        \ |> Enum.chunk_every(n)\n    end\n  end\nend"
    approach: 'To solve this problem, we conceptually flatten the 2D grid into a 1D
      array of size $m \times n$. In this 1D representation, shifting the grid $k$ times
      is equivalent to a cyclic shift where every element moves forward by $k$ positions.
      An element at row $i$ and column $j$ in the original grid corresponds to index
      $i \times n + j$ in the 1D representation. After shifting, its new 1D index is
      $(i \times n + j + k) \pmod{m \times n}$.


      To implement this efficiently, we calculate the new position for each element
      directly using the modulo and division operators. Given the new 1D index $new\_idx$,
      the corresponding 2D coordinates are row $new\_idx / n$ and column $new\_idx \pmod
      n$. We iterate through the original grid, calculate these new coordinates for
      each value, and populate a result grid with the shifted values. This approach
      ensures we handle the row-to-row and bottom-to-top wraps naturally.'
    time_complexity: O(m \times n). The algorithm performs a single pass over all elements
      in the $m \times n$ grid to calculate their new positions and place them in the
      result structure. Each calculation (multiplication, addition, and modulo) takes
      constant time.
    space_complexity: O(m \times n). We allocate a new 2D structure of the same size
      as the input to store the shifted result. Excluding the space required for the
      output, the auxiliary space used for index calculations is $O(1)$.
    elapsed_time: 105.75404691696167
    model: gemini-3-flash-preview
    generated_at: '2026-07-20 03:09:15 '
---

## Problem #1260: Shift 2D Grid

**Difficulty:** Easy

**Topics:** Array, Matrix, Simulation

## Problem Description

<p>Given a 2D <code>grid</code> of size <code>m x n</code>&nbsp;and an integer <code>k</code>. You need to shift the <code>grid</code>&nbsp;<code>k</code> times.</p>

<p>In one shift operation:</p>

<ul>
	<li>Element at <code>grid[i][j]</code> moves to <code>grid[i][j + 1]</code>.</li>
	<li>Element at <code>grid[i][n - 1]</code> moves to <code>grid[i + 1][0]</code>.</li>
	<li>Element at <code>grid[m&nbsp;- 1][n - 1]</code> moves to <code>grid[0][0]</code>.</li>
</ul>

<p>Return the <em>2D grid</em> after applying shift operation <code>k</code> times.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/11/05/e1.png" style="width: 400px; height: 178px;" />
<pre>
<strong>Input:</strong> <code>grid</code> = [[1,2,3],[4,5,6],[7,8,9]], k = 1
<strong>Output:</strong> [[9,1,2],[3,4,5],[6,7,8]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/11/05/e2.png" style="width: 400px; height: 166px;" />
<pre>
<strong>Input:</strong> <code>grid</code> = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
<strong>Output:</strong> [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> <code>grid</code> = [[1,2,3],[4,5,6],[7,8,9]], k = 9
<strong>Output:</strong> [[1,2,3],[4,5,6],[7,8,9]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m ==&nbsp;grid.length</code></li>
	<li><code>n ==&nbsp;grid[i].length</code></li>
	<li><code>1 &lt;= m &lt;= 50</code></li>
	<li><code>1 &lt;= n &lt;= 50</code></li>
	<li><code>-1000 &lt;= grid[i][j] &lt;= 1000</code></li>
	<li><code>0 &lt;= k &lt;= 100</code></li>
</ul>


## Hints

1. Simulate step by step. move grid[i][j] to grid[i][j+1]. handle last column of the grid.

2. Put the matrix row by row to a vector. take k % vector.length and move last k of the vector to the beginning. put the vector to the matrix back the same way.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem, we conceptually flatten the 2D grid into a 1D array of size $m \times n$. In this 1D representation, shifting the grid $k$ times is equivalent to a cyclic shift where every element moves forward by $k$ positions. An element at row $i$ and column $j$ in the original grid corresponds to index $i \times n + j$ in the 1D representation. After shifting, its new 1D index is $(i \times n + j + k) \pmod{m \times n}$.

To implement this efficiently, we calculate the new position for each element directly using the modulo and division operators. Given the new 1D index $new\_idx$, the corresponding 2D coordinates are row $new\_idx / n$ and column $new\_idx \pmod n$. We iterate through the original grid, calculate these new coordinates for each value, and populate a result grid with the shifted values. This approach ensures we handle the row-to-row and bottom-to-top wraps naturally.

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
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        int total = m * n;
        k %= total;
        vector<vector<int>> res(m, vector<int>(n));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int oldIdx = i * n + j;
                int newIdx = (oldIdx + k) % total;
                res[newIdx / n][newIdx % n] = grid[i][j];
            }
        }
        return res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int total = m * n;
        k %= total;
        int[][] temp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int index = (i * n + j + k) % total;
                temp[index / n][index % n] = grid[i][j];
            }
        }
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                row.add(temp[i][j]);
            }
            result.add(row);
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
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        total = m * n
        k %= total
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                old_idx = i * n + j
                new_idx = (old_idx + k) % total
                res[new_idx // n][new_idx % n] = grid[i][j]
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                old_idx = i * n + j
                new_idx = (old_idx + k) % total
                res[new_idx // n][new_idx % n] = grid[i][j]
        return res
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
int** shiftGrid(int** grid, int gridSize, int* gridColSize, int k, int* returnSize, int** returnColumnSizes) {
    int m = gridSize;
    int n = gridColSize[0];
    int total = m * n;
    k %= total;
    int** res = (int**)malloc(m * sizeof(int*));
    *returnColumnSizes = (int*)malloc(m * sizeof(int));
    *returnSize = m;
    for (int i = 0; i < m; i++) {
        res[i] = (int*)malloc(n * sizeof(int));
        (*returnColumnSizes)[i] = n;
    }
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int oldIdx = i * n + j;
            int newIdx = (oldIdx + k) % total;
            res[newIdx / n][newIdx % n] = grid[i][j];
        }
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public IList<IList<int>> ShiftGrid(int[][] grid, int k) {
        int m = grid.Length;
        int n = grid[0].Length;
        int total = m * n;
        k %= total;
        int[][] temp = new int[m][];
        for (int i = 0; i < m; i++) {
            temp[i] = new int[n];
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int index = (i * n + j + k) % total;
                temp[index / n][index % n] = grid[i][j];
            }
        }
        IList<IList<int>> result = new List<IList<int>>();
        for (int i = 0; i < m; i++) {
            result.Add(new List<int>(temp[i]));
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
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 */
var shiftGrid = function(grid, k) {
    const m = grid.length;
    const n = grid[0].length;
    const total = m * n;
    k %= total;
    const res = Array.from({ length: m }, () => Array(n).fill(0));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            let oldIdx = i * n + j;
            let newIdx = (oldIdx + k) % total;
            res[Math.floor(newIdx / n)][newIdx % n] = grid[i][j];
        }
    }
    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function shiftGrid(grid: number[][], k: number): number[][] {
    const m = grid.length;
    const n = grid[0].length;
    const total = m * n;
    const shift = k % total;
    const result: number[][] = Array.from({ length: m }, () => new Array(n).fill(0));

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const flatIdx = (i * n + j + shift) % total;
            const newR = Math.floor(flatIdx / n);
            const newC = flatIdx % n;
            result[newR][newC] = grid[i][j];
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
     * @param Integer[][] $grid
     * @param Integer $k
     * @return Integer[][]
     */
    function shiftGrid($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $total = $m * $n;
        $shift = $k % $total;
        $result = [];
        for ($i = 0; $i < $m; $i++) {
            $result[$i] = array_fill(0, $n, 0);
        }

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $flatIdx = ($i * $n + $j + $shift) % $total;
                $newR = (int)($flatIdx / $n);
                $newC = $flatIdx % $n;
                $result[$newR][$newC] = $grid[$i][$j];
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
    func shiftGrid(_ grid: [[Int]], _ k: Int) -> [[Int]] {
        let m = grid.count
        let n = grid[0].count
        let total = m * n
        let shift = k % total
        var result = Array(repeating: Array(repeating: 0, count: n), count: m)

        for i in 0..<m {
            for j in 0..<n {
                let flatIdx = (i * n + j + shift) % total
                let newR = flatIdx / n
                let newC = flatIdx % n
                result[newR][newC] = grid[i][j]
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
    fun shiftGrid(grid: Array<IntArray>, k: Int): List<List<Int>> {
        val m = grid.size
        val n = grid[0].size
        val total = m * n
        val shift = k % total
        val result = Array(m) { IntArray(n) }

        for (i in 0 until m) {
            for (j in 0 until n) {
                val flatIdx = (i * n + j + shift) % total
                val newR = flatIdx / n
                val newC = flatIdx % n
                result[newR][newC] = grid[i][j]
            }
        }

        return result.map { it.toList() }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<List<int>> shiftGrid(List<List<int>> grid, int k) {
    int m = grid.length;
    int n = grid[0].length;
    int total = m * n;
    int shift = k % total;
    List<List<int>> result = List.generate(m, (_) => List<int>.filled(n, 0));

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        int flatIdx = (i * n + j + shift) % total;
        int newR = flatIdx ~/ n;
        int newC = flatIdx % n;
        result[newR][newC] = grid[i][j];
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
func shiftGrid(grid [][]int, k int) [][]int {
    m := len(grid)
    n := len(grid[0])
    total := m * n
    shift := k % total

    result := make([][]int, m)
    for i := range result {
        result[i] = make([]int, n)
    }

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            flatIdx := (i*n + j + shift) % total
            newR := flatIdx / n
            newC := flatIdx % n
            result[newR][newC] = grid[i][j]
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
def shift_grid(grid, k)
  m = grid.length
  n = grid[0].length
  size = m * n
  k %= size
  return grid if k == 0

  flat = grid.flatten
  rotated = flat.rotate(-k)
  rotated.each_slice(n).to_a
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def shiftGrid(grid: Array[Array[Int]], k: Int): List[List[Int]] = {
        val m = grid.length
        val n = grid(0).length
        val size = m * n
        val s = k % size
        val flat = grid.flatten
        val result = new Array[Int](size)

        for (i <- 0 until size) {
            result((i + s) % size) = flat(i)
        }

        result.grouped(n).map(_.toList).toList
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn shift_grid(grid: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let size = m * n;
        let k = (k as usize) % size;

        if k == 0 {
            return grid;
        }

        let mut flat: Vec<i32> = grid.into_iter().flatten().collect();
        flat.rotate_right(k);

        flat.chunks(n)
            .map(|chunk| chunk.to_vec())
            .collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (shift-grid grid k)
  (-> (listof (listof exact-integer?)) exact-integer? (listof (listof exact-integer?)))
  (let* ([m (length grid)]
         [n (length (car grid))]
         [size (* m n)]
         [s (modulo k size)])
    (if (zero? s)
        grid
        (let* ([flat (flatten grid)]
               [pos (- size s)]
               [prefix (take flat pos)]
               [suffix (drop flat pos)]
               [rotated (append suffix prefix)])
          (let loop ([lst rotated])
            (if (null? lst)
                '()
                (cons (take lst n) (loop (drop lst n)))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec shift_grid(Grid :: [[integer()]], K :: integer()) -> [[integer()]].
shift_grid(Grid, K) ->
  M = length(Grid),
  N = length(hd(Grid)),
  Size = M * N,
  Shift = K rem Size,
  Flat = lists:flatten(Grid),
  Rotated = if 
    Shift == 0 -> Flat;
    true ->
      {Prefix, Suffix} = lists:split(Size - Shift, Flat),
      Suffix ++ Prefix
  end,
  chunk(Rotated, N).

chunk([], _) -> [];
chunk(List, N) ->
  {Chunk, Rest} = lists:split(N, List),
  [Chunk | chunk(Rest, N)].
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec shift_grid(grid :: [[integer]], k :: integer) :: [[integer]]
  def shift_grid(grid, k) do
    m = length(grid)
    n = length(hd(grid))
    size = m * n
    shift = rem(k, size)
    if shift == 0 do
      grid
    else
      flat = List.flatten(grid)
      {prefix, suffix} = Enum.split(flat, size - shift)
      (suffix ++ prefix)
      |> Enum.chunk_every(n)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m \times n). The algorithm performs a single pass over all elements in the $m \times n$ grid to calculate their new positions and place them in the result structure. Each calculation (multiplication, addition, and modulo) takes constant time.
- **Space Complexity:** O(m \times n). We allocate a new 2D structure of the same size as the input to store the shifted result. Excluding the space required for the output, the auxiliary space used for index calculations is $O(1)$.
