---
layout: post
title: "Magic Squares In Grid"
date: 2025-12-30 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Math", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/magic-squares-in-grid/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool isMagic(int r, int c, const std::vector<std::vector<int>>&\
        \ grid) {\n        // 1. Center must be 5\n        if (grid[r+1][c+1] != 5)\
        \ {\n            return false;\n        }\n\n        // 2. All numbers must\
        \ be distinct and between 1 and 9\n        std::vector<bool> seen(10, false);\n\
        \        for (int i = 0; i < 3; ++i) {\n            for (int j = 0; j < 3; ++j)\
        \ {\n                int num = grid[r+i][c+j];\n                if (num < 1\
        \ || num > 9) {\n                    return false;\n                }\n    \
        \            if (seen[num]) {\n                    return false; // Duplicate\n\
        \                }\n                seen[num] = true;\n            }\n     \
        \   }\n\n        // 3. All sums must be 15\n        // Rows\n        if (!((grid[r][c]\
        \ + grid[r][c+1] + grid[r][c+2] == 15) &&\n              (grid[r+1][c] + grid[r+1][c+1]\
        \ + grid[r+1][c+2] == 15) &&\n              (grid[r+2][c] + grid[r+2][c+1] +\
        \ grid[r+2][c+2] == 15))) {\n            return false;\n        }\n\n      \
        \  // Columns\n        if (!((grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15)\
        \ &&\n              (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15) &&\n\
        \              (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15))) {\n\
        \            return false;\n        }\n\n        // Diagonals\n        if (!((grid[r][c]\
        \ + grid[r+1][c+1] + grid[r+2][c+2] == 15) &&\n              (grid[r][c+2] +\
        \ grid[r+1][c+1] + grid[r+2][c] == 15))) {\n            return false;\n    \
        \    }\n\n        return true;\n    }\n\n    int numMagicSquaresInside(std::vector<std::vector<int>>&\
        \ grid) {\n        int R = grid.size();\n        int C = grid[0].size();\n\n\
        \        if (R < 3 || C < 3) {\n            return 0;\n        }\n\n       \
        \ int count = 0;\n        for (int r = 0; r <= R - 3; ++r) {\n            for\
        \ (int c = 0; c <= C - 3; ++c) {\n                if (isMagic(r, c, grid)) {\n\
        \                    count++;\n                }\n            }\n        }\n\
        \n        return count;\n    }\n};"
      java: "import java.util.HashSet;\nimport java.util.Set;\n\nclass Solution {\n\
        \    public int numMagicSquaresInside(int[][] grid) {\n        int R = grid.length;\n\
        \        int C = grid[0].length;\n\n        if (R < 3 || C < 3) {\n        \
        \    return 0;\n        }\n\n        int count = 0;\n        for (int r = 0;\
        \ r <= R - 3; ++r) {\n            for (int c = 0; c <= C - 3; ++c) {\n     \
        \           if (isMagic(r, c, grid)) {\n                    count++;\n     \
        \           }\n            }\n        }\n\n        return count;\n    }\n\n\
        \    private boolean isMagic(int r, int c, int[][] grid) {\n        // 1. Center\
        \ must be 5\n        if (grid[r+1][c+1] != 5) {\n            return false;\n\
        \        }\n\n        // 2. All numbers must be distinct and between 1 and 9\n\
        \        boolean[] seen = new boolean[10]; // Indices 1-9\n        for (int\
        \ i = 0; i < 3; ++i) {\n            for (int j = 0; j < 3; ++j) {\n        \
        \        int num = grid[r+i][c+j];\n                if (num < 1 || num > 9)\
        \ {\n                    return false;\n                }\n                if\
        \ (seen[num]) {\n                    return false; // Duplicate\n          \
        \      }\n                seen[num] = true;\n            }\n        }\n\n  \
        \      // 3. All sums must be 15\n        // Rows\n        if (!((grid[r][c]\
        \ + grid[r][c+1] + grid[r][c+2] == 15) &&\n              (grid[r+1][c] + grid[r+1][c+1]\
        \ + grid[r+1][c+2] == 15) &&\n              (grid[r+2][c] + grid[r+2][c+1] +\
        \ grid[r+2][c+2] == 15))) {\n            return false;\n        }\n\n      \
        \  // Columns\n        if (!((grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15)\
        \ &&\n              (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15) &&\n\
        \              (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15))) {\n\
        \            return false;\n        }\n\n        // Diagonals\n        if (!((grid[r][c]\
        \ + grid[r+1][c+1] + grid[r+2][c+2] == 15) &&\n              (grid[r][c+2] +\
        \ grid[r+1][c+1] + grid[r+2][c] == 15))) {\n            return false;\n    \
        \    }\n\n        return true;\n    }\n}"
      python: "class Solution:\n    def numMagicSquaresInside(self, grid: List[List[int]])\
        \ -> int:\n        R, C = len(grid), len(grid[0])\n\n        def is_magic(r,\
        \ c):\n            # 1. Center must be 5\n            if grid[r+1][c+1] != 5:\n\
        \                return False\n\n            # 2. All numbers must be distinct\
        \ and between 1 and 9\n            seen = [False] * 10\n            for i in\
        \ range(3):\n                for j in range(3):\n                    num = grid[r+i][c+j]\n\
        \                    if not (1 <= num <= 9):\n                        return\
        \ False\n                    if seen[num]:\n                        return False\
        \ # Duplicate\n                    seen[num] = True\n\n            # 3. All\
        \ sums must be 15\n            # Rows\n            if not (grid[r][c] + grid[r][c+1]\
        \ + grid[r][c+2] == 15 and \\\n                    grid[r+1][c] + grid[r+1][c+1]\
        \ + grid[r+1][c+2] == 15 and \\\n                    grid[r+2][c] + grid[r+2][c+1]\
        \ + grid[r+2][c+2] == 15):\n                return False\n\n            # Columns\n\
        \            if not (grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15 and \\\n\
        \                    grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15 and\
        \ \\\n                    grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] ==\
        \ 15):\n                return False\n\n            # Diagonals\n          \
        \  if not (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15 and \\\n     \
        \               grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15):\n     \
        \           return False\n\n            return True\n\n        count = 0\n \
        \       if R < 3 or C < 3:\n            return 0\n\n        for r in range(R\
        \ - 2):\n            for c in range(C - 2):\n                if is_magic(r,\
        \ c):\n                    count += 1\n\n        return count"
      python3: "class Solution:\n    def numMagicSquaresInside(self, grid: List[List[int]])\
        \ -> int:\n        R, C = len(grid), len(grid[0])\n\n        def is_magic(r,\
        \ c):\n            # 1. Center must be 5\n            if grid[r+1][c+1] != 5:\n\
        \                return False\n\n            # 2. All numbers must be distinct\
        \ and between 1 and 9\n            seen = [False] * 10\n            for i in\
        \ range(3):\n                for j in range(3):\n                    num = grid[r+i][c+j]\n\
        \                    if not (1 <= num <= 9):\n                        return\
        \ False\n                    if seen[num]:\n                        return False\
        \ # Duplicate\n                    seen[num] = True\n\n            # 3. All\
        \ sums must be 15\n            # Rows\n            if not (grid[r][c] + grid[r][c+1]\
        \ + grid[r][c+2] == 15 and \\\n                    grid[r+1][c] + grid[r+1][c+1]\
        \ + grid[r+1][c+2] == 15 and \\\n                    grid[r+2][c] + grid[r+2][c+1]\
        \ + grid[r+2][c+2] == 15):\n                return False\n\n            # Columns\n\
        \            if not (grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15 and \\\n\
        \                    grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15 and\
        \ \\\n                    grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] ==\
        \ 15):\n                return False\n\n            # Diagonals\n          \
        \  if not (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15 and \\\n     \
        \               grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15):\n     \
        \           return False\n\n            return True\n\n        count = 0\n \
        \       if R < 3 or C < 3:\n            return 0\n\n        for r in range(R\
        \ - 2):\n            for c in range(C - 2):\n                if is_magic(r,\
        \ c):\n                    count += 1\n\n        return count"
      c: "#include <stdbool.h>\n#include <string.h> // For memset\n\n// Helper function\
        \ to check if a 3x3 subgrid starting at (r, c) is a magic square\nbool isMagic(int\
        \ r, int c, int** grid, int gridSize, int* gridColSize) {\n    // 1. Center\
        \ must be 5\n    if (grid[r+1][c+1] != 5) {\n        return false;\n    }\n\n\
        \    // 2. All numbers must be distinct and between 1 and 9\n    bool seen[10];\
        \ // Indices 1-9\n    memset(seen, 0, sizeof(seen)); // Initialize all to false\n\
        \n    for (int i = 0; i < 3; ++i) {\n        for (int j = 0; j < 3; ++j) {\n\
        \            int num = grid[r+i][c+j];\n            if (num < 1 || num > 9)\
        \ {\n                return false;\n            }\n            if (seen[num])\
        \ {\n                return false; // Duplicate\n            }\n           \
        \ seen[num] = true;\n        }\n    }\n\n    // 3. All sums must be 15\n   \
        \ // Rows\n    if (!((grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15) &&\n \
        \         (grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 15) &&\n      \
        \    (grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15))) {\n        return\
        \ false;\n    }\n\n    // Columns\n    if (!((grid[r][c] + grid[r+1][c] + grid[r+2][c]\
        \ == 15) &&\n          (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15)\
        \ &&\n          (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15))) {\n\
        \        return false;\n    }\n\n    // Diagonals\n    if (!((grid[r][c] + grid[r+1][c+1]\
        \ + grid[r+2][c+2] == 15) &&\n          (grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]\
        \ == 15))) {\n        return false;\n    }\n\n    return true;\n}\n\nint numMagicSquaresInside(int**\
        \ grid, int gridSize, int* gridColSize) {\n    int R = gridSize;\n    int C\
        \ = gridColSize[0]; // Assuming all rows have the same number of columns\n\n\
        \    if (R < 3 || C < 3) {\n        return 0;\n    }\n\n    int count = 0;\n\
        \    for (int r = 0; r <= R - 3; ++r) {\n        for (int c = 0; c <= C - 3;\
        \ ++c) {\n            if (isMagic(r, c, grid, gridSize, gridColSize)) {\n  \
        \              count++;\n            }\n        }\n    }\n\n    return count;\n\
        }"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int NumMagicSquaresInside(int[][] grid) {\n        int R = grid.Length;\n\
        \        int C = grid[0].Length;\n\n        if (R < 3 || C < 3) {\n        \
        \    return 0;\n        }\n\n        int count = 0;\n        for (int r = 0;\
        \ r <= R - 3; ++r) {\n            for (int c = 0; c <= C - 3; ++c) {\n     \
        \           if (IsMagic(r, c, grid)) {\n                    count++;\n     \
        \           }\n            }\n        }\n\n        return count;\n    }\n\n\
        \    private bool IsMagic(int r, int c, int[][] grid) {\n        // 1. Center\
        \ must be 5\n        if (grid[r+1][c+1] != 5) {\n            return false;\n\
        \        }\n\n        // 2. All numbers must be distinct and between 1 and 9\n\
        \        bool[] seen = new bool[10]; // Indices 1-9\n        for (int i = 0;\
        \ i < 3; ++i) {\n            for (int j = 0; j < 3; ++j) {\n               \
        \ int num = grid[r+i][c+j];\n                if (num < 1 || num > 9) {\n   \
        \                 return false;\n                }\n                if (seen[num])\
        \ {\n                    return false; // Duplicate\n                }\n   \
        \             seen[num] = true;\n            }\n        }\n\n        // 3. All\
        \ sums must be 15\n        // Rows\n        if (!((grid[r][c] + grid[r][c+1]\
        \ + grid[r][c+2] == 15) &&\n              (grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2]\
        \ == 15) &&\n              (grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] ==\
        \ 15))) {\n            return false;\n        }\n\n        // Columns\n    \
        \    if (!((grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15) &&\n           \
        \   (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15) &&\n            \
        \  (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15))) {\n            return\
        \ false;\n        }\n\n        // Diagonals\n        if (!((grid[r][c] + grid[r+1][c+1]\
        \ + grid[r+2][c+2] == 15) &&\n              (grid[r][c+2] + grid[r+1][c+1] +\
        \ grid[r+2][c] == 15))) {\n            return false;\n        }\n\n        return\
        \ true;\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @return {number}\n */\nvar numMagicSquaresInside\
        \ = function(grid) {\n    const R = grid.length;\n    const C = grid[0].length;\n\
        \n    if (R < 3 || C < 3) {\n        return 0;\n    }\n\n    let count = 0;\n\
        \    for (let r = 0; r <= R - 3; ++r) {\n        for (let c = 0; c <= C - 3;\
        \ ++c) {\n            if (isMagic(r, c, grid)) {\n                count++;\n\
        \            }\n        }\n    }\n\n    return count;\n};\n\nfunction isMagic(r,\
        \ c, grid) {\n    // 1. Center must be 5\n    if (grid[r+1][c+1] !== 5) {\n\
        \        return false;\n    }\n\n    // 2. All numbers must be distinct and\
        \ between 1 and 9\n    const seen = new Array(10).fill(false); // Indices 1-9\n\
        \    for (let i = 0; i < 3; ++i) {\n        for (let j = 0; j < 3; ++j) {\n\
        \            const num = grid[r+i][c+j];\n            if (num < 1 || num > 9)\
        \ {\n                return false;\n            }\n            if (seen[num])\
        \ {\n                return false; // Duplicate\n            }\n           \
        \ seen[num] = true;\n        }\n    }\n\n    // 3. All sums must be 15\n   \
        \ // Rows\n    if (!((grid[r][c] + grid[r][c+1] + grid[r][c+2] === 15) &&\n\
        \          (grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] === 15) &&\n    \
        \      (grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] === 15))) {\n       \
        \ return false;\n    }\n\n    // Columns\n    if (!((grid[r][c] + grid[r+1][c]\
        \ + grid[r+2][c] === 15) &&\n          (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1]\
        \ === 15) &&\n          (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] ===\
        \ 15))) {\n        return false;\n    }\n\n    // Diagonals\n    if (!((grid[r][c]\
        \ + grid[r+1][c+1] + grid[r+2][c+2] === 15) &&\n          (grid[r][c+2] + grid[r+1][c+1]\
        \ + grid[r+2][c] === 15))) {\n        return false;\n    }\n\n    return true;\n\
        }"
      typescript: "function numMagicSquaresInside(grid: number[][]): number {\n    const\
        \ R = grid.length;\n    const C = grid[0].length;\n\n    if (R < 3 || C < 3)\
        \ {\n        return 0;\n    }\n\n    let count = 0;\n    for (let r = 0; r <=\
        \ R - 3; ++r) {\n        for (let c = 0; c <= C - 3; ++c) {\n            if\
        \ (isMagic(r, c, grid)) {\n                count++;\n            }\n       \
        \ }\n    }\n\n    return count;\n}\n\nfunction isMagic(r: number, c: number,\
        \ grid: number[][]): boolean {\n    // 1. Center must be 5\n    if (grid[r+1][c+1]\
        \ !== 5) {\n        return false;\n    }\n\n    // 2. All numbers must be distinct\
        \ and between 1 and 9\n    const seen: boolean[] = new Array(10).fill(false);\
        \ // Indices 1-9\n    for (let i = 0; i < 3; ++i) {\n        for (let j = 0;\
        \ j < 3; ++j) {\n            const num = grid[r+i][c+j];\n            if (num\
        \ < 1 || num > 9) {\n                return false;\n            }\n        \
        \    if (seen[num]) {\n                return false; // Duplicate\n        \
        \    }\n            seen[num] = true;\n        }\n    }\n\n    // 3. All sums\
        \ must be 15\n    // Rows\n    if (!((grid[r][c] + grid[r][c+1] + grid[r][c+2]\
        \ === 15) &&\n          (grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] ===\
        \ 15) &&\n          (grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] === 15)))\
        \ {\n        return false;\n    }\n\n    // Columns\n    if (!((grid[r][c] +\
        \ grid[r+1][c] + grid[r+2][c] === 15) &&\n          (grid[r][c+1] + grid[r+1][c+1]\
        \ + grid[r+2][c+1] === 15) &&\n          (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2]\
        \ === 15))) {\n        return false;\n    }\n\n    // Diagonals\n    if (!((grid[r][c]\
        \ + grid[r+1][c+1] + grid[r+2][c+2] === 15) &&\n          (grid[r][c+2] + grid[r+1][c+1]\
        \ + grid[r+2][c] === 15))) {\n        return false;\n    }\n\n    return true;\n\
        }"
      php: "<?php\nclass Solution {\n\n    /**\n     * @param Integer[][] $grid\n  \
        \   * @return Integer\n     */\n    function numMagicSquaresInside($grid) {\n\
        \        $R = count($grid);\n        $C = count($grid[0]);\n\n        if ($R\
        \ < 3 || $C < 3) {\n            return 0;\n        }\n\n        $count = 0;\n\
        \        for ($r = 0; $r <= $R - 3; ++$r) {\n            for ($c = 0; $c <=\
        \ $C - 3; ++$c) {\n                if ($this->isMagic($r, $c, $grid)) {\n  \
        \                  $count++;\n                }\n            }\n        }\n\n\
        \        return $count;\n    }\n\n    private function isMagic($r, $c, $grid)\
        \ {\n        // 1. Center must be 5\n        if ($grid[$r+1][$c+1] !== 5) {\n\
        \            return false;\n        }\n\n        // 2. All numbers must be distinct\
        \ and between 1 and 9\n        $seen = array_fill(0, 10, false); // Indices\
        \ 1-9\n        for ($i = 0; $i < 3; ++$i) {\n            for ($j = 0; $j < 3;\
        \ ++$j) {\n                $num = $grid[$r+$i][$c+$j];\n                if ($num\
        \ < 1 || $num > 9) {\n                    return false;\n                }\n\
        \                if ($seen[$num]) {\n                    return false; // Duplicate\n\
        \                }\n                $seen[$num] = true;\n            }\n   \
        \     }\n\n        // 3. All sums must be 15\n        // Rows\n        if (!((($grid[$r][$c]\
        \ + $grid[$r][$c+1] + $grid[$r][$c+2]) === 15) &&\n              (($grid[$r+1][$c]\
        \ + $grid[$r+1][$c+1] + $grid[$r+1][$c+2]) === 15) &&\n              (($grid[$r+2][$c]\
        \ + $grid[$r+2][$c+1] + $grid[$r+2][$c+2]) === 15))) {\n            return false;\n\
        \        }\n\n        // Columns\n        if (!((($grid[$r][$c] + $grid[$r+1][$c]\
        \ + $grid[$r+2][$c]) === 15) &&\n              (($grid[$r][$c+1] + $grid[$r+1][$c+1]\
        \ + $grid[$r+2][$c+1]) === 15) &&\n              (($grid[$r][$c+2] + $grid[$r+1][$c+2]\
        \ + $grid[$r+2][$c+2]) === 15))) {\n            return false;\n        }\n\n\
        \        // Diagonals\n        if (!((($grid[$r][$c] + $grid[$r+1][$c+1] + $grid[$r+2][$c+2])\
        \ === 15) &&\n              (($grid[$r][$c+2] + $grid[$r+1][$c+1] + $grid[$r+2][$c])\
        \ === 15))) {\n            return false;\n        }\n\n        return true;\n\
        \    }\n}\n?>"
      swift: "class Solution {\n    func numMagicSquaresInside(_ grid: [[Int]]) -> Int\
        \ {\n        let R = grid.count\n        let C = grid[0].count\n\n        if\
        \ R < 3 || C < 3 {\n            return 0\n        }\n\n        var count = 0\n\
        \        for r in 0...R - 3 {\n            for c in 0...C - 3 {\n          \
        \      if isMagic(r, c, grid) {\n                    count += 1\n          \
        \      }\n            }\n        }\n\n        return count\n    }\n\n    private\
        \ func isMagic(_ r: Int, _ c: Int, _ grid: [[Int]]) -> Bool {\n        // 1.\
        \ Center must be 5\n        if grid[r+1][c+1] != 5 {\n            return false\n\
        \        }\n\n        // 2. All numbers must be distinct and between 1 and 9\n\
        \        var seen = Array(repeating: false, count: 10) // Indices 1-9\n    \
        \    for i in 0..<3 {\n            for j in 0..<3 {\n                let num\
        \ = grid[r+i][c+j]\n                if num < 1 || num > 9 {\n              \
        \      return false\n                }\n                if seen[num] {\n   \
        \                 return false // Duplicate\n                }\n           \
        \     seen[num] = true\n            }\n        }\n\n        // 3. All sums must\
        \ be 15\n        // Rows\n        if !((grid[r][c] + grid[r][c+1] + grid[r][c+2]\
        \ == 15) &&\n             (grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] ==\
        \ 15) &&\n             (grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15))\
        \ {\n            return false\n        }\n\n        // Columns\n        if !((grid[r][c]\
        \ + grid[r+1][c] + grid[r+2][c] == 15) &&\n             (grid[r][c+1] + grid[r+1][c+1]\
        \ + grid[r+2][c+1] == 15) &&\n             (grid[r][c+2] + grid[r+1][c+2] +\
        \ grid[r+2][c+2] == 15)) {\n            return false\n        }\n\n        //\
        \ Diagonals\n        if !((grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15)\
        \ &&\n             (grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15)) {\n\
        \            return false\n        }\n\n        return true\n    }\n}"
      kotlin: "class Solution {\n    fun numMagicSquaresInside(grid: Array<IntArray>):\
        \ Int {\n        val R = grid.size\n        val C = grid[0].size\n\n       \
        \ if (R < 3 || C < 3) {\n            return 0\n        }\n\n        var count\
        \ = 0\n        for (r in 0..R - 3) {\n            for (c in 0..C - 3) {\n  \
        \              if (isMagic(r, c, grid)) {\n                    count++\n   \
        \             }\n            }\n        }\n\n        return count\n    }\n\n\
        \    private fun isMagic(r: Int, c: Int, grid: Array<IntArray>): Boolean {\n\
        \        // 1. Center must be 5\n        if (grid[r+1][c+1] != 5) {\n      \
        \      return false\n        }\n\n        // 2. All numbers must be distinct\
        \ and between 1 and 9\n        val seen = BooleanArray(10) // Indices 1-9\n\
        \        for (i in 0 until 3) {\n            for (j in 0 until 3) {\n      \
        \          val num = grid[r+i][c+j]\n                if (num < 1 || num > 9)\
        \ {\n                    return false\n                }\n                if\
        \ (seen[num]) {\n                    return false // Duplicate\n           \
        \     }\n                seen[num] = true\n            }\n        }\n\n    \
        \    // 3. All sums must be 15\n        // Rows\n        if (!((grid[r][c] +\
        \ grid[r][c+1] + grid[r][c+2] == 15) &&\n              (grid[r+1][c] + grid[r+1][c+1]\
        \ + grid[r+1][c+2] == 15) &&\n              (grid[r+2][c] + grid[r+2][c+1] +\
        \ grid[r+2][c+2] == 15))) {\n            return false\n        }\n\n       \
        \ // Columns\n        if (!((grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15)\
        \ &&\n              (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15) &&\n\
        \              (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15))) {\n\
        \            return false\n        }\n\n        // Diagonals\n        if (!((grid[r][c]\
        \ + grid[r+1][c+1] + grid[r+2][c+2] == 15) &&\n              (grid[r][c+2] +\
        \ grid[r+1][c+1] + grid[r+2][c] == 15))) {\n            return false\n     \
        \   }\n\n        return true\n    }\n}"
      dart: "class Solution {\n  int numMagicSquaresInside(List<List<int>> grid) {\n\
        \    int R = grid.length;\n    int C = grid[0].length;\n\n    if (R < 3 || C\
        \ < 3) {\n      return 0;\n    }\n\n    int count = 0;\n    for (int r = 0;\
        \ r <= R - 3; ++r) {\n      for (int c = 0; c <= C - 3; ++c) {\n        if (isMagic(r,\
        \ c, grid)) {\n          count++;\n        }\n      }\n    }\n\n    return count;\n\
        \  }\n\n  bool isMagic(int r, int c, List<List<int>> grid) {\n    // 1. Center\
        \ must be 5\n    if (grid[r + 1][c + 1] != 5) {\n      return false;\n    }\n\
        \n    // 2. All numbers must be distinct and between 1 and 9\n    List<bool>\
        \ seen = List.filled(10, false); // Indices 1-9\n    for (int i = 0; i < 3;\
        \ ++i) {\n      for (int j = 0; j < 3; ++j) {\n        int num = grid[r + i][c\
        \ + j];\n        if (num < 1 || num > 9) {\n          return false;\n      \
        \  }\n        if (seen[num]) {\n          return false; // Duplicate\n     \
        \   }\n        seen[num] = true;\n      }\n    }\n\n    // 3. All sums must\
        \ be 15\n    // Rows\n    if (!((grid[r][c] + grid[r][c + 1] + grid[r][c + 2]\
        \ == 15) &&\n        (grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c +\
        \ 2] == 15) &&\n        (grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c\
        \ + 2] == 15))) {\n      return false;\n    }\n\n    // Columns\n    if (!((grid[r][c]\
        \ + grid[r + 1][c] + grid[r + 2][c] == 15) &&\n        (grid[r][c + 1] + grid[r\
        \ + 1][c + 1] + grid[r + 2][c + 1] == 15) &&\n        (grid[r][c + 2] + grid[r\
        \ + 1][c + 2] + grid[r + 2][c + 2] == 15))) {\n      return false;\n    }\n\n\
        \    // Diagonals\n    if (!((grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c\
        \ + 2] == 15) &&\n        (grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c]\
        \ == 15))) {\n      return false;\n    }\n\n    return true;\n  }\n}"
      go: "package main\n\nfunc numMagicSquaresInside(grid [][]int) int {\n    R :=\
        \ len(grid)\n    C := len(grid[0])\n\n    if R < 3 || C < 3 {\n        return\
        \ 0\n    }\n\n    count := 0\n    for r := 0; r <= R - 3; r++ {\n        for\
        \ c := 0; c <= C - 3; c++ {\n            if isMagic(r, c, grid) {\n        \
        \        count++\n            }\n        }\n    }\n\n    return count\n}\n\n\
        func isMagic(r, c int, grid [][]int) bool {\n    // 1. Center must be 5\n  \
        \  if grid[r+1][c+1] != 5 {\n        return false\n    }\n\n    // 2. All numbers\
        \ must be distinct and between 1 and 9\n    seen := make([]bool, 10) // Indices\
        \ 1-9\n    for i := 0; i < 3; i++ {\n        for j := 0; j < 3; j++ {\n    \
        \        num := grid[r+i][c+j]\n            if num < 1 || num > 9 {\n      \
        \          return false\n            }\n            if seen[num] {\n       \
        \         return false // Duplicate\n            }\n            seen[num] =\
        \ true\n        }\n    }\n\n    // 3. All sums must be 15\n    // Rows\n   \
        \ if !((grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15) &&\n         (grid[r+1][c]\
        \ + grid[r+1][c+1] + grid[r+1][c+2] == 15) &&\n         (grid[r+2][c] + grid[r+2][c+1]\
        \ + grid[r+2][c+2] == 15)) {\n        return false\n    }\n\n    // Columns\n\
        \    if !((grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15) &&\n         (grid[r][c+1]\
        \ + grid[r+1][c+1] + grid[r+2][c+1] == 15) &&\n         (grid[r][c+2] + grid[r+1][c+2]\
        \ + grid[r+2][c+2] == 15)) {\n        return false\n    }\n\n    // Diagonals\n\
        \    if !((grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15) &&\n        \
        \ (grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15)) {\n        return false\n\
        \    }\n\n    return true\n}"
      ruby: "# @param {Integer[][]} grid\n# @return {Integer}\ndef num_magic_squares_inside(grid)\n\
        \    r_len = grid.length\n    c_len = grid[0].length\n\n    return 0 if r_len\
        \ < 3 || c_len < 3\n\n    count = 0\n    (0..r_len - 3).each do |r|\n      \
        \  (0..c_len - 3).each do |c|\n            count += 1 if is_magic(r, c, grid)\n\
        \        end\n    end\n\n    count\nend\n\ndef is_magic(r, c, grid)\n    # 1.\
        \ Center must be 5\n    return false if grid[r+1][c+1] != 5\n\n    # 2. All\
        \ numbers must be distinct and between 1 and 9\n    seen = Array.new(10, false)\
        \ # Indices 1-9\n    (0..2).each do |i|\n        (0..2).each do |j|\n      \
        \      num = grid[r+i][c+j]\n            return false if num < 1 || num > 9\n\
        \            return false if seen[num] # Duplicate\n            seen[num] =\
        \ true\n        end\n    end\n\n    # 3. All sums must be 15\n    # Rows\n \
        \   return false unless (grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15 &&\n\
        \                         grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] ==\
        \ 15 &&\n                         grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2]\
        \ == 15)\n\n    # Columns\n    return false unless (grid[r][c] + grid[r+1][c]\
        \ + grid[r+2][c] == 15 &&\n                         grid[r][c+1] + grid[r+1][c+1]\
        \ + grid[r+2][c+1] == 15 &&\n                         grid[r][c+2] + grid[r+1][c+2]\
        \ + grid[r+2][c+2] == 15)\n\n    # Diagonals\n    return false unless (grid[r][c]\
        \ + grid[r+1][c+1] + grid[r+2][c+2] == 15 &&\n                         grid[r][c+2]\
        \ + grid[r+1][c+1] + grid[r+2][c] == 15)\n\n    true\nend"
      scala: "object Solution {\n    def numMagicSquaresInside(grid: Array[Array[Int]]):\
        \ Int = {\n        val R = grid.length\n        val C = grid(0).length\n\n \
        \       if (R < 3 || C < 3) {\n            return 0\n        }\n\n        var\
        \ count = 0\n        for (r <- 0 to R - 3) {\n            for (c <- 0 to C -\
        \ 3) {\n                if (isMagic(r, c, grid)) {\n                    count\
        \ += 1\n                }\n            }\n        }\n\n        count\n    }\n\
        \n    private def isMagic(r: Int, c: Int, grid: Array[Array[Int]]): Boolean\
        \ = {\n        // 1. Center must be 5\n        if (grid(r+1)(c+1) != 5) {\n\
        \            return false\n        }\n\n        // 2. All numbers must be distinct\
        \ and between 1 and 9\n        val seen = Array.fill(10)(false) // Indices 1-9\n\
        \        for (i <- 0 until 3) {\n            for (j <- 0 until 3) {\n      \
        \          val num = grid(r+i)(c+j)\n                if (num < 1 || num > 9)\
        \ {\n                    return false\n                }\n                if\
        \ (seen(num)) {\n                    return false // Duplicate\n           \
        \     }\n                seen(num) = true\n            }\n        }\n\n    \
        \    // 3. All sums must be 15\n        // Rows\n        if (!((grid(r)(c) +\
        \ grid(r)(c+1) + grid(r)(c+2) == 15) &&\n              (grid(r+1)(c) + grid(r+1)(c+1)\
        \ + grid(r+1)(c+2) == 15) &&\n              (grid(r+2)(c) + grid(r+2)(c+1) +\
        \ grid(r+2)(c+2) == 15))) {\n            return false\n        }\n\n       \
        \ // Columns\n        if (!((grid(r)(c) + grid(r+1)(c) + grid(r+2)(c) == 15)\
        \ &&\n              (grid(r)(c+1) + grid(r+1)(c+1) + grid(r+2)(c+1) == 15) &&\n\
        \              (grid(r)(c+2) + grid(r+1)(c+2) + grid(r+2)(c+2) == 15))) {\n\
        \            return false\n        }\n\n        // Diagonals\n        if (!((grid(r)(c)\
        \ + grid(r+1)(c+1) + grid(r+2)(c+2) == 15) &&\n              (grid(r)(c+2) +\
        \ grid(r+1)(c+1) + grid(r+2)(c) == 15))) {\n            return false\n     \
        \   }\n\n        true\n    }\n}"
      rust: "impl Solution {\n    pub fn num_magic_squares_inside(grid: Vec<Vec<i32>>)\
        \ -> i32 {\n        let r_len = grid.len();\n        let c_len = grid[0].len();\n\
        \n        if r_len < 3 || c_len < 3 {\n            return 0;\n        }\n\n\
        \        let mut count = 0;\n        for r in 0..=r_len - 3 {\n            for\
        \ c in 0..=c_len - 3 {\n                if Solution::is_magic(r, c, &grid) {\n\
        \                    count += 1;\n                }\n            }\n       \
        \ }\n\n        count\n    }\n\n    fn is_magic(r: usize, c: usize, grid: &Vec<Vec<i32>>)\
        \ -> bool {\n        // 1. Center must be 5\n        if grid[r+1][c+1] != 5\
        \ {\n            return false;\n        }\n\n        // 2. All numbers must\
        \ be distinct and between 1 and 9\n        let mut seen = [false; 10]; // Indices\
        \ 1-9\n        for i in 0..3 {\n            for j in 0..3 {\n              \
        \  let num = grid[r+i][c+j];\n                if num < 1 || num > 9 {\n    \
        \                return false;\n                }\n                if seen[num\
        \ as usize] {\n                    return false; // Duplicate\n            \
        \    }\n                seen[num as usize] = true;\n            }\n        }\n\
        \n        // 3. All sums must be 15\n        // Rows\n        if !((grid[r][c]\
        \ + grid[r][c+1] + grid[r][c+2] == 15) &&\n             (grid[r+1][c] + grid[r+1][c+1]\
        \ + grid[r+1][c+2] == 15) &&\n             (grid[r+2][c] + grid[r+2][c+1] +\
        \ grid[r+2][c+2] == 15)) {\n            return false;\n        }\n\n       \
        \ // Columns\n        if !((grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15)\
        \ &&\n             (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15) &&\n\
        \             (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15)) {\n  \
        \          return false;\n        }\n\n        // Diagonals\n        if !((grid[r][c]\
        \ + grid[r+1][c+1] + grid[r+2][c+2] == 15) &&\n             (grid[r][c+2] +\
        \ grid[r+1][c+1] + grid[r+2][c] == 15)) {\n            return false;\n     \
        \   }\n\n        true\n    }\n}"
      racket: "#lang racket\n\n(define (num-magic-squares-inside grid)\n  (define R\
        \ (vector-length grid))\n  (define C (vector-length (vector-ref grid 0)))\n\n\
        \  (define (is-magic? r c)\n    (call-with-current-continuation\n     (lambda\
        \ (return)\n       ;; 1. Center must be 5\n       (when (not (= (vector-ref\
        \ (vector-ref grid (+ r 1)) (+ c 1)) 5))\n         (return #f))\n\n       ;;\
        \ 2. All numbers must be distinct and between 1 and 9\n       (define seen (make-vector\
        \ 10 #f))\n       (for* ([i (in-range 3)]\n              [j (in-range 3)])\n\
        \         (define num (vector-ref (vector-ref grid (+ r i)) (+ c j)))\n    \
        \     (when (or (< num 1) (> num 9))\n           (return #f))\n         (when\
        \ (vector-ref seen num)\n           (return #f)) ; Duplicate\n         (vector-set!\
        \ seen num #t))\n\n       ;; 3. All sums must be 15\n       ;; Rows\n      \
        \ (when (not (and (= (+ (vector-ref (vector-ref grid r) c) (vector-ref (vector-ref\
        \ grid r) (+ c 1)) (vector-ref (vector-ref grid r) (+ c 2))) 15)\n         \
        \              (= (+ (vector-ref (vector-ref grid (+ r 1)) c) (vector-ref (vector-ref\
        \ grid (+ r 1)) (+ c 1)) (vector-ref (vector-ref grid (+ r 1)) (+ c 2))) 15)\n\
        \                       (= (+ (vector-ref (vector-ref grid (+ r 2)) c) (vector-ref\
        \ (vector-ref grid (+ r 2)) (+ c 1)) (vector-ref (vector-ref grid (+ r 2)) (+\
        \ c 2))) 15)))\n         (return #f))\n\n       ;; Columns\n       (when (not\
        \ (and (= (+ (vector-ref (vector-ref grid r) c) (vector-ref (vector-ref grid\
        \ (+ r 1)) c) (vector-ref (vector-ref grid (+ r 2)) c)) 15)\n              \
        \         (= (+ (vector-ref (vector-ref grid r) (+ c 1)) (vector-ref (vector-ref\
        \ grid (+ r 1)) (+ c 1)) (vector-ref (vector-ref grid (+ r 2)) (+ c 1))) 15)\n\
        \                       (= (+ (vector-ref (vector-ref grid r) (+ c 2)) (vector-ref\
        \ (vector-ref grid (+ r 1)) (+ c 2)) (vector-ref (vector-ref grid (+ r 2)) (+\
        \ c 2))) 15)))\n         (return #f))\n\n       ;; Diagonals\n       (when (not\
        \ (and (= (+ (vector-ref (vector-ref grid r) c) (vector-ref (vector-ref grid\
        \ (+ r 1)) (+ c 1)) (vector-ref (vector-ref grid (+ r 2)) (+ c 2))) 15)\n  \
        \                     (= (+ (vector-ref (vector-ref grid r) (+ c 2)) (vector-ref\
        \ (vector-ref grid (+ r 1)) (+ c 1)) (vector-ref (vector-ref grid (+ r 2)) c))\
        \ 15)))\n         (return #f))\n\n       #t))) ; All checks passed\n\n  (for*/sum\
        \ ([r (in-range (max 0 (- R 2)))]\n             [c (in-range (max 0 (- C 2)))])\n\
        \    (if (is-magic? r c) 1 0)))"
      erlang: "-module(solution).\n-export([num_magic_squares_inside/1]).\n\nnum_magic_squares_inside(Grid)\
        \ ->\nR = length(Grid),\nC = length(hd(Grid)),\n\ncase {R, C} of\n{R_val, C_val}\
        \ when R_val < 3; C_val < 3 -> 0;\n_ ->\nCount = 0,\nnum_magic_squares_inside_loop(0,\
        \ R - 3, 0, C - 3, Grid, Count)\nend.\n\nnum_magic_squares_inside_loop(R_idx,\
        \ R_max, C_idx, C_max, Grid, Acc) when R_idx > R_max -> Acc;\nnum_magic_squares_inside_loop(R_idx,\
        \ R_max, C_idx, C_max, Grid, Acc) when C_idx > C_max ->\nnum_magic_squares_inside_loop(R_idx\
        \ + 1, R_max, 0, C_max, Grid, Acc);\nnum_magic_squares_inside_loop(R_idx, R_max,\
        \ C_idx, C_max, Grid, Acc) ->\nNewAcc = case is_magic(R_idx, C_idx, Grid) of\n\
        true -> Acc + 1;\nfalse -> Acc\nend,\nnum_magic_squares_inside_loop(R_idx, R_max,\
        \ C_idx + 1, C_max, Grid, NewAcc).\n\nis_magic(R_start, C_start, Grid) ->\n\
        % Helper to get element at (row, col)\n% Lists are 1-indexed in Erlang, so add\
        \ 1 to 0-indexed R_start, C_start\nget_elem = fun(Row, Col, G) ->\nlists:nth(Col\
        \ + 1, lists:nth(Row + 1, G))\nend,\n\n% 1. Center must be 5\nCenter = get_elem(R_start\
        \ + 1, C_start + 1, Grid),\nif Center =/= 5 -> false; true ->\n% 2. All numbers\
        \ must be distinct and between 1 and 9\nNums = [\nget_elem(R_start, C_start),\
        \ get_elem(R_start, C_start + 1), get_elem(R_start, C_start + 2),\nget_elem(R_start\
        \ + 1, C_start), get_elem(R_start + 1, C_start + 1), get_elem(R_start + 1, C_start\
        \ + 2),\nget_elem(R_start + 2, C_start), get_elem(R_start + 2, C_start + 1),\
        \ get_elem(R_start + 2, C_start + 2)\n],\n\n% Check range and distinctness\n\
        CheckNums = fun\n([], _) -> true;\n([H|T], CurrentSeen) when H < 1; H > 9 ->\
        \ false;\n([H|T], CurrentSeen) ->\n    case maps:is_key(H, CurrentSeen) of\n\
        \        true -> false; % Duplicate\n        false -> CheckNums(T, maps:put(H,\
        \ true, CurrentSeen))\n    end\nend,\n\nif CheckNums(Nums, #{}) =:= false ->\
        \ false; true ->\n% 3. All sums must be 15\n% Rows\nRow1Sum = get_elem(R_start,\
        \ C_start) + get_elem(R_start, C_start + 1) + get_elem(R_start, C_start + 2),\n\
        Row2Sum = get_elem(R_start + 1, C_start) + get_elem(R_start + 1, C_start + 1)\
        \ + get_elem(R_start + 1, C_start + 2),\nRow3Sum = get_elem(R_start + 2, C_start)\
        \ + get_elem(R_start + 2, C_start + 1) + get_elem(R_start + 2, C_start + 2),\n\
        \n% Columns\nCol1Sum = get_elem(R_start, C_start) + get_elem(R_start + 1, C_start)\
        \ + get_elem(R_start + 2, C_start),\nCol2Sum = get_elem(R_start, C_start + 1)\
        \ + get_elem(R_start + 1, C_start + 1) + get_elem(R_start + 2, C_start + 1),\n\
        Col3Sum = get_elem(R_start, C_start + 2) + get_elem(R_start + 1, C_start + 2)\
        \ + get_elem(R_start + 2, C_start + 2),\n\n% Diagonals\nDiag1Sum = get_elem(R_start,\
        \ C_start) + get_elem(R_start + 1, C_start + 1) + get_elem(R_start + 2, C_start\
        \ + 2),\nDiag2Sum = get_elem(R_start, C_start + 2) + get_elem(R_start + 1, C_start\
        \ + 1) + get_elem(R_start + 2, C_start),\n\nif Row1Sum =:= 15, Row2Sum =:= 15,\
        \ Row3Sum =:= 15,\n   Col1Sum =:= 15, Col2Sum =:= 15, Col3Sum =:= 15,\n   Diag1Sum\
        \ =:= 15, Diag2Sum =:= 15 -> true;\n   true -> false\nend\nend\nend."
      elixir: "defmodule Solution do\n  @spec num_magic_squares_inside(grid :: [[integer]])\
        \ :: integer\n  def num_magic_squares_inside(grid) do\n    r = length(grid)\n\
        \    c = length(hd(grid))\n\n    if r < 3 || c < 3 do\n      0\n    else\n \
        \     0..(r - 3)\n      |> Enum.reduce(0, fn r_idx, acc ->\n        0..(c -\
        \ 3)\n        |> Enum.reduce(acc, fn c_idx, inner_acc ->\n          if is_magic(r_idx,\
        \ c_idx, grid) do\n            inner_acc + 1\n          else\n            inner_acc\n\
        \          end\n        end)\n      end)\n    end\n  end\n\n  defp is_magic(r_start,\
        \ c_start, grid) do\n    # Helper to get element at (row, col)\n    # Lists\
        \ are 0-indexed in Elixir\n    get_elem = fn row, col ->\n      Enum.at(Enum.at(grid,\
        \ row), col)\n    end\n\n    # 1. Center must be 5\n    center = get_elem.(r_start\
        \ + 1, c_start + 1)\n    if center != 5, do: (\n      false\n    ) else (\n\
        \      # 2. All numbers must be distinct and between 1 and 9\n      nums = [\n\
        \        get_elem.(r_start, c_start), get_elem.(r_start, c_start + 1), get_elem.(r_start,\
        \ c_start + 2),\n        get_elem.(r_start + 1, c_start), get_elem.(r_start\
        \ + 1, c_start + 1), get_elem.(r_start + 1, c_start + 2),\n        get_elem.(r_start\
        \ + 2, c_start), get_elem.(r_start + 2, c_start + 1), get_elem.(r_start + 2,\
        \ c_start + 2)\n      ]\n\n      # Check range and distinctness\n      seen\
        \ = MapSet.new()\n      check_nums = fn\n        [], _ -> true\n        [h |\
        \ t], current_seen when h < 1 or h > 9 -> false\n        [h | t], current_seen\
        \ ->\n          if MapSet.member?(current_seen, h) do\n            false # Duplicate\n\
        \          else\n            check_nums.(t, MapSet.put(current_seen, h))\n \
        \         end\n      end\n\n      if not check_nums.(nums, seen), do: (\n  \
        \      false\n      ) else (\n        # 3. All sums must be 15\n        # Rows\n\
        \        row1_sum = get_elem.(r_start, c_start) + get_elem.(r_start, c_start\
        \ + 1) + get_elem.(r_start, c_start + 2)\n        row2_sum = get_elem.(r_start\
        \ + 1, c_start) + get_elem.(r_start + 1, c_start + 1) + get_elem.(r_start +\
        \ 1, c_start + 2)\n        row3_sum = get_elem.(r_start + 2, c_start) + get_elem.(r_start\
        \ + 2, c_start + 1) + get_elem.(r_start + 2, c_start + 2)\n\n        # Columns\n\
        \        col1_sum = get_elem.(r_start, c_start) + get_elem.(r_start + 1, c_start)\
        \ + get_elem.(r_start + 2, c_start)\n        col2_sum = get_elem.(r_start, c_start\
        \ + 1) + get_elem.(r_start + 1, c_start + 1) + get_elem.(r_start + 2, c_start\
        \ + 1)\n        col3_sum = get_elem.(r_start, c_start + 2) + get_elem.(r_start\
        \ + 1, c_start + 2) + get_elem.(r_start + 2, c_start + 2)\n\n        # Diagonals\n\
        \        diag1_sum = get_elem.(r_start, c_start) + get_elem.(r_start + 1, c_start\
        \ + 1) + get_elem.(r_start + 2, c_start + 2)\n        diag2_sum = get_elem.(r_start,\
        \ c_start + 2) + get_elem.(r_start + 1, c_start + 1) + get_elem.(r_start + 2,\
        \ c_start)\n\n        if row1_sum == 15 && row2_sum == 15 && row3_sum == 15\
        \ &&\n           col1_sum == 15 && col2_sum == 15 && col3_sum == 15 &&\n   \
        \        diag1_sum == 15 && diag2_sum == 15 do\n          true\n        else\n\
        \          false\n        end\n      )\n    )\n  end\nend"
    approach: 'The problem asks us to count the number of 3x3 magic square subgrids
      within a given larger grid. A 3x3 magic square is defined by three key properties:
      it must contain distinct numbers from 1 to 9, and all its rows, columns, and both
      main diagonals must sum to the same value. For a 3x3 grid containing distinct
      numbers from 1 to 9, the sum of all numbers is 1+2+...+9 = 45. Since there are
      three rows (or columns), each row, column, and diagonal must sum to 45 / 3 = 15.
      Additionally, a known property of such magic squares is that the center element
      must always be 5.'
    time_complexity: 'The time complexity is O(R * C), where R is the number of rows
      and C is the number of columns in the input grid. We iterate through all possible
      top-left corners of 3x3 subgrids. There are (R-2) * (C-2) such corners. For each
      potential subgrid, the `isMagic` helper function performs a constant number of
      operations: checking the center element, iterating through 9 numbers to verify
      range (1-9) and distinctness using a fixed-size boolean array, and performing
      8 fixed-sum checks. Since R and C are constrained to be at most 10, the total
      number of subgrids is at most 8 * 8 = 64, making the overall operation count very
      small and effectively constant.'
    space_complexity: The space complexity is O(1). The `isMagic` helper function uses
      a boolean array of size 10 (to track numbers 0-9) to check for distinctness and
      range. This array's size is constant and does not depend on the dimensions of
      the input grid.
    elapsed_time: 142.51752257347107
    model: gemini-2.5-flash
    generated_at: '2025-12-30 01:10:00 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int numMagicSquaresInside(vector<vector<int>>&\
        \ grid) {\n        int count = 0;\n        int row = grid.size();\n        int\
        \ col = grid[0].size();\n        for (int i = 0; i < row - 2; i++) {\n     \
        \       for (int j = 0; j < col - 2; j++) {\n                if (isMagic(grid,\
        \ i, j)) {\n                    count++;\n                }\n            }\n\
        \        }\n        return count;\n    }\n\n    bool isMagic(vector<vector<int>>&\
        \ grid, int i, int j) {\n        vector<int> nums;\n        for (int x = i;\
        \ x < i + 3; x++) {\n            for (int y = j; y < j + 3; y++) {\n       \
        \         nums.push_back(grid[x][y]);\n            }\n        }\n        sort(nums.begin(),\
        \ nums.end());\n        if (nums != vector<int>{1, 2, 3, 4, 5, 6, 7, 8, 9})\
        \ {\n            return false;\n        }\n        int sum = grid[i][j] + grid[i][j\
        \ + 1] + grid[i][j + 2];\n        for (int x = i; x < i + 3; x++) {\n      \
        \      if (grid[x][j] + grid[x][j + 1] + grid[x][j + 2] != sum) {\n        \
        \        return false;\n            }\n        }\n        for (int y = j; y\
        \ < j + 3; y++) {\n            if (grid[i][y] + grid[i + 1][y] + grid[i + 2][y]\
        \ != sum) {\n                return false;\n            }\n        }\n     \
        \   if (grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != sum) {\n   \
        \         return false;\n        }\n        if (grid[i][j + 2] + grid[i + 1][j\
        \ + 1] + grid[i + 2][j] != sum) {\n            return false;\n        }\n  \
        \      return true;\n    }\n};"
      java: "class Solution {\n    public int numMagicSquaresInside(int[][] grid) {\n\
        \        int count = 0;\n        int row = grid.length;\n        int col = grid[0].length;\n\
        \        for (int i = 0; i < row - 2; i++) {\n            for (int j = 0; j\
        \ < col - 2; j++) {\n                if (isMagic(grid, i, j)) {\n          \
        \          count++;\n                }\n            }\n        }\n        return\
        \ count;\n    }\n\n    public boolean isMagic(int[][] grid, int i, int j) {\n\
        \        int[] nums = new int[9];\n        int index = 0;\n        for (int\
        \ x = i; x < i + 3; x++) {\n            for (int y = j; y < j + 3; y++) {\n\
        \                nums[index++] = grid[x][y];\n            }\n        }\n   \
        \     Arrays.sort(nums);\n        for (int k = 0; k < 9; k++) {\n          \
        \  if (nums[k] != k + 1) {\n                return false;\n            }\n \
        \       }\n        int sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2];\n\
        \        for (int x = i; x < i + 3; x++) {\n            if (grid[x][j] + grid[x][j\
        \ + 1] + grid[x][j + 2] != sum) {\n                return false;\n         \
        \   }\n        }\n        for (int y = j; y < j + 3; y++) {\n            if\
        \ (grid[i][y] + grid[i + 1][y] + grid[i + 2][y] != sum) {\n                return\
        \ false;\n            }\n        }\n        if (grid[i][j] + grid[i + 1][j +\
        \ 1] + grid[i + 2][j + 2] != sum) {\n            return false;\n        }\n\
        \        if (grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != sum) {\n\
        \            return false;\n        }\n        return true;\n    }\n}"
      python: "class Solution:\n    def numMagicSquaresInside(self, grid: list[list[int]])\
        \ -> int:\n        count = 0\n        row = len(grid)\n        col = len(grid[0])\n\
        \        for i in range(row - 2):\n            for j in range(col - 2):\n  \
        \              if self.isMagic(grid, i, j):\n                    count += 1\n\
        \        return count\n\n    def isMagic(self, grid: list[list[int]], i: int,\
        \ j: int) -> bool:\n        nums = [grid[x][y] for x in range(i, i + 3) for\
        \ y in range(j, j + 3)]\n        if sorted(nums) != list(range(1, 10)):\n  \
        \          return False\n        sum_ = grid[i][j] + grid[i][j + 1] + grid[i][j\
        \ + 2]\n        for x in range(i, i + 3):\n            if grid[x][j] + grid[x][j\
        \ + 1] + grid[x][j + 2] != sum_:\n                return False\n        for\
        \ y in range(j, j + 3):\n            if grid[i][y] + grid[i + 1][y] + grid[i\
        \ + 2][y] != sum_:\n                return False\n        if grid[i][j] + grid[i\
        \ + 1][j + 1] + grid[i + 2][j + 2] != sum_:\n            return False\n    \
        \    if grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != sum_:\n    \
        \        return False\n        return True"
      python3: "class Solution:\n    def numMagicSquaresInside(self, grid: list[list[int]])\
        \ -> int:\n        count = 0\n        row = len(grid)\n        col = len(grid[0])\n\
        \        for i in range(row - 2):\n            for j in range(col - 2):\n  \
        \              if self.isMagic(grid, i, j):\n                    count += 1\n\
        \        return count\n\n    def isMagic(self, grid: list[list[int]], i: int,\
        \ j: int) -> bool:\n        nums = [grid[x][y] for x in range(i, i + 3) for\
        \ y in range(j, j + 3)]\n        if sorted(nums) != list(range(1, 10)):\n  \
        \          return False\n        sum_ = grid[i][j] + grid[i][j + 1] + grid[i][j\
        \ + 2]\n        for x in range(i, i + 3):\n            if grid[x][j] + grid[x][j\
        \ + 1] + grid[x][j + 2] != sum_:\n                return False\n        for\
        \ y in range(j, j + 3):\n            if grid[i][y] + grid[i + 1][y] + grid[i\
        \ + 2][y] != sum_:\n                return False\n        if grid[i][j] + grid[i\
        \ + 1][j + 1] + grid[i + 2][j + 2] != sum_:\n            return False\n    \
        \    if grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != sum_:\n    \
        \        return False\n        return True"
      c: "typedef struct {\n    int** grid;\n    int gridSize;\n    int* gridColSize;\n\
        } Solution;\n\nint numMagicSquaresInside(int** grid, int gridSize, int* gridColSize)\
        \ {\n    int count = 0;\n    for (int i = 0; i < gridSize - 2; i++) {\n    \
        \    for (int j = 0; j < gridColSize[i] - 2; j++) {\n            if (isMagic(grid,\
        \ i, j, gridSize, gridColSize)) {\n                count++;\n            }\n\
        \        }\n    }\n    return count;\n}\n\nint isMagic(int** grid, int i, int\
        \ j, int gridSize, int* gridColSize) {\n    int nums[9];\n    int index = 0;\n\
        \    for (int x = i; x < i + 3; x++) {\n        for (int y = j; y < j + 3; y++)\
        \ {\n            nums[index++] = grid[x][y];\n        }\n    }\n    int temp;\n\
        \    for (int k = 0; k < 9; k++) {\n        for (int l = k + 1; l < 9; l++)\
        \ {\n            if (nums[k] > nums[l]) {\n                temp = nums[k];\n\
        \                nums[k] = nums[l];\n                nums[l] = temp;\n     \
        \       }\n        }\n    }\n    for (int k = 0; k < 9; k++) {\n        if (nums[k]\
        \ != k + 1) {\n            return 0;\n        }\n    }\n    int sum = grid[i][j]\
        \ + grid[i][j + 1] + grid[i][j + 2];\n    for (int x = i; x < i + 3; x++) {\n\
        \        if (grid[x][j] + grid[x][j + 1] + grid[x][j + 2] != sum) {\n      \
        \      return 0;\n        }\n    }\n    for (int y = j; y < j + 3; y++) {\n\
        \        if (grid[i][y] + grid[i + 1][y] + grid[i + 2][y] != sum) {\n      \
        \      return 0;\n        }\n    }\n    if (grid[i][j] + grid[i + 1][j + 1]\
        \ + grid[i + 2][j + 2] != sum) {\n        return 0;\n    }\n    if (grid[i][j\
        \ + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != sum) {\n        return 0;\n\
        \    }\n    return 1;\n}"
      csharp: "public class Solution {\n    public int NumMagicSquaresInside(int[][]\
        \ grid) {\n        int count = 0;\n        int row = grid.Length;\n        int\
        \ col = grid[0].Length;\n        for (int i = 0; i < row - 2; i++) {\n     \
        \       for (int j = 0; j < col - 2; j++) {\n                if (IsMagic(grid,\
        \ i, j)) {\n                    count++;\n                }\n            }\n\
        \        }\n        return count;\n    }\n\n    public bool IsMagic(int[][]\
        \ grid, int i, int j) {\n        int[] nums = new int[9];\n        int index\
        \ = 0;\n        for (int x = i; x < i + 3; x++) {\n            for (int y =\
        \ j; y < j + 3; y++) {\n                nums[index++] = grid[x][y];\n      \
        \      }\n        }\n        Array.Sort(nums);\n        for (int k = 0; k <\
        \ 9; k++) {\n            if (nums[k] != k + 1) {\n                return false;\n\
        \            }\n        }\n        int sum = grid[i][j] + grid[i][j + 1] + grid[i][j\
        \ + 2];\n        for (int x = i; x < i + 3; x++) {\n            if (grid[x][j]\
        \ + grid[x][j + 1] + grid[x][j + 2] != sum) {\n                return false;\n\
        \            }\n        }\n        for (int y = j; y < j + 3; y++) {\n     \
        \       if (grid[i][y] + grid[i + 1][y] + grid[i + 2][y] != sum) {\n       \
        \         return false;\n            }\n        }\n        if (grid[i][j] +\
        \ grid[i + 1][j + 1] + grid[i + 2][j + 2] != sum) {\n            return false;\n\
        \        }\n        if (grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]\
        \ != sum) {\n            return false;\n        }\n        return true;\n  \
        \  }\n}"
      javascript: "var numMagicSquaresInside = function(grid) {\n    let count = 0;\n\
        \    let row = grid.length;\n    let col = grid[0].length;\n    for (let i =\
        \ 0; i < row - 2; i++) {\n        for (let j = 0; j < col - 2; j++) {\n    \
        \        if (isMagic(grid, i, j)) {\n                count++;\n            }\n\
        \        }\n    }\n    return count;\n};\n\nvar isMagic = function(grid, i,\
        \ j) {\n    let nums = [];\n    for (let x = i; x < i + 3; x++) {\n        for\
        \ (let y = j; y < j + 3; y++) {\n            nums.push(grid[x][y]);\n      \
        \  }\n    }\n    nums.sort((a, b) => a - b);\n    for (let k = 0; k < 9; k++)\
        \ {\n        if (nums[k] !== k + 1) {\n            return false;\n        }\n\
        \    }\n    let sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2];\n    for\
        \ (let x = i; x < i + 3; x++) {\n        if (grid[x][j] + grid[x][j + 1] + grid[x][j\
        \ + 2] !== sum) {\n            return false;\n        }\n    }\n    for (let\
        \ y = j; y < j + 3; y++) {\n        if (grid[i][y] + grid[i + 1][y] + grid[i\
        \ + 2][y] !== sum) {\n            return false;\n        }\n    }\n    if (grid[i][j]\
        \ + grid[i + 1][j + 1] + grid[i + 2][j + 2] !== sum) {\n        return false;\n\
        \    }\n    if (grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] !== sum)\
        \ {\n        return false;\n    }\n    return true;\n};"
      typescript: "function numMagicSquaresInside(grid: number[][]): number {\n    let\
        \ count: number = 0;\n    let row: number = grid.length;\n    let col: number\
        \ = grid[0].length;\n    for (let i: number = 0; i < row - 2; i++) {\n     \
        \   for (let j: number = 0; j < col - 2; j++) {\n            if (isMagic(grid,\
        \ i, j)) {\n                count++;\n            }\n        }\n    }\n    return\
        \ count;\n}\n\nfunction isMagic(grid: number[][], i: number, j: number): boolean\
        \ {\n    let nums: number[] = [];\n    for (let x: number = i; x < i + 3; x++)\
        \ {\n        for (let y: number = j; y < j + 3; y++) {\n            nums.push(grid[x][y]);\n\
        \        }\n    }\n    nums.sort((a, b) => a - b);\n    for (let k: number =\
        \ 0; k < 9; k++) {\n        if (nums[k] !== k + 1) {\n            return false;\n\
        \        }\n    }\n    let sum: number = grid[i][j] + grid[i][j + 1] + grid[i][j\
        \ + 2];\n    for (let x: number = i; x < i + 3; x++) {\n        if (grid[x][j]\
        \ + grid[x][j + 1] + grid[x][j + 2] !== sum) {\n            return false;\n\
        \        }\n    }\n    for (let y: number = j; y < j + 3; y++) {\n        if\
        \ (grid[i][y] + grid[i + 1][y] + grid[i + 2][y] !== sum) {\n            return\
        \ false;\n        }\n    }\n    if (grid[i][j] + grid[i + 1][j + 1] + grid[i\
        \ + 2][j + 2] !== sum) {\n        return false;\n    }\n    if (grid[i][j +\
        \ 2] + grid[i + 1][j + 1] + grid[i + 2][j] !== sum) {\n        return false;\n\
        \    }\n    return true;\n}"
      php: "class Solution {\n    function numMagicSquaresInside($grid) {\n        $count\
        \ = 0;\n        $row = count($grid);\n        $col = count($grid[0]);\n    \
        \    for ($i = 0; $i < $row - 2; $i++) {\n            for ($j = 0; $j < $col\
        \ - 2; $j++) {\n                if ($this->isMagic($grid, $i, $j)) {\n     \
        \               $count++;\n                }\n            }\n        }\n   \
        \     return $count;\n    }\n\n    function isMagic($grid, $i, $j) {\n     \
        \   $nums = array();\n        for ($x = $i; $x < $i + 3; $x++) {\n         \
        \   for ($y = $j; $y < $j + 3; $y++) {\n                $nums[] = $grid[$x][$y];\n\
        \            }\n        }\n        sort($nums);\n        for ($k = 0; $k < 9;\
        \ $k++) {\n            if ($nums[$k] != $k + 1) {\n                return false;\n\
        \            }\n        }\n        $sum = $grid[$i][$j] + $grid[$i][$j + 1]\
        \ + $grid[$i][$j + 2];\n        for ($x = $i; $x < $i + 3; $x++) {\n       \
        \     if ($grid[$x][$j] + $grid[$x][$j + 1] + $grid[$x][$j + 2] != $sum) {\n\
        \                return false;\n            }\n        }\n        for ($y =\
        \ $j; $y < $j + 3; $y++) {\n            if ($grid[$i][$y] + $grid[$i + 1][$y]\
        \ + $grid[$i + 2][$y] != $sum) {\n                return false;\n          \
        \  }\n        }\n        if ($grid[$i][$j] + $grid[$i + 1][$j + 1] + $grid[$i\
        \ + 2][$j + 2] != $sum) {\n            return false;\n        }\n        if\
        \ ($grid[$i][$j + 2] + $grid[$i + 1][$j + 1] + $grid[$i + 2][$j] != $sum) {\n\
        \            return false;\n        }\n        return true;\n    }\n}"
      swift: "class Solution {\n    func numMagicSquaresInside(_ grid: [[Int]]) -> Int\
        \ {\n        var count = 0\n        let row = grid.count\n        let col =\
        \ grid[0].count\n        for i in 0..<row-2 {\n            for j in 0..<col-2\
        \ {\n                if isMagic(grid, i, j) {\n                    count +=\
        \ 1\n                }\n            }\n        }\n        return count\n   \
        \ }\n\n    func isMagic(_ grid: [[Int]], _ i: Int, _ j: Int) -> Bool {\n   \
        \     var nums: [Int] = []\n        for x in i...i+2 {\n            for y in\
        \ j...j+2 {\n                nums.append(grid[x][y])\n            }\n      \
        \  }\n        nums.sort()\n        for k in 0...8 {\n            if nums[k]\
        \ != k + 1 {\n                return false\n            }\n        }\n     \
        \   let sum = grid[i][j] + grid[i][j+1] + grid[i][j+2]\n        for x in i...i+2\
        \ {\n            if grid[x][j] + grid[x][j+1] + grid[x][j+2] != sum {\n    \
        \            return false\n            }\n        }\n        for y in j...j+2\
        \ {\n            if grid[i][y] + grid[i+1][y] + grid[i+2][y] != sum {\n    \
        \            return false\n            }\n        }\n        if grid[i][j] +\
        \ grid[i+1][j+1] + grid[i+2][j+2] != sum {\n            return false\n     \
        \   }\n        if grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] != sum {\n  \
        \          return false\n        }\n        return true\n    }\n}"
      kotlin: "class Solution {\n    fun numMagicSquaresInside(grid: Array<IntArray>):\
        \ Int {\n        var count = 0\n        val row = grid.size\n        val col\
        \ = grid[0].size\n        for (i in 0 until row - 2) {\n            for (j in\
        \ 0 until col - 2) {\n                if (isMagic(grid, i, j)) {\n         \
        \           count++\n                }\n            }\n        }\n        return\
        \ count\n    }\n\n    fun isMagic(grid: Array<IntArray>, i: Int, j: Int): Boolean\
        \ {\n        val nums = mutableListOf<Int>()\n        for (x in i until i +\
        \ 3) {\n            for (y in j until j + 3) {\n                nums.add(grid[x][y])\n\
        \            }\n        }\n        nums.sort()\n        for (k in 0 until 9)\
        \ {\n            if (nums[k] != k + 1) {\n                return false\n   \
        \         }\n        }\n        val sum = grid[i][j] + grid[i][j + 1] + grid[i][j\
        \ + 2]\n        for (x in i until i + 3) {\n            if (grid[x][j] + grid[x][j\
        \ + 1] + grid[x][j + 2] != sum) {\n                return false\n          \
        \  }\n        }\n        for (y in j until j + 3) {\n            if (grid[i][y]\
        \ + grid[i + 1][y] + grid[i + 2][y] != sum) {\n                return false\n\
        \            }\n        }\n        if (grid[i][j] + grid[i + 1][j + 1] + grid[i\
        \ + 2][j + 2] != sum) {\n            return false\n        }\n        if (grid[i][j\
        \ + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != sum) {\n            return false\n\
        \        }\n        return true\n    }\n}"
      dart: "class Solution {\n    int numMagicSquaresInside(List<List<int>> grid) {\n\
        \        int count = 0;\n        int row = grid.length;\n        int col = grid[0].length;\n\
        \        for (int i = 0; i < row - 2; i++) {\n            for (int j = 0; j\
        \ < col - 2; j++) {\n                if (isMagic(grid, i, j)) {\n          \
        \          count++;\n                }\n            }\n        }\n        return\
        \ count;\n    }\n\n    bool isMagic(List<List<int>> grid, int i, int j) {\n\
        \        List<int> nums = [];\n        for (int x = i; x < i + 3; x++) {\n \
        \           for (int y = j; y < j + 3; y++) {\n                nums.add(grid[x][y]);\n\
        \            }\n        }\n        nums.sort();\n        for (int k = 0; k <\
        \ 9; k++) {\n            if (nums[k] != k + 1) {\n                return false;\n\
        \            }\n        }\n        int sum = grid[i][j] + grid[i][j + 1] + grid[i][j\
        \ + 2];\n        for (int x = i; x < i + 3; x++) {\n            if (grid[x][j]\
        \ + grid[x][j + 1] + grid[x][j + 2] != sum) {\n                return false;\n\
        \            }\n        }\n        for (int y = j; y < j + 3; y++) {\n     \
        \       if (grid[i][y] + grid[i + 1][y] + grid[i + 2][y] != sum) {\n       \
        \         return false;\n            }\n        }\n        if (grid[i][j] +\
        \ grid[i + 1][j + 1] + grid[i + 2][j + 2] != sum) {\n            return false;\n\
        \        }\n        if (grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]\
        \ != sum) {\n            return false;\n        }\n        return true;\n  \
        \  }\n}"
      go: "package main\n\nimport (\n    \"fmt\"\n    \"sort\"\n)\n\ntype Solution struct{}\n\
        \nfunc (s *Solution) numMagicSquaresInside(grid [][]int) int {\n    count :=\
        \ 0\n    row := len(grid)\n    col := len(grid[0])\n    for i := 0; i < row-2;\
        \ i++ {\n        for j := 0; j < col-2; j++ {\n            if s.isMagic(grid,\
        \ i, j) {\n                count++\n            }\n        }\n    }\n    return\
        \ count\n}\n\nfunc (s *Solution) isMagic(grid [][]int, i, j int) bool {\n  \
        \  nums := make([]int, 0)\n    for x := i; x < i+3; x++ {\n        for y :=\
        \ j; y < j+3; y++ {\n            nums = append(nums, grid[x][y])\n        }\n\
        \    }\n    sort.Ints(nums)\n    for k := 0; k < 9; k++ {\n        if nums[k]\
        \ != k+1 {\n            return false\n        }\n    }\n    sum := grid[i][j]\
        \ + grid[i][j+1] + grid[i][j+2]\n    for x := i; x < i+3; x++ {\n        if\
        \ grid[x][j]+grid[x][j+1]+grid[x][j+2] != sum {\n            return false\n\
        \        }\n    }\n    for y := j; y < j+3; y++ {\n        if grid[i][y]+grid[i+1][y]+grid[i+2][y]\
        \ != sum {\n            return false\n        }\n    }\n    if grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]\
        \ != sum {\n        return false\n    }\n    if grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]\
        \ != sum {\n        return false\n    }\n    return true\n}"
      ruby: "class Solution\n    def num_magic_squares_inside(grid)\n        count =\
        \ 0\n        row = grid.size\n        col = grid[0].size\n        (0...row-2).each\
        \ do |i|\n            (0...col-2).each do |j|\n                if is_magic(grid,\
        \ i, j)\n                    count += 1\n                end\n            end\n\
        \        end\n        count\n    end\n\n    def is_magic(grid, i, j)\n     \
        \   nums = []\n        (i...i+3).each do |x|\n            (j...j+3).each do\
        \ |y|\n                nums << grid[x][y]\n            end\n        end\n  \
        \      nums.sort!\n        (0...9).each do |k|\n            return false if\
        \ nums[k] != k + 1\n        end\n        sum = grid[i][j] + grid[i][j+1] + grid[i][j+2]\n\
        \        (i...i+3).each do |x|\n            return false if grid[x][j] + grid[x][j+1]\
        \ + grid[x][j+2] != sum\n        end\n        (j...j+3).each do |y|\n      \
        \      return false if grid[i][y] + grid[i+1][y] + grid[i+2][y] != sum\n   \
        \     end\n        return false if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]\
        \ != sum\n        return false if grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]\
        \ != sum\n        true\n    end\nend"
      scala: "object Solution {\n    def numMagicSquaresInside(grid: Array[Array[Int]]):\
        \ Int = {\n        var count = 0\n        val row = grid.length\n        val\
        \ col = grid(0).length\n        for (i <- 0 until row - 2) {\n            for\
        \ (j <- 0 until col - 2) {\n                if (isMagic(grid, i, j)) {\n   \
        \                 count += 1\n                }\n            }\n        }\n\
        \        count\n    }\n\n    def isMagic(grid: Array[Array[Int]], i: Int, j:\
        \ Int): Boolean = {\n        val nums = for (x <- i until i + 3; y <- j until\
        \ j + 3) yield grid(x)(y)\n        val sortedNums = nums.sorted\n        if\
        \ (!sortedNums.sameElements((1 to 9).toList)) {\n            return false\n\
        \        }\n        val sum = grid(i)(j) + grid(i)(j + 1) + grid(i)(j + 2)\n\
        \        for (x <- i until i + 3) {\n            if (grid(x)(j) + grid(x)(j\
        \ + 1) + grid(x)(j + 2) != sum) {\n                return false\n          \
        \  }\n        }\n        for (y <- j until j + 3) {\n            if (grid(i)(y)\
        \ + grid(i + 1)(y) + grid(i + 2)(y) != sum) {\n                return false\n\
        \            }\n        }\n        if (grid(i)(j) + grid(i + 1)(j + 1) + grid(i\
        \ + 2)(j + 2) != sum) {\n            return false\n        }\n        if (grid(i)(j\
        \ + 2) + grid(i + 1)(j + 1) + grid(i + 2)(j) != sum) {\n            return false\n\
        \        }\n        true\n    }\n}"
      rust: "struct Solution;\n\nimpl Solution {\n    pub fn num_magic_squares_inside(grid:\
        \ Vec<Vec<i32>>) -> i32 {\n        let mut count = 0;\n        let row = grid.len();\n\
        \        let col = grid[0].len();\n        for i in 0..row - 2 {\n         \
        \   for j in 0..col - 2 {\n                if Solution::is_magic(&grid, i, j)\
        \ {\n                    count += 1;\n                }\n            }\n   \
        \     }\n        count\n    }\n\n    pub fn is_magic(grid: &Vec<Vec<i32>>, i:\
        \ usize, j: usize) -> bool {\n        let mut nums: Vec<i32> = Vec::new();\n\
        \        for x in i..i + 3 {\n            for y in j..j + 3 {\n            \
        \    nums.push(grid[x][y]);\n            }\n        }\n        nums.sort_unstable();\n\
        \        for k in 0..9 {\n            if nums[k as usize] != (k + 1) as i32\
        \ {\n                return false;\n            }\n        }\n        let sum\
        \ = grid[i][j] + grid[i][j + 1] + grid[i][j + 2];\n        for x in i..i + 3\
        \ {\n            if grid[x][j] + grid[x][j + 1] + grid[x][j + 2] != sum {\n\
        \                return false;\n            }\n        }\n        for y in j..j\
        \ + 3 {\n            if grid[i][y] + grid[i + 1][y] + grid[i + 2][y] != sum\
        \ {\n                return false;\n            }\n        }\n        if grid[i][j]\
        \ + grid[i + 1][j + 1] + grid[i + 2][j + 2] != sum {\n            return false;\n\
        \        }\n        if grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]\
        \ != sum {\n            return false;\n        }\n        true\n    }\n}"
      racket: "(define (num-magic-squares-inside grid)\n    (let ((count 0)\n      \
        \    (row (length grid))\n          (col (length (car grid))))\n        (for\
        \ ((i (range 0 (- row 2))))\n            (for ((j (range 0 (- col 2))))\n  \
        \              (when (is-magic grid i j)\n                    (set! count (+\
        \ count 1)))))\n        count)\n\n(define (is-magic grid i j)\n    (let ((nums\
        \ (for*/list ((x (range i (+ i 3)))\n                             (y (range\
        \ j (+ j 3))))\n                        (list-ref (list-ref grid x) y))))\n\
        \        (and (= (sort nums) (range 1 10))\n             (= (apply + (take nums\
        \ 3))\n                (apply + (take (drop nums 3) 3))\n                (apply\
        \ + (take (drop nums 6) 3))\n                (apply + (list-ref nums 0)\n  \
        \                            (list-ref nums 4)\n                           \
        \   (list-ref nums 8))\n                (apply + (list-ref nums 2)\n       \
        \                       (list-ref nums 4)\n                              (list-ref\
        \ nums 6))))))"
      erlang: "num_magic_squares_inside(Grid) ->\n    length([1 || I <- lists:seq(0,\
        \ length(Grid) - 3),\n                   J <- lists:seq(0, length(hd(Grid))\
        \ - 3),\n                   is_magic(Grid, I, J)]).\n\nis_magic(Grid, I, J)\
        \ ->\n    lists:sort([element(X, Y, Grid) || X <- lists:seq(I, I + 2),\n   \
        \                                     Y <- lists:seq(J, J + 2)]) = lists:seq(1,\
        \ 9)\n    andalso\n    lists:foldl(fun({X, Y}, Sum) -> element(X, Y, Grid) +\
        \ Sum end, 0,\n                [{I, J}, {I, J + 1}, {I, J + 2}]) =\n    lists:foldl(fun({X,\
        \ Y}, Sum) -> element(X, Y, Grid) + Sum end, 0,\n                [{I + 1, J},\
        \ {I + 1, J + 1}, {I + 1, J + 2}])\n    andalso\n    lists:foldl(fun({X, Y},\
        \ Sum) -> element(X, Y, Grid) + Sum end, 0,\n                [{I + 2, J}, {I\
        \ + 2, J + 1}, {I + 2, J + 2}])\n    andalso\n    element(I, J, Grid) + element(I\
        \ + 1, J + 1, Grid) + element(I + 2, J + 2, Grid) =\n    element(I, J + 2, Grid)\
        \ + element(I + 1, J + 1, Grid) + element(I + 2, J, Grid).\n\nelement(X, Y,\
        \ Grid) ->\n    element(Y + 1, lists:nth(X + 1, Grid))."
      elixir: "defmodule Solution do\n    def num_magic_squares_inside(grid) do\n  \
        \      count = 0\n        row = length(grid)\n        col = length(Enum.at(grid,\
        \ 0))\n        for i <- 0..row-3 do\n            for j <- 0..col-3 do\n    \
        \            if is_magic(grid, i, j) do\n                    count = count +\
        \ 1\n                end\n            end\n        end\n        count\n    end\n\
        \n    def is_magic(grid, i, j) do\n        nums = for x <- i..i+2, y <- j..j+2,\
        \ do: Enum.at(Enum.at(grid, x), y)\n        sorted_nums = Enum.sort(nums)\n\
        \        if sorted_nums != Enum.to_list(1..9) do\n            false\n      \
        \  else\n            sum = Enum.at(Enum.at(grid, i), j) + Enum.at(Enum.at(grid,\
        \ i), j+1) + Enum.at(Enum.at(grid, i), j+2)\n            for x <- i..i+2 do\n\
        \                if Enum.at(Enum.at(grid, x), j) + Enum.at(Enum.at(grid, x),\
        \ j+1) + Enum.at(Enum.at(grid, x), j+2) != sum do\n                    false\n\
        \                end\n            end\n            for y <- j..j+2 do\n    \
        \            if Enum.at(Enum.at(grid, i), y) + Enum.at(Enum.at(grid, i+1), y)\
        \ + Enum.at(Enum.at(grid, i+2), y) != sum do\n                    false\n  \
        \              end\n            end\n            if Enum.at(Enum.at(grid, i),\
        \ j) + Enum.at(Enum.at(grid, i+1), j+1) + Enum.at(Enum.at(grid, i+2), j+2) !=\
        \ sum do\n                false\n            end\n            if Enum.at(Enum.at(grid,\
        \ i), j+2) + Enum.at(Enum.at(grid, i+1), j+1) + Enum.at(Enum.at(grid, i+2),\
        \ j) != sum do\n                false\n            end\n            true\n \
        \       end\n    end\nend"
    approach: The algorithm works by iterating over each possible 3x3 subgrid in the
      given grid. For each subgrid, it checks if the numbers are distinct and between
      1 and 9. Then, it calculates the sum of the first row and checks if the sums of
      all other rows, columns, and diagonals are equal to this sum. If all conditions
      are met, it increments the count of magic squares. The key intuition is to use
      a set to efficiently check for distinct numbers and to calculate the sums of rows,
      columns, and diagonals only once for each subgrid.
    time_complexity: O(row * col) where row and col are the dimensions of the grid.
      This is because we are iterating over each cell in the grid once to consider it
      as the top-left cell of a potential 3x3 subgrid. For each subgrid, we perform
      a constant amount of work to check if it is a magic square.
    space_complexity: O(1) because we are using a constant amount of space to store
      the count of magic squares and the sums of rows, columns, and diagonals. We are
      not using any data structures that scale with the size of the input grid.
    elapsed_time: 17.28275203704834
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-30 01:10:17 '
---

