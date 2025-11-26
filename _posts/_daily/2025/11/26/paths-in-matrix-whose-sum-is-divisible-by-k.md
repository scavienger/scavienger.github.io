---
layout: post
title: "Paths in Matrix Whose Sum Is Divisible by K"
date: 2025-11-26 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Dynamic Programming", "Matrix"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int numberOfPaths(std::vector<std::vector<int>>&\
        \ grid, int k) {\n        int MOD = 1e9 + 7;\n        int m = grid.size();\n\
        \        int n = grid[0].size();\n\n        // dp[j][rem] stores the number\
        \ of paths to (current_row, j) with sum % k == rem\n        std::vector<std::vector<int>>\
        \ dp(n, std::vector<int>(k, 0));\n\n        // Base case: (0, 0)\n        dp[0][grid[0][0]\
        \ % k] = 1;\n\n        // Fill the first row (i = 0)\n        for (int j = 1;\
        \ j < n; ++j) {\n            int val = grid[0][j];\n            int val_rem\
        \ = val % k;\n            for (int prev_rem = 0; prev_rem < k; ++prev_rem) {\n\
        \                if (dp[j-1][prev_rem] > 0) {\n                    int current_rem\
        \ = (prev_rem + val_rem) % k;\n                    dp[j][current_rem] = (dp[j][current_rem]\
        \ + dp[j-1][prev_rem]) % MOD;\n                }\n            }\n        }\n\
        \n        // Fill subsequent rows (i from 1 to m-1)\n        for (int i = 1;\
        \ i < m; ++i) {\n            // new_dp_row will store counts for the current\
        \ row i\n            std::vector<std::vector<int>> new_dp_row(n, std::vector<int>(k,\
        \ 0));\n\n            // First cell of current row (i, 0)\n            int val\
        \ = grid[i][0];\n            int val_rem = val % k;\n            for (int prev_rem\
        \ = 0; prev_rem < k; ++prev_rem) {\n                if (dp[0][prev_rem] > 0)\
        \ { // Paths from (i-1, 0)\n                    int current_rem = (prev_rem\
        \ + val_rem) % k;\n                    new_dp_row[0][current_rem] = (new_dp_row[0][current_rem]\
        \ + dp[0][prev_rem]) % MOD;\n                }\n            }\n\n          \
        \  // Remaining cells of current row (i, j) for j from 1 to n-1\n          \
        \  for (int j = 1; j < n; ++j) {\n                val = grid[i][j];\n      \
        \          val_rem = val % k;\n                for (int prev_rem = 0; prev_rem\
        \ < k; ++prev_rem) {\n                    // Paths from (i-1, j)\n         \
        \           if (dp[j][prev_rem] > 0) {\n                        int current_rem\
        \ = (prev_rem + val_rem) % k;\n                        new_dp_row[j][current_rem]\
        \ = (new_dp_row[j][current_rem] + dp[j][prev_rem]) % MOD;\n                \
        \    }\n\n                    // Paths from (i, j-1)\n                    if\
        \ (new_dp_row[j-1][prev_rem] > 0) {\n                        int current_rem\
        \ = (prev_rem + val_rem) % k;\n                        new_dp_row[j][current_rem]\
        \ = (new_dp_row[j][current_rem] + new_dp_row[j-1][prev_rem]) % MOD;\n      \
        \              }\n                }\n            }\n\n            dp = new_dp_row;\
        \ // Update dp to be the current row for the next iteration\n        }\n\n \
        \       return dp[n-1][0];\n    }\n};"
      java: "class Solution {\n    public int numberOfPaths(int[][] grid, int k) {\n\
        \        int MOD = 1_000_000_007;\n        int m = grid.length;\n        int\
        \ n = grid[0].length;\n\n        // dp[j][rem] stores the number of paths to\
        \ (current_row, j) with sum % k == rem\n        int[][] dp = new int[n][k];\n\
        \n        // Base case: (0, 0)\n        dp[0][grid[0][0] % k] = 1;\n\n     \
        \   // Fill the first row (i = 0)\n        for (int j = 1; j < n; ++j) {\n \
        \           int val = grid[0][j];\n            int val_rem = val % k;\n    \
        \        for (int prev_rem = 0; prev_rem < k; ++prev_rem) {\n              \
        \  if (dp[j-1][prev_rem] > 0) {\n                    int current_rem = (prev_rem\
        \ + val_rem) % k;\n                    dp[j][current_rem] = (dp[j][current_rem]\
        \ + dp[j-1][prev_rem]) % MOD;\n                }\n            }\n        }\n\
        \n        // Fill subsequent rows (i from 1 to m-1)\n        for (int i = 1;\
        \ i < m; ++i) {\n            // new_dp_row will store counts for the current\
        \ row i\n            int[][] newDpRow = new int[n][k];\n\n            // First\
        \ cell of current row (i, 0)\n            int val = grid[i][0];\n          \
        \  int val_rem = val % k;\n            for (int prev_rem = 0; prev_rem < k;\
        \ ++prev_rem) {\n                if (dp[0][prev_rem] > 0) { // Paths from (i-1,\
        \ 0)\n                    int current_rem = (prev_rem + val_rem) % k;\n    \
        \                newDpRow[0][current_rem] = (newDpRow[0][current_rem] + dp[0][prev_rem])\
        \ % MOD;\n                }\n            }\n\n            // Remaining cells\
        \ of current row (i, j) for j from 1 to n-1\n            for (int j = 1; j <\
        \ n; ++j) {\n                val = grid[i][j];\n                val_rem = val\
        \ % k;\n                for (int prev_rem = 0; prev_rem < k; ++prev_rem) {\n\
        \                    // Paths from (i-1, j)\n                    if (dp[j][prev_rem]\
        \ > 0) {\n                        int current_rem = (prev_rem + val_rem) % k;\n\
        \                        newDpRow[j][current_rem] = (newDpRow[j][current_rem]\
        \ + dp[j][prev_rem]) % MOD;\n                    }\n\n                    //\
        \ Paths from (i, j-1)\n                    if (newDpRow[j-1][prev_rem] > 0)\
        \ {\n                        int current_rem = (prev_rem + val_rem) % k;\n \
        \                       newDpRow[j][current_rem] = (newDpRow[j][current_rem]\
        \ + newDpRow[j-1][prev_rem]) % MOD;\n                    }\n               \
        \ }\n            }\n\n            dp = newDpRow; // Update dp to be the current\
        \ row for the next iteration\n        }\n\n        return dp[n-1][0];\n    }\n\
        }"
      python: "class Solution:\n    def numberOfPaths(self, grid: List[List[int]], k:\
        \ int) -> int:\n        MOD = 10**9 + 7\n        m = len(grid)\n        n =\
        \ len(grid[0])\n\n        # dp[j][rem] stores the number of paths to (current_row,\
        \ j) with sum % k == rem\n        dp = [[0] * k for _ in range(n)]\n\n     \
        \   # Base case: (0, 0)\n        dp[0][grid[0][0] % k] = 1\n\n        # Fill\
        \ the first row (i = 0)\n        for j in range(1, n):\n            val = grid[0][j]\n\
        \            val_rem = val % k\n            for prev_rem in range(k):\n    \
        \            if dp[j-1][prev_rem] > 0:\n                    current_rem = (prev_rem\
        \ + val_rem) % k\n                    dp[j][current_rem] = (dp[j][current_rem]\
        \ + dp[j-1][prev_rem]) % MOD\n\n        # Fill subsequent rows (i from 1 to\
        \ m-1)\n        for i in range(1, m):\n            # new_dp_row will store counts\
        \ for the current row i\n            new_dp_row = [[0] * k for _ in range(n)]\n\
        \n            # First cell of current row (i, 0)\n            val = grid[i][0]\n\
        \            val_rem = val % k\n            for prev_rem in range(k):\n    \
        \            if dp[0][prev_rem] > 0: # Paths from (i-1, 0)\n               \
        \     current_rem = (prev_rem + val_rem) % k\n                    new_dp_row[0][current_rem]\
        \ = (new_dp_row[0][current_rem] + dp[0][prev_rem]) % MOD\n\n            # Remaining\
        \ cells of current row (i, j) for j from 1 to n-1\n            for j in range(1,\
        \ n):\n                val = grid[i][j]\n                val_rem = val % k\n\
        \                for prev_rem in range(k):\n                    # Paths from\
        \ (i-1, j)\n                    if dp[j][prev_rem] > 0:\n                  \
        \      current_rem = (prev_rem + val_rem) % k\n                        new_dp_row[j][current_rem]\
        \ = (new_dp_row[j][current_rem] + dp[j][prev_rem]) % MOD\n\n               \
        \     # Paths from (i, j-1)\n                    if new_dp_row[j-1][prev_rem]\
        \ > 0:\n                        current_rem = (prev_rem + val_rem) % k\n   \
        \                     new_dp_row[j][current_rem] = (new_dp_row[j][current_rem]\
        \ + new_dp_row[j-1][prev_rem]) % MOD\n\n            dp = new_dp_row # Update\
        \ dp to be the current row for the next iteration\n\n        return dp[n-1][0]"
      python3: "class Solution:\n    def numberOfPaths(self, grid: List[List[int]],\
        \ k: int) -> int:\n        MOD = 10**9 + 7\n        m = len(grid)\n        n\
        \ = len(grid[0])\n\n        # dp[j][rem] stores the number of paths to (current_row,\
        \ j) with sum % k == rem\n        dp = [[0] * k for _ in range(n)]\n\n     \
        \   # Base case: (0, 0)\n        dp[0][grid[0][0] % k] = 1\n\n        # Fill\
        \ the first row (i = 0)\n        for j in range(1, n):\n            val = grid[0][j]\n\
        \            val_rem = val % k\n            for prev_rem in range(k):\n    \
        \            if dp[j-1][prev_rem] > 0:\n                    current_rem = (prev_rem\
        \ + val_rem) % k\n                    dp[j][current_rem] = (dp[j][current_rem]\
        \ + dp[j-1][prev_rem]) % MOD\n\n        # Fill subsequent rows (i from 1 to\
        \ m-1)\n        for i in range(1, m):\n            # new_dp_row will store counts\
        \ for the current row i\n            new_dp_row = [[0] * k for _ in range(n)]\n\
        \n            # First cell of current row (i, 0)\n            val = grid[i][0]\n\
        \            val_rem = val % k\n            for prev_rem in range(k):\n    \
        \            if dp[0][prev_rem] > 0: # Paths from (i-1, 0)\n               \
        \     current_rem = (prev_rem + val_rem) % k\n                    new_dp_row[0][current_rem]\
        \ = (new_dp_row[0][current_rem] + dp[0][prev_rem]) % MOD\n\n            # Remaining\
        \ cells of current row (i, j) for j from 1 to n-1\n            for j in range(1,\
        \ n):\n                val = grid[i][j]\n                val_rem = val % k\n\
        \                for prev_rem in range(k):\n                    # Paths from\
        \ (i-1, j)\n                    if dp[j][prev_rem] > 0:\n                  \
        \      current_rem = (prev_rem + val_rem) % k\n                        new_dp_row[j][current_rem]\
        \ = (new_dp_row[j][current_rem] + dp[j][prev_rem]) % MOD\n\n               \
        \     # Paths from (i, j-1)\n                    if new_dp_row[j-1][prev_rem]\
        \ > 0:\n                        current_rem = (prev_rem + val_rem) % k\n   \
        \                     new_dp_row[j][current_rem] = (new_dp_row[j][current_rem]\
        \ + new_dp_row[j-1][prev_rem]) % MOD\n\n            dp = new_dp_row # Update\
        \ dp to be the current row for the next iteration\n\n        return dp[n-1][0]"
      c: "#include <stdlib.h>\n#include <string.h>\n\nint numberOfPaths(int** grid,\
        \ int gridSize, int* gridColSize, int k) {\n    int MOD = 1e9 + 7;\n    int\
        \ m = gridSize;\n    int n = gridColSize[0];\n\n    // dp[j][rem] stores the\
        \ number of paths to (current_row, j) with sum % k == rem\n    int** dp = (int**)malloc(n\
        \ * sizeof(int*));\n    for (int j = 0; j < n; ++j) {\n        dp[j] = (int*)calloc(k,\
        \ sizeof(int));\n    }\n\n    // Base case: (0, 0)\n    dp[0][grid[0][0] % k]\
        \ = 1;\n\n    // Fill the first row (i = 0)\n    for (int j = 1; j < n; ++j)\
        \ {\n        int val = grid[0][j];\n        int val_rem = val % k;\n       \
        \ for (int prev_rem = 0; prev_rem < k; ++prev_rem) {\n            if (dp[j-1][prev_rem]\
        \ > 0) {\n                int current_rem = (prev_rem + val_rem) % k;\n    \
        \            dp[j][current_rem] = (dp[j][current_rem] + dp[j-1][prev_rem]) %\
        \ MOD;\n            }\n        }\n    }\n\n    // Fill subsequent rows (i from\
        \ 1 to m-1)\n    for (int i = 1; i < m; ++i) {\n        // new_dp_row will store\
        \ counts for the current row i\n        int** new_dp_row = (int**)malloc(n *\
        \ sizeof(int*));\n        for (int j = 0; j < n; ++j) {\n            new_dp_row[j]\
        \ = (int*)calloc(k, sizeof(int));\n        }\n\n        // First cell of current\
        \ row (i, 0)\n        int val = grid[i][0];\n        int val_rem = val % k;\n\
        \        for (int prev_rem = 0; prev_rem < k; ++prev_rem) {\n            if\
        \ (dp[0][prev_rem] > 0) { // Paths from (i-1, 0)\n                int current_rem\
        \ = (prev_rem + val_rem) % k;\n                new_dp_row[0][current_rem] =\
        \ (new_dp_row[0][current_rem] + dp[0][prev_rem]) % MOD;\n            }\n   \
        \     }\n\n        // Remaining cells of current row (i, j) for j from 1 to\
        \ n-1\n        for (int j = 1; j < n; ++j) {\n            val = grid[i][j];\n\
        \            val_rem = val % k;\n            for (int prev_rem = 0; prev_rem\
        \ < k; ++prev_rem) {\n                // Paths from (i-1, j)\n             \
        \   if (dp[j][prev_rem] > 0) {\n                    int current_rem = (prev_rem\
        \ + val_rem) % k;\n                    new_dp_row[j][current_rem] = (new_dp_row[j][current_rem]\
        \ + dp[j][prev_rem]) % MOD;\n                }\n\n                // Paths from\
        \ (i, j-1)\n                if (new_dp_row[j-1][prev_rem] > 0) {\n         \
        \           int current_rem = (prev_rem + val_rem) % k;\n                  \
        \  new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + new_dp_row[j-1][prev_rem])\
        \ % MOD;\n                }\n            }\n        }\n\n        // Free previous\
        \ dp and update\n        for (int j = 0; j < n; ++j) {\n            free(dp[j]);\n\
        \        }\n        free(dp);\n        dp = new_dp_row; // Update dp to be the\
        \ current row for the next iteration\n    }\n\n    int result = dp[n-1][0];\n\
        \n    // Free final dp\n    for (int j = 0; j < n; ++j) {\n        free(dp[j]);\n\
        \    }\n    free(dp);\n\n    return result;\n}"
      csharp: "public class Solution {\n    public int NumberOfPaths(int[][] grid, int\
        \ k) {\n        int MOD = 1_000_000_007;\n        int m = grid.Length;\n   \
        \     int n = grid[0].Length;\n\n        // dp[j][rem] stores the number of\
        \ paths to (current_row, j) with sum % k == rem\n        int[][] dp = new int[n][];\n\
        \        for (int j = 0; j < n; j++) {\n            dp[j] = new int[k];\n  \
        \      }\n\n        // Base case: (0, 0)\n        dp[0][grid[0][0] % k] = 1;\n\
        \n        // Fill the first row (i = 0)\n        for (int j = 1; j < n; ++j)\
        \ {\n            int val = grid[0][j];\n            int valRem = val % k;\n\
        \            for (int prevRem = 0; prevRem < k; ++prevRem) {\n             \
        \   if (dp[j-1][prevRem] > 0) {\n                    int currentRem = (prevRem\
        \ + valRem) % k;\n                    dp[j][currentRem] = (dp[j][currentRem]\
        \ + dp[j-1][prevRem]) % MOD;\n                }\n            }\n        }\n\n\
        \        // Fill subsequent rows (i from 1 to m-1)\n        for (int i = 1;\
        \ i < m; ++i) {\n            // newDpRow will store counts for the current row\
        \ i\n            int[][] newDpRow = new int[n][];\n            for (int j =\
        \ 0; j < n; j++) {\n                newDpRow[j] = new int[k];\n            }\n\
        \n            // First cell of current row (i, 0)\n            int val = grid[i][0];\n\
        \            int valRem = val % k;\n            for (int prevRem = 0; prevRem\
        \ < k; ++prevRem) {\n                if (dp[0][prevRem] > 0) { // Paths from\
        \ (i-1, 0)\n                    int currentRem = (prevRem + valRem) % k;\n \
        \                   newDpRow[0][currentRem] = (newDpRow[0][currentRem] + dp[0][prevRem])\
        \ % MOD;\n                }\n            }\n\n            // Remaining cells\
        \ of current row (i, j) for j from 1 to n-1\n            for (int j = 1; j <\
        \ n; ++j) {\n                val = grid[i][j];\n                valRem = val\
        \ % k;\n                for (int prevRem = 0; prevRem < k; ++prevRem) {\n  \
        \                  // Paths from (i-1, j)\n                    if (dp[j][prevRem]\
        \ > 0) {\n                        int currentRem = (prevRem + valRem) % k;\n\
        \                        newDpRow[j][currentRem] = (newDpRow[j][currentRem]\
        \ + dp[j][prevRem]) % MOD;\n                    }\n\n                    //\
        \ Paths from (i, j-1)\n                    if (newDpRow[j-1][prevRem] > 0) {\n\
        \                        int currentRem = (prevRem + valRem) % k;\n        \
        \                newDpRow[j][currentRem] = (newDpRow[j][currentRem] + newDpRow[j-1][prevRem])\
        \ % MOD;\n                    }\n                }\n            }\n\n      \
        \      dp = newDpRow; // Update dp to be the current row for the next iteration\n\
        \        }\n\n        return dp[n-1][0];\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @param {number} k\n * @return\
        \ {number}\n */\nvar numberOfPaths = function(grid, k) {\n    const MOD = 1e9\
        \ + 7;\n    const m = grid.length;\n    const n = grid[0].length;\n\n    //\
        \ dp[j][rem] stores the number of paths to (current_row, j) with sum % k ==\
        \ rem\n    let dp = Array(n).fill(0).map(() => Array(k).fill(0));\n\n    //\
        \ Base case: (0, 0)\n    dp[0][grid[0][0] % k] = 1;\n\n    // Fill the first\
        \ row (i = 0)\n    for (let j = 1; j < n; ++j) {\n        const val = grid[0][j];\n\
        \        const val_rem = val % k;\n        for (let prev_rem = 0; prev_rem <\
        \ k; ++prev_rem) {\n            if (dp[j-1][prev_rem] > 0) {\n             \
        \   const current_rem = (prev_rem + val_rem) % k;\n                dp[j][current_rem]\
        \ = (dp[j][current_rem] + dp[j-1][prev_rem]) % MOD;\n            }\n       \
        \ }\n    }\n\n    // Fill subsequent rows (i from 1 to m-1)\n    for (let i\
        \ = 1; i < m; ++i) {\n        // new_dp_row will store counts for the current\
        \ row i\n        let new_dp_row = Array(n).fill(0).map(() => Array(k).fill(0));\n\
        \n        // First cell of current row (i, 0)\n        const val = grid[i][0];\n\
        \        const val_rem = val % k;\n        for (let prev_rem = 0; prev_rem <\
        \ k; ++prev_rem) {\n            if (dp[0][prev_rem] > 0) { // Paths from (i-1,\
        \ 0)\n                const current_rem = (prev_rem + val_rem) % k;\n      \
        \          new_dp_row[0][current_rem] = (new_dp_row[0][current_rem] + dp[0][prev_rem])\
        \ % MOD;\n            }\n        }\n\n        // Remaining cells of current\
        \ row (i, j) for j from 1 to n-1\n        for (let j = 1; j < n; ++j) {\n  \
        \          const val = grid[i][j];\n            const val_rem = val % k;\n \
        \           for (let prev_rem = 0; prev_rem < k; ++prev_rem) {\n           \
        \     // Paths from (i-1, j)\n                if (dp[j][prev_rem] > 0) {\n \
        \                   const current_rem = (prev_rem + val_rem) % k;\n        \
        \            new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + dp[j][prev_rem])\
        \ % MOD;\n                }\n\n                // Paths from (i, j-1)\n    \
        \            if (new_dp_row[j-1][prev_rem] > 0) {\n                    const\
        \ current_rem = (prev_rem + val_rem) % k;\n                    new_dp_row[j][current_rem]\
        \ = (new_dp_row[j][current_rem] + new_dp_row[j-1][prev_rem]) % MOD;\n      \
        \          }\n            }\n        }\n\n        dp = new_dp_row; // Update\
        \ dp to be the current row for the next iteration\n    }\n\n    return dp[n-1][0];\n\
        };"
      typescript: "function numberOfPaths(grid: number[][], k: number): number {\n \
        \   const MOD = 10**9 + 7;\n    const m = grid.length;\n    const n = grid[0].length;\n\
        \n    // dp[j][rem] stores the number of paths to (current_row, j) with sum\
        \ % k == rem\n    let dp: number[][] = Array(n).fill(0).map(() => Array(k).fill(0));\n\
        \n    // Base case: (0, 0)\n    dp[0][grid[0][0] % k] = 1;\n\n    // Fill the\
        \ first row (i = 0)\n    for (let j = 1; j < n; ++j) {\n        const val =\
        \ grid[0][j];\n        const val_rem = val % k;\n        for (let prev_rem =\
        \ 0; prev_rem < k; ++prev_rem) {\n            if (dp[j-1][prev_rem] > 0) {\n\
        \                const current_rem = (prev_rem + val_rem) % k;\n           \
        \     dp[j][current_rem] = (dp[j][current_rem] + dp[j-1][prev_rem]) % MOD;\n\
        \            }\n        }\n    }\n\n    // Fill subsequent rows (i from 1 to\
        \ m-1)\n    for (let i = 1; i < m; ++i) {\n        // new_dp_row will store\
        \ counts for the current row i\n        let new_dp_row: number[][] = Array(n).fill(0).map(()\
        \ => Array(k).fill(0));\n\n        // First cell of current row (i, 0)\n   \
        \     const val = grid[i][0];\n        const val_rem = val % k;\n        for\
        \ (let prev_rem = 0; prev_rem < k; ++prev_rem) {\n            if (dp[0][prev_rem]\
        \ > 0) { // Paths from (i-1, 0)\n                const current_rem = (prev_rem\
        \ + val_rem) % k;\n                new_dp_row[0][current_rem] = (new_dp_row[0][current_rem]\
        \ + dp[0][prev_rem]) % MOD;\n            }\n        }\n\n        // Remaining\
        \ cells of current row (i, j) for j from 1 to n-1\n        for (let j = 1; j\
        \ < n; ++j) {\n            const val = grid[i][j];\n            const val_rem\
        \ = val % k;\n            for (let prev_rem = 0; prev_rem < k; ++prev_rem) {\n\
        \                // Paths from (i-1, j)\n                if (dp[j][prev_rem]\
        \ > 0) {\n                    const current_rem = (prev_rem + val_rem) % k;\n\
        \                    new_dp_row[j][current_rem] = (new_dp_row[j][current_rem]\
        \ + dp[j][prev_rem]) % MOD;\n                }\n\n                // Paths from\
        \ (i, j-1)\n                if (new_dp_row[j-1][prev_rem] > 0) {\n         \
        \           const current_rem = (prev_rem + val_rem) % k;\n                \
        \    new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + new_dp_row[j-1][prev_rem])\
        \ % MOD;\n                }\n            }\n        }\n\n        dp = new_dp_row;\
        \ // Update dp to be the current row for the next iteration\n    }\n\n    return\
        \ dp[n-1][0];\n}"
      php: "class Solution {\n    /**\n     * @param int[][] $grid\n     * @param int\
        \ $k\n     * @return int\n     */\n    function numberOfPaths(array $grid, int\
        \ $k): int {\n        $MOD = 10**9 + 7;\n        $m = count($grid);\n      \
        \  $n = count($grid[0]);\n\n        // dp[j][rem] stores the number of paths\
        \ to (current_row, j) with sum % k == rem\n        $dp = array_fill(0, $n, array_fill(0,\
        \ $k, 0));\n\n        // Base case: (0, 0)\n        $dp[0][$grid[0][0] % $k]\
        \ = 1;\n\n        // Fill the first row (i = 0)\n        for ($j = 1; $j < $n;\
        \ ++$j) {\n            $val = $grid[0][$j];\n            $val_rem = $val % $k;\n\
        \            for ($prev_rem = 0; $prev_rem < $k; ++$prev_rem) {\n          \
        \      if ($dp[$j-1][$prev_rem] > 0) {\n                    $current_rem = ($prev_rem\
        \ + $val_rem) % $k;\n                    $dp[$j][$current_rem] = ($dp[$j][$current_rem]\
        \ + $dp[$j-1][$prev_rem]) % $MOD;\n                }\n            }\n      \
        \  }\n\n        // Fill subsequent rows (i from 1 to m-1)\n        for ($i =\
        \ 1; $i < $m; ++$i) {\n            // new_dp_row will store counts for the current\
        \ row i\n            $new_dp_row = array_fill(0, $n, array_fill(0, $k, 0));\n\
        \n            // First cell of current row (i, 0)\n            $val = $grid[$i][0];\n\
        \            $val_rem = $val % $k;\n            for ($prev_rem = 0; $prev_rem\
        \ < $k; ++$prev_rem) {\n                if ($dp[0][$prev_rem] > 0) { // Paths\
        \ from (i-1, 0)\n                    $current_rem = ($prev_rem + $val_rem) %\
        \ $k;\n                    $new_dp_row[0][$current_rem] = ($new_dp_row[0][$current_rem]\
        \ + $dp[0][$prev_rem]) % $MOD;\n                }\n            }\n\n       \
        \     // Remaining cells of current row (i, j) for j from 1 to n-1\n       \
        \     for ($j = 1; $j < $n; ++$j) {\n                $val = $grid[$i][$j];\n\
        \                $val_rem = $val % $k;\n                for ($prev_rem = 0;\
        \ $prev_rem < $k; ++$prev_rem) {\n                    // Paths from (i-1, j)\n\
        \                    if ($dp[$j][$prev_rem] > 0) {\n                       \
        \ $current_rem = ($prev_rem + $val_rem) % $k;\n                        $new_dp_row[$j][$current_rem]\
        \ = ($new_dp_row[$j][$current_rem] + $dp[$j][$prev_rem]) % $MOD;\n         \
        \           }\n\n                    // Paths from (i, j-1)\n              \
        \      if ($new_dp_row[$j-1][$prev_rem] > 0) {\n                        $current_rem\
        \ = ($prev_rem + $val_rem) % $k;\n                        $new_dp_row[$j][$current_rem]\
        \ = ($new_dp_row[$j][$current_rem] + $new_dp_row[$j-1][$prev_rem]) % $MOD;\n\
        \                    }\n                }\n            }\n\n            $dp\
        \ = $new_dp_row; // Update dp to be the current row for the next iteration\n\
        \        }\n\n        return $dp[$n-1][0];\n    }\n}"
      swift: "class Solution {\n    func numberOfPaths(_ grid: [[Int]], _ k: Int) ->\
        \ Int {\n        let MOD = 1_000_000_007\n        let m = grid.count\n     \
        \   let n = grid[0].count\n\n        // dp[j][rem] stores the number of paths\
        \ to (current_row, j) with sum % k == rem\n        var dp = Array(repeating:\
        \ Array(repeating: 0, count: k), count: n)\n\n        // Base case: (0, 0)\n\
        \        dp[0][grid[0][0] % k] = 1\n\n        // Fill the first row (i = 0)\n\
        \        for j in 1..<n {\n            let val = grid[0][j]\n            let\
        \ val_rem = val % k\n            for prev_rem in 0..<k {\n                if\
        \ dp[j-1][prev_rem] > 0 {\n                    let current_rem = (prev_rem +\
        \ val_rem) % k\n                    dp[j][current_rem] = (dp[j][current_rem]\
        \ + dp[j-1][prev_rem]) % MOD\n                }\n            }\n        }\n\n\
        \        // Fill subsequent rows (i from 1 to m-1)\n        for i in 1..<m {\n\
        \            // new_dp_row will store counts for the current row i\n       \
        \     var new_dp_row = Array(repeating: Array(repeating: 0, count: k), count:\
        \ n)\n\n            // First cell of current row (i, 0)\n            let val\
        \ = grid[i][0]\n            let val_rem = val % k\n            for prev_rem\
        \ in 0..<k {\n                if dp[0][prev_rem] > 0 { // Paths from (i-1, 0)\n\
        \                    let current_rem = (prev_rem + val_rem) % k\n          \
        \          new_dp_row[0][current_rem] = (new_dp_row[0][current_rem] + dp[0][prev_rem])\
        \ % MOD\n                }\n            }\n\n            // Remaining cells\
        \ of current row (i, j) for j from 1 to n-1\n            for j in 1..<n {\n\
        \                let val = grid[i][j]\n                let val_rem = val % k\n\
        \                for prev_rem in 0..<k {\n                    // Paths from\
        \ (i-1, j)\n                    if dp[j][prev_rem] > 0 {\n                 \
        \       let current_rem = (prev_rem + val_rem) % k\n                       \
        \ new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + dp[j][prev_rem])\
        \ % MOD;\n                    }\n\n                    // Paths from (i, j-1)\n\
        \                    if new_dp_row[j-1][prev_rem] > 0 {\n                  \
        \      let current_rem = (prev_rem + val_rem) % k\n                        new_dp_row[j][current_rem]\
        \ = (new_dp_row[j][current_rem] + new_dp_row[j-1][prev_rem]) % MOD;\n      \
        \              }\n                }\n            }\n\n            dp = new_dp_row\
        \ // Update dp to be the current row for the next iteration\n        }\n\n \
        \       return dp[n-1][0]\n    }\n}"
      kotlin: "class Solution {\n    fun numberOfPaths(grid: Array<IntArray>, k: Int):\
        \ Int {\n        val MOD = 1_000_000_007\n        val m = grid.size\n      \
        \  val n = grid[0].size\n\n        // dp[j][rem] stores the number of paths\
        \ to (current_row, j) with sum % k == rem\n        var dp = Array(n) { IntArray(k)\
        \ { 0 } }\n\n        // Base case: (0, 0)\n        dp[0][grid[0][0] % k] = 1\n\
        \n        // Fill the first row (i = 0)\n        for (j in 1 until n) {\n  \
        \          val val = grid[0][j]\n            val val_rem = val % k\n       \
        \     for (prev_rem in 0 until k) {\n                if (dp[j-1][prev_rem] >\
        \ 0) {\n                    val current_rem = (prev_rem + val_rem) % k\n   \
        \                 dp[j][current_rem] = (dp[j][current_rem] + dp[j-1][prev_rem])\
        \ % MOD\n                }\n            }\n        }\n\n        // Fill subsequent\
        \ rows (i from 1 to m-1)\n        for (i in 1 until m) {\n            // new_dp_row\
        \ will store counts for the current row i\n            val newDpRow = Array(n)\
        \ { IntArray(k) { 0 } }\n\n            // First cell of current row (i, 0)\n\
        \            val val = grid[i][0]\n            val val_rem = val % k\n     \
        \       for (prev_rem in 0 until k) {\n                if (dp[0][prev_rem] >\
        \ 0) { // Paths from (i-1, 0)\n                    val current_rem = (prev_rem\
        \ + val_rem) % k\n                    newDpRow[0][current_rem] = (newDpRow[0][current_rem]\
        \ + dp[0][prev_rem]) % MOD\n                }\n            }\n\n           \
        \ // Remaining cells of current row (i, j) for j from 1 to n-1\n           \
        \ for (j in 1 until n) {\n                val = grid[i][j]\n               \
        \ val_rem = val % k\n                for (prev_rem in 0 until k) {\n       \
        \             // Paths from (i-1, j)\n                    if (dp[j][prev_rem]\
        \ > 0) {\n                        val current_rem = (prev_rem + val_rem) % k\n\
        \                        newDpRow[j][current_rem] = (newDpRow[j][current_rem]\
        \ + dp[j][prev_rem]) % MOD\n                    }\n\n                    //\
        \ Paths from (i, j-1)\n                    if (newDpRow[j-1][prev_rem] > 0)\
        \ {\n                        val current_rem = (prev_rem + val_rem) % k\n  \
        \                      newDpRow[j][current_rem] = (newDpRow[j][current_rem]\
        \ + newDpRow[j-1][prev_rem]) % MOD\n                    }\n                }\n\
        \            }\n\n            dp = newDpRow // Update dp to be the current row\
        \ for the next iteration\n        }\n\n        return dp[n-1][0]\n    }\n}"
      dart: "class Solution {\n  int numberOfPaths(List<List<int>> grid, int k) {\n\
        \    final int MOD = 1000000007;\n    int m = grid.length;\n    int n = grid[0].length;\n\
        \n    // dp[j][rem] stores the number of paths to (current_row, j) with sum\
        \ % k == rem\n    List<List<int>> dp = List.generate(n, (_) => List.filled(k,\
        \ 0));\n\n    // Base case: (0, 0)\n    dp[0][grid[0][0] % k] = 1;\n\n    //\
        \ Fill the first row (i = 0)\n    for (int j = 1; j < n; ++j) {\n      int val\
        \ = grid[0][j];\n      int valRem = val % k;\n      for (int prevRem = 0; prevRem\
        \ < k; ++prevRem) {\n        if (dp[j-1][prevRem] > 0) {\n          int currentRem\
        \ = (prevRem + valRem) % k;\n          dp[j][currentRem] = (dp[j][currentRem]\
        \ + dp[j-1][prevRem]) % MOD;\n        }\n      }\n    }\n\n    // Fill subsequent\
        \ rows (i from 1 to m-1)\n    for (int i = 1; i < m; ++i) {\n      // newDpRow\
        \ will store counts for the current row i\n      List<List<int>> newDpRow =\
        \ List.generate(n, (_) => List.filled(k, 0));\n\n      // First cell of current\
        \ row (i, 0)\n      int val = grid[i][0];\n      int valRem = val % k;\n   \
        \   for (int prevRem = 0; prevRem < k; ++prevRem) {\n        if (dp[0][prevRem]\
        \ > 0) { // Paths from (i-1, 0)\n          int currentRem = (prevRem + valRem)\
        \ % k;\n          newDpRow[0][currentRem] = (newDpRow[0][currentRem] + dp[0][prevRem])\
        \ % MOD;\n        }\n      }\n\n      // Remaining cells of current row (i,\
        \ j) for j from 1 to n-1\n      for (int j = 1; j < n; ++j) {\n        val =\
        \ grid[i][j];\n        valRem = val % k;\n        for (int prevRem = 0; prevRem\
        \ < k; ++prevRem) {\n          // Paths from (i-1, j)\n          if (dp[j][prevRem]\
        \ > 0) {\n            int currentRem = (prevRem + valRem) % k;\n           \
        \ newDpRow[j][currentRem] = (newDpRow[j][currentRem] + dp[j][prevRem]) % MOD;\n\
        \          }\n\n          // Paths from (i, j-1)\n          if (newDpRow[j-1][prevRem]\
        \ > 0) {\n            int currentRem = (prevRem + valRem) % k;\n           \
        \ newDpRow[j][currentRem] = (newDpRow[j][currentRem] + newDpRow[j-1][prevRem])\
        \ % MOD;\n          }\n        }\n      }\n\n      dp = newDpRow; // Update\
        \ dp to be the current row for the next iteration\n    }\n\n    return dp[n-1][0];\n\
        \  }\n}"
      go: "func numberOfPaths(grid [][]int, k int) int {\n    MOD := 1_000_000_007\n\
        \    m := len(grid)\n    n := len(grid[0])\n\n    // dp[j][rem] stores the number\
        \ of paths to (current_row, j) with sum % k == rem\n    dp := make([][]int,\
        \ n)\n    for j := range dp {\n        dp[j] = make([]int, k)\n    }\n\n   \
        \ // Base case: (0, 0)\n    dp[0][grid[0][0]%k] = 1\n\n    // Fill the first\
        \ row (i = 0)\n    for j := 1; j < n; j++ {\n        val := grid[0][j]\n   \
        \     val_rem := val % k\n        for prev_rem := 0; prev_rem < k; prev_rem++\
        \ {\n            if dp[j-1][prev_rem] > 0 {\n                current_rem :=\
        \ (prev_rem + val_rem) % k\n                dp[j][current_rem] = (dp[j][current_rem]\
        \ + dp[j-1][prev_rem]) % MOD\n            }\n        }\n    }\n\n    // Fill\
        \ subsequent rows (i from 1 to m-1)\n    for i := 1; i < m; i++ {\n        //\
        \ new_dp_row will store counts for the current row i\n        new_dp_row :=\
        \ make([][]int, n)\n        for j := range new_dp_row {\n            new_dp_row[j]\
        \ = make([]int, k)\n        }\n\n        // First cell of current row (i, 0)\n\
        \        val := grid[i][0]\n        val_rem := val % k\n        for prev_rem\
        \ := 0; prev_rem < k; prev_rem++ {\n            if dp[0][prev_rem] > 0 { //\
        \ Paths from (i-1, 0)\n                current_rem := (prev_rem + val_rem) %\
        \ k\n                new_dp_row[0][current_rem] = (new_dp_row[0][current_rem]\
        \ + dp[0][prev_rem]) % MOD\n            }\n        }\n\n        // Remaining\
        \ cells of current row (i, j) for j from 1 to n-1\n        for j := 1; j < n;\
        \ j++ {\n            val = grid[i][j]\n            val_rem = val % k\n     \
        \       for prev_rem := 0; prev_rem < k; prev_rem++ {\n                // Paths\
        \ from (i-1, j)\n                if dp[j][prev_rem] > 0 {\n                \
        \    current_rem := (prev_rem + val_rem) % k\n                    new_dp_row[j][current_rem]\
        \ = (new_dp_row[j][current_rem] + dp[j][prev_rem]) % MOD\n                }\n\
        \n                // Paths from (i, j-1)\n                if new_dp_row[j-1][prev_rem]\
        \ > 0 {\n                    current_rem := (prev_rem + val_rem) % k\n     \
        \               new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + new_dp_row[j-1][prev_rem])\
        \ % MOD\n                }\n            }\n        }\n\n        dp = new_dp_row\
        \ // Update dp to be the current row for the next iteration\n    }\n\n    return\
        \ dp[n-1][0]\n}"
      ruby: "class Solution\n    # @param {Integer[][]} grid\n    # @param {Integer}\
        \ k\n    # @return {Integer}\n    def number_of_paths(grid, k)\n        mod\
        \ = 10**9 + 7\n        m = grid.length\n        n = grid[0].length\n\n     \
        \   # dp[j][rem] stores the number of paths to (current_row, j) with sum % k\
        \ == rem\n        dp = Array.new(n) { Array.new(k, 0) }\n\n        # Base case:\
        \ (0, 0)\n        dp[0][grid[0][0] % k] = 1\n\n        # Fill the first row\
        \ (i = 0)\n        (1...n).each do |j|\n            val = grid[0][j]\n     \
        \       val_rem = val % k\n            (0...k).each do |prev_rem|\n        \
        \        if dp[j-1][prev_rem] > 0\n                    current_rem = (prev_rem\
        \ + val_rem) % k\n                    dp[j][current_rem] = (dp[j][current_rem]\
        \ + dp[j-1][prev_rem]) % mod\n                end\n            end\n       \
        \ end\n\n        # Fill subsequent rows (i from 1 to m-1)\n        (1...m).each\
        \ do |i|\n            # new_dp_row will store counts for the current row i\n\
        \            new_dp_row = Array.new(n) { Array.new(k, 0) }\n\n            #\
        \ First cell of current row (i, 0)\n            val = grid[i][0]\n         \
        \   val_rem = val % k\n            (0...k).each do |prev_rem|\n            \
        \    if dp[0][prev_rem] > 0 # Paths from (i-1, 0)\n                    current_rem\
        \ = (prev_rem + val_rem) % k\n                    new_dp_row[0][current_rem]\
        \ = (new_dp_row[0][current_rem] + dp[0][prev_rem]) % mod\n                end\n\
        \            end\n\n            # Remaining cells of current row (i, j) for\
        \ j from 1 to n-1\n            (1...n).each do |j|\n                val = grid[i][j]\n\
        \                val_rem = val % k\n                (0...k).each do |prev_rem|\n\
        \                    # Paths from (i-1, j)\n                    if dp[j][prev_rem]\
        \ > 0\n                        current_rem = (prev_rem + val_rem) % k\n    \
        \                    new_dp_row[j][current_rem] = (new_dp_row[j][current_rem]\
        \ + dp[j][prev_rem]) % mod\n                    end\n\n                    #\
        \ Paths from (i, j-1)\n                    if new_dp_row[j-1][prev_rem] > 0\n\
        \                        current_rem = (prev_rem + val_rem) % k\n          \
        \              new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + new_dp_row[j-1][prev_rem])\
        \ % mod\n                    end\n                end\n            end\n\n \
        \           dp = new_dp_row # Update dp to be the current row for the next iteration\n\
        \        end\n\n        return dp[n-1][0]\n    end\nend"
      scala: "object Solution {\n    def numberOfPaths(grid: Array[Array[Int]], k: Int):\
        \ Int = {\n        val MOD = 1_000_000_007\n        val m = grid.length\n  \
        \      val n = grid(0).length\n\n        // dp(j)(rem) stores the number of\
        \ paths to (current_row, j) with sum % k == rem\n        var dp: Array[Array[Int]]\
        \ = Array.fill(n)(Array.fill(k)(0))\n\n        // Base case: (0, 0)\n      \
        \  dp(0)(grid(0)(0) % k) = 1\n\n        // Fill the first row (i = 0)\n    \
        \    for (j <- 1 until n) {\n            val val_ = grid(0)(j)\n           \
        \ val val_rem = val_ % k\n            for (prev_rem <- 0 until k) {\n      \
        \          if (dp(j-1)(prev_rem) > 0) {\n                    val current_rem\
        \ = (prev_rem + val_rem) % k\n                    dp(j)(current_rem) = (dp(j)(current_rem)\
        \ + dp(j-1)(prev_rem)) % MOD\n                }\n            }\n        }\n\n\
        \        // Fill subsequent rows (i from 1 to m-1)\n        for (i <- 1 until\
        \ m) {\n            // new_dp_row will store counts for the current row i\n\
        \            val new_dp_row: Array[Array[Int]] = Array.fill(n)(Array.fill(k)(0))\n\
        \n            // First cell of current row (i, 0)\n            val val_ = grid(i)(0)\n\
        \            val val_rem = val_ % k\n            for (prev_rem <- 0 until k)\
        \ {\n                if (dp(0)(prev_rem) > 0) { // Paths from (i-1, 0)\n   \
        \                 val current_rem = (prev_rem + val_rem) % k\n             \
        \       new_dp_row(0)(current_rem) = (new_dp_row(0)(current_rem) + dp(0)(prev_rem))\
        \ % MOD\n                }\n            }\n\n            // Remaining cells\
        \ of current row (i, j) for j from 1 to n-1\n            for (j <- 1 until n)\
        \ {\n                val val_curr = grid(i)(j)\n                val val_rem_curr\
        \ = val_curr % k\n                for (prev_rem <- 0 until k) {\n          \
        \          // Paths from (i-1, j)\n                    if (dp(j)(prev_rem) >\
        \ 0) {\n                        val current_rem = (prev_rem + val_rem_curr)\
        \ % k\n                        new_dp_row(j)(current_rem) = (new_dp_row(j)(current_rem)\
        \ + dp(j)(prev_rem)) % MOD\n                    }\n\n                    //\
        \ Paths from (i, j-1)\n                    if (new_dp_row(j-1)(prev_rem) > 0)\
        \ {\n                        val current_rem = (prev_rem + val_rem_curr) % k\n\
        \                        new_dp_row(j)(current_rem) = (new_dp_row(j)(current_rem)\
        \ + new_dp_row(j-1)(prev_rem)) % MOD\n                    }\n              \
        \  }\n            }\n\n            dp = new_dp_row // Update dp to be the current\
        \ row for the next iteration\n        }\n\n        dp(n-1)(0)\n    }\n}"
      rust: "impl Solution {\n    pub fn number_of_paths(grid: Vec<Vec<i32>>, k: i32)\
        \ -> i32 {\n        let modular: i32 = 1_000_000_007;\n        let m = grid.len();\n\
        \        let n = grid[0].len();\n        let k_usize = k as usize;\n\n     \
        \   // dp[j][rem] stores the number of paths to (current_row, j) with sum %\
        \ k == rem\n        let mut dp: Vec<Vec<i32>> = vec![vec![0; k_usize]; n];\n\
        \n        // Base case: (0, 0)\n        dp[0][(grid[0][0] % k) as usize] = 1;\n\
        \n        // Fill the first row (i = 0)\n        for j in 1..n {\n         \
        \   let val = grid[0][j];\n            let val_rem = val % k;\n            for\
        \ prev_rem_idx in 0..k_usize {\n                if dp[j-1][prev_rem_idx] > 0\
        \ {\n                    let current_rem = (prev_rem_idx as i32 + val_rem) %\
        \ k;\n                    dp[j][current_rem as usize] = (dp[j][current_rem as\
        \ usize] + dp[j-1][prev_rem_idx]) % modular;\n                }\n          \
        \  }\n        }\n\n        // Fill subsequent rows (i from 1 to m-1)\n     \
        \   for i in 1..m {\n            // new_dp_row will store counts for the current\
        \ row i\n            let mut new_dp_row: Vec<Vec<i32>> = vec![vec![0; k_usize];\
        \ n];\n\n            // First cell of current row (i, 0)\n            let val\
        \ = grid[i][0];\n            let val_rem = val % k;\n            for prev_rem_idx\
        \ in 0..k_usize {\n                if dp[0][prev_rem_idx] > 0 { // Paths from\
        \ (i-1, 0)\n                    let current_rem = (prev_rem_idx as i32 + val_rem)\
        \ % k;\n                    new_dp_row[0][current_rem as usize] = (new_dp_row[0][current_rem\
        \ as usize] + dp[0][prev_rem_idx]) % modular;\n                }\n         \
        \   }\n\n            // Remaining cells of current row (i, j) for j from 1 to\
        \ n-1\n            for j in 1..n {\n                let val = grid[i][j];\n\
        \                let val_rem = val % k;\n                for prev_rem_idx in\
        \ 0..k_usize {\n                    // Paths from (i-1, j)\n               \
        \     if dp[j][prev_rem_idx] > 0 {\n                        let current_rem\
        \ = (prev_rem_idx as i32 + val_rem) % k;\n                        new_dp_row[j][current_rem\
        \ as usize] = (new_dp_row[j][current_rem as usize] + dp[j][prev_rem_idx]) %\
        \ modular;\n                    }\n\n                    // Paths from (i, j-1)\n\
        \                    if new_dp_row[j-1][prev_rem_idx] > 0 {\n              \
        \          let current_rem = (prev_rem_idx as i32 + val_rem) % k;\n        \
        \                new_dp_row[j][current_rem as usize] = (new_dp_row[j][current_rem\
        \ as usize] + new_dp_row[j-1][prev_rem_idx]) % modular;\n                  \
        \  }\n                }\n            }\n\n            dp = new_dp_row; // Update\
        \ dp to be the current row for the next iteration\n        }\n\n        dp[n-1][0]\
        \ as i32\n    }\n}"
      racket: "#lang racket\n(define (number-of-paths grid k)\n  (define MOD 1000000007)\n\
        \  (define m (vector-length grid))\n  (define n (vector-length (vector-ref grid\
        \ 0)))\n\n  ;; dp[j][rem] stores the number of paths to (current_row, j) with\
        \ sum % k == rem\n  (define dp (build-vector n (lambda (j) (build-vector k (lambda\
        \ (rem) 0)))))\n\n  ;; Base case: (0, 0)\n  (vector-set! (vector-ref dp 0) (modulo\
        \ (vector-ref (vector-ref grid 0) 0) k) 1)\n\n  ;; Fill the first row (i = 0)\n\
        \  (for ([j (in-range 1 n)])\n    (define val (vector-ref (vector-ref grid 0)\
        \ j))\n    (define val-rem (modulo val k))\n    (for ([prev-rem (in-range 0\
        \ k)])\n      (when (> (vector-ref (vector-ref dp (- j 1)) prev-rem) 0)\n  \
        \      (define current-rem (modulo (+ prev-rem val-rem) k))\n        (vector-set!\
        \ (vector-ref dp j) current-rem\n                     (modulo (+ (vector-ref\
        \ (vector-ref dp j) current-rem)\n                                (vector-ref\
        \ (vector-ref dp (- j 1)) prev-rem))\n                             MOD)))))\n\
        \n  ;; Fill subsequent rows (i from 1 to m-1)\n  (for ([i (in-range 1 m)])\n\
        \    ;; new-dp-row will store counts for the current row i\n    (define new-dp-row\
        \ (build-vector n (lambda (j) (build-vector k (lambda (rem) 0)))))\n\n    ;;\
        \ First cell of current row (i, 0)\n    (define val (vector-ref (vector-ref\
        \ grid i) 0))\n    (define val-rem (modulo val k))\n    (for ([prev-rem (in-range\
        \ 0 k)])\n      (when (> (vector-ref (vector-ref dp 0) prev-rem) 0) ;; Paths\
        \ from (i-1, 0)\n        (define current-rem (modulo (+ prev-rem val-rem) k))\n\
        \        (vector-set! (vector-ref new-dp-row 0) current-rem\n              \
        \       (modulo (+ (vector-ref (vector-ref new-dp-row 0) current-rem)\n    \
        \                            (vector-ref (vector-ref dp 0) prev-rem))\n    \
        \                         MOD))))\n\n    ;; Remaining cells of current row (i,\
        \ j) for j from 1 to n-1\n    (for ([j (in-range 1 n)])\n      (define val (vector-ref\
        \ (vector-ref grid i) j))\n      (define val-rem (modulo val k))\n      (for\
        \ ([prev-rem (in-range 0 k)])\n        ;; Paths from (i-1, j)\n        (when\
        \ (> (vector-ref (vector-ref dp j) prev-rem) 0)\n          (define current-rem\
        \ (modulo (+ prev-rem val-rem) k))\n          (vector-set! (vector-ref new-dp-row\
        \ j) current-rem\n                       (modulo (+ (vector-ref (vector-ref\
        \ new-dp-row j) current-rem)\n                                  (vector-ref\
        \ (vector-ref dp j) prev-rem))\n                               MOD)))\n\n  \
        \      ;; Paths from (i, j-1)\n        (when (> (vector-ref (vector-ref new-dp-row\
        \ (- j 1)) prev-rem) 0)\n          (define current-rem (modulo (+ prev-rem val-rem)\
        \ k))\n          (vector-set! (vector-ref new-dp-row j) current-rem\n      \
        \                 (modulo (+ (vector-ref (vector-ref new-dp-row j) current-rem)\n\
        \                                  (vector-ref (vector-ref new-dp-row (- j 1))\
        \ prev-rem))\n                               MOD)))))\n\n    (set! dp new-dp-row)\
        \ ;; Update dp to be the current row for the next iteration\n    )\n\n  (vector-ref\
        \ (vector-ref dp (- n 1)) 0))"
      erlang: "-module(solution).\n-export([number_of_paths/2]).\n\nnumber_of_paths(Grid,\
        \ K) ->\n    MOD = 1000000007,\n    M = length(Grid),\n    N = length(hd(Grid)),\n\
        \n    % dp[j][rem] stores the number of paths to (current_row, j) with sum %\
        \ K == rem\n    % Represent dp as a list of lists (vectors in other languages)\n\
        \    Dp = lists:duplicate(N, lists:duplicate(K, 0)),\n\n    % Base case: (0,\
        \ 0)\n    Grid00 = hd(hd(Grid)),\n    Dp1 = set_in_list_of_lists(Dp, 0, Grid00\
        \ rem K, 1),\n\n    % Fill the first row (i = 0)\n    Dp2 = lists:foldl(fun(J,\
        \ CurrentDp) ->\n        Val = lists:nth(J + 1, hd(Grid)),\n        ValRem =\
        \ Val rem K,\n        lists:foldl(fun(PrevRem, InnerDp) ->\n            PrevCount\
        \ = get_in_list_of_lists(InnerDp, J - 1, PrevRem),\n            if PrevCount\
        \ > 0 ->\n                CurrentRem = (PrevRem + ValRem) rem K,\n         \
        \       set_in_list_of_lists(InnerDp, J, CurrentRem, (get_in_list_of_lists(InnerDp,\
        \ J, CurrentRem) + PrevCount) rem MOD)\n            else\n                InnerDp\n\
        \            end\n        end, CurrentDp, lists:seq(0, K - 1))\n    end, Dp1,\
        \ lists:seq(1, N - 1)),\n\n    % Fill subsequent rows (i from 1 to M-1)\n  \
        \  FinalDp = lists:foldl(fun(I, CurrentDp) ->\n        % new_dp_row will store\
        \ counts for the current row I\n        NewDpRow = lists:duplicate(N, lists:duplicate(K,\
        \ 0)),\n\n        % First cell of current row (I, 0)\n        ValI0 = lists:nth(1,\
        \ lists:nth(I + 1, Grid)),\n        ValRemI0 = ValI0 rem K,\n        NewDpRow1\
        \ = lists:foldl(fun(PrevRem, InnerNewDpRow) ->\n            PrevCount = get_in_list_of_lists(CurrentDp,\
        \ 0, PrevRem),\n            if PrevCount > 0 -> % Paths from (I-1, 0)\n    \
        \            CurrentRem = (PrevRem + ValRemI0) rem K,\n                set_in_list_of_lists(InnerNewDpRow,\
        \ 0, CurrentRem, (get_in_list_of_lists(InnerNewDpRow, 0, CurrentRem) + PrevCount)\
        \ rem MOD)\n            else\n                InnerNewDpRow\n            end\n\
        \        end, NewDpRow, lists:seq(0, K - 1)),\n\n        % Remaining cells of\
        \ current row (I, J) for J from 1 to N-1\n        lists:foldl(fun(J, InnerNewDpRow)\
        \ ->\n            ValIJ = lists:nth(J + 1, lists:nth(I + 1, Grid)),\n      \
        \      ValRemIJ = ValIJ rem K,\n            lists:foldl(fun(PrevRem, DeepestNewDpRow)\
        \ ->\n                % Paths from (I-1, J)\n                PrevCountFromAbove\
        \ = get_in_list_of_lists(CurrentDp, J, PrevRem),\n                TempDpRow1\
        \ = if PrevCountFromAbove > 0 ->\n                    CurrentRem = (PrevRem\
        \ + ValRemIJ) rem K,\n                    set_in_list_of_lists(DeepestNewDpRow,\
        \ J, CurrentRem, (get_in_list_of_lists(DeepestNewDpRow, J, CurrentRem) + PrevCountFromAbove)\
        \ rem MOD)\n                else\n                    DeepestNewDpRow\n    \
        \            end,\n\n                % Paths from (I, J-1)\n               \
        \ PrevCountFromLeft = get_in_list_of_lists(DeepestNewDpRow, J - 1, PrevRem),\n\
        \                if PrevCountFromLeft > 0 ->\n                    CurrentRem\
        \ = (PrevRem + ValRemIJ) rem K,\n                    set_in_list_of_lists(TempDpRow1,\
        \ J, CurrentRem, (get_in_list_of_lists(TempDpRow1, J, CurrentRem) + PrevCountFromLeft)\
        \ rem MOD)\n                else\n                    TempDpRow1\n         \
        \       end\n            end, InnerNewDpRow, lists:seq(0, K - 1))\n        end,\
        \ NewDpRow1, lists:seq(1, N - 1))\n    end, Dp2, lists:seq(1, M - 1)),\n\n \
        \   get_in_list_of_lists(FinalDp, N - 1, 0).\n\n% Helper function to get a value\
        \ from a list of lists (0-indexed)\nget_in_list_of_lists(ListOfLists, RowIdx,\
        \ ColIdx) ->\n    lists:nth(ColIdx + 1, lists:nth(RowIdx + 1, ListOfLists)).\n\
        \n% Helper function to set a value in a list of lists (0-indexed)\nset_in_list_of_lists(ListOfLists,\
        \ RowIdx, ColIdx, Value) ->\n    Row = lists:nth(RowIdx + 1, ListOfLists),\n\
        \    NewRow = set_in_list(Row, ColIdx, Value),\n    set_in_list(ListOfLists,\
        \ RowIdx, NewRow).\n\n% Helper function to set a value in a list (0-indexed)\n\
        set_in_list(List, Index, Value) ->\n    lists:replace_nth(Index + 1, Value,\
        \ List)."
      elixir: "defmodule Solution do\n  @mod 1_000_000_007\n\n  @spec number_of_paths(grid\
        \ :: [[integer]], k :: integer) :: integer\n  def number_of_paths(grid, k) do\n\
        \    m = length(grid)\n    n = length(hd(grid))\n\n    # dp[j][rem] stores the\
        \ number of paths to (current_row, j) with sum % k == rem\n    # Represent dp\
        \ as a list of lists (vectors in other languages)\n    dp = List.duplicate(n,\
        \ List.duplicate(k, 0))\n\n    # Base case: (0, 0)\n    grid_0_0 = hd(hd(grid))\n\
        \    dp = put_in_list_of_lists(dp, 0, rem(grid_0_0, k), 1)\n\n    # Fill the\
        \ first row (i = 0)\n    dp = Enum.reduce(1..(n - 1), dp, fn j, current_dp ->\n\
        \      val = Enum.at(hd(grid), j)\n      val_rem = rem(val, k)\n      Enum.reduce(0..(k\
        \ - 1), current_dp, fn prev_rem, inner_dp ->\n        prev_count = get_in_list_of_lists(inner_dp,\
        \ j - 1, prev_rem)\n        if prev_count > 0 do\n          current_rem = rem(prev_rem\
        \ + val_rem, k)\n          put_in_list_of_lists(inner_dp, j, current_rem, rem(get_in_list_of_lists(inner_dp,\
        \ j, current_rem) + prev_count, @mod))\n        else\n          inner_dp\n \
        \       end\n      end)\n    end)\n\n    # Fill subsequent rows (i from 1 to\
        \ m-1)\n    final_dp = Enum.reduce(1..(m - 1), dp, fn i, current_dp ->\n   \
        \   # new_dp_row will store counts for the current row i\n      new_dp_row =\
        \ List.duplicate(n, List.duplicate(k, 0))\n\n      # First cell of current row\
        \ (i, 0)\n      val_i_0 = Enum.at(Enum.at(grid, i), 0)\n      val_rem_i_0 =\
        \ rem(val_i_0, k)\n      new_dp_row = Enum.reduce(0..(k - 1), new_dp_row, fn\
        \ prev_rem, inner_new_dp_row ->\n        prev_count = get_in_list_of_lists(current_dp,\
        \ 0, prev_rem)\n        if prev_count > 0 do # Paths from (i-1, 0)\n       \
        \   current_rem = rem(prev_rem + val_rem_i_0, k)\n          put_in_list_of_lists(inner_new_dp_row,\
        \ 0, current_rem, rem(get_in_list_of_lists(inner_new_dp_row, 0, current_rem)\
        \ + prev_count, @mod))\n        else\n          inner_new_dp_row\n        end\n\
        \      end)\n\n      # Remaining cells of current row (i, j) for j from 1 to\
        \ n-1\n      Enum.reduce(1..(n - 1), new_dp_row, fn j, inner_new_dp_row ->\n\
        \        val_i_j = Enum.at(Enum.at(grid, i), j)\n        val_rem_i_j = rem(val_i_j,\
        \ k)\n        Enum.reduce(0..(k - 1), inner_new_dp_row, fn prev_rem, deepest_new_dp_row\
        \ ->\n          # Paths from (i-1, j)\n          prev_count_from_above = get_in_list_of_lists(current_dp,\
        \ j, prev_rem)\n          temp_dp_row_1 = if prev_count_from_above > 0 do\n\
        \            current_rem = rem(prev_rem + val_rem_i_j, k)\n            put_in_list_of_lists(deepest_new_dp_row,\
        \ j, current_rem, rem(get_in_list_of_lists(deepest_new_dp_row, j, current_rem)\
        \ + prev_count_from_above, @mod))\n          else\n            deepest_new_dp_row\n\
        \          end\n\n          # Paths from (i, j-1)\n          prev_count_from_left\
        \ = get_in_list_of_lists(temp_dp_row_1, j - 1, prev_rem)\n          if prev_count_from_left\
        \ > 0 do\n            current_rem = rem(prev_rem + val_rem_i_j, k)\n       \
        \     put_in_list_of_lists(temp_dp_row_1, j, current_rem, rem(get_in_list_of_lists(temp_dp_row_1,\
        \ j, current_rem) + prev_count_from_left, @mod))\n          else\n         \
        \   temp_dp_row_1\n          end\n        end)\n      end)\n    end)\n\n   \
        \ get_in_list_of_lists(final_dp, n - 1, 0)\n  end\n\n  # Helper function to\
        \ get a value from a list of lists (0-indexed)\n  defp get_in_list_of_lists(list_of_lists,\
        \ row_idx, col_idx) do\n    list_of_lists\n    |> Enum.at(row_idx)\n    |> Enum.at(col_idx)\n\
        \  end\n\n  # Helper function to set a value in a list of lists (0-indexed)\n\
        \  defp put_in_list_of_lists(list_of_lists, row_idx, col_idx, value) do\n  \
        \  list_of_lists\n    |> List.update_at(row_idx, fn row ->\n      List.update_at(row,\
        \ col_idx, fn _ -> value end)\n    end)\n  end\nend"
    approach: 'The problem asks for the number of paths from (0,0) to (m-1, n-1) with
      a sum divisible by k, moving only down or right. This is a classic dynamic programming
      problem. We define dp[i][j][rem] as the number of paths from (0,0) to cell (i,j)
      such that the sum of elements along the path has a remainder rem when divided
      by k. The base case is dp[0][0][grid[0][0] % k] = 1. For any other cell (i,j),
      a path can reach it either from (i-1, j) (moving down) or (i, j-1) (moving right).
      If a path to (i-1, j) had a sum remainder prev_rem_up, and grid[i][j] has remainder
      val_rem = grid[i][j] % k, then the new path to (i,j) will have remainder (prev_rem_up
      + val_rem) % k. Similarly for paths from (i, j-1). Thus, dp[i][j][current_rem]
      is the sum of dp[i-1][j][(current_rem - val_rem + k) % k] and dp[i][j-1][(current_rem
      - val_rem + k) % k], all modulo 10^9 + 7.

      To optimize space, we observe that dp[i][j] only depends on values from the previous
      row (i-1) and the current row (i) but previous column (j-1). This allows us to
      reduce the space complexity from O(m * n * k) to O(n * k) by only storing the
      DP states for the current and previous rows. We iterate through rows i from 0
      to m-1. For each row i, we compute new_dp_row[j][rem] based on dp[j][rem] (from
      (i-1, j)) and new_dp_row[j-1][rem] (from (i, j-1)). After processing a row, new_dp_row
      becomes the dp for the next iteration. The final answer is dp[n-1][0], representing
      paths to the bottom-right corner (m-1, n-1) with a sum remainder of 0.'
    time_complexity: The time complexity is O(m * n * k). We iterate through each of
      the m rows and n columns. For each cell (i, j), we iterate k times (for each possible
      remainder) to update its DP states. Given m * n <= 5 * 10^4 and k <= 50, the total
      operations are at most 5 * 10^4 * 50 = 2.5 * 10^6, which is efficient enough.
    space_complexity: The space complexity is O(n * k). We use two 2D arrays, `dp` and
      `new_dp_row`, each of size n * k, to store the DP states for the current and previous
      rows. This is because the calculation for the current row only depends on the
      previous row and already computed values in the current row. Given n <= 5 * 10^4
      and k <= 50, the space required is at most 5 * 10^4 * 50 * sizeof(int), which
      is approximately 10MB, well within typical memory limits.
    elapsed_time: 164.07619738578796
    model: gemini-2.5-flash
    generated_at: '2025-11-26 01:06:20 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int numberOfPaths(vector<vector<int>>& grid,\
        \ int k) {\n        int m = grid.size(), n = grid[0].size();\n        vector<vector<vector<int>>>\
        \ dp(m, vector<vector<int>>(n, vector<int>(k, 0)));\n        dp[0][0][grid[0][0]\
        \ % k] = 1;\n        for (int i = 0; i < m; i++) {\n            for (int j =\
        \ 0; j < n; j++) {\n                if (i == 0 && j == 0) continue;\n      \
        \          for (int val = 0; val < k; val++) {\n                    if (i >\
        \ 0) dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val];\n                \
        \    if (j > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i][j-1][val];\n     \
        \           }\n            }\n        }\n        return dp[m-1][n-1][0];\n \
        \   }\n};"
      java: "class Solution {\n    public int numberOfPaths(int[][] grid, int k) {\n\
        \        int m = grid.length, n = grid[0].length;\n        int[][][] dp = new\
        \ int[m][n][k];\n        dp[0][0][grid[0][0] % k] = 1;\n        for (int i =\
        \ 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n            \
        \    if (i == 0 && j == 0) continue;\n                for (int val = 0; val\
        \ < k; val++) {\n                    if (i > 0) dp[i][j][(val + grid[i][j])\
        \ % k] += dp[i-1][j][val];\n                    if (j > 0) dp[i][j][(val + grid[i][j])\
        \ % k] += dp[i][j-1][val];\n                }\n            }\n        }\n  \
        \      return dp[m-1][n-1][0];\n    }\n}"
      python: "class Solution:\n    def numberOfPaths(self, grid: List[List[int]], k:\
        \ int) -> int:\n        m, n = len(grid), len(grid[0])\n        dp = [[[0]*k\
        \ for _ in range(n)] for _ in range(m)]\n        dp[0][0][grid[0][0] % k] =\
        \ 1\n        for i in range(m):\n            for j in range(n):\n          \
        \      if i == 0 and j == 0: continue\n                for val in range(k):\n\
        \                    if i > 0: dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val]\n\
        \                    if j > 0: dp[i][j][(val + grid[i][j]) % k] += dp[i][j-1][val]\n\
        \        return dp[m-1][n-1][0]"
      python3: "class Solution:\n    def numberOfPaths(self, grid: List[List[int]],\
        \ k: int) -> int:\n        m, n = len(grid), len(grid[0])\n        dp = [[[0]*k\
        \ for _ in range(n)] for _ in range(m)]\n        dp[0][0][grid[0][0] % k] =\
        \ 1\n        for i in range(m):\n            for j in range(n):\n          \
        \      if i == 0 and j == 0: continue\n                for val in range(k):\n\
        \                    if i > 0: dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val]\n\
        \                    if j > 0: dp[i][j][(val + grid[i][j]) % k] += dp[i][j-1][val]\n\
        \        return dp[m-1][n-1][0]"
      c: "typedef struct {\n    int** grid;\n    int gridSize;\n    int* gridColSize;\n\
        } Solution;\n\nint numberOfPaths(int** grid, int gridSize, int* gridColSize,\
        \ int k) {\n    int m = gridSize, n = gridColSize[0];\n    int*** dp = (int***)malloc(m\
        \ * sizeof(int**));\n    for (int i = 0; i < m; i++) {\n        dp[i] = (int**)malloc(n\
        \ * sizeof(int*));\n        for (int j = 0; j < n; j++) {\n            dp[i][j]\
        \ = (int*)malloc(k * sizeof(int));\n        }\n    }\n    dp[0][0][grid[0][0]\
        \ % k] = 1;\n    for (int i = 0; i < m; i++) {\n        for (int j = 0; j <\
        \ n; j++) {\n            if (i == 0 && j == 0) continue;\n            for (int\
        \ val = 0; val < k; val++) {\n                if (i > 0) dp[i][j][(val + grid[i][j])\
        \ % k] += dp[i-1][j][val];\n                if (j > 0) dp[i][j][(val + grid[i][j])\
        \ % k] += dp[i][j-1][val];\n            }\n        }\n    }\n    int res = dp[m-1][n-1][0];\n\
        \    for (int i = 0; i < m; i++) {\n        for (int j = 0; j < n; j++) {\n\
        \            free(dp[i][j]);\n        }\n        free(dp[i]);\n    }\n    free(dp);\n\
        \    return res;\n}"
      csharp: "public class Solution {\n    public int NumberOfPaths(int[][] grid, int\
        \ k) {\n        int m = grid.Length, n = grid[0].Length;\n        int[,,] dp\
        \ = new int[m, n, k];\n        dp[0, 0, grid[0][0] % k] = 1;\n        for (int\
        \ i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n        \
        \        if (i == 0 && j == 0) continue;\n                for (int val = 0;\
        \ val < k; val++) {\n                    if (i > 0) dp[i, j, (val + grid[i][j])\
        \ % k] += dp[i-1, j, val];\n                    if (j > 0) dp[i, j, (val + grid[i][j])\
        \ % k] += dp[i, j-1, val];\n                }\n            }\n        }\n  \
        \      return dp[m-1, n-1, 0];\n    }\n}"
      javascript: "var numberOfPaths = function(grid, k) {\n    let m = grid.length,\
        \ n = grid[0].length;\n    let dp = Array(m).fill().map(() => Array(n).fill().map(()\
        \ => Array(k).fill(0)));\n    dp[0][0][grid[0][0] % k] = 1;\n    for (let i\
        \ = 0; i < m; i++) {\n        for (let j = 0; j < n; j++) {\n            if\
        \ (i == 0 && j == 0) continue;\n            for (let val = 0; val < k; val++)\
        \ {\n                if (i > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val];\n\
        \                if (j > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i][j-1][val];\n\
        \            }\n        }\n    }\n    return dp[m-1][n-1][0];\n};"
      typescript: "function numberOfPaths(grid: number[][], k: number): number {\n \
        \   let m: number = grid.length, n: number = grid[0].length;\n    let dp: number[][][]\
        \ = Array(m).fill().map(() => Array(n).fill().map(() => Array(k).fill(0)));\n\
        \    dp[0][0][grid[0][0] % k] = 1;\n    for (let i: number = 0; i < m; i++)\
        \ {\n        for (let j: number = 0; j < n; j++) {\n            if (i == 0 &&\
        \ j == 0) continue;\n            for (let val: number = 0; val < k; val++) {\n\
        \                if (i > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val];\n\
        \                if (j > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i][j-1][val];\n\
        \            }\n        }\n    }\n    return dp[m-1][n-1][0];\n}"
      php: "class Solution {\n    function numberOfPaths($grid, $k) {\n        $m =\
        \ count($grid);\n        $n = count($grid[0]);\n        $dp = array_fill(0,\
        \ $m, array_fill(0, $n, array_fill(0, $k, 0)));\n        $dp[0][0][$grid[0][0]\
        \ % $k] = 1;\n        for ($i = 0; $i < $m; $i++) {\n            for ($j = 0;\
        \ $j < $n; $j++) {\n                if ($i == 0 && $j == 0) continue;\n    \
        \            for ($val = 0; $val < $k; $val++) {\n                    if ($i\
        \ > 0) $dp[$i][$j][($val + $grid[$i][$j]) % $k] += $dp[$i-1][$j][$val];\n  \
        \                  if ($j > 0) $dp[$i][$j][($val + $grid[$i][$j]) % $k] += $dp[$i][$j-1][$val];\n\
        \                }\n            }\n        }\n        return $dp[$m-1][$n-1][0];\n\
        \    }\n}"
      swift: "class Solution {\n    func numberOfPaths(_ grid: [[Int]], _ k: Int) ->\
        \ Int {\n        let m = grid.count\n        let n = grid[0].count\n       \
        \ var dp = Array(repeating: Array(repeating: Array(repeating: 0, count: k),\
        \ count: n), count: m)\n        dp[0][0][grid[0][0] % k] = 1\n        for i\
        \ in 0..<m {\n            for j in 0..<n {\n                if i == 0 && j ==\
        \ 0 { continue }\n                for val in 0..<k {\n                    if\
        \ i > 0 { dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val] }\n          \
        \          if j > 0 { dp[i][j][(val + grid[i][j]) % k] += dp[i][j-1][val] }\n\
        \                }\n            }\n        }\n        return dp[m-1][n-1][0]\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun numberOfPaths(grid: Array<IntArray>, k: Int):\
        \ Int {\n        val m = grid.size\n        val n = grid[0].size\n        val\
        \ dp = Array(m) { Array(n) { IntArray(k) } }\n        dp[0][0][grid[0][0] %\
        \ k] = 1\n        for (i in 0 until m) {\n            for (j in 0 until n) {\n\
        \                if (i == 0 && j == 0) continue\n                for (val in\
        \ 0 until k) {\n                    if (i > 0) dp[i][j][(val + grid[i][j]) %\
        \ k] += dp[i-1][j][val]\n                    if (j > 0) dp[i][j][(val + grid[i][j])\
        \ % k] += dp[i][j-1][val]\n                }\n            }\n        }\n   \
        \     return dp[m-1][n-1][0]\n    }\n}"
      dart: "class Solution {\n    int numberOfPaths(List<List<int>> grid, int k) {\n\
        \        int m = grid.length, n = grid[0].length;\n        List<List<List<int>>>\
        \ dp = List.generate(m, (i) => List.generate(n, (j) => List.generate(k, (k)\
        \ => 0)));\n        dp[0][0][grid[0][0] % k] = 1;\n        for (int i = 0; i\
        \ < m; i++) {\n            for (int j = 0; j < n; j++) {\n                if\
        \ (i == 0 && j == 0) continue;\n                for (int val = 0; val < k; val++)\
        \ {\n                    if (i > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val];\n\
        \                    if (j > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i][j-1][val];\n\
        \                }\n            }\n        }\n        return dp[m-1][n-1][0];\n\
        \    }\n}"
      go: "func numberOfPaths(grid [][]int, k int) int {\n    m, n := len(grid), len(grid[0])\n\
        \    dp := make([][][]int, m)\n    for i := range dp {\n        dp[i] = make([][]int,\
        \ n)\n        for j := range dp[i] {\n            dp[i][j] = make([]int, k)\n\
        \        }\n    }\n    dp[0][0][grid[0][0]%k] = 1\n    for i := 0; i < m; i++\
        \ {\n        for j := 0; j < n; j++ {\n            if i == 0 && j == 0 { continue\
        \ }\n            for val := 0; val < k; val++ {\n                if i > 0 {\
        \ dp[i][j][(val+grid[i][j])%k] += dp[i-1][j][val] }\n                if j >\
        \ 0 { dp[i][j][(val+grid[i][j])%k] += dp[i][j-1][val] }\n            }\n   \
        \     }\n    }\n    return dp[m-1][n-1][0]\n}"
      ruby: "def number_of_paths(grid, k)\n    m, n = grid.size, grid[0].size\n    dp\
        \ = Array.new(m) { Array.new(n) { Array.new(k, 0) } }\n    dp[0][0][grid[0][0]\
        \ % k] = 1\n    (0...m).each do |i|\n        (0...n).each do |j|\n         \
        \   next if i == 0 && j == 0\n            (0...k).each do |val|\n          \
        \      if i > 0\n                    dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val]\n\
        \                end\n                if j > 0\n                    dp[i][j][(val\
        \ + grid[i][j]) % k] += dp[i][j-1][val]\n                end\n            end\n\
        \        end\n    end\n    dp[m-1][n-1][0]\nend"
      scala: "object Solution {\n    def numberOfPaths(grid: Array[Array[Int]], k: Int):\
        \ Int = {\n        val m = grid.length\n        val n = grid(0).length\n   \
        \     val dp = Array.ofDim[Int](m, n, k)\n        dp(0)(0)(grid(0)(0) % k) =\
        \ 1\n        for (i <- 0 until m) {\n            for (j <- 0 until n) {\n  \
        \              if (i == 0 && j == 0) {\n                    // do nothing\n\
        \                } else {\n                    for (val <- 0 until k) {\n  \
        \                      if (i > 0) dp(i)(j)((val + grid(i)(j)) % k) += dp(i-1)(j)(val)\n\
        \                        if (j > 0) dp(i)(j)((val + grid(i)(j)) % k) += dp(i)(j-1)(val)\n\
        \                    }\n                }\n            }\n        }\n      \
        \  dp(m-1)(n-1)(0)\n    }\n}"
      rust: "struct Solution;\nimpl Solution {\n    pub fn number_of_paths(grid: Vec<Vec<i32>>,\
        \ k: i32) -> i32 {\n        let m = grid.len() as usize;\n        let n = grid[0].len()\
        \ as usize;\n        let mut dp: Vec<Vec<Vec<i32>>> = vec![vec![vec![0; k as\
        \ usize]; n]; m];\n        dp[0][0][grid[0][0] as usize % k as usize] = 1;\n\
        \        for i in 0..m {\n            for j in 0..n {\n                if i\
        \ == 0 && j == 0 { continue; }\n                for val in 0..k {\n        \
        \            if i > 0 { dp[i][j][(val + grid[i][j]) as usize % k as usize] +=\
        \ dp[i-1][j][val as usize]; }\n                    if j > 0 { dp[i][j][(val\
        \ + grid[i][j]) as usize % k as usize] += dp[i][j-1][val as usize]; }\n    \
        \            }\n            }\n        }\n        dp[m-1][n-1][0]\n    }\n}"
      racket: "define (number-of-paths grid k)\n    (let* (\n        (m (length grid))\n\
        \        (n (length (car grid)))\n        (dp (make-array m n k)))\n       \
        \ (array-set! dp 0 0 (modulo (array-ref grid 0 0) k) 1)\n        (for* (\n \
        \           (i (range m))\n            (j (range n)))\n            (when (not\
        \ (and (= i 0) (= j 0)))\n                (for (\n                    (val (range\
        \ k)))\n                    (when (> i 0)\n                        (array-set!\
        \ dp i j (modulo (+ val (array-ref grid i j)) k) (+ (array-ref dp i j (modulo\
        \ (+ val (array-ref grid i j)) k)) (array-ref dp (- i 1) j val))))\n       \
        \             (when (> j 0)\n                        (array-set! dp i j (modulo\
        \ (+ val (array-ref grid i j)) k) (+ (array-ref dp i j (modulo (+ val (array-ref\
        \ grid i j)) k)) (array-ref dp i (- j 1) val))))))\n        (array-ref dp (-\
        \ m 1) (- n 1) 0))"
      erlang: "number_of_paths(Grid, K) ->\n    M = length(Grid),\n    N = length(hd(Grid)),\n\
        \    DP = array:new([M, N, K], 0),\n    array:set(0, 0, (element(1, hd(Grid))\
        \ rem K), 1, DP),\n    number_of_paths(M, N, Grid, K, DP, 0, 0).\n\nnumber_of_paths(M,\
        \ N, Grid, K, DP, I, J) when I < M, J < N ->\n    case {I, J} of\n        {0,\
        \ 0} -> number_of_paths(M, N, Grid, K, DP, I, J + 1);\n        _ ->\n      \
        \      lists:foreach(fun(Val) ->\n                case I > 0 of\n          \
        \          true ->\n                        NewVal = (Val + element(I, element(J,\
        \ Grid)) rem K),\n                        array:set(I, J, NewVal, array:get(I,\
        \ J, NewVal) + array:get(I - 1, J, Val), DP);\n                    false ->\
        \ ok\n                end,\n                case J > 0 of\n                \
        \    true ->\n                        NewVal = (Val + element(I, element(J,\
        \ Grid)) rem K),\n                        array:set(I, J, NewVal, array:get(I,\
        \ J, NewVal) + array:get(I, J - 1, Val), DP);\n                    false ->\
        \ ok\n                end\n            end, lists:seq(0, K - 1)),\n        \
        \    number_of_paths(M, N, Grid, K, DP, I + 1, 0)\n    end;\nnumber_of_paths(M,\
        \ N, Grid, K, DP, I, J) when I == M, J == N ->\n    array:get(M - 1, N - 1,\
        \ 0, DP)."
      elixir: "def number_of_paths(grid, k) do\n    m = length(grid)\n    n = length(Enum.at(grid,\
        \ 0))\n    dp = :array.new([m, n, k], 0)\n    :array.set(0, 0, rem(Enum.at(Enum.at(grid,\
        \ 0), 0), k), 1, dp)\n    number_of_paths(m, n, grid, k, dp, 0, 0)\nend\n\n\
        defp number_of_paths(m, n, grid, k, dp, i, j) when i < m and j < n do\n    case\
        \ {i, j} do\n        {0, 0} -> number_of_paths(m, n, grid, k, dp, i, j + 1)\n\
        \        _ ->\n            Enum.each(0..(k - 1), fn val ->\n               \
        \ new_val = rem(val + Enum.at(Enum.at(grid, i), j), k)\n                :array.set(i,\
        \ j, new_val, :array.get(i, j, new_val) + :array.get(i - 1, j, val), dp)\n \
        \               :array.set(i, j, new_val, :array.get(i, j, new_val) + :array.get(i,\
        \ j - 1, val), dp)\n            end)\n            number_of_paths(m, n, grid,\
        \ k, dp, i + 1, 0)\n    end\nend\n\ndefp number_of_paths(m, n, grid, k, dp,\
        \ i, j) when i == m and j == n do\n    :array.get(m - 1, n - 1, 0, dp)\nend"
    approach: The problem can be solved using dynamic programming. The key intuition
      is to consider the remainders of the sum of elements on the path when divided
      by k. We can use a 3D DP array, dp, where dp[i][j][value] represents the number
      of paths from the top-left cell to the cell at position (i, j) such that the sum
      of elements on the path has a remainder of value when divided by k. We can fill
      up this DP array by iterating over each cell in the grid and considering the possible
      paths that can reach that cell. The final answer will be stored in dp[m-1][n-1][0],
      where m and n are the number of rows and columns in the grid, respectively. The
      actual numbers in the grid do not matter, what matters are the remainders when
      divided by k, so we can use the modulo operator to simplify the problem.
    time_complexity: The time complexity of this solution is O(m*n*k), where m and n
      are the number of rows and columns in the grid, respectively, and k is the divisor.
      This is because we need to fill up the 3D DP array, which has a size of m*n*k.
    space_complexity: The space complexity of this solution is also O(m*n*k), as we
      need to store the 3D DP array. However, we can optimize the space complexity by
      using a 2D DP array and iterating over the rows and columns of the grid, instead
      of storing the entire 3D array.
    elapsed_time: 11.727733850479126
    model: llama-3.3-70b-versatile
    generated_at: '2025-11-26 01:06:31 '
