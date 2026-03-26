---
layout: post
title: "Equal Sum Grid Partition II"
date: 2026-03-26 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Hash Table", "Matrix", "Enumeration", "Prefix Sum"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/equal-sum-grid-partition-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool canPartitionGrid(vector<vector<int>>&\
        \ grid) {\n        int m = grid.size();\n        int n = grid[0].size();\n \
        \       long long total_sum = 0;\n        vector<int> total_val_count(100001,\
        \ 0);\n        for (int i = 0; i < m; ++i) {\n            for (int j = 0; j\
        \ < n; ++j) {\n                total_sum += grid[i][j];\n                total_val_count[grid[i][j]]++;\n\
        \            }\n        }\n\n        // Horizontal cuts\n        vector<long\
        \ long> row_sums(m, 0);\n        for (int i = 0; i < m; ++i)\n            for\
        \ (int j = 0; j < n; ++j) row_sums[i] += grid[i][j];\n\n        long long s1\
        \ = 0;\n        vector<int> count1(100001, 0);\n        for (int i = 0; i <\
        \ m - 1; ++i) {\n            for (int j = 0; j < n; ++j) count1[grid[i][j]]++;\n\
        \            s1 += row_sums[i];\n            long long s2 = total_sum - s1;\n\
        \            if (s1 == s2) return true;\n            if (s1 > s2) {\n      \
        \          long long target = s1 - s2;\n                if (target <= 100000\
        \ && count1[target] > 0) {\n                    if (n > 1 && (i + 1) > 1) return\
        \ true;\n                    if (n > 1 && (target == grid[0][0] || target ==\
        \ grid[0][n - 1])) return true;\n                    if ((i + 1) > 1 && (target\
        \ == grid[0][0] || target == grid[i][0])) return true;\n                   \
        \ if (n == 1 && (i + 1) == 1 && target == grid[0][0]) return true;\n       \
        \         }\n            }\n            if (s2 > s1) {\n                long\
        \ long target = s2 - s1;\n                if (target <= 100000 && (total_val_count[target]\
        \ - count1[target]) > 0) {\n                    int h2 = m - 1 - i;\n      \
        \              if (n > 1 && h2 > 1) return true;\n                    if (n\
        \ > 1 && (target == grid[i + 1][0] || target == grid[i + 1][n - 1])) return\
        \ true;\n                    if (h2 > 1 && (target == grid[i + 1][0] || target\
        \ == grid[m - 1][0])) return true;\n                    if (n == 1 && h2 ==\
        \ 1 && target == grid[i + 1][0]) return true;\n                }\n         \
        \   }\n        }\n\n        // Vertical cuts\n        vector<long long> col_sums(n,\
        \ 0);\n        for (int j = 0; j < n; ++j)\n            for (int i = 0; i <\
        \ m; ++i) col_sums[j] += grid[i][j];\n\n        s1 = 0;\n        fill(count1.begin(),\
        \ count1.end(), 0);\n        for (int j = 0; j < n - 1; ++j) {\n           \
        \ for (int i = 0; i < m; ++i) count1[grid[i][j]]++;\n            s1 += col_sums[j];\n\
        \            long long s2 = total_sum - s1;\n            if (s1 == s2) return\
        \ true;\n            if (s1 > s2) {\n                long long target = s1 -\
        \ s2;\n                if (target <= 100000 && count1[target] > 0) {\n     \
        \               if (m > 1 && (j + 1) > 1) return true;\n                   \
        \ if (m > 1 && (target == grid[0][0] || target == grid[m - 1][0])) return true;\n\
        \                    if ((j + 1) > 1 && (target == grid[0][0] || target == grid[0][j]))\
        \ return true;\n                    if (m == 1 && (j + 1) == 1 && target ==\
        \ grid[0][0]) return true;\n                }\n            }\n            if\
        \ (s2 > s1) {\n                long long target = s2 - s1;\n               \
        \ if (target <= 100000 && (total_val_count[target] - count1[target]) > 0) {\n\
        \                    int w2 = n - 1 - j;\n                    if (m > 1 && w2\
        \ > 1) return true;\n                    if (m > 1 && (target == grid[0][j +\
        \ 1] || target == grid[m - 1][j + 1])) return true;\n                    if\
        \ (w2 > 1 && (target == grid[0][j + 1] || target == grid[0][n - 1])) return\
        \ true;\n                    if (m == 1 && w2 == 1 && target == grid[0][j +\
        \ 1]) return true;\n                }\n            }\n        }\n        return\
        \ false;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public boolean canPartitionGrid(int[][]\
        \ grid) {\n        int m = grid.length;\n        int n = grid[0].length;\n \
        \       long totalSum = 0;\n        int[] totalValCount = new int[100001];\n\
        \        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++)\
        \ {\n                totalSum += grid[i][j];\n                totalValCount[grid[i][j]]++;\n\
        \            }\n        }\n\n        long[] rowSums = new long[m];\n       \
        \ for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) rowSums[i]\
        \ += grid[i][j];\n        }\n\n        long s1 = 0;\n        int[] count1 =\
        \ new int[100001];\n        for (int i = 0; i < m - 1; i++) {\n            for\
        \ (int j = 0; j < n; j++) count1[grid[i][j]]++;\n            s1 += rowSums[i];\n\
        \            long s2 = totalSum - s1;\n            if (s1 == s2) return true;\n\
        \            if (s1 > s2) {\n                long target = s1 - s2;\n      \
        \          if (target <= 100000 && count1[(int)target] > 0) {\n            \
        \        if (n > 1 && (i + 1) > 1) return true;\n                    if (n >\
        \ 1 && (target == grid[0][0] || target == grid[0][n - 1])) return true;\n  \
        \                  if ((i + 1) > 1 && (target == grid[0][0] || target == grid[i][0]))\
        \ return true;\n                    if (n == 1 && (i + 1) == 1 && target ==\
        \ grid[0][0]) return true;\n                }\n            }\n            if\
        \ (s2 > s1) {\n                long target = s2 - s1;\n                if (target\
        \ <= 100000 && (totalValCount[(int)target] - count1[(int)target]) > 0) {\n \
        \                   int h2 = m - 1 - i;\n                    if (n > 1 && h2\
        \ > 1) return true;\n                    if (n > 1 && (target == grid[i + 1][0]\
        \ || target == grid[i + 1][n - 1])) return true;\n                    if (h2\
        \ > 1 && (target == grid[i + 1][0] || target == grid[m - 1][0])) return true;\n\
        \                    if (n == 1 && h2 == 1 && target == grid[i + 1][0]) return\
        \ true;\n                }\n            }\n        }\n\n        long[] colSums\
        \ = new long[n];\n        for (int j = 0; j < n; j++) {\n            for (int\
        \ i = 0; i < m; i++) colSums[j] += grid[i][j];\n        }\n\n        s1 = 0;\n\
        \        Arrays.fill(count1, 0);\n        for (int j = 0; j < n - 1; j++) {\n\
        \            for (int i = 0; i < m; i++) count1[grid[i][j]]++;\n           \
        \ s1 += colSums[j];\n            long s2 = totalSum - s1;\n            if (s1\
        \ == s2) return true;\n            if (s1 > s2) {\n                long target\
        \ = s1 - s2;\n                if (target <= 100000 && count1[(int)target] >\
        \ 0) {\n                    if (m > 1 && (j + 1) > 1) return true;\n       \
        \             if (m > 1 && (target == grid[0][0] || target == grid[m - 1][0]))\
        \ return true;\n                    if ((j + 1) > 1 && (target == grid[0][0]\
        \ || target == grid[0][j])) return true;\n                    if (m == 1 &&\
        \ (j + 1) == 1 && target == grid[0][0]) return true;\n                }\n  \
        \          }\n            if (s2 > s1) {\n                long target = s2 -\
        \ s1;\n                if (target <= 100000 && (totalValCount[(int)target] -\
        \ count1[(int)target]) > 0) {\n                    int w2 = n - 1 - j;\n   \
        \                 if (m > 1 && w2 > 1) return true;\n                    if\
        \ (m > 1 && (target == grid[0][j + 1] || target == grid[m - 1][j + 1])) return\
        \ true;\n                    if (w2 > 1 && (target == grid[0][j + 1] || target\
        \ == grid[0][n - 1])) return true;\n                    if (m == 1 && w2 ==\
        \ 1 && target == grid[0][j + 1]) return true;\n                }\n         \
        \   }\n        }\n        return false;\n    }\n}"
      python: "class Solution(object):\n    def canPartitionGrid(self, grid):\n    \
        \    m, n = len(grid), len(grid[0])\n        total_sum = sum(sum(row) for row\
        \ in grid)\n        total_val_count = {}\n        for row in grid:\n       \
        \     for val in row:\n                total_val_count[val] = total_val_count.get(val,\
        \ 0) + 1\n\n        def check_h():\n            row_sums = [sum(row) for row\
        \ in grid]\n            s1, count1 = 0, {}\n            for i in range(m - 1):\n\
        \                for val in grid[i]: count1[val] = count1.get(val, 0) + 1\n\
        \                s1 += row_sums[i]\n                s2 = total_sum - s1\n  \
        \              if s1 == s2: return True\n                if s1 > s2:\n     \
        \               target = s1 - s2\n                    if target <= 100000 and\
        \ count1.get(target, 0) > 0:\n                        if n > 1 and i + 1 > 1:\
        \ return True\n                        if n > 1 and (target == grid[0][0] or\
        \ target == grid[0][n-1]): return True\n                        if i + 1 > 1\
        \ and (target == grid[0][0] or target == grid[i][0]): return True\n        \
        \                if n == 1 and i + 1 == 1 and target == grid[0][0]: return True\n\
        \                if s2 > s1:\n                    target = s2 - s1\n       \
        \             if target <= 100000 and total_val_count.get(target, 0) - count1.get(target,\
        \ 0) > 0:\n                        h2 = m - 1 - i\n                        if\
        \ n > 1 and h2 > 1: return True\n                        if n > 1 and (target\
        \ == grid[i+1][0] or target == grid[i+1][n-1]): return True\n              \
        \          if h2 > 1 and (target == grid[i+1][0] or target == grid[m-1][0]):\
        \ return True\n                        if n == 1 and h2 == 1 and target == grid[i+1][0]:\
        \ return True\n            return False\n\n        def check_v():\n        \
        \    col_sums = [sum(grid[r][c] for r in range(m)) for c in range(n)]\n    \
        \        s1, count1 = 0, {}\n            for j in range(n - 1):\n          \
        \      for r in range(m): val = grid[r][j]; count1[val] = count1.get(val, 0)\
        \ + 1\n                s1 += col_sums[j]\n                s2 = total_sum - s1\n\
        \                if s1 == s2: return True\n                if s1 > s2:\n   \
        \                 target = s1 - s2\n                    if target <= 100000\
        \ and count1.get(target, 0) > 0:\n                        if m > 1 and j + 1\
        \ > 1: return True\n                        if m > 1 and (target == grid[0][0]\
        \ or target == grid[m-1][0]): return True\n                        if j + 1\
        \ > 1 and (target == grid[0][0] or target == grid[0][j]): return True\n    \
        \                    if m == 1 and j + 1 == 1 and target == grid[0][0]: return\
        \ True\n                if s2 > s1:\n                    target = s2 - s1\n\
        \                    if target <= 100000 and total_val_count.get(target, 0)\
        \ - count1.get(target, 0) > 0:\n                        w2 = n - 1 - j\n   \
        \                     if m > 1 and w2 > 1: return True\n                   \
        \     if m > 1 and (target == grid[0][j+1] or target == grid[m-1][j+1]): return\
        \ True\n                        if w2 > 1 and (target == grid[0][j+1] or target\
        \ == grid[0][n-1]): return True\n                        if m == 1 and w2 ==\
        \ 1 and target == grid[0][j+1]: return True\n            return False\n\n  \
        \      return check_h() or check_v()"
      python3: "class Solution:\n    def canPartitionGrid(self, grid: List[List[int]])\
        \ -> bool:\n        m, n = len(grid), len(grid[0])\n        total_sum = sum(sum(row)\
        \ for row in grid)\n        total_val_count = {}\n        for row in grid:\n\
        \            for val in row:\n                total_val_count[val] = total_val_count.get(val,\
        \ 0) + 1\n\n        def check_h():\n            row_sums = [sum(row) for row\
        \ in grid]\n            s1, count1 = 0, {}\n            for i in range(m - 1):\n\
        \                for val in grid[i]: count1[val] = count1.get(val, 0) + 1\n\
        \                s1 += row_sums[i]\n                s2 = total_sum - s1\n  \
        \              if s1 == s2: return True\n                if s1 > s2:\n     \
        \               target = s1 - s2\n                    if target <= 100000 and\
        \ count1.get(target, 0) > 0:\n                        if n > 1 and i + 1 > 1:\
        \ return True\n                        if n > 1 and (target == grid[0][0] or\
        \ target == grid[0][n-1]): return True\n                        if i + 1 > 1\
        \ and (target == grid[0][0] or target == grid[i][0]): return True\n        \
        \                if n == 1 and i + 1 == 1 and target == grid[0][0]: return True\n\
        \                if s2 > s1:\n                    target = s2 - s1\n       \
        \             if target <= 100000 and total_val_count.get(target, 0) - count1.get(target,\
        \ 0) > 0:\n                        h2 = m - 1 - i\n                        if\
        \ n > 1 and h2 > 1: return True\n                        if n > 1 and (target\
        \ == grid[i+1][0] or target == grid[i+1][n-1]): return True\n              \
        \          if h2 > 1 and (target == grid[i+1][0] or target == grid[m-1][0]):\
        \ return True\n                        if n == 1 and h2 == 1 and target == grid[i+1][0]:\
        \ return True\n            return False\n\n        def check_v():\n        \
        \    col_sums = [sum(grid[r][c] for r in range(m)) for c in range(n)]\n    \
        \        s1, count1 = 0, {}\n            for j in range(n - 1):\n          \
        \      for r in range(m): val = grid[r][j]; count1[val] = count1.get(val, 0)\
        \ + 1\n                s1 += col_sums[j]\n                s2 = total_sum - s1\n\
        \                if s1 == s2: return True\n                if s1 > s2:\n   \
        \                 target = s1 - s2\n                    if target <= 100000\
        \ and count1.get(target, 0) > 0:\n                        if m > 1 and j + 1\
        \ > 1: return True\n                        if m > 1 and (target == grid[0][0]\
        \ or target == grid[m-1][0]): return True\n                        if j + 1\
        \ > 1 and (target == grid[0][0] or target == grid[0][j]): return True\n    \
        \                    if m == 1 and j + 1 == 1 and target == grid[0][0]: return\
        \ True\n                if s2 > s1:\n                    target = s2 - s1\n\
        \                    if target <= 100000 and total_val_count.get(target, 0)\
        \ - count1.get(target, 0) > 0:\n                        w2 = n - 1 - j\n   \
        \                     if m > 1 and w2 > 1: return True\n                   \
        \     if m > 1 and (target == grid[0][j+1] or target == grid[m-1][j+1]): return\
        \ True\n                        if w2 > 1 and (target == grid[0][j+1] or target\
        \ == grid[0][n-1]): return True\n                        if m == 1 and w2 ==\
        \ 1 and target == grid[0][j+1]: return True\n            return False\n\n  \
        \      return check_h() or check_v()"
      c: "bool canPartitionGrid(int** grid, int gridSize, int* gridColSize) {\n    int\
        \ m = gridSize;\n    int n = gridColSize[0];\n    long long total_sum = 0;\n\
        \    int total_val_count[100001] = {0};\n    for (int i = 0; i < m; i++) {\n\
        \        for (int j = 0; j < n; j++) {\n            total_sum += grid[i][j];\n\
        \            total_val_count[grid[i][j]]++;\n        }\n    }\n\n    long long\
        \ row_sums[m];\n    for (int i = 0; i < m; i++) {\n        row_sums[i] = 0;\n\
        \        for (int j = 0; j < n; j++) row_sums[i] += grid[i][j];\n    }\n\n \
        \   long long s1 = 0;\n    int count1[100001] = {0};\n    for (int i = 0; i\
        \ < m - 1; i++) {\n        for (int j = 0; j < n; j++) count1[grid[i][j]]++;\n\
        \        s1 += row_sums[i];\n        long long s2 = total_sum - s1;\n      \
        \  if (s1 == s2) return true;\n        if (s1 > s2) {\n            long long\
        \ target = s1 - s2;\n            if (target <= 100000 && count1[target] > 0)\
        \ {\n                if (n > 1 && (i + 1) > 1) return true;\n              \
        \  if (n > 1 && (target == grid[0][0] || target == grid[0][n - 1])) return true;\n\
        \                if ((i + 1) > 1 && (target == grid[0][0] || target == grid[i][0]))\
        \ return true;\n                if (n == 1 && (i + 1) == 1 && target == grid[0][0])\
        \ return true;\n            }\n        }\n        if (s2 > s1) {\n         \
        \   long long target = s2 - s1;\n            if (target <= 100000 && (total_val_count[target]\
        \ - count1[target]) > 0) {\n                int h2 = m - 1 - i;\n          \
        \      if (n > 1 && h2 > 1) return true;\n                if (n > 1 && (target\
        \ == grid[i + 1][0] || target == grid[i + 1][n - 1])) return true;\n       \
        \         if (h2 > 1 && (target == grid[i + 1][0] || target == grid[m - 1][0]))\
        \ return true;\n                if (n == 1 && h2 == 1 && target == grid[i +\
        \ 1][0]) return true;\n            }\n        }\n    }\n\n    long long col_sums[n];\n\
        \    for (int j = 0; j < n; j++) {\n        col_sums[j] = 0;\n        for (int\
        \ i = 0; i < m; i++) col_sums[j] += grid[i][j];\n    }\n\n    s1 = 0;\n    memset(count1,\
        \ 0, sizeof(count1));\n    for (int j = 0; j < n - 1; j++) {\n        for (int\
        \ i = 0; i < m; i++) count1[grid[i][j]]++;\n        s1 += col_sums[j];\n   \
        \     long long s2 = total_sum - s1;\n        if (s1 == s2) return true;\n \
        \       if (s1 > s2) {\n            long long target = s1 - s2;\n          \
        \  if (target <= 100000 && count1[target] > 0) {\n                if (m > 1\
        \ && (j + 1) > 1) return true;\n                if (m > 1 && (target == grid[0][0]\
        \ || target == grid[m - 1][0])) return true;\n                if ((j + 1) >\
        \ 1 && (target == grid[0][0] || target == grid[0][j])) return true;\n      \
        \          if (m == 1 && (j + 1) == 1 && target == grid[0][0]) return true;\n\
        \            }\n        }\n        if (s2 > s1) {\n            long long target\
        \ = s2 - s1;\n            if (target <= 100000 && (total_val_count[target] -\
        \ count1[target]) > 0) {\n                int w2 = n - 1 - j;\n            \
        \    if (m > 1 && w2 > 1) return true;\n                if (m > 1 && (target\
        \ == grid[0][j + 1] || target == grid[m - 1][j + 1])) return true;\n       \
        \         if (w2 > 1 && (target == grid[0][j + 1] || target == grid[0][n - 1]))\
        \ return true;\n                if (m == 1 && w2 == 1 && target == grid[0][j\
        \ + 1]) return true;\n            }\n        }\n    }\n    return false;\n}"
      csharp: "public class Solution {\n    public bool CanPartitionGrid(int[][] grid)\
        \ {\n        int m = grid.Length;\n        int n = grid[0].Length;\n       \
        \ long totalSum = 0;\n        int[] totalValCount = new int[100001];\n     \
        \   for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n\
        \                totalSum += grid[i][j];\n                totalValCount[grid[i][j]]++;\n\
        \            }\n        }\n\n        long[] rowSums = new long[m];\n       \
        \ for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) rowSums[i]\
        \ += grid[i][j];\n        }\n\n        long s1 = 0;\n        int[] count1 =\
        \ new int[100001];\n        for (int i = 0; i < m - 1; i++) {\n            for\
        \ (int j = 0; j < n; j++) count1[grid[i][j]]++;\n            s1 += rowSums[i];\n\
        \            long s2 = totalSum - s1;\n            if (s1 == s2) return true;\n\
        \            if (s1 > s2) {\n                long target = s1 - s2;\n      \
        \          if (target <= 100000 && count1[(int)target] > 0) {\n            \
        \        if (n > 1 && (i + 1) > 1) return true;\n                    if (n >\
        \ 1 && (target == grid[0][0] || target == grid[0][n - 1])) return true;\n  \
        \                  if ((i + 1) > 1 && (target == grid[0][0] || target == grid[i][0]))\
        \ return true;\n                    if (n == 1 && (i + 1) == 1 && target ==\
        \ grid[0][0]) return true;\n                }\n            }\n            if\
        \ (s2 > s1) {\n                long target = s2 - s1;\n                if (target\
        \ <= 100000 && (totalValCount[(int)target] - count1[(int)target]) > 0) {\n \
        \                   int h2 = m - 1 - i;\n                    if (n > 1 && h2\
        \ > 1) return true;\n                    if (n > 1 && (target == grid[i + 1][0]\
        \ || target == grid[i + 1][n - 1])) return true;\n                    if (h2\
        \ > 1 && (target == grid[i + 1][0] || target == grid[m - 1][0])) return true;\n\
        \                    if (n == 1 && h2 == 1 && target == grid[i + 1][0]) return\
        \ true;\n                }\n            }\n        }\n\n        long[] colSums\
        \ = new long[n];\n        for (int j = 0; j < n; j++) {\n            for (int\
        \ i = 0; i < m; i++) colSums[j] += grid[i][j];\n        }\n\n        s1 = 0;\n\
        \        System.Array.Fill(count1, 0);\n        for (int j = 0; j < n - 1; j++)\
        \ {\n            for (int i = 0; i < m; i++) count1[grid[i][j]]++;\n       \
        \     s1 += colSums[j];\n            long s2 = totalSum - s1;\n            if\
        \ (s1 == s2) return true;\n            if (s1 > s2) {\n                long\
        \ target = s1 - s2;\n                if (target <= 100000 && count1[(int)target]\
        \ > 0) {\n                    if (m > 1 && (j + 1) > 1) return true;\n     \
        \               if (m > 1 && (target == grid[0][0] || target == grid[m - 1][0]))\
        \ return true;\n                    if ((j + 1) > 1 && (target == grid[0][0]\
        \ || target == grid[0][j])) return true;\n                    if (m == 1 &&\
        \ (j + 1) == 1 && target == grid[0][0]) return true;\n                }\n  \
        \          }\n            if (s2 > s1) {\n                long target = s2 -\
        \ s1;\n                if (target <= 100000 && (totalValCount[(int)target] -\
        \ count1[(int)target]) > 0) {\n                    int w2 = n - 1 - j;\n   \
        \                 if (m > 1 && w2 > 1) return true;\n                    if\
        \ (m > 1 && (target == grid[0][j + 1] || target == grid[m - 1][j + 1])) return\
        \ true;\n                    if (w2 > 1 && (target == grid[0][j + 1] || target\
        \ == grid[0][n - 1])) return true;\n                    if (m == 1 && w2 ==\
        \ 1 && target == grid[0][j + 1]) return true;\n                }\n         \
        \   }\n        }\n        return false;\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @return {boolean}\n */\nvar\
        \ canPartitionGrid = function(grid) {\n    const m = grid.length;\n    const\
        \ n = grid[0].length;\n    let totalSum = 0;\n    const totalValCount = new\
        \ Int32Array(100001);\n    for (let i = 0; i < m; i++) {\n        for (let j\
        \ = 0; j < n; j++) {\n            totalSum += grid[i][j];\n            totalValCount[grid[i][j]]++;\n\
        \        }\n    }\n\n    const rowSums = new BigInt64Array(m);\n    for (let\
        \ i = 0; i < m; i++) {\n        let s = 0n;\n        for (let j = 0; j < n;\
        \ j++) s += BigInt(grid[i][j]);\n        rowSums[i] = s;\n    }\n\n    let s1\
        \ = 0n;\n    const count1 = new Int32Array(100001);\n    for (let i = 0; i <\
        \ m - 1; i++) {\n        for (let j = 0; j < n; j++) count1[grid[i][j]]++;\n\
        \        s1 += rowSums[i];\n        let s2 = BigInt(totalSum) - s1;\n      \
        \  if (s1 === s2) return true;\n        if (s1 > s2) {\n            let target\
        \ = Number(s1 - s2);\n            if (target <= 100000 && count1[target] > 0)\
        \ {\n                if (n > 1 && (i + 1) > 1) return true;\n              \
        \  if (n > 1 && (target === grid[0][0] || target === grid[0][n - 1])) return\
        \ true;\n                if ((i + 1) > 1 && (target === grid[0][0] || target\
        \ === grid[i][0])) return true;\n                if (n === 1 && (i + 1) ===\
        \ 1 && target === grid[0][0]) return true;\n            }\n        }\n     \
        \   if (s2 > s1) {\n            let target = Number(s2 - s1);\n            if\
        \ (target <= 100000 && (totalValCount[target] - count1[target]) > 0) {\n   \
        \             let h2 = m - 1 - i;\n                if (n > 1 && h2 > 1) return\
        \ true;\n                if (n > 1 && (target === grid[i + 1][0] || target ===\
        \ grid[i + 1][n - 1])) return true;\n                if (h2 > 1 && (target ===\
        \ grid[i + 1][0] || target === grid[m - 1][0])) return true;\n             \
        \   if (n === 1 && h2 === 1 && target === grid[i + 1][0]) return true;\n   \
        \         }\n        }\n    }\n\n    const colSums = new BigInt64Array(n);\n\
        \    for (let j = 0; j < n; j++) {\n        let s = 0n;\n        for (let i\
        \ = 0; i < m; i++) s += BigInt(grid[i][j]);\n        colSums[j] = s;\n    }\n\
        \n    s1 = 0n;\n    count1.fill(0);\n    for (let j = 0; j < n - 1; j++) {\n\
        \        for (let i = 0; i < m; i++) count1[grid[i][j]]++;\n        s1 += colSums[j];\n\
        \        let s2 = BigInt(totalSum) - s1;\n        if (s1 === s2) return true;\n\
        \        if (s1 > s2) {\n            let target = Number(s1 - s2);\n       \
        \     if (target <= 100000 && count1[target] > 0) {\n                if (m >\
        \ 1 && (j + 1) > 1) return true;\n                if (m > 1 && (target === grid[0][0]\
        \ || target === grid[m - 1][0])) return true;\n                if ((j + 1) >\
        \ 1 && (target === grid[0][0] || target === grid[0][j])) return true;\n    \
        \            if (m === 1 && (j + 1) === 1 && target === grid[0][0]) return true;\n\
        \            }\n        }\n        if (s2 > s1) {\n            let target =\
        \ Number(s2 - s1);\n            if (target <= 100000 && (totalValCount[target]\
        \ - count1[target]) > 0) {\n                let w2 = n - 1 - j;\n          \
        \      if (m > 1 && w2 > 1) return true;\n                if (m > 1 && (target\
        \ === grid[0][j + 1] || target === grid[m - 1][j + 1])) return true;\n     \
        \           if (w2 > 1 && (target === grid[0][j + 1] || target === grid[0][n\
        \ - 1])) return true;\n                if (m === 1 && w2 === 1 && target ===\
        \ grid[0][j + 1]) return true;\n            }\n        }\n    }\n    return\
        \ false;\n};"
      typescript: "function canPartitionGrid(grid: number[][]): boolean {\n    const\
        \ m = grid.length;\n    const n = grid[0].length;\n    let totalSum = 0;\n \
        \   const rowSums = new Array(m).fill(0);\n    const colSums = new Array(n).fill(0);\n\
        \    let map2 = new Map<number, number>();\n\n    for (let i = 0; i < m; i++)\
        \ {\n        for (let j = 0; j < n; j++) {\n            const val = grid[i][j];\n\
        \            totalSum += val;\n            rowSums[i] += val;\n            colSums[j]\
        \ += val;\n            map2.set(val, (map2.get(val) || 0) + 1);\n        }\n\
        \    }\n\n    const isValid = (x: number, r_start: number, r_end: number, c_start:\
        \ number, c_end: number, map: Map<number, number>): boolean => {\n        const\
        \ H = r_end - r_start + 1;\n        const W = c_end - c_start + 1;\n       \
        \ if (H >= 2 && W >= 2) return map.has(x);\n        if (H === 1 && W === 1)\
        \ return grid[r_start][c_start] === x;\n        if (H === 1) return grid[r_start][c_start]\
        \ === x || grid[r_start][c_end] === x;\n        if (W === 1) return grid[r_start][c_start]\
        \ === x || grid[r_end][c_start] === x;\n        return false;\n    };\n\n  \
        \  let s1 = 0, map1 = new Map<number, number>();\n    for (let i = 0; i < m\
        \ - 1; i++) {\n        for (let j = 0; j < n; j++) {\n            const val\
        \ = grid[i][j];\n            map1.set(val, (map1.get(val) || 0) + 1);\n    \
        \        const count2 = map2.get(val)!;\n            if (count2 === 1) map2.delete(val);\
        \ else map2.set(val, count2 - 1);\n        }\n        s1 += rowSums[i];\n  \
        \      let s2 = totalSum - s1;\n        if (s1 === s2) return true;\n      \
        \  if (s1 > s2) { if (isValid(s1 - s2, 0, i, 0, n - 1, map1)) return true; }\n\
        \        else { if (isValid(s2 - s1, i + 1, m - 1, 0, n - 1, map2)) return true;\
        \ }\n    }\n\n    s1 = 0; map1.clear(); map2.clear();\n    for (let i = 0; i\
        \ < m; i++) {\n        for (let j = 0; j < n; j++) {\n            const val\
        \ = grid[i][j];\n            map2.set(val, (map2.get(val) || 0) + 1);\n    \
        \    }\n    }\n\n    for (let j = 0; j < n - 1; j++) {\n        for (let i =\
        \ 0; i < m; i++) {\n            const val = grid[i][j];\n            map1.set(val,\
        \ (map1.get(val) || 0) + 1);\n            const count2 = map2.get(val)!;\n \
        \           if (count2 === 1) map2.delete(val); else map2.set(val, count2 -\
        \ 1);\n        }\n        s1 += colSums[j];\n        let s2 = totalSum - s1;\n\
        \        if (s1 === s2) return true;\n        if (s1 > s2) { if (isValid(s1\
        \ - s2, 0, m - 1, 0, j, map1)) return true; }\n        else { if (isValid(s2\
        \ - s1, 0, m - 1, j + 1, n - 1, map2)) return true; }\n    }\n\n    return false;\n\
        };"
      php: "class Solution {\n    function canPartitionGrid($grid) {\n        $m = count($grid);\n\
        \        $n = count($grid[0]);\n        $totalSum = 0;\n        $rowSums = array_fill(0,\
        \ $m, 0);\n        $colSums = array_fill(0, $n, 0);\n        $map2 = [];\n\n\
        \        for ($i = 0; $i < $m; $i++) {\n            for ($j = 0; $j < $n; $j++)\
        \ {\n                $val = $grid[$i][$j];\n                $totalSum += $val;\n\
        \                $rowSums[$i] += $val;\n                $colSums[$j] += $val;\n\
        \                $map2[$val] = ($map2[$val] ?? 0) + 1;\n            }\n    \
        \    }\n\n        $isValid = function($x, $rs, $re, $cs, $ce, &$map) use (&$grid)\
        \ {\n            $h = $re - $rs + 1;\n            $w = $ce - $cs + 1;\n    \
        \        if ($h >= 2 && $w >= 2) return isset($map[$x]);\n            if ($h\
        \ === 1 && $w === 1) return $grid[$rs][$cs] === $x;\n            if ($h ===\
        \ 1) return $grid[$rs][$cs] === $x || $grid[$rs][$ce] === $x;\n            if\
        \ ($w === 1) return $grid[$rs][$cs] === $x || $grid[$re][$cs] === $x;\n    \
        \        return false;\n        };\n\n        $s1 = 0; $map1 = [];\n       \
        \ for ($i = 0; $i < $m - 1; $i++) {\n            foreach ($grid[$i] as $val)\
        \ {\n                $map1[$val] = ($map1[$val] ?? 0) + 1;\n               \
        \ if (--$map2[$val] === 0) unset($map2[$val]);\n            }\n            $s1\
        \ += $rowSums[$i];\n            $s2 = $totalSum - $s1;\n            if ($s1\
        \ === $s2) return true;\n            if ($s1 > $s2) { if ($isValid($s1 - $s2,\
        \ 0, $i, 0, $n - 1, $map1)) return true; }\n            else { if ($isValid($s2\
        \ - $s1, $i + 1, $m - 1, 0, $n - 1, $map2)) return true; }\n        }\n\n  \
        \      $s1 = 0; $map1 = []; $map2 = [];\n        foreach ($grid as $row) foreach\
        \ ($row as $v) $map2[$v] = ($map2[$v] ?? 0) + 1;\n        for ($j = 0; $j <\
        \ $n - 1; $j++) {\n            for ($i = 0; $i < $m; $i++) {\n             \
        \   $val = $grid[$i][$j];\n                $map1[$val] = ($map1[$val] ?? 0)\
        \ + 1;\n                if (--$map2[$val] === 0) unset($map2[$val]);\n     \
        \       }\n            $s1 += $colSums[$j];\n            $s2 = $totalSum - $s1;\n\
        \            if ($s1 === $s2) return true;\n            if ($s1 > $s2) { if\
        \ ($isValid($s1 - $s2, 0, $m - 1, 0, $j, $map1)) return true; }\n          \
        \  else { if ($isValid($s2 - $s1, 0, $m - 1, $j + 1, $n - 1, $map2)) return\
        \ true; }\n        }\n        return false;\n    }\n}"
      swift: "class Solution {\n    func canPartitionGrid(_ grid: [[Int]]) -> Bool {\n\
        \        let m = grid.count\n        let n = grid[0].count\n        var totalSum\
        \ = 0\n        var rowSums = Array(repeating: 0, count: m)\n        var colSums\
        \ = Array(repeating: 0, count: n)\n        var map2 = [Int: Int]()\n\n     \
        \   for i in 0..<m {\n            for j in 0..<n {\n                let val\
        \ = grid[i][j]\n                totalSum += val\n                rowSums[i]\
        \ += val\n                colSums[j] += val\n                map2[val, default:\
        \ 0] += 1\n            }\n        }\n\n        func isValid(_ x: Int, _ rs:\
        \ Int, _ re: Int, _ cs: Int, _ ce: Int, _ map: [Int: Int]) -> Bool {\n     \
        \       let h = re - rs + 1, w = ce - cs + 1\n            if h >= 2 && w >=\
        \ 2 { return map[x] != nil }\n            if h == 1 && w == 1 { return grid[rs][cs]\
        \ == x }\n            if h == 1 { return grid[rs][cs] == x || grid[rs][ce] ==\
        \ x }\n            if w == 1 { return grid[rs][cs] == x || grid[re][cs] == x\
        \ }\n            return false\n        }\n\n        var s1 = 0, map1 = [Int:\
        \ Int]()\n        for i in 0..<m - 1 {\n            for j in 0..<n {\n     \
        \           let val = grid[i][j]\n                map1[val, default: 0] += 1\n\
        \                map2[val]! -= 1\n                if map2[val] == 0 { map2[val]\
        \ = nil }\n            }\n            s1 += rowSums[i]\n            let s2 =\
        \ totalSum - s1\n            if s1 == s2 { return true }\n            if s1\
        \ > s2 { if isValid(s1 - s2, 0, i, 0, n - 1, map1) { return true } }\n     \
        \       else { if isValid(s2 - s1, i + 1, m - 1, 0, n - 1, map2) { return true\
        \ } }\n        }\n\n        s1 = 0; map1 = [:]; map2 = [:]\n        for r in\
        \ grid { for v in r { map2[v, default: 0] += 1 } }\n        for j in 0..<n -\
        \ 1 {\n            for i in 0..<m {\n                let val = grid[i][j]\n\
        \                map1[val, default: 0] += 1\n                map2[val]! -= 1\n\
        \                if map2[val] == 0 { map2[val] = nil }\n            }\n    \
        \        s1 += colSums[j]\n            let s2 = totalSum - s1\n            if\
        \ s1 == s2 { return true }\n            if s1 > s2 { if isValid(s1 - s2, 0,\
        \ m - 1, 0, j, map1) { return true } }\n            else { if isValid(s2 - s1,\
        \ 0, m - 1, j + 1, n - 1, map2) { return true } }\n        }\n        return\
        \ false\n    }\n}"
      kotlin: "class Solution {\n    fun canPartitionGrid(grid: Array<IntArray>): Boolean\
        \ {\n        val m = grid.size\n        val n = grid[0].size\n        var totalSum:\
        \ Long = 0\n        val rowSums = LongArray(m)\n        val colSums = LongArray(n)\n\
        \        val map2 = HashMap<Int, Int>()\n        for (i in 0 until m) {\n  \
        \          for (j in 0 until n) {\n                val v = grid[i][j]\n    \
        \            totalSum += v\n                rowSums[i] += v.toLong()\n     \
        \           colSums[j] += v.toLong()\n                map2[v] = map2.getOrDefault(v,\
        \ 0) + 1\n            }\n        }\n        fun isValid(x: Long, rs: Int, re:\
        \ Int, cs: Int, ce: Int, map: HashMap<Int, Int>): Boolean {\n            val\
        \ h = re - rs + 1\n            val w = ce - cs + 1\n            if (x > Int.MAX_VALUE)\
        \ return false\n            val xi = x.toInt()\n            if (h >= 2 && w\
        \ >= 2) return map.containsKey(xi)\n            if (h == 1 && w == 1) return\
        \ grid[rs][cs] == xi\n            if (h == 1) return grid[rs][cs] == xi || grid[rs][ce]\
        \ == xi\n            if (w == 1) return grid[rs][cs] == xi || grid[re][cs] ==\
        \ xi\n            return false\n        }\n        var s1: Long = 0\n      \
        \  val map1 = HashMap<Int, Int>()\n        for (i in 0 until m - 1) {\n    \
        \        for (j in 0 until n) {\n                val v = grid[i][j]\n      \
        \          map1[v] = map1.getOrDefault(v, 0) + 1\n                map2[v] =\
        \ map2[v]!! - 1\n                if (map2[v] == 0) map2.remove(v)\n        \
        \    }\n            s1 += rowSums[i]\n            val s2 = totalSum - s1\n \
        \           if (s1 == s2) return true\n            if (s1 > s2) { if (isValid(s1\
        \ - s2, 0, i, 0, n - 1, map1)) return true }\n            else { if (isValid(s2\
        \ - s1, i + 1, m - 1, 0, n - 1, map2)) return true }\n        }\n        s1\
        \ = 0; map1.clear(); map2.clear()\n        for (row in grid) for (v in row)\
        \ map2[v] = map2.getOrDefault(v, 0) + 1\n        for (j in 0 until n - 1) {\n\
        \            for (i in 0 until m) {\n                val v = grid[i][j]\n  \
        \              map1[v] = map1.getOrDefault(v, 0) + 1\n                map2[v]\
        \ = map2[v]!! - 1\n                if (map2[v] == 0) map2.remove(v)\n      \
        \      }\n            s1 += colSums[j]\n            val s2 = totalSum - s1\n\
        \            if (s1 == s2) return true\n            if (s1 > s2) { if (isValid(s1\
        \ - s2, 0, m - 1, 0, j, map1)) return true }\n            else { if (isValid(s2\
        \ - s1, 0, m - 1, j + 1, n - 1, map2)) return true }\n        }\n        return\
        \ false\n    }\n}"
      dart: "class Solution {\n  bool canPartitionGrid(List<List<int>> grid) {\n   \
        \ int m = grid.length, n = grid[0].length, totalSum = 0;\n    List<int> rowSums\
        \ = List.filled(m, 0), colSums = List.filled(n, 0);\n    Map<int, int> map2\
        \ = {};\n    for (int i = 0; i < m; i++) {\n      for (int j = 0; j < n; j++)\
        \ {\n        int v = grid[i][j];\n        totalSum += v; rowSums[i] += v; colSums[j]\
        \ += v;\n        map2[v] = (map2[v] ?? 0) + 1;\n      }\n    }\n    bool isValid(int\
        \ x, int rs, int re, int cs, int ce, Map<int, int> map) {\n      int h = re\
        \ - rs + 1, w = ce - cs + 1;\n      if (h >= 2 && w >= 2) return map.containsKey(x);\n\
        \      if (h == 1 && w == 1) return grid[rs][cs] == x;\n      if (h == 1) return\
        \ grid[rs][cs] == x || grid[rs][ce] == x;\n      if (w == 1) return grid[rs][cs]\
        \ == x || grid[re][cs] == x;\n      return false;\n    }\n    int s1 = 0; Map<int,\
        \ int> map1 = {};\n    for (int i = 0; i < m - 1; i++) {\n      for (int val\
        \ in grid[i]) {\n        map1[val] = (map1[val] ?? 0) + 1;\n        map2[val]\
        \ = map2[val]! - 1;\n        if (map2[val] == 0) map2.remove(val);\n      }\n\
        \      s1 += rowSums[i];\n      int s2 = totalSum - s1;\n      if (s1 == s2)\
        \ return true;\n      if (s1 > s2) { if (isValid(s1 - s2, 0, i, 0, n - 1, map1))\
        \ return true; }\n      else { if (isValid(s2 - s1, i + 1, m - 1, 0, n - 1,\
        \ map2)) return true; }\n    }\n    s1 = 0; map1.clear(); map2.clear();\n  \
        \  for (var r in grid) for (var v in r) map2[v] = (map2[v] ?? 0) + 1;\n    for\
        \ (int j = 0; j < n - 1; j++) {\n      for (int i = 0; i < m; i++) {\n     \
        \   int v = grid[i][j];\n        map1[v] = (map1[v] ?? 0) + 1;\n        map2[v]\
        \ = map2[v]! - 1;\n        if (map2[v] == 0) map2.remove(v);\n      }\n    \
        \  s1 += colSums[j];\n      int s2 = totalSum - s1;\n      if (s1 == s2) return\
        \ true;\n      if (s1 > s2) { if (isValid(s1 - s2, 0, m - 1, 0, j, map1)) return\
        \ true; }\n      else { if (isValid(s2 - s1, 0, m - 1, j + 1, n - 1, map2))\
        \ return true; }\n    }\n    return false;\n  }\n}"
      go: "func canPartitionGrid(grid [][]int) bool {\n    m, n := len(grid), len(grid[0])\n\
        \    var totalSum int64\n    rowSums, colSums := make([]int64, m), make([]int64,\
        \ n)\n    map2 := make(map[int]int)\n    for i := 0; i < m; i++ {\n        for\
        \ j := 0; j < n; j++ {\n            v := grid[i][j]\n            totalSum +=\
        \ int64(v)\n            rowSums[i] += int64(v)\n            colSums[j] += int64(v)\n\
        \            map2[v]++\n        }\n    }\n    isValid := func(x int64, rs, re,\
        \ cs, ce int, freq map[int]int) bool {\n        h, w := re-rs+1, ce-cs+1\n \
        \       xi := int(x)\n        if x > 1000000000 { return false }\n        if\
        \ h >= 2 && w >= 2 { _, ok := freq[xi]; return ok }\n        if h == 1 && w\
        \ == 1 { return grid[rs][cs] == xi }\n        if h == 1 { return grid[rs][cs]\
        \ == xi || grid[rs][ce] == xi }\n        if w == 1 { return grid[rs][cs] ==\
        \ xi || grid[re][cs] == xi }\n        return false\n    }\n    var s1 int64;\
        \ map1 := make(map[int]int)\n    for i := 0; i < m-1; i++ {\n        for _,\
        \ v := range grid[i] {\n            map1[v]++; map2[v]--; if map2[v] == 0 {\
        \ delete(map2, v) }\n        }\n        s1 += rowSums[i]; s2 := totalSum - s1\n\
        \        if s1 == s2 { return true }\n        if s1 > s2 { if isValid(s1-s2,\
        \ 0, i, 0, n-1, map1) { return true } }\n        if s2 > s1 { if isValid(s2-s1,\
        \ i+1, m-1, 0, n-1, map2) { return true } }\n    }\n    s1 = 0; map1 = make(map[int]int);\
        \ map2 = make(map[int]int)\n    for i := 0; i < m; i++ { for j := 0; j < n;\
        \ j++ { map2[grid[i][j]]++ } }\n    for j := 0; j < n-1; j++ {\n        for\
        \ i := 0; i < m; i++ {\n            v := grid[i][j]; map1[v]++; map2[v]--; if\
        \ map2[v] == 0 { delete(map2, v) }\n        }\n        s1 += colSums[j]; s2\
        \ := totalSum - s1\n        if s1 == s2 { return true }\n        if s1 > s2\
        \ { if isValid(s1-s2, 0, m-1, 0, j, map1) { return true } }\n        if s2 >\
        \ s1 { if isValid(s2-s1, 0, m-1, j+1, n-1, map2) { return true } }\n    }\n\
        \    return false\n}"
      ruby: "def check_h(grid, m, n)\n  row_sums = grid.map { |row| row.sum }\n  total_sum\
        \ = row_sums.sum\n  count1 = Hash.new(0)\n  count2 = Hash.new(0)\n  grid.each\
        \ { |row| row.each { |val| count2[val] += 1 } }\n  s1 = 0\n  (0...m - 1).each\
        \ do |i|\n    s1 += row_sums[i]\n    s2 = total_sum - s1\n    grid[i].each do\
        \ |val|\n      count1[val] += 1\n      count2[val] -= 1\n      count2.delete(val)\
        \ if count2[val] == 0\n    end\n\n    if s1 == s2\n      return true\n    elsif\
        \ s1 > s2\n      target = s1 - s2\n      if i + 1 > 1 && n > 1\n        return\
        \ true if count1.key?(target)\n      elsif i + 1 == 1 && n > 1\n        return\
        \ true if target == grid[0][0] || target == grid[0][n - 1]\n      elsif n ==\
        \ 1 && i + 1 > 1\n        return true if target == grid[0][0] || target == grid[i][0]\n\
        \      elsif i + 1 == 1 && n == 1\n        return true if target == grid[0][0]\n\
        \      end\n    else\n      target = s2 - s1\n      if m - i - 1 > 1 && n >\
        \ 1\n        return true if count2.key?(target)\n      elsif m - i - 1 == 1\
        \ && n > 1\n        return true if target == grid[m - 1][0] || target == grid[m\
        \ - 1][n - 1]\n      elsif n == 1 && m - i - 1 > 1\n        return true if target\
        \ == grid[i + 1][0] || target == grid[m - 1][0]\n      elsif m - i - 1 == 1\
        \ && n == 1\n        return true if target == grid[m - 1][0]\n      end\n  \
        \  end\n  end\n  false\nend\n\ndef can_partition_grid(grid)\n  return true if\
        \ check_h(grid, grid.size, grid[0].size)\n  return true if check_h(grid.transpose,\
        \ grid[0].size, grid.size)\n  false\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n  def canPartitionGrid(grid:\
        \ Array[Array[Int]]): Boolean = {\n    def check(g: Array[Array[Int]]): Boolean\
        \ = {\n      val m = g.length\n      if (m < 2) return false\n      val n =\
        \ g(0).length\n      val rowSums = g.map(_.map(_.toLong).sum)\n      val totalSum\
        \ = rowSums.sum\n      val count1 = mutable.HashMap[Int, Int]().withDefaultValue(0)\n\
        \      val count2 = mutable.HashMap[Int, Int]().withDefaultValue(0)\n      for\
        \ (r <- 0 until m; c <- 0 until n) { val v = g(r)(c); count2(v) += 1 }\n   \
        \   var s1 = 0L\n      for (i <- 0 until m - 1) {\n        s1 += rowSums(i)\n\
        \        val s2 = totalSum - s1\n        for (c <- 0 until n) {\n          val\
        \ v = g(i)(c)\n          count1(v) += 1\n          count2(v) -= 1\n        \
        \  if (count2(v) == 0) count2.remove(v)\n        }\n        if (s1 == s2) return\
        \ true\n        if (s1 > s2) {\n          val target = s1 - s2\n          if\
        \ (target <= 1000000000L) {\n            val t = target.toInt\n            val\
        \ r1 = i + 1; val c1 = n\n            if (r1 > 1 && c1 > 1) { if (count1.contains(t))\
        \ return true }\n            else if (r1 == 1 && c1 > 1) { if (t == g(0)(0)\
        \ || t == g(0)(n - 1)) return true }\n            else if (c1 == 1 && r1 > 1)\
        \ { if (t == g(0)(0) || t == g(i)(0)) return true }\n            else if (r1\
        \ == 1 && c1 == 1) { if (t == g(0)(0)) return true }\n          }\n        }\
        \ else {\n          val target = s2 - s1\n          if (target <= 1000000000L)\
        \ {\n            val t = target.toInt\n            val r2 = m - i - 1; val c2\
        \ = n\n            if (r2 > 1 && c2 > 1) { if (count2.contains(t)) return true\
        \ }\n            else if (r2 == 1 && c2 > 1) { if (t == g(m - 1)(0) || t ==\
        \ g(m - 1)(n - 1)) return true }\n            else if (c2 == 1 && r2 > 1) {\
        \ if (t == g(i + 1)(0) || t == g(m - 1)(0)) return true }\n            else\
        \ if (r2 == 1 && c2 == 1) { if (t == g(m - 1)(0)) return true }\n          }\n\
        \        }\n      }\n      false\n    }\n    check(grid) || check(grid.transpose)\n\
        \  }\n}"
      rust: "use std::collections::HashMap;\n\nimpl Solution {\n    pub fn can_partition_grid(grid:\
        \ Vec<Vec<i32>>) -> bool {\n        fn check(g: &Vec<Vec<i32>>) -> bool {\n\
        \            let m = g.len();\n            let n = g[0].len();\n           \
        \ if m < 2 { return false; }\n            let mut row_sums = vec![0i64; m];\n\
        \            let mut total_sum = 0i64;\n            let mut count2 = HashMap::new();\n\
        \            for r in 0..m {\n                for c in 0..n {\n            \
        \        let v = g[r][c];\n                    row_sums[r] += v as i64;\n  \
        \                  *count2.entry(v).or_insert(0) += 1;\n                }\n\
        \                total_sum += row_sums[r];\n            }\n            let mut\
        \ s1 = 0i64;\n            let mut count1 = HashMap::new();\n            for\
        \ i in 0..m - 1 {\n                s1 += row_sums[i];\n                let s2\
        \ = total_sum - s1;\n                for c in 0..n {\n                    let\
        \ v = g[i][c];\n                    *count1.entry(v).or_insert(0) += 1;\n  \
        \                  let c2 = count2.get_mut(&v).unwrap();\n                 \
        \   *c2 -= 1;\n                    if *c2 == 0 { count2.remove(&v); }\n    \
        \            }\n                if s1 == s2 { return true; }\n             \
        \   if s1 > s2 {\n                    let target = s1 - s2;\n              \
        \      if target <= 1000000 { \n                        let t = target as i32;\n\
        \                        let r1 = i + 1; let c1 = n;\n                     \
        \   if r1 > 1 && c1 > 1 { if count1.contains_key(&t) { return true; } }\n  \
        \                      else if r1 == 1 && c1 > 1 { if t == g[0][0] || t == g[0][n-1]\
        \ { return true; } }\n                        else if c1 == 1 && r1 > 1 { if\
        \ t == g[0][0] || t == g[i][0] { return true; } }\n                        else\
        \ if r1 == 1 && c1 == 1 { if t == g[0][0] { return true; } }\n             \
        \       }\n                } else {\n                    let target = s2 - s1;\n\
        \                    if target <= 1000000 {\n                        let t =\
        \ target as i32;\n                        let r2 = m - i - 1; let c2 = n;\n\
        \                        if r2 > 1 && c2 > 1 { if count2.contains_key(&t) {\
        \ return true; } }\n                        else if r2 == 1 && c2 > 1 { if t\
        \ == g[m-1][0] || t == g[m-1][n-1] { return true; } }\n                    \
        \    else if c2 == 1 && r2 > 1 { if t == g[i+1][0] || t == g[m-1][0] { return\
        \ true; } }\n                        else if r2 == 1 && c2 == 1 { if t == g[m-1][0]\
        \ { return true; } }\n                    }\n                }\n           \
        \ }\n            false\n        }\n        if check(&grid) { return true; }\n\
        \        let m = grid.len();\n        let n = grid[0].len();\n        let mut\
        \ transposed = vec![vec![0; m]; n];\n        for r in 0..m { for c in 0..n {\
        \ transposed[c][r] = grid[r][c]; } }\n        check(&transposed)\n    }\n}"
      racket: "(define/contract (can-partition-grid grid)\n  (-> (listof (listof exact-integer?))\
        \ boolean?)\n  (define (check g)\n    (let* ([m (length g)] [n (length (first\
        \ g))]\n           [g-vec (list->vector (map list->vector g))]\n           [row-sums\
        \ (list->vector (map (lambda (row) (apply + row)) g))]\n           [total-sum\
        \ (for/sum ([s row-sums]) s)]\n           [count1 (make-hash)] [count2 (make-hash)])\n\
        \      (for* ([r (in-range m)] [c (in-range n)])\n        (let ([v (vector-ref\
        \ (vector-ref g-vec r) c)])\n          (hash-set! count2 v (+ (hash-ref count2\
        \ v 0) 1))))\n      (let loop ([i 0] [s1 0])\n        (if (< i (- m 1))\n  \
        \          (let* ([s1-new (+ s1 (vector-ref row-sums i))] [s2 (- total-sum s1-new)])\n\
        \              (for ([c (in-range n)])\n                (let* ([v (vector-ref\
        \ (vector-ref g-vec i) c)] [c2 (hash-ref count2 v)])\n                  (hash-set!\
        \ count1 v (+ (hash-ref count1 v 0) 1))\n                  (if (= c2 1) (hash-remove!\
        \ count2 v) (hash-set! count2 v (- c2 1)))))\n              (cond\n        \
        \        [(= s1-new s2) #t]\n                [(> s1-new s2)\n              \
        \   (let ([target (- s1-new s2)])\n                   (if (let ([r1 (+ i 1)]\
        \ [c1 n])\n                         (cond [(and (> r1 1) (> c1 1)) (hash-has-key?\
        \ count1 target)]\n                               [(and (= r1 1) (> c1 1)) (or\
        \ (= target (vector-ref (vector-ref g-vec 0) 0)) (= target (vector-ref (vector-ref\
        \ g-vec 0) (- n 1))))]\n                               [(and (= c1 1) (> r1\
        \ 1)) (or (= target (vector-ref (vector-ref g-vec 0) 0)) (= target (vector-ref\
        \ (vector-ref g-vec i) 0)))]\n                               [else (= target\
        \ (vector-ref (vector-ref g-vec 0) 0))]))\n                       #t (loop (+\
        \ i 1) s1-new))]\n                [else\n                 (let ([target (- s2\
        \ s1-new)])\n                   (if (let ([r2 (- m i 1)] [c2 n])\n         \
        \                (cond [(and (> r2 1) (> c2 1)) (hash-has-key? count2 target)]\n\
        \                               [(and (= r2 1) (> c2 1)) (or (= target (vector-ref\
        \ (vector-ref g-vec (- m 1)) 0)) (= target (vector-ref (vector-ref g-vec (-\
        \ m 1)) (- n 1))))]\n                               [(and (= c2 1) (> r2 1))\
        \ (or (= target (vector-ref (vector-ref g-vec (+ i 1)) 0)) (= target (vector-ref\
        \ (vector-ref g-vec (- m 1)) 0)))]\n                               [else (=\
        \ target (vector-ref (vector-ref g-vec (- m 1)) 0))]))\n                   \
        \    #t (loop (+ i 1) s1-new))]))\n            #f))))\n  (or (check grid) (if\
        \ (null? grid) #f (check (apply map list grid)))))"
      erlang: "-spec can_partition_grid(Grid :: [[integer()]]) -> boolean().\ncan_partition_grid(Grid)\
        \ ->\n    check_h(Grid) orelse check_h(transpose(Grid)).\n\ntranspose([[]|_])\
        \ -> [];\ntranspose(Grid) -> [lists:map(fun hd/1, Grid) | transpose(lists:map(fun\
        \ tl/1, Grid))].\n\ncheck_h(Grid) ->\n    M = length(Grid),\n    if M < 2 ->\
        \ false;\n       true -> \n           RowSums = [lists:sum(Row) || Row <- Grid],\n\
        \           TotalSum = lists:sum(RowSums),\n           Count2 = lists:foldl(fun(Row,\
        \ Acc) ->\n               lists:foldl(fun(V, Acc2) ->\n                   maps:update_with(V,\
        \ fun(C) -> C + 1 end, 1, Acc2)\n               end, Acc, Row) end, #{}, Grid),\n\
        \           GridVec = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),\n\
        \           RowSumsVec = list_to_tuple(RowSums),\n           check_h_loop(1,\
        \ 0, M, length(element(1, GridVec)), TotalSum, RowSumsVec, GridVec, #{}, Count2)\n\
        \    end.\n\ncheck_h_loop(I, S1, M, N, TotalSum, RowSumsVec, GridVec, Count1,\
        \ Count2) when I < M ->\n    RowI = element(I, GridVec),\n    S1Next = S1 +\
        \ element(I, RowSumsVec),\n    S2 = TotalSum - S1Next,\n    {NewCount1, NewCount2}\
        \ = update_counts(tuple_to_list(RowI), Count1, Count2),\n    case check_cond(I,\
        \ S1Next, S2, M, N, GridVec, NewCount1, NewCount2) of\n        true -> true;\n\
        \        false -> check_h_loop(I + 1, S1Next, M, N, TotalSum, RowSumsVec, GridVec,\
        \ NewCount1, NewCount2)\n    end;\ncheck_h_loop(_, _, _, _, _, _, _, _, _) ->\
        \ false.\n\nupdate_counts([], C1, C2) -> {C1, C2};\nupdate_counts([V|Rest],\
        \ C1, C2) ->\n    NewC1 = maps:update_with(V, fun(C) -> C + 1 end, 1, C1),\n\
        \    NewC2 = case maps:get(V, C2) of 1 -> maps:remove(V, C2); N -> maps:put(V,\
        \ N - 1, C2) end,\n    update_counts(Rest, NewC1, NewC2).\n\ncheck_cond(I, S1,\
        \ S2, M, N, GridVec, C1, C2) ->\n    if S1 == S2 -> true;\n       S1 > S2 ->\
        \ \n           T = S1 - S2, R1 = I, \n           if (R1>1) and (N>1) -> maps:is_key(T,\
        \ C1);\n              (R1==1) and (N>1) -> (T == element(1, element(1, GridVec)))\
        \ orelse (T == element(N, element(1, GridVec)));\n              (N==1) and (R1>1)\
        \ -> (T == element(1, element(1, GridVec))) orelse (T == element(1, element(I,\
        \ GridVec)));\n              true -> T == element(1, element(1, GridVec))\n\
        \           end;\n       S2 > S1 -> \n           T = S2 - S1, R2 = M - I,\n\
        \           if (R2>1) and (N>1) -> maps:is_key(T, C2);\n              (R2==1)\
        \ and (N>1) -> (T == element(1, element(M, GridVec))) orelse (T == element(N,\
        \ element(M, GridVec)));\n              (N==1) and (R2>1) -> (T == element(1,\
        \ element(I+1, GridVec))) orelse (T == element(1, element(M, GridVec)));\n \
        \             true -> T == element(1, element(M, GridVec))\n           end\n\
        \    end."
      elixir: "defmodule Solution do\n  @spec can_partition_grid(grid :: [[integer]])\
        \ :: boolean\n  def can_partition_grid(grid) do\n    check_h(grid) or check_h(grid\
        \ |> Enum.zip() |> Enum.map(&Tuple.to_list/1))\n  end\n\n  defp check_h(grid)\
        \ do\n    m = length(grid)\n    if m < 2, do: false, else: (\n      n = length(hd(grid))\n\
        \      row_sums = Enum.map(grid, &Enum.sum/1)\n      total_sum = Enum.sum(row_sums)\n\
        \      count2 = Enum.reduce(grid, %{}, fn row, acc ->\n        Enum.reduce(row,\
        \ acc, fn v, a -> Map.update(a, v, 1, &(&1 + 1)) end)\n      end)\n      grid_vec\
        \ = grid |> Enum.map(&List.to_tuple/1) |> List.to_tuple()\n      row_sums_vec\
        \ = List.to_tuple(row_sums)\n      check_h_loop(1, 0, m, n, total_sum, row_sums_vec,\
        \ grid_vec, %{}, count2)\n    )\n  end\n\n  defp check_h_loop(i, s1, m, n, total_sum,\
        \ row_sums_vec, grid_vec, count1, count2) when i < m do\n    row_i = element_at(grid_vec,\
        \ i)\n    s1_next = s1 + elem(row_sums_vec, i - 1)\n    s2 = total_sum - s1_next\n\
        \    {new_c1, new_c2} = update_counts(Tuple.to_list(row_i), count1, count2)\n\
        \    if check_condition(i, s1_next, s2, m, n, grid_vec, new_c1, new_c2) do true\n\
        \    else check_h_loop(i + 1, s1_next, m, n, total_sum, row_sums_vec, grid_vec,\
        \ new_c1, new_c2) end\n  end\n  defp check_h_loop(_, _, _, _, _, _, _, _, _),\
        \ do: false\n\n  defp update_counts(row, c1, c2) do\n    Enum.reduce(row, {c1,\
        \ c2}, fn v, {a1, a2} ->\n      {Map.update(a1, v, 1, &(&1 + 1)), case Map.get(a2,\
        \ v) do 1 -> Map.delete(a2, v); n -> Map.put(a2, v, n - 1) end}\n    end)\n\
        \  end\n\n  defp check_condition(i, s1, s2, m, n, grid_vec, c1, c2) do\n   \
        \ cond do\n      s1 == s2 -> true\n      s1 > s2 ->\n        t = s1 - s2\n \
        \       cond do\n          i > 1 and n > 1 -> Map.has_key?(c1, t)\n        \
        \  i == 1 and n > 1 -> t == elem(elem(grid_vec, 0), 0) or t == elem(elem(grid_vec,\
        \ 0), n - 1)\n          n == 1 and i > 1 -> t == elem(elem(grid_vec, 0), 0)\
        \ or t == elem(elem(grid_vec, i - 1), 0)\n          true -> t == elem(elem(grid_vec,\
        \ 0), 0)\n        end\n      true ->\n        t = s2 - s1\n        r2 = m -\
        \ i\n        cond do\n          r2 > 1 and n > 1 -> Map.has_key?(c2, t)\n  \
        \        r2 == 1 and n > 1 -> t == elem(elem(grid_vec, m - 1), 0) or t == elem(elem(grid_vec,\
        \ m - 1), n - 1)\n          n == 1 and r2 > 1 -> t == elem(elem(grid_vec, i),\
        \ 0) or t == elem(elem(grid_vec, m - 1), 0)\n          true -> t == elem(elem(grid_vec,\
        \ m - 1), 0)\n        end\n    end\n  end\n  defp element_at(tuple, i), do:\
        \ elem(tuple, i - 1)\nend"
    approach: The problem asks whether we can partition a grid into two non-empty sections
      by a single horizontal or vertical cut such that their sums are equal, possibly
      after discounting one cell from either section. A key insight is that removing
      a cell from a section only disconnects it if the section is a single row or single
      column and the removed cell is not an endpoint. For any section with both dimensions
      greater than 1, removing any single cell keeps it connected. We can iterate through
      all possible horizontal and vertical cut positions, maintaining the sum and value
      frequencies of each section to verify the partitioning condition efficiently.
    time_complexity: O(m * n + V), where m and n are the grid dimensions and V is the
      maximum value in the grid. We perform a constant number of passes over the grid
      to compute row and column sums and maintain frequency counts of elements. Frequency
      maps or arrays of size up to 10^5 are used to check for target values in O(1)
      time.
    space_complexity: O(m * n + V) to store the grid, row/column sums, and the frequency
      counts of cell values. The total number of cells m * n is up to 10^5, and the
      maximum cell value V is also 10^5.
    elapsed_time: 360.9079248905182
    model: gemini-3-flash-preview
    generated_at: '2026-03-26 01:51:41 '