## Problem #840: Magic Squares In Grid

**Difficulty:** Medium

**Topics:** Array, Hash Table, Math, Matrix

## Problem Description

<p>A <code>3 x 3</code> <strong>magic square</strong> is a <code>3 x 3</code> grid filled with distinct numbers <strong>from </strong>1<strong> to </strong>9 such that each row, column, and both diagonals all have the same sum.</p>

<p>Given a <code>row x col</code> <code>grid</code> of integers, how many <code>3 x 3</code> magic square subgrids are there?</p>

<p>Note: while a magic square can only contain numbers from 1 to 9, <code>grid</code> may contain numbers up to 15.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/11/magic_main.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
<strong>Output:</strong> 1
<strong>Explanation: </strong>
The following subgrid is a 3 x 3 magic square:
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/11/magic_valid.jpg" style="width: 242px; height: 242px;" />
while this one is not:
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/11/magic_invalid.jpg" style="width: 242px; height: 242px;" />
In total, there is only one magic square inside the given grid.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[8]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>row == grid.length</code></li>
	<li><code>col == grid[i].length</code></li>
	<li><code>1 &lt;= row, col &lt;= 10</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 15</code></li>
</ul>


## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-30 01:10:00 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to count the number of 3x3 magic square subgrids within a given larger grid. A 3x3 magic square is defined by three key properties: it must contain distinct numbers from 1 to 9, and all its rows, columns, and both main diagonals must sum to the same value. For a 3x3 grid containing distinct numbers from 1 to 9, the sum of all numbers is 1+2+...+9 = 45. Since there are three rows (or columns), each row, column, and diagonal must sum to 45 / 3 = 15. Additionally, a known property of such magic squares is that the center element must always be 5.

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
    bool isMagic(int r, int c, const std::vector<std::vector<int>>& grid) {
        // 1. Center must be 5
        if (grid[r+1][c+1] != 5) {
            return false;
        }

        // 2. All numbers must be distinct and between 1 and 9
        std::vector<bool> seen(10, false);
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                int num = grid[r+i][c+j];
                if (num < 1 || num > 9) {
                    return false;
                }
                if (seen[num]) {
                    return false; // Duplicate
                }
                seen[num] = true;
            }
        }

        // 3. All sums must be 15
        // Rows
        if (!((grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15) &&
              (grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 15) &&
              (grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15))) {
            return false;
        }

        // Columns
        if (!((grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15) &&
              (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15) &&
              (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15))) {
            return false;
        }

        // Diagonals
        if (!((grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15) &&
              (grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15))) {
            return false;
        }

        return true;
    }

    int numMagicSquaresInside(std::vector<std::vector<int>>& grid) {
        int R = grid.size();
        int C = grid[0].size();

        if (R < 3 || C < 3) {
            return 0;
        }

        int count = 0;
        for (int r = 0; r <= R - 3; ++r) {
            for (int c = 0; c <= C - 3; ++c) {
                if (isMagic(r, c, grid)) {
                    count++;
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
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int numMagicSquaresInside(int[][] grid) {
        int R = grid.length;
        int C = grid[0].length;

        if (R < 3 || C < 3) {
            return 0;
        }

        int count = 0;
        for (int r = 0; r <= R - 3; ++r) {
            for (int c = 0; c <= C - 3; ++c) {
                if (isMagic(r, c, grid)) {
                    count++;
                }
            }
        }

        return count;
    }

    private boolean isMagic(int r, int c, int[][] grid) {
        // 1. Center must be 5
        if (grid[r+1][c+1] != 5) {
            return false;
        }

        // 2. All numbers must be distinct and between 1 and 9
        boolean[] seen = new boolean[10]; // Indices 1-9
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                int num = grid[r+i][c+j];
                if (num < 1 || num > 9) {
                    return false;
                }
                if (seen[num]) {
                    return false; // Duplicate
                }
                seen[num] = true;
            }
        }

        // 3. All sums must be 15
        // Rows
        if (!((grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15) &&
              (grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 15) &&
              (grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15))) {
            return false;
        }

        // Columns
        if (!((grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15) &&
              (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15) &&
              (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15))) {
            return false;
        }

        // Diagonals
        if (!((grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15) &&
              (grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15))) {
            return false;
        }

        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def is_magic(r, c):
            # 1. Center must be 5
            if grid[r+1][c+1] != 5:
                return False

            # 2. All numbers must be distinct and between 1 and 9
            seen = [False] * 10
            for i in range(3):
                for j in range(3):
                    num = grid[r+i][c+j]
                    if not (1 <= num <= 9):
                        return False
                    if seen[num]:
                        return False # Duplicate
                    seen[num] = True

            # 3. All sums must be 15
            # Rows
            if not (grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15 and \
                    grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 15 and \
                    grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15):
                return False

            # Columns
            if not (grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15 and \
                    grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15 and \
                    grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15):
                return False

            # Diagonals
            if not (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15 and \
                    grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15):
                return False

            return True

        count = 0
        if R < 3 or C < 3:
            return 0

        for r in range(R - 2):
            for c in range(C - 2):
                if is_magic(r, c):
                    count += 1

        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def is_magic(r, c):
            # 1. Center must be 5
            if grid[r+1][c+1] != 5:
                return False

            # 2. All numbers must be distinct and between 1 and 9
            seen = [False] * 10
            for i in range(3):
                for j in range(3):
                    num = grid[r+i][c+j]
                    if not (1 <= num <= 9):
                        return False
                    if seen[num]:
                        return False # Duplicate
                    seen[num] = True

            # 3. All sums must be 15
            # Rows
            if not (grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15 and \
                    grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 15 and \
                    grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15):
                return False

            # Columns
            if not (grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15 and \
                    grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15 and \
                    grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15):
                return False

            # Diagonals
            if not (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15 and \
                    grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15):
                return False

            return True

        count = 0
        if R < 3 or C < 3:
            return 0

        for r in range(R - 2):
            for c in range(C - 2):
                if is_magic(r, c):
                    count += 1

        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <string.h> // For memset

// Helper function to check if a 3x3 subgrid starting at (r, c) is a magic square
bool isMagic(int r, int c, int** grid, int gridSize, int* gridColSize) {
    // 1. Center must be 5
    if (grid[r+1][c+1] != 5) {
        return false;
    }

    // 2. All numbers must be distinct and between 1 and 9
    bool seen[10]; // Indices 1-9
    memset(seen, 0, sizeof(seen)); // Initialize all to false

    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            int num = grid[r+i][c+j];
            if (num < 1 || num > 9) {
                return false;
            }
            if (seen[num]) {
                return false; // Duplicate
            }
            seen[num] = true;
        }
    }

    // 3. All sums must be 15
    // Rows
    if (!((grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15) &&
          (grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 15) &&
          (grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15))) {
        return false;
    }

    // Columns
    if (!((grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15) &&
          (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15) &&
          (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15))) {
        return false;
    }

    // Diagonals
    if (!((grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15) &&
          (grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15))) {
        return false;
    }

    return true;
}

int numMagicSquaresInside(int** grid, int gridSize, int* gridColSize) {
    int R = gridSize;
    int C = gridColSize[0]; // Assuming all rows have the same number of columns

    if (R < 3 || C < 3) {
        return 0;
    }

    int count = 0;
    for (int r = 0; r <= R - 3; ++r) {
        for (int c = 0; c <= C - 3; ++c) {
            if (isMagic(r, c, grid, gridSize, gridColSize)) {
                count++;
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
using System;
using System.Collections.Generic;

public class Solution {
    public int NumMagicSquaresInside(int[][] grid) {
        int R = grid.Length;
        int C = grid[0].Length;

        if (R < 3 || C < 3) {
            return 0;
        }

        int count = 0;
        for (int r = 0; r <= R - 3; ++r) {
            for (int c = 0; c <= C - 3; ++c) {
                if (IsMagic(r, c, grid)) {
                    count++;
                }
            }
        }

        return count;
    }

    private bool IsMagic(int r, int c, int[][] grid) {
        // 1. Center must be 5
        if (grid[r+1][c+1] != 5) {
            return false;
        }

        // 2. All numbers must be distinct and between 1 and 9
        bool[] seen = new bool[10]; // Indices 1-9
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                int num = grid[r+i][c+j];
                if (num < 1 || num > 9) {
                    return false;
                }
                if (seen[num]) {
                    return false; // Duplicate
                }
                seen[num] = true;
            }
        }

        // 3. All sums must be 15
        // Rows
        if (!((grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15) &&
              (grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 15) &&
              (grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15))) {
            return false;
        }

        // Columns
        if (!((grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15) &&
              (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15) &&
              (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15))) {
            return false;
        }

        // Diagonals
        if (!((grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15) &&
              (grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15))) {
            return false;
        }

        return true;
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
var numMagicSquaresInside = function(grid) {
    const R = grid.length;
    const C = grid[0].length;

    if (R < 3 || C < 3) {
        return 0;
    }

    let count = 0;
    for (let r = 0; r <= R - 3; ++r) {
        for (let c = 0; c <= C - 3; ++c) {
            if (isMagic(r, c, grid)) {
                count++;
            }
        }
    }

    return count;
};

function isMagic(r, c, grid) {
    // 1. Center must be 5
    if (grid[r+1][c+1] !== 5) {
        return false;
    }

    // 2. All numbers must be distinct and between 1 and 9
    const seen = new Array(10).fill(false); // Indices 1-9
    for (let i = 0; i < 3; ++i) {
        for (let j = 0; j < 3; ++j) {
            const num = grid[r+i][c+j];
            if (num < 1 || num > 9) {
                return false;
            }
            if (seen[num]) {
                return false; // Duplicate
            }
            seen[num] = true;
        }
    }

    // 3. All sums must be 15
    // Rows
    if (!((grid[r][c] + grid[r][c+1] + grid[r][c+2] === 15) &&
          (grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] === 15) &&
          (grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] === 15))) {
        return false;
    }

    // Columns
    if (!((grid[r][c] + grid[r+1][c] + grid[r+2][c] === 15) &&
          (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] === 15) &&
          (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] === 15))) {
        return false;
    }

    // Diagonals
    if (!((grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] === 15) &&
          (grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] === 15))) {
        return false;
    }

    return true;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numMagicSquaresInside(grid: number[][]): number {
    const R = grid.length;
    const C = grid[0].length;

    if (R < 3 || C < 3) {
        return 0;
    }

    let count = 0;
    for (let r = 0; r <= R - 3; ++r) {
        for (let c = 0; c <= C - 3; ++c) {
            if (isMagic(r, c, grid)) {
                count++;
            }
        }
    }

    return count;
}

