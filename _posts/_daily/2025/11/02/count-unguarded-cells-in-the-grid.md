---
layout: post
title: "Count Unguarded Cells in the Grid"
date: 2025-11-02 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Matrix", "Simulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-unguarded-cells-in-the-grid/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int countUnguarded(int m, int n, vector<vector<int>>&\
        \ guards, vector<vector<int>>& walls) {\n        vector<vector<int>> grid(m,\
        \ vector<int>(n, 0));\n        for (const auto& wall : walls) grid[wall[0]][wall[1]]\
        \ = 2;\n        for (const auto& guard : guards) grid[guard[0]][guard[1]] =\
        \ 3;\n\n        const int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0,\
        \ 1}};\n        for (const auto& guard : guards) {\n            for (const auto&\
        \ direction : directions) {\n                int row = guard[0] + direction[0];\n\
        \                int col = guard[1] + direction[1];\n                while (row\
        \ >= 0 && row < m && col >= 0 && col < n && grid[row][col] != 2 && grid[row][col]\
        \ != 3) {\n                    if (grid[row][col] == 0) grid[row][col] = 1;\n\
        \                    row += direction[0];\n                    col += direction[1];\n\
        \                }\n            }\n        }\n\n        int unguarded = 0;\n\
        \        for (const auto& row : grid) {\n            for (int cell : row) {\n\
        \                if (cell == 0) ++unguarded;\n            }\n        }\n   \
        \     return unguarded;\n    }\n};"
      java: "class Solution {\n    public int countUnguarded(int m, int n, int[][] guards,\
        \ int[][] walls) {\n        int[][] grid = new int[m][n];\n        for (int[]\
        \ wall : walls) grid[wall[0]][wall[1]] = 2;\n        for (int[] guard : guards)\
        \ grid[guard[0]][guard[1]] = 3;\n\n        int[][] directions = {{-1, 0}, {1,\
        \ 0}, {0, -1}, {0, 1}};\n        for (int[] guard : guards) {\n            for\
        \ (int[] direction : directions) {\n                int row = guard[0] + direction[0];\n\
        \                int col = guard[1] + direction[1];\n                while (row\
        \ >= 0 && row < m && col >= 0 && col < n && grid[row][col] != 2 && grid[row][col]\
        \ != 3) {\n                    if (grid[row][col] == 0) grid[row][col] = 1;\n\
        \                    row += direction[0];\n                    col += direction[1];\n\
        \                }\n            }\n        }\n\n        int unguarded = 0;\n\
        \        for (int[] row : grid) {\n            for (int cell : row) {\n    \
        \            if (cell == 0) unguarded++;\n            }\n        }\n       \
        \ return unguarded;\n    }\n}"
      python: "class Solution(object):\n    def countUnguarded(self, m, n, guards, walls):\n\
        \        \"\"\"\n        :type m: int\n        :type n: int\n        :type guards:\
        \ List[List[int]]\n        :type walls: List[List[int]]\n        :rtype: int\n\
        \        \"\"\"\n        grid = [[0] * n for _ in range(m)]\n        for row,\
        \ col in walls:\n            grid[row][col] = 2\n        for row, col in guards:\n\
        \            grid[row][col] = 3\n\n        directions = ((-1, 0), (1, 0), (0,\
        \ -1), (0, 1))\n        for guard_row, guard_col in guards:\n            for\
        \ dr, dc in directions:\n                row, col = guard_row + dr, guard_col\
        \ + dc\n                while 0 <= row < m and 0 <= col < n and grid[row][col]\
        \ not in (2, 3):\n                    if grid[row][col] == 0:\n            \
        \            grid[row][col] = 1\n                    row += dr\n           \
        \         col += dc\n\n        return sum(cell == 0 for row in grid for cell\
        \ in row)"
      python3: "class Solution:\n    def countUnguarded(self, m: int, n: int, guards:\
        \ list[list[int]], walls: list[list[int]]) -> int:\n        grid = [[0] * n\
        \ for _ in range(m)]\n        for row, col in walls:\n            grid[row][col]\
        \ = 2\n        for row, col in guards:\n            grid[row][col] = 3\n\n \
        \       directions = ((-1, 0), (1, 0), (0, -1), (0, 1))\n        for guard_row,\
        \ guard_col in guards:\n            for dr, dc in directions:\n            \
        \    row, col = guard_row + dr, guard_col + dc\n                while 0 <= row\
        \ < m and 0 <= col < n and grid[row][col] not in (2, 3):\n                 \
        \   if grid[row][col] == 0:\n                        grid[row][col] = 1\n  \
        \                  row += dr\n                    col += dc\n\n        return\
        \ sum(cell == 0 for row in grid for cell in row)"
      c: "int countUnguarded(int m, int n, int** guards, int guardsSize, int* guardsColSize,\
        \ int** walls, int wallsSize, int* wallsColSize) {\n    int** grid = (int**)calloc(m,\
        \ sizeof(int*));\n    for (int row = 0; row < m; ++row) {\n        grid[row]\
        \ = (int*)calloc(n, sizeof(int));\n    }\n\n    for (int i = 0; i < wallsSize;\
        \ ++i) {\n        grid[walls[i][0]][walls[i][1]] = 2;\n    }\n    for (int i\
        \ = 0; i < guardsSize; ++i) {\n        grid[guards[i][0]][guards[i][1]] = 3;\n\
        \    }\n\n    int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};\n \
        \   for (int i = 0; i < guardsSize; ++i) {\n        int guardRow = guards[i][0];\n\
        \        int guardCol = guards[i][1];\n        for (int d = 0; d < 4; ++d) {\n\
        \            int row = guardRow + directions[d][0];\n            int col = guardCol\
        \ + directions[d][1];\n            while (row >= 0 && row < m && col >= 0 &&\
        \ col < n && grid[row][col] != 2 && grid[row][col] != 3) {\n               \
        \ if (grid[row][col] == 0) grid[row][col] = 1;\n                row += directions[d][0];\n\
        \                col += directions[d][1];\n            }\n        }\n    }\n\
        \n    int unguarded = 0;\n    for (int row = 0; row < m; ++row) {\n        for\
        \ (int col = 0; col < n; ++col) {\n            if (grid[row][col] == 0) ++unguarded;\n\
        \        }\n        free(grid[row]);\n    }\n    free(grid);\n    return unguarded;\n\
        }"
      csharp: "public class Solution {\n    public int CountUnguarded(int m, int n,\
        \ int[][] guards, int[][] walls) {\n        int[,] grid = new int[m, n];\n \
        \       foreach (int[] wall in walls) {\n            grid[wall[0], wall[1]]\
        \ = 2;\n        }\n        foreach (int[] guard in guards) {\n            grid[guard[0],\
        \ guard[1]] = 3;\n        }\n\n        int[][] directions = new int[][] {\n\
        \            new int[] { -1, 0 },\n            new int[] { 1, 0 },\n       \
        \     new int[] { 0, -1 },\n            new int[] { 0, 1 }\n        };\n\n \
        \       foreach (int[] guard in guards) {\n            foreach (int[] direction\
        \ in directions) {\n                int row = guard[0] + direction[0];\n   \
        \             int col = guard[1] + direction[1];\n                while (row\
        \ >= 0 && row < m && col >= 0 && col < n && grid[row, col] != 2 && grid[row,\
        \ col] != 3) {\n                    if (grid[row, col] == 0) {\n           \
        \             grid[row, col] = 1;\n                    }\n                 \
        \   row += direction[0];\n                    col += direction[1];\n       \
        \         }\n            }\n        }\n\n        int count = 0;\n        for\
        \ (int row = 0; row < m; row++) {\n            for (int col = 0; col < n; col++)\
        \ {\n                if (grid[row, col] == 0) {\n                    count++;\n\
        \                }\n            }\n        }\n        return count;\n    }\n\
        }"
      javascript: "/**\n * @param {number} m\n * @param {number} n\n * @param {number[][]}\
        \ guards\n * @param {number[][]} walls\n * @return {number}\n */\nvar countUnguarded\
        \ = function(m, n, guards, walls) {\n    const grid = Array.from({ length: m\
        \ }, () => Array(n).fill(0));\n    for (const [row, col] of walls) {\n     \
        \   grid[row][col] = 2;\n    }\n    for (const [row, col] of guards) {\n   \
        \     grid[row][col] = 3;\n    }\n\n    const directions = [[-1, 0], [1, 0],\
        \ [0, -1], [0, 1]];\n    for (const [guardRow, guardCol] of guards) {\n    \
        \    for (const [dr, dc] of directions) {\n            let row = guardRow +\
        \ dr;\n            let col = guardCol + dc;\n            while (row >= 0 &&\
        \ row < m && col >= 0 && col < n && grid[row][col] !== 2 && grid[row][col] !==\
        \ 3) {\n                if (grid[row][col] === 0) {\n                    grid[row][col]\
        \ = 1;\n                }\n                row += dr;\n                col +=\
        \ dc;\n            }\n        }\n    }\n\n    let count = 0;\n    for (let row\
        \ = 0; row < m; row++) {\n        for (let col = 0; col < n; col++) {\n    \
        \        if (grid[row][col] === 0) {\n                count++;\n           \
        \ }\n        }\n    }\n    return count;\n};"
      typescript: "function countUnguarded(m: number, n: number, guards: number[][],\
        \ walls: number[][]): number {\n    const grid: number[][] = Array.from({ length:\
        \ m }, () => Array(n).fill(0));\n    for (const [row, col] of walls) {\n   \
        \     grid[row][col] = 2;\n    }\n    for (const [row, col] of guards) {\n \
        \       grid[row][col] = 3;\n    }\n\n    const directions: number[][] = [[-1,\
        \ 0], [1, 0], [0, -1], [0, 1]];\n    for (const [guardRow, guardCol] of guards)\
        \ {\n        for (const [dr, dc] of directions) {\n            let row = guardRow\
        \ + dr;\n            let col = guardCol + dc;\n            while (row >= 0 &&\
        \ row < m && col >= 0 && col < n && grid[row][col] !== 2 && grid[row][col] !==\
        \ 3) {\n                if (grid[row][col] === 0) {\n                    grid[row][col]\
        \ = 1;\n                }\n                row += dr;\n                col +=\
        \ dc;\n            }\n        }\n    }\n\n    let count = 0;\n    for (let row\
        \ = 0; row < m; row++) {\n        for (let col = 0; col < n; col++) {\n    \
        \        if (grid[row][col] === 0) {\n                count++;\n           \
        \ }\n        }\n    }\n    return count;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $m\n     * @param Integer\
        \ $n\n     * @param Integer[][] $guards\n     * @param Integer[][] $walls\n\
        \     * @return Integer\n     */\n    function countUnguarded($m, $n, $guards,\
        \ $walls) {\n        $grid = array_fill(0, $m, array_fill(0, $n, 0));\n    \
        \    foreach ($walls as $wall) {\n            $grid[$wall[0]][$wall[1]] = 2;\n\
        \        }\n        foreach ($guards as $guard) {\n            $grid[$guard[0]][$guard[1]]\
        \ = 3;\n        }\n\n        $directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];\n\
        \        foreach ($guards as $guard) {\n            foreach ($directions as\
        \ $direction) {\n                $row = $guard[0] + $direction[0];\n       \
        \         $col = $guard[1] + $direction[1];\n                while ($row >=\
        \ 0 && $row < $m && $col >= 0 && $col < $n && $grid[$row][$col] !== 2 && $grid[$row][$col]\
        \ !== 3) {\n                    if ($grid[$row][$col] === 0) {\n           \
        \             $grid[$row][$col] = 1;\n                    }\n              \
        \      $row += $direction[0];\n                    $col += $direction[1];\n\
        \                }\n            }\n        }\n\n        $count = 0;\n      \
        \  for ($row = 0; $row < $m; $row++) {\n            for ($col = 0; $col < $n;\
        \ $col++) {\n                if ($grid[$row][$col] === 0) {\n              \
        \      $count++;\n                }\n            }\n        }\n        return\
        \ $count;\n    }\n}"
      swift: "class Solution {\n    func countUnguarded(_ m: Int, _ n: Int, _ guards:\
        \ [[Int]], _ walls: [[Int]]) -> Int {\n        var grid = Array(repeating: Array(repeating:\
        \ 0, count: n), count: m)\n        for wall in walls {\n            grid[wall[0]][wall[1]]\
        \ = 2\n        }\n        for guardPosition in guards {\n            grid[guardPosition[0]][guardPosition[1]]\
        \ = 3\n        }\n\n        let directions = [(-1, 0), (1, 0), (0, -1), (0,\
        \ 1)]\n        for guardPosition in guards {\n            for (dr, dc) in directions\
        \ {\n                var row = guardPosition[0] + dr\n                var col\
        \ = guardPosition[1] + dc\n                while row >= 0 && row < m && col\
        \ >= 0 && col < n && grid[row][col] != 2 && grid[row][col] != 3 {\n        \
        \            if grid[row][col] == 0 {\n                        grid[row][col]\
        \ = 1\n                    }\n                    row += dr\n              \
        \      col += dc\n                }\n            }\n        }\n\n        var\
        \ count = 0\n        for row in 0..<m {\n            for col in 0..<n {\n  \
        \              if grid[row][col] == 0 {\n                    count += 1\n  \
        \              }\n            }\n        }\n        return count\n    }\n}"
      kotlin: "class Solution {\n    fun countUnguarded(m: Int, n: Int, guards: Array<IntArray>,\
        \ walls: Array<IntArray>): Int {\n        val grid = Array(m) { IntArray(n)\
        \ }\n        for (wall in walls) {\n            grid[wall[0]][wall[1]] = 2\n\
        \        }\n        for (guard in guards) {\n            grid[guard[0]][guard[1]]\
        \ = 3\n        }\n\n        val directions = arrayOf(intArrayOf(-1, 0), intArrayOf(1,\
        \ 0), intArrayOf(0, -1), intArrayOf(0, 1))\n        for (guard in guards) {\n\
        \            for (direction in directions) {\n                var row = guard[0]\
        \ + direction[0]\n                var col = guard[1] + direction[1]\n      \
        \          while (row in 0 until m && col in 0 until n && grid[row][col] !=\
        \ 2 && grid[row][col] != 3) {\n                    if (grid[row][col] == 0)\
        \ {\n                        grid[row][col] = 1\n                    }\n   \
        \                 row += direction[0]\n                    col += direction[1]\n\
        \                }\n            }\n        }\n\n        var count = 0\n    \
        \    for (row in grid) {\n            for (cell in row) {\n                if\
        \ (cell == 0) count++\n            }\n        }\n        return count\n    }\n\
        }"
      dart: "class Solution {\n  int countUnguarded(int m, int n, List<List<int>> guards,\
        \ List<List<int>> walls) {\n    final grid = List.generate(m, (_) => List<int>.filled(n,\
        \ 0));\n    for (final wall in walls) {\n      grid[wall[0]][wall[1]] = 2;\n\
        \    }\n    for (final guard in guards) {\n      grid[guard[0]][guard[1]] =\
        \ 3;\n    }\n\n    const directions = [\n      [-1, 0],\n      [1, 0],\n   \
        \   [0, -1],\n      [0, 1],\n    ];\n    for (final guard in guards) {\n   \
        \   for (final direction in directions) {\n        var row = guard[0] + direction[0];\n\
        \        var col = guard[1] + direction[1];\n        while (row >= 0 && row\
        \ < m && col >= 0 && col < n &&\n            grid[row][col] != 2 && grid[row][col]\
        \ != 3) {\n          if (grid[row][col] == 0) {\n            grid[row][col]\
        \ = 1;\n          }\n          row += direction[0];\n          col += direction[1];\n\
        \        }\n      }\n    }\n\n    var count = 0;\n    for (final row in grid)\
        \ {\n      for (final cell in row) {\n        if (cell == 0) count++;\n    \
        \  }\n    }\n    return count;\n  }\n}"
      go: "func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {\n\t\
        grid := make([][]int, m)\n\tfor row := range grid {\n\t\tgrid[row] = make([]int,\
        \ n)\n\t}\n\tfor _, wall := range walls {\n\t\tgrid[wall[0]][wall[1]] = 2\n\t\
        }\n\tfor _, guard := range guards {\n\t\tgrid[guard[0]][guard[1]] = 3\n\t}\n\
        \n\tdirections := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}\n\tfor _, guard\
        \ := range guards {\n\t\tfor _, direction := range directions {\n\t\t\trow :=\
        \ guard[0] + direction[0]\n\t\t\tcol := guard[1] + direction[1]\n\t\t\tfor row\
        \ >= 0 && row < m && col >= 0 && col < n && grid[row][col] != 2 && grid[row][col]\
        \ != 3 {\n\t\t\t\tif grid[row][col] == 0 {\n\t\t\t\t\tgrid[row][col] = 1\n\t\
        \t\t\t}\n\t\t\t\trow += direction[0]\n\t\t\t\tcol += direction[1]\n\t\t\t}\n\
        \t\t}\n\t}\n\n\tcount := 0\n\tfor _, row := range grid {\n\t\tfor _, cell :=\
        \ range row {\n\t\t\tif cell == 0 {\n\t\t\t\tcount++\n\t\t\t}\n\t\t}\n\t}\n\t\
        return count\n}"
      ruby: "# @param {Integer} m\n# @param {Integer} n\n# @param {Integer[][]} guards\n\
        # @param {Integer[][]} walls\n# @return {Integer}\ndef count_unguarded(m, n,\
        \ guards, walls)\n  grid = Array.new(m) { Array.new(n, 0) }\n  walls.each do\
        \ |row, col|\n    grid[row][col] = 2\n  end\n  guards.each do |row, col|\n \
        \   grid[row][col] = 3\n  end\n\n  directions = [[-1, 0], [1, 0], [0, -1], [0,\
        \ 1]]\n  guards.each do |guard_row, guard_col|\n    directions.each do |dr,\
        \ dc|\n      row = guard_row + dr\n      col = guard_col + dc\n      while row\
        \ >= 0 && row < m && col >= 0 && col < n && grid[row][col] != 2 && grid[row][col]\
        \ != 3\n        grid[row][col] = 1 if grid[row][col] == 0\n        row += dr\n\
        \        col += dc\n      end\n    end\n  end\n\n  grid.sum { |row| row.count(0)\
        \ }\nend"
      scala: "object Solution {\n    def countUnguarded(m: Int, n: Int, guards: Array[Array[Int]],\
        \ walls: Array[Array[Int]]): Int = {\n        val grid = Array.fill(m, n)(0)\n\
        \        walls.foreach { wall =>\n            grid(wall(0))(wall(1)) = 2\n \
        \       }\n        guards.foreach { guard =>\n            grid(guard(0))(guard(1))\
        \ = 3\n        }\n\n        val directions = Array((-1, 0), (1, 0), (0, -1),\
        \ (0, 1))\n        guards.foreach { guard =>\n            directions.foreach\
        \ { case (dr, dc) =>\n                var row = guard(0) + dr\n            \
        \    var col = guard(1) + dc\n                while (row >= 0 && row < m &&\
        \ col >= 0 && col < n && grid(row)(col) != 2 && grid(row)(col) != 3) {\n   \
        \                 if (grid(row)(col) == 0) {\n                        grid(row)(col)\
        \ = 1\n                    }\n                    row += dr\n              \
        \      col += dc\n                }\n            }\n        }\n\n        grid.iterator.map(_.count(_\
        \ == 0)).sum\n    }\n}"
      rust: "impl Solution {\n    pub fn count_unguarded(m: i32, n: i32, guards: Vec<Vec<i32>>,\
        \ walls: Vec<Vec<i32>>) -> i32 {\n        let rows = m as usize;\n        let\
        \ cols = n as usize;\n        let mut grid = vec![vec![0u8; cols]; rows];\n\n\
        \        for wall in &walls {\n            grid[wall[0] as usize][wall[1] as\
        \ usize] = 2;\n        }\n        for guard in &guards {\n            grid[guard[0]\
        \ as usize][guard[1] as usize] = 3;\n        }\n\n        let directions = [(-1i32,\
        \ 0i32), (1, 0), (0, -1), (0, 1)];\n        for guard in &guards {\n       \
        \     for (dr, dc) in directions {\n                let mut row = guard[0] +\
        \ dr;\n                let mut col = guard[1] + dc;\n                while row\
        \ >= 0 && row < m && col >= 0 && col < n {\n                    let cell = &mut\
        \ grid[row as usize][col as usize];\n                    if *cell == 2 || *cell\
        \ == 3 {\n                        break;\n                    }\n          \
        \          if *cell == 0 {\n                        *cell = 1;\n           \
        \         }\n                    row += dr;\n                    col += dc;\n\
        \                }\n            }\n        }\n\n        grid.iter().flatten().filter(|&&cell|\
        \ cell == 0).count() as i32\n    }\n}"
      racket: "(define/contract (count-unguarded m n guards walls)\n  (-> exact-integer?\
        \ exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?))\
        \ exact-integer?)\n  (let ([grid (build-vector m (lambda (_) (make-vector n\
        \ 0)))])\n    (for-each\n     (lambda (wall)\n       (vector-set! (vector-ref\
        \ grid (first wall)) (second wall) 2))\n     walls)\n    (for-each\n     (lambda\
        \ (guard)\n       (vector-set! (vector-ref grid (first guard)) (second guard)\
        \ 3))\n     guards)\n    (define directions '((-1 0) (1 0) (0 -1) (0 1)))\n\
        \    (for-each\n     (lambda (guard)\n       (for-each\n        (lambda (direction)\n\
        \          (let loop ([row (+ (first guard) (first direction))]\n          \
        \           [col (+ (second guard) (second direction))])\n            (when\
        \ (and (<= 0 row) (< row m) (<= 0 col) (< col n)\n                       (not\
        \ (member (vector-ref (vector-ref grid row) col) '(2 3))))\n              (when\
        \ (= (vector-ref (vector-ref grid row) col) 0)\n                (vector-set!\
        \ (vector-ref grid row) col 1))\n              (loop (+ row (first direction))\
        \ (+ col (second direction)))))\n        directions))\n     guards)\n    (for*/sum\
        \ ([row (in-range m)] [col (in-range n)])\n      (if (= (vector-ref (vector-ref\
        \ grid row) col) 0) 1 0))))"
      erlang: "-spec count_unguarded(M :: integer(), N :: integer(), Guards :: [[integer()]],\
        \ Walls :: [[integer()]]) -> integer().\ncount_unguarded(M, N, Guards, Walls)\
        \ ->\n  Grid0 = array:new([{size, M}, {default, array:new([{size, N}, {default,\
        \ 0}])}]),\n  Grid1 = lists:foldl(\n    fun([Row, Col], Grid) ->\n      RowArray\
        \ = array:get(Row, Grid),\n      array:set(Row, array:set(Col, 2, RowArray),\
        \ Grid)\n    end,\n    Grid0,\n    Walls\n  ),\n  Grid2 = lists:foldl(\n   \
        \ fun([Row, Col], Grid) ->\n      RowArray = array:get(Row, Grid),\n      array:set(Row,\
        \ array:set(Col, 3, RowArray), Grid)\n    end,\n    Grid1,\n    Guards\n  ),\n\
        \  Directions = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}],\n  Grid3 = lists:foldl(\n\
        \    fun([GuardRow, GuardCol], Grid) ->\n      lists:foldl(\n        fun({Dr,\
        \ Dc}, CurrentGrid) ->\n          scan(GuardRow + Dr, GuardCol + Dc, Dr, Dc,\
        \ M, N, CurrentGrid)\n        end,\n        Grid,\n        Directions\n    \
        \  )\n    end,\n    Grid2,\n    Guards\n  ),\n  lists:sum([\n    case array:get(Col,\
        \ array:get(Row, Grid3)) of\n      0 -> 1;\n      _ -> 0\n    end\n    || Row\
        \ <- lists:seq(0, M - 1), Col <- lists:seq(0, N - 1)\n  ]).\n\nscan(Row, Col,\
        \ Dr, Dc, M, N, Grid) when Row >= 0, Row < M, Col >= 0, Col < N ->\n  RowArray\
        \ = array:get(Row, Grid),\n  case array:get(Col, RowArray) of\n    2 -> Grid;\n\
        \    3 -> Grid;\n    0 ->\n      UpdatedGrid = array:set(Row, array:set(Col,\
        \ 1, RowArray), Grid),\n      scan(Row + Dr, Col + Dc, Dr, Dc, M, N, UpdatedGrid);\n\
        \    1 -> scan(Row + Dr, Col + Dc, Dr, Dc, M, N, Grid)\n  end;\nscan(_Row, _Col,\
        \ _Dr, _Dc, _M, _N, Grid) -> Grid."
      elixir: "defmodule Solution do\n  @spec count_unguarded(m :: integer, n :: integer,\
        \ guards :: [[integer]], walls :: [[integer]]) :: integer\n  def count_unguarded(m,\
        \ n, guards, walls) do\n    grid = List.duplicate(List.duplicate(0, n), m)\n\
        \    grid = Enum.reduce(walls, grid, fn [row, col], acc -> put_in(acc, [Access.at(row),\
        \ Access.at(col)], 2) end)\n    grid = Enum.reduce(guards, grid, fn [row, col],\
        \ acc -> put_in(acc, [Access.at(row), Access.at(col)], 3) end)\n\n    directions\
        \ = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]\n\n    grid =\n      Enum.reduce(guards,\
        \ grid, fn [guard_row, guard_col], acc ->\n        Enum.reduce(directions, acc,\
        \ fn {dr, dc}, current_grid ->\n          scan(guard_row + dr, guard_col + dc,\
        \ dr, dc, m, n, current_grid)\n        end)\n      end)\n\n    Enum.sum(Enum.map(grid,\
        \ fn row -> Enum.count(row, &(&1 == 0)) end))\n  end\n\n  defp scan(row, col,\
        \ dr, dc, m, n, grid)\n       when row >= 0 and row < m and col >= 0 and col\
        \ < n do\n    cell = grid |> Enum.at(row) |> Enum.at(col)\n\n    if cell in\
        \ [2, 3] do\n      grid\n    else\n      updated_grid =\n        if cell ==\
        \ 0 do\n          put_in(grid, [Access.at(row), Access.at(col)], 1)\n      \
        \  else\n          grid\n        end\n\n      scan(row + dr, col + dc, dr, dc,\
        \ m, n, updated_grid)\n    end\n  end\n\n  defp scan(_row, _col, _dr, _dc, _m,\
        \ _n, grid), do: grid\nend"
    approach: 'Create a grid that marks each cell as empty, a guard, or a wall. For
      every guard, scan outward in the four cardinal directions, marking empty cells
      as guarded until the scan reaches the edge of the grid or an occupied cell.


      Count the cells that are still empty after all scans. Guards and walls stop visibility,
      and cells seen by multiple guards are counted only once.'
    time_complexity: O(m * n + g * (m + n)), where g is the number of guards. Initializing
      and counting the grid takes O(m * n), and scanning in four directions from every
      guard takes at most O(m + n) per guard.
    space_complexity: O(m * n) for the grid state.
    elapsed_time: 142.7330813407898
    model: gpt-6-luna
    generated_at: '2026-11-13 00:16:52 '
