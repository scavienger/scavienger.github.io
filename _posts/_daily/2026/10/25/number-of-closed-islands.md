---
layout: post
title: "Number of Closed Islands"
date: 2026-10-25 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Depth-First Search", "Breadth-First Search", "Union-Find", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/number-of-closed-islands/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    void dfs(vector<vector<int>>& grid, int r,\
        \ int c) {\n        if (r < 0 || r >= grid.size() || c < 0 || c >= grid[0].size()\
        \ || grid[r][c] == 1) {\n            return;\n        }\n        grid[r][c]\
        \ = 1;\n        dfs(grid, r + 1, c);\n        dfs(grid, r - 1, c);\n       \
        \ dfs(grid, r, c + 1);\n        dfs(grid, r, c - 1);\n    }\n\n    int closedIsland(vector<vector<int>>&\
        \ grid) {\n        if (grid.empty()) return 0;\n        int rows = grid.size();\n\
        \        int cols = grid[0].size();\n\n        for (int i = 0; i < rows; i++)\
        \ {\n            dfs(grid, i, 0);\n            dfs(grid, i, cols - 1);\n   \
        \     }\n        for (int j = 0; j < cols; j++) {\n            dfs(grid, 0,\
        \ j);\n            dfs(grid, rows - 1, j);\n        }\n\n        int count =\
        \ 0;\n        for (int i = 0; i < rows; i++) {\n            for (int j = 0;\
        \ j < cols; j++) {\n                if (grid[i][j] == 0) {\n               \
        \     count++;\n                    dfs(grid, i, j);\n                }\n  \
        \          }\n        }\n        return count;\n    }\n};"
      java: "class Solution {\n    public int closedIsland(int[][] grid) {\n       \
        \ if (grid == null || grid.length == 0) return 0;\n        int rows = grid.length;\n\
        \        int cols = grid[0].length;\n\n        for (int i = 0; i < rows; i++)\
        \ {\n            dfs(grid, i, 0);\n            dfs(grid, i, cols - 1);\n   \
        \     }\n        for (int j = 0; j < cols; j++) {\n            dfs(grid, 0,\
        \ j);\n            dfs(grid, rows - 1, j);\n        }\n\n        int count =\
        \ 0;\n        for (int i = 0; i < rows; i++) {\n            for (int j = 0;\
        \ j < cols; j++) {\n                if (grid[i][j] == 0) {\n               \
        \     count++;\n                    dfs(grid, i, j);\n                }\n  \
        \          }\n        }\n        return count;\n    }\n\n    private void dfs(int[][]\
        \ grid, int r, int c) {\n        if (r < 0 || r >= grid.length || c < 0 || c\
        \ >= grid[0].length || grid[r][c] == 1) {\n            return;\n        }\n\
        \        grid[r][c] = 1;\n        dfs(grid, r + 1, c);\n        dfs(grid, r\
        \ - 1, c);\n        dfs(grid, r, c + 1);\n        dfs(grid, r, c - 1);\n   \
        \ }\n}"
      python: "import sys\n\nclass Solution(object):\n    def closedIsland(self, grid):\n\
        \        \"\"\"\n        :type grid: List[List[int]]\n        :rtype: int\n\
        \        \"\"\"\n        if not grid or not grid[0]:\n            return 0\n\
        \n        sys.setrecursionlimit(10000)\n        rows = len(grid)\n        cols\
        \ = len(grid[0])\n\n        def dfs(r, c):\n            if r < 0 or r >= rows\
        \ or c < 0 or c >= cols or grid[r][c] == 1:\n                return\n      \
        \      grid[r][c] = 1\n            dfs(r + 1, c)\n            dfs(r - 1, c)\n\
        \            dfs(r, c + 1)\n            dfs(r, c - 1)\n\n        for r in range(rows):\n\
        \            dfs(r, 0)\n            dfs(r, cols - 1)\n        for c in range(cols):\n\
        \            dfs(0, c)\n            dfs(rows - 1, c)\n\n        count = 0\n\
        \        for r in range(rows):\n            for c in range(cols):\n        \
        \        if grid[r][c] == 0:\n                    count += 1\n             \
        \       dfs(r, c)\n        return count"
      python3: "import sys\n\nclass Solution:\n    def closedIsland(self, grid: list[list[int]])\
        \ -> int:\n        if not grid or not grid[0]:\n            return 0\n\n   \
        \     sys.setrecursionlimit(10000)\n        rows = len(grid)\n        cols =\
        \ len(grid[0])\n\n        def dfs(r, c):\n            if r < 0 or r >= rows\
        \ or c < 0 or c >= cols or grid[r][c] == 1:\n                return\n      \
        \      grid[r][c] = 1\n            dfs(r + 1, c)\n            dfs(r - 1, c)\n\
        \            dfs(r, c + 1)\n            dfs(r, c - 1)\n\n        for r in range(rows):\n\
        \            dfs(r, 0)\n            dfs(r, cols - 1)\n        for c in range(cols):\n\
        \            dfs(0, c)\n            dfs(rows - 1, c)\n\n        count = 0\n\
        \        for r in range(rows):\n            for c in range(cols):\n        \
        \        if grid[r][c] == 0:\n                    count += 1\n             \
        \       dfs(r, c)\n        return count"
      c: "void dfs(int** grid, int r, int c, int rows, int cols) {\n    if (r < 0 ||\
        \ r >= rows || c < 0 || c >= cols || grid[r][c] == 1) {\n        return;\n \
        \   }\n    grid[r][c] = 1;\n    dfs(grid, r + 1, c, rows, cols);\n    dfs(grid,\
        \ r - 1, c, rows, cols);\n    dfs(grid, r, c + 1, rows, cols);\n    dfs(grid,\
        \ r, c - 1, rows, cols);\n}\n\nint closedIsland(int** grid, int gridSize, int*\
        \ gridColSize) {\n    if (gridSize == 0) return 0;\n    int rows = gridSize;\n\
        \    int cols = gridColSize[0];\n\n    for (int i = 0; i < rows; i++) {\n  \
        \      dfs(grid, i, 0, rows, cols);\n        dfs(grid, i, cols - 1, rows, cols);\n\
        \    }\n    for (int j = 0; j < cols; j++) {\n        dfs(grid, 0, j, rows,\
        \ cols);\n        dfs(grid, rows - 1, j, rows, cols);\n    }\n\n    int count\
        \ = 0;\n    for (int i = 0; i < rows; i++) {\n        for (int j = 0; j < cols;\
        \ j++) {\n            if (grid[i][j] == 0) {\n                count++;\n   \
        \             dfs(grid, i, j, rows, cols);\n            }\n        }\n    }\n\
        \    return count;\n}"
      csharp: "public class Solution {\n    public int ClosedIsland(int[][] grid) {\n\
        \        int rows = grid.Length;\n        int cols = grid[0].Length;\n\n   \
        \     for (int i = 0; i < rows; i++) {\n            for (int j = 0; j < cols;\
        \ j++) {\n                if (i == 0 || i == rows - 1 || j == 0 || j == cols\
        \ - 1) {\n                    if (grid[i][j] == 0) {\n                     \
        \   Dfs(grid, i, j);\n                    }\n                }\n           \
        \ }\n        }\n\n        int count = 0;\n        for (int i = 0; i < rows;\
        \ i++) {\n            for (int j = 0; j < cols; j++) {\n                if (grid[i][j]\
        \ == 0) {\n                    count++;\n                    Dfs(grid, i, j);\n\
        \                }\n            }\n        }\n\n        return count;\n    }\n\
        \n    private void Dfs(int[][] grid, int r, int c) {\n        if (r < 0 || r\
        \ >= grid.Length || c < 0 || c >= grid[0].Length || grid[r][c] == 1) {\n   \
        \         return;\n        }\n\n        grid[r][c] = 1;\n        Dfs(grid, r\
        \ + 1, c);\n        Dfs(grid, r - 1, c);\n        Dfs(grid, r, c + 1);\n   \
        \     Dfs(grid, r, c - 1);\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @return {number}\n */\nvar closedIsland\
        \ = function(grid) {\n    const rows = grid.length;\n    const cols = grid[0].length;\n\
        \n    function dfs(r, c) {\n        if (r < 0 || r >= rows || c < 0 || c >=\
        \ cols || grid[r][c] === 1) {\n            return;\n        }\n        grid[r][c]\
        \ = 1;\n        dfs(r + 1, c);\n        dfs(r - 1, c);\n        dfs(r, c + 1);\n\
        \        dfs(r, c - 1);\n    }\n\n    for (let i = 0; i < rows; i++) {\n   \
        \     for (let j = 0; j < cols; j++) {\n            if (i === 0 || i === rows\
        \ - 1 || j === 0 || j === cols - 1) {\n                if (grid[i][j] === 0)\
        \ {\n                    dfs(i, j);\n                }\n            }\n    \
        \    }\n    }\n\n    let count = 0;\n    for (let i = 0; i < rows; i++) {\n\
        \        for (let j = 0; j < cols; j++) {\n            if (grid[i][j] === 0)\
        \ {\n                count++;\n                dfs(i, j);\n            }\n \
        \       }\n    }\n\n    return count;\n};"
      typescript: "function closedIsland(grid: number[][]): number {\n    const rows\
        \ = grid.length;\n    const cols = grid[0].length;\n\n    function dfs(r: number,\
        \ c: number): void {\n        if (r < 0 || r >= rows || c < 0 || c >= cols ||\
        \ grid[r][c] === 1) {\n            return;\n        }\n        grid[r][c] =\
        \ 1;\n        dfs(r + 1, c);\n        dfs(r - 1, c);\n        dfs(r, c + 1);\n\
        \        dfs(r, c - 1);\n    }\n\n    for (let i = 0; i < rows; i++) {\n   \
        \     for (let j = 0; j < cols; j++) {\n            if (i === 0 || i === rows\
        \ - 1 || j === 0 || j === cols - 1) {\n                if (grid[i][j] === 0)\
        \ {\n                    dfs(i, j);\n                }\n            }\n    \
        \    }\n    }\n\n    let count = 0;\n    for (let i = 0; i < rows; i++) {\n\
        \        for (let j = 0; j < cols; j++) {\n            if (grid[i][j] === 0)\
        \ {\n                count++;\n                dfs(i, j);\n            }\n \
        \       }\n    }\n\n    return count;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @return\
        \ Integer\n     */\n    function closedIsland($grid) {\n        $rows = count($grid);\n\
        \        if ($rows === 0) return 0;\n        $cols = count($grid[0]);\n\n  \
        \      for ($i = 0; $i < $rows; $i++) {\n            for ($j = 0; $j < $cols;\
        \ $j++) {\n                if ($i == 0 || $i == $rows - 1 || $j == 0 || $j ==\
        \ $cols - 1) {\n                    if ($grid[$i][$j] == 0) {\n            \
        \            $this->dfs($grid, $i, $j, $rows, $cols);\n                    }\n\
        \                }\n            }\n        }\n\n        $count = 0;\n      \
        \  for ($i = 0; $i < $rows; $i++) {\n            for ($j = 0; $j < $cols; $j++)\
        \ {\n                if ($grid[$i][$j] == 0) {\n                    $count++;\n\
        \                    $this->dfs($grid, $i, $j, $rows, $cols);\n            \
        \    }\n            }\n        }\n\n        return $count;\n    }\n\n    function\
        \ dfs(&$grid, $r, $c, $rows, $cols) {\n        if ($r < 0 || $r >= $rows ||\
        \ $c < 0 || $c >= $cols || $grid[$r][$c] == 1) {\n            return;\n    \
        \    }\n\n        $grid[$r][$c] = 1;\n        $this->dfs($grid, $r + 1, $c,\
        \ $rows, $cols);\n        $this->dfs($grid, $r - 1, $c, $rows, $cols);\n   \
        \     $this->dfs($grid, $r, $c + 1, $rows, $cols);\n        $this->dfs($grid,\
        \ $r, $c - 1, $rows, $cols);\n    }\n}"
      swift: "class Solution {\n    func closedIsland(_ grid: [[Int]]) -> Int {\n  \
        \      var grid = grid\n        let rows = grid.count\n        if rows == 0\
        \ { return 0 }\n        let cols = grid[0].count\n\n        func dfs(_ r: Int,\
        \ _ c: Int) {\n            if r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c]\
        \ == 1 {\n                return\n            }\n            grid[r][c] = 1\n\
        \            dfs(r + 1, c)\n            dfs(r - 1, c)\n            dfs(r, c\
        \ + 1)\n            dfs(r, c - 1)\n        }\n\n        for i in 0..<rows {\n\
        \            for j in 0..<cols {\n                if i == 0 || i == rows - 1\
        \ || j == 0 || j == cols - 1 {\n                    if grid[i][j] == 0 {\n \
        \                       dfs(i, j)\n                    }\n                }\n\
        \            }\n        }\n\n        var count = 0\n        for i in 0..<rows\
        \ {\n            for j in 0..<cols {\n                if grid[i][j] == 0 {\n\
        \                    count += 1\n                    dfs(i, j)\n           \
        \     }\n            }\n        }\n\n        return count\n    }\n}"
      kotlin: "class Solution {\n    fun closedIsland(grid: Array<IntArray>): Int {\n\
        \        val rows = grid.size\n        val cols = grid[0].size\n\n        fun\
        \ dfs(r: Int, c: Int) {\n            if (r < 0 || r >= rows || c < 0 || c >=\
        \ cols || grid[r][c] == 1) return\n            grid[r][c] = 1\n            dfs(r\
        \ + 1, c)\n            dfs(r - 1, c)\n            dfs(r, c + 1)\n          \
        \  dfs(r, c - 1)\n        }\n\n        for (r in 0 until rows) {\n         \
        \   dfs(r, 0)\n            dfs(r, cols - 1)\n        }\n        for (c in 0\
        \ until cols) {\n            dfs(0, c)\n            dfs(rows - 1, c)\n     \
        \   }\n\n        var count = 0\n        for (r in 0 until rows) {\n        \
        \    for (c in 0 until cols) {\n                if (grid[r][c] == 0) {\n   \
        \                 count++\n                    dfs(r, c)\n                }\n\
        \            }\n        }\n        return count\n    }\n}"
      dart: "class Solution {\n  int closedIsland(List<List<int>> grid) {\n    int rows\
        \ = grid.length;\n    int cols = grid[0].length;\n\n    void dfs(int r, int\
        \ c) {\n      if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] ==\
        \ 1) return;\n      grid[r][c] = 1;\n      dfs(r + 1, c);\n      dfs(r - 1,\
        \ c);\n      dfs(r, c + 1);\n      dfs(r, c - 1);\n    }\n\n    for (int r =\
        \ 0; r < rows; r++) {\n      dfs(r, 0);\n      dfs(r, cols - 1);\n    }\n  \
        \  for (int c = 0; c < cols; c++) {\n      dfs(0, c);\n      dfs(rows - 1, c);\n\
        \    }\n\n    int count = 0;\n    for (int r = 0; r < rows; r++) {\n      for\
        \ (int c = 0; c < cols; c++) {\n        if (grid[r][c] == 0) {\n          count++;\n\
        \          dfs(r, c);\n        }\n      }\n    }\n    return count;\n  }\n}"
      go: "func closedIsland(grid [][]int) int {\n\trows := len(grid)\n\tcols := len(grid[0])\n\
        \tvar dfs func(r, c int)\n\tdfs = func(r, c int) {\n\t\tif r < 0 || r >= rows\
        \ || c < 0 || c >= cols || grid[r][c] == 1 {\n\t\t\treturn\n\t\t}\n\t\tgrid[r][c]\
        \ = 1\n\t\tdfs(r+1, c)\n\t\tdfs(r-1, c)\n\t\tdfs(r, c+1)\n\t\tdfs(r, c-1)\n\t\
        }\n\n\tfor r := 0; r < rows; r++ {\n\t\tdfs(r, 0)\n\t\tdfs(r, cols-1)\n\t}\n\
        \tfor c := 0; c < cols; c++ {\n\t\tdfs(0, c)\n\t\tdfs(rows-1, c)\n\t}\n\n\t\
        count := 0\n\tfor r := 0; r < rows; r++ {\n\t\tfor c := 0; c < cols; c++ {\n\
        \t\t\tif grid[r][c] == 0 {\n\t\t\t\tcount++\n\t\t\t\tdfs(r, c)\n\t\t\t}\n\t\t\
        }\n\t}\n\treturn count\n}"
      ruby: "# @param {Integer[][]} grid\n# @return {Integer}\ndef closed_island(grid)\n\
        \  rows = grid.length\n  cols = grid[0].length\n\n  dfs = lambda do |r, c|\n\
        \    return if r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == 1\n\
        \    grid[r][c] = 1\n    dfs.call(r + 1, c)\n    dfs.call(r - 1, c)\n    dfs.call(r,\
        \ c + 1)\n    dfs.call(r, c - 1)\n  end\n\n  (0...rows).each do |r|\n    dfs.call(r,\
        \ 0)\n    dfs.call(r, cols - 1)\n  end\n  (0...cols).each do |c|\n    dfs.call(0,\
        \ c)\n    dfs.call(rows - 1, c)\n  end\n\n  count = 0\n  (0...rows).each do\
        \ |r|\n    (0...cols).each do |c|\n      if grid[r][c] == 0\n        count +=\
        \ 1\n        dfs.call(r, c)\n      end\n    end\n  end\n  count\nend"
      scala: "object Solution {\n    def closedIsland(grid: Array[Array[Int]]): Int\
        \ = {\n        val rows = grid.length\n        val cols = grid(0).length\n\n\
        \        def dfs(r: Int, c: Int): Unit = {\n            if (r < 0 || r >= rows\
        \ || c < 0 || c >= cols || grid(r)(c) == 1) return\n            grid(r)(c) =\
        \ 1\n            dfs(r + 1, c)\n            dfs(r - 1, c)\n            dfs(r,\
        \ c + 1)\n            dfs(r, c - 1)\n        }\n\n        for (r <- 0 until\
        \ rows) {\n            dfs(r, 0)\n            dfs(r, cols - 1)\n        }\n\
        \        for (c <- 0 until cols) {\n            dfs(0, c)\n            dfs(rows\
        \ - 1, c)\n        }\n\n        var count = 0\n        for (r <- 0 until rows)\
        \ {\n            for (c <- 0 until cols) {\n                if (grid(r)(c) ==\
        \ 0) {\n                    count += 1\n                    dfs(r, c)\n    \
        \            }\n            }\n        }\n        count\n    }\n}"
      rust: "impl Solution {\n    pub fn closed_island(mut grid: Vec<Vec<i32>>) -> i32\
        \ {\n        let rows = grid.len() as i32;\n        let cols = grid[0].len()\
        \ as i32;\n\n        fn dfs(r: i32, c: i32, rows: i32, cols: i32, grid: &mut\
        \ Vec<Vec<i32>>) {\n            if r < 0 || r >= rows || c < 0 || c >= cols\
        \ || grid[r as usize][c as usize] == 1 {\n                return;\n        \
        \    }\n            grid[r as usize][c as usize] = 1;\n            dfs(r - 1,\
        \ c, rows, cols, grid);\n            dfs(r + 1, c, rows, cols, grid);\n    \
        \        dfs(r, c - 1, rows, cols, grid);\n            dfs(r, c + 1, rows, cols,\
        \ grid);\n        }\n\n        for r in 0..rows {\n            dfs(r, 0, rows,\
        \ cols, &mut grid);\n            dfs(r, cols - 1, rows, cols, &mut grid);\n\
        \        }\n        for c in 0..cols {\n            dfs(0, c, rows, cols, &mut\
        \ grid);\n            dfs(rows - 1, c, rows, cols, &mut grid);\n        }\n\n\
        \        let mut count = 0;\n        for r in 0..rows {\n            for c in\
        \ 0..cols {\n                if grid[r as usize][c as usize] == 0 {\n      \
        \              count += 1;\n                    dfs(r, c, rows, cols, &mut grid);\n\
        \                }\n            }\n        }\n        count\n    }\n}"
      racket: "(define/contract (closed-island grid)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer?)\n  (let* ([rows (length grid)]\n         [cols (length (car\
        \ grid))]\n         [vec-grid (list->vector (map list->vector grid))])\n   \
        \ (define (dfs r c)\n      (when (and (>= r 0) (< r rows) (>= c 0) (< c cols)\n\
        \                 (= (vector-ref (vector-ref vec-grid r) c) 0))\n        (vector-set!\
        \ (vector-ref vec-grid r) c 1)\n        (dfs (- r 1) c)\n        (dfs (+ r 1)\
        \ c)\n        (dfs r (- c 1))\n        (dfs r (+ c 1))))\n\n    (for ([r (in-range\
        \ rows)])\n      (when (= (vector-ref (vector-ref vec-grid r) 0) 0) (dfs r 0))\n\
        \      (when (= (vector-ref (vector-ref vec-grid r) (- cols 1)) 0) (dfs r (-\
        \ cols 1))))\n    (for ([c (in-range cols)])\n      (when (= (vector-ref (vector-ref\
        \ vec-grid 0) c) 0) (dfs 0 c))\n      (when (= (vector-ref (vector-ref vec-grid\
        \ (- rows 1)) c) 0) (dfs (- rows 1) c)))\n\n    (let ([count 0])\n      (for*\
        \ ([r (in-range rows)]\n             [c (in-range cols)])\n        (when (=\
        \ (vector-ref (vector-ref vec-grid r) c) 0)\n          (set! count (+ count\
        \ 1))\n          (dfs r c)))\n      count)))"
      erlang: "-spec closed_island(Grid :: [[integer()]]) -> integer().\nclosed_island(Grid)\
        \ ->\n    Rows = length(Grid),\n    Cols = length(hd(Grid)),\n    {GridMap,\
        \ _} = lists:foldl(fun(Row, {M1, R}) ->\n        {M2, _} = lists:foldl(fun(Val,\
        \ {M3, C}) ->\n            {maps:put({R, C}, Val, M3), C + 1}\n        end,\
        \ {M1, 0}, Row),\n        {M2, R + 1}\n    end, {#{}, 0}, Grid),\n    DFS =\
        \ fun DFS(R, C, Map, Self) ->\n        case maps:get({R, C}, Map, 1) of\n  \
        \          0 ->\n                M1 = maps:put({R, C}, 1, Map),\n          \
        \      M2 = Self(R - 1, C, M1, Self),\n                M3 = Self(R + 1, C, M2,\
        \ Self),\n                M4 = Self(R, C - 1, M3, Self),\n                Self(R,\
        \ C + 1, M4, Self);\n            1 -> Map\n        end\n    end,\n    Map1 =\
        \ lists:foldl(fun(R, MapAcc) ->\n        M1 = DFS(R, 0, MapAcc, DFS),\n    \
        \    DFS(R, Cols - 1, M1, DFS)\n    end, GridMap, lists:seq(0, Rows - 1)),\n\
        \    Map2 = lists:foldl(fun(C, MapAcc) ->\n        M1 = DFS(0, C, MapAcc, DFS),\n\
        \        DFS(Rows - 1, C, M1, DFS)\n    end, Map1, lists:seq(0, Cols - 1)),\n\
        \    {_FinalMap, Count} = lists:foldl(fun(R, {M_r, Acc_r}) ->\n        lists:foldl(fun(C,\
        \ {M_c, Acc_c}) ->\n            case maps:get({R, C}, M_c) of\n            \
        \    0 -> {DFS(R, C, M_c, DFS), Acc_c + 1};\n                1 -> {M_c, Acc_c}\n\
        \            end\n        end, {M_r, Acc_r}, lists:seq(0, Cols - 1))\n    end,\
        \ {Map2, 0}, lists:seq(0, Rows - 1)),\n    Count."
      elixir: "defmodule Solution do\n  @spec closed_island(grid :: [[integer]]) ::\
        \ integer\n  def closed_island(grid) do\n    rows = length(grid)\n    cols =\
        \ length(hd(grid))\n\n    grid_map = for {row, r} <- Enum.with_index(grid),\n\
        \                   {val, c} <- Enum.with_index(row),\n                   into:\
        \ %{}, do: {{r, c}, val}\n\n    dfs = fn dfs_fn, r, c, map ->\n      case Map.get(map,\
        \ {r, c}, 1) do\n        0 ->\n          map = Map.put(map, {r, c}, 1)\n   \
        \       map = dfs_fn.(dfs_fn, r - 1, c, map)\n          map = dfs_fn.(dfs_fn,\
        \ r + 1, c, map)\n          map = dfs_fn.(dfs_fn, r, c - 1, map)\n         \
        \ dfs_fn.(dfs_fn, r, c + 1, map)\n        1 -> map\n      end\n    end\n\n \
        \   grid_map = Enum.reduce(0..(rows - 1), grid_map, fn r, acc ->\n      acc\
        \ = dfs.(dfs, r, 0, acc)\n      dfs.(dfs, r, cols - 1, acc)\n    end)\n\n  \
        \  grid_map = Enum.reduce(0..(cols - 1), grid_map, fn c, acc ->\n      acc =\
        \ dfs.(dfs, 0, c, acc)\n      dfs.(dfs, rows - 1, c, acc)\n    end)\n\n    {_final_map,\
        \ count} = Enum.reduce(0..(rows - 1), {grid_map, 0}, fn r, {m, acc} ->\n   \
        \   Enum.reduce(0..(cols - 1), {m, acc}, fn c, {m_inner, acc_inner} ->\n   \
        \     if Map.get(m_inner, {r, c}) == 0 do\n          {dfs.(dfs, r, c, m_inner),\
        \ acc_inner + 1}\n        else\n          {m_inner, acc_inner}\n        end\n\
        \      end)\n    end)\n\n    count\n  end\nend"
    approach: 'The core of the algorithm is to eliminate any island that touches the
      boundary of the grid, as these cannot be closed islands. Since a closed island
      must be entirely surrounded by water (1s), any connected group of land cells (0s)
      that reaches the edge is considered ''open''. We use a depth-first search (DFS)
      to traverse all 0s starting from the four edges (top, bottom, left, right) and
      mark them as water (flipping them to 1s). This effectively ''floods'' all open
      islands so that they are no longer counted as potential candidates.


      After removing boundary-connected land, we iterate through the entire grid and
      look for remaining 0s. Every 0 we encounter must be part of a closed island. For
      each new closed island found, we increment our total count and perform a DFS starting
      from that cell to flip all its connected land cells to 1s. This marking process
      ensures that every cell in a closed island is counted exactly once. The final
      result is the total number of closed islands discovered during the interior scan.'
    time_complexity: O(M * N) with one-paragraph explanation. Here, M is the number
      of rows and N is the number of columns in the grid. We visit every cell a constant
      number of times during the initial boundary-clearing scan and the subsequent island-counting
      scan, ensuring the performance is linear relative to the total number of cells
      in the grid.
    space_complexity: O(M * N) with one-paragraph explanation. This is the worst-case
      space complexity for the recursion stack during the depth-first search. If the
      grid is composed entirely of land, the DFS could potentially reach a depth equal
      to the total number of cells, although in practice it is limited by the connectivity
      and shape of the land masses.
    elapsed_time: 206.65179824829102
    model: gemini-3-flash-preview
    generated_at: '2026-10-25 02:37:57 '
