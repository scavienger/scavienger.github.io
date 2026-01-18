---
layout: post
title: "Largest Magic Square"
date: 2026-01-18 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Matrix", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/largest-magic-square/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int largestMagicSquare(std::vector<std::vector<int>>&\
        \ grid) {\n        int m = grid.size();\n        int n = grid[0].size();\n\n\
        \        std::vector<std::vector<long long>> R(m, std::vector<long long>(n +\
        \ 1, 0));\n        for (int i = 0; i < m; ++i) {\n            for (int j = 0;\
        \ j < n; ++j) {\n                R[i][j+1] = R[i][j] + grid[i][j];\n       \
        \     }\n        }\n\n        std::vector<std::vector<long long>> C(m + 1, std::vector<long\
        \ long>(n, 0));\n        for (int j = 0; j < n; ++j) {\n            for (int\
        \ i = 0; i < m; ++i) {\n                C[i+1][j] = C[i][j] + grid[i][j];\n\
        \            }\n        }\n\n        for (int k = std::min(m, n); k >= 1; --k)\
        \ {\n            for (int r = 0; r <= m - k; ++r) {\n                for (int\
        \ c = 0; c <= n - k; ++c) {\n\n                    long long target_sum = R[r][c+k]\
        \ - R[r][c];\n\n                    bool is_magic = true;\n\n              \
        \      for (int i = 0; i < k; ++i) {\n                        if ((R[r+i][c+k]\
        \ - R[r+i][c]) != target_sum) {\n                            is_magic = false;\n\
        \                            break;\n                        }\n           \
        \         }\n                    if (!is_magic) {\n                        continue;\n\
        \                    }\n\n                    for (int j = 0; j < k; ++j) {\n\
        \                        if ((C[r+k][c+j] - C[r][c+j]) != target_sum) {\n  \
        \                          is_magic = false;\n                            break;\n\
        \                        }\n                    }\n                    if (!is_magic)\
        \ {\n                        continue;\n                    }\n\n          \
        \          long long diag_sum = 0;\n                    for (int i = 0; i <\
        \ k; ++i) {\n                        diag_sum += grid[r+i][c+i];\n         \
        \           }\n                    if (diag_sum != target_sum) {\n         \
        \               is_magic = false;\n                    }\n                 \
        \   if (!is_magic) {\n                        continue;\n                  \
        \  }\n\n                    long long anti_diag_sum = 0;\n                 \
        \   for (int i = 0; i < k; ++i) {\n                        anti_diag_sum +=\
        \ grid[r+i][c+k-1-i];\n                    }\n                    if (anti_diag_sum\
        \ != target_sum) {\n                        is_magic = false;\n            \
        \        }\n                    if (!is_magic) {\n                        continue;\n\
        \                    }\n\n                    return k;\n                }\n\
        \            }\n        }\n\n        return 1;\n    }\n};"
      java: "class Solution {\n    public int largestMagicSquare(int[][] grid) {\n \
        \       int m = grid.length;\n        int n = grid[0].length;\n\n        long[][]\
        \ R = new long[m][n + 1];\n        for (int i = 0; i < m; ++i) {\n         \
        \   for (int j = 0; j < n; ++j) {\n                R[i][j+1] = R[i][j] + grid[i][j];\n\
        \            }\n        }\n\n        long[][] C = new long[m + 1][n];\n    \
        \    for (int j = 0; j < n; ++j) {\n            for (int i = 0; i < m; ++i)\
        \ {\n                C[i+1][j] = C[i][j] + grid[i][j];\n            }\n    \
        \    }\n\n        for (int k = Math.min(m, n); k >= 1; --k) {\n            for\
        \ (int r = 0; r <= m - k; ++r) {\n                for (int c = 0; c <= n - k;\
        \ ++c) {\n\n                    long target_sum = R[r][c+k] - R[r][c];\n\n \
        \                   boolean is_magic = true;\n\n                    for (int\
        \ i = 0; i < k; ++i) {\n                        if ((R[r+i][c+k] - R[r+i][c])\
        \ != target_sum) {\n                            is_magic = false;\n        \
        \                    break;\n                        }\n                   \
        \ }\n                    if (!is_magic) {\n                        continue;\n\
        \                    }\n\n                    for (int j = 0; j < k; ++j) {\n\
        \                        if ((C[r+k][c+j] - C[r][c+j]) != target_sum) {\n  \
        \                          is_magic = false;\n                            break;\n\
        \                        }\n                    }\n                    if (!is_magic)\
        \ {\n                        continue;\n                    }\n\n          \
        \          long diag_sum = 0;\n                    for (int i = 0; i < k; ++i)\
        \ {\n                        diag_sum += grid[r+i][c+i];\n                 \
        \   }\n                    if (diag_sum != target_sum) {\n                 \
        \       is_magic = false;\n                    }\n                    if (!is_magic)\
        \ {\n                        continue;\n                    }\n\n          \
        \          long anti_diag_sum = 0;\n                    for (int i = 0; i <\
        \ k; ++i) {\n                        anti_diag_sum += grid[r+i][c+k-1-i];\n\
        \                    }\n                    if (anti_diag_sum != target_sum)\
        \ {\n                        is_magic = false;\n                    }\n    \
        \                if (!is_magic) {\n                        continue;\n     \
        \               }\n\n                    return k;\n                }\n    \
        \        }\n        }\n\n        return 1;\n    }\n}"
      python: "class Solution(object):\n    def largestMagicSquare(self, grid):\n  \
        \      \"\"\"\n        :type grid: List[List[int]]\n        :rtype: int\n  \
        \      \"\"\"\n        m, n = len(grid), len(grid[0])\n\n        R = [[0] *\
        \ (n + 1) for _ in range(m)]\n        for i in range(m):\n            for j\
        \ in range(n):\n                R[i][j+1] = R[i][j] + grid[i][j]\n\n       \
        \ C = [[0] * n for _ in range(m + 1)]\n        for j in range(n):\n        \
        \    for i in range(m):\n                C[i+1][j] = C[i][j] + grid[i][j]\n\n\
        \        for k in range(min(m, n), 0, -1):\n            for r in range(m - k\
        \ + 1):\n                for c in range(n - k + 1):\n\n                    target_sum\
        \ = R[r][c+k] - R[r][c]\n\n                    is_magic = True\n\n         \
        \           for i in range(k):\n                        if (R[r+i][c+k] - R[r+i][c])\
        \ != target_sum:\n                            is_magic = False\n           \
        \                 break\n                    if not is_magic:\n            \
        \            continue\n\n                    for j in range(k):\n          \
        \              if (C[r+k][c+j] - C[r][c+j]) != target_sum:\n               \
        \             is_magic = False\n                            break\n        \
        \            if not is_magic:\n                        continue\n\n        \
        \            diag_sum = 0\n                    for i in range(k):\n        \
        \                diag_sum += grid[r+i][c+i]\n                    if diag_sum\
        \ != target_sum:\n                        is_magic = False\n               \
        \     if not is_magic:\n                        continue\n\n               \
        \     anti_diag_sum = 0\n                    for i in range(k):\n          \
        \              anti_diag_sum += grid[r+i][c+k-1-i]\n                    if anti_diag_sum\
        \ != target_sum:\n                        is_magic = False\n               \
        \     if not is_magic:\n                        continue\n\n               \
        \     return k\n\n        return 1"
      python3: "class Solution:\n    def largestMagicSquare(self, grid: List[List[int]])\
        \ -> int:\n        m, n = len(grid), len(grid[0])\n\n        R = [[0] * (n +\
        \ 1) for _ in range(m)]\n        for i in range(m):\n            for j in range(n):\n\
        \                R[i][j+1] = R[i][j] + grid[i][j]\n\n        C = [[0] * n for\
        \ _ in range(m + 1)]\n        for j in range(n):\n            for i in range(m):\n\
        \                C[i+1][j] = C[i][j] + grid[i][j]\n\n        for k in range(min(m,\
        \ n), 0, -1):\n            for r in range(m - k + 1):\n                for c\
        \ in range(n - k + 1):\n\n                    target_sum = R[r][c+k] - R[r][c]\n\
        \n                    is_magic = True\n\n                    for i in range(k):\n\
        \                        if (R[r+i][c+k] - R[r+i][c]) != target_sum:\n     \
        \                       is_magic = False\n                            break\n\
        \                    if not is_magic:\n                        continue\n\n\
        \                    for j in range(k):\n                        if (C[r+k][c+j]\
        \ - C[r][c+j]) != target_sum:\n                            is_magic = False\n\
        \                            break\n                    if not is_magic:\n \
        \                       continue\n\n                    diag_sum = 0\n     \
        \               for i in range(k):\n                        diag_sum += grid[r+i][c+i]\n\
        \                    if diag_sum != target_sum:\n                        is_magic\
        \ = False\n                    if not is_magic:\n                        continue\n\
        \n                    anti_diag_sum = 0\n                    for i in range(k):\n\
        \                        anti_diag_sum += grid[r+i][c+k-1-i]\n             \
        \       if anti_diag_sum != target_sum:\n                        is_magic =\
        \ False\n                    if not is_magic:\n                        continue\n\
        \n                    return k\n\n        return 1"
      c: "#include <stdlib.h>\n\nint largestMagicSquare(int** grid, int gridSize, int*\
        \ gridColSize) {\n    int m = gridSize;\n    int n = gridColSize[0];\n\n   \
        \ long long** R = (long long**)malloc(m * sizeof(long long*));\n    for (int\
        \ i = 0; i < m; ++i) {\n        R[i] = (long long*)calloc(n + 1, sizeof(long\
        \ long));\n        for (int j = 0; j < n; ++j) {\n            R[i][j+1] = R[i][j]\
        \ + grid[i][j];\n        }\n    }\n\n    long long** C = (long long**)malloc((m\
        \ + 1) * sizeof(long long*));\n    for (int i = 0; i < m + 1; ++i) {\n     \
        \   C[i] = (long long*)calloc(n, sizeof(long long));\n    }\n    for (int j\
        \ = 0; j < n; ++j) {\n        for (int i = 0; i < m; ++i) {\n            C[i+1][j]\
        \ = C[i][j] + grid[i][j];\n        }\n    }\n\n    int min_mn = (m < n) ? m\
        \ : n;\n    for (int k = min_mn; k >= 1; --k) {\n        for (int r = 0; r <=\
        \ m - k; ++r) {\n            for (int c = 0; c <= n - k; ++c) {\n\n        \
        \        long long target_sum = R[r][c+k] - R[r][c];\n\n                int\
        \ is_magic = 1;\n\n                for (int i = 0; i < k; ++i) {\n         \
        \           if ((R[r+i][c+k] - R[r+i][c]) != target_sum) {\n               \
        \         is_magic = 0;\n                        break;\n                  \
        \  }\n                }\n                if (!is_magic) {\n                \
        \    continue;\n                }\n\n                for (int j = 0; j < k;\
        \ ++j) {\n                    if ((C[r+k][c+j] - C[r][c+j]) != target_sum) {\n\
        \                        is_magic = 0;\n                        break;\n   \
        \                 }\n                }\n                if (!is_magic) {\n \
        \                   continue;\n                }\n\n                long long\
        \ diag_sum = 0;\n                for (int i = 0; i < k; ++i) {\n           \
        \         diag_sum += grid[r+i][c+i];\n                }\n                if\
        \ (diag_sum != target_sum) {\n                    is_magic = 0;\n          \
        \      }\n                if (!is_magic) {\n                    continue;\n\
        \                }\n\n                long long anti_diag_sum = 0;\n       \
        \         for (int i = 0; i < k; ++i) {\n                    anti_diag_sum +=\
        \ grid[r+i][c+k-1-i];\n                }\n                if (anti_diag_sum\
        \ != target_sum) {\n                    is_magic = 0;\n                }\n \
        \               if (!is_magic) {\n                    continue;\n          \
        \      }\n\n                for (int i = 0; i < m; ++i) {\n                \
        \    free(R[i]);\n                }\n                free(R);\n            \
        \    for (int i = 0; i < m + 1; ++i) {\n                    free(C[i]);\n  \
        \              }\n                free(C);\n                return k;\n    \
        \        }\n        }\n    }\n\n    for (int i = 0; i < m; ++i) {\n        free(R[i]);\n\
        \    }\n    free(R);\n    for (int i = 0; i < m + 1; ++i) {\n        free(C[i]);\n\
        \    }\n    free(C);\n    return 1;\n}"
      csharp: "public class Solution {\n    public int LargestMagicSquare(int[][] grid)\
        \ {\n        int m = grid.Length;\n        int n = grid[0].Length;\n\n     \
        \   long[][] R = new long[m][n + 1];\n        for (int i = 0; i < m; ++i) {\n\
        \            for (int j = 0; j < n; ++j) {\n                R[i][j+1] = R[i][j]\
        \ + grid[i][j];\n            }\n        }\n\n        long[][] C = new long[m\
        \ + 1][n];\n        for (int j = 0; j < n; ++j) {\n            for (int i =\
        \ 0; i < m; ++i) {\n                C[i+1][j] = C[i][j] + grid[i][j];\n    \
        \        }\n        }\n\n        for (int k = Math.Min(m, n); k >= 1; --k) {\n\
        \            for (int r = 0; r <= m - k; ++r) {\n                for (int c\
        \ = 0; c <= n - k; ++c) {\n\n                    long target_sum = R[r][c+k]\
        \ - R[r][c];\n\n                    bool is_magic = true;\n\n              \
        \      for (int i = 0; i < k; ++i) {\n                        if ((R[r+i][c+k]\
        \ - R[r+i][c]) != target_sum) {\n                            is_magic = false;\n\
        \                            break;\n                        }\n           \
        \         }\n                    if (!is_magic) {\n                        continue;\n\
        \                    }\n\n                    for (int j = 0; j < k; ++j) {\n\
        \                        if ((C[r+k][c+j] - C[r][c+j]) != target_sum) {\n  \
        \                          is_magic = false;\n                            break;\n\
        \                        }\n                    }\n                    if (!is_magic)\
        \ {\n                        continue;\n                    }\n\n          \
        \          long diag_sum = 0;\n                    for (int i = 0; i < k; ++i)\
        \ {\n                        diag_sum += grid[r+i][c+i];\n                 \
        \   }\n                    if (diag_sum != target_sum) {\n                 \
        \       is_magic = false;\n                    }\n                    if (!is_magic)\
        \ {\n                        continue;\n                    }\n\n          \
        \          long anti_diag_sum = 0;\n                    for (int i = 0; i <\
        \ k; ++i) {\n                        anti_diag_sum += grid[r+i][c+k-1-i];\n\
        \                    }\n                    if (anti_diag_sum != target_sum)\
        \ {\n                        is_magic = false;\n                    }\n    \
        \                if (!is_magic) {\n                        continue;\n     \
        \               }\n\n                    return k;\n                }\n    \
        \        }\n        }\n\n        return 1;\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @return {number}\n */\nvar largestMagicSquare\
        \ = function(grid) {\n    let m = grid.length;\n    let n = grid[0].length;\n\
        \n    let R = Array(m).fill(0).map(() => Array(n + 1).fill(0));\n    for (let\
        \ i = 0; i < m; ++i) {\n        for (let j = 0; j < n; ++j) {\n            R[i][j+1]\
        \ = R[i][j] + grid[i][j];\n        }\n    }\n\n    let C = Array(m + 1).fill(0).map(()\
        \ => Array(n).fill(0));\n    for (let j = 0; j < n; ++j) {\n        for (let\
        \ i = 0; i < m; ++i) {\n            C[i+1][j] = C[i][j] + grid[i][j];\n    \
        \    }\n    }\n\n    for (let k = Math.min(m, n); k >= 1; --k) {\n        for\
        \ (let r = 0; r <= m - k; ++r) {\n            for (let c = 0; c <= n - k; ++c)\
        \ {\n\n                let target_sum = R[r][c+k] - R[r][c];\n\n           \
        \     let is_magic = true;\n\n                for (let i = 0; i < k; ++i) {\n\
        \                    if ((R[r+i][c+k] - R[r+i][c]) !== target_sum) {\n     \
        \                   is_magic = false;\n                        break;\n    \
        \                }\n                }\n                if (!is_magic) {\n  \
        \                  continue;\n                }\n\n                for (let\
        \ j = 0; j < k; ++j) {\n                    if ((C[r+k][c+j] - C[r][c+j]) !==\
        \ target_sum) {\n                        is_magic = false;\n               \
        \         break;\n                    }\n                }\n               \
        \ if (!is_magic) {\n                    continue;\n                }\n\n   \
        \             let diag_sum = 0;\n                for (let i = 0; i < k; ++i)\
        \ {\n                    diag_sum += grid[r+i][c+i];\n                }\n  \
        \              if (diag_sum !== target_sum) {\n                    is_magic\
        \ = false;\n                }\n                if (!is_magic) {\n          \
        \          continue;\n                }\n\n                let anti_diag_sum\
        \ = 0;\n                for (let i = 0; i < k; ++i) {\n                    anti_diag_sum\
        \ += grid[r+i][c+k-1-i];\n                }\n                if (anti_diag_sum\
        \ !== target_sum) {\n                    is_magic = false;\n               \
        \ }\n                if (!is_magic) {\n                    continue;\n     \
        \           }\n\n                return k;\n            }\n        }\n    }\n\
        \n    return 1;\n};"
      typescript: "function largestMagicSquare(grid: number[][]): number {\n    let\
        \ m = grid.length;\n    let n = grid[0].length;\n\n    let R: number[][] = Array(m).fill(0).map(()\
        \ => Array(n + 1).fill(0));\n    for (let i = 0; i < m; ++i) {\n        for\
        \ (let j = 0; j < n; ++j) {\n            R[i][j+1] = R[i][j] + grid[i][j];\n\
        \        }\n    }\n\n    let C: number[][] = Array(m + 1).fill(0).map(() =>\
        \ Array(n).fill(0));\n    for (let j = 0; j < n; ++j) {\n        for (let i\
        \ = 0; i < m; ++i) {\n            C[i+1][j] = C[i][j] + grid[i][j];\n      \
        \  }\n    }\n\n    for (let k = Math.min(m, n); k >= 1; --k) {\n        for\
        \ (let r = 0; r <= m - k; ++r) {\n            for (let c = 0; c <= n - k; ++c)\
        \ {\n\n                let target_sum = R[r][c+k] - R[r][c];\n\n           \
        \     let is_magic = true;\n\n                for (let i = 0; i < k; ++i) {\n\
        \                    if ((R[r+i][c+k] - R[r+i][c]) !== target_sum) {\n     \
        \                   is_magic = false;\n                        break;\n    \
        \                }\n                }\n                if (!is_magic) {\n  \
        \                  continue;\n                }\n\n                for (let\
        \ j = 0; j < k; ++j) {\n                    if ((C[r+k][c+j] - C[r][c+j]) !==\
        \ target_sum) {\n                        is_magic = false;\n               \
        \         break;\n                    }\n                }\n               \
        \ if (!is_magic) {\n                    continue;\n                }\n\n   \
        \             let diag_sum = 0;\n                for (let i = 0; i < k; ++i)\
        \ {\n                    diag_sum += grid[r+i][c+i];\n                }\n  \
        \              if (diag_sum !== target_sum) {\n                    is_magic\
        \ = false;\n                }\n                if (!is_magic) {\n          \
        \          continue;\n                }\n\n                let anti_diag_sum\
        \ = 0;\n                for (let i = 0; i < k; ++i) {\n                    anti_diag_sum\
        \ += grid[r+i][c+k-1-i];\n                }\n                if (anti_diag_sum\
        \ !== target_sum) {\n                    is_magic = false;\n               \
        \ }\n                if (!is_magic) {\n                    continue;\n     \
        \           }\n\n                return k;\n            }\n        }\n    }\n\
        \n    return 1;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @return\
        \ Integer\n     */\n    function largestMagicSquare($grid) {\n        $m = count($grid);\n\
        \        $n = count($grid[0]);\n\n        $R = array_fill(0, $m, array_fill(0,\
        \ $n + 1, 0));\n        for ($i = 0; $i < $m; ++$i) {\n            for ($j =\
        \ 0; $j < $n; ++$j) {\n                $R[$i][$j+1] = $R[$i][$j] + $grid[$i][$j];\n\
        \            }\n        }\n\n        $C = array_fill(0, $m + 1, array_fill(0,\
        \ $n, 0));\n        for ($j = 0; $j < $n; ++$j) {\n            for ($i = 0;\
        \ $i < $m; ++$i) {\n                $C[$i+1][$j] = $C[$i][$j] + $grid[$i][$j];\n\
        \            }\n        }\n\n        $min_mn = min($m, $n);\n        for ($k\
        \ = $min_mn; $k >= 1; --$k) {\n            for ($r = 0; $r <= $m - $k; ++$r)\
        \ {\n                for ($c = 0; $c <= $n - $k; ++$c) {\n\n               \
        \     $target_sum = $R[$r][$c+$k] - $R[$r][$c];\n\n                    $is_magic\
        \ = true;\n\n                    for ($i = 0; $i < $k; ++$i) {\n           \
        \             if (($R[$r+$i][$c+$k] - $R[$r+$i][$c]) != $target_sum) {\n   \
        \                         $is_magic = false;\n                            break;\n\
        \                        }\n                    }\n                    if (!$is_magic)\
        \ {\n                        continue;\n                    }\n\n          \
        \          for ($j = 0; $j < $k; ++$j) {\n                        if (($C[$r+$k][$c+$j]\
        \ - $C[$r][$c+$j]) != $target_sum) {\n                            $is_magic\
        \ = false;\n                            break;\n                        }\n\
        \                    }\n                    if (!$is_magic) {\n            \
        \            continue;\n                    }\n\n                    $diag_sum\
        \ = 0;\n                    for ($i = 0; $i < $k; ++$i) {\n                \
        \        $diag_sum += $grid[$r+$i][$c+$i];\n                    }\n        \
        \            if ($diag_sum != $target_sum) {\n                        $is_magic\
        \ = false;\n                    }\n                    if (!$is_magic) {\n \
        \                       continue;\n                    }\n\n               \
        \     $anti_diag_sum = 0;\n                    for ($i = 0; $i < $k; ++$i) {\n\
        \                        $anti_diag_sum += $grid[$r+$i][$c+$k-1-$i];\n     \
        \               }\n                    if ($anti_diag_sum != $target_sum) {\n\
        \                        $is_magic = false;\n                    }\n       \
        \             if (!$is_magic) {\n                        continue;\n       \
        \             }\n\n                    return $k;\n                }\n     \
        \       }\n        }\n\n        return 1;\n    }\n}"
      swift: "class Solution {\n    func largestMagicSquare(_ grid: [[Int]]) -> Int\
        \ {\n        let m = grid.count\n        let n = grid[0].count\n\n        var\
        \ R = Array(repeating: Array(repeating: 0, count: n + 1), count: m)\n      \
        \  for i in 0..<m {\n            for j in 0..<n {\n                R[i][j+1]\
        \ = R[i][j] + grid[i][j]\n            }\n        }\n\n        var C = Array(repeating:\
        \ Array(repeating: 0, count: n), count: m + 1)\n        for j in 0..<n {\n \
        \           for i in 0..<m {\n                C[i+1][j] = C[i][j] + grid[i][j]\n\
        \            }\n        }\n\n        let minMN = min(m, n)\n        for k in\
        \ (1...minMN).reversed() {\n            for r in 0...(m - k) {\n           \
        \     for c in 0...(n - k) {\n\n                    let target_sum = R[r][c+k]\
        \ - R[r][c]\n\n                    var is_magic = true\n\n                 \
        \   for i in 0..<k {\n                        if (R[r+i][c+k] - R[r+i][c]) !=\
        \ target_sum {\n                            is_magic = false\n             \
        \               break\n                        }\n                    }\n  \
        \                  if !is_magic {\n                        continue\n      \
        \              }\n\n                    for i in 0..<k {\n                 \
        \       if (C[r+k][c+i] - C[r][c+i]) != target_sum {\n                     \
        \       is_magic = false\n                            break\n              \
        \          }\n                    }\n                    if !is_magic {\n  \
        \                      continue\n                    }\n\n                 \
        \   var diag_sum = 0\n                    for i in 0..<k {\n               \
        \         diag_sum += grid[r+i][c+i]\n                    }\n              \
        \      if diag_sum != target_sum {\n                        is_magic = false\n\
        \                    }\n                    if !is_magic {\n               \
        \         continue\n                    }\n\n                    var anti_diag_sum\
        \ = 0\n                    for i in 0..<k {\n                        anti_diag_sum\
        \ += grid[r+i][c+k-1-i]\n                    }\n                    if anti_diag_sum\
        \ != target_sum {\n                        is_magic = false\n              \
        \      }\n                    if !is_magic {\n                        continue\n\
        \                    }\n\n                    return k\n                }\n\
        \            }\n        }\n\n        return 1\n    }\n}"
      kotlin: "class Solution {\n    fun largestMagicSquare(grid: Array<IntArray>):\
        \ Int {\n        val m = grid.size\n        val n = grid[0].size\n\n       \
        \ val rowPrefixSums = Array(m) { LongArray(n + 1) }\n        for (i in 0 until\
        \ m) {\n            for (j in 0 until n) {\n                rowPrefixSums[i][j\
        \ + 1] = rowPrefixSums[i][j] + grid[i][j]\n            }\n        }\n\n    \
        \    val colPrefixSums = Array(m + 1) { LongArray(n) }\n        for (j in 0\
        \ until n) {\n            for (i in 0 until m) {\n                colPrefixSums[i\
        \ + 1][j] = colPrefixSums[i][j] + grid[i][j]\n            }\n        }\n\n \
        \       for (k in Math.min(m, n) downTo 1) {\n            for (r in 0..m - k)\
        \ {\n                for (c in 0..n - k) {\n                    if (isMagicSquare(r,\
        \ c, k, grid, rowPrefixSums, colPrefixSums)) {\n                        return\
        \ k\n                    }\n                }\n            }\n        }\n  \
        \      return 1 // Every 1x1 grid is a magic square\n    }\n\n    private fun\
        \ isMagicSquare(\n        r: Int, c: Int, k: Int,\n        grid: Array<IntArray>,\n\
        \        rowPrefixSums: Array<LongArray>,\n        colPrefixSums: Array<LongArray>\n\
        \    ): Boolean {\n        val targetSum = rowPrefixSums[r][c + k] - rowPrefixSums[r][c]\n\
        \n        // Check row sums\n        for (i in r until r + k) {\n          \
        \  if (rowPrefixSums[i][c + k] - rowPrefixSums[i][c] != targetSum) {\n     \
        \           return false\n            }\n        }\n\n        // Check column\
        \ sums\n        for (j in c until c + k) {\n            if (colPrefixSums[r\
        \ + k][j] - colPrefixSums[r][j] != targetSum) {\n                return false\n\
        \            }\n        }\n\n        // Check main diagonal sum\n        var\
        \ diag1Sum: Long = 0\n        for (x in 0 until k) {\n            diag1Sum +=\
        \ grid[r + x][c + x]\n        }\n        if (diag1Sum != targetSum) {\n    \
        \        return false\n        }\n\n        // Check anti-diagonal sum\n   \
        \     var diag2Sum: Long = 0\n        for (x in 0 until k) {\n            diag2Sum\
        \ += grid[r + x][c + k - 1 - x]\n        }\n        if (diag2Sum != targetSum)\
        \ {\n            return false\n        }\n\n        return true\n    }\n}"
      dart: "class Solution {\n  int largestMagicSquare(List<List<int>> grid) {\n  \
        \  final int m = grid.length;\n    final int n = grid[0].length;\n\n    final\
        \ List<List<int>> rowPrefixSums = List.generate(m, (_) => List.filled(n + 1,\
        \ 0));\n    for (int i = 0; i < m; i++) {\n      for (int j = 0; j < n; j++)\
        \ {\n        rowPrefixSums[i][j + 1] = rowPrefixSums[i][j] + grid[i][j];\n \
        \     }\n    }\n\n    final List<List<int>> colPrefixSums = List.generate(m\
        \ + 1, (_) => List.filled(n, 0));\n    for (int j = 0; j < n; j++) {\n     \
        \ for (int i = 0; i < m; i++) {\n        colPrefixSums[i + 1][j] = colPrefixSums[i][j]\
        \ + grid[i][j];\n      }\n    }\n\n    for (int k = (m < n ? m : n); k >= 1;\
        \ k--) {\n      for (int r = 0; r <= m - k; r++) {\n        for (int c = 0;\
        \ c <= n - k; c++) {\n          if (isMagicSquare(r, c, k, grid, rowPrefixSums,\
        \ colPrefixSums)) {\n            return k;\n          }\n        }\n      }\n\
        \    }\n    return 1; // Every 1x1 grid is a magic square\n  }\n\n  bool isMagicSquare(\n\
        \    int r, int c, int k,\n    List<List<int>> grid,\n    List<List<int>> rowPrefixSums,\n\
        \    List<List<int>> colPrefixSums\n  ) {\n    final int targetSum = rowPrefixSums[r][c\
        \ + k] - rowPrefixSums[r][c];\n\n    // Check row sums\n    for (int i = r;\
        \ i < r + k; i++) {\n      if (rowPrefixSums[i][c + k] - rowPrefixSums[i][c]\
        \ != targetSum) {\n        return false;\n      }\n    }\n\n    // Check column\
        \ sums\n    for (int j = c; j < c + k; j++) {\n      if (colPrefixSums[r + k][j]\
        \ - colPrefixSums[r][j] != targetSum) {\n        return false;\n      }\n  \
        \  }\n\n    // Check main diagonal sum\n    int diag1Sum = 0;\n    for (int\
        \ x = 0; x < k; x++) {\n      diag1Sum += grid[r + x][c + x];\n    }\n    if\
        \ (diag1Sum != targetSum) {\n      return false;\n    }\n\n    // Check anti-diagonal\
        \ sum\n    int diag2Sum = 0;\n    for (int x = 0; x < k; x++) {\n      diag2Sum\
        \ += grid[r + x][c + k - 1 - x];\n    }\n    if (diag2Sum != targetSum) {\n\
        \      return false;\n    }\n\n    return true;\n  }\n}"
      go: "func largestMagicSquare(grid [][]int) int {\n    m := len(grid)\n    n :=\
        \ len(grid[0])\n\n    rowPrefixSums := make([][]int, m)\n    for i := 0; i <\
        \ m; i++ {\n        rowPrefixSums[i] = make([]int, n+1)\n        for j := 0;\
        \ j < n; j++ {\n            rowPrefixSums[i][j+1] = rowPrefixSums[i][j] + grid[i][j]\n\
        \        }\n    }\n\n    colPrefixSums := make([][]int, m+1)\n    for i := 0;\
        \ i <= m; i++ {\n        colPrefixSums[i] = make([]int, n)\n    }\n    for j\
        \ := 0; j < n; j++ {\n        for i := 0; i < m; i++ {\n            colPrefixSums[i+1][j]\
        \ = colPrefixSums[i][j] + grid[i][j]\n        }\n    }\n\n    minDim := m\n\
        \    if n < minDim {\n        minDim = n\n    }\n\n    for k := minDim; k >=\
        \ 1; k-- {\n        for r := 0; r <= m-k; r++ {\n            for c := 0; c <=\
        \ n-k; c++ {\n                if isMagicSquare(r, c, k, grid, rowPrefixSums,\
        \ colPrefixSums) {\n                    return k\n                }\n      \
        \      }\n        }\n    }\n    return 1 // Every 1x1 grid is a magic square\n\
        }\n\nfunc isMagicSquare(\n    r, c, k int,\n    grid [][]int,\n    rowPrefixSums\
        \ [][]int,\n    colPrefixSums [][]int\n) bool {\n    targetSum := rowPrefixSums[r][c+k]\
        \ - rowPrefixSums[r][c]\n\n    // Check row sums\n    for i := r; i < r+k; i++\
        \ {\n        if rowPrefixSums[i][c+k]-rowPrefixSums[i][c] != targetSum {\n \
        \           return false\n        }\n    }\n\n    // Check column sums\n   \
        \ for j := c; j < c+k; j++ {\n        if colPrefixSums[r+k][j]-colPrefixSums[r][j]\
        \ != targetSum {\n            return false\n        }\n    }\n\n    // Check\
        \ main diagonal sum\n    diag1Sum := 0\n    for x := 0; x < k; x++ {\n     \
        \   diag1Sum += grid[r+x][c+x]\n    }\n    if diag1Sum != targetSum {\n    \
        \    return false\n    }\n\n    // Check anti-diagonal sum\n    diag2Sum :=\
        \ 0\n    for x := 0; x < k; x++ {\n        diag2Sum += grid[r+x][c+k-1-x]\n\
        \    }\n    if diag2Sum != targetSum {\n        return false\n    }\n\n    return\
        \ true\n}"
      ruby: "# @param {Integer[][]} grid\n# @return {Integer}\ndef largest_magic_square(grid)\n\
        \    m = grid.length\n    n = grid[0].length\n\n    row_prefix_sums = Array.new(m)\
        \ { Array.new(n + 1, 0) }\n    (0...m).each do |i|\n        (0...n).each do\
        \ |j|\n            row_prefix_sums[i][j + 1] = row_prefix_sums[i][j] + grid[i][j]\n\
        \        end\n    end\n\n    col_prefix_sums = Array.new(m + 1) { Array.new(n,\
        \ 0) }\n    (0...n).each do |j|\n        (0...m).each do |i|\n            col_prefix_sums[i\
        \ + 1][j] = col_prefix_sums[i][j] + grid[i][j]\n        end\n    end\n\n   \
        \ min_dim = [m, n].min\n\n    min_dim.downto(1) do |k|\n        (0..m - k).each\
        \ do |r|\n            (0..n - k).each do |c|\n                if is_magic_square(r,\
        \ c, k, grid, row_prefix_sums, col_prefix_sums)\n                    return\
        \ k\n                end\n            end\n        end\n    end\n    1 # Every\
        \ 1x1 grid is a magic square\nend\n\ndef is_magic_square(r, c, k, grid, row_prefix_sums,\
        \ col_prefix_sums)\n    target_sum = row_prefix_sums[r][c + k] - row_prefix_sums[r][c]\n\
        \n    # Check row sums\n    (r...r + k).each do |i|\n        if row_prefix_sums[i][c\
        \ + k] - row_prefix_sums[i][c] != target_sum\n            return false\n   \
        \     end\n    end\n\n    # Check column sums\n    (c...c + k).each do |j|\n\
        \        if col_prefix_sums[r + k][j] - col_prefix_sums[r][j] != target_sum\n\
        \            return false\n        end\n    end\n\n    # Check main diagonal\
        \ sum\n    diag1_sum = 0\n    (0...k).each do |x|\n        diag1_sum += grid[r\
        \ + x][c + x]\n    end\n    if diag1_sum != target_sum\n        return false\n\
        \    end\n\n    # Check anti-diagonal sum\n    diag2_sum = 0\n    (0...k).each\
        \ do |x|\n        diag2_sum += grid[r + x][c + k - 1 - x]\n    end\n    if diag2_sum\
        \ != target_sum\n        return false\n    end\n\n    true\nend"
      scala: "object Solution {\n    def largestMagicSquare(grid: Array[Array[Int]]):\
        \ Int = {\n        val m = grid.length\n        val n = grid(0).length\n\n \
        \       val rowPrefixSums = Array.ofDim[Long](m, n + 1)\n        for (i <- 0\
        \ until m) {\n            for (j <- 0 until n) {\n                rowPrefixSums(i)(j\
        \ + 1) = rowPrefixSums(i)(j) + grid(i)(j)\n            }\n        }\n\n    \
        \    val colPrefixSums = Array.ofDim[Long](m + 1, n)\n        for (j <- 0 until\
        \ n) {\n            for (i <- 0 until m) {\n                colPrefixSums(i\
        \ + 1)(j) = colPrefixSums(i)(j) + grid(i)(j)\n            }\n        }\n\n \
        \       val minDim = Math.min(m, n)\n\n        for (k <- minDim to 1 by -1)\
        \ {\n            for (r <- 0 to m - k) {\n                for (c <- 0 to n -\
        \ k) {\n                    if (isMagicSquare(r, c, k, grid, rowPrefixSums,\
        \ colPrefixSums)) {\n                        return k\n                    }\n\
        \                }\n            }\n        }\n        1 // Every 1x1 grid is\
        \ a magic square\n    }\n\n    private def isMagicSquare(\n        r: Int, c:\
        \ Int, k: Int,\n        grid: Array[Array[Int]],\n        rowPrefixSums: Array[Array[Long]],\n\
        \        colPrefixSums: Array[Array[Long]]\n    ): Boolean = {\n        val\
        \ targetSum = rowPrefixSums(r)(c + k) - rowPrefixSums(r)(c)\n\n        // Check\
        \ row sums\n        for (i <- r until r + k) {\n            if (rowPrefixSums(i)(c\
        \ + k) - rowPrefixSums(i)(c) != targetSum) {\n                return false\n\
        \            }\n        }\n\n        // Check column sums\n        for (j <-\
        \ c until c + k) {\n            if (colPrefixSums(r + k)(j) - colPrefixSums(r)(j)\
        \ != targetSum) {\n                return false\n            }\n        }\n\n\
        \        // Check main diagonal sum\n        var diag1Sum: Long = 0\n      \
        \  for (x <- 0 until k) {\n            diag1Sum += grid(r + x)(c + x)\n    \
        \    }\n        if (diag1Sum != targetSum) {\n            return false\n   \
        \     }\n\n        // Check anti-diagonal sum\n        var diag2Sum: Long =\
        \ 0\n        for (x <- 0 until k) {\n            diag2Sum += grid(r + x)(c +\
        \ k - 1 - x)\n        }\n        if (diag2Sum != targetSum) {\n            return\
        \ false\n        }\n\n        true\n    }\n}"
      rust: "impl Solution {\n    pub fn largest_magic_square(grid: Vec<Vec<i32>>) ->\
        \ i32 {\n        let m = grid.len();\n        let n = grid[0].len();\n\n   \
        \     let mut row_prefix_sums = vec![vec![0; n + 1]; m];\n        for i in 0..m\
        \ {\n            for j in 0..n {\n                row_prefix_sums[i][j + 1]\
        \ = row_prefix_sums[i][j] + grid[i][j];\n            }\n        }\n\n      \
        \  let mut col_prefix_sums = vec![vec![0; n]; m + 1];\n        for j in 0..n\
        \ {\n            for i in 0..m {\n                col_prefix_sums[i + 1][j]\
        \ = col_prefix_sums[i][j] + grid[i][j];\n            }\n        }\n\n      \
        \  let min_dim = m.min(n);\n\n        for k in (1..=min_dim).rev() {\n     \
        \       for r in 0..=(m - k) {\n                for c in 0..=(n - k) {\n   \
        \                 if Self::is_magic_square(r, c, k, &grid, &row_prefix_sums,\
        \ &col_prefix_sums) {\n                        return k as i32;\n          \
        \          }\n                }\n            }\n        }\n        1 // Every\
        \ 1x1 grid is a magic square\n    }\n\n    fn is_magic_square(\n        r: usize,\
        \ c: usize, k: usize,\n        grid: &Vec<Vec<i32>>,\n        row_prefix_sums:\
        \ &Vec<Vec<i32>>,\n        col_prefix_sums: &Vec<Vec<i32>>\n    ) -> bool {\n\
        \        let target_sum = row_prefix_sums[r][c + k] - row_prefix_sums[r][c];\n\
        \n        // Check row sums\n        for i in r..(r + k) {\n            if row_prefix_sums[i][c\
        \ + k] - row_prefix_sums[i][c] != target_sum {\n                return false;\n\
        \            }\n        }\n\n        // Check column sums\n        for j in\
        \ c..(c + k) {\n            if col_prefix_sums[r + k][j] - col_prefix_sums[r][j]\
        \ != target_sum {\n                return false;\n            }\n        }\n\
        \n        // Check main diagonal sum\n        let mut diag1_sum = 0;\n     \
        \   for x in 0..k {\n            diag1_sum += grid[r + x][c + x];\n        }\n\
        \        if diag1_sum != target_sum {\n            return false;\n        }\n\
        \n        // Check anti-diagonal sum\n        let mut diag2_sum = 0;\n     \
        \   for x in 0..k {\n            diag2_sum += grid[r + x][c + k - 1 - x];\n\
        \        }\n        if diag2_sum != target_sum {\n            return false;\n\
        \        }\n\n        true\n    }\n}"
      racket: "(define/contract (largest-magic-square grid)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer?)\n  (define m (length grid))\n  (define n (length (car grid)))\n\
        \n  ;; Precompute row prefix sums\n  (define row-prefix-sums (make-vector m))\n\
        \  (for ([i (in-range m)])\n    (define current-row (list-ref grid i))\n   \
        \ (define row-sums-vec (make-vector (+ n 1) 0))\n    (for ([j (in-range n)])\n\
        \      (vector-set! row-sums-vec (+ j 1) (+ (vector-ref row-sums-vec j) (list-ref\
        \ current-row j))))\n    (vector-set! row-prefix-sums i row-sums-vec))\n\n \
        \ ;; Precompute column prefix sums\n  (define col-prefix-sums (make-vector (+\
        \ m 1)))\n  (for ([i (in-range (+ m 1))])\n    (vector-set! col-prefix-sums\
        \ i (make-vector n 0)))\n  (for ([j (in-range n)])\n    (for ([i (in-range m)])\n\
        \      (vector-set! (vector-ref col-prefix-sums (+ i 1)) j\n               \
        \    (+ (vector-ref (vector-ref col-prefix-sums i) j)\n                    \
        \  (list-ref (list-ref grid i) j)))))\n\n  (define (is-magic-square? r c k)\n\
        \    (define target-sum (- (vector-ref (vector-ref row-prefix-sums r) (+ c k))\n\
        \                          (vector-ref (vector-ref row-prefix-sums r) c)))\n\
        \n    ;; Check row sums\n    (for ([i (in-range r (+ r k))])\n      (when (!=\
        \ (- (vector-ref (vector-ref row-prefix-sums i) (+ c k))\n                 \
        \  (vector-ref (vector-ref row-prefix-sums i) c))\n               target-sum)\n\
        \        (return-from is-magic-square? #f)))\n\n    ;; Check column sums\n \
        \   (for ([j (in-range c (+ c k))])\n      (when (!= (- (vector-ref (vector-ref\
        \ col-prefix-sums (+ r k)) j)\n                   (vector-ref (vector-ref col-prefix-sums\
        \ r) j))\n               target-sum)\n        (return-from is-magic-square?\
        \ #f)))\n\n    ;; Check main diagonal sum\n    (define diag1-sum 0)\n    (for\
        \ ([x (in-range k)])\n      (set! diag1-sum (+ diag1-sum (list-ref (list-ref\
        \ grid (+ r x)) (+ c x)))))\n    (when (!= diag1-sum target-sum)\n      (return-from\
        \ is-magic-square? #f))\n\n    ;; Check anti-diagonal sum\n    (define diag2-sum\
        \ 0)\n    (for ([x (in-range k)])\n      (set! diag2-sum (+ diag2-sum (list-ref\
        \ (list-ref grid (+ r x)) (- (+ c k 1) x 1)))))\n    (when (!= diag2-sum target-sum)\n\
        \      (return-from is-magic-square? #f))\n\n    #t)\n\n  (define min-dim (min\
        \ m n))\n\n  (for ([k (in-range min-dim 0 -1)])\n    (for ([r (in-range (+ (-\
        \ m k) 1))])\n      (for ([c (in-range (+ (- n k) 1))])\n        (when (is-magic-square?\
        \ r c k)\n          (return-from largest-magic-square k)))))\n  1)"
      erlang: "-spec largest_magic_square(Grid :: [[integer()]]) -> integer().\nlargest_magic_square(Grid)\
        \ ->\n  M = length(Grid),\n  N = length(hd(Grid)),\n\n  % Precompute row prefix\
        \ sums\n  RowPrefixSums = lists:map(fun(Row) ->\n    lists:foldl(fun(Val, Acc)\
        \ -> Acc ++ [hd(Acc) + Val] end, [0], Row)\n  end, Grid),\n\n  % Precompute\
        \ column prefix sums\n  ColPrefixSumsList = lists:foldl(fun(Row, Acc) ->\n \
        \   [lists:zipwith(fun(ColSum, Val) -> ColSum + Val end, hd(Acc), Row) | Acc]\n\
        \  end, [[lists:duplicate(N, 0)]], Grid),\n  ColPrefixSumsReversed = lists:reverse(ColPrefixSumsList),\n\
        \n  % Helper function to get element from list of lists (0-indexed)\n  GetElem\
        \ = fun(List, R, C) ->\n    lists:nth(C + 1, lists:nth(R + 1, List))\n  end,\n\
        \n  % Helper function to get row prefix sum\n  GetRowPrefixSum = fun(R, C_end,\
        \ C_start) ->\n    lists:nth(C_end + 1, lists:nth(R + 1, RowPrefixSums)) - lists:nth(C_start\
        \ + 1, lists:nth(R + 1, RowPrefixSums))\n  end,\n\n  % Helper function to get\
        \ column prefix sum\n  GetColPrefixSum = fun(R_end, R_start, C) ->\n    lists:nth(C\
        \ + 1, lists:nth(R_end + 1, ColPrefixSumsReversed)) - lists:nth(C + 1, lists:nth(R_start\
        \ + 1, ColPrefixSumsReversed))\n  end,\n\n  IsMagicSquare = fun(R, C, K) ->\n\
        \    TargetSum = GetRowPrefixSum(R, C + K, C),\n\n    % Check row sums\n   \
        \ RowSumsOk = lists:all(fun(I) ->\n      GetRowPrefixSum(I, C + K, C) == TargetSum\n\
        \    end, lists:seq(R, R + K - 1)),\n\n    % Check column sums\n    ColSumsOk\
        \ = lists:all(fun(J) ->\n      GetColPrefixSum(R + K, R, J) == TargetSum\n \
        \   end, lists:seq(C, C + K - 1)),\n\n    % Check main diagonal sum\n    Diag1Sum\
        \ = lists:foldl(fun(X, Acc) ->\n      Acc + GetElem(Grid, R + X, C + X)\n  \
        \  end, 0, lists:seq(0, K - 1)),\n    Diag1Ok = Diag1Sum == TargetSum,\n\n \
        \   % Check anti-diagonal sum\n    Diag2Sum = lists:foldl(fun(X, Acc) ->\n \
        \     Acc + GetElem(Grid, R + X, C + K - 1 - X)\n    end, 0, lists:seq(0, K\
        \ - 1)),\n    Diag2Ok = Diag2Sum == TargetSum,\n\n    RowSumsOk andalso ColSumsOk\
        \ andalso Diag1Ok andalso Diag2Ok\n  end,\n\n  MinDim = min(M, N),\n\n  lists:foldl(fun(K,\
        \ Acc) ->\n    case lists:foldl(fun(R, InnerAcc) ->\n      case lists:foldl(fun(C,\
        \ InnermostAcc) ->\n        if InnermostAcc /= 0 -> InnermostAcc; % Already\
        \ found a magic square\n           IsMagicSquare(R, C, K) -> K;\n          \
        \ true -> 0\n        end\n      end, 0, lists:seq(0, N - K)) of\n      0 ->\
        \ InnerAcc;\n      FoundK -> FoundK\n    end\n    end, 0, lists:seq(0, M - K))\
        \ of\n    0 -> Acc;\n    FoundK -> FoundK\n  end\n  end, 1, lists:seq(MinDim,\
        \ 1, -1))."
      elixir: "defmodule Solution do\n  @spec largest_magic_square(grid :: [[integer]])\
        \ :: integer\n  def largest_magic_square(grid) do\n    m = Enum.count(grid)\n\
        \    n = Enum.count(hd(grid))\n\n    # Precompute row prefix sums\n    row_prefix_sums\
        \ = Enum.map(grid, fn row ->\n      Enum.reduce(row, [0], fn val, acc -> acc\
        \ ++ [List.last(acc) + val] end)\n    end)\n\n    # Precompute column prefix\
        \ sums\n    # col_prefix_sums[i][j] stores sum of grid[0][j] to grid[i-1][j]\n\
        \    col_prefix_sums = \n      Enum.reduce(0..(m-1), [[List.duplicate(0, n)]],\
        \ fn i, acc ->\n        prev_row_sums = List.first(acc)\n        current_row\
        \ = Enum.at(grid, i)\n        new_row_sums = \n          Enum.zip(prev_row_sums,\
        \ current_row)\n          |> Enum.map(fn {col_sum, val} -> col_sum + val end)\n\
        \        [new_row_sums | acc]\n      end)\n      |> Enum.reverse()\n\n    #\
        \ Helper function to get element from list of lists (0-indexed)\n    get_elem\
        \ = fn list, r, c ->\n      list |> Enum.at(r) |> Enum.at(c)\n    end\n\n  \
        \  # Helper function to get row prefix sum\n    get_row_prefix_sum = fn r, c_end,\
        \ c_start ->\n      Enum.at(row_prefix_sums, r) |> Enum.at(c_end + 1) - (Enum.at(row_prefix_sums,\
        \ r) |> Enum.at(c_start + 1))\n    end\n\n    # Helper function to get column\
        \ prefix sum\n    get_col_prefix_sum = fn r_end, r_start, c ->\n      Enum.at(col_prefix_sums,\
        \ r_end + 1) |> Enum.at(c) - (Enum.at(col_prefix_sums, r_start + 1) |> Enum.at(c))\n\
        \    end\n\n    is_magic_square = fn r, c, k ->\n      target_sum = get_row_prefix_sum.(r,\
        \ c + k, c)\n\n      # Check row sums\n      row_sums_ok = Enum.all?(r..(r +\
        \ k - 1), fn i ->\n        get_row_prefix_sum.(i, c + k, c) == target_sum\n\
        \      end)\n\n      # Check column sums\n      col_sums_ok = Enum.all?(c..(c\
        \ + k - 1), fn j ->\n        get_col_prefix_sum.(r + k, r, j) == target_sum\n\
        \      end)\n\n      # Check main diagonal sum\n      diag1_sum = Enum.reduce(0..(k\
        \ - 1), 0, fn x, acc ->\n        acc + get_elem.(grid, r + x, c + x)\n     \
        \ end)\n      diag1_ok = diag1_sum == target_sum\n\n      # Check anti-diagonal\
        \ sum\n      diag2_sum = Enum.reduce(0..(k - 1), 0, fn x, acc ->\n        acc\
        \ + get_elem.(grid, r + x, c + k - 1 - x)\n      end)\n      diag2_ok = diag2_sum\
        \ == target_sum\n\n      row_sums_ok && col_sums_ok && diag1_ok && diag2_ok\n\
        \    end\n\n    min_dim = min(m, n)\n\n    Enum.reduce(min_dim..1, 1, fn k,\
        \ acc ->\n      if acc != 1, do: acc, # Already found a larger magic square\n\
        \      else: (\n        found_k = \n          Enum.reduce_while(0..(m - k),\
        \ 0, fn r, _ ->\n            found_k_in_row = \n              Enum.reduce_while(0..(n\
        \ - k), 0, fn c, _ ->\n                if is_magic_square.(r, c, k) do\n   \
        \               {:halt, k}\n                else\n                  {:cont,\
        \ 0}\n                end\n              end)\n            if found_k_in_row\
        \ != 0 do\n              {:halt, found_k_in_row}\n            else\n       \
        \       {:cont, 0}\n            end\n          end)\n        if found_k != 0,\
        \ do: found_k, else: acc\n      )\n    end)\n  end\nend"
    approach: 'The problem asks for the size of the largest magic square within a given
      grid. A k x k magic square requires all its row sums, column sums, and both diagonal
      sums to be equal. Since every 1x1 grid is trivially a magic square, the answer
      is at least 1. The constraints (m, n <= 50) suggest that a polynomial time complexity
      involving m and n, up to around O(m*n*min(m,n)^2), would be acceptable.


      The core idea is to iterate through all possible square sizes `k` from `min(m,
      n)` down to `1`. For each `k`, we iterate through all possible top-left corners
      `(r, c)` in the grid where a `k x k` square can start. The first `k` for which
      we find a valid magic square will be the largest. To efficiently check if a `k
      x k` square is magic, we precompute two prefix sum arrays: `row_prefix_sums[i][j]`
      stores the sum of elements in `grid[i]` from index `0` to `j-1`, and `col_prefix_sums[i][j]`
      stores the sum of elements in `grid[0][j]` to `grid[i-1][j]`. These prefix sums
      allow us to calculate any row or column sum within a square in O(1) time.


      With the prefix sum arrays, checking a `k x k` square starting at `(r, c)` involves
      several steps. First, we calculate the sum of the first row of the candidate square
      using `row_prefix_sums` to establish a `target_sum`. Then, we verify that all
      other `k-1` row sums and all `k` column sums (using `row_prefix_sums` and `col_prefix_sums`
      respectively) are equal to this `target_sum`. Finally, we directly compute the
      sums of the main diagonal and anti-diagonal (each taking O(k) time) and compare
      them to the `target_sum`. If all these checks pass, we have found a magic square
      of size `k`, and since we are iterating `k` downwards, this `k` is the largest
      possible, so we return it immediately.'
    time_complexity: The time complexity is dominated by the nested loops for `k`, `r`,
      and `c`, and the `check` function. Precomputing prefix sums takes O(m*n) time.
      The outer loop for `k` runs `min(m, n)` times. The loops for `r` and `c` run `(m-k+1)`
      and `(n-k+1)` times respectively. Inside these loops, the `check` function takes
      O(k) time (O(1) for each row/column sum using prefix sums, and O(k) for each diagonal
      sum). Thus, the total time complexity is approximately O(sum_{k=1}^{min(m,n)}
      (m-k+1)(n-k+1) * k), which simplifies to O(m*n*min(m,n)^2). Given m, n <= 50,
      this is roughly 50 * 50 * 50^2 = 6.25 * 10^6 operations, which is efficient enough.
    space_complexity: The space complexity is determined by the two prefix sum arrays,
      `row_prefix_sums` and `col_prefix_sums`. `row_prefix_sums` has dimensions `m x
      (n+1)` and `col_prefix_sums` has dimensions `(m+1) x n`. Therefore, the total
      space complexity is O(m*n). For m, n <= 50, this is 50 * 50 = 2500 integers, which
      is a very small memory footprint.
    elapsed_time: 188.10139179229736
    model: gemini-2.5-flash
    generated_at: '2026-01-18 01:18:28 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int largestMagicSquare(vector<vector<int>>&\
        \ grid) {\n        int m = grid.size(), n = grid[0].size(), max_size = min(m,\
        \ n);\n        for (int k = max_size; k > 0; --k) {\n            for (int i\
        \ = 0; i <= m - k; ++i) {\n                for (int j = 0; j <= n - k; ++j)\
        \ {\n                    if (isMagic(grid, i, j, k)) return k;\n           \
        \     }\n            }\n        }\n        return 1;\n    }\n\n    bool isMagic(vector<vector<int>>&\
        \ grid, int x, int y, int k) {\n        int sum = 0;\n        for (int i = x;\
        \ i < x + k; ++i) sum += grid[i][y];\n        for (int i = x; i < x + k; ++i)\
        \ {\n            int row_sum = 0, col_sum = 0;\n            for (int j = y;\
        \ j < y + k; ++j) {\n                row_sum += grid[i][j];\n              \
        \  col_sum += grid[i + j - x][y + j - x];\n            }\n            if (row_sum\
        \ != sum || col_sum != sum) return false;\n        }\n        int dia_sum1 =\
        \ 0, dia_sum2 = 0;\n        for (int i = 0; i < k; ++i) {\n            dia_sum1\
        \ += grid[x + i][y + i];\n            dia_sum2 += grid[x + i][y + k - 1 - i];\n\
        \        }\n        return dia_sum1 == sum && dia_sum2 == sum;\n    }\n};"
      java: "class Solution {\n    public int largestMagicSquare(int[][] grid) {\n \
        \       int m = grid.length, n = grid[0].length, max_size = Math.min(m, n);\n\
        \        for (int k = max_size; k > 0; --k) {\n            for (int i = 0; i\
        \ <= m - k; ++i) {\n                for (int j = 0; j <= n - k; ++j) {\n   \
        \                 if (isMagic(grid, i, j, k)) return k;\n                }\n\
        \            }\n        }\n        return 1;\n    }\n\n    private boolean isMagic(int[][]\
        \ grid, int x, int y, int k) {\n        int sum = 0;\n        for (int i = x;\
        \ i < x + k; ++i) sum += grid[i][y];\n        for (int i = x; i < x + k; ++i)\
        \ {\n            int row_sum = 0, col_sum = 0;\n            for (int j = y;\
        \ j < y + k; ++j) {\n                row_sum += grid[i][j];\n              \
        \  col_sum += grid[i + j - x][y + j - x];\n            }\n            if (row_sum\
        \ != sum || col_sum != sum) return false;\n        }\n        int dia_sum1 =\
        \ 0, dia_sum2 = 0;\n        for (int i = 0; i < k; ++i) {\n            dia_sum1\
        \ += grid[x + i][y + i];\n            dia_sum2 += grid[x + i][y + k - 1 - i];\n\
        \        }\n        return dia_sum1 == sum && dia_sum2 == sum;\n    }\n}"
      python: "class Solution(object):\n    def largestMagicSquare(self, grid):\n  \
        \      m, n = len(grid), len(grid[0])\n        max_size = min(m, n)\n      \
        \  for k in range(max_size, 0, -1):\n            for i in range(m - k + 1):\n\
        \                for j in range(n - k + 1):\n                    if self.isMagic(grid,\
        \ i, j, k):\n                        return k\n        return 1\n\n    def isMagic(self,\
        \ grid, x, y, k):\n        sum_val = sum(grid[x][y:y+k])\n        for i in range(x,\
        \ x+k):\n            if sum(grid[i][y:y+k]) != sum_val:\n                return\
        \ False\n        for j in range(y, y+k):\n            if sum(grid[i][j] for\
        \ i in range(x, x+k)) != sum_val:\n                return False\n        dia_sum1\
        \ = sum(grid[x+i][y+i] for i in range(k))\n        dia_sum2 = sum(grid[x+i][y+k-1-i]\
        \ for i in range(k))\n        return dia_sum1 == sum_val and dia_sum2 == sum_val"
      python3: "class Solution:\n    def largestMagicSquare(self, grid: list[list[int]])\
        \ -> int:\n        m, n = len(grid), len(grid[0])\n        max_size = min(m,\
        \ n)\n        for k in range(max_size, 0, -1):\n            for i in range(m\
        \ - k + 1):\n                for j in range(n - k + 1):\n                  \
        \  if self.isMagic(grid, i, j, k):\n                        return k\n     \
        \   return 1\n\n    def isMagic(self, grid: list[list[int]], x: int, y: int,\
        \ k: int) -> bool:\n        sum_val = sum(grid[x][y:y+k])\n        for i in\
        \ range(x, x+k):\n            if sum(grid[i][y:y+k]) != sum_val:\n         \
        \       return False\n        for j in range(y, y+k):\n            if sum(grid[i][j]\
        \ for i in range(x, x+k)) != sum_val:\n                return False\n      \
        \  dia_sum1 = sum(grid[x+i][y+i] for i in range(k))\n        dia_sum2 = sum(grid[x+i][y+k-1-i]\
        \ for i in range(k))\n        return dia_sum1 == sum_val and dia_sum2 == sum_val"
      c: "int largestMagicSquare(int** grid, int gridSize, int* gridColSize) {\n   \
        \ int m = gridSize, n = *gridColSize, max_size = (m < n) ? m : n;\n    for (int\
        \ k = max_size; k > 0; --k) {\n        for (int i = 0; i <= m - k; ++i) {\n\
        \            for (int j = 0; j <= n - k; ++j) {\n                if (isMagic(grid,\
        \ i, j, k, n)) return k;\n            }\n        }\n    }\n    return 1;\n}\n\
        \nint isMagic(int** grid, int x, int y, int k, int n) {\n    int sum = 0;\n\
        \    for (int i = x; i < x + k; ++i) sum += grid[i][y];\n    for (int i = x;\
        \ i < x + k; ++i) {\n        int row_sum = 0, col_sum = 0;\n        for (int\
        \ j = y; j < y + k; ++j) {\n            row_sum += grid[i][j];\n           \
        \ col_sum += grid[i + j - x][y + j - x];\n        }\n        if (row_sum !=\
        \ sum || col_sum != sum) return 0;\n    }\n    int dia_sum1 = 0, dia_sum2 =\
        \ 0;\n    for (int i = 0; i < k; ++i) {\n        dia_sum1 += grid[x + i][y +\
        \ i];\n        dia_sum2 += grid[x + i][y + k - 1 - i];\n    }\n    return dia_sum1\
        \ == sum && dia_sum2 == sum;\n}"
      csharp: "public class Solution {\n    public int LargestMagicSquare(int[][] grid)\
        \ {\n        int m = grid.Length, n = grid[0].Length, max_size = Math.Min(m,\
        \ n);\n        for (int k = max_size; k > 0; --k) {\n            for (int i\
        \ = 0; i <= m - k; ++i) {\n                for (int j = 0; j <= n - k; ++j)\
        \ {\n                    if (IsMagic(grid, i, j, k)) return k;\n           \
        \     }\n            }\n        }\n        return 1;\n    }\n\n    private bool\
        \ IsMagic(int[][] grid, int x, int y, int k) {\n        int sum = 0;\n     \
        \   for (int i = x; i < x + k; ++i) sum += grid[i][y];\n        for (int i =\
        \ x; i < x + k; ++i) {\n            int row_sum = 0, col_sum = 0;\n        \
        \    for (int j = y; j < y + k; ++j) {\n                row_sum += grid[i][j];\n\
        \                col_sum += grid[i + j - x][y + j - x];\n            }\n   \
        \         if (row_sum != sum || col_sum != sum) return false;\n        }\n \
        \       int dia_sum1 = 0, dia_sum2 = 0;\n        for (int i = 0; i < k; ++i)\
        \ {\n            dia_sum1 += grid[x + i][y + i];\n            dia_sum2 += grid[x\
        \ + i][y + k - 1 - i];\n        }\n        return dia_sum1 == sum && dia_sum2\
        \ == sum;\n    }\n}"
      javascript: "var largestMagicSquare = function(grid) {\n    let m = grid.length,\
        \ n = grid[0].length, max_size = Math.min(m, n);\n    for (let k = max_size;\
        \ k > 0; --k) {\n        for (let i = 0; i <= m - k; ++i) {\n            for\
        \ (let j = 0; j <= n - k; ++j) {\n                if (isMagic(grid, i, j, k))\
        \ return k;\n            }\n        }\n    }\n    return 1;\n};\n\nfunction\
        \ isMagic(grid, x, y, k) {\n    let sum = 0;\n    for (let i = x; i < x + k;\
        \ ++i) sum += grid[i][y];\n    for (let i = x; i < x + k; ++i) {\n        let\
        \ row_sum = 0, col_sum = 0;\n        for (let j = y; j < y + k; ++j) {\n   \
        \         row_sum += grid[i][j];\n            col_sum += grid[i + j - x][y +\
        \ j - x];\n        }\n        if (row_sum != sum || col_sum != sum) return false;\n\
        \    }\n    let dia_sum1 = 0, dia_sum2 = 0;\n    for (let i = 0; i < k; ++i)\
        \ {\n        dia_sum1 += grid[x + i][y + i];\n        dia_sum2 += grid[x + i][y\
        \ + k - 1 - i];\n    }\n    return dia_sum1 == sum && dia_sum2 == sum;\n}"
      typescript: "function largestMagicSquare(grid: number[][]): number {\n    let\
        \ m = grid.length, n = grid[0].length, max_size = Math.min(m, n);\n    for (let\
        \ k = max_size; k > 0; --k) {\n        for (let i = 0; i <= m - k; ++i) {\n\
        \            for (let j = 0; j <= n - k; ++j) {\n                if (isMagic(grid,\
        \ i, j, k)) return k;\n            }\n        }\n    }\n    return 1;\n}\n\n\
        function isMagic(grid: number[][], x: number, y: number, k: number): boolean\
        \ {\n    let sum = 0;\n    for (let i = x; i < x + k; ++i) sum += grid[i][y];\n\
        \    for (let i = x; i < x + k; ++i) {\n        let row_sum = 0, col_sum = 0;\n\
        \        for (let j = y; j < y + k; ++j) {\n            row_sum += grid[i][j];\n\
        \            col_sum += grid[i + j - x][y + j - x];\n        }\n        if (row_sum\
        \ != sum || col_sum != sum) return false;\n    }\n    let dia_sum1 = 0, dia_sum2\
        \ = 0;\n    for (let i = 0; i < k; ++i) {\n        dia_sum1 += grid[x + i][y\
        \ + i];\n        dia_sum2 += grid[x + i][y + k - 1 - i];\n    }\n    return\
        \ dia_sum1 == sum && dia_sum2 == sum;\n}"
      php: "class Solution {\n    function largestMagicSquare($grid) {\n        $m =\
        \ count($grid);\n        $n = count($grid[0]);\n        $max_size = min($m,\
        \ $n);\n        for ($k = $max_size; $k > 0; --$k) {\n            for ($i =\
        \ 0; $i <= $m - $k; ++$i) {\n                for ($j = 0; $j <= $n - $k; ++$j)\
        \ {\n                    if ($this->isMagic($grid, $i, $j, $k)) return $k;\n\
        \                }\n            }\n        }\n        return 1;\n    }\n\n \
        \   function isMagic($grid, $x, $y, $k) {\n        $sum = 0;\n        for ($i\
        \ = $x; $i < $x + $k; ++$i) $sum += $grid[$i][$y];\n        for ($i = $x; $i\
        \ < $x + $k; ++$i) {\n            $row_sum = 0;\n            $col_sum = 0;\n\
        \            for ($j = $y; $j < $y + $k; ++$j) {\n                $row_sum +=\
        \ $grid[$i][$j];\n                $col_sum += $grid[$i + $j - $x][$y + $j -\
        \ $x];\n            }\n            if ($row_sum != $sum || $col_sum != $sum)\
        \ return false;\n        }\n        $dia_sum1 = 0;\n        $dia_sum2 = 0;\n\
        \        for ($i = 0; $i < $k; ++$i) {\n            $dia_sum1 += $grid[$x +\
        \ $i][$y + $i];\n            $dia_sum2 += $grid[$x + $i][$y + $k - 1 - $i];\n\
        \        }\n        return $dia_sum1 == $sum && $dia_sum2 == $sum;\n    }\n}"
      swift: "class Solution {\n    func largestMagicSquare(_ grid: [[Int]]) -> Int\
        \ {\n        let m = grid.count\n        let n = grid[0].count\n        let\
        \ max_size = min(m, n)\n        for k in stride(from: max_size, to: 0, by: -1)\
        \ {\n            for i in 0...m-k {\n                for j in 0...n-k {\n  \
        \                  if isMagic(grid, i, j, k) {\n                        return\
        \ k\n                    }\n                }\n            }\n        }\n  \
        \      return 1\n    }\n\n    func isMagic(_ grid: [[Int]], _ x: Int, _ y: Int,\
        \ _ k: Int) -> Bool {\n        var sum = 0\n        for i in x..<x+k {\n   \
        \         sum += grid[i][y]\n        }\n        for i in x..<x+k {\n       \
        \     var row_sum = 0\n            var col_sum = 0\n            for j in y..<y+k\
        \ {\n                row_sum += grid[i][j]\n                col_sum += grid[i\
        \ + j - x][y + j - x]\n            }\n            if row_sum != sum || col_sum\
        \ != sum {\n                return false\n            }\n        }\n       \
        \ var dia_sum1 = 0\n        var dia_sum2 = 0\n        for i in 0..<k {\n   \
        \         dia_sum1 += grid[x + i][y + i]\n            dia_sum2 += grid[x + i][y\
        \ + k - 1 - i]\n        }\n        return dia_sum1 == sum && dia_sum2 == sum\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun largestMagicSquare(grid: Array<IntArray>):\
        \ Int {\n        val m = grid.size\n        val n = grid[0].size\n        var\
        \ maxSize = 1\n        for (size in n downTo 1) {\n            for (i in 0 until\
        \ m - size + 1) {\n                for (j in 0 until n - size + 1) {\n     \
        \               if (isMagicSquare(grid, i, j, size)) {\n                   \
        \     maxSize = maxOf(maxSize, size)\n                    }\n              \
        \  }\n            }\n        }\n        return maxSize\n    }\n\n    private\
        \ fun isMagicSquare(grid: Array<IntArray>, row: Int, col: Int, size: Int): Boolean\
        \ {\n        val expectedSum = grid[row][col] + grid[row][col + 1]\n       \
        \ for (i in row until row + size) {\n            var sum = 0\n            for\
        \ (j in col until col + size) {\n                sum += grid[i][j]\n       \
        \     }\n            if (sum != expectedSum) return false\n        }\n     \
        \   for (j in col until col + size) {\n            var sum = 0\n           \
        \ for (i in row until row + size) {\n                sum += grid[i][j]\n   \
        \         }\n            if (sum != expectedSum) return false\n        }\n \
        \       var sum = 0\n        for (i in 0 until size) {\n            sum += grid[row\
        \ + i][col + i]\n        }\n        if (sum != expectedSum) return false\n \
        \       sum = 0\n        for (i in 0 until size) {\n            sum += grid[row\
        \ + i][col + size - 1 - i]\n        }\n        return sum == expectedSum\n \
        \   }\n}"
      dart: "class Solution {\n  int largestMagicSquare(List<List<int>> grid) {\n  \
        \  int m = grid.length;\n    int n = grid[0].length;\n    int maxSize = 1;\n\
        \    for (int size = n; size >= 1; size--) {\n      for (int i = 0; i <= m -\
        \ size; i++) {\n        for (int j = 0; j <= n - size; j++) {\n          if\
        \ (isMagicSquare(grid, i, j, size)) {\n            maxSize = size;\n       \
        \   }\n        }\n      }\n    }\n    return maxSize;\n  }\n\n  bool isMagicSquare(List<List<int>>\
        \ grid, int row, int col, int size) {\n    int expectedSum = 0;\n    for (int\
        \ i = row; i < row + size; i++) {\n      expectedSum += grid[i][col];\n    }\n\
        \    for (int i = row; i < row + size; i++) {\n      int sum = 0;\n      for\
        \ (int j = col; j < col + size; j++) {\n        sum += grid[i][j];\n      }\n\
        \      if (sum != expectedSum) return false;\n    }\n    for (int j = col; j\
        \ < col + size; j++) {\n      int sum = 0;\n      for (int i = row; i < row\
        \ + size; i++) {\n        sum += grid[i][j];\n      }\n      if (sum != expectedSum)\
        \ return false;\n    }\n    int sum = 0;\n    for (int i = 0; i < size; i++)\
        \ {\n      sum += grid[row + i][col + i];\n    }\n    if (sum != expectedSum)\
        \ return false;\n    sum = 0;\n    for (int i = 0; i < size; i++) {\n      sum\
        \ += grid[row + i][col + size - 1 - i];\n    }\n    return sum == expectedSum;\n\
        \  }\n}"
      go: "func largestMagicSquare(grid [][]int) int {\n    m, n := len(grid), len(grid[0])\n\
        \    maxSize := 1\n    for size := n; size >= 1; size-- {\n        for i :=\
        \ 0; i <= m-size; i++ {\n            for j := 0; j <= n-size; j++ {\n      \
        \          if isMagicSquare(grid, i, j, size) {\n                    maxSize\
        \ = size\n                }\n            }\n        }\n    }\n    return maxSize\n\
        }\n\nfunc isMagicSquare(grid [][]int, row, col, size int) bool {\n    expectedSum\
        \ := 0\n    for i := row; i < row+size; i++ {\n        expectedSum += grid[i][col]\n\
        \    }\n    for i := row; i < row+size; i++ {\n        sum := 0\n        for\
        \ j := col; j < col+size; j++ {\n            sum += grid[i][j]\n        }\n\
        \        if sum != expectedSum {\n            return false\n        }\n    }\n\
        \    for j := col; j < col+size; j++ {\n        sum := 0\n        for i := row;\
        \ i < row+size; i++ {\n            sum += grid[i][j]\n        }\n        if\
        \ sum != expectedSum {\n            return false\n        }\n    }\n    sum\
        \ := 0\n    for i := 0; i < size; i++ {\n        sum += grid[row+i][col+i]\n\
        \    }\n    if sum != expectedSum {\n        return false\n    }\n    sum =\
        \ 0\n    for i := 0; i < size; i++ {\n        sum += grid[row+i][col+size-1-i]\n\
        \    }\n    return sum == expectedSum\n}"
      ruby: "def largest_magic_square(grid)\n  m, n = grid.size, grid[0].size\n  max_size\
        \ = 1\n  (n).downto(1) do |size|\n    (0...m - size + 1).each do |i|\n     \
        \ (0...n - size + 1).each do |j|\n        if is_magic_square(grid, i, j, size)\n\
        \          max_size = size\n        end\n      end\n    end\n  end\n  max_size\n\
        end\n\nprivate\n\ndef is_magic_square(grid, row, col, size)\n  expected_sum\
        \ = 0\n  (row...row + size).each do |i|\n    expected_sum += grid[i][col]\n\
        \  end\n  (row...row + size).each do |i|\n    sum = 0\n    (col...col + size).each\
        \ do |j|\n      sum += grid[i][j]\n    end\n    return false if sum != expected_sum\n\
        \  end\n  (col...col + size).each do |j|\n    sum = 0\n    (row...row + size).each\
        \ do |i|\n      sum += grid[i][j]\n    end\n    return false if sum != expected_sum\n\
        \  end\n  sum = 0\n  (0...size).each do |i|\n    sum += grid[row + i][col +\
        \ i]\n  end\n  return false if sum != expected_sum\n  sum = 0\n  (0...size).each\
        \ do |i|\n    sum += grid[row + i][col + size - 1 - i]\n  end\n  sum == expected_sum\n\
        end"
      scala: "object Solution {\n  def largestMagicSquare(grid: Array[Array[Int]]):\
        \ Int = {\n    val m = grid.length\n    val n = grid(0).length\n    var maxSize\
        \ = 1\n    for (size <- n to 1 by -1) {\n      for (i <- 0 until m - size +\
        \ 1) {\n        for (j <- 0 until n - size + 1) {\n          if (isMagicSquare(grid,\
        \ i, j, size)) {\n            maxSize = size\n          }\n        }\n     \
        \ }\n    }\n    maxSize\n  }\n\n  private def isMagicSquare(grid: Array[Array[Int]],\
        \ row: Int, col: Int, size: Int): Boolean = {\n    val expectedSum = (row until\
        \ row + size).map(i => grid(i)(col)).sum\n    (row until row + size).forall\
        \ { i =>\n      (col until col + size).map(j => grid(i)(j)).sum == expectedSum\n\
        \    } &&\n    (col until col + size).forall { j =>\n      (row until row +\
        \ size).map(i => grid(i)(j)).sum == expectedSum\n    } &&\n    (0 until size).map(i\
        \ => grid(row + i)(col + i)).sum == expectedSum &&\n    (0 until size).map(i\
        \ => grid(row + i)(col + size - 1 - i)).sum == expectedSum\n  }\n}"
      rust: "impl Solution {\n  pub fn largest_magic_square(grid: Vec<Vec<i32>>) ->\
        \ i32 {\n    let m = grid.len() as i32;\n    let n = grid[0].len() as i32;\n\
        \    let mut max_size = 1;\n    for size in (1..=n).rev() {\n      for i in\
        \ 0..=m - size {\n        for j in 0..=n - size {\n          if Solution::is_magic_square(&grid,\
        \ i as usize, j as usize, size as usize) {\n            max_size = size;\n \
        \         }\n        }\n      }\n    }\n    max_size\n  }\n\n  fn is_magic_square(grid:\
        \ &Vec<Vec<i32>>, row: usize, col: usize, size: usize) -> bool {\n    let mut\
        \ expected_sum = 0;\n    for i in row..row + size {\n      expected_sum += grid[i][col];\n\
        \    }\n    for i in row..row + size {\n      let mut sum = 0;\n      for j\
        \ in col..col + size {\n        sum += grid[i][j];\n      }\n      if sum !=\
        \ expected_sum {\n        return false;\n      }\n    }\n    for j in col..col\
        \ + size {\n      let mut sum = 0;\n      for i in row..row + size {\n     \
        \   sum += grid[i][j];\n      }\n      if sum != expected_sum {\n        return\
        \ false;\n      }\n    }\n    let mut sum = 0;\n    for i in 0..size {\n   \
        \   sum += grid[row + i][col + i];\n    }\n    if sum != expected_sum {\n  \
        \    return false;\n    }\n    sum = 0;\n    for i in 0..size {\n      sum +=\
        \ grid[row + i][col + size - 1 - i];\n    }\n    sum == expected_sum\n  }\n}"
      racket: "(define/contract (largest-magic-square grid)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer?)\n  (let* ([m (length grid)]\n         [n (length (car grid))]\n\
        \         [max-size 1])\n    (for ([size (in-range n 0 -1)])\n      (for ([i\
        \ (in-range m)])\n        (for ([j (in-range n)])\n          (when (and (>=\
        \ m (+ i size)) (>= n (+ j size)))\n            (when (is-magic-square grid\
        \ i j size)\n              (set! max-size size))))))\n    max-size))\n\n(define\
        \ (is-magic-square grid row col size)\n  (let* ([expected-sum (apply + (map\
        \ (lambda (i) (list-ref (list-ref grid i) col))\n                          \
        \              (range row (+ row size))))]\n         [rows (map (lambda (i)\
        \ (apply + (map (lambda (j) (list-ref (list-ref grid i) (+ j col)))\n      \
        \                                            (range 0 size))))\n           \
        \             (range row (+ row size)))])\n    (andmap (lambda (x) (= x expected-sum))\
        \ rows)\n    (let ([cols (map (lambda (j) (apply + (map (lambda (i) (list-ref\
        \ (list-ref grid (+ i row)) (+ j col)))\n                                  \
        \                (range 0 size))))\n                             (range 0 size))])\n\
        \      (and (andmap (lambda (x) (= x expected-sum)) cols)\n           (= expected-sum\
        \ (apply + (map (lambda (i) (list-ref (list-ref grid (+ i row)) (+ i col)))\n\
        \                                           (range 0 size))))\n           (=\
        \ expected-sum (apply + (map (lambda (i) (list-ref (list-ref grid (+ i row))\
        \ (+ (- size 1 i) col)))\n                                           (range\
        \ 0 size))))))))"
      erlang: "largest_magic_square(Grid) ->\n  MaxSize = 1,\n  M = length(Grid),\n\
        \  N = length(hd(Grid)),\n  lists:foreach(fun(Size) ->\n                   \
        \  lists:foreach(fun(I) ->\n                                   lists:foreach(fun(J)\
        \ ->\n                                                 case is_magic_square(Grid,\
        \ I, J, Size) of\n                                                   true ->\
        \ MaxSize = Size;\n                                                   false\
        \ -> ok\n                                                 end\n            \
        \                           end, lists:seq(0, M - Size)),\n                \
        \             lists:seq(0, N - Size))\n                 end, lists:seq(N, 1,\
        \ -1)),\n  MaxSize.\n\nis_magic_square(Grid, Row, Col, Size) ->\n  ExpectedSum\
        \ = lists:sum([lists:nth(Col + 1, lists:nth(Row + 1, Grid)) || _ <- lists:seq(0,\
        \ Size - 1)]),\n  lists:all(fun(I) -> lists:sum([lists:nth(J + 1, lists:nth(I\
        \ + Row + 1, Grid)) || J <- lists:seq(0, Size - 1)]) =:= ExpectedSum end,\n\
        \           lists:seq(0, Size - 1)) andalso\n  lists:all(fun(J) -> lists:sum([lists:nth(J\
        \ + 1, lists:nth(I + Row + 1, Grid)) || I <- lists:seq(0, Size - 1)]) =:= ExpectedSum\
        \ end,\n           lists:seq(0, Size - 1)) andalso\n  lists:sum([lists:nth(Col\
        \ + I + 1, lists:nth(Row + I + 1, Grid)) || I <- lists:seq(0, Size - 1)]) =:=\
        \ ExpectedSum andalso\n  lists:sum([lists:nth(Col + Size - 1 - I + 1, lists:nth(Row\
        \ + I + 1, Grid)) || I <- lists:seq(0, Size - 1)]) =:= ExpectedSum."
      elixir: "defmodule Solution do\n  @spec largest_magic_square(grid :: [[integer]])\
        \ :: integer\n  def largest_magic_square(grid) do\n    m = length(grid)\n  \
        \  n = length(Enum.at(grid, 0))\n    max_size = 1\n    Enum.reduce((n)..1, max_size,\
        \ fn size, max_size ->\n      Enum.reduce(0..(m - size), max_size, fn i, max_size\
        \ ->\n        Enum.reduce(0..(n - size), max_size, fn j, max_size ->\n     \
        \     if is_magic_square(grid, i, j, size) do\n            size\n          else\n\
        \            max_size\n          end\n        end)\n      end)\n    end)\n \
        \ end\n\n  defp is_magic_square(grid, row, col, size) do\n    expected_sum =\n\
        \      Enum.reduce(row..(row + size - 1), 0, fn i, sum ->\n        sum + Enum.at(Enum.at(grid,\
        \ i), col)\n      end)\n    rows =\n      Enum.map(row..(row + size - 1), fn\
        \ i ->\n        Enum.reduce(col..(col + size - 1), 0, fn j, sum ->\n       \
        \   sum + Enum.at(Enum.at(grid, i), j)\n        end)\n      end)\n    cols =\n\
        \      Enum.map(col..(col + size - 1), fn j ->\n        Enum.reduce(row..(row\
        \ + size - 1), 0, fn i, sum ->\n          sum + Enum.at(Enum.at(grid, i), j)\n\
        \        end)\n      end)\n    Enum.all?(rows, fn x -> x == expected_sum end)\
        \ and\n      Enum.all?(cols, fn x -> x == expected_sum end) and\n      Enum.reduce(0..(size\
        \ - 1), 0, fn i, sum ->\n        sum + Enum.at(Enum.at(grid, row + i), col +\
        \ i)\n      end) == expected_sum and\n      Enum.reduce(0..(size - 1), 0, fn\
        \ i, sum ->\n        sum + Enum.at(Enum.at(grid, row + i), col + size - 1 -\
        \ i)\n      end) == expected_sum\n  end\nend"
    approach: The algorithm works by checking all possible squares within the given
      grid. For each square, it calculates the sum of each row, column, and diagonal.
      If all sums are equal, then the square is a magic square. The algorithm keeps
      track of the largest magic square found so far and returns its size at the end.
      The key intuition is to use a brute force approach to check all possible squares,
      as the grid size is relatively small (up to 50x50). This approach ensures that
      all possible magic squares are considered, including those with non-distinct integers.
    time_complexity: The time complexity is O(m^3 * n^3) where m and n are the dimensions
      of the grid. This is because for each cell in the grid, we are potentially checking
      all possible squares that can be formed with that cell as the top-left corner.
      The sum of each row, column, and diagonal is calculated for each square, resulting
      in a cubic time complexity.
    space_complexity: The space complexity is O(1) as we are not using any additional
      space that scales with the input size. We are only using a constant amount of
      space to store the maximum size of the magic square found so far.
    elapsed_time: 16.674260139465332
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-18 01:18:49 '
---

