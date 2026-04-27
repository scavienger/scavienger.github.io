---
layout: post
title: "Check if There is a Valid Path in a Grid"
date: 2026-04-27 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Depth-First Search", "Breadth-First Search", "Union-Find", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool hasValidPath(vector<vector<int>>& grid)\
        \ {\n        int m = grid.size();\n        int n = grid[0].size();\n       \
        \ int dirs[7][2][2] = {\n            {{0, 0}, {0, 0}},\n            {{0, -1},\
        \ {0, 1}},\n            {{-1, 0}, {1, 0}},\n            {{0, -1}, {1, 0}},\n\
        \            {{0, 1}, {1, 0}},\n            {{0, -1}, {-1, 0}},\n          \
        \  {{0, 1}, {-1, 0}}\n        };\n\n        vector<vector<bool>> visited(m,\
        \ vector<bool>(n, false));\n        queue<pair<int, int>> q;\n        q.push({0,\
        \ 0});\n        visited[0][0] = true;\n\n        while (!q.empty()) {\n    \
        \        pair<int, int> curr = q.front();\n            q.pop();\n          \
        \  int r = curr.first;\n            int c = curr.second;\n\n            if (r\
        \ == m - 1 && c == n - 1) return true;\n\n            int type = grid[r][c];\n\
        \            for (int i = 0; i < 2; ++i) {\n                int dr = dirs[type][i][0];\n\
        \                int dc = dirs[type][i][1];\n                int nr = r + dr;\n\
        \                int nc = c + dc;\n\n                if (nr >= 0 && nr < m &&\
        \ nc >= 0 && nc < n && !visited[nr][nc]) {\n                    int nType =\
        \ grid[nr][nc];\n                    bool connects = false;\n              \
        \      for (int j = 0; j < 2; ++j) {\n                        if (nr + dirs[nType][j][0]\
        \ == r && nc + dirs[nType][j][1] == c) {\n                            connects\
        \ = true;\n                            break;\n                        }\n \
        \                   }\n                    if (connects) {\n               \
        \         visited[nr][nc] = true;\n                        q.push({nr, nc});\n\
        \                    }\n                }\n            }\n        }\n      \
        \  return false;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public boolean hasValidPath(int[][]\
        \ grid) {\n        int m = grid.length;\n        int n = grid[0].length;\n \
        \       int[][][] dirs = {\n            {{0, 0}, {0, 0}},\n            {{0,\
        \ -1}, {0, 1}}, // 1\n            {{-1, 0}, {1, 0}}, // 2\n            {{0,\
        \ -1}, {1, 0}}, // 3\n            {{0, 1}, {1, 0}},  // 4\n            {{0,\
        \ -1}, {-1, 0}},// 5\n            {{0, 1}, {-1, 0}}  // 6\n        };\n\n  \
        \      boolean[][] visited = new boolean[m][n];\n        Queue<int[]> queue\
        \ = new LinkedList<>();\n        queue.offer(new int[]{0, 0});\n        visited[0][0]\
        \ = true;\n\n        while (!queue.isEmpty()) {\n            int[] curr = queue.poll();\n\
        \            int r = curr[0];\n            int c = curr[1];\n\n            if\
        \ (r == m - 1 && c == n - 1) return true;\n\n            int type = grid[r][c];\n\
        \            for (int[] d : dirs[type]) {\n                int nr = r + d[0];\n\
        \                int nc = c + d[1];\n\n                if (nr >= 0 && nr < m\
        \ && nc >= 0 && nc < n && !visited[nr][nc]) {\n                    int nType\
        \ = grid[nr][nc];\n                    boolean connects = false;\n         \
        \           for (int[] backD : dirs[nType]) {\n                        if (nr\
        \ + backD[0] == r && nc + backD[1] == c) {\n                            connects\
        \ = true;\n                            break;\n                        }\n \
        \                   }\n                    if (connects) {\n               \
        \         visited[nr][nc] = true;\n                        queue.offer(new int[]{nr,\
        \ nc});\n                    }\n                }\n            }\n        }\n\
        \        return false;\n    }\n}"
      python: "import collections\n\nclass Solution(object):\n    def hasValidPath(self,\
        \ grid):\n        \"\"\"\n        :type grid: List[List[int]]\n        :rtype:\
        \ bool\n        \"\"\"\n        m = len(grid)\n        n = len(grid[0])\n  \
        \      directions = {\n            1: [(0, -1), (0, 1)],\n            2: [(-1,\
        \ 0), (1, 0)],\n            3: [(0, -1), (1, 0)],\n            4: [(0, 1), (1,\
        \ 0)],\n            5: [(0, -1), (-1, 0)],\n            6: [(0, 1), (-1, 0)]\n\
        \        }\n\n        queue = collections.deque([(0, 0)])\n        visited =\
        \ set([(0, 0)])\n\n        while queue:\n            r, c = queue.popleft()\n\
        \            if r == m - 1 and c == n - 1:\n                return True\n\n\
        \            for dr, dc in directions[grid[r][c]]:\n                nr, nc =\
        \ r + dr, c + dc\n                if 0 <= nr < m and 0 <= nc < n and (nr, nc)\
        \ not in visited:\n                    can_connect = False\n               \
        \     for dnr, dnc in directions[grid[nr][nc]]:\n                        if\
        \ nr + dnr == r and nc + dnc == c:\n                            can_connect\
        \ = True\n                            break\n                    if can_connect:\n\
        \                        visited.add((nr, nc))\n                        queue.append((nr,\
        \ nc))\n\n        return False"
      python3: "import collections\n\nclass Solution:\n    def hasValidPath(self, grid:\
        \ List[List[int]]) -> bool:\n        m, n = len(grid), len(grid[0])\n      \
        \  directions = {\n            1: [(0, -1), (0, 1)],\n            2: [(-1, 0),\
        \ (1, 0)],\n            3: [(0, -1), (1, 0)],\n            4: [(0, 1), (1, 0)],\n\
        \            5: [(0, -1), (-1, 0)],\n            6: [(0, 1), (-1, 0)]\n    \
        \    }\n\n        queue = collections.deque([(0, 0)])\n        visited = set([(0,\
        \ 0)])\n\n        while queue:\n            r, c = queue.popleft()\n       \
        \     if r == m - 1 and c == n - 1:\n                return True\n\n       \
        \     for dr, dc in directions[grid[r][c]]:\n                nr, nc = r + dr,\
        \ c + dc\n                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in\
        \ visited:\n                    can_connect = False\n                    for\
        \ dnr, dnc in directions[grid[nr][nc]]:\n                        if nr + dnr\
        \ == r and nc + dnc == c:\n                            can_connect = True\n\
        \                            break\n                    if can_connect:\n  \
        \                      visited.add((nr, nc))\n                        queue.append((nr,\
        \ nc))\n\n        return False"
      c: "#include <stdbool.h>\n#include <stdlib.h>\n\nbool hasValidPath(int** grid,\
        \ int gridSize, int* gridColSize) {\n    int m = gridSize;\n    int n = gridColSize[0];\n\
        \n    int dirs[7][2][2] = {\n        {{0, 0}, {0, 0}},\n        {{0, -1}, {0,\
        \ 1}}, // 1\n        {{-1, 0}, {1, 0}}, // 2\n        {{0, -1}, {1, 0}}, //\
        \ 3\n        {{0, 1}, {1, 0}},  // 4\n        {{0, -1}, {-1, 0}},// 5\n    \
        \    {{0, 1}, {-1, 0}}  // 6\n    };\n\n    bool* visited = (bool*)calloc(m\
        \ * n, sizeof(bool));\n    int (*queue)[2] = (int (*)[2])malloc(m * n * sizeof(int[2]));\n\
        \    int head = 0, tail = 0;\n\n    queue[tail][0] = 0;\n    queue[tail][1]\
        \ = 0;\n    tail++;\n    visited[0] = true;\n\n    bool found = false;\n   \
        \ while (head < tail) {\n        int r = queue[head][0];\n        int c = queue[head][1];\n\
        \        head++;\n\n        if (r == m - 1 && c == n - 1) {\n            found\
        \ = true;\n            break;\n        }\n\n        int type = grid[r][c];\n\
        \        for (int i = 0; i < 2; i++) {\n            int dr = dirs[type][i][0];\n\
        \            int dc = dirs[type][i][1];\n            int nr = r + dr;\n    \
        \        int nc = c + dc;\n\n            if (nr >= 0 && nr < m && nc >= 0 &&\
        \ nc < n && !visited[nr * n + nc]) {\n                int nType = grid[nr][nc];\n\
        \                bool back = false;\n                for (int j = 0; j < 2;\
        \ j++) {\n                    if (nr + dirs[nType][j][0] == r && nc + dirs[nType][j][1]\
        \ == c) {\n                        back = true;\n                        break;\n\
        \                    }\n                }\n                if (back) {\n   \
        \                 visited[nr * n + nc] = true;\n                    queue[tail][0]\
        \ = nr;\n                    queue[tail][1] = nc;\n                    tail++;\n\
        \                }\n            }\n        }\n    }\n\n    free(visited);\n\
        \    free(queue);\n    return found;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public bool HasValidPath(int[][] grid) {\n        int m = grid.Length;\n\
        \        int n = grid[0].Length;\n        int[][][] dirs = new int[7][][] {\n\
        \            new int[][] {},\n            new int[][] { new int[] { 0, -1 },\
        \ new int[] { 0, 1 } },\n            new int[][] { new int[] { -1, 0 }, new\
        \ int[] { 1, 0 } },\n            new int[][] { new int[] { 0, -1 }, new int[]\
        \ { 1, 0 } },\n            new int[][] { new int[] { 0, 1 }, new int[] { 1,\
        \ 0 } },\n            new int[][] { new int[] { 0, -1 }, new int[] { -1, 0 }\
        \ },\n            new int[][] { new int[] { 0, 1 }, new int[] { -1, 0 } }\n\
        \        };\n\n        bool[,] visited = new bool[m, n];\n        Stack<(int\
        \ r, int c)> stack = new Stack<(int r, int c)>();\n\n        stack.Push((0,\
        \ 0));\n        visited[0, 0] = true;\n\n        while (stack.Count > 0) {\n\
        \            var curr = stack.Pop();\n            int r = curr.r, c = curr.c;\n\
        \n            if (r == m - 1 && c == n - 1) return true;\n\n            foreach\
        \ (var d in dirs[grid[r][c]]) {\n                int nr = r + d[0];\n      \
        \          int nc = c + d[1];\n\n                if (nr >= 0 && nr < m && nc\
        \ >= 0 && nc < n && !visited[nr, nc]) {\n                    foreach (var backDir\
        \ in dirs[grid[nr][nc]]) {\n                        if (nr + backDir[0] == r\
        \ && nc + backDir[1] == c) {\n                            visited[nr, nc] =\
        \ true;\n                            stack.Push((nr, nc));\n               \
        \             break;\n                        }\n                    }\n   \
        \             }\n            }\n        }\n\n        return false;\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @return {boolean}\n */\nvar\
        \ hasValidPath = function(grid) {\n    const m = grid.length;\n    const n =\
        \ grid[0].length;\n    const dirs = [\n        [],\n        [[0, -1], [0, 1]],\n\
        \        [[-1, 0], [1, 0]],\n        [[0, -1], [1, 0]],\n        [[0, 1], [1,\
        \ 0]],\n        [[0, -1], [-1, 0]],\n        [[0, 1], [-1, 0]]\n    ];\n\n \
        \   const visited = Array.from({ length: m }, () => Array(n).fill(false));\n\
        \    const stack = [[0, 0]];\n    visited[0][0] = true;\n\n    while (stack.length\
        \ > 0) {\n        const [r, c] = stack.pop();\n\n        if (r === m - 1 &&\
        \ c === n - 1) return true;\n\n        for (const [dr, dc] of dirs[grid[r][c]])\
        \ {\n            const nr = r + dr;\n            const nc = c + dc;\n\n    \
        \        if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc]) {\n\
        \                for (const [ndr, ndc] of dirs[grid[nr][nc]]) {\n          \
        \          if (nr + ndr === r && nc + ndc === c) {\n                       \
        \ visited[nr][nc] = true;\n                        stack.push([nr, nc]);\n \
        \                       break;\n                    }\n                }\n \
        \           }\n        }\n    }\n\n    return false;\n};"
      typescript: "function hasValidPath(grid: number[][]): boolean {\n    const m =\
        \ grid.length;\n    const n = grid[0].length;\n    const dirs: number[][][]\
        \ = [\n        [],\n        [[0, -1], [0, 1]],\n        [[-1, 0], [1, 0]],\n\
        \        [[0, -1], [1, 0]],\n        [[0, 1], [1, 0]],\n        [[0, -1], [-1,\
        \ 0]],\n        [[0, 1], [-1, 0]]\n    ];\n\n    const visited: boolean[][]\
        \ = Array.from({ length: m }, () => Array(n).fill(false));\n    const stack:\
        \ [number, number][] = [[0, 0]];\n    visited[0][0] = true;\n\n    while (stack.length\
        \ > 0) {\n        const [r, c] = stack.pop()!;\n\n        if (r === m - 1 &&\
        \ c === n - 1) return true;\n\n        for (const [dr, dc] of dirs[grid[r][c]])\
        \ {\n            const nr = r + dr;\n            const nc = c + dc;\n\n    \
        \        if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc]) {\n\
        \                for (const [ndr, ndc] of dirs[grid[nr][nc]]) {\n          \
        \          if (nr + ndr === r && nc + ndc === c) {\n                       \
        \ visited[nr][nc] = true;\n                        stack.push([nr, nc]);\n \
        \                       break;\n                    }\n                }\n \
        \           }\n        }\n    }\n\n    return false;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @return\
        \ Boolean\n     */\n    function hasValidPath($grid) {\n        $m = count($grid);\n\
        \        $n = count($grid[0]);\n        $dirs = [\n            [],\n       \
        \     [[0, -1], [0, 1]],\n            [[-1, 0], [1, 0]],\n            [[0, -1],\
        \ [1, 0]],\n            [[0, 1], [1, 0]],\n            [[0, -1], [-1, 0]],\n\
        \            [[0, 1], [-1, 0]]\n        ];\n\n        $visited = array_fill(0,\
        \ $m, array_fill(0, $n, false));\n        $stack = [[0, 0]];\n        $visited[0][0]\
        \ = true;\n\n        while (!empty($stack)) {\n            $curr = array_pop($stack);\n\
        \            $r = $curr[0];\n            $c = $curr[1];\n\n            if ($r\
        \ == $m - 1 && $c == $n - 1) return true;\n\n            foreach ($dirs[$grid[$r][$c]]\
        \ as $d) {\n                $nr = $r + $d[0];\n                $nc = $c + $d[1];\n\
        \n                if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && !$visited[$nr][$nc])\
        \ {\n                    foreach ($dirs[$grid[$nr][$nc]] as $backDir) {\n  \
        \                      if ($nr + $backDir[0] == $r && $nc + $backDir[1] == $c)\
        \ {\n                            $visited[$nr][$nc] = true;\n              \
        \              $stack[] = [$nr, $nc];\n                            break;\n\
        \                        }\n                    }\n                }\n     \
        \       }\n        }\n\n        return false;\n    }\n}"
      swift: "class Solution {\n    func hasValidPath(_ grid: [[Int]]) -> Bool {\n \
        \       let m = grid.count\n        let n = grid[0].count\n        let dirs:\
        \ [[[Int]]] = [\n            [],\n            [[0, -1], [0, 1]],\n         \
        \   [[-1, 0], [1, 0]],\n            [[0, -1], [1, 0]],\n            [[0, 1],\
        \ [1, 0]],\n            [[0, -1], [-1, 0]],\n            [[0, 1], [-1, 0]]\n\
        \        ]\n\n        var visited = Array(repeating: Array(repeating: false,\
        \ count: n), count: m)\n        var stack = [(Int, Int)]()\n\n        stack.append((0,\
        \ 0))\n        visited[0][0] = true\n\n        while let (r, c) = stack.popLast()\
        \ {\n            if r == m - 1 && c == n - 1 { return true }\n\n           \
        \ for d in dirs[grid[r][c]] {\n                let nr = r + d[0]\n         \
        \       let nc = c + d[1]\n\n                if nr >= 0 && nr < m && nc >= 0\
        \ && nc < n && !visited[nr][nc] {\n                    for backDir in dirs[grid[nr][nc]]\
        \ {\n                        if nr + backDir[0] == r && nc + backDir[1] == c\
        \ {\n                            visited[nr][nc] = true\n                  \
        \          stack.append((nr, nc))\n                            break\n     \
        \                   }\n                    }\n                }\n          \
        \  }\n        }\n\n        return false\n    }\n}"
      kotlin: "import java.util.LinkedList\nimport java.util.Queue\n\nclass Solution\
        \ {\n    fun hasValidPath(grid: Array<IntArray>): Boolean {\n        val m =\
        \ grid.size\n        val n = grid[0].size\n        val connections = arrayOf(\n\
        \            intArrayOf(),\n            intArrayOf(2, 3), // 1: Left, Right\n\
        \            intArrayOf(0, 1), // 2: Up, Down\n            intArrayOf(2, 1),\
        \ // 3: Left, Down\n            intArrayOf(3, 1), // 4: Right, Down\n      \
        \      intArrayOf(2, 0), // 5: Left, Up\n            intArrayOf(3, 0)  // 6:\
        \ Right, Up\n        )\n        val dx = intArrayOf(-1, 1, 0, 0) // Up, Down,\
        \ Left, Right\n        val dy = intArrayOf(0, 0, -1, 1)\n        val opposite\
        \ = intArrayOf(1, 0, 3, 2)\n        val visited = Array(m) { BooleanArray(n)\
        \ }\n        val queue: Queue<IntArray> = LinkedList()\n\n        queue.offer(intArrayOf(0,\
        \ 0))\n        visited[0][0] = true\n\n        while (queue.isNotEmpty()) {\n\
        \            val curr = queue.poll()\n            val r = curr[0]\n        \
        \    val c = curr[1]\n            if (r == m - 1 && c == n - 1) return true\n\
        \n            for (dir in connections[grid[r][c]]) {\n                val nr\
        \ = r + dx[dir]\n                val nc = c + dy[dir]\n                if (nr\
        \ in 0 until m && nc in 0 until n && !visited[nr][nc]) {\n                 \
        \   val nType = grid[nr][nc]\n                    val opp = opposite[dir]\n\
        \                    if (connections[nType].contains(opp)) {\n             \
        \           visited[nr][nc] = true\n                        queue.offer(intArrayOf(nr,\
        \ nc))\n                    }\n                }\n            }\n        }\n\
        \        return false\n    }\n}"
      dart: "import 'dart:collection';\n\nclass Solution {\n  bool hasValidPath(List<List<int>>\
        \ grid) {\n    int m = grid.length;\n    int n = grid[0].length;\n    List<List<int>>\
        \ connections = [\n      [],\n      [2, 3], // 1: Left, Right\n      [0, 1],\
        \ // 2: Up, Down\n      [2, 1], // 3: Left, Down\n      [3, 1], // 4: Right,\
        \ Down\n      [2, 0], // 5: Left, Up\n      [3, 0]  // 6: Right, Up\n    ];\n\
        \    List<int> dx = [-1, 1, 0, 0]; // Up, Down, Left, Right\n    List<int> dy\
        \ = [0, 0, -1, 1];\n    List<int> opposite = [1, 0, 3, 2];\n    List<List<bool>>\
        \ visited = List.generate(m, (i) => List.filled(n, false));\n    Queue<List<int>>\
        \ queue = Queue();\n\n    queue.add([0, 0]);\n    visited[0][0] = true;\n\n\
        \    while (queue.isNotEmpty) {\n      List<int> curr = queue.removeFirst();\n\
        \      int r = curr[0];\n      int c = curr[1];\n      if (r == m - 1 && c ==\
        \ n - 1) return true;\n\n      for (int dir in connections[grid[r][c]]) {\n\
        \        int nr = r + dx[dir];\n        int nc = c + dy[dir];\n        if (nr\
        \ >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc]) {\n          int\
        \ nType = grid[nr][nc];\n          int opp = opposite[dir];\n          if (connections[nType].contains(opp))\
        \ {\n            visited[nr][nc] = true;\n            queue.add([nr, nc]);\n\
        \          }\n        }\n      }\n    }\n    return false;\n  }\n}"
      go: "func hasValidPath(grid [][]int) bool {\n\tm := len(grid)\n\tn := len(grid[0])\n\
        \tconnections := [][]int{\n\t\t{},\n\t\t{2, 3}, // 1: Left, Right\n\t\t{0, 1},\
        \ // 2: Up, Down\n\t\t{2, 1}, // 3: Left, Down\n\t\t{3, 1}, // 4: Right, Down\n\
        \t\t{2, 0}, // 5: Left, Up\n\t\t{3, 0}, // 6: Right, Up\n\t}\n\tdx := []int{-1,\
        \ 1, 0, 0} // Up, Down, Left, Right\n\tdy := []int{0, 0, -1, 1}\n\topposite\
        \ := []int{1, 0, 3, 2}\n\tvisited := make([][]bool, m)\n\tfor i := range visited\
        \ {\n\t\tvisited[i] = make([]bool, n)\n\t}\n\tqueue := [][]int{{0, 0}}\n\tvisited[0][0]\
        \ = true\n\tfor len(queue) > 0 {\n\t\tcurr := queue[0]\n\t\tqueue = queue[1:]\n\
        \t\tr, c := curr[0], curr[1]\n\t\tif r == m-1 && c == n-1 {\n\t\t\treturn true\n\
        \t\t}\n\t\tfor _, dir := range connections[grid[r][c]] {\n\t\t\tnr, nc := r+dx[dir],\
        \ c+dy[dir]\n\t\t\tif nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc]\
        \ {\n\t\t\t\tnType := grid[nr][nc]\n\t\t\t\topp := opposite[dir]\n\t\t\t\tcanConnect\
        \ := false\n\t\t\t\tfor _, ndir := range connections[nType] {\n\t\t\t\t\tif\
        \ ndir == opp {\n\t\t\t\t\t\tcanConnect = true\n\t\t\t\t\t\tbreak\n\t\t\t\t\t\
        }\n\t\t\t\t}\n\t\t\t\tif canConnect {\n\t\t\t\t\tvisited[nr][nc] = true\n\t\t\
        \t\t\tqueue = append(queue, []int{nr, nc})\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t}\n\
        \treturn false\n}"
      ruby: "# @param {Integer[][]} grid\n# @return {Boolean}\ndef has_valid_path(grid)\n\
        \  m = grid.length\n  n = grid[0].length\n  connections = [\n    [],\n    [2,\
        \ 3], # 1: Left, Right\n    [0, 1], # 2: Up, Down\n    [2, 1], # 3: Left, Down\n\
        \    [3, 1], # 4: Right, Down\n    [2, 0], # 5: Left, Up\n    [3, 0]  # 6: Right,\
        \ Up\n  ]\n  dx = [-1, 1, 0, 0] # Up, Down, Left, Right\n  dy = [0, 0, -1, 1]\n\
        \  opposite = [1, 0, 3, 2]\n  visited = Array.new(m) { Array.new(n, false) }\n\
        \  queue = [[0, 0]]\n  visited[0][0] = true\n  head = 0\n  while head < queue.length\n\
        \    r, c = queue[head]\n    head += 1\n    return true if r == m - 1 && c ==\
        \ n - 1\n\n    connections[grid[r][c]].each do |dir|\n      nr, nc = r + dx[dir],\
        \ c + dy[dir]\n      if nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc]\n\
        \        n_type = grid[nr][nc]\n        opp = opposite[dir]\n        if connections[n_type].include?(opp)\n\
        \          visited[nr][nc] = true\n          queue.push([nr, nc])\n        end\n\
        \      end\n    end\n  end\n  false\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n  def hasValidPath(grid:\
        \ Array[Array[Int]]): Boolean = {\n    val m = grid.length\n    val n = grid(0).length\n\
        \    val connections = Array(\n      Array.empty[Int],\n      Array(2, 3), //\
        \ 1: Left, Right\n      Array(0, 1), // 2: Up, Down\n      Array(2, 1), // 3:\
        \ Left, Down\n      Array(3, 1), // 4: Right, Down\n      Array(2, 0), // 5:\
        \ Left, Up\n      Array(3, 0)  // 6: Right, Up\n    )\n    val dx = Array(-1,\
        \ 1, 0, 0) // Up, Down, Left, Right\n    val dy = Array(0, 0, -1, 1)\n    val\
        \ opposite = Array(1, 0, 3, 2)\n    val visited = Array.ofDim[Boolean](m, n)\n\
        \    val queue = mutable.Queue[(Int, Int)]()\n\n    queue.enqueue((0, 0))\n\
        \    visited(0)(0) = true\n\n    while (queue.nonEmpty) {\n      val (r, c)\
        \ = queue.dequeue()\n      if (r == m - 1 && c == n - 1) return true\n\n   \
        \   for (dir <- connections(grid(r)(c))) {\n        val nr = r + dx(dir)\n \
        \       val nc = c + dy(dir)\n        if (nr >= 0 && nr < m && nc >= 0 && nc\
        \ < n && !visited(nr)(nc)) {\n          val nType = grid(nr)(nc)\n         \
        \ val opp = opposite(dir)\n          if (connections(nType).contains(opp)) {\n\
        \            visited(nr)(nc) = true\n            queue.enqueue((nr, nc))\n \
        \         }\n        }\n      }\n    }\n    false\n  }\n}"
      rust: "impl Solution {\n    pub fn has_valid_path(grid: Vec<Vec<i32>>) -> bool\
        \ {\n        let m = grid.len();\n        let n = grid[0].len();\n        let\
        \ mut visited = vec![vec![false; n]; m];\n        let mut stack = vec![(0, 0)];\n\
        \        visited[0][0] = true;\n\n        let dirs: [Vec<(i32, i32)>; 7] = [\n\
        \            vec![],\n            vec![(0, -1), (0, 1)],\n            vec![(-1,\
        \ 0), (1, 0)],\n            vec![(0, -1), (1, 0)],\n            vec![(0, 1),\
        \ (1, 0)],\n            vec![(0, -1), (-1, 0)],\n            vec![(0, 1), (-1,\
        \ 0)],\n        ];\n\n        while let Some((r, c)) = stack.pop() {\n     \
        \       if r == m - 1 && c == n - 1 {\n                return true;\n      \
        \      }\n            let street_type = grid[r][c] as usize;\n            for\
        \ &(dr, dc) in &dirs[street_type] {\n                let nr = r as i32 + dr;\n\
        \                let nc = c as i32 + dc;\n                if nr >= 0 && nr <\
        \ m as i32 && nc >= 0 && nc < n as i32 {\n                    let unr = nr as\
        \ usize;\n                    let unc = nc as usize;\n                    if\
        \ !visited[unr][unc] {\n                        let next_street_type = grid[unr][unc]\
        \ as usize;\n                        if dirs[next_street_type].iter().any(|&(ndr,\
        \ ndc)| {\n                            unr as i32 + ndr == r as i32 && unc as\
        \ i32 + ndc == c as i32\n                        }) {\n                    \
        \        visited[unr][unc] = true;\n                            stack.push((unr,\
        \ unc));\n                        }\n                    }\n               \
        \ }\n            }\n        }\n        false\n    }\n}"
      racket: "(define/contract (has-valid-path grid)\n  (-> (listof (listof exact-integer?))\
        \ boolean?)\n  (let* ([m (length grid)]\n         [n (length (first grid))]\n\
        \         [grid-vec (list->vector (map list->vector grid))]\n         [dirs\
        \ (vector #()\n                       '((0 -1) (0 1))\n                    \
        \   '((-1 0) (1 0))\n                       '((0 -1) (1 0))\n              \
        \         '((0 1) (1 0))\n                       '((0 -1) (-1 0))\n        \
        \               '((0 1) (-1 0)))]\n         [visited (make-vector (* m n) 0)])\n\
        \    (define (get-grid r c) (vector-ref (vector-ref grid-vec r) c))\n    (define\
        \ (is-visited? r c) (= 1 (vector-ref visited (+ (* r n) c))))\n    (define (set-visited!\
        \ r c) (vector-set! visited (+ (* r n) c) 1))\n\n    (define (can-move? r c\
        \ nr nc)\n      (and (>= nr 0) (< nr m) (>= nc 0) (< nc n)\n           (not\
        \ (is-visited? nr nc))\n           (let ([curr-dirs (vector-ref dirs (get-grid\
        \ r c))]\n                 [next-dirs (vector-ref dirs (get-grid nr nc))])\n\
        \             (and (member (list (- nr r) (- nc c)) curr-dirs)\n           \
        \       (member (list (- r nr) (- c nc)) next-dirs)))))\n\n    (set-visited!\
        \ 0 0)\n    (let loop ([front (list (cons 0 0))] [back '()])\n      (cond\n\
        \        [(and (null? front) (null? back)) #f]\n        [(null? front) (loop\
        \ (reverse back) '())]\n        [else\n         (let* ([curr (car front)]\n\
        \                [r (car curr)]\n                [c (cdr curr)])\n         \
        \  (if (and (= r (- m 1)) (= c (- n 1)))\n               #t\n              \
        \ (let ([neighbors (for/list ([d (vector-ref dirs (get-grid r c))]\n       \
        \                                    #:let [nr (+ r (car d))\n             \
        \                                     nc (+ c (cadr d))]\n                 \
        \                          #:when (can-move? r c nr nc))\n                 \
        \                 (set-visited! nr nc)\n                                  (cons\
        \ nr nc))])\n                 (loop (cdr front) (foldl cons back neighbors))))]))))"
      erlang: "-spec has_valid_path(Grid :: [[integer()]]) -> boolean().\nhas_valid_path(Grid)\
        \ ->\n  M = length(Grid),\n  N = length(hd(Grid)),\n  Rows = lists:zip(lists:seq(0,\
        \ M - 1), Grid),\n  GridMap = maps:from_list([{{R, C}, Val} || {R, Row} <- Rows,\
        \ {C, Val} <- lists:zip(lists:seq(0, N - 1), Row)]),\n  Dirs = #{1 => [{0, -1},\
        \ {0, 1}], 2 => [{-1, 0}, {1, 0}], 3 => [{0, -1}, {1, 0}], 4 => [{0, 1}, {1,\
        \ 0}], 5 => [{0, -1}, {-1, 0}], 6 => [{0, 1}, {-1, 0}]},\n  Q = queue:in({0,\
        \ 0}, queue:new()),\n  Visited = sets:from_list([{0, 0}]),\n  bfs(Q, Visited,\
        \ M, N, GridMap, Dirs).\n\nbfs(Q, Visited, M, N, GridMap, Dirs) ->\n  case queue:out(Q)\
        \ of\n    {empty, _} -> false;\n    {{value, {R, C}}, Q2} ->\n      if\n   \
        \     R == M - 1, C == N - 1 -> true;\n        true ->\n          Type = maps:get({R,\
        \ C}, GridMap),\n          TypeDirs = maps:get(Type, Dirs),\n          Neighbors\
        \ = [{NR, NC} || {DR, DC} <- TypeDirs, \n                                  \
        \ NR <- [R + DR], NC <- [C + DC],\n                                   NR >=\
        \ 0, NR < M, NC >= 0, NC < N,\n                                   not sets:is_element({NR,\
        \ NC}, Visited),\n                                   check_back(NR, NC, R, C,\
        \ GridMap, Dirs)],\n          NewVisited = lists:foldl(fun(P, V) -> sets:add_element(P,\
        \ V) end, Visited, Neighbors),\n          NewQ = lists:foldl(fun(P, AccQ) ->\
        \ queue:in(P, AccQ) end, Q2, Neighbors),\n          bfs(NewQ, NewVisited, M,\
        \ N, GridMap, Dirs)\n      end\n  end.\n\ncheck_back(NR, NC, R, C, GridMap,\
        \ Dirs) ->\n  NextType = maps:get({NR, NC}, GridMap),\n  NextDirs = maps:get(NextType,\
        \ Dirs),\n  lists:any(fun({NDR, NDC}) -> NR + NDR == R andalso NC + NDC == C\
        \ end, NextDirs)."
      elixir: "defmodule Solution do\n  @spec has_valid_path(grid :: [[integer]]) ::\
        \ boolean\n  def has_valid_path(grid) do\n    m = length(grid)\n    n = length(hd(grid))\n\
        \    grid_map = for {row, r} <- Enum.with_index(grid), {val, c} <- Enum.with_index(row),\
        \ into: %{}, do: {{r, c}, val}\n    dirs = %{\n      1 => [{0, -1}, {0, 1}],\n\
        \      2 => [{-1, 0}, {1, 0}],\n      3 => [{0, -1}, {1, 0}],\n      4 => [{0,\
        \ 1}, {1, 0}],\n      5 => [{0, -1}, {-1, 0}],\n      6 => [{0, 1}, {-1, 0}]\n\
        \    }\n    bfs(:queue.from_list([{0, 0}]), MapSet.new([{0, 0}]), m, n, grid_map,\
        \ dirs)\n  end\n\n  defp bfs(q, visited, m, n, grid_map, dirs) do\n    case\
        \ :queue.out(q) do\n      {:empty, _} -> false\n      {{:value, {r, c}}, nq}\
        \ ->\n        if r == m - 1 and c == n - 1 do\n          true\n        else\n\
        \          neighbors = get_neighbors(r, c, grid_map, dirs, m, n, visited)\n\
        \          new_visited = Enum.reduce(neighbors, visited, &MapSet.put(&2, &1))\n\
        \          new_q = Enum.reduce(neighbors, nq, &:queue.in(&1, &2))\n        \
        \  bfs(new_q, new_visited, m, n, grid_map, dirs)\n        end\n    end\n  end\n\
        \n  defp get_neighbors(r, c, grid_map, dirs, m, n, visited) do\n    type = Map.get(grid_map,\
        \ {r, c})\n    curr_dirs = Map.get(dirs, type)\n    curr_dirs\n    |> Enum.map(fn\
        \ {dr, dc} -> {r + dr, c + dc} end)\n    |> Enum.filter(fn {nr, nc} ->\n   \
        \   nr >= 0 and nr < m and nc >= 0 and nc < n and\n      not MapSet.member?(visited,\
        \ {nr, nc}) and\n      check_back(nr, nc, r, c, grid_map, dirs)\n    end)\n\
        \  end\n\n  defp check_back(nr, nc, r, c, grid_map, dirs) do\n    next_type\
        \ = Map.get(grid_map, {nr, nc})\n    next_dirs = Map.get(dirs, next_type)\n\
        \    Enum.any?(next_dirs, fn {ndr, ndc} -> nr + ndr == r and nc + ndc == c end)\n\
        \  end\nend"
    approach: The problem can be solved by traversing the grid using Breadth-First Search
      (BFS) to explore all reachable cells starting from the top-left corner (0, 0).
      Each street type in a cell defines two specific directions (Up, Down, Left, or
      Right) that a path can follow. To ensure a move to an adjacent cell is valid,
      we must verify both that the current street type allows movement in that direction
      and that the target cell's street type contains a reciprocal connection back to
      the current cell.
    time_complexity: O(M * N) where M is the number of rows and N is the number of columns
      in the grid. Each cell is visited at most once and added to the queue, and for
      each cell, we perform a constant number of operations to check its two possible
      connections.
    space_complexity: O(M * N) to store the visited status of each cell and the queue
      used for the BFS traversal, both of which can contain up to M * N elements in
      the worst case.
    elapsed_time: 300.31863927841187
    model: gemini-3-flash-preview
    generated_at: '2026-04-27 02:09:28 '
