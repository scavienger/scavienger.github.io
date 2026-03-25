---
layout: post
title: "Equal Sum Grid Partition I"
date: 2026-03-25 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Matrix", "Enumeration", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/equal-sum-grid-partition-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool canPartitionGrid(vector<vector<int>>&\
        \ grid) {\n        int m = grid.size();\n        int n = grid[0].size();\n \
        \       long long totalSum = 0;\n        vector<long long> rowSums(m, 0);\n\
        \        for (int i = 0; i < m; ++i) {\n            for (int j = 0; j < n; ++j)\
        \ {\n                rowSums[i] += grid[i][j];\n            }\n            totalSum\
        \ += rowSums[i];\n        }\n\n        if (totalSum % 2 != 0) return false;\n\
        \        long long target = totalSum / 2;\n        long long currentSum = 0;\n\
        \n        for (int i = 0; i < m - 1; ++i) {\n            currentSum += rowSums[i];\n\
        \            if (currentSum == target) return true;\n        }\n\n        currentSum\
        \ = 0;\n        for (int j = 0; j < n - 1; ++j) {\n            long long colSum\
        \ = 0;\n            for (int i = 0; i < m; ++i) {\n                colSum +=\
        \ grid[i][j];\n            }\n            currentSum += colSum;\n          \
        \  if (currentSum == target) return true;\n        }\n\n        return false;\n\
        \    }\n};"
      java: "class Solution {\n    public boolean canPartitionGrid(int[][] grid) {\n\
        \        int m = grid.length;\n        int n = grid[0].length;\n        long\
        \ totalSum = 0;\n        long[] rowSums = new long[m];\n        for (int i =\
        \ 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n            \
        \    rowSums[i] += grid[i][j];\n            }\n            totalSum += rowSums[i];\n\
        \        }\n\n        if (totalSum % 2 != 0) return false;\n        long target\
        \ = totalSum / 2;\n        long currentSum = 0;\n\n        for (int i = 0; i\
        \ < m - 1; i++) {\n            currentSum += rowSums[i];\n            if (currentSum\
        \ == target) return true;\n        }\n\n        currentSum = 0;\n        for\
        \ (int j = 0; j < n - 1; j++) {\n            long colSum = 0;\n            for\
        \ (int i = 0; i < m; i++) {\n                colSum += grid[i][j];\n       \
        \     }\n            currentSum += colSum;\n            if (currentSum == target)\
        \ return true;\n        }\n\n        return false;\n    }\n}"
      python: "class Solution(object):\n    def canPartitionGrid(self, grid):\n    \
        \    \"\"\"\n        :type grid: List[List[int]]\n        :rtype: bool\n   \
        \     \"\"\"\n        m = len(grid)\n        n = len(grid[0])\n        row_sums\
        \ = [sum(row) for row in grid]\n        total_sum = sum(row_sums)\n\n      \
        \  if total_sum % 2 != 0:\n            return False\n\n        target = total_sum\
        \ // 2\n        current_sum = 0\n        for i in range(m - 1):\n          \
        \  current_sum += row_sums[i]\n            if current_sum == target:\n     \
        \           return True\n\n        current_sum = 0\n        for j in range(n\
        \ - 1):\n            col_sum = sum(grid[i][j] for i in range(m))\n         \
        \   current_sum += col_sum\n            if current_sum == target:\n        \
        \        return True\n\n        return False"
      python3: "class Solution:\n    def canPartitionGrid(self, grid: List[List[int]])\
        \ -> bool:\n        m = len(grid)\n        n = len(grid[0])\n        row_sums\
        \ = [sum(row) for row in grid]\n        total_sum = sum(row_sums)\n\n      \
        \  if total_sum % 2 != 0:\n            return False\n\n        target = total_sum\
        \ // 2\n        current_sum = 0\n        for i in range(m - 1):\n          \
        \  current_sum += row_sums[i]\n            if current_sum == target:\n     \
        \           return True\n\n        current_sum = 0\n        for j in range(n\
        \ - 1):\n            col_sum = sum(grid[i][j] for i in range(m))\n         \
        \   current_sum += col_sum\n            if current_sum == target:\n        \
        \        return True\n\n        return False"
      c: "bool canPartitionGrid(int** grid, int gridSize, int* gridColSize) {\n    int\
        \ m = gridSize;\n    int n = gridColSize[0];\n    long long totalSum = 0;\n\
        \    long long* rowSums = (long long*)malloc(m * sizeof(long long));\n\n   \
        \ for (int i = 0; i < m; i++) {\n        rowSums[i] = 0;\n        for (int j\
        \ = 0; j < n; j++) {\n            rowSums[i] += grid[i][j];\n        }\n   \
        \     totalSum += rowSums[i];\n    }\n\n    if (totalSum % 2 == 0) {\n     \
        \   long long target = totalSum / 2;\n        long long currentSum = 0;\n\n\
        \        for (int i = 0; i < m - 1; i++) {\n            currentSum += rowSums[i];\n\
        \            if (currentSum == target) {\n                free(rowSums);\n \
        \               return true;\n            }\n        }\n\n        currentSum\
        \ = 0;\n        for (int j = 0; j < n - 1; j++) {\n            long long colSum\
        \ = 0;\n            for (int i = 0; i < m; i++) {\n                colSum +=\
        \ grid[i][j];\n            }\n            currentSum += colSum;\n          \
        \  if (currentSum == target) {\n                free(rowSums);\n           \
        \     return true;\n            }\n        }\n    }\n\n    free(rowSums);\n\
        \    return false;\n}"
      csharp: "public class Solution {\n    public bool CanPartitionGrid(int[][] grid)\
        \ {\n        int m = grid.Length;\n        int n = grid[0].Length;\n       \
        \ long totalSum = 0;\n        long[] rowSums = new long[m];\n\n        for (int\
        \ i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n        \
        \        rowSums[i] += grid[i][j];\n            }\n            totalSum += rowSums[i];\n\
        \        }\n\n        if (totalSum % 2 != 0) return false;\n        long target\
        \ = totalSum / 2;\n        long currentSum = 0;\n\n        for (int i = 0; i\
        \ < m - 1; i++) {\n            currentSum += rowSums[i];\n            if (currentSum\
        \ == target) return true;\n        }\n\n        currentSum = 0;\n        for\
        \ (int j = 0; j < n - 1; j++) {\n            long colSum = 0;\n            for\
        \ (int i = 0; i < m; i++) {\n                colSum += grid[i][j];\n       \
        \     }\n            currentSum += colSum;\n            if (currentSum == target)\
        \ return true;\n        }\n\n        return false;\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @return {boolean}\n */\nvar\
        \ canPartitionGrid = function(grid) {\n    const m = grid.length;\n    const\
        \ n = grid[0].length;\n    let totalSum = 0;\n    const rowSums = new Array(m).fill(0);\n\
        \n    for (let i = 0; i < m; i++) {\n        for (let j = 0; j < n; j++) {\n\
        \            rowSums[i] += grid[i][j];\n        }\n        totalSum += rowSums[i];\n\
        \    }\n\n    if (totalSum % 2 !== 0) return false;\n    const target = totalSum\
        \ / 2;\n    let currentSum = 0;\n\n    for (let i = 0; i < m - 1; i++) {\n \
        \       currentSum += rowSums[i];\n        if (currentSum === target) return\
        \ true;\n    }\n\n    currentSum = 0;\n    for (let j = 0; j < n - 1; j++) {\n\
        \        let colSum = 0;\n        for (let i = 0; i < m; i++) {\n          \
        \  colSum += grid[i][j];\n        }\n        currentSum += colSum;\n       \
        \ if (currentSum === target) return true;\n    }\n\n    return false;\n};"
      typescript: "function canPartitionGrid(grid: number[][]): boolean {\n    const\
        \ m = grid.length;\n    const n = grid[0].length;\n    let totalSum = 0;\n \
        \   const rowSums = new Array(m).fill(0);\n    const colSums = new Array(n).fill(0);\n\
        \n    for (let i = 0; i < m; i++) {\n        const row = grid[i];\n        for\
        \ (let j = 0; j < n; j++) {\n            const val = row[j];\n            rowSums[i]\
        \ += val;\n            colSums[j] += val;\n            totalSum += val;\n  \
        \      }\n    }\n\n    if (totalSum % 2 !== 0) return false;\n    const target\
        \ = totalSum / 2;\n\n    let curR = 0;\n    for (let i = 0; i < m - 1; i++)\
        \ {\n        curR += rowSums[i];\n        if (curR === target) return true;\n\
        \    }\n\n    let curC = 0;\n    for (let j = 0; j < n - 1; j++) {\n       \
        \ curC += colSums[j];\n        if (curC === target) return true;\n    }\n\n\
        \    return false;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @return\
        \ Boolean\n     */\n    function canPartitionGrid($grid) {\n        $m = count($grid);\n\
        \        $n = count($grid[0]);\n        $totalSum = 0;\n        $rowSums = array_fill(0,\
        \ $m, 0);\n        $colSums = array_fill(0, $n, 0);\n\n        for ($i = 0;\
        \ $i < $m; $i++) {\n            $row = $grid[$i];\n            for ($j = 0;\
        \ $j < $n; $j++) {\n                $val = $row[$j];\n                $rowSums[$i]\
        \ += $val;\n                $colSums[$j] += $val;\n                $totalSum\
        \ += $val;\n            }\n        }\n\n        if ($totalSum % 2 !== 0) return\
        \ false;\n        $target = $totalSum / 2;\n\n        $curR = 0;\n        for\
        \ ($i = 0; $i < $m - 1; $i++) {\n            $curR += $rowSums[$i];\n      \
        \      if ($curR == $target) return true;\n        }\n\n        $curC = 0;\n\
        \        for ($j = 0; $j < $n - 1; $j++) {\n            $curC += $colSums[$j];\n\
        \            if ($curC == $target) return true;\n        }\n\n        return\
        \ false;\n    }\n}"
      swift: "class Solution {\n    func canPartitionGrid(_ grid: [[Int]]) -> Bool {\n\
        \        let m = grid.count\n        let n = grid[0].count\n        var totalSum\
        \ = 0\n        var rowSums = Array(repeating: 0, count: m)\n        var colSums\
        \ = Array(repeating: 0, count: n)\n\n        for i in 0..<m {\n            let\
        \ row = grid[i]\n            for j in 0..<n {\n                let val = row[j]\n\
        \                rowSums[i] += val\n                colSums[j] += val\n    \
        \            totalSum += val\n            }\n        }\n\n        if totalSum\
        \ % 2 != 0 { return false }\n        let target = totalSum / 2\n\n        var\
        \ curR = 0\n        for i in 0..<(m - 1) {\n            curR += rowSums[i]\n\
        \            if curR == target { return true }\n        }\n\n        var curC\
        \ = 0\n        for j in 0..<(n - 1) {\n            curC += colSums[j]\n    \
        \        if curC == target { return true }\n        }\n\n        return false\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun canPartitionGrid(grid: Array<IntArray>): Boolean\
        \ {\n        val m = grid.size\n        val n = grid[0].size\n        var totalSum:\
        \ Long = 0\n        val rowSums = LongArray(m)\n        val colSums = LongArray(n)\n\
        \n        for (i in 0 until m) {\n            val row = grid[i]\n          \
        \  for (j in 0 until n) {\n                val value = row[j].toLong()\n   \
        \             rowSums[i] += value\n                colSums[j] += value\n   \
        \             totalSum += value\n            }\n        }\n\n        if (totalSum\
        \ % 2 != 0L) return false\n        val target = totalSum / 2\n\n        var\
        \ curR: Long = 0\n        for (i in 0 until m - 1) {\n            curR += rowSums[i]\n\
        \            if (curR == target) return true\n        }\n\n        var curC:\
        \ Long = 0\n        for (j in 0 until n - 1) {\n            curC += colSums[j]\n\
        \            if (curC == target) return true\n        }\n\n        return false\n\
        \    }\n}"
      dart: "class Solution {\n  bool canPartitionGrid(List<List<int>> grid) {\n   \
        \ int m = grid.length;\n    int n = grid[0].length;\n    int totalSum = 0;\n\
        \    List<int> rowSums = List.filled(m, 0);\n    List<int> colSums = List.filled(n,\
        \ 0);\n\n    for (int i = 0; i < m; i++) {\n      List<int> row = grid[i];\n\
        \      for (int j = 0; j < n; j++) {\n        int val = row[j];\n        rowSums[i]\
        \ += val;\n        colSums[j] += val;\n        totalSum += val;\n      }\n \
        \   }\n\n    if (totalSum % 2 != 0) return false;\n    int target = totalSum\
        \ ~/ 2;\n\n    int curR = 0;\n    for (int i = 0; i < m - 1; i++) {\n      curR\
        \ += rowSums[i];\n      if (curR == target) return true;\n    }\n\n    int curC\
        \ = 0;\n    for (int j = 0; j < n - 1; j++) {\n      curC += colSums[j];\n \
        \     if (curC == target) return true;\n    }\n\n    return false;\n  }\n}"
      go: "func canPartitionGrid(grid [][]int) bool {\n    m := len(grid)\n    n :=\
        \ len(grid[0])\n    var totalSum int64\n    rowSums := make([]int64, m)\n  \
        \  colSums := make([]int64, n)\n\n    for i := 0; i < m; i++ {\n        row\
        \ := grid[i]\n        for j := 0; j < n; j++ {\n            val := int64(row[j])\n\
        \            rowSums[i] += val\n            colSums[j] += val\n            totalSum\
        \ += val\n        }\n    }\n\n    if totalSum%2 != 0 {\n        return false\n\
        \    }\n\n    target := totalSum / 2\n    var curR int64\n    for i := 0; i\
        \ < m-1; i++ {\n        curR += rowSums[i]\n        if curR == target {\n  \
        \          return true\n        }\n    }\n\n    var curC int64\n    for j :=\
        \ 0; j < n-1; j++ {\n        curC += colSums[j]\n        if curC == target {\n\
        \            return true\n        }\n    }\n\n    return false\n}"
      ruby: "def can_partition_grid(grid)\n  m = grid.length\n  n = grid[0].length\n\
        \  row_sums = Array.new(m, 0)\n  col_sums = Array.new(n, 0)\n  total_sum = 0\n\
        \  grid.each_with_index do |row, i|\n    r_sum = 0\n    row.each_with_index\
        \ do |val, j|\n      r_sum += val\n      col_sums[j] += val\n    end\n    row_sums[i]\
        \ = r_sum\n    total_sum += r_sum\n  end\n  return false if total_sum % 2 !=\
        \ 0\n  target = total_sum / 2\n  acc = 0\n  (0...(m - 1)).each do |i|\n    acc\
        \ += row_sums[i]\n    return true if acc == target\n  end\n  acc = 0\n  (0...(n\
        \ - 1)).each do |j|\n    acc += col_sums[j]\n    return true if acc == target\n\
        \  end\n  false\nend"
      scala: "object Solution {\n    def canPartitionGrid(grid: Array[Array[Int]]):\
        \ Boolean = {\n        val m = grid.length\n        val n = grid(0).length\n\
        \        val rowSums = new Array[Long](m)\n        val colSums = new Array[Long](n)\n\
        \        var totalSum: Long = 0\n\n        for (i <- 0 until m) {\n        \
        \    var rSum: Long = 0\n            for (j <- 0 until n) {\n              \
        \  val v = grid(i)(j).toLong\n                rSum += v\n                colSums(j)\
        \ += v\n            }\n            rowSums(i) = rSum\n            totalSum +=\
        \ rSum\n        }\n\n        if (totalSum % 2 != 0) return false\n        val\
        \ target = totalSum / 2\n\n        var currentAcc: Long = 0\n        for (i\
        \ <- 0 until m - 1) {\n            currentAcc += rowSums(i)\n            if\
        \ (currentAcc == target) return true\n        }\n\n        currentAcc = 0\n\
        \        for (j <- 0 until n - 1) {\n            currentAcc += colSums(j)\n\
        \            if (currentAcc == target) return true\n        }\n\n        false\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn can_partition_grid(grid: Vec<Vec<i32>>) ->\
        \ bool {\n        let m = grid.len();\n        let n = grid[0].len();\n    \
        \    let mut total_sum: i64 = 0;\n        let mut row_sums = vec![0i64; m];\n\
        \        let mut col_sums = vec![0i64; n];\n\n        for i in 0..m {\n    \
        \        let mut r_sum: i64 = 0;\n            for j in 0..n {\n            \
        \    let val = grid[i][j] as i64;\n                r_sum += val;\n         \
        \       col_sums[j] += val;\n            }\n            row_sums[i] = r_sum;\n\
        \            total_sum += r_sum;\n        }\n\n        if total_sum % 2 != 0\
        \ {\n            return false;\n        }\n        let target = total_sum /\
        \ 2;\n\n        let mut acc = 0i64;\n        for i in 0..m - 1 {\n         \
        \   acc += row_sums[i];\n            if acc == target {\n                return\
        \ true;\n            }\n        }\n\n        acc = 0i64;\n        for j in 0..n\
        \ - 1 {\n            acc += col_sums[j];\n            if acc == target {\n \
        \               return true;\n            }\n        }\n\n        false\n  \
        \  }\n}"
      racket: "(define/contract (can-partition-grid grid)\n  (-> (listof (listof exact-integer?))\
        \ boolean?)\n  (let* ([row-sums (map (lambda (r) (apply + r)) grid)]\n     \
        \    [total-sum (apply + row-sums)])\n    (if (odd? total-sum)\n        #f\n\
        \        (let ([target (/ total-sum 2)]\n              [col-sums (apply map\
        \ + grid)])\n          (or (check-partition row-sums target)\n             \
        \ (check-partition col-sums target))))))\n\n(define (check-partition sums target)\n\
        \  (if (<= (length sums) 1)\n      #f\n      (let loop ([lst (take sums (- (length\
        \ sums) 1))]\n                 [acc 0])\n        (cond\n          [(empty? lst)\
        \ #f]\n          [(= (+ acc (car lst)) target) #t]\n          [else (loop (cdr\
        \ lst) (+ acc (car lst)))]))))"
      erlang: "can_partition_grid(Grid) ->\n    RowSums = [lists:foldl(fun(X, Acc) ->\
        \ X + Acc end, 0, Row) || Row <- Grid],\n    TotalSum = lists:foldl(fun(X, Acc)\
        \ -> X + Acc end, 0, RowSums),\n    case TotalSum rem 2 of\n        1 -> false;\n\
        \        0 ->\n            Target = TotalSum div 2,\n            ColSums = col_sums(Grid),\n\
        \            check_partition(RowSums, Target) orelse check_partition(ColSums,\
        \ Target)\n    end.\n\ncheck_partition(Sums, Target) ->\n    case Sums of\n\
        \        [] -> false;\n        [_Last] -> false;\n        [H|T] -> check_partition_rec(T,\
        \ H, Target)\n    end.\n\ncheck_partition_rec([], _Acc, _Target) -> false;\n\
        check_partition_rec([_Last], Acc, Target) -> Acc == Target;\ncheck_partition_rec([H|T],\
        \ Acc, Target) ->\n    if Acc == Target -> true;\n       true -> check_partition_rec(T,\
        \ Acc + H, Target)\n    end.\n\ncol_sums([H|T]) ->\n    lists:foldl(\n     \
        \   fun(Row, Acc) -> lists:zipwith(fun(X, Y) -> X + Y end, Row, Acc) end,\n\
        \        H,\n        T\n    )."
      elixir: "defmodule Solution do\n  @spec can_partition_grid(grid :: [[integer]])\
        \ :: boolean\n  def can_partition_grid(grid) do\n    row_sums = Enum.map(grid,\
        \ fn row -> Enum.sum(row) end)\n    total_sum = Enum.sum(row_sums)\n\n    if\
        \ rem(total_sum, 2) != 0 do\n      false\n    else\n      target = div(total_sum,\
        \ 2)\n      col_sums = Enum.zip_with(grid, &Enum.sum/1)\n      check_partition(row_sums,\
        \ target) or check_partition(col_sums, target)\n    end\n  end\n\n  defp check_partition(sums,\
        \ target) do\n    if Enum.count(sums) <= 1 do\n      false\n    else\n     \
        \ sums\n      |> Enum.slice(0, Enum.count(sums) - 1)\n      |> Enum.reduce_while(0,\
        \ fn x, acc ->\n        new_acc = acc + x\n        if new_acc == target, do:\
        \ {:halt, true}, else: {:cont, new_acc}\n      end) == true\n    end\n  end\n\
        end"
    approach: 'The algorithm first computes the total sum of all elements in the grid
      and pre-calculates the sum of each row. Since we are looking for a partition into
      two equal sums, the target sum for each section must be exactly half of the total
      sum. If the total sum is odd, a partition is impossible because all grid elements
      are integers, so we immediately return false.


      To check for a horizontal cut, we iterate through the row sums and maintain a
      running prefix sum; if this sum matches the target at any index before the final
      row, a valid partition exists. If no horizontal cut is found, we perform a similar
      check for vertical cuts by iterating through each column, calculating its sum,
      and updating a running prefix sum of column totals. This approach ensures all
      potential cuts are evaluated while staying efficient within the constraints.'
    time_complexity: O(m * n), where m is the number of rows and n is the number of
      columns. Calculating the total sum and row sums requires a single traversal of
      the grid, and checking for a vertical cut requires an additional column-wise traversal
      of the grid. Both operations are proportional to the total number of cells in
      the grid.
    space_complexity: O(m), where m is the number of rows. This space is used to store
      the individual row sums. The column sums are computed and added to a running prefix
      sum one by one, avoiding the need for additional $O(n)$ storage beyond the input
      grid.
    elapsed_time: 210.287691116333
    model: gemini-3-flash-preview
    generated_at: '2026-03-25 01:30:05 '
