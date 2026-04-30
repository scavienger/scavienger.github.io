---
layout: post
title: "Maximum Path Score in a Grid"
date: 2026-04-30 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Dynamic Programming", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-path-score-in-a-grid/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxPathScore(vector<vector<int>>& grid,\
        \ int k) {\n        int m = grid.size();\n        int n = grid[0].size();\n\
        \        int k_limit = min(k, m + n);\n        vector<vector<int>> dp(n, vector<int>(k_limit\
        \ + 1, -1));\n        dp[0][0] = 0;\n\n        for (int i = 0; i < m; ++i) {\n\
        \            vector<vector<int>> next_dp(n, vector<int>(k_limit + 1, -1));\n\
        \            for (int j = 0; j < n; ++j) {\n                if (i == 0 && j\
        \ == 0) {\n                    next_dp[0][0] = 0;\n                    continue;\n\
        \                }\n                int cost_inc = (grid[i][j] > 0 ? 1 : 0);\n\
        \                int score_inc = grid[i][j];\n                int local_limit\
        \ = min(k_limit, i + j);\n\n                for (int c = cost_inc; c <= local_limit;\
        \ ++c) {\n                    int best_prev = -1;\n                    if (i\
        \ > 0) best_prev = max(best_prev, dp[j][c - cost_inc]);\n                  \
        \  if (j > 0) best_prev = max(best_prev, next_dp[j - 1][c - cost_inc]);\n\n\
        \                    if (best_prev != -1) {\n                        next_dp[j][c]\
        \ = best_prev + score_inc;\n                    }\n                }\n     \
        \       }\n            dp.swap(next_dp);\n        }\n\n        int max_score\
        \ = -1;\n        for (int c = 0; c <= k_limit; ++c) {\n            max_score\
        \ = max(max_score, dp[n - 1][c]);\n        }\n        return max_score;\n  \
        \  }\n};"
      java: "class Solution {\n    public int maxPathScore(int[][] grid, int k) {\n\
        \        int m = grid.length;\n        int n = grid[0].length;\n        int\
        \ kLimit = Math.min(k, m + n);\n        int[][] dp = new int[n][kLimit + 1];\n\
        \        for (int i = 0; i < n; i++) {\n            java.util.Arrays.fill(dp[i],\
        \ -1);\n        }\n        dp[0][0] = 0;\n\n        for (int i = 0; i < m; i++)\
        \ {\n            int[][] nextDp = new int[n][kLimit + 1];\n            for (int\
        \ j = 0; j < n; j++) {\n                java.util.Arrays.fill(nextDp[j], -1);\n\
        \                if (i == 0 && j == 0) {\n                    nextDp[0][0] =\
        \ 0;\n                    continue;\n                }\n                int\
        \ costInc = (grid[i][j] > 0 ? 1 : 0);\n                int scoreInc = grid[i][j];\n\
        \                int localLimit = Math.min(kLimit, i + j);\n\n             \
        \   for (int c = costInc; c <= localLimit; c++) {\n                    int bestPrev\
        \ = -1;\n                    if (i > 0) bestPrev = Math.max(bestPrev, dp[j][c\
        \ - costInc]);\n                    if (j > 0) bestPrev = Math.max(bestPrev,\
        \ nextDp[j - 1][c - costInc]);\n\n                    if (bestPrev != -1) {\n\
        \                        nextDp[j][c] = bestPrev + scoreInc;\n             \
        \       }\n                }\n            }\n            dp = nextDp;\n    \
        \    }\n\n        int maxScore = -1;\n        for (int c = 0; c <= kLimit; c++)\
        \ {\n            maxScore = Math.max(maxScore, dp[n - 1][c]);\n        }\n \
        \       return maxScore;\n    }\n}"
      python: "class Solution(object):\n    def maxPathScore(self, grid, k):\n     \
        \   \"\"\"\n        :type grid: List[List[int]]\n        :type k: int\n    \
        \    :rtype: int\n        \"\"\"\n        m = len(grid)\n        n = len(grid[0])\n\
        \        k_limit = min(k, m + n)\n        dp = [[-1] * (k_limit + 1) for _ in\
        \ range(n)]\n        dp[0][0] = 0\n\n        for i in range(m):\n          \
        \  next_dp = [[-1] * (k_limit + 1) for _ in range(n)]\n            for j in\
        \ range(n):\n                if i == 0 and j == 0:\n                    next_dp[0][0]\
        \ = 0\n                    continue\n                cost_inc = 1 if grid[i][j]\
        \ > 0 else 0\n                score_inc = grid[i][j]\n                local_limit\
        \ = min(k_limit, i + j)\n\n                prev_row = dp[j]\n              \
        \  if i > 0 and j > 0:\n                    prev_col = next_dp[j - 1]\n    \
        \                for c in range(cost_inc, local_limit + 1):\n              \
        \          v1 = prev_row[c - cost_inc]\n                        v2 = prev_col[c\
        \ - cost_inc]\n                        if v2 > v1: v1 = v2\n               \
        \         if v1 != -1:\n                            next_dp[j][c] = v1 + score_inc\n\
        \                elif i > 0:\n                    for c in range(cost_inc, local_limit\
        \ + 1):\n                        v1 = prev_row[c - cost_inc]\n             \
        \           if v1 != -1:\n                            next_dp[j][c] = v1 + score_inc\n\
        \                else:\n                    prev_col = next_dp[j - 1]\n    \
        \                for c in range(cost_inc, local_limit + 1):\n              \
        \          v2 = prev_col[c - cost_inc]\n                        if v2 != -1:\n\
        \                            next_dp[j][c] = v2 + score_inc\n            dp\
        \ = next_dp\n\n        ans = max(dp[n - 1])\n        return ans if ans != -1\
        \ else -1"
      python3: "class Solution:\n    def maxPathScore(self, grid: List[List[int]], k:\
        \ int) -> int:\n        m, n = len(grid), len(grid[0])\n        k_limit = min(k,\
        \ m + n)\n        dp = [[-1] * (k_limit + 1) for _ in range(n)]\n        dp[0][0]\
        \ = 0\n\n        for i in range(m):\n            next_dp = [[-1] * (k_limit\
        \ + 1) for _ in range(n)]\n            for j in range(n):\n                if\
        \ i == 0 and j == 0:\n                    next_dp[0][0] = 0\n              \
        \      continue\n                cost_inc = 1 if grid[i][j] > 0 else 0\n   \
        \             score_inc = grid[i][j]\n                local_limit = min(k_limit,\
        \ i + j)\n\n                prev_row = dp[j]\n                if i > 0 and j\
        \ > 0:\n                    prev_col = next_dp[j - 1]\n                    for\
        \ c in range(cost_inc, local_limit + 1):\n                        v1 = prev_row[c\
        \ - cost_inc]\n                        v2 = prev_col[c - cost_inc]\n       \
        \                 if v2 > v1: v1 = v2\n                        if v1 != -1:\n\
        \                            next_dp[j][c] = v1 + score_inc\n              \
        \  elif i > 0:\n                    for c in range(cost_inc, local_limit + 1):\n\
        \                        v1 = prev_row[c - cost_inc]\n                     \
        \   if v1 != -1:\n                            next_dp[j][c] = v1 + score_inc\n\
        \                else:\n                    prev_col = next_dp[j - 1]\n    \
        \                for c in range(cost_inc, local_limit + 1):\n              \
        \          v2 = prev_col[c - cost_inc]\n                        if v2 != -1:\n\
        \                            next_dp[j][c] = v2 + score_inc\n            dp\
        \ = next_dp\n\n        ans = max(dp[n - 1])\n        return ans if ans != -1\
        \ else -1"
      c: "#define MAX(a, b) ((a) > (b) ? (a) : (b))\n\nint maxPathScore(int** grid,\
        \ int gridSize, int* gridColSize, int k) {\n    int m = gridSize;\n    int n\
        \ = gridColSize[0];\n    int k_limit = k;\n    if (k_limit > m + n) k_limit\
        \ = m + n;\n\n    int* dp = (int*)malloc(n * (k_limit + 1) * sizeof(int));\n\
        \    int* next_dp = (int*)malloc(n * (k_limit + 1) * sizeof(int));\n\n    for\
        \ (int j = 0; j < n; j++) {\n        for (int c = 0; c <= k_limit; c++) {\n\
        \            dp[j * (k_limit + 1) + c] = -1;\n        }\n    }\n    dp[0] =\
        \ 0;\n\n    for (int i = 0; i < m; i++) {\n        for (int j = 0; j < n; j++)\
        \ {\n            for (int c = 0; c <= k_limit; c++) {\n                next_dp[j\
        \ * (k_limit + 1) + c] = -1;\n            }\n        }\n\n        for (int j\
        \ = 0; j < n; j++) {\n            if (i == 0 && j == 0) {\n                next_dp[0]\
        \ = 0;\n                continue;\n            }\n            int cost_inc =\
        \ (grid[i][j] > 0 ? 1 : 0);\n            int score_inc = grid[i][j];\n     \
        \       int local_limit = (i + j < k_limit ? i + j : k_limit);\n\n         \
        \   for (int c = cost_inc; c <= local_limit; c++) {\n                int best_prev\
        \ = -1;\n                if (i > 0) best_prev = MAX(best_prev, dp[j * (k_limit\
        \ + 1) + (c - cost_inc)]);\n                if (j > 0) best_prev = MAX(best_prev,\
        \ next_dp[(j - 1) * (k_limit + 1) + (c - cost_inc)]);\n\n                if\
        \ (best_prev != -1) {\n                    next_dp[j * (k_limit + 1) + c] =\
        \ best_prev + score_inc;\n                }\n            }\n        }\n    \
        \    memcpy(dp, next_dp, n * (k_limit + 1) * sizeof(int));\n    }\n\n    int\
        \ max_score = -1;\n    for (int c = 0; c <= k_limit; c++) {\n        max_score\
        \ = MAX(max_score, dp[(n - 1) * (k_limit + 1) + c]);\n    }\n\n    free(dp);\n\
        \    free(next_dp);\n    return max_score;\n}"
      csharp: "public class Solution {\n    public int MaxPathScore(int[][] grid, int\
        \ k) {\n        int m = grid.Length;\n        int n = grid[0].Length;\n    \
        \    int effectiveK = Math.Min(k, m + n - 1);\n\n        int[][] dp = new int[n][];\n\
        \        for (int j = 0; j < n; j++) {\n            dp[j] = new int[effectiveK\
        \ + 1];\n            for (int c = 0; c <= effectiveK; c++) {\n             \
        \   dp[j][c] = -1;\n            }\n        }\n\n        int startVal = grid[0][0];\n\
        \        int startCost = startVal > 0 ? 1 : 0;\n        if (startCost <= effectiveK)\
        \ {\n            dp[0][startCost] = startVal;\n        }\n\n        for (int\
        \ i = 0; i < m; i++) {\n            int[][] nextDp = new int[n][];\n       \
        \     for (int j = 0; j < n; j++) {\n                nextDp[j] = new int[effectiveK\
        \ + 1];\n                for (int c = 0; c <= effectiveK; c++) {\n         \
        \           nextDp[j][c] = -1;\n                }\n            }\n\n       \
        \     for (int j = 0; j < n; j++) {\n                int currVal = grid[i][j];\n\
        \                int currCost = currVal > 0 ? 1 : 0;\n\n                if (i\
        \ == 0 && j == 0) {\n                    if (startCost <= effectiveK) {\n  \
        \                      nextDp[0][startCost] = startVal;\n                  \
        \  }\n                    continue;\n                }\n\n                for\
        \ (int c = currCost; c <= effectiveK; c++) {\n                    int fromTop\
        \ = (i > 0) ? dp[j][c - currCost] : -1;\n                    int fromLeft =\
        \ (j > 0) ? nextDp[j - 1][c - currCost] : -1;\n\n                    int maxPrev\
        \ = fromTop > fromLeft ? fromTop : fromLeft;\n                    if (maxPrev\
        \ != -1) {\n                        nextDp[j][c] = maxPrev + currVal;\n    \
        \                }\n                }\n            }\n            dp = nextDp;\n\
        \        }\n\n        int maxScore = -1;\n        for (int c = 0; c <= effectiveK;\
        \ c++) {\n            if (dp[n - 1][c] > maxScore) {\n                maxScore\
        \ = dp[n - 1][c];\n            }\n        }\n        return maxScore;\n    }\n\
        }"
      javascript: "/**\n * @param {number[][]} grid\n * @param {number} k\n * @return\
        \ {number}\n */\nvar maxPathScore = function(grid, k) {\n    const m = grid.length;\n\
        \    const n = grid[0].length;\n    const effectiveK = Math.min(k, m + n - 1);\n\
        \    let dp = Array.from({ length: n }, () => new Int32Array(effectiveK + 1).fill(-1));\n\
        \n    const startVal = grid[0][0];\n    const startCost = startVal > 0 ? 1 :\
        \ 0;\n    if (startCost <= effectiveK) {\n        dp[0][startCost] = startVal;\n\
        \    }\n\n    for (let i = 0; i < m; i++) {\n        let nextDp = Array.from({\
        \ length: n }, () => new Int32Array(effectiveK + 1).fill(-1));\n        for\
        \ (let j = 0; j < n; j++) {\n            if (i === 0 && j === 0) {\n       \
        \         if (startCost <= effectiveK) nextDp[0][startCost] = startVal;\n  \
        \              continue;\n            }\n            const currVal = grid[i][j];\n\
        \            const currCost = currVal > 0 ? 1 : 0;\n            for (let c =\
        \ currCost; c <= effectiveK; c++) {\n                const fromTop = (i > 0)\
        \ ? dp[j][c - currCost] : -1;\n                const fromLeft = (j > 0) ? nextDp[j\
        \ - 1][c - currCost] : -1;\n                const maxPrev = fromTop > fromLeft\
        \ ? fromTop : fromLeft;\n                if (maxPrev !== -1) {\n           \
        \         nextDp[j][c] = maxPrev + currVal;\n                }\n           \
        \ }\n        }\n        dp = nextDp;\n    }\n\n    let maxScore = -1;\n    for\
        \ (let c = 0; c <= effectiveK; c++) {\n        if (dp[n - 1][c] > maxScore)\
        \ maxScore = dp[n - 1][c];\n    }\n    return maxScore;\n};"
      typescript: "function maxPathScore(grid: number[][], k: number): number {\n  \
        \  const m = grid.length;\n    const n = grid[0].length;\n    const effectiveK\
        \ = Math.min(k, m + n - 1);\n    let dp: Int32Array[] = Array.from({ length:\
        \ n }, () => new Int32Array(effectiveK + 1).fill(-1));\n\n    const startVal\
        \ = grid[0][0];\n    const startCost = startVal > 0 ? 1 : 0;\n    if (startCost\
        \ <= effectiveK) {\n        dp[0][startCost] = startVal;\n    }\n\n    for (let\
        \ i = 0; i < m; i++) {\n        const nextDp: Int32Array[] = Array.from({ length:\
        \ n }, () => new Int32Array(effectiveK + 1).fill(-1));\n        for (let j =\
        \ 0; j < n; j++) {\n            if (i === 0 && j === 0) {\n                if\
        \ (startCost <= effectiveK) nextDp[0][startCost] = startVal;\n             \
        \   continue;\n            }\n            const currVal = grid[i][j];\n    \
        \        const currCost = currVal > 0 ? 1 : 0;\n            for (let c = currCost;\
        \ c <= effectiveK; c++) {\n                const fromTop = (i > 0) ? dp[j][c\
        \ - currCost] : -1;\n                const fromLeft = (j > 0) ? nextDp[j - 1][c\
        \ - currCost] : -1;\n                const maxPrev = fromTop > fromLeft ? fromTop\
        \ : fromLeft;\n                if (maxPrev !== -1) {\n                    nextDp[j][c]\
        \ = maxPrev + currVal;\n                }\n            }\n        }\n      \
        \  dp = nextDp;\n    }\n\n    let maxScore = -1;\n    for (let c = 0; c <= effectiveK;\
        \ c++) {\n        if (dp[n - 1][c] > maxScore) maxScore = dp[n - 1][c];\n  \
        \  }\n    return maxScore;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @param\
        \ Integer $k\n     * @return Integer\n     */\n    function maxPathScore($grid,\
        \ $k) {\n        $m = count($grid);\n        $n = count($grid[0]);\n       \
        \ $effectiveK = min($k, $m + $n - 1);\n\n        $dp = array_fill(0, $n, array_fill(0,\
        \ $effectiveK + 1, -1));\n\n        $startVal = $grid[0][0];\n        $startCost\
        \ = $startVal > 0 ? 1 : 0;\n        if ($startCost <= $effectiveK) {\n     \
        \       $dp[0][$startCost] = $startVal;\n        }\n\n        for ($i = 0; $i\
        \ < $m; $i++) {\n            $nextDp = array_fill(0, $n, array_fill(0, $effectiveK\
        \ + 1, -1));\n            for ($j = 0; $j < $n; $j++) {\n                $currVal\
        \ = $grid[$i][$j];\n                $currCost = $currVal > 0 ? 1 : 0;\n\n  \
        \              if ($i == 0 && $j == 0) {\n                    if ($startCost\
        \ <= $effectiveK) {\n                        $nextDp[0][$startCost] = $startVal;\n\
        \                    }\n                    continue;\n                }\n\n\
        \                for ($c = $currCost; $c <= $effectiveK; $c++) {\n         \
        \           $fromTop = ($i > 0) ? $dp[$j][$c - $currCost] : -1;\n          \
        \          $fromLeft = ($j > 0) ? $nextDp[$j - 1][$c - $currCost] : -1;\n\n\
        \                    $maxPrev = ($fromTop > $fromLeft) ? $fromTop : $fromLeft;\n\
        \                    if ($maxPrev != -1) {\n                        $nextDp[$j][$c]\
        \ = $maxPrev + $currVal;\n                    }\n                }\n       \
        \     }\n            $dp = $nextDp;\n        }\n\n        $maxScore = -1;\n\
        \        for ($c = 0; $c <= $effectiveK; $c++) {\n            if ($dp[$n - 1][$c]\
        \ > $maxScore) {\n                $maxScore = $dp[$n - 1][$c];\n           \
        \ }\n        }\n        return $maxScore;\n    }\n}"
      swift: "class Solution {\n    func maxPathScore(_ grid: [[Int]], _ k: Int) ->\
        \ Int {\n        let m = grid.count\n        let n = grid[0].count\n       \
        \ let effectiveK = min(k, m + n - 1)\n\n        var dp = Array(repeating: Array(repeating:\
        \ -1, count: effectiveK + 1), count: n)\n\n        let startVal = grid[0][0]\n\
        \        let startCost = startVal > 0 ? 1 : 0\n        if startCost <= effectiveK\
        \ {\n            dp[0][startCost] = startVal\n        }\n\n        for i in\
        \ 0..<m {\n            var nextDp = Array(repeating: Array(repeating: -1, count:\
        \ effectiveK + 1), count: n)\n            for j in 0..<n {\n               \
        \ let currVal = grid[i][j]\n                let currCost = currVal > 0 ? 1 :\
        \ 0\n\n                if i == 0 && j == 0 {\n                    if startCost\
        \ <= effectiveK {\n                        nextDp[0][startCost] = startVal\n\
        \                    }\n                    continue\n                }\n\n\
        \                for c in currCost...effectiveK {\n                    let fromTop\
        \ = (i > 0) ? dp[j][c - currCost] : -1\n                    let fromLeft = (j\
        \ > 0) ? nextDp[j - 1][c - currCost] : -1\n\n                    let maxPrev\
        \ = fromTop > fromLeft ? fromTop : fromLeft\n                    if maxPrev\
        \ != -1 {\n                        nextDp[j][c] = maxPrev + currVal\n      \
        \              }\n                }\n            }\n            dp = nextDp\n\
        \        }\n\n        var maxScore = -1\n        for c in 0...effectiveK {\n\
        \            if dp[n - 1][c] > maxScore {\n                maxScore = dp[n -\
        \ 1][c]\n            }\n        }\n        return maxScore\n    }\n}"
      kotlin: "class Solution {\n    fun maxPathScore(grid: Array<IntArray>, k: Int):\
        \ Int {\n        val m = grid.size\n        val n = grid[0].size\n        val\
        \ effectiveK = if (k > m + n) m + n else k\n        var dp = Array(n) { IntArray(effectiveK\
        \ + 1) { -1 } }\n\n        val cost0 = if (grid[0][0] == 0) 0 else 1\n     \
        \   if (cost0 <= effectiveK) {\n            dp[0][cost0] = grid[0][0]\n    \
        \    }\n\n        for (i in 0 until m) {\n            val nextDp = Array(n)\
        \ { IntArray(effectiveK + 1) { -1 } }\n            for (j in 0 until n) {\n\
        \                if (i == 0 && j == 0) {\n                    if (cost0 <= effectiveK)\
        \ nextDp[0][cost0] = grid[0][0]\n                    continue\n            \
        \    }\n                val cellCost = if (grid[i][j] == 0) 0 else 1\n     \
        \           val cellScore = grid[i][j]\n                for (c in cellCost..effectiveK)\
        \ {\n                    var prevMax = -1\n                    if (i > 0 &&\
        \ dp[j][c - cellCost] != -1) {\n                        if (dp[j][c - cellCost]\
        \ > prevMax) prevMax = dp[j][c - cellCost]\n                    }\n        \
        \            if (j > 0 && nextDp[j - 1][c - cellCost] != -1) {\n           \
        \             if (nextDp[j - 1][c - cellCost] > prevMax) prevMax = nextDp[j\
        \ - 1][c - cellCost]\n                    }\n                    if (prevMax\
        \ != -1) {\n                        nextDp[j][c] = prevMax + cellScore\n   \
        \                 }\n                }\n            }\n            dp = nextDp\n\
        \        }\n\n        var maxScore = -1\n        for (c in 0..effectiveK) {\n\
        \            if (dp[n - 1][c] > maxScore) {\n                maxScore = dp[n\
        \ - 1][c]\n            }\n        }\n        return maxScore\n    }\n}"
      dart: "class Solution {\n  int maxPathScore(List<List<int>> grid, int k) {\n \
        \   int m = grid.length;\n    int n = grid[0].length;\n    int effectiveK =\
        \ k > m + n ? m + n : k;\n    List<List<int>> dp = List.generate(n, (_) => List.filled(effectiveK\
        \ + 1, -1));\n\n    int cost0 = grid[0][0] == 0 ? 0 : 1;\n    if (cost0 <= effectiveK)\
        \ {\n      dp[0][cost0] = grid[0][0];\n    }\n\n    for (int i = 0; i < m; i++)\
        \ {\n      List<List<int>> nextDp = List.generate(n, (_) => List.filled(effectiveK\
        \ + 1, -1));\n      for (int j = 0; j < n; j++) {\n        if (i == 0 && j ==\
        \ 0) {\n          if (cost0 <= effectiveK) nextDp[0][cost0] = grid[0][0];\n\
        \          continue;\n        }\n        int cellCost = grid[i][j] == 0 ? 0\
        \ : 1;\n        int cellScore = grid[i][j];\n        for (int c = cellCost;\
        \ c <= effectiveK; c++) {\n          int prevMax = -1;\n          if (i > 0\
        \ && dp[j][c - cellCost] != -1) {\n            if (dp[j][c - cellCost] > prevMax)\
        \ prevMax = dp[j][c - cellCost];\n          }\n          if (j > 0 && nextDp[j\
        \ - 1][c - cellCost] != -1) {\n            if (nextDp[j - 1][c - cellCost] >\
        \ prevMax) prevMax = nextDp[j - 1][c - cellCost];\n          }\n          if\
        \ (prevMax != -1) {\n            nextDp[j][c] = prevMax + cellScore;\n     \
        \     }\n        }\n      }\n      dp = nextDp;\n    }\n\n    int maxScore =\
        \ -1;\n    for (int c = 0; c <= effectiveK; c++) {\n      if (dp[n - 1][c] >\
        \ maxScore) {\n        maxScore = dp[n - 1][c];\n      }\n    }\n    return\
        \ maxScore;\n  }\n}"
      go: "func maxPathScore(grid [][]int, k int) int {\n\tm := len(grid)\n\tn := len(grid[0])\n\
        \teffectiveK := k\n\tif effectiveK > m+n {\n\t\teffectiveK = m + n\n\t}\n\n\t\
        dp := make([][]int, n)\n\tfor j := range dp {\n\t\tdp[j] = make([]int, effectiveK+1)\n\
        \t\tfor c := range dp[j] {\n\t\t\tdp[j][c] = -1\n\t\t}\n\t}\n\n\tcost0 := 0\n\
        \tif grid[0][0] != 0 {\n\t\tcost0 = 1\n\t}\n\tif cost0 <= effectiveK {\n\t\t\
        dp[0][cost0] = grid[0][0]\n\t}\n\n\tfor i := 0; i < m; i++ {\n\t\tnextDp :=\
        \ make([][]int, n)\n\t\tfor r := range nextDp {\n\t\t\tnextDp[r] = make([]int,\
        \ effectiveK+1)\n\t\t\tfor c := range nextDp[r] {\n\t\t\t\tnextDp[r][c] = -1\n\
        \t\t\t}\n\t\t}\n\n\t\tfor j := 0; j < n; j++ {\n\t\t\tif i == 0 && j == 0 {\n\
        \t\t\t\tif cost0 <= effectiveK {\n\t\t\t\t\tnextDp[0][cost0] = grid[0][0]\n\t\
        \t\t\t}\n\t\t\t\tcontinue\n\t\t\t}\n\t\t\tcellCost := 0\n\t\t\tif grid[i][j]\
        \ != 0 {\n\t\t\t\tcellCost = 1\n\t\t\t}\n\t\t\tcellScore := grid[i][j]\n\n\t\
        \t\tfor c := cellCost; c <= effectiveK; c++ {\n\t\t\t\tprevMax := -1\n\t\t\t\
        \tif i > 0 && dp[j][c-cellCost] != -1 {\n\t\t\t\t\tprevMax = dp[j][c-cellCost]\n\
        \t\t\t\t}\n\t\t\t\tif j > 0 && nextDp[j-1][c-cellCost] != -1 {\n\t\t\t\t\tif\
        \ nextDp[j-1][c-cellCost] > prevMax {\n\t\t\t\t\t\tprevMax = nextDp[j-1][c-cellCost]\n\
        \t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\tif prevMax != -1 {\n\t\t\t\t\tnextDp[j][c] =\
        \ prevMax + cellScore\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t\tdp = nextDp\n\t}\n\n\t\
        maxScore := -1\n\tfor c := 0; c <= effectiveK; c++ {\n\t\tif dp[n-1][c] > maxScore\
        \ {\n\t\t\tmaxScore = dp[n-1][c]\n\t\t}\n\t}\n\treturn maxScore\n}"
      ruby: "# @param {Integer[][]} grid\n# @param {Integer} k\n# @return {Integer}\n\
        def max_path_score(grid, k)\n  m = grid.length\n  n = grid[0].length\n  k_limit\
        \ = k < m + n ? k : m + n\n  dp = Array.new(n) { Array.new(k_limit + 1, -1)\
        \ }\n\n  cost0 = grid[0][0] == 0 ? 0 : 1\n  dp[0][cost0] = grid[0][0] if cost0\
        \ <= k_limit\n\n  (0...m).each do |i|\n    next_dp = Array.new(n) { Array.new(k_limit\
        \ + 1, -1) }\n    (0...n).each do |j|\n      if i == 0 && j == 0\n        next_dp[0][cost0]\
        \ = grid[0][0] if cost0 <= k_limit\n        next\n      end\n\n      cell_cost\
        \ = grid[i][j] == 0 ? 0 : 1\n      cell_score = grid[i][j]\n\n      (cell_cost..k_limit).each\
        \ do |c|\n        prev_max = -1\n        if i > 0 && dp[j][c - cell_cost] !=\
        \ -1\n          prev_max = dp[j][c - cell_cost]\n        end\n        if j >\
        \ 0 && next_dp[j - 1][c - cell_cost] != -1\n          left_v = next_dp[j - 1][c\
        \ - cell_cost]\n          prev_max = left_v if left_v > prev_max\n        end\n\
        \n        next_dp[j][c] = prev_max + cell_score if prev_max != -1\n      end\n\
        \    end\n    dp = next_dp\n  end\n\n  max_s = dp[n - 1].max\n  max_s.nil? ||\
        \ max_s < 0 ? -1 : max_s\nend"
      scala: "object Solution {\n  def maxPathScore(grid: Array[Array[Int]], k: Int):\
        \ Int = {\n    val m = grid.length\n    val n = grid(0).length\n    val effectiveK\
        \ = if (k > m + n) m + n else k\n    var dp = Array.fill(n, effectiveK + 1)(-1)\n\
        \n    val cost0 = if (grid(0)(0) == 0) 0 else 1\n    if (cost0 <= effectiveK)\
        \ {\n      dp(0)(cost0) = grid(0)(0)\n    }\n\n    for (i <- 0 until m) {\n\
        \      val nextDp = Array.fill(n, effectiveK + 1)(-1)\n      for (j <- 0 until\
        \ n) {\n        if (i == 0 && j == 0) {\n          if (cost0 <= effectiveK)\
        \ nextDp(0)(cost0) = grid(0)(0)\n        } else {\n          val cellCost =\
        \ if (grid(i)(j) == 0) 0 else 1\n          val cellScore = grid(i)(j)\n    \
        \      for (c <- cellCost to effectiveK) {\n            var prevMax = -1\n \
        \           if (i > 0 && dp(j)(c - cellCost) != -1) {\n              prevMax\
        \ = Math.max(prevMax, dp(j)(c - cellCost))\n            }\n            if (j\
        \ > 0 && nextDp(j - 1)(c - cellCost) != -1) {\n              prevMax = Math.max(prevMax,\
        \ nextDp(j - 1)(c - cellCost))\n            }\n            if (prevMax != -1)\
        \ {\n              nextDp(j)(c) = prevMax + cellScore\n            }\n     \
        \     }\n        }\n      }\n      dp = nextDp\n    }\n\n    var maxScore =\
        \ -1\n    for (c <- 0 to effectiveK) {\n      maxScore = Math.max(maxScore,\
        \ dp(n - 1)(c))\n    }\n    maxScore\n  }\n}"
      rust: "impl Solution {\n    pub fn max_path_score(grid: Vec<Vec<i32>>, k: i32)\
        \ -> i32 {\n        let m = grid.len();\n        let n = grid[0].len();\n  \
        \      let k_usize = k as usize;\n        let mut dp = vec![vec![-1; k_usize\
        \ + 1]; n];\n\n        for i in 0..m {\n            let mut next_dp = vec![vec![-1;\
        \ k_usize + 1]; n];\n            for j in 0..n {\n                let val =\
        \ grid[i][j];\n                let ci = if val == 0 { 0 } else { 1 };\n    \
        \            let si = val;\n\n                if i == 0 && j == 0 {\n      \
        \              next_dp[0][0] = 0;\n                    continue;\n         \
        \       }\n\n                for c in ci..=k_usize {\n                    let\
        \ mut max_prev = -1;\n                    if i > 0 {\n                     \
        \   max_prev = max_prev.max(dp[j][c - ci]);\n                    }\n       \
        \             if j > 0 {\n                        max_prev = max_prev.max(next_dp[j\
        \ - 1][c - ci]);\n                    }\n\n                    if max_prev !=\
        \ -1 {\n                        next_dp[j][c] = max_prev + si;\n           \
        \         }\n                }\n            }\n            dp = next_dp;\n \
        \       }\n\n        let mut ans = -1;\n        for c in 0..=k_usize {\n   \
        \         ans = ans.max(dp[n - 1][c]);\n        }\n        ans\n    }\n}"
      racket: "(define/contract (max-path-score grid k)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer? exact-integer?)\n  (let* ([m (length grid)]\n         [n (length\
        \ (first grid))]\n         [k1 (+ k 1)]\n         [grid-vec (list->vector (map\
        \ list->vector grid))]\n         [dp (make-vector (* n k1) -1)])\n\n    (vector-set!\
        \ dp 0 0)\n\n    (for ([i (in-range m)])\n      (let ([next-dp (make-vector\
        \ (* n k1) -1)])\n        (for ([j (in-range n)])\n          (let* ([val (vector-ref\
        \ (vector-ref grid-vec i) j)]\n                 [ci (if (= val 0) 0 1)]\n  \
        \               [si val])\n            (if (and (= i 0) (= j 0))\n         \
        \       (vector-set! next-dp 0 0)\n                (for ([c (in-range ci k1)])\n\
        \                  (let* ([prev-c (- c ci)]\n                         [max-prev\
        \ -1])\n                    (when (> i 0)\n                      (let ([v (vector-ref\
        \ dp (+ (* j k1) prev-c))])\n                        (when (> v max-prev) (set!\
        \ max-prev v))))\n                    (when (> j 0)\n                      (let\
        \ ([v (vector-ref next-dp (+ (* (- j 1) k1) prev-c))])\n                   \
        \     (when (> v max-prev) (set! max-prev v))))\n\n                    (when\
        \ (> max-prev -1)\n                      (vector-set! next-dp (+ (* j k1) c)\
        \ (+ max-prev si))))))))\n        (set! dp next-dp)))\n\n    (let ([ans -1])\n\
        \      (for ([c (in-range k1)])\n        (let ([v (vector-ref dp (+ (* (- n\
        \ 1) k1) c))])\n          (when (> v ans) (set! ans v))))\n      ans)))"
      erlang: "-spec max_path_score(Grid :: [[integer()]], K :: integer()) -> integer().\n\
        max_path_score(Grid, K) ->\n    M = length(Grid),\n    N = length(hd(Grid)),\n\
        \    GridVec = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),\n    InitialDP\
        \ = list_to_tuple([list_to_tuple([-1 || _ <- lists:seq(0, K)]) || _ <- lists:seq(1,\
        \ N)]),\n    FinalDP = solve(0, M, N, K, GridVec, InitialDP),\n    LastCol =\
        \ element(N, FinalDP),\n    lists:max([-1 | tuple_to_list(LastCol)]).\n\nsolve(I,\
        \ M, N, K, GridVec, PrevDP) when I < M ->\n    GridRow = element(I + 1, GridVec),\n\
        \    CurrRow = solve_row(0, N, I, K, GridRow, PrevDP, []),\n    solve(I + 1,\
        \ M, N, K, GridVec, CurrRow);\nsolve(_, _, _, _, _, PrevDP) ->\n    PrevDP.\n\
        \nsolve_row(J, N, I, K, GridRow, PrevDP, RowCurrentList) when J < N ->\n   \
        \ Val = element(J + 1, GridRow),\n    Ci = if Val == 0 -> 0; true -> 1 end,\n\
        \    Si = Val,\n    ColDP = if\n        I == 0, J == 0 -> \n            list_to_tuple([0\
        \ | [-1 || _ <- lists:seq(1, K)]]);\n        true ->\n            ColAbove =\
        \ element(J + 1, PrevDP),\n            ColLeft = if J > 0 -> hd(RowCurrentList);\
        \ true -> undefined end,\n            build_col(0, K, Ci, Si, I, J, ColAbove,\
        \ ColLeft, [])\n    end,\n    solve_row(J + 1, N, I, K, GridRow, PrevDP, [ColDP\
        \ | RowCurrentList]);\nsolve_row(_, _, _, _, _, _, RowCurrentList) ->\n    list_to_tuple(lists:reverse(RowCurrentList)).\n\
        \nbuild_col(C, K, Ci, Si, I, J, ColAbove, ColLeft, Acc) when C =< K ->\n   \
        \ PrevC = C - Ci,\n    Score = if\n        PrevC < 0 -> -1;\n        true ->\n\
        \            VAbove = if I > 0 -> element(PrevC + 1, ColAbove); true -> -1 end,\n\
        \            VLeft = if J > 0 -> element(PrevC + 1, ColLeft); true -> -1 end,\n\
        \            MaxP = if VAbove > VLeft -> VAbove; true -> VLeft end,\n      \
        \      if MaxP == -1 -> -1; true -> MaxP + Si end\n    end,\n    build_col(C\
        \ + 1, K, Ci, Si, I, J, ColAbove, ColLeft, [Score | Acc]);\nbuild_col(_, _,\
        \ _, _, _, _, _, _, Acc) ->\n    list_to_tuple(lists:reverse(Acc))."
      elixir: "defmodule Solution do\n  @spec max_path_score(grid :: [[integer]], k\
        \ :: integer) :: integer\n  def max_path_score(grid, k) do\n    m = length(grid)\n\
        \    n = length(hd(grid))\n    grid_matrix = grid |> Enum.map(&List.to_tuple/1)\
        \ |> List.to_tuple()\n    initial_dp = List.duplicate(List.duplicate(-1, k +\
        \ 1) |> List.to_tuple(), n) |> List.to_tuple()\n    final_dp = solve(0, m, n,\
        \ k, grid_matrix, initial_dp)\n    last_col = elem(final_dp, n - 1)\n    last_col\
        \ |> Tuple.to_list() |> Enum.max() |> max(-1)\n  end\n\n  defp solve(i, m, n,\
        \ k, grid_matrix, prev_dp) when i < m do\n    grid_row = elem(grid_matrix, i)\n\
        \    curr_row = solve_row(0, n, i, k, grid_row, prev_dp, [])\n    solve(i +\
        \ 1, m, n, k, grid_matrix, curr_row)\n  end\n  defp solve(_, _, _, _, _, prev_dp),\
        \ do: prev_dp\n\n  defp solve_row(j, n, i, k, grid_row, prev_dp, row_current_list)\
        \ when j < n do\n    val = elem(grid_row, j)\n    ci = if val == 0, do: 0, else:\
        \ 1\n    si = val\n    col_dp = cond do\n      i == 0 and j == 0 ->\n      \
        \  List.to_tuple([0 | List.duplicate(-1, k)])\n      true ->\n        col_above\
        \ = elem(prev_dp, j)\n        col_left = if j > 0, do: hd(row_current_list),\
        \ else: nil\n        build_col(0, k, ci, si, i, j, col_above, col_left, [])\n\
        \    end\n    solve_row(j + 1, n, i, k, grid_row, prev_dp, [col_dp | row_current_list])\n\
        \  end\n  defp solve_row(_, _, _, _, _, _, row_current_list) do\n    row_current_list\
        \ |> Enum.reverse() |> List.to_tuple()\n  end\n\n  defp build_col(c, k, ci,\
        \ si, i, j, col_above, col_left, acc) when c <= k do\n    prev_c = c - ci\n\
        \    score = if prev_c < 0 do\n      -1\n    else\n      v_above = if i > 0,\
        \ do: elem(col_above, prev_c), else: -1\n      v_left = if j > 0, do: elem(col_left,\
        \ prev_c), else: -1\n      max_p = max(v_above, v_left)\n      if max_p == -1,\
        \ do: -1, else: max_p + si\n    end\n    build_col(c + 1, k, ci, si, i, j, col_above,\
        \ col_left, [score | acc])\n  end\n  defp build_col(_, _, _, _, _, _, _, _,\
        \ acc) do\n    acc |> Enum.reverse() |> List.to_tuple()\n  end\nend"
    approach: 'We solve this problem using dynamic programming with the state dp[i][j][c]
      representing the maximum score achievable at cell (i, j) with a total cost of
      exactly c. Since we can only move right or down, the state at (i, j) depends on
      (i-1, j) and (i, j-1). For each cell, we compute the cost and score increments:
      a grid value of 0 adds 0 to score and cost, while values 1 or 2 add 1 to the cost
      and their respective values to the score. The transition follows: dp[i][j][c]
      = max(dp[i-1][j][c - cost_inc], dp[i][j-1][c - cost_inc]) + score_inc.'
    time_complexity: O(m * n * min(k, m + n)) where m and n are the grid dimensions.
      Since any path from the top-left to the bottom-right has a fixed length of m +
      n - 1 and each cell adds at most 1 to the cost, the total cost never exceeds m
      + n - 1, allowing us to cap the effective value of k.
    space_complexity: O(n * min(k, m + n)) because we only need the DP results from
      the previous row and the cell to the left in the current row to compute the next
      state. We use two DP rows (or a slightly optimized version of this) to maintain
      results for only the current and previous grid states.
    elapsed_time: 437.8027710914612
    model: gemini-3-flash-preview
    generated_at: '2026-04-30 02:19:26 '