---

## Problem #3548: Equal Sum Grid Partition II

**Difficulty:** Hard

**Topics:** Array, Hash Table, Matrix, Enumeration, Prefix Sum

## Problem Description

<p>You are given an <code>m x n</code> matrix <code>grid</code> of positive integers. Your task is to determine if it is possible to make <strong>either one horizontal or one vertical cut</strong> on the grid such that:</p>

<ul>
	<li>Each of the two resulting sections formed by the cut is <strong>non-empty</strong>.</li>
	<li>The sum of elements in both sections is <b>equal</b>, or can be made equal by discounting <strong>at most</strong> one single cell in total (from either section).</li>
	<li>If a cell is discounted, the rest of the section must <strong>remain connected</strong>.</li>
</ul>

<p>Return <code>true</code> if such a partition exists; otherwise, return <code>false</code>.</p>

<p><strong>Note:</strong> A section is <strong>connected</strong> if every cell in it can be reached from any other cell by moving up, down, left, or right through other cells in the section.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,4],[2,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/03/30/lc.jpeg" style="height: 180px; width: 180px;" /></p>

<ul>
	<li>A horizontal cut after the first row gives sums <code>1 + 4 = 5</code> and <code>2 + 3 = 5</code>, which are equal. Thus, the answer is <code>true</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,2],[3,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/04/01/chatgpt-image-apr-1-2025-at-05_28_12-pm.png" style="height: 180px; width: 180px;" /></p>

<ul>
	<li>A vertical cut after the first column gives sums <code>1 + 3 = 4</code> and <code>2 + 4 = 6</code>.</li>
	<li>By discounting 2 from the right section (<code>6 - 2 = 4</code>), both sections have equal sums and remain connected. Thus, the answer is <code>true</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,2,4],[2,3,5]]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2025/04/01/chatgpt-image-apr-2-2025-at-02_50_29-am.png" style="height: 180px; width: 180px;" /></strong></p>

