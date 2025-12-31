---
layout: post
title: "Last Day Where You Can Still Cross"
date: 2025-12-31 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Binary Search", "Depth-First Search", "Breadth-First Search", "Union Find", "Matrix"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/last-day-where-you-can-still-cross/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <queue>\n#include <utility>\n\nclass Solution\
        \ {\npublic:\n    bool canCross(int row, int col, int day_num, const std::vector<std::vector<int>>&\
        \ cells) {\n        std::vector<std::vector<bool>> grid(row, std::vector<bool>(col,\
        \ false)); // false for land, true for water\n        for (int i = 0; i < day_num;\
        \ ++i) {\n            grid[cells[i][0] - 1][cells[i][1] - 1] = true; // Mark\
        \ as water\n        }\n\n        std::queue<std::pair<int, int>> q;\n      \
        \  std::vector<std::vector<bool>> visited(row, std::vector<bool>(col, false));\n\
        \n        // Add all land cells in the top row to the queue\n        for (int\
        \ c = 0; c < col; ++c) {\n            if (!grid[0][c]) { // If it's land\n \
        \               q.push({0, c});\n                visited[0][c] = true;\n   \
        \         }\n        }\n\n        int dr[] = {-1, 1, 0, 0};\n        int dc[]\
        \ = {0, 0, -1, 1};\n\n        while (!q.empty()) {\n            std::pair<int,\
        \ int> curr = q.front();\n            q.pop();\n            int r = curr.first;\n\
        \            int c = curr.second;\n\n            if (r == row - 1) { // Reached\
        \ the bottom row\n                return true;\n            }\n\n          \
        \  for (int i = 0; i < 4; ++i) {\n                int nr = r + dr[i];\n    \
        \            int nc = c + dc[i];\n\n                if (nr >= 0 && nr < row\
        \ && nc >= 0 && nc < col &&\n                    !grid[nr][nc] && !visited[nr][nc])\
        \ {\n                    visited[nr][nc] = true;\n                    q.push({nr,\
        \ nc});\n                }\n            }\n        }\n\n        return false;\n\
        \    }\n\n    int latestDayToCross(int row, int col, std::vector<std::vector<int>>&\
        \ cells) {\n        int low = 1;\n        int high = cells.size(); // Max day\
        \ is when all cells are flooded\n        int ans = 0;\n\n        while (low\
        \ <= high) {\n            int mid = low + (high - low) / 2;\n            if\
        \ (canCross(row, col, mid, cells)) {\n                ans = mid;\n         \
        \       low = mid + 1; // Try a later day\n            } else {\n          \
        \      high = mid - 1; // Must be an earlier day\n            }\n        }\n\
        \n        return ans;\n    }\n};"
      java: "import java.util.LinkedList;\nimport java.util.Queue;\nimport java.util.List;\n\
        \nclass Solution {\n    private boolean canCross(int row, int col, int dayNum,\
        \ List<List<Integer>> cells) {\n        boolean[][] grid = new boolean[row][col];\
        \ // false for land, true for water\n        for (int i = 0; i < dayNum; i++)\
        \ {\n            grid[cells.get(i).get(0) - 1][cells.get(i).get(1) - 1] = true;\
        \ // Mark as water\n        }\n\n        Queue<int[]> q = new LinkedList<>();\n\
        \        boolean[][] visited = new boolean[row][col];\n\n        // Add all\
        \ land cells in the top row to the queue\n        for (int c = 0; c < col; c++)\
        \ {\n            if (!grid[0][c]) { // If it's land\n                q.offer(new\
        \ int[]{0, c});\n                visited[0][c] = true;\n            }\n    \
        \    }\n\n        int[] dr = {-1, 1, 0, 0};\n        int[] dc = {0, 0, -1, 1};\n\
        \n        while (!q.isEmpty()) {\n            int[] curr = q.poll();\n     \
        \       int r = curr[0];\n            int c = curr[1];\n\n            if (r\
        \ == row - 1) { // Reached the bottom row\n                return true;\n  \
        \          }\n\n            for (int i = 0; i < 4; i++) {\n                int\
        \ nr = r + dr[i];\n                int nc = c + dc[i];\n\n                if\
        \ (nr >= 0 && nr < row && nc >= 0 && nc < col &&\n                    !grid[nr][nc]\
        \ && !visited[nr][nc]) {\n                    visited[nr][nc] = true;\n    \
        \                q.offer(new int[]{nr, nc});\n                }\n          \
        \  }\n        }\n\n        return false;\n    }\n\n    public int latestDayToCross(int\
        \ row, int col, List<List<Integer>> cells) {\n        int low = 1;\n       \
        \ int high = cells.size(); // Max day is when all cells are flooded\n      \
        \  int ans = 0;\n\n        while (low <= high) {\n            int mid = low\
        \ + (high - low) / 2;\n            if (canCross(row, col, mid, cells)) {\n \
        \               ans = mid;\n                low = mid + 1; // Try a later day\n\
        \            } else {\n                high = mid - 1; // Must be an earlier\
        \ day\n            }\n        }\n\n        return ans;\n    }\n}"
      python: "import collections\nfrom typing import List\n\nclass Solution:\n    def\
        \ latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:\n\
        \n        def can_cross(day_num: int) -> bool:\n            # Create a grid\
        \ representing the state on day_num\n            # True for water, False for\
        \ land\n            grid = [[False] * col for _ in range(row)]\n           \
        \ for i in range(day_num):\n                r, c = cells[i][0] - 1, cells[i][1]\
        \ - 1 # Convert to 0-based\n                grid[r][c] = True # Mark as water\n\
        \n            # BFS to check connectivity\n            q = collections.deque()\n\
        \            visited = [[False] * col for _ in range(row)]\n\n            #\
        \ Add all land cells in the top row to the queue\n            for c_idx in range(col):\n\
        \                if not grid[0][c_idx]: # If it's land\n                   \
        \ q.append((0, c_idx))\n                    visited[0][c_idx] = True\n\n   \
        \         # Directions for BFS\n            dr = [-1, 1, 0, 0]\n           \
        \ dc = [0, 0, -1, 1]\n\n            while q:\n                r, c = q.popleft()\n\
        \n                if r == row - 1: # Reached the bottom row\n              \
        \      return True\n\n                for i in range(4):\n                 \
        \   nr, nc = r + dr[i], c + dc[i]\n\n                    # Check bounds\n  \
        \                  if 0 <= nr < row and 0 <= nc < col:\n                   \
        \     # If it's land and not visited\n                        if not grid[nr][nc]\
        \ and not visited[nr][nc]:\n                            visited[nr][nc] = True\n\
        \                            q.append((nr, nc))\n\n            return False\
        \ # No path found\n\n        # Binary search for the latest day\n        low\
        \ = 1\n        high = len(cells) # Max day is when all cells are flooded\n \
        \       ans = 0\n\n        while low <= high:\n            mid = low + (high\
        \ - low) // 2\n            if can_cross(mid):\n                ans = mid\n \
        \               low = mid + 1 # Try a later day\n            else:\n       \
        \         high = mid - 1 # Must be an earlier day\n\n        return ans"
      python3: "import collections\nfrom typing import List\n\nclass Solution:\n   \
        \ def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) ->\
        \ int:\n\n        def can_cross(day_num: int) -> bool:\n            # Create\
        \ a grid representing the state on day_num\n            # True for water, False\
        \ for land\n            grid = [[False] * col for _ in range(row)]\n       \
        \     for i in range(day_num):\n                r, c = cells[i][0] - 1, cells[i][1]\
        \ - 1 # Convert to 0-based\n                grid[r][c] = True # Mark as water\n\
        \n            # BFS to check connectivity\n            q = collections.deque()\n\
        \            visited = [[False] * col for _ in range(row)]\n\n            #\
        \ Add all land cells in the top row to the queue\n            for c_idx in range(col):\n\
        \                if not grid[0][c_idx]: # If it's land\n                   \
        \ q.append((0, c_idx))\n                    visited[0][c_idx] = True\n\n   \
        \         # Directions for BFS\n            dr = [-1, 1, 0, 0]\n           \
        \ dc = [0, 0, -1, 1]\n\n            while q:\n                r, c = q.popleft()\n\
        \n                if r == row - 1: # Reached the bottom row\n              \
        \      return True\n\n                for i in range(4):\n                 \
        \   nr, nc = r + dr[i], c + dc[i]\n\n                    # Check bounds\n  \
        \                  if 0 <= nr < row and 0 <= nc < col:\n                   \
        \     # If it's land and not visited\n                        if not grid[nr][nc]\
        \ and not visited[nr][nc]:\n                            visited[nr][nc] = True\n\
        \                            q.append((nr, nc))\n\n            return False\
        \ # No path found\n\n        # Binary search for the latest day\n        low\
        \ = 1\n        high = len(cells) # Max day is when all cells are flooded\n \
        \       ans = 0\n\n        while low <= high:\n            mid = low + (high\
        \ - low) // 2\n            if can_cross(mid):\n                ans = mid\n \
        \               low = mid + 1 # Try a later day\n            else:\n       \
        \         high = mid - 1 # Must be an earlier day\n\n        return ans"
      c: "#include <stdlib.h>\n#include <stdbool.h>\n#include <string.h>\n\n// Structure\
        \ to represent a cell coordinate\ntypedef struct {\n    int r;\n    int c;\n\
        } Cell;\n\n// Function to check if a path exists on a given day\nbool canCross(int\
        \ row, int col, int day_num, int** cells) {\n    // Dynamically allocate grid\
        \ and initialize to false (land)\n    bool* grid_flat = (bool*)calloc(row *\
        \ col, sizeof(bool)); // false for land, true for water\n    if (grid_flat ==\
        \ NULL) return false; // Handle allocation failure\n\n    for (int i = 0; i\
        \ < day_num; ++i) {\n        int r_idx = cells[i][0] - 1;\n        int c_idx\
        \ = cells[i][1] - 1;\n        grid_flat[r_idx * col + c_idx] = true; // Mark\
        \ as water\n    }\n\n    // Queue for BFS (using a simple array as a circular\
        \ buffer)\n    Cell* q_buffer = (Cell*)malloc(row * col * sizeof(Cell));\n \
        \   if (q_buffer == NULL) {\n        free(grid_flat);\n        return false;\n\
        \    }\n    int q_head = 0;\n    int q_tail = 0;\n\n    // Visited array\n \
        \   bool* visited_flat = (bool*)calloc(row * col, sizeof(bool));\n    if (visited_flat\
        \ == NULL) {\n        free(grid_flat);\n        free(q_buffer);\n        return\
        \ false;\n    }\n\n    // Add all land cells in the top row to the queue\n \
        \   for (int c = 0; c < col; ++c) {\n        if (!grid_flat[0 * col + c]) {\
        \ // If it's land\n            q_buffer[q_tail++] = (Cell){0, c};\n        \
        \    visited_flat[0 * col + c] = true;\n        }\n    }\n\n    int dr[] = {-1,\
        \ 1, 0, 0};\n    int dc[] = {0, 0, -1, 1};\n\n    while (q_head < q_tail) {\n\
        \        Cell curr = q_buffer[q_head++];\n        int r = curr.r;\n        int\
        \ c = curr.c;\n\n        if (r == row - 1) { // Reached the bottom row\n   \
        \         free(grid_flat);\n            free(q_buffer);\n            free(visited_flat);\n\
        \            return true;\n        }\n\n        for (int i = 0; i < 4; ++i)\
        \ {\n            int nr = r + dr[i];\n            int nc = c + dc[i];\n\n  \
        \          if (nr >= 0 && nr < row && nc >= 0 && nc < col &&\n             \
        \   !grid_flat[nr * col + nc] && !visited_flat[nr * col + nc]) {\n         \
        \       visited_flat[nr * col + nc] = true;\n                q_buffer[q_tail++]\
        \ = (Cell){nr, nc};\n            }\n        }\n    }\n\n    free(grid_flat);\n\
        \    free(q_buffer);\n    free(visited_flat);\n    return false;\n}\n\nint latestDayToCross(int\
        \ row, int col, int** cells, int cellsSize, int* cellsColSize) {\n    int low\
        \ = 1;\n    int high = cellsSize;\n    int ans = 0;\n\n    while (low <= high)\
        \ {\n        int mid = low + (high - low) / 2;\n        if (canCross(row, col,\
        \ mid, cells)) {\n            ans = mid;\n            low = mid + 1;\n     \
        \   } else {\n            high = mid - 1;\n        }\n    }\n\n    return ans;\n\
        }"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    private bool CanCross(int row, int col, int dayNum, int[][] cells)\
        \ {\n        bool[][] grid = new bool[row][]; // false for land, true for water\n\
        \        for (int i = 0; i < row; i++) {\n            grid[i] = new bool[col];\n\
        \        }\n\n        for (int i = 0; i < dayNum; i++) {\n            grid[cells[i][0]\
        \ - 1][cells[i][1] - 1] = true; // Mark as water\n        }\n\n        Queue<(int\
        \ r, int c)> q = new Queue<(int r, int c)>();\n        bool[][] visited = new\
        \ bool[row][];\n        for (int i = 0; i < row; i++) {\n            visited[i]\
        \ = new bool[col];\n        }\n\n        // Add all land cells in the top row\
        \ to the queue\n        for (int c = 0; c < col; c++) {\n            if (!grid[0][c])\
        \ { // If it's land\n                q.Enqueue((0, c));\n                visited[0][c]\
        \ = true;\n            }\n        }\n\n        int[] dr = {-1, 1, 0, 0};\n \
        \       int[] dc = {0, 0, -1, 1};\n\n        while (q.Count > 0) {\n       \
        \     (int r, int c) curr = q.Dequeue();\n\n            if (curr.r == row -\
        \ 1) { // Reached the bottom row\n                return true;\n           \
        \ }\n\n            for (int i = 0; i < 4; i++) {\n                int nr = curr.r\
        \ + dr[i];\n                int nc = curr.c + dc[i];\n\n                if (nr\
        \ >= 0 && nr < row && nc >= 0 && nc < col &&\n                    !grid[nr][nc]\
        \ && !visited[nr][nc]) {\n                    visited[nr][nc] = true;\n    \
        \                q.Enqueue((nr, nc));\n                }\n            }\n  \
        \      }\n\n        return false;\n    }\n\n    public int LatestDayToCross(int\
        \ row, int col, int[][] cells) {\n        int low = 1;\n        int high = cells.Length;\
        \ // Max day is when all cells are flooded\n        int ans = 0;\n\n       \
        \ while (low <= high) {\n            int mid = low + (high - low) / 2;\n   \
        \         if (CanCross(row, col, mid, cells)) {\n                ans = mid;\n\
        \                low = mid + 1; // Try a later day\n            } else {\n \
        \               high = mid - 1; // Must be an earlier day\n            }\n \
        \       }\n\n        return ans;\n    }\n}"
      javascript: "/**\n * @param {number} row\n * @param {number} col\n * @param {number[][]}\
        \ cells\n * @return {number}\n */\nvar latestDayToCross = function(row, col,\
        \ cells) {\n\n    const canCross = (dayNum) => {\n        // Create a grid representing\
        \ the state on dayNum\n        // false for land, true for water\n        const\
        \ grid = Array(row).fill(0).map(() => Array(col).fill(false));\n        for\
        \ (let i = 0; i < dayNum; i++) {\n            const r = cells[i][0] - 1;\n \
        \           const c = cells[i][1] - 1;\n            grid[r][c] = true; // Mark\
        \ as water\n        }\n\n        // BFS to check connectivity\n        const\
        \ q = [];\n        const visited = Array(row).fill(0).map(() => Array(col).fill(false));\n\
        \n        // Add all land cells in the top row to the queue\n        for (let\
        \ c = 0; c < col; c++) {\n            if (!grid[0][c]) { // If it's land\n \
        \               q.push([0, c]);\n                visited[0][c] = true;\n   \
        \         }\n        }\n\n        // Directions for BFS\n        const dr =\
        \ [-1, 1, 0, 0];\n        const dc = [0, 0, -1, 1];\n\n        let head = 0;\n\
        \        while (head < q.length) {\n            const [r, c] = q[head++];\n\n\
        \            if (r === row - 1) { // Reached the bottom row\n              \
        \  return true;\n            }\n\n            for (let i = 0; i < 4; i++) {\n\
        \                const nr = r + dr[i];\n                const nc = c + dc[i];\n\
        \n                // Check bounds\n                if (nr >= 0 && nr < row &&\
        \ nc >= 0 && nc < col) {\n                    // If it's land and not visited\n\
        \                    if (!grid[nr][nc] && !visited[nr][nc]) {\n            \
        \            visited[nr][nc] = true;\n                        q.push([nr, nc]);\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    return false; // No path found\n    };\n\n    // Binary search for the\
        \ latest day\n    let low = 1;\n    let high = cells.length; // Max day is when\
        \ all cells are flooded\n    let ans = 0;\n\n    while (low <= high) {\n   \
        \     const mid = Math.floor(low + (high - low) / 2);\n        if (canCross(mid))\
        \ {\n            ans = mid;\n            low = mid + 1; // Try a later day\n\
        \        } else {\n            high = mid - 1; // Must be an earlier day\n \
        \       }\n    }\n\n    return ans;\n};"
      typescript: "function latestDayToCross(row: number, col: number, cells: number[][]):\
        \ number {\n\n    const canCross = (dayNum: number): boolean => {\n        //\
        \ Create a grid representing the state on dayNum\n        // false for land,\
        \ true for water\n        const grid: boolean[][] = Array(row).fill(0).map(()\
        \ => Array(col).fill(false));\n        for (let i = 0; i < dayNum; i++) {\n\
        \            const r = cells[i][0] - 1;\n            const c = cells[i][1] -\
        \ 1;\n            grid[r][c] = true; // Mark as water\n        }\n\n       \
        \ // BFS to check connectivity\n        const q: [number, number][] = [];\n\
        \        const visited: boolean[][] = Array(row).fill(0).map(() => Array(col).fill(false));\n\
        \n        // Add all land cells in the top row to the queue\n        for (let\
        \ c = 0; c < col; c++) {\n            if (!grid[0][c]) { // If it's land\n \
        \               q.push([0, c]);\n                visited[0][c] = true;\n   \
        \         }\n        }\n\n        // Directions for BFS\n        const dr =\
        \ [-1, 1, 0, 0];\n        const dc = [0, 0, -1, 1];\n\n        let head = 0;\n\
        \        while (head < q.length) {\n            const [r, c] = q[head++];\n\n\
        \            if (r === row - 1) { // Reached the bottom row\n              \
        \  return true;\n            }\n\n            for (let i = 0; i < 4; i++) {\n\
        \                const nr = r + dr[i];\n                const nc = c + dc[i];\n\
        \n                // Check bounds\n                if (nr >= 0 && nr < row &&\
        \ nc >= 0 && nc < col) {\n                    // If it's land and not visited\n\
        \                    if (!grid[nr][nc] && !visited[nr][nc]) {\n            \
        \            visited[nr][nc] = true;\n                        q.push([nr, nc]);\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    return false; // No path found\n    };\n\n    // Binary search for the\
        \ latest day\n    let low = 1;\n    let high = cells.length; // Max day is when\
        \ all cells are flooded\n    let ans = 0;\n\n    while (low <= high) {\n   \
        \     const mid = Math.floor(low + (high - low) / 2);\n        if (canCross(mid))\
        \ {\n            ans = mid;\n            low = mid + 1; // Try a later day\n\
        \        } else {\n            high = mid - 1; // Must be an earlier day\n \
        \       }\n    }\n\n    return ans;\n};"
      php: "<?php\nclass Solution {\n\n    /**\n     * @param Integer $row\n     * @param\
        \ Integer $col\n     * @param Integer[][] $cells\n     * @return Integer\n \
        \    */\n    function latestDayToCross($row, $col, $cells) {\n\n        $canCross\
        \ = function($dayNum) use ($row, $col, $cells) {\n            // Create a grid\
        \ representing the state on dayNum\n            // false for land, true for\
        \ water\n            $grid = array_fill(0, $row, array_fill(0, $col, false));\n\
        \            for ($i = 0; $i < $dayNum; $i++) {\n                $r = $cells[$i][0]\
        \ - 1;\n                $c = $cells[$i][1] - 1;\n                $grid[$r][$c]\
        \ = true; // Mark as water\n            }\n\n            // BFS to check connectivity\n\
        \            $q = new SplQueue();\n            $visited = array_fill(0, $row,\
        \ array_fill(0, $col, false));\n\n            // Add all land cells in the top\
        \ row to the queue\n            for ($c_idx = 0; $c_idx < $col; $c_idx++) {\n\
        \                if (!$grid[0][$c_idx]) { // If it's land\n                \
        \    $q->enqueue([0, $c_idx]);\n                    $visited[0][$c_idx] = true;\n\
        \                }\n            }\n\n            // Directions for BFS\n   \
        \         $dr = [-1, 1, 0, 0];\n            $dc = [0, 0, -1, 1];\n\n       \
        \     while (!$q->isEmpty()) {\n                list($r, $c) = $q->dequeue();\n\
        \n                if ($r === $row - 1) { // Reached the bottom row\n       \
        \             return true;\n                }\n\n                for ($i = 0;\
        \ $i < 4; $i++) {\n                    $nr = $r + $dr[$i];\n               \
        \     $nc = $c + $dc[$i];\n\n                    // Check bounds\n         \
        \           if ($nr >= 0 && $nr < $row && $nc >= 0 && $nc < $col) {\n      \
        \                  // If it's land and not visited\n                       \
        \ if (!$grid[$nr][$nc] && !$visited[$nr][$nc]) {\n                         \
        \   $visited[$nr][$nc] = true;\n                            $q->enqueue([$nr,\
        \ $nc]);\n                        }\n                    }\n               \
        \ }\n            }\n\n            return false; // No path found\n        };\n\
        \n        // Binary search for the latest day\n        $low = 1;\n        $high\
        \ = count($cells); // Max day is when all cells are flooded\n        $ans =\
        \ 0;\n\n        while ($low <= $high) {\n            $mid = floor($low + ($high\
        \ - $low) / 2);\n            if ($canCross($mid)) {\n                $ans =\
        \ $mid;\n                $low = $mid + 1; // Try a later day\n            }\
        \ else {\n                $high = $mid - 1; // Must be an earlier day\n    \
        \        }\n        }\n\n        return $ans;\n    }\n}\n?>"
      swift: "import Foundation\n\nclass Solution {\n    private func canCross(_ row:\
        \ Int, _ col: Int, _ dayNum: Int, _ cells: [[Int]]) -> Bool {\n        var grid\
        \ = Array(repeating: Array(repeating: false, count: col), count: row) // false\
        \ for land, true for water\n        for i in 0..<dayNum {\n            grid[cells[i][0]\
        \ - 1][cells[i][1] - 1] = true // Mark as water\n        }\n\n        var q\
        \ = [(Int, Int)]()\n        var visited = Array(repeating: Array(repeating:\
        \ false, count: col), count: row)\n\n        // Add all land cells in the top\
        \ row to the queue\n        for c in 0..<col {\n            if !grid[0][c] {\
        \ // If it's land\n                q.append((0, c))\n                visited[0][c]\
        \ = true\n            }\n        }\n\n        let dr = [-1, 1, 0, 0]\n     \
        \   let dc = [0, 0, -1, 1]\n\n        var head = 0\n        while head < q.count\
        \ {\n            let (r, c) = q[head]\n            head += 1\n\n           \
        \ if r == row - 1 { // Reached the bottom row\n                return true\n\
        \            }\n\n            for i in 0..<4 {\n                let nr = r +\
        \ dr[i]\n                let nc = c + dc[i]\n\n                if nr >= 0 &&\
        \ nr < row && nc >= 0 && nc < col &&\n                    !grid[nr][nc] && !visited[nr][nc]\
        \ {\n                    visited[nr][nc] = true\n                    q.append((nr,\
        \ nc))\n                }\n            }\n        }\n\n        return false\n\
        \    }\n\n    func latestDayToCross(_ row: Int, _ col: Int, _ cells: [[Int]])\
        \ -> Int {\n        var low = 1\n        var high = cells.count // Max day is\
        \ when all cells are flooded\n        var ans = 0\n\n        while low <= high\
        \ {\n            let mid = low + (high - low) / 2\n            if canCross(row,\
        \ col, mid, cells) {\n                ans = mid\n                low = mid +\
        \ 1 // Try a later day\n            } else {\n                high = mid - 1\
        \ // Must be an earlier day\n            }\n        }\n\n        return ans\n\
        \    }\n}"
      kotlin: "import java.util.LinkedList\nimport java.util.Queue\n\nclass Solution\
        \ {\n    private fun canCross(row: Int, col: Int, dayNum: Int, cells: Array<IntArray>):\
        \ Boolean {\n        val grid = Array(row) { BooleanArray(col) { false } } //\
        \ false for land, true for water\n        for (i in 0 until dayNum) {\n    \
        \        grid[cells[i][0] - 1][cells[i][1] - 1] = true // Mark as water\n  \
        \      }\n\n        val q: Queue<Pair<Int, Int>> = LinkedList()\n        val\
        \ visited = Array(row) { BooleanArray(col) { false } }\n\n        // Add all\
        \ land cells in the top row to the queue\n        for (c in 0 until col) {\n\
        \            if (!grid[0][c]) { // If it's land\n                q.offer(Pair(0,\
        \ c))\n                visited[0][c] = true\n            }\n        }\n\n  \
        \      val dr = intArrayOf(-1, 1, 0, 0)\n        val dc = intArrayOf(0, 0, -1,\
        \ 1)\n\n        while (q.isNotEmpty()) {\n            val (r, c) = q.poll()\n\
        \n            if (r == row - 1) { // Reached the bottom row\n              \
        \  return true\n            }\n\n            for (i in 0 until 4) {\n      \
        \          val nr = r + dr[i]\n                val nc = c + dc[i]\n\n      \
        \          if (nr >= 0 && nr < row && nc >= 0 && nc < col &&\n             \
        \       !grid[nr][nc] && !visited[nr][nc]) {\n                    visited[nr][nc]\
        \ = true\n                    q.offer(Pair(nr, nc))\n                }\n   \
        \         }\n        }\n\n        return false\n    }\n\n    fun latestDayToCross(row:\
        \ Int, col: Int, cells: Array<IntArray>): Int {\n        var low = 1\n     \
        \   var high = cells.size // Max day is when all cells are flooded\n       \
        \ var ans = 0\n\n        while (low <= high) {\n            val mid = low +\
        \ (high - low) / 2\n            if (canCross(row, col, mid, cells)) {\n    \
        \            ans = mid\n                low = mid + 1 // Try a later day\n \
        \           } else {\n                high = mid - 1 // Must be an earlier day\n\
        \            }\n        }\n\n        return ans\n    }\n}"
      dart: "import 'dart:collection';\n\nclass Solution {\n  bool _canCross(int row,\
        \ int col, int dayNum, List<List<int>> cells) {\n    List<List<bool>> grid =\
        \ List.generate(row, (_) => List.filled(col, false)); // false for land, true\
        \ for water\n    for (int i = 0; i < dayNum; i++) {\n      grid[cells[i][0]\
        \ - 1][cells[i][1] - 1] = true; // Mark as water\n    }\n\n    Queue<List<int>>\
        \ q = Queue<List<int>>();\n    List<List<bool>> visited = List.generate(row,\
        \ (_) => List.filled(col, false));\n\n    // Add all land cells in the top row\
        \ to the queue\n    for (int c = 0; c < col; c++) {\n      if (!grid[0][c])\
        \ { // If it's land\n        q.add([0, c]);\n        visited[0][c] = true;\n\
        \      }\n    }\n\n    List<int> dr = [-1, 1, 0, 0];\n    List<int> dc = [0,\
        \ 0, -1, 1];\n\n    while (q.isNotEmpty) {\n      List<int> curr = q.removeFirst();\n\
        \      int r = curr[0];\n      int c = curr[1];\n\n      if (r == row - 1) {\
        \ // Reached the bottom row\n        return true;\n      }\n\n      for (int\
        \ i = 0; i < 4; i++) {\n        int nr = r + dr[i];\n        int nc = c + dc[i];\n\
        \n        if (nr >= 0 && nr < row && nc >= 0 && nc < col &&\n            !grid[nr][nc]\
        \ && !visited[nr][nc]) {\n          visited[nr][nc] = true;\n          q.add([nr,\
        \ nc]);\n        }\n      }\n    }\n\n    return false;\n  }\n\n  int latestDayToCross(int\
        \ row, int col, List<List<int>> cells) {\n    int low = 1;\n    int high = cells.length;\
        \ // Max day is when all cells are flooded\n    int ans = 0;\n\n    while (low\
        \ <= high) {\n      int mid = low + (high - low) ~/ 2;\n      if (_canCross(row,\
        \ col, mid, cells)) {\n        ans = mid;\n        low = mid + 1; // Try a later\
        \ day\n      } else {\n        high = mid - 1; // Must be an earlier day\n \
        \     }\n    }\n\n    return ans;\n  }\n}"
      go: "package main\n\nimport (\n\t\"container/list\"\n)\n\ntype Cell struct {\n\
        \tr int\n\tc int\n}\n\nfunc canCross(row, col, dayNum int, cells [][]int) bool\
        \ {\n\tgrid := make([][]bool, row)\n\tfor i := range grid {\n\t\tgrid[i] = make([]bool,\
        \ col) // false for land, true for water\n\t}\n\n\tfor i := 0; i < dayNum; i++\
        \ {\n\t\tgrid[cells[i][0]-1][cells[i][1]-1] = true // Mark as water\n\t}\n\n\
        \tq := list.New()\n\tvisited := make([][]bool, row)\n\tfor i := range visited\
        \ {\n\t\tvisited[i] = make([]bool, col)\n\t}\n\n\t// Add all land cells in the\
        \ top row to the queue\n\tfor c := 0; c < col; c++ {\n\t\tif !grid[0][c] { //\
        \ If it's land\n\t\t\tq.PushBack(Cell{0, c})\n\t\t\tvisited[0][c] = true\n\t\
        \t}\n\t}\n\n\tdr := []int{-1, 1, 0, 0}\n\tdc := []int{0, 0, -1, 1}\n\n\tfor\
        \ q.Len() > 0 {\n\t\telem := q.Front()\n\t\tq.Remove(elem)\n\t\tcurr := elem.Value.(Cell)\n\
        \t\tr := curr.r\n\t\tc := curr.c\n\n\t\tif r == row-1 { // Reached the bottom\
        \ row\n\t\t\treturn true\n\t\t}\n\n\t\tfor i := 0; i < 4; i++ {\n\t\t\tnr :=\
        \ r + dr[i]\n\t\t\tnc := c + dc[i]\n\n\t\t\tif nr >= 0 && nr < row && nc >=\
        \ 0 && nc < col &&\n\t\t\t\t!grid[nr][nc] && !visited[nr][nc] {\n\t\t\t\tvisited[nr][nc]\
        \ = true\n\t\t\t\tq.PushBack(Cell{nr, nc})\n\t\t\t}\n\t\t}\n\t}\n\n\treturn\
        \ false\n}\n\nfunc latestDayToCross(row int, col int, cells [][]int) int {\n\
        \tlow := 1\n\thigh := len(cells) // Max day is when all cells are flooded\n\t\
        ans := 0\n\n\tfor low <= high {\n\t\tmid := low + (high-low)/2\n\t\tif canCross(row,\
        \ col, mid, cells) {\n\t\t\tans = mid\n\t\t\tlow = mid + 1 // Try a later day\n\
        \t\t} else {\n\t\t\thigh = mid - 1 // Must be an earlier day\n\t\t}\n\t}\n\n\
        \treturn ans\n}"
      ruby: "class Solution\n    # @param {Integer} row\n    # @param {Integer} col\n\
        \    # @param {Integer[][]} cells\n    # @return {Integer}\n    def latest_day_to_cross(row,\
        \ col, cells)\n\n        can_cross = lambda do |day_num|\n            # Create\
        \ a grid representing the state on day_num\n            # false for land, true\
        \ for water\n            grid = Array.new(row) { Array.new(col, false) }\n \
        \           (0...day_num).each do |i|\n                r = cells[i][0] - 1\n\
        \                c = cells[i][1] - 1\n                grid[r][c] = true # Mark\
        \ as water\n            end\n\n            # BFS to check connectivity\n   \
        \         q = []\n            visited = Array.new(row) { Array.new(col, false)\
        \ }\n\n            # Add all land cells in the top row to the queue\n      \
        \      (0...col).each do |c_idx|\n                if !grid[0][c_idx] # If it's\
        \ land\n                    q.push([0, c_idx])\n                    visited[0][c_idx]\
        \ = true\n                end\n            end\n\n            # Directions for\
        \ BFS\n            dr = [-1, 1, 0, 0]\n            dc = [0, 0, -1, 1]\n\n  \
        \          head = 0\n            while head < q.length\n                r, c\
        \ = q[head]\n                head += 1\n\n                if r == row - 1 #\
        \ Reached the bottom row\n                    return true\n                end\n\
        \n                (0...4).each do |i|\n                    nr = r + dr[i]\n\
        \                    nc = c + dc[i]\n\n                    # Check bounds\n\
        \                    if nr >= 0 && nr < row && nc >= 0 && nc < col\n       \
        \                 # If it's land and not visited\n                        if\
        \ !grid[nr][nc] && !visited[nr][nc]\n                            visited[nr][nc]\
        \ = true\n                            q.push([nr, nc])\n                   \
        \     end\n                    end\n                end\n            end\n\n\
        \            return false # No path found\n        end\n\n        # Binary search\
        \ for the latest day\n        low = 1\n        high = cells.length # Max day\
        \ is when all cells are flooded\n        ans = 0\n\n        while low <= high\n\
        \            mid = low + (high - low) / 2\n            if can_cross.call(mid)\n\
        \                ans = mid\n                low = mid + 1 # Try a later day\n\
        \            else\n                high = mid - 1 # Must be an earlier day\n\
        \            end\n        end\n\n        return ans\n    end\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def latestDayToCross(row:\
        \ Int, col: Int, cells: Array[Array[Int]]): Int = {\n\n        def canCross(dayNum:\
        \ Int): Boolean = {\n            // Create a grid representing the state on\
        \ dayNum\n            // false for land, true for water\n            val grid:\
        \ Array[Array[Boolean]] = Array.ofDim[Boolean](row, col)\n            for (i\
        \ <- 0 until dayNum) {\n                val r = cells(i)(0) - 1\n          \
        \      val c = cells(i)(1) - 1\n                grid(r)(c) = true // Mark as\
        \ water\n            }\n\n            // BFS to check connectivity\n       \
        \     val q = mutable.Queue[(Int, Int)]()\n            val visited: Array[Array[Boolean]]\
        \ = Array.ofDim[Boolean](row, col)\n\n            // Add all land cells in the\
        \ top row to the queue\n            for (c_idx <- 0 until col) {\n         \
        \       if (!grid(0)(c_idx)) { // If it's land\n                    q.enqueue((0,\
        \ c_idx))\n                    visited(0)(c_idx) = true\n                }\n\
        \            }\n\n            // Directions for BFS\n            val dr = Array(-1,\
        \ 1, 0, 0)\n            val dc = Array(0, 0, -1, 1)\n\n            while (q.nonEmpty)\
        \ {\n                val (r, c) = q.dequeue()\n\n                if (r == row\
        \ - 1) { // Reached the bottom row\n                    return true\n      \
        \          }\n\n                for (i <- 0 until 4) {\n                   \
        \ val nr = r + dr(i)\n                    val nc = c + dc(i)\n\n           \
        \         // Check bounds\n                    if (nr >= 0 && nr < row && nc\
        \ >= 0 && nc < col) {\n                        // If it's land and not visited\n\
        \                        if (!grid(nr)(nc) && !visited(nr)(nc)) {\n        \
        \                    visited(nr)(nc) = true\n                            q.enqueue((nr,\
        \ nc))\n                        }\n                    }\n                }\n\
        \            }\n\n            return false // No path found\n        }\n\n \
        \       // Binary search for the latest day\n        var low = 1\n        var\
        \ high = cells.length // Max day is when all cells are flooded\n        var\
        \ ans = 0\n\n        while (low <= high) {\n            val mid = low + (high\
        \ - low) / 2\n            if (canCross(mid)) {\n                ans = mid\n\
        \                low = mid + 1 // Try a later day\n            } else {\n  \
        \              high = mid - 1 // Must be an earlier day\n            }\n   \
        \     }\n\n        return ans\n    }\n}"
      rust: "use std::collections::VecDeque;\n\nstruct Solution;\n\nimpl Solution {\n\
        \    fn can_cross(row: i32, col: i32, day_num: usize, cells: &Vec<Vec<i32>>)\
        \ -> bool {\n        let mut grid = vec![vec![false; col as usize]; row as usize];\
        \ // false for land, true for water\n        for i in 0..day_num {\n       \
        \     let r = cells[i][0] as usize - 1;\n            let c = cells[i][1] as\
        \ usize - 1;\n            grid[r][c] = true; // Mark as water\n        }\n\n\
        \        let mut q = VecDeque::new();\n        let mut visited = vec![vec![false;\
        \ col as usize]; row as usize];\n\n        // Add all land cells in the top\
        \ row to the queue\n        for c_idx in 0..col {\n            if !grid[0][c_idx\
        \ as usize] { // If it's land\n                q.push_back((0, c_idx));\n  \
        \              visited[0][c_idx as usize] = true;\n            }\n        }\n\
        \n        let dr = [-1, 1, 0, 0];\n        let dc = [0, 0, -1, 1];\n\n     \
        \   while let Some((r, c)) = q.pop_front() {\n            if r == row - 1 {\
        \ // Reached the bottom row\n                return true;\n            }\n\n\
        \            for i in 0..4 {\n                let nr = r + dr[i];\n        \
        \        let nc = c + dc[i];\n\n                if nr >= 0 && nr < row && nc\
        \ >= 0 && nc < col {\n                    if !grid[nr as usize][nc as usize]\
        \ && !visited[nr as usize][nc as usize] {\n                        visited[nr\
        \ as usize][nc as usize] = true;\n                        q.push_back((nr, nc));\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    false // No path found\n    }\n\n    pub fn latest_day_to_cross(row: i32,\
        \ col: i32, cells: Vec<Vec<i32>>) -> i32 {\n        let mut low = 1;\n     \
        \   let mut high = cells.len() as i32; // Max day is when all cells are flooded\n\
        \        let mut ans = 0;\n\n        while low <= high {\n            let mid\
        \ = low + (high - low) / 2;\n            if Self::can_cross(row, col, mid as\
        \ usize, &cells) {\n                ans = mid;\n                low = mid +\
        \ 1; // Try a later day\n            } else {\n                high = mid -\
        \ 1; // Must be an earlier day\n            }\n        }\n\n        ans\n  \
        \  }\n}"
      racket: "#lang racket\n\n(define (latest-day-to-cross row col cells)\n\n  (define\
        \ (can-cross day-num)\n    ;; Create a grid representing the state on day-num\n\
        \    ;; #f for land, #t for water\n    (define grid (make-vector row (make-vector\
        \ col #f)))\n    (for ([i (in-range day-num)])\n      (define cell (vector-ref\
        \ cells i))\n      (define r (- (vector-ref cell 0) 1))\n      (define c (-\
        \ (vector-ref cell 1) 1))\n      (vector-set! (vector-ref grid r) c #t) ; Mark\
        \ as water\n      )\n\n    ;; BFS to check connectivity\n    (define q (make-queue))\n\
        \    (define visited (make-vector row (make-vector col #f)))\n\n    ;; Add all\
        \ land cells in the top row to the queue\n    (for ([c-idx (in-range col)])\n\
        \      (when (not (vector-ref (vector-ref grid 0) c-idx)) ; If it's land\n \
        \       (queue-enqueue! q (list 0 c-idx))\n        (vector-set! (vector-ref\
        \ visited 0) c-idx #t)\n        ))\n\n    ;; Directions for BFS\n    (define\
        \ dr '(-1 1 0 0))\n    (define dc '(0 0 -1 1))\n\n    (let loop ()\n      (when\
        \ (not (queue-empty? q))\n        (define curr (queue-dequeue! q))\n       \
        \ (define r (car curr))\n        (define c (cadr curr))\n\n        (when (=\
        \ r (- row 1)) ; Reached the bottom row\n          (void (queue-clear! q)) ;\
        \ Clear queue to stop loop\n          (error 'can-cross \"Should not reach here\
        \ if true\")) ; This is a hack, will return true below\n\n        (for ([i (in-range\
        \ 4)])\n          (define nr (+ r (list-ref dr i)))\n          (define nc (+\
        \ c (list-ref dc i)))\n\n          ;; Check bounds\n          (when (and (>=\
        \ nr 0) (< nr row) (>= nc 0) (< nc col))\n            ;; If it's land and not\
        \ visited\n            (when (and (not (vector-ref (vector-ref grid nr) nc))\n\
        \                       (not (vector-ref (vector-ref visited nr) nc)))\n   \
        \           (vector-set! (vector-ref visited nr) nc #t)\n              (queue-enqueue!\
        \ q (list nr nc))\n              ))\n          )\n        (loop)\n        ))\n\
        \n    ;; After BFS, check if any bottom row cell was visited\n    (for/or ([c\
        \ (in-range col)])\n      (vector-ref (vector-ref visited (- row 1)) c))\n \
        \   )\n\n  ;; Binary search for the latest day\n  (define low 1)\n  (define\
        \ high (vector-length cells)) ; Max day is when all cells are flooded\n  (define\
        \ ans 0)\n\n  (let loop ( (l low) (h high) (a ans) )\n    (if (<= l h)\n   \
        \     (let* ([mid (+ l (quotient (- h l) 2))])\n          (if (can-cross mid)\n\
        \              (loop (+ mid 1) h mid) ; Try a later day\n              (loop\
        \ l (- mid 1) a)   ; Must be an earlier day\n              ))\n        a))\n\
        \  )\n\n;; Helper for queue (Racket's queue is mutable)\n(define (make-queue)\
        \ (make-mutable-queue))\n(define (queue-enqueue! q item) (mutable-queue-enqueue!\
        \ q item))\n(define (queue-dequeue! q) (mutable-queue-dequeue! q))\n(define\
        \ (queue-empty? q) (mutable-queue-empty? q))\n(define (queue-clear! q) (mutable-queue-clear!\
        \ q))"
      erlang: "-module(solution).\n-export([latest_day_to_cross/3]).\n\nlatest_day_to_cross(Row,\
        \ Col, Cells) ->\n    Low = 1,\n    High = length(Cells),\n    binary_search(Low,\
        \ High, 0, Row, Col, Cells).\n\nbinary_search(Low, High, Ans, Row, Col, Cells)\
        \ when Low =< High ->\n    Mid = Low + (High - Low) div 2,\n    case can_cross(Row,\
        \ Col, Mid, Cells) of\n        true -> binary_search(Mid + 1, High, Mid, Row,\
        \ Col, Cells);\n        false -> binary_search(Low, Mid - 1, Ans, Row, Col,\
        \ Cells)\n    end;\nbinary_search(_, _, Ans, _, _, _) ->\n    Ans.\n\ncan_cross(Row,\
        \ Col, DayNum, Cells) ->\n    Grid = create_grid(Row, Col, DayNum, Cells),\n\
        \n    Q = queue:new(),\n    Visited = create_visited(Row, Col),\n\n    % Add\
        \ all land cells in the top row to the queue\n    {Q1, Visited1} = lists:foldl(\n\
        \        fun(C_idx, {AccQ, AccVisited}) ->\n            case get_grid_val(Grid,\
        \ 0, C_idx, Col) of\n                false -> % If it's land\n             \
        \       NewQ = queue:in({0, C_idx}, AccQ),\n                    NewVisited =\
        \ set_visited(AccVisited, 0, C_idx, Col, true),\n                    {NewQ,\
        \ NewVisited};\n                true ->\n                    {AccQ, AccVisited}\n\
        \            end\n        end, {Q, Visited}, lists:seq(0, Col - 1)),\n\n   \
        \ bfs(Q1, Visited1, Row, Col, Grid).\n\nbfs(Q, Visited, Row, Col, Grid) ->\n\
        \    case queue:out(Q) of\n        {{value, {R, C}}, RestQ} ->\n           \
        \ if R == Row - 1 ->\n                true;\n            true ->\n         \
        \       DR = [-1, 1, 0, 0],\n                DC = [0, 0, -1, 1],\n\n       \
        \         {NewQ, NewVisited} = lists:foldl(\n                    fun(I, {AccQ,\
        \ AccVisited}) ->\n                        NR = R + lists:nth(I + 1, DR),\n\
        \                        NC = C + lists:nth(I + 1, DC),\n\n                \
        \        if NR >= 0 andalso NR < Row andalso NC >= 0 andalso NC < Col ->\n \
        \                           case get_grid_val(Grid, NR, NC, Col) of\n      \
        \                          false -> % If it's land\n                       \
        \             case get_visited(AccVisited, NR, NC, Col) of\n               \
        \                         false ->\n                                       \
        \     NewQ = queue:in({NR, NC}, AccQ),\n                                   \
        \         NewVisited = set_visited(AccVisited, NR, NC, Col, true),\n       \
        \                                     {NewQ, NewVisited};\n                \
        \                        true ->\n                                         \
        \   {AccQ, AccVisited}\n                                    end;\n         \
        \                       true ->\n                                    {AccQ,\
        \ AccVisited}\n                            end;\n                        true\
        \ ->\n                            {AccQ, AccVisited}\n                     \
        \   end\n                    end, {RestQ, Visited}, lists:seq(0, 3)),\n    \
        \            bfs(NewQ, NewVisited, Row, Col, Grid)\n            end;\n     \
        \   {empty, _} ->\n            false\n    end.\n\ncreate_grid(Row, Col, DayNum,\
        \ Cells) ->\n    Grid = array:new([{size, Row * Col}, {fixed, true}, {default,\
        \ false}]),\n    lists:foldl(\n        fun(I, AccGrid) ->\n            Cell\
        \ = lists:nth(I + 1, Cells),\n            R = lists:nth(1, Cell) - 1,\n    \
        \        C = lists:nth(2, Cell) - 1,\n            array:set(R * Col + C, true,\
        \ AccGrid)\n        end, Grid, lists:seq(0, DayNum - 1)).\n\nget_grid_val(Grid,\
        \ R, C, Col) ->\n    array:get(R * Col + C, Grid).\n\ncreate_visited(Row, Col)\
        \ ->\n    array:new([{size, Row * Col}, {fixed, true}, {default, false}]).\n\
        \nget_visited(Visited, R, C, Col) ->\n    array:get(R * Col + C, Visited).\n\
        \nset_visited(Visited, R, C, Col, Val) ->\n    array:set(R * Col + C, Val, Visited)."
      elixir: "defmodule Solution do\n  def latest_day_to_cross(row, col, cells) do\n\
        \    low = 1\n    high = length(cells)\n    binary_search(low, high, 0, row,\
        \ col, cells)\n  end\n\n  defp binary_search(low, high, ans, row, col, cells)\
        \ when low <= high do\n    mid = low + div(high - low, 2)\n    if can_cross(row,\
        \ col, mid, cells) do\n      binary_search(mid + 1, high, mid, row, col, cells)\n\
        \    else\n      binary_search(low, mid - 1, ans, row, col, cells)\n    end\n\
        \  end\n  defp binary_search(_, _, ans, _, _, _), do: ans\n\n  defp can_cross(row,\
        \ col, day_num, cells) do\n    grid = create_grid(row, col, day_num, cells)\n\
        \n    q = :queue.new()\n    visited = create_visited(row, col)\n\n    # Add\
        \ all land cells in the top row to the queue\n    {q_init, visited_init} = Enum.reduce(0..(col\
        \ - 1), {q, visited}, fn c_idx, {acc_q, acc_visited} ->\n      case get_grid_val(grid,\
        \ 0, c_idx, col) do\n        false -> # If it's land\n          new_q = :queue.in({0,\
        \ c_idx}, acc_q)\n          new_visited = set_visited(acc_visited, 0, c_idx,\
        \ col, true)\n          {new_q, new_visited}\n        true ->\n          {acc_q,\
        \ acc_visited}\n      end\n    end)\n\n    bfs(q_init, visited_init, row, col,\
        \ grid)\n  end\n\n  defp bfs(q, visited, row, col, grid) do\n    case :queue.out(q)\
        \ do\n      {{:value, {r, c}}, rest_q} ->\n        if r == row - 1 do\n    \
        \      true\n        else\n          dr = [-1, 1, 0, 0]\n          dc = [0,\
        \ 0, -1, 1]\n\n          {new_q, new_visited} = Enum.reduce(0..3, {rest_q, visited},\
        \ fn i, {acc_q, acc_visited} ->\n            nr = r + Enum.at(dr, i)\n     \
        \       nc = c + Enum.at(dc, i)\n\n            if nr >= 0 and nr < row and nc\
        \ >= 0 and nc < col do\n              case get_grid_val(grid, nr, nc, col) do\n\
        \                false -> # If it's land\n                  case get_visited(acc_visited,\
        \ nr, nc, col) do\n                    false ->\n                      new_q\
        \ = :queue.in({nr, nc}, acc_q)\n                      new_visited = set_visited(acc_visited,\
        \ nr, nc, col, true)\n                      {new_q, new_visited}\n         \
        \           true ->\n                      {acc_q, acc_visited}\n          \
        \        end\n                true ->\n                  {acc_q, acc_visited}\n\
        \              end\n            else\n              {acc_q, acc_visited}\n \
        \           end\n          end)\n          bfs(new_q, new_visited, row, col,\
        \ grid)\n        end\n      {:empty, _} ->\n        false\n    end\n  end\n\n\
        \  defp create_grid(row, col, day_num, cells) do\n    grid = :array.new([{:size,\
        \ row * col}, {:fixed, true}, {:default, false}])\n    Enum.reduce(0..(day_num\
        \ - 1), grid, fn i, acc_grid ->\n      [r_cell, c_cell] = Enum.at(cells, i)\n\
        \      r = r_cell - 1\n      c = c_cell - 1\n      :array.set(r * col + c, true,\
        \ acc_grid)\n    end)\n  end\n\n  defp get_grid_val(grid, r, c, col), do: :array.get(r\
        \ * col + c, grid)\n\n  defp create_visited(row, col), do: :array.new([{:size,\
        \ row * col}, {:fixed, true}, {:default, false}])\n\n  defp get_visited(visited,\
        \ r, c, col), do: :array.get(r * col + c, visited)\n\n  defp set_visited(visited,\
        \ r, c, col, val), do: :array.set(r * col + c, val, visited)\nend"
    approach: 'The problem asks for the latest day a path exists from the top to the
      bottom row. This monotonic property (if a path exists on day `D`, it also exists
      on any day `d < D`) suggests using binary search on the number of days. We define
      a `can_cross(day_num)` function which returns `true` if it''s possible to cross
      on `day_num`, and `false` otherwise. The binary search will then find the largest
      `day_num` for which `can_cross(day_num)` is true.


      The `can_cross(day_num)` function works as follows: it constructs the grid state
      for the given `day_num`. This means marking the first `day_num` cells from the
      input `cells` array as water (1-based coordinates are converted to 0-based). All
      other cells are considered land. Then, a Breadth-First Search (BFS) is performed.
      The BFS starts from all land cells in the top row. It explores adjacent land cells
      (up, down, left, right). If the BFS successfully reaches any cell in the bottom
      row, it means a path exists, and the function returns `true`. If the BFS completes
      without reaching the bottom row, it returns `false`.'
    time_complexity: The time complexity is O(row * col * log(row * col)). The binary
      search performs O(log(row * col)) iterations. In each iteration, the `can_cross`
      function initializes a grid and performs a BFS. Initializing the grid takes O(row
      * col) time (to set all cells to land and then mark `day_num` cells as water).
      The BFS itself visits each cell and edge at most once, taking O(row * col) time.
      Thus, each call to `can_cross` is O(row * col).
    space_complexity: The space complexity is O(row * col). This is primarily due to
      storing the grid state (boolean matrix) and the `visited` matrix for the BFS,
      both of which are of size `row * col`. Additionally, the BFS queue can store up
      to O(row * col) cells in the worst case.
    elapsed_time: 128.81301188468933
    model: gemini-2.5-flash
    generated_at: '2025-12-31 01:11:12 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int latestDayToCross(int row, int col, vector<vector<int>>&\
        \ cells) {\n        int low = 0, high = cells.size() - 1;\n        while (low\
        \ <= high) {\n            int mid = low + (high - low) / 2;\n            vector<vector<int>>\
        \ grid(row, vector<int>(col, 0));\n            for (int i = 0; i <= mid; i++)\
        \ {\n                grid[cells[i][0] - 1][cells[i][1] - 1] = 1;\n         \
        \   }\n            if (canCross(grid)) {\n                low = mid + 1;\n \
        \           } else {\n                high = mid - 1;\n            }\n     \
        \   }\n        return low - 1;\n    }\n\n    bool canCross(vector<vector<int>>&\
        \ grid) {\n        int row = grid.size(), col = grid[0].size();\n        vector<vector<bool>>\
        \ visited(row, vector<bool>(col, false));\n        for (int i = 0; i < row;\
        \ i++) {\n            if (dfs(grid, visited, i, 0)) {\n                return\
        \ true;\n            }\n        }\n        return false;\n    }\n\n    bool\
        \ dfs(vector<vector<int>>& grid, vector<vector<bool>>& visited, int x, int y)\
        \ {\n        int row = grid.size(), col = grid[0].size();\n        if (y ==\
        \ col - 1) {\n            return true;\n        }\n        visited[x][y] = true;\n\
        \        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};\n\
        \        for (auto& dir : directions) {\n            int nx = x + dir[0], ny\
        \ = y + dir[1];\n            if (nx >= 0 && nx < row && ny >= 0 && ny < col\
        \ && !visited[nx][ny] && grid[nx][ny] == 0) {\n                if (dfs(grid,\
        \ visited, nx, ny)) {\n                    return true;\n                }\n\
        \            }\n        }\n        return false;\n    }\n}"
      java: "class Solution {\n    public int latestDayToCross(int row, int col, int[][]\
        \ cells) {\n        int low = 0, high = cells.length - 1;\n        while (low\
        \ <= high) {\n            int mid = low + (high - low) / 2;\n            int[][]\
        \ grid = new int[row][col];\n            for (int i = 0; i <= mid; i++) {\n\
        \                grid[cells[i][0] - 1][cells[i][1] - 1] = 1;\n            }\n\
        \            if (canCross(grid)) {\n                low = mid + 1;\n       \
        \     } else {\n                high = mid - 1;\n            }\n        }\n\
        \        return low - 1;\n    }\n\n    private boolean canCross(int[][] grid)\
        \ {\n        int row = grid.length, col = grid[0].length;\n        boolean[][]\
        \ visited = new boolean[row][col];\n        for (int i = 0; i < row; i++) {\n\
        \            if (dfs(grid, visited, i, 0)) {\n                return true;\n\
        \            }\n        }\n        return false;\n    }\n\n    private boolean\
        \ dfs(int[][] grid, boolean[][] visited, int x, int y) {\n        int row =\
        \ grid.length, col = grid[0].length;\n        if (y == col - 1) {\n        \
        \    return true;\n        }\n        visited[x][y] = true;\n        int[][]\
        \ directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};\n        for (int[] dir :\
        \ directions) {\n            int nx = x + dir[0], ny = y + dir[1];\n       \
        \     if (nx >= 0 && nx < row && ny >= 0 && ny < col && !visited[nx][ny] &&\
        \ grid[nx][ny] == 0) {\n                if (dfs(grid, visited, nx, ny)) {\n\
        \                    return true;\n                }\n            }\n      \
        \  }\n        return false;\n    }\n}"
      python: "class Solution:\n    def latestDayToCross(self, row: int, col: int, cells:\
        \ List[List[int]]) -> int:\n        low, high = 0, len(cells) - 1\n        while\
        \ low <= high:\n            mid = (low + high) // 2\n            grid = [[0]\
        \ * col for _ in range(row)]\n            for i in range(mid + 1):\n       \
        \         grid[cells[i][0] - 1][cells[i][1] - 1] = 1\n            if self.canCross(grid):\n\
        \                low = mid + 1\n            else:\n                high = mid\
        \ - 1\n        return low - 1\n\n    def canCross(self, grid):\n        row,\
        \ col = len(grid), len(grid[0])\n        visited = [[False] * col for _ in range(row)]\n\
        \        for i in range(row):\n            if self.dfs(grid, visited, i, 0):\n\
        \                return True\n        return False\n\n    def dfs(self, grid,\
        \ visited, x, y):\n        row, col = len(grid), len(grid[0])\n        if y\
        \ == col - 1:\n            return True\n        visited[x][y] = True\n     \
        \   directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]\n        for dx, dy in directions:\n\
        \            nx, ny = x + dx, y + dy\n            if 0 <= nx < row and 0 <=\
        \ ny < col and not visited[nx][ny] and grid[nx][ny] == 0:\n                if\
        \ self.dfs(grid, visited, nx, ny):\n                    return True\n      \
        \  return False"
      python3: "class Solution:\n    def latestDayToCross(self, row: int, col: int,\
        \ cells: List[List[int]]) -> int:\n        low, high = 0, len(cells) - 1\n \
        \       while low <= high:\n            mid = (low + high) // 2\n          \
        \  grid = [[0] * col for _ in range(row)]\n            for i in range(mid +\
        \ 1):\n                grid[cells[i][0] - 1][cells[i][1] - 1] = 1\n        \
        \    if self.canCross(grid):\n                low = mid + 1\n            else:\n\
        \                high = mid - 1\n        return low - 1\n\n    def canCross(self,\
        \ grid):\n        row, col = len(grid), len(grid[0])\n        visited = [[False]\
        \ * col for _ in range(row)]\n        for i in range(row):\n            if self.dfs(grid,\
        \ visited, i, 0):\n                return True\n        return False\n\n   \
        \ def dfs(self, grid, visited, x, y):\n        row, col = len(grid), len(grid[0])\n\
        \        if y == col - 1:\n            return True\n        visited[x][y] =\
        \ True\n        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]\n        for\
        \ dx, dy in directions:\n            nx, ny = x + dx, y + dy\n            if\
        \ 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and grid[nx][ny] ==\
        \ 0:\n                if self.dfs(grid, visited, nx, ny):\n                \
        \    return True\n        return False"
      c: "typedef struct {\n    int** grid;\n    int row;\n    int col;\n} Solution;\n\
        \nSolution* solutionCreate(int row, int col) {\n    Solution* obj = (Solution*)\
        \ malloc(sizeof(Solution));\n    obj->row = row;\n    obj->col = col;\n    obj->grid\
        \ = (int**) malloc(row * sizeof(int*));\n    for (int i = 0; i < row; i++) {\n\
        \        obj->grid[i] = (int*) malloc(col * sizeof(int));\n    }\n    return\
        \ obj;\n}\n\nint solutionLatestDayToCross(Solution* obj, int** cells, int cellsSize)\
        \ {\n    int low = 0, high = cellsSize - 1;\n    while (low <= high) {\n   \
        \     int mid = low + (high - low) / 2;\n        for (int i = 0; i < obj->row;\
        \ i++) {\n            for (int j = 0; j < obj->col; j++) {\n               \
        \ obj->grid[i][j] = 0;\n            }\n        }\n        for (int i = 0; i\
        \ <= mid; i++) {\n            obj->grid[cells[i][0] - 1][cells[i][1] - 1] =\
        \ 1;\n        }\n        if (canCross(obj->grid, obj->row, obj->col)) {\n  \
        \          low = mid + 1;\n        } else {\n            high = mid - 1;\n \
        \       }\n    }\n    return low - 1;\n}\n\nint canCross(int** grid, int row,\
        \ int col) {\n    int** visited = (int**) malloc(row * sizeof(int*));\n    for\
        \ (int i = 0; i < row; i++) {\n        visited[i] = (int*) malloc(col * sizeof(int));\n\
        \    }\n    for (int i = 0; i < row; i++) {\n        for (int j = 0; j < col;\
        \ j++) {\n            visited[i][j] = 0;\n        }\n    }\n    for (int i =\
        \ 0; i < row; i++) {\n        if (dfs(grid, visited, i, 0, row, col)) {\n  \
        \          return 1;\n        }\n    }\n    return 0;\n}\n\nint dfs(int** grid,\
        \ int** visited, int x, int y, int row, int col) {\n    if (y == col - 1) {\n\
        \        return 1;\n    }\n    visited[x][y] = 1;\n    int directions[][2] =\
        \ {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};\n    for (int i = 0; i < 4; i++) {\n \
        \       int nx = x + directions[i][0], ny = y + directions[i][1];\n        if\
        \ (nx >= 0 && nx < row && ny >= 0 && ny < col && !visited[nx][ny] && grid[nx][ny]\
        \ == 0) {\n            if (dfs(grid, visited, nx, ny, row, col)) {\n       \
        \         return 1;\n            }\n        }\n    }\n    return 0;\n}"
      csharp: "public class Solution {\n    public int LatestDayToCross(int row, int\
        \ col, int[][] cells) {\n        int low = 0, high = cells.Length - 1;\n   \
        \     while (low <= high) {\n            int mid = low + (high - low) / 2;\n\
        \            int[][] grid = new int[row][];\n            for (int i = 0; i <\
        \ row; i++) {\n                grid[i] = new int[col];\n            }\n    \
        \        for (int i = 0; i <= mid; i++) {\n                grid[cells[i][0]\
        \ - 1][cells[i][1] - 1] = 1;\n            }\n            if (CanCross(grid))\
        \ {\n                low = mid + 1;\n            } else {\n                high\
        \ = mid - 1;\n            }\n        }\n        return low - 1;\n    }\n\n \
        \   private bool CanCross(int[][] grid) {\n        int row = grid.Length, col\
        \ = grid[0].Length;\n        bool[][] visited = new bool[row][];\n        for\
        \ (int i = 0; i < row; i++) {\n            visited[i] = new bool[col];\n   \
        \     }\n        for (int i = 0; i < row; i++) {\n            if (Dfs(grid,\
        \ visited, i, 0)) {\n                return true;\n            }\n        }\n\
        \        return false;\n    }\n\n    private bool Dfs(int[][] grid, bool[][]\
        \ visited, int x, int y) {\n        int row = grid.Length, col = grid[0].Length;\n\
        \        if (y == col - 1) {\n            return true;\n        }\n        visited[x][y]\
        \ = true;\n        int[][] directions = { new int[] { -1, 0 }, new int[] { 1,\
        \ 0 }, new int[] { 0, -1 }, new int[] { 0, 1 } };\n        for (int i = 0; i\
        \ < 4; i++) {\n            int nx = x + directions[i][0], ny = y + directions[i][1];\n\
        \            if (nx >= 0 && nx < row && ny >= 0 && ny < col && !visited[nx][ny]\
        \ && grid[nx][ny] == 0) {\n                if (Dfs(grid, visited, nx, ny)) {\n\
        \                    return true;\n                }\n            }\n      \
        \  }\n        return false;\n    }\n}"
      javascript: "var latestDayToCross = function(row, col, cells) {\n    let low =\
        \ 0, high = cells.length - 1;\n    while (low <= high) {\n        let mid =\
        \ Math.floor((low + high) / 2);\n        let grid = Array(row).fill(0).map(()\
        \ => Array(col).fill(0));\n        for (let i = 0; i <= mid; i++) {\n      \
        \      grid[cells[i][0] - 1][cells[i][1] - 1] = 1;\n        }\n        if (canCross(grid))\
        \ {\n            low = mid + 1;\n        } else {\n            high = mid -\
        \ 1;\n        }\n    }\n    return low - 1;\n};\n\nvar canCross = function(grid)\
        \ {\n    let row = grid.length, col = grid[0].length;\n    let visited = Array(row).fill(0).map(()\
        \ => Array(col).fill(false));\n    for (let i = 0; i < row; i++) {\n       \
        \ if (dfs(grid, visited, i, 0)) {\n            return true;\n        }\n   \
        \ }\n    return false;\n};\n\nvar dfs = function(grid, visited, x, y) {\n  \
        \  let row = grid.length, col = grid[0].length;\n    if (y === col - 1) {\n\
        \        return true;\n    }\n    visited[x][y] = true;\n    let directions\
        \ = [[-1, 0], [1, 0], [0, -1], [0, 1]];\n    for (let i = 0; i < 4; i++) {\n\
        \        let nx = x + directions[i][0], ny = y + directions[i][1];\n       \
        \ if (nx >= 0 && nx < row && ny >= 0 && ny < col && !visited[nx][ny] && grid[nx][ny]\
        \ === 0) {\n            if (dfs(grid, visited, nx, ny)) {\n                return\
        \ true;\n            }\n        }\n    }\n    return false;\n};"
      typescript: "function latestDayToCross(row: number, col: number, cells: number[][]):\
        \ number {\n    let low: number = 0, high: number = cells.length - 1;\n    while\
        \ (low <= high) {\n        let mid: number = Math.floor((low + high) / 2);\n\
        \        let grid: number[][] = Array(row).fill(0).map(() => Array(col).fill(0));\n\
        \        for (let i: number = 0; i <= mid; i++) {\n            grid[cells[i][0]\
        \ - 1][cells[i][1] - 1] = 1;\n        }\n        if (canCross(grid)) {\n   \
        \         low = mid + 1;\n        } else {\n            high = mid - 1;\n  \
        \      }\n    }\n    return low - 1;\n}\n\nfunction canCross(grid: number[][]):\
        \ boolean {\n    let row: number = grid.length, col: number = grid[0].length;\n\
        \    let visited: boolean[][] = Array(row).fill(0).map(() => Array(col).fill(false));\n\
        \    for (let i: number = 0; i < row; i++) {\n        if (dfs(grid, visited,\
        \ i, 0)) {\n            return true;\n        }\n    }\n    return false;\n\
        }\n\nfunction dfs(grid: number[][], visited: boolean[][], x: number, y: number):\
        \ boolean {\n    let row: number = grid.length, col: number = grid[0].length;\n\
        \    if (y === col - 1) {\n        return true;\n    }\n    visited[x][y] =\
        \ true;\n    let directions: number[][] = [[-1, 0], [1, 0], [0, -1], [0, 1]];\n\
        \    for (let i: number = 0; i < 4; i++) {\n        let nx: number = x + directions[i][0],\
        \ ny: number = y + directions[i][1];\n        if (nx >= 0 && nx < row && ny\
        \ >= 0 && ny < col && !visited[nx][ny] && grid[nx][ny] === 0) {\n          \
        \  if (dfs(grid, visited, nx, ny)) {\n                return true;\n       \
        \     }\n        }\n    }\n    return false;\n}"
      php: "class Solution {\n    function latestDayToCross($row, $col, $cells) {\n\
        \        $low = 0; $high = count($cells) - 1;\n        while ($low <= $high)\
        \ {\n            $mid = floor(($low + $high) / 2);\n            $grid = array_fill(0,\
        \ $row, array_fill(0, $col, 0));\n            for ($i = 0; $i <= $mid; $i++)\
        \ {\n                $grid[$cells[$i][0] - 1][$cells[$i][1] - 1] = 1;\n    \
        \        }\n            if ($this->canCross($grid)) {\n                $low\
        \ = $mid + 1;\n            } else {\n                $high = $mid - 1;\n   \
        \         }\n        }\n        return $low - 1;\n    }\n\n    function canCross($grid)\
        \ {\n        $row = count($grid); $col = count($grid[0]);\n        $visited\
        \ = array_fill(0, $row, array_fill(0, $col, false));\n        for ($i = 0; $i\
        \ < $row; $i++) {\n            if ($this->dfs($grid, $visited, $i, 0)) {\n \
        \               return true;\n            }\n        }\n        return false;\n\
        \    }\n\n    function dfs($grid, &$visited, $x, $y) {\n        $row = count($grid);\
        \ $col = count($grid[0]);\n        if ($y == $col - 1) {\n            return\
        \ true;\n        }\n        $visited[$x][$y] = true;\n        $directions =\
        \ [[-1, 0], [1, 0], [0, -1], [0, 1]];\n        for ($i = 0; $i < 4; $i++) {\n\
        \            $nx = $x + $directions[$i][0]; $ny = $y + $directions[$i][1];\n\
        \            if ($nx >= 0 && $nx < $row && $ny >= 0 && $ny < $col && !$visited[$nx][$ny]\
        \ && $grid[$nx][$ny] == 0) {\n                if ($this->dfs($grid, $visited,\
        \ $nx, $ny)) {\n                    return true;\n                }\n      \
        \      }\n        }\n        return false;\n    }\n}"
      swift: "class Solution {\n    func latestDayToCross(_ row: Int, _ col: Int, _\
        \ cells: [[Int]]) -> Int {\n        var low: Int = 0, high: Int = cells.count\
        \ - 1\n        while low <= high {\n            let mid: Int = low + (high -\
        \ low) / 2\n            var grid: [[Int]] = Array(repeating: Array(repeating:\
        \ 0, count: col), count: row)\n            for i in 0...mid {\n            \
        \    grid[cells[i][0] - 1][cells[i][1] - 1] = 1\n            }\n           \
        \ if canCross(grid) {\n                low = mid + 1\n            } else {\n\
        \                high = mid - 1\n            }\n        }\n        return low\
        \ - 1\n    }\n\n    func canCross(_ grid: [[Int]]) -> Bool {\n        let row:\
        \ Int = grid.count, col: Int = grid[0].count\n        var visited: [[Bool]]\
        \ = Array(repeating: Array(repeating: false, count: col), count: row)\n    \
        \    for i in 0..<row {\n            if dfs(grid, &visited, i, 0) {\n      \
        \          return true\n            }\n        }\n        return false\n   \
        \ }\n\n    func dfs(_ grid: [[Int]], _ visited: inout [[Bool]], _ x: Int, _\
        \ y: Int) -> Bool {\n        let row: Int = grid.count, col: Int = grid[0].count\n\
        \        if y == col - 1 {\n            return true\n        }\n        visited[x][y]\
        \ = true\n        let directions: [(Int, Int)] = [(-1, 0), (1, 0), (0, -1),\
        \ (0, 1)]\n        for i in 0..<4 {\n            let nx: Int = x + directions[i].0,\
        \ ny: Int = y + directions[i].1\n            if nx >= 0 && nx < row && ny >=\
        \ 0 && ny < col && !visited[nx][ny] && grid[nx][ny] == 0 {\n               \
        \ if dfs(grid, &visited, nx, ny) {\n                    return true\n      \
        \          }\n            }\n        }\n        return false\n    }\n}"
      kotlin: "class Solution {\n    fun latestDayToCross(row: Int, col: Int, cells:\
        \ Array<IntArray>): Int {\n        var low: Int = 0\n        var high: Int =\
        \ cells.size - 1\n        while (low <= high) {\n            val mid: Int =\
        \ low + (high - low) / 2\n            val grid: Array<IntArray> = Array(row)\
        \ { IntArray(col) { 0 } }\n            for (i in 0..mid) {\n               \
        \ grid[cells[i][0] - 1][cells[i][1] - 1] = 1\n            }\n            if\
        \ (canCross(grid)) {\n                low = mid + 1\n            } else {\n\
        \                high = mid - 1\n            }\n        }\n        return low\
        \ - 1\n    }\n\n    fun canCross(grid: Array<IntArray>): Boolean {\n       \
        \ val row: Int = grid.size\n        val col: Int = grid[0].size\n        val\
        \ visited: Array<BooleanArray> = Array(row) { BooleanArray(col) { false } }\n\
        \        for (i in 0 until row) {\n            if (dfs(grid, visited, i, 0))\
        \ {\n                return true\n            }\n        }\n        return false\n\
        \    }\n\n    fun dfs(grid: Array<IntArray>, visited: Array<BooleanArray>, x:\
        \ Int, y: Int): Boolean {\n        val row: Int = grid.size\n        val col:\
        \ Int = grid[0].size\n        if (y == col - 1) {\n            return true\n\
        \        }\n        visited[x][y] = true\n        val directions: Array<IntArray>\
        \ = arrayOf(intArrayOf(-1, 0), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(0,\
        \ 1))\n        for (i in 0 until 4) {\n            val nx: Int = x + directions[i][0]\n\
        \            val ny: Int = y + directions[i][1]\n            if (nx in 0 until\
        \ row && ny in 0 until col && !visited[nx][ny] && grid[nx][ny] == 0) {\n   \
        \             if (dfs(grid, visited, nx, ny)) {\n                    return\
        \ true\n                }\n            }\n        }\n        return false\n\
        \    }\n}"
      dart: "class Solution {\n    int latestDayToCross(int row, int col, List<List<int>>\
        \ cells) {\n        int low = 0, high = cells.length - 1;\n        while (low\
        \ <= high) {\n            int mid = low + (high - low) ~/ 2;\n            List<List<int>>\
        \ grid = List.generate(row, (i) => List.generate(col, (j) => 0));\n        \
        \    for (int i = 0; i <= mid; i++) {\n                grid[cells[i][0] - 1][cells[i][1]\
        \ - 1] = 1;\n            }\n            if (canCross(grid)) {\n            \
        \    low = mid + 1;\n            } else {\n                high = mid - 1;\n\
        \            }\n        }\n        return low - 1;\n    }\n\n    bool canCross(List<List<int>>\
        \ grid) {\n        int row = grid.length, col = grid[0].length;\n        List<List<bool>>\
        \ visited = List.generate(row, (i) => List.generate(col, (j) => false));\n \
        \       for (int i = 0; i < row; i++) {\n            if (dfs(grid, visited,\
        \ i, 0)) {\n                return true;\n            }\n        }\n       \
        \ return false;\n    }\n\n    bool dfs(List<List<int>> grid, List<List<bool>>\
        \ visited, int x, int y) {\n        int row = grid.length, col = grid[0].length;\n\
        \        if (y == col - 1) {\n            return true;\n        }\n        visited[x][y]\
        \ = true;\n        List<List<int>> directions = [[-1, 0], [1, 0], [0, -1], [0,\
        \ 1]];\n        for (int i = 0; i < 4; i++) {\n            int nx = x + directions[i][0],\
        \ ny = y + directions[i][1];\n            if (nx >= 0 && nx < row && ny >= 0\
        \ && ny < col && !visited[nx][ny] && grid[nx][ny] == 0) {\n                if\
        \ (dfs(grid, visited, nx, ny)) {\n                    return true;\n       \
        \         }\n            }\n        }\n        return false;\n    }\n}"
      go: "package main\n\nimport (\n    \"fmt\"\n)\n\ntype Solution struct{}\n\nfunc\
        \ (s *Solution) latestDayToCross(row int, col int, cells [][]int) int {\n  \
        \  low, high := 0, len(cells)-1\n    for low <= high {\n        mid := low +\
        \ (high-low)/2\n        grid := make([][]int, row)\n        for i := range grid\
        \ {\n            grid[i] = make([]int, col)\n        }\n        for i := 0;\
        \ i <= mid; i++ {\n            grid[cells[i][0]-1][cells[i][1]-1] = 1\n    \
        \    }\n        if s.canCross(grid) {\n            low = mid + 1\n        }\
        \ else {\n            high = mid - 1\n        }\n    }\n    return low - 1\n\
        }\n\nfunc (s *Solution) canCross(grid [][]int) bool {\n    row, col := len(grid),\
        \ len(grid[0])\n    visited := make([][]bool, row)\n    for i := range visited\
        \ {\n        visited[i] = make([]bool, col)\n    }\n    for i := 0; i < row;\
        \ i++ {\n        if s.dfs(grid, visited, i, 0) {\n            return true\n\
        \        }\n    }\n    return false\n}\n\nfunc (s *Solution) dfs(grid [][]int,\
        \ visited [][]bool, x, y int) bool {\n    row, col := len(grid), len(grid[0])\n\
        \    if y == col-1 {\n        return true\n    }\n    visited[x][y] = true\n\
        \    directions := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}\n    for i := 0;\
        \ i < 4; i++ {\n        nx, ny := x+directions[i][0], y+directions[i][1]\n \
        \       if nx >= 0 && nx < row && ny >= 0 && ny < col && !visited[nx][ny] &&\
        \ grid[nx][ny] == 0 {\n            if s.dfs(grid, visited, nx, ny) {\n     \
        \           return true\n            }\n        }\n    }\n    return false\n\
        }"
      ruby: "class Solution\n    def latest_day_to_cross(row, col, cells)\n        low,\
        \ high = 0, cells.size - 1\n        while low <= high\n            mid = low\
        \ + (high - low) / 2\n            grid = Array.new(row) { Array.new(col, 0)\
        \ }\n            (0..mid).each do |i|\n                grid[cells[i][0] - 1][cells[i][1]\
        \ - 1] = 1\n            end\n            if can_cross(grid)\n              \
        \  low = mid + 1\n            else\n                high = mid - 1\n       \
        \     end\n        end\n        low - 1\n    end\n\n    def can_cross(grid)\n\
        \        row, col = grid.size, grid[0].size\n        visited = Array.new(row)\
        \ { Array.new(col, false) }\n        (0...row).each do |i|\n            return\
        \ true if dfs(grid, visited, i, 0)\n        end\n        false\n    end\n\n\
        \    def dfs(grid, visited, x, y)\n        row, col = grid.size, grid[0].size\n\
        \        return true if y == col - 1\n        visited[x][y] = true\n       \
        \ directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]\n        (0...4).each do |i|\n\
        \            nx, ny = x + directions[i][0], y + directions[i][1]\n         \
        \   if nx >= 0 && nx < row && ny >= 0 && ny < col && !visited[nx][ny] && grid[nx][ny]\
        \ == 0\n                return true if dfs(grid, visited, nx, ny)\n        \
        \    end\n        end\n        false\n    end\nend"
      scala: "object Solution {\n    def latestDayToCross(row: Int, col: Int, cells:\
        \ Array[Array[Int]]): Int = {\n        var low: Int = 0\n        var high: Int\
        \ = cells.length - 1\n        while (low <= high) {\n            val mid: Int\
        \ = low + (high - low) / 2\n            val grid: Array[Array[Int]] = Array.ofDim[Int](row,\
        \ col)\n            for (i <- 0 to mid) {\n                grid(cells(i)(0)\
        \ - 1)(cells(i)(1) - 1) = 1\n            }\n            if (canCross(grid))\
        \ {\n                low = mid + 1\n            } else {\n                high\
        \ = mid - 1\n            }\n        }\n        low - 1\n    }\n\n    def canCross(grid:\
        \ Array[Array[Int]]): Boolean = {\n        val row: Int = grid.length\n    \
        \    val col: Int = grid(0).length\n        val visited: Array[Array[Boolean]]\
        \ = Array.ofDim[Boolean](row, col)\n        for (i <- 0 until row) {\n     \
        \       if (dfs(grid, visited, i, 0)) {\n                return true\n     \
        \       }\n        }\n        false\n    }\n\n    def dfs(grid: Array[Array[Int]],\
        \ visited: Array[Array[Boolean]], x: Int, y: Int): Boolean = {\n        val\
        \ row: Int = grid.length\n        val col: Int = grid(0).length\n        if\
        \ (y == col - 1) {\n            return true\n        }\n        visited(x)(y)\
        \ = true\n        val directions: Array[Array[Int]] = Array.ofDim[Int](4, 2)\n\
        \        directions(0) = Array(-1, 0)\n        directions(1) = Array(1, 0)\n\
        \        directions(2) = Array(0, -1)\n        directions(3) = Array(0, 1)\n\
        \        for (i <- 0 until 4) {\n            val nx: Int = x + directions(i)(0)\n\
        \            val ny: Int = y + directions(i)(1)\n            if (nx >= 0 &&\
        \ nx < row && ny >= 0 && ny < col && !visited(nx)(ny) && grid(nx)(ny) == 0)\
        \ {\n                if (dfs(grid, visited, nx, ny)) {\n                   \
        \ return true\n                }\n            }\n        }\n        false\n\
        \    }\n}"
      rust: "struct Solution;\n\nimpl Solution {\n    pub fn latest_day_to_cross(row:\
        \ i32, col: i32, cells: Vec<Vec<i32>>) -> i32 {\n        let mut low: i32 =\
        \ 0;\n        let mut high: i32 = cells.len() as i32 - 1;\n        while low\
        \ <= high {\n            let mid: i32 = low + (high - low) / 2;\n          \
        \  let mut grid: Vec<Vec<i32>> = vec![vec![0; col as usize]; row as usize];\n\
        \            for i in 0..=mid {\n                grid[cells[i as usize][0] as\
        \ usize - 1][cells[i as usize][1] as usize - 1] = 1;\n            }\n      \
        \      if Solution::can_cross(&grid) {\n                low = mid + 1;\n   \
        \         } else {\n                high = mid - 1;\n            }\n       \
        \ }\n        low - 1\n    }\n\n    pub fn can_cross(grid: &Vec<Vec<i32>>) ->\
        \ bool {\n        let row: usize = grid.len();\n        let col: usize = grid[0].len();\n\
        \        let mut visited: Vec<Vec<bool>> = vec![vec![false; col]; row];\n  \
        \      for i in 0..row {\n            if Solution::dfs(&grid, &mut visited,\
        \ i, 0) {\n                return true;\n            }\n        }\n        false\n\
        \    }\n\n    pub fn dfs(grid: &Vec<Vec<i32>>, visited: &mut Vec<Vec<bool>>,\
        \ x: usize, y: usize) -> bool {\n        let row: usize = grid.len();\n    \
        \    let col: usize = grid[0].len();\n        if y == col - 1 {\n          \
        \  return true;\n        }\n        visited[x][y] = true;\n        let directions:\
        \ Vec<(i32, i32)> = vec![(-1, 0), (1, 0), (0, -1), (0, 1)];\n        for i in\
        \ 0..4 {\n            let nx: i32 = x as i32 + directions[i].0;\n          \
        \  let ny: i32 = y as i32 + directions[i].1;\n            if nx >= 0 && nx <\
        \ row as i32 && ny >= 0 && ny < col as i32 && !visited[nx as usize][ny as usize]\
        \ && grid[nx as usize][ny as usize] == 0 {\n                if Solution::dfs(&grid,\
        \ visited, nx as usize, ny as usize) {\n                    return true;\n \
        \               }\n            }\n        }\n        false\n    }\n}"
      racket: "define (latest-day-to-cross row col cells)\n    (let loop ((low 0) (high\
        \ (sub1 (length cells))))\n        (if (> low high)\n            (sub1 low)\n\
        \            (let ((mid (quotient (+ low high) 2)))\n                (let ((grid\
        \ (make-grid row col)))\n                    (for ((i (range (add1 mid))))\n\
        \                        (grid-set! grid (sub1 (list-ref (list-ref cells i)\
        \ 0)) (sub1 (list-ref (list-ref cells i) 1)) 1))\n                    (if (can-cross?\
        \ grid)\n                        (loop (add1 mid) high)\n                  \
        \      (loop low (sub1 mid)))))))\n\n(define (can-cross? grid)\n    (let ((row\
        \ (grid-rows grid)) (col (grid-cols grid)) (visited (make-visited row col)))\n\
        \        (let loop ((i 0))\n            (if (= i row)\n                #f\n\
        \                (if (dfs grid visited i 0)\n                    #t\n      \
        \              (loop (add1 i))))))\n\n(define (dfs grid visited x y)\n    (if\
        \ (= y (sub1 (grid-cols grid)))\n        #t\n        (begin\n            (visited-set!\
        \ visited x y #t)\n            (let loop ((i 0))\n                (if (= i 4)\n\
        \                    #f\n                    (let ((nx (+ x (list-ref (list-ref\
        \ directions i) 0))) (ny (+ y (list-ref (list-ref directions i) 1))))\n    \
        \                    (if (and (>= nx 0) (< nx (grid-rows grid)) (>= ny 0) (<\
        \ ny (grid-cols grid)) (not (visited-ref visited nx ny)) (= (grid-ref grid nx\
        \ ny) 0))\n                            (if (dfs grid visited nx ny)\n      \
        \                          #t\n                                (loop (add1 i)))\n\
        \                            (loop (add1 i)))))))))\n\n(define directions (list\
        \ (list -1 0) (list 1 0) (list 0 -1) (list 0 1)))\n\n(define (make-grid row\
        \ col)\n    (build-list row (lambda (x) (build-list col (lambda (y) 0)))))\n\
        \n(define (grid-rows grid) (length grid))\n(define (grid-cols grid) (length\
        \ (list-ref grid 0)))\n(define (grid-ref grid x y) (list-ref (list-ref grid\
        \ x) y))\n(define (grid-set! grid x y val) (list-set! (list-ref grid x) y val))\n\
        \n(define (make-visited row col)\n    (build-list row (lambda (x) (build-list\
        \ col (lambda (y) #f)))))\n\n(define (visited-ref visited x y) (list-ref (list-ref\
        \ visited x) y))\n(define (visited-set! visited x y val) (list-set! (list-ref\
        \ visited x) y val))"
      erlang: "latest_day_to_cross(Row, Col, Cells) ->\n    Low = 0,\n    High = length(Cells)\
        \ - 1,\n    loop(Low, High, Cells, Row, Col).\n\nloop(Low, High, Cells, Row,\
        \ Col) when Low > High -> Low - 1;\nloop(Low, High, Cells, Row, Col) ->\n  \
        \  Mid = Low + (High - Low) div 2,\n    Grid = create_grid(Row, Col),\n    update_grid(Grid,\
        \ Cells, Mid),\n    case can_cross(Grid) of\n        true -> loop(Mid + 1, High,\
        \ Cells, Row, Col);\n        false -> loop(Low, Mid - 1, Cells, Row, Col)\n\
        \    end.\n\ncreate_grid(Row, Col) ->\n    [ [ 0 || _ <- lists:seq(1, Col) ]\
        \ || _ <- lists:seq(1, Row) ].\n\nupdate_grid(Grid, Cells, Mid) ->\n    lists:foldl(fun({X,\
        \ Y}, Acc) ->\n        update_grid(Acc, X - 1, Y - 1, 1)\n    end, Grid, lists:sublist(Cells,\
        \ Mid + 1)).\n\nupdate_grid(Grid, X, Y, Val) ->\n    lists:map(fun(List) when\
        \ X == 0 ->\n        [ Val | lists:sublist(List, 2, length(List)) ];\n     \
        \   (H) -> [H | update_grid(lists:sublist(List, 2, length(List)), X - 1, Y,\
        \ Val)]\n    end, Grid).\n\ncan_cross(Grid) ->\n    lists:any(fun(X) -> dfs(Grid,\
        \ X, 0) end, lists:seq(0, length(Grid) - 1)).\n\ndfs(Grid, X, Y) ->\n    Y ==\
        \ length(lists:nth(1, Grid)) - 1;\n\ndfs(Grid, X, Y) ->\n    lists:foldl(fun(Direction,\
        \ Acc) ->\n        {DX, DY} = Direction,\n        NX = X + DX,\n        NY =\
        \ Y + DY,\n        case {NX, NY} of\n            {N, N} when N < 0; N >= length(Grid)\
        \ -> Acc;\n            {_, NY} when NY < 0; NY >= length(lists:nth(1, Grid))\
        \ -> Acc;\n            {NX, NY} ->\n                case lists:nth(NX + 1, Grid)\
        \ of\n                    [H | _] when H == 0 -> dfs(Grid, NX, NY);\n      \
        \              _ -> Acc\n                end\n        end\n    end, false, [{-1,\
        \ 0}, {1, 0}, {0, -1}, {0, 1}])."
      elixir: "defmodule Solution do\n    def latest_day_to_cross(row, col, cells) do\n\
        \        low = 0\n        high = length(cells) - 1\n        loop(low, high,\
        \ cells, row, col)\n    end\n\n    defp loop(low, high, cells, row, col) when\
        \ low > high, do: low - 1\n    defp loop(low, high, cells, row, col) do\n  \
        \      mid = div(low + high, 2)\n        grid = create_grid(row, col)\n    \
        \    update_grid(grid, cells, mid)\n        case can_cross(grid) do\n      \
        \      true -> loop(mid + 1, high, cells, row, col)\n            false -> loop(low,\
        \ mid - 1, cells, row, col)\n        end\n    end\n\n    defp create_grid(row,\
        \ col), do: for(_ <- 1..row, do: for(_ <- 1..col, do: 0))\n\n    defp update_grid(grid,\
        \ cells, mid) do\n        Enum.reduce(1..mid, grid, fn i, acc ->\n         \
        \   update_grid(acc, Enum.at(cells, i - 1), 1)\n        end)\n    end\n\n  \
        \  defp update_grid(grid, [x, y], val) do\n        List.update_at(grid, x -\
        \ 1, fn row -> List.update_at(row, y - 1, fn _ -> val end))\n    end\n\n   \
        \ defp can_cross(grid) do\n        Enum.any?(0..length(grid) - 1, fn x -> dfs(grid,\
        \ x, 0) end)\n    end\n\n    defp dfs(grid, x, y) do\n        y == length(Enum.at(grid,\
        \ 0)) - 1\n    end\n\n    defp dfs(grid, x, y) do\n        Enum.reduce([{-1,\
        \ 0}, {1, 0}, {0, -1}, {0, 1}], false, fn {dx, dy}, acc ->\n            nx =\
        \ x + dx\n            ny = y + dy\n            cond do\n                nx <\
        \ 0 or nx >= length(grid) -> acc\n                ny < 0 or ny >= length(Enum.at(grid,\
        \ 0)) -> acc\n                true -> dfs(grid, nx, ny)\n            end\n \
        \       end)\n    end\nend"
    approach: The problem can be solved using a graph algorithm and binary search. We
      start by initializing a 2D grid with all land cells. Then, we use binary search
      to find the last day where it is possible to walk from the top to the bottom by
      only walking on land cells. For each day in the binary search range, we update
      the grid according to the given cells and check if there is a path from the top
      to the bottom using a depth-first search (DFS) algorithm. If there is a path,
      we update the lower bound of the binary search range; otherwise, we update the
      upper bound. The key intuition is that the problem can be reduced to finding the
      last day where the top and bottom rows are connected in the grid.
    time_complexity: The time complexity of the solution is O(row * col * log(row *
      col)) because we are using binary search to find the last day and DFS to check
      if there is a path from the top to the bottom. The binary search reduces the number
      of days we need to check, and the DFS algorithm checks if there is a path in the
      grid.
    space_complexity: The space complexity of the solution is O(row * col) because we
      need to store the grid and the visited cells during the DFS. The space complexity
      is linear with respect to the size of the input grid.
    elapsed_time: 24.288334846496582
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-31 01:11:36 '
---