---

## Problem #1254: Number of Closed Islands

**Difficulty:** Medium

**Topics:** Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix

## Problem Description

<p>Given a 2D&nbsp;<code>grid</code> consists of <code>0s</code> (land)&nbsp;and <code>1s</code> (water).&nbsp; An <em>island</em> is a maximal 4-directionally connected group of <code><font face="monospace">0</font>s</code> and a <em>closed island</em>&nbsp;is an island <strong>totally</strong>&nbsp;(all left, top, right, bottom) surrounded by <code>1s.</code></p>

<p>Return the number of <em>closed islands</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/10/31/sample_3_1610.png" style="width: 240px; height: 120px;" /></p>

<pre>
<strong>Input:</strong> grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
Islands in gray are closed because they are completely surrounded by water (group of 1s).</pre>

<p><strong class="example">Example 2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/10/31/sample_4_1610.png" style="width: 160px; height: 80px;" /></p>

<pre>
<strong>Input:</strong> grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,1,1,1,1,1,1],
&nbsp;              [1,0,0,0,0,0,1],
&nbsp;              [1,0,1,1,1,0,1],
&nbsp;              [1,0,1,0,1,0,1],
&nbsp;              [1,0,1,1,1,0,1],
&nbsp;              [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= grid.length, grid[0].length &lt;= 100</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;=1</code></li>
</ul>


## Hints

1. Exclude connected group of 0s on the corners because they are not closed island.

2. Return number of connected component of 0s on the grid.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core of the algorithm is to eliminate any island that touches the boundary of the grid, as these cannot be closed islands. Since a closed island must be entirely surrounded by water (1s), any connected group of land cells (0s) that reaches the edge is considered 'open'. We use a depth-first search (DFS) to traverse all 0s starting from the four edges (top, bottom, left, right) and mark them as water (flipping them to 1s). This effectively 'floods' all open islands so that they are no longer counted as potential candidates.

After removing boundary-connected land, we iterate through the entire grid and look for remaining 0s. Every 0 we encounter must be part of a closed island. For each new closed island found, we increment our total count and perform a DFS starting from that cell to flip all its connected land cells to 1s. This marking process ensures that every cell in a closed island is counted exactly once. The final result is the total number of closed islands discovered during the interior scan.

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
    void dfs(vector<vector<int>>& grid, int r, int c) {
        if (r < 0 || r >= grid.size() || c < 0 || c >= grid[0].size() || grid[r][c] == 1) {
            return;
        }
        grid[r][c] = 1;
        dfs(grid, r + 1, c);
        dfs(grid, r - 1, c);
        dfs(grid, r, c + 1);
        dfs(grid, r, c - 1);
    }

    int closedIsland(vector<vector<int>>& grid) {
        if (grid.empty()) return 0;
        int rows = grid.size();
        int cols = grid[0].size();

        for (int i = 0; i < rows; i++) {
            dfs(grid, i, 0);
            dfs(grid, i, cols - 1);
        }
        for (int j = 0; j < cols; j++) {
            dfs(grid, 0, j);
            dfs(grid, rows - 1, j);
        }

        int count = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 0) {
                    count++;
                    dfs(grid, i, j);
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
    public int closedIsland(int[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        int rows = grid.length;
        int cols = grid[0].length;

        for (int i = 0; i < rows; i++) {
            dfs(grid, i, 0);
            dfs(grid, i, cols - 1);
        }
        for (int j = 0; j < cols; j++) {
            dfs(grid, 0, j);
            dfs(grid, rows - 1, j);
        }

        int count = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 0) {
                    count++;
                    dfs(grid, i, j);
                }
            }
        }
        return count;
    }

    private void dfs(int[][] grid, int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] == 1) {
            return;
        }
        grid[r][c] = 1;
        dfs(grid, r + 1, c);
        dfs(grid, r - 1, c);
        dfs(grid, r, c + 1);
        dfs(grid, r, c - 1);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import sys