<ul>
	<li>A horizontal cut after the first row gives <code>1 + 2 + 4 = 7</code> and <code>2 + 3 + 5 = 10</code>.</li>
	<li>By discounting 3 from the bottom section (<code>10 - 3 = 7</code>), both sections have equal sums, but they do not remain connected as it splits the bottom section into two parts (<code>[2]</code> and <code>[5]</code>). Thus, the answer is <code>false</code>.</li>
</ul>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[4,1,8],[3,2,6]]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>No valid cut exists, so the answer is <code>false</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m == grid.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= n == grid[i].length &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. In a grid (or any subgrid), when can a section be disconnected? Can disconnected components occur if the section spans more than one row and more than one column?

2. Handle single rows or single columns separately. For all other partitions, maintain the sums and value frequencies of each section to check whether removing at most one element from one section can make the two sums equal.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks whether we can partition a grid into two non-empty sections by a single horizontal or vertical cut such that their sums are equal, possibly after discounting one cell from either section. A key insight is that removing a cell from a section only disconnects it if the section is a single row or single column and the removed cell is not an endpoint. For any section with both dimensions greater than 1, removing any single cell keeps it connected. We can iterate through all possible horizontal and vertical cut positions, maintaining the sum and value frequencies of each section to verify the partitioning condition efficiently.

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
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        long long total_sum = 0;
        vector<int> total_val_count(100001, 0);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                total_sum += grid[i][j];
                total_val_count[grid[i][j]]++;
            }
        }

        // Horizontal cuts
        vector<long long> row_sums(m, 0);
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j) row_sums[i] += grid[i][j];

        long long s1 = 0;
        vector<int> count1(100001, 0);
        for (int i = 0; i < m - 1; ++i) {
            for (int j = 0; j < n; ++j) count1[grid[i][j]]++;
            s1 += row_sums[i];
            long long s2 = total_sum - s1;
            if (s1 == s2) return true;
            if (s1 > s2) {
                long long target = s1 - s2;
                if (target <= 100000 && count1[target] > 0) {
                    if (n > 1 && (i + 1) > 1) return true;
                    if (n > 1 && (target == grid[0][0] || target == grid[0][n - 1])) return true;
                    if ((i + 1) > 1 && (target == grid[0][0] || target == grid[i][0])) return true;
                    if (n == 1 && (i + 1) == 1 && target == grid[0][0]) return true;
                }
            }
            if (s2 > s1) {
                long long target = s2 - s1;
                if (target <= 100000 && (total_val_count[target] - count1[target]) > 0) {
                    int h2 = m - 1 - i;
                    if (n > 1 && h2 > 1) return true;
                    if (n > 1 && (target == grid[i + 1][0] || target == grid[i + 1][n - 1])) return true;
                    if (h2 > 1 && (target == grid[i + 1][0] || target == grid[m - 1][0])) return true;
                    if (n == 1 && h2 == 1 && target == grid[i + 1][0]) return true;
                }
            }
        }

        // Vertical cuts
        vector<long long> col_sums(n, 0);
        for (int j = 0; j < n; ++j)
            for (int i = 0; i < m; ++i) col_sums[j] += grid[i][j];

        s1 = 0;
        fill(count1.begin(), count1.end(), 0);
        for (int j = 0; j < n - 1; ++j) {
            for (int i = 0; i < m; ++i) count1[grid[i][j]]++;
            s1 += col_sums[j];
            long long s2 = total_sum - s1;
            if (s1 == s2) return true;
            if (s1 > s2) {
                long long target = s1 - s2;
                if (target <= 100000 && count1[target] > 0) {
                    if (m > 1 && (j + 1) > 1) return true;
                    if (m > 1 && (target == grid[0][0] || target == grid[m - 1][0])) return true;
                    if ((j + 1) > 1 && (target == grid[0][0] || target == grid[0][j])) return true;
                    if (m == 1 && (j + 1) == 1 && target == grid[0][0]) return true;
                }
            }
            if (s2 > s1) {
                long long target = s2 - s1;
                if (target <= 100000 && (total_val_count[target] - count1[target]) > 0) {
                    int w2 = n - 1 - j;
                    if (m > 1 && w2 > 1) return true;
                    if (m > 1 && (target == grid[0][j + 1] || target == grid[m - 1][j + 1])) return true;
                    if (w2 > 1 && (target == grid[0][j + 1] || target == grid[0][n - 1])) return true;
                    if (m == 1 && w2 == 1 && target == grid[0][j + 1]) return true;
                }
            }
        }
        return false;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;