## Problem #1970: Last Day Where You Can Still Cross

**Difficulty:** Hard

**Topics:** Array, Binary Search, Depth-First Search, Breadth-First Search, Union Find, Matrix

## Problem Description

<p>There is a <strong>1-based</strong> binary matrix where <code>0</code> represents land and <code>1</code> represents water. You are given integers <code>row</code> and <code>col</code> representing the number of rows and columns in the matrix, respectively.</p>

<p>Initially on day <code>0</code>, the <strong>entire</strong> matrix is <strong>land</strong>. However, each day a new cell becomes flooded with <strong>water</strong>. You are given a <strong>1-based</strong> 2D array <code>cells</code>, where <code>cells[i] = [r<sub>i</sub>, c<sub>i</sub>]</code> represents that on the <code>i<sup>th</sup></code> day, the cell on the <code>r<sub>i</sub><sup>th</sup></code> row and <code>c<sub>i</sub><sup>th</sup></code> column (<strong>1-based</strong> coordinates) will be covered with <strong>water</strong> (i.e., changed to <code>1</code>).</p>

<p>You want to find the <strong>last</strong> day that it is possible to walk from the <strong>top</strong> to the <strong>bottom</strong> by only walking on land cells. You can start from <strong>any</strong> cell in the top row and end at <strong>any</strong> cell in the bottom row. You can only travel in the<strong> four</strong> cardinal directions (left, right, up, and down).</p>