## Problem #1895: Largest Magic Square

**Difficulty:** Medium

**Topics:** Array, Matrix, Prefix Sum

## Problem Description

<p>A <code>k x k</code> <strong>magic square</strong> is a <code>k x k</code> grid filled with integers such that every row sum, every column sum, and both diagonal sums are <strong>all equal</strong>. The integers in the magic square <strong>do not have to be distinct</strong>. Every <code>1 x 1</code> grid is trivially a <strong>magic square</strong>.</p>

<p>Given an <code>m x n</code> integer <code>grid</code>, return <em>the <strong>size</strong> (i.e., the side length </em><code>k</code><em>) of the <strong>largest magic square</strong> that can be found within this grid</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/29/magicsquare-grid.jpg" style="width: 413px; height: 335px;" />
<pre>
<strong>Input:</strong> grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The largest magic square has a size of 3.
Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
- Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
- Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
- Diagonal sums: 5+4+3 = 6+4+2 = 12
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/29/magicsquare2-grid.jpg" style="width: 333px; height: 255px;" />
<pre>
<strong>Input:</strong> grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>6</sup></code></li>
</ul>


## Hints

1. Check all squares in the matrix and find the largest one.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-18 01:18:28 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the size of the largest magic square within a given grid. A k x k magic square requires all its row sums, column sums, and both diagonal sums to be equal. Since every 1x1 grid is trivially a magic square, the answer is at least 1. The constraints (m, n <= 50) suggest that a polynomial time complexity involving m and n, up to around O(m*n*min(m,n)^2), would be acceptable.

