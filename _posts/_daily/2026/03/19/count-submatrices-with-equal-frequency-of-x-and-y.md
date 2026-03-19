---
layout: post
title: "Count Submatrices With Equal Frequency of X and Y"
date: 2026-03-19 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Matrix", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int numberOfSubmatrices(vector<vector<char>>&\
        \ grid) {\n        int R = grid.size();\n        int C = grid[0].size();\n \
        \       vector<int> diff(C + 1, 0);\n        vector<int> hasX(C + 1, 0);\n \
        \       int totalCount = 0;\n        for (int r = 0; r < R; ++r) {\n       \
        \     int rowDiff = 0;\n            int rowX = 0;\n            for (int c =\
        \ 0; c < C; ++c) {\n                if (grid[r][c] == 'X') {\n             \
        \       rowDiff++;\n                    rowX++;\n                } else if (grid[r][c]\
        \ == 'Y') {\n                    rowDiff--;\n                }\n           \
        \     diff[c + 1] += rowDiff;\n                hasX[c + 1] += rowX;\n      \
        \          if (diff[c + 1] == 0 && hasX[c + 1] > 0) {\n                    totalCount++;\n\
        \                }\n            }\n        }\n        return totalCount;\n \
        \   }\n};"
      java: "class Solution {\n    public int numberOfSubmatrices(char[][] grid) {\n\
        \        int R = grid.length;\n        int C = grid[0].length;\n        int[]\
        \ diff = new int[C + 1];\n        int[] hasX = new int[C + 1];\n        int\
        \ totalCount = 0;\n        for (int r = 0; r < R; r++) {\n            int rowDiff\
        \ = 0;\n            int rowX = 0;\n            for (int c = 0; c < C; c++) {\n\
        \                if (grid[r][c] == 'X') {\n                    rowDiff++;\n\
        \                    rowX++;\n                } else if (grid[r][c] == 'Y')\
        \ {\n                    rowDiff--;\n                }\n                diff[c\
        \ + 1] += rowDiff;\n                hasX[c + 1] += rowX;\n                if\
        \ (diff[c + 1] == 0 && hasX[c + 1] > 0) {\n                    totalCount++;\n\
        \                }\n            }\n        }\n        return totalCount;\n \
        \   }\n}"
      python: "class Solution(object):\n    def numberOfSubmatrices(self, grid):\n \
        \       \"\"\"\n        :type grid: List[List[str]]\n        :rtype: int\n \
        \       \"\"\"\n        R = len(grid)\n        C = len(grid[0])\n        diff\
        \ = [0] * (C + 1)\n        hasX = [0] * (C + 1)\n        totalCount = 0\n  \
        \      for r in range(R):\n            rowDiff = 0\n            rowX = 0\n \
        \           for c in range(C):\n                char = grid[r][c]\n        \
        \        if char == 'X':\n                    rowDiff += 1\n               \
        \     rowX += 1\n                elif char == 'Y':\n                    rowDiff\
        \ -= 1\n                diff[c + 1] += rowDiff\n                hasX[c + 1]\
        \ += rowX\n                if diff[c + 1] == 0 and hasX[c + 1] > 0:\n      \
        \              totalCount += 1\n        return totalCount"
      python3: "class Solution:\n    def numberOfSubmatrices(self, grid: List[List[str]])\
        \ -> int:\n        R = len(grid)\n        C = len(grid[0])\n        diff = [0]\
        \ * (C + 1)\n        hasX = [0] * (C + 1)\n        totalCount = 0\n        for\
        \ r in range(R):\n            rowDiff = 0\n            rowX = 0\n          \
        \  for c in range(C):\n                char = grid[r][c]\n                if\
        \ char == 'X':\n                    rowDiff += 1\n                    rowX +=\
        \ 1\n                elif char == 'Y':\n                    rowDiff -= 1\n \
        \               diff[c + 1] += rowDiff\n                hasX[c + 1] += rowX\n\
        \                if diff[c + 1] == 0 and hasX[c + 1] > 0:\n                \
        \    totalCount += 1\n        return totalCount"
      c: "#include <stdlib.h>\n\nint numberOfSubmatrices(char** grid, int gridSize,\
        \ int* gridColSize) {\n    int R = gridSize;\n    int C = gridColSize[0];\n\
        \    int* diff = (int*)calloc(C + 1, sizeof(int));\n    int* hasX = (int*)calloc(C\
        \ + 1, sizeof(int));\n    int totalCount = 0;\n    for (int r = 0; r < R; r++)\
        \ {\n        int rowDiff = 0;\n        int rowX = 0;\n        for (int c = 0;\
        \ c < C; c++) {\n            if (grid[r][c] == 'X') {\n                rowDiff++;\n\
        \                rowX++;\n            } else if (grid[r][c] == 'Y') {\n    \
        \            rowDiff--;\n            }\n            diff[c + 1] += rowDiff;\n\
        \            hasX[c + 1] += rowX;\n            if (diff[c + 1] == 0 && hasX[c\
        \ + 1] > 0) {\n                totalCount++;\n            }\n        }\n   \
        \ }\n    free(diff);\n    free(hasX);\n    return totalCount;\n}"
      csharp: "public class Solution {\n    public int NumberOfSubmatrices(char[][]\
        \ grid) {\n        int R = grid.Length;\n        int C = grid[0].Length;\n \
        \       int[] diff = new int[C + 1];\n        int[] hasX = new int[C + 1];\n\
        \        int totalCount = 0;\n        for (int r = 0; r < R; r++) {\n      \
        \      int rowDiff = 0;\n            int rowX = 0;\n            for (int c =\
        \ 0; c < C; c++) {\n                if (grid[r][c] == 'X') {\n             \
        \       rowDiff++;\n                    rowX++;\n                } else if (grid[r][c]\
        \ == 'Y') {\n                    rowDiff--;\n                }\n           \
        \     diff[c + 1] += rowDiff;\n                hasX[c + 1] += rowX;\n      \
        \          if (diff[c + 1] == 0 && hasX[c + 1] > 0) {\n                    totalCount++;\n\
        \                }\n            }\n        }\n        return totalCount;\n \
        \   }\n}"
      javascript: "/**\n * @param {character[][]} grid\n * @return {number}\n */\nvar\
        \ numberOfSubmatrices = function(grid) {\n    const R = grid.length;\n    const\
        \ C = grid[0].length;\n    const diff = new Int32Array(C + 1);\n    const hasX\
        \ = new Int32Array(C + 1);\n    let totalCount = 0;\n    for (let r = 0; r <\
        \ R; r++) {\n        let rowDiff = 0;\n        let rowX = 0;\n        for (let\
        \ c = 0; c < C; c++) {\n            if (grid[r][c] === 'X') {\n            \
        \    rowDiff++;\n                rowX++;\n            } else if (grid[r][c]\
        \ === 'Y') {\n                rowDiff--;\n            }\n            diff[c\
        \ + 1] += rowDiff;\n            hasX[c + 1] += rowX;\n            if (diff[c\
        \ + 1] === 0 && hasX[c + 1] > 0) {\n                totalCount++;\n        \
        \    }\n        }\n    }\n    return totalCount;\n};"
      typescript: "function numberOfSubmatrices(grid: string[][]): number {\n    const\
        \ rows = grid.length;\n    const cols = grid[0].length;\n    const diffs = new\
        \ Int32Array(cols);\n    const xCounts = new Int32Array(cols);\n    let count\
        \ = 0;\n    for (let i = 0; i < rows; i++) {\n        let rowDiff = 0;\n   \
        \     let rowX = 0;\n        for (let j = 0; j < cols; j++) {\n            const\
        \ char = grid[i][j];\n            if (char === 'X') {\n                rowDiff++;\n\
        \                rowX++;\n            } else if (char === 'Y') {\n         \
        \       rowDiff--;\n            }\n            diffs[j] += rowDiff;\n      \
        \      xCounts[j] += rowX;\n            if (xCounts[j] > 0 && diffs[j] === 0)\
        \ {\n                count++;\n            }\n        }\n    }\n    return count;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param String[][] $grid\n     * @return\
        \ Integer\n     */\n    function numberOfSubmatrices($grid) {\n        $rows\
        \ = count($grid);\n        $cols = count($grid[0]);\n        $diffs = array_fill(0,\
        \ $cols, 0);\n        $xCounts = array_fill(0, $cols, 0);\n        $count =\
        \ 0;\n        for ($i = 0; $i < $rows; $i++) {\n            $rowDiff = 0;\n\
        \            $rowX = 0;\n            for ($j = 0; $j < $cols; $j++) {\n    \
        \            $char = $grid[$i][$j];\n                if ($char === 'X') {\n\
        \                    $rowDiff++;\n                    $rowX++;\n           \
        \     } else if ($char === 'Y') {\n                    $rowDiff--;\n       \
        \         }\n                $diffs[$j] += $rowDiff;\n                $xCounts[$j]\
        \ += $rowX;\n                if ($xCounts[$j] > 0 && $diffs[$j] === 0) {\n \
        \                   $count++;\n                }\n            }\n        }\n\
        \        return $count;\n    }\n}"
      swift: "class Solution {\n    func numberOfSubmatrices(_ grid: [[Character]])\
        \ -> Int {\n        let rows = grid.count\n        let cols = grid[0].count\n\
        \        var diffs = Array(repeating: 0, count: cols)\n        var xCounts =\
        \ Array(repeating: 0, count: cols)\n        var count = 0\n        for i in\
        \ 0..<rows {\n            var rowDiff = 0\n            var rowX = 0\n      \
        \      for j in 0..<cols {\n                let char = grid[i][j]\n        \
        \        if char == \"X\" {\n                    rowDiff += 1\n            \
        \        rowX += 1\n                } else if char == \"Y\" {\n            \
        \        rowDiff -= 1\n                }\n                diffs[j] += rowDiff\n\
        \                xCounts[j] += rowX\n                if xCounts[j] > 0 && diffs[j]\
        \ == 0 {\n                    count += 1\n                }\n            }\n\
        \        }\n        return count\n    }\n}"
      kotlin: "class Solution {\n    fun numberOfSubmatrices(grid: Array<CharArray>):\
        \ Int {\n        val rows = grid.size\n        val cols = grid[0].size\n   \
        \     val diffs = IntArray(cols)\n        val xCounts = IntArray(cols)\n   \
        \     var count = 0\n        for (i in 0 until rows) {\n            var rowDiff\
        \ = 0\n            var rowX = 0\n            for (j in 0 until cols) {\n   \
        \             val char = grid[i][j]\n                if (char == 'X') {\n  \
        \                  rowDiff++\n                    rowX++\n                }\
        \ else if (char == 'Y') {\n                    rowDiff--\n                }\n\
        \                diffs[j] += rowDiff\n                xCounts[j] += rowX\n \
        \               if (xCounts[j] > 0 && diffs[j] == 0) {\n                   \
        \ count++\n                }\n            }\n        }\n        return count\n\
        \    }\n}"
      dart: "class Solution {\n  int numberOfSubmatrices(List<List<String>> grid) {\n\
        \    int rows = grid.length;\n    int cols = grid[0].length;\n    List<int>\
        \ diffs = List<int>.filled(cols, 0);\n    List<int> xCounts = List<int>.filled(cols,\
        \ 0);\n    int count = 0;\n    for (int i = 0; i < rows; i++) {\n      int rowDiff\
        \ = 0;\n      int rowX = 0;\n      for (int j = 0; j < cols; j++) {\n      \
        \  String char = grid[i][j];\n        if (char == 'X') {\n          rowDiff++;\n\
        \          rowX++;\n        } else if (char == 'Y') {\n          rowDiff--;\n\
        \        }\n        diffs[j] += rowDiff;\n        xCounts[j] += rowX;\n    \
        \    if (xCounts[j] > 0 && diffs[j] == 0) {\n          count++;\n        }\n\
        \      }\n    }\n    return count;\n  }\n}"
      go: "func numberOfSubmatrices(grid [][]byte) int {\n    rows := len(grid)\n  \
        \  cols := len(grid[0])\n    diffs := make([]int, cols)\n    xCounts := make([]int,\
        \ cols)\n    count := 0\n    for i := 0; i < rows; i++ {\n        rowDiff :=\
        \ 0\n        rowX := 0\n        for j := 0; j < cols; j++ {\n            char\
        \ := grid[i][j]\n            if char == 'X' {\n                rowDiff++\n \
        \               rowX++\n            } else if char == 'Y' {\n              \
        \  rowDiff--\n            }\n            diffs[j] += rowDiff\n            xCounts[j]\
        \ += rowX\n            if xCounts[j] > 0 && diffs[j] == 0 {\n              \
        \  count++\n            }\n        }\n    }\n    return count\n}"
      ruby: "def number_of_submatrices(grid)\n  rows = grid.length\n  cols = grid[0].length\n\
        \  diff = Array.new(cols + 1, 0)\n  has_x = Array.new(cols + 1, 0)\n  count\
        \ = 0\n  rows.times do |r|\n    row_diff_p = 0\n    row_has_x_p = 0\n    cols.times\
        \ do |c|\n      char = grid[r][c]\n      if char == 'X'\n        row_diff_p\
        \ += 1\n        row_has_x_p += 1\n      elsif char == 'Y'\n        row_diff_p\
        \ -= 1\n      end\n      diff[c + 1] += row_diff_p\n      has_x[c + 1] += row_has_x_p\n\
        \      count += 1 if diff[c + 1] == 0 && has_x[c + 1] > 0\n    end\n  end\n\
        \  count\nend"
      scala: "object Solution {\n  def numberOfSubmatrices(grid: Array[Array[Char]]):\
        \ Int = {\n    val rows = grid.length\n    val cols = grid(0).length\n    val\
        \ diff = new Array[Int](cols + 1)\n    val hasX = new Array[Int](cols + 1)\n\
        \    var count = 0\n    for (r <- 0 until rows) {\n      var rowDiffP = 0\n\
        \      var rowHasXP = 0\n      for (c <- 0 until cols) {\n        val char =\
        \ grid(r)(c)\n        if (char == 'X') {\n          rowDiffP += 1\n        \
        \  rowHasXP += 1\n        } else if (char == 'Y') {\n          rowDiffP -= 1\n\
        \        }\n        diff(c + 1) += rowDiffP\n        hasX(c + 1) += rowHasXP\n\
        \        if (diff(c + 1) == 0 && hasX(c + 1) > 0) count += 1\n      }\n    }\n\
        \    count\n  }\n}"
      rust: "impl Solution {\n    pub fn number_of_submatrices(grid: Vec<Vec<char>>)\
        \ -> i32 {\n        let rows = grid.len();\n        let cols = grid[0].len();\n\
        \        let mut diff = vec![0; cols + 1];\n        let mut has_x = vec![0;\
        \ cols + 1];\n        let mut count = 0;\n        for r in 0..rows {\n     \
        \       let mut row_diff_p = 0;\n            let mut row_has_x_p = 0;\n    \
        \        for c in 0..cols {\n                match grid[r][c] {\n          \
        \          'X' => {\n                        row_diff_p += 1;\n            \
        \            row_has_x_p += 1;\n                    }\n                    'Y'\
        \ => {\n                        row_diff_p -= 1;\n                    }\n  \
        \                  _ => {}\n                }\n                diff[c + 1] +=\
        \ row_diff_p;\n                has_x[c + 1] += row_has_x_p;\n              \
        \  if diff[c + 1] == 0 && has_x[c + 1] > 0 {\n                    count += 1;\n\
        \                }\n            }\n        }\n        count\n    }\n}"
      racket: "(define/contract (number-of-submatrices grid)\n  (-> (listof (listof\
        \ char?)) exact-integer?)\n  (let* ([rows (length grid)]\n         [cols (length\
        \ (car grid))]\n         [diff (make-vector (+ cols 1) 0)]\n         [has-x\
        \ (make-vector (+ cols 1) 0)])\n    (let ([count 0])\n      (for ([row-list\
        \ grid])\n        (let ([row-diff-p 0]\n              [row-has-x-p 0])\n   \
        \       (for ([char row-list]\n                [c (in-range cols)])\n      \
        \      (cond\n              [(char=? char #\\X)\n               (set! row-diff-p\
        \ (+ row-diff-p 1))\n               (set! row-has-x-p (+ row-has-x-p 1))]\n\
        \              [(char=? char #\\Y)\n               (set! row-diff-p (- row-diff-p\
        \ 1))]\n              [else (void)])\n            (let ([new-diff (+ (vector-ref\
        \ diff (+ c 1)) row-diff-p)]\n                  [new-has-x (+ (vector-ref has-x\
        \ (+ c 1)) row-has-x-p)])\n              (vector-set! diff (+ c 1) new-diff)\n\
        \              (vector-set! has-x (+ c 1) new-has-x)\n              (when (and\
        \ (= new-diff 0) (> new-has-x 0))\n                (set! count (+ count 1)))))))\n\
        \      count)))"
      erlang: "-spec number_of_submatrices(Grid :: [[char()]]) -> integer().\nnumber_of_submatrices(Grid)\
        \ ->\n  Cols = length(hd(Grid)),\n  compute(Grid, erlang:make_tuple(Cols + 1,\
        \ 0), erlang:make_tuple(Cols + 1, 0), 0).\n\ncompute([], _, _, TotalCount) ->\
        \ TotalCount;\ncompute([Row | Rest], PrevDiffRow, PrevHasXRow, TotalCount) ->\n\
        \  {NewDiffRow, NewHasXRow, RowCount} = process_row(Row, 1, 0, 0, PrevDiffRow,\
        \ PrevHasXRow, [], [], 0),\n  compute(Rest, NewDiffRow, NewHasXRow, TotalCount\
        \ + RowCount).\n\nprocess_row([], _, _, _, _, _, AccDiff, AccHasX, RowCount)\
        \ ->\n  {list_to_tuple([0 | lists:reverse(AccDiff)]), list_to_tuple([0 | lists:reverse(AccHasX)]),\
        \ RowCount};\nprocess_row([Char | Rest], ColIdx, CurrDiffP, CurrHasXP, PrevDiffRow,\
        \ PrevHasXRow, AccD, AccH, RowCount) ->\n  {VD, VX} = case Char of $X -> {1,\
        \ 1}; $Y -> {-1, 0}; $. -> {0, 0} end,\n  NewDiffP = CurrDiffP + VD,\n  NewHasXP\
        \ = CurrHasXP + VX,\n  TotalDiff = NewDiffP + element(ColIdx + 1, PrevDiffRow),\n\
        \  TotalHasX = NewHasXP + element(ColIdx + 1, PrevHasXRow),\n  NewCount = if\
        \ (TotalDiff == 0) and (TotalHasX > 0) -> RowCount + 1; true -> RowCount end,\n\
        \  process_row(Rest, ColIdx + 1, NewDiffP, NewHasXP, PrevDiffRow, PrevHasXRow,\
        \ [TotalDiff | AccD], [TotalHasX | AccH], NewCount)."
      elixir: "defmodule Solution do\n  @spec number_of_submatrices(grid :: [[char]])\
        \ :: integer\n  def number_of_submatrices(grid) do\n    cols = length(hd(grid))\n\
        \    initial = {List.to_tuple(List.duplicate(0, cols + 1)), List.to_tuple(List.duplicate(0,\
        \ cols + 1)), 0}\n    {_, _, total_count} = Enum.reduce(grid, initial, fn row,\
        \ {prev_d, prev_h, acc} ->\n      {new_d, new_h, row_count} = process_row(row,\
        \ 0, 0, 0, prev_d, prev_h, [], [], 0)\n      {new_d, new_h, acc + row_count}\n\
        \    end)\n    total_count\n  end\n\n  defp process_row([], _, _, _, _, _, acc_d,\
        \ acc_h, row_count) do\n    {List.to_tuple([0 | Enum.reverse(acc_d)]), List.to_tuple([0\
        \ | Enum.reverse(acc_h)]), row_count}\n  end\n\n  defp process_row([char | rest],\
        \ c_idx, cdp, chxp, prev_d, prev_h, acc_d, acc_h, row_count) do\n    {v_d, v_x}\
        \ = case char do\n      ?X -> {1, 1}\n      ?Y -> {-1, 0}\n      ?. -> {0, 0}\n\
        \    end\n    new_cdp = cdp + v_d\n    new_chxp = chxp + v_x\n    total_d =\
        \ new_cdp + elem(prev_d, c_idx + 1)\n    total_h = new_chxp + elem(prev_h, c_idx\
        \ + 1)\n    new_row_count = row_count + (if total_d == 0 and total_h > 0, do:\
        \ 1, else: 0)\n    process_row(rest, c_idx + 1, new_cdp, new_chxp, prev_d, prev_h,\
        \ [total_d | acc_d], [total_h | acc_h], new_row_count)\n  end\nend"
    approach: 'To solve this problem efficiently, we use a 2D prefix sum approach focused
      on submatrices starting at the top-left corner (0, 0). Each submatrix is uniquely
      defined by its bottom-right corner (i, j). We maintain two pieces of information
      for every submatrix: the difference between the number of ''X'' and ''Y'' characters,
      and the total count of ''X'' characters. By assigning ''X'' a value of 1, ''Y''
      a value of -1, and ''.'' a value of 0, a submatrix has equal frequencies of ''X''
      and ''Y'' if the sum of these values is exactly zero.


      To optimize space, we iterate through the grid row by row and update 1D prefix
      sum arrays for the columns. For each cell (r, c), we maintain a running horizontal
      sum (row sum) for both the value difference and the ''X'' count. We then add these
      horizontal sums to the 1D arrays containing the vertical cumulative sums from
      previous rows. This allows us to calculate the required metrics for the submatrix
      ending at (r, c) in constant time. If the accumulated difference is zero and the
      ''X'' count is at least one, we increment the result counter.'
    time_complexity: O(R * C) where R is the number of rows and C is the number of columns.
      We traverse every cell of the grid exactly once, performing constant time calculations
      for prefix sums at each step.
    space_complexity: O(C) where C is the number of columns. By processing the grid
      row by row, we only need 1D arrays to store the cumulative sums from the top down
      to the current row.
    elapsed_time: 170.33137345314026
    model: gemini-3-flash-preview
    generated_at: '2026-03-19 01:30:50 '
