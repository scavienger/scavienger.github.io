---
layout: post
title: "Count Negative Numbers in a Sorted Matrix"
date: 2025-12-28 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Binary Search", "Matrix"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int countNegatives(std::vector<std::vector<int>>&\
        \ grid) {\n        int m = grid.size();\n        int n = grid[0].size();\n \
        \       int count = 0;\n        int r = 0;\n        int c = n - 1;\n\n     \
        \   while (r < m && c >= 0) {\n            if (grid[r][c] < 0) {\n         \
        \       count += (m - r);\n                c--;\n            } else {\n    \
        \            r++;\n            }\n        }\n\n        return count;\n    }\n\
        };"
      java: "class Solution {\n    public int countNegatives(int[][] grid) {\n     \
        \   int m = grid.length;\n        int n = grid[0].length;\n        int count\
        \ = 0;\n        int r = 0;\n        int c = n - 1;\n\n        while (r < m &&\
        \ c >= 0) {\n            if (grid[r][c] < 0) {\n                count += (m\
        \ - r);\n                c--;\n            } else {\n                r++;\n\
        \            }\n        }\n\n        return count;\n    }\n}"
      python: "class Solution:\n    def countNegatives(self, grid: List[List[int]])\
        \ -> int:\n        m = len(grid)\n        n = len(grid[0])\n        count =\
        \ 0\n        r = 0\n        c = n - 1\n\n        while r < m and c >= 0:\n \
        \           if grid[r][c] < 0:\n                count += (m - r)\n         \
        \       c -= 1\n            else:\n                r += 1\n\n        return\
        \ count"
      python3: "class Solution:\n    def countNegatives(self, grid: List[List[int]])\
        \ -> int:\n        m = len(grid)\n        n = len(grid[0])\n        count =\
        \ 0\n        r = 0\n        c = n - 1\n\n        while r < m and c >= 0:\n \
        \           if grid[r][c] < 0:\n                count += (m - r)\n         \
        \       c -= 1\n            else:\n                r += 1\n\n        return\
        \ count"
      c: "int countNegatives(int** grid, int gridSize, int* gridColSize) {\n    int\
        \ m = gridSize;\n    int n = gridColSize[0];\n    int count = 0;\n    int r\
        \ = 0;\n    int c = n - 1;\n\n    while (r < m && c >= 0) {\n        if (grid[r][c]\
        \ < 0) {\n            count += (m - r);\n            c--;\n        } else {\n\
        \            r++;\n        }\n    }\n\n    return count;\n}"
      csharp: "public class Solution {\n    public int CountNegatives(int[][] grid)\
        \ {\n        int m = grid.Length;\n        int n = grid[0].Length;\n       \
        \ int count = 0;\n        int r = 0;\n        int c = n - 1;\n\n        while\
        \ (r < m && c >= 0) {\n            if (grid[r][c] < 0) {\n                count\
        \ += (m - r);\n                c--;\n            } else {\n                r++;\n\
        \            }\n        }\n\n        return count;\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @return {number}\n */\nvar countNegatives\
        \ = function(grid) {\n    const m = grid.length;\n    const n = grid[0].length;\n\
        \    let count = 0;\n    let r = 0;\n    let c = n - 1;\n\n    while (r < m\
        \ && c >= 0) {\n        if (grid[r][c] < 0) {\n            count += (m - r);\n\
        \            c--;\n        } else {\n            r++;\n        }\n    }\n\n\
        \    return count;\n};"
      typescript: "function countNegatives(grid: number[][]): number {\n    const m:\
        \ number = grid.length;\n    const n: number = grid[0].length;\n    let count:\
        \ number = 0;\n    let r: number = 0;\n    let c: number = n - 1;\n\n    while\
        \ (r < m && c >= 0) {\n        if (grid[r][c] < 0) {\n            count += (m\
        \ - r);\n            c--;\n        } else {\n            r++;\n        }\n \
        \   }\n\n    return count;\n}"
      php: "class Solution {\n\n    /**\n     * @param int[][] $grid\n     * @return\
        \ int\n     */\n    function countNegatives(array $grid): int {\n        $m\
        \ = count($grid);\n        $n = count($grid[0]);\n        $count = 0;\n    \
        \    $r = 0;\n        $c = $n - 1;\n\n        while ($r < $m && $c >= 0) {\n\
        \            if ($grid[$r][$c] < 0) {\n                $count += ($m - $r);\n\
        \                $c--;\n            } else {\n                $r++;\n      \
        \      }\n        }\n\n        return $count;\n    }\n}"
      swift: "class Solution {\n    func countNegatives(_ grid: [[Int]]) -> Int {\n\
        \        let m = grid.count\n        let n = grid[0].count\n        var count\
        \ = 0\n        var r = 0\n        var c = n - 1\n\n        while r < m && c\
        \ >= 0 {\n            if grid[r][c] < 0 {\n                count += (m - r)\n\
        \                c -= 1\n            } else {\n                r += 1\n    \
        \        }\n        }\n\n        return count\n    }\n}"
      kotlin: "class Solution {\n    fun countNegatives(grid: Array<IntArray>): Int\
        \ {\n        val m = grid.size\n        val n = grid[0].size\n        var count\
        \ = 0\n        var r = 0\n        var c = n - 1\n\n        while (r < m && c\
        \ >= 0) {\n            if (grid[r][c] < 0) {\n                count += (m -\
        \ r)\n                c--\n            } else {\n                r++\n     \
        \       }\n        }\n\n        return count\n    }\n}"
      dart: "class Solution {\n  int countNegatives(List<List<int>> grid) {\n    int\
        \ m = grid.length;\n    int n = grid[0].length;\n    int count = 0;\n    int\
        \ r = 0;\n    int c = n - 1;\n\n    while (r < m && c >= 0) {\n      if (grid[r][c]\
        \ < 0) {\n        count += (m - r);\n        c--;\n      } else {\n        r++;\n\
        \      }\n    }\n\n    return count;\n  }\n}"
      go: "func countNegatives(grid [][]int) int {\n    m := len(grid)\n    n := len(grid[0])\n\
        \    count := 0\n    r := 0\n    c := n - 1\n\n    for r < m && c >= 0 {\n \
        \       if grid[r][c] < 0 {\n            count += (m - r)\n            c--\n\
        \        } else {\n            r++\n        }\n    }\n\n    return count\n}"
      ruby: "# @param {Integer[][]} grid\n# @return {Integer}\ndef count_negatives(grid)\n\
        \    m = grid.length\n    n = grid[0].length\n    count = 0\n    r = 0\n   \
        \ c = n - 1\n\n    while r < m && c >= 0\n        if grid[r][c] < 0\n      \
        \      count += (m - r)\n            c -= 1\n        else\n            r +=\
        \ 1\n        end\n    end\n\n    count\nend"
      scala: "object Solution {\n    def countNegatives(grid: Array[Array[Int]]): Int\
        \ = {\n        val m = grid.length\n        val n = grid(0).length\n       \
        \ var count = 0\n        var r = 0\n        var c = n - 1\n\n        while (r\
        \ < m && c >= 0) {\n            if (grid(r)(c) < 0) {\n                count\
        \ += (m - r)\n                c -= 1\n            } else {\n               \
        \ r += 1\n            }\n        }\n\n        count\n    }\n}"
      rust: "impl Solution {\n    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32\
        \ {\n        let m = grid.len();\n        let n = grid[0].len();\n        let\
        \ mut count = 0;\n        let mut r = 0;\n        let mut c = n as isize - 1;\n\
        \n        while r < m && c >= 0 {\n            if grid[r][c as usize] < 0 {\n\
        \                count += (m - r) as i32;\n                c -= 1;\n       \
        \     } else {\n                r += 1;\n            }\n        }\n\n      \
        \  count\n    }\n}"
      racket: "#lang racket\n\n(define (count-negatives grid)\n  (define m (length grid))\n\
        \  (define n (length (car grid)))\n  (define count (make-box 0))\n  (define\
        \ r (make-box 0))\n  (define c (make-box (- n 1)))\n\n  (let loop ()\n    (when\
        \ (and (< (unbox r) m) (>= (unbox c) 0))\n      (if (< (list-ref (list-ref grid\
        \ (unbox r)) (unbox c)) 0)\n          (begin\n            (set-box! count (+\
        \ (unbox count) (- m (unbox r))))\n            (set-box! c (- (unbox c) 1)))\n\
        \          (set-box! r (+ (unbox r) 1)))\n      (loop)))\n  (unbox count))"
      erlang: "-module(solution).\n-export([count_negatives/1]).\n\ncount_negatives(Grid)\
        \ ->\n    M = length(Grid),\n    N = length(hd(Grid)),\n    count_negatives_loop(Grid,\
        \ M, N, 0, N - 1, 0).\n\ncount_negatives_loop(Grid, M, N, R, C, Count) when\
        \ R < M, C >= 0 ->\n    Row = lists:nth(R + 1, Grid),\n    Element = lists:nth(C\
        \ + 1, Row),\n    if\n        Element < 0 ->\n            count_negatives_loop(Grid,\
        \ M, N, R, C - 1, Count + (M - R));\n        true ->\n            count_negatives_loop(Grid,\
        \ M, N, R + 1, C, Count)\n    end;\ncount_negatives_loop(_Grid, _M, _N, _R,\
        \ _C, Count) ->\n    Count."
      elixir: "defmodule Solution do\n  @spec count_negatives(grid :: [[integer]]) ::\
        \ integer\n  def count_negatives(grid) do\n    m = length(grid)\n    n = length(hd(grid))\n\
        \    count_negatives_loop(grid, m, n, 0, n - 1, 0)\n  end\n\n  defp count_negatives_loop(grid,\
        \ m, n, r, c, count) when r < m and c >= 0 do\n    row = Enum.at(grid, r)\n\
        \    element = Enum.at(row, c)\n\n    if element < 0 do\n      count_negatives_loop(grid,\
        \ m, n, r, c - 1, count + (m - r))\n    else\n      count_negatives_loop(grid,\
        \ m, n, r + 1, c, count)\n    end\n  end\n\n  defp count_negatives_loop(_grid,\
        \ _m, _n, _r, _c, count) do\n    count\n  end\nend"
    approach: 'The problem asks us to count negative numbers in a matrix sorted in non-increasing
      order both row-wise and column-wise. A brute-force approach would iterate through
      every element, resulting in O(m*n) time complexity. However, the sorted property
      allows for a more efficient O(m+n) solution.


      The optimized approach starts from the top-right corner of the matrix (row 0,
      column n-1). We maintain two pointers, `r` for the current row and `c` for the
      current column. If the element `grid[r][c]` is negative, it implies that all elements
      below it in the same column (i.e., `grid[r][c], grid[r+1][c], ..., grid[m-1][c]`)
      must also be negative due to the column-wise non-increasing sort. Therefore, we
      can add `m - r` to our total count of negative numbers and then move one column
      to the left (decrement `c`) to search for more negatives. If `grid[r][c]` is non-negative,
      it implies that all elements to its left in the current row (i.e., `grid[r][0],
      ..., grid[r][c]`) must also be non-negative due to the row-wise non-increasing
      sort. In this case, we move down one row (increment `r`) to find potential negative
      numbers. The process continues until `r` goes out of bounds (`r >= m`) or `c`
      goes out of bounds (`c < 0`).'
    time_complexity: The time complexity is O(m + n). In each step of the algorithm,
      we either increment the row pointer `r` or decrement the column pointer `c`. The
      row pointer `r` starts at 0 and goes up to `m`, while the column pointer `c` starts
      at `n-1` and goes down to `-1`. Since `r` can be incremented at most `m` times
      and `c` can be decremented at most `n` times, the total number of operations is
      proportional to `m + n`.
    space_complexity: The space complexity is O(1). The algorithm uses a constant amount
      of extra space to store variables such as `m`, `n`, `count`, `r`, and `c`, regardless
      of the input matrix size.
    elapsed_time: 49.281973361968994
    model: gemini-2.5-flash
    generated_at: '2025-12-28 01:16:07 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int countNegatives(vector<vector<int>>& grid)\
        \ {\n        int count = 0;\n        for (auto& row : grid) {\n            int\
        \ left = 0, right = row.size() - 1;\n            while (left <= right) {\n \
        \               int mid = left + (right - left) / 2;\n                if (row[mid]\
        \ < 0) {\n                    right = mid - 1;\n                } else {\n \
        \                   left = mid + 1;\n                }\n            }\n    \
        \        count += row.size() - left;\n        }\n        return count;\n   \
        \ }\n};"
      java: "class Solution {\n    public int countNegatives(int[][] grid) {\n     \
        \   int count = 0;\n        for (int[] row : grid) {\n            int left =\
        \ 0, right = row.length - 1;\n            while (left <= right) {\n        \
        \        int mid = left + (right - left) / 2;\n                if (row[mid]\
        \ < 0) {\n                    right = mid - 1;\n                } else {\n \
        \                   left = mid + 1;\n                }\n            }\n    \
        \        count += row.length - left;\n        }\n        return count;\n   \
        \ }\n}"
      python: "class Solution:\n    def countNegatives(self, grid: List[List[int]])\
        \ -> int:\n        count = 0\n        for row in grid:\n            left, right\
        \ = 0, len(row) - 1\n            while left <= right:\n                mid =\
        \ left + (right - left) // 2\n                if row[mid] < 0:\n           \
        \         right = mid - 1\n                else:\n                    left =\
        \ mid + 1\n            count += len(row) - left\n        return count"
      python3: "class Solution:\n    def countNegatives(self, grid: List[List[int]])\
        \ -> int:\n        count = 0\n        for row in grid:\n            left, right\
        \ = 0, len(row) - 1\n            while left <= right:\n                mid =\
        \ left + (right - left) // 2\n                if row[mid] < 0:\n           \
        \         right = mid - 1\n                else:\n                    left =\
        \ mid + 1\n            count += len(row) - left\n        return count"
      c: "int countNegatives(int** grid, int gridSize, int* gridColSize) {\n    int\
        \ count = 0;\n    for (int i = 0; i < gridSize; i++) {\n        int left = 0,\
        \ right = gridColSize[i] - 1;\n        while (left <= right) {\n           \
        \ int mid = left + (right - left) / 2;\n            if (grid[i][mid] < 0) {\n\
        \                right = mid - 1;\n            } else {\n                left\
        \ = mid + 1;\n            }\n        }\n        count += gridColSize[i] - left;\n\
        \    }\n    return count;\n}"
      csharp: "public class Solution {\n    public int CountNegatives(int[][] grid)\
        \ {\n        int count = 0;\n        foreach (int[] row in grid) {\n       \
        \     int left = 0, right = row.Length - 1;\n            while (left <= right)\
        \ {\n                int mid = left + (right - left) / 2;\n                if\
        \ (row[mid] < 0) {\n                    right = mid - 1;\n                }\
        \ else {\n                    left = mid + 1;\n                }\n         \
        \   }\n            count += row.Length - left;\n        }\n        return count;\n\
        \    }\n}"
      javascript: "var countNegatives = function(grid) {\n    let count = 0;\n    for\
        \ (let row of grid) {\n        let left = 0, right = row.length - 1;\n     \
        \   while (left <= right) {\n            let mid = left + Math.floor((right\
        \ - left) / 2);\n            if (row[mid] < 0) {\n                right = mid\
        \ - 1;\n            } else {\n                left = mid + 1;\n            }\n\
        \        }\n        count += row.length - left;\n    }\n    return count;\n\
        };"
      typescript: "function countNegatives(grid: number[][]): number {\n    let count:\
        \ number = 0;\n    for (let row of grid) {\n        let left: number = 0, right:\
        \ number = row.length - 1;\n        while (left <= right) {\n            let\
        \ mid: number = left + Math.floor((right - left) / 2);\n            if (row[mid]\
        \ < 0) {\n                right = mid - 1;\n            } else {\n         \
        \       left = mid + 1;\n            }\n        }\n        count += row.length\
        \ - left;\n    }\n    return count;\n}"
      php: "class Solution {\n    function countNegatives($grid) {\n        $count =\
        \ 0;\n        foreach ($grid as $row) {\n            $left = 0; $right = count($row)\
        \ - 1;\n            while ($left <= $right) {\n                $mid = $left\
        \ + floor(($right - $left) / 2);\n                if ($row[$mid] < 0) {\n  \
        \                  $right = $mid - 1;\n                } else {\n          \
        \          $left = $mid + 1;\n                }\n            }\n           \
        \ $count += count($row) - $left;\n        }\n        return $count;\n    }\n\
        }"
      swift: "class Solution {\n    func countNegatives(_ grid: [[Int]]) -> Int {\n\
        \        var count = 0\n        for row in grid {\n            var left = 0,\
        \ right = row.count - 1\n            while left <= right {\n               \
        \ let mid = left + (right - left) / 2\n                if row[mid] < 0 {\n \
        \                   right = mid - 1\n                } else {\n            \
        \        left = mid + 1\n                }\n            }\n            count\
        \ += row.count - left\n        }\n        return count\n    }\n}"
      kotlin: "class Solution {\n    fun countNegatives(grid: Array<IntArray>): Int\
        \ {\n        var count = 0\n        for (row in grid) {\n            var left\
        \ = 0\n            var right = row.size - 1\n            while (left <= right)\
        \ {\n                val mid = left + (right - left) / 2\n                if\
        \ (row[mid] < 0) {\n                    right = mid - 1\n                } else\
        \ {\n                    left = mid + 1\n                }\n            }\n\
        \            count += row.size - left\n        }\n        return count\n   \
        \ }\n}"
      dart: "class Solution {\n    int countNegatives(List<List<int>> grid) {\n    \
        \    int count = 0;\n        for (var row in grid) {\n            int left =\
        \ 0, right = row.length - 1;\n            while (left <= right) {\n        \
        \        int mid = left + (right - left) ~/ 2;\n                if (row[mid]\
        \ < 0) {\n                    right = mid - 1;\n                } else {\n \
        \                   left = mid + 1;\n                }\n            }\n    \
        \        count += row.length - left;\n        }\n        return count;\n   \
        \ }\n}"
      go: "func countNegatives(grid [][]int) int {\n    count := 0\n    for _, row :=\
        \ range grid {\n        left, right := 0, len(row)-1\n        for left <= right\
        \ {\n            mid := left + (right-left)/2\n            if row[mid] < 0 {\n\
        \                right = mid - 1\n            } else {\n                left\
        \ = mid + 1\n            }\n        }\n        count += len(row) - left\n  \
        \  }\n    return count\n}"
      ruby: "def count_negatives(grid)\n    count = 0\n    grid.each do |row|\n    \
        \    left, right = 0, row.size - 1\n        while left <= right\n          \
        \  mid = left + (right - left) / 2\n            if row[mid] < 0\n          \
        \      right = mid - 1\n            else\n                left = mid + 1\n \
        \           end\n        end\n        count += row.size - left\n    end\n  \
        \  count\nend"
      scala: "object Solution {\n    def countNegatives(grid: Array[Array[Int]]): Int\
        \ = {\n        var count = 0\n        for (row <- grid) {\n            var left\
        \ = 0\n            var right = row.length - 1\n            while (left <= right)\
        \ {\n                val mid = left + (right - left) / 2\n                if\
        \ (row(mid) < 0) {\n                    right = mid - 1\n                } else\
        \ {\n                    left = mid + 1\n                }\n            }\n\
        \            count += row.length - left\n        }\n        count\n    }\n}"
      rust: "impl Solution {\n    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32\
        \ {\n        let mut count = 0;\n        for row in grid {\n            let\
        \ mut left = 0;\n            let mut right = row.len() - 1;\n            while\
        \ left <= right {\n                let mid = left + (right - left) / 2;\n  \
        \              if row[mid] < 0 {\n                    right = mid - 1;\n   \
        \             } else {\n                    left = mid + 1;\n              \
        \  }\n            }\n            count += row.len() as i32 - left as i32;\n\
        \        }\n        count\n    }\n}"
      racket: "define (count-negatives grid)\n    (let loop ((grid grid) (count 0))\n\
        \        (if (null? grid)\n            count\n            (let ((row (car grid))\n\
        \                  (left 0)\n                  (right (sub1 (length row))))\n\
        \                (let loop ((left left) (right right))\n                   \
        \ (if (> left right)\n                        (loop (cdr grid) (+ count (sub1\
        \ (length row)) left))\n                        (let ((mid (quotient (+ left\
        \ right) 2)))\n                            (if (< (list-ref row mid) 0)\n  \
        \                              (loop left (sub1 mid))\n                    \
        \            (loop (add1 mid) right))))))))))"
      erlang: "count_negatives(Grid) ->\n    count_negatives(Grid, 0).\n\ncount_negatives([],\
        \ Count) -> Count;\ncount_negatives([Row|Grid], Count) ->\n    count_negatives(Grid,\
        \ Count + count_negatives_in_row(Row, 0, length(Row) - 1)).\n\ncount_negatives_in_row(Row,\
        \ Left, Right) when Left > Right -> 0;\ncount_negatives_in_row(Row, Left, Right)\
        \ ->\n    Mid = Left + (Right - Left) div 2,\n    case lists:nth(Mid + 1, Row)\
        \ of\n        X when X < 0 ->\n            count_negatives_in_row(Row, Left,\
        \ Mid - 1) + length(Row) - Mid;\n        _ ->\n            count_negatives_in_row(Row,\
        \ Mid + 1, Right)\n    end."
      elixir: "def count_negatives(grid) do\n    count_negatives(grid, 0)\nend\n\ndefp\
        \ count_negatives([], count), do: count\n\ndefp count_negatives([row|grid],\
        \ count) do\n    count_negatives(grid, count + count_negatives_in_row(row, 0,\
        \ length(row) - 1))\nend\n\ndefp count_negatives_in_row(row, left, right) when\
        \ left > right, do: 0\n\ndefp count_negatives_in_row(row, left, right) do\n\
        \    mid = left + div(right - left, 2)\n    case Enum.at(row, mid) do\n    \
        \    x when x < 0 ->\n            count_negatives_in_row(row, left, mid - 1)\
        \ + length(row) - mid\n        _ ->\n            count_negatives_in_row(row,\
        \ mid + 1, right)\n    end\nend"
    approach: "The problem can be solved by iterating over each row in the grid and\
      \ using binary search to find the first negative number in the row. Since the\
      \ grid is sorted in non-increasing order both row-wise and column-wise, we can\
      \ start the binary search from the end of each row and move towards the start\
      \ until we find the first negative number. The key intuition here is that once\
      \ we find the first negative number in a row, all numbers to its right will also\
      \ be negative. Therefore, we can simply count the number of negative numbers in\
      \ each row and add them up to get the total count of negative numbers in the grid.\
      \ \n  The algorithm starts by initializing a variable to store the count of negative\
      \ numbers. Then, it iterates over each row in the grid. For each row, it uses\
      \ binary search to find the first negative number. Once the first negative number\
      \ is found, it calculates the count of negative numbers in the row by subtracting\
      \ the index of the first negative number from the length of the row. This count\
      \ is then added to the total count of negative numbers. The algorithm finally\
      \ returns the total count of negative numbers in the grid."
    time_complexity: The time complexity of the algorithm is O(m * log n), where m is
      the number of rows in the grid and n is the number of columns. This is because
      for each row, we are performing a binary search which takes O(log n) time. Since
      we are doing this for m rows, the total time complexity becomes O(m * log n).
    space_complexity: The space complexity of the algorithm is O(1), which means the
      space required does not change with the size of the input grid. This is because
      we are only using a constant amount of space to store the count of negative numbers
      and the indices for the binary search.
    elapsed_time: 6.061354637145996
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-28 01:16:13 '
---