<p>Return <em>the <strong>last</strong> day where it is possible to walk from the <strong>top</strong> to the <strong>bottom</strong> by only walking on land cells</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/27/1.png" style="width: 624px; height: 162px;" />
<pre>
<strong>Input:</strong> row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 2.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/27/2.png" style="width: 504px; height: 178px;" />
<pre>
<strong>Input:</strong> row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 1.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/27/3.png" style="width: 666px; height: 167px;" />
<pre>
<strong>Input:</strong> row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= row, col &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>4 &lt;= row * col &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>cells.length == row * col</code></li>
	<li><code>1 &lt;= r<sub>i</sub> &lt;= row</code></li>
	<li><code>1 &lt;= c<sub>i</sub> &lt;= col</code></li>
	<li>All the values of <code>cells</code> are <strong>unique</strong>.</li>
</ul>


## Hints

1. What graph algorithm allows us to find whether a path exists?

2. Can we use binary search to help us solve the problem?

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-31 01:11:12 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the latest day a path exists from the top to the bottom row. This monotonic property (if a path exists on day `D`, it also exists on any day `d < D`) suggests using binary search on the number of days. We define a `can_cross(day_num)` function which returns `true` if it's possible to cross on `day_num`, and `false` otherwise. The binary search will then find the largest `day_num` for which `can_cross(day_num)` is true.