---

## Problem #2435: Paths in Matrix Whose Sum Is Divisible by K

**Difficulty:** Hard

**Topics:** Array, Dynamic Programming, Matrix

## Problem Description

<p>You are given a <strong>0-indexed</strong> <code>m x n</code> integer matrix <code>grid</code> and an integer <code>k</code>. You are currently at position <code>(0, 0)</code> and you want to reach position <code>(m - 1, n - 1)</code> moving only <strong>down</strong> or <strong>right</strong>.</p>

<p>Return<em> the number of paths where the sum of the elements on the path is divisible by </em><code>k</code>. Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2022/08/13/image-20220813183124-1.png" style="width: 437px; height: 200px;" />
<pre>
<strong>Input:</strong> grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two paths where the sum of the elements on the path is divisible by k.
The first path highlighted in red has a sum of 5 + 2 + 4 + 5 + 2 = 18 which is divisible by 3.
The second path highlighted in blue has a sum of 5 + 3 + 0 + 5 + 2 = 15 which is divisible by 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="https://assets.leetcode.com/uploads/2022/08/17/image-20220817112930-3.png" style="height: 85px; width: 132px;" />
<pre>
<strong>Input:</strong> grid = [[0,0]], k = 5
<strong>Output:</strong> 1
<strong>Explanation:</strong> The path highlighted in red has a sum of 0 + 0 = 0 which is divisible by 5.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img src="https://assets.leetcode.com/uploads/2022/08/12/image-20220812224605-3.png" style="width: 257px; height: 200px;" />
<pre>
<strong>Input:</strong> grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1
<strong>Output:</strong> 10
<strong>Explanation:</strong> Every integer is divisible by 1 so the sum of the elements on every possible path is divisible by k.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 50</code></li>
</ul>