---

## Problem #2257: Count Unguarded Cells in the Grid

**Difficulty:** Medium

**Topics:** Array, Matrix, Simulation

## Problem Description

<p>You are given two integers <code>m</code> and <code>n</code> representing a <strong>0-indexed</strong> <code>m x n</code> grid. You are also given two 2D integer arrays <code>guards</code> and <code>walls</code> where <code>guards[i] = [row<sub>i</sub>, col<sub>i</sub>]</code> and <code>walls[j] = [row<sub>j</sub>, col<sub>j</sub>]</code> represent the positions of the <code>i<sup>th</sup></code> guard and <code>j<sup>th</sup></code> wall respectively.</p>

<p>A guard can see <b>every</b> cell in the four cardinal directions (north, east, south, or west) starting from their position unless <strong>obstructed</strong> by a wall or another guard. A cell is <strong>guarded</strong> if there is <strong>at least</strong> one guard that can see it.</p>

<p>Return<em> the number of unoccupied cells that are <strong>not</strong> <strong>guarded</strong>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/03/10/example1drawio2.png" style="width: 300px; height: 204px;" />
<pre>
<strong>Input:</strong> m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
<strong>Output:</strong> 7
<strong>Explanation:</strong> The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/03/10/example2drawio.png" style="width: 200px; height: 201px;" />
<pre>
<strong>Input:</strong> m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= guards.length, walls.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>2 &lt;= guards.length + walls.length &lt;= m * n</code></li>
	<li><code>guards[i].length == walls[j].length == 2</code></li>
	<li><code>0 &lt;= row<sub>i</sub>, row<sub>j</sub> &lt; m</code></li>
	<li><code>0 &lt;= col<sub>i</sub>, col<sub>j</sub> &lt; n</code></li>
	<li>All the positions in <code>guards</code> and <code>walls</code> are <strong>unique</strong>.</li>