## Problem #1351: Count Negative Numbers in a Sorted Matrix

**Difficulty:** Easy

**Topics:** Array, Binary Search, Matrix

## Problem Description

<p>Given a <code>m x n</code> matrix <code>grid</code> which is sorted in non-increasing order both row-wise and column-wise, return <em>the number of <strong>negative</strong> numbers in</em> <code>grid</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
<strong>Output:</strong> 8
<strong>Explanation:</strong> There are 8 negatives number in the matrix.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[3,2],[1,0]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>-100 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you find an <code>O(n + m)</code> solution?

## Hints

1. Use binary search for optimization or simply brute force.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-28 01:16:07 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to count negative numbers in a matrix sorted in non-increasing order both row-wise and column-wise. A brute-force approach would iterate through every element, resulting in O(m*n) time complexity. However, the sorted property allows for a more efficient O(m+n) solution.

The optimized approach starts from the top-right corner of the matrix (row 0, column n-1). We maintain two pointers, `r` for the current row and `c` for the current column. If the element `grid[r][c]` is negative, it implies that all elements below it in the same column (i.e., `grid[r][c], grid[r+1][c], ..., grid[m-1][c]`) must also be negative due to the column-wise non-increasing sort. Therefore, we can add `m - r` to our total count of negative numbers and then move one column to the left (decrement `c`) to search for more negatives. If `grid[r][c]` is non-negative, it implies that all elements to its left in the current row (i.e., `grid[r][0], ..., grid[r][c]`) must also be non-negative due to the row-wise non-increasing sort. In this case, we move down one row (increment `r`) to find potential negative numbers. The process continues until `r` goes out of bounds (`r >= m`) or `c` goes out of bounds (`c < 0`).

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-cpp-gemini-2-5-flash" checked>
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-java-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python3-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-c-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-csharp-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-javascript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-typescript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-php-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-swift-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-kotlin-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-dart-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-go-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-ruby-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-scala-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-rust-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-racket-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-erlang-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-elixir-gemini-2-5-flash">
  <div class="tab-labels">
    <label for="lang-cpp-gemini-2-5-flash">C++</label>
    <label for="lang-java-gemini-2-5-flash">Java</label>
    <label for="lang-python-gemini-2-5-flash">Python</label>
    <label for="lang-python3-gemini-2-5-flash">Python3</label>
    <label for="lang-c-gemini-2-5-flash">C</label>
    <label for="lang-csharp-gemini-2-5-flash">C#</label>
    <label for="lang-javascript-gemini-2-5-flash">JavaScript</label>
    <label for="lang-typescript-gemini-2-5-flash">TypeScript</label>
    <label for="lang-php-gemini-2-5-flash">PHP</label>
    <label for="lang-swift-gemini-2-5-flash">Swift</label>
    <label for="lang-kotlin-gemini-2-5-flash">Kotlin</label>
    <label for="lang-dart-gemini-2-5-flash">Dart</label>
    <label for="lang-go-gemini-2-5-flash">Go</label>
    <label for="lang-ruby-gemini-2-5-flash">Ruby</label>
    <label for="lang-scala-gemini-2-5-flash">Scala</label>
    <label for="lang-rust-gemini-2-5-flash">Rust</label>
    <label for="lang-racket-gemini-2-5-flash">Racket</label>
    <label for="lang-erlang-gemini-2-5-flash">Erlang</label>
    <label for="lang-elixir-gemini-2-5-flash">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    int countNegatives(std::vector<std::vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int count = 0;
        int r = 0;
        int c = n - 1;

        while (r < m && c >= 0) {
            if (grid[r][c] < 0) {
                count += (m - r);
                c--;
            } else {
                r++;
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
    public int countNegatives(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int count = 0;
        int r = 0;
        int c = n - 1;

        while (r < m && c >= 0) {
            if (grid[r][c] < 0) {
                count += (m - r);
                c--;
            } else {
                r++;
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
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        r = 0
        c = n - 1

        while r < m and c >= 0:
            if grid[r][c] < 0:
                count += (m - r)
                c -= 1
            else:
                r += 1

        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        r = 0
        c = n - 1

        while r < m and c >= 0:
            if grid[r][c] < 0:
                count += (m - r)
                c -= 1
            else:
                r += 1

        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countNegatives(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];
    int count = 0;
    int r = 0;
    int c = n - 1;

    while (r < m && c >= 0) {
        if (grid[r][c] < 0) {
            count += (m - r);
            c--;
        } else {
            r++;
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
    public int CountNegatives(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int count = 0;
        int r = 0;
        int c = n - 1;

        while (r < m && c >= 0) {
            if (grid[r][c] < 0) {
                count += (m - r);
                c--;
            } else {
                r++;
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
 * @return {number}
 */
var countNegatives = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    let count = 0;
    let r = 0;
    let c = n - 1;

    while (r < m && c >= 0) {
        if (grid[r][c] < 0) {
            count += (m - r);
            c--;
        } else {
            r++;
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
function countNegatives(grid: number[][]): number {
    const m: number = grid.length;
    const n: number = grid[0].length;
    let count: number = 0;
    let r: number = 0;
    let c: number = n - 1;

    while (r < m && c >= 0) {
        if (grid[r][c] < 0) {
            count += (m - r);
            c--;
        } else {
            r++;
        }
    }

    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param int[][] $grid
     * @return int
     */
    function countNegatives(array $grid): int {
        $m = count($grid);
        $n = count($grid[0]);
        $count = 0;
        $r = 0;
        $c = $n - 1;

        while ($r < $m && $c >= 0) {
            if ($grid[$r][$c] < 0) {
                $count += ($m - $r);
                $c--;
            } else {
                $r++;
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
    func countNegatives(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var count = 0
        var r = 0
        var c = n - 1

        while r < m && c >= 0 {
            if grid[r][c] < 0 {
                count += (m - r)
                c -= 1
            } else {
                r += 1
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
    fun countNegatives(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var count = 0
        var r = 0
        var c = n - 1

        while (r < m && c >= 0) {
            if (grid[r][c] < 0) {
                count += (m - r)
                c--
            } else {
                r++
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
  int countNegatives(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    int count = 0;
    int r = 0;
    int c = n - 1;

    while (r < m && c >= 0) {
      if (grid[r][c] < 0) {
        count += (m - r);
        c--;
      } else {
        r++;
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
func countNegatives(grid [][]int) int {
    m := len(grid)
    n := len(grid[0])
    count := 0
    r := 0
    c := n - 1

    for r < m && c >= 0 {
        if grid[r][c] < 0 {
            count += (m - r)
            c--
        } else {
            r++
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
# @return {Integer}
def count_negatives(grid)
    m = grid.length
    n = grid[0].length
    count = 0
    r = 0
    c = n - 1

    while r < m && c >= 0
        if grid[r][c] < 0
            count += (m - r)
            c -= 1
        else
            r += 1
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
    def countNegatives(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        val n = grid(0).length
        var count = 0
        var r = 0
        var c = n - 1

        while (r < m && c >= 0) {
            if (grid(r)(c) < 0) {
                count += (m - r)
                c -= 1
            } else {
                r += 1
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
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut count = 0;
        let mut r = 0;
        let mut c = n as isize - 1;

        while r < m && c >= 0 {
            if grid[r][c as usize] < 0 {
                count += (m - r) as i32;
                c -= 1;
            } else {
                r += 1;
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
#lang racket

(define (count-negatives grid)
  (define m (length grid))
  (define n (length (car grid)))
  (define count (make-box 0))
  (define r (make-box 0))
  (define c (make-box (- n 1)))

  (let loop ()
    (when (and (< (unbox r) m) (>= (unbox c) 0))
      (if (< (list-ref (list-ref grid (unbox r)) (unbox c)) 0)
          (begin
            (set-box! count (+ (unbox count) (- m (unbox r))))
            (set-box! c (- (unbox c) 1)))
          (set-box! r (+ (unbox r) 1)))
      (loop)))
  (unbox count))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([count_negatives/1]).

count_negatives(Grid) ->
    M = length(Grid),
    N = length(hd(Grid)),
    count_negatives_loop(Grid, M, N, 0, N - 1, 0).

count_negatives_loop(Grid, M, N, R, C, Count) when R < M, C >= 0 ->
    Row = lists:nth(R + 1, Grid),
    Element = lists:nth(C + 1, Row),
    if
        Element < 0 ->
            count_negatives_loop(Grid, M, N, R, C - 1, Count + (M - R));
        true ->
            count_negatives_loop(Grid, M, N, R + 1, C, Count)
    end;
count_negatives_loop(_Grid, _M, _N, _R, _C, Count) ->
    Count.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_negatives(grid :: [[integer]]) :: integer
  def count_negatives(grid) do
    m = length(grid)
    n = length(hd(grid))
    count_negatives_loop(grid, m, n, 0, n - 1, 0)
  end

  defp count_negatives_loop(grid, m, n, r, c, count) when r < m and c >= 0 do
    row = Enum.at(grid, r)
    element = Enum.at(row, c)

    if element < 0 do
      count_negatives_loop(grid, m, n, r, c - 1, count + (m - r))
    else
      count_negatives_loop(grid, m, n, r + 1, c, count)
    end
  end

  defp count_negatives_loop(_grid, _m, _n, _r, _c, count) do
    count
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(m + n). In each step of the algorithm, we either increment the row pointer `r` or decrement the column pointer `c`. The row pointer `r` starts at 0 and goes up to `m`, while the column pointer `c` starts at `n-1` and goes down to `-1`. Since `r` can be incremented at most `m` times and `c` can be decremented at most `n` times, the total number of operations is proportional to `m + n`.

- **Space Complexity:** The space complexity is O(1). The algorithm uses a constant amount of extra space to store variables such as `m`, `n`, `count`, `r`, and `c`, regardless of the input matrix size.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-28 01:16:13 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by iterating over each row in the grid and using binary search to find the first negative number in the row. Since the grid is sorted in non-increasing order both row-wise and column-wise, we can start the binary search from the end of each row and move towards the start until we find the first negative number. The key intuition here is that once we find the first negative number in a row, all numbers to its right will also be negative. Therefore, we can simply count the number of negative numbers in each row and add them up to get the total count of negative numbers in the grid. 
  The algorithm starts by initializing a variable to store the count of negative numbers. Then, it iterates over each row in the grid. For each row, it uses binary search to find the first negative number. Once the first negative number is found, it calculates the count of negative numbers in the row by subtracting the index of the first negative number from the length of the row. This count is then added to the total count of negative numbers. The algorithm finally returns the total count of negative numbers in the grid.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-cpp-llama-3-3-70b-versatile" checked>
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-java-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python3-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-c-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-csharp-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-javascript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-typescript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-php-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-swift-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-kotlin-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-dart-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-go-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-ruby-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-scala-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-rust-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-racket-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-erlang-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-elixir-llama-3-3-70b-versatile">
  <div class="tab-labels">
    <label for="lang-cpp-llama-3-3-70b-versatile">C++</label>
    <label for="lang-java-llama-3-3-70b-versatile">Java</label>
    <label for="lang-python-llama-3-3-70b-versatile">Python</label>
    <label for="lang-python3-llama-3-3-70b-versatile">Python3</label>
    <label for="lang-c-llama-3-3-70b-versatile">C</label>
    <label for="lang-csharp-llama-3-3-70b-versatile">C#</label>
    <label for="lang-javascript-llama-3-3-70b-versatile">JavaScript</label>
    <label for="lang-typescript-llama-3-3-70b-versatile">TypeScript</label>
    <label for="lang-php-llama-3-3-70b-versatile">PHP</label>
    <label for="lang-swift-llama-3-3-70b-versatile">Swift</label>
    <label for="lang-kotlin-llama-3-3-70b-versatile">Kotlin</label>
    <label for="lang-dart-llama-3-3-70b-versatile">Dart</label>
    <label for="lang-go-llama-3-3-70b-versatile">Go</label>
    <label for="lang-ruby-llama-3-3-70b-versatile">Ruby</label>
    <label for="lang-scala-llama-3-3-70b-versatile">Scala</label>
    <label for="lang-rust-llama-3-3-70b-versatile">Rust</label>
    <label for="lang-racket-llama-3-3-70b-versatile">Racket</label>
    <label for="lang-erlang-llama-3-3-70b-versatile">Erlang</label>
    <label for="lang-elixir-llama-3-3-70b-versatile">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int count = 0;
        for (auto& row : grid) {
            int left = 0, right = row.size() - 1;
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (row[mid] < 0) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            count += row.size() - left;
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
    public int countNegatives(int[][] grid) {
        int count = 0;
        for (int[] row : grid) {
            int left = 0, right = row.length - 1;
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (row[mid] < 0) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            count += row.length - left;
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
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            left, right = 0, len(row) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            count += len(row) - left
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            left, right = 0, len(row) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            count += len(row) - left
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countNegatives(int** grid, int gridSize, int* gridColSize) {
    int count = 0;
    for (int i = 0; i < gridSize; i++) {
        int left = 0, right = gridColSize[i] - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (grid[i][mid] < 0) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        count += gridColSize[i] - left;
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
    public int CountNegatives(int[][] grid) {
        int count = 0;
        foreach (int[] row in grid) {
            int left = 0, right = row.Length - 1;
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (row[mid] < 0) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            count += row.Length - left;
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
var countNegatives = function(grid) {
    let count = 0;
    for (let row of grid) {
        let left = 0, right = row.length - 1;
        while (left <= right) {
            let mid = left + Math.floor((right - left) / 2);
            if (row[mid] < 0) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        count += row.length - left;
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countNegatives(grid: number[][]): number {
    let count: number = 0;
    for (let row of grid) {
        let left: number = 0, right: number = row.length - 1;
        while (left <= right) {
            let mid: number = left + Math.floor((right - left) / 2);
            if (row[mid] < 0) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        count += row.length - left;
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function countNegatives($grid) {
        $count = 0;
        foreach ($grid as $row) {
            $left = 0; $right = count($row) - 1;
            while ($left <= $right) {
                $mid = $left + floor(($right - $left) / 2);
                if ($row[$mid] < 0) {
                    $right = $mid - 1;
                } else {
                    $left = $mid + 1;
                }
            }
            $count += count($row) - $left;
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
    func countNegatives(_ grid: [[Int]]) -> Int {
        var count = 0
        for row in grid {
            var left = 0, right = row.count - 1
            while left <= right {
                let mid = left + (right - left) / 2
                if row[mid] < 0 {
                    right = mid - 1
                } else {
                    left = mid + 1
                }
            }
            count += row.count - left
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
    fun countNegatives(grid: Array<IntArray>): Int {
        var count = 0
        for (row in grid) {
            var left = 0
            var right = row.size - 1
            while (left <= right) {
                val mid = left + (right - left) / 2
                if (row[mid] < 0) {
                    right = mid - 1
                } else {
                    left = mid + 1
                }
            }
            count += row.size - left
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
    int countNegatives(List<List<int>> grid) {
        int count = 0;
        for (var row in grid) {
            int left = 0, right = row.length - 1;
            while (left <= right) {
                int mid = left + (right - left) ~/ 2;
                if (row[mid] < 0) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            count += row.length - left;
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
func countNegatives(grid [][]int) int {
    count := 0
    for _, row := range grid {
        left, right := 0, len(row)-1
        for left <= right {
            mid := left + (right-left)/2
            if row[mid] < 0 {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        count += len(row) - left
    }
    return count
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def count_negatives(grid)
    count = 0
    grid.each do |row|
        left, right = 0, row.size - 1
        while left <= right
            mid = left + (right - left) / 2
            if row[mid] < 0
                right = mid - 1
            else
                left = mid + 1
            end
        end
        count += row.size - left
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
    def countNegatives(grid: Array[Array[Int]]): Int = {
        var count = 0
        for (row <- grid) {
            var left = 0
            var right = row.length - 1
            while (left <= right) {
                val mid = left + (right - left) / 2
                if (row(mid) < 0) {
                    right = mid - 1
                } else {
                    left = mid + 1
                }
            }
            count += row.length - left
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
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let mut count = 0;
        for row in grid {
            let mut left = 0;
            let mut right = row.len() - 1;
            while left <= right {
                let mid = left + (right - left) / 2;
                if row[mid] < 0 {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            count += row.len() as i32 - left as i32;
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
define (count-negatives grid)
    (let loop ((grid grid) (count 0))
        (if (null? grid)
            count
            (let ((row (car grid))
                  (left 0)
                  (right (sub1 (length row))))
                (let loop ((left left) (right right))
                    (if (> left right)
                        (loop (cdr grid) (+ count (sub1 (length row)) left))
                        (let ((mid (quotient (+ left right) 2)))
                            (if (< (list-ref row mid) 0)
                                (loop left (sub1 mid))
                                (loop (add1 mid) right))))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
count_negatives(Grid) ->
    count_negatives(Grid, 0).

count_negatives([], Count) -> Count;
count_negatives([Row|Grid], Count) ->
    count_negatives(Grid, Count + count_negatives_in_row(Row, 0, length(Row) - 1)).

count_negatives_in_row(Row, Left, Right) when Left > Right -> 0;
count_negatives_in_row(Row, Left, Right) ->
    Mid = Left + (Right - Left) div 2,
    case lists:nth(Mid + 1, Row) of
        X when X < 0 ->
            count_negatives_in_row(Row, Left, Mid - 1) + length(Row) - Mid;
        _ ->
            count_negatives_in_row(Row, Mid + 1, Right)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def count_negatives(grid) do
    count_negatives(grid, 0)
end

defp count_negatives([], count), do: count

defp count_negatives([row|grid], count) do
    count_negatives(grid, count + count_negatives_in_row(row, 0, length(row) - 1))
end

defp count_negatives_in_row(row, left, right) when left > right, do: 0

defp count_negatives_in_row(row, left, right) do
    mid = left + div(right - left, 2)
    case Enum.at(row, mid) do
        x when x < 0 ->
            count_negatives_in_row(row, left, mid - 1) + length(row) - mid
        _ ->
            count_negatives_in_row(row, mid + 1, right)
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the algorithm is O(m * log n), where m is the number of rows in the grid and n is the number of columns. This is because for each row, we are performing a binary search which takes O(log n) time. Since we are doing this for m rows, the total time complexity becomes O(m * log n).

- **Space Complexity:** The space complexity of the algorithm is O(1), which means the space required does not change with the size of the input grid. This is because we are only using a constant amount of space to store the count of negative numbers and the indices for the binary search.

</div>
</details>