## Hints

1. The actual numbers in grid do not matter. What matters are the remainders you get when you divide the numbers by k.

2. We can use dynamic programming to solve this problem. What can we use as states?

3. Let dp[i][j][value] represent the number of paths where the sum of the elements on the path has a remainder of value when divided by k.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-26 01:06:20 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the number of paths from (0,0) to (m-1, n-1) with a sum divisible by k, moving only down or right. This is a classic dynamic programming problem. We define dp[i][j][rem] as the number of paths from (0,0) to cell (i,j) such that the sum of elements along the path has a remainder rem when divided by k. The base case is dp[0][0][grid[0][0] % k] = 1. For any other cell (i,j), a path can reach it either from (i-1, j) (moving down) or (i, j-1) (moving right). If a path to (i-1, j) had a sum remainder prev_rem_up, and grid[i][j] has remainder val_rem = grid[i][j] % k, then the new path to (i,j) will have remainder (prev_rem_up + val_rem) % k. Similarly for paths from (i, j-1). Thus, dp[i][j][current_rem] is the sum of dp[i-1][j][(current_rem - val_rem + k) % k] and dp[i][j-1][(current_rem - val_rem + k) % k], all modulo 10^9 + 7.
To optimize space, we observe that dp[i][j] only depends on values from the previous row (i-1) and the current row (i) but previous column (j-1). This allows us to reduce the space complexity from O(m * n * k) to O(n * k) by only storing the DP states for the current and previous rows. We iterate through rows i from 0 to m-1. For each row i, we compute new_dp_row[j][rem] based on dp[j][rem] (from (i-1, j)) and new_dp_row[j-1][rem] (from (i, j-1)). After processing a row, new_dp_row becomes the dp for the next iteration. The final answer is dp[n-1][0], representing paths to the bottom-right corner (m-1, n-1) with a sum remainder of 0.

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
    int numberOfPaths(std::vector<std::vector<int>>& grid, int k) {
        int MOD = 1e9 + 7;
        int m = grid.size();
        int n = grid[0].size();

        // dp[j][rem] stores the number of paths to (current_row, j) with sum % k == rem
        std::vector<std::vector<int>> dp(n, std::vector<int>(k, 0));

        // Base case: (0, 0)
        dp[0][grid[0][0] % k] = 1;

        // Fill the first row (i = 0)
        for (int j = 1; j < n; ++j) {
            int val = grid[0][j];
            int val_rem = val % k;
            for (int prev_rem = 0; prev_rem < k; ++prev_rem) {
                if (dp[j-1][prev_rem] > 0) {
                    int current_rem = (prev_rem + val_rem) % k;
                    dp[j][current_rem] = (dp[j][current_rem] + dp[j-1][prev_rem]) % MOD;
                }
            }
        }

        // Fill subsequent rows (i from 1 to m-1)
        for (int i = 1; i < m; ++i) {
            // new_dp_row will store counts for the current row i
            std::vector<std::vector<int>> new_dp_row(n, std::vector<int>(k, 0));

            // First cell of current row (i, 0)
            int val = grid[i][0];
            int val_rem = val % k;
            for (int prev_rem = 0; prev_rem < k; ++prev_rem) {
                if (dp[0][prev_rem] > 0) { // Paths from (i-1, 0)
                    int current_rem = (prev_rem + val_rem) % k;
                    new_dp_row[0][current_rem] = (new_dp_row[0][current_rem] + dp[0][prev_rem]) % MOD;
                }
            }

            // Remaining cells of current row (i, j) for j from 1 to n-1
            for (int j = 1; j < n; ++j) {
                val = grid[i][j];
                val_rem = val % k;
                for (int prev_rem = 0; prev_rem < k; ++prev_rem) {
                    // Paths from (i-1, j)
                    if (dp[j][prev_rem] > 0) {
                        int current_rem = (prev_rem + val_rem) % k;
                        new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + dp[j][prev_rem]) % MOD;
                    }

                    // Paths from (i, j-1)
                    if (new_dp_row[j-1][prev_rem] > 0) {
                        int current_rem = (prev_rem + val_rem) % k;
                        new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + new_dp_row[j-1][prev_rem]) % MOD;
                    }
                }
            }

            dp = new_dp_row; // Update dp to be the current row for the next iteration
        }

        return dp[n-1][0];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int numberOfPaths(int[][] grid, int k) {
        int MOD = 1_000_000_007;
        int m = grid.length;
        int n = grid[0].length;

        // dp[j][rem] stores the number of paths to (current_row, j) with sum % k == rem
        int[][] dp = new int[n][k];

        // Base case: (0, 0)
        dp[0][grid[0][0] % k] = 1;

        // Fill the first row (i = 0)
        for (int j = 1; j < n; ++j) {
            int val = grid[0][j];
            int val_rem = val % k;
            for (int prev_rem = 0; prev_rem < k; ++prev_rem) {
                if (dp[j-1][prev_rem] > 0) {
                    int current_rem = (prev_rem + val_rem) % k;
                    dp[j][current_rem] = (dp[j][current_rem] + dp[j-1][prev_rem]) % MOD;
                }
            }
        }

        // Fill subsequent rows (i from 1 to m-1)
        for (int i = 1; i < m; ++i) {
            // new_dp_row will store counts for the current row i
            int[][] newDpRow = new int[n][k];

            // First cell of current row (i, 0)
            int val = grid[i][0];
            int val_rem = val % k;
            for (int prev_rem = 0; prev_rem < k; ++prev_rem) {
                if (dp[0][prev_rem] > 0) { // Paths from (i-1, 0)
                    int current_rem = (prev_rem + val_rem) % k;
                    newDpRow[0][current_rem] = (newDpRow[0][current_rem] + dp[0][prev_rem]) % MOD;
                }
            }

            // Remaining cells of current row (i, j) for j from 1 to n-1
            for (int j = 1; j < n; ++j) {
                val = grid[i][j];
                val_rem = val % k;
                for (int prev_rem = 0; prev_rem < k; ++prev_rem) {
                    // Paths from (i-1, j)
                    if (dp[j][prev_rem] > 0) {
                        int current_rem = (prev_rem + val_rem) % k;
                        newDpRow[j][current_rem] = (newDpRow[j][current_rem] + dp[j][prev_rem]) % MOD;
                    }

                    // Paths from (i, j-1)
                    if (newDpRow[j-1][prev_rem] > 0) {
                        int current_rem = (prev_rem + val_rem) % k;
                        newDpRow[j][current_rem] = (newDpRow[j][current_rem] + newDpRow[j-1][prev_rem]) % MOD;
                    }
                }
            }

            dp = newDpRow; // Update dp to be the current row for the next iteration
        }

        return dp[n-1][0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])

        # dp[j][rem] stores the number of paths to (current_row, j) with sum % k == rem
        dp = [[0] * k for _ in range(n)]

        # Base case: (0, 0)
        dp[0][grid[0][0] % k] = 1

        # Fill the first row (i = 0)
        for j in range(1, n):
            val = grid[0][j]
            val_rem = val % k
            for prev_rem in range(k):
                if dp[j-1][prev_rem] > 0:
                    current_rem = (prev_rem + val_rem) % k
                    dp[j][current_rem] = (dp[j][current_rem] + dp[j-1][prev_rem]) % MOD

        # Fill subsequent rows (i from 1 to m-1)
        for i in range(1, m):
            # new_dp_row will store counts for the current row i
            new_dp_row = [[0] * k for _ in range(n)]

            # First cell of current row (i, 0)
            val = grid[i][0]
            val_rem = val % k
            for prev_rem in range(k):
                if dp[0][prev_rem] > 0: # Paths from (i-1, 0)
                    current_rem = (prev_rem + val_rem) % k
                    new_dp_row[0][current_rem] = (new_dp_row[0][current_rem] + dp[0][prev_rem]) % MOD

            # Remaining cells of current row (i, j) for j from 1 to n-1
            for j in range(1, n):
                val = grid[i][j]
                val_rem = val % k
                for prev_rem in range(k):
                    # Paths from (i-1, j)
                    if dp[j][prev_rem] > 0:
                        current_rem = (prev_rem + val_rem) % k
                        new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + dp[j][prev_rem]) % MOD

                    # Paths from (i, j-1)
                    if new_dp_row[j-1][prev_rem] > 0:
                        current_rem = (prev_rem + val_rem) % k
                        new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + new_dp_row[j-1][prev_rem]) % MOD

            dp = new_dp_row # Update dp to be the current row for the next iteration

        return dp[n-1][0]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])

        # dp[j][rem] stores the number of paths to (current_row, j) with sum % k == rem
        dp = [[0] * k for _ in range(n)]

        # Base case: (0, 0)
        dp[0][grid[0][0] % k] = 1

        # Fill the first row (i = 0)
        for j in range(1, n):
            val = grid[0][j]
            val_rem = val % k
            for prev_rem in range(k):
                if dp[j-1][prev_rem] > 0:
                    current_rem = (prev_rem + val_rem) % k
                    dp[j][current_rem] = (dp[j][current_rem] + dp[j-1][prev_rem]) % MOD

        # Fill subsequent rows (i from 1 to m-1)
        for i in range(1, m):
            # new_dp_row will store counts for the current row i
            new_dp_row = [[0] * k for _ in range(n)]

            # First cell of current row (i, 0)
            val = grid[i][0]
            val_rem = val % k
            for prev_rem in range(k):
                if dp[0][prev_rem] > 0: # Paths from (i-1, 0)
                    current_rem = (prev_rem + val_rem) % k
                    new_dp_row[0][current_rem] = (new_dp_row[0][current_rem] + dp[0][prev_rem]) % MOD

            # Remaining cells of current row (i, j) for j from 1 to n-1
            for j in range(1, n):
                val = grid[i][j]
                val_rem = val % k
                for prev_rem in range(k):
                    # Paths from (i-1, j)
                    if dp[j][prev_rem] > 0:
                        current_rem = (prev_rem + val_rem) % k
                        new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + dp[j][prev_rem]) % MOD

                    # Paths from (i, j-1)
                    if new_dp_row[j-1][prev_rem] > 0:
                        current_rem = (prev_rem + val_rem) % k
                        new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + new_dp_row[j-1][prev_rem]) % MOD

            dp = new_dp_row # Update dp to be the current row for the next iteration

        return dp[n-1][0]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