The `can_cross(day_num)` function works as follows: it constructs the grid state for the given `day_num`. This means marking the first `day_num` cells from the input `cells` array as water (1-based coordinates are converted to 0-based). All other cells are considered land. Then, a Breadth-First Search (BFS) is performed. The BFS starts from all land cells in the top row. It explores adjacent land cells (up, down, left, right). If the BFS successfully reaches any cell in the bottom row, it means a path exists, and the function returns `true`. If the BFS completes without reaching the bottom row, it returns `false`.

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
#include <vector>
#include <queue>
#include <utility>

class Solution {
public:
    bool canCross(int row, int col, int day_num, const std::vector<std::vector<int>>& cells) {
        std::vector<std::vector<bool>> grid(row, std::vector<bool>(col, false)); // false for land, true for water
        for (int i = 0; i < day_num; ++i) {
            grid[cells[i][0] - 1][cells[i][1] - 1] = true; // Mark as water
        }

        std::queue<std::pair<int, int>> q;
        std::vector<std::vector<bool>> visited(row, std::vector<bool>(col, false));

        // Add all land cells in the top row to the queue
        for (int c = 0; c < col; ++c) {
            if (!grid[0][c]) { // If it's land
                q.push({0, c});
                visited[0][c] = true;
            }
        }

        int dr[] = {-1, 1, 0, 0};
        int dc[] = {0, 0, -1, 1};

        while (!q.empty()) {
            std::pair<int, int> curr = q.front();
            q.pop();
            int r = curr.first;
            int c = curr.second;

            if (r == row - 1) { // Reached the bottom row
                return true;
            }

            for (int i = 0; i < 4; ++i) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (nr >= 0 && nr < row && nc >= 0 && nc < col &&
                    !grid[nr][nc] && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    q.push({nr, nc});
                }
            }
        }