The core idea is to iterate through all possible square sizes `k` from `min(m, n)` down to `1`. For each `k`, we iterate through all possible top-left corners `(r, c)` in the grid where a `k x k` square can start. The first `k` for which we find a valid magic square will be the largest. To efficiently check if a `k x k` square is magic, we precompute two prefix sum arrays: `row_prefix_sums[i][j]` stores the sum of elements in `grid[i]` from index `0` to `j-1`, and `col_prefix_sums[i][j]` stores the sum of elements in `grid[0][j]` to `grid[i-1][j]`. These prefix sums allow us to calculate any row or column sum within a square in O(1) time.

With the prefix sum arrays, checking a `k x k` square starting at `(r, c)` involves several steps. First, we calculate the sum of the first row of the candidate square using `row_prefix_sums` to establish a `target_sum`. Then, we verify that all other `k-1` row sums and all `k` column sums (using `row_prefix_sums` and `col_prefix_sums` respectively) are equal to this `target_sum`. Finally, we directly compute the sums of the main diagonal and anti-diagonal (each taking O(k) time) and compare them to the `target_sum`. If all these checks pass, we have found a magic square of size `k`, and since we are iterating `k` downwards, this `k` is the largest possible, so we return it immediately.

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
    int largestMagicSquare(std::vector<std::vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        std::vector<std::vector<long long>> R(m, std::vector<long long>(n + 1, 0));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                R[i][j+1] = R[i][j] + grid[i][j];
            }
        }

        std::vector<std::vector<long long>> C(m + 1, std::vector<long long>(n, 0));
        for (int j = 0; j < n; ++j) {
            for (int i = 0; i < m; ++i) {
                C[i+1][j] = C[i][j] + grid[i][j];
            }
        }

        for (int k = std::min(m, n); k >= 1; --k) {
            for (int r = 0; r <= m - k; ++r) {
                for (int c = 0; c <= n - k; ++c) {

                    long long target_sum = R[r][c+k] - R[r][c];

                    bool is_magic = true;

                    for (int i = 0; i < k; ++i) {
                        if ((R[r+i][c+k] - R[r+i][c]) != target_sum) {
                            is_magic = false;
                            break;
                        }
                    }
                    if (!is_magic) {
                        continue;
                    }

                    for (int j = 0; j < k; ++j) {
                        if ((C[r+k][c+j] - C[r][c+j]) != target_sum) {
                            is_magic = false;
                            break;
                        }
                    }
                    if (!is_magic) {
                        continue;
                    }

                    long long diag_sum = 0;
                    for (int i = 0; i < k; ++i) {
                        diag_sum += grid[r+i][c+i];
                    }
                    if (diag_sum != target_sum) {
                        is_magic = false;
                    }
                    if (!is_magic) {
                        continue;
                    }

                    long long anti_diag_sum = 0;
                    for (int i = 0; i < k; ++i) {
                        anti_diag_sum += grid[r+i][c+k-1-i];
                    }
                    if (anti_diag_sum != target_sum) {
                        is_magic = false;
                    }
                    if (!is_magic) {
                        continue;
                    }

                    return k;
                }
            }
        }

        return 1;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int largestMagicSquare(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        long[][] R = new long[m][n + 1];
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                R[i][j+1] = R[i][j] + grid[i][j];
            }
        }

        long[][] C = new long[m + 1][n];
        for (int j = 0; j < n; ++j) {
            for (int i = 0; i < m; ++i) {
                C[i+1][j] = C[i][j] + grid[i][j];
            }
        }

        for (int k = Math.min(m, n); k >= 1; --k) {
            for (int r = 0; r <= m - k; ++r) {
                for (int c = 0; c <= n - k; ++c) {

                    long target_sum = R[r][c+k] - R[r][c];

                    boolean is_magic = true;

                    for (int i = 0; i < k; ++i) {
                        if ((R[r+i][c+k] - R[r+i][c]) != target_sum) {
                            is_magic = false;
                            break;
                        }
                    }
                    if (!is_magic) {
                        continue;
                    }

                    for (int j = 0; j < k; ++j) {
                        if ((C[r+k][c+j] - C[r][c+j]) != target_sum) {
                            is_magic = false;
                            break;
                        }
                    }
                    if (!is_magic) {
                        continue;
                    }

                    long diag_sum = 0;
                    for (int i = 0; i < k; ++i) {
                        diag_sum += grid[r+i][c+i];
                    }
                    if (diag_sum != target_sum) {
                        is_magic = false;
                    }
                    if (!is_magic) {
                        continue;
                    }

                    long anti_diag_sum = 0;
                    for (int i = 0; i < k; ++i) {
                        anti_diag_sum += grid[r+i][c+k-1-i];
                    }
                    if (anti_diag_sum != target_sum) {
                        is_magic = false;
                    }
                    if (!is_magic) {
                        continue;
                    }

                    return k;
                }
            }
        }

        return 1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        R = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                R[i][j+1] = R[i][j] + grid[i][j]

        C = [[0] * n for _ in range(m + 1)]
        for j in range(n):
            for i in range(m):
                C[i+1][j] = C[i][j] + grid[i][j]

        for k in range(min(m, n), 0, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):

                    target_sum = R[r][c+k] - R[r][c]

                    is_magic = True

                    for i in range(k):
                        if (R[r+i][c+k] - R[r+i][c]) != target_sum:
                            is_magic = False
                            break
                    if not is_magic:
                        continue

                    for j in range(k):
                        if (C[r+k][c+j] - C[r][c+j]) != target_sum:
                            is_magic = False
                            break
                    if not is_magic:
                        continue

                    diag_sum = 0
                    for i in range(k):
                        diag_sum += grid[r+i][c+i]
                    if diag_sum != target_sum:
                        is_magic = False
                    if not is_magic:
                        continue

                    anti_diag_sum = 0
                    for i in range(k):
                        anti_diag_sum += grid[r+i][c+k-1-i]
                    if anti_diag_sum != target_sum:
                        is_magic = False
                    if not is_magic:
                        continue

                    return k

        return 1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        R = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                R[i][j+1] = R[i][j] + grid[i][j]

        C = [[0] * n for _ in range(m + 1)]
        for j in range(n):
            for i in range(m):
                C[i+1][j] = C[i][j] + grid[i][j]

        for k in range(min(m, n), 0, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):

                    target_sum = R[r][c+k] - R[r][c]

                    is_magic = True

                    for i in range(k):
                        if (R[r+i][c+k] - R[r+i][c]) != target_sum:
                            is_magic = False
                            break
                    if not is_magic:
                        continue

                    for j in range(k):
                        if (C[r+k][c+j] - C[r][c+j]) != target_sum:
                            is_magic = False
                            break
                    if not is_magic:
                        continue

                    diag_sum = 0
                    for i in range(k):
                        diag_sum += grid[r+i][c+i]
                    if diag_sum != target_sum:
                        is_magic = False
                    if not is_magic:
                        continue

                    anti_diag_sum = 0
                    for i in range(k):
                        anti_diag_sum += grid[r+i][c+k-1-i]
                    if anti_diag_sum != target_sum:
                        is_magic = False
                    if not is_magic:
                        continue

                    return k

        return 1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int largestMagicSquare(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];

    long long** R = (long long**)malloc(m * sizeof(long long*));
    for (int i = 0; i < m; ++i) {
        R[i] = (long long*)calloc(n + 1, sizeof(long long));
        for (int j = 0; j < n; ++j) {
            R[i][j+1] = R[i][j] + grid[i][j];
        }
    }

    long long** C = (long long**)malloc((m + 1) * sizeof(long long*));
    for (int i = 0; i < m + 1; ++i) {
        C[i] = (long long*)calloc(n, sizeof(long long));
    }
    for (int j = 0; j < n; ++j) {
        for (int i = 0; i < m; ++i) {
            C[i+1][j] = C[i][j] + grid[i][j];
        }
    }

    int min_mn = (m < n) ? m : n;
    for (int k = min_mn; k >= 1; --k) {
        for (int r = 0; r <= m - k; ++r) {
            for (int c = 0; c <= n - k; ++c) {

                long long target_sum = R[r][c+k] - R[r][c];

                int is_magic = 1;

                for (int i = 0; i < k; ++i) {
                    if ((R[r+i][c+k] - R[r+i][c]) != target_sum) {
                        is_magic = 0;
                        break;
                    }
                }
                if (!is_magic) {
                    continue;
                }

                for (int j = 0; j < k; ++j) {
                    if ((C[r+k][c+j] - C[r][c+j]) != target_sum) {
                        is_magic = 0;
                        break;
                    }
                }
                if (!is_magic) {
                    continue;
                }

                long long diag_sum = 0;
                for (int i = 0; i < k; ++i) {
                    diag_sum += grid[r+i][c+i];
                }
                if (diag_sum != target_sum) {
                    is_magic = 0;
                }
                if (!is_magic) {
                    continue;
                }

                long long anti_diag_sum = 0;
                for (int i = 0; i < k; ++i) {
                    anti_diag_sum += grid[r+i][c+k-1-i];
                }
                if (anti_diag_sum != target_sum) {
                    is_magic = 0;
                }
                if (!is_magic) {
                    continue;
                }

                for (int i = 0; i < m; ++i) {
                    free(R[i]);
                }
                free(R);
                for (int i = 0; i < m + 1; ++i) {
                    free(C[i]);
                }
                free(C);
                return k;
            }
        }
    }

    for (int i = 0; i < m; ++i) {
        free(R[i]);
    }
    free(R);
    for (int i = 0; i < m + 1; ++i) {
        free(C[i]);
    }
    free(C);
    return 1;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int LargestMagicSquare(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;

        long[][] R = new long[m][n + 1];
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                R[i][j+1] = R[i][j] + grid[i][j];
            }
        }

        long[][] C = new long[m + 1][n];
        for (int j = 0; j < n; ++j) {
            for (int i = 0; i < m; ++i) {
                C[i+1][j] = C[i][j] + grid[i][j];
            }
        }

        for (int k = Math.Min(m, n); k >= 1; --k) {
            for (int r = 0; r <= m - k; ++r) {
                for (int c = 0; c <= n - k; ++c) {

                    long target_sum = R[r][c+k] - R[r][c];

                    bool is_magic = true;

                    for (int i = 0; i < k; ++i) {
                        if ((R[r+i][c+k] - R[r+i][c]) != target_sum) {
                            is_magic = false;
                            break;
                        }
                    }
                    if (!is_magic) {
                        continue;
                    }

                    for (int j = 0; j < k; ++j) {
                        if ((C[r+k][c+j] - C[r][c+j]) != target_sum) {
                            is_magic = false;
                            break;
                        }
                    }
                    if (!is_magic) {
                        continue;
                    }

                    long diag_sum = 0;
                    for (int i = 0; i < k; ++i) {
                        diag_sum += grid[r+i][c+i];
                    }
                    if (diag_sum != target_sum) {
                        is_magic = false;
                    }
                    if (!is_magic) {
                        continue;
                    }

                    long anti_diag_sum = 0;
                    for (int i = 0; i < k; ++i) {
                        anti_diag_sum += grid[r+i][c+k-1-i];
                    }
                    if (anti_diag_sum != target_sum) {
                        is_magic = false;
                    }
                    if (!is_magic) {
                        continue;
                    }

                    return k;
                }
            }
        }

        return 1;
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
var largestMagicSquare = function(grid) {
    let m = grid.length;
    let n = grid[0].length;

    let R = Array(m).fill(0).map(() => Array(n + 1).fill(0));
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            R[i][j+1] = R[i][j] + grid[i][j];
        }
    }

    let C = Array(m + 1).fill(0).map(() => Array(n).fill(0));
    for (let j = 0; j < n; ++j) {
        for (let i = 0; i < m; ++i) {
            C[i+1][j] = C[i][j] + grid[i][j];
        }
    }

    for (let k = Math.min(m, n); k >= 1; --k) {
        for (let r = 0; r <= m - k; ++r) {
            for (let c = 0; c <= n - k; ++c) {

                let target_sum = R[r][c+k] - R[r][c];

                let is_magic = true;

                for (let i = 0; i < k; ++i) {
                    if ((R[r+i][c+k] - R[r+i][c]) !== target_sum) {
                        is_magic = false;
                        break;
                    }
                }
                if (!is_magic) {
                    continue;
                }

                for (let j = 0; j < k; ++j) {
                    if ((C[r+k][c+j] - C[r][c+j]) !== target_sum) {
                        is_magic = false;
                        break;
                    }
                }
                if (!is_magic) {
                    continue;
                }

                let diag_sum = 0;
                for (let i = 0; i < k; ++i) {
                    diag_sum += grid[r+i][c+i];
                }
                if (diag_sum !== target_sum) {
                    is_magic = false;
                }
                if (!is_magic) {
                    continue;
                }

                let anti_diag_sum = 0;
                for (let i = 0; i < k; ++i) {
                    anti_diag_sum += grid[r+i][c+k-1-i];
                }
                if (anti_diag_sum !== target_sum) {
                    is_magic = false;
                }
                if (!is_magic) {
                    continue;
                }

                return k;
            }
        }
    }

    return 1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function largestMagicSquare(grid: number[][]): number {
    let m = grid.length;
    let n = grid[0].length;

    let R: number[][] = Array(m).fill(0).map(() => Array(n + 1).fill(0));
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            R[i][j+1] = R[i][j] + grid[i][j];
        }
    }

    let C: number[][] = Array(m + 1).fill(0).map(() => Array(n).fill(0));
    for (let j = 0; j < n; ++j) {
        for (let i = 0; i < m; ++i) {
            C[i+1][j] = C[i][j] + grid[i][j];
        }
    }

    for (let k = Math.min(m, n); k >= 1; --k) {
        for (let r = 0; r <= m - k; ++r) {
            for (let c = 0; c <= n - k; ++c) {

                let target_sum = R[r][c+k] - R[r][c];

                let is_magic = true;

                for (let i = 0; i < k; ++i) {
                    if ((R[r+i][c+k] - R[r+i][c]) !== target_sum) {
                        is_magic = false;
                        break;
                    }
                }
                if (!is_magic) {
                    continue;
                }

                for (let j = 0; j < k; ++j) {
                    if ((C[r+k][c+j] - C[r][c+j]) !== target_sum) {
                        is_magic = false;
                        break;
                    }
                }
                if (!is_magic) {
                    continue;
                }

                let diag_sum = 0;
                for (let i = 0; i < k; ++i) {
                    diag_sum += grid[r+i][c+i];
                }
                if (diag_sum !== target_sum) {
                    is_magic = false;
                }
                if (!is_magic) {
                    continue;
                }

                let anti_diag_sum = 0;
                for (let i = 0; i < k; ++i) {
                    anti_diag_sum += grid[r+i][c+k-1-i];
                }
                if (anti_diag_sum !== target_sum) {
                    is_magic = false;
                }
                if (!is_magic) {
                    continue;
                }

                return k;
            }
        }
    }

    return 1;
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
    function largestMagicSquare($grid) {
        $m = count($grid);
        $n = count($grid[0]);

        $R = array_fill(0, $m, array_fill(0, $n + 1, 0));
        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                $R[$i][$j+1] = $R[$i][$j] + $grid[$i][$j];
            }
        }

        $C = array_fill(0, $m + 1, array_fill(0, $n, 0));
        for ($j = 0; $j < $n; ++$j) {
            for ($i = 0; $i < $m; ++$i) {
                $C[$i+1][$j] = $C[$i][$j] + $grid[$i][$j];
            }
        }

        $min_mn = min($m, $n);
        for ($k = $min_mn; $k >= 1; --$k) {
            for ($r = 0; $r <= $m - $k; ++$r) {
                for ($c = 0; $c <= $n - $k; ++$c) {

                    $target_sum = $R[$r][$c+$k] - $R[$r][$c];

                    $is_magic = true;

                    for ($i = 0; $i < $k; ++$i) {
                        if (($R[$r+$i][$c+$k] - $R[$r+$i][$c]) != $target_sum) {
                            $is_magic = false;
                            break;
                        }
                    }
                    if (!$is_magic) {
                        continue;
                    }

                    for ($j = 0; $j < $k; ++$j) {
                        if (($C[$r+$k][$c+$j] - $C[$r][$c+$j]) != $target_sum) {
                            $is_magic = false;
                            break;
                        }
                    }
                    if (!$is_magic) {
                        continue;
                    }

                    $diag_sum = 0;
                    for ($i = 0; $i < $k; ++$i) {
                        $diag_sum += $grid[$r+$i][$c+$i];
                    }
                    if ($diag_sum != $target_sum) {
                        $is_magic = false;
                    }
                    if (!$is_magic) {
                        continue;
                    }

                    $anti_diag_sum = 0;
                    for ($i = 0; $i < $k; ++$i) {
                        $anti_diag_sum += $grid[$r+$i][$c+$k-1-$i];
                    }
                    if ($anti_diag_sum != $target_sum) {
                        $is_magic = false;
                    }
                    if (!$is_magic) {
                        continue;
                    }

                    return $k;
                }
            }
        }

        return 1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func largestMagicSquare(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count

        var R = Array(repeating: Array(repeating: 0, count: n + 1), count: m)
        for i in 0..<m {
            for j in 0..<n {
                R[i][j+1] = R[i][j] + grid[i][j]
            }
        }

        var C = Array(repeating: Array(repeating: 0, count: n), count: m + 1)
        for j in 0..<n {
            for i in 0..<m {
                C[i+1][j] = C[i][j] + grid[i][j]
            }
        }

        let minMN = min(m, n)
        for k in (1...minMN).reversed() {
            for r in 0...(m - k) {
                for c in 0...(n - k) {

                    let target_sum = R[r][c+k] - R[r][c]

                    var is_magic = true

                    for i in 0..<k {
                        if (R[r+i][c+k] - R[r+i][c]) != target_sum {
                            is_magic = false
                            break
                        }
                    }
                    if !is_magic {
                        continue
                    }

                    for i in 0..<k {
                        if (C[r+k][c+i] - C[r][c+i]) != target_sum {
                            is_magic = false
                            break
                        }
                    }
                    if !is_magic {
                        continue
                    }

                    var diag_sum = 0
                    for i in 0..<k {
                        diag_sum += grid[r+i][c+i]
                    }
                    if diag_sum != target_sum {
                        is_magic = false
                    }
                    if !is_magic {
                        continue
                    }

                    var anti_diag_sum = 0
                    for i in 0..<k {
                        anti_diag_sum += grid[r+i][c+k-1-i]
                    }
                    if anti_diag_sum != target_sum {
                        is_magic = false
                    }
                    if !is_magic {
                        continue
                    }

                    return k
                }
            }
        }

        return 1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun largestMagicSquare(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size

        val rowPrefixSums = Array(m) { LongArray(n + 1) }
        for (i in 0 until m) {
            for (j in 0 until n) {
                rowPrefixSums[i][j + 1] = rowPrefixSums[i][j] + grid[i][j]
            }
        }

        val colPrefixSums = Array(m + 1) { LongArray(n) }
        for (j in 0 until n) {
            for (i in 0 until m) {
                colPrefixSums[i + 1][j] = colPrefixSums[i][j] + grid[i][j]
            }
        }

        for (k in Math.min(m, n) downTo 1) {
            for (r in 0..m - k) {
                for (c in 0..n - k) {
                    if (isMagicSquare(r, c, k, grid, rowPrefixSums, colPrefixSums)) {
                        return k
                    }
                }
            }
        }
        return 1 // Every 1x1 grid is a magic square
    }

    private fun isMagicSquare(
        r: Int, c: Int, k: Int,
        grid: Array<IntArray>,
        rowPrefixSums: Array<LongArray>,
        colPrefixSums: Array<LongArray>
    ): Boolean {
        val targetSum = rowPrefixSums[r][c + k] - rowPrefixSums[r][c]

        // Check row sums
        for (i in r until r + k) {
            if (rowPrefixSums[i][c + k] - rowPrefixSums[i][c] != targetSum) {
                return false
            }
        }

        // Check column sums
        for (j in c until c + k) {
            if (colPrefixSums[r + k][j] - colPrefixSums[r][j] != targetSum) {
                return false
            }
        }

        // Check main diagonal sum
        var diag1Sum: Long = 0
        for (x in 0 until k) {
            diag1Sum += grid[r + x][c + x]
        }
        if (diag1Sum != targetSum) {
            return false
        }

        // Check anti-diagonal sum
        var diag2Sum: Long = 0
        for (x in 0 until k) {
            diag2Sum += grid[r + x][c + k - 1 - x]
        }
        if (diag2Sum != targetSum) {
            return false
        }

        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int largestMagicSquare(List<List<int>> grid) {
    final int m = grid.length;
    final int n = grid[0].length;

    final List<List<int>> rowPrefixSums = List.generate(m, (_) => List.filled(n + 1, 0));
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        rowPrefixSums[i][j + 1] = rowPrefixSums[i][j] + grid[i][j];
      }
    }

    final List<List<int>> colPrefixSums = List.generate(m + 1, (_) => List.filled(n, 0));
    for (int j = 0; j < n; j++) {
      for (int i = 0; i < m; i++) {
        colPrefixSums[i + 1][j] = colPrefixSums[i][j] + grid[i][j];
      }
    }

    for (int k = (m < n ? m : n); k >= 1; k--) {
      for (int r = 0; r <= m - k; r++) {
        for (int c = 0; c <= n - k; c++) {
          if (isMagicSquare(r, c, k, grid, rowPrefixSums, colPrefixSums)) {
            return k;
          }
        }
      }
    }
    return 1; // Every 1x1 grid is a magic square
  }

  bool isMagicSquare(
    int r, int c, int k,
    List<List<int>> grid,
    List<List<int>> rowPrefixSums,
    List<List<int>> colPrefixSums
  ) {
    final int targetSum = rowPrefixSums[r][c + k] - rowPrefixSums[r][c];

    // Check row sums
    for (int i = r; i < r + k; i++) {
      if (rowPrefixSums[i][c + k] - rowPrefixSums[i][c] != targetSum) {
        return false;
      }
    }

    // Check column sums
    for (int j = c; j < c + k; j++) {
      if (colPrefixSums[r + k][j] - colPrefixSums[r][j] != targetSum) {
        return false;
      }
    }

    // Check main diagonal sum
    int diag1Sum = 0;
    for (int x = 0; x < k; x++) {
      diag1Sum += grid[r + x][c + x];
    }
    if (diag1Sum != targetSum) {
      return false;
    }

    // Check anti-diagonal sum
    int diag2Sum = 0;
    for (int x = 0; x < k; x++) {
      diag2Sum += grid[r + x][c + k - 1 - x];
    }
    if (diag2Sum != targetSum) {
      return false;
    }

    return true;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func largestMagicSquare(grid [][]int) int {
    m := len(grid)
    n := len(grid[0])

    rowPrefixSums := make([][]int, m)
    for i := 0; i < m; i++ {
        rowPrefixSums[i] = make([]int, n+1)
        for j := 0; j < n; j++ {
            rowPrefixSums[i][j+1] = rowPrefixSums[i][j] + grid[i][j]
        }
    }

    colPrefixSums := make([][]int, m+1)
    for i := 0; i <= m; i++ {
        colPrefixSums[i] = make([]int, n)
    }
    for j := 0; j < n; j++ {
        for i := 0; i < m; i++ {
            colPrefixSums[i+1][j] = colPrefixSums[i][j] + grid[i][j]
        }
    }

    minDim := m
    if n < minDim {
        minDim = n
    }

    for k := minDim; k >= 1; k-- {
        for r := 0; r <= m-k; r++ {
            for c := 0; c <= n-k; c++ {
                if isMagicSquare(r, c, k, grid, rowPrefixSums, colPrefixSums) {
                    return k
                }
            }
        }
    }
    return 1 // Every 1x1 grid is a magic square
}

func isMagicSquare(
    r, c, k int,
    grid [][]int,
    rowPrefixSums [][]int,
    colPrefixSums [][]int
) bool {
    targetSum := rowPrefixSums[r][c+k] - rowPrefixSums[r][c]

    // Check row sums
    for i := r; i < r+k; i++ {
        if rowPrefixSums[i][c+k]-rowPrefixSums[i][c] != targetSum {
            return false
        }
    }

    // Check column sums
    for j := c; j < c+k; j++ {
        if colPrefixSums[r+k][j]-colPrefixSums[r][j] != targetSum {
            return false
        }
    }

    // Check main diagonal sum
    diag1Sum := 0
    for x := 0; x < k; x++ {
        diag1Sum += grid[r+x][c+x]
    }
    if diag1Sum != targetSum {
        return false
    }

    // Check anti-diagonal sum
    diag2Sum := 0
    for x := 0; x < k; x++ {
        diag2Sum += grid[r+x][c+k-1-x]
    }
    if diag2Sum != targetSum {
        return false
    }

    return true
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[][]} grid
# @return {Integer}
def largest_magic_square(grid)
    m = grid.length
    n = grid[0].length

    row_prefix_sums = Array.new(m) { Array.new(n + 1, 0) }
    (0...m).each do |i|
        (0...n).each do |j|
            row_prefix_sums[i][j + 1] = row_prefix_sums[i][j] + grid[i][j]
        end
    end

    col_prefix_sums = Array.new(m + 1) { Array.new(n, 0) }
    (0...n).each do |j|
        (0...m).each do |i|
            col_prefix_sums[i + 1][j] = col_prefix_sums[i][j] + grid[i][j]
        end
    end

    min_dim = [m, n].min

    min_dim.downto(1) do |k|
        (0..m - k).each do |r|
            (0..n - k).each do |c|
                if is_magic_square(r, c, k, grid, row_prefix_sums, col_prefix_sums)
                    return k
                end
            end
        end
    end
    1 # Every 1x1 grid is a magic square
end

def is_magic_square(r, c, k, grid, row_prefix_sums, col_prefix_sums)
    target_sum = row_prefix_sums[r][c + k] - row_prefix_sums[r][c]

    # Check row sums
    (r...r + k).each do |i|
        if row_prefix_sums[i][c + k] - row_prefix_sums[i][c] != target_sum
            return false
        end
    end

    # Check column sums
    (c...c + k).each do |j|
        if col_prefix_sums[r + k][j] - col_prefix_sums[r][j] != target_sum
            return false
        end
    end

    # Check main diagonal sum
    diag1_sum = 0
    (0...k).each do |x|
        diag1_sum += grid[r + x][c + x]
    end
    if diag1_sum != target_sum
        return false
    end

    # Check anti-diagonal sum
    diag2_sum = 0
    (0...k).each do |x|
        diag2_sum += grid[r + x][c + k - 1 - x]
    end
    if diag2_sum != target_sum
        return false
    end

    true
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def largestMagicSquare(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        val n = grid(0).length

        val rowPrefixSums = Array.ofDim[Long](m, n + 1)
        for (i <- 0 until m) {
            for (j <- 0 until n) {
                rowPrefixSums(i)(j + 1) = rowPrefixSums(i)(j) + grid(i)(j)
            }
        }

        val colPrefixSums = Array.ofDim[Long](m + 1, n)
        for (j <- 0 until n) {
            for (i <- 0 until m) {
                colPrefixSums(i + 1)(j) = colPrefixSums(i)(j) + grid(i)(j)
            }
        }

        val minDim = Math.min(m, n)

        for (k <- minDim to 1 by -1) {
            for (r <- 0 to m - k) {
                for (c <- 0 to n - k) {
                    if (isMagicSquare(r, c, k, grid, rowPrefixSums, colPrefixSums)) {
                        return k
                    }
                }
            }
        }
        1 // Every 1x1 grid is a magic square
    }

    private def isMagicSquare(
        r: Int, c: Int, k: Int,
        grid: Array[Array[Int]],
        rowPrefixSums: Array[Array[Long]],
        colPrefixSums: Array[Array[Long]]
    ): Boolean = {
        val targetSum = rowPrefixSums(r)(c + k) - rowPrefixSums(r)(c)

        // Check row sums
        for (i <- r until r + k) {
            if (rowPrefixSums(i)(c + k) - rowPrefixSums(i)(c) != targetSum) {
                return false
            }
        }

        // Check column sums
        for (j <- c until c + k) {
            if (colPrefixSums(r + k)(j) - colPrefixSums(r)(j) != targetSum) {
                return false
            }
        }

        // Check main diagonal sum
        var diag1Sum: Long = 0
        for (x <- 0 until k) {
            diag1Sum += grid(r + x)(c + x)
        }
        if (diag1Sum != targetSum) {
            return false
        }

        // Check anti-diagonal sum
        var diag2Sum: Long = 0
        for (x <- 0 until k) {
            diag2Sum += grid(r + x)(c + k - 1 - x)
        }
        if (diag2Sum != targetSum) {
            return false
        }

        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn largest_magic_square(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();

        let mut row_prefix_sums = vec![vec![0; n + 1]; m];
        for i in 0..m {
            for j in 0..n {
                row_prefix_sums[i][j + 1] = row_prefix_sums[i][j] + grid[i][j];
            }
        }

        let mut col_prefix_sums = vec![vec![0; n]; m + 1];
        for j in 0..n {
            for i in 0..m {
                col_prefix_sums[i + 1][j] = col_prefix_sums[i][j] + grid[i][j];
            }
        }

        let min_dim = m.min(n);

        for k in (1..=min_dim).rev() {
            for r in 0..=(m - k) {
                for c in 0..=(n - k) {
                    if Self::is_magic_square(r, c, k, &grid, &row_prefix_sums, &col_prefix_sums) {
                        return k as i32;
                    }
                }
            }
        }
        1 // Every 1x1 grid is a magic square
    }

    fn is_magic_square(
        r: usize, c: usize, k: usize,
        grid: &Vec<Vec<i32>>,
        row_prefix_sums: &Vec<Vec<i32>>,
        col_prefix_sums: &Vec<Vec<i32>>
    ) -> bool {
        let target_sum = row_prefix_sums[r][c + k] - row_prefix_sums[r][c];

        // Check row sums
        for i in r..(r + k) {
            if row_prefix_sums[i][c + k] - row_prefix_sums[i][c] != target_sum {
                return false;
            }
        }

        // Check column sums
        for j in c..(c + k) {
            if col_prefix_sums[r + k][j] - col_prefix_sums[r][j] != target_sum {
                return false;
            }
        }

        // Check main diagonal sum
        let mut diag1_sum = 0;
        for x in 0..k {
            diag1_sum += grid[r + x][c + x];
        }
        if diag1_sum != target_sum {
            return false;
        }

        // Check anti-diagonal sum
        let mut diag2_sum = 0;
        for x in 0..k {
            diag2_sum += grid[r + x][c + k - 1 - x];
        }
        if diag2_sum != target_sum {
            return false;
        }

        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (largest-magic-square grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (define m (length grid))
  (define n (length (car grid)))

  ;; Precompute row prefix sums
  (define row-prefix-sums (make-vector m))
  (for ([i (in-range m)])
    (define current-row (list-ref grid i))
    (define row-sums-vec (make-vector (+ n 1) 0))
    (for ([j (in-range n)])
      (vector-set! row-sums-vec (+ j 1) (+ (vector-ref row-sums-vec j) (list-ref current-row j))))
    (vector-set! row-prefix-sums i row-sums-vec))

  ;; Precompute column prefix sums
  (define col-prefix-sums (make-vector (+ m 1)))
  (for ([i (in-range (+ m 1))])
    (vector-set! col-prefix-sums i (make-vector n 0)))
  (for ([j (in-range n)])
    (for ([i (in-range m)])
      (vector-set! (vector-ref col-prefix-sums (+ i 1)) j
                   (+ (vector-ref (vector-ref col-prefix-sums i) j)
                      (list-ref (list-ref grid i) j)))))

  (define (is-magic-square? r c k)
    (define target-sum (- (vector-ref (vector-ref row-prefix-sums r) (+ c k))
                          (vector-ref (vector-ref row-prefix-sums r) c)))

    ;; Check row sums
    (for ([i (in-range r (+ r k))])
      (when (!= (- (vector-ref (vector-ref row-prefix-sums i) (+ c k))
                   (vector-ref (vector-ref row-prefix-sums i) c))
               target-sum)
        (return-from is-magic-square? #f)))

    ;; Check column sums
    (for ([j (in-range c (+ c k))])
      (when (!= (- (vector-ref (vector-ref col-prefix-sums (+ r k)) j)
                   (vector-ref (vector-ref col-prefix-sums r) j))
               target-sum)
        (return-from is-magic-square? #f)))

    ;; Check main diagonal sum
    (define diag1-sum 0)
    (for ([x (in-range k)])
      (set! diag1-sum (+ diag1-sum (list-ref (list-ref grid (+ r x)) (+ c x)))))
    (when (!= diag1-sum target-sum)
      (return-from is-magic-square? #f))

    ;; Check anti-diagonal sum
    (define diag2-sum 0)
    (for ([x (in-range k)])
      (set! diag2-sum (+ diag2-sum (list-ref (list-ref grid (+ r x)) (- (+ c k 1) x 1)))))
    (when (!= diag2-sum target-sum)
      (return-from is-magic-square? #f))

    #t)

  (define min-dim (min m n))

  (for ([k (in-range min-dim 0 -1)])
    (for ([r (in-range (+ (- m k) 1))])
      (for ([c (in-range (+ (- n k) 1))])
        (when (is-magic-square? r c k)
          (return-from largest-magic-square k)))))
  1)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec largest_magic_square(Grid :: [[integer()]]) -> integer().
largest_magic_square(Grid) ->
  M = length(Grid),
  N = length(hd(Grid)),

  % Precompute row prefix sums
  RowPrefixSums = lists:map(fun(Row) ->
    lists:foldl(fun(Val, Acc) -> Acc ++ [hd(Acc) + Val] end, [0], Row)
  end, Grid),

  % Precompute column prefix sums
  ColPrefixSumsList = lists:foldl(fun(Row, Acc) ->
    [lists:zipwith(fun(ColSum, Val) -> ColSum + Val end, hd(Acc), Row) | Acc]
  end, [[lists:duplicate(N, 0)]], Grid),
  ColPrefixSumsReversed = lists:reverse(ColPrefixSumsList),

  % Helper function to get element from list of lists (0-indexed)
  GetElem = fun(List, R, C) ->
    lists:nth(C + 1, lists:nth(R + 1, List))
  end,

  % Helper function to get row prefix sum
  GetRowPrefixSum = fun(R, C_end, C_start) ->
    lists:nth(C_end + 1, lists:nth(R + 1, RowPrefixSums)) - lists:nth(C_start + 1, lists:nth(R + 1, RowPrefixSums))
  end,

  % Helper function to get column prefix sum
  GetColPrefixSum = fun(R_end, R_start, C) ->
    lists:nth(C + 1, lists:nth(R_end + 1, ColPrefixSumsReversed)) - lists:nth(C + 1, lists:nth(R_start + 1, ColPrefixSumsReversed))
  end,

  IsMagicSquare = fun(R, C, K) ->
    TargetSum = GetRowPrefixSum(R, C + K, C),

    % Check row sums
    RowSumsOk = lists:all(fun(I) ->
      GetRowPrefixSum(I, C + K, C) == TargetSum
    end, lists:seq(R, R + K - 1)),

    % Check column sums
    ColSumsOk = lists:all(fun(J) ->
      GetColPrefixSum(R + K, R, J) == TargetSum
    end, lists:seq(C, C + K - 1)),

    % Check main diagonal sum
    Diag1Sum = lists:foldl(fun(X, Acc) ->
      Acc + GetElem(Grid, R + X, C + X)
    end, 0, lists:seq(0, K - 1)),
    Diag1Ok = Diag1Sum == TargetSum,

    % Check anti-diagonal sum
    Diag2Sum = lists:foldl(fun(X, Acc) ->
      Acc + GetElem(Grid, R + X, C + K - 1 - X)
    end, 0, lists:seq(0, K - 1)),
    Diag2Ok = Diag2Sum == TargetSum,

    RowSumsOk andalso ColSumsOk andalso Diag1Ok andalso Diag2Ok
  end,

  MinDim = min(M, N),

  lists:foldl(fun(K, Acc) ->
    case lists:foldl(fun(R, InnerAcc) ->
      case lists:foldl(fun(C, InnermostAcc) ->
        if InnermostAcc /= 0 -> InnermostAcc; % Already found a magic square
           IsMagicSquare(R, C, K) -> K;
           true -> 0
        end
      end, 0, lists:seq(0, N - K)) of
      0 -> InnerAcc;
      FoundK -> FoundK
    end
    end, 0, lists:seq(0, M - K)) of
    0 -> Acc;
    FoundK -> FoundK
  end
  end, 1, lists:seq(MinDim, 1, -1)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec largest_magic_square(grid :: [[integer]]) :: integer
  def largest_magic_square(grid) do
    m = Enum.count(grid)
    n = Enum.count(hd(grid))

    # Precompute row prefix sums
    row_prefix_sums = Enum.map(grid, fn row ->
      Enum.reduce(row, [0], fn val, acc -> acc ++ [List.last(acc) + val] end)
    end)

    # Precompute column prefix sums
    # col_prefix_sums[i][j] stores sum of grid[0][j] to grid[i-1][j]
    col_prefix_sums = 
      Enum.reduce(0..(m-1), [[List.duplicate(0, n)]], fn i, acc ->
        prev_row_sums = List.first(acc)
        current_row = Enum.at(grid, i)
        new_row_sums = 
          Enum.zip(prev_row_sums, current_row)
          |> Enum.map(fn {col_sum, val} -> col_sum + val end)
        [new_row_sums | acc]
      end)
      |> Enum.reverse()

    # Helper function to get element from list of lists (0-indexed)
    get_elem = fn list, r, c ->
      list |> Enum.at(r) |> Enum.at(c)
    end

    # Helper function to get row prefix sum
    get_row_prefix_sum = fn r, c_end, c_start ->
      Enum.at(row_prefix_sums, r) |> Enum.at(c_end + 1) - (Enum.at(row_prefix_sums, r) |> Enum.at(c_start + 1))
    end

    # Helper function to get column prefix sum
    get_col_prefix_sum = fn r_end, r_start, c ->
      Enum.at(col_prefix_sums, r_end + 1) |> Enum.at(c) - (Enum.at(col_prefix_sums, r_start + 1) |> Enum.at(c))
    end

    is_magic_square = fn r, c, k ->
      target_sum = get_row_prefix_sum.(r, c + k, c)

      # Check row sums
      row_sums_ok = Enum.all?(r..(r + k - 1), fn i ->
        get_row_prefix_sum.(i, c + k, c) == target_sum
      end)

      # Check column sums
      col_sums_ok = Enum.all?(c..(c + k - 1), fn j ->
        get_col_prefix_sum.(r + k, r, j) == target_sum
      end)

      # Check main diagonal sum
      diag1_sum = Enum.reduce(0..(k - 1), 0, fn x, acc ->
        acc + get_elem.(grid, r + x, c + x)
      end)
      diag1_ok = diag1_sum == target_sum

      # Check anti-diagonal sum
      diag2_sum = Enum.reduce(0..(k - 1), 0, fn x, acc ->
        acc + get_elem.(grid, r + x, c + k - 1 - x)
      end)
      diag2_ok = diag2_sum == target_sum

      row_sums_ok && col_sums_ok && diag1_ok && diag2_ok
    end

    min_dim = min(m, n)

    Enum.reduce(min_dim..1, 1, fn k, acc ->
      if acc != 1, do: acc, # Already found a larger magic square
      else: (
        found_k = 
          Enum.reduce_while(0..(m - k), 0, fn r, _ ->
            found_k_in_row = 
              Enum.reduce_while(0..(n - k), 0, fn c, _ ->
                if is_magic_square.(r, c, k) do
                  {:halt, k}
                else
                  {:cont, 0}
                end
              end)
            if found_k_in_row != 0 do
              {:halt, found_k_in_row}
            else
              {:cont, 0}
            end
          end)
        if found_k != 0, do: found_k, else: acc
      )
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is dominated by the nested loops for `k`, `r`, and `c`, and the `check` function. Precomputing prefix sums takes O(m*n) time. The outer loop for `k` runs `min(m, n)` times. The loops for `r` and `c` run `(m-k+1)` and `(n-k+1)` times respectively. Inside these loops, the `check` function takes O(k) time (O(1) for each row/column sum using prefix sums, and O(k) for each diagonal sum). Thus, the total time complexity is approximately O(sum_{k=1}^{min(m,n)} (m-k+1)(n-k+1) * k), which simplifies to O(m*n*min(m,n)^2). Given m, n <= 50, this is roughly 50 * 50 * 50^2 = 6.25 * 10^6 operations, which is efficient enough.

- **Space Complexity:** The space complexity is determined by the two prefix sum arrays, `row_prefix_sums` and `col_prefix_sums`. `row_prefix_sums` has dimensions `m x (n+1)` and `col_prefix_sums` has dimensions `(m+1) x n`. Therefore, the total space complexity is O(m*n). For m, n <= 50, this is 50 * 50 = 2500 integers, which is a very small memory footprint.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-18 01:18:49 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The algorithm works by checking all possible squares within the given grid. For each square, it calculates the sum of each row, column, and diagonal. If all sums are equal, then the square is a magic square. The algorithm keeps track of the largest magic square found so far and returns its size at the end. The key intuition is to use a brute force approach to check all possible squares, as the grid size is relatively small (up to 50x50). This approach ensures that all possible magic squares are considered, including those with non-distinct integers.

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
    int largestMagicSquare(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size(), max_size = min(m, n);
        for (int k = max_size; k > 0; --k) {
            for (int i = 0; i <= m - k; ++i) {
                for (int j = 0; j <= n - k; ++j) {
                    if (isMagic(grid, i, j, k)) return k;
                }
            }
        }
        return 1;
    }

    bool isMagic(vector<vector<int>>& grid, int x, int y, int k) {
        int sum = 0;
        for (int i = x; i < x + k; ++i) sum += grid[i][y];
        for (int i = x; i < x + k; ++i) {
            int row_sum = 0, col_sum = 0;
            for (int j = y; j < y + k; ++j) {
                row_sum += grid[i][j];
                col_sum += grid[i + j - x][y + j - x];
            }
            if (row_sum != sum || col_sum != sum) return false;
        }
        int dia_sum1 = 0, dia_sum2 = 0;
        for (int i = 0; i < k; ++i) {
            dia_sum1 += grid[x + i][y + i];
            dia_sum2 += grid[x + i][y + k - 1 - i];
        }
        return dia_sum1 == sum && dia_sum2 == sum;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int largestMagicSquare(int[][] grid) {
        int m = grid.length, n = grid[0].length, max_size = Math.min(m, n);
        for (int k = max_size; k > 0; --k) {
            for (int i = 0; i <= m - k; ++i) {
                for (int j = 0; j <= n - k; ++j) {
                    if (isMagic(grid, i, j, k)) return k;
                }
            }
        }
        return 1;
    }

    private boolean isMagic(int[][] grid, int x, int y, int k) {
        int sum = 0;
        for (int i = x; i < x + k; ++i) sum += grid[i][y];
        for (int i = x; i < x + k; ++i) {
            int row_sum = 0, col_sum = 0;
            for (int j = y; j < y + k; ++j) {
                row_sum += grid[i][j];
                col_sum += grid[i + j - x][y + j - x];
            }
            if (row_sum != sum || col_sum != sum) return false;
        }
        int dia_sum1 = 0, dia_sum2 = 0;
        for (int i = 0; i < k; ++i) {
            dia_sum1 += grid[x + i][y + i];
            dia_sum2 += grid[x + i][y + k - 1 - i];
        }
        return dia_sum1 == sum && dia_sum2 == sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])
        max_size = min(m, n)
        for k in range(max_size, 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if self.isMagic(grid, i, j, k):
                        return k
        return 1

    def isMagic(self, grid, x, y, k):
        sum_val = sum(grid[x][y:y+k])
        for i in range(x, x+k):
            if sum(grid[i][y:y+k]) != sum_val:
                return False
        for j in range(y, y+k):
            if sum(grid[i][j] for i in range(x, x+k)) != sum_val:
                return False
        dia_sum1 = sum(grid[x+i][y+i] for i in range(k))
        dia_sum2 = sum(grid[x+i][y+k-1-i] for i in range(k))
        return dia_sum1 == sum_val and dia_sum2 == sum_val
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_size = min(m, n)
        for k in range(max_size, 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if self.isMagic(grid, i, j, k):
                        return k
        return 1

    def isMagic(self, grid: list[list[int]], x: int, y: int, k: int) -> bool:
        sum_val = sum(grid[x][y:y+k])
        for i in range(x, x+k):
            if sum(grid[i][y:y+k]) != sum_val:
                return False
        for j in range(y, y+k):
            if sum(grid[i][j] for i in range(x, x+k)) != sum_val:
                return False
        dia_sum1 = sum(grid[x+i][y+i] for i in range(k))
        dia_sum2 = sum(grid[x+i][y+k-1-i] for i in range(k))
        return dia_sum1 == sum_val and dia_sum2 == sum_val
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int largestMagicSquare(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = *gridColSize, max_size = (m < n) ? m : n;
    for (int k = max_size; k > 0; --k) {
        for (int i = 0; i <= m - k; ++i) {
            for (int j = 0; j <= n - k; ++j) {
                if (isMagic(grid, i, j, k, n)) return k;
            }
        }
    }
    return 1;
}

int isMagic(int** grid, int x, int y, int k, int n) {
    int sum = 0;
    for (int i = x; i < x + k; ++i) sum += grid[i][y];
    for (int i = x; i < x + k; ++i) {
        int row_sum = 0, col_sum = 0;
        for (int j = y; j < y + k; ++j) {
            row_sum += grid[i][j];
            col_sum += grid[i + j - x][y + j - x];
        }
        if (row_sum != sum || col_sum != sum) return 0;
    }
    int dia_sum1 = 0, dia_sum2 = 0;
    for (int i = 0; i < k; ++i) {
        dia_sum1 += grid[x + i][y + i];
        dia_sum2 += grid[x + i][y + k - 1 - i];
    }
    return dia_sum1 == sum && dia_sum2 == sum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int LargestMagicSquare(int[][] grid) {
        int m = grid.Length, n = grid[0].Length, max_size = Math.Min(m, n);
        for (int k = max_size; k > 0; --k) {
            for (int i = 0; i <= m - k; ++i) {
                for (int j = 0; j <= n - k; ++j) {
                    if (IsMagic(grid, i, j, k)) return k;
                }
            }
        }
        return 1;
    }

    private bool IsMagic(int[][] grid, int x, int y, int k) {
        int sum = 0;
        for (int i = x; i < x + k; ++i) sum += grid[i][y];
        for (int i = x; i < x + k; ++i) {
            int row_sum = 0, col_sum = 0;
            for (int j = y; j < y + k; ++j) {
                row_sum += grid[i][j];
                col_sum += grid[i + j - x][y + j - x];
            }
            if (row_sum != sum || col_sum != sum) return false;
        }
        int dia_sum1 = 0, dia_sum2 = 0;
        for (int i = 0; i < k; ++i) {
            dia_sum1 += grid[x + i][y + i];
            dia_sum2 += grid[x + i][y + k - 1 - i];
        }
        return dia_sum1 == sum && dia_sum2 == sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var largestMagicSquare = function(grid) {
    let m = grid.length, n = grid[0].length, max_size = Math.min(m, n);
    for (let k = max_size; k > 0; --k) {
        for (let i = 0; i <= m - k; ++i) {
            for (let j = 0; j <= n - k; ++j) {
                if (isMagic(grid, i, j, k)) return k;
            }
        }
    }
    return 1;
};

function isMagic(grid, x, y, k) {
    let sum = 0;
    for (let i = x; i < x + k; ++i) sum += grid[i][y];
    for (let i = x; i < x + k; ++i) {
        let row_sum = 0, col_sum = 0;
        for (let j = y; j < y + k; ++j) {
            row_sum += grid[i][j];
            col_sum += grid[i + j - x][y + j - x];
        }
        if (row_sum != sum || col_sum != sum) return false;
    }
    let dia_sum1 = 0, dia_sum2 = 0;
    for (let i = 0; i < k; ++i) {
        dia_sum1 += grid[x + i][y + i];
        dia_sum2 += grid[x + i][y + k - 1 - i];
    }
    return dia_sum1 == sum && dia_sum2 == sum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function largestMagicSquare(grid: number[][]): number {
    let m = grid.length, n = grid[0].length, max_size = Math.min(m, n);
    for (let k = max_size; k > 0; --k) {
        for (let i = 0; i <= m - k; ++i) {
            for (let j = 0; j <= n - k; ++j) {
                if (isMagic(grid, i, j, k)) return k;
            }
        }
    }
    return 1;
}

function isMagic(grid: number[][], x: number, y: number, k: number): boolean {
    let sum = 0;
    for (let i = x; i < x + k; ++i) sum += grid[i][y];
    for (let i = x; i < x + k; ++i) {
        let row_sum = 0, col_sum = 0;
        for (let j = y; j < y + k; ++j) {
            row_sum += grid[i][j];
            col_sum += grid[i + j - x][y + j - x];
        }
        if (row_sum != sum || col_sum != sum) return false;
    }
    let dia_sum1 = 0, dia_sum2 = 0;
    for (let i = 0; i < k; ++i) {
        dia_sum1 += grid[x + i][y + i];
        dia_sum2 += grid[x + i][y + k - 1 - i];
    }
    return dia_sum1 == sum && dia_sum2 == sum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function largestMagicSquare($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $max_size = min($m, $n);
        for ($k = $max_size; $k > 0; --$k) {
            for ($i = 0; $i <= $m - $k; ++$i) {
                for ($j = 0; $j <= $n - $k; ++$j) {
                    if ($this->isMagic($grid, $i, $j, $k)) return $k;
                }
            }
        }
        return 1;
    }

    function isMagic($grid, $x, $y, $k) {
        $sum = 0;
        for ($i = $x; $i < $x + $k; ++$i) $sum += $grid[$i][$y];
        for ($i = $x; $i < $x + $k; ++$i) {
            $row_sum = 0;
            $col_sum = 0;
            for ($j = $y; $j < $y + $k; ++$j) {
                $row_sum += $grid[$i][$j];
                $col_sum += $grid[$i + $j - $x][$y + $j - $x];
            }
            if ($row_sum != $sum || $col_sum != $sum) return false;
        }
        $dia_sum1 = 0;
        $dia_sum2 = 0;
        for ($i = 0; $i < $k; ++$i) {
            $dia_sum1 += $grid[$x + $i][$y + $i];
            $dia_sum2 += $grid[$x + $i][$y + $k - 1 - $i];
        }
        return $dia_sum1 == $sum && $dia_sum2 == $sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func largestMagicSquare(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        let max_size = min(m, n)
        for k in stride(from: max_size, to: 0, by: -1) {
            for i in 0...m-k {
                for j in 0...n-k {
                    if isMagic(grid, i, j, k) {
                        return k
                    }
                }
            }
        }
        return 1
    }

    func isMagic(_ grid: [[Int]], _ x: Int, _ y: Int, _ k: Int) -> Bool {
        var sum = 0
        for i in x..<x+k {
            sum += grid[i][y]
        }
        for i in x..<x+k {
            var row_sum = 0
            var col_sum = 0
            for j in y..<y+k {
                row_sum += grid[i][j]
                col_sum += grid[i + j - x][y + j - x]
            }
            if row_sum != sum || col_sum != sum {
                return false
            }
        }
        var dia_sum1 = 0
        var dia_sum2 = 0
        for i in 0..<k {
            dia_sum1 += grid[x + i][y + i]
            dia_sum2 += grid[x + i][y + k - 1 - i]
        }
        return dia_sum1 == sum && dia_sum2 == sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun largestMagicSquare(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var maxSize = 1
        for (size in n downTo 1) {
            for (i in 0 until m - size + 1) {
                for (j in 0 until n - size + 1) {
                    if (isMagicSquare(grid, i, j, size)) {
                        maxSize = maxOf(maxSize, size)
                    }
                }
            }
        }
        return maxSize
    }

    private fun isMagicSquare(grid: Array<IntArray>, row: Int, col: Int, size: Int): Boolean {
        val expectedSum = grid[row][col] + grid[row][col + 1]
        for (i in row until row + size) {
            var sum = 0
            for (j in col until col + size) {
                sum += grid[i][j]
            }
            if (sum != expectedSum) return false
        }
        for (j in col until col + size) {
            var sum = 0
            for (i in row until row + size) {
                sum += grid[i][j]
            }
            if (sum != expectedSum) return false
        }
        var sum = 0
        for (i in 0 until size) {
            sum += grid[row + i][col + i]
        }
        if (sum != expectedSum) return false
        sum = 0
        for (i in 0 until size) {
            sum += grid[row + i][col + size - 1 - i]
        }
        return sum == expectedSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int largestMagicSquare(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    int maxSize = 1;
    for (int size = n; size >= 1; size--) {
      for (int i = 0; i <= m - size; i++) {
        for (int j = 0; j <= n - size; j++) {
          if (isMagicSquare(grid, i, j, size)) {
            maxSize = size;
          }
        }
      }
    }
    return maxSize;
  }

  bool isMagicSquare(List<List<int>> grid, int row, int col, int size) {
    int expectedSum = 0;
    for (int i = row; i < row + size; i++) {
      expectedSum += grid[i][col];
    }
    for (int i = row; i < row + size; i++) {
      int sum = 0;
      for (int j = col; j < col + size; j++) {
        sum += grid[i][j];
      }
      if (sum != expectedSum) return false;
    }
    for (int j = col; j < col + size; j++) {
      int sum = 0;
      for (int i = row; i < row + size; i++) {
        sum += grid[i][j];
      }
      if (sum != expectedSum) return false;
    }
    int sum = 0;
    for (int i = 0; i < size; i++) {
      sum += grid[row + i][col + i];
    }
    if (sum != expectedSum) return false;
    sum = 0;
    for (int i = 0; i < size; i++) {
      sum += grid[row + i][col + size - 1 - i];
    }
    return sum == expectedSum;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func largestMagicSquare(grid [][]int) int {
    m, n := len(grid), len(grid[0])
    maxSize := 1
    for size := n; size >= 1; size-- {
        for i := 0; i <= m-size; i++ {
            for j := 0; j <= n-size; j++ {
                if isMagicSquare(grid, i, j, size) {
                    maxSize = size
                }
            }
        }
    }
    return maxSize
}

func isMagicSquare(grid [][]int, row, col, size int) bool {
    expectedSum := 0
    for i := row; i < row+size; i++ {
        expectedSum += grid[i][col]
    }
    for i := row; i < row+size; i++ {
        sum := 0
        for j := col; j < col+size; j++ {
            sum += grid[i][j]
        }
        if sum != expectedSum {
            return false
        }
    }
    for j := col; j < col+size; j++ {
        sum := 0
        for i := row; i < row+size; i++ {
            sum += grid[i][j]
        }
        if sum != expectedSum {
            return false
        }
    }
    sum := 0
    for i := 0; i < size; i++ {
        sum += grid[row+i][col+i]
    }
    if sum != expectedSum {
        return false
    }
    sum = 0
    for i := 0; i < size; i++ {
        sum += grid[row+i][col+size-1-i]
    }
    return sum == expectedSum
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def largest_magic_square(grid)
  m, n = grid.size, grid[0].size
  max_size = 1
  (n).downto(1) do |size|
    (0...m - size + 1).each do |i|
      (0...n - size + 1).each do |j|
        if is_magic_square(grid, i, j, size)
          max_size = size
        end
      end
    end
  end
  max_size
end

private

def is_magic_square(grid, row, col, size)
  expected_sum = 0
  (row...row + size).each do |i|
    expected_sum += grid[i][col]
  end
  (row...row + size).each do |i|
    sum = 0
    (col...col + size).each do |j|
      sum += grid[i][j]
    end
    return false if sum != expected_sum
  end
  (col...col + size).each do |j|
    sum = 0
    (row...row + size).each do |i|
      sum += grid[i][j]
    end
    return false if sum != expected_sum
  end
  sum = 0
  (0...size).each do |i|
    sum += grid[row + i][col + i]
  end
  return false if sum != expected_sum
  sum = 0
  (0...size).each do |i|
    sum += grid[row + i][col + size - 1 - i]
  end
  sum == expected_sum
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def largestMagicSquare(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var maxSize = 1
    for (size <- n to 1 by -1) {
      for (i <- 0 until m - size + 1) {
        for (j <- 0 until n - size + 1) {
          if (isMagicSquare(grid, i, j, size)) {
            maxSize = size
          }
        }
      }
    }
    maxSize
  }

  private def isMagicSquare(grid: Array[Array[Int]], row: Int, col: Int, size: Int): Boolean = {
    val expectedSum = (row until row + size).map(i => grid(i)(col)).sum
    (row until row + size).forall { i =>
      (col until col + size).map(j => grid(i)(j)).sum == expectedSum
    } &&
    (col until col + size).forall { j =>
      (row until row + size).map(i => grid(i)(j)).sum == expectedSum
    } &&
    (0 until size).map(i => grid(row + i)(col + i)).sum == expectedSum &&
    (0 until size).map(i => grid(row + i)(col + size - 1 - i)).sum == expectedSum
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
  pub fn largest_magic_square(grid: Vec<Vec<i32>>) -> i32 {
    let m = grid.len() as i32;
    let n = grid[0].len() as i32;
    let mut max_size = 1;
    for size in (1..=n).rev() {
      for i in 0..=m - size {
        for j in 0..=n - size {
          if Solution::is_magic_square(&grid, i as usize, j as usize, size as usize) {
            max_size = size;
          }
        }
      }
    }
    max_size
  }

  fn is_magic_square(grid: &Vec<Vec<i32>>, row: usize, col: usize, size: usize) -> bool {
    let mut expected_sum = 0;
    for i in row..row + size {
      expected_sum += grid[i][col];
    }
    for i in row..row + size {
      let mut sum = 0;
      for j in col..col + size {
        sum += grid[i][j];
      }
      if sum != expected_sum {
        return false;
      }
    }
    for j in col..col + size {
      let mut sum = 0;
      for i in row..row + size {
        sum += grid[i][j];
      }
      if sum != expected_sum {
        return false;
      }
    }
    let mut sum = 0;
    for i in 0..size {
      sum += grid[row + i][col + i];
    }
    if sum != expected_sum {
      return false;
    }
    sum = 0;
    for i in 0..size {
      sum += grid[row + i][col + size - 1 - i];
    }
    sum == expected_sum
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (largest-magic-square grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([m (length grid)]
         [n (length (car grid))]
         [max-size 1])
    (for ([size (in-range n 0 -1)])
      (for ([i (in-range m)])
        (for ([j (in-range n)])
          (when (and (>= m (+ i size)) (>= n (+ j size)))
            (when (is-magic-square grid i j size)
              (set! max-size size))))))
    max-size))

(define (is-magic-square grid row col size)
  (let* ([expected-sum (apply + (map (lambda (i) (list-ref (list-ref grid i) col))
                                        (range row (+ row size))))]
         [rows (map (lambda (i) (apply + (map (lambda (j) (list-ref (list-ref grid i) (+ j col)))
                                                  (range 0 size))))
                        (range row (+ row size)))])
    (andmap (lambda (x) (= x expected-sum)) rows)
    (let ([cols (map (lambda (j) (apply + (map (lambda (i) (list-ref (list-ref grid (+ i row)) (+ j col)))
                                                  (range 0 size))))
                             (range 0 size))])
      (and (andmap (lambda (x) (= x expected-sum)) cols)
           (= expected-sum (apply + (map (lambda (i) (list-ref (list-ref grid (+ i row)) (+ i col)))
                                           (range 0 size))))
           (= expected-sum (apply + (map (lambda (i) (list-ref (list-ref grid (+ i row)) (+ (- size 1 i) col)))
                                           (range 0 size))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
largest_magic_square(Grid) ->
  MaxSize = 1,
  M = length(Grid),
  N = length(hd(Grid)),
  lists:foreach(fun(Size) ->
                     lists:foreach(fun(I) ->
                                   lists:foreach(fun(J) ->
                                                 case is_magic_square(Grid, I, J, Size) of
                                                   true -> MaxSize = Size;
                                                   false -> ok
                                                 end
                                       end, lists:seq(0, M - Size)),
                             lists:seq(0, N - Size))
                 end, lists:seq(N, 1, -1)),
  MaxSize.

is_magic_square(Grid, Row, Col, Size) ->
  ExpectedSum = lists:sum([lists:nth(Col + 1, lists:nth(Row + 1, Grid)) || _ <- lists:seq(0, Size - 1)]),
  lists:all(fun(I) -> lists:sum([lists:nth(J + 1, lists:nth(I + Row + 1, Grid)) || J <- lists:seq(0, Size - 1)]) =:= ExpectedSum end,
           lists:seq(0, Size - 1)) andalso
  lists:all(fun(J) -> lists:sum([lists:nth(J + 1, lists:nth(I + Row + 1, Grid)) || I <- lists:seq(0, Size - 1)]) =:= ExpectedSum end,
           lists:seq(0, Size - 1)) andalso
  lists:sum([lists:nth(Col + I + 1, lists:nth(Row + I + 1, Grid)) || I <- lists:seq(0, Size - 1)]) =:= ExpectedSum andalso
  lists:sum([lists:nth(Col + Size - 1 - I + 1, lists:nth(Row + I + 1, Grid)) || I <- lists:seq(0, Size - 1)]) =:= ExpectedSum.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec largest_magic_square(grid :: [[integer]]) :: integer
  def largest_magic_square(grid) do
    m = length(grid)
    n = length(Enum.at(grid, 0))
    max_size = 1
    Enum.reduce((n)..1, max_size, fn size, max_size ->
      Enum.reduce(0..(m - size), max_size, fn i, max_size ->
        Enum.reduce(0..(n - size), max_size, fn j, max_size ->
          if is_magic_square(grid, i, j, size) do
            size
          else
            max_size
          end
        end)
      end)
    end)
  end

  defp is_magic_square(grid, row, col, size) do
    expected_sum =
      Enum.reduce(row..(row + size - 1), 0, fn i, sum ->
        sum + Enum.at(Enum.at(grid, i), col)
      end)
    rows =
      Enum.map(row..(row + size - 1), fn i ->
        Enum.reduce(col..(col + size - 1), 0, fn j, sum ->
          sum + Enum.at(Enum.at(grid, i), j)
        end)
      end)
    cols =
      Enum.map(col..(col + size - 1), fn j ->
        Enum.reduce(row..(row + size - 1), 0, fn i, sum ->
          sum + Enum.at(Enum.at(grid, i), j)
        end)
      end)
    Enum.all?(rows, fn x -> x == expected_sum end) and
      Enum.all?(cols, fn x -> x == expected_sum end) and
      Enum.reduce(0..(size - 1), 0, fn i, sum ->
        sum + Enum.at(Enum.at(grid, row + i), col + i)
      end) == expected_sum and
      Enum.reduce(0..(size - 1), 0, fn i, sum ->
        sum + Enum.at(Enum.at(grid, row + i), col + size - 1 - i)
      end) == expected_sum
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(m^3 * n^3) where m and n are the dimensions of the grid. This is because for each cell in the grid, we are potentially checking all possible squares that can be formed with that cell as the top-left corner. The sum of each row, column, and diagonal is calculated for each square, resulting in a cubic time complexity.

- **Space Complexity:** The space complexity is O(1) as we are not using any additional space that scales with the input size. We are only using a constant amount of space to store the maximum size of the magic square found so far.

</div>
</details>