int numberOfPaths(int** grid, int gridSize, int* gridColSize, int k) {
    int MOD = 1e9 + 7;
    int m = gridSize;
    int n = gridColSize[0];

    // dp[j][rem] stores the number of paths to (current_row, j) with sum % k == rem
    int** dp = (int**)malloc(n * sizeof(int*));
    for (int j = 0; j < n; ++j) {
        dp[j] = (int*)calloc(k, sizeof(int));
    }

    // Base case: (0, 0)
    dp[0][grid[0][0] % k] = 1;

    // Fill the first row (i = 0)
    for (int j = 1; j < n; ++j) {
        int val = grid[0][j];
        int val_rem = val % k;
        for (int prev_rem = 0; prev_rem < k; ++prev_rem) {
            if (dp[j-1][prev_rem] > 0) {
                int current_rem = (prev_rem + val_rem) % k;
                dp[j][current_rem] = (dp[j][current_rem] + dp[j-1][prev_rem]) % MOD;
            }
        }
    }

    // Fill subsequent rows (i from 1 to m-1)
    for (int i = 1; i < m; ++i) {
        // new_dp_row will store counts for the current row i
        int** new_dp_row = (int**)malloc(n * sizeof(int*));
        for (int j = 0; j < n; ++j) {
            new_dp_row[j] = (int*)calloc(k, sizeof(int));
        }

        // First cell of current row (i, 0)
        int val = grid[i][0];
        int val_rem = val % k;
        for (int prev_rem = 0; prev_rem < k; ++prev_rem) {
            if (dp[0][prev_rem] > 0) { // Paths from (i-1, 0)
                int current_rem = (prev_rem + val_rem) % k;
                new_dp_row[0][current_rem] = (new_dp_row[0][current_rem] + dp[0][prev_rem]) % MOD;
            }
        }

        // Remaining cells of current row (i, j) for j from 1 to n-1
        for (int j = 1; j < n; ++j) {
            val = grid[i][j];
            val_rem = val % k;
            for (int prev_rem = 0; prev_rem < k; ++prev_rem) {
                // Paths from (i-1, j)
                if (dp[j][prev_rem] > 0) {
                    int current_rem = (prev_rem + val_rem) % k;
                    new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + dp[j][prev_rem]) % MOD;
                }

                // Paths from (i, j-1)
                if (new_dp_row[j-1][prev_rem] > 0) {
                    int current_rem = (prev_rem + val_rem) % k;
                    new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + new_dp_row[j-1][prev_rem]) % MOD;
                }
            }
        }

        // Free previous dp and update
        for (int j = 0; j < n; ++j) {
            free(dp[j]);
        }
        free(dp);
        dp = new_dp_row; // Update dp to be the current row for the next iteration
    }

    int result = dp[n-1][0];

    // Free final dp
    for (int j = 0; j < n; ++j) {
        free(dp[j]);
    }
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
    public int NumberOfPaths(int[][] grid, int k) {
        int MOD = 1_000_000_007;
        int m = grid.Length;
        int n = grid[0].Length;

        // dp[j][rem] stores the number of paths to (current_row, j) with sum % k == rem
        int[][] dp = new int[n][];
        for (int j = 0; j < n; j++) {
            dp[j] = new int[k];
        }

        // Base case: (0, 0)
        dp[0][grid[0][0] % k] = 1;

        // Fill the first row (i = 0)
        for (int j = 1; j < n; ++j) {
            int val = grid[0][j];
            int valRem = val % k;
            for (int prevRem = 0; prevRem < k; ++prevRem) {
                if (dp[j-1][prevRem] > 0) {
                    int currentRem = (prevRem + valRem) % k;
                    dp[j][currentRem] = (dp[j][currentRem] + dp[j-1][prevRem]) % MOD;
                }
            }
        }

        // Fill subsequent rows (i from 1 to m-1)
        for (int i = 1; i < m; ++i) {
            // newDpRow will store counts for the current row i
            int[][] newDpRow = new int[n][];
            for (int j = 0; j < n; j++) {
                newDpRow[j] = new int[k];
            }

            // First cell of current row (i, 0)
            int val = grid[i][0];
            int valRem = val % k;
            for (int prevRem = 0; prevRem < k; ++prevRem) {
                if (dp[0][prevRem] > 0) { // Paths from (i-1, 0)
                    int currentRem = (prevRem + valRem) % k;
                    newDpRow[0][currentRem] = (newDpRow[0][currentRem] + dp[0][prevRem]) % MOD;
                }
            }

            // Remaining cells of current row (i, j) for j from 1 to n-1
            for (int j = 1; j < n; ++j) {
                val = grid[i][j];
                valRem = val % k;
                for (int prevRem = 0; prevRem < k; ++prevRem) {
                    // Paths from (i-1, j)
                    if (dp[j][prevRem] > 0) {
                        int currentRem = (prevRem + valRem) % k;
                        newDpRow[j][currentRem] = (newDpRow[j][currentRem] + dp[j][prevRem]) % MOD;
                    }

                    // Paths from (i, j-1)
                    if (newDpRow[j-1][prevRem] > 0) {
                        int currentRem = (prevRem + valRem) % k;
                        newDpRow[j][currentRem] = (newDpRow[j][currentRem] + newDpRow[j-1][prevRem]) % MOD;
                    }
                }
            }

            dp = newDpRow; // Update dp to be the current row for the next iteration
        }

        return dp[n-1][0];
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
var numberOfPaths = function(grid, k) {
    const MOD = 1e9 + 7;
    const m = grid.length;
    const n = grid[0].length;

    // dp[j][rem] stores the number of paths to (current_row, j) with sum % k == rem
    let dp = Array(n).fill(0).map(() => Array(k).fill(0));

    // Base case: (0, 0)
    dp[0][grid[0][0] % k] = 1;

    // Fill the first row (i = 0)
    for (let j = 1; j < n; ++j) {
        const val = grid[0][j];
        const val_rem = val % k;
        for (let prev_rem = 0; prev_rem < k; ++prev_rem) {
            if (dp[j-1][prev_rem] > 0) {
                const current_rem = (prev_rem + val_rem) % k;
                dp[j][current_rem] = (dp[j][current_rem] + dp[j-1][prev_rem]) % MOD;
            }
        }
    }

    // Fill subsequent rows (i from 1 to m-1)
    for (let i = 1; i < m; ++i) {
        // new_dp_row will store counts for the current row i
        let new_dp_row = Array(n).fill(0).map(() => Array(k).fill(0));

        // First cell of current row (i, 0)
        const val = grid[i][0];
        const val_rem = val % k;
        for (let prev_rem = 0; prev_rem < k; ++prev_rem) {
            if (dp[0][prev_rem] > 0) { // Paths from (i-1, 0)
                const current_rem = (prev_rem + val_rem) % k;
                new_dp_row[0][current_rem] = (new_dp_row[0][current_rem] + dp[0][prev_rem]) % MOD;
            }
        }

        // Remaining cells of current row (i, j) for j from 1 to n-1
        for (let j = 1; j < n; ++j) {
            const val = grid[i][j];
            const val_rem = val % k;
            for (let prev_rem = 0; prev_rem < k; ++prev_rem) {
                // Paths from (i-1, j)
                if (dp[j][prev_rem] > 0) {
                    const current_rem = (prev_rem + val_rem) % k;
                    new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + dp[j][prev_rem]) % MOD;
                }

                // Paths from (i, j-1)
                if (new_dp_row[j-1][prev_rem] > 0) {
                    const current_rem = (prev_rem + val_rem) % k;
                    new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + new_dp_row[j-1][prev_rem]) % MOD;
                }
            }
        }

        dp = new_dp_row; // Update dp to be the current row for the next iteration
    }

    return dp[n-1][0];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numberOfPaths(grid: number[][], k: number): number {
    const MOD = 10**9 + 7;
    const m = grid.length;
    const n = grid[0].length;

    // dp[j][rem] stores the number of paths to (current_row, j) with sum % k == rem
    let dp: number[][] = Array(n).fill(0).map(() => Array(k).fill(0));

    // Base case: (0, 0)
    dp[0][grid[0][0] % k] = 1;

    // Fill the first row (i = 0)
    for (let j = 1; j < n; ++j) {
        const val = grid[0][j];
        const val_rem = val % k;
        for (let prev_rem = 0; prev_rem < k; ++prev_rem) {
            if (dp[j-1][prev_rem] > 0) {
                const current_rem = (prev_rem + val_rem) % k;
                dp[j][current_rem] = (dp[j][current_rem] + dp[j-1][prev_rem]) % MOD;
            }
        }
    }

    // Fill subsequent rows (i from 1 to m-1)
    for (let i = 1; i < m; ++i) {
        // new_dp_row will store counts for the current row i
        let new_dp_row: number[][] = Array(n).fill(0).map(() => Array(k).fill(0));

        // First cell of current row (i, 0)
        const val = grid[i][0];
        const val_rem = val % k;
        for (let prev_rem = 0; prev_rem < k; ++prev_rem) {
            if (dp[0][prev_rem] > 0) { // Paths from (i-1, 0)
                const current_rem = (prev_rem + val_rem) % k;
                new_dp_row[0][current_rem] = (new_dp_row[0][current_rem] + dp[0][prev_rem]) % MOD;
            }
        }

        // Remaining cells of current row (i, j) for j from 1 to n-1
        for (let j = 1; j < n; ++j) {
            const val = grid[i][j];
            const val_rem = val % k;
            for (let prev_rem = 0; prev_rem < k; ++prev_rem) {
                // Paths from (i-1, j)
                if (dp[j][prev_rem] > 0) {
                    const current_rem = (prev_rem + val_rem) % k;
                    new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + dp[j][prev_rem]) % MOD;
                }

                // Paths from (i, j-1)
                if (new_dp_row[j-1][prev_rem] > 0) {
                    const current_rem = (prev_rem + val_rem) % k;
                    new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + new_dp_row[j-1][prev_rem]) % MOD;
                }
            }
        }

        dp = new_dp_row; // Update dp to be the current row for the next iteration
    }

    return dp[n-1][0];
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
     * @param int $k
     * @return int
     */
    function numberOfPaths(array $grid, int $k): int {
        $MOD = 10**9 + 7;
        $m = count($grid);
        $n = count($grid[0]);

        // dp[j][rem] stores the number of paths to (current_row, j) with sum % k == rem
        $dp = array_fill(0, $n, array_fill(0, $k, 0));

        // Base case: (0, 0)
        $dp[0][$grid[0][0] % $k] = 1;

        // Fill the first row (i = 0)
        for ($j = 1; $j < $n; ++$j) {
            $val = $grid[0][$j];
            $val_rem = $val % $k;
            for ($prev_rem = 0; $prev_rem < $k; ++$prev_rem) {
                if ($dp[$j-1][$prev_rem] > 0) {
                    $current_rem = ($prev_rem + $val_rem) % $k;
                    $dp[$j][$current_rem] = ($dp[$j][$current_rem] + $dp[$j-1][$prev_rem]) % $MOD;
                }
            }
        }

        // Fill subsequent rows (i from 1 to m-1)
        for ($i = 1; $i < $m; ++$i) {
            // new_dp_row will store counts for the current row i
            $new_dp_row = array_fill(0, $n, array_fill(0, $k, 0));

            // First cell of current row (i, 0)
            $val = $grid[$i][0];
            $val_rem = $val % $k;
            for ($prev_rem = 0; $prev_rem < $k; ++$prev_rem) {
                if ($dp[0][$prev_rem] > 0) { // Paths from (i-1, 0)
                    $current_rem = ($prev_rem + $val_rem) % $k;
                    $new_dp_row[0][$current_rem] = ($new_dp_row[0][$current_rem] + $dp[0][$prev_rem]) % $MOD;
                }
            }

            // Remaining cells of current row (i, j) for j from 1 to n-1
            for ($j = 1; $j < $n; ++$j) {
                $val = $grid[$i][$j];
                $val_rem = $val % $k;
                for ($prev_rem = 0; $prev_rem < $k; ++$prev_rem) {
                    // Paths from (i-1, j)
                    if ($dp[$j][$prev_rem] > 0) {
                        $current_rem = ($prev_rem + $val_rem) % $k;
                        $new_dp_row[$j][$current_rem] = ($new_dp_row[$j][$current_rem] + $dp[$j][$prev_rem]) % $MOD;
                    }

                    // Paths from (i, j-1)
                    if ($new_dp_row[$j-1][$prev_rem] > 0) {
                        $current_rem = ($prev_rem + $val_rem) % $k;
                        $new_dp_row[$j][$current_rem] = ($new_dp_row[$j][$current_rem] + $new_dp_row[$j-1][$prev_rem]) % $MOD;
                    }
                }
            }

            $dp = $new_dp_row; // Update dp to be the current row for the next iteration
        }

        return $dp[$n-1][0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func numberOfPaths(_ grid: [[Int]], _ k: Int) -> Int {
        let MOD = 1_000_000_007
        let m = grid.count
        let n = grid[0].count

        // dp[j][rem] stores the number of paths to (current_row, j) with sum % k == rem
        var dp = Array(repeating: Array(repeating: 0, count: k), count: n)

        // Base case: (0, 0)
        dp[0][grid[0][0] % k] = 1

        // Fill the first row (i = 0)
        for j in 1..<n {
            let val = grid[0][j]
            let val_rem = val % k
            for prev_rem in 0..<k {
                if dp[j-1][prev_rem] > 0 {
                    let current_rem = (prev_rem + val_rem) % k
                    dp[j][current_rem] = (dp[j][current_rem] + dp[j-1][prev_rem]) % MOD
                }
            }
        }

        // Fill subsequent rows (i from 1 to m-1)
        for i in 1..<m {
            // new_dp_row will store counts for the current row i
            var new_dp_row = Array(repeating: Array(repeating: 0, count: k), count: n)

            // First cell of current row (i, 0)
            let val = grid[i][0]
            let val_rem = val % k
            for prev_rem in 0..<k {
                if dp[0][prev_rem] > 0 { // Paths from (i-1, 0)
                    let current_rem = (prev_rem + val_rem) % k
                    new_dp_row[0][current_rem] = (new_dp_row[0][current_rem] + dp[0][prev_rem]) % MOD
                }
            }

            // Remaining cells of current row (i, j) for j from 1 to n-1
            for j in 1..<n {
                let val = grid[i][j]
                let val_rem = val % k
                for prev_rem in 0..<k {
                    // Paths from (i-1, j)
                    if dp[j][prev_rem] > 0 {
                        let current_rem = (prev_rem + val_rem) % k
                        new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + dp[j][prev_rem]) % MOD;
                    }

                    // Paths from (i, j-1)
                    if new_dp_row[j-1][prev_rem] > 0 {
                        let current_rem = (prev_rem + val_rem) % k
                        new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + new_dp_row[j-1][prev_rem]) % MOD;
                    }
                }
            }

            dp = new_dp_row // Update dp to be the current row for the next iteration
        }

        return dp[n-1][0]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun numberOfPaths(grid: Array<IntArray>, k: Int): Int {
        val MOD = 1_000_000_007
        val m = grid.size
        val n = grid[0].size

        // dp[j][rem] stores the number of paths to (current_row, j) with sum % k == rem
        var dp = Array(n) { IntArray(k) { 0 } }

        // Base case: (0, 0)
        dp[0][grid[0][0] % k] = 1

        // Fill the first row (i = 0)
        for (j in 1 until n) {
            val val = grid[0][j]
            val val_rem = val % k
            for (prev_rem in 0 until k) {
                if (dp[j-1][prev_rem] > 0) {
                    val current_rem = (prev_rem + val_rem) % k
                    dp[j][current_rem] = (dp[j][current_rem] + dp[j-1][prev_rem]) % MOD
                }
            }
        }

        // Fill subsequent rows (i from 1 to m-1)
        for (i in 1 until m) {
            // new_dp_row will store counts for the current row i
            val newDpRow = Array(n) { IntArray(k) { 0 } }

            // First cell of current row (i, 0)
            val val = grid[i][0]
            val val_rem = val % k
            for (prev_rem in 0 until k) {
                if (dp[0][prev_rem] > 0) { // Paths from (i-1, 0)
                    val current_rem = (prev_rem + val_rem) % k
                    newDpRow[0][current_rem] = (newDpRow[0][current_rem] + dp[0][prev_rem]) % MOD
                }
            }

            // Remaining cells of current row (i, j) for j from 1 to n-1
            for (j in 1 until n) {
                val = grid[i][j]
                val_rem = val % k
                for (prev_rem in 0 until k) {
                    // Paths from (i-1, j)
                    if (dp[j][prev_rem] > 0) {
                        val current_rem = (prev_rem + val_rem) % k
                        newDpRow[j][current_rem] = (newDpRow[j][current_rem] + dp[j][prev_rem]) % MOD
                    }

                    // Paths from (i, j-1)
                    if (newDpRow[j-1][prev_rem] > 0) {
                        val current_rem = (prev_rem + val_rem) % k
                        newDpRow[j][current_rem] = (newDpRow[j][current_rem] + newDpRow[j-1][prev_rem]) % MOD
                    }
                }
            }

            dp = newDpRow // Update dp to be the current row for the next iteration
        }

        return dp[n-1][0]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int numberOfPaths(List<List<int>> grid, int k) {
    final int MOD = 1000000007;
    int m = grid.length;
    int n = grid[0].length;

    // dp[j][rem] stores the number of paths to (current_row, j) with sum % k == rem
    List<List<int>> dp = List.generate(n, (_) => List.filled(k, 0));

    // Base case: (0, 0)
    dp[0][grid[0][0] % k] = 1;

    // Fill the first row (i = 0)
    for (int j = 1; j < n; ++j) {
      int val = grid[0][j];
      int valRem = val % k;
      for (int prevRem = 0; prevRem < k; ++prevRem) {
        if (dp[j-1][prevRem] > 0) {
          int currentRem = (prevRem + valRem) % k;
          dp[j][currentRem] = (dp[j][currentRem] + dp[j-1][prevRem]) % MOD;
        }
      }
    }

    // Fill subsequent rows (i from 1 to m-1)
    for (int i = 1; i < m; ++i) {
      // newDpRow will store counts for the current row i
      List<List<int>> newDpRow = List.generate(n, (_) => List.filled(k, 0));

      // First cell of current row (i, 0)
      int val = grid[i][0];
      int valRem = val % k;
      for (int prevRem = 0; prevRem < k; ++prevRem) {
        if (dp[0][prevRem] > 0) { // Paths from (i-1, 0)
          int currentRem = (prevRem + valRem) % k;
          newDpRow[0][currentRem] = (newDpRow[0][currentRem] + dp[0][prevRem]) % MOD;
        }
      }

      // Remaining cells of current row (i, j) for j from 1 to n-1
      for (int j = 1; j < n; ++j) {
        val = grid[i][j];
        valRem = val % k;
        for (int prevRem = 0; prevRem < k; ++prevRem) {
          // Paths from (i-1, j)
          if (dp[j][prevRem] > 0) {
            int currentRem = (prevRem + valRem) % k;
            newDpRow[j][currentRem] = (newDpRow[j][currentRem] + dp[j][prevRem]) % MOD;
          }

          // Paths from (i, j-1)
          if (newDpRow[j-1][prevRem] > 0) {
            int currentRem = (prevRem + valRem) % k;
            newDpRow[j][currentRem] = (newDpRow[j][currentRem] + newDpRow[j-1][prevRem]) % MOD;
          }
        }
      }

      dp = newDpRow; // Update dp to be the current row for the next iteration
    }

    return dp[n-1][0];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func numberOfPaths(grid [][]int, k int) int {
    MOD := 1_000_000_007
    m := len(grid)
    n := len(grid[0])

    // dp[j][rem] stores the number of paths to (current_row, j) with sum % k == rem
    dp := make([][]int, n)
    for j := range dp {
        dp[j] = make([]int, k)
    }

    // Base case: (0, 0)
    dp[0][grid[0][0]%k] = 1

    // Fill the first row (i = 0)
    for j := 1; j < n; j++ {
        val := grid[0][j]
        val_rem := val % k
        for prev_rem := 0; prev_rem < k; prev_rem++ {
            if dp[j-1][prev_rem] > 0 {
                current_rem := (prev_rem + val_rem) % k
                dp[j][current_rem] = (dp[j][current_rem] + dp[j-1][prev_rem]) % MOD
            }
        }
    }

    // Fill subsequent rows (i from 1 to m-1)
    for i := 1; i < m; i++ {
        // new_dp_row will store counts for the current row i
        new_dp_row := make([][]int, n)
        for j := range new_dp_row {
            new_dp_row[j] = make([]int, k)
        }

        // First cell of current row (i, 0)
        val := grid[i][0]
        val_rem := val % k
        for prev_rem := 0; prev_rem < k; prev_rem++ {
            if dp[0][prev_rem] > 0 { // Paths from (i-1, 0)
                current_rem := (prev_rem + val_rem) % k
                new_dp_row[0][current_rem] = (new_dp_row[0][current_rem] + dp[0][prev_rem]) % MOD
            }
        }

        // Remaining cells of current row (i, j) for j from 1 to n-1
        for j := 1; j < n; j++ {
            val = grid[i][j]
            val_rem = val % k
            for prev_rem := 0; prev_rem < k; prev_rem++ {
                // Paths from (i-1, j)
                if dp[j][prev_rem] > 0 {
                    current_rem := (prev_rem + val_rem) % k
                    new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + dp[j][prev_rem]) % MOD
                }

                // Paths from (i, j-1)
                if new_dp_row[j-1][prev_rem] > 0 {
                    current_rem := (prev_rem + val_rem) % k
                    new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + new_dp_row[j-1][prev_rem]) % MOD
                }
            }
        }

        dp = new_dp_row // Update dp to be the current row for the next iteration
    }

    return dp[n-1][0]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    # @param {Integer[][]} grid
    # @param {Integer} k
    # @return {Integer}
    def number_of_paths(grid, k)
        mod = 10**9 + 7
        m = grid.length
        n = grid[0].length

        # dp[j][rem] stores the number of paths to (current_row, j) with sum % k == rem
        dp = Array.new(n) { Array.new(k, 0) }

        # Base case: (0, 0)
        dp[0][grid[0][0] % k] = 1

        # Fill the first row (i = 0)
        (1...n).each do |j|
            val = grid[0][j]
            val_rem = val % k
            (0...k).each do |prev_rem|
                if dp[j-1][prev_rem] > 0
                    current_rem = (prev_rem + val_rem) % k
                    dp[j][current_rem] = (dp[j][current_rem] + dp[j-1][prev_rem]) % mod
                end
            end
        end

        # Fill subsequent rows (i from 1 to m-1)
        (1...m).each do |i|
            # new_dp_row will store counts for the current row i
            new_dp_row = Array.new(n) { Array.new(k, 0) }

            # First cell of current row (i, 0)
            val = grid[i][0]
            val_rem = val % k
            (0...k).each do |prev_rem|
                if dp[0][prev_rem] > 0 # Paths from (i-1, 0)
                    current_rem = (prev_rem + val_rem) % k
                    new_dp_row[0][current_rem] = (new_dp_row[0][current_rem] + dp[0][prev_rem]) % mod
                end
            end

            # Remaining cells of current row (i, j) for j from 1 to n-1
            (1...n).each do |j|
                val = grid[i][j]
                val_rem = val % k
                (0...k).each do |prev_rem|
                    # Paths from (i-1, j)
                    if dp[j][prev_rem] > 0
                        current_rem = (prev_rem + val_rem) % k
                        new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + dp[j][prev_rem]) % mod
                    end

                    # Paths from (i, j-1)
                    if new_dp_row[j-1][prev_rem] > 0
                        current_rem = (prev_rem + val_rem) % k
                        new_dp_row[j][current_rem] = (new_dp_row[j][current_rem] + new_dp_row[j-1][prev_rem]) % mod
                    end
                end
            end

            dp = new_dp_row # Update dp to be the current row for the next iteration
        end

        return dp[n-1][0]
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def numberOfPaths(grid: Array[Array[Int]], k: Int): Int = {
        val MOD = 1_000_000_007
        val m = grid.length
        val n = grid(0).length

        // dp(j)(rem) stores the number of paths to (current_row, j) with sum % k == rem
        var dp: Array[Array[Int]] = Array.fill(n)(Array.fill(k)(0))

        // Base case: (0, 0)
        dp(0)(grid(0)(0) % k) = 1

        // Fill the first row (i = 0)
        for (j <- 1 until n) {
            val val_ = grid(0)(j)
            val val_rem = val_ % k
            for (prev_rem <- 0 until k) {
                if (dp(j-1)(prev_rem) > 0) {
                    val current_rem = (prev_rem + val_rem) % k
                    dp(j)(current_rem) = (dp(j)(current_rem) + dp(j-1)(prev_rem)) % MOD
                }
            }
        }

        // Fill subsequent rows (i from 1 to m-1)
        for (i <- 1 until m) {
            // new_dp_row will store counts for the current row i
            val new_dp_row: Array[Array[Int]] = Array.fill(n)(Array.fill(k)(0))

            // First cell of current row (i, 0)
            val val_ = grid(i)(0)
            val val_rem = val_ % k
            for (prev_rem <- 0 until k) {
                if (dp(0)(prev_rem) > 0) { // Paths from (i-1, 0)
                    val current_rem = (prev_rem + val_rem) % k
                    new_dp_row(0)(current_rem) = (new_dp_row(0)(current_rem) + dp(0)(prev_rem)) % MOD
                }
            }

            // Remaining cells of current row (i, j) for j from 1 to n-1
            for (j <- 1 until n) {
                val val_curr = grid(i)(j)
                val val_rem_curr = val_curr % k
                for (prev_rem <- 0 until k) {
                    // Paths from (i-1, j)
                    if (dp(j)(prev_rem) > 0) {
                        val current_rem = (prev_rem + val_rem_curr) % k
                        new_dp_row(j)(current_rem) = (new_dp_row(j)(current_rem) + dp(j)(prev_rem)) % MOD
                    }

                    // Paths from (i, j-1)
                    if (new_dp_row(j-1)(prev_rem) > 0) {
                        val current_rem = (prev_rem + val_rem_curr) % k
                        new_dp_row(j)(current_rem) = (new_dp_row(j)(current_rem) + new_dp_row(j-1)(prev_rem)) % MOD
                    }
                }
            }

            dp = new_dp_row // Update dp to be the current row for the next iteration
        }

        dp(n-1)(0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn number_of_paths(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let modular: i32 = 1_000_000_007;
        let m = grid.len();
        let n = grid[0].len();
        let k_usize = k as usize;

        // dp[j][rem] stores the number of paths to (current_row, j) with sum % k == rem
        let mut dp: Vec<Vec<i32>> = vec![vec![0; k_usize]; n];

        // Base case: (0, 0)
        dp[0][(grid[0][0] % k) as usize] = 1;

        // Fill the first row (i = 0)
        for j in 1..n {
            let val = grid[0][j];
            let val_rem = val % k;
            for prev_rem_idx in 0..k_usize {
                if dp[j-1][prev_rem_idx] > 0 {
                    let current_rem = (prev_rem_idx as i32 + val_rem) % k;
                    dp[j][current_rem as usize] = (dp[j][current_rem as usize] + dp[j-1][prev_rem_idx]) % modular;
                }
            }
        }

        // Fill subsequent rows (i from 1 to m-1)
        for i in 1..m {
            // new_dp_row will store counts for the current row i
            let mut new_dp_row: Vec<Vec<i32>> = vec![vec![0; k_usize]; n];

            // First cell of current row (i, 0)
            let val = grid[i][0];
            let val_rem = val % k;
            for prev_rem_idx in 0..k_usize {
                if dp[0][prev_rem_idx] > 0 { // Paths from (i-1, 0)
                    let current_rem = (prev_rem_idx as i32 + val_rem) % k;
                    new_dp_row[0][current_rem as usize] = (new_dp_row[0][current_rem as usize] + dp[0][prev_rem_idx]) % modular;
                }
            }

            // Remaining cells of current row (i, j) for j from 1 to n-1
            for j in 1..n {
                let val = grid[i][j];
                let val_rem = val % k;
                for prev_rem_idx in 0..k_usize {
                    // Paths from (i-1, j)
                    if dp[j][prev_rem_idx] > 0 {
                        let current_rem = (prev_rem_idx as i32 + val_rem) % k;
                        new_dp_row[j][current_rem as usize] = (new_dp_row[j][current_rem as usize] + dp[j][prev_rem_idx]) % modular;
                    }

                    // Paths from (i, j-1)
                    if new_dp_row[j-1][prev_rem_idx] > 0 {
                        let current_rem = (prev_rem_idx as i32 + val_rem) % k;
                        new_dp_row[j][current_rem as usize] = (new_dp_row[j][current_rem as usize] + new_dp_row[j-1][prev_rem_idx]) % modular;
                    }
                }
            }

            dp = new_dp_row; // Update dp to be the current row for the next iteration
        }

        dp[n-1][0] as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
(define (number-of-paths grid k)
  (define MOD 1000000007)
  (define m (vector-length grid))
  (define n (vector-length (vector-ref grid 0)))

  ;; dp[j][rem] stores the number of paths to (current_row, j) with sum % k == rem
  (define dp (build-vector n (lambda (j) (build-vector k (lambda (rem) 0)))))

  ;; Base case: (0, 0)
  (vector-set! (vector-ref dp 0) (modulo (vector-ref (vector-ref grid 0) 0) k) 1)

  ;; Fill the first row (i = 0)
  (for ([j (in-range 1 n)])
    (define val (vector-ref (vector-ref grid 0) j))
    (define val-rem (modulo val k))
    (for ([prev-rem (in-range 0 k)])
      (when (> (vector-ref (vector-ref dp (- j 1)) prev-rem) 0)
        (define current-rem (modulo (+ prev-rem val-rem) k))
        (vector-set! (vector-ref dp j) current-rem
                     (modulo (+ (vector-ref (vector-ref dp j) current-rem)
                                (vector-ref (vector-ref dp (- j 1)) prev-rem))
                             MOD)))))

  ;; Fill subsequent rows (i from 1 to m-1)
  (for ([i (in-range 1 m)])
    ;; new-dp-row will store counts for the current row i
    (define new-dp-row (build-vector n (lambda (j) (build-vector k (lambda (rem) 0)))))

    ;; First cell of current row (i, 0)
    (define val (vector-ref (vector-ref grid i) 0))
    (define val-rem (modulo val k))
    (for ([prev-rem (in-range 0 k)])
      (when (> (vector-ref (vector-ref dp 0) prev-rem) 0) ;; Paths from (i-1, 0)
        (define current-rem (modulo (+ prev-rem val-rem) k))
        (vector-set! (vector-ref new-dp-row 0) current-rem
                     (modulo (+ (vector-ref (vector-ref new-dp-row 0) current-rem)
                                (vector-ref (vector-ref dp 0) prev-rem))
                             MOD))))

    ;; Remaining cells of current row (i, j) for j from 1 to n-1
    (for ([j (in-range 1 n)])
      (define val (vector-ref (vector-ref grid i) j))
      (define val-rem (modulo val k))
      (for ([prev-rem (in-range 0 k)])
        ;; Paths from (i-1, j)
        (when (> (vector-ref (vector-ref dp j) prev-rem) 0)
          (define current-rem (modulo (+ prev-rem val-rem) k))
          (vector-set! (vector-ref new-dp-row j) current-rem
                       (modulo (+ (vector-ref (vector-ref new-dp-row j) current-rem)
                                  (vector-ref (vector-ref dp j) prev-rem))
                               MOD)))

        ;; Paths from (i, j-1)
        (when (> (vector-ref (vector-ref new-dp-row (- j 1)) prev-rem) 0)
          (define current-rem (modulo (+ prev-rem val-rem) k))
          (vector-set! (vector-ref new-dp-row j) current-rem
                       (modulo (+ (vector-ref (vector-ref new-dp-row j) current-rem)
                                  (vector-ref (vector-ref new-dp-row (- j 1)) prev-rem))
                               MOD)))))

    (set! dp new-dp-row) ;; Update dp to be the current row for the next iteration
    )

  (vector-ref (vector-ref dp (- n 1)) 0))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([number_of_paths/2]).

number_of_paths(Grid, K) ->
    MOD = 1000000007,
    M = length(Grid),
    N = length(hd(Grid)),

    % dp[j][rem] stores the number of paths to (current_row, j) with sum % K == rem
    % Represent dp as a list of lists (vectors in other languages)
    Dp = lists:duplicate(N, lists:duplicate(K, 0)),

    % Base case: (0, 0)
    Grid00 = hd(hd(Grid)),
    Dp1 = set_in_list_of_lists(Dp, 0, Grid00 rem K, 1),

    % Fill the first row (i = 0)
    Dp2 = lists:foldl(fun(J, CurrentDp) ->
        Val = lists:nth(J + 1, hd(Grid)),
        ValRem = Val rem K,
        lists:foldl(fun(PrevRem, InnerDp) ->
            PrevCount = get_in_list_of_lists(InnerDp, J - 1, PrevRem),
            if PrevCount > 0 ->
                CurrentRem = (PrevRem + ValRem) rem K,
                set_in_list_of_lists(InnerDp, J, CurrentRem, (get_in_list_of_lists(InnerDp, J, CurrentRem) + PrevCount) rem MOD)
            else
                InnerDp
            end
        end, CurrentDp, lists:seq(0, K - 1))
    end, Dp1, lists:seq(1, N - 1)),

    % Fill subsequent rows (i from 1 to M-1)
    FinalDp = lists:foldl(fun(I, CurrentDp) ->
        % new_dp_row will store counts for the current row I
        NewDpRow = lists:duplicate(N, lists:duplicate(K, 0)),

        % First cell of current row (I, 0)
        ValI0 = lists:nth(1, lists:nth(I + 1, Grid)),
        ValRemI0 = ValI0 rem K,
        NewDpRow1 = lists:foldl(fun(PrevRem, InnerNewDpRow) ->
            PrevCount = get_in_list_of_lists(CurrentDp, 0, PrevRem),
            if PrevCount > 0 -> % Paths from (I-1, 0)
                CurrentRem = (PrevRem + ValRemI0) rem K,
                set_in_list_of_lists(InnerNewDpRow, 0, CurrentRem, (get_in_list_of_lists(InnerNewDpRow, 0, CurrentRem) + PrevCount) rem MOD)
            else
                InnerNewDpRow
            end
        end, NewDpRow, lists:seq(0, K - 1)),

        % Remaining cells of current row (I, J) for J from 1 to N-1
        lists:foldl(fun(J, InnerNewDpRow) ->
            ValIJ = lists:nth(J + 1, lists:nth(I + 1, Grid)),
            ValRemIJ = ValIJ rem K,
            lists:foldl(fun(PrevRem, DeepestNewDpRow) ->
                % Paths from (I-1, J)
                PrevCountFromAbove = get_in_list_of_lists(CurrentDp, J, PrevRem),
                TempDpRow1 = if PrevCountFromAbove > 0 ->
                    CurrentRem = (PrevRem + ValRemIJ) rem K,
                    set_in_list_of_lists(DeepestNewDpRow, J, CurrentRem, (get_in_list_of_lists(DeepestNewDpRow, J, CurrentRem) + PrevCountFromAbove) rem MOD)
                else
                    DeepestNewDpRow
                end,

                % Paths from (I, J-1)
                PrevCountFromLeft = get_in_list_of_lists(DeepestNewDpRow, J - 1, PrevRem),
                if PrevCountFromLeft > 0 ->
                    CurrentRem = (PrevRem + ValRemIJ) rem K,
                    set_in_list_of_lists(TempDpRow1, J, CurrentRem, (get_in_list_of_lists(TempDpRow1, J, CurrentRem) + PrevCountFromLeft) rem MOD)
                else
                    TempDpRow1
                end
            end, InnerNewDpRow, lists:seq(0, K - 1))
        end, NewDpRow1, lists:seq(1, N - 1))
    end, Dp2, lists:seq(1, M - 1)),

    get_in_list_of_lists(FinalDp, N - 1, 0).

% Helper function to get a value from a list of lists (0-indexed)
get_in_list_of_lists(ListOfLists, RowIdx, ColIdx) ->
    lists:nth(ColIdx + 1, lists:nth(RowIdx + 1, ListOfLists)).

% Helper function to set a value in a list of lists (0-indexed)
set_in_list_of_lists(ListOfLists, RowIdx, ColIdx, Value) ->
    Row = lists:nth(RowIdx + 1, ListOfLists),
    NewRow = set_in_list(Row, ColIdx, Value),
    set_in_list(ListOfLists, RowIdx, NewRow).

% Helper function to set a value in a list (0-indexed)
set_in_list(List, Index, Value) ->
    lists:replace_nth(Index + 1, Value, List).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @mod 1_000_000_007

  @spec number_of_paths(grid :: [[integer]], k :: integer) :: integer
  def number_of_paths(grid, k) do
    m = length(grid)
    n = length(hd(grid))

    # dp[j][rem] stores the number of paths to (current_row, j) with sum % k == rem
    # Represent dp as a list of lists (vectors in other languages)
    dp = List.duplicate(n, List.duplicate(k, 0))

    # Base case: (0, 0)
    grid_0_0 = hd(hd(grid))
    dp = put_in_list_of_lists(dp, 0, rem(grid_0_0, k), 1)

    # Fill the first row (i = 0)
    dp = Enum.reduce(1..(n - 1), dp, fn j, current_dp ->
      val = Enum.at(hd(grid), j)
      val_rem = rem(val, k)
      Enum.reduce(0..(k - 1), current_dp, fn prev_rem, inner_dp ->
        prev_count = get_in_list_of_lists(inner_dp, j - 1, prev_rem)
        if prev_count > 0 do
          current_rem = rem(prev_rem + val_rem, k)
          put_in_list_of_lists(inner_dp, j, current_rem, rem(get_in_list_of_lists(inner_dp, j, current_rem) + prev_count, @mod))
        else
          inner_dp
        end
      end)
    end)

    # Fill subsequent rows (i from 1 to m-1)
    final_dp = Enum.reduce(1..(m - 1), dp, fn i, current_dp ->
      # new_dp_row will store counts for the current row i
      new_dp_row = List.duplicate(n, List.duplicate(k, 0))

      # First cell of current row (i, 0)
      val_i_0 = Enum.at(Enum.at(grid, i), 0)
      val_rem_i_0 = rem(val_i_0, k)
      new_dp_row = Enum.reduce(0..(k - 1), new_dp_row, fn prev_rem, inner_new_dp_row ->
        prev_count = get_in_list_of_lists(current_dp, 0, prev_rem)
        if prev_count > 0 do # Paths from (i-1, 0)
          current_rem = rem(prev_rem + val_rem_i_0, k)
          put_in_list_of_lists(inner_new_dp_row, 0, current_rem, rem(get_in_list_of_lists(inner_new_dp_row, 0, current_rem) + prev_count, @mod))
        else
          inner_new_dp_row
        end
      end)

      # Remaining cells of current row (i, j) for j from 1 to n-1
      Enum.reduce(1..(n - 1), new_dp_row, fn j, inner_new_dp_row ->
        val_i_j = Enum.at(Enum.at(grid, i), j)
        val_rem_i_j = rem(val_i_j, k)
        Enum.reduce(0..(k - 1), inner_new_dp_row, fn prev_rem, deepest_new_dp_row ->
          # Paths from (i-1, j)
          prev_count_from_above = get_in_list_of_lists(current_dp, j, prev_rem)
          temp_dp_row_1 = if prev_count_from_above > 0 do
            current_rem = rem(prev_rem + val_rem_i_j, k)
            put_in_list_of_lists(deepest_new_dp_row, j, current_rem, rem(get_in_list_of_lists(deepest_new_dp_row, j, current_rem) + prev_count_from_above, @mod))
          else
            deepest_new_dp_row
          end

          # Paths from (i, j-1)
          prev_count_from_left = get_in_list_of_lists(temp_dp_row_1, j - 1, prev_rem)
          if prev_count_from_left > 0 do
            current_rem = rem(prev_rem + val_rem_i_j, k)
            put_in_list_of_lists(temp_dp_row_1, j, current_rem, rem(get_in_list_of_lists(temp_dp_row_1, j, current_rem) + prev_count_from_left, @mod))
          else
            temp_dp_row_1
          end
        end)
      end)
    end)

    get_in_list_of_lists(final_dp, n - 1, 0)
  end

  # Helper function to get a value from a list of lists (0-indexed)
  defp get_in_list_of_lists(list_of_lists, row_idx, col_idx) do
    list_of_lists
    |> Enum.at(row_idx)
    |> Enum.at(col_idx)
  end

  # Helper function to set a value in a list of lists (0-indexed)
  defp put_in_list_of_lists(list_of_lists, row_idx, col_idx, value) do
    list_of_lists
    |> List.update_at(row_idx, fn row ->
      List.update_at(row, col_idx, fn _ -> value end)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(m * n * k). We iterate through each of the m rows and n columns. For each cell (i, j), we iterate k times (for each possible remainder) to update its DP states. Given m * n <= 5 * 10^4 and k <= 50, the total operations are at most 5 * 10^4 * 50 = 2.5 * 10^6, which is efficient enough.

- **Space Complexity:** The space complexity is O(n * k). We use two 2D arrays, `dp` and `new_dp_row`, each of size n * k, to store the DP states for the current and previous rows. This is because the calculation for the current row only depends on the previous row and already computed values in the current row. Given n <= 5 * 10^4 and k <= 50, the space required is at most 5 * 10^4 * 50 * sizeof(int), which is approximately 10MB, well within typical memory limits.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-26 01:06:31 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved using dynamic programming. The key intuition is to consider the remainders of the sum of elements on the path when divided by k. We can use a 3D DP array, dp, where dp[i][j][value] represents the number of paths from the top-left cell to the cell at position (i, j) such that the sum of elements on the path has a remainder of value when divided by k. We can fill up this DP array by iterating over each cell in the grid and considering the possible paths that can reach that cell. The final answer will be stored in dp[m-1][n-1][0], where m and n are the number of rows and columns in the grid, respectively. The actual numbers in the grid do not matter, what matters are the remainders when divided by k, so we can use the modulo operator to simplify the problem.

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
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(k, 0)));
        dp[0][0][grid[0][0] % k] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                for (int val = 0; val < k; val++) {
                    if (i > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val];
                    if (j > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i][j-1][val];
                }
            }
        }
        return dp[m-1][n-1][0];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int numberOfPaths(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        int[][][] dp = new int[m][n][k];
        dp[0][0][grid[0][0] % k] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                for (int val = 0; val < k; val++) {
                    if (i > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val];
                    if (j > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i][j-1][val];
                }
            }
        }
        return dp[m-1][n-1][0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0]*k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                for val in range(k):
                    if i > 0: dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val]
                    if j > 0: dp[i][j][(val + grid[i][j]) % k] += dp[i][j-1][val]
        return dp[m-1][n-1][0]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0]*k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                for val in range(k):
                    if i > 0: dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val]
                    if j > 0: dp[i][j][(val + grid[i][j]) % k] += dp[i][j-1][val]
        return dp[m-1][n-1][0]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int** grid;
    int gridSize;
    int* gridColSize;
} Solution;