        return false;
    }

    int latestDayToCross(int row, int col, std::vector<std::vector<int>>& cells) {
        int low = 1;
        int high = cells.size(); // Max day is when all cells are flooded
        int ans = 0;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canCross(row, col, mid, cells)) {
                ans = mid;
                low = mid + 1; // Try a later day
            } else {
                high = mid - 1; // Must be an earlier day
            }
        }

        return ans;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.LinkedList;
import java.util.Queue;
import java.util.List;

class Solution {
    private boolean canCross(int row, int col, int dayNum, List<List<Integer>> cells) {
        boolean[][] grid = new boolean[row][col]; // false for land, true for water
        for (int i = 0; i < dayNum; i++) {
            grid[cells.get(i).get(0) - 1][cells.get(i).get(1) - 1] = true; // Mark as water
        }

        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[row][col];

        // Add all land cells in the top row to the queue
        for (int c = 0; c < col; c++) {
            if (!grid[0][c]) { // If it's land
                q.offer(new int[]{0, c});
                visited[0][c] = true;
            }
        }

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int r = curr[0];
            int c = curr[1];

            if (r == row - 1) { // Reached the bottom row
                return true;
            }

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (nr >= 0 && nr < row && nc >= 0 && nc < col &&
                    !grid[nr][nc] && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    q.offer(new int[]{nr, nc});
                }
            }
        }

        return false;
    }

    public int latestDayToCross(int row, int col, List<List<Integer>> cells) {
        int low = 1;
        int high = cells.size(); // Max day is when all cells are flooded
        int ans = 0;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canCross(row, col, mid, cells)) {
                ans = mid;
                low = mid + 1; // Try a later day
            } else {
                high = mid - 1; // Must be an earlier day
            }
        }

        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import collections
from typing import List

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        def can_cross(day_num: int) -> bool:
            # Create a grid representing the state on day_num
            # True for water, False for land
            grid = [[False] * col for _ in range(row)]
            for i in range(day_num):
                r, c = cells[i][0] - 1, cells[i][1] - 1 # Convert to 0-based
                grid[r][c] = True # Mark as water

            # BFS to check connectivity
            q = collections.deque()
            visited = [[False] * col for _ in range(row)]

            # Add all land cells in the top row to the queue
            for c_idx in range(col):
                if not grid[0][c_idx]: # If it's land
                    q.append((0, c_idx))
                    visited[0][c_idx] = True

            # Directions for BFS
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]

            while q:
                r, c = q.popleft()

                if r == row - 1: # Reached the bottom row
                    return True

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]

                    # Check bounds
                    if 0 <= nr < row and 0 <= nc < col:
                        # If it's land and not visited
                        if not grid[nr][nc] and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))

            return False # No path found

        # Binary search for the latest day
        low = 1
        high = len(cells) # Max day is when all cells are flooded
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2
            if can_cross(mid):
                ans = mid
                low = mid + 1 # Try a later day
            else:
                high = mid - 1 # Must be an earlier day

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections
from typing import List

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        def can_cross(day_num: int) -> bool:
            # Create a grid representing the state on day_num
            # True for water, False for land
            grid = [[False] * col for _ in range(row)]
            for i in range(day_num):
                r, c = cells[i][0] - 1, cells[i][1] - 1 # Convert to 0-based
                grid[r][c] = True # Mark as water

            # BFS to check connectivity
            q = collections.deque()
            visited = [[False] * col for _ in range(row)]

            # Add all land cells in the top row to the queue
            for c_idx in range(col):
                if not grid[0][c_idx]: # If it's land
                    q.append((0, c_idx))
                    visited[0][c_idx] = True

            # Directions for BFS
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]

            while q:
                r, c = q.popleft()

                if r == row - 1: # Reached the bottom row
                    return True

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]

                    # Check bounds
                    if 0 <= nr < row and 0 <= nc < col:
                        # If it's land and not visited
                        if not grid[nr][nc] and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))

            return False # No path found

        # Binary search for the latest day
        low = 1
        high = len(cells) # Max day is when all cells are flooded
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2
            if can_cross(mid):
                ans = mid
                low = mid + 1 # Try a later day
            else:
                high = mid - 1 # Must be an earlier day

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

// Structure to represent a cell coordinate
typedef struct {
    int r;
    int c;
} Cell;

