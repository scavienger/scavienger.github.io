---
layout: post
title: "Maximum Non Negative Product in a Matrix"
date: 2026-03-23 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Dynamic Programming", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxProductPath(vector<vector<int>>& grid)\
        \ {\n        int m = grid.size(), n = grid[0].size();\n        long long maxDP[15][15],\
        \ minDP[15][15];\n        long long MOD = 1e9 + 7;\n\n        maxDP[0][0] =\
        \ minDP[0][0] = grid[0][0];\n        for (int i = 1; i < m; ++i) maxDP[i][0]\
        \ = minDP[i][0] = maxDP[i - 1][0] * grid[i][0];\n        for (int j = 1; j <\
        \ n; ++j) maxDP[0][j] = minDP[0][j] = maxDP[0][j - 1] * grid[0][j];\n\n    \
        \    for (int i = 1; i < m; ++i) {\n            for (int j = 1; j < n; ++j)\
        \ {\n                long long v = grid[i][j];\n                long long a\
        \ = maxDP[i - 1][j] * v, b = maxDP[i][j - 1] * v;\n                long long\
        \ c = minDP[i - 1][j] * v, d = minDP[i][j - 1] * v;\n                maxDP[i][j]\
        \ = max({a, b, c, d});\n                minDP[i][j] = min({a, b, c, d});\n \
        \           }\n        }\n\n        long long res = maxDP[m - 1][n - 1];\n \
        \       return res < 0 ? -1 : res % MOD;\n    }\n};"
      java: "class Solution {\n    public int maxProductPath(int[][] grid) {\n     \
        \   int m = grid.length, n = grid[0].length;\n        long[][] maxDP = new long[m][n];\n\
        \        long[][] minDP = new long[m][n];\n        long MOD = 1000000007;\n\n\
        \        maxDP[0][0] = minDP[0][0] = grid[0][0];\n        for (int i = 1; i\
        \ < m; i++) maxDP[i][0] = minDP[i][0] = maxDP[i - 1][0] * grid[i][0];\n    \
        \    for (int j = 1; j < n; j++) maxDP[0][j] = minDP[0][j] = maxDP[0][j - 1]\
        \ * grid[0][j];\n\n        for (int i = 1; i < m; i++) {\n            for (int\
        \ j = 1; j < n; j++) {\n                long v = grid[i][j];\n             \
        \   long a = maxDP[i - 1][j] * v, b = maxDP[i][j - 1] * v;\n               \
        \ long c = minDP[i - 1][j] * v, d = minDP[i][j - 1] * v;\n                maxDP[i][j]\
        \ = Math.max(a, Math.max(b, Math.max(c, d)));\n                minDP[i][j] =\
        \ Math.min(a, Math.min(b, Math.min(c, d)));\n            }\n        }\n\n  \
        \      long res = maxDP[m - 1][n - 1];\n        return res < 0 ? -1 : (int)\
        \ (res % MOD);\n    }\n}"
      python: "class Solution(object):\n    def maxProductPath(self, grid):\n      \
        \  \"\"\"\n        :type grid: List[List[int]]\n        :rtype: int\n      \
        \  \"\"\"\n        m, n = len(grid), len(grid[0])\n        max_dp = [[0] * n\
        \ for _ in range(m)]\n        min_dp = [[0] * n for _ in range(m)]\n\n     \
        \   max_dp[0][0] = min_dp[0][0] = grid[0][0]\n        for i in range(1, m):\n\
        \            max_dp[i][0] = min_dp[i][0] = max_dp[i-1][0] * grid[i][0]\n   \
        \     for j in range(1, n):\n            max_dp[0][j] = min_dp[0][j] = max_dp[0][j-1]\
        \ * grid[0][j]\n\n        for i in range(1, m):\n            for j in range(1,\
        \ n):\n                v = grid[i][j]\n                a, b, c, d = max_dp[i-1][j]*v,\
        \ max_dp[i][j-1]*v, min_dp[i-1][j]*v, min_dp[i][j-1]*v\n                max_dp[i][j]\
        \ = max(a, b, c, d)\n                min_dp[i][j] = min(a, b, c, d)\n\n    \
        \    res = max_dp[m-1][n-1]\n        return res % 1000000007 if res >= 0 else\
        \ -1"
      python3: "class Solution:\n    def maxProductPath(self, grid: List[List[int]])\
        \ -> int:\n        m, n = len(grid), len(grid[0])\n        max_dp = [[0] * n\
        \ for _ in range(m)]\n        min_dp = [[0] * n for _ in range(m)]\n\n     \
        \   max_dp[0][0] = min_dp[0][0] = grid[0][0]\n        for i in range(1, m):\n\
        \            max_dp[i][0] = min_dp[i][0] = max_dp[i-1][0] * grid[i][0]\n   \
        \     for j in range(1, n):\n            max_dp[0][j] = min_dp[0][j] = max_dp[0][j-1]\
        \ * grid[0][j]\n\n        for i in range(1, m):\n            for j in range(1,\
        \ n):\n                v = grid[i][j]\n                vals = (max_dp[i-1][j]*v,\
        \ max_dp[i][j-1]*v, min_dp[i-1][j]*v, min_dp[i][j-1]*v)\n                max_dp[i][j]\
        \ = max(vals)\n                min_dp[i][j] = min(vals)\n\n        res = max_dp[m-1][n-1]\n\
        \        return res % 1000000007 if res >= 0 else -1"
      c: "int maxProductPath(int** grid, int gridSize, int* gridColSize) {\n    int\
        \ m = gridSize, n = gridColSize[0];\n    long long maxDP[15][15], minDP[15][15];\n\
        \n    maxDP[0][0] = minDP[0][0] = grid[0][0];\n    for (int i = 1; i < m; i++)\
        \ maxDP[i][0] = minDP[i][0] = maxDP[i - 1][0] * grid[i][0];\n    for (int j\
        \ = 1; j < n; j++) maxDP[0][j] = minDP[0][j] = maxDP[0][j - 1] * grid[0][j];\n\
        \n    for (int i = 1; i < m; i++) {\n        for (int j = 1; j < n; j++) {\n\
        \            long long v = grid[i][j];\n            long long a = maxDP[i -\
        \ 1][j] * v, b = maxDP[i][j - 1] * v, c = minDP[i - 1][j] * v, d = minDP[i][j\
        \ - 1] * v;\n            long long curMax = a, curMin = a;\n            if (b\
        \ > curMax) curMax = b; if (c > curMax) curMax = c; if (d > curMax) curMax =\
        \ d;\n            if (b < curMin) curMin = b; if (c < curMin) curMin = c; if\
        \ (d < curMin) curMin = d;\n            maxDP[i][j] = curMax; minDP[i][j] =\
        \ curMin;\n        }\n    }\n    long long res = maxDP[m - 1][n - 1];\n    return\
        \ res < 0 ? -1 : (int)(res % 1000000007);\n}"
      csharp: "public class Solution {\n    public int MaxProductPath(int[][] grid)\
        \ {\n        int m = grid.Length, n = grid[0].Length;\n        long[,] maxDP\
        \ = new long[m, n];\n        long[,] minDP = new long[m, n];\n        long MOD\
        \ = 1000000007;\n\n        maxDP[0, 0] = minDP[0, 0] = grid[0][0];\n       \
        \ for (int i = 1; i < m; i++) maxDP[i, 0] = minDP[i, 0] = maxDP[i - 1, 0] *\
        \ grid[i][0];\n        for (int j = 1; j < n; j++) maxDP[0, j] = minDP[0, j]\
        \ = maxDP[0, j - 1] * grid[0][j];\n\n        for (int i = 1; i < m; i++) {\n\
        \            for (int j = 1; j < n; j++) {\n                long v = grid[i][j];\n\
        \                long a = maxDP[i - 1, j] * v, b = maxDP[i, j - 1] * v;\n  \
        \              long c = minDP[i - 1, j] * v, d = minDP[i, j - 1] * v;\n    \
        \            maxDP[i, j] = Math.Max(a, Math.Max(b, Math.Max(c, d)));\n     \
        \           minDP[i, j] = Math.Min(a, Math.Min(b, Math.Min(c, d)));\n      \
        \      }\n        }\n\n        long res = maxDP[m - 1, n - 1];\n        return\
        \ res < 0 ? -1 : (int)(res % MOD);\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @return {number}\n */\nvar maxProductPath\
        \ = function(grid) {\n    let m = grid.length, n = grid[0].length;\n    let\
        \ maxDP = Array.from({ length: m }, () => new BigInt64Array(n));\n    let minDP\
        \ = Array.from({ length: m }, () => new BigInt64Array(n));\n\n    maxDP[0][0]\
        \ = minDP[0][0] = BigInt(grid[0][0]);\n    for (let i = 1; i < m; i++) maxDP[i][0]\
        \ = minDP[i][0] = maxDP[i - 1][0] * BigInt(grid[i][0]);\n    for (let j = 1;\
        \ j < n; j++) maxDP[0][j] = minDP[0][j] = maxDP[0][j - 1] * BigInt(grid[0][j]);\n\
        \n    for (let i = 1; i < m; i++) {\n        for (let j = 1; j < n; j++) {\n\
        \            let v = BigInt(grid[i][j]);\n            let a = maxDP[i - 1][j]\
        \ * v, b = maxDP[i][j - 1] * v;\n            let c = minDP[i - 1][j] * v, d\
        \ = minDP[i][j - 1] * v;\n            let maxVal = a; if (b > maxVal) maxVal\
        \ = b; if (c > maxVal) maxVal = c; if (d > maxVal) maxVal = d;\n           \
        \ let minVal = a; if (b < minVal) minVal = b; if (c < minVal) minVal = c; if\
        \ (d < minVal) minVal = d;\n            maxDP[i][j] = maxVal; minDP[i][j] =\
        \ minVal;\n        }\n    }\n\n    let res = maxDP[m - 1][n - 1];\n    return\
        \ res < 0n ? -1 : Number(res % 1000000007n);\n};"
      typescript: "function maxProductPath(grid: number[][]): number {\n    const m\
        \ = grid.length;\n    const n = grid[0].length;\n    const dpMax: bigint[][]\
        \ = Array.from({ length: m }, () => Array(n).fill(0n));\n    const dpMin: bigint[][]\
        \ = Array.from({ length: m }, () => Array(n).fill(0n));\n\n    dpMax[0][0] =\
        \ BigInt(grid[0][0]);\n    dpMin[0][0] = BigInt(grid[0][0]);\n\n    for (let\
        \ i = 1; i < m; i++) {\n        dpMax[i][0] = dpMin[i][0] = dpMax[i - 1][0]\
        \ * BigInt(grid[i][0]);\n    }\n    for (let j = 1; j < n; j++) {\n        dpMax[0][j]\
        \ = dpMin[0][j] = dpMax[0][j - 1] * BigInt(grid[0][j]);\n    }\n\n    for (let\
        \ i = 1; i < m; i++) {\n        for (let j = 1; j < n; j++) {\n            const\
        \ val = BigInt(grid[i][j]);\n            const c1 = dpMax[i - 1][j] * val;\n\
        \            const c2 = dpMin[i - 1][j] * val;\n            const c3 = dpMax[i][j\
        \ - 1] * val;\n            const c4 = dpMin[i][j - 1] * val;\n\n           \
        \ let mx = c1;\n            if (c2 > mx) mx = c2;\n            if (c3 > mx)\
        \ mx = c3;\n            if (c4 > mx) mx = c4;\n\n            let mn = c1;\n\
        \            if (c2 < mn) mn = c2;\n            if (c3 < mn) mn = c3;\n    \
        \        if (c4 < mn) mn = c4;\n\n            dpMax[i][j] = mx;\n          \
        \  dpMin[i][j] = mn;\n        }\n    }\n\n    const res = dpMax[m - 1][n - 1];\n\
        \    if (res < 0n) return -1;\n    return Number(res % 1000000007n);\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @return\
        \ Integer\n     */\n    function maxProductPath($grid) {\n        $m = count($grid);\n\
        \        $n = count($grid[0]);\n        $dpMax = array_fill(0, $m, array_fill(0,\
        \ $n, 0));\n        $dpMin = array_fill(0, $m, array_fill(0, $n, 0));\n\n  \
        \      $dpMax[0][0] = $dpMin[0][0] = $grid[0][0];\n\n        for ($i = 1; $i\
        \ < $m; $i++) {\n            $dpMax[$i][0] = $dpMin[$i][0] = $dpMax[$i - 1][0]\
        \ * $grid[$i][0];\n        }\n        for ($j = 1; $j < $n; $j++) {\n      \
        \      $dpMax[0][$j] = $dpMin[0][$j] = $dpMax[0][$j - 1] * $grid[0][$j];\n \
        \       }\n\n        for ($i = 1; $i < $m; $i++) {\n            for ($j = 1;\
        \ $j < $n; $j++) {\n                $val = $grid[$i][j];\n                $c1\
        \ = $dpMax[$i - 1][$j] * $val;\n                $c2 = $dpMin[$i - 1][$j] * $val;\n\
        \                $c3 = $dpMax[$i][$j - 1] * $val;\n                $c4 = $dpMin[$i][$j\
        \ - 1] * $val;\n                $dpMax[$i][$j] = max($c1, $c2, $c3, $c4);\n\
        \                $dpMin[$i][$j] = min($c1, $c2, $c3, $c4);\n            }\n\
        \        }\n\n        $res = $dpMax[$m - 1][$n - 1];\n        if ($res < 0)\
        \ return -1;\n        return $res % 1000000007;\n    }\n}"
      swift: "class Solution {\n    func maxProductPath(_ grid: [[Int]]) -> Int {\n\
        \        let m = grid.count\n        let n = grid[0].count\n        var dpMax\
        \ = Array(repeating: Array(repeating: 0, count: n), count: m)\n        var dpMin\
        \ = Array(repeating: Array(repeating: 0, count: n), count: m)\n\n        dpMax[0][0]\
        \ = grid[0][0]\n        dpMin[0][0] = grid[0][0]\n\n        for i in 1..<m {\n\
        \            dpMax[i][0] = dpMax[i-1][0] * grid[i][0]\n            dpMin[i][0]\
        \ = dpMax[i][0]\n        }\n        for j in 1..<n {\n            dpMax[0][j]\
        \ = dpMax[0][j-1] * grid[0][j]\n            dpMin[0][j] = dpMax[0][j]\n    \
        \    }\n\n        if m > 1 && n > 1 {\n            for i in 1..<m {\n      \
        \          for j in 1..<n {\n                    let val = grid[i][j]\n    \
        \                let c1 = dpMax[i-1][j] * val\n                    let c2 =\
        \ dpMin[i-1][j] * val\n                    let c3 = dpMax[i][j-1] * val\n  \
        \                  let c4 = dpMin[i][j-1] * val\n                    dpMax[i][j]\
        \ = max(max(c1, c2), max(c3, c4))\n                    dpMin[i][j] = min(min(c1,\
        \ c2), min(c3, c4))\n                }\n            }\n        }\n\n       \
        \ let res = dpMax[m-1][n-1]\n        if res < 0 {\n            return -1\n \
        \       }\n        return res % 1_000_000_007\n    }\n}"
      kotlin: "class Solution {\n    fun maxProductPath(grid: Array<IntArray>): Int\
        \ {\n        val m = grid.size\n        val n = grid[0].size\n        val dpMax\
        \ = Array(m) { LongArray(n) }\n        val dpMin = Array(m) { LongArray(n) }\n\
        \n        dpMax[0][0] = grid[0][0].toLong()\n        dpMin[0][0] = grid[0][0].toLong()\n\
        \n        for (i in 1 until m) {\n            dpMax[i][0] = dpMax[i - 1][0]\
        \ * grid[i][0]\n            dpMin[i][0] = dpMax[i][0]\n        }\n        for\
        \ (j in 1 until n) {\n            dpMax[0][j] = dpMax[0][j - 1] * grid[0][j]\n\
        \            dpMin[0][j] = dpMax[0][j]\n        }\n\n        for (i in 1 until\
        \ m) {\n            for (j in 1 until n) {\n                val valGrid = grid[i][j].toLong()\n\
        \                val c1 = dpMax[i - 1][j] * valGrid\n                val c2\
        \ = dpMin[i - 1][j] * valGrid\n                val c3 = dpMax[i][j - 1] * valGrid\n\
        \                val c4 = dpMin[i][j - 1] * valGrid\n                dpMax[i][j]\
        \ = maxOf(maxOf(c1, c2), maxOf(c3, c4))\n                dpMin[i][j] = minOf(minOf(c1,\
        \ c2), minOf(c3, c4))\n            }\n        }\n\n        val res = dpMax[m\
        \ - 1][n - 1]\n        return if (res < 0) -1 else (res % 1000000007).toInt()\n\
        \    }\n}"
      dart: "class Solution {\n  int maxProductPath(List<List<int>> grid) {\n    int\
        \ m = grid.length;\n    int n = grid[0].length;\n    List<List<int>> dpMax =\
        \ List.generate(m, (_) => List.filled(n, 0));\n    List<List<int>> dpMin = List.generate(m,\
        \ (_) => List.filled(n, 0));\n\n    dpMax[0][0] = dpMin[0][0] = grid[0][0];\n\
        \n    for (int i = 1; i < m; i++) {\n      dpMax[i][0] = dpMin[i][0] = dpMax[i\
        \ - 1][0] * grid[i][0];\n    }\n    for (int j = 1; j < n; j++) {\n      dpMax[0][j]\
        \ = dpMin[0][j] = dpMax[0][j - 1] * grid[0][j];\n    }\n\n    for (int i = 1;\
        \ i < m; i++) {\n      for (int j = 1; j < n; j++) {\n        int val = grid[i][j];\n\
        \        int c1 = dpMax[i - 1][j] * val;\n        int c2 = dpMin[i - 1][j] *\
        \ val;\n        int c3 = dpMax[i][j - 1] * val;\n        int c4 = dpMin[i][j\
        \ - 1] * val;\n\n        int mx = c1;\n        if (c2 > mx) mx = c2;\n     \
        \   if (c3 > mx) mx = c3;\n        if (c4 > mx) mx = c4;\n\n        int mn =\
        \ c1;\n        if (c2 < mn) mn = c2;\n        if (c3 < mn) mn = c3;\n      \
        \  if (c4 < mn) mn = c4;\n\n        dpMax[i][j] = mx;\n        dpMin[i][j] =\
        \ mn;\n      }\n    }\n\n    int res = dpMax[m - 1][n - 1];\n    if (res < 0)\
        \ return -1;\n    return res % 1000000007;\n  }\n}"
      go: "func maxProductPath(grid [][]int) int {\n\tm, n := len(grid), len(grid[0])\n\
        \tdpMax := make([][]int64, m)\n\tdpMin := make([][]int64, m)\n\tfor i := range\
        \ dpMax {\n\t\tdpMax[i] = make([]int64, n)\n\t\tdpMin[i] = make([]int64, n)\n\
        \t}\n\n\tdpMax[0][0] = int64(grid[0][0])\n\tdpMin[0][0] = int64(grid[0][0])\n\
        \n\tfor i := 1; i < m; i++ {\n\t\tdpMax[i][0] = dpMax[i-1][0] * int64(grid[i][0])\n\
        \t\tdpMin[i][0] = dpMax[i][0]\n\t}\n\tfor j := 1; j < n; j++ {\n\t\tdpMax[0][j]\
        \ = dpMax[0][j-1] * int64(grid[0][j])\n\t\tdpMin[0][j] = dpMax[0][j]\n\t}\n\n\
        \tfor i := 1; i < m; i++ {\n\t\tfor j := 1; j < n; j++ {\n\t\t\tval := int64(grid[i][j])\n\
        \t\t\tc1 := dpMax[i-1][j] * val\n\t\t\tc2 := dpMin[i-1][j] * val\n\t\t\tc3 :=\
        \ dpMax[i][j-1] * val\n\t\t\tc4 := dpMin[i][j-1] * val\n\n\t\t\tmx := c1\n\t\
        \t\tif c2 > mx { mx = c2 }\n\t\t\tif c3 > mx { mx = c3 }\n\t\t\tif c4 > mx {\
        \ mx = c4 }\n\n\t\t\tmn := c1\n\t\t\tif c2 < mn { mn = c2 }\n\t\t\tif c3 < mn\
        \ { mn = c3 }\n\t\t\tif c4 < mn { mn = c4 }\n\n\t\t\tdpMax[i][j] = mx\n\t\t\t\
        dpMin[i][j] = mn\n\t\t}\n\t}\n\n\tres := dpMax[m-1][n-1]\n\tif res < 0 {\n\t\
        \treturn -1\n\t}\n\treturn int(res % 1000000007)\n}"
      ruby: "def max_product_path(grid)\n  m, n = grid.size, grid[0].size\n  dp_max\
        \ = Array.new(m) { Array.new(n) }\n  dp_min = Array.new(m) { Array.new(n) }\n\
        \n  dp_max[0][0] = dp_min[0][0] = grid[0][0]\n\n  (1...m).each { |i| dp_max[i][0]\
        \ = dp_min[i][0] = dp_max[i-1][0] * grid[i][0] }\n  (1...n).each { |j| dp_max[0][j]\
        \ = dp_min[0][j] = dp_max[0][j-1] * grid[0][j] }\n\n  (1...m).each do |i|\n\
        \    (1...n).each do |j|\n      val = grid[i][j]\n      opts = [\n        dp_max[i-1][j]\
        \ * val,\n        dp_min[i-1][j] * val,\n        dp_max[i][j-1] * val,\n   \
        \     dp_min[i][j-1] * val\n      ]\n      dp_max[i][j] = opts.max\n      dp_min[i][j]\
        \ = opts.min\n    end\n  end\n\n  res = dp_max[m-1][n-1]\n  res < 0 ? -1 : res\
        \ % 1000000007\nend"
      scala: "object Solution {\n  def maxProductPath(grid: Array[Array[Int]]): Int\
        \ = {\n    val m = grid.length\n    val n = grid(0).length\n    val dpMax =\
        \ Array.ofDim[Long](m, n)\n    val dpMin = Array.ofDim[Long](m, n)\n\n    dpMax(0)(0)\
        \ = grid(0)(0).toLong\n    dpMin(0)(0) = grid(0)(0).toLong\n\n    for (i <-\
        \ 1 until m) {\n      dpMax(i)(0) = dpMax(i - 1)(0) * grid(i)(0).toLong\n  \
        \    dpMin(i)(0) = dpMax(i)(0)\n    }\n    for (j <- 1 until n) {\n      dpMax(0)(j)\
        \ = dpMax(0)(j - 1) * grid(0)(j).toLong\n      dpMin(0)(j) = dpMax(0)(j)\n \
        \   }\n\n    for (i <- 1 until m; j <- 1 until n) {\n      val v = grid(i)(j).toLong\n\
        \      val options = Array(\n        dpMax(i - 1)(j) * v,\n        dpMin(i -\
        \ 1)(j) * v,\n        dpMax(i)(j - 1) * v,\n        dpMin(i)(j - 1) * v\n  \
        \    )\n      dpMax(i)(j) = options.max\n      dpMin(i)(j) = options.min\n \
        \   }\n\n    val res = dpMax(m - 1)(n - 1)\n    if (res < 0) -1 else (res %\
        \ 1000000007).toInt\n  }\n}"
      rust: "impl Solution {\n    pub fn max_product_path(grid: Vec<Vec<i32>>) -> i32\
        \ {\n        let m = grid.len();\n        let n = grid[0].len();\n        let\
        \ mut dp_max = vec![vec![0i64; n]; m];\n        let mut dp_min = vec![vec![0i64;\
        \ n]; m];\n\n        dp_max[0][0] = grid[0][0] as i64;\n        dp_min[0][0]\
        \ = grid[0][0] as i64;\n\n        for i in 1..m {\n            dp_max[i][0]\
        \ = dp_max[i - 1][0] * grid[i][0] as i64;\n            dp_min[i][0] = dp_max[i][0];\n\
        \        }\n        for j in 1..n {\n            dp_max[0][j] = dp_max[0][j\
        \ - 1] * grid[0][j] as i64;\n            dp_min[0][j] = dp_max[0][j];\n    \
        \    }\n\n        for i in 1..m {\n            for j in 1..n {\n           \
        \     let v = grid[i][j] as i64;\n                let options = [\n        \
        \            dp_max[i - 1][j] * v,\n                    dp_min[i - 1][j] * v,\n\
        \                    dp_max[i][j - 1] * v,\n                    dp_min[i][j\
        \ - 1] * v,\n                ];\n                dp_max[i][j] = *options.iter().max().unwrap();\n\
        \                dp_min[i][j] = *options.iter().min().unwrap();\n          \
        \  }\n        }\n\n        let res = dp_max[m - 1][n - 1];\n        if res <\
        \ 0 {\n            -1\n        } else {\n            (res % 1_000_000_007) as\
        \ i32\n        }\n    }\n}"
      racket: "(define/contract (max-product-path grid)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer?)\n  (let* ([m (length grid)]\n         [n (length (car grid))]\n\
        \         [vec-grid (list->vector (map list->vector grid))]\n         [dp-max\
        \ (make-vector m)]\n         [dp-min (make-vector m)])\n    (for ([i (in-range\
        \ m)])\n      (vector-set! dp-max i (make-vector n 0))\n      (vector-set! dp-min\
        \ i (make-vector n 0)))\n    (let ([v00 (vector-ref (vector-ref vec-grid 0)\
        \ 0)])\n      (vector-set! (vector-ref dp-max 0) 0 v00)\n      (vector-set!\
        \ (vector-ref dp-min 0) 0 v00))\n    (for ([i (in-range 1 m)])\n      (let ([v\
        \ (vector-ref (vector-ref vec-grid i) 0)]\n            [prev (vector-ref (vector-ref\
        \ dp-max (- i 1)) 0)])\n        (vector-set! (vector-ref dp-max i) 0 (* prev\
        \ v))\n        (vector-set! (vector-ref dp-min i) 0 (* prev v))))\n    (for\
        \ ([j (in-range 1 n)])\n      (let ([v (vector-ref (vector-ref vec-grid 0) j)]\n\
        \            [prev (vector-ref (vector-ref dp-max 0) (- j 1))])\n        (vector-set!\
        \ (vector-ref dp-max 0) j (* prev v))\n        (vector-set! (vector-ref dp-min\
        \ 0) j (* prev v))))\n    (for ([i (in-range 1 m)])\n      (for ([j (in-range\
        \ 1 n)])\n        (let* ([v (vector-ref (vector-ref vec-grid i) j)]\n      \
        \         [a (* (vector-ref (vector-ref dp-max (- i 1)) j) v)]\n           \
        \    [b (* (vector-ref (vector-ref dp-min (- i 1)) j) v)]\n               [c\
        \ (* (vector-ref (vector-ref dp-max i) (- j 1)) v)]\n               [d (* (vector-ref\
        \ (vector-ref dp-min i) (- j 1)) v)]\n               [opts (list a b c d)])\n\
        \          (vector-set! (vector-ref dp-max i) j (apply max opts))\n        \
        \  (vector-set! (vector-ref dp-min i) j (apply min opts)))))\n    (let ([res\
        \ (vector-ref (vector-ref dp-max (- m 1)) (- n 1))])\n      (if (< res 0) -1\
        \ (modulo res 1000000007)))))"
      erlang: "-spec max_product_path(Grid :: [[integer()]]) -> integer().\nmax_product_path(Grid)\
        \ ->\n    M = length(Grid),\n    N = length(hd(Grid)),\n    GridVec = list_to_tuple([list_to_tuple(Row)\
        \ || Row <- Grid]),\n    V00 = element(1, element(1, GridVec)),\n    Dp1 = #{{0,\
        \ 0} => {V00, V00}},\n    Dp2 = if M > 1 ->\n              lists:foldl(fun(I,\
        \ Acc) ->\n                  {PrevMax, _} = maps:get({I-1, 0}, Acc),\n     \
        \             Val = PrevMax * element(1, element(I+1, GridVec)),\n         \
        \         Acc#{ {I, 0} => {Val, Val} }\n              end, Dp1, lists:seq(1,\
        \ M-1));\n          true -> Dp1\n          end,\n    Dp3 = if N > 1 ->\n   \
        \           lists:foldl(fun(J, Acc) ->\n                  {PrevMax, _} = maps:get({0,\
        \ J-1}, Acc),\n                  Val = PrevMax * element(J+1, element(1, GridVec)),\n\
        \                  Acc#{ {0, J} => {Val, Val} }\n              end, Dp2, lists:seq(1,\
        \ N-1));\n          true -> Dp2\n          end,\n    FinalDp = if M > 1 andalso\
        \ N > 1 ->\n                  lists:foldl(fun(I, AccI) ->\n                \
        \      lists:foldl(fun(J, AccJ) ->\n                          V = element(J+1,\
        \ element(I+1, GridVec)),\n                          {MaxU, MinU} = maps:get({I-1,\
        \ J}, AccJ),\n                          {MaxL, MinL} = maps:get({I, J-1}, AccJ),\n\
        \                          Opts = [MaxU * V, MinU * V, MaxL * V, MinL * V],\n\
        \                          AccJ#{ {I, J} => {lists:max(Opts), lists:min(Opts)}\
        \ }\n                      end, AccI, lists:seq(1, N-1))\n                 \
        \ end, Dp3, lists:seq(1, M-1));\n              true -> Dp3\n              end,\n\
        \    {ResMax, _} = maps:get({M-1, N-1}, FinalDp),\n    if ResMax < 0 -> -1;\n\
        \       true -> ResMax rem 1000000007\n    end."
      elixir: "defmodule Solution do\n  @spec max_product_path(grid :: [[integer]])\
        \ :: integer\n  def max_product_path(grid) do\n    m = length(grid)\n    n =\
        \ length(hd(grid))\n    grid_tuple = grid |> Enum.map(&List.to_tuple/1) |> List.to_tuple()\n\
        \    dp = %{}\n    v00 = elem(elem(grid_tuple, 0), 0)\n    dp = Map.put(dp,\
        \ {0, 0}, {v00, v00})\n    dp = if m > 1 do\n      Enum.reduce(1..(m - 1), dp,\
        \ fn i, acc ->\n        {prev_max, _} = Map.get(acc, {i - 1, 0})\n        val\
        \ = prev_max * elem(elem(grid_tuple, i), 0)\n        Map.put(acc, {i, 0}, {val,\
        \ val})\n      end)\n    else\n      dp\n    end\n    dp = if n > 1 do\n   \
        \   Enum.reduce(1..(n - 1), dp, fn j, acc ->\n        {prev_max, _} = Map.get(acc,\
        \ {0, j - 1})\n        val = prev_max * elem(elem(grid_tuple, 0), j)\n     \
        \   Map.put(acc, {0, j}, {val, val})\n      end)\n    else\n      dp\n    end\n\
        \    dp = if m > 1 and n > 1 do\n      Enum.reduce(1..(m - 1), dp, fn i, acc_i\
        \ ->\n        Enum.reduce(1..(n - 1), acc_i, fn j, acc_j ->\n          v = elem(elem(grid_tuple,\
        \ i), j)\n          {max_u, min_u} = Map.get(acc_j, {i - 1, j})\n          {max_l,\
        \ min_l} = Map.get(acc_j, {i, j - 1})\n          opts = [max_u * v, min_u *\
        \ v, max_l * v, min_l * v]\n          Map.put(acc_j, {i, j}, {Enum.max(opts),\
        \ Enum.min(opts)})\n        end)\n      end)\n    else\n      dp\n    end\n\
        \    {res_max, _} = Map.get(dp, {m - 1, n - 1})\n    if res_max < 0, do: -1,\
        \ else: rem(res_max, 1000000007)\n  end\nend"
    approach: 'The problem is solved using dynamic programming by tracking both the
      maximum and minimum possible products at each cell $(i, j)$. Since the grid contains
      negative numbers, a negative cell value can convert a minimum (highly negative)
      product into a maximum (highly positive) one. We maintain two 2D arrays, `maxDP`
      and `minDP`, where `maxDP[i][j]` stores the largest possible product and `minDP[i][j]`
      stores the smallest possible product reachable at cell $(i, j)$ from the top-left
      corner.


      At each cell, the maximum and minimum products are computed based on the products
      from the cell above $(i-1, j)$ and the cell to the left $(i, j-1)$. If the current
      cell value is non-negative, the maximum product at $(i, j)$ is the maximum of
      the adjacent maximums multiplied by the current value. If the current cell value
      is negative, the maximum product is the minimum of the adjacent minimums multiplied
      by the current value. After traversing the entire grid, the result is the value
      at `maxDP[m-1][n-1]`. If it is negative, we return -1; otherwise, we return the
      result modulo $10^9 + 7$.'
    time_complexity: O(m * n) because we iterate through each cell of the m x n grid
      exactly once, performing a constant amount of work per cell.
    space_complexity: O(m * n) because we use two 2D DP tables of size m x n to store
      the intermediate maximum and minimum path products.
    elapsed_time: 207.1158139705658
    model: gemini-3-flash-preview
    generated_at: '2026-03-23 01:31:15 '