</ul>


## Hints

1. Create a 2D array to represent the grid. Can you mark the tiles that can be seen by a guard?

2. Iterate over the guards, and for each of the 4 directions, advance the current tile and mark the tile. When should you stop advancing?

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

Create a grid that marks each cell as empty, a guard, or a wall. For every guard, scan outward in the four cardinal directions, marking empty cells as guarded until the scan reaches the edge of the grid or an occupied cell.

Count the cells that are still empty after all scans. Guards and walls stop visibility, and cells seen by multiple guards are counted only once.

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
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        vector<vector<int>> grid(m, vector<int>(n, 0));
        for (const auto& wall : walls) grid[wall[0]][wall[1]] = 2;
        for (const auto& guard : guards) grid[guard[0]][guard[1]] = 3;

        const int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (const auto& guard : guards) {
            for (const auto& direction : directions) {
                int row = guard[0] + direction[0];
                int col = guard[1] + direction[1];
                while (row >= 0 && row < m && col >= 0 && col < n && grid[row][col] != 2 && grid[row][col] != 3) {
                    if (grid[row][col] == 0) grid[row][col] = 1;
                    row += direction[0];
                    col += direction[1];
                }
            }
        }

        int unguarded = 0;
        for (const auto& row : grid) {
            for (int cell : row) {
                if (cell == 0) ++unguarded;
            }
        }
        return unguarded;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
        int[][] grid = new int[m][n];
        for (int[] wall : walls) grid[wall[0]][wall[1]] = 2;
        for (int[] guard : guards) grid[guard[0]][guard[1]] = 3;

        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (int[] guard : guards) {
            for (int[] direction : directions) {
                int row = guard[0] + direction[0];
                int col = guard[1] + direction[1];
                while (row >= 0 && row < m && col >= 0 && col < n && grid[row][col] != 2 && grid[row][col] != 3) {
                    if (grid[row][col] == 0) grid[row][col] = 1;
                    row += direction[0];
                    col += direction[1];
                }
            }
        }

        int unguarded = 0;
        for (int[] row : grid) {
            for (int cell : row) {
                if (cell == 0) unguarded++;
            }
        }
        return unguarded;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [[0] * n for _ in range(m)]
        for row, col in walls:
            grid[row][col] = 2
        for row, col in guards:
            grid[row][col] = 3

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for guard_row, guard_col in guards:
            for dr, dc in directions:
                row, col = guard_row + dr, guard_col + dc
                while 0 <= row < m and 0 <= col < n and grid[row][col] not in (2, 3):
                    if grid[row][col] == 0:
                        grid[row][col] = 1
                    row += dr
                    col += dc

        return sum(cell == 0 for row in grid for cell in row)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for row, col in walls:
            grid[row][col] = 2
        for row, col in guards:
            grid[row][col] = 3

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for guard_row, guard_col in guards:
            for dr, dc in directions:
                row, col = guard_row + dr, guard_col + dc
                while 0 <= row < m and 0 <= col < n and grid[row][col] not in (2, 3):
                    if grid[row][col] == 0:
                        grid[row][col] = 1
                    row += dr
                    col += dc

        return sum(cell == 0 for row in grid for cell in row)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countUnguarded(int m, int n, int** guards, int guardsSize, int* guardsColSize, int** walls, int wallsSize, int* wallsColSize) {
    int** grid = (int**)calloc(m, sizeof(int*));
    for (int row = 0; row < m; ++row) {
        grid[row] = (int*)calloc(n, sizeof(int));
    }

    for (int i = 0; i < wallsSize; ++i) {
        grid[walls[i][0]][walls[i][1]] = 2;
    }
    for (int i = 0; i < guardsSize; ++i) {
        grid[guards[i][0]][guards[i][1]] = 3;
    }

    int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    for (int i = 0; i < guardsSize; ++i) {
        int guardRow = guards[i][0];
        int guardCol = guards[i][1];
        for (int d = 0; d < 4; ++d) {
            int row = guardRow + directions[d][0];
            int col = guardCol + directions[d][1];
            while (row >= 0 && row < m && col >= 0 && col < n && grid[row][col] != 2 && grid[row][col] != 3) {
                if (grid[row][col] == 0) grid[row][col] = 1;
                row += directions[d][0];
                col += directions[d][1];
            }
        }
    }

    int unguarded = 0;
    for (int row = 0; row < m; ++row) {
        for (int col = 0; col < n; ++col) {
            if (grid[row][col] == 0) ++unguarded;
        }
        free(grid[row]);
    }
    free(grid);
    return unguarded;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountUnguarded(int m, int n, int[][] guards, int[][] walls) {
        int[,] grid = new int[m, n];
        foreach (int[] wall in walls) {
            grid[wall[0], wall[1]] = 2;
        }
        foreach (int[] guard in guards) {
            grid[guard[0], guard[1]] = 3;
        }

        int[][] directions = new int[][] {
            new int[] { -1, 0 },
            new int[] { 1, 0 },
            new int[] { 0, -1 },
            new int[] { 0, 1 }
        };

        foreach (int[] guard in guards) {
            foreach (int[] direction in directions) {
                int row = guard[0] + direction[0];
                int col = guard[1] + direction[1];
                while (row >= 0 && row < m && col >= 0 && col < n && grid[row, col] != 2 && grid[row, col] != 3) {
                    if (grid[row, col] == 0) {
                        grid[row, col] = 1;
                    }
                    row += direction[0];
                    col += direction[1];
                }
            }
        }

        int count = 0;
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (grid[row, col] == 0) {
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

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} guards
 * @param {number[][]} walls
 * @return {number}
 */
var countUnguarded = function(m, n, guards, walls) {
    const grid = Array.from({ length: m }, () => Array(n).fill(0));
    for (const [row, col] of walls) {
        grid[row][col] = 2;
    }
    for (const [row, col] of guards) {
        grid[row][col] = 3;
    }

    const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    for (const [guardRow, guardCol] of guards) {
        for (const [dr, dc] of directions) {
            let row = guardRow + dr;
            let col = guardCol + dc;
            while (row >= 0 && row < m && col >= 0 && col < n && grid[row][col] !== 2 && grid[row][col] !== 3) {
                if (grid[row][col] === 0) {
                    grid[row][col] = 1;
                }
                row += dr;
                col += dc;
            }
        }
    }

    let count = 0;
    for (let row = 0; row < m; row++) {
        for (let col = 0; col < n; col++) {
            if (grid[row][col] === 0) {
                count++;
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
function countUnguarded(m: number, n: number, guards: number[][], walls: number[][]): number {
    const grid: number[][] = Array.from({ length: m }, () => Array(n).fill(0));
    for (const [row, col] of walls) {
        grid[row][col] = 2;
    }
    for (const [row, col] of guards) {
        grid[row][col] = 3;
    }

    const directions: number[][] = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    for (const [guardRow, guardCol] of guards) {
        for (const [dr, dc] of directions) {
            let row = guardRow + dr;
            let col = guardCol + dc;
            while (row >= 0 && row < m && col >= 0 && col < n && grid[row][col] !== 2 && grid[row][col] !== 3) {
                if (grid[row][col] === 0) {
                    grid[row][col] = 1;
                }
                row += dr;
                col += dc;
            }
        }
    }

    let count = 0;
    for (let row = 0; row < m; row++) {
        for (let col = 0; col < n; col++) {
            if (grid[row][col] === 0) {
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
     * @param Integer $m
     * @param Integer $n
     * @param Integer[][] $guards
     * @param Integer[][] $walls
     * @return Integer
     */
    function countUnguarded($m, $n, $guards, $walls) {
        $grid = array_fill(0, $m, array_fill(0, $n, 0));
        foreach ($walls as $wall) {
            $grid[$wall[0]][$wall[1]] = 2;
        }
        foreach ($guards as $guard) {
            $grid[$guard[0]][$guard[1]] = 3;
        }

        $directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        foreach ($guards as $guard) {
            foreach ($directions as $direction) {
                $row = $guard[0] + $direction[0];
                $col = $guard[1] + $direction[1];
                while ($row >= 0 && $row < $m && $col >= 0 && $col < $n && $grid[$row][$col] !== 2 && $grid[$row][$col] !== 3) {
                    if ($grid[$row][$col] === 0) {
                        $grid[$row][$col] = 1;
                    }
                    $row += $direction[0];
                    $col += $direction[1];
                }
            }
        }

        $count = 0;
        for ($row = 0; $row < $m; $row++) {
            for ($col = 0; $col < $n; $col++) {
                if ($grid[$row][$col] === 0) {
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
    func countUnguarded(_ m: Int, _ n: Int, _ guards: [[Int]], _ walls: [[Int]]) -> Int {
        var grid = Array(repeating: Array(repeating: 0, count: n), count: m)
        for wall in walls {
            grid[wall[0]][wall[1]] = 2
        }
        for guardPosition in guards {
            grid[guardPosition[0]][guardPosition[1]] = 3
        }

        let directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for guardPosition in guards {
            for (dr, dc) in directions {
                var row = guardPosition[0] + dr
                var col = guardPosition[1] + dc
                while row >= 0 && row < m && col >= 0 && col < n && grid[row][col] != 2 && grid[row][col] != 3 {
                    if grid[row][col] == 0 {
                        grid[row][col] = 1
                    }
                    row += dr
                    col += dc
                }
            }
        }

        var count = 0
        for row in 0..<m {
            for col in 0..<n {
                if grid[row][col] == 0 {
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
    fun countUnguarded(m: Int, n: Int, guards: Array<IntArray>, walls: Array<IntArray>): Int {
        val grid = Array(m) { IntArray(n) }
        for (wall in walls) {
            grid[wall[0]][wall[1]] = 2
        }
        for (guard in guards) {
            grid[guard[0]][guard[1]] = 3
        }

        val directions = arrayOf(intArrayOf(-1, 0), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(0, 1))
        for (guard in guards) {
            for (direction in directions) {
                var row = guard[0] + direction[0]
                var col = guard[1] + direction[1]
                while (row in 0 until m && col in 0 until n && grid[row][col] != 2 && grid[row][col] != 3) {
                    if (grid[row][col] == 0) {
                        grid[row][col] = 1
                    }
                    row += direction[0]
                    col += direction[1]
                }
            }
        }

        var count = 0
        for (row in grid) {
            for (cell in row) {
                if (cell == 0) count++
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
  int countUnguarded(int m, int n, List<List<int>> guards, List<List<int>> walls) {
    final grid = List.generate(m, (_) => List<int>.filled(n, 0));
    for (final wall in walls) {
      grid[wall[0]][wall[1]] = 2;
    }
    for (final guard in guards) {
      grid[guard[0]][guard[1]] = 3;
    }

    const directions = [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1],
    ];
    for (final guard in guards) {
      for (final direction in directions) {
        var row = guard[0] + direction[0];
        var col = guard[1] + direction[1];
        while (row >= 0 && row < m && col >= 0 && col < n &&
            grid[row][col] != 2 && grid[row][col] != 3) {
          if (grid[row][col] == 0) {
            grid[row][col] = 1;
          }
          row += direction[0];
          col += direction[1];
        }
      }
    }

    var count = 0;
    for (final row in grid) {
      for (final cell in row) {
        if (cell == 0) count++;
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
func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
	grid := make([][]int, m)
	for row := range grid {
		grid[row] = make([]int, n)
	}
	for _, wall := range walls {
		grid[wall[0]][wall[1]] = 2
	}
	for _, guard := range guards {
		grid[guard[0]][guard[1]] = 3
	}

	directions := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	for _, guard := range guards {
		for _, direction := range directions {
			row := guard[0] + direction[0]
			col := guard[1] + direction[1]
			for row >= 0 && row < m && col >= 0 && col < n && grid[row][col] != 2 && grid[row][col] != 3 {
				if grid[row][col] == 0 {
					grid[row][col] = 1
				}
				row += direction[0]
				col += direction[1]
			}
		}
	}

	count := 0
	for _, row := range grid {
		for _, cell := range row {
			if cell == 0 {
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
# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} guards
# @param {Integer[][]} walls
# @return {Integer}
def count_unguarded(m, n, guards, walls)
  grid = Array.new(m) { Array.new(n, 0) }
  walls.each do |row, col|
    grid[row][col] = 2
  end
  guards.each do |row, col|
    grid[row][col] = 3
  end

  directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
  guards.each do |guard_row, guard_col|
    directions.each do |dr, dc|
      row = guard_row + dr
      col = guard_col + dc
      while row >= 0 && row < m && col >= 0 && col < n && grid[row][col] != 2 && grid[row][col] != 3
        grid[row][col] = 1 if grid[row][col] == 0
        row += dr
        col += dc
      end
    end
  end

  grid.sum { |row| row.count(0) }
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countUnguarded(m: Int, n: Int, guards: Array[Array[Int]], walls: Array[Array[Int]]): Int = {
        val grid = Array.fill(m, n)(0)
        walls.foreach { wall =>
            grid(wall(0))(wall(1)) = 2
        }
        guards.foreach { guard =>
            grid(guard(0))(guard(1)) = 3
        }

        val directions = Array((-1, 0), (1, 0), (0, -1), (0, 1))
        guards.foreach { guard =>
            directions.foreach { case (dr, dc) =>
                var row = guard(0) + dr
                var col = guard(1) + dc
                while (row >= 0 && row < m && col >= 0 && col < n && grid(row)(col) != 2 && grid(row)(col) != 3) {
                    if (grid(row)(col) == 0) {
                        grid(row)(col) = 1
                    }
                    row += dr
                    col += dc
                }
            }
        }

        grid.iterator.map(_.count(_ == 0)).sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_unguarded(m: i32, n: i32, guards: Vec<Vec<i32>>, walls: Vec<Vec<i32>>) -> i32 {
        let rows = m as usize;
        let cols = n as usize;
        let mut grid = vec![vec![0u8; cols]; rows];

        for wall in &walls {
            grid[wall[0] as usize][wall[1] as usize] = 2;
        }
        for guard in &guards {
            grid[guard[0] as usize][guard[1] as usize] = 3;
        }

        let directions = [(-1i32, 0i32), (1, 0), (0, -1), (0, 1)];
        for guard in &guards {
            for (dr, dc) in directions {
                let mut row = guard[0] + dr;
                let mut col = guard[1] + dc;
                while row >= 0 && row < m && col >= 0 && col < n {
                    let cell = &mut grid[row as usize][col as usize];
                    if *cell == 2 || *cell == 3 {
                        break;
                    }
                    if *cell == 0 {
                        *cell = 1;
                    }
                    row += dr;
                    col += dc;
                }
            }
        }

        grid.iter().flatten().filter(|&&cell| cell == 0).count() as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (count-unguarded m n guards walls)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer?)
  (let ([grid (build-vector m (lambda (_) (make-vector n 0)))])
    (for-each
     (lambda (wall)
       (vector-set! (vector-ref grid (first wall)) (second wall) 2))
     walls)
    (for-each
     (lambda (guard)
       (vector-set! (vector-ref grid (first guard)) (second guard) 3))
     guards)
    (define directions '((-1 0) (1 0) (0 -1) (0 1)))
    (for-each
     (lambda (guard)
       (for-each
        (lambda (direction)
          (let loop ([row (+ (first guard) (first direction))]
                     [col (+ (second guard) (second direction))])
            (when (and (<= 0 row) (< row m) (<= 0 col) (< col n)
                       (not (member (vector-ref (vector-ref grid row) col) '(2 3))))
              (when (= (vector-ref (vector-ref grid row) col) 0)
                (vector-set! (vector-ref grid row) col 1))
              (loop (+ row (first direction)) (+ col (second direction)))))
        directions))
     guards)
    (for*/sum ([row (in-range m)] [col (in-range n)])
      (if (= (vector-ref (vector-ref grid row) col) 0) 1 0))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec count_unguarded(M :: integer(), N :: integer(), Guards :: [[integer()]], Walls :: [[integer()]]) -> integer().
count_unguarded(M, N, Guards, Walls) ->
  Grid0 = array:new([{size, M}, {default, array:new([{size, N}, {default, 0}])}]),
  Grid1 = lists:foldl(
    fun([Row, Col], Grid) ->
      RowArray = array:get(Row, Grid),
      array:set(Row, array:set(Col, 2, RowArray), Grid)
    end,
    Grid0,
    Walls
  ),
  Grid2 = lists:foldl(
    fun([Row, Col], Grid) ->
      RowArray = array:get(Row, Grid),
      array:set(Row, array:set(Col, 3, RowArray), Grid)
    end,
    Grid1,
    Guards
  ),
  Directions = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}],
  Grid3 = lists:foldl(
    fun([GuardRow, GuardCol], Grid) ->
      lists:foldl(
        fun({Dr, Dc}, CurrentGrid) ->
          scan(GuardRow + Dr, GuardCol + Dc, Dr, Dc, M, N, CurrentGrid)
        end,
        Grid,
        Directions
      )
    end,
    Grid2,
    Guards
  ),
  lists:sum([
    case array:get(Col, array:get(Row, Grid3)) of
      0 -> 1;
      _ -> 0
    end
    || Row <- lists:seq(0, M - 1), Col <- lists:seq(0, N - 1)
  ]).

scan(Row, Col, Dr, Dc, M, N, Grid) when Row >= 0, Row < M, Col >= 0, Col < N ->
  RowArray = array:get(Row, Grid),
  case array:get(Col, RowArray) of
    2 -> Grid;
    3 -> Grid;
    0 ->
      UpdatedGrid = array:set(Row, array:set(Col, 1, RowArray), Grid),
      scan(Row + Dr, Col + Dc, Dr, Dc, M, N, UpdatedGrid);
    1 -> scan(Row + Dr, Col + Dc, Dr, Dc, M, N, Grid)
  end;
scan(_Row, _Col, _Dr, _Dc, _M, _N, Grid) -> Grid.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_unguarded(m :: integer, n :: integer, guards :: [[integer]], walls :: [[integer]]) :: integer
  def count_unguarded(m, n, guards, walls) do
    grid = List.duplicate(List.duplicate(0, n), m)
    grid = Enum.reduce(walls, grid, fn [row, col], acc -> put_in(acc, [Access.at(row), Access.at(col)], 2) end)
    grid = Enum.reduce(guards, grid, fn [row, col], acc -> put_in(acc, [Access.at(row), Access.at(col)], 3) end)

    directions = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

    grid =
      Enum.reduce(guards, grid, fn [guard_row, guard_col], acc ->
        Enum.reduce(directions, acc, fn {dr, dc}, current_grid ->
          scan(guard_row + dr, guard_col + dc, dr, dc, m, n, current_grid)
        end)
      end)

    Enum.sum(Enum.map(grid, fn row -> Enum.count(row, &(&1 == 0)) end))
  end

  defp scan(row, col, dr, dc, m, n, grid)
       when row >= 0 and row < m and col >= 0 and col < n do
    cell = grid |> Enum.at(row) |> Enum.at(col)

    if cell in [2, 3] do
      grid
    else
      updated_grid =
        if cell == 0 do
          put_in(grid, [Access.at(row), Access.at(col)], 1)
        else
          grid
        end

      scan(row + dr, col + dc, dr, dc, m, n, updated_grid)
    end
  end

  defp scan(_row, _col, _dr, _dc, _m, _n, grid), do: grid
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m * n + g * (m + n)), where g is the number of guards. Initializing and counting the grid takes O(m * n), and scanning in four directions from every guard takes at most O(m + n) per guard.
- **Space Complexity:** O(m * n) for the grid state.
