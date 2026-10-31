---
layout: post
title: "Twisted Mirror Path Count"
date: 2026-10-31 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Dynamic Programming", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/twisted-mirror-path-count/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int uniquePaths(vector<vector<int>>& grid)\
        \ {\n        int m = grid.size();\n        int n = grid[0].size();\n       \
        \ int MOD = 1000000007;\n\n        struct Pos {\n            int r, c;\n   \
        \     };\n\n        vector<vector<Pos>> memo_right(m, vector<Pos>(n, {-1, -1}));\n\
        \        vector<vector<Pos>> memo_down(m, vector<Pos>(n, {-1, -1}));\n\n   \
        \     for (int i = m - 1; i >= 0; --i) {\n            for (int j = n - 1; j\
        \ >= 0; --j) {\n                if (grid[i][j] == 0) {\n                   \
        \ memo_right[i][j] = {i, j};\n                    memo_down[i][j] = {i, j};\n\
        \                } else {\n                    if (i + 1 < m) memo_right[i][j]\
        \ = memo_down[i + 1][j];\n                    if (j + 1 < n) memo_down[i][j]\
        \ = memo_right[i][j + 1];\n                }\n            }\n        }\n\n \
        \       vector<vector<int>> dp(m, vector<int>(n, 0));\n        dp[0][0] = 1;\n\
        \n        for (int i = 0; i < m; ++i) {\n            for (int j = 0; j < n;\
        \ ++j) {\n                if (dp[i][j] == 0) continue;\n\n                if\
        \ (j + 1 < n) {\n                    Pos target = memo_right[i][j + 1];\n  \
        \                  if (target.r != -1) {\n                        dp[target.r][target.c]\
        \ = (dp[target.r][target.c] + dp[i][j]) % MOD;\n                    }\n    \
        \            }\n\n                if (i + 1 < m) {\n                    Pos\
        \ target = memo_down[i + 1][j];\n                    if (target.r != -1) {\n\
        \                        dp[target.r][target.c] = (dp[target.r][target.c] +\
        \ dp[i][j]) % MOD;\n                    }\n                }\n            }\n\
        \        }\n\n        return dp[m - 1][n - 1];\n    }\n};"
      java: "class Solution {\n    public int uniquePaths(int[][] grid) {\n        int\
        \ m = grid.length;\n        int n = grid[0].length;\n        int MOD = 1000000007;\n\
        \n        int[][] memoRightR = new int[m][n];\n        int[][] memoRightC =\
        \ new int[m][n];\n        int[][] memoDownR = new int[m][n];\n        int[][]\
        \ memoDownC = new int[m][n];\n\n        for (int i = 0; i < m; i++) {\n    \
        \        for (int j = 0; j < n; j++) {\n                memoRightR[i][j] = memoDownR[i][j]\
        \ = -1;\n            }\n        }\n\n        for (int i = m - 1; i >= 0; i--)\
        \ {\n            for (int j = n - 1; j >= 0; j--) {\n                if (grid[i][j]\
        \ == 0) {\n                    memoRightR[i][j] = memoDownR[i][j] = i;\n   \
        \                 memoRightC[i][j] = memoDownC[i][j] = j;\n                }\
        \ else {\n                    if (i + 1 < m) {\n                        memoRightR[i][j]\
        \ = memoDownR[i + 1][j];\n                        memoRightC[i][j] = memoDownC[i\
        \ + 1][j];\n                    }\n                    if (j + 1 < n) {\n  \
        \                      memoDownR[i][j] = memoRightR[i][j + 1];\n           \
        \             memoDownC[i][j] = memoRightC[i][j + 1];\n                    }\n\
        \                }\n            }\n        }\n\n        int[][] dp = new int[m][n];\n\
        \        dp[0][0] = 1;\n\n        for (int i = 0; i < m; i++) {\n          \
        \  for (int j = 0; j < n; j++) {\n                if (dp[i][j] == 0) continue;\n\
        \n                if (j + 1 < n) {\n                    int tr = memoRightR[i][j\
        \ + 1];\n                    int tc = memoRightC[i][j + 1];\n              \
        \      if (tr != -1) {\n                        dp[tr][tc] = (dp[tr][tc] + dp[i][j])\
        \ % MOD;\n                    }\n                }\n\n                if (i\
        \ + 1 < m) {\n                    int tr = memoDownR[i + 1][j];\n          \
        \          int tc = memoDownC[i + 1][j];\n                    if (tr != -1)\
        \ {\n                        dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD;\n \
        \                   }\n                }\n            }\n        }\n\n     \
        \   return dp[m - 1][n - 1];\n    }\n}"
      python: "class Solution(object):\n    def uniquePaths(self, grid):\n        \"\
        \"\"\n        :type grid: List[List[int]]\n        :rtype: int\n        \"\"\
        \"\n        m = len(grid)\n        n = len(grid[0])\n        MOD = 1000000007\n\
        \n        memo_right = [[(-1, -1) for _ in range(n)] for _ in range(m)]\n  \
        \      memo_down = [[(-1, -1) for _ in range(n)] for _ in range(m)]\n\n    \
        \    for i in range(m - 1, -1, -1):\n            for j in range(n - 1, -1, -1):\n\
        \                if grid[i][j] == 0:\n                    memo_right[i][j] =\
        \ (i, j)\n                    memo_down[i][j] = (i, j)\n                else:\n\
        \                    if i + 1 < m:\n                        memo_right[i][j]\
        \ = memo_down[i + 1][j]\n                    if j + 1 < n:\n               \
        \         memo_down[i][j] = memo_right[i][j + 1]\n\n        dp = [[0] * n for\
        \ _ in range(m)]\n        dp[0][0] = 1\n\n        for i in range(m):\n     \
        \       for j in range(n):\n                if dp[i][j] == 0:\n            \
        \        continue\n\n                if j + 1 < n:\n                    tr,\
        \ tc = memo_right[i][j + 1]\n                    if tr != -1:\n            \
        \            dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD\n\n                if\
        \ i + 1 < m:\n                    tr, tc = memo_down[i + 1][j]\n           \
        \         if tr != -1:\n                        dp[tr][tc] = (dp[tr][tc] + dp[i][j])\
        \ % MOD\n\n        return dp[m - 1][n - 1]"
      python3: "class Solution:\n    def uniquePaths(self, grid: List[List[int]]) ->\
        \ int:\n        m = len(grid)\n        n = len(grid[0])\n        MOD = 10**9\
        \ + 7\n\n        memo_right = [[(-1, -1) for _ in range(n)] for _ in range(m)]\n\
        \        memo_down = [[(-1, -1) for _ in range(n)] for _ in range(m)]\n\n  \
        \      for i in range(m - 1, -1, -1):\n            for j in range(n - 1, -1,\
        \ -1):\n                if grid[i][j] == 0:\n                    memo_right[i][j]\
        \ = (i, j)\n                    memo_down[i][j] = (i, j)\n                else:\n\
        \                    if i + 1 < m:\n                        memo_right[i][j]\
        \ = memo_down[i + 1][j]\n                    if j + 1 < n:\n               \
        \         memo_down[i][j] = memo_right[i][j + 1]\n\n        dp = [[0] * n for\
        \ _ in range(m)]\n        dp[0][0] = 1\n\n        for i in range(m):\n     \
        \       for j in range(n):\n                if dp[i][j] == 0:\n            \
        \        continue\n\n                if j + 1 < n:\n                    tr,\
        \ tc = memo_right[i][j + 1]\n                    if tr != -1:\n            \
        \            dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD\n\n                if\
        \ i + 1 < m:\n                    tr, tc = memo_down[i + 1][j]\n           \
        \         if tr != -1:\n                        dp[tr][tc] = (dp[tr][tc] + dp[i][j])\
        \ % MOD\n\n        return dp[m - 1][n - 1]"
      c: "int uniquePaths(int** grid, int gridSize, int* gridColSize) {\n    int m =\
        \ gridSize;\n    int n = gridColSize[0];\n    int MOD = 1000000007;\n\n    int*\
        \ memoRightR = (int*)malloc(m * n * sizeof(int));\n    int* memoRightC = (int*)malloc(m\
        \ * n * sizeof(int));\n    int* memoDownR = (int*)malloc(m * n * sizeof(int));\n\
        \    int* memoDownC = (int*)malloc(m * n * sizeof(int));\n\n    for (int i =\
        \ 0; i < m * n; i++) {\n        memoRightR[i] = -1;\n        memoDownR[i] =\
        \ -1;\n    }\n\n    for (int i = m - 1; i >= 0; i--) {\n        for (int j =\
        \ n - 1; j >= 0; j--) {\n            int idx = i * n + j;\n            if (grid[i][j]\
        \ == 0) {\n                memoRightR[idx] = memoDownR[idx] = i;\n         \
        \       memoRightC[idx] = memoDownC[idx] = j;\n            } else {\n      \
        \          if (i + 1 < m) {\n                    memoRightR[idx] = memoDownR[(i\
        \ + 1) * n + j];\n                    memoRightC[idx] = memoDownC[(i + 1) *\
        \ n + j];\n                }\n                if (j + 1 < n) {\n           \
        \         memoDownR[idx] = memoRightR[i * n + (j + 1)];\n                  \
        \  memoDownC[idx] = memoRightC[i * n + (j + 1)];\n                }\n      \
        \      }\n        }\n    }\n\n    int* dp = (int*)calloc(m * n, sizeof(int));\n\
        \    dp[0] = 1;\n\n    for (int i = 0; i < m; i++) {\n        for (int j = 0;\
        \ j < n; j++) {\n            int idx = i * n + j;\n            if (dp[idx] ==\
        \ 0) continue;\n\n            if (j + 1 < n) {\n                int tr = memoRightR[i\
        \ * n + (j + 1)];\n                int tc = memoRightC[i * n + (j + 1)];\n \
        \               if (tr != -1) {\n                    int t_idx = tr * n + tc;\n\
        \                    dp[t_idx] = (dp[t_idx] + dp[idx]) % MOD;\n            \
        \    }\n            }\n\n            if (i + 1 < m) {\n                int tr\
        \ = memoDownR[(i + 1) * n + j];\n                int tc = memoDownC[(i + 1)\
        \ * n + j];\n                if (tr != -1) {\n                    int t_idx\
        \ = tr * n + tc;\n                    dp[t_idx] = (dp[t_idx] + dp[idx]) % MOD;\n\
        \                }\n            }\n        }\n    }\n\n    int result = dp[m\
        \ * n - 1];\n    free(memoRightR);\n    free(memoRightC);\n    free(memoDownR);\n\
        \    free(memoDownC);\n    free(dp);\n    return result;\n}"
      csharp: "public class Solution {\n    public int UniquePaths(int[][] grid) {\n\
        \        int m = grid.Length;\n        int n = grid[0].Length;\n        int\
        \ MOD = 1000000007;\n\n        int[,] fRightRow = new int[m, n];\n        int[,]\
        \ fRightCol = new int[m, n];\n        int[,] fDownRow = new int[m, n];\n   \
        \     int[,] fDownCol = new int[m, n];\n\n        for (int r = m - 1; r >= 0;\
        \ r--) {\n            for (int c = n - 1; c >= 0; c--) {\n                if\
        \ (grid[r][c] == 0) {\n                    fRightRow[r, c] = r;\n          \
        \          fRightCol[r, c] = c;\n                    fDownRow[r, c] = r;\n \
        \                   fDownCol[r, c] = c;\n                } else {\n        \
        \            if (r + 1 < m) {\n                        fRightRow[r, c] = fDownRow[r\
        \ + 1, c];\n                        fRightCol[r, c] = fDownCol[r + 1, c];\n\
        \                    } else {\n                        fRightRow[r, c] = -1;\n\
        \                        fRightCol[r, c] = -1;\n                    }\n    \
        \                if (c + 1 < n) {\n                        fDownRow[r, c] =\
        \ fRightRow[r, c + 1];\n                        fDownCol[r, c] = fRightCol[r,\
        \ c + 1];\n                    } else {\n                        fDownRow[r,\
        \ c] = -1;\n                        fDownCol[r, c] = -1;\n                 \
        \   }\n                }\n            }\n        }\n\n        int[,] dp = new\
        \ int[m, n];\n        dp[0, 0] = 1;\n\n        for (int r = 0; r < m; r++) {\n\
        \            for (int c = 0; c < n; c++) {\n                if (dp[r, c] ==\
        \ 0) continue;\n\n                if (c + 1 < n) {\n                    int\
        \ nr = fRightRow[r, c + 1];\n                    int nc = fRightCol[r, c + 1];\n\
        \                    if (nr != -1) {\n                        dp[nr, nc] = (dp[nr,\
        \ nc] + dp[r, c]) % MOD;\n                    }\n                }\n\n     \
        \           if (r + 1 < m) {\n                    int nr = fDownRow[r + 1, c];\n\
        \                    int nc = fDownCol[r + 1, c];\n                    if (nr\
        \ != -1) {\n                        dp[nr, nc] = (dp[nr, nc] + dp[r, c]) % MOD;\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    return dp[m - 1, n - 1];\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @return {number}\n */\nvar uniquePaths\
        \ = function(grid) {\n    const m = grid.length;\n    const n = grid[0].length;\n\
        \    const MOD = 1000000007;\n\n    const fRightRow = Array.from({ length: m\
        \ }, () => new Int32Array(n).fill(-1));\n    const fRightCol = Array.from({\
        \ length: m }, () => new Int32Array(n).fill(-1));\n    const fDownRow = Array.from({\
        \ length: m }, () => new Int32Array(n).fill(-1));\n    const fDownCol = Array.from({\
        \ length: m }, () => new Int32Array(n).fill(-1));\n\n    for (let r = m - 1;\
        \ r >= 0; r--) {\n        for (let c = n - 1; c >= 0; c--) {\n            if\
        \ (grid[r][c] === 0) {\n                fRightRow[r][c] = r;\n             \
        \   fRightCol[r][c] = c;\n                fDownRow[r][c] = r;\n            \
        \    fDownCol[r][c] = c;\n            } else {\n                if (r + 1 <\
        \ m) {\n                    fRightRow[r][c] = fDownRow[r + 1][c];\n        \
        \            fRightCol[r][c] = fDownCol[r + 1][c];\n                }\n    \
        \            if (c + 1 < n) {\n                    fDownRow[r][c] = fRightRow[r][c\
        \ + 1];\n                    fDownCol[r][c] = fRightCol[r][c + 1];\n       \
        \         }\n            }\n        }\n    }\n\n    const dp = Array.from({\
        \ length: m }, () => new Int32Array(n).fill(0));\n    dp[0][0] = 1;\n\n    for\
        \ (let r = 0; r < m; r++) {\n        for (let c = 0; c < n; c++) {\n       \
        \     if (dp[r][c] === 0) continue;\n\n            if (c + 1 < n) {\n      \
        \          const nr = fRightRow[r][c + 1];\n                const nc = fRightCol[r][c\
        \ + 1];\n                if (nr !== -1) {\n                    dp[nr][nc] =\
        \ (dp[nr][nc] + dp[r][c]) % MOD;\n                }\n            }\n\n     \
        \       if (r + 1 < m) {\n                const nr = fDownRow[r + 1][c];\n \
        \               const nc = fDownCol[r + 1][c];\n                if (nr !== -1)\
        \ {\n                    dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD;\n     \
        \           }\n            }\n        }\n    }\n\n    return dp[m - 1][n - 1];\n\
        };"
      typescript: "function uniquePaths(grid: number[][]): number {\n    const m = grid.length;\n\
        \    const n = grid[0].length;\n    const MOD = 1000000007;\n\n    const fRightRow:\
        \ Int32Array[] = Array.from({ length: m }, () => new Int32Array(n).fill(-1));\n\
        \    const fRightCol: Int32Array[] = Array.from({ length: m }, () => new Int32Array(n).fill(-1));\n\
        \    const fDownRow: Int32Array[] = Array.from({ length: m }, () => new Int32Array(n).fill(-1));\n\
        \    const fDownCol: Int32Array[] = Array.from({ length: m }, () => new Int32Array(n).fill(-1));\n\
        \n    for (let r = m - 1; r >= 0; r--) {\n        for (let c = n - 1; c >= 0;\
        \ c--) {\n            if (grid[r][c] === 0) {\n                fRightRow[r][c]\
        \ = r;\n                fRightCol[r][c] = c;\n                fDownRow[r][c]\
        \ = r;\n                fDownCol[r][c] = c;\n            } else {\n        \
        \        if (r + 1 < m) {\n                    fRightRow[r][c] = fDownRow[r\
        \ + 1][c];\n                    fRightCol[r][c] = fDownCol[r + 1][c];\n    \
        \            }\n                if (c + 1 < n) {\n                    fDownRow[r][c]\
        \ = fRightRow[r][c + 1];\n                    fDownCol[r][c] = fRightCol[r][c\
        \ + 1];\n                }\n            }\n        }\n    }\n\n    const dp:\
        \ Int32Array[] = Array.from({ length: m }, () => new Int32Array(n).fill(0));\n\
        \    dp[0][0] = 1;\n\n    for (let r = 0; r < m; r++) {\n        for (let c\
        \ = 0; c < n; c++) {\n            if (dp[r][c] === 0) continue;\n\n        \
        \    if (c + 1 < n) {\n                const nr = fRightRow[r][c + 1];\n   \
        \             const nc = fRightCol[r][c + 1];\n                if (nr !== -1)\
        \ {\n                    dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD;\n     \
        \           }\n            }\n\n            if (r + 1 < m) {\n             \
        \   const nr = fDownRow[r + 1][c];\n                const nc = fDownCol[r +\
        \ 1][c];\n                if (nr !== -1) {\n                    dp[nr][nc] =\
        \ (dp[nr][nc] + dp[r][c]) % MOD;\n                }\n            }\n       \
        \ }\n    }\n\n    return dp[m - 1][n - 1];\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @return\
        \ Integer\n     */\n    function uniquePaths($grid) {\n        $m = count($grid);\n\
        \        $n = count($grid[0]);\n        $MOD = 1000000007;\n\n        $fRightRow\
        \ = array_fill(0, $m, array_fill(0, $n, -1));\n        $fRightCol = array_fill(0,\
        \ $m, array_fill(0, $n, -1));\n        $fDownRow = array_fill(0, $m, array_fill(0,\
        \ $n, -1));\n        $fDownCol = array_fill(0, $m, array_fill(0, $n, -1));\n\
        \n        for ($r = $m - 1; $r >= 0; $r--) {\n            for ($c = $n - 1;\
        \ $c >= 0; $c--) {\n                if ($grid[$r][$c] == 0) {\n            \
        \        $fRightRow[$r][$c] = $r;\n                    $fRightCol[$r][$c] =\
        \ $c;\n                    $fDownRow[$r][$c] = $r;\n                    $fDownCol[$r][$c]\
        \ = $c;\n                } else {\n                    if ($r + 1 < $m) {\n\
        \                        $fRightRow[$r][$c] = $fDownRow[$r + 1][$c];\n     \
        \                   $fRightCol[$r][$c] = $fDownCol[$r + 1][$c];\n          \
        \          }\n                    if ($c + 1 < $n) {\n                     \
        \   $fDownRow[$r][$c] = $fRightRow[$r][$c + 1];\n                        $fDownCol[$r][$c]\
        \ = $fRightCol[$r][$c + 1];\n                    }\n                }\n    \
        \        }\n        }\n\n        $dp = array_fill(0, $m, array_fill(0, $n, 0));\n\
        \        $dp[0][0] = 1;\n\n        for ($r = 0; $r < $m; $r++) {\n         \
        \   for ($c = 0; $c < $n; $c++) {\n                if ($dp[$r][$c] == 0) continue;\n\
        \n                if ($c + 1 < $n) {\n                    $nr = $fRightRow[$r][$c\
        \ + 1];\n                    $nc = $fRightCol[$r][$c + 1];\n               \
        \     if ($nr != -1) {\n                        $dp[$nr][$nc] = ($dp[$nr][$nc]\
        \ + $dp[$r][$c]) % $MOD;\n                    }\n                }\n\n     \
        \           if ($r + 1 < $m) {\n                    $nr = $fDownRow[$r + 1][$c];\n\
        \                    $nc = $fDownCol[$r + 1][$c];\n                    if ($nr\
        \ != -1) {\n                        $dp[$nr][$nc] = ($dp[$nr][$nc] + $dp[$r][$c])\
        \ % $MOD;\n                    }\n                }\n            }\n       \
        \ }\n\n        return $dp[$m - 1][$n - 1];\n    }\n}"
      swift: "class Solution {\n    func uniquePaths(_ grid: [[Int]]) -> Int {\n   \
        \     let m = grid.count\n        let n = grid[0].count\n        let MOD = 1000000007\n\
        \n        var fRightRow = Array(repeating: Array(repeating: -1, count: n), count:\
        \ m)\n        var fRightCol = Array(repeating: Array(repeating: -1, count: n),\
        \ count: m)\n        var fDownRow = Array(repeating: Array(repeating: -1, count:\
        \ n), count: m)\n        var fDownCol = Array(repeating: Array(repeating: -1,\
        \ count: n), count: m)\n\n        for r in (0..<m).reversed() {\n          \
        \  for c in (0..<n).reversed() {\n                if grid[r][c] == 0 {\n   \
        \                 fRightRow[r][c] = r\n                    fRightCol[r][c] =\
        \ c\n                    fDownRow[r][c] = r\n                    fDownCol[r][c]\
        \ = c\n                } else {\n                    if r + 1 < m {\n      \
        \                  fRightRow[r][c] = fDownRow[r + 1][c]\n                  \
        \      fRightCol[r][c] = fDownCol[r + 1][c]\n                    }\n       \
        \             if c + 1 < n {\n                        fDownRow[r][c] = fRightRow[r][c\
        \ + 1]\n                        fDownCol[r][c] = fRightCol[r][c + 1]\n     \
        \               }\n                }\n            }\n        }\n\n        var\
        \ dp = Array(repeating: Array(repeating: 0, count: n), count: m)\n        dp[0][0]\
        \ = 1\n\n        for r in 0..<m {\n            for c in 0..<n {\n          \
        \      if dp[r][c] == 0 { continue }\n\n                if c + 1 < n {\n   \
        \                 let nr = fRightRow[r][c + 1]\n                    let nc =\
        \ fRightCol[r][c + 1]\n                    if nr != -1 {\n                 \
        \       dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD\n                    }\n\
        \                }\n\n                if r + 1 < m {\n                    let\
        \ nr = fDownRow[r + 1][c]\n                    let nc = fDownCol[r + 1][c]\n\
        \                    if nr != -1 {\n                        dp[nr][nc] = (dp[nr][nc]\
        \ + dp[r][c]) % MOD\n                    }\n                }\n            }\n\
        \        }\n\n        return dp[m - 1][n - 1]\n    }\n}"
      kotlin: "class Solution {\n    fun uniquePaths(grid: Array<IntArray>): Int {\n\
        \        val m = grid.size\n        val n = grid[0].size\n        val MOD =\
        \ 1000000007L\n\n        val memoR = Array(m) { IntArray(n) { -1 } }\n     \
        \   val memoD = Array(m) { IntArray(n) { -1 } }\n\n        for (r in m - 1 downTo\
        \ 0) {\n            for (c in n - 1 downTo 0) {\n                if (grid[r][c]\
        \ == 0) {\n                    memoR[r][c] = r * n + c\n                   \
        \ memoD[r][c] = r * n + c\n                } else {\n                    if\
        \ (r + 1 < m) memoR[r][c] = memoD[r + 1][c]\n                    if (c + 1 <\
        \ n) memoD[r][c] = memoR[r][c + 1]\n                }\n            }\n     \
        \   }\n\n        val dp = Array(m) { LongArray(n) }\n        dp[0][0] = 1\n\n\
        \        for (i in 0 until m) {\n            for (j in 0 until n) {\n      \
        \          if (dp[i][j] == 0L) continue\n\n                val targetR = if\
        \ (j + 1 < n) memoR[i][j + 1] else -1\n                if (targetR != -1) {\n\
        \                    val tr = targetR / n\n                    val tc = targetR\
        \ % n\n                    dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD\n    \
        \            }\n\n                val targetD = if (i + 1 < m) memoD[i + 1][j]\
        \ else -1\n                if (targetD != -1) {\n                    val tr\
        \ = targetD / n\n                    val tc = targetD % n\n                \
        \    dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD\n                }\n       \
        \     }\n        }\n\n        return dp[m - 1][n - 1].toInt()\n    }\n}"
      dart: "class Solution {\n  int uniquePaths(List<List<int>> grid) {\n    int m\
        \ = grid.length;\n    int n = grid[0].length;\n    int MOD = 1000000007;\n\n\
        \    List<List<int>> memoR = List.generate(m, (_) => List.filled(n, -1));\n\
        \    List<List<int>> memoD = List.generate(m, (_) => List.filled(n, -1));\n\n\
        \    for (int r = m - 1; r >= 0; r--) {\n      for (int c = n - 1; c >= 0; c--)\
        \ {\n        if (grid[r][c] == 0) {\n          memoR[r][c] = r * n + c;\n  \
        \        memoD[r][c] = r * n + c;\n        } else {\n          if (r + 1 < m)\
        \ memoR[r][c] = memoD[r + 1][c];\n          if (c + 1 < n) memoD[r][c] = memoR[r][c\
        \ + 1];\n        }\n      }\n    }\n\n    List<List<int>> dp = List.generate(m,\
        \ (_) => List.filled(n, 0));\n    dp[0][0] = 1;\n\n    for (int i = 0; i < m;\
        \ i++) {\n      for (int j = 0; j < n; j++) {\n        if (dp[i][j] == 0) continue;\n\
        \n        int targetR = (j + 1 < n) ? memoR[i][j + 1] : -1;\n        if (targetR\
        \ != -1) {\n          int tr = targetR ~/ n;\n          int tc = targetR % n;\n\
        \          dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD;\n        }\n\n      \
        \  int targetD = (i + 1 < m) ? memoD[i + 1][j] : -1;\n        if (targetD !=\
        \ -1) {\n          int tr = targetD ~/ n;\n          int tc = targetD % n;\n\
        \          dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD;\n        }\n      }\n\
        \    }\n\n    return dp[m - 1][n - 1];\n  }\n}"
      go: "func uniquePaths(grid [][]int) int {\n\tm := len(grid)\n\tn := len(grid[0])\n\
        \tMOD := 1000000007\n\n\tmemoR := make([][]int, m)\n\tmemoD := make([][]int,\
        \ m)\n\tfor i := 0; i < m; i++ {\n\t\tmemoR[i] = make([]int, n)\n\t\tmemoD[i]\
        \ = make([]int, n)\n\t\tfor j := 0; j < n; j++ {\n\t\t\tmemoR[i][j] = -1\n\t\
        \t\tmemoD[i][j] = -1\n\t\t}\n\t}\n\n\tfor r := m - 1; r >= 0; r-- {\n\t\tfor\
        \ c := n - 1; c >= 0; c-- {\n\t\t\tif grid[r][c] == 0 {\n\t\t\t\tmemoR[r][c]\
        \ = r*n + c\n\t\t\t\tmemoD[r][c] = r*n + c\n\t\t\t} else {\n\t\t\t\tif r+1 <\
        \ m {\n\t\t\t\t\tmemoR[r][c] = memoD[r+1][c]\n\t\t\t\t}\n\t\t\t\tif c+1 < n\
        \ {\n\t\t\t\t\tmemoD[r][c] = memoR[r][c+1]\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t}\n\
        \n\tdp := make([][]int, m)\n\tfor i := 0; i < m; i++ {\n\t\tdp[i] = make([]int,\
        \ n)\n\t}\n\tdp[0][0] = 1\n\n\tfor i := 0; i < m; i++ {\n\t\tfor j := 0; j <\
        \ n; j++ {\n\t\t\tif dp[i][j] == 0 {\n\t\t\t\tcontinue\n\t\t\t}\n\n\t\t\ttargetR\
        \ := -1\n\t\t\tif j+1 < n {\n\t\t\t\ttargetR = memoR[i][j+1]\n\t\t\t}\n\t\t\t\
        if targetR != -1 {\n\t\t\t\ttr := targetR / n\n\t\t\t\ttc := targetR % n\n\t\
        \t\t\tdp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD\n\t\t\t}\n\n\t\t\ttargetD :=\
        \ -1\n\t\t\tif i+1 < m {\n\t\t\t\ttargetD = memoD[i+1][j]\n\t\t\t}\n\t\t\tif\
        \ targetD != -1 {\n\t\t\t\ttr := targetD / n\n\t\t\t\ttc := targetD % n\n\t\t\
        \t\tdp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD\n\t\t\t}\n\t\t}\n\t}\n\n\treturn\
        \ dp[m-1][n-1]\n}"
      ruby: "# @param {Integer[][]} grid\n# @return {Integer}\ndef unique_paths(grid)\n\
        \  m = grid.length\n  n = grid[0].length\n  mod = 1_000_000_007\n\n  memo_r\
        \ = Array.new(m) { Array.new(n, -1) }\n  memo_d = Array.new(m) { Array.new(n,\
        \ -1) }\n\n  (m - 1).downto(0) do |r|\n    (n - 1).downto(0) do |c|\n      if\
        \ grid[r][c] == 0\n        memo_r[r][c] = r * n + c\n        memo_d[r][c] =\
        \ r * n + c\n      else\n        memo_r[r][c] = memo_d[r + 1][c] if r + 1 <\
        \ m\n        memo_d[r][c] = memo_r[r][c + 1] if c + 1 < n\n      end\n    end\n\
        \  end\n\n  dp = Array.new(m) { Array.new(n, 0) }\n  dp[0][0] = 1\n\n  (0...m).each\
        \ do |i|\n    (0...n).each do |j|\n      next if dp[i][j] == 0\n\n      target_r\
        \ = j + 1 < n ? memo_r[i][j + 1] : -1\n      if target_r != -1\n        tr,\
        \ tc = target_r.divmod(n)\n        dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % mod\n\
        \      end\n\n      target_d = i + 1 < m ? memo_d[i + 1][j] : -1\n      if target_d\
        \ != -1\n        tr, tc = target_d.divmod(n)\n        dp[tr][tc] = (dp[tr][tc]\
        \ + dp[i][j]) % mod\n      end\n    end\n  end\n\n  dp[m - 1][n - 1]\nend"
      scala: "object Solution {\n    def uniquePaths(grid: Array[Array[Int]]): Int =\
        \ {\n        val m = grid.length\n        val n = grid(0).length\n        val\
        \ MOD = 1000000007L\n\n        val memoR = Array.fill(m, n)(-1)\n        val\
        \ memoD = Array.fill(m, n)(-1)\n\n        for (r <- m - 1 to 0 by -1) {\n  \
        \          for (c <- n - 1 to 0 by -1) {\n                if (grid(r)(c) ==\
        \ 0) {\n                    memoR(r)(c) = r * n + c\n                    memoD(r)(c)\
        \ = r * n + c\n                } else {\n                    if (r + 1 < m)\
        \ memoR(r)(c) = memoD(r + 1)(c)\n                    if (c + 1 < n) memoD(r)(c)\
        \ = memoR(r)(c + 1)\n                }\n            }\n        }\n\n       \
        \ val dp = Array.ofDim[Long](m, n)\n        dp(0)(0) = 1L\n\n        for (i\
        \ <- 0 until m) {\n            for (j <- 0 until n) {\n                if (dp(i)(j)\
        \ != 0L) {\n                    val targetR = if (j + 1 < n) memoR(i)(j + 1)\
        \ else -1\n                    if (targetR != -1) {\n                      \
        \  val tr = targetR / n\n                        val tc = targetR % n\n    \
        \                    dp(tr)(tc) = (dp(tr)(tc) + dp(i)(j)) % MOD\n          \
        \          }\n\n                    val targetD = if (i + 1 < m) memoD(i + 1)(j)\
        \ else -1\n                    if (targetD != -1) {\n                      \
        \  val tr = targetD / n\n                        val tc = targetD % n\n    \
        \                    dp(tr)(tc) = (dp(tr)(tc) + dp(i)(j)) % MOD\n          \
        \          }\n                }\n            }\n        }\n\n        dp(m -\
        \ 1)(n - 1).toInt\n    }\n}"
      rust: "impl Solution {\n    pub fn unique_paths(grid: Vec<Vec<i32>>) -> i32 {\n\
        \        let m = grid.len();\n        let n = grid[0].len();\n        let mod_val\
        \ = 1_000_000_007i32;\n\n        let mut memo = vec![-1i32; m * n * 2];\n\n\
        \        for r in (0..m).rev() {\n            for c in (0..n).rev() {\n    \
        \            let idx0 = (r * n + c) * 2;\n                let idx1 = (r * n\
        \ + c) * 2 + 1;\n                if grid[r][c] == 0 {\n                    memo[idx0]\
        \ = (r * n + c) as i32;\n                    memo[idx1] = (r * n + c) as i32;\n\
        \                } else {\n                    if r + 1 < m {\n            \
        \            memo[idx0] = memo[((r + 1) * n + c) * 2 + 1];\n               \
        \     }\n                    if c + 1 < n {\n                        memo[idx1]\
        \ = memo[(r * n + (c + 1)) * 2];\n                    }\n                }\n\
        \            }\n        }\n\n        let mut dp = vec![0i32; m * n];\n     \
        \   dp[0] = 1;\n\n        for r in 0..m {\n            for c in 0..n {\n   \
        \             let ways = dp[r * n + c];\n                if ways == 0 {\n  \
        \                  continue;\n                }\n\n                if c + 1\
        \ < n {\n                    let target_idx = memo[(r * n + (c + 1)) * 2];\n\
        \                    if target_idx != -1 {\n                        let t =\
        \ target_idx as usize;\n                        dp[t] = ((dp[t] as i64 + ways\
        \ as i64) % mod_val as i64) as i32;\n                    }\n               \
        \ }\n\n                if r + 1 < m {\n                    let target_idx =\
        \ memo[((r + 1) * n + c) * 2 + 1];\n                    if target_idx != -1\
        \ {\n                        let t = target_idx as usize;\n                \
        \        dp[t] = ((dp[t] as i64 + ways as i64) % mod_val as i64) as i32;\n \
        \                   }\n                }\n            }\n        }\n\n     \
        \   dp[m * n - 1]\n    }\n}"
      racket: "(define/contract (unique-paths grid)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer?)\n  (let* ([m (length grid)]\n         [n (length (car grid))]\n\
        \         [grid-vec (list->vector (map list->vector grid))]\n         [mod-val\
        \ 1000000007]\n         [memo (make-vector (* m n 2) -1)]\n         [dp (make-vector\
        \ (* m n) 0)])\n\n    (for ([r (in-range (- m 1) -1 -1)])\n      (for ([c (in-range\
        \ (- n 1) -1 -1)])\n        (let ([idx0 (* (+ (* r n) c) 2)]\n             \
        \ [idx1 (+ (* (+ (* r n) c) 2) 1)])\n          (if (= (vector-ref (vector-ref\
        \ grid-vec r) c) 0)\n              (begin\n                (vector-set! memo\
        \ idx0 (+ (* r n) c))\n                (vector-set! memo idx1 (+ (* r n) c)))\n\
        \              (begin\n                (when (< (+ r 1) m)\n               \
        \   (vector-set! memo idx0 (vector-ref memo (+ (* (+ (* (+ r 1) n) c) 2) 1))))\n\
        \                (when (< (+ c 1) n)\n                  (vector-set! memo idx1\
        \ (vector-ref memo (* (+ (* r n) (+ c 1)) 2)))))))))\n\n    (vector-set! dp\
        \ 0 1)\n    (for ([r (in-range m)])\n      (for ([c (in-range n)])\n       \
        \ (let ([ways (vector-ref dp (+ (* r n) c))])\n          (when (> ways 0)\n\
        \            (when (< (+ c 1) n)\n              (let ([target (vector-ref memo\
        \ (* (+ (* r n) (+ c 1)) 2))])\n                (when (>= target 0)\n      \
        \            (vector-set! dp target (modulo (+ (vector-ref dp target) ways)\
        \ mod-val)))))\n            (when (< (+ r 1) m)\n              (let ([target\
        \ (vector-ref memo (+ (* (+ (* (+ r 1) n) c) 2) 1))])\n                (when\
        \ (>= target 0)\n                  (vector-set! dp target (modulo (+ (vector-ref\
        \ dp target) ways) mod-val)))))))))\n\n    (vector-ref dp (- (* m n) 1))))"
      erlang: "-spec unique_paths(Grid :: [[integer()]]) -> integer().\nunique_paths(Grid)\
        \ ->\n    M = length(Grid),\n    N = length(hd(Grid)),\n    GridTuple = list_to_tuple([list_to_tuple(Row)\
        \ || Row <- Grid]),\n    Mod = 1000000007,\n    erlang:erase(),\n\n    lists:foreach(fun(R)\
        \ ->\n        lists:foreach(fun(C) ->\n            Idx0 = (R * N + C) * 2,\n\
        \            Idx1 = (R * N + C) * 2 + 1,\n            Cell = element(C + 1,\
        \ element(R + 1, GridTuple)),\n            if\n                Cell == 0 ->\n\
        \                    erlang:put({memo, Idx0}, R * N + C),\n                \
        \    erlang:put({memo, Idx1}, R * N + C);\n                true ->\n       \
        \             if R + 1 < M ->\n                        NextIdx1 = ((R + 1) *\
        \ N + C) * 2 + 1,\n                        case erlang:get({memo, NextIdx1})\
        \ of\n                            undefined -> ok;\n                       \
        \     V0 -> erlang:put({memo, Idx0}, V0)\n                        end;\n   \
        \                 true -> ok\n                    end,\n                   \
        \ if C + 1 < N ->\n                        NextIdx0 = (R * N + (C + 1)) * 2,\n\
        \                        case erlang:get({memo, NextIdx0}) of\n            \
        \                undefined -> ok;\n                            V1 -> erlang:put({memo,\
        \ Idx1}, V1)\n                        end;\n                    true -> ok\n\
        \                    end\n            end\n        end, lists:seq(N - 1, 0,\
        \ -1))\n    end, lists:seq(M - 1, 0, -1)),\n\n    erlang:put({dp, 0}, 1),\n\
        \    lists:foreach(fun(R) ->\n        lists:foreach(fun(C) ->\n            case\
        \ erlang:get({dp, R * N + C}) of\n                undefined -> ok;\n       \
        \         Ways ->\n                    if C + 1 < N ->\n                   \
        \     case erlang:get({memo, (R * N + (C + 1)) * 2}) of\n                  \
        \          undefined -> ok;\n                            TR ->\n           \
        \                     Old = case erlang:get({dp, TR}) of\n                 \
        \                   undefined -> 0;\n                                    V_Old\
        \ -> V_Old\n                                end,\n                         \
        \       erlang:put({dp, TR}, (Old + Ways) rem Mod)\n                       \
        \ end;\n                    true -> ok\n                    end,\n         \
        \           if R + 1 < M ->\n                        case erlang:get({memo,\
        \ ((R + 1) * N + C) * 2 + 1}) of\n                            undefined -> ok;\n\
        \                            TD ->\n                                Old2 = case\
        \ erlang:get({dp, TD}) of\n                                    undefined ->\
        \ 0;\n                                    V_Old2 -> V_Old2\n               \
        \                 end,\n                                erlang:put({dp, TD},\
        \ (Old2 + Ways) rem Mod)\n                        end;\n                   \
        \ true -> ok\n                    end\n            end\n        end, lists:seq(0,\
        \ N - 1))\n    end, lists:seq(0, M - 1)),\n\n    Result = case erlang:get({dp,\
        \ M * N - 1}) of\n        undefined -> 0;\n        VF -> VF\n    end,\n    erlang:erase(),\n\
        \    Result."
      elixir: "defmodule Solution do\n  @spec unique_paths(grid :: [[integer]]) :: integer\n\
        \  def unique_paths(grid) do\n    m = length(grid)\n    n = length(hd(grid))\n\
        \    grid_tuple = grid |> Enum.map(&List.to_tuple/1) |> List.to_tuple()\n  \
        \  mod = 1_000_000_007\n\n    Process.put(:dp_store, %{})\n    Process.put(:memo_store,\
        \ %{})\n\n    for r <- (m - 1)..0, c <- (n - 1)..0 do\n      idx0 = (r * n +\
        \ c) * 2\n      idx1 = (r * n + c) * 2 + 1\n      if elem(elem(grid_tuple, r),\
        \ c) == 0 do\n        Process.put({:memo, idx0}, r * n + c)\n        Process.put({:memo,\
        \ idx1}, r * n + c)\n      else\n        if r + 1 < m do\n          v0 = Process.get({:memo,\
        \ ((r + 1) * n + c) * 2 + 1})\n          if v0, do: Process.put({:memo, idx0},\
        \ v0)\n        end\n        if c + 1 < n do\n          v1 = Process.get({:memo,\
        \ (r * n + (c + 1)) * 2})\n          if v1, do: Process.put({:memo, idx1}, v1)\n\
        \        end\n      end\n    end\n\n    Process.put({:dp, 0}, 1)\n\n    for\
        \ r <- 0..(m - 1), c <- 0..(n - 1) do\n      ways = Process.get({:dp, r * n\
        \ + c}, 0)\n      if ways > 0 do\n        if c + 1 < n do\n          target_right\
        \ = Process.get({:memo, (r * n + (c + 1)) * 2})\n          if target_right do\n\
        \            old = Process.get({:dp, target_right}, 0)\n            Process.put({:dp,\
        \ target_right}, rem(old + ways, mod))\n          end\n        end\n       \
        \ if r + 1 < m do\n          target_down = Process.get({:memo, ((r + 1) * n\
        \ + c) * 2 + 1})\n          if target_down do\n            old = Process.get({:dp,\
        \ target_down}, 0)\n            Process.put({:dp, target_down}, rem(old + ways,\
        \ mod))\n          end\n        end\n      end\n    end\n\n    res = Process.get({:dp,\
        \ m * n - 1}, 0)\n    res\n  end\nend"
    approach: 'The problem is solved using a combination of jump-target precomputation
      and dynamic programming. For each cell in the grid, we precompute where a robot
      would ultimately land if it attempts to enter that cell from either the left (moving
      right) or the top (moving down). Since a mirror cell reflects the robot into an
      adjacent cell based on its entry direction (right to down, down to right), multiple
      reflections can occur in a chain. We use two memoization tables, `memo_right`
      and `memo_down`, computed in reverse row-major order from the bottom-right of
      the grid to the top-left. If a cell contains a mirror, its landing target is the
      landing target of the cell it reflects into; if it contains a 0, the target is
      the cell itself. If any reflection leads out of bounds, the target is marked as
      invalid.


      After precomputing these jump targets, we use a dynamic programming table `dp`
      where `dp[i][j]` represents the number of unique valid paths to cell `(i, j)`.
      Starting with `dp[0][0] = 1`, we iterate through the grid in row-major order.
      For each reachable cell, we attempt two moves: right and down. By looking up the
      precomputed landing targets for these moves, we add the current path count to
      the `dp` value of the destination cells (modulo $10^9 + 7$). This approach is
      efficient because each move and reflection sequence always moves the robot toward
      a cell with a larger row or column index, preventing cycles and ensuring that
      all possible valid paths are counted correctly.'
    time_complexity: 'O(m \cdot n). We perform two full passes over the $m \times n$
      grid: one to precompute the landing targets and one to update the dynamic programming
      table. Each operation within these passes takes constant time, resulting in a
      linear time complexity relative to the total number of cells.'
    space_complexity: O(m \cdot n). We store two landing-target tables (for entry from
      the left and top) and one dynamic programming table, each of size $m \times n$,
      to store path counts and coordinate data.
    elapsed_time: 350.64808893203735
    model: gemini-3-flash-preview
    generated_at: '2026-10-31 03:36:57 '