class Solution {
    public boolean canPartitionGrid(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        long totalSum = 0;
        int[] totalValCount = new int[100001];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                totalSum += grid[i][j];
                totalValCount[grid[i][j]]++;
            }
        }

        long[] rowSums = new long[m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) rowSums[i] += grid[i][j];
        }

        long s1 = 0;
        int[] count1 = new int[100001];
        for (int i = 0; i < m - 1; i++) {
            for (int j = 0; j < n; j++) count1[grid[i][j]]++;
            s1 += rowSums[i];
            long s2 = totalSum - s1;
            if (s1 == s2) return true;
            if (s1 > s2) {
                long target = s1 - s2;
                if (target <= 100000 && count1[(int)target] > 0) {
                    if (n > 1 && (i + 1) > 1) return true;
                    if (n > 1 && (target == grid[0][0] || target == grid[0][n - 1])) return true;
                    if ((i + 1) > 1 && (target == grid[0][0] || target == grid[i][0])) return true;
                    if (n == 1 && (i + 1) == 1 && target == grid[0][0]) return true;
                }
            }
            if (s2 > s1) {
                long target = s2 - s1;
                if (target <= 100000 && (totalValCount[(int)target] - count1[(int)target]) > 0) {
                    int h2 = m - 1 - i;
                    if (n > 1 && h2 > 1) return true;
                    if (n > 1 && (target == grid[i + 1][0] || target == grid[i + 1][n - 1])) return true;
                    if (h2 > 1 && (target == grid[i + 1][0] || target == grid[m - 1][0])) return true;
                    if (n == 1 && h2 == 1 && target == grid[i + 1][0]) return true;
                }
            }
        }

        long[] colSums = new long[n];
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m; i++) colSums[j] += grid[i][j];
        }

        s1 = 0;
        Arrays.fill(count1, 0);
        for (int j = 0; j < n - 1; j++) {
            for (int i = 0; i < m; i++) count1[grid[i][j]]++;
            s1 += colSums[j];
            long s2 = totalSum - s1;
            if (s1 == s2) return true;
            if (s1 > s2) {
                long target = s1 - s2;
                if (target <= 100000 && count1[(int)target] > 0) {
                    if (m > 1 && (j + 1) > 1) return true;
                    if (m > 1 && (target == grid[0][0] || target == grid[m - 1][0])) return true;
                    if ((j + 1) > 1 && (target == grid[0][0] || target == grid[0][j])) return true;
                    if (m == 1 && (j + 1) == 1 && target == grid[0][0]) return true;
                }
            }
            if (s2 > s1) {
                long target = s2 - s1;
                if (target <= 100000 && (totalValCount[(int)target] - count1[(int)target]) > 0) {
                    int w2 = n - 1 - j;
                    if (m > 1 && w2 > 1) return true;
                    if (m > 1 && (target == grid[0][j + 1] || target == grid[m - 1][j + 1])) return true;
                    if (w2 > 1 && (target == grid[0][j + 1] || target == grid[0][n - 1])) return true;
                    if (m == 1 && w2 == 1 && target == grid[0][j + 1]) return true;
                }
            }
        }
        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)
        total_val_count = {}
        for row in grid:
            for val in row:
                total_val_count[val] = total_val_count.get(val, 0) + 1

        def check_h():
            row_sums = [sum(row) for row in grid]
            s1, count1 = 0, {}
            for i in range(m - 1):
                for val in grid[i]: count1[val] = count1.get(val, 0) + 1
                s1 += row_sums[i]
                s2 = total_sum - s1
                if s1 == s2: return True
                if s1 > s2:
                    target = s1 - s2
                    if target <= 100000 and count1.get(target, 0) > 0:
                        if n > 1 and i + 1 > 1: return True
                        if n > 1 and (target == grid[0][0] or target == grid[0][n-1]): return True
                        if i + 1 > 1 and (target == grid[0][0] or target == grid[i][0]): return True
                        if n == 1 and i + 1 == 1 and target == grid[0][0]: return True
                if s2 > s1:
                    target = s2 - s1
                    if target <= 100000 and total_val_count.get(target, 0) - count1.get(target, 0) > 0:
                        h2 = m - 1 - i
                        if n > 1 and h2 > 1: return True
                        if n > 1 and (target == grid[i+1][0] or target == grid[i+1][n-1]): return True
                        if h2 > 1 and (target == grid[i+1][0] or target == grid[m-1][0]): return True
                        if n == 1 and h2 == 1 and target == grid[i+1][0]: return True
            return False

        def check_v():
            col_sums = [sum(grid[r][c] for r in range(m)) for c in range(n)]
            s1, count1 = 0, {}
            for j in range(n - 1):
                for r in range(m): val = grid[r][j]; count1[val] = count1.get(val, 0) + 1
                s1 += col_sums[j]
                s2 = total_sum - s1
                if s1 == s2: return True
                if s1 > s2:
                    target = s1 - s2
                    if target <= 100000 and count1.get(target, 0) > 0:
                        if m > 1 and j + 1 > 1: return True
                        if m > 1 and (target == grid[0][0] or target == grid[m-1][0]): return True
                        if j + 1 > 1 and (target == grid[0][0] or target == grid[0][j]): return True
                        if m == 1 and j + 1 == 1 and target == grid[0][0]: return True
                if s2 > s1:
                    target = s2 - s1
                    if target <= 100000 and total_val_count.get(target, 0) - count1.get(target, 0) > 0:
                        w2 = n - 1 - j
                        if m > 1 and w2 > 1: return True
                        if m > 1 and (target == grid[0][j+1] or target == grid[m-1][j+1]): return True
                        if w2 > 1 and (target == grid[0][j+1] or target == grid[0][n-1]): return True
                        if m == 1 and w2 == 1 and target == grid[0][j+1]: return True
            return False

        return check_h() or check_v()
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)
        total_val_count = {}
        for row in grid:
            for val in row:
                total_val_count[val] = total_val_count.get(val, 0) + 1

        def check_h():
            row_sums = [sum(row) for row in grid]
            s1, count1 = 0, {}
            for i in range(m - 1):
                for val in grid[i]: count1[val] = count1.get(val, 0) + 1
                s1 += row_sums[i]
                s2 = total_sum - s1
                if s1 == s2: return True
                if s1 > s2:
                    target = s1 - s2
                    if target <= 100000 and count1.get(target, 0) > 0:
                        if n > 1 and i + 1 > 1: return True
                        if n > 1 and (target == grid[0][0] or target == grid[0][n-1]): return True
                        if i + 1 > 1 and (target == grid[0][0] or target == grid[i][0]): return True
                        if n == 1 and i + 1 == 1 and target == grid[0][0]: return True
                if s2 > s1:
                    target = s2 - s1
                    if target <= 100000 and total_val_count.get(target, 0) - count1.get(target, 0) > 0:
                        h2 = m - 1 - i
                        if n > 1 and h2 > 1: return True
                        if n > 1 and (target == grid[i+1][0] or target == grid[i+1][n-1]): return True
                        if h2 > 1 and (target == grid[i+1][0] or target == grid[m-1][0]): return True
                        if n == 1 and h2 == 1 and target == grid[i+1][0]: return True
            return False

        def check_v():
            col_sums = [sum(grid[r][c] for r in range(m)) for c in range(n)]
            s1, count1 = 0, {}
            for j in range(n - 1):
                for r in range(m): val = grid[r][j]; count1[val] = count1.get(val, 0) + 1
                s1 += col_sums[j]
                s2 = total_sum - s1
                if s1 == s2: return True
                if s1 > s2:
                    target = s1 - s2
                    if target <= 100000 and count1.get(target, 0) > 0:
                        if m > 1 and j + 1 > 1: return True
                        if m > 1 and (target == grid[0][0] or target == grid[m-1][0]): return True
                        if j + 1 > 1 and (target == grid[0][0] or target == grid[0][j]): return True
                        if m == 1 and j + 1 == 1 and target == grid[0][0]: return True
                if s2 > s1:
                    target = s2 - s1
                    if target <= 100000 and total_val_count.get(target, 0) - count1.get(target, 0) > 0:
                        w2 = n - 1 - j
                        if m > 1 and w2 > 1: return True
                        if m > 1 and (target == grid[0][j+1] or target == grid[m-1][j+1]): return True
                        if w2 > 1 and (target == grid[0][j+1] or target == grid[0][n-1]): return True
                        if m == 1 and w2 == 1 and target == grid[0][j+1]: return True
            return False

        return check_h() or check_v()
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool canPartitionGrid(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];
    long long total_sum = 0;
    int total_val_count[100001] = {0};
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            total_sum += grid[i][j];
            total_val_count[grid[i][j]]++;
        }
    }

    long long row_sums[m];
    for (int i = 0; i < m; i++) {
        row_sums[i] = 0;
        for (int j = 0; j < n; j++) row_sums[i] += grid[i][j];
    }

    long long s1 = 0;
    int count1[100001] = {0};
    for (int i = 0; i < m - 1; i++) {
        for (int j = 0; j < n; j++) count1[grid[i][j]]++;
        s1 += row_sums[i];
        long long s2 = total_sum - s1;
        if (s1 == s2) return true;
        if (s1 > s2) {
            long long target = s1 - s2;
            if (target <= 100000 && count1[target] > 0) {
                if (n > 1 && (i + 1) > 1) return true;
                if (n > 1 && (target == grid[0][0] || target == grid[0][n - 1])) return true;
                if ((i + 1) > 1 && (target == grid[0][0] || target == grid[i][0])) return true;
                if (n == 1 && (i + 1) == 1 && target == grid[0][0]) return true;
            }
        }
        if (s2 > s1) {
            long long target = s2 - s1;
            if (target <= 100000 && (total_val_count[target] - count1[target]) > 0) {
                int h2 = m - 1 - i;
                if (n > 1 && h2 > 1) return true;
                if (n > 1 && (target == grid[i + 1][0] || target == grid[i + 1][n - 1])) return true;
                if (h2 > 1 && (target == grid[i + 1][0] || target == grid[m - 1][0])) return true;
                if (n == 1 && h2 == 1 && target == grid[i + 1][0]) return true;
            }
        }
    }

    long long col_sums[n];
    for (int j = 0; j < n; j++) {
        col_sums[j] = 0;
        for (int i = 0; i < m; i++) col_sums[j] += grid[i][j];
    }

    s1 = 0;
    memset(count1, 0, sizeof(count1));
    for (int j = 0; j < n - 1; j++) {
        for (int i = 0; i < m; i++) count1[grid[i][j]]++;
        s1 += col_sums[j];
        long long s2 = total_sum - s1;
        if (s1 == s2) return true;
        if (s1 > s2) {
            long long target = s1 - s2;
            if (target <= 100000 && count1[target] > 0) {
                if (m > 1 && (j + 1) > 1) return true;
                if (m > 1 && (target == grid[0][0] || target == grid[m - 1][0])) return true;
                if ((j + 1) > 1 && (target == grid[0][0] || target == grid[0][j])) return true;
                if (m == 1 && (j + 1) == 1 && target == grid[0][0]) return true;
            }
        }
        if (s2 > s1) {
            long long target = s2 - s1;
            if (target <= 100000 && (total_val_count[target] - count1[target]) > 0) {
                int w2 = n - 1 - j;
                if (m > 1 && w2 > 1) return true;
                if (m > 1 && (target == grid[0][j + 1] || target == grid[m - 1][j + 1])) return true;
                if (w2 > 1 && (target == grid[0][j + 1] || target == grid[0][n - 1])) return true;
                if (m == 1 && w2 == 1 && target == grid[0][j + 1]) return true;
            }
        }
    }
    return false;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool CanPartitionGrid(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        long totalSum = 0;
        int[] totalValCount = new int[100001];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                totalSum += grid[i][j];
                totalValCount[grid[i][j]]++;
            }
        }

        long[] rowSums = new long[m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) rowSums[i] += grid[i][j];
        }

        long s1 = 0;
        int[] count1 = new int[100001];
        for (int i = 0; i < m - 1; i++) {
            for (int j = 0; j < n; j++) count1[grid[i][j]]++;
            s1 += rowSums[i];
            long s2 = totalSum - s1;
            if (s1 == s2) return true;
            if (s1 > s2) {
                long target = s1 - s2;
                if (target <= 100000 && count1[(int)target] > 0) {
                    if (n > 1 && (i + 1) > 1) return true;
                    if (n > 1 && (target == grid[0][0] || target == grid[0][n - 1])) return true;
                    if ((i + 1) > 1 && (target == grid[0][0] || target == grid[i][0])) return true;
                    if (n == 1 && (i + 1) == 1 && target == grid[0][0]) return true;
                }
            }
            if (s2 > s1) {
                long target = s2 - s1;
                if (target <= 100000 && (totalValCount[(int)target] - count1[(int)target]) > 0) {
                    int h2 = m - 1 - i;
                    if (n > 1 && h2 > 1) return true;
                    if (n > 1 && (target == grid[i + 1][0] || target == grid[i + 1][n - 1])) return true;
                    if (h2 > 1 && (target == grid[i + 1][0] || target == grid[m - 1][0])) return true;
                    if (n == 1 && h2 == 1 && target == grid[i + 1][0]) return true;
                }
            }
        }

        long[] colSums = new long[n];
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m; i++) colSums[j] += grid[i][j];
        }

        s1 = 0;
        System.Array.Fill(count1, 0);
        for (int j = 0; j < n - 1; j++) {
            for (int i = 0; i < m; i++) count1[grid[i][j]]++;
            s1 += colSums[j];
            long s2 = totalSum - s1;
            if (s1 == s2) return true;
            if (s1 > s2) {
                long target = s1 - s2;
                if (target <= 100000 && count1[(int)target] > 0) {
                    if (m > 1 && (j + 1) > 1) return true;
                    if (m > 1 && (target == grid[0][0] || target == grid[m - 1][0])) return true;
                    if ((j + 1) > 1 && (target == grid[0][0] || target == grid[0][j])) return true;
                    if (m == 1 && (j + 1) == 1 && target == grid[0][0]) return true;
                }
            }
            if (s2 > s1) {
                long target = s2 - s1;
                if (target <= 100000 && (totalValCount[(int)target] - count1[(int)target]) > 0) {
                    int w2 = n - 1 - j;
                    if (m > 1 && w2 > 1) return true;
                    if (m > 1 && (target == grid[0][j + 1] || target == grid[m - 1][j + 1])) return true;
                    if (w2 > 1 && (target == grid[0][j + 1] || target == grid[0][n - 1])) return true;
                    if (m == 1 && w2 == 1 && target == grid[0][j + 1]) return true;
                }
            }
        }
        return false;
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
 * @return {boolean}
 */