---

## Problem #3212: Count Submatrices With Equal Frequency of X and Y

**Difficulty:** Medium

**Topics:** Array, Matrix, Prefix Sum

## Problem Description

<p>Given a 2D character matrix <code>grid</code>, where <code>grid[i][j]</code> is either <code>&#39;X&#39;</code>, <code>&#39;Y&#39;</code>, or <code>&#39;.&#39;</code>, return the number of <span data-keyword="submatrix">submatrices</span> that contain:</p>

<ul>
	<li><code>grid[0][0]</code></li>
	<li>an <strong>equal</strong> frequency of <code>&#39;X&#39;</code> and <code>&#39;Y&#39;</code>.</li>
	<li><strong>at least</strong> one <code>&#39;X&#39;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[&quot;X&quot;,&quot;Y&quot;,&quot;.&quot;],[&quot;Y&quot;,&quot;.&quot;,&quot;.&quot;]]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/06/07/examplems.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 175px; height: 350px;" /></strong></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[&quot;X&quot;,&quot;X&quot;],[&quot;X&quot;,&quot;Y&quot;]]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>No submatrix has an equal frequency of <code>&#39;X&#39;</code> and <code>&#39;Y&#39;</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;.&quot;]]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>No submatrix has at least one <code>&#39;X&#39;</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= grid.length, grid[i].length &lt;= 1000</code></li>
	<li><code>grid[i][j]</code> is either <code>&#39;X&#39;</code>, <code>&#39;Y&#39;</code>, or <code>&#39;.&#39;</code>.</li>