---

## Problem #3665: Twisted Mirror Path Count

**Difficulty:** Medium

**Topics:** Array, Dynamic Programming, Matrix

## Problem Description

<p>Given an <code>m x n</code> binary grid <code>grid</code> where:</p>

<ul>
	<li><code>grid[i][j] == 0</code> represents an empty cell, and</li>
	<li><code>grid[i][j] == 1</code> represents a mirror.</li>
</ul>

<p>A robot starts at the top-left corner of the grid <code>(0, 0)</code> and wants to reach the bottom-right corner <code>(m - 1, n - 1)</code>. It can move only <strong>right</strong> or <strong>down</strong>. If the robot attempts to move into a mirror cell, it is <strong>reflected</strong> before entering that cell:</p>

<ul>
	<li>If it tries to move <strong>right</strong> into a mirror, it is turned <strong>down</strong> and moved into the cell directly below the mirror.</li>
	<li>If it tries to move <strong>down</strong> into a mirror, it is turned <strong>right</strong> and moved into the cell directly to the right of the mirror.</li>
</ul>

<p>If this reflection would cause the robot to move outside the <code>grid</code> boundaries, the path is considered invalid and should not be counted.</p>

<p>Return the number of unique valid paths from <code>(0, 0)</code> to <code>(m - 1, n - 1)</code>.</p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p><strong>Note</strong>: If a reflection moves the robot into a mirror cell, the robot is immediately reflected again based on the direction it used to enter that mirror: if it entered while moving right, it will be turned down; if it entered while moving down, it will be turned right. This process will continue until either the last cell is reached, the robot moves out of bounds or the robot moves to a non-mirror cell.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[0,1,0],[0,0,1],[1,0,0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">Number</th>
			<th align="left" style="border: 1px solid black;">Full Path</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="left" style="border: 1px solid black;">(0, 0) &rarr; (0, 1) [M] &rarr; (1, 1) &rarr; (1, 2) [M] &rarr; (2, 2)</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="left" style="border: 1px solid black;">(0, 0) &rarr; (0, 1) [M] &rarr; (1, 1) &rarr; (2, 1) &rarr; (2, 2)</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="left" style="border: 1px solid black;">(0, 0) &rarr; (1, 0) &rarr; (1, 1) &rarr; (1, 2) [M] &rarr; (2, 2)</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">4</td>
			<td align="left" style="border: 1px solid black;">(0, 0) &rarr; (1, 0) &rarr; (1, 1) &rarr; (2, 1) &rarr; (2, 2)</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">5</td>
			<td align="left" style="border: 1px solid black;">(0, 0) &rarr; (1, 0) &rarr; (2, 0) [M] &rarr; (2, 1) &rarr; (2, 2)</td>
		</tr>
	</tbody>
</table>

<ul data-end="606" data-start="521">
	<li data-end="606" data-start="521">
	<p data-end="606" data-start="523"><code>[M]</code> indicates the robot attempted to enter a mirror cell and instead reflected.</p>
	</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[0,0],[0,0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">Number</th>
			<th align="left" style="border: 1px solid black;">Full Path</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="left" style="border: 1px solid black;">(0, 0) &rarr; (0, 1) &rarr; (1, 1)</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="left" style="border: 1px solid black;">(0, 0) &rarr; (1, 0) &rarr; (1, 1)</td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = </span>[[0,1,1],[1,1,0]]</p>

<p><strong>Output:</strong> 1</p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">Number</th>
			<th align="left" style="border: 1px solid black;">Full Path</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="left" style="border: 1px solid black;">(0, 0) &rarr; (0, 1) [M] &rarr; (1, 1) [M] &rarr; (1, 2)</td>
		</tr>
	</tbody>
</table>
<code>(0, 0) &rarr; (1, 0) [M] &rarr; (1, 1) [M] &rarr; (2, 1)</code> goes out of bounds, so it is invalid.</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li data-end="41" data-start="21"><code data-end="39" data-start="21">m == grid.length</code></li>
	<li data-end="67" data-start="44"><code data-end="65" data-start="44">n == grid[i].length</code></li>
	<li data-end="91" data-start="70"><code data-end="89" data-start="70">2 &lt;= m, n &lt;= 500</code></li>
	<li data-end="129" data-start="94"><code data-end="106" data-start="94">grid[i][j]</code> is either <code data-end="120" data-is-only-node="" data-start="117">0</code> or <code data-end="127" data-start="124">1</code>.</li>
	<li data-end="169" data-start="132"><code data-end="167" data-start="132">grid[0][0] == grid[m - 1][n - 1] == 0</code></li>
</ul>


## Hints

1. Precompute, for each cell and each move (right/down), where you actually land if there’s a mirror next—store these "jump" targets in a `go[i][j][0/1]` table.

2. Let `dp[i][j]` = number of ways to reach (i,j); set `dp[0][0] = 1`, then scan cells in row‑major order and for each `dp[i][j] > 0` add `dp[i][j]` into `dp[x][y]` for both precomputed moves.

3. Always take additions modulo `10^9+7`, and skip any jump target that falls outside the grid.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem is solved using a combination of jump-target precomputation and dynamic programming. For each cell in the grid, we precompute where a robot would ultimately land if it attempts to enter that cell from either the left (moving right) or the top (moving down). Since a mirror cell reflects the robot into an adjacent cell based on its entry direction (right to down, down to right), multiple reflections can occur in a chain. We use two memoization tables, `memo_right` and `memo_down`, computed in reverse row-major order from the bottom-right of the grid to the top-left. If a cell contains a mirror, its landing target is the landing target of the cell it reflects into; if it contains a 0, the target is the cell itself. If any reflection leads out of bounds, the target is marked as invalid.

After precomputing these jump targets, we use a dynamic programming table `dp` where `dp[i][j]` represents the number of unique valid paths to cell `(i, j)`. Starting with `dp[0][0] = 1`, we iterate through the grid in row-major order. For each reachable cell, we attempt two moves: right and down. By looking up the precomputed landing targets for these moves, we add the current path count to the `dp` value of the destination cells (modulo $10^9 + 7$). This approach is efficient because each move and reflection sequence always moves the robot toward a cell with a larger row or column index, preventing cycles and ensuring that all possible valid paths are counted correctly.

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
    int uniquePaths(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int MOD = 1000000007;

        struct Pos {
            int r, c;
        };

        vector<vector<Pos>> memo_right(m, vector<Pos>(n, {-1, -1}));
        vector<vector<Pos>> memo_down(m, vector<Pos>(n, {-1, -1}));

        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (grid[i][j] == 0) {
                    memo_right[i][j] = {i, j};
                    memo_down[i][j] = {i, j};
                } else {
                    if (i + 1 < m) memo_right[i][j] = memo_down[i + 1][j];
                    if (j + 1 < n) memo_down[i][j] = memo_right[i][j + 1];
                }
            }
        }

        vector<vector<int>> dp(m, vector<int>(n, 0));
        dp[0][0] = 1;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (dp[i][j] == 0) continue;

                if (j + 1 < n) {
                    Pos target = memo_right[i][j + 1];
                    if (target.r != -1) {
                        dp[target.r][target.c] = (dp[target.r][target.c] + dp[i][j]) % MOD;
                    }
                }

                if (i + 1 < m) {
                    Pos target = memo_down[i + 1][j];
                    if (target.r != -1) {
                        dp[target.r][target.c] = (dp[target.r][target.c] + dp[i][j]) % MOD;
                    }
                }
            }
        }

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
    public int uniquePaths(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int MOD = 1000000007;

        int[][] memoRightR = new int[m][n];
        int[][] memoRightC = new int[m][n];
        int[][] memoDownR = new int[m][n];
        int[][] memoDownC = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                memoRightR[i][j] = memoDownR[i][j] = -1;
            }
        }

        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i][j] == 0) {
                    memoRightR[i][j] = memoDownR[i][j] = i;
                    memoRightC[i][j] = memoDownC[i][j] = j;
                } else {
                    if (i + 1 < m) {
                        memoRightR[i][j] = memoDownR[i + 1][j];
                        memoRightC[i][j] = memoDownC[i + 1][j];
                    }
                    if (j + 1 < n) {
                        memoDownR[i][j] = memoRightR[i][j + 1];
                        memoDownC[i][j] = memoRightC[i][j + 1];
                    }
                }
            }
        }

        int[][] dp = new int[m][n];
        dp[0][0] = 1;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dp[i][j] == 0) continue;

                if (j + 1 < n) {
                    int tr = memoRightR[i][j + 1];
                    int tc = memoRightC[i][j + 1];
                    if (tr != -1) {
                        dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD;
                    }
                }

                if (i + 1 < m) {
                    int tr = memoDownR[i + 1][j];
                    int tc = memoDownC[i + 1][j];
                    if (tr != -1) {
                        dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD;
                    }
                }
            }
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
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        MOD = 1000000007

        memo_right = [[(-1, -1) for _ in range(n)] for _ in range(m)]
        memo_down = [[(-1, -1) for _ in range(n)] for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    memo_right[i][j] = (i, j)
                    memo_down[i][j] = (i, j)
                else:
                    if i + 1 < m:
                        memo_right[i][j] = memo_down[i + 1][j]
                    if j + 1 < n:
                        memo_down[i][j] = memo_right[i][j + 1]

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue

                if j + 1 < n:
                    tr, tc = memo_right[i][j + 1]
                    if tr != -1:
                        dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD

                if i + 1 < m:
                    tr, tc = memo_down[i + 1][j]
                    if tr != -1:
                        dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD

        return dp[m - 1][n - 1]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7

        memo_right = [[(-1, -1) for _ in range(n)] for _ in range(m)]
        memo_down = [[(-1, -1) for _ in range(n)] for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    memo_right[i][j] = (i, j)
                    memo_down[i][j] = (i, j)
                else:
                    if i + 1 < m:
                        memo_right[i][j] = memo_down[i + 1][j]
                    if j + 1 < n:
                        memo_down[i][j] = memo_right[i][j + 1]

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue

                if j + 1 < n:
                    tr, tc = memo_right[i][j + 1]
                    if tr != -1:
                        dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD

                if i + 1 < m:
                    tr, tc = memo_down[i + 1][j]
                    if tr != -1:
                        dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD

        return dp[m - 1][n - 1]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int uniquePaths(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];
    int MOD = 1000000007;

    int* memoRightR = (int*)malloc(m * n * sizeof(int));
    int* memoRightC = (int*)malloc(m * n * sizeof(int));
    int* memoDownR = (int*)malloc(m * n * sizeof(int));
    int* memoDownC = (int*)malloc(m * n * sizeof(int));

    for (int i = 0; i < m * n; i++) {
        memoRightR[i] = -1;
        memoDownR[i] = -1;
    }

    for (int i = m - 1; i >= 0; i--) {
        for (int j = n - 1; j >= 0; j--) {
            int idx = i * n + j;
            if (grid[i][j] == 0) {
                memoRightR[idx] = memoDownR[idx] = i;
                memoRightC[idx] = memoDownC[idx] = j;
            } else {
                if (i + 1 < m) {
                    memoRightR[idx] = memoDownR[(i + 1) * n + j];
                    memoRightC[idx] = memoDownC[(i + 1) * n + j];
                }
                if (j + 1 < n) {
                    memoDownR[idx] = memoRightR[i * n + (j + 1)];
                    memoDownC[idx] = memoRightC[i * n + (j + 1)];
                }
            }
        }
    }

    int* dp = (int*)calloc(m * n, sizeof(int));
    dp[0] = 1;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int idx = i * n + j;
            if (dp[idx] == 0) continue;

            if (j + 1 < n) {
                int tr = memoRightR[i * n + (j + 1)];
                int tc = memoRightC[i * n + (j + 1)];
                if (tr != -1) {
                    int t_idx = tr * n + tc;
                    dp[t_idx] = (dp[t_idx] + dp[idx]) % MOD;
                }
            }

            if (i + 1 < m) {
                int tr = memoDownR[(i + 1) * n + j];
                int tc = memoDownC[(i + 1) * n + j];
                if (tr != -1) {
                    int t_idx = tr * n + tc;
                    dp[t_idx] = (dp[t_idx] + dp[idx]) % MOD;
                }
            }
        }
    }

    int result = dp[m * n - 1];
    free(memoRightR);
    free(memoRightC);
    free(memoDownR);
    free(memoDownC);
    free(dp);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int UniquePaths(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int MOD = 1000000007;

        int[,] fRightRow = new int[m, n];
        int[,] fRightCol = new int[m, n];
        int[,] fDownRow = new int[m, n];
        int[,] fDownCol = new int[m, n];

        for (int r = m - 1; r >= 0; r--) {
            for (int c = n - 1; c >= 0; c--) {
                if (grid[r][c] == 0) {
                    fRightRow[r, c] = r;
                    fRightCol[r, c] = c;
                    fDownRow[r, c] = r;
                    fDownCol[r, c] = c;
                } else {
                    if (r + 1 < m) {
                        fRightRow[r, c] = fDownRow[r + 1, c];
                        fRightCol[r, c] = fDownCol[r + 1, c];
                    } else {
                        fRightRow[r, c] = -1;
                        fRightCol[r, c] = -1;
                    }
                    if (c + 1 < n) {
                        fDownRow[r, c] = fRightRow[r, c + 1];
                        fDownCol[r, c] = fRightCol[r, c + 1];
                    } else {
                        fDownRow[r, c] = -1;
                        fDownCol[r, c] = -1;
                    }
                }
            }
        }

        int[,] dp = new int[m, n];
        dp[0, 0] = 1;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (dp[r, c] == 0) continue;

                if (c + 1 < n) {
                    int nr = fRightRow[r, c + 1];
                    int nc = fRightCol[r, c + 1];
                    if (nr != -1) {
                        dp[nr, nc] = (dp[nr, nc] + dp[r, c]) % MOD;
                    }
                }

                if (r + 1 < m) {
                    int nr = fDownRow[r + 1, c];
                    int nc = fDownCol[r + 1, c];
                    if (nr != -1) {
                        dp[nr, nc] = (dp[nr, nc] + dp[r, c]) % MOD;
                    }
                }
            }
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
/**
 * @param {number[][]} grid
 * @return {number}
 */