int numberOfPaths(int** grid, int gridSize, int* gridColSize, int k) {
    int m = gridSize, n = gridColSize[0];
    int*** dp = (int***)malloc(m * sizeof(int**));
    for (int i = 0; i < m; i++) {
        dp[i] = (int**)malloc(n * sizeof(int*));
        for (int j = 0; j < n; j++) {
            dp[i][j] = (int*)malloc(k * sizeof(int));
        }
    }
    dp[0][0][grid[0][0] % k] = 1;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0 && j == 0) continue;
            for (int val = 0; val < k; val++) {
                if (i > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val];
                if (j > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i][j-1][val];
            }
        }
    }
    int res = dp[m-1][n-1][0];
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            free(dp[i][j]);
        }
        free(dp[i]);
    }
    free(dp);
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int NumberOfPaths(int[][] grid, int k) {
        int m = grid.Length, n = grid[0].Length;
        int[,,] dp = new int[m, n, k];
        dp[0, 0, grid[0][0] % k] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                for (int val = 0; val < k; val++) {
                    if (i > 0) dp[i, j, (val + grid[i][j]) % k] += dp[i-1, j, val];
                    if (j > 0) dp[i, j, (val + grid[i][j]) % k] += dp[i, j-1, val];
                }
            }
        }
        return dp[m-1, n-1, 0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var numberOfPaths = function(grid, k) {
    let m = grid.length, n = grid[0].length;
    let dp = Array(m).fill().map(() => Array(n).fill().map(() => Array(k).fill(0)));
    dp[0][0][grid[0][0] % k] = 1;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i == 0 && j == 0) continue;
            for (let val = 0; val < k; val++) {
                if (i > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val];
                if (j > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i][j-1][val];
            }
        }
    }
    return dp[m-1][n-1][0];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numberOfPaths(grid: number[][], k: number): number {
    let m: number = grid.length, n: number = grid[0].length;
    let dp: number[][][] = Array(m).fill().map(() => Array(n).fill().map(() => Array(k).fill(0)));
    dp[0][0][grid[0][0] % k] = 1;
    for (let i: number = 0; i < m; i++) {
        for (let j: number = 0; j < n; j++) {
            if (i == 0 && j == 0) continue;
            for (let val: number = 0; val < k; val++) {
                if (i > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val];
                if (j > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i][j-1][val];
            }
        }
    }
    return dp[m-1][n-1][0];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function numberOfPaths($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $dp = array_fill(0, $m, array_fill(0, $n, array_fill(0, $k, 0)));
        $dp[0][0][$grid[0][0] % $k] = 1;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($i == 0 && $j == 0) continue;
                for ($val = 0; $val < $k; $val++) {
                    if ($i > 0) $dp[$i][$j][($val + $grid[$i][$j]) % $k] += $dp[$i-1][$j][$val];
                    if ($j > 0) $dp[$i][$j][($val + $grid[$i][$j]) % $k] += $dp[$i][$j-1][$val];
                }
            }
        }
        return $dp[$m-1][$n-1][0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func numberOfPaths(_ grid: [[Int]], _ k: Int) -> Int {
        let m = grid.count
        let n = grid[0].count
        var dp = Array(repeating: Array(repeating: Array(repeating: 0, count: k), count: n), count: m)
        dp[0][0][grid[0][0] % k] = 1
        for i in 0..<m {
            for j in 0..<n {
                if i == 0 && j == 0 { continue }
                for val in 0..<k {
                    if i > 0 { dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val] }
                    if j > 0 { dp[i][j][(val + grid[i][j]) % k] += dp[i][j-1][val] }
                }
            }
        }
        return dp[m-1][n-1][0]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun numberOfPaths(grid: Array<IntArray>, k: Int): Int {
        val m = grid.size
        val n = grid[0].size
        val dp = Array(m) { Array(n) { IntArray(k) } }
        dp[0][0][grid[0][0] % k] = 1
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (i == 0 && j == 0) continue
                for (val in 0 until k) {
                    if (i > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val]
                    if (j > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i][j-1][val]
                }
            }
        }
        return dp[m-1][n-1][0]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int numberOfPaths(List<List<int>> grid, int k) {
        int m = grid.length, n = grid[0].length;
        List<List<List<int>>> dp = List.generate(m, (i) => List.generate(n, (j) => List.generate(k, (k) => 0)));
        dp[0][0][grid[0][0] % k] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                for (int val = 0; val < k; val++) {
                    if (i > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val];
                    if (j > 0) dp[i][j][(val + grid[i][j]) % k] += dp[i][j-1][val];
                }
            }
        }
        return dp[m-1][n-1][0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func numberOfPaths(grid [][]int, k int) int {
    m, n := len(grid), len(grid[0])
    dp := make([][][]int, m)
    for i := range dp {
        dp[i] = make([][]int, n)
        for j := range dp[i] {
            dp[i][j] = make([]int, k)
        }
    }
    dp[0][0][grid[0][0]%k] = 1
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if i == 0 && j == 0 { continue }
            for val := 0; val < k; val++ {
                if i > 0 { dp[i][j][(val+grid[i][j])%k] += dp[i-1][j][val] }
                if j > 0 { dp[i][j][(val+grid[i][j])%k] += dp[i][j-1][val] }
            }
        }
    }
    return dp[m-1][n-1][0]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def number_of_paths(grid, k)
    m, n = grid.size, grid[0].size
    dp = Array.new(m) { Array.new(n) { Array.new(k, 0) } }
    dp[0][0][grid[0][0] % k] = 1
    (0...m).each do |i|
        (0...n).each do |j|
            next if i == 0 && j == 0
            (0...k).each do |val|
                if i > 0
                    dp[i][j][(val + grid[i][j]) % k] += dp[i-1][j][val]
                end
                if j > 0
                    dp[i][j][(val + grid[i][j]) % k] += dp[i][j-1][val]
                end
            end
        end
    end
    dp[m-1][n-1][0]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def numberOfPaths(grid: Array[Array[Int]], k: Int): Int = {
        val m = grid.length
        val n = grid(0).length
        val dp = Array.ofDim[Int](m, n, k)
        dp(0)(0)(grid(0)(0) % k) = 1
        for (i <- 0 until m) {
            for (j <- 0 until n) {
                if (i == 0 && j == 0) {
                    // do nothing
                } else {
                    for (val <- 0 until k) {
                        if (i > 0) dp(i)(j)((val + grid(i)(j)) % k) += dp(i-1)(j)(val)
                        if (j > 0) dp(i)(j)((val + grid(i)(j)) % k) += dp(i)(j-1)(val)
                    }
                }
            }
        }
        dp(m-1)(n-1)(0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
struct Solution;
impl Solution {
    pub fn number_of_paths(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let m = grid.len() as usize;
        let n = grid[0].len() as usize;
        let mut dp: Vec<Vec<Vec<i32>>> = vec![vec![vec![0; k as usize]; n]; m];
        dp[0][0][grid[0][0] as usize % k as usize] = 1;
        for i in 0..m {
            for j in 0..n {
                if i == 0 && j == 0 { continue; }
                for val in 0..k {
                    if i > 0 { dp[i][j][(val + grid[i][j]) as usize % k as usize] += dp[i-1][j][val as usize]; }
                    if j > 0 { dp[i][j][(val + grid[i][j]) as usize % k as usize] += dp[i][j-1][val as usize]; }
                }
            }
        }
        dp[m-1][n-1][0]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define (number-of-paths grid k)
    (let* (
        (m (length grid))
        (n (length (car grid)))
        (dp (make-array m n k)))
        (array-set! dp 0 0 (modulo (array-ref grid 0 0) k) 1)
        (for* (
            (i (range m))
            (j (range n)))
            (when (not (and (= i 0) (= j 0)))
                (for (
                    (val (range k)))
                    (when (> i 0)
                        (array-set! dp i j (modulo (+ val (array-ref grid i j)) k) (+ (array-ref dp i j (modulo (+ val (array-ref grid i j)) k)) (array-ref dp (- i 1) j val))))
                    (when (> j 0)
                        (array-set! dp i j (modulo (+ val (array-ref grid i j)) k) (+ (array-ref dp i j (modulo (+ val (array-ref grid i j)) k)) (array-ref dp i (- j 1) val))))))
        (array-ref dp (- m 1) (- n 1) 0))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
number_of_paths(Grid, K) ->
    M = length(Grid),
    N = length(hd(Grid)),
    DP = array:new([M, N, K], 0),
    array:set(0, 0, (element(1, hd(Grid)) rem K), 1, DP),
    number_of_paths(M, N, Grid, K, DP, 0, 0).

number_of_paths(M, N, Grid, K, DP, I, J) when I < M, J < N ->
    case {I, J} of
        {0, 0} -> number_of_paths(M, N, Grid, K, DP, I, J + 1);
        _ ->
            lists:foreach(fun(Val) ->
                case I > 0 of
                    true ->
                        NewVal = (Val + element(I, element(J, Grid)) rem K),
                        array:set(I, J, NewVal, array:get(I, J, NewVal) + array:get(I - 1, J, Val), DP);
                    false -> ok
                end,
                case J > 0 of
                    true ->
                        NewVal = (Val + element(I, element(J, Grid)) rem K),
                        array:set(I, J, NewVal, array:get(I, J, NewVal) + array:get(I, J - 1, Val), DP);
                    false -> ok
                end
            end, lists:seq(0, K - 1)),
            number_of_paths(M, N, Grid, K, DP, I + 1, 0)
    end;
number_of_paths(M, N, Grid, K, DP, I, J) when I == M, J == N ->
    array:get(M - 1, N - 1, 0, DP).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def number_of_paths(grid, k) do
    m = length(grid)
    n = length(Enum.at(grid, 0))
    dp = :array.new([m, n, k], 0)
    :array.set(0, 0, rem(Enum.at(Enum.at(grid, 0), 0), k), 1, dp)
    number_of_paths(m, n, grid, k, dp, 0, 0)
end

defp number_of_paths(m, n, grid, k, dp, i, j) when i < m and j < n do
    case {i, j} do
        {0, 0} -> number_of_paths(m, n, grid, k, dp, i, j + 1)
        _ ->
            Enum.each(0..(k - 1), fn val ->
                new_val = rem(val + Enum.at(Enum.at(grid, i), j), k)
                :array.set(i, j, new_val, :array.get(i, j, new_val) + :array.get(i - 1, j, val), dp)
                :array.set(i, j, new_val, :array.get(i, j, new_val) + :array.get(i, j - 1, val), dp)
            end)
            number_of_paths(m, n, grid, k, dp, i + 1, 0)
    end
end

defp number_of_paths(m, n, grid, k, dp, i, j) when i == m and j == n do
    :array.get(m - 1, n - 1, 0, dp)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(m*n*k), where m and n are the number of rows and columns in the grid, respectively, and k is the divisor. This is because we need to fill up the 3D DP array, which has a size of m*n*k.

- **Space Complexity:** The space complexity of this solution is also O(m*n*k), as we need to store the 3D DP array. However, we can optimize the space complexity by using a 2D DP array and iterating over the rows and columns of the grid, instead of storing the entire 3D array.

</div>
</details>