// Function to check if a path exists on a given day
bool canCross(int row, int col, int day_num, int** cells) {
    // Dynamically allocate grid and initialize to false (land)
    bool* grid_flat = (bool*)calloc(row * col, sizeof(bool)); // false for land, true for water
    if (grid_flat == NULL) return false; // Handle allocation failure

    for (int i = 0; i < day_num; ++i) {
        int r_idx = cells[i][0] - 1;
        int c_idx = cells[i][1] - 1;
        grid_flat[r_idx * col + c_idx] = true; // Mark as water
    }

    // Queue for BFS (using a simple array as a circular buffer)
    Cell* q_buffer = (Cell*)malloc(row * col * sizeof(Cell));
    if (q_buffer == NULL) {
        free(grid_flat);
        return false;
    }
    int q_head = 0;
    int q_tail = 0;

    // Visited array
    bool* visited_flat = (bool*)calloc(row * col, sizeof(bool));
    if (visited_flat == NULL) {
        free(grid_flat);
        free(q_buffer);
        return false;
    }

    // Add all land cells in the top row to the queue
    for (int c = 0; c < col; ++c) {
        if (!grid_flat[0 * col + c]) { // If it's land
            q_buffer[q_tail++] = (Cell){0, c};
            visited_flat[0 * col + c] = true;
        }
    }

    int dr[] = {-1, 1, 0, 0};
    int dc[] = {0, 0, -1, 1};

    while (q_head < q_tail) {
        Cell curr = q_buffer[q_head++];
        int r = curr.r;
        int c = curr.c;

        if (r == row - 1) { // Reached the bottom row
            free(grid_flat);
            free(q_buffer);
            free(visited_flat);
            return true;
        }

        for (int i = 0; i < 4; ++i) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (nr >= 0 && nr < row && nc >= 0 && nc < col &&
                !grid_flat[nr * col + nc] && !visited_flat[nr * col + nc]) {
                visited_flat[nr * col + nc] = true;
                q_buffer[q_tail++] = (Cell){nr, nc};
            }
        }
    }

    free(grid_flat);
    free(q_buffer);
    free(visited_flat);
    return false;
}