var canPartitionGrid = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    let totalSum = 0;
    const totalValCount = new Int32Array(100001);
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            totalSum += grid[i][j];
            totalValCount[grid[i][j]]++;
        }
    }

    const rowSums = new BigInt64Array(m);
    for (let i = 0; i < m; i++) {
        let s = 0n;
        for (let j = 0; j < n; j++) s += BigInt(grid[i][j]);
        rowSums[i] = s;
    }

    let s1 = 0n;
    const count1 = new Int32Array(100001);
    for (let i = 0; i < m - 1; i++) {
        for (let j = 0; j < n; j++) count1[grid[i][j]]++;
        s1 += rowSums[i];
        let s2 = BigInt(totalSum) - s1;
        if (s1 === s2) return true;
        if (s1 > s2) {
            let target = Number(s1 - s2);
            if (target <= 100000 && count1[target] > 0) {
                if (n > 1 && (i + 1) > 1) return true;
                if (n > 1 && (target === grid[0][0] || target === grid[0][n - 1])) return true;
                if ((i + 1) > 1 && (target === grid[0][0] || target === grid[i][0])) return true;
                if (n === 1 && (i + 1) === 1 && target === grid[0][0]) return true;
            }
        }
        if (s2 > s1) {
            let target = Number(s2 - s1);
            if (target <= 100000 && (totalValCount[target] - count1[target]) > 0) {
                let h2 = m - 1 - i;
                if (n > 1 && h2 > 1) return true;
                if (n > 1 && (target === grid[i + 1][0] || target === grid[i + 1][n - 1])) return true;
                if (h2 > 1 && (target === grid[i + 1][0] || target === grid[m - 1][0])) return true;
                if (n === 1 && h2 === 1 && target === grid[i + 1][0]) return true;
            }
        }
    }

    const colSums = new BigInt64Array(n);
    for (let j = 0; j < n; j++) {
        let s = 0n;
        for (let i = 0; i < m; i++) s += BigInt(grid[i][j]);
        colSums[j] = s;
    }

    s1 = 0n;
    count1.fill(0);
    for (let j = 0; j < n - 1; j++) {
        for (let i = 0; i < m; i++) count1[grid[i][j]]++;
        s1 += colSums[j];
        let s2 = BigInt(totalSum) - s1;
        if (s1 === s2) return true;
        if (s1 > s2) {
            let target = Number(s1 - s2);
            if (target <= 100000 && count1[target] > 0) {
                if (m > 1 && (j + 1) > 1) return true;
                if (m > 1 && (target === grid[0][0] || target === grid[m - 1][0])) return true;
                if ((j + 1) > 1 && (target === grid[0][0] || target === grid[0][j])) return true;
                if (m === 1 && (j + 1) === 1 && target === grid[0][0]) return true;
            }
        }
        if (s2 > s1) {
            let target = Number(s2 - s1);
            if (target <= 100000 && (totalValCount[target] - count1[target]) > 0) {
                let w2 = n - 1 - j;
                if (m > 1 && w2 > 1) return true;
                if (m > 1 && (target === grid[0][j + 1] || target === grid[m - 1][j + 1])) return true;
                if (w2 > 1 && (target === grid[0][j + 1] || target === grid[0][n - 1])) return true;
                if (m === 1 && w2 === 1 && target === grid[0][j + 1]) return true;
            }
        }
    }
    return false;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function canPartitionGrid(grid: number[][]): boolean {
    const m = grid.length;
    const n = grid[0].length;
    let totalSum = 0;
    const rowSums = new Array(m).fill(0);
    const colSums = new Array(n).fill(0);
    let map2 = new Map<number, number>();

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const val = grid[i][j];
            totalSum += val;
            rowSums[i] += val;
            colSums[j] += val;
            map2.set(val, (map2.get(val) || 0) + 1);
        }
    }

    const isValid = (x: number, r_start: number, r_end: number, c_start: number, c_end: number, map: Map<number, number>): boolean => {
        const H = r_end - r_start + 1;
        const W = c_end - c_start + 1;
        if (H >= 2 && W >= 2) return map.has(x);
        if (H === 1 && W === 1) return grid[r_start][c_start] === x;
        if (H === 1) return grid[r_start][c_start] === x || grid[r_start][c_end] === x;
        if (W === 1) return grid[r_start][c_start] === x || grid[r_end][c_start] === x;
        return false;
    };

    let s1 = 0, map1 = new Map<number, number>();
    for (let i = 0; i < m - 1; i++) {
        for (let j = 0; j < n; j++) {
            const val = grid[i][j];
            map1.set(val, (map1.get(val) || 0) + 1);
            const count2 = map2.get(val)!;
            if (count2 === 1) map2.delete(val); else map2.set(val, count2 - 1);
        }
        s1 += rowSums[i];
        let s2 = totalSum - s1;
        if (s1 === s2) return true;
        if (s1 > s2) { if (isValid(s1 - s2, 0, i, 0, n - 1, map1)) return true; }
        else { if (isValid(s2 - s1, i + 1, m - 1, 0, n - 1, map2)) return true; }
    }

    s1 = 0; map1.clear(); map2.clear();
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const val = grid[i][j];
            map2.set(val, (map2.get(val) || 0) + 1);
        }
    }

    for (let j = 0; j < n - 1; j++) {
        for (let i = 0; i < m; i++) {
            const val = grid[i][j];
            map1.set(val, (map1.get(val) || 0) + 1);
            const count2 = map2.get(val)!;
            if (count2 === 1) map2.delete(val); else map2.set(val, count2 - 1);
        }
        s1 += colSums[j];
        let s2 = totalSum - s1;
        if (s1 === s2) return true;
        if (s1 > s2) { if (isValid(s1 - s2, 0, m - 1, 0, j, map1)) return true; }
        else { if (isValid(s2 - s1, 0, m - 1, j + 1, n - 1, map2)) return true; }
    }

    return false;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function canPartitionGrid($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $totalSum = 0;
        $rowSums = array_fill(0, $m, 0);
        $colSums = array_fill(0, $n, 0);
        $map2 = [];

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $val = $grid[$i][$j];
                $totalSum += $val;
                $rowSums[$i] += $val;
                $colSums[$j] += $val;
                $map2[$val] = ($map2[$val] ?? 0) + 1;
            }
        }

        $isValid = function($x, $rs, $re, $cs, $ce, &$map) use (&$grid) {
            $h = $re - $rs + 1;
            $w = $ce - $cs + 1;
            if ($h >= 2 && $w >= 2) return isset($map[$x]);
            if ($h === 1 && $w === 1) return $grid[$rs][$cs] === $x;
            if ($h === 1) return $grid[$rs][$cs] === $x || $grid[$rs][$ce] === $x;
            if ($w === 1) return $grid[$rs][$cs] === $x || $grid[$re][$cs] === $x;
            return false;
        };

        $s1 = 0; $map1 = [];
        for ($i = 0; $i < $m - 1; $i++) {
            foreach ($grid[$i] as $val) {
                $map1[$val] = ($map1[$val] ?? 0) + 1;
                if (--$map2[$val] === 0) unset($map2[$val]);
            }
            $s1 += $rowSums[$i];
            $s2 = $totalSum - $s1;
            if ($s1 === $s2) return true;
            if ($s1 > $s2) { if ($isValid($s1 - $s2, 0, $i, 0, $n - 1, $map1)) return true; }
            else { if ($isValid($s2 - $s1, $i + 1, $m - 1, 0, $n - 1, $map2)) return true; }
        }

        $s1 = 0; $map1 = []; $map2 = [];
        foreach ($grid as $row) foreach ($row as $v) $map2[$v] = ($map2[$v] ?? 0) + 1;
        for ($j = 0; $j < $n - 1; $j++) {
            for ($i = 0; $i < $m; $i++) {
                $val = $grid[$i][$j];
                $map1[$val] = ($map1[$val] ?? 0) + 1;
                if (--$map2[$val] === 0) unset($map2[$val]);
            }
            $s1 += $colSums[$j];
            $s2 = $totalSum - $s1;
            if ($s1 === $s2) return true;
            if ($s1 > $s2) { if ($isValid($s1 - $s2, 0, $m - 1, 0, $j, $map1)) return true; }
            else { if ($isValid($s2 - $s1, 0, $m - 1, $j + 1, $n - 1, $map2)) return true; }
        }
        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func canPartitionGrid(_ grid: [[Int]]) -> Bool {
        let m = grid.count
        let n = grid[0].count
        var totalSum = 0
        var rowSums = Array(repeating: 0, count: m)
        var colSums = Array(repeating: 0, count: n)
        var map2 = [Int: Int]()

        for i in 0..<m {
            for j in 0..<n {
                let val = grid[i][j]
                totalSum += val
                rowSums[i] += val
                colSums[j] += val
                map2[val, default: 0] += 1
            }
        }

        func isValid(_ x: Int, _ rs: Int, _ re: Int, _ cs: Int, _ ce: Int, _ map: [Int: Int]) -> Bool {
            let h = re - rs + 1, w = ce - cs + 1
            if h >= 2 && w >= 2 { return map[x] != nil }
            if h == 1 && w == 1 { return grid[rs][cs] == x }
            if h == 1 { return grid[rs][cs] == x || grid[rs][ce] == x }
            if w == 1 { return grid[rs][cs] == x || grid[re][cs] == x }
            return false
        }

        var s1 = 0, map1 = [Int: Int]()
        for i in 0..<m - 1 {
            for j in 0..<n {
                let val = grid[i][j]
                map1[val, default: 0] += 1
                map2[val]! -= 1
                if map2[val] == 0 { map2[val] = nil }
            }
            s1 += rowSums[i]
            let s2 = totalSum - s1
            if s1 == s2 { return true }
            if s1 > s2 { if isValid(s1 - s2, 0, i, 0, n - 1, map1) { return true } }
            else { if isValid(s2 - s1, i + 1, m - 1, 0, n - 1, map2) { return true } }
        }

        s1 = 0; map1 = [:]; map2 = [:]
        for r in grid { for v in r { map2[v, default: 0] += 1 } }
        for j in 0..<n - 1 {
            for i in 0..<m {
                let val = grid[i][j]
                map1[val, default: 0] += 1
                map2[val]! -= 1
                if map2[val] == 0 { map2[val] = nil }
            }
            s1 += colSums[j]
            let s2 = totalSum - s1
            if s1 == s2 { return true }
            if s1 > s2 { if isValid(s1 - s2, 0, m - 1, 0, j, map1) { return true } }
            else { if isValid(s2 - s1, 0, m - 1, j + 1, n - 1, map2) { return true } }
        }
        return false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun canPartitionGrid(grid: Array<IntArray>): Boolean {
        val m = grid.size
        val n = grid[0].size
        var totalSum: Long = 0
        val rowSums = LongArray(m)
        val colSums = LongArray(n)
        val map2 = HashMap<Int, Int>()
        for (i in 0 until m) {
            for (j in 0 until n) {
                val v = grid[i][j]
                totalSum += v
                rowSums[i] += v.toLong()
                colSums[j] += v.toLong()
                map2[v] = map2.getOrDefault(v, 0) + 1
            }
        }
        fun isValid(x: Long, rs: Int, re: Int, cs: Int, ce: Int, map: HashMap<Int, Int>): Boolean {
            val h = re - rs + 1
            val w = ce - cs + 1
            if (x > Int.MAX_VALUE) return false
            val xi = x.toInt()
            if (h >= 2 && w >= 2) return map.containsKey(xi)
            if (h == 1 && w == 1) return grid[rs][cs] == xi
            if (h == 1) return grid[rs][cs] == xi || grid[rs][ce] == xi
            if (w == 1) return grid[rs][cs] == xi || grid[re][cs] == xi
            return false
        }
        var s1: Long = 0
        val map1 = HashMap<Int, Int>()
        for (i in 0 until m - 1) {
            for (j in 0 until n) {
                val v = grid[i][j]
                map1[v] = map1.getOrDefault(v, 0) + 1
                map2[v] = map2[v]!! - 1
                if (map2[v] == 0) map2.remove(v)
            }
            s1 += rowSums[i]
            val s2 = totalSum - s1
            if (s1 == s2) return true
            if (s1 > s2) { if (isValid(s1 - s2, 0, i, 0, n - 1, map1)) return true }
            else { if (isValid(s2 - s1, i + 1, m - 1, 0, n - 1, map2)) return true }
        }
        s1 = 0; map1.clear(); map2.clear()
        for (row in grid) for (v in row) map2[v] = map2.getOrDefault(v, 0) + 1
        for (j in 0 until n - 1) {
            for (i in 0 until m) {
                val v = grid[i][j]
                map1[v] = map1.getOrDefault(v, 0) + 1
                map2[v] = map2[v]!! - 1
                if (map2[v] == 0) map2.remove(v)
            }
            s1 += colSums[j]
            val s2 = totalSum - s1
            if (s1 == s2) return true
            if (s1 > s2) { if (isValid(s1 - s2, 0, m - 1, 0, j, map1)) return true }
            else { if (isValid(s2 - s1, 0, m - 1, j + 1, n - 1, map2)) return true }
        }
        return false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool canPartitionGrid(List<List<int>> grid) {
    int m = grid.length, n = grid[0].length, totalSum = 0;
    List<int> rowSums = List.filled(m, 0), colSums = List.filled(n, 0);
    Map<int, int> map2 = {};
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        int v = grid[i][j];
        totalSum += v; rowSums[i] += v; colSums[j] += v;
        map2[v] = (map2[v] ?? 0) + 1;
      }
    }
    bool isValid(int x, int rs, int re, int cs, int ce, Map<int, int> map) {
      int h = re - rs + 1, w = ce - cs + 1;
      if (h >= 2 && w >= 2) return map.containsKey(x);
      if (h == 1 && w == 1) return grid[rs][cs] == x;
      if (h == 1) return grid[rs][cs] == x || grid[rs][ce] == x;
      if (w == 1) return grid[rs][cs] == x || grid[re][cs] == x;
      return false;
    }
    int s1 = 0; Map<int, int> map1 = {};
    for (int i = 0; i < m - 1; i++) {
      for (int val in grid[i]) {
        map1[val] = (map1[val] ?? 0) + 1;
        map2[val] = map2[val]! - 1;
        if (map2[val] == 0) map2.remove(val);
      }
      s1 += rowSums[i];
      int s2 = totalSum - s1;
      if (s1 == s2) return true;
      if (s1 > s2) { if (isValid(s1 - s2, 0, i, 0, n - 1, map1)) return true; }
      else { if (isValid(s2 - s1, i + 1, m - 1, 0, n - 1, map2)) return true; }
    }
    s1 = 0; map1.clear(); map2.clear();
    for (var r in grid) for (var v in r) map2[v] = (map2[v] ?? 0) + 1;
    for (int j = 0; j < n - 1; j++) {
      for (int i = 0; i < m; i++) {
        int v = grid[i][j];
        map1[v] = (map1[v] ?? 0) + 1;
        map2[v] = map2[v]! - 1;
        if (map2[v] == 0) map2.remove(v);
      }
      s1 += colSums[j];
      int s2 = totalSum - s1;
      if (s1 == s2) return true;
      if (s1 > s2) { if (isValid(s1 - s2, 0, m - 1, 0, j, map1)) return true; }
      else { if (isValid(s2 - s1, 0, m - 1, j + 1, n - 1, map2)) return true; }
    }
    return false;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func canPartitionGrid(grid [][]int) bool {
    m, n := len(grid), len(grid[0])
    var totalSum int64
    rowSums, colSums := make([]int64, m), make([]int64, n)
    map2 := make(map[int]int)
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            v := grid[i][j]
            totalSum += int64(v)
            rowSums[i] += int64(v)
            colSums[j] += int64(v)
            map2[v]++
        }
    }
    isValid := func(x int64, rs, re, cs, ce int, freq map[int]int) bool {
        h, w := re-rs+1, ce-cs+1
        xi := int(x)
        if x > 1000000000 { return false }
        if h >= 2 && w >= 2 { _, ok := freq[xi]; return ok }
        if h == 1 && w == 1 { return grid[rs][cs] == xi }
        if h == 1 { return grid[rs][cs] == xi || grid[rs][ce] == xi }
        if w == 1 { return grid[rs][cs] == xi || grid[re][cs] == xi }
        return false
    }
    var s1 int64; map1 := make(map[int]int)
    for i := 0; i < m-1; i++ {
        for _, v := range grid[i] {
            map1[v]++; map2[v]--; if map2[v] == 0 { delete(map2, v) }
        }
        s1 += rowSums[i]; s2 := totalSum - s1
        if s1 == s2 { return true }
        if s1 > s2 { if isValid(s1-s2, 0, i, 0, n-1, map1) { return true } }
        if s2 > s1 { if isValid(s2-s1, i+1, m-1, 0, n-1, map2) { return true } }
    }
    s1 = 0; map1 = make(map[int]int); map2 = make(map[int]int)
    for i := 0; i < m; i++ { for j := 0; j < n; j++ { map2[grid[i][j]]++ } }
    for j := 0; j < n-1; j++ {
        for i := 0; i < m; i++ {
            v := grid[i][j]; map1[v]++; map2[v]--; if map2[v] == 0 { delete(map2, v) }
        }
        s1 += colSums[j]; s2 := totalSum - s1
        if s1 == s2 { return true }
        if s1 > s2 { if isValid(s1-s2, 0, m-1, 0, j, map1) { return true } }
        if s2 > s1 { if isValid(s2-s1, 0, m-1, j+1, n-1, map2) { return true } }
    }
    return false
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def check_h(grid, m, n)
  row_sums = grid.map { |row| row.sum }
  total_sum = row_sums.sum
  count1 = Hash.new(0)
  count2 = Hash.new(0)
  grid.each { |row| row.each { |val| count2[val] += 1 } }
  s1 = 0
  (0...m - 1).each do |i|
    s1 += row_sums[i]
    s2 = total_sum - s1
    grid[i].each do |val|
      count1[val] += 1
      count2[val] -= 1
      count2.delete(val) if count2[val] == 0
    end

    if s1 == s2
      return true
    elsif s1 > s2
      target = s1 - s2
      if i + 1 > 1 && n > 1
        return true if count1.key?(target)
      elsif i + 1 == 1 && n > 1
        return true if target == grid[0][0] || target == grid[0][n - 1]
      elsif n == 1 && i + 1 > 1
        return true if target == grid[0][0] || target == grid[i][0]
      elsif i + 1 == 1 && n == 1
        return true if target == grid[0][0]
      end
    else
      target = s2 - s1
      if m - i - 1 > 1 && n > 1
        return true if count2.key?(target)
      elsif m - i - 1 == 1 && n > 1
        return true if target == grid[m - 1][0] || target == grid[m - 1][n - 1]
      elsif n == 1 && m - i - 1 > 1
        return true if target == grid[i + 1][0] || target == grid[m - 1][0]
      elsif m - i - 1 == 1 && n == 1
        return true if target == grid[m - 1][0]
      end
    end
  end
  false