---

## Problem #3742: Maximum Path Score in a Grid

**Difficulty:** Medium

**Topics:** Array, Dynamic Programming, Matrix

## Problem Description

<p>You are given an <code>m x n</code> grid where each cell contains one of the values 0, 1, or 2. You are also given an integer <code>k</code>.</p>

<p>You start from the top-left corner <code>(0, 0)</code> and want to reach the bottom-right corner <code>(m - 1, n - 1)</code> by moving only <strong>right</strong> or <strong>down</strong>.</p>

<p>Each cell contributes a specific score and incurs an associated cost, according to their cell values:</p>

<ul>
	<li>0: adds 0 to your score and costs 0.</li>
	<li>1: adds 1 to your score and costs 1.</li>
	<li>2: adds 2 to your score and costs 1. ​​​​​​​</li>
</ul>

<p>Return the <strong>maximum</strong> score achievable without exceeding a total cost of <code>k</code>, or -1 if no valid path exists.</p>

<p><strong>Note:</strong> If you reach the last cell but the total cost exceeds <code>k</code>, the path is invalid.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[0, 1],[2, 0]], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong>​​​​​​​</p>

<p>The optimal path is:</p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Cell</th>
			<th style="border: 1px solid black;">grid[i][j]</th>
			<th style="border: 1px solid black;">Score</th>
			<th style="border: 1px solid black;">Total<br />
			Score</th>
			<th style="border: 1px solid black;">Cost</th>
			<th style="border: 1px solid black;">Total<br />
			Cost</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">(0, 0)</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">(1, 0)</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">(1, 1)</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

