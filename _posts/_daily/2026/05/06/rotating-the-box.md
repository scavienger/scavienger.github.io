---
layout: post
title: "Rotating the Box"
date: 2026-05-06 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Two Pointers", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/rotating-the-box/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<vector<char>> rotateTheBox(vector<vector<char>>&\
        \ boxGrid) {\n        int m = boxGrid.size();\n        int n = boxGrid[0].size();\n\
        \n        for (int i = 0; i < m; ++i) {\n            int emptyPos = n - 1;\n\
        \            for (int j = n - 1; j >= 0; --j) {\n                if (boxGrid[i][j]\
        \ == '*') {\n                    emptyPos = j - 1;\n                } else if\
        \ (boxGrid[i][j] == '#') {\n                    boxGrid[i][j] = '.';\n     \
        \               boxGrid[i][emptyPos] = '#';\n                    emptyPos--;\n\
        \                }\n            }\n        }\n\n        vector<vector<char>>\
        \ res(n, vector<char>(m));\n        for (int i = 0; i < m; ++i) {\n        \
        \    for (int j = 0; j < n; ++j) {\n                res[j][m - 1 - i] = boxGrid[i][j];\n\
        \            }\n        }\n\n        return res;\n    }\n};"
      java: "class Solution {\n    public char[][] rotateTheBox(char[][] boxGrid) {\n\
        \        int m = boxGrid.length;\n        int n = boxGrid[0].length;\n\n   \
        \     for (int i = 0; i < m; i++) {\n            int emptyPos = n - 1;\n   \
        \         for (int j = n - 1; j >= 0; j--) {\n                if (boxGrid[i][j]\
        \ == '*') {\n                    emptyPos = j - 1;\n                } else if\
        \ (boxGrid[i][j] == '#') {\n                    boxGrid[i][j] = '.';\n     \
        \               boxGrid[i][emptyPos] = '#';\n                    emptyPos--;\n\
        \                }\n            }\n        }\n\n        char[][] res = new char[n][m];\n\
        \        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++)\
        \ {\n                res[j][m - 1 - i] = boxGrid[i][j];\n            }\n   \
        \     }\n\n        return res;\n    }\n}"
      python: "class Solution(object):\n    def rotateTheBox(self, boxGrid):\n     \
        \   \"\"\"\n        :type boxGrid: List[List[str]]\n        :rtype: List[List[str]]\n\
        \        \"\"\"\n        m = len(boxGrid)\n        n = len(boxGrid[0])\n\n \
        \       for i in range(m):\n            empty_pos = n - 1\n            for j\
        \ in range(n - 1, -1, -1):\n                if boxGrid[i][j] == '*':\n     \
        \               empty_pos = j - 1\n                elif boxGrid[i][j] == '#':\n\
        \                    boxGrid[i][j] = '.'\n                    boxGrid[i][empty_pos]\
        \ = '#'\n                    empty_pos -= 1\n\n        res = [['' for _ in range(m)]\
        \ for _ in range(n)]\n        for i in range(m):\n            for j in range(n):\n\
        \                res[j][m - 1 - i] = boxGrid[i][j]\n\n        return res"
      python3: "class Solution:\n    def rotateTheBox(self, boxGrid: List[List[str]])\
        \ -> List[List[str]]:\n        m = len(boxGrid)\n        n = len(boxGrid[0])\n\
        \n        for i in range(m):\n            empty_pos = n - 1\n            for\
        \ j in range(n - 1, -1, -1):\n                if boxGrid[i][j] == '*':\n   \
        \                 empty_pos = j - 1\n                elif boxGrid[i][j] == '#':\n\
        \                    boxGrid[i][j] = '.'\n                    boxGrid[i][empty_pos]\
        \ = '#'\n                    empty_pos -= 1\n\n        res = [['' for _ in range(m)]\
        \ for _ in range(n)]\n        for i in range(m):\n            for j in range(n):\n\
        \                res[j][m - 1 - i] = boxGrid[i][j]\n\n        return res"
      c: "/**\n * Return an array of arrays of size *returnSize.\n * The sizes of the\
        \ arrays are returned as *returnColumnSizes array.\n * Note: Both returned array\
        \ and *columnSizes array must be malloced, assume caller calls free().\n */\n\
        char** rotateTheBox(char** boxGrid, int boxGridSize, int* boxGridColSize, int*\
        \ returnSize, int** returnColumnSizes) {\n    int m = boxGridSize;\n    int\
        \ n = boxGridColSize[0];\n\n    for (int i = 0; i < m; i++) {\n        int emptyPos\
        \ = n - 1;\n        for (int j = n - 1; j >= 0; j--) {\n            if (boxGrid[i][j]\
        \ == '*') {\n                emptyPos = j - 1;\n            } else if (boxGrid[i][j]\
        \ == '#') {\n                boxGrid[i][j] = '.';\n                boxGrid[i][emptyPos]\
        \ = '#';\n                emptyPos--;\n            }\n        }\n    }\n\n \
        \   char** res = (char**)malloc(n * sizeof(char*));\n    *returnColumnSizes\
        \ = (int*)malloc(n * sizeof(int));\n    *returnSize = n;\n    for (int j = 0;\
        \ j < n; j++) {\n        res[j] = (char*)malloc(m * sizeof(char));\n       \
        \ (*returnColumnSizes)[j] = m;\n    }\n\n    for (int i = 0; i < m; i++) {\n\
        \        for (int j = 0; j < n; j++) {\n            res[j][m - 1 - i] = boxGrid[i][j];\n\
        \        }\n    }\n\n    return res;\n}"
      csharp: "public class Solution {\n    public char[][] RotateTheBox(char[][] boxGrid)\
        \ {\n        int m = boxGrid.Length;\n        int n = boxGrid[0].Length;\n \
        \       for (int i = 0; i < m; i++) {\n            int empty = n - 1;\n    \
        \        for (int j = n - 1; j >= 0; j--) {\n                if (boxGrid[i][j]\
        \ == '*') {\n                    empty = j - 1;\n                } else if (boxGrid[i][j]\
        \ == '#') {\n                    boxGrid[i][j] = '.';\n                    boxGrid[i][empty]\
        \ = '#';\n                    empty--;\n                }\n            }\n \
        \       }\n        char[][] res = new char[n][];\n        for (int j = 0; j\
        \ < n; j++) {\n            res[j] = new char[m];\n            for (int i = 0;\
        \ i < m; i++) {\n                res[j][m - 1 - i] = boxGrid[i][j];\n      \
        \      }\n        }\n        return res;\n    }\n}"
      javascript: "/**\n * @param {character[][]} boxGrid\n * @return {character[][]}\n\
        \ */\nvar rotateTheBox = function(boxGrid) {\n    let m = boxGrid.length;\n\
        \    let n = boxGrid[0].length;\n    for (let i = 0; i < m; i++) {\n       \
        \ let empty = n - 1;\n        for (let j = n - 1; j >= 0; j--) {\n         \
        \   if (boxGrid[i][j] === '*') {\n                empty = j - 1;\n         \
        \   } else if (boxGrid[i][j] === '#') {\n                boxGrid[i][j] = '.';\n\
        \                boxGrid[i][empty] = '#';\n                empty--;\n      \
        \      }\n        }\n    }\n    let res = Array.from({ length: n }, () => new\
        \ Array(m));\n    for (let i = 0; i < m; i++) {\n        for (let j = 0; j <\
        \ n; j++) {\n            res[j][m - 1 - i] = boxGrid[i][j];\n        }\n   \
        \ }\n    return res;\n};"
      typescript: "function rotateTheBox(boxGrid: string[][]): string[][] {\n    const\
        \ m = boxGrid.length;\n    const n = boxGrid[0].length;\n    for (let i = 0;\
        \ i < m; i++) {\n        let empty = n - 1;\n        for (let j = n - 1; j >=\
        \ 0; j--) {\n            if (boxGrid[i][j] === '*') {\n                empty\
        \ = j - 1;\n            } else if (boxGrid[i][j] === '#') {\n              \
        \  boxGrid[i][j] = '.';\n                boxGrid[i][empty] = '#';\n        \
        \        empty--;\n            }\n        }\n    }\n    const res: string[][]\
        \ = Array.from({ length: n }, () => new Array(m));\n    for (let i = 0; i <\
        \ m; i++) {\n        for (let j = 0; j < n; j++) {\n            res[j][m - 1\
        \ - i] = boxGrid[i][j];\n        }\n    }\n    return res;\n};"
      php: "class Solution {\n\n    /**\n     * @param String[][] $boxGrid\n     * @return\
        \ String[][]\n     */\n    function rotateTheBox($boxGrid) {\n        $m = count($boxGrid);\n\
        \        $n = count($boxGrid[0]);\n        for ($i = 0; $i < $m; $i++) {\n \
        \           $empty = $n - 1;\n            for ($j = $n - 1; $j >= 0; $j--) {\n\
        \                if ($boxGrid[$i][$j] === '*') {\n                    $empty\
        \ = $j - 1;\n                } else if ($boxGrid[$i][$j] === '#') {\n      \
        \              $boxGrid[$i][$j] = '.';\n                    $boxGrid[$i][$empty]\
        \ = '#';\n                    $empty--;\n                }\n            }\n\
        \        }\n        $res = [];\n        for ($j = 0; $j < $n; $j++) {\n    \
        \        $res[$j] = array_fill(0, $m, '.');\n            for ($i = 0; $i < $m;\
        \ $i++) {\n                $res[$j][$m - 1 - $i] = $boxGrid[$i][$j];\n     \
        \       }\n        }\n        return $res;\n    }\n}"
      swift: "class Solution {\n    func rotateTheBox(_ boxGrid: [[Character]]) -> [[Character]]\
        \ {\n        var grid = boxGrid\n        let m = grid.count\n        let n =\
        \ grid[0].count\n        for i in 0..<m {\n            var empty = n - 1\n \
        \           for j in (0..<n).reversed() {\n                if grid[i][j] ==\
        \ \"*\" {\n                    empty = j - 1\n                } else if grid[i][j]\
        \ == \"#\" {\n                    grid[i][j] = \".\"\n                    grid[i][empty]\
        \ = \"#\"\n                    empty -= 1\n                }\n            }\n\
        \        }\n        var res = Array(repeating: Array(repeating: Character(\"\
        .\"), count: m), count: n)\n        for i in 0..<m {\n            for j in 0..<n\
        \ {\n                res[j][m - 1 - i] = grid[i][j]\n            }\n       \
        \ }\n        return res\n    }\n}"
      kotlin: "class Solution {\n    fun rotateTheBox(boxGrid: Array<CharArray>): Array<CharArray>\
        \ {\n        val m = boxGrid.size\n        val n = boxGrid[0].size\n\n     \
        \   for (i in 0 until m) {\n            var emptyPos = n - 1\n            for\
        \ (j in n - 1 downTo 0) {\n                if (boxGrid[i][j] == '*') {\n   \
        \                 emptyPos = j - 1\n                } else if (boxGrid[i][j]\
        \ == '#') {\n                    boxGrid[i][j] = '.'\n                    boxGrid[i][emptyPos]\
        \ = '#'\n                    emptyPos--\n                }\n            }\n\
        \        }\n\n        val result = Array(n) { CharArray(m) }\n        for (i\
        \ in 0 until m) {\n            for (j in 0 until n) {\n                result[j][m\
        \ - 1 - i] = boxGrid[i][j]\n            }\n        }\n        return result\n\
        \    }\n}"
      dart: "class Solution {\n  List<List<String>> rotateTheBox(List<List<String>>\
        \ boxGrid) {\n    int m = boxGrid.length;\n    int n = boxGrid[0].length;\n\n\
        \    for (int i = 0; i < m; i++) {\n      int emptyPos = n - 1;\n      for (int\
        \ j = n - 1; j >= 0; j--) {\n        if (boxGrid[i][j] == '*') {\n         \
        \ emptyPos = j - 1;\n        } else if (boxGrid[i][j] == '#') {\n          boxGrid[i][j]\
        \ = '.';\n          boxGrid[i][emptyPos] = '#';\n          emptyPos--;\n   \
        \     }\n      }\n    }\n\n    List<List<String>> result = List.generate(n,\
        \ (_) => List.filled(m, '.'));\n    for (int i = 0; i < m; i++) {\n      for\
        \ (int j = 0; j < n; j++) {\n        result[j][m - 1 - i] = boxGrid[i][j];\n\
        \      }\n    }\n    return result;\n  }\n}"
      go: "func rotateTheBox(boxGrid [][]byte) [][]byte {\n    m := len(boxGrid)\n \
        \   n := len(boxGrid[0])\n\n    for i := 0; i < m; i++ {\n        emptyPos :=\
        \ n - 1\n        for j := n - 1; j >= 0; j-- {\n            if boxGrid[i][j]\
        \ == '*' {\n                emptyPos = j - 1\n            } else if boxGrid[i][j]\
        \ == '#' {\n                boxGrid[i][j] = '.'\n                boxGrid[i][emptyPos]\
        \ = '#'\n                emptyPos--\n            }\n        }\n    }\n\n   \
        \ result := make([][]byte, n)\n    for j := 0; j < n; j++ {\n        result[j]\
        \ = make([]byte, m)\n    }\n\n    for i := 0; i < m; i++ {\n        for j :=\
        \ 0; j < n; j++ {\n            result[j][m-1-i] = boxGrid[i][j]\n        }\n\
        \    }\n    return result\n}"
      ruby: "# @param {Character[][]} box_grid\n# @return {Character[][]}\ndef rotate_the_box(box_grid)\n\
        \  m = box_grid.length\n  n = box_grid[0].length\n\n  (0...m).each do |i|\n\
        \    empty_pos = n - 1\n    (n - 1).step(0, -1).each do |j|\n      if box_grid[i][j]\
        \ == '*'\n        empty_pos = j - 1\n      elsif box_grid[i][j] == '#'\n   \
        \     box_grid[i][j] = '.'\n        box_grid[i][empty_pos] = '#'\n        empty_pos\
        \ -= 1\n      end\n    end\n  end\n\n  result = Array.new(n) { Array.new(m)\
        \ }\n  (0...m).each do |i|\n    (0...n).each do |j|\n      result[j][m - 1 -\
        \ i] = box_grid[i][j]\n    end\n  end\n  result\nend"
      scala: "object Solution {\n    def rotateTheBox(boxGrid: Array[Array[Char]]):\
        \ Array[Array[Char]] = {\n        val m = boxGrid.length\n        val n = boxGrid(0).length\n\
        \n        for (i <- 0 until m) {\n            var emptyPos = n - 1\n       \
        \     for (j <- n - 1 to 0 by -1) {\n                if (boxGrid(i)(j) == '*')\
        \ {\n                    emptyPos = j - 1\n                } else if (boxGrid(i)(j)\
        \ == '#') {\n                    boxGrid(i)(j) = '.'\n                    boxGrid(i)(emptyPos)\
        \ = '#'\n                    emptyPos -= 1\n                }\n            }\n\
        \        }\n\n        val result = Array.ofDim[Char](n, m)\n        for (i <-\
        \ 0 until m) {\n            for (j <- 0 until n) {\n                result(j)(m\
        \ - 1 - i) = boxGrid(i)(j)\n            }\n        }\n        result\n    }\n\
        }"
      rust: "impl Solution {\n    pub fn rotate_the_box(mut box_grid: Vec<Vec<char>>)\
        \ -> Vec<Vec<char>> {\n        let m = box_grid.len();\n        if m == 0 {\n\
        \            return vec![];\n        }\n        let n = box_grid[0].len();\n\
        \n        for i in 0..m {\n            let mut empty_pos = (n - 1) as i32;\n\
        \            for j in (0..n).rev() {\n                if box_grid[i][j] == '*'\
        \ {\n                    empty_pos = (j as i32) - 1;\n                } else\
        \ if box_grid[i][j] == '#' {\n                    let current_stone_j = j;\n\
        \                    let target_pos = empty_pos as usize;\n                \
        \    box_grid[i][current_stone_j] = '.';\n                    box_grid[i][target_pos]\
        \ = '#';\n                    empty_pos -= 1;\n                }\n         \
        \   }\n        }\n\n        let mut rotated = vec![vec!['.'; m]; n];\n     \
        \   for i in 0..m {\n            for j in 0..n {\n                rotated[j][m\
        \ - 1 - i] = box_grid[i][j];\n            }\n        }\n        rotated\n  \
        \  }\n}"
      racket: "(require racket/list)\n\n(define/contract (rotate-the-box boxGrid)\n\
        \  (-> (listof (listof char?)) (listof (listof char?)))\n  (let ()\n    (define\
        \ (process-row row)\n      (let loop ([lst row] [acc '()])\n        (if (null?\
        \ lst)\n            (apply append (reverse acc))\n            (let-values ([(seg\
        \ rest) (splitf-at lst (lambda (c) (not (char=? c #\\*))))])\n             \
        \ (if (null? seg)\n                  (let-values ([(stars next-rest) (splitf-at\
        \ rest (lambda (c) (char=? c #\\*)))])\n                    (loop next-rest\
        \ (cons stars acc)))\n                  (let* ([stones (count (lambda (c) (char=?\
        \ c #\\#)) seg)]\n                         [dots (- (length seg) stones)]\n\
        \                         [processed (append (make-list dots #\\.) (make-list\
        \ stones #\\#))])\n                    (loop rest (cons processed acc))))))))\n\
        \    (define (rotate-matrix matrix)\n      (if (null? matrix)\n          '()\n\
        \          (let ([transposed (apply map list matrix)])\n            (map reverse\
        \ transposed))))\n    (rotate-matrix (map process-row boxGrid))))"
      erlang: "-spec rotate_the_box(BoxGrid :: [[char()]]) -> [[char()]].\nrotate_the_box(BoxGrid)\
        \ ->\n  Processed = [process_row(Row) || Row <- BoxGrid],\n  rotate(Processed).\n\
        \nprocess_row(Row) ->\n  Segments = chunk_row(Row),\n  lists:append([process_segment(S)\
        \ || S <- Segments]).\n\nchunk_row([]) -> [];\nchunk_row([$* | _] = L) ->\n\
        \  {Stars, Rest} = lists:splitwith(fun(C) -> C == $* end, L),\n  [Stars | chunk_row(Rest)];\n\
        chunk_row(L) ->\n  {Seg, Rest} = lists:splitwith(fun(C) -> C /= $* end, L),\n\
        \  [Seg | chunk_row(Rest)].\n\nprocess_segment([$* | _] = Stars) ->\n  Stars;\n\
        process_segment(Seg) ->\n  StonesCount = length([C || C <- Seg, C == $#]),\n\
        \  DotsCount = length(Seg) - StonesCount,\n  lists:duplicate(DotsCount, $.)\
        \ ++ lists:duplicate(StonesCount, $#).\n\nrotate(Matrix) ->\n  T = transpose(Matrix),\n\
        \  [lists:reverse(R) || R <- T].\n\ntranspose([[] | _]) -> [];\ntranspose(Matrix)\
        \ ->\n  [lists:map(fun(Row) -> hd(Row) end, Matrix) | transpose(lists:map(fun(Row)\
        \ -> tl(Row) end, Matrix))]."
      elixir: "defmodule Solution do\n  @spec rotate_the_box(box_grid :: [[char]]) ::\
        \ [[char]]\n  def rotate_the_box(box_grid) do\n    box_grid\n    |> Enum.map(&process_row/1)\n\
        \    |> rotate_matrix()\n  end\n\n  defp process_row(row) do\n    row\n    |>\
        \ Enum.chunk_by(&(&1 == ?*))\n    |> Enum.flat_map(fn\n      [?* | _] = stars\
        \ ->\n        stars\n      segment ->\n        stones = Enum.count(segment,\
        \ &(&1 == ?#))\n        dots = length(segment) - stones\n        List.duplicate(?.,\
        \ dots) ++ List.duplicate(?#, stones)\n    end)\n  end\n\n  defp rotate_matrix(matrix)\
        \ do\n    matrix\n    |> Enum.zip()\n    |> Enum.map(fn tuple ->\n      tuple\n\
        \      |> Tuple.to_list()\n      |> Enum.reverse()\n    end)\n  end\nend"
    approach: The problem can be solved by first simulating the gravity effect horizontally
      for each row independently before performing the matrix rotation. Since the box
      will be rotated 90 degrees clockwise, stones falling 'down' in the final matrix
      is equivalent to stones sliding to the 'right' in the original box. For each row,
      we iterate from right to left, maintaining a pointer to the rightmost available
      empty cell. When we encounter a stone ('#'), we move it to this available position
      and shift the pointer to the next spot on the left. If we hit an obstacle ('*'),
      the pointer resets to the position immediately to its left, as stones cannot pass
      through or land on obstacles.
    time_complexity: O(m * n) where m is the number of rows and n is the number of columns
      in the boxGrid. We traverse every cell in the grid once to apply gravity and once
      more to perform the rotation, resulting in linear time relative to the number
      of elements.
    space_complexity: O(m * n) where m is the number of rows and n is the number of
      columns. This is primarily for the output grid of size n x m required for the
      rotated result. The gravity calculation itself is performed with O(1) additional
      space beyond the grid storage.
    elapsed_time: 263.97597098350525
    model: gemini-3-flash-preview
    generated_at: '2026-05-06 02:10:58 '