---

## Problem #1391: Check if There is a Valid Path in a Grid

**Difficulty:** Medium

**Topics:** Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix

## Problem Description

<p>You are given an <code>m x n</code> <code>grid</code>. Each cell of <code>grid</code> represents a street. The street of <code>grid[i][j]</code> can be:</p>

<ul>
	<li><code>1</code> which means a street connecting the left cell and the right cell.</li>
	<li><code>2</code> which means a street connecting the upper cell and the lower cell.</li>
	<li><code>3</code> which means a street connecting the left cell and the lower cell.</li>
	<li><code>4</code> which means a street connecting the right cell and the lower cell.</li>
	<li><code>5</code> which means a street connecting the left cell and the upper cell.</li>
	<li><code>6</code> which means a street connecting the right cell and the upper cell.</li>
</ul>
<img alt="" src="https://assets.leetcode.com/uploads/2020/03/05/main.png" style="width: 450px; height: 708px;" />
<p>You will initially start at the street of the upper-left cell <code>(0, 0)</code>. A valid path in the grid is a path that starts from the upper left cell <code>(0, 0)</code> and ends at the bottom-right cell <code>(m - 1, n - 1)</code>. <strong>The path should only follow the streets</strong>.</p>

<p><strong>Notice</strong> that you are <strong>not allowed</strong> to change any street.</p>

