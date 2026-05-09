---
layout: post
title: "Cyclically Rotating a Grid"
date: 2026-05-09 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Matrix", "Simulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/cyclically-rotating-a-grid/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<vector<int>> rotateGrid(vector<vector<int>>&\
        \ grid, int k) {\n        int m = grid.size(), n = grid[0].size();\n       \
        \ int layers = min(m, n) / 2;\n        for (int i = 0; i < layers; ++i) {\n\
        \            vector<int> layer;\n            for (int r = i; r < m - 1 - i;\
        \ ++r) layer.push_back(grid[r][i]);\n            for (int c = i; c < n - 1 -\
        \ i; ++c) layer.push_back(grid[m - 1 - i][c]);\n            for (int r = m -\
        \ 1 - i; r > i; --r) layer.push_back(grid[r][n - 1 - i]);\n            for (int\
        \ c = n - 1 - i; c > i; --c) layer.push_back(grid[i][c]);\n\n            int\
        \ len = layer.size();\n            int rk = k % len;\n            int idx =\
        \ 0;\n            for (int r = i; r < m - 1 - i; ++r) grid[r][i] = layer[(idx++\
        \ + rk) % len];\n            for (int c = i; c < n - 1 - i; ++c) grid[m - 1\
        \ - i][c] = layer[(idx++ + rk) % len];\n            for (int r = m - 1 - i;\
        \ r > i; --r) grid[r][n - 1 - i] = layer[(idx++ + rk) % len];\n            for\
        \ (int c = n - 1 - i; c > i; --c) grid[i][c] = layer[(idx++ + rk) % len];\n\
        \        }\n        return grid;\n    }\n};"
      java: "class Solution {\n    public int[][] rotateGrid(int[][] grid, int k) {\n\
        \        int m = grid.length, n = grid[0].length;\n        int layers = Math.min(m,\
        \ n) / 2;\n        for (int i = 0; i < layers; ++i) {\n            int len =\
        \ 2 * (m - 2 * i) + 2 * (n - 2 * i) - 4;\n            int[] layer = new int[len];\n\
        \            int idx = 0;\n            for (int r = i; r < m - 1 - i; ++r) layer[idx++]\
        \ = grid[r][i];\n            for (int c = i; c < n - 1 - i; ++c) layer[idx++]\
        \ = grid[m - 1 - i][c];\n            for (int r = m - 1 - i; r > i; --r) layer[idx++]\
        \ = grid[r][n - 1 - i];\n            for (int c = n - 1 - i; c > i; --c) layer[idx++]\
        \ = grid[i][c];\n\n            int rk = k % len;\n            idx = 0;\n   \
        \         for (int r = i; r < m - 1 - i; ++r) grid[r][i] = layer[(idx++ + rk)\
        \ % len];\n            for (int c = i; c < n - 1 - i; ++c) grid[m - 1 - i][c]\
        \ = layer[(idx++ + rk) % len];\n            for (int r = m - 1 - i; r > i; --r)\
        \ grid[r][n - 1 - i] = layer[(idx++ + rk) % len];\n            for (int c =\
        \ n - 1 - i; c > i; --c) grid[i][c] = layer[(idx++ + rk) % len];\n        }\n\
        \        return grid;\n    }\n}"
      python: "class Solution(object):\n    def rotateGrid(self, grid, k):\n       \
        \ \"\"\"\n        :type grid: List[List[int]]\n        :type k: int\n      \
        \  :rtype: List[List[int]]\n        \"\"\"\n        m, n = len(grid), len(grid[0])\n\
        \        num_layers = min(m, n) // 2\n        for i in range(num_layers):\n\
        \            layer = []\n            for r in range(i, m - 1 - i): layer.append(grid[r][i])\n\
        \            for c in range(i, n - 1 - i): layer.append(grid[m - 1 - i][c])\n\
        \            for r in range(m - 1 - i, i, -1): layer.append(grid[r][n - 1 -\
        \ i])\n            for c in range(n - 1 - i, i, -1): layer.append(grid[i][c])\n\
        \n            length = len(layer)\n            rk = k % length\n           \
        \ idx = 0\n            for r in range(i, m - 1 - i):\n                grid[r][i]\
        \ = layer[(idx + rk) % length]\n                idx += 1\n            for c\
        \ in range(i, n - 1 - i):\n                grid[m - 1 - i][c] = layer[(idx +\
        \ rk) % length]\n                idx += 1\n            for r in range(m - 1\
        \ - i, i, -1):\n                grid[r][n - 1 - i] = layer[(idx + rk) % length]\n\
        \                idx += 1\n            for c in range(n - 1 - i, i, -1):\n \
        \               grid[i][c] = layer[(idx + rk) % length]\n                idx\
        \ += 1\n        return grid"
      python3: "class Solution:\n    def rotateGrid(self, grid: List[List[int]], k:\
        \ int) -> List[List[int]]:\n        m, n = len(grid), len(grid[0])\n       \
        \ num_layers = min(m, n) // 2\n        for i in range(num_layers):\n       \
        \     layer = []\n            for r in range(i, m - 1 - i): layer.append(grid[r][i])\n\
        \            for c in range(i, n - 1 - i): layer.append(grid[m - 1 - i][c])\n\
        \            for r in range(m - 1 - i, i, -1): layer.append(grid[r][n - 1 -\
        \ i])\n            for c in range(n - 1 - i, i, -1): layer.append(grid[i][c])\n\
        \n            length = len(layer)\n            rk = k % length\n           \
        \ idx = 0\n            for r in range(i, m - 1 - i):\n                grid[r][i]\
        \ = layer[(idx + rk) % length]\n                idx += 1\n            for c\
        \ in range(i, n - 1 - i):\n                grid[m - 1 - i][c] = layer[(idx +\
        \ rk) % length]\n                idx += 1\n            for r in range(m - 1\
        \ - i, i, -1):\n                grid[r][n - 1 - i] = layer[(idx + rk) % length]\n\
        \                idx += 1\n            for c in range(n - 1 - i, i, -1):\n \
        \               grid[i][c] = layer[(idx + rk) % length]\n                idx\
        \ += 1\n        return grid"
      c: "/**\n * Return an array of arrays of size *returnSize.\n * The sizes of the\
        \ arrays are returned as *returnColumnSizes array.\n * Note: Both returned array\
        \ and *columnSizes array must be malloced, assume caller calls free().\n */\n\
        int** rotateGrid(int** grid, int gridSize, int* gridColSize, int k, int* returnSize,\
        \ int** returnColumnSizes){\n    int m = gridSize;\n    int n = gridColSize[0];\n\
        \    int** res = (int**)malloc(m * sizeof(int*));\n    *returnColumnSizes =\
        \ (int*)malloc(m * sizeof(int));\n    *returnSize = m;\n    for (int i = 0;\
        \ i < m; i++) {\n        res[i] = (int*)malloc(n * sizeof(int));\n        (*returnColumnSizes)[i]\
        \ = n;\n        for (int j = 0; j < n; j++) res[i][j] = grid[i][j];\n    }\n\
        \n    int num_layers = (m < n ? m : n) / 2;\n    for (int i = 0; i < num_layers;\
        \ i++) {\n        int len = 2 * (m - 2 * i) + 2 * (n - 2 * i) - 4;\n       \
        \ int* layer = (int*)malloc(len * sizeof(int));\n        int idx = 0;\n    \
        \    for (int r = i; r < m - 1 - i; r++) layer[idx++] = res[r][i];\n       \
        \ for (int c = i; c < n - 1 - i; c++) layer[idx++] = res[m - 1 - i][c];\n  \
        \      for (int r = m - 1 - i; r > i; r--) layer[idx++] = res[r][n - 1 - i];\n\
        \        for (int c = n - 1 - i; c > i; c--) layer[idx++] = res[i][c];\n\n \
        \       int rk = k % len;\n        idx = 0;\n        for (int r = i; r < m -\
        \ 1 - i; r++) res[r][i] = layer[(idx++ + rk) % len];\n        for (int c = i;\
        \ c < n - 1 - i; c++) res[m - 1 - i][c] = layer[(idx++ + rk) % len];\n     \
        \   for (int r = m - 1 - i; r > i; r--) res[r][n - 1 - i] = layer[(idx++ + rk)\
        \ % len];\n        for (int c = n - 1 - i; c > i; c--) res[i][c] = layer[(idx++\
        \ + rk) % len];\n        free(layer);\n    }\n\n    return res;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int[][] RotateGrid(int[][] grid, int k) {\n        int m = grid.Length;\n\
        \        int n = grid[0].Length;\n        int numLayers = Math.Min(m, n) / 2;\n\
        \n        for (int l = 0; l < numLayers; l++) {\n            List<int[]> path\
        \ = new List<int[]>();\n\n            for (int r = l; r < m - 1 - l; r++) path.Add(new\
        \ int[] { r, l });\n            for (int c = l; c < n - 1 - l; c++) path.Add(new\
        \ int[] { m - 1 - l, c });\n            for (int r = m - 1 - l; r > l; r--)\
        \ path.Add(new int[] { r, n - 1 - l });\n            for (int c = n - 1 - l;\
        \ c > l; c--) path.Add(new int[] { l, c });\n\n            int len = path.Count;\n\
        \            int actualK = k % len;\n            int[] vals = new int[len];\n\
        \            for (int i = 0; i < len; i++) {\n                vals[i] = grid[path[i][0]][path[i][1]];\n\
        \            }\n\n            for (int i = 0; i < len; i++) {\n            \
        \    int[] nextPos = path[(i + actualK) % len];\n                grid[nextPos[0]][nextPos[1]]\
        \ = vals[i];\n            }\n        }\n\n        return grid;\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @param {number} k\n * @return\
        \ {number[][]}\n */\nvar rotateGrid = function(grid, k) {\n    const m = grid.length;\n\
        \    const n = grid[0].length;\n    const numLayers = Math.min(m, n) / 2;\n\n\
        \    for (let l = 0; l < numLayers; l++) {\n        const path = [];\n\n   \
        \     for (let r = l; r < m - 1 - l; r++) path.push([r, l]);\n        for (let\
        \ c = l; c < n - 1 - l; c++) path.push([m - 1 - l, c]);\n        for (let r\
        \ = m - 1 - l; r > l; r--) path.push([r, n - 1 - l]);\n        for (let c =\
        \ n - 1 - l; c > l; c--) path.push([l, c]);\n\n        const len = path.length;\n\
        \        const actualK = k % len;\n        const vals = path.map(p => grid[p[0]][p[1]]);\n\
        \n        for (let i = 0; i < len; i++) {\n            const [nr, nc] = path[(i\
        \ + actualK) % len];\n            grid[nr][nc] = vals[i];\n        }\n    }\n\
        \n    return grid;\n};"
      typescript: "function rotateGrid(grid: number[][], k: number): number[][] {\n\
        \    const m = grid.length;\n    const n = grid[0].length;\n    const numLayers\
        \ = Math.floor(Math.min(m, n) / 2);\n\n    for (let l = 0; l < numLayers; l++)\
        \ {\n        const path: [number, number][] = [];\n\n        for (let r = l;\
        \ r < m - 1 - l; r++) path.push([r, l]);\n        for (let c = l; c < n - 1\
        \ - l; c++) path.push([m - 1 - l, c]);\n        for (let r = m - 1 - l; r >\
        \ l; r--) path.push([r, n - 1 - l]);\n        for (let c = n - 1 - l; c > l;\
        \ c--) path.push([l, c]);\n\n        const len = path.length;\n        const\
        \ actualK = k % len;\n        const vals = path.map(p => grid[p[0]][p[1]]);\n\
        \n        for (let i = 0; i < len; i++) {\n            const [nr, nc] = path[(i\
        \ + actualK) % len];\n            grid[nr][nc] = vals[i];\n        }\n    }\n\
        \n    return grid;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @param\
        \ Integer $k\n     * @return Integer[][]\n     */\n    function rotateGrid($grid,\
        \ $k) {\n        $m = count($grid);\n        $n = count($grid[0]);\n       \
        \ $numLayers = min($m, $n) / 2;\n\n        for ($l = 0; $l < $numLayers; $l++)\
        \ {\n            $path = [];\n\n            for ($r = $l; $r < $m - 1 - $l;\
        \ $r++) $path[] = [$r, $l];\n            for ($c = $l; $c < $n - 1 - $l; $c++)\
        \ $path[] = [$m - 1 - $l, $c];\n            for ($r = $m - 1 - $l; $r > $l;\
        \ $r--) $path[] = [$r, $n - 1 - $l];\n            for ($c = $n - 1 - $l; $c\
        \ > $l; $c--) $path[] = [$l, $c];\n\n            $len = count($path);\n    \
        \        $actualK = $k % $len;\n            $vals = [];\n            foreach\
        \ ($path as $p) {\n                $vals[] = $grid[$p[0]][$p[1]];\n        \
        \    }\n\n            for ($i = 0; $i < $len; $i++) {\n                $nextPos\
        \ = $path[($i + $actualK) % $len];\n                $grid[$nextPos[0]][$nextPos[1]]\
        \ = $vals[$i];\n            }\n        }\n\n        return $grid;\n    }\n}"
      swift: "class Solution {\n    func rotateGrid(_ grid: [[Int]], _ k: Int) -> [[Int]]\
        \ {\n        var grid = grid\n        let m = grid.count\n        let n = grid[0].count\n\
        \        let numLayers = min(m, n) / 2\n\n        for l in 0..<numLayers {\n\
        \            var path = [(Int, Int)]()\n\n            for r in l..<(m - 1 -\
        \ l) {\n                path.append((r, l))\n            }\n            for\
        \ c in l..<(n - 1 - l) {\n                path.append((m - 1 - l, c))\n    \
        \        }\n            for r in stride(from: m - 1 - l, to: l, by: -1) {\n\
        \                path.append((r, n - 1 - l))\n            }\n            for\
        \ c in stride(from: n - 1 - l, to: l, by: -1) {\n                path.append((l,\
        \ c))\n            }\n\n            let count = path.count\n            let\
        \ actualK = k % count\n            var vals = [Int]()\n            for p in\
        \ path {\n                vals.append(grid[p.0][p.1])\n            }\n\n   \
        \         for i in 0..<count {\n                let nextPos = path[(i + actualK)\
        \ % count]\n                grid[nextPos.0][nextPos.1] = vals[i]\n         \
        \   }\n        }\n\n        return grid\n    }\n}"
      kotlin: "class Solution {\n    fun rotateGrid(grid: Array<IntArray>, k: Int):\
        \ Array<IntArray> {\n        val m = grid.size\n        val n = grid[0].size\n\
        \        val numLayers = (if (m < n) m else n) / 2\n        for (i in 0 until\
        \ numLayers) {\n            val r1 = i\n            val c1 = i\n           \
        \ val r2 = m - 1 - i\n            val c2 = n - 1 - i\n\n            val elements\
        \ = mutableListOf<Int>()\n            for (c in c1 until c2) elements.add(grid[r1][c])\n\
        \            for (r in r1 until r2) elements.add(grid[r][c2])\n            for\
        \ (c in c2 downTo c1 + 1) elements.add(grid[r2][c])\n            for (r in r2\
        \ downTo r1 + 1) elements.add(grid[r][c1])\n\n            val size = elements.size\n\
        \            val shift = k % size\n            var idx = 0\n            for\
        \ (c in c1 until c2) {\n                grid[r1][c] = elements[(idx + shift)\
        \ % size]\n                idx++\n            }\n            for (r in r1 until\
        \ r2) {\n                grid[r][c2] = elements[(idx + shift) % size]\n    \
        \            idx++\n            }\n            for (c in c2 downTo c1 + 1) {\n\
        \                grid[r2][c] = elements[(idx + shift) % size]\n            \
        \    idx++\n            }\n            for (r in r2 downTo r1 + 1) {\n     \
        \           grid[r][c1] = elements[(idx + shift) % size]\n                idx++\n\
        \            }\n        }\n        return grid\n    }\n}"
      dart: "class Solution {\n  List<List<int>> rotateGrid(List<List<int>> grid, int\
        \ k) {\n    int m = grid.length;\n    int n = grid[0].length;\n    int numLayers\
        \ = (m < n ? m : n) ~/ 2;\n    for (int i = 0; i < numLayers; i++) {\n     \
        \ int r1 = i, c1 = i;\n      int r2 = m - 1 - i, c2 = n - 1 - i;\n      List<int>\
        \ elements = [];\n      for (int c = c1; c < c2; c++) elements.add(grid[r1][c]);\n\
        \      for (int r = r1; r < r2; r++) elements.add(grid[r][c2]);\n      for (int\
        \ c = c2; c > c1; c--) elements.add(grid[r2][c]);\n      for (int r = r2; r\
        \ > r1; r--) elements.add(grid[r][c1]);\n\n      int size = elements.length;\n\
        \      int shift = k % size;\n      int idx = 0;\n      for (int c = c1; c <\
        \ c2; c++) {\n        grid[r1][c] = elements[(idx + shift) % size];\n      \
        \  idx++;\n      }\n      for (int r = r1; r < r2; r++) {\n        grid[r][c2]\
        \ = elements[(idx + shift) % size];\n        idx++;\n      }\n      for (int\
        \ c = c2; c > c1; c--) {\n        grid[r2][c] = elements[(idx + shift) % size];\n\
        \        idx++;\n      }\n      for (int r = r2; r > r1; r--) {\n        grid[r][c1]\
        \ = elements[(idx + shift) % size];\n        idx++;\n      }\n    }\n    return\
        \ grid;\n  }\n}"
      go: "func rotateGrid(grid [][]int, k int) [][]int {\n    m := len(grid)\n    n\
        \ := len(grid[0])\n    numLayers := m\n    if n < m {\n        numLayers = n\n\
        \    }\n    numLayers /= 2\n    for i := 0; i < numLayers; i++ {\n        r1,\
        \ c1 := i, i\n        r2, c2 := m-1-i, n-1-i\n\n        elements := make([]int,\
        \ 0, 2*(r2-r1+c2-c1))\n        for c := c1; c < c2; c++ { elements = append(elements,\
        \ grid[r1][c]) }\n        for r := r1; r < r2; r++ { elements = append(elements,\
        \ grid[r][c2]) }\n        for c := c2; c > c1; c-- { elements = append(elements,\
        \ grid[r2][c]) }\n        for r := r2; r > r1; r-- { elements = append(elements,\
        \ grid[r][c1]) }\n\n        size := len(elements)\n        shift := k % size\n\
        \        idx := 0\n        for c := c1; c < c2; c++ {\n            grid[r1][c]\
        \ = elements[(idx+shift)%size]\n            idx++\n        }\n        for r\
        \ := r1; r < r2; r++ {\n            grid[r][c2] = elements[(idx+shift)%size]\n\
        \            idx++\n        }\n        for c := c2; c > c1; c-- {\n        \
        \    grid[r2][c] = elements[(idx+shift)%size]\n            idx++\n        }\n\
        \        for r := r2; r > r1; r-- {\n            grid[r][c1] = elements[(idx+shift)%size]\n\
        \            idx++\n        }\n    }\n    return grid\n}"
      ruby: "# @param {Integer[][]} grid\n# @param {Integer} k\n# @return {Integer[][]}\n\
        def rotate_grid(grid, k)\n    m = grid.length\n    n = grid[0].length\n    num_layers\
        \ = (m < n ? m : n) / 2\n    (0...num_layers).each do |i|\n        r1, c1 =\
        \ i, i\n        r2, c2 = m - 1 - i, n - 1 - i\n\n        elements = []\n   \
        \     (c1...c2).each { |c| elements << grid[r1][c] }\n        (r1...r2).each\
        \ { |r| elements << grid[r][c2] }\n        c2.downto(c1 + 1).each { |c| elements\
        \ << grid[r2][c] }\n        r2.downto(r1 + 1).each { |r| elements << grid[r][c1]\
        \ }\n\n        size = elements.length\n        shift = k % size\n        idx\
        \ = 0\n        (c1...c2).each do |c|\n            grid[r1][c] = elements[(idx\
        \ + shift) % size]\n            idx += 1\n        end\n        (r1...r2).each\
        \ do |r|\n            grid[r][c2] = elements[(idx + shift) % size]\n       \
        \     idx += 1\n        end\n        c2.downto(c1 + 1).each do |c|\n       \
        \     grid[r2][c] = elements[(idx + shift) % size]\n            idx += 1\n \
        \       end\n        r2.downto(r1 + 1).each do |r|\n            grid[r][c1]\
        \ = elements[(idx + shift) % size]\n            idx += 1\n        end\n    end\n\
        \    grid\nend"
      scala: "object Solution {\n    def rotateGrid(grid: Array[Array[Int]], k: Int):\
        \ Array[Array[Int]] = {\n        val m = grid.length\n        val n = grid(0).length\n\
        \        val numLayers = (if (m < n) m else n) / 2\n        for (i <- 0 until\
        \ numLayers) {\n            val r1 = i\n            val c1 = i\n           \
        \ val r2 = m - 1 - i\n            val c2 = n - 1 - i\n\n            val elements\
        \ = new scala.collection.mutable.ArrayBuffer[Int]()\n            for (c <- c1\
        \ until c2) elements += grid(r1)(c)\n            for (r <- r1 until r2) elements\
        \ += grid(r)(c2)\n            for (c <- c2 until c1 by -1) elements += grid(r2)(c)\n\
        \            for (r <- r2 until r1 by -1) elements += grid(r)(c1)\n\n      \
        \      val size = elements.length\n            val shift = k % size\n      \
        \      var idx = 0\n            for (c <- c1 until c2) {\n                grid(r1)(c)\
        \ = elements((idx + shift) % size)\n                idx += 1\n            }\n\
        \            for (r <- r1 until r2) {\n                grid(r)(c2) = elements((idx\
        \ + shift) % size)\n                idx += 1\n            }\n            for\
        \ (c <- c2 until c1 by -1) {\n                grid(r2)(c) = elements((idx +\
        \ shift) % size)\n                idx += 1\n            }\n            for (r\
        \ <- r2 until r1 by -1) {\n                grid(r)(c1) = elements((idx + shift)\
        \ % size)\n                idx += 1\n            }\n        }\n        grid\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn rotate_grid(mut grid: Vec<Vec<i32>>, k: i32)\
        \ -> Vec<Vec<i32>> {\n        let m = grid.len();\n        let n = grid[0].len();\n\
        \        let num_layers = (m.min(n)) / 2;\n\n        for l in 0..num_layers\
        \ {\n            let mut path = Vec::new();\n            for r in l..m - 1 -\
        \ l { path.push((r, l)); }\n            for c in l..n - 1 - l { path.push((m\
        \ - 1 - l, c)); }\n            for r in (l + 1..m - l).rev() { path.push((r,\
        \ n - 1 - l)); }\n            for c in (l + 1..n - l).rev() { path.push((l,\
        \ c)); }\n\n            let len = path.len();\n            if len == 0 { continue;\
        \ }\n            let shift = (k as usize) % len;\n            if shift == 0\
        \ { continue; }\n\n            let mut original_values = Vec::new();\n     \
        \       for &(r, c) in &path {\n                original_values.push(grid[r][c]);\n\
        \            }\n\n            for i in 0..len {\n                let (r, c)\
        \ = path[(i + shift) % len];\n                grid[r][c] = original_values[i];\n\
        \            }\n        }\n        grid\n    }\n}"
      racket: "(define/contract (rotate-grid grid k)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer? (listof (listof exact-integer?)))\n  (let* ([m (length grid)]\n\
        \         [n (length (first grid))]\n         [grid-vec (list->vector (map list->vector\
        \ grid))]\n         [num-layers (quotient (min m n) 2)])\n    (for ([l (in-range\
        \ num-layers)])\n      (let* ([path (append\n                    (for/list ([r\
        \ (in-range l (- m 1 l))]) (list r l))\n                    (for/list ([c (in-range\
        \ l (- n 1 l))]) (list (- m 1 l) c))\n                    (for/list ([r (in-range\
        \ (- m 1 l) l -1)]) (list r (- n 1 l)))\n                    (for/list ([c (in-range\
        \ (- n 1 l) l -1)]) (list l c)))]\n             [len (length path)]\n      \
        \       [shift (remainder k len)]\n             [values (for/list ([pos path])\n\
        \                       (vector-ref (vector-ref grid-vec (first pos)) (second\
        \ pos)))]\n             [rotated-values (if (= shift 0) \n                 \
        \                values\n                                 (append (drop values\
        \ (- len shift)) (take values (- len shift))))])\n        (for ([pos path] [val\
        \ rotated-values])\n          (vector-set! (vector-ref grid-vec (first pos))\
        \ (second pos) val))))\n    (map vector->list (vector->list grid-vec))))"
      erlang: "-module(solution).\n-export([rotate_grid/2]).\n\nrotate_grid(Grid, K)\
        \ ->\n    M = length(Grid),\n    N = length(hd(Grid)),\n    GridMap = grid_to_map(Grid),\n\
        \    NumLayers = erlang:min(M, N) div 2,\n    FinalMap = rotate_layers(0, NumLayers,\
        \ M, N, K, GridMap),\n    map_to_grid(M, N, FinalMap).\n\ngrid_to_map(Grid)\
        \ ->\n    lists:foldl(fun({Row, R}, Acc) ->\n        lists:foldl(fun({Val, C},\
        \ AccInner) ->\n            maps:put({R, C}, Val, AccInner)\n        end, Acc,\
        \ lists:zip(Row, lists:seq(0, length(Row) - 1)))\n    end, #{}, lists:zip(Grid,\
        \ lists:seq(0, length(Grid) - 1))).\n\nrotate_layers(L, NumLayers, _M, _N, _K,\
        \ Map) when L >= NumLayers -> Map;\nrotate_layers(L, NumLayers, M, N, K, Map)\
        \ ->\n    Path = get_path(L, M, N),\n    Len = length(Path),\n    Shift = K\
        \ rem Len,\n    Values = [maps:get(Pos, Map) || Pos <- Path],\n    RotatedValues\
        \ = rotate_list(Values, Shift, Len),\n    NewMap = lists:foldl(fun({Pos, Val},\
        \ Acc) ->\n        maps:put(Pos, Val, Acc)\n    end, Map, lists:zip(Path, RotatedValues)),\n\
        \    rotate_layers(L + 1, NumLayers, M, N, K, NewMap).\n\nget_path(L, M, N)\
        \ ->\n    Left = [{R, L} || R <- lists:seq(L, M - 2 - L)],\n    Bottom = [{M\
        \ - 1 - L, C} || C <- lists:seq(L, N - 2 - L)],\n    Right = [{R, N - 1 - L}\
        \ || R <- lists:seq(M - 1 - L, L + 1, -1)],\n    Top = [{L, C} || C <- lists:seq(N\
        \ - 1 - L, L + 1, -1)],\n    Left ++ Bottom ++ Right ++ Top.\n\nrotate_list(Values,\
        \ 0, _Len) -> Values;\nrotate_list(Values, Shift, Len) ->\n    {Tail, Head}\
        \ = lists:split(Len - Shift, Values),\n    Head ++ Tail.\n\nmap_to_grid(M, N,\
        \ Map) ->\n    [ [maps:get({R, C}, Map) || C <- lists:seq(0, N - 1)] || R <-\
        \ lists:seq(0, M - 1)]."
      elixir: "defmodule Solution do\n  @spec rotate_grid(grid :: [[integer]], k ::\
        \ integer) :: [[integer]]\n  def rotate_grid(grid, k) do\n    m = length(grid)\n\
        \    n = length(hd(grid))\n    map = for {row, r} <- Enum.with_index(grid),\n\
        \              {val, c} <- Enum.with_index(row),\n              into: %{}, do:\
        \ {{r, c}, val}\n\n    num_layers = div(min(m, n), 2)\n\n    final_map = Enum.reduce(0..(num_layers\
        \ - 1), map, fn l, acc ->\n      path = get_path(l, m, n)\n      len = length(path)\n\
        \      shift = rem(k, len)\n      values = Enum.map(path, &Map.get(acc, &1))\n\
        \      rotated_values = rotate_list(values, shift, len)\n\n      Enum.reduce(Enum.zip(path,\
        \ rotated_values), acc, fn {coord, val}, acc_inner ->\n        Map.put(acc_inner,\
        \ coord, val)\n      end)\n    end)\n\n    for r <- 0..(m - 1) do\n      for\
        \ c <- 0..(n - 1), do: Map.get(final_map, {r, c})\n    end\n  end\n\n  defp\
        \ get_path(l, m, n) do\n    left = for r <- l..(m - 2 - l), do: {r, l}\n   \
        \ bottom = for c <- l..(n - 2 - l), do: {m - 1 - l, c}\n    right = for r <-\
        \ (m - 1 - l)..(l + 1), do: {r, n - 1 - l}\n    top = for c <- (n - 1 - l)..(l\
        \ + 1), do: {l, c}\n    left ++ bottom ++ right ++ top\n  end\n\n  defp rotate_list(values,\
        \ 0, _len), do: values\n  defp rotate_list(values, shift, len) do\n    {tail,\
        \ head} = Enum.split(values, len - shift)\n    head ++ tail\n  end\nend"
    approach: The problem asks to rotate each layer of an $m \times n$ grid counter-clockwise
      $k$ times. Since both $m$ and $n$ are even, the grid is composed of $\min(m, n)
      / 2$ layers. We process each layer independently by extracting its elements into
      a linear array in counter-clockwise order. This order starts from the top-left
      of the layer, moves down the left edge, right along the bottom, up the right edge,
      and finally left along the top edge.
    time_complexity: 'O(m \times n) with a one-paragraph explanation: The algorithm
      visits each cell in the grid exactly twice—once to extract its value into a layer-specific
      linear array and once to write the new, rotated value back into the grid. Since
      the total number of elements across all layers is exactly $m \times n$, the overall
      time complexity is linear with respect to the total number of cells in the matrix.'
    space_complexity: 'O(m \times n) with a one-paragraph explanation: We utilize extra
      space to store the elements of the layers. In C++ and Python, we process one layer
      at a time, resulting in $O(\max(m, n))$ extra space, but in languages like Java
      and C where a return matrix must be explicitly allocated, or for overall clarity,
      the complexity is $O(m \times n)$. Given the small constraints (up to 50x50),
      this is well within memory limits.'
    elapsed_time: 410.573926448822
    model: gemini-3-flash-preview
    generated_at: '2026-05-09 02:16:47 '