class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        sys.setrecursionlimit(10000)
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return
            grid[r][c] = 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    count += 1
                    dfs(r, c)
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import sys

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        sys.setrecursionlimit(10000)
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return
            grid[r][c] = 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    count += 1
                    dfs(r, c)
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
void dfs(int** grid, int r, int c, int rows, int cols) {
    if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == 1) {
        return;
    }
    grid[r][c] = 1;
    dfs(grid, r + 1, c, rows, cols);
    dfs(grid, r - 1, c, rows, cols);
    dfs(grid, r, c + 1, rows, cols);
    dfs(grid, r, c - 1, rows, cols);
}

int closedIsland(int** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0) return 0;
    int rows = gridSize;
    int cols = gridColSize[0];

    for (int i = 0; i < rows; i++) {
        dfs(grid, i, 0, rows, cols);
        dfs(grid, i, cols - 1, rows, cols);
    }
    for (int j = 0; j < cols; j++) {
        dfs(grid, 0, j, rows, cols);
        dfs(grid, rows - 1, j, rows, cols);
    }

    int count = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == 0) {
                count++;
                dfs(grid, i, j, rows, cols);
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
    public int ClosedIsland(int[][] grid) {
        int rows = grid.Length;
        int cols = grid[0].Length;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (i == 0 || i == rows - 1 || j == 0 || j == cols - 1) {
                    if (grid[i][j] == 0) {
                        Dfs(grid, i, j);
                    }
                }
            }
        }

        int count = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 0) {
                    count++;
                    Dfs(grid, i, j);
                }
            }
        }

        return count;
    }

    private void Dfs(int[][] grid, int r, int c) {
        if (r < 0 || r >= grid.Length || c < 0 || c >= grid[0].Length || grid[r][c] == 1) {
            return;
        }

        grid[r][c] = 1;
        Dfs(grid, r + 1, c);
        Dfs(grid, r - 1, c);
        Dfs(grid, r, c + 1);
        Dfs(grid, r, c - 1);
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
var closedIsland = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;

    function dfs(r, c) {
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] === 1) {
            return;
        }
        grid[r][c] = 1;
        dfs(r + 1, c);
        dfs(r - 1, c);
        dfs(r, c + 1);
        dfs(r, c - 1);
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (i === 0 || i === rows - 1 || j === 0 || j === cols - 1) {
                if (grid[i][j] === 0) {
                    dfs(i, j);
                }
            }
        }
    }

    let count = 0;
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (grid[i][j] === 0) {
                count++;
                dfs(i, j);
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
function closedIsland(grid: number[][]): number {
    const rows = grid.length;
    const cols = grid[0].length;

    function dfs(r: number, c: number): void {
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] === 1) {
            return;
        }
        grid[r][c] = 1;
        dfs(r + 1, c);
        dfs(r - 1, c);
        dfs(r, c + 1);
        dfs(r, c - 1);
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (i === 0 || i === rows - 1 || j === 0 || j === cols - 1) {
                if (grid[i][j] === 0) {
                    dfs(i, j);
                }
            }
        }
    }

    let count = 0;
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (grid[i][j] === 0) {
                count++;
                dfs(i, j);
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
     * @return Integer
     */
    function closedIsland($grid) {
        $rows = count($grid);
        if ($rows === 0) return 0;
        $cols = count($grid[0]);

        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                if ($i == 0 || $i == $rows - 1 || $j == 0 || $j == $cols - 1) {
                    if ($grid[$i][$j] == 0) {
                        $this->dfs($grid, $i, $j, $rows, $cols);
                    }
                }
            }
        }

        $count = 0;
        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                if ($grid[$i][$j] == 0) {
                    $count++;
                    $this->dfs($grid, $i, $j, $rows, $cols);
                }
            }
        }

        return $count;
    }

    function dfs(&$grid, $r, $c, $rows, $cols) {
        if ($r < 0 || $r >= $rows || $c < 0 || $c >= $cols || $grid[$r][$c] == 1) {
            return;
        }

        $grid[$r][$c] = 1;
        $this->dfs($grid, $r + 1, $c, $rows, $cols);
        $this->dfs($grid, $r - 1, $c, $rows, $cols);
        $this->dfs($grid, $r, $c + 1, $rows, $cols);
        $this->dfs($grid, $r, $c - 1, $rows, $cols);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func closedIsland(_ grid: [[Int]]) -> Int {
        var grid = grid
        let rows = grid.count
        if rows == 0 { return 0 }
        let cols = grid[0].count

        func dfs(_ r: Int, _ c: Int) {
            if r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == 1 {
                return
            }
            grid[r][c] = 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        }

        for i in 0..<rows {
            for j in 0..<cols {
                if i == 0 || i == rows - 1 || j == 0 || j == cols - 1 {
                    if grid[i][j] == 0 {
                        dfs(i, j)
                    }
                }
            }
        }

        var count = 0
        for i in 0..<rows {
            for j in 0..<cols {
                if grid[i][j] == 0 {
                    count += 1
                    dfs(i, j)
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
    fun closedIsland(grid: Array<IntArray>): Int {
        val rows = grid.size
        val cols = grid[0].size

        fun dfs(r: Int, c: Int) {
            if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == 1) return
            grid[r][c] = 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        }

        for (r in 0 until rows) {
            dfs(r, 0)
            dfs(r, cols - 1)
        }
        for (c in 0 until cols) {
            dfs(0, c)
            dfs(rows - 1, c)
        }

        var count = 0
        for (r in 0 until rows) {
            for (c in 0 until cols) {
                if (grid[r][c] == 0) {
                    count++
                    dfs(r, c)
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
  int closedIsland(List<List<int>> grid) {
    int rows = grid.length;
    int cols = grid[0].length;

    void dfs(int r, int c) {
      if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == 1) return;
      grid[r][c] = 1;
      dfs(r + 1, c);
      dfs(r - 1, c);
      dfs(r, c + 1);
      dfs(r, c - 1);
    }

    for (int r = 0; r < rows; r++) {
      dfs(r, 0);
      dfs(r, cols - 1);
    }
    for (int c = 0; c < cols; c++) {
      dfs(0, c);
      dfs(rows - 1, c);
    }

    int count = 0;
    for (int r = 0; r < rows; r++) {
      for (int c = 0; c < cols; c++) {
        if (grid[r][c] == 0) {
          count++;
          dfs(r, c);
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
func closedIsland(grid [][]int) int {
	rows := len(grid)
	cols := len(grid[0])
	var dfs func(r, c int)
	dfs = func(r, c int) {
		if r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == 1 {
			return
		}
		grid[r][c] = 1
		dfs(r+1, c)
		dfs(r-1, c)
		dfs(r, c+1)
		dfs(r, c-1)
	}

	for r := 0; r < rows; r++ {
		dfs(r, 0)
		dfs(r, cols-1)
	}
	for c := 0; c < cols; c++ {
		dfs(0, c)
		dfs(rows-1, c)
	}

	count := 0
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if grid[r][c] == 0 {
				count++
				dfs(r, c)
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
# @return {Integer}
def closed_island(grid)
  rows = grid.length
  cols = grid[0].length

  dfs = lambda do |r, c|
    return if r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == 1
    grid[r][c] = 1
    dfs.call(r + 1, c)
    dfs.call(r - 1, c)
    dfs.call(r, c + 1)
    dfs.call(r, c - 1)
  end

  (0...rows).each do |r|
    dfs.call(r, 0)
    dfs.call(r, cols - 1)
  end
  (0...cols).each do |c|
    dfs.call(0, c)
    dfs.call(rows - 1, c)
  end

  count = 0
  (0...rows).each do |r|
    (0...cols).each do |c|
      if grid[r][c] == 0
        count += 1
        dfs.call(r, c)
      end
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
    def closedIsland(grid: Array[Array[Int]]): Int = {
        val rows = grid.length
        val cols = grid(0).length

        def dfs(r: Int, c: Int): Unit = {
            if (r < 0 || r >= rows || c < 0 || c >= cols || grid(r)(c) == 1) return
            grid(r)(c) = 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        }

        for (r <- 0 until rows) {
            dfs(r, 0)
            dfs(r, cols - 1)
        }
        for (c <- 0 until cols) {
            dfs(0, c)
            dfs(rows - 1, c)
        }

        var count = 0
        for (r <- 0 until rows) {
            for (c <- 0 until cols) {
                if (grid(r)(c) == 0) {
                    count += 1
                    dfs(r, c)
                }
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
    pub fn closed_island(mut grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len() as i32;
        let cols = grid[0].len() as i32;

        fn dfs(r: i32, c: i32, rows: i32, cols: i32, grid: &mut Vec<Vec<i32>>) {
            if r < 0 || r >= rows || c < 0 || c >= cols || grid[r as usize][c as usize] == 1 {
                return;
            }
            grid[r as usize][c as usize] = 1;
            dfs(r - 1, c, rows, cols, grid);
            dfs(r + 1, c, rows, cols, grid);
            dfs(r, c - 1, rows, cols, grid);
            dfs(r, c + 1, rows, cols, grid);
        }

        for r in 0..rows {
            dfs(r, 0, rows, cols, &mut grid);
            dfs(r, cols - 1, rows, cols, &mut grid);
        }
        for c in 0..cols {
            dfs(0, c, rows, cols, &mut grid);
            dfs(rows - 1, c, rows, cols, &mut grid);
        }

        let mut count = 0;
        for r in 0..rows {
            for c in 0..cols {
                if grid[r as usize][c as usize] == 0 {
                    count += 1;
                    dfs(r, c, rows, cols, &mut grid);
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
(define/contract (closed-island grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([rows (length grid)]
         [cols (length (car grid))]
         [vec-grid (list->vector (map list->vector grid))])
    (define (dfs r c)
      (when (and (>= r 0) (< r rows) (>= c 0) (< c cols)
                 (= (vector-ref (vector-ref vec-grid r) c) 0))
        (vector-set! (vector-ref vec-grid r) c 1)
        (dfs (- r 1) c)
        (dfs (+ r 1) c)
        (dfs r (- c 1))
        (dfs r (+ c 1))))

    (for ([r (in-range rows)])
      (when (= (vector-ref (vector-ref vec-grid r) 0) 0) (dfs r 0))
      (when (= (vector-ref (vector-ref vec-grid r) (- cols 1)) 0) (dfs r (- cols 1))))
    (for ([c (in-range cols)])
      (when (= (vector-ref (vector-ref vec-grid 0) c) 0) (dfs 0 c))
      (when (= (vector-ref (vector-ref vec-grid (- rows 1)) c) 0) (dfs (- rows 1) c)))

    (let ([count 0])
      (for* ([r (in-range rows)]
             [c (in-range cols)])
        (when (= (vector-ref (vector-ref vec-grid r) c) 0)
          (set! count (+ count 1))
          (dfs r c)))
      count)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec closed_island(Grid :: [[integer()]]) -> integer().
closed_island(Grid) ->
    Rows = length(Grid),
    Cols = length(hd(Grid)),
    {GridMap, _} = lists:foldl(fun(Row, {M1, R}) ->
        {M2, _} = lists:foldl(fun(Val, {M3, C}) ->
            {maps:put({R, C}, Val, M3), C + 1}
        end, {M1, 0}, Row),
        {M2, R + 1}
    end, {#{}, 0}, Grid),
    DFS = fun DFS(R, C, Map, Self) ->
        case maps:get({R, C}, Map, 1) of
            0 ->
                M1 = maps:put({R, C}, 1, Map),
                M2 = Self(R - 1, C, M1, Self),
                M3 = Self(R + 1, C, M2, Self),
                M4 = Self(R, C - 1, M3, Self),
                Self(R, C + 1, M4, Self);
            1 -> Map
        end
    end,
    Map1 = lists:foldl(fun(R, MapAcc) ->
        M1 = DFS(R, 0, MapAcc, DFS),
        DFS(R, Cols - 1, M1, DFS)
    end, GridMap, lists:seq(0, Rows - 1)),
    Map2 = lists:foldl(fun(C, MapAcc) ->
        M1 = DFS(0, C, MapAcc, DFS),
        DFS(Rows - 1, C, M1, DFS)
    end, Map1, lists:seq(0, Cols - 1)),
    {_FinalMap, Count} = lists:foldl(fun(R, {M_r, Acc_r}) ->
        lists:foldl(fun(C, {M_c, Acc_c}) ->
            case maps:get({R, C}, M_c) of
                0 -> {DFS(R, C, M_c, DFS), Acc_c + 1};
                1 -> {M_c, Acc_c}
            end
        end, {M_r, Acc_r}, lists:seq(0, Cols - 1))
    end, {Map2, 0}, lists:seq(0, Rows - 1)),
    Count.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec closed_island(grid :: [[integer]]) :: integer
  def closed_island(grid) do
    rows = length(grid)
    cols = length(hd(grid))

    grid_map = for {row, r} <- Enum.with_index(grid),
                   {val, c} <- Enum.with_index(row),
                   into: %{}, do: {{r, c}, val}

    dfs = fn dfs_fn, r, c, map ->
      case Map.get(map, {r, c}, 1) do
        0 ->
          map = Map.put(map, {r, c}, 1)
          map = dfs_fn.(dfs_fn, r - 1, c, map)
          map = dfs_fn.(dfs_fn, r + 1, c, map)
          map = dfs_fn.(dfs_fn, r, c - 1, map)
          dfs_fn.(dfs_fn, r, c + 1, map)
        1 -> map
      end
    end

    grid_map = Enum.reduce(0..(rows - 1), grid_map, fn r, acc ->
      acc = dfs.(dfs, r, 0, acc)
      dfs.(dfs, r, cols - 1, acc)
    end)

    grid_map = Enum.reduce(0..(cols - 1), grid_map, fn c, acc ->
      acc = dfs.(dfs, 0, c, acc)
      dfs.(dfs, rows - 1, c, acc)
    end)

    {_final_map, count} = Enum.reduce(0..(rows - 1), {grid_map, 0}, fn r, {m, acc} ->
      Enum.reduce(0..(cols - 1), {m, acc}, fn c, {m_inner, acc_inner} ->
        if Map.get(m_inner, {r, c}) == 0 do
          {dfs.(dfs, r, c, m_inner), acc_inner + 1}
        else
          {m_inner, acc_inner}
        end
      end)
    end)

    count
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(M * N) with one-paragraph explanation. Here, M is the number of rows and N is the number of columns in the grid. We visit every cell a constant number of times during the initial boundary-clearing scan and the subsequent island-counting scan, ensuring the performance is linear relative to the total number of cells in the grid.
- **Space Complexity:** O(M * N) with one-paragraph explanation. This is the worst-case space complexity for the recursion stack during the depth-first search. If the grid is composed entirely of land, the DFS could potentially reach a depth equal to the total number of cells, although in practice it is limited by the connectivity and shape of the land masses.