---

## Problem #3546: Equal Sum Grid Partition I

**Difficulty:** Medium

**Topics:** Array, Matrix, Enumeration, Prefix Sum

## Problem Description

<p>You are given an <code>m x n</code> matrix <code>grid</code> of positive integers. Your task is to determine if it is possible to make <strong>either one horizontal or one vertical cut</strong> on the grid such that:</p>

<ul>
	<li>Each of the two resulting sections formed by the cut is <strong>non-empty</strong>.</li>
	<li>The sum of the elements in both sections is <strong>equal</strong>.</li>
</ul>

<p>Return <code>true</code> if such a partition exists; otherwise return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,4],[2,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/03/30/lc.png" style="width: 200px;" /><img alt="" src="https://assets.leetcode.com/uploads/2025/03/30/lc.jpeg" style="width: 200px; height: 200px;" /></p>

<p>A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is <code>true</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,3],[2,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is <code>false</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m == grid.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= n == grid[i].length &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. There are two types of cuts: a `horizontal` cut or a `vertical` cut.

2. For a `horizontal` cut at row `r` (0 <= r <m - 1), split `grid` into rows 0...r vs. r+1...m-1 and compare their sums.

3. For a `vertical` cut at column `c` (0 <= c < n - 1), split `grid` into columns 0...c vs. c+1...n-1 and compare their sums.

4. Brute‑force all possible `r` and `c` cuts; if any yields equal section sums, return `true`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm first computes the total sum of all elements in the grid and pre-calculates the sum of each row. Since we are looking for a partition into two equal sums, the target sum for each section must be exactly half of the total sum. If the total sum is odd, a partition is impossible because all grid elements are integers, so we immediately return false.

To check for a horizontal cut, we iterate through the row sums and maintain a running prefix sum; if this sum matches the target at any index before the final row, a valid partition exists. If no horizontal cut is found, we perform a similar check for vertical cuts by iterating through each column, calculating its sum, and updating a running prefix sum of column totals. This approach ensures all potential cuts are evaluated while staying efficient within the constraints.

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
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        long long totalSum = 0;
        vector<long long> rowSums(m, 0);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                rowSums[i] += grid[i][j];
            }
            totalSum += rowSums[i];
        }

        if (totalSum % 2 != 0) return false;
        long long target = totalSum / 2;
        long long currentSum = 0;

        for (int i = 0; i < m - 1; ++i) {
            currentSum += rowSums[i];
            if (currentSum == target) return true;
        }

        currentSum = 0;
        for (int j = 0; j < n - 1; ++j) {
            long long colSum = 0;
            for (int i = 0; i < m; ++i) {
                colSum += grid[i][j];
            }
            currentSum += colSum;
            if (currentSum == target) return true;
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
    public boolean canPartitionGrid(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        long totalSum = 0;
        long[] rowSums = new long[m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                rowSums[i] += grid[i][j];
            }
            totalSum += rowSums[i];
        }

        if (totalSum % 2 != 0) return false;
        long target = totalSum / 2;
        long currentSum = 0;

        for (int i = 0; i < m - 1; i++) {
            currentSum += rowSums[i];
            if (currentSum == target) return true;
        }

        currentSum = 0;
        for (int j = 0; j < n - 1; j++) {
            long colSum = 0;
            for (int i = 0; i < m; i++) {
                colSum += grid[i][j];
            }
            currentSum += colSum;
            if (currentSum == target) return true;
        }

        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        row_sums = [sum(row) for row in grid]
        total_sum = sum(row_sums)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        current_sum = 0
        for i in range(m - 1):
            current_sum += row_sums[i]
            if current_sum == target:
                return True

        current_sum = 0
        for j in range(n - 1):
            col_sum = sum(grid[i][j] for i in range(m))
            current_sum += col_sum
            if current_sum == target:
                return True

        return False
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        row_sums = [sum(row) for row in grid]
        total_sum = sum(row_sums)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        current_sum = 0
        for i in range(m - 1):
            current_sum += row_sums[i]
            if current_sum == target:
                return True

        current_sum = 0
        for j in range(n - 1):
            col_sum = sum(grid[i][j] for i in range(m))
            current_sum += col_sum
            if current_sum == target:
                return True

        return False
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool canPartitionGrid(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];
    long long totalSum = 0;
    long long* rowSums = (long long*)malloc(m * sizeof(long long));

    for (int i = 0; i < m; i++) {
        rowSums[i] = 0;
        for (int j = 0; j < n; j++) {
            rowSums[i] += grid[i][j];
        }
        totalSum += rowSums[i];
    }

    if (totalSum % 2 == 0) {
        long long target = totalSum / 2;
        long long currentSum = 0;

        for (int i = 0; i < m - 1; i++) {
            currentSum += rowSums[i];
            if (currentSum == target) {
                free(rowSums);
                return true;
            }
        }

        currentSum = 0;
        for (int j = 0; j < n - 1; j++) {
            long long colSum = 0;
            for (int i = 0; i < m; i++) {
                colSum += grid[i][j];
            }
            currentSum += colSum;
            if (currentSum == target) {
                free(rowSums);
                return true;
            }
        }
    }

    free(rowSums);
    return false;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool CanPartitionGrid(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        long totalSum = 0;
        long[] rowSums = new long[m];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                rowSums[i] += grid[i][j];
            }
            totalSum += rowSums[i];
        }

        if (totalSum % 2 != 0) return false;
        long target = totalSum / 2;
        long currentSum = 0;

        for (int i = 0; i < m - 1; i++) {
            currentSum += rowSums[i];
            if (currentSum == target) return true;
        }

        currentSum = 0;
        for (int j = 0; j < n - 1; j++) {
            long colSum = 0;
            for (int i = 0; i < m; i++) {
                colSum += grid[i][j];
            }
            currentSum += colSum;
            if (currentSum == target) return true;
        }

        return false;
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
 * @return {boolean}
 */