---

## Problem #1914: Cyclically Rotating a Grid

**Difficulty:** Medium

**Topics:** Array, Matrix, Simulation

## Problem Description

<p>You are given an <code>m x n</code> integer matrix <code>grid</code>​​​, where <code>m</code> and <code>n</code> are both <strong>even</strong> integers, and an integer <code>k</code>.</p>

<p>The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid.png" style="width: 231px; height: 258px;" /></p>

<p>A cyclic rotation of the matrix is done by cyclically rotating <strong>each layer</strong> in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the <strong>counter-clockwise</strong> direction. An example rotation is shown below:</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/22/explanation_grid.jpg" style="width: 500px; height: 268px;" />
<p>Return <em>the matrix after applying </em><code>k</code> <em>cyclic rotations to it</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/19/rod2.png" style="width: 421px; height: 191px;" />
<pre>
<strong>Input:</strong> grid = [[40,10],[30,20]], k = 1
<strong>Output:</strong> [[10,20],[40,30]]
<strong>Explanation:</strong> The figures above represent the grid at every state.
</pre>

<p><strong class="example">Example 2:</strong></p>
<strong><img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid5.png" style="width: 231px; height: 262px;" /></strong> <strong><img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid6.png" style="width: 231px; height: 262px;" /></strong> <strong><img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid7.png" style="width: 231px; height: 262px;" /></strong>

