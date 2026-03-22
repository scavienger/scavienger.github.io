---
layout: post
title: "Determine Whether Matrix Can Be Obtained By Rotation"
date: 2026-03-22 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Matrix"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool findRotation(vector<vector<int>>& mat,\
        \ vector<vector<int>>& target) {\n        int n = mat.size();\n        for (int\
        \ r = 0; r < 4; ++r) {\n            if (mat == target) return true;\n\n    \
        \        for (int i = 0; i < n; ++i) {\n                for (int j = i + 1;\
        \ j < n; ++j) {\n                    swap(mat[i][j], mat[j][i]);\n         \
        \       }\n            }\n            for (int i = 0; i < n; ++i) {\n      \
        \          for (int j = 0; j < n / 2; ++j) {\n                    swap(mat[i][j],\
        \ mat[i][n - 1 - j]);\n                }\n            }\n        }\n       \
        \ return false;\n    }\n};"
      java: "class Solution {\n    public boolean findRotation(int[][] mat, int[][]\
        \ target) {\n        int n = mat.length;\n        for (int r = 0; r < 4; r++)\
        \ {\n            if (isEqual(mat, target)) return true;\n            rotate(mat);\n\
        \        }\n        return false;\n    }\n\n    private void rotate(int[][]\
        \ mat) {\n        int n = mat.length;\n        for (int i = 0; i < n; i++) {\n\
        \            for (int j = i + 1; j < n; j++) {\n                int temp = mat[i][j];\n\
        \                mat[i][j] = mat[j][i];\n                mat[j][i] = temp;\n\
        \            }\n        }\n        for (int i = 0; i < n; i++) {\n         \
        \   for (int j = 0; j < n / 2; j++) {\n                int temp = mat[i][j];\n\
        \                mat[i][j] = mat[i][n - 1 - j];\n                mat[i][n -\
        \ 1 - j] = temp;\n            }\n        }\n    }\n\n    private boolean isEqual(int[][]\
        \ m1, int[][] m2) {\n        for (int i = 0; i < m1.length; i++) {\n       \
        \     for (int j = 0; j < m1[0].length; j++) {\n                if (m1[i][j]\
        \ != m2[i][j]) return false;\n            }\n        }\n        return true;\n\
        \    }\n}"
      python: "class Solution(object):\n    def findRotation(self, mat, target):\n \
        \       \"\"\"\n        :type mat: List[List[int]]\n        :type target: List[List[int]]\n\
        \        :rtype: bool\n        \"\"\"\n        for _ in range(4):\n        \
        \    if mat == target:\n                return True\n            mat = [list(row)\
        \ for row in zip(*mat[::-1])]\n        return False"
      python3: "class Solution:\n    def findRotation(self, mat: List[List[int]], target:\
        \ List[List[int]]) -> bool:\n        for _ in range(4):\n            if mat\
        \ == target:\n                return True\n            mat = [list(row) for\
        \ row in zip(*mat[::-1])]\n        return False"
      c: "bool findRotation(int** mat, int matSize, int* matColSize, int** target, int\
        \ targetSize, int* targetColSize) {\n    int n = matSize;\n    for (int r =\
        \ 0; r < 4; r++) {\n        bool same = true;\n        for (int i = 0; i < n;\
        \ i++) {\n            for (int j = 0; j < n; j++) {\n                if (mat[i][j]\
        \ != target[i][j]) {\n                    same = false;\n                  \
        \  break;\n                }\n            }\n            if (!same) break;\n\
        \        }\n        if (same) return true;\n\n        for (int i = 0; i < n;\
        \ i++) {\n            for (int j = i + 1; j < n; j++) {\n                int\
        \ tmp = mat[i][j];\n                mat[i][j] = mat[j][i];\n               \
        \ mat[j][i] = tmp;\n            }\n        }\n        for (int i = 0; i < n;\
        \ i++) {\n            for (int j = 0; j < n / 2; j++) {\n                int\
        \ tmp = mat[i][j];\n                mat[i][j] = mat[i][n - 1 - j];\n       \
        \         mat[i][n - 1 - j] = tmp;\n            }\n        }\n    }\n    return\
        \ false;\n}"
      csharp: "public class Solution {\n    public bool FindRotation(int[][] mat, int[][]\
        \ target) {\n        int n = mat.Length;\n        for (int r = 0; r < 4; r++)\
        \ {\n            if (IsEqual(mat, target)) return true;\n            Rotate(mat);\n\
        \        }\n        return false;\n    }\n\n    private void Rotate(int[][]\
        \ mat) {\n        int n = mat.Length;\n        for (int i = 0; i < n; i++) {\n\
        \            for (int j = i + 1; j < n; j++) {\n                int temp = mat[i][j];\n\
        \                mat[i][j] = mat[j][i];\n                mat[j][i] = temp;\n\
        \            }\n        }\n        for (int i = 0; i < n; i++) {\n         \
        \   for (int j = 0; j < n / 2; j++) {\n                int temp = mat[i][j];\n\
        \                mat[i][j] = mat[i][n - 1 - j];\n                mat[i][n -\
        \ 1 - j] = temp;\n            }\n        }\n    }\n\n    private bool IsEqual(int[][]\
        \ m1, int[][] m2) {\n        for (int i = 0; i < m1.Length; i++) {\n       \
        \     for (int j = 0; j < m1[0].Length; j++) {\n                if (m1[i][j]\
        \ != m2[i][j]) return false;\n            }\n        }\n        return true;\n\
        \    }\n}"
      javascript: "/**\n * @param {number[][]} mat\n * @param {number[][]} target\n\
        \ * @return {boolean}\n */\nvar findRotation = function(mat, target) {\n   \
        \ const n = mat.length;\n    const isEqual = (m1, m2) => {\n        for (let\
        \ i = 0; i < n; i++) {\n            for (let j = 0; j < n; j++) {\n        \
        \        if (m1[i][j] !== m2[i][j]) return false;\n            }\n        }\n\
        \        return true;\n    };\n    const rotate = (m) => {\n        for (let\
        \ i = 0; i < n; i++) {\n            for (let j = i + 1; j < n; j++) {\n    \
        \            [m[i][j], m[j][i]] = [m[j][i], m[i][j]];\n            }\n     \
        \   }\n        for (let i = 0; i < n; i++) {\n            m[i].reverse();\n\
        \        }\n    };\n    for (let r = 0; r < 4; r++) {\n        if (isEqual(mat,\
        \ target)) return true;\n        rotate(mat);\n    }\n    return false;\n};"
      typescript: "function findRotation(mat: number[][], target: number[][]): boolean\
        \ {\n    const n = mat.length;\n    const rot = [true, true, true, true];\n\
        \    for (let i = 0; i < n; i++) {\n        for (let j = 0; j < n; j++) {\n\
        \            if (mat[i][j] !== target[i][j]) rot[0] = false;\n            if\
        \ (mat[i][j] !== target[j][n - 1 - i]) rot[1] = false;\n            if (mat[i][j]\
        \ !== target[n - 1 - i][n - 1 - j]) rot[2] = false;\n            if (mat[i][j]\
        \ !== target[n - 1 - j][i]) rot[3] = false;\n        }\n    }\n    return rot[0]\
        \ || rot[1] || rot[2] || rot[3];\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $mat\n     * @param\
        \ Integer[][] $target\n     * @return Boolean\n     */\n    function findRotation($mat,\
        \ $target) {\n        $n = count($mat);\n        $rot = [true, true, true, true];\n\
        \        for ($i = 0; $i < $n; $i++) {\n            for ($j = 0; $j < $n; $j++)\
        \ {\n                if ($mat[$i][$j] !== $target[$i][$j]) $rot[0] = false;\n\
        \                if ($mat[$i][$j] !== $target[$j][$n - 1 - $i]) $rot[1] = false;\n\
        \                if ($mat[$i][$j] !== $target[$n - 1 - $i][$n - 1 - $j]) $rot[2]\
        \ = false;\n                if ($mat[$i][$j] !== $target[$n - 1 - $j][$i]) $rot[3]\
        \ = false;\n            }\n        }\n        return $rot[0] || $rot[1] || $rot[2]\
        \ || $rot[3];\n    }\n}"
      swift: "class Solution {\n    func findRotation(_ mat: [[Int]], _ target: [[Int]])\
        \ -> Bool {\n        let n = mat.count\n        var rot = [true, true, true,\
        \ true]\n        for i in 0..<n {\n            for j in 0..<n {\n          \
        \      if mat[i][j] != target[i][j] { rot[0] = false }\n                if mat[i][j]\
        \ != target[j][n - 1 - i] { rot[1] = false }\n                if mat[i][j] !=\
        \ target[n - 1 - i][n - 1 - j] { rot[2] = false }\n                if mat[i][j]\
        \ != target[n - 1 - j][i] { rot[3] = false }\n            }\n        }\n   \
        \     return rot[0] || rot[1] || rot[2] || rot[3]\n    }\n}"
      kotlin: "class Solution {\n    fun findRotation(mat: Array<IntArray>, target:\
        \ Array<IntArray>): Boolean {\n        val n = mat.size\n        val rot = booleanArrayOf(true,\
        \ true, true, true)\n        for (i in 0 until n) {\n            for (j in 0\
        \ until n) {\n                if (mat[i][j] != target[i][j]) rot[0] = false\n\
        \                if (mat[i][j] != target[j][n - 1 - i]) rot[1] = false\n   \
        \             if (mat[i][j] != target[n - 1 - i][n - 1 - j]) rot[2] = false\n\
        \                if (mat[i][j] != target[n - 1 - j][i]) rot[3] = false\n   \
        \         }\n        }\n        return rot[0] || rot[1] || rot[2] || rot[3]\n\
        \    }\n}"
      dart: "class Solution {\n  bool findRotation(List<List<int>> mat, List<List<int>>\
        \ target) {\n    int n = mat.length;\n    List<bool> rot = [true, true, true,\
        \ true];\n    for (int i = 0; i < n; i++) {\n      for (int j = 0; j < n; j++)\
        \ {\n        if (mat[i][j] != target[i][j]) rot[0] = false;\n        if (mat[i][j]\
        \ != target[j][n - 1 - i]) rot[1] = false;\n        if (mat[i][j] != target[n\
        \ - 1 - i][n - 1 - j]) rot[2] = false;\n        if (mat[i][j] != target[n -\
        \ 1 - j][i]) rot[3] = false;\n      }\n    }\n    return rot[0] || rot[1] ||\
        \ rot[2] || rot[3];\n  }\n}"
      go: "func findRotation(mat [][]int, target [][]int) bool {\n    n := len(mat)\n\
        \    rot := [4]bool{true, true, true, true}\n    for i := 0; i < n; i++ {\n\
        \        for j := 0; j < n; j++ {\n            if mat[i][j] != target[i][j]\
        \ {\n                rot[0] = false\n            }\n            if mat[i][j]\
        \ != target[j][n-1-i] {\n                rot[1] = false\n            }\n   \
        \         if mat[i][j] != target[n-1-i][n-1-j] {\n                rot[2] = false\n\
        \            }\n            if mat[i][j] != target[n-1-j][i] {\n           \
        \     rot[3] = false\n            }\n        }\n    }\n    return rot[0] ||\
        \ rot[1] || rot[2] || rot[3]\n}"
      ruby: "def find_rotation(mat, target)\n  4.times do\n    return true if mat ==\
        \ target\n    n = mat.length\n    new_mat = Array.new(n) { Array.new(n) }\n\
        \    (0...n).each do |i|\n      (0...n).each do |j|\n        new_mat[j][n -\
        \ 1 - i] = mat[i][j]\n      end\n    end\n    mat = new_mat\n  end\n  false\n\
        end"
      scala: "object Solution {\n  def findRotation(mat: Array[Array[Int]], target:\
        \ Array[Array[Int]]): Boolean = {\n    val targetSeq = target.map(_.toSeq).toSeq\n\
        \    var curr = mat\n    for (_ <- 0 until 4) {\n      if (curr.map(_.toSeq).toSeq\
        \ == targetSeq) return true\n      val n = curr.length\n      val next = Array.ofDim[Int](n,\
        \ n)\n      for (i <- 0 until n; j <- 0 until n) {\n        next(j)(n - 1 -\
        \ i) = curr(i)(j)\n      }\n      curr = next\n    }\n    false\n  }\n}"
      rust: "impl Solution {\n    pub fn find_rotation(mat: Vec<Vec<i32>>, target: Vec<Vec<i32>>)\
        \ -> bool {\n        let mut curr = mat;\n        for _ in 0..4 {\n        \
        \    if curr == target {\n                return true;\n            }\n    \
        \        let n = curr.len();\n            let mut next = vec![vec![0; n]; n];\n\
        \            for i in 0..n {\n                for j in 0..n {\n            \
        \        next[j][n - 1 - i] = curr[i][j];\n                }\n            }\n\
        \            curr = next;\n        }\n        false\n    }\n}"
      racket: "(define/contract (find-rotation mat target)\n  (-> (listof (listof exact-integer?))\
        \ (listof (listof exact-integer?)) boolean?)\n  (define (rotate m)\n    (let\
        \ ([n (length m)])\n      (for/list ([j (in-range n)])\n        (for/list ([i\
        \ (in-range (- n 1) -1 -1)])\n          (list-ref (list-ref m i) j)))))\n  (let\
        \ loop ([curr mat] [k 0])\n    (cond\n      [(= k 4) #f]\n      [(equal? curr\
        \ target) #t]\n      [else (loop (rotate curr) (+ k 1))])))"
      erlang: "-spec find_rotation(Mat :: [[integer()]], Target :: [[integer()]]) ->\
        \ boolean().\nfind_rotation(Mat, Target) ->\n  check_all(Mat, Target, 4).\n\n\
        check_all(_Mat, _Target, 0) -> false;\ncheck_all(Mat, Target, Count) ->\n  case\
        \ Mat =:= Target of\n    true -> true;\n    false -> check_all(rotate(Mat),\
        \ Target, Count - 1)\n  end.\n\nrotate(Mat) ->\n  N = length(Mat),\n  [[lists:nth(I,\
        \ Row) || Row <- lists:reverse(Mat)] || I <- lists:seq(1, N)]."
      elixir: "defmodule Solution do\n  @spec find_rotation(mat :: [[integer]], target\
        \ :: [[integer]]) :: boolean\n  def find_rotation(mat, target) do\n    do_find(mat,\
        \ target, 4)\n  end\n\n  defp do_find(_mat, _target, 0), do: false\n  defp do_find(mat,\
        \ target, count) do\n    if mat == target do\n      true\n    else\n      do_find(rotate(mat),\
        \ target, count - 1)\n    end\n  end\n\n  defp rotate(mat) do\n    mat\n   \
        \ |> Enum.reverse()\n    |> Enum.zip()\n    |> Enum.map(&Tuple.to_list/1)\n\
        \  end\nend"
    approach: 'To determine if the matrix ''mat'' can be transformed into ''target''
      through rotations, we iteratively apply a 90-degree clockwise rotation and compare
      the resulting matrix with ''target''. A total of four possible orientations exist:
      0, 90, 180, and 270 degrees. Rotation by 360 degrees returns the matrix to its
      original state, so we only need to check these four configurations.


      The 90-degree clockwise rotation is efficiently implemented in-place by first
      transposing the matrix (swapping elements mat[i][j] and mat[j][i]) and then reversing
      the elements in each row (swapping mat[i][j] and mat[i][n-1-j]). If any of these
      four states match the target matrix element-by-element, the function returns true.
      If no match is found after all rotations, it returns false.'
    time_complexity: O(n^2). We perform a maximum of four rotations and four comparisons.
      Each check and each rotation requires visiting every element in the n x n matrix,
      leading to a complexity of 4 * (n^2 + n^2), which simplifies to O(n^2).
    space_complexity: O(1). The algorithm performs rotations in-place using a single
      temporary variable for swaps. While some high-level language features (like Python's
      zip) might create temporary copies, the algorithm can be fully implemented using
      only constant auxiliary space.
    elapsed_time: 94.80729603767395
    model: gemini-3-flash-preview
    generated_at: '2026-03-22 01:29:38 '
