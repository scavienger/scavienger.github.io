---
layout: post
title: "Minimum Cost Path with Teleportations"
date: 2026-01-28 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Dynamic Programming", "Matrix"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/minimum-cost-path-with-teleportations/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minCost(vector<vector<int>>& grid, int\
        \ k) {\n        int m = grid.size(), n = grid[0].size();\n        int INF =\
        \ 1e9;\n        vector<vector<int>> dp(m, vector<int>(n, INF));\n        dp[0][0]\
        \ = 0;\n\n        for (int p = 0; p <= k; ++p) {\n            vector<vector<int>>\
        \ next_dp(m, vector<int>(n, INF));\n            if (p == 0) {\n            \
        \    next_dp[0][0] = 0;\n            } else {\n                vector<int> min_at_val(10001,\
        \ INF);\n                for (int r = 0; r < m; ++r) {\n                   \
        \ for (int c = 0; c < n; ++c) {\n                        if (dp[r][c] < INF)\
        \ {\n                            min_at_val[grid[r][c]] = min(min_at_val[grid[r][c]],\
        \ dp[r][c]);\n                        }\n                    }\n           \
        \     }\n                int suffix_min = INF;\n                for (int v =\
        \ 10000; v >= 0; --v) {\n                    suffix_min = min(suffix_min, min_at_val[v]);\n\
        \                    min_at_val[v] = suffix_min;\n                }\n      \
        \          for (int r = 0; r < m; ++r) {\n                    for (int c = 0;\
        \ c < n; ++c) {\n                        next_dp[r][c] = min_at_val[grid[r][c]];\n\
        \                    }\n                }\n            }\n            for (int\
        \ r = 0; r < m; ++r) {\n                for (int c = 0; c < n; ++c) {\n    \
        \                if (r > 0) next_dp[r][c] = min(next_dp[r][c], next_dp[r - 1][c]\
        \ + grid[r][c]);\n                    if (c > 0) next_dp[r][c] = min(next_dp[r][c],\
        \ next_dp[r][c - 1] + grid[r][c]);\n                }\n            }\n     \
        \       dp = next_dp;\n        }\n\n        int ans = INF;\n        return dp[m\
        \ - 1][n - 1];\n    }\n};"
      java: "class Solution {\n    public int minCost(int[][] grid, int k) {\n     \
        \   int m = grid.length, n = grid[0].length;\n        int INF = 1000000000;\n\
        \        int[][] dp = new int[m][n];\n        for (int i = 0; i < m; i++) java.util.Arrays.fill(dp[i],\
        \ INF);\n        dp[0][0] = 0;\n\n        for (int p = 0; p <= k; p++) {\n \
        \           int[][] next_dp = new int[m][n];\n            for (int i = 0; i\
        \ < m; i++) java.util.Arrays.fill(next_dp[i], INF);\n            if (p == 0)\
        \ {\n                next_dp[0][0] = 0;\n            } else {\n            \
        \    int[] minAtVal = new int[10001];\n                java.util.Arrays.fill(minAtVal,\
        \ INF);\n                for (int r = 0; r < m; r++) {\n                   \
        \ for (int c = 0; c < n; c++) {\n                        if (dp[r][c] < INF)\
        \ {\n                            minAtVal[grid[r][c]] = Math.min(minAtVal[grid[r][c]],\
        \ dp[r][c]);\n                        }\n                    }\n           \
        \     }\n                int suffixMin = INF;\n                for (int v =\
        \ 10000; v >= 0; v--) {\n                    suffixMin = Math.min(suffixMin,\
        \ minAtVal[v]);\n                    minAtVal[v] = suffixMin;\n            \
        \    }\n                for (int r = 0; r < m; r++) {\n                    for\
        \ (int c = 0; c < n; c++) {\n                        next_dp[r][c] = minAtVal[grid[r][c]];\n\
        \                    }\n                }\n            }\n            for (int\
        \ r = 0; r < m; r++) {\n                for (int c = 0; c < n; c++) {\n    \
        \                if (r > 0) next_dp[r][c] = Math.min(next_dp[r][c], next_dp[r\
        \ - 1][c] + grid[r][c]);\n                    if (c > 0) next_dp[r][c] = Math.min(next_dp[r][c],\
        \ next_dp[r][c - 1] + grid[r][c]);\n                }\n            }\n     \
        \       dp = next_dp;\n        }\n        return dp[m - 1][n - 1];\n    }\n}"
      python: "class Solution(object):\n    def minCost(self, grid, k):\n        m,\
        \ n = len(grid), len(grid[0])\n        INF = 10**9\n        dp = [[INF] * n\
        \ for _ in range(m)]\n        dp[0][0] = 0\n\n        for p in range(k + 1):\n\
        \            next_dp = [[INF] * n for _ in range(m)]\n            if p == 0:\n\
        \                next_dp[0][0] = 0\n            else:\n                min_at_val\
        \ = [INF] * 10001\n                for r in range(m):\n                    for\
        \ c in range(n):\n                        if dp[r][c] < INF:\n             \
        \               v = grid[r][c]\n                            if dp[r][c] < min_at_val[v]:\n\
        \                                min_at_val[v] = dp[r][c]\n\n              \
        \  suffix_min = INF\n                for v in range(10000, -1, -1):\n      \
        \              if min_at_val[v] < suffix_min:\n                        suffix_min\
        \ = min_at_val[v]\n                    min_at_val[v] = suffix_min\n\n      \
        \          for r in range(m):\n                    for c in range(n):\n    \
        \                    next_dp[r][c] = min_at_val[grid[r][c]]\n\n            for\
        \ r in range(m):\n                for c in range(n):\n                    if\
        \ r > 0:\n                        if next_dp[r-1][c] + grid[r][c] < next_dp[r][c]:\n\
        \                            next_dp[r][c] = next_dp[r-1][c] + grid[r][c]\n\
        \                    if c > 0:\n                        if next_dp[r][c-1] +\
        \ grid[r][c] < next_dp[r][c]:\n                            next_dp[r][c] = next_dp[r][c-1]\
        \ + grid[r][c]\n            dp = next_dp\n\n        return dp[m-1][n-1]"
      python3: "class Solution:\n    def minCost(self, grid: List[List[int]], k: int)\
        \ -> int:\n        m, n = len(grid), len(grid[0])\n        INF = 10**9\n   \
        \     dp = [[INF] * n for _ in range(m)]\n        dp[0][0] = 0\n\n        for\
        \ p in range(k + 1):\n            next_dp = [[INF] * n for _ in range(m)]\n\
        \            if p == 0:\n                next_dp[0][0] = 0\n            else:\n\
        \                min_at_val = [INF] * 10001\n                for r in range(m):\n\
        \                    for c in range(n):\n                        if dp[r][c]\
        \ < INF:\n                            v = grid[r][c]\n                     \
        \       if dp[r][c] < min_at_val[v]:\n                                min_at_val[v]\
        \ = dp[r][c]\n\n                suffix_min = INF\n                for v in range(10000,\
        \ -1, -1):\n                    if min_at_val[v] < suffix_min:\n           \
        \             suffix_min = min_at_val[v]\n                    min_at_val[v]\
        \ = suffix_min\n\n                for r in range(m):\n                    for\
        \ c in range(n):\n                        next_dp[r][c] = min_at_val[grid[r][c]]\n\
        \n            for r in range(m):\n                for c in range(n):\n     \
        \               if r > 0:\n                        if next_dp[r-1][c] + grid[r][c]\
        \ < next_dp[r][c]:\n                            next_dp[r][c] = next_dp[r-1][c]\
        \ + grid[r][c]\n                    if c > 0:\n                        if next_dp[r][c-1]\
        \ + grid[r][c] < next_dp[r][c]:\n                            next_dp[r][c] =\
        \ next_dp[r][c-1] + grid[r][c]\n            dp = next_dp\n\n        return dp[m-1][n-1]"
      c: "int minCost(int** grid, int gridSize, int* gridColSize, int k) {\n    int\
        \ m = gridSize, n = gridColSize[0];\n    int INF = 1000000000;\n    int dp[80][80];\n\
        \    int next_dp[80][80];\n\n    for (int i = 0; i < m; i++) for (int j = 0;\
        \ j < n; j++) dp[i][j] = INF;\n    dp[0][0] = 0;\n\n    int* min_at_val = (int*)malloc(sizeof(int)\
        \ * 10001);\n\n    for (int p = 0; p <= k; p++) {\n        for (int i = 0; i\
        \ < m; i++) for (int j = 0; j < n; j++) next_dp[i][j] = INF;\n        if (p\
        \ == 0) {\n            next_dp[0][0] = 0;\n        } else {\n            for\
        \ (int v = 0; v <= 10000; v++) min_at_val[v] = INF;\n            for (int r\
        \ = 0; r < m; r++) {\n                for (int c = 0; c < n; c++) {\n      \
        \              if (dp[r][c] < INF) {\n                        if (dp[r][c] <\
        \ min_at_val[grid[r][c]]) min_at_val[grid[r][c]] = dp[r][c];\n             \
        \       }\n                }\n            }\n            int suffix_min = INF;\n\
        \            for (int v = 10000; v >= 0; v--) {\n                if (min_at_val[v]\
        \ < suffix_min) suffix_min = min_at_val[v];\n                min_at_val[v] =\
        \ suffix_min;\n            }\n            for (int r = 0; r < m; r++) {\n  \
        \              for (int c = 0; c < n; c++) {\n                    next_dp[r][c]\
        \ = min_at_val[grid[r][c]];\n                }\n            }\n        }\n \
        \       for (int r = 0; r < m; r++) {\n            for (int c = 0; c < n; c++)\
        \ {\n                if (r > 0) {\n                    int val = next_dp[r-1][c]\
        \ + grid[r][c];\n                    if (val < next_dp[r][c]) next_dp[r][c]\
        \ = val;\n                }\n                if (c > 0) {\n                \
        \    int val = next_dp[r][c-1] + grid[r][c];\n                    if (val <\
        \ next_dp[r][c]) next_dp[r][c] = val;\n                }\n            }\n  \
        \      }\n        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) dp[i][j]\
        \ = next_dp[i][j];\n    }\n\n    free(min_at_val);\n    return dp[m-1][n-1];\n\
        }"
      csharp: "public class Solution {\n    public int MinCost(int[][] grid, int k)\
        \ {\n        int m = grid.Length, n = grid[0].Length;\n        int INF = 1000000000;\n\
        \        int[,] dp = new int[m, n];\n        for (int i = 0; i < m; i++) for\
        \ (int j = 0; j < n; j++) dp[i, j] = INF;\n        dp[0, 0] = 0;\n\n       \
        \ for (int p = 0; p <= k; p++) {\n            int[,] next_dp = new int[m, n];\n\
        \            for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) next_dp[i,\
        \ j] = INF;\n            if (p == 0) {\n                next_dp[0, 0] = 0;\n\
        \            } else {\n                int[] minAtVal = new int[10001];\n  \
        \              for (int v = 0; v <= 10000; v++) minAtVal[v] = INF;\n       \
        \         for (int r = 0; r < m; r++) {\n                    for (int c = 0;\
        \ c < n; c++) {\n                        if (dp[r, c] < INF) {\n           \
        \                 minAtVal[grid[r][c]] = Math.Min(minAtVal[grid[r][c]], dp[r,\
        \ c]);\n                        }\n                    }\n                }\n\
        \                int suffixMin = INF;\n                for (int v = 10000; v\
        \ >= 0; v--) {\n                    suffixMin = Math.Min(suffixMin, minAtVal[v]);\n\
        \                    minAtVal[v] = suffixMin;\n                }\n         \
        \       for (int r = 0; r < m; r++) {\n                    for (int c = 0; c\
        \ < n; c++) {\n                        next_dp[r, c] = minAtVal[grid[r][c]];\n\
        \                    }\n                }\n            }\n            for (int\
        \ r = 0; r < m; r++) {\n                for (int c = 0; c < n; c++) {\n    \
        \                if (r > 0) next_dp[r, c] = Math.Min(next_dp[r, c], next_dp[r\
        \ - 1, c] + grid[r][c]);\n                    if (c > 0) next_dp[r, c] = Math.Min(next_dp[r,\
        \ c], next_dp[r, c - 1] + grid[r][c]);\n                }\n            }\n \
        \           dp = next_dp;\n        }\n        return dp[m - 1, n - 1];\n   \
        \ }\n}"
      javascript: "var minCost = function(grid, k) {\n    const m = grid.length, n =\
        \ grid[0].length;\n    const INF = 1e9;\n    let dp = Array.from({ length: m\
        \ }, () => Array(n).fill(INF));\n    dp[0][0] = 0;\n\n    for (let p = 0; p\
        \ <= k; p++) {\n        let nextDp = Array.from({ length: m }, () => Array(n).fill(INF));\n\
        \        if (p === 0) {\n            nextDp[0][0] = 0;\n        } else {\n \
        \           let minAtVal = new Array(10001).fill(INF);\n            for (let\
        \ r = 0; r < m; r++) {\n                for (let c = 0; c < n; c++) {\n    \
        \                if (dp[r][c] < INF) {\n                        minAtVal[grid[r][c]]\
        \ = Math.min(minAtVal[grid[r][c]], dp[r][c]);\n                    }\n     \
        \           }\n            }\n            let suffixMin = INF;\n           \
        \ for (let v = 10000; v >= 0; v--) {\n                suffixMin = Math.min(suffixMin,\
        \ minAtVal[v]);\n                minAtVal[v] = suffixMin;\n            }\n \
        \           for (let r = 0; r < m; r++) {\n                for (let c = 0; c\
        \ < n; c++) {\n                    nextDp[r][c] = minAtVal[grid[r][c]];\n  \
        \              }\n            }\n        }\n        for (let r = 0; r < m; r++)\
        \ {\n            for (let c = 0; c < n; c++) {\n                if (r > 0) nextDp[r][c]\
        \ = Math.min(nextDp[r][c], nextDp[r - 1][c] + grid[r][c]);\n               \
        \ if (c > 0) nextDp[r][c] = Math.min(nextDp[r][c], nextDp[r][c - 1] + grid[r][c]);\n\
        \            }\n        }\n        dp = nextDp;\n    }\n    return dp[m - 1][n\
        \ - 1];\n};"
      typescript: "function minCost(grid: number[][], k: number): number {\n    const\
        \ m = grid.length;\n    const n = grid[0].length;\n    const INF = 1000000000;\n\
        \    let dp: number[][] = Array.from({ length: m }, () => Array(n).fill(INF));\n\
        \n    dp[0][0] = 0;\n    for (let i = 0; i < m; i++) {\n        for (let j =\
        \ 0; j < n; j++) {\n            if (i > 0) dp[i][j] = Math.min(dp[i][j], dp[i\
        \ - 1][j] + grid[i][j]);\n            if (j > 0) dp[i][j] = Math.min(dp[i][j],\
        \ dp[i][j - 1] + grid[i][j]);\n        }\n    }\n\n    for (let t = 0; t < k;\
        \ t++) {\n        let nextDp = dp.map(row => [...row]);\n        let minAtVal\
        \ = new Array(10001).fill(INF);\n        for (let i = 0; i < m; i++) {\n   \
        \         for (let j = 0; j < n; j++) {\n                if (dp[i][j] < minAtVal[grid[i][j]])\
        \ {\n                    minAtVal[grid[i][j]] = dp[i][j];\n                }\n\
        \            }\n        }\n\n        let suffixMin = new Array(10001).fill(INF);\n\
        \        suffixMin[10000] = minAtVal[10000];\n        for (let v = 9999; v >=\
        \ 0; v--) {\n            suffixMin[v] = Math.min(minAtVal[v], suffixMin[v +\
        \ 1]);\n        }\n\n        for (let i = 0; i < m; i++) {\n            for\
        \ (let j = 0; j < n; j++) {\n                if (suffixMin[grid[i][j]] < nextDp[i][j])\
        \ {\n                    nextDp[i][j] = suffixMin[grid[i][j]];\n           \
        \     }\n            }\n        }\n\n        for (let i = 0; i < m; i++) {\n\
        \            for (let j = 0; j < n; j++) {\n                if (i > 0) nextDp[i][j]\
        \ = Math.min(nextDp[i][j], nextDp[i - 1][j] + grid[i][j]);\n               \
        \ if (j > 0) nextDp[i][j] = Math.min(nextDp[i][j], nextDp[i][j - 1] + grid[i][j]);\n\
        \            }\n        }\n        dp = nextDp;\n    }\n\n    return dp[m -\
        \ 1][n - 1];\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @param\
        \ Integer $k\n     * @return Integer\n     */\n    function minCost($grid, $k)\
        \ {\n        $m = count($grid);\n        $n = count($grid[0]);\n        $INF\
        \ = 1000000000;\n        $dp = [];\n        for ($i = 0; $i < $m; $i++) {\n\
        \            $dp[$i] = array_fill(0, $n, $INF);\n        }\n\n        $dp[0][0]\
        \ = 0;\n        for ($i = 0; $i < $m; $i++) {\n            for ($j = 0; $j <\
        \ $n; $j++) {\n                if ($i > 0) $dp[$i][$j] = min($dp[$i][$j], $dp[$i\
        \ - 1][$j] + $grid[$i][$j]);\n                if ($j > 0) $dp[$i][$j] = min($dp[$i][$j],\
        \ $dp[$i][$j - 1] + $grid[$i][$j]);\n            }\n        }\n\n        for\
        \ ($t = 0; $t < $k; $t++) {\n            $nextDp = $dp;\n            $minAtVal\
        \ = array_fill(0, 10001, $INF);\n            for ($i = 0; $i < $m; $i++) {\n\
        \                for ($j = 0; $j < $n; $j++) {\n                    if ($dp[$i][$j]\
        \ < $minAtVal[$grid[$i][$j]]) {\n                        $minAtVal[$grid[$i][$j]]\
        \ = $dp[$i][$j];\n                    }\n                }\n            }\n\n\
        \            $suffixMin = array_fill(0, 10001, $INF);\n            $suffixMin[10000]\
        \ = $minAtVal[10000];\n            for ($v = 9999; $v >= 0; $v--) {\n      \
        \          $suffixMin[$v] = min($minAtVal[$v], $suffixMin[$v + 1]);\n      \
        \      }\n\n            for ($i = 0; $i < $m; $i++) {\n                for ($j\
        \ = 0; $j < $n; $j++) {\n                    if ($suffixMin[$grid[$i][$j]] <\
        \ $nextDp[$i][$j]) {\n                        $nextDp[$i][$j] = $suffixMin[$grid[$i][$j]];\n\
        \                    }\n                }\n            }\n\n            for\
        \ ($i = 0; $i < $m; $i++) {\n                for ($j = 0; $j < $n; $j++) {\n\
        \                    if ($i > 0) $nextDp[$i][$j] = min($nextDp[$i][$j], $nextDp[$i\
        \ - 1][$j] + $grid[$i][$j]);\n                    if ($j > 0) $nextDp[$i][$j]\
        \ = min($nextDp[$i][$j], $nextDp[$i][$j - 1] + $grid[$i][$j]);\n           \
        \     }\n            }\n            $dp = $nextDp;\n        }\n\n        return\
        \ $dp[$m - 1][$n - 1];\n    }\n}"
      swift: "class Solution {\n    func minCost(_ grid: [[Int]], _ k: Int) -> Int {\n\
        \        let m = grid.count\n        let n = grid[0].count\n        let INF\
        \ = 1_000_000_000\n        var dp = Array(repeating: Array(repeating: INF, count:\
        \ n), count: m)\n\n        dp[0][0] = 0\n        for i in 0..<m {\n        \
        \    for j in 0..<n {\n                if i > 0 { dp[i][j] = min(dp[i][j], dp[i-1][j]\
        \ + grid[i][j]) }\n                if j > 0 { dp[i][j] = min(dp[i][j], dp[i][j-1]\
        \ + grid[i][j]) }\n            }\n        }\n\n        for _ in 0..<k {\n  \
        \          var nextDp = dp\n            var minAtVal = Array(repeating: INF,\
        \ count: 10001)\n            for i in 0..<m {\n                for j in 0..<n\
        \ {\n                    minAtVal[grid[i][j]] = min(minAtVal[grid[i][j]], dp[i][j])\n\
        \                }\n            }\n\n            var suffixMin = Array(repeating:\
        \ INF, count: 10001)\n            suffixMin[10000] = minAtVal[10000]\n     \
        \       for v in stride(from: 9999, through: 0, by: -1) {\n                suffixMin[v]\
        \ = min(minAtVal[v], suffixMin[v+1])\n            }\n\n            for i in\
        \ 0..<m {\n                for j in 0..<n {\n                    nextDp[i][j]\
        \ = min(nextDp[i][j], suffixMin[grid[i][j]])\n                }\n          \
        \  }\n\n            for i in 0..<m {\n                for j in 0..<n {\n   \
        \                 if i > 0 { nextDp[i][j] = min(nextDp[i][j], nextDp[i-1][j]\
        \ + grid[i][j]) }\n                    if j > 0 { nextDp[i][j] = min(nextDp[i][j],\
        \ nextDp[i][j-1] + grid[i][j]) }\n                }\n            }\n       \
        \     dp = nextDp\n        }\n\n        return dp[m - 1][n - 1]\n    }\n}"
      kotlin: "class Solution {\n    fun minCost(grid: Array<IntArray>, k: Int): Int\
        \ {\n        val m = grid.size\n        val n = grid[0].size\n        val INF\
        \ = 1000000000\n        var dp = Array(m) { IntArray(n) { INF } }\n\n      \
        \  dp[0][0] = 0\n        for (i in 0 until m) {\n            for (j in 0 until\
        \ n) {\n                if (i > 0) dp[i][j] = if (dp[i - 1][j] + grid[i][j]\
        \ < dp[i][j]) dp[i - 1][j] + grid[i][j] else dp[i][j]\n                if (j\
        \ > 0) dp[i][j] = if (dp[i][j - 1] + grid[i][j] < dp[i][j]) dp[i][j - 1] + grid[i][j]\
        \ else dp[i][j]\n            }\n        }\n\n        repeat(k) {\n         \
        \   val nextDp = Array(m) { dp[it].copyOf() }\n            val minAtVal = IntArray(10001)\
        \ { INF }\n            for (i in 0 until m) {\n                for (j in 0 until\
        \ n) {\n                    if (dp[i][j] < minAtVal[grid[i][j]]) {\n       \
        \                 minAtVal[grid[i][j]] = dp[i][j]\n                    }\n \
        \               }\n            }\n\n            val suffixMin = IntArray(10001)\n\
        \            suffixMin[10000] = minAtVal[10000]\n            for (v in 9999\
        \ downTo 0) {\n                suffixMin[v] = if (minAtVal[v] < suffixMin[v\
        \ + 1]) minAtVal[v] else suffixMin[v + 1]\n            }\n\n            for\
        \ (i in 0 until m) {\n                for (j in 0 until n) {\n             \
        \       if (suffixMin[grid[i][j]] < nextDp[i][j]) {\n                      \
        \  nextDp[i][j] = suffixMin[grid[i][j]]\n                    }\n           \
        \     }\n            }\n\n            for (i in 0 until m) {\n             \
        \   for (j in 0 until n) {\n                    if (i > 0) nextDp[i][j] = if\
        \ (nextDp[i - 1][j] + grid[i][j] < nextDp[i][j]) nextDp[i - 1][j] + grid[i][j]\
        \ else nextDp[i][j]\n                    if (j > 0) nextDp[i][j] = if (nextDp[i][j\
        \ - 1] + grid[i][j] < nextDp[i][j]) nextDp[i][j - 1] + grid[i][j] else nextDp[i][j]\n\
        \                }\n            }\n            dp = nextDp\n        }\n\n  \
        \      return dp[m - 1][n - 1]\n    }\n}"
      dart: "class Solution {\n  int minCost(List<List<int>> grid, int k) {\n    int\
        \ m = grid.length;\n    int n = grid[0].length;\n    int INF = 1000000000;\n\
        \    List<List<int>> dp = List.generate(m, (_) => List.filled(n, INF));\n\n\
        \    dp[0][0] = 0;\n    for (int i = 0; i < m; i++) {\n      for (int j = 0;\
        \ j < n; j++) {\n        if (i > 0) dp[i][j] = (dp[i - 1][j] + grid[i][j] <\
        \ dp[i][j]) ? dp[i - 1][j] + grid[i][j] : dp[i][j];\n        if (j > 0) dp[i][j]\
        \ = (dp[i][j - 1] + grid[i][j] < dp[i][j]) ? dp[i][j - 1] + grid[i][j] : dp[i][j];\n\
        \      }\n    }\n\n    for (int t = 0; t < k; t++) {\n      List<List<int>>\
        \ nextDp = List.generate(m, (i) => List<int>.from(dp[i]));\n      List<int>\
        \ minAtVal = List.filled(10001, INF);\n      for (int i = 0; i < m; i++) {\n\
        \        for (int j = 0; j < n; j++) {\n          if (dp[i][j] < minAtVal[grid[i][j]])\
        \ {\n            minAtVal[grid[i][j]] = dp[i][j];\n          }\n        }\n\
        \      }\n\n      List<int> suffixMin = List.filled(10001, INF);\n      suffixMin[10000]\
        \ = minAtVal[10000];\n      for (int v = 9999; v >= 0; v--) {\n        suffixMin[v]\
        \ = (minAtVal[v] < suffixMin[v + 1]) ? minAtVal[v] : suffixMin[v + 1];\n   \
        \   }\n\n      for (int i = 0; i < m; i++) {\n        for (int j = 0; j < n;\
        \ j++) {\n          if (suffixMin[grid[i][j]] < nextDp[i][j]) {\n          \
        \  nextDp[i][j] = suffixMin[grid[i][j]];\n          }\n        }\n      }\n\n\
        \      for (int i = 0; i < m; i++) {\n        for (int j = 0; j < n; j++) {\n\
        \          if (i > 0) nextDp[i][j] = (nextDp[i - 1][j] + grid[i][j] < nextDp[i][j])\
        \ ? nextDp[i - 1][j] + grid[i][j] : nextDp[i][j];\n          if (j > 0) nextDp[i][j]\
        \ = (nextDp[i][j - 1] + grid[i][j] < nextDp[i][j]) ? nextDp[i][j - 1] + grid[i][j]\
        \ : nextDp[i][j];\n        }\n      }\n      dp = nextDp;\n    }\n\n    return\
        \ dp[m - 1][n - 1];\n  }\n}"
      go: "func minCost(grid [][]int, k int) int {\n\tm := len(grid)\n\tn := len(grid[0])\n\
        \tINF := 1000000000\n\n\tdp := make([][]int, m)\n\tfor i := 0; i < m; i++ {\n\
        \t\tdp[i] = make([]int, n)\n\t\tfor j := 0; j < n; j++ {\n\t\t\tdp[i][j] = INF\n\
        \t\t}\n\t}\n\n\tdp[0][0] = 0\n\tfor i := 0; i < m; i++ {\n\t\tfor j := 0; j\
        \ < n; j++ {\n\t\t\tif i > 0 && dp[i-1][j]+grid[i][j] < dp[i][j] {\n\t\t\t\t\
        dp[i][j] = dp[i-1][j] + grid[i][j]\n\t\t\t}\n\t\t\tif j > 0 && dp[i][j-1]+grid[i][j]\
        \ < dp[i][j] {\n\t\t\t\tdp[i][j] = dp[i][j-1] + grid[i][j]\n\t\t\t}\n\t\t}\n\
        \t}\n\n\tfor t := 0; t < k; t++ {\n\t\tnextDp := make([][]int, m)\n\t\tminAtVal\
        \ := make([]int, 10001)\n\t\tfor i := 0; i < 10001; i++ {\n\t\t\tminAtVal[i]\
        \ = INF\n\t\t}\n\n\t\tfor i := 0; i < m; i++ {\n\t\t\tnextDp[i] = make([]int,\
        \ n)\n\t\t\tcopy(nextDp[i], dp[i])\n\t\t\tfor j := 0; j < n; j++ {\n\t\t\t\t\
        if dp[i][j] < minAtVal[grid[i][j]] {\n\t\t\t\t\tminAtVal[grid[i][j]] = dp[i][j]\n\
        \t\t\t\t}\n\t\t\t}\n\t\t}\n\n\t\tsuffixMin := make([]int, 10001)\n\t\tsuffixMin[10000]\
        \ = minAtVal[10000]\n\t\tfor v := 9999; v >= 0; v-- {\n\t\t\tsuffixMin[v] =\
        \ minAtVal[v]\n\t\t\tif suffixMin[v+1] < suffixMin[v] {\n\t\t\t\tsuffixMin[v]\
        \ = suffixMin[v+1]\n\t\t\t}\n\t\t}\n\n\t\tfor i := 0; i < m; i++ {\n\t\t\tfor\
        \ j := 0; j < n; j++ {\n\t\t\t\tif suffixMin[grid[i][j]] < nextDp[i][j] {\n\t\
        \t\t\t\tnextDp[i][j] = suffixMin[grid[i][j]]\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\n\t\
        \tfor i := 0; i < m; i++ {\n\t\t\tfor j := 0; j < n; j++ {\n\t\t\t\tif i > 0\
        \ && nextDp[i-1][j]+grid[i][j] < nextDp[i][j] {\n\t\t\t\t\tnextDp[i][j] = nextDp[i-1][j]\
        \ + grid[i][j]\n\t\t\t\t}\n\t\t\t\tif j > 0 && nextDp[i][j-1]+grid[i][j] < nextDp[i][j]\
        \ {\n\t\t\t\t\tnextDp[i][j] = nextDp[i][j-1] + grid[i][j]\n\t\t\t\t}\n\t\t\t\
        }\n\t\t}\n\t\tdp = nextDp\n\t}\n\n\treturn dp[m-1][n-1]\n}"
      ruby: "def min_cost(grid, k)\n  m, n = grid.length, grid[0].length\n  inf = 1_000_000_000\n\
        \  dp = Array.new(k + 1) { Array.new(m) { Array.new(n, inf) } }\n  dp[0][0][0]\
        \ = 0\n\n  (0..k).each do |p|\n    if p > 0\n      min_at_val = Array.new(10001,\
        \ inf)\n      (0...m).each do |i|\n        (0...n).each do |j|\n          v\
        \ = grid[i][j]\n          min_at_val[v] = [min_at_val[v], dp[p - 1][i][j]].min\n\
        \        end\n      end\n      suffix_min = Array.new(10002, inf)\n      10000.downto(0)\
        \ do |v|\n        suffix_min[v] = [suffix_min[v + 1], min_at_val[v]].min\n \
        \     end\n      (0...m).each do |i|\n        (0...n).each do |j|\n        \
        \  v = grid[i][j]\n          dp[p][i][j] = [dp[p][i][j], suffix_min[v]].min\n\
        \        end\n      end\n    end\n    (0...m).each do |i|\n      (0...n).each\
        \ do |j|\n        dp[p][i][j] = [dp[p][i][j], dp[p][i - 1][j] + grid[i][j]].min\
        \ if i > 0\n        dp[p][i][j] = [dp[p][i][j], dp[p][i][j - 1] + grid[i][j]].min\
        \ if j > 0\n      end\n    end\n  end\n\n  ans = inf\n  (0..k).each { |p| ans\
        \ = [ans, dp[p][m - 1][n - 1]].min }\n  ans\nend"
      scala: "object Solution {\n  def minCost(grid: Array[Array[Int]], k: Int): Int\
        \ = {\n    val m = grid.length\n    val n = grid(0).length\n    val inf = 1000000000\n\
        \    val dp = Array.fill(k + 1, m, n)(inf)\n\n    dp(0)(0)(0) = 0\n\n    for\
        \ (p <- 0 to k) {\n      if (p > 0) {\n        val minAtVal = Array.fill(10001)(inf)\n\
        \        for (i <- 0 until m; j <- 0 until n) {\n          val v = grid(i)(j)\n\
        \          if (dp(p - 1)(i)(j) < minAtVal(v)) minAtVal(v) = dp(p - 1)(i)(j)\n\
        \        }\n        val suffixMin = Array.fill(10002)(inf)\n        for (v <-\
        \ 10000 to 0 by -1) {\n          suffixMin(v) = Math.min(suffixMin(v + 1), minAtVal(v))\n\
        \        }\n        for (i <- 0 until m; j <- 0 until n) {\n          dp(p)(i)(j)\
        \ = Math.min(dp(p)(i)(j), suffixMin(grid(i)(j)))\n        }\n      }\n     \
        \ for (i <- 0 until m; j <- 0 until n) {\n        if (i > 0) dp(p)(i)(j) = Math.min(dp(p)(i)(j),\
        \ dp(p)(i - 1)(j) + grid(i)(j))\n        if (j > 0) dp(p)(i)(j) = Math.min(dp(p)(i)(j),\
        \ dp(p)(i)(j - 1) + grid(i)(j))\n      }\n    }\n\n    var ans = inf\n    for\
        \ (p <- 0 to k) ans = Math.min(ans, dp(p)(m - 1)(n - 1))\n    ans\n  }\n}"
      rust: "impl Solution {\n    pub fn min_cost(grid: Vec<Vec<i32>>, k: i32) -> i32\
        \ {\n        let m = grid.len();\n        let n = grid[0].len();\n        let\
        \ k = k as usize;\n        let inf = 1_000_000_000i32;\n        let mut dp =\
        \ vec![vec![vec![inf; n]; m]; k + 1];\n        dp[0][0][0] = 0;\n        for\
        \ p in 0..=k {\n            if p > 0 {\n                let mut min_at_val =\
        \ vec![inf; 10001];\n                for i in 0..m {\n                    for\
        \ j in 0..n {\n                        let v = grid[i][j] as usize;\n      \
        \                  min_at_val[v] = min_at_val[v].min(dp[p - 1][i][j]);\n   \
        \                 }\n                }\n                let mut suffix_min =\
        \ vec![inf; 10002];\n                for v in (0..=10000).rev() {\n        \
        \            suffix_min[v] = suffix_min[v + 1].min(min_at_val[v]);\n       \
        \         }\n                for i in 0..m {\n                    for j in 0..n\
        \ {\n                        let v = grid[i][j] as usize;\n                \
        \        dp[p][i][j] = dp[p][i][j].min(suffix_min[v]);\n                   \
        \ }\n                }\n            }\n            for i in 0..m {\n       \
        \         for j in 0..n {\n                    let v = grid[i][j];\n       \
        \             if i > 0 {\n                        dp[p][i][j] = dp[p][i][j].min(dp[p][i\
        \ - 1][j] + v);\n                    }\n                    if j > 0 {\n   \
        \                     dp[p][i][j] = dp[p][i][j].min(dp[p][i][j - 1] + v);\n\
        \                    }\n                }\n            }\n        }\n      \
        \  let mut ans = inf;\n        for p in 0..=k {\n            ans = ans.min(dp[p][m\
        \ - 1][n - 1]);\n        }\n        ans\n    }\n}"
      racket: "(define/contract (min-cost grid k)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer? exact-integer?)\n  (let* ([m (length grid)]\n         [n (length\
        \ (first grid))]\n         [grid-vec (list->vector (map list->vector grid))]\n\
        \         [inf 1000000000]\n         [dp (make-vector (+ k 1))])\n    (for ([p\
        \ (in-range (+ k 1))])\n      (vector-set! dp p (make-vector m))\n      (for\
        \ ([i (in-range m)])\n        (vector-set! (vector-ref dp p) i (make-vector\
        \ n inf))))\n    (vector-set! (vector-ref (vector-ref dp 0) 0) 0 0)\n    (for\
        \ ([p (in-range (+ k 1))])\n      (when (> p 0)\n        (let ([min-at-val (make-vector\
        \ 10001 inf)])\n          (for ([i (in-range m)])\n            (for ([j (in-range\
        \ n)])\n              (let ([v (vector-ref (vector-ref grid-vec i) j)]\n   \
        \                 [cost (vector-ref (vector-ref (vector-ref dp (- p 1)) i) j)])\n\
        \                (vector-set! min-at-val v (min (vector-ref min-at-val v) cost)))))\n\
        \          (let ([suffix-min (make-vector 10002 inf)])\n            (for ([v\
        \ (in-range 10000 -1 -1)])\n              (vector-set! suffix-min v (min (vector-ref\
        \ suffix-min (+ v 1)) (vector-ref min-at-val v))))\n            (for ([i (in-range\
        \ m)])\n              (for ([j (in-range n)])\n                (let ([v (vector-ref\
        \ (vector-ref grid-vec i) j)])\n                  (vector-set! (vector-ref (vector-ref\
        \ dp p) i) j (vector-ref suffix-min v))))))))\n      (let ([curr-dp-p (vector-ref\
        \ dp p)])\n        (for ([i (in-range m)])\n          (let ([curr-row (vector-ref\
        \ curr-dp-p i)]\n                [row-grid (vector-ref grid-vec i)]\n      \
        \          [prev-row (if (> i 0) (vector-ref curr-dp-p (- i 1)) #f)])\n    \
        \        (for ([j (in-range n)])\n              (let* ([v (vector-ref row-grid\
        \ j)]\n                     [current (vector-ref curr-row j)]\n            \
        \         [v1 (if prev-row (+ (vector-ref prev-row j) v) inf)]\n           \
        \          [v2 (if (> j 0) (+ (vector-ref curr-row (- j 1)) v) inf)])\n    \
        \            (vector-set! curr-row j (min current v1 v2))))))))\n    (let ([ans\
        \ inf])\n      (for ([p (in-range (+ k 1))])\n        (set! ans (min ans (vector-ref\
        \ (vector-ref (vector-ref dp p) (- m 1)) (- n 1)))))\n      ans)))"
      erlang: "min_cost(Grid, K) ->\n  M = length(Grid),\n  N = length(hd(Grid)),\n\
        \  GridArray = array:from_list([array:from_list(Row) || Row <- Grid]),\n  Inf\
        \ = 1000000000,\n  InitialDP = array:from_list([\n    if I == 0 -> array:set(0,\
        \ 0, array:new(N, {default, Inf}));\n       true -> array:new(N, {default, Inf})\n\
        \    end || I <- lists:seq(0, M-1)\n  ]),\n  DP0 = update_grid_dp(InitialDP,\
        \ GridArray, M, N, Inf),\n  FinalDPs = lists:foldl(fn(_, AccDPs) ->\n    PrevDP\
        \ = hd(AccDPs),\n    MinAtVal0 = array:new(10001, {default, Inf}),\n    MinAtVal\
        \ = lists:foldl(fn(I, AccV) ->\n      Row = array:get(I, PrevDP),\n      RowGrid\
        \ = array:get(I, GridArray),\n      lists:foldl(fn(J, AccV2) ->\n        V =\
        \ array:get(J, RowGrid),\n        array:set(V, erlang:min(array:get(V, AccV2),\
        \ array:get(J, Row)), AccV2)\n      end, AccV, lists:seq(0, N-1))\n    end,\
        \ MinAtVal0, lists:seq(0, M-1)),\n    SuffixMin0 = array:new(10002, {default,\
        \ Inf}),\n    SuffixMin = lists:foldl(fn(V, AccS) ->\n      array:set(V, erlang:min(array:get(V+1,\
        \ AccS), array:get(V, MinAtVal)), AccS)\n    end, SuffixMin0, lists:seq(10000,\
        \ 0, -1)),\n    TeleportDP = array:from_list([\n      array:from_list([\n  \
        \      array:get(array:get(J, array:get(I, GridArray)), SuffixMin)\n      ||\
        \ J <- lists:seq(0, N-1)])\n    || I <- lists:seq(0, M-1)]),\n    [update_grid_dp(TeleportDP,\
        \ GridArray, M, N, Inf) | AccDPs]\n  end, [DP0], if K > 0 -> lists:seq(1, K);\
        \ true -> [] end),\n  lists:min([array:get(N-1, array:get(M-1, D)) || D <- FinalDPs]).\n\
        \nupdate_grid_dp(DP, GridArray, M, N, Inf) ->\n  lists:foldl(fn(I, AccDP) ->\n\
        \    RowGrid = array:get(I, GridArray),\n    RowDP = array:get(I, AccDP),\n\
        \    PrevRowDP = if I > 0 -> array:get(I-1, AccDP); true -> undefined end,\n\
        \    NewRowDP = lists:foldl(fn(J, AccRow) ->\n      V = array:get(J, RowGrid),\n\
        \      V1 = if PrevRowDP /= undefined -> array:get(J, PrevRowDP) + V; true ->\
        \ Inf end,\n      V2 = if J > 0 -> array:get(J-1, AccRow) + V; true -> Inf end,\n\
        \      array:set(J, erlang:min(array:get(J, AccRow), erlang:min(V1, V2)), AccRow)\n\
        \    end, RowDP, lists:seq(0, N-1)),\n    array:set(I, NewRowDP, AccDP)\n  end,\
        \ DP, lists:seq(0, M-1))."
      elixir: "defmodule Solution do\n  @spec min_cost(grid :: [[integer]], k :: integer)\
        \ :: integer\n  def min_cost(grid_list, k) do\n    grid = grid_list |> Enum.map(&List.to_tuple/1)\
        \ |> List.to_tuple()\n    m = tuple_size(grid)\n    n = tuple_size(elem(grid,\
        \ 0))\n    inf = 1_000_000_000\n    dp0_initial = for i <- 0..(m-1) do\n   \
        \   if i == 0, do: put_elem(Tuple.duplicate(inf, n), 0, 0), else: Tuple.duplicate(inf,\
        \ n)\n    end |> List.to_tuple()\n    dp0 = update_grid_dp(dp0_initial, grid,\
        \ m, n, inf)\n    ranges = if k > 0, do: 1..k, else: []\n    {_last_dp, ans_list}\
        \ = Enum.reduce(ranges, {dp0, [elem(elem(dp0, m-1), n-1)]}, fn _, {prev_dp,\
        \ acc_ans} ->\n      min_at_val = Enum.reduce(0..(m-1), %{}, fn i, acc_i ->\n\
        \        row_dp = elem(prev_dp, i)\n        row_grid = elem(grid, i)\n     \
        \   Enum.reduce(0..(n-1), acc_i, fn j, acc_j ->\n          v = elem(row_grid,\
        \ j)\n          Map.update(acc_j, v, elem(row_dp, j), &min(&1, elem(row_dp,\
        \ j)))\n        end)\n      end)\n      {_, suffix_min} = Enum.reduce(10000..0,\
        \ {inf, %{}}, fn v, {curr_min, acc_s} ->\n        new_min = min(curr_min, Map.get(min_at_val,\
        \ v, inf))\n        {new_min, Map.put(acc_s, v, new_min)}\n      end)\n    \
        \  teleport_dp = (for i <- 0..(m-1) do\n        row_grid = elem(grid, i)\n \
        \       (for j <- 0..(n-1) do Map.get(suffix_min, elem(row_grid, j), inf) end)\
        \ |> List.to_tuple()\n      end) |> List.to_tuple()\n      new_dp = update_grid_dp(teleport_dp,\
        \ grid, m, n, inf)\n      {new_dp, [elem(elem(new_dp, m-1), n-1) | acc_ans]}\n\
        \    end)\n    Enum.min(ans_list)\n  end\n  defp update_grid_dp(dp, grid, m,\
        \ n, inf) do\n    Enum.reduce(0..(m-1), dp, fn i, acc_dp ->\n      row_grid\
        \ = elem(grid, i)\n      prev_row = if i > 0, do: elem(acc_dp, i-1), else: nil\n\
        \      new_row = Enum.reduce(0..(n-1), elem(acc_dp, i), fn j, acc_row ->\n \
        \       v = elem(row_grid, j)\n        v1 = if prev_row, do: elem(prev_row,\
        \ j) + v, else: inf\n        v2 = if j > 0, do: elem(acc_row, j-1) + v, else:\
        \ inf\n        put_elem(acc_row, j, min(elem(acc_row, j), min(v1, v2)))\n  \
        \    end)\n      put_elem(acc_dp, i, new_row)\n    end)\n  end\nend"
    approach: 'The problem is solved using dynamic programming with k teleportation
      stages. We maintain a DP table where dp[i][j] represents the minimum cost to reach
      cell (i, j) with at most p teleports. For each stage p from 0 to k, we first handle
      the teleportation option: a teleport can occur from any cell (r, c) to (i, j)
      if grid[i, j] <= grid[r, c], incurring a cost of 0. To efficiently calculate this,
      we use a suffix minimum array where suffix_min[v] stores the minimum cost from
      the previous stage p-1 among all cells with grid values at least v. This allows
      us to initialize the costs for stage p in O(MN + V) time, where V is the range
      of grid values.'
    time_complexity: O(k * (m * n + V)), where m and n are the grid dimensions, k is
      the maximum number of teleports, and V is the maximum grid value (10,000). The
      outer loop runs k+1 times, and each iteration performs a suffix minimum precomputation
      (O(V)), a teleportation update (O(m * n)), and a standard grid DP (O(m * n)).
    space_complexity: O(m * n + V) to store the DP table (only two stages are needed)
      and the suffix minimum array. Given the constraints m, n <= 80 and V <= 10,000,
      this fits well within memory limits.
    elapsed_time: 452.4124038219452
    model: gemini-3-flash-preview
    generated_at: '2026-01-28 01:18:06 '