<pre>
<strong>Input:</strong> grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
<strong>Output:</strong> [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
<strong>Explanation:</strong> The figures above represent the grid at every state.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>2 &lt;= m, n &lt;= 50</code></li>
	<li>Both <code>m</code> and <code>n</code> are <strong>even</strong> integers.</li>
	<li><code>1 &lt;= grid[i][j] &lt;=<sup> </sup>5000</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>

## Hints

1. First, you need to consider each layer separately as an array.

2. Just cycle this array and then re-assign it.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks to rotate each layer of an $m \times n$ grid counter-clockwise $k$ times. Since both $m$ and $n$ are even, the grid is composed of $\min(m, n) / 2$ layers. We process each layer independently by extracting its elements into a linear array in counter-clockwise order. This order starts from the top-left of the layer, moves down the left edge, right along the bottom, up the right edge, and finally left along the top edge.

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
    vector<vector<int>> rotateGrid(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        int layers = min(m, n) / 2;
        for (int i = 0; i < layers; ++i) {
            vector<int> layer;
            for (int r = i; r < m - 1 - i; ++r) layer.push_back(grid[r][i]);
            for (int c = i; c < n - 1 - i; ++c) layer.push_back(grid[m - 1 - i][c]);
            for (int r = m - 1 - i; r > i; --r) layer.push_back(grid[r][n - 1 - i]);
            for (int c = n - 1 - i; c > i; --c) layer.push_back(grid[i][c]);

            int len = layer.size();
            int rk = k % len;
            int idx = 0;
            for (int r = i; r < m - 1 - i; ++r) grid[r][i] = layer[(idx++ + rk) % len];
            for (int c = i; c < n - 1 - i; ++c) grid[m - 1 - i][c] = layer[(idx++ + rk) % len];
            for (int r = m - 1 - i; r > i; --r) grid[r][n - 1 - i] = layer[(idx++ + rk) % len];
            for (int c = n - 1 - i; c > i; --c) grid[i][c] = layer[(idx++ + rk) % len];
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
    public int[][] rotateGrid(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        int layers = Math.min(m, n) / 2;
        for (int i = 0; i < layers; ++i) {
            int len = 2 * (m - 2 * i) + 2 * (n - 2 * i) - 4;
            int[] layer = new int[len];
            int idx = 0;
            for (int r = i; r < m - 1 - i; ++r) layer[idx++] = grid[r][i];
            for (int c = i; c < n - 1 - i; ++c) layer[idx++] = grid[m - 1 - i][c];
            for (int r = m - 1 - i; r > i; --r) layer[idx++] = grid[r][n - 1 - i];
            for (int c = n - 1 - i; c > i; --c) layer[idx++] = grid[i][c];

            int rk = k % len;
            idx = 0;
            for (int r = i; r < m - 1 - i; ++r) grid[r][i] = layer[(idx++ + rk) % len];
            for (int c = i; c < n - 1 - i; ++c) grid[m - 1 - i][c] = layer[(idx++ + rk) % len];
            for (int r = m - 1 - i; r > i; --r) grid[r][n - 1 - i] = layer[(idx++ + rk) % len];
            for (int c = n - 1 - i; c > i; --c) grid[i][c] = layer[(idx++ + rk) % len];
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
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2
        for i in range(num_layers):
            layer = []
            for r in range(i, m - 1 - i): layer.append(grid[r][i])
            for c in range(i, n - 1 - i): layer.append(grid[m - 1 - i][c])
            for r in range(m - 1 - i, i, -1): layer.append(grid[r][n - 1 - i])
            for c in range(n - 1 - i, i, -1): layer.append(grid[i][c])

            length = len(layer)
            rk = k % length
            idx = 0
            for r in range(i, m - 1 - i):
                grid[r][i] = layer[(idx + rk) % length]
                idx += 1
            for c in range(i, n - 1 - i):
                grid[m - 1 - i][c] = layer[(idx + rk) % length]
                idx += 1
            for r in range(m - 1 - i, i, -1):
                grid[r][n - 1 - i] = layer[(idx + rk) % length]
                idx += 1
            for c in range(n - 1 - i, i, -1):
                grid[i][c] = layer[(idx + rk) % length]
                idx += 1
        return grid
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2
        for i in range(num_layers):
            layer = []
            for r in range(i, m - 1 - i): layer.append(grid[r][i])
            for c in range(i, n - 1 - i): layer.append(grid[m - 1 - i][c])
            for r in range(m - 1 - i, i, -1): layer.append(grid[r][n - 1 - i])
            for c in range(n - 1 - i, i, -1): layer.append(grid[i][c])

            length = len(layer)
            rk = k % length
            idx = 0
            for r in range(i, m - 1 - i):
                grid[r][i] = layer[(idx + rk) % length]
                idx += 1
            for c in range(i, n - 1 - i):
                grid[m - 1 - i][c] = layer[(idx + rk) % length]
                idx += 1
            for r in range(m - 1 - i, i, -1):
                grid[r][n - 1 - i] = layer[(idx + rk) % length]
                idx += 1
            for c in range(n - 1 - i, i, -1):
                grid[i][c] = layer[(idx + rk) % length]
                idx += 1
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
int** rotateGrid(int** grid, int gridSize, int* gridColSize, int k, int* returnSize, int** returnColumnSizes){
    int m = gridSize;
    int n = gridColSize[0];
    int** res = (int**)malloc(m * sizeof(int*));
    *returnColumnSizes = (int*)malloc(m * sizeof(int));
    *returnSize = m;
    for (int i = 0; i < m; i++) {
        res[i] = (int*)malloc(n * sizeof(int));
        (*returnColumnSizes)[i] = n;
        for (int j = 0; j < n; j++) res[i][j] = grid[i][j];
    }

    int num_layers = (m < n ? m : n) / 2;
    for (int i = 0; i < num_layers; i++) {
        int len = 2 * (m - 2 * i) + 2 * (n - 2 * i) - 4;
        int* layer = (int*)malloc(len * sizeof(int));
        int idx = 0;
        for (int r = i; r < m - 1 - i; r++) layer[idx++] = res[r][i];
        for (int c = i; c < n - 1 - i; c++) layer[idx++] = res[m - 1 - i][c];
        for (int r = m - 1 - i; r > i; r--) layer[idx++] = res[r][n - 1 - i];
        for (int c = n - 1 - i; c > i; c--) layer[idx++] = res[i][c];

        int rk = k % len;
        idx = 0;
        for (int r = i; r < m - 1 - i; r++) res[r][i] = layer[(idx++ + rk) % len];
        for (int c = i; c < n - 1 - i; c++) res[m - 1 - i][c] = layer[(idx++ + rk) % len];
        for (int r = m - 1 - i; r > i; r--) res[r][n - 1 - i] = layer[(idx++ + rk) % len];
        for (int c = n - 1 - i; c > i; c--) res[i][c] = layer[(idx++ + rk) % len];
        free(layer);
    }

    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;

public class Solution {
    public int[][] RotateGrid(int[][] grid, int k) {
        int m = grid.Length;
        int n = grid[0].Length;
        int numLayers = Math.Min(m, n) / 2;

        for (int l = 0; l < numLayers; l++) {
            List<int[]> path = new List<int[]>();

            for (int r = l; r < m - 1 - l; r++) path.Add(new int[] { r, l });
            for (int c = l; c < n - 1 - l; c++) path.Add(new int[] { m - 1 - l, c });
            for (int r = m - 1 - l; r > l; r--) path.Add(new int[] { r, n - 1 - l });
            for (int c = n - 1 - l; c > l; c--) path.Add(new int[] { l, c });

            int len = path.Count;
            int actualK = k % len;
            int[] vals = new int[len];
            for (int i = 0; i < len; i++) {
                vals[i] = grid[path[i][0]][path[i][1]];
            }

            for (int i = 0; i < len; i++) {
                int[] nextPos = path[(i + actualK) % len];
                grid[nextPos[0]][nextPos[1]] = vals[i];
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
 * @param {number} k
 * @return {number[][]}
 */
var rotateGrid = function(grid, k) {
    const m = grid.length;
    const n = grid[0].length;
    const numLayers = Math.min(m, n) / 2;

    for (let l = 0; l < numLayers; l++) {
        const path = [];

        for (let r = l; r < m - 1 - l; r++) path.push([r, l]);
        for (let c = l; c < n - 1 - l; c++) path.push([m - 1 - l, c]);
        for (let r = m - 1 - l; r > l; r--) path.push([r, n - 1 - l]);
        for (let c = n - 1 - l; c > l; c--) path.push([l, c]);

        const len = path.length;
        const actualK = k % len;
        const vals = path.map(p => grid[p[0]][p[1]]);

        for (let i = 0; i < len; i++) {
            const [nr, nc] = path[(i + actualK) % len];
            grid[nr][nc] = vals[i];
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
function rotateGrid(grid: number[][], k: number): number[][] {
    const m = grid.length;
    const n = grid[0].length;
    const numLayers = Math.floor(Math.min(m, n) / 2);

    for (let l = 0; l < numLayers; l++) {
        const path: [number, number][] = [];

        for (let r = l; r < m - 1 - l; r++) path.push([r, l]);
        for (let c = l; c < n - 1 - l; c++) path.push([m - 1 - l, c]);
        for (let r = m - 1 - l; r > l; r--) path.push([r, n - 1 - l]);
        for (let c = n - 1 - l; c > l; c--) path.push([l, c]);

        const len = path.length;
        const actualK = k % len;
        const vals = path.map(p => grid[p[0]][p[1]]);

        for (let i = 0; i < len; i++) {
            const [nr, nc] = path[(i + actualK) % len];
            grid[nr][nc] = vals[i];
        }
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
     * @param Integer $k
     * @return Integer[][]
     */
    function rotateGrid($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $numLayers = min($m, $n) / 2;

        for ($l = 0; $l < $numLayers; $l++) {
            $path = [];

            for ($r = $l; $r < $m - 1 - $l; $r++) $path[] = [$r, $l];
            for ($c = $l; $c < $n - 1 - $l; $c++) $path[] = [$m - 1 - $l, $c];
            for ($r = $m - 1 - $l; $r > $l; $r--) $path[] = [$r, $n - 1 - $l];
            for ($c = $n - 1 - $l; $c > $l; $c--) $path[] = [$l, $c];

            $len = count($path);
            $actualK = $k % $len;
            $vals = [];
            foreach ($path as $p) {
                $vals[] = $grid[$p[0]][$p[1]];
            }

            for ($i = 0; $i < $len; $i++) {
                $nextPos = $path[($i + $actualK) % $len];
                $grid[$nextPos[0]][$nextPos[1]] = $vals[$i];
            }
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
    func rotateGrid(_ grid: [[Int]], _ k: Int) -> [[Int]] {
        var grid = grid
        let m = grid.count
        let n = grid[0].count
        let numLayers = min(m, n) / 2

        for l in 0..<numLayers {
            var path = [(Int, Int)]()

            for r in l..<(m - 1 - l) {
                path.append((r, l))
            }
            for c in l..<(n - 1 - l) {
                path.append((m - 1 - l, c))
            }
            for r in stride(from: m - 1 - l, to: l, by: -1) {
                path.append((r, n - 1 - l))
            }
            for c in stride(from: n - 1 - l, to: l, by: -1) {
                path.append((l, c))
            }

            let count = path.count
            let actualK = k % count
            var vals = [Int]()
            for p in path {
                vals.append(grid[p.0][p.1])
            }

            for i in 0..<count {
                let nextPos = path[(i + actualK) % count]
                grid[nextPos.0][nextPos.1] = vals[i]
            }
        }

        return grid
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun rotateGrid(grid: Array<IntArray>, k: Int): Array<IntArray> {
        val m = grid.size
        val n = grid[0].size
        val numLayers = (if (m < n) m else n) / 2
        for (i in 0 until numLayers) {
            val r1 = i
            val c1 = i
            val r2 = m - 1 - i
            val c2 = n - 1 - i

            val elements = mutableListOf<Int>()
            for (c in c1 until c2) elements.add(grid[r1][c])
            for (r in r1 until r2) elements.add(grid[r][c2])
            for (c in c2 downTo c1 + 1) elements.add(grid[r2][c])
            for (r in r2 downTo r1 + 1) elements.add(grid[r][c1])

            val size = elements.size
            val shift = k % size
            var idx = 0
            for (c in c1 until c2) {
                grid[r1][c] = elements[(idx + shift) % size]
                idx++
            }
            for (r in r1 until r2) {
                grid[r][c2] = elements[(idx + shift) % size]
                idx++
            }
            for (c in c2 downTo c1 + 1) {
                grid[r2][c] = elements[(idx + shift) % size]
                idx++
            }
            for (r in r2 downTo r1 + 1) {
                grid[r][c1] = elements[(idx + shift) % size]
                idx++
            }
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
  List<List<int>> rotateGrid(List<List<int>> grid, int k) {
    int m = grid.length;
    int n = grid[0].length;
    int numLayers = (m < n ? m : n) ~/ 2;
    for (int i = 0; i < numLayers; i++) {
      int r1 = i, c1 = i;
      int r2 = m - 1 - i, c2 = n - 1 - i;
      List<int> elements = [];
      for (int c = c1; c < c2; c++) elements.add(grid[r1][c]);
      for (int r = r1; r < r2; r++) elements.add(grid[r][c2]);
      for (int c = c2; c > c1; c--) elements.add(grid[r2][c]);
      for (int r = r2; r > r1; r--) elements.add(grid[r][c1]);

      int size = elements.length;
      int shift = k % size;
      int idx = 0;
      for (int c = c1; c < c2; c++) {
        grid[r1][c] = elements[(idx + shift) % size];
        idx++;
      }
      for (int r = r1; r < r2; r++) {
        grid[r][c2] = elements[(idx + shift) % size];
        idx++;
      }
      for (int c = c2; c > c1; c--) {
        grid[r2][c] = elements[(idx + shift) % size];
        idx++;
      }
      for (int r = r2; r > r1; r--) {
        grid[r][c1] = elements[(idx + shift) % size];
        idx++;
      }
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
func rotateGrid(grid [][]int, k int) [][]int {
    m := len(grid)
    n := len(grid[0])
    numLayers := m
    if n < m {
        numLayers = n
    }
    numLayers /= 2
    for i := 0; i < numLayers; i++ {
        r1, c1 := i, i
        r2, c2 := m-1-i, n-1-i

        elements := make([]int, 0, 2*(r2-r1+c2-c1))
        for c := c1; c < c2; c++ { elements = append(elements, grid[r1][c]) }
        for r := r1; r < r2; r++ { elements = append(elements, grid[r][c2]) }
        for c := c2; c > c1; c-- { elements = append(elements, grid[r2][c]) }
        for r := r2; r > r1; r-- { elements = append(elements, grid[r][c1]) }

        size := len(elements)
        shift := k % size
        idx := 0
        for c := c1; c < c2; c++ {
            grid[r1][c] = elements[(idx+shift)%size]
            idx++
        }
        for r := r1; r < r2; r++ {
            grid[r][c2] = elements[(idx+shift)%size]
            idx++
        }
        for c := c2; c > c1; c-- {
            grid[r2][c] = elements[(idx+shift)%size]
            idx++
        }
        for r := r2; r > r1; r-- {
            grid[r][c1] = elements[(idx+shift)%size]
            idx++
        }
    }
    return grid
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer[][]}
def rotate_grid(grid, k)
    m = grid.length
    n = grid[0].length
    num_layers = (m < n ? m : n) / 2
    (0...num_layers).each do |i|
        r1, c1 = i, i
        r2, c2 = m - 1 - i, n - 1 - i

        elements = []
        (c1...c2).each { |c| elements << grid[r1][c] }
        (r1...r2).each { |r| elements << grid[r][c2] }
        c2.downto(c1 + 1).each { |c| elements << grid[r2][c] }
        r2.downto(r1 + 1).each { |r| elements << grid[r][c1] }

        size = elements.length
        shift = k % size
        idx = 0
        (c1...c2).each do |c|
            grid[r1][c] = elements[(idx + shift) % size]
            idx += 1
        end
        (r1...r2).each do |r|
            grid[r][c2] = elements[(idx + shift) % size]
            idx += 1
        end
        c2.downto(c1 + 1).each do |c|
            grid[r2][c] = elements[(idx + shift) % size]
            idx += 1
        end
        r2.downto(r1 + 1).each do |r|
            grid[r][c1] = elements[(idx + shift) % size]
            idx += 1
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
    def rotateGrid(grid: Array[Array[Int]], k: Int): Array[Array[Int]] = {
        val m = grid.length
        val n = grid(0).length
        val numLayers = (if (m < n) m else n) / 2
        for (i <- 0 until numLayers) {
            val r1 = i
            val c1 = i
            val r2 = m - 1 - i
            val c2 = n - 1 - i

            val elements = new scala.collection.mutable.ArrayBuffer[Int]()
            for (c <- c1 until c2) elements += grid(r1)(c)
            for (r <- r1 until r2) elements += grid(r)(c2)
            for (c <- c2 until c1 by -1) elements += grid(r2)(c)
            for (r <- r2 until r1 by -1) elements += grid(r)(c1)

            val size = elements.length
            val shift = k % size
            var idx = 0
            for (c <- c1 until c2) {
                grid(r1)(c) = elements((idx + shift) % size)
                idx += 1
            }
            for (r <- r1 until r2) {
                grid(r)(c2) = elements((idx + shift) % size)
                idx += 1
            }
            for (c <- c2 until c1 by -1) {
                grid(r2)(c) = elements((idx + shift) % size)
                idx += 1
            }
            for (r <- r2 until r1 by -1) {
                grid(r)(c1) = elements((idx + shift) % size)
                idx += 1
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
    pub fn rotate_grid(mut grid: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let num_layers = (m.min(n)) / 2;

        for l in 0..num_layers {
            let mut path = Vec::new();
            for r in l..m - 1 - l { path.push((r, l)); }
            for c in l..n - 1 - l { path.push((m - 1 - l, c)); }
            for r in (l + 1..m - l).rev() { path.push((r, n - 1 - l)); }
            for c in (l + 1..n - l).rev() { path.push((l, c)); }

            let len = path.len();
            if len == 0 { continue; }
            let shift = (k as usize) % len;
            if shift == 0 { continue; }

            let mut original_values = Vec::new();
            for &(r, c) in &path {
                original_values.push(grid[r][c]);
            }

            for i in 0..len {
                let (r, c) = path[(i + shift) % len];
                grid[r][c] = original_values[i];
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
(define/contract (rotate-grid grid k)
  (-> (listof (listof exact-integer?)) exact-integer? (listof (listof exact-integer?)))
  (let* ([m (length grid)]
         [n (length (first grid))]
         [grid-vec (list->vector (map list->vector grid))]
         [num-layers (quotient (min m n) 2)])
    (for ([l (in-range num-layers)])
      (let* ([path (append
                    (for/list ([r (in-range l (- m 1 l))]) (list r l))
                    (for/list ([c (in-range l (- n 1 l))]) (list (- m 1 l) c))
                    (for/list ([r (in-range (- m 1 l) l -1)]) (list r (- n 1 l)))
                    (for/list ([c (in-range (- n 1 l) l -1)]) (list l c)))]
             [len (length path)]
             [shift (remainder k len)]
             [values (for/list ([pos path])
                       (vector-ref (vector-ref grid-vec (first pos)) (second pos)))]
             [rotated-values (if (= shift 0) 
                                 values
                                 (append (drop values (- len shift)) (take values (- len shift))))])
        (for ([pos path] [val rotated-values])
          (vector-set! (vector-ref grid-vec (first pos)) (second pos) val))))
    (map vector->list (vector->list grid-vec))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([rotate_grid/2]).

rotate_grid(Grid, K) ->
    M = length(Grid),
    N = length(hd(Grid)),
    GridMap = grid_to_map(Grid),
    NumLayers = erlang:min(M, N) div 2,
    FinalMap = rotate_layers(0, NumLayers, M, N, K, GridMap),
    map_to_grid(M, N, FinalMap).

grid_to_map(Grid) ->
    lists:foldl(fun({Row, R}, Acc) ->
        lists:foldl(fun({Val, C}, AccInner) ->
            maps:put({R, C}, Val, AccInner)
        end, Acc, lists:zip(Row, lists:seq(0, length(Row) - 1)))
    end, #{}, lists:zip(Grid, lists:seq(0, length(Grid) - 1))).

rotate_layers(L, NumLayers, _M, _N, _K, Map) when L >= NumLayers -> Map;
rotate_layers(L, NumLayers, M, N, K, Map) ->
    Path = get_path(L, M, N),
    Len = length(Path),
    Shift = K rem Len,
    Values = [maps:get(Pos, Map) || Pos <- Path],
    RotatedValues = rotate_list(Values, Shift, Len),
    NewMap = lists:foldl(fun({Pos, Val}, Acc) ->
        maps:put(Pos, Val, Acc)
    end, Map, lists:zip(Path, RotatedValues)),
    rotate_layers(L + 1, NumLayers, M, N, K, NewMap).

get_path(L, M, N) ->
    Left = [{R, L} || R <- lists:seq(L, M - 2 - L)],
    Bottom = [{M - 1 - L, C} || C <- lists:seq(L, N - 2 - L)],
    Right = [{R, N - 1 - L} || R <- lists:seq(M - 1 - L, L + 1, -1)],
    Top = [{L, C} || C <- lists:seq(N - 1 - L, L + 1, -1)],
    Left ++ Bottom ++ Right ++ Top.

rotate_list(Values, 0, _Len) -> Values;
rotate_list(Values, Shift, Len) ->
    {Tail, Head} = lists:split(Len - Shift, Values),
    Head ++ Tail.

map_to_grid(M, N, Map) ->
    [ [maps:get({R, C}, Map) || C <- lists:seq(0, N - 1)] || R <- lists:seq(0, M - 1)].
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec rotate_grid(grid :: [[integer]], k :: integer) :: [[integer]]
  def rotate_grid(grid, k) do
    m = length(grid)
    n = length(hd(grid))
    map = for {row, r} <- Enum.with_index(grid),
              {val, c} <- Enum.with_index(row),
              into: %{}, do: {{r, c}, val}

    num_layers = div(min(m, n), 2)

    final_map = Enum.reduce(0..(num_layers - 1), map, fn l, acc ->
      path = get_path(l, m, n)
      len = length(path)
      shift = rem(k, len)
      values = Enum.map(path, &Map.get(acc, &1))
      rotated_values = rotate_list(values, shift, len)

      Enum.reduce(Enum.zip(path, rotated_values), acc, fn {coord, val}, acc_inner ->
        Map.put(acc_inner, coord, val)
      end)
    end)

    for r <- 0..(m - 1) do
      for c <- 0..(n - 1), do: Map.get(final_map, {r, c})
    end
  end

  defp get_path(l, m, n) do
    left = for r <- l..(m - 2 - l), do: {r, l}
    bottom = for c <- l..(n - 2 - l), do: {m - 1 - l, c}
    right = for r <- (m - 1 - l)..(l + 1), do: {r, n - 1 - l}
    top = for c <- (n - 1 - l)..(l + 1), do: {l, c}
    left ++ bottom ++ right ++ top
  end

  defp rotate_list(values, 0, _len), do: values
  defp rotate_list(values, shift, len) do
    {tail, head} = Enum.split(values, len - shift)
    head ++ tail
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m \times n) with a one-paragraph explanation: The algorithm visits each cell in the grid exactly twice—once to extract its value into a layer-specific linear array and once to write the new, rotated value back into the grid. Since the total number of elements across all layers is exactly $m \times n$, the overall time complexity is linear with respect to the total number of cells in the matrix.
- **Space Complexity:** O(m \times n) with a one-paragraph explanation: We utilize extra space to store the elements of the layers. In C++ and Python, we process one layer at a time, resulting in $O(\max(m, n))$ extra space, but in languages like Java and C where a return matrix must be explicitly allocated, or for overall clarity, the complexity is $O(m \times n)$. Given the small constraints (up to 50x50), this is well within memory limits.