---

## Problem #1594: Maximum Non Negative Product in a Matrix

**Difficulty:** Medium

**Topics:** Array, Dynamic Programming, Matrix

## Problem Description

<p>You are given a <code>m x n</code> matrix <code>grid</code>. Initially, you are located at the top-left corner <code>(0, 0)</code>, and in each step, you can only <strong>move right or down</strong> in the matrix.</p>

<p>Among all possible paths starting from the top-left corner <code>(0, 0)</code> and ending in the bottom-right corner <code>(m - 1, n - 1)</code>, find the path with the <strong>maximum non-negative product</strong>. The product of a path is the product of all integers in the grid cells visited along the path.</p>

<p>Return the <em>maximum non-negative product <strong>modulo</strong> </em><code>10<sup>9</sup> + 7</code>. <em>If the maximum product is <strong>negative</strong>, return </em><code>-1</code>.</p>

<p>Notice that the modulo is performed after getting the maximum product.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/23/product1.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>Input:</strong> grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/23/product2.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>Input:</strong> grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
<strong>Output:</strong> 8
<strong>Explanation:</strong> Maximum non-negative product is shown (1 * 1 * -2 * -4 * 1 = 8).
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/23/product3.jpg" style="width: 164px; height: 165px;" />
<pre>
<strong>Input:</strong> grid = [[1,3],[0,-4]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Maximum non-negative product is shown (1 * 0 * -4 = 0).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 15</code></li>
	<li><code>-4 &lt;= grid[i][j] &lt;= 4</code></li>
</ul>


## Hints

1. Use Dynamic programming. Keep the highest value and lowest value you can achieve up to a point.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem is solved using dynamic programming by tracking both the maximum and minimum possible products at each cell $(i, j)$. Since the grid contains negative numbers, a negative cell value can convert a minimum (highly negative) product into a maximum (highly positive) one. We maintain two 2D arrays, `maxDP` and `minDP`, where `maxDP[i][j]` stores the largest possible product and `minDP[i][j]` stores the smallest possible product reachable at cell $(i, j)$ from the top-left corner.

At each cell, the maximum and minimum products are computed based on the products from the cell above $(i-1, j)$ and the cell to the left $(i, j-1)$. If the current cell value is non-negative, the maximum product at $(i, j)$ is the maximum of the adjacent maximums multiplied by the current value. If the current cell value is negative, the maximum product is the minimum of the adjacent minimums multiplied by the current value. After traversing the entire grid, the result is the value at `maxDP[m-1][n-1]`. If it is negative, we return -1; otherwise, we return the result modulo $10^9 + 7$.

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
    int maxProductPath(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        long long maxDP[15][15], minDP[15][15];
        long long MOD = 1e9 + 7;

        maxDP[0][0] = minDP[0][0] = grid[0][0];
        for (int i = 1; i < m; ++i) maxDP[i][0] = minDP[i][0] = maxDP[i - 1][0] * grid[i][0];
        for (int j = 1; j < n; ++j) maxDP[0][j] = minDP[0][j] = maxDP[0][j - 1] * grid[0][j];

        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                long long v = grid[i][j];
                long long a = maxDP[i - 1][j] * v, b = maxDP[i][j - 1] * v;
                long long c = minDP[i - 1][j] * v, d = minDP[i][j - 1] * v;
                maxDP[i][j] = max({a, b, c, d});
                minDP[i][j] = min({a, b, c, d});
            }
        }

        long long res = maxDP[m - 1][n - 1];
        return res < 0 ? -1 : res % MOD;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxProductPath(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        long[][] maxDP = new long[m][n];
        long[][] minDP = new long[m][n];
        long MOD = 1000000007;

        maxDP[0][0] = minDP[0][0] = grid[0][0];
        for (int i = 1; i < m; i++) maxDP[i][0] = minDP[i][0] = maxDP[i - 1][0] * grid[i][0];
        for (int j = 1; j < n; j++) maxDP[0][j] = minDP[0][j] = maxDP[0][j - 1] * grid[0][j];

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                long v = grid[i][j];
                long a = maxDP[i - 1][j] * v, b = maxDP[i][j - 1] * v;
                long c = minDP[i - 1][j] * v, d = minDP[i][j - 1] * v;
                maxDP[i][j] = Math.max(a, Math.max(b, Math.max(c, d)));
                minDP[i][j] = Math.min(a, Math.min(b, Math.min(c, d)));
            }
        }

        long res = maxDP[m - 1][n - 1];
        return res < 0 ? -1 : (int) (res % MOD);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]

        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        for i in range(1, m):
            max_dp[i][0] = min_dp[i][0] = max_dp[i-1][0] * grid[i][0]
        for j in range(1, n):
            max_dp[0][j] = min_dp[0][j] = max_dp[0][j-1] * grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                v = grid[i][j]
                a, b, c, d = max_dp[i-1][j]*v, max_dp[i][j-1]*v, min_dp[i-1][j]*v, min_dp[i][j-1]*v
                max_dp[i][j] = max(a, b, c, d)
                min_dp[i][j] = min(a, b, c, d)

        res = max_dp[m-1][n-1]
        return res % 1000000007 if res >= 0 else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]

        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        for i in range(1, m):
            max_dp[i][0] = min_dp[i][0] = max_dp[i-1][0] * grid[i][0]
        for j in range(1, n):
            max_dp[0][j] = min_dp[0][j] = max_dp[0][j-1] * grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                v = grid[i][j]
                vals = (max_dp[i-1][j]*v, max_dp[i][j-1]*v, min_dp[i-1][j]*v, min_dp[i][j-1]*v)
                max_dp[i][j] = max(vals)
                min_dp[i][j] = min(vals)

        res = max_dp[m-1][n-1]
        return res % 1000000007 if res >= 0 else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maxProductPath(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    long long maxDP[15][15], minDP[15][15];

    maxDP[0][0] = minDP[0][0] = grid[0][0];
    for (int i = 1; i < m; i++) maxDP[i][0] = minDP[i][0] = maxDP[i - 1][0] * grid[i][0];
    for (int j = 1; j < n; j++) maxDP[0][j] = minDP[0][j] = maxDP[0][j - 1] * grid[0][j];

    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            long long v = grid[i][j];
            long long a = maxDP[i - 1][j] * v, b = maxDP[i][j - 1] * v, c = minDP[i - 1][j] * v, d = minDP[i][j - 1] * v;
            long long curMax = a, curMin = a;
            if (b > curMax) curMax = b; if (c > curMax) curMax = c; if (d > curMax) curMax = d;
            if (b < curMin) curMin = b; if (c < curMin) curMin = c; if (d < curMin) curMin = d;
            maxDP[i][j] = curMax; minDP[i][j] = curMin;
        }
    }
    long long res = maxDP[m - 1][n - 1];
    return res < 0 ? -1 : (int)(res % 1000000007);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxProductPath(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        long[,] maxDP = new long[m, n];
        long[,] minDP = new long[m, n];
        long MOD = 1000000007;

        maxDP[0, 0] = minDP[0, 0] = grid[0][0];
        for (int i = 1; i < m; i++) maxDP[i, 0] = minDP[i, 0] = maxDP[i - 1, 0] * grid[i][0];
        for (int j = 1; j < n; j++) maxDP[0, j] = minDP[0, j] = maxDP[0, j - 1] * grid[0][j];

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                long v = grid[i][j];
                long a = maxDP[i - 1, j] * v, b = maxDP[i, j - 1] * v;
                long c = minDP[i - 1, j] * v, d = minDP[i, j - 1] * v;
                maxDP[i, j] = Math.Max(a, Math.Max(b, Math.Max(c, d)));
                minDP[i, j] = Math.Min(a, Math.Min(b, Math.Min(c, d)));
            }
        }

        long res = maxDP[m - 1, n - 1];
        return res < 0 ? -1 : (int)(res % MOD);
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
var maxProductPath = function(grid) {
    let m = grid.length, n = grid[0].length;
    let maxDP = Array.from({ length: m }, () => new BigInt64Array(n));
    let minDP = Array.from({ length: m }, () => new BigInt64Array(n));

    maxDP[0][0] = minDP[0][0] = BigInt(grid[0][0]);
    for (let i = 1; i < m; i++) maxDP[i][0] = minDP[i][0] = maxDP[i - 1][0] * BigInt(grid[i][0]);
    for (let j = 1; j < n; j++) maxDP[0][j] = minDP[0][j] = maxDP[0][j - 1] * BigInt(grid[0][j]);

    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            let v = BigInt(grid[i][j]);
            let a = maxDP[i - 1][j] * v, b = maxDP[i][j - 1] * v;
            let c = minDP[i - 1][j] * v, d = minDP[i][j - 1] * v;
            let maxVal = a; if (b > maxVal) maxVal = b; if (c > maxVal) maxVal = c; if (d > maxVal) maxVal = d;
            let minVal = a; if (b < minVal) minVal = b; if (c < minVal) minVal = c; if (d < minVal) minVal = d;
            maxDP[i][j] = maxVal; minDP[i][j] = minVal;
        }
    }

    let res = maxDP[m - 1][n - 1];
    return res < 0n ? -1 : Number(res % 1000000007n);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxProductPath(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const dpMax: bigint[][] = Array.from({ length: m }, () => Array(n).fill(0n));
    const dpMin: bigint[][] = Array.from({ length: m }, () => Array(n).fill(0n));

    dpMax[0][0] = BigInt(grid[0][0]);
    dpMin[0][0] = BigInt(grid[0][0]);

    for (let i = 1; i < m; i++) {
        dpMax[i][0] = dpMin[i][0] = dpMax[i - 1][0] * BigInt(grid[i][0]);
    }
    for (let j = 1; j < n; j++) {
        dpMax[0][j] = dpMin[0][j] = dpMax[0][j - 1] * BigInt(grid[0][j]);
    }

    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            const val = BigInt(grid[i][j]);
            const c1 = dpMax[i - 1][j] * val;
            const c2 = dpMin[i - 1][j] * val;
            const c3 = dpMax[i][j - 1] * val;
            const c4 = dpMin[i][j - 1] * val;

            let mx = c1;
            if (c2 > mx) mx = c2;
            if (c3 > mx) mx = c3;
            if (c4 > mx) mx = c4;

            let mn = c1;
            if (c2 < mn) mn = c2;
            if (c3 < mn) mn = c3;
            if (c4 < mn) mn = c4;

            dpMax[i][j] = mx;
            dpMin[i][j] = mn;
        }
    }

    const res = dpMax[m - 1][n - 1];
    if (res < 0n) return -1;
    return Number(res % 1000000007n);
}
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
    function maxProductPath($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $dpMax = array_fill(0, $m, array_fill(0, $n, 0));
        $dpMin = array_fill(0, $m, array_fill(0, $n, 0));

        $dpMax[0][0] = $dpMin[0][0] = $grid[0][0];

        for ($i = 1; $i < $m; $i++) {
            $dpMax[$i][0] = $dpMin[$i][0] = $dpMax[$i - 1][0] * $grid[$i][0];
        }
        for ($j = 1; $j < $n; $j++) {
            $dpMax[0][$j] = $dpMin[0][$j] = $dpMax[0][$j - 1] * $grid[0][$j];
        }

        for ($i = 1; $i < $m; $i++) {
            for ($j = 1; $j < $n; $j++) {
                $val = $grid[$i][j];
                $c1 = $dpMax[$i - 1][$j] * $val;
                $c2 = $dpMin[$i - 1][$j] * $val;
                $c3 = $dpMax[$i][$j - 1] * $val;
                $c4 = $dpMin[$i][$j - 1] * $val;
                $dpMax[$i][$j] = max($c1, $c2, $c3, $c4);
                $dpMin[$i][$j] = min($c1, $c2, $c3, $c4);
            }
        }

        $res = $dpMax[$m - 1][$n - 1];
        if ($res < 0) return -1;
        return $res % 1000000007;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxProductPath(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var dpMax = Array(repeating: Array(repeating: 0, count: n), count: m)
        var dpMin = Array(repeating: Array(repeating: 0, count: n), count: m)

        dpMax[0][0] = grid[0][0]
        dpMin[0][0] = grid[0][0]

        for i in 1..<m {
            dpMax[i][0] = dpMax[i-1][0] * grid[i][0]
            dpMin[i][0] = dpMax[i][0]
        }
        for j in 1..<n {
            dpMax[0][j] = dpMax[0][j-1] * grid[0][j]
            dpMin[0][j] = dpMax[0][j]
        }

        if m > 1 && n > 1 {
            for i in 1..<m {
                for j in 1..<n {
                    let val = grid[i][j]
                    let c1 = dpMax[i-1][j] * val
                    let c2 = dpMin[i-1][j] * val
                    let c3 = dpMax[i][j-1] * val
                    let c4 = dpMin[i][j-1] * val
                    dpMax[i][j] = max(max(c1, c2), max(c3, c4))
                    dpMin[i][j] = min(min(c1, c2), min(c3, c4))
                }
            }
        }

        let res = dpMax[m-1][n-1]
        if res < 0 {
            return -1
        }
        return res % 1_000_000_007
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxProductPath(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val dpMax = Array(m) { LongArray(n) }
        val dpMin = Array(m) { LongArray(n) }

        dpMax[0][0] = grid[0][0].toLong()
        dpMin[0][0] = grid[0][0].toLong()

        for (i in 1 until m) {
            dpMax[i][0] = dpMax[i - 1][0] * grid[i][0]
            dpMin[i][0] = dpMax[i][0]
        }
        for (j in 1 until n) {
            dpMax[0][j] = dpMax[0][j - 1] * grid[0][j]
            dpMin[0][j] = dpMax[0][j]
        }

        for (i in 1 until m) {
            for (j in 1 until n) {
                val valGrid = grid[i][j].toLong()
                val c1 = dpMax[i - 1][j] * valGrid
                val c2 = dpMin[i - 1][j] * valGrid
                val c3 = dpMax[i][j - 1] * valGrid
                val c4 = dpMin[i][j - 1] * valGrid
                dpMax[i][j] = maxOf(maxOf(c1, c2), maxOf(c3, c4))
                dpMin[i][j] = minOf(minOf(c1, c2), minOf(c3, c4))
            }
        }

        val res = dpMax[m - 1][n - 1]
        return if (res < 0) -1 else (res % 1000000007).toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxProductPath(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    List<List<int>> dpMax = List.generate(m, (_) => List.filled(n, 0));
    List<List<int>> dpMin = List.generate(m, (_) => List.filled(n, 0));

    dpMax[0][0] = dpMin[0][0] = grid[0][0];

    for (int i = 1; i < m; i++) {
      dpMax[i][0] = dpMin[i][0] = dpMax[i - 1][0] * grid[i][0];
    }
    for (int j = 1; j < n; j++) {
      dpMax[0][j] = dpMin[0][j] = dpMax[0][j - 1] * grid[0][j];
    }

    for (int i = 1; i < m; i++) {
      for (int j = 1; j < n; j++) {
        int val = grid[i][j];
        int c1 = dpMax[i - 1][j] * val;
        int c2 = dpMin[i - 1][j] * val;
        int c3 = dpMax[i][j - 1] * val;
        int c4 = dpMin[i][j - 1] * val;

        int mx = c1;
        if (c2 > mx) mx = c2;
        if (c3 > mx) mx = c3;
        if (c4 > mx) mx = c4;

        int mn = c1;
        if (c2 < mn) mn = c2;
        if (c3 < mn) mn = c3;
        if (c4 < mn) mn = c4;

        dpMax[i][j] = mx;
        dpMin[i][j] = mn;
      }
    }

    int res = dpMax[m - 1][n - 1];
    if (res < 0) return -1;
    return res % 1000000007;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxProductPath(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	dpMax := make([][]int64, m)
	dpMin := make([][]int64, m)
	for i := range dpMax {
		dpMax[i] = make([]int64, n)
		dpMin[i] = make([]int64, n)
	}

	dpMax[0][0] = int64(grid[0][0])
	dpMin[0][0] = int64(grid[0][0])

	for i := 1; i < m; i++ {
		dpMax[i][0] = dpMax[i-1][0] * int64(grid[i][0])
		dpMin[i][0] = dpMax[i][0]
	}
	for j := 1; j < n; j++ {
		dpMax[0][j] = dpMax[0][j-1] * int64(grid[0][j])
		dpMin[0][j] = dpMax[0][j]
	}

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			val := int64(grid[i][j])
			c1 := dpMax[i-1][j] * val
			c2 := dpMin[i-1][j] * val
			c3 := dpMax[i][j-1] * val
			c4 := dpMin[i][j-1] * val

			mx := c1
			if c2 > mx { mx = c2 }
			if c3 > mx { mx = c3 }
			if c4 > mx { mx = c4 }

			mn := c1
			if c2 < mn { mn = c2 }
			if c3 < mn { mn = c3 }
			if c4 < mn { mn = c4 }

			dpMax[i][j] = mx
			dpMin[i][j] = mn
		}
	}

	res := dpMax[m-1][n-1]
	if res < 0 {
		return -1
	}
	return int(res % 1000000007)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def max_product_path(grid)
  m, n = grid.size, grid[0].size
  dp_max = Array.new(m) { Array.new(n) }
  dp_min = Array.new(m) { Array.new(n) }

  dp_max[0][0] = dp_min[0][0] = grid[0][0]

  (1...m).each { |i| dp_max[i][0] = dp_min[i][0] = dp_max[i-1][0] * grid[i][0] }
  (1...n).each { |j| dp_max[0][j] = dp_min[0][j] = dp_max[0][j-1] * grid[0][j] }

  (1...m).each do |i|
    (1...n).each do |j|
      val = grid[i][j]
      opts = [
        dp_max[i-1][j] * val,
        dp_min[i-1][j] * val,
        dp_max[i][j-1] * val,
        dp_min[i][j-1] * val
      ]
      dp_max[i][j] = opts.max
      dp_min[i][j] = opts.min
    end
  end

  res = dp_max[m-1][n-1]
  res < 0 ? -1 : res % 1000000007
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def maxProductPath(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val dpMax = Array.ofDim[Long](m, n)
    val dpMin = Array.ofDim[Long](m, n)

    dpMax(0)(0) = grid(0)(0).toLong
    dpMin(0)(0) = grid(0)(0).toLong

    for (i <- 1 until m) {
      dpMax(i)(0) = dpMax(i - 1)(0) * grid(i)(0).toLong
      dpMin(i)(0) = dpMax(i)(0)
    }
    for (j <- 1 until n) {
      dpMax(0)(j) = dpMax(0)(j - 1) * grid(0)(j).toLong
      dpMin(0)(j) = dpMax(0)(j)
    }

    for (i <- 1 until m; j <- 1 until n) {
      val v = grid(i)(j).toLong
      val options = Array(
        dpMax(i - 1)(j) * v,
        dpMin(i - 1)(j) * v,
        dpMax(i)(j - 1) * v,
        dpMin(i)(j - 1) * v
      )
      dpMax(i)(j) = options.max
      dpMin(i)(j) = options.min
    }

    val res = dpMax(m - 1)(n - 1)
    if (res < 0) -1 else (res % 1000000007).toInt
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_product_path(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut dp_max = vec![vec![0i64; n]; m];
        let mut dp_min = vec![vec![0i64; n]; m];

        dp_max[0][0] = grid[0][0] as i64;
        dp_min[0][0] = grid[0][0] as i64;

        for i in 1..m {
            dp_max[i][0] = dp_max[i - 1][0] * grid[i][0] as i64;
            dp_min[i][0] = dp_max[i][0];
        }
        for j in 1..n {
            dp_max[0][j] = dp_max[0][j - 1] * grid[0][j] as i64;
            dp_min[0][j] = dp_max[0][j];
        }

        for i in 1..m {
            for j in 1..n {
                let v = grid[i][j] as i64;
                let options = [
                    dp_max[i - 1][j] * v,
                    dp_min[i - 1][j] * v,
                    dp_max[i][j - 1] * v,
                    dp_min[i][j - 1] * v,
                ];
                dp_max[i][j] = *options.iter().max().unwrap();
                dp_min[i][j] = *options.iter().min().unwrap();
            }
        }

        let res = dp_max[m - 1][n - 1];
        if res < 0 {
            -1
        } else {
            (res % 1_000_000_007) as i32
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-product-path grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([m (length grid)]
         [n (length (car grid))]
         [vec-grid (list->vector (map list->vector grid))]
         [dp-max (make-vector m)]
         [dp-min (make-vector m)])
    (for ([i (in-range m)])
      (vector-set! dp-max i (make-vector n 0))
      (vector-set! dp-min i (make-vector n 0)))
    (let ([v00 (vector-ref (vector-ref vec-grid 0) 0)])
      (vector-set! (vector-ref dp-max 0) 0 v00)
      (vector-set! (vector-ref dp-min 0) 0 v00))
    (for ([i (in-range 1 m)])
      (let ([v (vector-ref (vector-ref vec-grid i) 0)]
            [prev (vector-ref (vector-ref dp-max (- i 1)) 0)])
        (vector-set! (vector-ref dp-max i) 0 (* prev v))
        (vector-set! (vector-ref dp-min i) 0 (* prev v))))
    (for ([j (in-range 1 n)])
      (let ([v (vector-ref (vector-ref vec-grid 0) j)]
            [prev (vector-ref (vector-ref dp-max 0) (- j 1))])
        (vector-set! (vector-ref dp-max 0) j (* prev v))
        (vector-set! (vector-ref dp-min 0) j (* prev v))))
    (for ([i (in-range 1 m)])
      (for ([j (in-range 1 n)])
        (let* ([v (vector-ref (vector-ref vec-grid i) j)]
               [a (* (vector-ref (vector-ref dp-max (- i 1)) j) v)]
               [b (* (vector-ref (vector-ref dp-min (- i 1)) j) v)]
               [c (* (vector-ref (vector-ref dp-max i) (- j 1)) v)]
               [d (* (vector-ref (vector-ref dp-min i) (- j 1)) v)]
               [opts (list a b c d)])
          (vector-set! (vector-ref dp-max i) j (apply max opts))
          (vector-set! (vector-ref dp-min i) j (apply min opts)))))
    (let ([res (vector-ref (vector-ref dp-max (- m 1)) (- n 1))])
      (if (< res 0) -1 (modulo res 1000000007)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_product_path(Grid :: [[integer()]]) -> integer().
max_product_path(Grid) ->
    M = length(Grid),
    N = length(hd(Grid)),
    GridVec = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),
    V00 = element(1, element(1, GridVec)),
    Dp1 = #{{0, 0} => {V00, V00}},
    Dp2 = if M > 1 ->
              lists:foldl(fun(I, Acc) ->
                  {PrevMax, _} = maps:get({I-1, 0}, Acc),
                  Val = PrevMax * element(1, element(I+1, GridVec)),
                  Acc#{ {I, 0} => {Val, Val} }
              end, Dp1, lists:seq(1, M-1));
          true -> Dp1
          end,
    Dp3 = if N > 1 ->
              lists:foldl(fun(J, Acc) ->
                  {PrevMax, _} = maps:get({0, J-1}, Acc),
                  Val = PrevMax * element(J+1, element(1, GridVec)),
                  Acc#{ {0, J} => {Val, Val} }
              end, Dp2, lists:seq(1, N-1));
          true -> Dp2
          end,
    FinalDp = if M > 1 andalso N > 1 ->
                  lists:foldl(fun(I, AccI) ->
                      lists:foldl(fun(J, AccJ) ->
                          V = element(J+1, element(I+1, GridVec)),
                          {MaxU, MinU} = maps:get({I-1, J}, AccJ),
                          {MaxL, MinL} = maps:get({I, J-1}, AccJ),
                          Opts = [MaxU * V, MinU * V, MaxL * V, MinL * V],
                          AccJ#{ {I, J} => {lists:max(Opts), lists:min(Opts)} }
                      end, AccI, lists:seq(1, N-1))
                  end, Dp3, lists:seq(1, M-1));
              true -> Dp3
              end,
    {ResMax, _} = maps:get({M-1, N-1}, FinalDp),
    if ResMax < 0 -> -1;
       true -> ResMax rem 1000000007
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_product_path(grid :: [[integer]]) :: integer
  def max_product_path(grid) do
    m = length(grid)
    n = length(hd(grid))
    grid_tuple = grid |> Enum.map(&List.to_tuple/1) |> List.to_tuple()
    dp = %{}
    v00 = elem(elem(grid_tuple, 0), 0)
    dp = Map.put(dp, {0, 0}, {v00, v00})
    dp = if m > 1 do
      Enum.reduce(1..(m - 1), dp, fn i, acc ->
        {prev_max, _} = Map.get(acc, {i - 1, 0})
        val = prev_max * elem(elem(grid_tuple, i), 0)
        Map.put(acc, {i, 0}, {val, val})
      end)
    else
      dp
    end
    dp = if n > 1 do
      Enum.reduce(1..(n - 1), dp, fn j, acc ->
        {prev_max, _} = Map.get(acc, {0, j - 1})
        val = prev_max * elem(elem(grid_tuple, 0), j)
        Map.put(acc, {0, j}, {val, val})
      end)
    else
      dp
    end
    dp = if m > 1 and n > 1 do
      Enum.reduce(1..(m - 1), dp, fn i, acc_i ->
        Enum.reduce(1..(n - 1), acc_i, fn j, acc_j ->
          v = elem(elem(grid_tuple, i), j)
          {max_u, min_u} = Map.get(acc_j, {i - 1, j})
          {max_l, min_l} = Map.get(acc_j, {i, j - 1})
          opts = [max_u * v, min_u * v, max_l * v, min_l * v]
          Map.put(acc_j, {i, j}, {Enum.max(opts), Enum.min(opts)})
        end)
      end)
    else
      dp
    end
    {res_max, _} = Map.get(dp, {m - 1, n - 1})
    if res_max < 0, do: -1, else: rem(res_max, 1000000007)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m * n) because we iterate through each cell of the m x n grid exactly once, performing a constant amount of work per cell.
- **Space Complexity:** O(m * n) because we use two 2D DP tables of size m x n to store the intermediate maximum and minimum path products.