end

def can_partition_grid(grid)
  return true if check_h(grid, grid.size, grid[0].size)
  return true if check_h(grid.transpose, grid[0].size, grid.size)
  false
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
  def canPartitionGrid(grid: Array[Array[Int]]): Boolean = {
    def check(g: Array[Array[Int]]): Boolean = {
      val m = g.length
      if (m < 2) return false
      val n = g(0).length
      val rowSums = g.map(_.map(_.toLong).sum)
      val totalSum = rowSums.sum
      val count1 = mutable.HashMap[Int, Int]().withDefaultValue(0)
      val count2 = mutable.HashMap[Int, Int]().withDefaultValue(0)
      for (r <- 0 until m; c <- 0 until n) { val v = g(r)(c); count2(v) += 1 }
      var s1 = 0L
      for (i <- 0 until m - 1) {
        s1 += rowSums(i)
        val s2 = totalSum - s1
        for (c <- 0 until n) {
          val v = g(i)(c)
          count1(v) += 1
          count2(v) -= 1
          if (count2(v) == 0) count2.remove(v)
        }
        if (s1 == s2) return true
        if (s1 > s2) {
          val target = s1 - s2
          if (target <= 1000000000L) {
            val t = target.toInt
            val r1 = i + 1; val c1 = n
            if (r1 > 1 && c1 > 1) { if (count1.contains(t)) return true }
            else if (r1 == 1 && c1 > 1) { if (t == g(0)(0) || t == g(0)(n - 1)) return true }
            else if (c1 == 1 && r1 > 1) { if (t == g(0)(0) || t == g(i)(0)) return true }
            else if (r1 == 1 && c1 == 1) { if (t == g(0)(0)) return true }
          }
        } else {
          val target = s2 - s1
          if (target <= 1000000000L) {
            val t = target.toInt
            val r2 = m - i - 1; val c2 = n
            if (r2 > 1 && c2 > 1) { if (count2.contains(t)) return true }
            else if (r2 == 1 && c2 > 1) { if (t == g(m - 1)(0) || t == g(m - 1)(n - 1)) return true }
            else if (c2 == 1 && r2 > 1) { if (t == g(i + 1)(0) || t == g(m - 1)(0)) return true }
            else if (r2 == 1 && c2 == 1) { if (t == g(m - 1)(0)) return true }
          }
        }
      }
      false
    }
    check(grid) || check(grid.transpose)
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashMap;

impl Solution {
    pub fn can_partition_grid(grid: Vec<Vec<i32>>) -> bool {
        fn check(g: &Vec<Vec<i32>>) -> bool {
            let m = g.len();
            let n = g[0].len();
            if m < 2 { return false; }
            let mut row_sums = vec![0i64; m];
            let mut total_sum = 0i64;
            let mut count2 = HashMap::new();
            for r in 0..m {
                for c in 0..n {
                    let v = g[r][c];
                    row_sums[r] += v as i64;
                    *count2.entry(v).or_insert(0) += 1;
                }
                total_sum += row_sums[r];
            }
            let mut s1 = 0i64;
            let mut count1 = HashMap::new();
            for i in 0..m - 1 {
                s1 += row_sums[i];
                let s2 = total_sum - s1;
                for c in 0..n {
                    let v = g[i][c];
                    *count1.entry(v).or_insert(0) += 1;
                    let c2 = count2.get_mut(&v).unwrap();
                    *c2 -= 1;
                    if *c2 == 0 { count2.remove(&v); }
                }
                if s1 == s2 { return true; }
                if s1 > s2 {
                    let target = s1 - s2;
                    if target <= 1000000 { 
                        let t = target as i32;
                        let r1 = i + 1; let c1 = n;
                        if r1 > 1 && c1 > 1 { if count1.contains_key(&t) { return true; } }
                        else if r1 == 1 && c1 > 1 { if t == g[0][0] || t == g[0][n-1] { return true; } }
                        else if c1 == 1 && r1 > 1 { if t == g[0][0] || t == g[i][0] { return true; } }
                        else if r1 == 1 && c1 == 1 { if t == g[0][0] { return true; } }
                    }
                } else {
                    let target = s2 - s1;
                    if target <= 1000000 {
                        let t = target as i32;
                        let r2 = m - i - 1; let c2 = n;
                        if r2 > 1 && c2 > 1 { if count2.contains_key(&t) { return true; } }
                        else if r2 == 1 && c2 > 1 { if t == g[m-1][0] || t == g[m-1][n-1] { return true; } }
                        else if c2 == 1 && r2 > 1 { if t == g[i+1][0] || t == g[m-1][0] { return true; } }
                        else if r2 == 1 && c2 == 1 { if t == g[m-1][0] { return true; } }
                    }
                }
            }
            false
        }
        if check(&grid) { return true; }
        let m = grid.len();
        let n = grid[0].len();
        let mut transposed = vec![vec![0; m]; n];
        for r in 0..m { for c in 0..n { transposed[c][r] = grid[r][c]; } }
        check(&transposed)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (can-partition-grid grid)
  (-> (listof (listof exact-integer?)) boolean?)
  (define (check g)
    (let* ([m (length g)] [n (length (first g))]
           [g-vec (list->vector (map list->vector g))]
           [row-sums (list->vector (map (lambda (row) (apply + row)) g))]
           [total-sum (for/sum ([s row-sums]) s)]
           [count1 (make-hash)] [count2 (make-hash)])
      (for* ([r (in-range m)] [c (in-range n)])
        (let ([v (vector-ref (vector-ref g-vec r) c)])
          (hash-set! count2 v (+ (hash-ref count2 v 0) 1))))
      (let loop ([i 0] [s1 0])
        (if (< i (- m 1))
            (let* ([s1-new (+ s1 (vector-ref row-sums i))] [s2 (- total-sum s1-new)])
              (for ([c (in-range n)])
                (let* ([v (vector-ref (vector-ref g-vec i) c)] [c2 (hash-ref count2 v)])
                  (hash-set! count1 v (+ (hash-ref count1 v 0) 1))
                  (if (= c2 1) (hash-remove! count2 v) (hash-set! count2 v (- c2 1)))))
              (cond
                [(= s1-new s2) #t]
                [(> s1-new s2)
                 (let ([target (- s1-new s2)])
                   (if (let ([r1 (+ i 1)] [c1 n])
                         (cond [(and (> r1 1) (> c1 1)) (hash-has-key? count1 target)]
                               [(and (= r1 1) (> c1 1)) (or (= target (vector-ref (vector-ref g-vec 0) 0)) (= target (vector-ref (vector-ref g-vec 0) (- n 1))))]
                               [(and (= c1 1) (> r1 1)) (or (= target (vector-ref (vector-ref g-vec 0) 0)) (= target (vector-ref (vector-ref g-vec i) 0)))]
                               [else (= target (vector-ref (vector-ref g-vec 0) 0))]))
                       #t (loop (+ i 1) s1-new))]
                [else
                 (let ([target (- s2 s1-new)])
                   (if (let ([r2 (- m i 1)] [c2 n])
                         (cond [(and (> r2 1) (> c2 1)) (hash-has-key? count2 target)]
                               [(and (= r2 1) (> c2 1)) (or (= target (vector-ref (vector-ref g-vec (- m 1)) 0)) (= target (vector-ref (vector-ref g-vec (- m 1)) (- n 1))))]
                               [(and (= c2 1) (> r2 1)) (or (= target (vector-ref (vector-ref g-vec (+ i 1)) 0)) (= target (vector-ref (vector-ref g-vec (- m 1)) 0)))]
                               [else (= target (vector-ref (vector-ref g-vec (- m 1)) 0))]))
                       #t (loop (+ i 1) s1-new))]))
            #f))))
  (or (check grid) (if (null? grid) #f (check (apply map list grid)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec can_partition_grid(Grid :: [[integer()]]) -> boolean().
can_partition_grid(Grid) ->
    check_h(Grid) orelse check_h(transpose(Grid)).

transpose([[]|_]) -> [];
transpose(Grid) -> [lists:map(fun hd/1, Grid) | transpose(lists:map(fun tl/1, Grid))].

check_h(Grid) ->
    M = length(Grid),
    if M < 2 -> false;
       true -> 
           RowSums = [lists:sum(Row) || Row <- Grid],
           TotalSum = lists:sum(RowSums),
           Count2 = lists:foldl(fun(Row, Acc) ->
               lists:foldl(fun(V, Acc2) ->
                   maps:update_with(V, fun(C) -> C + 1 end, 1, Acc2)
               end, Acc, Row) end, #{}, Grid),
           GridVec = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),
           RowSumsVec = list_to_tuple(RowSums),
           check_h_loop(1, 0, M, length(element(1, GridVec)), TotalSum, RowSumsVec, GridVec, #{}, Count2)
    end.

check_h_loop(I, S1, M, N, TotalSum, RowSumsVec, GridVec, Count1, Count2) when I < M ->
    RowI = element(I, GridVec),
    S1Next = S1 + element(I, RowSumsVec),
    S2 = TotalSum - S1Next,
    {NewCount1, NewCount2} = update_counts(tuple_to_list(RowI), Count1, Count2),
    case check_cond(I, S1Next, S2, M, N, GridVec, NewCount1, NewCount2) of
        true -> true;
        false -> check_h_loop(I + 1, S1Next, M, N, TotalSum, RowSumsVec, GridVec, NewCount1, NewCount2)
    end;
check_h_loop(_, _, _, _, _, _, _, _, _) -> false.

update_counts([], C1, C2) -> {C1, C2};
update_counts([V|Rest], C1, C2) ->
    NewC1 = maps:update_with(V, fun(C) -> C + 1 end, 1, C1),
    NewC2 = case maps:get(V, C2) of 1 -> maps:remove(V, C2); N -> maps:put(V, N - 1, C2) end,
    update_counts(Rest, NewC1, NewC2).

check_cond(I, S1, S2, M, N, GridVec, C1, C2) ->
    if S1 == S2 -> true;
       S1 > S2 -> 
           T = S1 - S2, R1 = I, 
           if (R1>1) and (N>1) -> maps:is_key(T, C1);
              (R1==1) and (N>1) -> (T == element(1, element(1, GridVec))) orelse (T == element(N, element(1, GridVec)));
              (N==1) and (R1>1) -> (T == element(1, element(1, GridVec))) orelse (T == element(1, element(I, GridVec)));
              true -> T == element(1, element(1, GridVec))
           end;
       S2 > S1 -> 
           T = S2 - S1, R2 = M - I,
           if (R2>1) and (N>1) -> maps:is_key(T, C2);
              (R2==1) and (N>1) -> (T == element(1, element(M, GridVec))) orelse (T == element(N, element(M, GridVec)));
              (N==1) and (R2>1) -> (T == element(1, element(I+1, GridVec))) orelse (T == element(1, element(M, GridVec)));
              true -> T == element(1, element(M, GridVec))
           end
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec can_partition_grid(grid :: [[integer]]) :: boolean
  def can_partition_grid(grid) do
    check_h(grid) or check_h(grid |> Enum.zip() |> Enum.map(&Tuple.to_list/1))
  end

  defp check_h(grid) do
    m = length(grid)
    if m < 2, do: false, else: (
      n = length(hd(grid))
      row_sums = Enum.map(grid, &Enum.sum/1)
      total_sum = Enum.sum(row_sums)
      count2 = Enum.reduce(grid, %{}, fn row, acc ->
        Enum.reduce(row, acc, fn v, a -> Map.update(a, v, 1, &(&1 + 1)) end)
      end)
      grid_vec = grid |> Enum.map(&List.to_tuple/1) |> List.to_tuple()
      row_sums_vec = List.to_tuple(row_sums)
      check_h_loop(1, 0, m, n, total_sum, row_sums_vec, grid_vec, %{}, count2)
    )
  end

  defp check_h_loop(i, s1, m, n, total_sum, row_sums_vec, grid_vec, count1, count2) when i < m do
    row_i = element_at(grid_vec, i)
    s1_next = s1 + elem(row_sums_vec, i - 1)
    s2 = total_sum - s1_next
    {new_c1, new_c2} = update_counts(Tuple.to_list(row_i), count1, count2)
    if check_condition(i, s1_next, s2, m, n, grid_vec, new_c1, new_c2) do true
    else check_h_loop(i + 1, s1_next, m, n, total_sum, row_sums_vec, grid_vec, new_c1, new_c2) end
  end
  defp check_h_loop(_, _, _, _, _, _, _, _, _), do: false

  defp update_counts(row, c1, c2) do
    Enum.reduce(row, {c1, c2}, fn v, {a1, a2} ->
      {Map.update(a1, v, 1, &(&1 + 1)), case Map.get(a2, v) do 1 -> Map.delete(a2, v); n -> Map.put(a2, v, n - 1) end}
    end)
  end

  defp check_condition(i, s1, s2, m, n, grid_vec, c1, c2) do
    cond do
      s1 == s2 -> true
      s1 > s2 ->
        t = s1 - s2
        cond do
          i > 1 and n > 1 -> Map.has_key?(c1, t)
          i == 1 and n > 1 -> t == elem(elem(grid_vec, 0), 0) or t == elem(elem(grid_vec, 0), n - 1)
          n == 1 and i > 1 -> t == elem(elem(grid_vec, 0), 0) or t == elem(elem(grid_vec, i - 1), 0)
          true -> t == elem(elem(grid_vec, 0), 0)
        end
      true ->
        t = s2 - s1
        r2 = m - i
        cond do
          r2 > 1 and n > 1 -> Map.has_key?(c2, t)
          r2 == 1 and n > 1 -> t == elem(elem(grid_vec, m - 1), 0) or t == elem(elem(grid_vec, m - 1), n - 1)
          n == 1 and r2 > 1 -> t == elem(elem(grid_vec, i), 0) or t == elem(elem(grid_vec, m - 1), 0)
          true -> t == elem(elem(grid_vec, m - 1), 0)
        end
    end
  end
  defp element_at(tuple, i), do: elem(tuple, i - 1)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m * n + V), where m and n are the grid dimensions and V is the maximum value in the grid. We perform a constant number of passes over the grid to compute row and column sums and maintain frequency counts of elements. Frequency maps or arrays of size up to 10^5 are used to check for target values in O(1) time.
- **Space Complexity:** O(m * n + V) to store the grid, row/column sums, and the frequency counts of cell values. The total number of cells m * n is up to 10^5, and the maximum cell value V is also 10^5.