<p>Thus, the maximum possible score is 2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[0, 1],[1, 2]], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no path that reaches cell <code>(1, 1)</code>​​​​​​​ without exceeding cost k. Thus, the answer is -1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>3</sup>​​​​​​​</code></li>
	<li><code><sup>​​​​​​​</sup>grid[0][0] == 0</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 2</code></li>
</ul>


## Hints

1. Use dynamic programming.

2. Let `dp[i][j][c]` = max score at cell `(i,j)` with total cost exactly `c` (0 <= `c` <= `k`).

3. Update `dp[i][j][c]` from `(i-1,j)` and `(i,j-1)` using `cost = (grid[i][j] == 0 ? 0 : 1)` and `score = grid[i][j]`.

4. Answer = `max(dp[m-1][n-1][c])` for `c=0..k`, or `-1` if none.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

We solve this problem using dynamic programming with the state dp[i][j][c] representing the maximum score achievable at cell (i, j) with a total cost of exactly c. Since we can only move right or down, the state at (i, j) depends on (i-1, j) and (i, j-1). For each cell, we compute the cost and score increments: a grid value of 0 adds 0 to score and cost, while values 1 or 2 add 1 to the cost and their respective values to the score. The transition follows: dp[i][j][c] = max(dp[i-1][j][c - cost_inc], dp[i][j-1][c - cost_inc]) + score_inc.

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
    int maxPathScore(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        int k_limit = min(k, m + n);
        vector<vector<int>> dp(n, vector<int>(k_limit + 1, -1));
        dp[0][0] = 0;

        for (int i = 0; i < m; ++i) {
            vector<vector<int>> next_dp(n, vector<int>(k_limit + 1, -1));
            for (int j = 0; j < n; ++j) {
                if (i == 0 && j == 0) {
                    next_dp[0][0] = 0;
                    continue;
                }
                int cost_inc = (grid[i][j] > 0 ? 1 : 0);
                int score_inc = grid[i][j];
                int local_limit = min(k_limit, i + j);

                for (int c = cost_inc; c <= local_limit; ++c) {
                    int best_prev = -1;
                    if (i > 0) best_prev = max(best_prev, dp[j][c - cost_inc]);
                    if (j > 0) best_prev = max(best_prev, next_dp[j - 1][c - cost_inc]);

                    if (best_prev != -1) {
                        next_dp[j][c] = best_prev + score_inc;
                    }
                }
            }
            dp.swap(next_dp);
        }

        int max_score = -1;
        for (int c = 0; c <= k_limit; ++c) {
            max_score = max(max_score, dp[n - 1][c]);
        }
        return max_score;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxPathScore(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int kLimit = Math.min(k, m + n);
        int[][] dp = new int[n][kLimit + 1];
        for (int i = 0; i < n; i++) {
            java.util.Arrays.fill(dp[i], -1);
        }
        dp[0][0] = 0;

        for (int i = 0; i < m; i++) {
            int[][] nextDp = new int[n][kLimit + 1];
            for (int j = 0; j < n; j++) {
                java.util.Arrays.fill(nextDp[j], -1);
                if (i == 0 && j == 0) {
                    nextDp[0][0] = 0;
                    continue;
                }
                int costInc = (grid[i][j] > 0 ? 1 : 0);
                int scoreInc = grid[i][j];
                int localLimit = Math.min(kLimit, i + j);

                for (int c = costInc; c <= localLimit; c++) {
                    int bestPrev = -1;
                    if (i > 0) bestPrev = Math.max(bestPrev, dp[j][c - costInc]);
                    if (j > 0) bestPrev = Math.max(bestPrev, nextDp[j - 1][c - costInc]);

                    if (bestPrev != -1) {
                        nextDp[j][c] = bestPrev + scoreInc;
                    }
                }
            }
            dp = nextDp;
        }

        int maxScore = -1;
        for (int c = 0; c <= kLimit; c++) {
            maxScore = Math.max(maxScore, dp[n - 1][c]);
        }
        return maxScore;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxPathScore(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        k_limit = min(k, m + n)
        dp = [[-1] * (k_limit + 1) for _ in range(n)]
        dp[0][0] = 0

        for i in range(m):
            next_dp = [[-1] * (k_limit + 1) for _ in range(n)]
            for j in range(n):
                if i == 0 and j == 0:
                    next_dp[0][0] = 0
                    continue
                cost_inc = 1 if grid[i][j] > 0 else 0
                score_inc = grid[i][j]
                local_limit = min(k_limit, i + j)

                prev_row = dp[j]
                if i > 0 and j > 0:
                    prev_col = next_dp[j - 1]
                    for c in range(cost_inc, local_limit + 1):
                        v1 = prev_row[c - cost_inc]
                        v2 = prev_col[c - cost_inc]
                        if v2 > v1: v1 = v2
                        if v1 != -1:
                            next_dp[j][c] = v1 + score_inc
                elif i > 0:
                    for c in range(cost_inc, local_limit + 1):
                        v1 = prev_row[c - cost_inc]
                        if v1 != -1:
                            next_dp[j][c] = v1 + score_inc
                else:
                    prev_col = next_dp[j - 1]
                    for c in range(cost_inc, local_limit + 1):
                        v2 = prev_col[c - cost_inc]
                        if v2 != -1:
                            next_dp[j][c] = v2 + score_inc
            dp = next_dp

        ans = max(dp[n - 1])
        return ans if ans != -1 else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        k_limit = min(k, m + n)
        dp = [[-1] * (k_limit + 1) for _ in range(n)]
        dp[0][0] = 0

        for i in range(m):
            next_dp = [[-1] * (k_limit + 1) for _ in range(n)]
            for j in range(n):
                if i == 0 and j == 0:
                    next_dp[0][0] = 0
                    continue
                cost_inc = 1 if grid[i][j] > 0 else 0
                score_inc = grid[i][j]
                local_limit = min(k_limit, i + j)

                prev_row = dp[j]
                if i > 0 and j > 0:
                    prev_col = next_dp[j - 1]
                    for c in range(cost_inc, local_limit + 1):
                        v1 = prev_row[c - cost_inc]
                        v2 = prev_col[c - cost_inc]
                        if v2 > v1: v1 = v2
                        if v1 != -1:
                            next_dp[j][c] = v1 + score_inc
                elif i > 0:
                    for c in range(cost_inc, local_limit + 1):
                        v1 = prev_row[c - cost_inc]
                        if v1 != -1:
                            next_dp[j][c] = v1 + score_inc
                else:
                    prev_col = next_dp[j - 1]
                    for c in range(cost_inc, local_limit + 1):
                        v2 = prev_col[c - cost_inc]
                        if v2 != -1:
                            next_dp[j][c] = v2 + score_inc
            dp = next_dp

        ans = max(dp[n - 1])
        return ans if ans != -1 else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int maxPathScore(int** grid, int gridSize, int* gridColSize, int k) {
    int m = gridSize;
    int n = gridColSize[0];
    int k_limit = k;
    if (k_limit > m + n) k_limit = m + n;

    int* dp = (int*)malloc(n * (k_limit + 1) * sizeof(int));
    int* next_dp = (int*)malloc(n * (k_limit + 1) * sizeof(int));

    for (int j = 0; j < n; j++) {
        for (int c = 0; c <= k_limit; c++) {
            dp[j * (k_limit + 1) + c] = -1;
        }
    }
    dp[0] = 0;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            for (int c = 0; c <= k_limit; c++) {
                next_dp[j * (k_limit + 1) + c] = -1;
            }
        }

        for (int j = 0; j < n; j++) {
            if (i == 0 && j == 0) {
                next_dp[0] = 0;
                continue;
            }
            int cost_inc = (grid[i][j] > 0 ? 1 : 0);
            int score_inc = grid[i][j];
            int local_limit = (i + j < k_limit ? i + j : k_limit);

            for (int c = cost_inc; c <= local_limit; c++) {
                int best_prev = -1;
                if (i > 0) best_prev = MAX(best_prev, dp[j * (k_limit + 1) + (c - cost_inc)]);
                if (j > 0) best_prev = MAX(best_prev, next_dp[(j - 1) * (k_limit + 1) + (c - cost_inc)]);

                if (best_prev != -1) {
                    next_dp[j * (k_limit + 1) + c] = best_prev + score_inc;
                }
            }
        }
        memcpy(dp, next_dp, n * (k_limit + 1) * sizeof(int));
    }

    int max_score = -1;
    for (int c = 0; c <= k_limit; c++) {
        max_score = MAX(max_score, dp[(n - 1) * (k_limit + 1) + c]);
    }

    free(dp);
    free(next_dp);
    return max_score;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxPathScore(int[][] grid, int k) {
        int m = grid.Length;
        int n = grid[0].Length;
        int effectiveK = Math.Min(k, m + n - 1);

        int[][] dp = new int[n][];
        for (int j = 0; j < n; j++) {
            dp[j] = new int[effectiveK + 1];
            for (int c = 0; c <= effectiveK; c++) {
                dp[j][c] = -1;
            }
        }

        int startVal = grid[0][0];
        int startCost = startVal > 0 ? 1 : 0;
        if (startCost <= effectiveK) {
            dp[0][startCost] = startVal;
        }

        for (int i = 0; i < m; i++) {
            int[][] nextDp = new int[n][];
            for (int j = 0; j < n; j++) {
                nextDp[j] = new int[effectiveK + 1];
                for (int c = 0; c <= effectiveK; c++) {
                    nextDp[j][c] = -1;
                }
            }

            for (int j = 0; j < n; j++) {
                int currVal = grid[i][j];
                int currCost = currVal > 0 ? 1 : 0;

                if (i == 0 && j == 0) {
                    if (startCost <= effectiveK) {
                        nextDp[0][startCost] = startVal;
                    }
                    continue;
                }

                for (int c = currCost; c <= effectiveK; c++) {
                    int fromTop = (i > 0) ? dp[j][c - currCost] : -1;
                    int fromLeft = (j > 0) ? nextDp[j - 1][c - currCost] : -1;

                    int maxPrev = fromTop > fromLeft ? fromTop : fromLeft;
                    if (maxPrev != -1) {
                        nextDp[j][c] = maxPrev + currVal;
                    }
                }
            }
            dp = nextDp;
        }

        int maxScore = -1;
        for (int c = 0; c <= effectiveK; c++) {
            if (dp[n - 1][c] > maxScore) {
                maxScore = dp[n - 1][c];
            }
        }
        return maxScore;
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
 * @return {number}
 */
var maxPathScore = function(grid, k) {
    const m = grid.length;
    const n = grid[0].length;
    const effectiveK = Math.min(k, m + n - 1);
    let dp = Array.from({ length: n }, () => new Int32Array(effectiveK + 1).fill(-1));

    const startVal = grid[0][0];
    const startCost = startVal > 0 ? 1 : 0;
    if (startCost <= effectiveK) {
        dp[0][startCost] = startVal;
    }

    for (let i = 0; i < m; i++) {
        let nextDp = Array.from({ length: n }, () => new Int32Array(effectiveK + 1).fill(-1));
        for (let j = 0; j < n; j++) {
            if (i === 0 && j === 0) {
                if (startCost <= effectiveK) nextDp[0][startCost] = startVal;
                continue;
            }
            const currVal = grid[i][j];
            const currCost = currVal > 0 ? 1 : 0;
            for (let c = currCost; c <= effectiveK; c++) {
                const fromTop = (i > 0) ? dp[j][c - currCost] : -1;
                const fromLeft = (j > 0) ? nextDp[j - 1][c - currCost] : -1;
                const maxPrev = fromTop > fromLeft ? fromTop : fromLeft;
                if (maxPrev !== -1) {
                    nextDp[j][c] = maxPrev + currVal;
                }
            }
        }
        dp = nextDp;
    }

    let maxScore = -1;
    for (let c = 0; c <= effectiveK; c++) {
        if (dp[n - 1][c] > maxScore) maxScore = dp[n - 1][c];
    }
    return maxScore;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxPathScore(grid: number[][], k: number): number {
    const m = grid.length;
    const n = grid[0].length;
    const effectiveK = Math.min(k, m + n - 1);
    let dp: Int32Array[] = Array.from({ length: n }, () => new Int32Array(effectiveK + 1).fill(-1));

    const startVal = grid[0][0];
    const startCost = startVal > 0 ? 1 : 0;
    if (startCost <= effectiveK) {
        dp[0][startCost] = startVal;
    }

    for (let i = 0; i < m; i++) {
        const nextDp: Int32Array[] = Array.from({ length: n }, () => new Int32Array(effectiveK + 1).fill(-1));
        for (let j = 0; j < n; j++) {
            if (i === 0 && j === 0) {
                if (startCost <= effectiveK) nextDp[0][startCost] = startVal;
                continue;
            }
            const currVal = grid[i][j];
            const currCost = currVal > 0 ? 1 : 0;
            for (let c = currCost; c <= effectiveK; c++) {
                const fromTop = (i > 0) ? dp[j][c - currCost] : -1;
                const fromLeft = (j > 0) ? nextDp[j - 1][c - currCost] : -1;
                const maxPrev = fromTop > fromLeft ? fromTop : fromLeft;
                if (maxPrev !== -1) {
                    nextDp[j][c] = maxPrev + currVal;
                }
            }
        }
        dp = nextDp;
    }

    let maxScore = -1;
    for (let c = 0; c <= effectiveK; c++) {
        if (dp[n - 1][c] > maxScore) maxScore = dp[n - 1][c];
    }
    return maxScore;
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
     * @return Integer
     */
    function maxPathScore($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $effectiveK = min($k, $m + $n - 1);

        $dp = array_fill(0, $n, array_fill(0, $effectiveK + 1, -1));

        $startVal = $grid[0][0];
        $startCost = $startVal > 0 ? 1 : 0;
        if ($startCost <= $effectiveK) {
            $dp[0][$startCost] = $startVal;
        }

        for ($i = 0; $i < $m; $i++) {
            $nextDp = array_fill(0, $n, array_fill(0, $effectiveK + 1, -1));
            for ($j = 0; $j < $n; $j++) {
                $currVal = $grid[$i][$j];
                $currCost = $currVal > 0 ? 1 : 0;

                if ($i == 0 && $j == 0) {
                    if ($startCost <= $effectiveK) {
                        $nextDp[0][$startCost] = $startVal;
                    }
                    continue;
                }

                for ($c = $currCost; $c <= $effectiveK; $c++) {
                    $fromTop = ($i > 0) ? $dp[$j][$c - $currCost] : -1;
                    $fromLeft = ($j > 0) ? $nextDp[$j - 1][$c - $currCost] : -1;

                    $maxPrev = ($fromTop > $fromLeft) ? $fromTop : $fromLeft;
                    if ($maxPrev != -1) {
                        $nextDp[$j][$c] = $maxPrev + $currVal;
                    }
                }
            }
            $dp = $nextDp;
        }

        $maxScore = -1;
        for ($c = 0; $c <= $effectiveK; $c++) {
            if ($dp[$n - 1][$c] > $maxScore) {
                $maxScore = $dp[$n - 1][$c];
            }
        }
        return $maxScore;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxPathScore(_ grid: [[Int]], _ k: Int) -> Int {
        let m = grid.count
        let n = grid[0].count
        let effectiveK = min(k, m + n - 1)

        var dp = Array(repeating: Array(repeating: -1, count: effectiveK + 1), count: n)

        let startVal = grid[0][0]
        let startCost = startVal > 0 ? 1 : 0
        if startCost <= effectiveK {
            dp[0][startCost] = startVal
        }

        for i in 0..<m {
            var nextDp = Array(repeating: Array(repeating: -1, count: effectiveK + 1), count: n)
            for j in 0..<n {
                let currVal = grid[i][j]
                let currCost = currVal > 0 ? 1 : 0

                if i == 0 && j == 0 {
                    if startCost <= effectiveK {
                        nextDp[0][startCost] = startVal
                    }
                    continue
                }

                for c in currCost...effectiveK {
                    let fromTop = (i > 0) ? dp[j][c - currCost] : -1
                    let fromLeft = (j > 0) ? nextDp[j - 1][c - currCost] : -1

                    let maxPrev = fromTop > fromLeft ? fromTop : fromLeft
                    if maxPrev != -1 {
                        nextDp[j][c] = maxPrev + currVal
                    }
                }
            }
            dp = nextDp
        }

        var maxScore = -1
        for c in 0...effectiveK {
            if dp[n - 1][c] > maxScore {
                maxScore = dp[n - 1][c]
            }
        }
        return maxScore
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxPathScore(grid: Array<IntArray>, k: Int): Int {
        val m = grid.size
        val n = grid[0].size
        val effectiveK = if (k > m + n) m + n else k
        var dp = Array(n) { IntArray(effectiveK + 1) { -1 } }

        val cost0 = if (grid[0][0] == 0) 0 else 1
        if (cost0 <= effectiveK) {
            dp[0][cost0] = grid[0][0]
        }

        for (i in 0 until m) {
            val nextDp = Array(n) { IntArray(effectiveK + 1) { -1 } }
            for (j in 0 until n) {
                if (i == 0 && j == 0) {
                    if (cost0 <= effectiveK) nextDp[0][cost0] = grid[0][0]
                    continue
                }
                val cellCost = if (grid[i][j] == 0) 0 else 1
                val cellScore = grid[i][j]
                for (c in cellCost..effectiveK) {
                    var prevMax = -1
                    if (i > 0 && dp[j][c - cellCost] != -1) {
                        if (dp[j][c - cellCost] > prevMax) prevMax = dp[j][c - cellCost]
                    }
                    if (j > 0 && nextDp[j - 1][c - cellCost] != -1) {
                        if (nextDp[j - 1][c - cellCost] > prevMax) prevMax = nextDp[j - 1][c - cellCost]
                    }
                    if (prevMax != -1) {
                        nextDp[j][c] = prevMax + cellScore
                    }
                }
            }
            dp = nextDp
        }

        var maxScore = -1
        for (c in 0..effectiveK) {
            if (dp[n - 1][c] > maxScore) {
                maxScore = dp[n - 1][c]
            }
        }
        return maxScore
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxPathScore(List<List<int>> grid, int k) {
    int m = grid.length;
    int n = grid[0].length;
    int effectiveK = k > m + n ? m + n : k;
    List<List<int>> dp = List.generate(n, (_) => List.filled(effectiveK + 1, -1));

    int cost0 = grid[0][0] == 0 ? 0 : 1;
    if (cost0 <= effectiveK) {
      dp[0][cost0] = grid[0][0];
    }

    for (int i = 0; i < m; i++) {
      List<List<int>> nextDp = List.generate(n, (_) => List.filled(effectiveK + 1, -1));
      for (int j = 0; j < n; j++) {
        if (i == 0 && j == 0) {
          if (cost0 <= effectiveK) nextDp[0][cost0] = grid[0][0];
          continue;
        }
        int cellCost = grid[i][j] == 0 ? 0 : 1;
        int cellScore = grid[i][j];
        for (int c = cellCost; c <= effectiveK; c++) {
          int prevMax = -1;
          if (i > 0 && dp[j][c - cellCost] != -1) {
            if (dp[j][c - cellCost] > prevMax) prevMax = dp[j][c - cellCost];
          }
          if (j > 0 && nextDp[j - 1][c - cellCost] != -1) {
            if (nextDp[j - 1][c - cellCost] > prevMax) prevMax = nextDp[j - 1][c - cellCost];
          }
          if (prevMax != -1) {
            nextDp[j][c] = prevMax + cellScore;
          }
        }
      }
      dp = nextDp;
    }

    int maxScore = -1;
    for (int c = 0; c <= effectiveK; c++) {
      if (dp[n - 1][c] > maxScore) {
        maxScore = dp[n - 1][c];
      }
    }
    return maxScore;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxPathScore(grid [][]int, k int) int {
	m := len(grid)
	n := len(grid[0])
	effectiveK := k
	if effectiveK > m+n {
		effectiveK = m + n
	}

	dp := make([][]int, n)
	for j := range dp {
		dp[j] = make([]int, effectiveK+1)
		for c := range dp[j] {
			dp[j][c] = -1
		}
	}

	cost0 := 0
	if grid[0][0] != 0 {
		cost0 = 1
	}
	if cost0 <= effectiveK {
		dp[0][cost0] = grid[0][0]
	}

	for i := 0; i < m; i++ {
		nextDp := make([][]int, n)
		for r := range nextDp {
			nextDp[r] = make([]int, effectiveK+1)
			for c := range nextDp[r] {
				nextDp[r][c] = -1
			}
		}

		for j := 0; j < n; j++ {
			if i == 0 && j == 0 {
				if cost0 <= effectiveK {
					nextDp[0][cost0] = grid[0][0]
				}
				continue
			}
			cellCost := 0
			if grid[i][j] != 0 {
				cellCost = 1
			}
			cellScore := grid[i][j]

			for c := cellCost; c <= effectiveK; c++ {
				prevMax := -1
				if i > 0 && dp[j][c-cellCost] != -1 {
					prevMax = dp[j][c-cellCost]
				}
				if j > 0 && nextDp[j-1][c-cellCost] != -1 {
					if nextDp[j-1][c-cellCost] > prevMax {
						prevMax = nextDp[j-1][c-cellCost]
					}
				}
				if prevMax != -1 {
					nextDp[j][c] = prevMax + cellScore
				}
			}
		}
		dp = nextDp
	}

	maxScore := -1
	for c := 0; c <= effectiveK; c++ {
		if dp[n-1][c] > maxScore {
			maxScore = dp[n-1][c]
		}
	}
	return maxScore
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def max_path_score(grid, k)
  m = grid.length
  n = grid[0].length
  k_limit = k < m + n ? k : m + n
  dp = Array.new(n) { Array.new(k_limit + 1, -1) }

  cost0 = grid[0][0] == 0 ? 0 : 1
  dp[0][cost0] = grid[0][0] if cost0 <= k_limit

  (0...m).each do |i|
    next_dp = Array.new(n) { Array.new(k_limit + 1, -1) }
    (0...n).each do |j|
      if i == 0 && j == 0
        next_dp[0][cost0] = grid[0][0] if cost0 <= k_limit
        next
      end

      cell_cost = grid[i][j] == 0 ? 0 : 1
      cell_score = grid[i][j]

      (cell_cost..k_limit).each do |c|
        prev_max = -1
        if i > 0 && dp[j][c - cell_cost] != -1
          prev_max = dp[j][c - cell_cost]
        end
        if j > 0 && next_dp[j - 1][c - cell_cost] != -1
          left_v = next_dp[j - 1][c - cell_cost]
          prev_max = left_v if left_v > prev_max
        end

        next_dp[j][c] = prev_max + cell_score if prev_max != -1
      end
    end
    dp = next_dp
  end

  max_s = dp[n - 1].max
  max_s.nil? || max_s < 0 ? -1 : max_s
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def maxPathScore(grid: Array[Array[Int]], k: Int): Int = {
    val m = grid.length
    val n = grid(0).length
    val effectiveK = if (k > m + n) m + n else k
    var dp = Array.fill(n, effectiveK + 1)(-1)

    val cost0 = if (grid(0)(0) == 0) 0 else 1
    if (cost0 <= effectiveK) {
      dp(0)(cost0) = grid(0)(0)
    }

    for (i <- 0 until m) {
      val nextDp = Array.fill(n, effectiveK + 1)(-1)
      for (j <- 0 until n) {
        if (i == 0 && j == 0) {
          if (cost0 <= effectiveK) nextDp(0)(cost0) = grid(0)(0)
        } else {
          val cellCost = if (grid(i)(j) == 0) 0 else 1
          val cellScore = grid(i)(j)
          for (c <- cellCost to effectiveK) {
            var prevMax = -1
            if (i > 0 && dp(j)(c - cellCost) != -1) {
              prevMax = Math.max(prevMax, dp(j)(c - cellCost))
            }
            if (j > 0 && nextDp(j - 1)(c - cellCost) != -1) {
              prevMax = Math.max(prevMax, nextDp(j - 1)(c - cellCost))
            }
            if (prevMax != -1) {
              nextDp(j)(c) = prevMax + cellScore
            }
          }
        }
      }
      dp = nextDp
    }

    var maxScore = -1
    for (c <- 0 to effectiveK) {
      maxScore = Math.max(maxScore, dp(n - 1)(c))
    }
    maxScore
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_path_score(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let k_usize = k as usize;
        let mut dp = vec![vec![-1; k_usize + 1]; n];

        for i in 0..m {
            let mut next_dp = vec![vec![-1; k_usize + 1]; n];
            for j in 0..n {
                let val = grid[i][j];
                let ci = if val == 0 { 0 } else { 1 };
                let si = val;

                if i == 0 && j == 0 {
                    next_dp[0][0] = 0;
                    continue;
                }

                for c in ci..=k_usize {
                    let mut max_prev = -1;
                    if i > 0 {
                        max_prev = max_prev.max(dp[j][c - ci]);
                    }
                    if j > 0 {
                        max_prev = max_prev.max(next_dp[j - 1][c - ci]);
                    }

                    if max_prev != -1 {
                        next_dp[j][c] = max_prev + si;
                    }
                }
            }
            dp = next_dp;
        }

        let mut ans = -1;
        for c in 0..=k_usize {
            ans = ans.max(dp[n - 1][c]);
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
(define/contract (max-path-score grid k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ([m (length grid)]
         [n (length (first grid))]
         [k1 (+ k 1)]
         [grid-vec (list->vector (map list->vector grid))]
         [dp (make-vector (* n k1) -1)])

    (vector-set! dp 0 0)

    (for ([i (in-range m)])
      (let ([next-dp (make-vector (* n k1) -1)])
        (for ([j (in-range n)])
          (let* ([val (vector-ref (vector-ref grid-vec i) j)]
                 [ci (if (= val 0) 0 1)]
                 [si val])
            (if (and (= i 0) (= j 0))
                (vector-set! next-dp 0 0)
                (for ([c (in-range ci k1)])
                  (let* ([prev-c (- c ci)]
                         [max-prev -1])
                    (when (> i 0)
                      (let ([v (vector-ref dp (+ (* j k1) prev-c))])
                        (when (> v max-prev) (set! max-prev v))))
                    (when (> j 0)
                      (let ([v (vector-ref next-dp (+ (* (- j 1) k1) prev-c))])
                        (when (> v max-prev) (set! max-prev v))))

                    (when (> max-prev -1)
                      (vector-set! next-dp (+ (* j k1) c) (+ max-prev si))))))))
        (set! dp next-dp)))

    (let ([ans -1])
      (for ([c (in-range k1)])
        (let ([v (vector-ref dp (+ (* (- n 1) k1) c))])
          (when (> v ans) (set! ans v))))
      ans)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_path_score(Grid :: [[integer()]], K :: integer()) -> integer().
max_path_score(Grid, K) ->
    M = length(Grid),
    N = length(hd(Grid)),
    GridVec = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),
    InitialDP = list_to_tuple([list_to_tuple([-1 || _ <- lists:seq(0, K)]) || _ <- lists:seq(1, N)]),
    FinalDP = solve(0, M, N, K, GridVec, InitialDP),
    LastCol = element(N, FinalDP),
    lists:max([-1 | tuple_to_list(LastCol)]).

solve(I, M, N, K, GridVec, PrevDP) when I < M ->
    GridRow = element(I + 1, GridVec),
    CurrRow = solve_row(0, N, I, K, GridRow, PrevDP, []),
    solve(I + 1, M, N, K, GridVec, CurrRow);
solve(_, _, _, _, _, PrevDP) ->
    PrevDP.

solve_row(J, N, I, K, GridRow, PrevDP, RowCurrentList) when J < N ->
    Val = element(J + 1, GridRow),
    Ci = if Val == 0 -> 0; true -> 1 end,
    Si = Val,
    ColDP = if
        I == 0, J == 0 -> 
            list_to_tuple([0 | [-1 || _ <- lists:seq(1, K)]]);
        true ->
            ColAbove = element(J + 1, PrevDP),
            ColLeft = if J > 0 -> hd(RowCurrentList); true -> undefined end,
            build_col(0, K, Ci, Si, I, J, ColAbove, ColLeft, [])
    end,
    solve_row(J + 1, N, I, K, GridRow, PrevDP, [ColDP | RowCurrentList]);
solve_row(_, _, _, _, _, _, RowCurrentList) ->
    list_to_tuple(lists:reverse(RowCurrentList)).

build_col(C, K, Ci, Si, I, J, ColAbove, ColLeft, Acc) when C =< K ->
    PrevC = C - Ci,
    Score = if
        PrevC < 0 -> -1;
        true ->
            VAbove = if I > 0 -> element(PrevC + 1, ColAbove); true -> -1 end,
            VLeft = if J > 0 -> element(PrevC + 1, ColLeft); true -> -1 end,
            MaxP = if VAbove > VLeft -> VAbove; true -> VLeft end,
            if MaxP == -1 -> -1; true -> MaxP + Si end
    end,
    build_col(C + 1, K, Ci, Si, I, J, ColAbove, ColLeft, [Score | Acc]);
build_col(_, _, _, _, _, _, _, _, Acc) ->
    list_to_tuple(lists:reverse(Acc)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_path_score(grid :: [[integer]], k :: integer) :: integer
  def max_path_score(grid, k) do
    m = length(grid)
    n = length(hd(grid))
    grid_matrix = grid |> Enum.map(&List.to_tuple/1) |> List.to_tuple()
    initial_dp = List.duplicate(List.duplicate(-1, k + 1) |> List.to_tuple(), n) |> List.to_tuple()
    final_dp = solve(0, m, n, k, grid_matrix, initial_dp)
    last_col = elem(final_dp, n - 1)
    last_col |> Tuple.to_list() |> Enum.max() |> max(-1)
  end

  defp solve(i, m, n, k, grid_matrix, prev_dp) when i < m do
    grid_row = elem(grid_matrix, i)
    curr_row = solve_row(0, n, i, k, grid_row, prev_dp, [])
    solve(i + 1, m, n, k, grid_matrix, curr_row)
  end
  defp solve(_, _, _, _, _, prev_dp), do: prev_dp

  defp solve_row(j, n, i, k, grid_row, prev_dp, row_current_list) when j < n do
    val = elem(grid_row, j)
    ci = if val == 0, do: 0, else: 1
    si = val
    col_dp = cond do
      i == 0 and j == 0 ->
        List.to_tuple([0 | List.duplicate(-1, k)])
      true ->
        col_above = elem(prev_dp, j)
        col_left = if j > 0, do: hd(row_current_list), else: nil
        build_col(0, k, ci, si, i, j, col_above, col_left, [])
    end
    solve_row(j + 1, n, i, k, grid_row, prev_dp, [col_dp | row_current_list])
  end
  defp solve_row(_, _, _, _, _, _, row_current_list) do
    row_current_list |> Enum.reverse() |> List.to_tuple()
  end

  defp build_col(c, k, ci, si, i, j, col_above, col_left, acc) when c <= k do
    prev_c = c - ci
    score = if prev_c < 0 do
      -1
    else
      v_above = if i > 0, do: elem(col_above, prev_c), else: -1
      v_left = if j > 0, do: elem(col_left, prev_c), else: -1
      max_p = max(v_above, v_left)
      if max_p == -1, do: -1, else: max_p + si
    end
    build_col(c + 1, k, ci, si, i, j, col_above, col_left, [score | acc])
  end
  defp build_col(_, _, _, _, _, _, _, _, acc) do
    acc |> Enum.reverse() |> List.to_tuple()
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m * n * min(k, m + n)) where m and n are the grid dimensions. Since any path from the top-left to the bottom-right has a fixed length of m + n - 1 and each cell adds at most 1 to the cost, the total cost never exceeds m + n - 1, allowing us to cap the effective value of k.
- **Space Complexity:** O(n * min(k, m + n)) because we only need the DP results from the previous row and the cell to the left in the current row to compute the next state. We use two DP rows (or a slightly optimized version of this) to maintain results for only the current and previous grid states.