var canPartitionGrid = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    let totalSum = 0;
    const rowSums = new Array(m).fill(0);

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            rowSums[i] += grid[i][j];
        }
        totalSum += rowSums[i];
    }

    if (totalSum % 2 !== 0) return false;
    const target = totalSum / 2;
    let currentSum = 0;

    for (let i = 0; i < m - 1; i++) {
        currentSum += rowSums[i];
        if (currentSum === target) return true;
    }

    currentSum = 0;
    for (let j = 0; j < n - 1; j++) {
        let colSum = 0;
        for (let i = 0; i < m; i++) {
            colSum += grid[i][j];
        }
        currentSum += colSum;
        if (currentSum === target) return true;
    }

    return false;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function canPartitionGrid(grid: number[][]): boolean {
    const m = grid.length;
    const n = grid[0].length;
    let totalSum = 0;
    const rowSums = new Array(m).fill(0);
    const colSums = new Array(n).fill(0);

    for (let i = 0; i < m; i++) {
        const row = grid[i];
        for (let j = 0; j < n; j++) {
            const val = row[j];
            rowSums[i] += val;
            colSums[j] += val;
            totalSum += val;
        }
    }

    if (totalSum % 2 !== 0) return false;
    const target = totalSum / 2;

    let curR = 0;
    for (let i = 0; i < m - 1; i++) {
        curR += rowSums[i];
        if (curR === target) return true;
    }

    let curC = 0;
    for (let j = 0; j < n - 1; j++) {
        curC += colSums[j];
        if (curC === target) return true;
    }

    return false;
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
     * @return Boolean
     */
    function canPartitionGrid($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $totalSum = 0;
        $rowSums = array_fill(0, $m, 0);
        $colSums = array_fill(0, $n, 0);

        for ($i = 0; $i < $m; $i++) {
            $row = $grid[$i];
            for ($j = 0; $j < $n; $j++) {
                $val = $row[$j];
                $rowSums[$i] += $val;
                $colSums[$j] += $val;
                $totalSum += $val;
            }
        }

        if ($totalSum % 2 !== 0) return false;
        $target = $totalSum / 2;

        $curR = 0;
        for ($i = 0; $i < $m - 1; $i++) {
            $curR += $rowSums[$i];
            if ($curR == $target) return true;
        }

        $curC = 0;
        for ($j = 0; $j < $n - 1; $j++) {
            $curC += $colSums[$j];
            if ($curC == $target) return true;
        }

        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func canPartitionGrid(_ grid: [[Int]]) -> Bool {
        let m = grid.count
        let n = grid[0].count
        var totalSum = 0
        var rowSums = Array(repeating: 0, count: m)
        var colSums = Array(repeating: 0, count: n)

        for i in 0..<m {
            let row = grid[i]
            for j in 0..<n {
                let val = row[j]
                rowSums[i] += val
                colSums[j] += val
                totalSum += val
            }
        }

        if totalSum % 2 != 0 { return false }
        let target = totalSum / 2

        var curR = 0
        for i in 0..<(m - 1) {
            curR += rowSums[i]
            if curR == target { return true }
        }

        var curC = 0
        for j in 0..<(n - 1) {
            curC += colSums[j]
            if curC == target { return true }
        }

        return false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun canPartitionGrid(grid: Array<IntArray>): Boolean {
        val m = grid.size
        val n = grid[0].size
        var totalSum: Long = 0
        val rowSums = LongArray(m)
        val colSums = LongArray(n)

        for (i in 0 until m) {
            val row = grid[i]
            for (j in 0 until n) {
                val value = row[j].toLong()
                rowSums[i] += value
                colSums[j] += value
                totalSum += value
            }
        }

        if (totalSum % 2 != 0L) return false
        val target = totalSum / 2

        var curR: Long = 0
        for (i in 0 until m - 1) {
            curR += rowSums[i]
            if (curR == target) return true
        }

        var curC: Long = 0
        for (j in 0 until n - 1) {
            curC += colSums[j]
            if (curC == target) return true
        }

        return false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool canPartitionGrid(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    int totalSum = 0;
    List<int> rowSums = List.filled(m, 0);
    List<int> colSums = List.filled(n, 0);

    for (int i = 0; i < m; i++) {
      List<int> row = grid[i];
      for (int j = 0; j < n; j++) {
        int val = row[j];
        rowSums[i] += val;
        colSums[j] += val;
        totalSum += val;
      }
    }

    if (totalSum % 2 != 0) return false;
    int target = totalSum ~/ 2;

    int curR = 0;
    for (int i = 0; i < m - 1; i++) {
      curR += rowSums[i];
      if (curR == target) return true;
    }

    int curC = 0;
    for (int j = 0; j < n - 1; j++) {
      curC += colSums[j];
      if (curC == target) return true;
    }

    return false;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func canPartitionGrid(grid [][]int) bool {
    m := len(grid)
    n := len(grid[0])
    var totalSum int64
    rowSums := make([]int64, m)
    colSums := make([]int64, n)

    for i := 0; i < m; i++ {
        row := grid[i]
        for j := 0; j < n; j++ {
            val := int64(row[j])
            rowSums[i] += val
            colSums[j] += val
            totalSum += val
        }
    }

    if totalSum%2 != 0 {
        return false
    }

    target := totalSum / 2
    var curR int64
    for i := 0; i < m-1; i++ {
        curR += rowSums[i]
        if curR == target {
            return true
        }
    }

    var curC int64
    for j := 0; j < n-1; j++ {
        curC += colSums[j]
        if curC == target {
            return true
        }
    }

    return false
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def can_partition_grid(grid)
  m = grid.length
  n = grid[0].length
  row_sums = Array.new(m, 0)
  col_sums = Array.new(n, 0)
  total_sum = 0
  grid.each_with_index do |row, i|
    r_sum = 0
    row.each_with_index do |val, j|
      r_sum += val
      col_sums[j] += val
    end
    row_sums[i] = r_sum
    total_sum += r_sum
  end
  return false if total_sum % 2 != 0
  target = total_sum / 2
  acc = 0
  (0...(m - 1)).each do |i|
    acc += row_sums[i]
    return true if acc == target
  end
  acc = 0
  (0...(n - 1)).each do |j|
    acc += col_sums[j]
    return true if acc == target
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
    def canPartitionGrid(grid: Array[Array[Int]]): Boolean = {
        val m = grid.length
        val n = grid(0).length
        val rowSums = new Array[Long](m)
        val colSums = new Array[Long](n)
        var totalSum: Long = 0

        for (i <- 0 until m) {
            var rSum: Long = 0
            for (j <- 0 until n) {
                val v = grid(i)(j).toLong
                rSum += v
                colSums(j) += v
            }
            rowSums(i) = rSum
            totalSum += rSum
        }

        if (totalSum % 2 != 0) return false
        val target = totalSum / 2

        var currentAcc: Long = 0
        for (i <- 0 until m - 1) {
            currentAcc += rowSums(i)
            if (currentAcc == target) return true
        }

        currentAcc = 0
        for (j <- 0 until n - 1) {
            currentAcc += colSums(j)
            if (currentAcc == target) return true
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
    pub fn can_partition_grid(grid: Vec<Vec<i32>>) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        let mut total_sum: i64 = 0;
        let mut row_sums = vec![0i64; m];
        let mut col_sums = vec![0i64; n];

        for i in 0..m {
            let mut r_sum: i64 = 0;
            for j in 0..n {
                let val = grid[i][j] as i64;
                r_sum += val;
                col_sums[j] += val;
            }
            row_sums[i] = r_sum;
            total_sum += r_sum;
        }

        if total_sum % 2 != 0 {
            return false;
        }
        let target = total_sum / 2;

        let mut acc = 0i64;
        for i in 0..m - 1 {
            acc += row_sums[i];
            if acc == target {
                return true;
            }
        }

        acc = 0i64;
        for j in 0..n - 1 {
            acc += col_sums[j];
            if acc == target {
                return true;
            }
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
(define/contract (can-partition-grid grid)
  (-> (listof (listof exact-integer?)) boolean?)
  (let* ([row-sums (map (lambda (r) (apply + r)) grid)]
         [total-sum (apply + row-sums)])
    (if (odd? total-sum)
        #f
        (let ([target (/ total-sum 2)]
              [col-sums (apply map + grid)])
          (or (check-partition row-sums target)
              (check-partition col-sums target))))))

(define (check-partition sums target)
  (if (<= (length sums) 1)
      #f
      (let loop ([lst (take sums (- (length sums) 1))]
                 [acc 0])
        (cond
          [(empty? lst) #f]
          [(= (+ acc (car lst)) target) #t]
          [else (loop (cdr lst) (+ acc (car lst)))]))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
can_partition_grid(Grid) ->
    RowSums = [lists:foldl(fun(X, Acc) -> X + Acc end, 0, Row) || Row <- Grid],
    TotalSum = lists:foldl(fun(X, Acc) -> X + Acc end, 0, RowSums),
    case TotalSum rem 2 of
        1 -> false;
        0 ->
            Target = TotalSum div 2,
            ColSums = col_sums(Grid),
            check_partition(RowSums, Target) orelse check_partition(ColSums, Target)
    end.

check_partition(Sums, Target) ->
    case Sums of
        [] -> false;
        [_Last] -> false;
        [H|T] -> check_partition_rec(T, H, Target)
    end.

check_partition_rec([], _Acc, _Target) -> false;
check_partition_rec([_Last], Acc, Target) -> Acc == Target;
check_partition_rec([H|T], Acc, Target) ->
    if Acc == Target -> true;
       true -> check_partition_rec(T, Acc + H, Target)
    end.

col_sums([H|T]) ->
    lists:foldl(
        fun(Row, Acc) -> lists:zipwith(fun(X, Y) -> X + Y end, Row, Acc) end,
        H,
        T
    ).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec can_partition_grid(grid :: [[integer]]) :: boolean
  def can_partition_grid(grid) do
    row_sums = Enum.map(grid, fn row -> Enum.sum(row) end)
    total_sum = Enum.sum(row_sums)

    if rem(total_sum, 2) != 0 do
      false
    else
      target = div(total_sum, 2)
      col_sums = Enum.zip_with(grid, &Enum.sum/1)
      check_partition(row_sums, target) or check_partition(col_sums, target)
    end
  end

  defp check_partition(sums, target) do
    if Enum.count(sums) <= 1 do
      false
    else
      sums
      |> Enum.slice(0, Enum.count(sums) - 1)
      |> Enum.reduce_while(0, fn x, acc ->
        new_acc = acc + x
        if new_acc == target, do: {:halt, true}, else: {:cont, new_acc}
      end) == true
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m * n), where m is the number of rows and n is the number of columns. Calculating the total sum and row sums requires a single traversal of the grid, and checking for a vertical cut requires an additional column-wise traversal of the grid. Both operations are proportional to the total number of cells in the grid.
- **Space Complexity:** O(m), where m is the number of rows. This space is used to store the individual row sums. The column sums are computed and added to a running prefix sum one by one, avoiding the need for additional $O(n)$ storage beyond the input grid.