var uniquePaths = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const MOD = 1000000007;

    const fRightRow = Array.from({ length: m }, () => new Int32Array(n).fill(-1));
    const fRightCol = Array.from({ length: m }, () => new Int32Array(n).fill(-1));
    const fDownRow = Array.from({ length: m }, () => new Int32Array(n).fill(-1));
    const fDownCol = Array.from({ length: m }, () => new Int32Array(n).fill(-1));

    for (let r = m - 1; r >= 0; r--) {
        for (let c = n - 1; c >= 0; c--) {
            if (grid[r][c] === 0) {
                fRightRow[r][c] = r;
                fRightCol[r][c] = c;
                fDownRow[r][c] = r;
                fDownCol[r][c] = c;
            } else {
                if (r + 1 < m) {
                    fRightRow[r][c] = fDownRow[r + 1][c];
                    fRightCol[r][c] = fDownCol[r + 1][c];
                }
                if (c + 1 < n) {
                    fDownRow[r][c] = fRightRow[r][c + 1];
                    fDownCol[r][c] = fRightCol[r][c + 1];
                }
            }
        }
    }

    const dp = Array.from({ length: m }, () => new Int32Array(n).fill(0));
    dp[0][0] = 1;

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (dp[r][c] === 0) continue;

            if (c + 1 < n) {
                const nr = fRightRow[r][c + 1];
                const nc = fRightCol[r][c + 1];
                if (nr !== -1) {
                    dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD;
                }
            }

            if (r + 1 < m) {
                const nr = fDownRow[r + 1][c];
                const nc = fDownCol[r + 1][c];
                if (nr !== -1) {
                    dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD;
                }
            }
        }
    }

    return dp[m - 1][n - 1];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function uniquePaths(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const MOD = 1000000007;

    const fRightRow: Int32Array[] = Array.from({ length: m }, () => new Int32Array(n).fill(-1));
    const fRightCol: Int32Array[] = Array.from({ length: m }, () => new Int32Array(n).fill(-1));
    const fDownRow: Int32Array[] = Array.from({ length: m }, () => new Int32Array(n).fill(-1));
    const fDownCol: Int32Array[] = Array.from({ length: m }, () => new Int32Array(n).fill(-1));

    for (let r = m - 1; r >= 0; r--) {
        for (let c = n - 1; c >= 0; c--) {
            if (grid[r][c] === 0) {
                fRightRow[r][c] = r;
                fRightCol[r][c] = c;
                fDownRow[r][c] = r;
                fDownCol[r][c] = c;
            } else {
                if (r + 1 < m) {
                    fRightRow[r][c] = fDownRow[r + 1][c];
                    fRightCol[r][c] = fDownCol[r + 1][c];
                }
                if (c + 1 < n) {
                    fDownRow[r][c] = fRightRow[r][c + 1];
                    fDownCol[r][c] = fRightCol[r][c + 1];
                }
            }
        }
    }

    const dp: Int32Array[] = Array.from({ length: m }, () => new Int32Array(n).fill(0));
    dp[0][0] = 1;

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (dp[r][c] === 0) continue;

            if (c + 1 < n) {
                const nr = fRightRow[r][c + 1];
                const nc = fRightCol[r][c + 1];
                if (nr !== -1) {
                    dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD;
                }
            }

            if (r + 1 < m) {
                const nr = fDownRow[r + 1][c];
                const nc = fDownCol[r + 1][c];
                if (nr !== -1) {
                    dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD;
                }
            }
        }
    }

    return dp[m - 1][n - 1];
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
    function uniquePaths($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $MOD = 1000000007;

        $fRightRow = array_fill(0, $m, array_fill(0, $n, -1));
        $fRightCol = array_fill(0, $m, array_fill(0, $n, -1));
        $fDownRow = array_fill(0, $m, array_fill(0, $n, -1));
        $fDownCol = array_fill(0, $m, array_fill(0, $n, -1));

        for ($r = $m - 1; $r >= 0; $r--) {
            for ($c = $n - 1; $c >= 0; $c--) {
                if ($grid[$r][$c] == 0) {
                    $fRightRow[$r][$c] = $r;
                    $fRightCol[$r][$c] = $c;
                    $fDownRow[$r][$c] = $r;
                    $fDownCol[$r][$c] = $c;
                } else {
                    if ($r + 1 < $m) {
                        $fRightRow[$r][$c] = $fDownRow[$r + 1][$c];
                        $fRightCol[$r][$c] = $fDownCol[$r + 1][$c];
                    }
                    if ($c + 1 < $n) {
                        $fDownRow[$r][$c] = $fRightRow[$r][$c + 1];
                        $fDownCol[$r][$c] = $fRightCol[$r][$c + 1];
                    }
                }
            }
        }

        $dp = array_fill(0, $m, array_fill(0, $n, 0));
        $dp[0][0] = 1;

        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($dp[$r][$c] == 0) continue;

                if ($c + 1 < $n) {
                    $nr = $fRightRow[$r][$c + 1];
                    $nc = $fRightCol[$r][$c + 1];
                    if ($nr != -1) {
                        $dp[$nr][$nc] = ($dp[$nr][$nc] + $dp[$r][$c]) % $MOD;
                    }
                }

                if ($r + 1 < $m) {
                    $nr = $fDownRow[$r + 1][$c];
                    $nc = $fDownCol[$r + 1][$c];
                    if ($nr != -1) {
                        $dp[$nr][$nc] = ($dp[$nr][$nc] + $dp[$r][$c]) % $MOD;
                    }
                }
            }
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
    func uniquePaths(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        let MOD = 1000000007

        var fRightRow = Array(repeating: Array(repeating: -1, count: n), count: m)
        var fRightCol = Array(repeating: Array(repeating: -1, count: n), count: m)
        var fDownRow = Array(repeating: Array(repeating: -1, count: n), count: m)
        var fDownCol = Array(repeating: Array(repeating: -1, count: n), count: m)

        for r in (0..<m).reversed() {
            for c in (0..<n).reversed() {
                if grid[r][c] == 0 {
                    fRightRow[r][c] = r
                    fRightCol[r][c] = c
                    fDownRow[r][c] = r
                    fDownCol[r][c] = c
                } else {
                    if r + 1 < m {
                        fRightRow[r][c] = fDownRow[r + 1][c]
                        fRightCol[r][c] = fDownCol[r + 1][c]
                    }
                    if c + 1 < n {
                        fDownRow[r][c] = fRightRow[r][c + 1]
                        fDownCol[r][c] = fRightCol[r][c + 1]
                    }
                }
            }
        }

        var dp = Array(repeating: Array(repeating: 0, count: n), count: m)
        dp[0][0] = 1

        for r in 0..<m {
            for c in 0..<n {
                if dp[r][c] == 0 { continue }

                if c + 1 < n {
                    let nr = fRightRow[r][c + 1]
                    let nc = fRightCol[r][c + 1]
                    if nr != -1 {
                        dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD
                    }
                }

                if r + 1 < m {
                    let nr = fDownRow[r + 1][c]
                    let nc = fDownCol[r + 1][c]
                    if nr != -1 {
                        dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD
                    }
                }
            }
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
    fun uniquePaths(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val MOD = 1000000007L

        val memoR = Array(m) { IntArray(n) { -1 } }
        val memoD = Array(m) { IntArray(n) { -1 } }

        for (r in m - 1 downTo 0) {
            for (c in n - 1 downTo 0) {
                if (grid[r][c] == 0) {
                    memoR[r][c] = r * n + c
                    memoD[r][c] = r * n + c
                } else {
                    if (r + 1 < m) memoR[r][c] = memoD[r + 1][c]
                    if (c + 1 < n) memoD[r][c] = memoR[r][c + 1]
                }
            }
        }

        val dp = Array(m) { LongArray(n) }
        dp[0][0] = 1

        for (i in 0 until m) {
            for (j in 0 until n) {
                if (dp[i][j] == 0L) continue

                val targetR = if (j + 1 < n) memoR[i][j + 1] else -1
                if (targetR != -1) {
                    val tr = targetR / n
                    val tc = targetR % n
                    dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD
                }

                val targetD = if (i + 1 < m) memoD[i + 1][j] else -1
                if (targetD != -1) {
                    val tr = targetD / n
                    val tc = targetD % n
                    dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD
                }
            }
        }

        return dp[m - 1][n - 1].toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int uniquePaths(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    int MOD = 1000000007;

    List<List<int>> memoR = List.generate(m, (_) => List.filled(n, -1));
    List<List<int>> memoD = List.generate(m, (_) => List.filled(n, -1));

    for (int r = m - 1; r >= 0; r--) {
      for (int c = n - 1; c >= 0; c--) {
        if (grid[r][c] == 0) {
          memoR[r][c] = r * n + c;
          memoD[r][c] = r * n + c;
        } else {
          if (r + 1 < m) memoR[r][c] = memoD[r + 1][c];
          if (c + 1 < n) memoD[r][c] = memoR[r][c + 1];
        }
      }
    }

    List<List<int>> dp = List.generate(m, (_) => List.filled(n, 0));
    dp[0][0] = 1;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (dp[i][j] == 0) continue;

        int targetR = (j + 1 < n) ? memoR[i][j + 1] : -1;
        if (targetR != -1) {
          int tr = targetR ~/ n;
          int tc = targetR % n;
          dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD;
        }

        int targetD = (i + 1 < m) ? memoD[i + 1][j] : -1;
        if (targetD != -1) {
          int tr = targetD ~/ n;
          int tc = targetD % n;
          dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD;
        }
      }
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
func uniquePaths(grid [][]int) int {
	m := len(grid)
	n := len(grid[0])
	MOD := 1000000007

	memoR := make([][]int, m)
	memoD := make([][]int, m)
	for i := 0; i < m; i++ {
		memoR[i] = make([]int, n)
		memoD[i] = make([]int, n)
		for j := 0; j < n; j++ {
			memoR[i][j] = -1
			memoD[i][j] = -1
		}
	}

	for r := m - 1; r >= 0; r-- {
		for c := n - 1; c >= 0; c-- {
			if grid[r][c] == 0 {
				memoR[r][c] = r*n + c
				memoD[r][c] = r*n + c
			} else {
				if r+1 < m {
					memoR[r][c] = memoD[r+1][c]
				}
				if c+1 < n {
					memoD[r][c] = memoR[r][c+1]
				}
			}
		}
	}

	dp := make([][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int, n)
	}
	dp[0][0] = 1

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if dp[i][j] == 0 {
				continue
			}

			targetR := -1
			if j+1 < n {
				targetR = memoR[i][j+1]
			}
			if targetR != -1 {
				tr := targetR / n
				tc := targetR % n
				dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD
			}

			targetD := -1
			if i+1 < m {
				targetD = memoD[i+1][j]
			}
			if targetD != -1 {
				tr := targetD / n
				tc := targetD % n
				dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD
			}
		}
	}

	return dp[m-1][n-1]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[][]} grid
# @return {Integer}
def unique_paths(grid)
  m = grid.length
  n = grid[0].length
  mod = 1_000_000_007

  memo_r = Array.new(m) { Array.new(n, -1) }
  memo_d = Array.new(m) { Array.new(n, -1) }

  (m - 1).downto(0) do |r|
    (n - 1).downto(0) do |c|
      if grid[r][c] == 0
        memo_r[r][c] = r * n + c
        memo_d[r][c] = r * n + c
      else
        memo_r[r][c] = memo_d[r + 1][c] if r + 1 < m
        memo_d[r][c] = memo_r[r][c + 1] if c + 1 < n
      end
    end
  end

  dp = Array.new(m) { Array.new(n, 0) }
  dp[0][0] = 1

  (0...m).each do |i|
    (0...n).each do |j|
      next if dp[i][j] == 0

      target_r = j + 1 < n ? memo_r[i][j + 1] : -1
      if target_r != -1
        tr, tc = target_r.divmod(n)
        dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % mod
      end

      target_d = i + 1 < m ? memo_d[i + 1][j] : -1
      if target_d != -1
        tr, tc = target_d.divmod(n)
        dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % mod
      end
    end
  end

  dp[m - 1][n - 1]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def uniquePaths(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        val n = grid(0).length
        val MOD = 1000000007L

        val memoR = Array.fill(m, n)(-1)
        val memoD = Array.fill(m, n)(-1)

        for (r <- m - 1 to 0 by -1) {
            for (c <- n - 1 to 0 by -1) {
                if (grid(r)(c) == 0) {
                    memoR(r)(c) = r * n + c
                    memoD(r)(c) = r * n + c
                } else {
                    if (r + 1 < m) memoR(r)(c) = memoD(r + 1)(c)
                    if (c + 1 < n) memoD(r)(c) = memoR(r)(c + 1)
                }
            }
        }

        val dp = Array.ofDim[Long](m, n)
        dp(0)(0) = 1L

        for (i <- 0 until m) {
            for (j <- 0 until n) {
                if (dp(i)(j) != 0L) {
                    val targetR = if (j + 1 < n) memoR(i)(j + 1) else -1
                    if (targetR != -1) {
                        val tr = targetR / n
                        val tc = targetR % n
                        dp(tr)(tc) = (dp(tr)(tc) + dp(i)(j)) % MOD
                    }

                    val targetD = if (i + 1 < m) memoD(i + 1)(j) else -1
                    if (targetD != -1) {
                        val tr = targetD / n
                        val tc = targetD % n
                        dp(tr)(tc) = (dp(tr)(tc) + dp(i)(j)) % MOD
                    }
                }
            }
        }

        dp(m - 1)(n - 1).toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn unique_paths(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mod_val = 1_000_000_007i32;

        let mut memo = vec![-1i32; m * n * 2];

        for r in (0..m).rev() {
            for c in (0..n).rev() {
                let idx0 = (r * n + c) * 2;
                let idx1 = (r * n + c) * 2 + 1;
                if grid[r][c] == 0 {
                    memo[idx0] = (r * n + c) as i32;
                    memo[idx1] = (r * n + c) as i32;
                } else {
                    if r + 1 < m {
                        memo[idx0] = memo[((r + 1) * n + c) * 2 + 1];
                    }
                    if c + 1 < n {
                        memo[idx1] = memo[(r * n + (c + 1)) * 2];
                    }
                }
            }
        }

        let mut dp = vec![0i32; m * n];
        dp[0] = 1;

        for r in 0..m {
            for c in 0..n {
                let ways = dp[r * n + c];
                if ways == 0 {
                    continue;
                }

                if c + 1 < n {
                    let target_idx = memo[(r * n + (c + 1)) * 2];
                    if target_idx != -1 {
                        let t = target_idx as usize;
                        dp[t] = ((dp[t] as i64 + ways as i64) % mod_val as i64) as i32;
                    }
                }

                if r + 1 < m {
                    let target_idx = memo[((r + 1) * n + c) * 2 + 1];
                    if target_idx != -1 {
                        let t = target_idx as usize;
                        dp[t] = ((dp[t] as i64 + ways as i64) % mod_val as i64) as i32;
                    }
                }
            }
        }

        dp[m * n - 1]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (unique-paths grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([m (length grid)]
         [n (length (car grid))]
         [grid-vec (list->vector (map list->vector grid))]
         [mod-val 1000000007]
         [memo (make-vector (* m n 2) -1)]
         [dp (make-vector (* m n) 0)])

    (for ([r (in-range (- m 1) -1 -1)])
      (for ([c (in-range (- n 1) -1 -1)])
        (let ([idx0 (* (+ (* r n) c) 2)]
              [idx1 (+ (* (+ (* r n) c) 2) 1)])
          (if (= (vector-ref (vector-ref grid-vec r) c) 0)
              (begin
                (vector-set! memo idx0 (+ (* r n) c))
                (vector-set! memo idx1 (+ (* r n) c)))
              (begin
                (when (< (+ r 1) m)
                  (vector-set! memo idx0 (vector-ref memo (+ (* (+ (* (+ r 1) n) c) 2) 1))))
                (when (< (+ c 1) n)
                  (vector-set! memo idx1 (vector-ref memo (* (+ (* r n) (+ c 1)) 2)))))))))

    (vector-set! dp 0 1)
    (for ([r (in-range m)])
      (for ([c (in-range n)])
        (let ([ways (vector-ref dp (+ (* r n) c))])
          (when (> ways 0)
            (when (< (+ c 1) n)
              (let ([target (vector-ref memo (* (+ (* r n) (+ c 1)) 2))])
                (when (>= target 0)
                  (vector-set! dp target (modulo (+ (vector-ref dp target) ways) mod-val)))))
            (when (< (+ r 1) m)
              (let ([target (vector-ref memo (+ (* (+ (* (+ r 1) n) c) 2) 1))])
                (when (>= target 0)
                  (vector-set! dp target (modulo (+ (vector-ref dp target) ways) mod-val)))))))))

    (vector-ref dp (- (* m n) 1))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec unique_paths(Grid :: [[integer()]]) -> integer().
unique_paths(Grid) ->
    M = length(Grid),
    N = length(hd(Grid)),
    GridTuple = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),
    Mod = 1000000007,
    erlang:erase(),

    lists:foreach(fun(R) ->
        lists:foreach(fun(C) ->
            Idx0 = (R * N + C) * 2,
            Idx1 = (R * N + C) * 2 + 1,
            Cell = element(C + 1, element(R + 1, GridTuple)),
            if
                Cell == 0 ->
                    erlang:put({memo, Idx0}, R * N + C),
                    erlang:put({memo, Idx1}, R * N + C);
                true ->
                    if R + 1 < M ->
                        NextIdx1 = ((R + 1) * N + C) * 2 + 1,
                        case erlang:get({memo, NextIdx1}) of
                            undefined -> ok;
                            V0 -> erlang:put({memo, Idx0}, V0)
                        end;
                    true -> ok
                    end,
                    if C + 1 < N ->
                        NextIdx0 = (R * N + (C + 1)) * 2,
                        case erlang:get({memo, NextIdx0}) of
                            undefined -> ok;
                            V1 -> erlang:put({memo, Idx1}, V1)
                        end;
                    true -> ok
                    end
            end
        end, lists:seq(N - 1, 0, -1))
    end, lists:seq(M - 1, 0, -1)),

    erlang:put({dp, 0}, 1),
    lists:foreach(fun(R) ->
        lists:foreach(fun(C) ->
            case erlang:get({dp, R * N + C}) of
                undefined -> ok;
                Ways ->
                    if C + 1 < N ->
                        case erlang:get({memo, (R * N + (C + 1)) * 2}) of
                            undefined -> ok;
                            TR ->
                                Old = case erlang:get({dp, TR}) of
                                    undefined -> 0;
                                    V_Old -> V_Old
                                end,
                                erlang:put({dp, TR}, (Old + Ways) rem Mod)
                        end;
                    true -> ok
                    end,
                    if R + 1 < M ->
                        case erlang:get({memo, ((R + 1) * N + C) * 2 + 1}) of
                            undefined -> ok;
                            TD ->
                                Old2 = case erlang:get({dp, TD}) of
                                    undefined -> 0;
                                    V_Old2 -> V_Old2
                                end,
                                erlang:put({dp, TD}, (Old2 + Ways) rem Mod)
                        end;
                    true -> ok
                    end
            end
        end, lists:seq(0, N - 1))
    end, lists:seq(0, M - 1)),

    Result = case erlang:get({dp, M * N - 1}) of
        undefined -> 0;
        VF -> VF
    end,
    erlang:erase(),
    Result.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec unique_paths(grid :: [[integer]]) :: integer
  def unique_paths(grid) do
    m = length(grid)
    n = length(hd(grid))
    grid_tuple = grid |> Enum.map(&List.to_tuple/1) |> List.to_tuple()
    mod = 1_000_000_007

    Process.put(:dp_store, %{})
    Process.put(:memo_store, %{})

    for r <- (m - 1)..0, c <- (n - 1)..0 do
      idx0 = (r * n + c) * 2
      idx1 = (r * n + c) * 2 + 1
      if elem(elem(grid_tuple, r), c) == 0 do
        Process.put({:memo, idx0}, r * n + c)
        Process.put({:memo, idx1}, r * n + c)
      else
        if r + 1 < m do
          v0 = Process.get({:memo, ((r + 1) * n + c) * 2 + 1})
          if v0, do: Process.put({:memo, idx0}, v0)
        end
        if c + 1 < n do
          v1 = Process.get({:memo, (r * n + (c + 1)) * 2})
          if v1, do: Process.put({:memo, idx1}, v1)
        end
      end
    end

    Process.put({:dp, 0}, 1)

    for r <- 0..(m - 1), c <- 0..(n - 1) do
      ways = Process.get({:dp, r * n + c}, 0)
      if ways > 0 do
        if c + 1 < n do
          target_right = Process.get({:memo, (r * n + (c + 1)) * 2})
          if target_right do
            old = Process.get({:dp, target_right}, 0)
            Process.put({:dp, target_right}, rem(old + ways, mod))
          end
        end
        if r + 1 < m do
          target_down = Process.get({:memo, ((r + 1) * n + c) * 2 + 1})
          if target_down do
            old = Process.get({:dp, target_down}, 0)
            Process.put({:dp, target_down}, rem(old + ways, mod))
          end
        end
      end
    end

    res = Process.get({:dp, m * n - 1}, 0)
    res
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m \cdot n). We perform two full passes over the $m \times n$ grid: one to precompute the landing targets and one to update the dynamic programming table. Each operation within these passes takes constant time, resulting in a linear time complexity relative to the total number of cells.
- **Space Complexity:** O(m \cdot n). We store two landing-target tables (for entry from the left and top) and one dynamic programming table, each of size $m \times n$, to store path counts and coordinate data.