---

## Problem #1861: Rotating the Box

**Difficulty:** Medium

**Topics:** Array, Two Pointers, Matrix

## Problem Description

<p>You are given an <code>m x n</code> matrix of characters <code>boxGrid</code> representing a side-view of a box. Each cell of the box is one of the following:</p>

<ul>
	<li>A stone <code>&#39;#&#39;</code></li>
	<li>A stationary obstacle <code>&#39;*&#39;</code></li>
	<li>Empty <code>&#39;.&#39;</code></li>
</ul>

<p>The box is rotated <strong>90 degrees clockwise</strong>, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity <strong>does not</strong> affect the obstacles&#39; positions, and the inertia from the box&#39;s rotation <strong>does not </strong>affect the stones&#39; horizontal positions.</p>

<p>It is <strong>guaranteed</strong> that each stone in <code>boxGrid</code> rests on an obstacle, another stone, or the bottom of the box.</p>

<p>Return <em>an </em><code>n x m</code><em> matrix representing the box after the rotation described above</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcodewithstones.png" style="width: 300px; height: 150px;" /></p>

<pre>
<strong>Input:</strong> boxGrid = [[&quot;#&quot;,&quot;.&quot;,&quot;#&quot;]]
<strong>Output:</strong> [[&quot;.&quot;],
&nbsp;        [&quot;#&quot;],
&nbsp;        [&quot;#&quot;]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode2withstones.png" style="width: 375px; height: 195px;" /></p>

<pre>
<strong>Input:</strong> boxGrid = [[&quot;#&quot;,&quot;.&quot;,&quot;*&quot;,&quot;.&quot;],
&nbsp;             [&quot;#&quot;,&quot;#&quot;,&quot;*&quot;,&quot;.&quot;]]
<strong>Output:</strong> [[&quot;#&quot;,&quot;.&quot;],
&nbsp;        [&quot;#&quot;,&quot;#&quot;],
&nbsp;        [&quot;*&quot;,&quot;*&quot;],
&nbsp;        [&quot;.&quot;,&quot;.&quot;]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode3withstone.png" style="width: 400px; height: 218px;" /></p>

<pre>
<strong>Input:</strong> boxGrid = [[&quot;#&quot;,&quot;#&quot;,&quot;*&quot;,&quot;.&quot;,&quot;*&quot;,&quot;.&quot;],
&nbsp;             [&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;*&quot;,&quot;.&quot;,&quot;.&quot;],
&nbsp;             [&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;.&quot;,&quot;#&quot;,&quot;.&quot;]]
<strong>Output:</strong> [[&quot;.&quot;,&quot;#&quot;,&quot;#&quot;],
&nbsp;        [&quot;.&quot;,&quot;#&quot;,&quot;#&quot;],
&nbsp;        [&quot;#&quot;,&quot;#&quot;,&quot;*&quot;],
&nbsp;        [&quot;#&quot;,&quot;*&quot;,&quot;.&quot;],
&nbsp;        [&quot;#&quot;,&quot;.&quot;,&quot;*&quot;],
&nbsp;        [&quot;#&quot;,&quot;.&quot;,&quot;.&quot;]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == boxGrid.length</code></li>
	<li><code>n == boxGrid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>boxGrid[i][j]</code> is either <code>&#39;#&#39;</code>, <code>&#39;*&#39;</code>, or <code>&#39;.&#39;</code>.</li>
</ul>


## Hints

1. Rotate the box using the relation rotatedBox[i][j] = box[m - 1 - j][i].

2. Start iterating from the bottom of the box and for each empty cell check if there is any stone above it with no obstacles between them.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be solved by first simulating the gravity effect horizontally for each row independently before performing the matrix rotation. Since the box will be rotated 90 degrees clockwise, stones falling 'down' in the final matrix is equivalent to stones sliding to the 'right' in the original box. For each row, we iterate from right to left, maintaining a pointer to the rightmost available empty cell. When we encounter a stone ('#'), we move it to this available position and shift the pointer to the next spot on the left. If we hit an obstacle ('*'), the pointer resets to the position immediately to its left, as stones cannot pass through or land on obstacles.

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
    vector<vector<char>> rotateTheBox(vector<vector<char>>& boxGrid) {
        int m = boxGrid.size();
        int n = boxGrid[0].size();

        for (int i = 0; i < m; ++i) {
            int emptyPos = n - 1;
            for (int j = n - 1; j >= 0; --j) {
                if (boxGrid[i][j] == '*') {
                    emptyPos = j - 1;
                } else if (boxGrid[i][j] == '#') {
                    boxGrid[i][j] = '.';
                    boxGrid[i][emptyPos] = '#';
                    emptyPos--;
                }
            }
        }

        vector<vector<char>> res(n, vector<char>(m));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                res[j][m - 1 - i] = boxGrid[i][j];
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
    public char[][] rotateTheBox(char[][] boxGrid) {
        int m = boxGrid.length;
        int n = boxGrid[0].length;

        for (int i = 0; i < m; i++) {
            int emptyPos = n - 1;
            for (int j = n - 1; j >= 0; j--) {
                if (boxGrid[i][j] == '*') {
                    emptyPos = j - 1;
                } else if (boxGrid[i][j] == '#') {
                    boxGrid[i][j] = '.';
                    boxGrid[i][emptyPos] = '#';
                    emptyPos--;
                }
            }
        }

        char[][] res = new char[n][m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                res[j][m - 1 - i] = boxGrid[i][j];
            }
        }

        return res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        m = len(boxGrid)
        n = len(boxGrid[0])

        for i in range(m):
            empty_pos = n - 1
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    empty_pos = j - 1
                elif boxGrid[i][j] == '#':
                    boxGrid[i][j] = '.'
                    boxGrid[i][empty_pos] = '#'
                    empty_pos -= 1

        res = [['' for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = boxGrid[i][j]

        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        for i in range(m):
            empty_pos = n - 1
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    empty_pos = j - 1
                elif boxGrid[i][j] == '#':
                    boxGrid[i][j] = '.'
                    boxGrid[i][empty_pos] = '#'
                    empty_pos -= 1

        res = [['' for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = boxGrid[i][j]

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
char** rotateTheBox(char** boxGrid, int boxGridSize, int* boxGridColSize, int* returnSize, int** returnColumnSizes) {
    int m = boxGridSize;
    int n = boxGridColSize[0];

    for (int i = 0; i < m; i++) {
        int emptyPos = n - 1;
        for (int j = n - 1; j >= 0; j--) {
            if (boxGrid[i][j] == '*') {
                emptyPos = j - 1;
            } else if (boxGrid[i][j] == '#') {
                boxGrid[i][j] = '.';
                boxGrid[i][emptyPos] = '#';
                emptyPos--;
            }
        }
    }

    char** res = (char**)malloc(n * sizeof(char*));
    *returnColumnSizes = (int*)malloc(n * sizeof(int));
    *returnSize = n;
    for (int j = 0; j < n; j++) {
        res[j] = (char*)malloc(m * sizeof(char));
        (*returnColumnSizes)[j] = m;
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            res[j][m - 1 - i] = boxGrid[i][j];
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
    public char[][] RotateTheBox(char[][] boxGrid) {
        int m = boxGrid.Length;
        int n = boxGrid[0].Length;
        for (int i = 0; i < m; i++) {
            int empty = n - 1;
            for (int j = n - 1; j >= 0; j--) {
                if (boxGrid[i][j] == '*') {
                    empty = j - 1;
                } else if (boxGrid[i][j] == '#') {
                    boxGrid[i][j] = '.';
                    boxGrid[i][empty] = '#';
                    empty--;
                }
            }
        }
        char[][] res = new char[n][];
        for (int j = 0; j < n; j++) {
            res[j] = new char[m];
            for (int i = 0; i < m; i++) {
                res[j][m - 1 - i] = boxGrid[i][j];
            }
        }
        return res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {character[][]} boxGrid
 * @return {character[][]}
 */
var rotateTheBox = function(boxGrid) {
    let m = boxGrid.length;
    let n = boxGrid[0].length;
    for (let i = 0; i < m; i++) {
        let empty = n - 1;
        for (let j = n - 1; j >= 0; j--) {
            if (boxGrid[i][j] === '*') {
                empty = j - 1;
            } else if (boxGrid[i][j] === '#') {
                boxGrid[i][j] = '.';
                boxGrid[i][empty] = '#';
                empty--;
            }
        }
    }
    let res = Array.from({ length: n }, () => new Array(m));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            res[j][m - 1 - i] = boxGrid[i][j];
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
function rotateTheBox(boxGrid: string[][]): string[][] {
    const m = boxGrid.length;
    const n = boxGrid[0].length;
    for (let i = 0; i < m; i++) {
        let empty = n - 1;
        for (let j = n - 1; j >= 0; j--) {
            if (boxGrid[i][j] === '*') {
                empty = j - 1;
            } else if (boxGrid[i][j] === '#') {
                boxGrid[i][j] = '.';
                boxGrid[i][empty] = '#';
                empty--;
            }
        }
    }
    const res: string[][] = Array.from({ length: n }, () => new Array(m));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            res[j][m - 1 - i] = boxGrid[i][j];
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
     * @param String[][] $boxGrid
     * @return String[][]
     */
    function rotateTheBox($boxGrid) {
        $m = count($boxGrid);
        $n = count($boxGrid[0]);
        for ($i = 0; $i < $m; $i++) {
            $empty = $n - 1;
            for ($j = $n - 1; $j >= 0; $j--) {
                if ($boxGrid[$i][$j] === '*') {
                    $empty = $j - 1;
                } else if ($boxGrid[$i][$j] === '#') {
                    $boxGrid[$i][$j] = '.';
                    $boxGrid[$i][$empty] = '#';
                    $empty--;
                }
            }
        }
        $res = [];
        for ($j = 0; $j < $n; $j++) {
            $res[$j] = array_fill(0, $m, '.');
            for ($i = 0; $i < $m; $i++) {
                $res[$j][$m - 1 - $i] = $boxGrid[$i][$j];
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
    func rotateTheBox(_ boxGrid: [[Character]]) -> [[Character]] {
        var grid = boxGrid
        let m = grid.count
        let n = grid[0].count
        for i in 0..<m {
            var empty = n - 1
            for j in (0..<n).reversed() {
                if grid[i][j] == "*" {
                    empty = j - 1
                } else if grid[i][j] == "#" {
                    grid[i][j] = "."
                    grid[i][empty] = "#"
                    empty -= 1
                }
            }
        }
        var res = Array(repeating: Array(repeating: Character("."), count: m), count: n)
        for i in 0..<m {
            for j in 0..<n {
                res[j][m - 1 - i] = grid[i][j]
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
    fun rotateTheBox(boxGrid: Array<CharArray>): Array<CharArray> {
        val m = boxGrid.size
        val n = boxGrid[0].size

        for (i in 0 until m) {
            var emptyPos = n - 1
            for (j in n - 1 downTo 0) {
                if (boxGrid[i][j] == '*') {
                    emptyPos = j - 1
                } else if (boxGrid[i][j] == '#') {
                    boxGrid[i][j] = '.'
                    boxGrid[i][emptyPos] = '#'
                    emptyPos--
                }
            }
        }

        val result = Array(n) { CharArray(m) }
        for (i in 0 until m) {
            for (j in 0 until n) {
                result[j][m - 1 - i] = boxGrid[i][j]
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
  List<List<String>> rotateTheBox(List<List<String>> boxGrid) {
    int m = boxGrid.length;
    int n = boxGrid[0].length;

    for (int i = 0; i < m; i++) {
      int emptyPos = n - 1;
      for (int j = n - 1; j >= 0; j--) {
        if (boxGrid[i][j] == '*') {
          emptyPos = j - 1;
        } else if (boxGrid[i][j] == '#') {
          boxGrid[i][j] = '.';
          boxGrid[i][emptyPos] = '#';
          emptyPos--;
        }
      }
    }

    List<List<String>> result = List.generate(n, (_) => List.filled(m, '.'));
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        result[j][m - 1 - i] = boxGrid[i][j];
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
func rotateTheBox(boxGrid [][]byte) [][]byte {
    m := len(boxGrid)
    n := len(boxGrid[0])

    for i := 0; i < m; i++ {
        emptyPos := n - 1
        for j := n - 1; j >= 0; j-- {
            if boxGrid[i][j] == '*' {
                emptyPos = j - 1
            } else if boxGrid[i][j] == '#' {
                boxGrid[i][j] = '.'
                boxGrid[i][emptyPos] = '#'
                emptyPos--
            }
        }
    }

    result := make([][]byte, n)
    for j := 0; j < n; j++ {
        result[j] = make([]byte, m)
    }

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            result[j][m-1-i] = boxGrid[i][j]
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
# @param {Character[][]} box_grid
# @return {Character[][]}
def rotate_the_box(box_grid)
  m = box_grid.length
  n = box_grid[0].length

  (0...m).each do |i|
    empty_pos = n - 1
    (n - 1).step(0, -1).each do |j|
      if box_grid[i][j] == '*'
        empty_pos = j - 1
      elsif box_grid[i][j] == '#'
        box_grid[i][j] = '.'
        box_grid[i][empty_pos] = '#'
        empty_pos -= 1
      end
    end
  end

  result = Array.new(n) { Array.new(m) }
  (0...m).each do |i|
    (0...n).each do |j|
      result[j][m - 1 - i] = box_grid[i][j]
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
    def rotateTheBox(boxGrid: Array[Array[Char]]): Array[Array[Char]] = {
        val m = boxGrid.length
        val n = boxGrid(0).length

        for (i <- 0 until m) {
            var emptyPos = n - 1
            for (j <- n - 1 to 0 by -1) {
                if (boxGrid(i)(j) == '*') {
                    emptyPos = j - 1
                } else if (boxGrid(i)(j) == '#') {
                    boxGrid(i)(j) = '.'
                    boxGrid(i)(emptyPos) = '#'
                    emptyPos -= 1
                }
            }
        }

        val result = Array.ofDim[Char](n, m)
        for (i <- 0 until m) {
            for (j <- 0 until n) {
                result(j)(m - 1 - i) = boxGrid(i)(j)
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
    pub fn rotate_the_box(mut box_grid: Vec<Vec<char>>) -> Vec<Vec<char>> {
        let m = box_grid.len();
        if m == 0 {
            return vec![];
        }
        let n = box_grid[0].len();

        for i in 0..m {
            let mut empty_pos = (n - 1) as i32;
            for j in (0..n).rev() {
                if box_grid[i][j] == '*' {
                    empty_pos = (j as i32) - 1;
                } else if box_grid[i][j] == '#' {
                    let current_stone_j = j;
                    let target_pos = empty_pos as usize;
                    box_grid[i][current_stone_j] = '.';
                    box_grid[i][target_pos] = '#';
                    empty_pos -= 1;
                }
            }
        }

        let mut rotated = vec![vec!['.'; m]; n];
        for i in 0..m {
            for j in 0..n {
                rotated[j][m - 1 - i] = box_grid[i][j];
            }
        }
        rotated
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(require racket/list)

(define/contract (rotate-the-box boxGrid)
  (-> (listof (listof char?)) (listof (listof char?)))
  (let ()
    (define (process-row row)
      (let loop ([lst row] [acc '()])
        (if (null? lst)
            (apply append (reverse acc))
            (let-values ([(seg rest) (splitf-at lst (lambda (c) (not (char=? c #\*))))])
              (if (null? seg)
                  (let-values ([(stars next-rest) (splitf-at rest (lambda (c) (char=? c #\*)))])
                    (loop next-rest (cons stars acc)))
                  (let* ([stones (count (lambda (c) (char=? c #\#)) seg)]
                         [dots (- (length seg) stones)]
                         [processed (append (make-list dots #\.) (make-list stones #\#))])
                    (loop rest (cons processed acc))))))))
    (define (rotate-matrix matrix)
      (if (null? matrix)
          '()
          (let ([transposed (apply map list matrix)])
            (map reverse transposed))))
    (rotate-matrix (map process-row boxGrid))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec rotate_the_box(BoxGrid :: [[char()]]) -> [[char()]].
rotate_the_box(BoxGrid) ->
  Processed = [process_row(Row) || Row <- BoxGrid],
  rotate(Processed).

process_row(Row) ->
  Segments = chunk_row(Row),
  lists:append([process_segment(S) || S <- Segments]).

chunk_row([]) -> [];
chunk_row([$* | _] = L) ->
  {Stars, Rest} = lists:splitwith(fun(C) -> C == $* end, L),
  [Stars | chunk_row(Rest)];
chunk_row(L) ->
  {Seg, Rest} = lists:splitwith(fun(C) -> C /= $* end, L),
  [Seg | chunk_row(Rest)].

process_segment([$* | _] = Stars) ->
  Stars;
process_segment(Seg) ->
  StonesCount = length([C || C <- Seg, C == $#]),
  DotsCount = length(Seg) - StonesCount,
  lists:duplicate(DotsCount, $.) ++ lists:duplicate(StonesCount, $#).

rotate(Matrix) ->
  T = transpose(Matrix),
  [lists:reverse(R) || R <- T].

transpose([[] | _]) -> [];
transpose(Matrix) ->
  [lists:map(fun(Row) -> hd(Row) end, Matrix) | transpose(lists:map(fun(Row) -> tl(Row) end, Matrix))].
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec rotate_the_box(box_grid :: [[char]]) :: [[char]]
  def rotate_the_box(box_grid) do
    box_grid
    |> Enum.map(&process_row/1)
    |> rotate_matrix()
  end

  defp process_row(row) do
    row
    |> Enum.chunk_by(&(&1 == ?*))
    |> Enum.flat_map(fn
      [?* | _] = stars ->
        stars
      segment ->
        stones = Enum.count(segment, &(&1 == ?#))
        dots = length(segment) - stones
        List.duplicate(?., dots) ++ List.duplicate(?#, stones)
    end)
  end

  defp rotate_matrix(matrix) do
    matrix
    |> Enum.zip()
    |> Enum.map(fn tuple ->
      tuple
      |> Tuple.to_list()
      |> Enum.reverse()
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m * n) where m is the number of rows and n is the number of columns in the boxGrid. We traverse every cell in the grid once to apply gravity and once more to perform the rotation, resulting in linear time relative to the number of elements.
- **Space Complexity:** O(m * n) where m is the number of rows and n is the number of columns. This is primarily for the output grid of size n x m required for the rotated result. The gravity calculation itself is performed with O(1) additional space beyond the grid storage.