int latestDayToCross(int row, int col, int** cells, int cellsSize, int* cellsColSize) {
    int low = 1;
    int high = cellsSize;
    int ans = 0;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (canCross(row, col, mid, cells)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return ans;
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
    private bool CanCross(int row, int col, int dayNum, int[][] cells) {
        bool[][] grid = new bool[row][]; // false for land, true for water
        for (int i = 0; i < row; i++) {
            grid[i] = new bool[col];
        }

        for (int i = 0; i < dayNum; i++) {
            grid[cells[i][0] - 1][cells[i][1] - 1] = true; // Mark as water
        }

        Queue<(int r, int c)> q = new Queue<(int r, int c)>();
        bool[][] visited = new bool[row][];
        for (int i = 0; i < row; i++) {
            visited[i] = new bool[col];
        }

        // Add all land cells in the top row to the queue
        for (int c = 0; c < col; c++) {
            if (!grid[0][c]) { // If it's land
                q.Enqueue((0, c));
                visited[0][c] = true;
            }
        }

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        while (q.Count > 0) {
            (int r, int c) curr = q.Dequeue();

            if (curr.r == row - 1) { // Reached the bottom row
                return true;
            }

            for (int i = 0; i < 4; i++) {
                int nr = curr.r + dr[i];
                int nc = curr.c + dc[i];

                if (nr >= 0 && nr < row && nc >= 0 && nc < col &&
                    !grid[nr][nc] && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    q.Enqueue((nr, nc));
                }
            }
        }

        return false;
    }

    public int LatestDayToCross(int row, int col, int[][] cells) {
        int low = 1;
        int high = cells.Length; // Max day is when all cells are flooded
        int ans = 0;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (CanCross(row, col, mid, cells)) {
                ans = mid;
                low = mid + 1; // Try a later day
            } else {
                high = mid - 1; // Must be an earlier day
            }
        }

        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} row
 * @param {number} col
 * @param {number[][]} cells
 * @return {number}
 */
var latestDayToCross = function(row, col, cells) {

    const canCross = (dayNum) => {
        // Create a grid representing the state on dayNum
        // false for land, true for water
        const grid = Array(row).fill(0).map(() => Array(col).fill(false));
        for (let i = 0; i < dayNum; i++) {
            const r = cells[i][0] - 1;
            const c = cells[i][1] - 1;
            grid[r][c] = true; // Mark as water
        }

        // BFS to check connectivity
        const q = [];
        const visited = Array(row).fill(0).map(() => Array(col).fill(false));

        // Add all land cells in the top row to the queue
        for (let c = 0; c < col; c++) {
            if (!grid[0][c]) { // If it's land
                q.push([0, c]);
                visited[0][c] = true;
            }
        }

        // Directions for BFS
        const dr = [-1, 1, 0, 0];
        const dc = [0, 0, -1, 1];

        let head = 0;
        while (head < q.length) {
            const [r, c] = q[head++];

            if (r === row - 1) { // Reached the bottom row
                return true;
            }

            for (let i = 0; i < 4; i++) {
                const nr = r + dr[i];
                const nc = c + dc[i];

                // Check bounds
                if (nr >= 0 && nr < row && nc >= 0 && nc < col) {
                    // If it's land and not visited
                    if (!grid[nr][nc] && !visited[nr][nc]) {
                        visited[nr][nc] = true;
                        q.push([nr, nc]);
                    }
                }
            }
        }

        return false; // No path found
    };

    // Binary search for the latest day
    let low = 1;
    let high = cells.length; // Max day is when all cells are flooded
    let ans = 0;

    while (low <= high) {
        const mid = Math.floor(low + (high - low) / 2);
        if (canCross(mid)) {
            ans = mid;
            low = mid + 1; // Try a later day
        } else {
            high = mid - 1; // Must be an earlier day
        }
    }

    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function latestDayToCross(row: number, col: number, cells: number[][]): number {

    const canCross = (dayNum: number): boolean => {
        // Create a grid representing the state on dayNum
        // false for land, true for water
        const grid: boolean[][] = Array(row).fill(0).map(() => Array(col).fill(false));
        for (let i = 0; i < dayNum; i++) {
            const r = cells[i][0] - 1;
            const c = cells[i][1] - 1;
            grid[r][c] = true; // Mark as water
        }

        // BFS to check connectivity
        const q: [number, number][] = [];
        const visited: boolean[][] = Array(row).fill(0).map(() => Array(col).fill(false));

        // Add all land cells in the top row to the queue
        for (let c = 0; c < col; c++) {
            if (!grid[0][c]) { // If it's land
                q.push([0, c]);
                visited[0][c] = true;
            }
        }

        // Directions for BFS
        const dr = [-1, 1, 0, 0];
        const dc = [0, 0, -1, 1];

        let head = 0;
        while (head < q.length) {
            const [r, c] = q[head++];

            if (r === row - 1) { // Reached the bottom row
                return true;
            }

            for (let i = 0; i < 4; i++) {
                const nr = r + dr[i];
                const nc = c + dc[i];

                // Check bounds
                if (nr >= 0 && nr < row && nc >= 0 && nc < col) {
                    // If it's land and not visited
                    if (!grid[nr][nc] && !visited[nr][nc]) {
                        visited[nr][nc] = true;
                        q.push([nr, nc]);
                    }
                }
            }
        }

        return false; // No path found
    };

    // Binary search for the latest day
    let low = 1;
    let high = cells.length; // Max day is when all cells are flooded
    let ans = 0;

    while (low <= high) {
        const mid = Math.floor(low + (high - low) / 2);
        if (canCross(mid)) {
            ans = mid;
            low = mid + 1; // Try a later day
        } else {
            high = mid - 1; // Must be an earlier day
        }
    }

    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {

    /**
     * @param Integer $row
     * @param Integer $col
     * @param Integer[][] $cells
     * @return Integer
     */
    function latestDayToCross($row, $col, $cells) {

        $canCross = function($dayNum) use ($row, $col, $cells) {
            // Create a grid representing the state on dayNum
            // false for land, true for water
            $grid = array_fill(0, $row, array_fill(0, $col, false));
            for ($i = 0; $i < $dayNum; $i++) {
                $r = $cells[$i][0] - 1;
                $c = $cells[$i][1] - 1;
                $grid[$r][$c] = true; // Mark as water
            }

            // BFS to check connectivity
            $q = new SplQueue();
            $visited = array_fill(0, $row, array_fill(0, $col, false));

            // Add all land cells in the top row to the queue
            for ($c_idx = 0; $c_idx < $col; $c_idx++) {
                if (!$grid[0][$c_idx]) { // If it's land
                    $q->enqueue([0, $c_idx]);
                    $visited[0][$c_idx] = true;
                }
            }

            // Directions for BFS
            $dr = [-1, 1, 0, 0];
            $dc = [0, 0, -1, 1];

            while (!$q->isEmpty()) {
                list($r, $c) = $q->dequeue();

                if ($r === $row - 1) { // Reached the bottom row
                    return true;
                }

                for ($i = 0; $i < 4; $i++) {
                    $nr = $r + $dr[$i];
                    $nc = $c + $dc[$i];

                    // Check bounds
                    if ($nr >= 0 && $nr < $row && $nc >= 0 && $nc < $col) {
                        // If it's land and not visited
                        if (!$grid[$nr][$nc] && !$visited[$nr][$nc]) {
                            $visited[$nr][$nc] = true;
                            $q->enqueue([$nr, $nc]);
                        }
                    }
                }
            }

            return false; // No path found
        };

        // Binary search for the latest day
        $low = 1;
        $high = count($cells); // Max day is when all cells are flooded
        $ans = 0;

        while ($low <= $high) {
            $mid = floor($low + ($high - $low) / 2);
            if ($canCross($mid)) {
                $ans = $mid;
                $low = $mid + 1; // Try a later day
            } else {
                $high = $mid - 1; // Must be an earlier day
            }
        }

        return $ans;
    }
}
?>
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {
    private func canCross(_ row: Int, _ col: Int, _ dayNum: Int, _ cells: [[Int]]) -> Bool {
        var grid = Array(repeating: Array(repeating: false, count: col), count: row) // false for land, true for water
        for i in 0..<dayNum {
            grid[cells[i][0] - 1][cells[i][1] - 1] = true // Mark as water
        }

        var q = [(Int, Int)]()
        var visited = Array(repeating: Array(repeating: false, count: col), count: row)

        // Add all land cells in the top row to the queue
        for c in 0..<col {
            if !grid[0][c] { // If it's land
                q.append((0, c))
                visited[0][c] = true
            }
        }

        let dr = [-1, 1, 0, 0]
        let dc = [0, 0, -1, 1]

        var head = 0
        while head < q.count {
            let (r, c) = q[head]
            head += 1

            if r == row - 1 { // Reached the bottom row
                return true
            }

            for i in 0..<4 {
                let nr = r + dr[i]
                let nc = c + dc[i]

                if nr >= 0 && nr < row && nc >= 0 && nc < col &&
                    !grid[nr][nc] && !visited[nr][nc] {
                    visited[nr][nc] = true
                    q.append((nr, nc))
                }
            }
        }

        return false
    }

    func latestDayToCross(_ row: Int, _ col: Int, _ cells: [[Int]]) -> Int {
        var low = 1
        var high = cells.count // Max day is when all cells are flooded
        var ans = 0

        while low <= high {
            let mid = low + (high - low) / 2
            if canCross(row, col, mid, cells) {
                ans = mid
                low = mid + 1 // Try a later day
            } else {
                high = mid - 1 // Must be an earlier day
            }
        }

        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.LinkedList
import java.util.Queue

class Solution {
    private fun canCross(row: Int, col: Int, dayNum: Int, cells: Array<IntArray>): Boolean {
        val grid = Array(row) { BooleanArray(col) { false } } // false for land, true for water
        for (i in 0 until dayNum) {
            grid[cells[i][0] - 1][cells[i][1] - 1] = true // Mark as water
        }

        val q: Queue<Pair<Int, Int>> = LinkedList()
        val visited = Array(row) { BooleanArray(col) { false } }

        // Add all land cells in the top row to the queue
        for (c in 0 until col) {
            if (!grid[0][c]) { // If it's land
                q.offer(Pair(0, c))
                visited[0][c] = true
            }
        }

        val dr = intArrayOf(-1, 1, 0, 0)
        val dc = intArrayOf(0, 0, -1, 1)

        while (q.isNotEmpty()) {
            val (r, c) = q.poll()

            if (r == row - 1) { // Reached the bottom row
                return true
            }

            for (i in 0 until 4) {
                val nr = r + dr[i]
                val nc = c + dc[i]

                if (nr >= 0 && nr < row && nc >= 0 && nc < col &&
                    !grid[nr][nc] && !visited[nr][nc]) {
                    visited[nr][nc] = true
                    q.offer(Pair(nr, nc))
                }
            }
        }

        return false
    }

    fun latestDayToCross(row: Int, col: Int, cells: Array<IntArray>): Int {
        var low = 1
        var high = cells.size // Max day is when all cells are flooded
        var ans = 0

        while (low <= high) {
            val mid = low + (high - low) / 2
            if (canCross(row, col, mid, cells)) {
                ans = mid
                low = mid + 1 // Try a later day
            } else {
                high = mid - 1 // Must be an earlier day
            }
        }

        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:collection';

class Solution {
  bool _canCross(int row, int col, int dayNum, List<List<int>> cells) {
    List<List<bool>> grid = List.generate(row, (_) => List.filled(col, false)); // false for land, true for water
    for (int i = 0; i < dayNum; i++) {
      grid[cells[i][0] - 1][cells[i][1] - 1] = true; // Mark as water
    }

    Queue<List<int>> q = Queue<List<int>>();
    List<List<bool>> visited = List.generate(row, (_) => List.filled(col, false));

    // Add all land cells in the top row to the queue
    for (int c = 0; c < col; c++) {
      if (!grid[0][c]) { // If it's land
        q.add([0, c]);
        visited[0][c] = true;
      }
    }

    List<int> dr = [-1, 1, 0, 0];
    List<int> dc = [0, 0, -1, 1];

    while (q.isNotEmpty) {
      List<int> curr = q.removeFirst();
      int r = curr[0];
      int c = curr[1];

      if (r == row - 1) { // Reached the bottom row
        return true;
      }

      for (int i = 0; i < 4; i++) {
        int nr = r + dr[i];
        int nc = c + dc[i];

        if (nr >= 0 && nr < row && nc >= 0 && nc < col &&
            !grid[nr][nc] && !visited[nr][nc]) {
          visited[nr][nc] = true;
          q.add([nr, nc]);
        }
      }
    }

    return false;
  }

  int latestDayToCross(int row, int col, List<List<int>> cells) {
    int low = 1;
    int high = cells.length; // Max day is when all cells are flooded
    int ans = 0;

    while (low <= high) {
      int mid = low + (high - low) ~/ 2;
      if (_canCross(row, col, mid, cells)) {
        ans = mid;
        low = mid + 1; // Try a later day
      } else {
        high = mid - 1; // Must be an earlier day
      }
    }

    return ans;
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
	"container/list"
)

type Cell struct {
	r int
	c int
}

func canCross(row, col, dayNum int, cells [][]int) bool {
	grid := make([][]bool, row)
	for i := range grid {
		grid[i] = make([]bool, col) // false for land, true for water
	}

	for i := 0; i < dayNum; i++ {
		grid[cells[i][0]-1][cells[i][1]-1] = true // Mark as water
	}

	q := list.New()
	visited := make([][]bool, row)
	for i := range visited {
		visited[i] = make([]bool, col)
	}

	// Add all land cells in the top row to the queue
	for c := 0; c < col; c++ {
		if !grid[0][c] { // If it's land
			q.PushBack(Cell{0, c})
			visited[0][c] = true
		}
	}

	dr := []int{-1, 1, 0, 0}
	dc := []int{0, 0, -1, 1}

	for q.Len() > 0 {
		elem := q.Front()
		q.Remove(elem)
		curr := elem.Value.(Cell)
		r := curr.r
		c := curr.c

		if r == row-1 { // Reached the bottom row
			return true
		}

		for i := 0; i < 4; i++ {
			nr := r + dr[i]
			nc := c + dc[i]

			if nr >= 0 && nr < row && nc >= 0 && nc < col &&
				!grid[nr][nc] && !visited[nr][nc] {
				visited[nr][nc] = true
				q.PushBack(Cell{nr, nc})
			}
		}
	}

	return false
}

func latestDayToCross(row int, col int, cells [][]int) int {
	low := 1
	high := len(cells) // Max day is when all cells are flooded
	ans := 0

	for low <= high {
		mid := low + (high-low)/2
		if canCross(row, col, mid, cells) {
			ans = mid
			low = mid + 1 // Try a later day
		} else {
			high = mid - 1 // Must be an earlier day
		}
	}

	return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    # @param {Integer} row
    # @param {Integer} col
    # @param {Integer[][]} cells
    # @return {Integer}
    def latest_day_to_cross(row, col, cells)

        can_cross = lambda do |day_num|
            # Create a grid representing the state on day_num
            # false for land, true for water
            grid = Array.new(row) { Array.new(col, false) }
            (0...day_num).each do |i|
                r = cells[i][0] - 1
                c = cells[i][1] - 1
                grid[r][c] = true # Mark as water
            end

            # BFS to check connectivity
            q = []
            visited = Array.new(row) { Array.new(col, false) }

            # Add all land cells in the top row to the queue
            (0...col).each do |c_idx|
                if !grid[0][c_idx] # If it's land
                    q.push([0, c_idx])
                    visited[0][c_idx] = true
                end
            end

            # Directions for BFS
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]

            head = 0
            while head < q.length
                r, c = q[head]
                head += 1

                if r == row - 1 # Reached the bottom row
                    return true
                end

                (0...4).each do |i|
                    nr = r + dr[i]
                    nc = c + dc[i]

                    # Check bounds
                    if nr >= 0 && nr < row && nc >= 0 && nc < col
                        # If it's land and not visited
                        if !grid[nr][nc] && !visited[nr][nc]
                            visited[nr][nc] = true
                            q.push([nr, nc])
                        end
                    end
                end
            end

            return false # No path found
        end

        # Binary search for the latest day
        low = 1
        high = cells.length # Max day is when all cells are flooded
        ans = 0

        while low <= high
            mid = low + (high - low) / 2
            if can_cross.call(mid)
                ans = mid
                low = mid + 1 # Try a later day
            else
                high = mid - 1 # Must be an earlier day
            end
        end

        return ans
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def latestDayToCross(row: Int, col: Int, cells: Array[Array[Int]]): Int = {

        def canCross(dayNum: Int): Boolean = {
            // Create a grid representing the state on dayNum
            // false for land, true for water
            val grid: Array[Array[Boolean]] = Array.ofDim[Boolean](row, col)
            for (i <- 0 until dayNum) {
                val r = cells(i)(0) - 1
                val c = cells(i)(1) - 1
                grid(r)(c) = true // Mark as water
            }

            // BFS to check connectivity
            val q = mutable.Queue[(Int, Int)]()
            val visited: Array[Array[Boolean]] = Array.ofDim[Boolean](row, col)

            // Add all land cells in the top row to the queue
            for (c_idx <- 0 until col) {
                if (!grid(0)(c_idx)) { // If it's land
                    q.enqueue((0, c_idx))
                    visited(0)(c_idx) = true
                }
            }

            // Directions for BFS
            val dr = Array(-1, 1, 0, 0)
            val dc = Array(0, 0, -1, 1)

            while (q.nonEmpty) {
                val (r, c) = q.dequeue()

                if (r == row - 1) { // Reached the bottom row
                    return true
                }

                for (i <- 0 until 4) {
                    val nr = r + dr(i)
                    val nc = c + dc(i)

                    // Check bounds
                    if (nr >= 0 && nr < row && nc >= 0 && nc < col) {
                        // If it's land and not visited
                        if (!grid(nr)(nc) && !visited(nr)(nc)) {
                            visited(nr)(nc) = true
                            q.enqueue((nr, nc))
                        }
                    }
                }
            }

            return false // No path found
        }

        // Binary search for the latest day
        var low = 1
        var high = cells.length // Max day is when all cells are flooded
        var ans = 0

        while (low <= high) {
            val mid = low + (high - low) / 2
            if (canCross(mid)) {
                ans = mid
                low = mid + 1 // Try a later day
            } else {
                high = mid - 1 // Must be an earlier day
            }
        }

        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::VecDeque;

struct Solution;

impl Solution {
    fn can_cross(row: i32, col: i32, day_num: usize, cells: &Vec<Vec<i32>>) -> bool {
        let mut grid = vec![vec![false; col as usize]; row as usize]; // false for land, true for water
        for i in 0..day_num {
            let r = cells[i][0] as usize - 1;
            let c = cells[i][1] as usize - 1;
            grid[r][c] = true; // Mark as water
        }

        let mut q = VecDeque::new();
        let mut visited = vec![vec![false; col as usize]; row as usize];

        // Add all land cells in the top row to the queue
        for c_idx in 0..col {
            if !grid[0][c_idx as usize] { // If it's land
                q.push_back((0, c_idx));
                visited[0][c_idx as usize] = true;
            }
        }

        let dr = [-1, 1, 0, 0];
        let dc = [0, 0, -1, 1];

        while let Some((r, c)) = q.pop_front() {
            if r == row - 1 { // Reached the bottom row
                return true;
            }

            for i in 0..4 {
                let nr = r + dr[i];
                let nc = c + dc[i];

                if nr >= 0 && nr < row && nc >= 0 && nc < col {
                    if !grid[nr as usize][nc as usize] && !visited[nr as usize][nc as usize] {
                        visited[nr as usize][nc as usize] = true;
                        q.push_back((nr, nc));
                    }
                }
            }
        }

        false // No path found
    }

    pub fn latest_day_to_cross(row: i32, col: i32, cells: Vec<Vec<i32>>) -> i32 {
        let mut low = 1;
        let mut high = cells.len() as i32; // Max day is when all cells are flooded
        let mut ans = 0;

        while low <= high {
            let mid = low + (high - low) / 2;
            if Self::can_cross(row, col, mid as usize, &cells) {
                ans = mid;
                low = mid + 1; // Try a later day
            } else {
                high = mid - 1; // Must be an earlier day
            }
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
#lang racket

(define (latest-day-to-cross row col cells)

  (define (can-cross day-num)
    ;; Create a grid representing the state on day-num
    ;; #f for land, #t for water
    (define grid (make-vector row (make-vector col #f)))
    (for ([i (in-range day-num)])
      (define cell (vector-ref cells i))
      (define r (- (vector-ref cell 0) 1))
      (define c (- (vector-ref cell 1) 1))
      (vector-set! (vector-ref grid r) c #t) ; Mark as water
      )

    ;; BFS to check connectivity
    (define q (make-queue))
    (define visited (make-vector row (make-vector col #f)))

    ;; Add all land cells in the top row to the queue
    (for ([c-idx (in-range col)])
      (when (not (vector-ref (vector-ref grid 0) c-idx)) ; If it's land
        (queue-enqueue! q (list 0 c-idx))
        (vector-set! (vector-ref visited 0) c-idx #t)
        ))

    ;; Directions for BFS
    (define dr '(-1 1 0 0))
    (define dc '(0 0 -1 1))

    (let loop ()
      (when (not (queue-empty? q))
        (define curr (queue-dequeue! q))
        (define r (car curr))
        (define c (cadr curr))

        (when (= r (- row 1)) ; Reached the bottom row
          (void (queue-clear! q)) ; Clear queue to stop loop
          (error 'can-cross "Should not reach here if true")) ; This is a hack, will return true below

        (for ([i (in-range 4)])
          (define nr (+ r (list-ref dr i)))
          (define nc (+ c (list-ref dc i)))

          ;; Check bounds
          (when (and (>= nr 0) (< nr row) (>= nc 0) (< nc col))
            ;; If it's land and not visited
            (when (and (not (vector-ref (vector-ref grid nr) nc))
                       (not (vector-ref (vector-ref visited nr) nc)))
              (vector-set! (vector-ref visited nr) nc #t)
              (queue-enqueue! q (list nr nc))
              ))
          )
        (loop)
        ))

    ;; After BFS, check if any bottom row cell was visited
    (for/or ([c (in-range col)])
      (vector-ref (vector-ref visited (- row 1)) c))
    )

  ;; Binary search for the latest day
  (define low 1)
  (define high (vector-length cells)) ; Max day is when all cells are flooded
  (define ans 0)

  (let loop ( (l low) (h high) (a ans) )
    (if (<= l h)
        (let* ([mid (+ l (quotient (- h l) 2))])
          (if (can-cross mid)
              (loop (+ mid 1) h mid) ; Try a later day
              (loop l (- mid 1) a)   ; Must be an earlier day
              ))
        a))
  )

;; Helper for queue (Racket's queue is mutable)
(define (make-queue) (make-mutable-queue))
(define (queue-enqueue! q item) (mutable-queue-enqueue! q item))
(define (queue-dequeue! q) (mutable-queue-dequeue! q))
(define (queue-empty? q) (mutable-queue-empty? q))
(define (queue-clear! q) (mutable-queue-clear! q))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([latest_day_to_cross/3]).

latest_day_to_cross(Row, Col, Cells) ->
    Low = 1,
    High = length(Cells),
    binary_search(Low, High, 0, Row, Col, Cells).

binary_search(Low, High, Ans, Row, Col, Cells) when Low =< High ->
    Mid = Low + (High - Low) div 2,
    case can_cross(Row, Col, Mid, Cells) of
        true -> binary_search(Mid + 1, High, Mid, Row, Col, Cells);
        false -> binary_search(Low, Mid - 1, Ans, Row, Col, Cells)
    end;
binary_search(_, _, Ans, _, _, _) ->
    Ans.

can_cross(Row, Col, DayNum, Cells) ->
    Grid = create_grid(Row, Col, DayNum, Cells),

    Q = queue:new(),
    Visited = create_visited(Row, Col),

    % Add all land cells in the top row to the queue
    {Q1, Visited1} = lists:foldl(
        fun(C_idx, {AccQ, AccVisited}) ->
            case get_grid_val(Grid, 0, C_idx, Col) of
                false -> % If it's land
                    NewQ = queue:in({0, C_idx}, AccQ),
                    NewVisited = set_visited(AccVisited, 0, C_idx, Col, true),
                    {NewQ, NewVisited};
                true ->
                    {AccQ, AccVisited}
            end
        end, {Q, Visited}, lists:seq(0, Col - 1)),

    bfs(Q1, Visited1, Row, Col, Grid).

bfs(Q, Visited, Row, Col, Grid) ->
    case queue:out(Q) of
        {{value, {R, C}}, RestQ} ->
            if R == Row - 1 ->
                true;
            true ->
                DR = [-1, 1, 0, 0],
                DC = [0, 0, -1, 1],

                {NewQ, NewVisited} = lists:foldl(
                    fun(I, {AccQ, AccVisited}) ->
                        NR = R + lists:nth(I + 1, DR),
                        NC = C + lists:nth(I + 1, DC),

                        if NR >= 0 andalso NR < Row andalso NC >= 0 andalso NC < Col ->
                            case get_grid_val(Grid, NR, NC, Col) of
                                false -> % If it's land
                                    case get_visited(AccVisited, NR, NC, Col) of
                                        false ->
                                            NewQ = queue:in({NR, NC}, AccQ),
                                            NewVisited = set_visited(AccVisited, NR, NC, Col, true),
                                            {NewQ, NewVisited};
                                        true ->
                                            {AccQ, AccVisited}
                                    end;
                                true ->
                                    {AccQ, AccVisited}
                            end;
                        true ->
                            {AccQ, AccVisited}
                        end
                    end, {RestQ, Visited}, lists:seq(0, 3)),
                bfs(NewQ, NewVisited, Row, Col, Grid)
            end;
        {empty, _} ->
            false
    end.

create_grid(Row, Col, DayNum, Cells) ->
    Grid = array:new([{size, Row * Col}, {fixed, true}, {default, false}]),
    lists:foldl(
        fun(I, AccGrid) ->
            Cell = lists:nth(I + 1, Cells),
            R = lists:nth(1, Cell) - 1,
            C = lists:nth(2, Cell) - 1,
            array:set(R * Col + C, true, AccGrid)
        end, Grid, lists:seq(0, DayNum - 1)).

get_grid_val(Grid, R, C, Col) ->
    array:get(R * Col + C, Grid).

create_visited(Row, Col) ->
    array:new([{size, Row * Col}, {fixed, true}, {default, false}]).

get_visited(Visited, R, C, Col) ->
    array:get(R * Col + C, Visited).

set_visited(Visited, R, C, Col, Val) ->
    array:set(R * Col + C, Val, Visited).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  def latest_day_to_cross(row, col, cells) do
    low = 1
    high = length(cells)
    binary_search(low, high, 0, row, col, cells)
  end

  defp binary_search(low, high, ans, row, col, cells) when low <= high do
    mid = low + div(high - low, 2)
    if can_cross(row, col, mid, cells) do
      binary_search(mid + 1, high, mid, row, col, cells)
    else
      binary_search(low, mid - 1, ans, row, col, cells)
    end
  end
  defp binary_search(_, _, ans, _, _, _), do: ans

  defp can_cross(row, col, day_num, cells) do
    grid = create_grid(row, col, day_num, cells)

    q = :queue.new()
    visited = create_visited(row, col)

    # Add all land cells in the top row to the queue
    {q_init, visited_init} = Enum.reduce(0..(col - 1), {q, visited}, fn c_idx, {acc_q, acc_visited} ->
      case get_grid_val(grid, 0, c_idx, col) do
        false -> # If it's land
          new_q = :queue.in({0, c_idx}, acc_q)
          new_visited = set_visited(acc_visited, 0, c_idx, col, true)
          {new_q, new_visited}
        true ->
          {acc_q, acc_visited}
      end
    end)

    bfs(q_init, visited_init, row, col, grid)
  end

  defp bfs(q, visited, row, col, grid) do
    case :queue.out(q) do
      {{:value, {r, c}}, rest_q} ->
        if r == row - 1 do
          true
        else
          dr = [-1, 1, 0, 0]
          dc = [0, 0, -1, 1]

          {new_q, new_visited} = Enum.reduce(0..3, {rest_q, visited}, fn i, {acc_q, acc_visited} ->
            nr = r + Enum.at(dr, i)
            nc = c + Enum.at(dc, i)

            if nr >= 0 and nr < row and nc >= 0 and nc < col do
              case get_grid_val(grid, nr, nc, col) do
                false -> # If it's land
                  case get_visited(acc_visited, nr, nc, col) do
                    false ->
                      new_q = :queue.in({nr, nc}, acc_q)
                      new_visited = set_visited(acc_visited, nr, nc, col, true)
                      {new_q, new_visited}
                    true ->
                      {acc_q, acc_visited}
                  end
                true ->
                  {acc_q, acc_visited}
              end
            else
              {acc_q, acc_visited}
            end
          end)
          bfs(new_q, new_visited, row, col, grid)
        end
      {:empty, _} ->
        false
    end
  end

  defp create_grid(row, col, day_num, cells) do
    grid = :array.new([{:size, row * col}, {:fixed, true}, {:default, false}])
    Enum.reduce(0..(day_num - 1), grid, fn i, acc_grid ->
      [r_cell, c_cell] = Enum.at(cells, i)
      r = r_cell - 1
      c = c_cell - 1
      :array.set(r * col + c, true, acc_grid)
    end)
  end

  defp get_grid_val(grid, r, c, col), do: :array.get(r * col + c, grid)

  defp create_visited(row, col), do: :array.new([{:size, row * col}, {:fixed, true}, {:default, false}])

  defp get_visited(visited, r, c, col), do: :array.get(r * col + c, visited)

  defp set_visited(visited, r, c, col, val), do: :array.set(r * col + c, val, visited)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(row * col * log(row * col)). The binary search performs O(log(row * col)) iterations. In each iteration, the `can_cross` function initializes a grid and performs a BFS. Initializing the grid takes O(row * col) time (to set all cells to land and then mark `day_num` cells as water). The BFS itself visits each cell and edge at most once, taking O(row * col) time. Thus, each call to `can_cross` is O(row * col).

- **Space Complexity:** The space complexity is O(row * col). This is primarily due to storing the grid state (boolean matrix) and the `visited` matrix for the BFS, both of which are of size `row * col`. Additionally, the BFS queue can store up to O(row * col) cells in the worst case.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-31 01:11:36 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved using a graph algorithm and binary search. We start by initializing a 2D grid with all land cells. Then, we use binary search to find the last day where it is possible to walk from the top to the bottom by only walking on land cells. For each day in the binary search range, we update the grid according to the given cells and check if there is a path from the top to the bottom using a depth-first search (DFS) algorithm. If there is a path, we update the lower bound of the binary search range; otherwise, we update the upper bound. The key intuition is that the problem can be reduced to finding the last day where the top and bottom rows are connected in the grid.

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
    int latestDayToCross(int row, int col, vector<vector<int>>& cells) {
        int low = 0, high = cells.size() - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            vector<vector<int>> grid(row, vector<int>(col, 0));
            for (int i = 0; i <= mid; i++) {
                grid[cells[i][0] - 1][cells[i][1] - 1] = 1;
            }
            if (canCross(grid)) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return low - 1;
    }

    bool canCross(vector<vector<int>>& grid) {
        int row = grid.size(), col = grid[0].size();
        vector<vector<bool>> visited(row, vector<bool>(col, false));
        for (int i = 0; i < row; i++) {
            if (dfs(grid, visited, i, 0)) {
                return true;
            }
        }
        return false;
    }

    bool dfs(vector<vector<int>>& grid, vector<vector<bool>>& visited, int x, int y) {
        int row = grid.size(), col = grid[0].size();
        if (y == col - 1) {
            return true;
        }
        visited[x][y] = true;
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (auto& dir : directions) {
            int nx = x + dir[0], ny = y + dir[1];
            if (nx >= 0 && nx < row && ny >= 0 && ny < col && !visited[nx][ny] && grid[nx][ny] == 0) {
                if (dfs(grid, visited, nx, ny)) {
                    return true;
                }
            }
        }
        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int latestDayToCross(int row, int col, int[][] cells) {
        int low = 0, high = cells.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int[][] grid = new int[row][col];
            for (int i = 0; i <= mid; i++) {
                grid[cells[i][0] - 1][cells[i][1] - 1] = 1;
            }
            if (canCross(grid)) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return low - 1;
    }

    private boolean canCross(int[][] grid) {
        int row = grid.length, col = grid[0].length;
        boolean[][] visited = new boolean[row][col];
        for (int i = 0; i < row; i++) {
            if (dfs(grid, visited, i, 0)) {
                return true;
            }
        }
        return false;
    }

    private boolean dfs(int[][] grid, boolean[][] visited, int x, int y) {
        int row = grid.length, col = grid[0].length;
        if (y == col - 1) {
            return true;
        }
        visited[x][y] = true;
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (int[] dir : directions) {
            int nx = x + dir[0], ny = y + dir[1];
            if (nx >= 0 && nx < row && ny >= 0 && ny < col && !visited[nx][ny] && grid[nx][ny] == 0) {
                if (dfs(grid, visited, nx, ny)) {
                    return true;
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
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        low, high = 0, len(cells) - 1
        while low <= high:
            mid = (low + high) // 2
            grid = [[0] * col for _ in range(row)]
            for i in range(mid + 1):
                grid[cells[i][0] - 1][cells[i][1] - 1] = 1
            if self.canCross(grid):
                low = mid + 1
            else:
                high = mid - 1
        return low - 1

    def canCross(self, grid):
        row, col = len(grid), len(grid[0])
        visited = [[False] * col for _ in range(row)]
        for i in range(row):
            if self.dfs(grid, visited, i, 0):
                return True
        return False

    def dfs(self, grid, visited, x, y):
        row, col = len(grid), len(grid[0])
        if y == col - 1:
            return True
        visited[x][y] = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and grid[nx][ny] == 0:
                if self.dfs(grid, visited, nx, ny):
                    return True
        return False
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        low, high = 0, len(cells) - 1
        while low <= high:
            mid = (low + high) // 2
            grid = [[0] * col for _ in range(row)]
            for i in range(mid + 1):
                grid[cells[i][0] - 1][cells[i][1] - 1] = 1
            if self.canCross(grid):
                low = mid + 1
            else:
                high = mid - 1
        return low - 1

    def canCross(self, grid):
        row, col = len(grid), len(grid[0])
        visited = [[False] * col for _ in range(row)]
        for i in range(row):
            if self.dfs(grid, visited, i, 0):
                return True
        return False

    def dfs(self, grid, visited, x, y):
        row, col = len(grid), len(grid[0])
        if y == col - 1:
            return True
        visited[x][y] = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and grid[nx][ny] == 0:
                if self.dfs(grid, visited, nx, ny):
                    return True
        return False
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int** grid;
    int row;
    int col;
} Solution;

Solution* solutionCreate(int row, int col) {
    Solution* obj = (Solution*) malloc(sizeof(Solution));
    obj->row = row;
    obj->col = col;
    obj->grid = (int**) malloc(row * sizeof(int*));
    for (int i = 0; i < row; i++) {
        obj->grid[i] = (int*) malloc(col * sizeof(int));
    }
    return obj;
}

int solutionLatestDayToCross(Solution* obj, int** cells, int cellsSize) {
    int low = 0, high = cellsSize - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        for (int i = 0; i < obj->row; i++) {
            for (int j = 0; j < obj->col; j++) {
                obj->grid[i][j] = 0;
            }
        }
        for (int i = 0; i <= mid; i++) {
            obj->grid[cells[i][0] - 1][cells[i][1] - 1] = 1;
        }
        if (canCross(obj->grid, obj->row, obj->col)) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return low - 1;
}

int canCross(int** grid, int row, int col) {
    int** visited = (int**) malloc(row * sizeof(int*));
    for (int i = 0; i < row; i++) {
        visited[i] = (int*) malloc(col * sizeof(int));
    }
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            visited[i][j] = 0;
        }
    }
    for (int i = 0; i < row; i++) {
        if (dfs(grid, visited, i, 0, row, col)) {
            return 1;
        }
    }
    return 0;
}

int dfs(int** grid, int** visited, int x, int y, int row, int col) {
    if (y == col - 1) {
        return 1;
    }
    visited[x][y] = 1;
    int directions[][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    for (int i = 0; i < 4; i++) {
        int nx = x + directions[i][0], ny = y + directions[i][1];
        if (nx >= 0 && nx < row && ny >= 0 && ny < col && !visited[nx][ny] && grid[nx][ny] == 0) {
            if (dfs(grid, visited, nx, ny, row, col)) {
                return 1;
            }
        }
    }
    return 0;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int LatestDayToCross(int row, int col, int[][] cells) {
        int low = 0, high = cells.Length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int[][] grid = new int[row][];
            for (int i = 0; i < row; i++) {
                grid[i] = new int[col];
            }
            for (int i = 0; i <= mid; i++) {
                grid[cells[i][0] - 1][cells[i][1] - 1] = 1;
            }
            if (CanCross(grid)) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return low - 1;
    }

    private bool CanCross(int[][] grid) {
        int row = grid.Length, col = grid[0].Length;
        bool[][] visited = new bool[row][];
        for (int i = 0; i < row; i++) {
            visited[i] = new bool[col];
        }
        for (int i = 0; i < row; i++) {
            if (Dfs(grid, visited, i, 0)) {
                return true;
            }
        }
        return false;
    }

    private bool Dfs(int[][] grid, bool[][] visited, int x, int y) {
        int row = grid.Length, col = grid[0].Length;
        if (y == col - 1) {
            return true;
        }
        visited[x][y] = true;
        int[][] directions = { new int[] { -1, 0 }, new int[] { 1, 0 }, new int[] { 0, -1 }, new int[] { 0, 1 } };
        for (int i = 0; i < 4; i++) {
            int nx = x + directions[i][0], ny = y + directions[i][1];
            if (nx >= 0 && nx < row && ny >= 0 && ny < col && !visited[nx][ny] && grid[nx][ny] == 0) {
                if (Dfs(grid, visited, nx, ny)) {
                    return true;
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
var latestDayToCross = function(row, col, cells) {
    let low = 0, high = cells.length - 1;
    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        let grid = Array(row).fill(0).map(() => Array(col).fill(0));
        for (let i = 0; i <= mid; i++) {
            grid[cells[i][0] - 1][cells[i][1] - 1] = 1;
        }
        if (canCross(grid)) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return low - 1;
};

var canCross = function(grid) {
    let row = grid.length, col = grid[0].length;
    let visited = Array(row).fill(0).map(() => Array(col).fill(false));
    for (let i = 0; i < row; i++) {
        if (dfs(grid, visited, i, 0)) {
            return true;
        }
    }
    return false;
};

var dfs = function(grid, visited, x, y) {
    let row = grid.length, col = grid[0].length;
    if (y === col - 1) {
        return true;
    }
    visited[x][y] = true;
    let directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    for (let i = 0; i < 4; i++) {
        let nx = x + directions[i][0], ny = y + directions[i][1];
        if (nx >= 0 && nx < row && ny >= 0 && ny < col && !visited[nx][ny] && grid[nx][ny] === 0) {
            if (dfs(grid, visited, nx, ny)) {
                return true;
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
function latestDayToCross(row: number, col: number, cells: number[][]): number {
    let low: number = 0, high: number = cells.length - 1;
    while (low <= high) {
        let mid: number = Math.floor((low + high) / 2);
        let grid: number[][] = Array(row).fill(0).map(() => Array(col).fill(0));
        for (let i: number = 0; i <= mid; i++) {
            grid[cells[i][0] - 1][cells[i][1] - 1] = 1;
        }
        if (canCross(grid)) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return low - 1;
}

function canCross(grid: number[][]): boolean {
    let row: number = grid.length, col: number = grid[0].length;
    let visited: boolean[][] = Array(row).fill(0).map(() => Array(col).fill(false));
    for (let i: number = 0; i < row; i++) {
        if (dfs(grid, visited, i, 0)) {
            return true;
        }
    }
    return false;
}

function dfs(grid: number[][], visited: boolean[][], x: number, y: number): boolean {
    let row: number = grid.length, col: number = grid[0].length;
    if (y === col - 1) {
        return true;
    }
    visited[x][y] = true;
    let directions: number[][] = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    for (let i: number = 0; i < 4; i++) {
        let nx: number = x + directions[i][0], ny: number = y + directions[i][1];
        if (nx >= 0 && nx < row && ny >= 0 && ny < col && !visited[nx][ny] && grid[nx][ny] === 0) {
            if (dfs(grid, visited, nx, ny)) {
                return true;
            }
        }
    }
    return false;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function latestDayToCross($row, $col, $cells) {
        $low = 0; $high = count($cells) - 1;
        while ($low <= $high) {
            $mid = floor(($low + $high) / 2);
            $grid = array_fill(0, $row, array_fill(0, $col, 0));
            for ($i = 0; $i <= $mid; $i++) {
                $grid[$cells[$i][0] - 1][$cells[$i][1] - 1] = 1;
            }
            if ($this->canCross($grid)) {
                $low = $mid + 1;
            } else {
                $high = $mid - 1;
            }
        }
        return $low - 1;
    }

    function canCross($grid) {
        $row = count($grid); $col = count($grid[0]);
        $visited = array_fill(0, $row, array_fill(0, $col, false));
        for ($i = 0; $i < $row; $i++) {
            if ($this->dfs($grid, $visited, $i, 0)) {
                return true;
            }
        }
        return false;
    }

    function dfs($grid, &$visited, $x, $y) {
        $row = count($grid); $col = count($grid[0]);
        if ($y == $col - 1) {
            return true;
        }
        $visited[$x][$y] = true;
        $directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        for ($i = 0; $i < 4; $i++) {
            $nx = $x + $directions[$i][0]; $ny = $y + $directions[$i][1];
            if ($nx >= 0 && $nx < $row && $ny >= 0 && $ny < $col && !$visited[$nx][$ny] && $grid[$nx][$ny] == 0) {
                if ($this->dfs($grid, $visited, $nx, $ny)) {
                    return true;
                }
            }
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
    func latestDayToCross(_ row: Int, _ col: Int, _ cells: [[Int]]) -> Int {
        var low: Int = 0, high: Int = cells.count - 1
        while low <= high {
            let mid: Int = low + (high - low) / 2
            var grid: [[Int]] = Array(repeating: Array(repeating: 0, count: col), count: row)
            for i in 0...mid {
                grid[cells[i][0] - 1][cells[i][1] - 1] = 1
            }
            if canCross(grid) {
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        return low - 1
    }

    func canCross(_ grid: [[Int]]) -> Bool {
        let row: Int = grid.count, col: Int = grid[0].count
        var visited: [[Bool]] = Array(repeating: Array(repeating: false, count: col), count: row)
        for i in 0..<row {
            if dfs(grid, &visited, i, 0) {
                return true
            }
        }
        return false
    }

    func dfs(_ grid: [[Int]], _ visited: inout [[Bool]], _ x: Int, _ y: Int) -> Bool {
        let row: Int = grid.count, col: Int = grid[0].count
        if y == col - 1 {
            return true
        }
        visited[x][y] = true
        let directions: [(Int, Int)] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in 0..<4 {
            let nx: Int = x + directions[i].0, ny: Int = y + directions[i].1
            if nx >= 0 && nx < row && ny >= 0 && ny < col && !visited[nx][ny] && grid[nx][ny] == 0 {
                if dfs(grid, &visited, nx, ny) {
                    return true
                }
            }
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
    fun latestDayToCross(row: Int, col: Int, cells: Array<IntArray>): Int {
        var low: Int = 0
        var high: Int = cells.size - 1
        while (low <= high) {
            val mid: Int = low + (high - low) / 2
            val grid: Array<IntArray> = Array(row) { IntArray(col) { 0 } }
            for (i in 0..mid) {
                grid[cells[i][0] - 1][cells[i][1] - 1] = 1
            }
            if (canCross(grid)) {
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        return low - 1
    }

    fun canCross(grid: Array<IntArray>): Boolean {
        val row: Int = grid.size
        val col: Int = grid[0].size
        val visited: Array<BooleanArray> = Array(row) { BooleanArray(col) { false } }
        for (i in 0 until row) {
            if (dfs(grid, visited, i, 0)) {
                return true
            }
        }
        return false
    }

    fun dfs(grid: Array<IntArray>, visited: Array<BooleanArray>, x: Int, y: Int): Boolean {
        val row: Int = grid.size
        val col: Int = grid[0].size
        if (y == col - 1) {
            return true
        }
        visited[x][y] = true
        val directions: Array<IntArray> = arrayOf(intArrayOf(-1, 0), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(0, 1))
        for (i in 0 until 4) {
            val nx: Int = x + directions[i][0]
            val ny: Int = y + directions[i][1]
            if (nx in 0 until row && ny in 0 until col && !visited[nx][ny] && grid[nx][ny] == 0) {
                if (dfs(grid, visited, nx, ny)) {
                    return true
                }
            }
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
    int latestDayToCross(int row, int col, List<List<int>> cells) {
        int low = 0, high = cells.length - 1;
        while (low <= high) {
            int mid = low + (high - low) ~/ 2;
            List<List<int>> grid = List.generate(row, (i) => List.generate(col, (j) => 0));
            for (int i = 0; i <= mid; i++) {
                grid[cells[i][0] - 1][cells[i][1] - 1] = 1;
            }
            if (canCross(grid)) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return low - 1;
    }

    bool canCross(List<List<int>> grid) {
        int row = grid.length, col = grid[0].length;
        List<List<bool>> visited = List.generate(row, (i) => List.generate(col, (j) => false));
        for (int i = 0; i < row; i++) {
            if (dfs(grid, visited, i, 0)) {
                return true;
            }
        }
        return false;
    }

    bool dfs(List<List<int>> grid, List<List<bool>> visited, int x, int y) {
        int row = grid.length, col = grid[0].length;
        if (y == col - 1) {
            return true;
        }
        visited[x][y] = true;
        List<List<int>> directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        for (int i = 0; i < 4; i++) {
            int nx = x + directions[i][0], ny = y + directions[i][1];
            if (nx >= 0 && nx < row && ny >= 0 && ny < col && !visited[nx][ny] && grid[nx][ny] == 0) {
                if (dfs(grid, visited, nx, ny)) {
                    return true;
                }
            }
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
package main

import (
    "fmt"
)

type Solution struct{}

func (s *Solution) latestDayToCross(row int, col int, cells [][]int) int {
    low, high := 0, len(cells)-1
    for low <= high {
        mid := low + (high-low)/2
        grid := make([][]int, row)
        for i := range grid {
            grid[i] = make([]int, col)
        }
        for i := 0; i <= mid; i++ {
            grid[cells[i][0]-1][cells[i][1]-1] = 1
        }
        if s.canCross(grid) {
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    return low - 1
}

func (s *Solution) canCross(grid [][]int) bool {
    row, col := len(grid), len(grid[0])
    visited := make([][]bool, row)
    for i := range visited {
        visited[i] = make([]bool, col)
    }
    for i := 0; i < row; i++ {
        if s.dfs(grid, visited, i, 0) {
            return true
        }
    }
    return false
}

func (s *Solution) dfs(grid [][]int, visited [][]bool, x, y int) bool {
    row, col := len(grid), len(grid[0])
    if y == col-1 {
        return true
    }
    visited[x][y] = true
    directions := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
    for i := 0; i < 4; i++ {
        nx, ny := x+directions[i][0], y+directions[i][1]
        if nx >= 0 && nx < row && ny >= 0 && ny < col && !visited[nx][ny] && grid[nx][ny] == 0 {
            if s.dfs(grid, visited, nx, ny) {
                return true
            }
        }
    }
    return false
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def latest_day_to_cross(row, col, cells)
        low, high = 0, cells.size - 1
        while low <= high
            mid = low + (high - low) / 2
            grid = Array.new(row) { Array.new(col, 0) }
            (0..mid).each do |i|
                grid[cells[i][0] - 1][cells[i][1] - 1] = 1
            end
            if can_cross(grid)
                low = mid + 1
            else
                high = mid - 1
            end
        end
        low - 1
    end

    def can_cross(grid)
        row, col = grid.size, grid[0].size
        visited = Array.new(row) { Array.new(col, false) }
        (0...row).each do |i|
            return true if dfs(grid, visited, i, 0)
        end
        false
    end

    def dfs(grid, visited, x, y)
        row, col = grid.size, grid[0].size
        return true if y == col - 1
        visited[x][y] = true
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        (0...4).each do |i|
            nx, ny = x + directions[i][0], y + directions[i][1]
            if nx >= 0 && nx < row && ny >= 0 && ny < col && !visited[nx][ny] && grid[nx][ny] == 0
                return true if dfs(grid, visited, nx, ny)
            end
        end
        false
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def latestDayToCross(row: Int, col: Int, cells: Array[Array[Int]]): Int = {
        var low: Int = 0
        var high: Int = cells.length - 1
        while (low <= high) {
            val mid: Int = low + (high - low) / 2
            val grid: Array[Array[Int]] = Array.ofDim[Int](row, col)
            for (i <- 0 to mid) {
                grid(cells(i)(0) - 1)(cells(i)(1) - 1) = 1
            }
            if (canCross(grid)) {
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        low - 1
    }

    def canCross(grid: Array[Array[Int]]): Boolean = {
        val row: Int = grid.length
        val col: Int = grid(0).length
        val visited: Array[Array[Boolean]] = Array.ofDim[Boolean](row, col)
        for (i <- 0 until row) {
            if (dfs(grid, visited, i, 0)) {
                return true
            }
        }
        false
    }

    def dfs(grid: Array[Array[Int]], visited: Array[Array[Boolean]], x: Int, y: Int): Boolean = {
        val row: Int = grid.length
        val col: Int = grid(0).length
        if (y == col - 1) {
            return true
        }
        visited(x)(y) = true
        val directions: Array[Array[Int]] = Array.ofDim[Int](4, 2)
        directions(0) = Array(-1, 0)
        directions(1) = Array(1, 0)
        directions(2) = Array(0, -1)
        directions(3) = Array(0, 1)
        for (i <- 0 until 4) {
            val nx: Int = x + directions(i)(0)
            val ny: Int = y + directions(i)(1)
            if (nx >= 0 && nx < row && ny >= 0 && ny < col && !visited(nx)(ny) && grid(nx)(ny) == 0) {
                if (dfs(grid, visited, nx, ny)) {
                    return true
                }
            }
        }
        false
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
    pub fn latest_day_to_cross(row: i32, col: i32, cells: Vec<Vec<i32>>) -> i32 {
        let mut low: i32 = 0;
        let mut high: i32 = cells.len() as i32 - 1;
        while low <= high {
            let mid: i32 = low + (high - low) / 2;
            let mut grid: Vec<Vec<i32>> = vec![vec![0; col as usize]; row as usize];
            for i in 0..=mid {
                grid[cells[i as usize][0] as usize - 1][cells[i as usize][1] as usize - 1] = 1;
            }
            if Solution::can_cross(&grid) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        low - 1
    }

    pub fn can_cross(grid: &Vec<Vec<i32>>) -> bool {
        let row: usize = grid.len();
        let col: usize = grid[0].len();
        let mut visited: Vec<Vec<bool>> = vec![vec![false; col]; row];
        for i in 0..row {
            if Solution::dfs(&grid, &mut visited, i, 0) {
                return true;
            }
        }
        false
    }

    pub fn dfs(grid: &Vec<Vec<i32>>, visited: &mut Vec<Vec<bool>>, x: usize, y: usize) -> bool {
        let row: usize = grid.len();
        let col: usize = grid[0].len();
        if y == col - 1 {
            return true;
        }
        visited[x][y] = true;
        let directions: Vec<(i32, i32)> = vec![(-1, 0), (1, 0), (0, -1), (0, 1)];
        for i in 0..4 {
            let nx: i32 = x as i32 + directions[i].0;
            let ny: i32 = y as i32 + directions[i].1;
            if nx >= 0 && nx < row as i32 && ny >= 0 && ny < col as i32 && !visited[nx as usize][ny as usize] && grid[nx as usize][ny as usize] == 0 {
                if Solution::dfs(&grid, visited, nx as usize, ny as usize) {
                    return true;
                }
            }
        }
        false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define (latest-day-to-cross row col cells)
    (let loop ((low 0) (high (sub1 (length cells))))
        (if (> low high)
            (sub1 low)
            (let ((mid (quotient (+ low high) 2)))
                (let ((grid (make-grid row col)))
                    (for ((i (range (add1 mid))))
                        (grid-set! grid (sub1 (list-ref (list-ref cells i) 0)) (sub1 (list-ref (list-ref cells i) 1)) 1))
                    (if (can-cross? grid)
                        (loop (add1 mid) high)
                        (loop low (sub1 mid)))))))

(define (can-cross? grid)
    (let ((row (grid-rows grid)) (col (grid-cols grid)) (visited (make-visited row col)))
        (let loop ((i 0))
            (if (= i row)
                #f
                (if (dfs grid visited i 0)
                    #t
                    (loop (add1 i))))))

(define (dfs grid visited x y)
    (if (= y (sub1 (grid-cols grid)))
        #t
        (begin
            (visited-set! visited x y #t)
            (let loop ((i 0))
                (if (= i 4)
                    #f
                    (let ((nx (+ x (list-ref (list-ref directions i) 0))) (ny (+ y (list-ref (list-ref directions i) 1))))
                        (if (and (>= nx 0) (< nx (grid-rows grid)) (>= ny 0) (< ny (grid-cols grid)) (not (visited-ref visited nx ny)) (= (grid-ref grid nx ny) 0))
                            (if (dfs grid visited nx ny)
                                #t
                                (loop (add1 i)))
                            (loop (add1 i)))))))))

(define directions (list (list -1 0) (list 1 0) (list 0 -1) (list 0 1)))

(define (make-grid row col)
    (build-list row (lambda (x) (build-list col (lambda (y) 0)))))

(define (grid-rows grid) (length grid))
(define (grid-cols grid) (length (list-ref grid 0)))
(define (grid-ref grid x y) (list-ref (list-ref grid x) y))
(define (grid-set! grid x y val) (list-set! (list-ref grid x) y val))

(define (make-visited row col)
    (build-list row (lambda (x) (build-list col (lambda (y) #f)))))

(define (visited-ref visited x y) (list-ref (list-ref visited x) y))
(define (visited-set! visited x y val) (list-set! (list-ref visited x) y val))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
latest_day_to_cross(Row, Col, Cells) ->
    Low = 0,
    High = length(Cells) - 1,
    loop(Low, High, Cells, Row, Col).

loop(Low, High, Cells, Row, Col) when Low > High -> Low - 1;
loop(Low, High, Cells, Row, Col) ->
    Mid = Low + (High - Low) div 2,
    Grid = create_grid(Row, Col),
    update_grid(Grid, Cells, Mid),
    case can_cross(Grid) of
        true -> loop(Mid + 1, High, Cells, Row, Col);
        false -> loop(Low, Mid - 1, Cells, Row, Col)
    end.

create_grid(Row, Col) ->
    [ [ 0 || _ <- lists:seq(1, Col) ] || _ <- lists:seq(1, Row) ].

update_grid(Grid, Cells, Mid) ->
    lists:foldl(fun({X, Y}, Acc) ->
        update_grid(Acc, X - 1, Y - 1, 1)
    end, Grid, lists:sublist(Cells, Mid + 1)).

update_grid(Grid, X, Y, Val) ->
    lists:map(fun(List) when X == 0 ->
        [ Val | lists:sublist(List, 2, length(List)) ];
        (H) -> [H | update_grid(lists:sublist(List, 2, length(List)), X - 1, Y, Val)]
    end, Grid).

can_cross(Grid) ->
    lists:any(fun(X) -> dfs(Grid, X, 0) end, lists:seq(0, length(Grid) - 1)).

dfs(Grid, X, Y) ->
    Y == length(lists:nth(1, Grid)) - 1;

dfs(Grid, X, Y) ->
    lists:foldl(fun(Direction, Acc) ->
        {DX, DY} = Direction,
        NX = X + DX,
        NY = Y + DY,
        case {NX, NY} of
            {N, N} when N < 0; N >= length(Grid) -> Acc;
            {_, NY} when NY < 0; NY >= length(lists:nth(1, Grid)) -> Acc;
            {NX, NY} ->
                case lists:nth(NX + 1, Grid) of
                    [H | _] when H == 0 -> dfs(Grid, NX, NY);
                    _ -> Acc
                end
        end
    end, false, [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def latest_day_to_cross(row, col, cells) do
        low = 0
        high = length(cells) - 1
        loop(low, high, cells, row, col)
    end

    defp loop(low, high, cells, row, col) when low > high, do: low - 1
    defp loop(low, high, cells, row, col) do
        mid = div(low + high, 2)
        grid = create_grid(row, col)
        update_grid(grid, cells, mid)
        case can_cross(grid) do
            true -> loop(mid + 1, high, cells, row, col)
            false -> loop(low, mid - 1, cells, row, col)
        end
    end

    defp create_grid(row, col), do: for(_ <- 1..row, do: for(_ <- 1..col, do: 0))

    defp update_grid(grid, cells, mid) do
        Enum.reduce(1..mid, grid, fn i, acc ->
            update_grid(acc, Enum.at(cells, i - 1), 1)
        end)
    end

    defp update_grid(grid, [x, y], val) do
        List.update_at(grid, x - 1, fn row -> List.update_at(row, y - 1, fn _ -> val end))
    end

    defp can_cross(grid) do
        Enum.any?(0..length(grid) - 1, fn x -> dfs(grid, x, 0) end)
    end

    defp dfs(grid, x, y) do
        y == length(Enum.at(grid, 0)) - 1
    end

    defp dfs(grid, x, y) do
        Enum.reduce([{-1, 0}, {1, 0}, {0, -1}, {0, 1}], false, fn {dx, dy}, acc ->
            nx = x + dx
            ny = y + dy
            cond do
                nx < 0 or nx >= length(grid) -> acc
                ny < 0 or ny >= length(Enum.at(grid, 0)) -> acc
                true -> dfs(grid, nx, ny)
            end
        end)
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the solution is O(row * col * log(row * col)) because we are using binary search to find the last day and DFS to check if there is a path from the top to the bottom. The binary search reduces the number of days we need to check, and the DFS algorithm checks if there is a path in the grid.

- **Space Complexity:** The space complexity of the solution is O(row * col) because we need to store the grid and the visited cells during the DFS. The space complexity is linear with respect to the size of the input grid.

</div>
</details>