<p>Return <code>true</code><em> if there is a valid path in the grid or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/03/05/e1.png" style="width: 455px; height: 311px;" />
<pre>
<strong>Input:</strong> grid = [[2,4,3],[6,5,2]]
<strong>Output:</strong> true
<strong>Explanation:</strong> As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/03/05/e2.png" style="width: 455px; height: 293px;" />
<pre>
<strong>Input:</strong> grid = [[1,2,1],[1,2,1]]
<strong>Output:</strong> false
<strong>Explanation:</strong> As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,1,2]]
<strong>Output:</strong> false
<strong>Explanation:</strong> You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 6</code></li>
</ul>


## Hints

1. Start DFS from the node (0, 0) and follow the path till you stop.

2. When you reach a cell and cannot move anymore check that this cell is (m - 1, n - 1) or not.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be solved by traversing the grid using Breadth-First Search (BFS) to explore all reachable cells starting from the top-left corner (0, 0). Each street type in a cell defines two specific directions (Up, Down, Left, or Right) that a path can follow. To ensure a move to an adjacent cell is valid, we must verify both that the current street type allows movement in that direction and that the target cell's street type contains a reciprocal connection back to the current cell.

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
    bool hasValidPath(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int dirs[7][2][2] = {
            {{0, 0}, {0, 0}},
            {{0, -1}, {0, 1}},
            {{-1, 0}, {1, 0}},
            {{0, -1}, {1, 0}},
            {{0, 1}, {1, 0}},
            {{0, -1}, {-1, 0}},
            {{0, 1}, {-1, 0}}
        };

        vector<vector<bool>> visited(m, vector<bool>(n, false));
        queue<pair<int, int>> q;
        q.push({0, 0});
        visited[0][0] = true;

        while (!q.empty()) {
            pair<int, int> curr = q.front();
            q.pop();
            int r = curr.first;
            int c = curr.second;

            if (r == m - 1 && c == n - 1) return true;

            int type = grid[r][c];
            for (int i = 0; i < 2; ++i) {
                int dr = dirs[type][i][0];
                int dc = dirs[type][i][1];
                int nr = r + dr;
                int nc = c + dc;

                if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc]) {
                    int nType = grid[nr][nc];
                    bool connects = false;
                    for (int j = 0; j < 2; ++j) {
                        if (nr + dirs[nType][j][0] == r && nc + dirs[nType][j][1] == c) {
                            connects = true;
                            break;
                        }
                    }
                    if (connects) {
                        visited[nr][nc] = true;
                        q.push({nr, nc});
                    }
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
    public boolean hasValidPath(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][][] dirs = {
            {{0, 0}, {0, 0}},
            {{0, -1}, {0, 1}}, // 1
            {{-1, 0}, {1, 0}}, // 2
            {{0, -1}, {1, 0}}, // 3
            {{0, 1}, {1, 0}},  // 4
            {{0, -1}, {-1, 0}},// 5
            {{0, 1}, {-1, 0}}  // 6
        };

        boolean[][] visited = new boolean[m][n];
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0});
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0];
            int c = curr[1];

            if (r == m - 1 && c == n - 1) return true;

            int type = grid[r][c];
            for (int[] d : dirs[type]) {
                int nr = r + d[0];
                int nc = c + d[1];

                if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc]) {
                    int nType = grid[nr][nc];
                    boolean connects = false;
                    for (int[] backD : dirs[nType]) {
                        if (nr + backD[0] == r && nc + backD[1] == c) {
                            connects = true;
                            break;
                        }
                    }
                    if (connects) {
                        visited[nr][nc] = true;
                        queue.offer(new int[]{nr, nc});
                    }
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
import collections

class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        queue = collections.deque([(0, 0)])
        visited = set([(0, 0)])

        while queue:
            r, c = queue.popleft()
            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    can_connect = False
                    for dnr, dnc in directions[grid[nr][nc]]:
                        if nr + dnr == r and nc + dnc == c:
                            can_connect = True
                            break
                    if can_connect:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        return False
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        queue = collections.deque([(0, 0)])
        visited = set([(0, 0)])

        while queue:
            r, c = queue.popleft()
            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    can_connect = False
                    for dnr, dnc in directions[grid[nr][nc]]:
                        if nr + dnr == r and nc + dnc == c:
                            can_connect = True
                            break
                    if can_connect:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        return False
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <stdlib.h>

bool hasValidPath(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];

    int dirs[7][2][2] = {
        {{0, 0}, {0, 0}},
        {{0, -1}, {0, 1}}, // 1
        {{-1, 0}, {1, 0}}, // 2
        {{0, -1}, {1, 0}}, // 3
        {{0, 1}, {1, 0}},  // 4
        {{0, -1}, {-1, 0}},// 5
        {{0, 1}, {-1, 0}}  // 6
    };

    bool* visited = (bool*)calloc(m * n, sizeof(bool));
    int (*queue)[2] = (int (*)[2])malloc(m * n * sizeof(int[2]));
    int head = 0, tail = 0;

    queue[tail][0] = 0;
    queue[tail][1] = 0;
    tail++;
    visited[0] = true;

    bool found = false;
    while (head < tail) {
        int r = queue[head][0];
        int c = queue[head][1];
        head++;

        if (r == m - 1 && c == n - 1) {
            found = true;
            break;
        }

        int type = grid[r][c];
        for (int i = 0; i < 2; i++) {
            int dr = dirs[type][i][0];
            int dc = dirs[type][i][1];
            int nr = r + dr;
            int nc = c + dc;

            if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr * n + nc]) {
                int nType = grid[nr][nc];
                bool back = false;
                for (int j = 0; j < 2; j++) {
                    if (nr + dirs[nType][j][0] == r && nc + dirs[nType][j][1] == c) {
                        back = true;
                        break;
                    }
                }
                if (back) {
                    visited[nr * n + nc] = true;
                    queue[tail][0] = nr;
                    queue[tail][1] = nc;
                    tail++;
                }
            }
        }
    }

    free(visited);
    free(queue);
    return found;
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
    public bool HasValidPath(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int[][][] dirs = new int[7][][] {
            new int[][] {},
            new int[][] { new int[] { 0, -1 }, new int[] { 0, 1 } },
            new int[][] { new int[] { -1, 0 }, new int[] { 1, 0 } },
            new int[][] { new int[] { 0, -1 }, new int[] { 1, 0 } },
            new int[][] { new int[] { 0, 1 }, new int[] { 1, 0 } },
            new int[][] { new int[] { 0, -1 }, new int[] { -1, 0 } },
            new int[][] { new int[] { 0, 1 }, new int[] { -1, 0 } }
        };

        bool[,] visited = new bool[m, n];
        Stack<(int r, int c)> stack = new Stack<(int r, int c)>();

        stack.Push((0, 0));
        visited[0, 0] = true;

        while (stack.Count > 0) {
            var curr = stack.Pop();
            int r = curr.r, c = curr.c;

            if (r == m - 1 && c == n - 1) return true;

            foreach (var d in dirs[grid[r][c]]) {
                int nr = r + d[0];
                int nc = c + d[1];

                if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr, nc]) {
                    foreach (var backDir in dirs[grid[nr][nc]]) {
                        if (nr + backDir[0] == r && nc + backDir[1] == c) {
                            visited[nr, nc] = true;
                            stack.Push((nr, nc));
                            break;
                        }
                    }
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
var hasValidPath = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const dirs = [
        [],
        [[0, -1], [0, 1]],
        [[-1, 0], [1, 0]],
        [[0, -1], [1, 0]],
        [[0, 1], [1, 0]],
        [[0, -1], [-1, 0]],
        [[0, 1], [-1, 0]]
    ];

    const visited = Array.from({ length: m }, () => Array(n).fill(false));
    const stack = [[0, 0]];
    visited[0][0] = true;

    while (stack.length > 0) {
        const [r, c] = stack.pop();

        if (r === m - 1 && c === n - 1) return true;

        for (const [dr, dc] of dirs[grid[r][c]]) {
            const nr = r + dr;
            const nc = c + dc;

            if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc]) {
                for (const [ndr, ndc] of dirs[grid[nr][nc]]) {
                    if (nr + ndr === r && nc + ndc === c) {
                        visited[nr][nc] = true;
                        stack.push([nr, nc]);
                        break;
                    }
                }
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
function hasValidPath(grid: number[][]): boolean {
    const m = grid.length;
    const n = grid[0].length;
    const dirs: number[][][] = [
        [],
        [[0, -1], [0, 1]],
        [[-1, 0], [1, 0]],
        [[0, -1], [1, 0]],
        [[0, 1], [1, 0]],
        [[0, -1], [-1, 0]],
        [[0, 1], [-1, 0]]
    ];

    const visited: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));
    const stack: [number, number][] = [[0, 0]];
    visited[0][0] = true;

    while (stack.length > 0) {
        const [r, c] = stack.pop()!;

        if (r === m - 1 && c === n - 1) return true;

        for (const [dr, dc] of dirs[grid[r][c]]) {
            const nr = r + dr;
            const nc = c + dc;

            if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc]) {
                for (const [ndr, ndc] of dirs[grid[nr][nc]]) {
                    if (nr + ndr === r && nc + ndc === c) {
                        visited[nr][nc] = true;
                        stack.push([nr, nc]);
                        break;
                    }
                }
            }
        }
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

    /**
     * @param Integer[][] $grid
     * @return Boolean
     */
    function hasValidPath($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $dirs = [
            [],
            [[0, -1], [0, 1]],
            [[-1, 0], [1, 0]],
            [[0, -1], [1, 0]],
            [[0, 1], [1, 0]],
            [[0, -1], [-1, 0]],
            [[0, 1], [-1, 0]]
        ];

        $visited = array_fill(0, $m, array_fill(0, $n, false));
        $stack = [[0, 0]];
        $visited[0][0] = true;

        while (!empty($stack)) {
            $curr = array_pop($stack);
            $r = $curr[0];
            $c = $curr[1];

            if ($r == $m - 1 && $c == $n - 1) return true;

            foreach ($dirs[$grid[$r][$c]] as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];

                if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && !$visited[$nr][$nc]) {
                    foreach ($dirs[$grid[$nr][$nc]] as $backDir) {
                        if ($nr + $backDir[0] == $r && $nc + $backDir[1] == $c) {
                            $visited[$nr][$nc] = true;
                            $stack[] = [$nr, $nc];
                            break;
                        }
                    }
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
    func hasValidPath(_ grid: [[Int]]) -> Bool {
        let m = grid.count
        let n = grid[0].count
        let dirs: [[[Int]]] = [
            [],
            [[0, -1], [0, 1]],
            [[-1, 0], [1, 0]],
            [[0, -1], [1, 0]],
            [[0, 1], [1, 0]],
            [[0, -1], [-1, 0]],
            [[0, 1], [-1, 0]]
        ]

        var visited = Array(repeating: Array(repeating: false, count: n), count: m)
        var stack = [(Int, Int)]()

        stack.append((0, 0))
        visited[0][0] = true

        while let (r, c) = stack.popLast() {
            if r == m - 1 && c == n - 1 { return true }

            for d in dirs[grid[r][c]] {
                let nr = r + d[0]
                let nc = c + d[1]

                if nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc] {
                    for backDir in dirs[grid[nr][nc]] {
                        if nr + backDir[0] == r && nc + backDir[1] == c {
                            visited[nr][nc] = true
                            stack.append((nr, nc))
                            break
                        }
                    }
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
import java.util.LinkedList
import java.util.Queue

class Solution {
    fun hasValidPath(grid: Array<IntArray>): Boolean {
        val m = grid.size
        val n = grid[0].size
        val connections = arrayOf(
            intArrayOf(),
            intArrayOf(2, 3), // 1: Left, Right
            intArrayOf(0, 1), // 2: Up, Down
            intArrayOf(2, 1), // 3: Left, Down
            intArrayOf(3, 1), // 4: Right, Down
            intArrayOf(2, 0), // 5: Left, Up
            intArrayOf(3, 0)  // 6: Right, Up
        )
        val dx = intArrayOf(-1, 1, 0, 0) // Up, Down, Left, Right
        val dy = intArrayOf(0, 0, -1, 1)
        val opposite = intArrayOf(1, 0, 3, 2)
        val visited = Array(m) { BooleanArray(n) }
        val queue: Queue<IntArray> = LinkedList()

        queue.offer(intArrayOf(0, 0))
        visited[0][0] = true

        while (queue.isNotEmpty()) {
            val curr = queue.poll()
            val r = curr[0]
            val c = curr[1]
            if (r == m - 1 && c == n - 1) return true

            for (dir in connections[grid[r][c]]) {
                val nr = r + dx[dir]
                val nc = c + dy[dir]
                if (nr in 0 until m && nc in 0 until n && !visited[nr][nc]) {
                    val nType = grid[nr][nc]
                    val opp = opposite[dir]
                    if (connections[nType].contains(opp)) {
                        visited[nr][nc] = true
                        queue.offer(intArrayOf(nr, nc))
                    }
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
import 'dart:collection';

class Solution {
  bool hasValidPath(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    List<List<int>> connections = [
      [],
      [2, 3], // 1: Left, Right
      [0, 1], // 2: Up, Down
      [2, 1], // 3: Left, Down
      [3, 1], // 4: Right, Down
      [2, 0], // 5: Left, Up
      [3, 0]  // 6: Right, Up
    ];
    List<int> dx = [-1, 1, 0, 0]; // Up, Down, Left, Right
    List<int> dy = [0, 0, -1, 1];
    List<int> opposite = [1, 0, 3, 2];
    List<List<bool>> visited = List.generate(m, (i) => List.filled(n, false));
    Queue<List<int>> queue = Queue();

    queue.add([0, 0]);
    visited[0][0] = true;

    while (queue.isNotEmpty) {
      List<int> curr = queue.removeFirst();
      int r = curr[0];
      int c = curr[1];
      if (r == m - 1 && c == n - 1) return true;

      for (int dir in connections[grid[r][c]]) {
        int nr = r + dx[dir];
        int nc = c + dy[dir];
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc]) {
          int nType = grid[nr][nc];
          int opp = opposite[dir];
          if (connections[nType].contains(opp)) {
            visited[nr][nc] = true;
            queue.add([nr, nc]);
          }
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
func hasValidPath(grid [][]int) bool {
	m := len(grid)
	n := len(grid[0])
	connections := [][]int{
		{},
		{2, 3}, // 1: Left, Right
		{0, 1}, // 2: Up, Down
		{2, 1}, // 3: Left, Down
		{3, 1}, // 4: Right, Down
		{2, 0}, // 5: Left, Up
		{3, 0}, // 6: Right, Up
	}
	dx := []int{-1, 1, 0, 0} // Up, Down, Left, Right
	dy := []int{0, 0, -1, 1}
	opposite := []int{1, 0, 3, 2}
	visited := make([][]bool, m)
	for i := range visited {
		visited[i] = make([]bool, n)
	}
	queue := [][]int{{0, 0}}
	visited[0][0] = true
	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]
		r, c := curr[0], curr[1]
		if r == m-1 && c == n-1 {
			return true
		}
		for _, dir := range connections[grid[r][c]] {
			nr, nc := r+dx[dir], c+dy[dir]
			if nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc] {
				nType := grid[nr][nc]
				opp := opposite[dir]
				canConnect := false
				for _, ndir := range connections[nType] {
					if ndir == opp {
						canConnect = true
						break
					}
				}
				if canConnect {
					visited[nr][nc] = true
					queue = append(queue, []int{nr, nc})
				}
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
# @param {Integer[][]} grid
# @return {Boolean}
def has_valid_path(grid)
  m = grid.length
  n = grid[0].length
  connections = [
    [],
    [2, 3], # 1: Left, Right
    [0, 1], # 2: Up, Down
    [2, 1], # 3: Left, Down
    [3, 1], # 4: Right, Down
    [2, 0], # 5: Left, Up
    [3, 0]  # 6: Right, Up
  ]
  dx = [-1, 1, 0, 0] # Up, Down, Left, Right
  dy = [0, 0, -1, 1]
  opposite = [1, 0, 3, 2]
  visited = Array.new(m) { Array.new(n, false) }
  queue = [[0, 0]]
  visited[0][0] = true
  head = 0
  while head < queue.length
    r, c = queue[head]
    head += 1
    return true if r == m - 1 && c == n - 1

    connections[grid[r][c]].each do |dir|
      nr, nc = r + dx[dir], c + dy[dir]
      if nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc]
        n_type = grid[nr][nc]
        opp = opposite[dir]
        if connections[n_type].include?(opp)
          visited[nr][nc] = true
          queue.push([nr, nc])
        end
      end
    end
  end
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
  def hasValidPath(grid: Array[Array[Int]]): Boolean = {
    val m = grid.length
    val n = grid(0).length
    val connections = Array(
      Array.empty[Int],
      Array(2, 3), // 1: Left, Right
      Array(0, 1), // 2: Up, Down
      Array(2, 1), // 3: Left, Down
      Array(3, 1), // 4: Right, Down
      Array(2, 0), // 5: Left, Up
      Array(3, 0)  // 6: Right, Up
    )
    val dx = Array(-1, 1, 0, 0) // Up, Down, Left, Right
    val dy = Array(0, 0, -1, 1)
    val opposite = Array(1, 0, 3, 2)
    val visited = Array.ofDim[Boolean](m, n)
    val queue = mutable.Queue[(Int, Int)]()

    queue.enqueue((0, 0))
    visited(0)(0) = true

    while (queue.nonEmpty) {
      val (r, c) = queue.dequeue()
      if (r == m - 1 && c == n - 1) return true

      for (dir <- connections(grid(r)(c))) {
        val nr = r + dx(dir)
        val nc = c + dy(dir)
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited(nr)(nc)) {
          val nType = grid(nr)(nc)
          val opp = opposite(dir)
          if (connections(nType).contains(opp)) {
            visited(nr)(nc) = true
            queue.enqueue((nr, nc))
          }
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
impl Solution {
    pub fn has_valid_path(grid: Vec<Vec<i32>>) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        let mut visited = vec![vec![false; n]; m];
        let mut stack = vec![(0, 0)];
        visited[0][0] = true;

        let dirs: [Vec<(i32, i32)>; 7] = [
            vec![],
            vec![(0, -1), (0, 1)],
            vec![(-1, 0), (1, 0)],
            vec![(0, -1), (1, 0)],
            vec![(0, 1), (1, 0)],
            vec![(0, -1), (-1, 0)],
            vec![(0, 1), (-1, 0)],
        ];

        while let Some((r, c)) = stack.pop() {
            if r == m - 1 && c == n - 1 {
                return true;
            }
            let street_type = grid[r][c] as usize;
            for &(dr, dc) in &dirs[street_type] {
                let nr = r as i32 + dr;
                let nc = c as i32 + dc;
                if nr >= 0 && nr < m as i32 && nc >= 0 && nc < n as i32 {
                    let unr = nr as usize;
                    let unc = nc as usize;
                    if !visited[unr][unc] {
                        let next_street_type = grid[unr][unc] as usize;
                        if dirs[next_street_type].iter().any(|&(ndr, ndc)| {
                            unr as i32 + ndr == r as i32 && unc as i32 + ndc == c as i32
                        }) {
                            visited[unr][unc] = true;
                            stack.push((unr, unc));
                        }
                    }
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
(define/contract (has-valid-path grid)
  (-> (listof (listof exact-integer?)) boolean?)
  (let* ([m (length grid)]
         [n (length (first grid))]
         [grid-vec (list->vector (map list->vector grid))]
         [dirs (vector #()
                       '((0 -1) (0 1))
                       '((-1 0) (1 0))
                       '((0 -1) (1 0))
                       '((0 1) (1 0))
                       '((0 -1) (-1 0))
                       '((0 1) (-1 0)))]
         [visited (make-vector (* m n) 0)])
    (define (get-grid r c) (vector-ref (vector-ref grid-vec r) c))
    (define (is-visited? r c) (= 1 (vector-ref visited (+ (* r n) c))))
    (define (set-visited! r c) (vector-set! visited (+ (* r n) c) 1))

    (define (can-move? r c nr nc)
      (and (>= nr 0) (< nr m) (>= nc 0) (< nc n)
           (not (is-visited? nr nc))
           (let ([curr-dirs (vector-ref dirs (get-grid r c))]
                 [next-dirs (vector-ref dirs (get-grid nr nc))])
             (and (member (list (- nr r) (- nc c)) curr-dirs)
                  (member (list (- r nr) (- c nc)) next-dirs)))))

    (set-visited! 0 0)
    (let loop ([front (list (cons 0 0))] [back '()])
      (cond
        [(and (null? front) (null? back)) #f]
        [(null? front) (loop (reverse back) '())]
        [else
         (let* ([curr (car front)]
                [r (car curr)]
                [c (cdr curr)])
           (if (and (= r (- m 1)) (= c (- n 1)))
               #t
               (let ([neighbors (for/list ([d (vector-ref dirs (get-grid r c))]
                                           #:let [nr (+ r (car d))
                                                  nc (+ c (cadr d))]
                                           #:when (can-move? r c nr nc))
                                  (set-visited! nr nc)
                                  (cons nr nc))])
                 (loop (cdr front) (foldl cons back neighbors))))]))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec has_valid_path(Grid :: [[integer()]]) -> boolean().
has_valid_path(Grid) ->
  M = length(Grid),
  N = length(hd(Grid)),
  Rows = lists:zip(lists:seq(0, M - 1), Grid),
  GridMap = maps:from_list([{{R, C}, Val} || {R, Row} <- Rows, {C, Val} <- lists:zip(lists:seq(0, N - 1), Row)]),
  Dirs = #{1 => [{0, -1}, {0, 1}], 2 => [{-1, 0}, {1, 0}], 3 => [{0, -1}, {1, 0}], 4 => [{0, 1}, {1, 0}], 5 => [{0, -1}, {-1, 0}], 6 => [{0, 1}, {-1, 0}]},
  Q = queue:in({0, 0}, queue:new()),
  Visited = sets:from_list([{0, 0}]),
  bfs(Q, Visited, M, N, GridMap, Dirs).

bfs(Q, Visited, M, N, GridMap, Dirs) ->
  case queue:out(Q) of
    {empty, _} -> false;
    {{value, {R, C}}, Q2} ->
      if
        R == M - 1, C == N - 1 -> true;
        true ->
          Type = maps:get({R, C}, GridMap),
          TypeDirs = maps:get(Type, Dirs),
          Neighbors = [{NR, NC} || {DR, DC} <- TypeDirs, 
                                   NR <- [R + DR], NC <- [C + DC],
                                   NR >= 0, NR < M, NC >= 0, NC < N,
                                   not sets:is_element({NR, NC}, Visited),
                                   check_back(NR, NC, R, C, GridMap, Dirs)],
          NewVisited = lists:foldl(fun(P, V) -> sets:add_element(P, V) end, Visited, Neighbors),
          NewQ = lists:foldl(fun(P, AccQ) -> queue:in(P, AccQ) end, Q2, Neighbors),
          bfs(NewQ, NewVisited, M, N, GridMap, Dirs)
      end
  end.

check_back(NR, NC, R, C, GridMap, Dirs) ->
  NextType = maps:get({NR, NC}, GridMap),
  NextDirs = maps:get(NextType, Dirs),
  lists:any(fun({NDR, NDC}) -> NR + NDR == R andalso NC + NDC == C end, NextDirs).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec has_valid_path(grid :: [[integer]]) :: boolean
  def has_valid_path(grid) do
    m = length(grid)
    n = length(hd(grid))
    grid_map = for {row, r} <- Enum.with_index(grid), {val, c} <- Enum.with_index(row), into: %{}, do: {{r, c}, val}
    dirs = %{
      1 => [{0, -1}, {0, 1}],
      2 => [{-1, 0}, {1, 0}],
      3 => [{0, -1}, {1, 0}],
      4 => [{0, 1}, {1, 0}],
      5 => [{0, -1}, {-1, 0}],
      6 => [{0, 1}, {-1, 0}]
    }
    bfs(:queue.from_list([{0, 0}]), MapSet.new([{0, 0}]), m, n, grid_map, dirs)
  end

  defp bfs(q, visited, m, n, grid_map, dirs) do
    case :queue.out(q) do
      {:empty, _} -> false
      {{:value, {r, c}}, nq} ->
        if r == m - 1 and c == n - 1 do
          true
        else
          neighbors = get_neighbors(r, c, grid_map, dirs, m, n, visited)
          new_visited = Enum.reduce(neighbors, visited, &MapSet.put(&2, &1))
          new_q = Enum.reduce(neighbors, nq, &:queue.in(&1, &2))
          bfs(new_q, new_visited, m, n, grid_map, dirs)
        end
    end
  end

  defp get_neighbors(r, c, grid_map, dirs, m, n, visited) do
    type = Map.get(grid_map, {r, c})
    curr_dirs = Map.get(dirs, type)
    curr_dirs
    |> Enum.map(fn {dr, dc} -> {r + dr, c + dc} end)
    |> Enum.filter(fn {nr, nc} ->
      nr >= 0 and nr < m and nc >= 0 and nc < n and
      not MapSet.member?(visited, {nr, nc}) and
      check_back(nr, nc, r, c, grid_map, dirs)
    end)
  end

  defp check_back(nr, nc, r, c, grid_map, dirs) do
    next_type = Map.get(grid_map, {nr, nc})
    next_dirs = Map.get(dirs, next_type)
    Enum.any?(next_dirs, fn {ndr, ndc} -> nr + ndr == r and nc + ndc == c end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(M * N) where M is the number of rows and N is the number of columns in the grid. Each cell is visited at most once and added to the queue, and for each cell, we perform a constant number of operations to check its two possible connections.
- **Space Complexity:** O(M * N) to store the visited status of each cell and the queue used for the BFS traversal, both of which can contain up to M * N elements in the worst case.