---

## Problem #3651: Minimum Cost Path with Teleportations

**Difficulty:** Hard

**Topics:** Array, Dynamic Programming, Matrix

## Problem Description

<p>You are given a <code>m x n</code> 2D integer array <code>grid</code> and an integer <code>k</code>. You start at the top-left cell <code>(0, 0)</code> and your goal is to reach the bottom‐right cell <code>(m - 1, n - 1)</code>.</p>

<p>There are two types of moves available:</p>

<ul>
	<li>
	<p><strong>Normal move</strong>: You can move right or down from your current cell <code>(i, j)</code>, i.e. you can move to <code>(i, j + 1)</code> (right) or <code>(i + 1, j)</code> (down). The cost is the value of the destination cell.</p>
	</li>
	<li>
	<p><strong>Teleportation</strong>: You can teleport from any cell <code>(i, j)</code>, to any cell <code>(x, y)</code> such that <code>grid[x][y] &lt;= grid[i][j]</code>; the cost of this move is 0. You may teleport at most <code>k</code> times.</p>
	</li>
</ul>

<p>Return the <strong>minimum</strong> total cost to reach cell <code>(m - 1, n - 1)</code> from <code>(0, 0)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,3,3],[2,5,4],[4,3,5]], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<p>Initially we are at (0, 0) and cost is 0.</p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Current Position</th>
			<th style="border: 1px solid black;">Move</th>
			<th style="border: 1px solid black;">New Position</th>
			<th style="border: 1px solid black;">Total Cost</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>(0, 0)</code></td>
			<td style="border: 1px solid black;">Move Down</td>
			<td style="border: 1px solid black;"><code>(1, 0)</code></td>
			<td style="border: 1px solid black;"><code>0 + 2 = 2</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>(1, 0)</code></td>
			<td style="border: 1px solid black;">Move Right</td>
			<td style="border: 1px solid black;"><code>(1, 1)</code></td>
			<td style="border: 1px solid black;"><code>2 + 5 = 7</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>(1, 1)</code></td>
			<td style="border: 1px solid black;">Teleport to <code>(2, 2)</code></td>
			<td style="border: 1px solid black;"><code>(2, 2)</code></td>
			<td style="border: 1px solid black;"><code>7 + 0 = 7</code></td>
		</tr>
	</tbody>