---

## Problem #1886: Determine Whether Matrix Can Be Obtained By Rotation

**Difficulty:** Easy

**Topics:** Array, Matrix

## Problem Description

<p>Given two <code>n x n</code> binary matrices <code>mat</code> and <code>target</code>, return <code>true</code><em> if it is possible to make </em><code>mat</code><em> equal to </em><code>target</code><em> by <strong>rotating</strong> </em><code>mat</code><em> in <strong>90-degree increments</strong>, or </em><code>false</code><em> otherwise.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/20/grid3.png" style="width: 301px; height: 121px;" />
<pre>
<strong>Input:</strong> mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
<strong>Output:</strong> true
<strong>Explanation: </strong>We can rotate mat 90 degrees clockwise to make mat equal target.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/20/grid4.png" style="width: 301px; height: 121px;" />
<pre>
<strong>Input:</strong> mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to make mat equal to target by rotating mat.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/26/grid4.png" style="width: 661px; height: 184px;" />
<pre>
<strong>Input:</strong> mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
<strong>Output:</strong> true
<strong>Explanation: </strong>We can rotate mat 90 degrees clockwise two times to make mat equal target.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == mat.length == target.length</code></li>
	<li><code>n == mat[i].length == target[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 10</code></li>
	<li><code>mat[i][j]</code> and <code>target[i][j]</code> are either <code>0</code> or <code>1</code>.</li>
</ul>


## Hints

1. What is the maximum number of rotations you have to check?

2. Is there a formula you can use to rotate a matrix 90 degrees?

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To determine if the matrix 'mat' can be transformed into 'target' through rotations, we iteratively apply a 90-degree clockwise rotation and compare the resulting matrix with 'target'. A total of four possible orientations exist: 0, 90, 180, and 270 degrees. Rotation by 360 degrees returns the matrix to its original state, so we only need to check these four configurations.

The 90-degree clockwise rotation is efficiently implemented in-place by first transposing the matrix (swapping elements mat[i][j] and mat[j][i]) and then reversing the elements in each row (swapping mat[i][j] and mat[i][n-1-j]). If any of these four states match the target matrix element-by-element, the function returns true. If no match is found after all rotations, it returns false.

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
    bool findRotation(vector<vector<int>>& mat, vector<vector<int>>& target) {
        int n = mat.size();
        for (int r = 0; r < 4; ++r) {
            if (mat == target) return true;

            for (int i = 0; i < n; ++i) {
                for (int j = i + 1; j < n; ++j) {
                    swap(mat[i][j], mat[j][i]);
                }
            }
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n / 2; ++j) {
                    swap(mat[i][j], mat[i][n - 1 - j]);
                }
            }
        }
        return false;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean findRotation(int[][] mat, int[][] target) {
        int n = mat.length;
        for (int r = 0; r < 4; r++) {
            if (isEqual(mat, target)) return true;
            rotate(mat);
        }
        return false;
    }

    private void rotate(int[][] mat) {
        int n = mat.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = mat[i][j];
                mat[i][j] = mat[j][i];
                mat[j][i] = temp;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n / 2; j++) {
                int temp = mat[i][j];
                mat[i][j] = mat[i][n - 1 - j];
                mat[i][n - 1 - j] = temp;
            }
        }
    }

    private boolean isEqual(int[][] m1, int[][] m2) {
        for (int i = 0; i < m1.length; i++) {
            for (int j = 0; j < m1[0].length; j++) {
                if (m1[i][j] != m2[i][j]) return false;
            }
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        for _ in range(4):
            if mat == target:
                return True
            mat = [list(row) for row in zip(*mat[::-1])]
        return False
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            mat = [list(row) for row in zip(*mat[::-1])]
        return False
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool findRotation(int** mat, int matSize, int* matColSize, int** target, int targetSize, int* targetColSize) {
    int n = matSize;
    for (int r = 0; r < 4; r++) {
        bool same = true;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] != target[i][j]) {
                    same = false;
                    break;
                }
            }
            if (!same) break;
        }
        if (same) return true;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int tmp = mat[i][j];
                mat[i][j] = mat[j][i];
                mat[j][i] = tmp;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n / 2; j++) {
                int tmp = mat[i][j];
                mat[i][j] = mat[i][n - 1 - j];
                mat[i][n - 1 - j] = tmp;
            }
        }
    }
    return false;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool FindRotation(int[][] mat, int[][] target) {
        int n = mat.Length;
        for (int r = 0; r < 4; r++) {
            if (IsEqual(mat, target)) return true;
            Rotate(mat);
        }
        return false;
    }

    private void Rotate(int[][] mat) {
        int n = mat.Length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = mat[i][j];
                mat[i][j] = mat[j][i];
                mat[j][i] = temp;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n / 2; j++) {
                int temp = mat[i][j];
                mat[i][j] = mat[i][n - 1 - j];
                mat[i][n - 1 - j] = temp;
            }
        }
    }

    private bool IsEqual(int[][] m1, int[][] m2) {
        for (int i = 0; i < m1.Length; i++) {
            for (int j = 0; j < m1[0].Length; j++) {
                if (m1[i][j] != m2[i][j]) return false;
            }
        }
        return true;
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
 * @param {number[][]} target
 * @return {boolean}
 */
var findRotation = function(mat, target) {
    const n = mat.length;
    const isEqual = (m1, m2) => {
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                if (m1[i][j] !== m2[i][j]) return false;
            }
        }
        return true;
    };
    const rotate = (m) => {
        for (let i = 0; i < n; i++) {
            for (let j = i + 1; j < n; j++) {
                [m[i][j], m[j][i]] = [m[j][i], m[i][j]];
            }
        }
        for (let i = 0; i < n; i++) {
            m[i].reverse();
        }
    };
    for (let r = 0; r < 4; r++) {
        if (isEqual(mat, target)) return true;
        rotate(mat);
    }
    return false;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findRotation(mat: number[][], target: number[][]): boolean {
    const n = mat.length;
    const rot = [true, true, true, true];
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (mat[i][j] !== target[i][j]) rot[0] = false;
            if (mat[i][j] !== target[j][n - 1 - i]) rot[1] = false;
            if (mat[i][j] !== target[n - 1 - i][n - 1 - j]) rot[2] = false;
            if (mat[i][j] !== target[n - 1 - j][i]) rot[3] = false;
        }
    }
    return rot[0] || rot[1] || rot[2] || rot[3];
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
     * @param Integer[][] $target
     * @return Boolean
     */
    function findRotation($mat, $target) {
        $n = count($mat);
        $rot = [true, true, true, true];
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($mat[$i][$j] !== $target[$i][$j]) $rot[0] = false;
                if ($mat[$i][$j] !== $target[$j][$n - 1 - $i]) $rot[1] = false;
                if ($mat[$i][$j] !== $target[$n - 1 - $i][$n - 1 - $j]) $rot[2] = false;
                if ($mat[$i][$j] !== $target[$n - 1 - $j][$i]) $rot[3] = false;
            }
        }
        return $rot[0] || $rot[1] || $rot[2] || $rot[3];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func findRotation(_ mat: [[Int]], _ target: [[Int]]) -> Bool {
        let n = mat.count
        var rot = [true, true, true, true]
        for i in 0..<n {
            for j in 0..<n {
                if mat[i][j] != target[i][j] { rot[0] = false }
                if mat[i][j] != target[j][n - 1 - i] { rot[1] = false }
                if mat[i][j] != target[n - 1 - i][n - 1 - j] { rot[2] = false }
                if mat[i][j] != target[n - 1 - j][i] { rot[3] = false }
            }
        }
        return rot[0] || rot[1] || rot[2] || rot[3]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun findRotation(mat: Array<IntArray>, target: Array<IntArray>): Boolean {
        val n = mat.size
        val rot = booleanArrayOf(true, true, true, true)
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (mat[i][j] != target[i][j]) rot[0] = false
                if (mat[i][j] != target[j][n - 1 - i]) rot[1] = false
                if (mat[i][j] != target[n - 1 - i][n - 1 - j]) rot[2] = false
                if (mat[i][j] != target[n - 1 - j][i]) rot[3] = false
            }
        }
        return rot[0] || rot[1] || rot[2] || rot[3]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool findRotation(List<List<int>> mat, List<List<int>> target) {
    int n = mat.length;
    List<bool> rot = [true, true, true, true];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (mat[i][j] != target[i][j]) rot[0] = false;
        if (mat[i][j] != target[j][n - 1 - i]) rot[1] = false;
        if (mat[i][j] != target[n - 1 - i][n - 1 - j]) rot[2] = false;
        if (mat[i][j] != target[n - 1 - j][i]) rot[3] = false;
      }
    }
    return rot[0] || rot[1] || rot[2] || rot[3];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func findRotation(mat [][]int, target [][]int) bool {
    n := len(mat)
    rot := [4]bool{true, true, true, true}
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            if mat[i][j] != target[i][j] {
                rot[0] = false
            }
            if mat[i][j] != target[j][n-1-i] {
                rot[1] = false
            }
            if mat[i][j] != target[n-1-i][n-1-j] {
                rot[2] = false
            }
            if mat[i][j] != target[n-1-j][i] {
                rot[3] = false
            }
        }
    }
    return rot[0] || rot[1] || rot[2] || rot[3]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def find_rotation(mat, target)
  4.times do
    return true if mat == target
    n = mat.length
    new_mat = Array.new(n) { Array.new(n) }
    (0...n).each do |i|
      (0...n).each do |j|
        new_mat[j][n - 1 - i] = mat[i][j]
      end
    end
    mat = new_mat
  end
  false
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def findRotation(mat: Array[Array[Int]], target: Array[Array[Int]]): Boolean = {
    val targetSeq = target.map(_.toSeq).toSeq
    var curr = mat
    for (_ <- 0 until 4) {
      if (curr.map(_.toSeq).toSeq == targetSeq) return true
      val n = curr.length
      val next = Array.ofDim[Int](n, n)
      for (i <- 0 until n; j <- 0 until n) {
        next(j)(n - 1 - i) = curr(i)(j)
      }
      curr = next
    }
    false
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn find_rotation(mat: Vec<Vec<i32>>, target: Vec<Vec<i32>>) -> bool {
        let mut curr = mat;
        for _ in 0..4 {
            if curr == target {
                return true;
            }
            let n = curr.len();
            let mut next = vec![vec![0; n]; n];
            for i in 0..n {
                for j in 0..n {
                    next[j][n - 1 - i] = curr[i][j];
                }
            }
            curr = next;
        }
        false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (find-rotation mat target)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) boolean?)
  (define (rotate m)
    (let ([n (length m)])
      (for/list ([j (in-range n)])
        (for/list ([i (in-range (- n 1) -1 -1)])
          (list-ref (list-ref m i) j)))))
  (let loop ([curr mat] [k 0])
    (cond
      [(= k 4) #f]
      [(equal? curr target) #t]
      [else (loop (rotate curr) (+ k 1))])))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec find_rotation(Mat :: [[integer()]], Target :: [[integer()]]) -> boolean().
find_rotation(Mat, Target) ->
  check_all(Mat, Target, 4).

check_all(_Mat, _Target, 0) -> false;
check_all(Mat, Target, Count) ->
  case Mat =:= Target of
    true -> true;
    false -> check_all(rotate(Mat), Target, Count - 1)
  end.

rotate(Mat) ->
  N = length(Mat),
  [[lists:nth(I, Row) || Row <- lists:reverse(Mat)] || I <- lists:seq(1, N)].
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec find_rotation(mat :: [[integer]], target :: [[integer]]) :: boolean
  def find_rotation(mat, target) do
    do_find(mat, target, 4)
  end

  defp do_find(_mat, _target, 0), do: false
  defp do_find(mat, target, count) do
    if mat == target do
      true
    else
      do_find(rotate(mat), target, count - 1)
    end
  end

  defp rotate(mat) do
    mat
    |> Enum.reverse()
    |> Enum.zip()
    |> Enum.map(&Tuple.to_list/1)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n^2). We perform a maximum of four rotations and four comparisons. Each check and each rotation requires visiting every element in the n x n matrix, leading to a complexity of 4 * (n^2 + n^2), which simplifies to O(n^2).
- **Space Complexity:** O(1). The algorithm performs rotations in-place using a single temporary variable for swaps. While some high-level language features (like Python's zip) might create temporary copies, the algorithm can be fully implemented using only constant auxiliary space.