function isMagic(r: number, c: number, grid: number[][]): boolean {
    // 1. Center must be 5
    if (grid[r+1][c+1] !== 5) {
        return false;
    }

    // 2. All numbers must be distinct and between 1 and 9
    const seen: boolean[] = new Array(10).fill(false); // Indices 1-9
    for (let i = 0; i < 3; ++i) {
        for (let j = 0; j < 3; ++j) {
            const num = grid[r+i][c+j];
            if (num < 1 || num > 9) {
                return false;
            }
            if (seen[num]) {
                return false; // Duplicate
            }
            seen[num] = true;
        }
    }

    // 3. All sums must be 15
    // Rows
    if (!((grid[r][c] + grid[r][c+1] + grid[r][c+2] === 15) &&
          (grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] === 15) &&
          (grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] === 15))) {
        return false;
    }

    // Columns
    if (!((grid[r][c] + grid[r+1][c] + grid[r+2][c] === 15) &&
          (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] === 15) &&
          (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] === 15))) {
        return false;
    }

    // Diagonals
    if (!((grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] === 15) &&
          (grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] === 15))) {
        return false;
    }

    return true;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function numMagicSquaresInside($grid) {
        $R = count($grid);
        $C = count($grid[0]);

        if ($R < 3 || $C < 3) {
            return 0;
        }

        $count = 0;
        for ($r = 0; $r <= $R - 3; ++$r) {
            for ($c = 0; $c <= $C - 3; ++$c) {
                if ($this->isMagic($r, $c, $grid)) {
                    $count++;
                }
            }
        }

        return $count;
    }

    private function isMagic($r, $c, $grid) {
        // 1. Center must be 5
        if ($grid[$r+1][$c+1] !== 5) {
            return false;
        }

        // 2. All numbers must be distinct and between 1 and 9
        $seen = array_fill(0, 10, false); // Indices 1-9
        for ($i = 0; $i < 3; ++$i) {
            for ($j = 0; $j < 3; ++$j) {
                $num = $grid[$r+$i][$c+$j];
                if ($num < 1 || $num > 9) {
                    return false;
                }
                if ($seen[$num]) {
                    return false; // Duplicate
                }
                $seen[$num] = true;
            }
        }

        // 3. All sums must be 15
        // Rows
        if (!((($grid[$r][$c] + $grid[$r][$c+1] + $grid[$r][$c+2]) === 15) &&
              (($grid[$r+1][$c] + $grid[$r+1][$c+1] + $grid[$r+1][$c+2]) === 15) &&
              (($grid[$r+2][$c] + $grid[$r+2][$c+1] + $grid[$r+2][$c+2]) === 15))) {
            return false;
        }

        // Columns
        if (!((($grid[$r][$c] + $grid[$r+1][$c] + $grid[$r+2][$c]) === 15) &&
              (($grid[$r][$c+1] + $grid[$r+1][$c+1] + $grid[$r+2][$c+1]) === 15) &&
              (($grid[$r][$c+2] + $grid[$r+1][$c+2] + $grid[$r+2][$c+2]) === 15))) {
            return false;
        }

        // Diagonals
        if (!((($grid[$r][$c] + $grid[$r+1][$c+1] + $grid[$r+2][$c+2]) === 15) &&
              (($grid[$r][$c+2] + $grid[$r+1][$c+1] + $grid[$r+2][$c]) === 15))) {
            return false;
        }

        return true;
    }
}
?>
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func numMagicSquaresInside(_ grid: [[Int]]) -> Int {
        let R = grid.count
        let C = grid[0].count

        if R < 3 || C < 3 {
            return 0
        }

        var count = 0
        for r in 0...R - 3 {
            for c in 0...C - 3 {
                if isMagic(r, c, grid) {
                    count += 1
                }
            }
        }

        return count
    }

    private func isMagic(_ r: Int, _ c: Int, _ grid: [[Int]]) -> Bool {
        // 1. Center must be 5
        if grid[r+1][c+1] != 5 {
            return false
        }

        // 2. All numbers must be distinct and between 1 and 9
        var seen = Array(repeating: false, count: 10) // Indices 1-9
        for i in 0..<3 {
            for j in 0..<3 {
                let num = grid[r+i][c+j]
                if num < 1 || num > 9 {
                    return false
                }
                if seen[num] {
                    return false // Duplicate
                }
                seen[num] = true
            }
        }

        // 3. All sums must be 15
        // Rows
        if !((grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15) &&
             (grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 15) &&
             (grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15)) {
            return false
        }

        // Columns
        if !((grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15) &&
             (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15) &&
             (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15)) {
            return false
        }

        // Diagonals
        if !((grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15) &&
             (grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15)) {
            return false
        }

        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun numMagicSquaresInside(grid: Array<IntArray>): Int {
        val R = grid.size
        val C = grid[0].size

        if (R < 3 || C < 3) {
            return 0
        }

        var count = 0
        for (r in 0..R - 3) {
            for (c in 0..C - 3) {
                if (isMagic(r, c, grid)) {
                    count++
                }
            }
        }

        return count
    }

    private fun isMagic(r: Int, c: Int, grid: Array<IntArray>): Boolean {
        // 1. Center must be 5
        if (grid[r+1][c+1] != 5) {
            return false
        }

        // 2. All numbers must be distinct and between 1 and 9
        val seen = BooleanArray(10) // Indices 1-9
        for (i in 0 until 3) {
            for (j in 0 until 3) {
                val num = grid[r+i][c+j]
                if (num < 1 || num > 9) {
                    return false
                }
                if (seen[num]) {
                    return false // Duplicate
                }
                seen[num] = true
            }
        }

        // 3. All sums must be 15
        // Rows
        if (!((grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15) &&
              (grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 15) &&
              (grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15))) {
            return false
        }

        // Columns
        if (!((grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15) &&
              (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15) &&
              (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15))) {
            return false
        }

        // Diagonals
        if (!((grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15) &&
              (grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15))) {
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
  int numMagicSquaresInside(List<List<int>> grid) {
    int R = grid.length;
    int C = grid[0].length;

    if (R < 3 || C < 3) {
      return 0;
    }

    int count = 0;
    for (int r = 0; r <= R - 3; ++r) {
      for (int c = 0; c <= C - 3; ++c) {
        if (isMagic(r, c, grid)) {
          count++;
        }
      }
    }

    return count;
  }

  bool isMagic(int r, int c, List<List<int>> grid) {
    // 1. Center must be 5
    if (grid[r + 1][c + 1] != 5) {
      return false;
    }

    // 2. All numbers must be distinct and between 1 and 9
    List<bool> seen = List.filled(10, false); // Indices 1-9
    for (int i = 0; i < 3; ++i) {
      for (int j = 0; j < 3; ++j) {
        int num = grid[r + i][c + j];
        if (num < 1 || num > 9) {
          return false;
        }
        if (seen[num]) {
          return false; // Duplicate
        }
        seen[num] = true;
      }
    }

    // 3. All sums must be 15
    // Rows
    if (!((grid[r][c] + grid[r][c + 1] + grid[r][c + 2] == 15) &&
        (grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2] == 15) &&
        (grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2] == 15))) {
      return false;
    }

    // Columns
    if (!((grid[r][c] + grid[r + 1][c] + grid[r + 2][c] == 15) &&
        (grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1] == 15) &&
        (grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2] == 15))) {
      return false;
    }

    // Diagonals
    if (!((grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] == 15) &&
        (grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] == 15))) {
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
package main

func numMagicSquaresInside(grid [][]int) int {
    R := len(grid)
    C := len(grid[0])

    if R < 3 || C < 3 {
        return 0
    }

    count := 0
    for r := 0; r <= R - 3; r++ {
        for c := 0; c <= C - 3; c++ {
            if isMagic(r, c, grid) {
                count++
            }
        }
    }

    return count
}

func isMagic(r, c int, grid [][]int) bool {
    // 1. Center must be 5
    if grid[r+1][c+1] != 5 {
        return false
    }

    // 2. All numbers must be distinct and between 1 and 9
    seen := make([]bool, 10) // Indices 1-9
    for i := 0; i < 3; i++ {
        for j := 0; j < 3; j++ {
            num := grid[r+i][c+j]
            if num < 1 || num > 9 {
                return false
            }
            if seen[num] {
                return false // Duplicate
            }
            seen[num] = true
        }
    }

    // 3. All sums must be 15
    // Rows
    if !((grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15) &&
         (grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 15) &&
         (grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15)) {
        return false
    }

    // Columns
    if !((grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15) &&
         (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15) &&
         (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15)) {
        return false
    }

    // Diagonals
    if !((grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15) &&
         (grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15)) {
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
def num_magic_squares_inside(grid)
    r_len = grid.length
    c_len = grid[0].length

    return 0 if r_len < 3 || c_len < 3

    count = 0
    (0..r_len - 3).each do |r|
        (0..c_len - 3).each do |c|
            count += 1 if is_magic(r, c, grid)
        end
    end

    count
end

def is_magic(r, c, grid)
    # 1. Center must be 5
    return false if grid[r+1][c+1] != 5

    # 2. All numbers must be distinct and between 1 and 9
    seen = Array.new(10, false) # Indices 1-9
    (0..2).each do |i|
        (0..2).each do |j|
            num = grid[r+i][c+j]
            return false if num < 1 || num > 9
            return false if seen[num] # Duplicate
            seen[num] = true
        end
    end

    # 3. All sums must be 15
    # Rows
    return false unless (grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15 &&
                         grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 15 &&
                         grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15)

    # Columns
    return false unless (grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15 &&
                         grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15 &&
                         grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15)

    # Diagonals
    return false unless (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15 &&
                         grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15)

    true
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def numMagicSquaresInside(grid: Array[Array[Int]]): Int = {
        val R = grid.length
        val C = grid(0).length

        if (R < 3 || C < 3) {
            return 0
        }

        var count = 0
        for (r <- 0 to R - 3) {
            for (c <- 0 to C - 3) {
                if (isMagic(r, c, grid)) {
                    count += 1
                }
            }
        }

        count
    }

    private def isMagic(r: Int, c: Int, grid: Array[Array[Int]]): Boolean = {
        // 1. Center must be 5
        if (grid(r+1)(c+1) != 5) {
            return false
        }

        // 2. All numbers must be distinct and between 1 and 9
        val seen = Array.fill(10)(false) // Indices 1-9
        for (i <- 0 until 3) {
            for (j <- 0 until 3) {
                val num = grid(r+i)(c+j)
                if (num < 1 || num > 9) {
                    return false
                }
                if (seen(num)) {
                    return false // Duplicate
                }
                seen(num) = true
            }
        }

        // 3. All sums must be 15
        // Rows
        if (!((grid(r)(c) + grid(r)(c+1) + grid(r)(c+2) == 15) &&
              (grid(r+1)(c) + grid(r+1)(c+1) + grid(r+1)(c+2) == 15) &&
              (grid(r+2)(c) + grid(r+2)(c+1) + grid(r+2)(c+2) == 15))) {
            return false
        }

        // Columns
        if (!((grid(r)(c) + grid(r+1)(c) + grid(r+2)(c) == 15) &&
              (grid(r)(c+1) + grid(r+1)(c+1) + grid(r+2)(c+1) == 15) &&
              (grid(r)(c+2) + grid(r+1)(c+2) + grid(r+2)(c+2) == 15))) {
            return false
        }

        // Diagonals
        if (!((grid(r)(c) + grid(r+1)(c+1) + grid(r+2)(c+2) == 15) &&
              (grid(r)(c+2) + grid(r+1)(c+1) + grid(r+2)(c) == 15))) {
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
    pub fn num_magic_squares_inside(grid: Vec<Vec<i32>>) -> i32 {
        let r_len = grid.len();
        let c_len = grid[0].len();

        if r_len < 3 || c_len < 3 {
            return 0;
        }

        let mut count = 0;
        for r in 0..=r_len - 3 {
            for c in 0..=c_len - 3 {
                if Solution::is_magic(r, c, &grid) {
                    count += 1;
                }
            }
        }

        count
    }

    fn is_magic(r: usize, c: usize, grid: &Vec<Vec<i32>>) -> bool {
        // 1. Center must be 5
        if grid[r+1][c+1] != 5 {
            return false;
        }

        // 2. All numbers must be distinct and between 1 and 9
        let mut seen = [false; 10]; // Indices 1-9
        for i in 0..3 {
            for j in 0..3 {
                let num = grid[r+i][c+j];
                if num < 1 || num > 9 {
                    return false;
                }
                if seen[num as usize] {
                    return false; // Duplicate
                }
                seen[num as usize] = true;
            }
        }

        // 3. All sums must be 15
        // Rows
        if !((grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15) &&
             (grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 15) &&
             (grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15)) {
            return false;
        }

        // Columns
        if !((grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15) &&
             (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15) &&
             (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15)) {
            return false;
        }

        // Diagonals
        if !((grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15) &&
             (grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15)) {
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
#lang racket

(define (num-magic-squares-inside grid)
  (define R (vector-length grid))
  (define C (vector-length (vector-ref grid 0)))

  (define (is-magic? r c)
    (call-with-current-continuation
     (lambda (return)
       ;; 1. Center must be 5
       (when (not (= (vector-ref (vector-ref grid (+ r 1)) (+ c 1)) 5))
         (return #f))

       ;; 2. All numbers must be distinct and between 1 and 9
       (define seen (make-vector 10 #f))
       (for* ([i (in-range 3)]
              [j (in-range 3)])
         (define num (vector-ref (vector-ref grid (+ r i)) (+ c j)))
         (when (or (< num 1) (> num 9))
           (return #f))
         (when (vector-ref seen num)
           (return #f)) ; Duplicate
         (vector-set! seen num #t))

       ;; 3. All sums must be 15
       ;; Rows
       (when (not (and (= (+ (vector-ref (vector-ref grid r) c) (vector-ref (vector-ref grid r) (+ c 1)) (vector-ref (vector-ref grid r) (+ c 2))) 15)
                       (= (+ (vector-ref (vector-ref grid (+ r 1)) c) (vector-ref (vector-ref grid (+ r 1)) (+ c 1)) (vector-ref (vector-ref grid (+ r 1)) (+ c 2))) 15)
                       (= (+ (vector-ref (vector-ref grid (+ r 2)) c) (vector-ref (vector-ref grid (+ r 2)) (+ c 1)) (vector-ref (vector-ref grid (+ r 2)) (+ c 2))) 15)))
         (return #f))

       ;; Columns
       (when (not (and (= (+ (vector-ref (vector-ref grid r) c) (vector-ref (vector-ref grid (+ r 1)) c) (vector-ref (vector-ref grid (+ r 2)) c)) 15)
                       (= (+ (vector-ref (vector-ref grid r) (+ c 1)) (vector-ref (vector-ref grid (+ r 1)) (+ c 1)) (vector-ref (vector-ref grid (+ r 2)) (+ c 1))) 15)
                       (= (+ (vector-ref (vector-ref grid r) (+ c 2)) (vector-ref (vector-ref grid (+ r 1)) (+ c 2)) (vector-ref (vector-ref grid (+ r 2)) (+ c 2))) 15)))
         (return #f))

       ;; Diagonals
       (when (not (and (= (+ (vector-ref (vector-ref grid r) c) (vector-ref (vector-ref grid (+ r 1)) (+ c 1)) (vector-ref (vector-ref grid (+ r 2)) (+ c 2))) 15)
                       (= (+ (vector-ref (vector-ref grid r) (+ c 2)) (vector-ref (vector-ref grid (+ r 1)) (+ c 1)) (vector-ref (vector-ref grid (+ r 2)) c)) 15)))
         (return #f))

       #t))) ; All checks passed

  (for*/sum ([r (in-range (max 0 (- R 2)))]
             [c (in-range (max 0 (- C 2)))])
    (if (is-magic? r c) 1 0)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([num_magic_squares_inside/1]).

num_magic_squares_inside(Grid) ->
R = length(Grid),
C = length(hd(Grid)),

case {R, C} of
{R_val, C_val} when R_val < 3; C_val < 3 -> 0;
_ ->
Count = 0,
num_magic_squares_inside_loop(0, R - 3, 0, C - 3, Grid, Count)
end.

num_magic_squares_inside_loop(R_idx, R_max, C_idx, C_max, Grid, Acc) when R_idx > R_max -> Acc;
num_magic_squares_inside_loop(R_idx, R_max, C_idx, C_max, Grid, Acc) when C_idx > C_max ->
num_magic_squares_inside_loop(R_idx + 1, R_max, 0, C_max, Grid, Acc);
num_magic_squares_inside_loop(R_idx, R_max, C_idx, C_max, Grid, Acc) ->
NewAcc = case is_magic(R_idx, C_idx, Grid) of
true -> Acc + 1;
false -> Acc
end,
num_magic_squares_inside_loop(R_idx, R_max, C_idx + 1, C_max, Grid, NewAcc).

is_magic(R_start, C_start, Grid) ->
% Helper to get element at (row, col)
% Lists are 1-indexed in Erlang, so add 1 to 0-indexed R_start, C_start
get_elem = fun(Row, Col, G) ->
lists:nth(Col + 1, lists:nth(Row + 1, G))
end,

% 1. Center must be 5
Center = get_elem(R_start + 1, C_start + 1, Grid),
if Center =/= 5 -> false; true ->
% 2. All numbers must be distinct and between 1 and 9
Nums = [
get_elem(R_start, C_start), get_elem(R_start, C_start + 1), get_elem(R_start, C_start + 2),
get_elem(R_start + 1, C_start), get_elem(R_start + 1, C_start + 1), get_elem(R_start + 1, C_start + 2),
get_elem(R_start + 2, C_start), get_elem(R_start + 2, C_start + 1), get_elem(R_start + 2, C_start + 2)
],

% Check range and distinctness
CheckNums = fun
([], _) -> true;
([H|T], CurrentSeen) when H < 1; H > 9 -> false;
([H|T], CurrentSeen) ->
    case maps:is_key(H, CurrentSeen) of
        true -> false; % Duplicate
        false -> CheckNums(T, maps:put(H, true, CurrentSeen))
    end
end,

if CheckNums(Nums, #{}) =:= false -> false; true ->
% 3. All sums must be 15
% Rows
Row1Sum = get_elem(R_start, C_start) + get_elem(R_start, C_start + 1) + get_elem(R_start, C_start + 2),
Row2Sum = get_elem(R_start + 1, C_start) + get_elem(R_start + 1, C_start + 1) + get_elem(R_start + 1, C_start + 2),
Row3Sum = get_elem(R_start + 2, C_start) + get_elem(R_start + 2, C_start + 1) + get_elem(R_start + 2, C_start + 2),

% Columns
Col1Sum = get_elem(R_start, C_start) + get_elem(R_start + 1, C_start) + get_elem(R_start + 2, C_start),
Col2Sum = get_elem(R_start, C_start + 1) + get_elem(R_start + 1, C_start + 1) + get_elem(R_start + 2, C_start + 1),
Col3Sum = get_elem(R_start, C_start + 2) + get_elem(R_start + 1, C_start + 2) + get_elem(R_start + 2, C_start + 2),

% Diagonals
Diag1Sum = get_elem(R_start, C_start) + get_elem(R_start + 1, C_start + 1) + get_elem(R_start + 2, C_start + 2),
Diag2Sum = get_elem(R_start, C_start + 2) + get_elem(R_start + 1, C_start + 1) + get_elem(R_start + 2, C_start),

if Row1Sum =:= 15, Row2Sum =:= 15, Row3Sum =:= 15,
   Col1Sum =:= 15, Col2Sum =:= 15, Col3Sum =:= 15,
   Diag1Sum =:= 15, Diag2Sum =:= 15 -> true;
   true -> false
end
end
end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec num_magic_squares_inside(grid :: [[integer]]) :: integer
  def num_magic_squares_inside(grid) do
    r = length(grid)
    c = length(hd(grid))

    if r < 3 || c < 3 do
      0
    else
      0..(r - 3)
      |> Enum.reduce(0, fn r_idx, acc ->
        0..(c - 3)
        |> Enum.reduce(acc, fn c_idx, inner_acc ->
          if is_magic(r_idx, c_idx, grid) do
            inner_acc + 1
          else
            inner_acc
          end
        end)
      end)
    end
  end

  defp is_magic(r_start, c_start, grid) do
    # Helper to get element at (row, col)
    # Lists are 0-indexed in Elixir
    get_elem = fn row, col ->
      Enum.at(Enum.at(grid, row), col)
    end

    # 1. Center must be 5
    center = get_elem.(r_start + 1, c_start + 1)
    if center != 5, do: (
      false
    ) else (
      # 2. All numbers must be distinct and between 1 and 9
      nums = [
        get_elem.(r_start, c_start), get_elem.(r_start, c_start + 1), get_elem.(r_start, c_start + 2),
        get_elem.(r_start + 1, c_start), get_elem.(r_start + 1, c_start + 1), get_elem.(r_start + 1, c_start + 2),
        get_elem.(r_start + 2, c_start), get_elem.(r_start + 2, c_start + 1), get_elem.(r_start + 2, c_start + 2)
      ]

      # Check range and distinctness
      seen = MapSet.new()
      check_nums = fn
        [], _ -> true
        [h | t], current_seen when h < 1 or h > 9 -> false
        [h | t], current_seen ->
          if MapSet.member?(current_seen, h) do
            false # Duplicate
          else
            check_nums.(t, MapSet.put(current_seen, h))
          end
      end

      if not check_nums.(nums, seen), do: (
        false
      ) else (
        # 3. All sums must be 15
        # Rows
        row1_sum = get_elem.(r_start, c_start) + get_elem.(r_start, c_start + 1) + get_elem.(r_start, c_start + 2)
        row2_sum = get_elem.(r_start + 1, c_start) + get_elem.(r_start + 1, c_start + 1) + get_elem.(r_start + 1, c_start + 2)
        row3_sum = get_elem.(r_start + 2, c_start) + get_elem.(r_start + 2, c_start + 1) + get_elem.(r_start + 2, c_start + 2)

        # Columns
        col1_sum = get_elem.(r_start, c_start) + get_elem.(r_start + 1, c_start) + get_elem.(r_start + 2, c_start)
        col2_sum = get_elem.(r_start, c_start + 1) + get_elem.(r_start + 1, c_start + 1) + get_elem.(r_start + 2, c_start + 1)
        col3_sum = get_elem.(r_start, c_start + 2) + get_elem.(r_start + 1, c_start + 2) + get_elem.(r_start + 2, c_start + 2)

        # Diagonals
        diag1_sum = get_elem.(r_start, c_start) + get_elem.(r_start + 1, c_start + 1) + get_elem.(r_start + 2, c_start + 2)
        diag2_sum = get_elem.(r_start, c_start + 2) + get_elem.(r_start + 1, c_start + 1) + get_elem.(r_start + 2, c_start)

        if row1_sum == 15 && row2_sum == 15 && row3_sum == 15 &&
           col1_sum == 15 && col2_sum == 15 && col3_sum == 15 &&
           diag1_sum == 15 && diag2_sum == 15 do
          true
        else
          false
        end
      )
    )
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(R * C), where R is the number of rows and C is the number of columns in the input grid. We iterate through all possible top-left corners of 3x3 subgrids. There are (R-2) * (C-2) such corners. For each potential subgrid, the `isMagic` helper function performs a constant number of operations: checking the center element, iterating through 9 numbers to verify range (1-9) and distinctness using a fixed-size boolean array, and performing 8 fixed-sum checks. Since R and C are constrained to be at most 10, the total number of subgrids is at most 8 * 8 = 64, making the overall operation count very small and effectively constant.

- **Space Complexity:** The space complexity is O(1). The `isMagic` helper function uses a boolean array of size 10 (to track numbers 0-9) to check for distinctness and range. This array's size is constant and does not depend on the dimensions of the input grid.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-30 01:10:17 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The algorithm works by iterating over each possible 3x3 subgrid in the given grid. For each subgrid, it checks if the numbers are distinct and between 1 and 9. Then, it calculates the sum of the first row and checks if the sums of all other rows, columns, and diagonals are equal to this sum. If all conditions are met, it increments the count of magic squares. The key intuition is to use a set to efficiently check for distinct numbers and to calculate the sums of rows, columns, and diagonals only once for each subgrid.

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
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int count = 0;
        int row = grid.size();
        int col = grid[0].size();
        for (int i = 0; i < row - 2; i++) {
            for (int j = 0; j < col - 2; j++) {
                if (isMagic(grid, i, j)) {
                    count++;
                }
            }
        }
        return count;
    }

    bool isMagic(vector<vector<int>>& grid, int i, int j) {
        vector<int> nums;
        for (int x = i; x < i + 3; x++) {
            for (int y = j; y < j + 3; y++) {
                nums.push_back(grid[x][y]);
            }
        }
        sort(nums.begin(), nums.end());
        if (nums != vector<int>{1, 2, 3, 4, 5, 6, 7, 8, 9}) {
            return false;
        }
        int sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2];
        for (int x = i; x < i + 3; x++) {
            if (grid[x][j] + grid[x][j + 1] + grid[x][j + 2] != sum) {
                return false;
            }
        }
        for (int y = j; y < j + 3; y++) {
            if (grid[i][y] + grid[i + 1][y] + grid[i + 2][y] != sum) {
                return false;
            }
        }
        if (grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != sum) {
            return false;
        }
        if (grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != sum) {
            return false;
        }
        return true;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int numMagicSquaresInside(int[][] grid) {
        int count = 0;
        int row = grid.length;
        int col = grid[0].length;
        for (int i = 0; i < row - 2; i++) {
            for (int j = 0; j < col - 2; j++) {
                if (isMagic(grid, i, j)) {
                    count++;
                }
            }
        }
        return count;
    }

    public boolean isMagic(int[][] grid, int i, int j) {
        int[] nums = new int[9];
        int index = 0;
        for (int x = i; x < i + 3; x++) {
            for (int y = j; y < j + 3; y++) {
                nums[index++] = grid[x][y];
            }
        }
        Arrays.sort(nums);
        for (int k = 0; k < 9; k++) {
            if (nums[k] != k + 1) {
                return false;
            }
        }
        int sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2];
        for (int x = i; x < i + 3; x++) {
            if (grid[x][j] + grid[x][j + 1] + grid[x][j + 2] != sum) {
                return false;
            }
        }
        for (int y = j; y < j + 3; y++) {
            if (grid[i][y] + grid[i + 1][y] + grid[i + 2][y] != sum) {
                return false;
            }
        }
        if (grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != sum) {
            return false;
        }
        if (grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != sum) {
            return false;
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        count = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row - 2):
            for j in range(col - 2):
                if self.isMagic(grid, i, j):
                    count += 1
        return count

    def isMagic(self, grid: list[list[int]], i: int, j: int) -> bool:
        nums = [grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
        if sorted(nums) != list(range(1, 10)):
            return False
        sum_ = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
        for x in range(i, i + 3):
            if grid[x][j] + grid[x][j + 1] + grid[x][j + 2] != sum_:
                return False
        for y in range(j, j + 3):
            if grid[i][y] + grid[i + 1][y] + grid[i + 2][y] != sum_:
                return False
        if grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != sum_:
            return False
        if grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != sum_:
            return False
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        count = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row - 2):
            for j in range(col - 2):
                if self.isMagic(grid, i, j):
                    count += 1
        return count

    def isMagic(self, grid: list[list[int]], i: int, j: int) -> bool:
        nums = [grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
        if sorted(nums) != list(range(1, 10)):
            return False
        sum_ = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
        for x in range(i, i + 3):
            if grid[x][j] + grid[x][j + 1] + grid[x][j + 2] != sum_:
                return False
        for y in range(j, j + 3):
            if grid[i][y] + grid[i + 1][y] + grid[i + 2][y] != sum_:
                return False
        if grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != sum_:
            return False
        if grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != sum_:
            return False
        return True
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

int numMagicSquaresInside(int** grid, int gridSize, int* gridColSize) {
    int count = 0;
    for (int i = 0; i < gridSize - 2; i++) {
        for (int j = 0; j < gridColSize[i] - 2; j++) {
            if (isMagic(grid, i, j, gridSize, gridColSize)) {
                count++;
            }
        }
    }
    return count;
}

int isMagic(int** grid, int i, int j, int gridSize, int* gridColSize) {
    int nums[9];
    int index = 0;
    for (int x = i; x < i + 3; x++) {
        for (int y = j; y < j + 3; y++) {
            nums[index++] = grid[x][y];
        }
    }
    int temp;
    for (int k = 0; k < 9; k++) {
        for (int l = k + 1; l < 9; l++) {
            if (nums[k] > nums[l]) {
                temp = nums[k];
                nums[k] = nums[l];
                nums[l] = temp;
            }
        }
    }
    for (int k = 0; k < 9; k++) {
        if (nums[k] != k + 1) {
            return 0;
        }
    }
    int sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2];
    for (int x = i; x < i + 3; x++) {
        if (grid[x][j] + grid[x][j + 1] + grid[x][j + 2] != sum) {
            return 0;
        }
    }
    for (int y = j; y < j + 3; y++) {
        if (grid[i][y] + grid[i + 1][y] + grid[i + 2][y] != sum) {
            return 0;
        }
    }
    if (grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != sum) {
        return 0;
    }
    if (grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != sum) {
        return 0;
    }
    return 1;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int NumMagicSquaresInside(int[][] grid) {
        int count = 0;
        int row = grid.Length;
        int col = grid[0].Length;
        for (int i = 0; i < row - 2; i++) {
            for (int j = 0; j < col - 2; j++) {
                if (IsMagic(grid, i, j)) {
                    count++;
                }
            }
        }
        return count;
    }

    public bool IsMagic(int[][] grid, int i, int j) {
        int[] nums = new int[9];
        int index = 0;
        for (int x = i; x < i + 3; x++) {
            for (int y = j; y < j + 3; y++) {
                nums[index++] = grid[x][y];
            }
        }
        Array.Sort(nums);
        for (int k = 0; k < 9; k++) {
            if (nums[k] != k + 1) {
                return false;
            }
        }
        int sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2];
        for (int x = i; x < i + 3; x++) {
            if (grid[x][j] + grid[x][j + 1] + grid[x][j + 2] != sum) {
                return false;
            }
        }
        for (int y = j; y < j + 3; y++) {
            if (grid[i][y] + grid[i + 1][y] + grid[i + 2][y] != sum) {
                return false;
            }
        }
        if (grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != sum) {
            return false;
        }
        if (grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != sum) {
            return false;
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var numMagicSquaresInside = function(grid) {
    let count = 0;
    let row = grid.length;
    let col = grid[0].length;
    for (let i = 0; i < row - 2; i++) {
        for (let j = 0; j < col - 2; j++) {
            if (isMagic(grid, i, j)) {
                count++;
            }
        }
    }
    return count;
};

var isMagic = function(grid, i, j) {
    let nums = [];
    for (let x = i; x < i + 3; x++) {
        for (let y = j; y < j + 3; y++) {
            nums.push(grid[x][y]);
        }
    }
    nums.sort((a, b) => a - b);
    for (let k = 0; k < 9; k++) {
        if (nums[k] !== k + 1) {
            return false;
        }
    }
    let sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2];
    for (let x = i; x < i + 3; x++) {
        if (grid[x][j] + grid[x][j + 1] + grid[x][j + 2] !== sum) {
            return false;
        }
    }
    for (let y = j; y < j + 3; y++) {
        if (grid[i][y] + grid[i + 1][y] + grid[i + 2][y] !== sum) {
            return false;
        }
    }
    if (grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] !== sum) {
        return false;
    }
    if (grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] !== sum) {
        return false;
    }
    return true;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numMagicSquaresInside(grid: number[][]): number {
    let count: number = 0;
    let row: number = grid.length;
    let col: number = grid[0].length;
    for (let i: number = 0; i < row - 2; i++) {
        for (let j: number = 0; j < col - 2; j++) {
            if (isMagic(grid, i, j)) {
                count++;
            }
        }
    }
    return count;
}

function isMagic(grid: number[][], i: number, j: number): boolean {
    let nums: number[] = [];
    for (let x: number = i; x < i + 3; x++) {
        for (let y: number = j; y < j + 3; y++) {
            nums.push(grid[x][y]);
        }
    }
    nums.sort((a, b) => a - b);
    for (let k: number = 0; k < 9; k++) {
        if (nums[k] !== k + 1) {
            return false;
        }
    }
    let sum: number = grid[i][j] + grid[i][j + 1] + grid[i][j + 2];
    for (let x: number = i; x < i + 3; x++) {
        if (grid[x][j] + grid[x][j + 1] + grid[x][j + 2] !== sum) {
            return false;
        }
    }
    for (let y: number = j; y < j + 3; y++) {
        if (grid[i][y] + grid[i + 1][y] + grid[i + 2][y] !== sum) {
            return false;
        }
    }
    if (grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] !== sum) {
        return false;
    }
    if (grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] !== sum) {
        return false;
    }
    return true;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function numMagicSquaresInside($grid) {
        $count = 0;
        $row = count($grid);
        $col = count($grid[0]);
        for ($i = 0; $i < $row - 2; $i++) {
            for ($j = 0; $j < $col - 2; $j++) {
                if ($this->isMagic($grid, $i, $j)) {
                    $count++;
                }
            }
        }
        return $count;
    }

    function isMagic($grid, $i, $j) {
        $nums = array();
        for ($x = $i; $x < $i + 3; $x++) {
            for ($y = $j; $y < $j + 3; $y++) {
                $nums[] = $grid[$x][$y];
            }
        }
        sort($nums);
        for ($k = 0; $k < 9; $k++) {
            if ($nums[$k] != $k + 1) {
                return false;
            }
        }
        $sum = $grid[$i][$j] + $grid[$i][$j + 1] + $grid[$i][$j + 2];
        for ($x = $i; $x < $i + 3; $x++) {
            if ($grid[$x][$j] + $grid[$x][$j + 1] + $grid[$x][$j + 2] != $sum) {
                return false;
            }
        }
        for ($y = $j; $y < $j + 3; $y++) {
            if ($grid[$i][$y] + $grid[$i + 1][$y] + $grid[$i + 2][$y] != $sum) {
                return false;
            }
        }
        if ($grid[$i][$j] + $grid[$i + 1][$j + 1] + $grid[$i + 2][$j + 2] != $sum) {
            return false;
        }
        if ($grid[$i][$j + 2] + $grid[$i + 1][$j + 1] + $grid[$i + 2][$j] != $sum) {
            return false;
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func numMagicSquaresInside(_ grid: [[Int]]) -> Int {
        var count = 0
        let row = grid.count
        let col = grid[0].count
        for i in 0..<row-2 {
            for j in 0..<col-2 {
                if isMagic(grid, i, j) {
                    count += 1
                }
            }
        }
        return count
    }

    func isMagic(_ grid: [[Int]], _ i: Int, _ j: Int) -> Bool {
        var nums: [Int] = []
        for x in i...i+2 {
            for y in j...j+2 {
                nums.append(grid[x][y])
            }
        }
        nums.sort()
        for k in 0...8 {
            if nums[k] != k + 1 {
                return false
            }
        }
        let sum = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        for x in i...i+2 {
            if grid[x][j] + grid[x][j+1] + grid[x][j+2] != sum {
                return false
            }
        }
        for y in j...j+2 {
            if grid[i][y] + grid[i+1][y] + grid[i+2][y] != sum {
                return false
            }
        }
        if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != sum {
            return false
        }
        if grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] != sum {
            return false
        }
        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun numMagicSquaresInside(grid: Array<IntArray>): Int {
        var count = 0
        val row = grid.size
        val col = grid[0].size
        for (i in 0 until row - 2) {
            for (j in 0 until col - 2) {
                if (isMagic(grid, i, j)) {
                    count++
                }
            }
        }
        return count
    }

    fun isMagic(grid: Array<IntArray>, i: Int, j: Int): Boolean {
        val nums = mutableListOf<Int>()
        for (x in i until i + 3) {
            for (y in j until j + 3) {
                nums.add(grid[x][y])
            }
        }
        nums.sort()
        for (k in 0 until 9) {
            if (nums[k] != k + 1) {
                return false
            }
        }
        val sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
        for (x in i until i + 3) {
            if (grid[x][j] + grid[x][j + 1] + grid[x][j + 2] != sum) {
                return false
            }
        }
        for (y in j until j + 3) {
            if (grid[i][y] + grid[i + 1][y] + grid[i + 2][y] != sum) {
                return false
            }
        }
        if (grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != sum) {
            return false
        }
        if (grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != sum) {
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
    int numMagicSquaresInside(List<List<int>> grid) {
        int count = 0;
        int row = grid.length;
        int col = grid[0].length;
        for (int i = 0; i < row - 2; i++) {
            for (int j = 0; j < col - 2; j++) {
                if (isMagic(grid, i, j)) {
                    count++;
                }
            }
        }
        return count;
    }

    bool isMagic(List<List<int>> grid, int i, int j) {
        List<int> nums = [];
        for (int x = i; x < i + 3; x++) {
            for (int y = j; y < j + 3; y++) {
                nums.add(grid[x][y]);
            }
        }
        nums.sort();
        for (int k = 0; k < 9; k++) {
            if (nums[k] != k + 1) {
                return false;
            }
        }
        int sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2];
        for (int x = i; x < i + 3; x++) {
            if (grid[x][j] + grid[x][j + 1] + grid[x][j + 2] != sum) {
                return false;
            }
        }
        for (int y = j; y < j + 3; y++) {
            if (grid[i][y] + grid[i + 1][y] + grid[i + 2][y] != sum) {
                return false;
            }
        }
        if (grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != sum) {
            return false;
        }
        if (grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != sum) {
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
package main

import (
    "fmt"
    "sort"
)

type Solution struct{}

func (s *Solution) numMagicSquaresInside(grid [][]int) int {
    count := 0
    row := len(grid)
    col := len(grid[0])
    for i := 0; i < row-2; i++ {
        for j := 0; j < col-2; j++ {
            if s.isMagic(grid, i, j) {
                count++
            }
        }
    }
    return count
}

func (s *Solution) isMagic(grid [][]int, i, j int) bool {
    nums := make([]int, 0)
    for x := i; x < i+3; x++ {
        for y := j; y < j+3; y++ {
            nums = append(nums, grid[x][y])
        }
    }
    sort.Ints(nums)
    for k := 0; k < 9; k++ {
        if nums[k] != k+1 {
            return false
        }
    }
    sum := grid[i][j] + grid[i][j+1] + grid[i][j+2]
    for x := i; x < i+3; x++ {
        if grid[x][j]+grid[x][j+1]+grid[x][j+2] != sum {
            return false
        }
    }
    for y := j; y < j+3; y++ {
        if grid[i][y]+grid[i+1][y]+grid[i+2][y] != sum {
            return false
        }
    }
    if grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2] != sum {
        return false
    }
    if grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j] != sum {
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
class Solution
    def num_magic_squares_inside(grid)
        count = 0
        row = grid.size
        col = grid[0].size
        (0...row-2).each do |i|
            (0...col-2).each do |j|
                if is_magic(grid, i, j)
                    count += 1
                end
            end
        end
        count
    end

    def is_magic(grid, i, j)
        nums = []
        (i...i+3).each do |x|
            (j...j+3).each do |y|
                nums << grid[x][y]
            end
        end
        nums.sort!
        (0...9).each do |k|
            return false if nums[k] != k + 1
        end
        sum = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        (i...i+3).each do |x|
            return false if grid[x][j] + grid[x][j+1] + grid[x][j+2] != sum
        end
        (j...j+3).each do |y|
            return false if grid[i][y] + grid[i+1][y] + grid[i+2][y] != sum
        end
        return false if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != sum
        return false if grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] != sum
        true
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def numMagicSquaresInside(grid: Array[Array[Int]]): Int = {
        var count = 0
        val row = grid.length
        val col = grid(0).length
        for (i <- 0 until row - 2) {
            for (j <- 0 until col - 2) {
                if (isMagic(grid, i, j)) {
                    count += 1
                }
            }
        }
        count
    }

    def isMagic(grid: Array[Array[Int]], i: Int, j: Int): Boolean = {
        val nums = for (x <- i until i + 3; y <- j until j + 3) yield grid(x)(y)
        val sortedNums = nums.sorted
        if (!sortedNums.sameElements((1 to 9).toList)) {
            return false
        }
        val sum = grid(i)(j) + grid(i)(j + 1) + grid(i)(j + 2)
        for (x <- i until i + 3) {
            if (grid(x)(j) + grid(x)(j + 1) + grid(x)(j + 2) != sum) {
                return false
            }
        }
        for (y <- j until j + 3) {
            if (grid(i)(y) + grid(i + 1)(y) + grid(i + 2)(y) != sum) {
                return false
            }
        }
        if (grid(i)(j) + grid(i + 1)(j + 1) + grid(i + 2)(j + 2) != sum) {
            return false
        }
        if (grid(i)(j + 2) + grid(i + 1)(j + 1) + grid(i + 2)(j) != sum) {
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
struct Solution;

impl Solution {
    pub fn num_magic_squares_inside(grid: Vec<Vec<i32>>) -> i32 {
        let mut count = 0;
        let row = grid.len();
        let col = grid[0].len();
        for i in 0..row - 2 {
            for j in 0..col - 2 {
                if Solution::is_magic(&grid, i, j) {
                    count += 1;
                }
            }
        }
        count
    }

    pub fn is_magic(grid: &Vec<Vec<i32>>, i: usize, j: usize) -> bool {
        let mut nums: Vec<i32> = Vec::new();
        for x in i..i + 3 {
            for y in j..j + 3 {
                nums.push(grid[x][y]);
            }
        }
        nums.sort_unstable();
        for k in 0..9 {
            if nums[k as usize] != (k + 1) as i32 {
                return false;
            }
        }
        let sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2];
        for x in i..i + 3 {
            if grid[x][j] + grid[x][j + 1] + grid[x][j + 2] != sum {
                return false;
            }
        }
        for y in j..j + 3 {
            if grid[i][y] + grid[i + 1][y] + grid[i + 2][y] != sum {
                return false;
            }
        }
        if grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != sum {
            return false;
        }
        if grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != sum {
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
(define (num-magic-squares-inside grid)
    (let ((count 0)
          (row (length grid))
          (col (length (car grid))))
        (for ((i (range 0 (- row 2))))
            (for ((j (range 0 (- col 2))))
                (when (is-magic grid i j)
                    (set! count (+ count 1)))))
        count)

(define (is-magic grid i j)
    (let ((nums (for*/list ((x (range i (+ i 3)))
                             (y (range j (+ j 3))))
                        (list-ref (list-ref grid x) y))))
        (and (= (sort nums) (range 1 10))
             (= (apply + (take nums 3))
                (apply + (take (drop nums 3) 3))
                (apply + (take (drop nums 6) 3))
                (apply + (list-ref nums 0)
                              (list-ref nums 4)
                              (list-ref nums 8))
                (apply + (list-ref nums 2)
                              (list-ref nums 4)
                              (list-ref nums 6))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
num_magic_squares_inside(Grid) ->
    length([1 || I <- lists:seq(0, length(Grid) - 3),
                   J <- lists:seq(0, length(hd(Grid)) - 3),
                   is_magic(Grid, I, J)]).

is_magic(Grid, I, J) ->
    lists:sort([element(X, Y, Grid) || X <- lists:seq(I, I + 2),
                                        Y <- lists:seq(J, J + 2)]) = lists:seq(1, 9)
    andalso
    lists:foldl(fun({X, Y}, Sum) -> element(X, Y, Grid) + Sum end, 0,
                [{I, J}, {I, J + 1}, {I, J + 2}]) =
    lists:foldl(fun({X, Y}, Sum) -> element(X, Y, Grid) + Sum end, 0,
                [{I + 1, J}, {I + 1, J + 1}, {I + 1, J + 2}])
    andalso
    lists:foldl(fun({X, Y}, Sum) -> element(X, Y, Grid) + Sum end, 0,
                [{I + 2, J}, {I + 2, J + 1}, {I + 2, J + 2}])
    andalso
    element(I, J, Grid) + element(I + 1, J + 1, Grid) + element(I + 2, J + 2, Grid) =
    element(I, J + 2, Grid) + element(I + 1, J + 1, Grid) + element(I + 2, J, Grid).

element(X, Y, Grid) ->
    element(Y + 1, lists:nth(X + 1, Grid)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def num_magic_squares_inside(grid) do
        count = 0
        row = length(grid)
        col = length(Enum.at(grid, 0))
        for i <- 0..row-3 do
            for j <- 0..col-3 do
                if is_magic(grid, i, j) do
                    count = count + 1
                end
            end
        end
        count
    end

    def is_magic(grid, i, j) do
        nums = for x <- i..i+2, y <- j..j+2, do: Enum.at(Enum.at(grid, x), y)
        sorted_nums = Enum.sort(nums)
        if sorted_nums != Enum.to_list(1..9) do
            false
        else
            sum = Enum.at(Enum.at(grid, i), j) + Enum.at(Enum.at(grid, i), j+1) + Enum.at(Enum.at(grid, i), j+2)
            for x <- i..i+2 do
                if Enum.at(Enum.at(grid, x), j) + Enum.at(Enum.at(grid, x), j+1) + Enum.at(Enum.at(grid, x), j+2) != sum do
                    false
                end
            end
            for y <- j..j+2 do
                if Enum.at(Enum.at(grid, i), y) + Enum.at(Enum.at(grid, i+1), y) + Enum.at(Enum.at(grid, i+2), y) != sum do
                    false
                end
            end
            if Enum.at(Enum.at(grid, i), j) + Enum.at(Enum.at(grid, i+1), j+1) + Enum.at(Enum.at(grid, i+2), j+2) != sum do
                false
            end
            if Enum.at(Enum.at(grid, i), j+2) + Enum.at(Enum.at(grid, i+1), j+1) + Enum.at(Enum.at(grid, i+2), j) != sum do
                false
            end
            true
        end
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(row * col) where row and col are the dimensions of the grid. This is because we are iterating over each cell in the grid once to consider it as the top-left cell of a potential 3x3 subgrid. For each subgrid, we perform a constant amount of work to check if it is a magic square.

- **Space Complexity:** O(1) because we are using a constant amount of space to store the count of magic squares and the sums of rows, columns, and diagonals. We are not using any data structures that scale with the size of the input grid.

</div>
</details>