</ul>


## Hints

1. Replace `’X’` with 1, `’Y’` with -1 and `’.’` with 0.

2. You need to find how many submatrices `grid[0..x][0..y]` have a sum of 0 and at least one `’X’`.

3. Use prefix sum to calculate submatrices sum.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem efficiently, we use a 2D prefix sum approach focused on submatrices starting at the top-left corner (0, 0). Each submatrix is uniquely defined by its bottom-right corner (i, j). We maintain two pieces of information for every submatrix: the difference between the number of 'X' and 'Y' characters, and the total count of 'X' characters. By assigning 'X' a value of 1, 'Y' a value of -1, and '.' a value of 0, a submatrix has equal frequencies of 'X' and 'Y' if the sum of these values is exactly zero.

To optimize space, we iterate through the grid row by row and update 1D prefix sum arrays for the columns. For each cell (r, c), we maintain a running horizontal sum (row sum) for both the value difference and the 'X' count. We then add these horizontal sums to the 1D arrays containing the vertical cumulative sums from previous rows. This allows us to calculate the required metrics for the submatrix ending at (r, c) in constant time. If the accumulated difference is zero and the 'X' count is at least one, we increment the result counter.

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
    int numberOfSubmatrices(vector<vector<char>>& grid) {
        int R = grid.size();
        int C = grid[0].size();
        vector<int> diff(C + 1, 0);
        vector<int> hasX(C + 1, 0);
        int totalCount = 0;
        for (int r = 0; r < R; ++r) {
            int rowDiff = 0;
            int rowX = 0;
            for (int c = 0; c < C; ++c) {
                if (grid[r][c] == 'X') {
                    rowDiff++;
                    rowX++;
                } else if (grid[r][c] == 'Y') {
                    rowDiff--;
                }
                diff[c + 1] += rowDiff;
                hasX[c + 1] += rowX;
                if (diff[c + 1] == 0 && hasX[c + 1] > 0) {
                    totalCount++;
                }
            }
        }
        return totalCount;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int numberOfSubmatrices(char[][] grid) {
        int R = grid.length;
        int C = grid[0].length;
        int[] diff = new int[C + 1];
        int[] hasX = new int[C + 1];
        int totalCount = 0;
        for (int r = 0; r < R; r++) {
            int rowDiff = 0;
            int rowX = 0;
            for (int c = 0; c < C; c++) {
                if (grid[r][c] == 'X') {
                    rowDiff++;
                    rowX++;
                } else if (grid[r][c] == 'Y') {
                    rowDiff--;
                }
                diff[c + 1] += rowDiff;
                hasX[c + 1] += rowX;
                if (diff[c + 1] == 0 && hasX[c + 1] > 0) {
                    totalCount++;
                }
            }
        }
        return totalCount;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        R = len(grid)
        C = len(grid[0])
        diff = [0] * (C + 1)
        hasX = [0] * (C + 1)
        totalCount = 0
        for r in range(R):
            rowDiff = 0
            rowX = 0
            for c in range(C):
                char = grid[r][c]
                if char == 'X':
                    rowDiff += 1
                    rowX += 1
                elif char == 'Y':
                    rowDiff -= 1
                diff[c + 1] += rowDiff
                hasX[c + 1] += rowX
                if diff[c + 1] == 0 and hasX[c + 1] > 0:
                    totalCount += 1
        return totalCount
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        diff = [0] * (C + 1)
        hasX = [0] * (C + 1)
        totalCount = 0
        for r in range(R):
            rowDiff = 0
            rowX = 0
            for c in range(C):
                char = grid[r][c]
                if char == 'X':
                    rowDiff += 1
                    rowX += 1
                elif char == 'Y':
                    rowDiff -= 1
                diff[c + 1] += rowDiff
                hasX[c + 1] += rowX
                if diff[c + 1] == 0 and hasX[c + 1] > 0:
                    totalCount += 1
        return totalCount
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int numberOfSubmatrices(char** grid, int gridSize, int* gridColSize) {
    int R = gridSize;
    int C = gridColSize[0];
    int* diff = (int*)calloc(C + 1, sizeof(int));
    int* hasX = (int*)calloc(C + 1, sizeof(int));
    int totalCount = 0;
    for (int r = 0; r < R; r++) {
        int rowDiff = 0;
        int rowX = 0;
        for (int c = 0; c < C; c++) {
            if (grid[r][c] == 'X') {
                rowDiff++;
                rowX++;
            } else if (grid[r][c] == 'Y') {
                rowDiff--;
            }
            diff[c + 1] += rowDiff;
            hasX[c + 1] += rowX;
            if (diff[c + 1] == 0 && hasX[c + 1] > 0) {
                totalCount++;
            }
        }
    }
    free(diff);
    free(hasX);
    return totalCount;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int NumberOfSubmatrices(char[][] grid) {
        int R = grid.Length;
        int C = grid[0].Length;
        int[] diff = new int[C + 1];
        int[] hasX = new int[C + 1];
        int totalCount = 0;
        for (int r = 0; r < R; r++) {
            int rowDiff = 0;
            int rowX = 0;
            for (int c = 0; c < C; c++) {
                if (grid[r][c] == 'X') {
                    rowDiff++;
                    rowX++;
                } else if (grid[r][c] == 'Y') {
                    rowDiff--;
                }
                diff[c + 1] += rowDiff;
                hasX[c + 1] += rowX;
                if (diff[c + 1] == 0 && hasX[c + 1] > 0) {
                    totalCount++;
                }
            }
        }
        return totalCount;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numberOfSubmatrices = function(grid) {
    const R = grid.length;
    const C = grid[0].length;
    const diff = new Int32Array(C + 1);
    const hasX = new Int32Array(C + 1);
    let totalCount = 0;
    for (let r = 0; r < R; r++) {
        let rowDiff = 0;
        let rowX = 0;
        for (let c = 0; c < C; c++) {
            if (grid[r][c] === 'X') {
                rowDiff++;
                rowX++;
            } else if (grid[r][c] === 'Y') {
                rowDiff--;
            }
            diff[c + 1] += rowDiff;
            hasX[c + 1] += rowX;
            if (diff[c + 1] === 0 && hasX[c + 1] > 0) {
                totalCount++;
            }
        }
    }
    return totalCount;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numberOfSubmatrices(grid: string[][]): number {
    const rows = grid.length;
    const cols = grid[0].length;
    const diffs = new Int32Array(cols);
    const xCounts = new Int32Array(cols);
    let count = 0;
    for (let i = 0; i < rows; i++) {
        let rowDiff = 0;
        let rowX = 0;
        for (let j = 0; j < cols; j++) {
            const char = grid[i][j];
            if (char === 'X') {
                rowDiff++;
                rowX++;
            } else if (char === 'Y') {
                rowDiff--;
            }
            diffs[j] += rowDiff;
            xCounts[j] += rowX;
            if (xCounts[j] > 0 && diffs[j] === 0) {
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
     * @param String[][] $grid
     * @return Integer
     */
    function numberOfSubmatrices($grid) {
        $rows = count($grid);
        $cols = count($grid[0]);
        $diffs = array_fill(0, $cols, 0);
        $xCounts = array_fill(0, $cols, 0);
        $count = 0;
        for ($i = 0; $i < $rows; $i++) {
            $rowDiff = 0;
            $rowX = 0;
            for ($j = 0; $j < $cols; $j++) {
                $char = $grid[$i][$j];
                if ($char === 'X') {
                    $rowDiff++;
                    $rowX++;
                } else if ($char === 'Y') {
                    $rowDiff--;
                }
                $diffs[$j] += $rowDiff;
                $xCounts[$j] += $rowX;
                if ($xCounts[$j] > 0 && $diffs[$j] === 0) {
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
    func numberOfSubmatrices(_ grid: [[Character]]) -> Int {
        let rows = grid.count
        let cols = grid[0].count
        var diffs = Array(repeating: 0, count: cols)
        var xCounts = Array(repeating: 0, count: cols)
        var count = 0
        for i in 0..<rows {
            var rowDiff = 0
            var rowX = 0
            for j in 0..<cols {
                let char = grid[i][j]
                if char == "X" {
                    rowDiff += 1
                    rowX += 1
                } else if char == "Y" {
                    rowDiff -= 1
                }
                diffs[j] += rowDiff
                xCounts[j] += rowX
                if xCounts[j] > 0 && diffs[j] == 0 {
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
    fun numberOfSubmatrices(grid: Array<CharArray>): Int {
        val rows = grid.size
        val cols = grid[0].size
        val diffs = IntArray(cols)
        val xCounts = IntArray(cols)
        var count = 0
        for (i in 0 until rows) {
            var rowDiff = 0
            var rowX = 0
            for (j in 0 until cols) {
                val char = grid[i][j]
                if (char == 'X') {
                    rowDiff++
                    rowX++
                } else if (char == 'Y') {
                    rowDiff--
                }
                diffs[j] += rowDiff
                xCounts[j] += rowX
                if (xCounts[j] > 0 && diffs[j] == 0) {
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
  int numberOfSubmatrices(List<List<String>> grid) {
    int rows = grid.length;
    int cols = grid[0].length;
    List<int> diffs = List<int>.filled(cols, 0);
    List<int> xCounts = List<int>.filled(cols, 0);
    int count = 0;
    for (int i = 0; i < rows; i++) {
      int rowDiff = 0;
      int rowX = 0;
      for (int j = 0; j < cols; j++) {
        String char = grid[i][j];
        if (char == 'X') {
          rowDiff++;
          rowX++;
        } else if (char == 'Y') {
          rowDiff--;
        }
        diffs[j] += rowDiff;
        xCounts[j] += rowX;
        if (xCounts[j] > 0 && diffs[j] == 0) {
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
func numberOfSubmatrices(grid [][]byte) int {
    rows := len(grid)
    cols := len(grid[0])
    diffs := make([]int, cols)
    xCounts := make([]int, cols)
    count := 0
    for i := 0; i < rows; i++ {
        rowDiff := 0
        rowX := 0
        for j := 0; j < cols; j++ {
            char := grid[i][j]
            if char == 'X' {
                rowDiff++
                rowX++
            } else if char == 'Y' {
                rowDiff--
            }
            diffs[j] += rowDiff
            xCounts[j] += rowX
            if xCounts[j] > 0 && diffs[j] == 0 {
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
def number_of_submatrices(grid)
  rows = grid.length
  cols = grid[0].length
  diff = Array.new(cols + 1, 0)
  has_x = Array.new(cols + 1, 0)
  count = 0
  rows.times do |r|
    row_diff_p = 0
    row_has_x_p = 0
    cols.times do |c|
      char = grid[r][c]
      if char == 'X'
        row_diff_p += 1
        row_has_x_p += 1
      elsif char == 'Y'
        row_diff_p -= 1
      end
      diff[c + 1] += row_diff_p
      has_x[c + 1] += row_has_x_p
      count += 1 if diff[c + 1] == 0 && has_x[c + 1] > 0
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
  def numberOfSubmatrices(grid: Array[Array[Char]]): Int = {
    val rows = grid.length
    val cols = grid(0).length
    val diff = new Array[Int](cols + 1)
    val hasX = new Array[Int](cols + 1)
    var count = 0
    for (r <- 0 until rows) {
      var rowDiffP = 0
      var rowHasXP = 0
      for (c <- 0 until cols) {
        val char = grid(r)(c)
        if (char == 'X') {
          rowDiffP += 1
          rowHasXP += 1
        } else if (char == 'Y') {
          rowDiffP -= 1
        }
        diff(c + 1) += rowDiffP
        hasX(c + 1) += rowHasXP
        if (diff(c + 1) == 0 && hasX(c + 1) > 0) count += 1
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
    pub fn number_of_submatrices(grid: Vec<Vec<char>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        let mut diff = vec![0; cols + 1];
        let mut has_x = vec![0; cols + 1];
        let mut count = 0;
        for r in 0..rows {
            let mut row_diff_p = 0;
            let mut row_has_x_p = 0;
            for c in 0..cols {
                match grid[r][c] {
                    'X' => {
                        row_diff_p += 1;
                        row_has_x_p += 1;
                    }
                    'Y' => {
                        row_diff_p -= 1;
                    }
                    _ => {}
                }
                diff[c + 1] += row_diff_p;
                has_x[c + 1] += row_has_x_p;
                if diff[c + 1] == 0 && has_x[c + 1] > 0 {
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
(define/contract (number-of-submatrices grid)
  (-> (listof (listof char?)) exact-integer?)
  (let* ([rows (length grid)]
         [cols (length (car grid))]
         [diff (make-vector (+ cols 1) 0)]
         [has-x (make-vector (+ cols 1) 0)])
    (let ([count 0])
      (for ([row-list grid])
        (let ([row-diff-p 0]
              [row-has-x-p 0])
          (for ([char row-list]
                [c (in-range cols)])
            (cond
              [(char=? char #\X)
               (set! row-diff-p (+ row-diff-p 1))
               (set! row-has-x-p (+ row-has-x-p 1))]
              [(char=? char #\Y)
               (set! row-diff-p (- row-diff-p 1))]
              [else (void)])
            (let ([new-diff (+ (vector-ref diff (+ c 1)) row-diff-p)]
                  [new-has-x (+ (vector-ref has-x (+ c 1)) row-has-x-p)])
              (vector-set! diff (+ c 1) new-diff)
              (vector-set! has-x (+ c 1) new-has-x)
              (when (and (= new-diff 0) (> new-has-x 0))
                (set! count (+ count 1)))))))
      count)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec number_of_submatrices(Grid :: [[char()]]) -> integer().
number_of_submatrices(Grid) ->
  Cols = length(hd(Grid)),
  compute(Grid, erlang:make_tuple(Cols + 1, 0), erlang:make_tuple(Cols + 1, 0), 0).

compute([], _, _, TotalCount) -> TotalCount;
compute([Row | Rest], PrevDiffRow, PrevHasXRow, TotalCount) ->
  {NewDiffRow, NewHasXRow, RowCount} = process_row(Row, 1, 0, 0, PrevDiffRow, PrevHasXRow, [], [], 0),
  compute(Rest, NewDiffRow, NewHasXRow, TotalCount + RowCount).

process_row([], _, _, _, _, _, AccDiff, AccHasX, RowCount) ->
  {list_to_tuple([0 | lists:reverse(AccDiff)]), list_to_tuple([0 | lists:reverse(AccHasX)]), RowCount};
process_row([Char | Rest], ColIdx, CurrDiffP, CurrHasXP, PrevDiffRow, PrevHasXRow, AccD, AccH, RowCount) ->
  {VD, VX} = case Char of $X -> {1, 1}; $Y -> {-1, 0}; $. -> {0, 0} end,
  NewDiffP = CurrDiffP + VD,
  NewHasXP = CurrHasXP + VX,
  TotalDiff = NewDiffP + element(ColIdx + 1, PrevDiffRow),
  TotalHasX = NewHasXP + element(ColIdx + 1, PrevHasXRow),
  NewCount = if (TotalDiff == 0) and (TotalHasX > 0) -> RowCount + 1; true -> RowCount end,
  process_row(Rest, ColIdx + 1, NewDiffP, NewHasXP, PrevDiffRow, PrevHasXRow, [TotalDiff | AccD], [TotalHasX | AccH], NewCount).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec number_of_submatrices(grid :: [[char]]) :: integer
  def number_of_submatrices(grid) do
    cols = length(hd(grid))
    initial = {List.to_tuple(List.duplicate(0, cols + 1)), List.to_tuple(List.duplicate(0, cols + 1)), 0}
    {_, _, total_count} = Enum.reduce(grid, initial, fn row, {prev_d, prev_h, acc} ->
      {new_d, new_h, row_count} = process_row(row, 0, 0, 0, prev_d, prev_h, [], [], 0)
      {new_d, new_h, acc + row_count}
    end)
    total_count
  end

  defp process_row([], _, _, _, _, _, acc_d, acc_h, row_count) do
    {List.to_tuple([0 | Enum.reverse(acc_d)]), List.to_tuple([0 | Enum.reverse(acc_h)]), row_count}
  end

  defp process_row([char | rest], c_idx, cdp, chxp, prev_d, prev_h, acc_d, acc_h, row_count) do
    {v_d, v_x} = case char do
      ?X -> {1, 1}
      ?Y -> {-1, 0}
      ?. -> {0, 0}
    end
    new_cdp = cdp + v_d
    new_chxp = chxp + v_x
    total_d = new_cdp + elem(prev_d, c_idx + 1)
    total_h = new_chxp + elem(prev_h, c_idx + 1)
    new_row_count = row_count + (if total_d == 0 and total_h > 0, do: 1, else: 0)
    process_row(rest, c_idx + 1, new_cdp, new_chxp, prev_d, prev_h, [total_d | acc_d], [total_h | acc_h], new_row_count)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(R * C) where R is the number of rows and C is the number of columns. We traverse every cell of the grid exactly once, performing constant time calculations for prefix sums at each step.
- **Space Complexity:** O(C) where C is the number of columns. By processing the grid row by row, we only need 1D arrays to store the cumulative sums from the top down to the current row.