</table>

<p>The minimum cost to reach bottom-right cell is 7.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,2],[2,3],[3,4]], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation: </strong></p>

<p>Initially we are at (0, 0) and cost is 0.</p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Current Position</th>
			<th style="border: 1px solid black;">Move</th>
			<th style="border: 1px solid black;">New Position</th>
			<th style="border: 1px solid black;">Total Cost</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>(0, 0)</code></td>
			<td style="border: 1px solid black;">Move Down</td>
			<td style="border: 1px solid black;"><code>(1, 0)</code></td>
			<td style="border: 1px solid black;"><code>0 + 2 = 2</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>(1, 0)</code></td>
			<td style="border: 1px solid black;">Move Right</td>
			<td style="border: 1px solid black;"><code>(1, 1)</code></td>
			<td style="border: 1px solid black;"><code>2 + 3 = 5</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>(1, 1)</code></td>
			<td style="border: 1px solid black;">Move Down</td>
			<td style="border: 1px solid black;"><code>(2, 1)</code></td>
			<td style="border: 1px solid black;"><code>5 + 4 = 9</code></td>
		</tr>
	</tbody>
</table>

<p>The minimum cost to reach bottom-right cell is 9.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= m, n &lt;= 80</code></li>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10</code></li>
</ul>


## Hints

1. Use dynamic programming to solve the problem efficiently.

2. Think of the solution in terms of up to `k` teleportation steps. At each step, compute the minimum cost to reach each cell, either through a normal move or a teleportation from the previous step.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem is solved using dynamic programming with k teleportation stages. We maintain a DP table where dp[i][j] represents the minimum cost to reach cell (i, j) with at most p teleports. For each stage p from 0 to k, we first handle the teleportation option: a teleport can occur from any cell (r, c) to (i, j) if grid[i, j] <= grid[r, c], incurring a cost of 0. To efficiently calculate this, we use a suffix minimum array where suffix_min[v] stores the minimum cost from the previous stage p-1 among all cells with grid values at least v. This allows us to initialize the costs for stage p in O(MN + V) time, where V is the range of grid values.

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
    int minCost(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        int INF = 1e9;
        vector<vector<int>> dp(m, vector<int>(n, INF));
        dp[0][0] = 0;

        for (int p = 0; p <= k; ++p) {
            vector<vector<int>> next_dp(m, vector<int>(n, INF));
            if (p == 0) {
                next_dp[0][0] = 0;
            } else {
                vector<int> min_at_val(10001, INF);
                for (int r = 0; r < m; ++r) {
                    for (int c = 0; c < n; ++c) {
                        if (dp[r][c] < INF) {
                            min_at_val[grid[r][c]] = min(min_at_val[grid[r][c]], dp[r][c]);
                        }
                    }
                }
                int suffix_min = INF;
                for (int v = 10000; v >= 0; --v) {
                    suffix_min = min(suffix_min, min_at_val[v]);
                    min_at_val[v] = suffix_min;
                }
                for (int r = 0; r < m; ++r) {
                    for (int c = 0; c < n; ++c) {
                        next_dp[r][c] = min_at_val[grid[r][c]];
                    }
                }
            }
            for (int r = 0; r < m; ++r) {
                for (int c = 0; c < n; ++c) {
                    if (r > 0) next_dp[r][c] = min(next_dp[r][c], next_dp[r - 1][c] + grid[r][c]);
                    if (c > 0) next_dp[r][c] = min(next_dp[r][c], next_dp[r][c - 1] + grid[r][c]);
                }
            }
            dp = next_dp;
        }

        int ans = INF;
        return dp[m - 1][n - 1];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minCost(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        int INF = 1000000000;
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) java.util.Arrays.fill(dp[i], INF);
        dp[0][0] = 0;

        for (int p = 0; p <= k; p++) {
            int[][] next_dp = new int[m][n];
            for (int i = 0; i < m; i++) java.util.Arrays.fill(next_dp[i], INF);
            if (p == 0) {
                next_dp[0][0] = 0;
            } else {
                int[] minAtVal = new int[10001];
                java.util.Arrays.fill(minAtVal, INF);
                for (int r = 0; r < m; r++) {
                    for (int c = 0; c < n; c++) {
                        if (dp[r][c] < INF) {
                            minAtVal[grid[r][c]] = Math.min(minAtVal[grid[r][c]], dp[r][c]);
                        }
                    }
                }
                int suffixMin = INF;
                for (int v = 10000; v >= 0; v--) {
                    suffixMin = Math.min(suffixMin, minAtVal[v]);
                    minAtVal[v] = suffixMin;
                }
                for (int r = 0; r < m; r++) {
                    for (int c = 0; c < n; c++) {
                        next_dp[r][c] = minAtVal[grid[r][c]];
                    }
                }
            }
            for (int r = 0; r < m; r++) {
                for (int c = 0; c < n; c++) {
                    if (r > 0) next_dp[r][c] = Math.min(next_dp[r][c], next_dp[r - 1][c] + grid[r][c]);
                    if (c > 0) next_dp[r][c] = Math.min(next_dp[r][c], next_dp[r][c - 1] + grid[r][c]);
                }
            }
            dp = next_dp;
        }
        return dp[m - 1][n - 1];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minCost(self, grid, k):
        m, n = len(grid), len(grid[0])
        INF = 10**9
        dp = [[INF] * n for _ in range(m)]
        dp[0][0] = 0

        for p in range(k + 1):
            next_dp = [[INF] * n for _ in range(m)]
            if p == 0:
                next_dp[0][0] = 0
            else:
                min_at_val = [INF] * 10001
                for r in range(m):
                    for c in range(n):
                        if dp[r][c] < INF:
                            v = grid[r][c]
                            if dp[r][c] < min_at_val[v]:
                                min_at_val[v] = dp[r][c]

                suffix_min = INF
                for v in range(10000, -1, -1):
                    if min_at_val[v] < suffix_min:
                        suffix_min = min_at_val[v]
                    min_at_val[v] = suffix_min

                for r in range(m):
                    for c in range(n):
                        next_dp[r][c] = min_at_val[grid[r][c]]

            for r in range(m):
                for c in range(n):
                    if r > 0:
                        if next_dp[r-1][c] + grid[r][c] < next_dp[r][c]:
                            next_dp[r][c] = next_dp[r-1][c] + grid[r][c]
                    if c > 0:
                        if next_dp[r][c-1] + grid[r][c] < next_dp[r][c]:
                            next_dp[r][c] = next_dp[r][c-1] + grid[r][c]
            dp = next_dp

        return dp[m-1][n-1]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**9
        dp = [[INF] * n for _ in range(m)]
        dp[0][0] = 0

        for p in range(k + 1):
            next_dp = [[INF] * n for _ in range(m)]
            if p == 0:
                next_dp[0][0] = 0
            else:
                min_at_val = [INF] * 10001
                for r in range(m):
                    for c in range(n):
                        if dp[r][c] < INF:
                            v = grid[r][c]
                            if dp[r][c] < min_at_val[v]:
                                min_at_val[v] = dp[r][c]

                suffix_min = INF
                for v in range(10000, -1, -1):
                    if min_at_val[v] < suffix_min:
                        suffix_min = min_at_val[v]
                    min_at_val[v] = suffix_min

                for r in range(m):
                    for c in range(n):
                        next_dp[r][c] = min_at_val[grid[r][c]]

            for r in range(m):
                for c in range(n):
                    if r > 0:
                        if next_dp[r-1][c] + grid[r][c] < next_dp[r][c]:
                            next_dp[r][c] = next_dp[r-1][c] + grid[r][c]
                    if c > 0:
                        if next_dp[r][c-1] + grid[r][c] < next_dp[r][c]:
                            next_dp[r][c] = next_dp[r][c-1] + grid[r][c]
            dp = next_dp

        return dp[m-1][n-1]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minCost(int** grid, int gridSize, int* gridColSize, int k) {
    int m = gridSize, n = gridColSize[0];
    int INF = 1000000000;
    int dp[80][80];
    int next_dp[80][80];

    for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) dp[i][j] = INF;
    dp[0][0] = 0;

    int* min_at_val = (int*)malloc(sizeof(int) * 10001);

    for (int p = 0; p <= k; p++) {
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) next_dp[i][j] = INF;
        if (p == 0) {
            next_dp[0][0] = 0;
        } else {
            for (int v = 0; v <= 10000; v++) min_at_val[v] = INF;
            for (int r = 0; r < m; r++) {
                for (int c = 0; c < n; c++) {
                    if (dp[r][c] < INF) {
                        if (dp[r][c] < min_at_val[grid[r][c]]) min_at_val[grid[r][c]] = dp[r][c];
                    }
                }
            }
            int suffix_min = INF;
            for (int v = 10000; v >= 0; v--) {
                if (min_at_val[v] < suffix_min) suffix_min = min_at_val[v];
                min_at_val[v] = suffix_min;
            }
            for (int r = 0; r < m; r++) {
                for (int c = 0; c < n; c++) {
                    next_dp[r][c] = min_at_val[grid[r][c]];
                }
            }
        }
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (r > 0) {
                    int val = next_dp[r-1][c] + grid[r][c];
                    if (val < next_dp[r][c]) next_dp[r][c] = val;
                }
                if (c > 0) {
                    int val = next_dp[r][c-1] + grid[r][c];
                    if (val < next_dp[r][c]) next_dp[r][c] = val;
                }
            }
        }
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) dp[i][j] = next_dp[i][j];
    }

    free(min_at_val);
    return dp[m-1][n-1];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinCost(int[][] grid, int k) {
        int m = grid.Length, n = grid[0].Length;
        int INF = 1000000000;
        int[,] dp = new int[m, n];
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) dp[i, j] = INF;
        dp[0, 0] = 0;

        for (int p = 0; p <= k; p++) {
            int[,] next_dp = new int[m, n];
            for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) next_dp[i, j] = INF;
            if (p == 0) {
                next_dp[0, 0] = 0;
            } else {
                int[] minAtVal = new int[10001];
                for (int v = 0; v <= 10000; v++) minAtVal[v] = INF;
                for (int r = 0; r < m; r++) {
                    for (int c = 0; c < n; c++) {
                        if (dp[r, c] < INF) {
                            minAtVal[grid[r][c]] = Math.Min(minAtVal[grid[r][c]], dp[r, c]);
                        }
                    }
                }
                int suffixMin = INF;
                for (int v = 10000; v >= 0; v--) {
                    suffixMin = Math.Min(suffixMin, minAtVal[v]);
                    minAtVal[v] = suffixMin;
                }
                for (int r = 0; r < m; r++) {
                    for (int c = 0; c < n; c++) {
                        next_dp[r, c] = minAtVal[grid[r][c]];
                    }
                }
            }
            for (int r = 0; r < m; r++) {
                for (int c = 0; c < n; c++) {
                    if (r > 0) next_dp[r, c] = Math.Min(next_dp[r, c], next_dp[r - 1, c] + grid[r][c]);
                    if (c > 0) next_dp[r, c] = Math.Min(next_dp[r, c], next_dp[r, c - 1] + grid[r][c]);
                }
            }
            dp = next_dp;
        }
        return dp[m - 1, n - 1];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var minCost = function(grid, k) {
    const m = grid.length, n = grid[0].length;
    const INF = 1e9;
    let dp = Array.from({ length: m }, () => Array(n).fill(INF));
    dp[0][0] = 0;

    for (let p = 0; p <= k; p++) {
        let nextDp = Array.from({ length: m }, () => Array(n).fill(INF));
        if (p === 0) {
            nextDp[0][0] = 0;
        } else {
            let minAtVal = new Array(10001).fill(INF);
            for (let r = 0; r < m; r++) {
                for (let c = 0; c < n; c++) {
                    if (dp[r][c] < INF) {
                        minAtVal[grid[r][c]] = Math.min(minAtVal[grid[r][c]], dp[r][c]);
                    }
                }
            }
            let suffixMin = INF;
            for (let v = 10000; v >= 0; v--) {
                suffixMin = Math.min(suffixMin, minAtVal[v]);
                minAtVal[v] = suffixMin;
            }
            for (let r = 0; r < m; r++) {
                for (let c = 0; c < n; c++) {
                    nextDp[r][c] = minAtVal[grid[r][c]];
                }
            }
        }
        for (let r = 0; r < m; r++) {
            for (let c = 0; c < n; c++) {
                if (r > 0) nextDp[r][c] = Math.min(nextDp[r][c], nextDp[r - 1][c] + grid[r][c]);
                if (c > 0) nextDp[r][c] = Math.min(nextDp[r][c], nextDp[r][c - 1] + grid[r][c]);
            }
        }
        dp = nextDp;
    }
    return dp[m - 1][n - 1];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minCost(grid: number[][], k: number): number {
    const m = grid.length;
    const n = grid[0].length;
    const INF = 1000000000;
    let dp: number[][] = Array.from({ length: m }, () => Array(n).fill(INF));

    dp[0][0] = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i > 0) dp[i][j] = Math.min(dp[i][j], dp[i - 1][j] + grid[i][j]);
            if (j > 0) dp[i][j] = Math.min(dp[i][j], dp[i][j - 1] + grid[i][j]);
        }
    }

    for (let t = 0; t < k; t++) {
        let nextDp = dp.map(row => [...row]);
        let minAtVal = new Array(10001).fill(INF);
        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n; j++) {
                if (dp[i][j] < minAtVal[grid[i][j]]) {
                    minAtVal[grid[i][j]] = dp[i][j];
                }
            }
        }

        let suffixMin = new Array(10001).fill(INF);
        suffixMin[10000] = minAtVal[10000];
        for (let v = 9999; v >= 0; v--) {
            suffixMin[v] = Math.min(minAtVal[v], suffixMin[v + 1]);
        }

        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n; j++) {
                if (suffixMin[grid[i][j]] < nextDp[i][j]) {
                    nextDp[i][j] = suffixMin[grid[i][j]];
                }
            }
        }

        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n; j++) {
                if (i > 0) nextDp[i][j] = Math.min(nextDp[i][j], nextDp[i - 1][j] + grid[i][j]);
                if (j > 0) nextDp[i][j] = Math.min(nextDp[i][j], nextDp[i][j - 1] + grid[i][j]);
            }
        }
        dp = nextDp;
    }

    return dp[m - 1][n - 1];
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
     * @param Integer $k
     * @return Integer
     */
    function minCost($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $INF = 1000000000;
        $dp = [];
        for ($i = 0; $i < $m; $i++) {
            $dp[$i] = array_fill(0, $n, $INF);
        }

        $dp[0][0] = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($i > 0) $dp[$i][$j] = min($dp[$i][$j], $dp[$i - 1][$j] + $grid[$i][$j]);
                if ($j > 0) $dp[$i][$j] = min($dp[$i][$j], $dp[$i][$j - 1] + $grid[$i][$j]);
            }
        }

        for ($t = 0; $t < $k; $t++) {
            $nextDp = $dp;
            $minAtVal = array_fill(0, 10001, $INF);
            for ($i = 0; $i < $m; $i++) {
                for ($j = 0; $j < $n; $j++) {
                    if ($dp[$i][$j] < $minAtVal[$grid[$i][$j]]) {
                        $minAtVal[$grid[$i][$j]] = $dp[$i][$j];
                    }
                }
            }

            $suffixMin = array_fill(0, 10001, $INF);
            $suffixMin[10000] = $minAtVal[10000];
            for ($v = 9999; $v >= 0; $v--) {
                $suffixMin[$v] = min($minAtVal[$v], $suffixMin[$v + 1]);
            }

            for ($i = 0; $i < $m; $i++) {
                for ($j = 0; $j < $n; $j++) {
                    if ($suffixMin[$grid[$i][$j]] < $nextDp[$i][$j]) {
                        $nextDp[$i][$j] = $suffixMin[$grid[$i][$j]];
                    }
                }
            }

            for ($i = 0; $i < $m; $i++) {
                for ($j = 0; $j < $n; $j++) {
                    if ($i > 0) $nextDp[$i][$j] = min($nextDp[$i][$j], $nextDp[$i - 1][$j] + $grid[$i][$j]);
                    if ($j > 0) $nextDp[$i][$j] = min($nextDp[$i][$j], $nextDp[$i][$j - 1] + $grid[$i][$j]);
                }
            }
            $dp = $nextDp;
        }

        return $dp[$m - 1][$n - 1];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minCost(_ grid: [[Int]], _ k: Int) -> Int {
        let m = grid.count
        let n = grid[0].count
        let INF = 1_000_000_000
        var dp = Array(repeating: Array(repeating: INF, count: n), count: m)

        dp[0][0] = 0
        for i in 0..<m {
            for j in 0..<n {
                if i > 0 { dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j]) }
                if j > 0 { dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j]) }
            }
        }

        for _ in 0..<k {
            var nextDp = dp
            var minAtVal = Array(repeating: INF, count: 10001)
            for i in 0..<m {
                for j in 0..<n {
                    minAtVal[grid[i][j]] = min(minAtVal[grid[i][j]], dp[i][j])
                }
            }

            var suffixMin = Array(repeating: INF, count: 10001)
            suffixMin[10000] = minAtVal[10000]
            for v in stride(from: 9999, through: 0, by: -1) {
                suffixMin[v] = min(minAtVal[v], suffixMin[v+1])
            }

            for i in 0..<m {
                for j in 0..<n {
                    nextDp[i][j] = min(nextDp[i][j], suffixMin[grid[i][j]])
                }
            }

            for i in 0..<m {
                for j in 0..<n {
                    if i > 0 { nextDp[i][j] = min(nextDp[i][j], nextDp[i-1][j] + grid[i][j]) }
                    if j > 0 { nextDp[i][j] = min(nextDp[i][j], nextDp[i][j-1] + grid[i][j]) }
                }
            }
            dp = nextDp
        }

        return dp[m - 1][n - 1]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minCost(grid: Array<IntArray>, k: Int): Int {
        val m = grid.size
        val n = grid[0].size
        val INF = 1000000000
        var dp = Array(m) { IntArray(n) { INF } }

        dp[0][0] = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (i > 0) dp[i][j] = if (dp[i - 1][j] + grid[i][j] < dp[i][j]) dp[i - 1][j] + grid[i][j] else dp[i][j]
                if (j > 0) dp[i][j] = if (dp[i][j - 1] + grid[i][j] < dp[i][j]) dp[i][j - 1] + grid[i][j] else dp[i][j]
            }
        }

        repeat(k) {
            val nextDp = Array(m) { dp[it].copyOf() }
            val minAtVal = IntArray(10001) { INF }
            for (i in 0 until m) {
                for (j in 0 until n) {
                    if (dp[i][j] < minAtVal[grid[i][j]]) {
                        minAtVal[grid[i][j]] = dp[i][j]
                    }
                }
            }

            val suffixMin = IntArray(10001)
            suffixMin[10000] = minAtVal[10000]
            for (v in 9999 downTo 0) {
                suffixMin[v] = if (minAtVal[v] < suffixMin[v + 1]) minAtVal[v] else suffixMin[v + 1]
            }

            for (i in 0 until m) {
                for (j in 0 until n) {
                    if (suffixMin[grid[i][j]] < nextDp[i][j]) {
                        nextDp[i][j] = suffixMin[grid[i][j]]
                    }
                }
            }

            for (i in 0 until m) {
                for (j in 0 until n) {
                    if (i > 0) nextDp[i][j] = if (nextDp[i - 1][j] + grid[i][j] < nextDp[i][j]) nextDp[i - 1][j] + grid[i][j] else nextDp[i][j]
                    if (j > 0) nextDp[i][j] = if (nextDp[i][j - 1] + grid[i][j] < nextDp[i][j]) nextDp[i][j - 1] + grid[i][j] else nextDp[i][j]
                }
            }
            dp = nextDp
        }

        return dp[m - 1][n - 1]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minCost(List<List<int>> grid, int k) {
    int m = grid.length;
    int n = grid[0].length;
    int INF = 1000000000;
    List<List<int>> dp = List.generate(m, (_) => List.filled(n, INF));

    dp[0][0] = 0;
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (i > 0) dp[i][j] = (dp[i - 1][j] + grid[i][j] < dp[i][j]) ? dp[i - 1][j] + grid[i][j] : dp[i][j];
        if (j > 0) dp[i][j] = (dp[i][j - 1] + grid[i][j] < dp[i][j]) ? dp[i][j - 1] + grid[i][j] : dp[i][j];
      }
    }

    for (int t = 0; t < k; t++) {
      List<List<int>> nextDp = List.generate(m, (i) => List<int>.from(dp[i]));
      List<int> minAtVal = List.filled(10001, INF);
      for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
          if (dp[i][j] < minAtVal[grid[i][j]]) {
            minAtVal[grid[i][j]] = dp[i][j];
          }
        }
      }

      List<int> suffixMin = List.filled(10001, INF);
      suffixMin[10000] = minAtVal[10000];
      for (int v = 9999; v >= 0; v--) {
        suffixMin[v] = (minAtVal[v] < suffixMin[v + 1]) ? minAtVal[v] : suffixMin[v + 1];
      }

      for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
          if (suffixMin[grid[i][j]] < nextDp[i][j]) {
            nextDp[i][j] = suffixMin[grid[i][j]];
          }
        }
      }

      for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
          if (i > 0) nextDp[i][j] = (nextDp[i - 1][j] + grid[i][j] < nextDp[i][j]) ? nextDp[i - 1][j] + grid[i][j] : nextDp[i][j];
          if (j > 0) nextDp[i][j] = (nextDp[i][j - 1] + grid[i][j] < nextDp[i][j]) ? nextDp[i][j - 1] + grid[i][j] : nextDp[i][j];
        }
      }
      dp = nextDp;
    }

    return dp[m - 1][n - 1];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minCost(grid [][]int, k int) int {
	m := len(grid)
	n := len(grid[0])
	INF := 1000000000

	dp := make([][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int, n)
		for j := 0; j < n; j++ {
			dp[i][j] = INF
		}
	}

	dp[0][0] = 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i > 0 && dp[i-1][j]+grid[i][j] < dp[i][j] {
				dp[i][j] = dp[i-1][j] + grid[i][j]
			}
			if j > 0 && dp[i][j-1]+grid[i][j] < dp[i][j] {
				dp[i][j] = dp[i][j-1] + grid[i][j]
			}
		}
	}

	for t := 0; t < k; t++ {
		nextDp := make([][]int, m)
		minAtVal := make([]int, 10001)
		for i := 0; i < 10001; i++ {
			minAtVal[i] = INF
		}

		for i := 0; i < m; i++ {
			nextDp[i] = make([]int, n)
			copy(nextDp[i], dp[i])
			for j := 0; j < n; j++ {
				if dp[i][j] < minAtVal[grid[i][j]] {
					minAtVal[grid[i][j]] = dp[i][j]
				}
			}
		}

		suffixMin := make([]int, 10001)
		suffixMin[10000] = minAtVal[10000]
		for v := 9999; v >= 0; v-- {
			suffixMin[v] = minAtVal[v]
			if suffixMin[v+1] < suffixMin[v] {
				suffixMin[v] = suffixMin[v+1]
			}
		}

		for i := 0; i < m; i++ {
			for j := 0; j < n; j++ {
				if suffixMin[grid[i][j]] < nextDp[i][j] {
					nextDp[i][j] = suffixMin[grid[i][j]]
				}
			}
		}

		for i := 0; i < m; i++ {
			for j := 0; j < n; j++ {
				if i > 0 && nextDp[i-1][j]+grid[i][j] < nextDp[i][j] {
					nextDp[i][j] = nextDp[i-1][j] + grid[i][j]
				}
				if j > 0 && nextDp[i][j-1]+grid[i][j] < nextDp[i][j] {
					nextDp[i][j] = nextDp[i][j-1] + grid[i][j]
				}
			}
		}
		dp = nextDp
	}

	return dp[m-1][n-1]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def min_cost(grid, k)
  m, n = grid.length, grid[0].length
  inf = 1_000_000_000
  dp = Array.new(k + 1) { Array.new(m) { Array.new(n, inf) } }
  dp[0][0][0] = 0

  (0..k).each do |p|
    if p > 0
      min_at_val = Array.new(10001, inf)
      (0...m).each do |i|
        (0...n).each do |j|
          v = grid[i][j]
          min_at_val[v] = [min_at_val[v], dp[p - 1][i][j]].min
        end
      end
      suffix_min = Array.new(10002, inf)
      10000.downto(0) do |v|
        suffix_min[v] = [suffix_min[v + 1], min_at_val[v]].min
      end
      (0...m).each do |i|
        (0...n).each do |j|
          v = grid[i][j]
          dp[p][i][j] = [dp[p][i][j], suffix_min[v]].min
        end
      end
    end
    (0...m).each do |i|
      (0...n).each do |j|
        dp[p][i][j] = [dp[p][i][j], dp[p][i - 1][j] + grid[i][j]].min if i > 0
        dp[p][i][j] = [dp[p][i][j], dp[p][i][j - 1] + grid[i][j]].min if j > 0
      end
    end
  end

  ans = inf
  (0..k).each { |p| ans = [ans, dp[p][m - 1][n - 1]].min }
  ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def minCost(grid: Array[Array[Int]], k: Int): Int = {
    val m = grid.length
    val n = grid(0).length
    val inf = 1000000000
    val dp = Array.fill(k + 1, m, n)(inf)

    dp(0)(0)(0) = 0

    for (p <- 0 to k) {
      if (p > 0) {
        val minAtVal = Array.fill(10001)(inf)
        for (i <- 0 until m; j <- 0 until n) {
          val v = grid(i)(j)
          if (dp(p - 1)(i)(j) < minAtVal(v)) minAtVal(v) = dp(p - 1)(i)(j)
        }
        val suffixMin = Array.fill(10002)(inf)
        for (v <- 10000 to 0 by -1) {
          suffixMin(v) = Math.min(suffixMin(v + 1), minAtVal(v))
        }
        for (i <- 0 until m; j <- 0 until n) {
          dp(p)(i)(j) = Math.min(dp(p)(i)(j), suffixMin(grid(i)(j)))
        }
      }
      for (i <- 0 until m; j <- 0 until n) {
        if (i > 0) dp(p)(i)(j) = Math.min(dp(p)(i)(j), dp(p)(i - 1)(j) + grid(i)(j))
        if (j > 0) dp(p)(i)(j) = Math.min(dp(p)(i)(j), dp(p)(i)(j - 1) + grid(i)(j))
      }
    }

    var ans = inf
    for (p <- 0 to k) ans = Math.min(ans, dp(p)(m - 1)(n - 1))
    ans
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_cost(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let k = k as usize;
        let inf = 1_000_000_000i32;
        let mut dp = vec![vec![vec![inf; n]; m]; k + 1];
        dp[0][0][0] = 0;
        for p in 0..=k {
            if p > 0 {
                let mut min_at_val = vec![inf; 10001];
                for i in 0..m {
                    for j in 0..n {
                        let v = grid[i][j] as usize;
                        min_at_val[v] = min_at_val[v].min(dp[p - 1][i][j]);
                    }
                }
                let mut suffix_min = vec![inf; 10002];
                for v in (0..=10000).rev() {
                    suffix_min[v] = suffix_min[v + 1].min(min_at_val[v]);
                }
                for i in 0..m {
                    for j in 0..n {
                        let v = grid[i][j] as usize;
                        dp[p][i][j] = dp[p][i][j].min(suffix_min[v]);
                    }
                }
            }
            for i in 0..m {
                for j in 0..n {
                    let v = grid[i][j];
                    if i > 0 {
                        dp[p][i][j] = dp[p][i][j].min(dp[p][i - 1][j] + v);
                    }
                    if j > 0 {
                        dp[p][i][j] = dp[p][i][j].min(dp[p][i][j - 1] + v);
                    }
                }
            }
        }
        let mut ans = inf;
        for p in 0..=k {
            ans = ans.min(dp[p][m - 1][n - 1]);
        }
        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-cost grid k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ([m (length grid)]
         [n (length (first grid))]
         [grid-vec (list->vector (map list->vector grid))]
         [inf 1000000000]
         [dp (make-vector (+ k 1))])
    (for ([p (in-range (+ k 1))])
      (vector-set! dp p (make-vector m))
      (for ([i (in-range m)])
        (vector-set! (vector-ref dp p) i (make-vector n inf))))
    (vector-set! (vector-ref (vector-ref dp 0) 0) 0 0)
    (for ([p (in-range (+ k 1))])
      (when (> p 0)
        (let ([min-at-val (make-vector 10001 inf)])
          (for ([i (in-range m)])
            (for ([j (in-range n)])
              (let ([v (vector-ref (vector-ref grid-vec i) j)]
                    [cost (vector-ref (vector-ref (vector-ref dp (- p 1)) i) j)])
                (vector-set! min-at-val v (min (vector-ref min-at-val v) cost)))))
          (let ([suffix-min (make-vector 10002 inf)])
            (for ([v (in-range 10000 -1 -1)])
              (vector-set! suffix-min v (min (vector-ref suffix-min (+ v 1)) (vector-ref min-at-val v))))
            (for ([i (in-range m)])
              (for ([j (in-range n)])
                (let ([v (vector-ref (vector-ref grid-vec i) j)])
                  (vector-set! (vector-ref (vector-ref dp p) i) j (vector-ref suffix-min v))))))))
      (let ([curr-dp-p (vector-ref dp p)])
        (for ([i (in-range m)])
          (let ([curr-row (vector-ref curr-dp-p i)]
                [row-grid (vector-ref grid-vec i)]
                [prev-row (if (> i 0) (vector-ref curr-dp-p (- i 1)) #f)])
            (for ([j (in-range n)])
              (let* ([v (vector-ref row-grid j)]
                     [current (vector-ref curr-row j)]
                     [v1 (if prev-row (+ (vector-ref prev-row j) v) inf)]
                     [v2 (if (> j 0) (+ (vector-ref curr-row (- j 1)) v) inf)])
                (vector-set! curr-row j (min current v1 v2))))))))
    (let ([ans inf])
      (for ([p (in-range (+ k 1))])
        (set! ans (min ans (vector-ref (vector-ref (vector-ref dp p) (- m 1)) (- n 1)))))
      ans)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
min_cost(Grid, K) ->
  M = length(Grid),
  N = length(hd(Grid)),
  GridArray = array:from_list([array:from_list(Row) || Row <- Grid]),
  Inf = 1000000000,
  InitialDP = array:from_list([
    if I == 0 -> array:set(0, 0, array:new(N, {default, Inf}));
       true -> array:new(N, {default, Inf})
    end || I <- lists:seq(0, M-1)
  ]),
  DP0 = update_grid_dp(InitialDP, GridArray, M, N, Inf),
  FinalDPs = lists:foldl(fn(_, AccDPs) ->
    PrevDP = hd(AccDPs),
    MinAtVal0 = array:new(10001, {default, Inf}),
    MinAtVal = lists:foldl(fn(I, AccV) ->
      Row = array:get(I, PrevDP),
      RowGrid = array:get(I, GridArray),
      lists:foldl(fn(J, AccV2) ->
        V = array:get(J, RowGrid),
        array:set(V, erlang:min(array:get(V, AccV2), array:get(J, Row)), AccV2)
      end, AccV, lists:seq(0, N-1))
    end, MinAtVal0, lists:seq(0, M-1)),
    SuffixMin0 = array:new(10002, {default, Inf}),
    SuffixMin = lists:foldl(fn(V, AccS) ->
      array:set(V, erlang:min(array:get(V+1, AccS), array:get(V, MinAtVal)), AccS)
    end, SuffixMin0, lists:seq(10000, 0, -1)),
    TeleportDP = array:from_list([
      array:from_list([
        array:get(array:get(J, array:get(I, GridArray)), SuffixMin)
      || J <- lists:seq(0, N-1)])
    || I <- lists:seq(0, M-1)]),
    [update_grid_dp(TeleportDP, GridArray, M, N, Inf) | AccDPs]
  end, [DP0], if K > 0 -> lists:seq(1, K); true -> [] end),
  lists:min([array:get(N-1, array:get(M-1, D)) || D <- FinalDPs]).

update_grid_dp(DP, GridArray, M, N, Inf) ->
  lists:foldl(fn(I, AccDP) ->
    RowGrid = array:get(I, GridArray),
    RowDP = array:get(I, AccDP),
    PrevRowDP = if I > 0 -> array:get(I-1, AccDP); true -> undefined end,
    NewRowDP = lists:foldl(fn(J, AccRow) ->
      V = array:get(J, RowGrid),
      V1 = if PrevRowDP /= undefined -> array:get(J, PrevRowDP) + V; true -> Inf end,
      V2 = if J > 0 -> array:get(J-1, AccRow) + V; true -> Inf end,
      array:set(J, erlang:min(array:get(J, AccRow), erlang:min(V1, V2)), AccRow)
    end, RowDP, lists:seq(0, N-1)),
    array:set(I, NewRowDP, AccDP)
  end, DP, lists:seq(0, M-1)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_cost(grid :: [[integer]], k :: integer) :: integer
  def min_cost(grid_list, k) do
    grid = grid_list |> Enum.map(&List.to_tuple/1) |> List.to_tuple()
    m = tuple_size(grid)
    n = tuple_size(elem(grid, 0))
    inf = 1_000_000_000
    dp0_initial = for i <- 0..(m-1) do
      if i == 0, do: put_elem(Tuple.duplicate(inf, n), 0, 0), else: Tuple.duplicate(inf, n)
    end |> List.to_tuple()
    dp0 = update_grid_dp(dp0_initial, grid, m, n, inf)
    ranges = if k > 0, do: 1..k, else: []
    {_last_dp, ans_list} = Enum.reduce(ranges, {dp0, [elem(elem(dp0, m-1), n-1)]}, fn _, {prev_dp, acc_ans} ->
      min_at_val = Enum.reduce(0..(m-1), %{}, fn i, acc_i ->
        row_dp = elem(prev_dp, i)
        row_grid = elem(grid, i)
        Enum.reduce(0..(n-1), acc_i, fn j, acc_j ->
          v = elem(row_grid, j)
          Map.update(acc_j, v, elem(row_dp, j), &min(&1, elem(row_dp, j)))
        end)
      end)
      {_, suffix_min} = Enum.reduce(10000..0, {inf, %{}}, fn v, {curr_min, acc_s} ->
        new_min = min(curr_min, Map.get(min_at_val, v, inf))
        {new_min, Map.put(acc_s, v, new_min)}
      end)
      teleport_dp = (for i <- 0..(m-1) do
        row_grid = elem(grid, i)
        (for j <- 0..(n-1) do Map.get(suffix_min, elem(row_grid, j), inf) end) |> List.to_tuple()
      end) |> List.to_tuple()
      new_dp = update_grid_dp(teleport_dp, grid, m, n, inf)
      {new_dp, [elem(elem(new_dp, m-1), n-1) | acc_ans]}
    end)
    Enum.min(ans_list)
  end
  defp update_grid_dp(dp, grid, m, n, inf) do
    Enum.reduce(0..(m-1), dp, fn i, acc_dp ->
      row_grid = elem(grid, i)
      prev_row = if i > 0, do: elem(acc_dp, i-1), else: nil
      new_row = Enum.reduce(0..(n-1), elem(acc_dp, i), fn j, acc_row ->
        v = elem(row_grid, j)
        v1 = if prev_row, do: elem(prev_row, j) + v, else: inf
        v2 = if j > 0, do: elem(acc_row, j-1) + v, else: inf
        put_elem(acc_row, j, min(elem(acc_row, j), min(v1, v2)))
      end)
      put_elem(acc_dp, i, new_row)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(k * (m * n + V)), where m and n are the grid dimensions, k is the maximum number of teleports, and V is the maximum grid value (10,000). The outer loop runs k+1 times, and each iteration performs a suffix minimum precomputation (O(V)), a teleportation update (O(m * n)), and a standard grid DP (O(m * n)).
- **Space Complexity:** O(m * n + V) to store the DP table (only two stages are needed) and the suffix minimum array. Given the constraints m, n <= 80 and V <= 10,000, this fits well within memory limits.
