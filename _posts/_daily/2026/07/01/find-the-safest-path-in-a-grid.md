---
layout: post
title: "Find the Safest Path in a Grid"
date: 2026-07-01 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Binary Search", "Breadth-First Search", "Union-Find", "Heap (Priority Queue)", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/find-the-safest-path-in-a-grid/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maximumSafenessFactor(vector<vector<int>>&\
        \ grid) {\n        int n = grid.size();\n        if (grid[0][0] == 1 || grid[n\
        \ - 1][n - 1] == 1) return 0;\n\n        vector<vector<int>> dist(n, vector<int>(n,\
        \ -1));\n        queue<pair<int, int>> q;\n\n        for (int i = 0; i < n;\
        \ ++i) {\n            for (int j = 0; j < n; ++j) {\n                if (grid[i][j]\
        \ == 1) {\n                    dist[i][j] = 0;\n                    q.push({i,\
        \ j});\n                }\n            }\n        }\n\n        int dr[] = {0,\
        \ 0, 1, -1};\n        int dc[] = {1, -1, 0, 0};\n\n        while (!q.empty())\
        \ {\n            pair<int, int> curr = q.front();\n            q.pop();\n  \
        \          for (int i = 0; i < 4; ++i) {\n                int ni = curr.first\
        \ + dr[i], nj = curr.second + dc[i];\n                if (ni >= 0 && ni < n\
        \ && nj >= 0 && nj < n && dist[ni][nj] == -1) {\n                    dist[ni][nj]\
        \ = dist[curr.first][curr.second] + 1;\n                    q.push({ni, nj});\n\
        \                }\n            }\n        }\n\n        priority_queue<pair<int,\
        \ pair<int, int>>> pq;\n        pq.push({dist[0][0], {0, 0}});\n        vector<vector<int>>\
        \ max_safe(n, vector<int>(n, -1));\n        max_safe[0][0] = dist[0][0];\n\n\
        \        while (!pq.empty()) {\n            int d = pq.top().first;\n      \
        \      int r = pq.top().second.first;\n            int c = pq.top().second.second;\n\
        \            pq.pop();\n\n            if (r == n - 1 && c == n - 1) return d;\n\
        \n            for (int i = 0; i < 4; ++i) {\n                int ni = r + dr[i],\
        \ nj = c + dc[i];\n                if (ni >= 0 && ni < n && nj >= 0 && nj <\
        \ n) {\n                    int new_s = min(d, dist[ni][nj]);\n            \
        \        if (new_s > max_safe[ni][nj]) {\n                        max_safe[ni][nj]\
        \ = new_s;\n                        pq.push({new_s, {ni, nj}});\n          \
        \          }\n                }\n            }\n        }\n\n        return\
        \ 0;\n    }\n};"
      java: "class Solution {\n    public int maximumSafenessFactor(List<List<Integer>>\
        \ grid) {\n        int n = grid.size();\n        int[][] dist = new int[n][n];\n\
        \        for (int i = 0; i < n; i++) Arrays.fill(dist[i], -1);\n        Deque<int[]>\
        \ q = new ArrayDeque<>();\n\n        for (int i = 0; i < n; i++) {\n       \
        \     for (int j = 0; j < n; j++) {\n                if (grid.get(i).get(j)\
        \ == 1) {\n                    dist[i][j] = 0;\n                    q.add(new\
        \ int[]{i, j});\n                }\n            }\n        }\n\n        int[]\
        \ dr = {0, 0, 1, -1};\n        int[] dc = {1, -1, 0, 0};\n\n        while (!q.isEmpty())\
        \ {\n            int[] curr = q.poll();\n            for (int i = 0; i < 4;\
        \ i++) {\n                int ni = curr[0] + dr[i], nj = curr[1] + dc[i];\n\
        \                if (ni >= 0 && ni < n && nj >= 0 && nj < n && dist[ni][nj]\
        \ == -1) {\n                    dist[ni][nj] = dist[curr[0]][curr[1]] + 1;\n\
        \                    q.add(new int[]{ni, nj});\n                }\n        \
        \    }\n        }\n\n        PriorityQueue<int[]> pq = new PriorityQueue<>((a,\
        \ b) -> b[0] - a[0]);\n        pq.add(new int[]{dist[0][0], 0, 0});\n      \
        \  int[][] maxSafe = new int[n][n];\n        for (int i = 0; i < n; i++) Arrays.fill(maxSafe[i],\
        \ -1);\n        maxSafe[0][0] = dist[0][0];\n\n        while (!pq.isEmpty())\
        \ {\n            int[] curr = pq.poll();\n            int d = curr[0], r = curr[1],\
        \ c = curr[2];\n\n            if (r == n - 1 && c == n - 1) return d;\n\n  \
        \          for (int i = 0; i < 4; i++) {\n                int ni = r + dr[i],\
        \ nj = c + dc[i];\n                if (ni >= 0 && ni < n && nj >= 0 && nj <\
        \ n) {\n                    int s = Math.min(d, dist[ni][nj]);\n           \
        \         if (s > maxSafe[ni][nj]) {\n                        maxSafe[ni][nj]\
        \ = s;\n                        pq.add(new int[]{s, ni, nj});\n            \
        \        }\n                }\n            }\n        }\n\n        return 0;\n\
        \    }\n}"
      python: "import heapq\nfrom collections import deque\n\nclass Solution(object):\n\
        \    def maximumSafenessFactor(self, grid):\n        \"\"\"\n        :type grid:\
        \ List[List[int]]\n        :rtype: int\n        \"\"\"\n        n = len(grid)\n\
        \        dist = [[-1] * n for _ in range(n)]\n        q = deque()\n\n      \
        \  for r in range(n):\n            for c in range(n):\n                if grid[r][c]\
        \ == 1:\n                    dist[r][c] = 0\n                    q.append((r,\
        \ c))\n\n        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]\n        while q:\n\
        \            r, c = q.popleft()\n            for dr, dc in dirs:\n         \
        \       nr, nc = r + dr, c + dc\n                if 0 <= nr < n and 0 <= nc\
        \ < n and dist[nr][nc] == -1:\n                    dist[nr][nc] = dist[r][c]\
        \ + 1\n                    q.append((nr, nc))\n\n        pq = [(-dist[0][0],\
        \ 0, 0)]\n        max_safe = [[-1] * n for _ in range(n)]\n        max_safe[0][0]\
        \ = dist[0][0]\n\n        while pq:\n            d, r, c = heapq.heappop(pq)\n\
        \            d = -d\n            if r == n - 1 and c == n - 1:\n           \
        \     return d\n            for dr, dc in dirs:\n                nr, nc = r\
        \ + dr, c + dc\n                if 0 <= nr < n and 0 <= nc < n:\n          \
        \          new_s = min(d, dist[nr][nc])\n                    if new_s > max_safe[nr][nc]:\n\
        \                        max_safe[nr][nc] = new_s\n                        heapq.heappush(pq,\
        \ (-new_s, nr, nc))\n        return 0"
      python3: "import heapq\nfrom collections import deque\n\nclass Solution:\n   \
        \ def maximumSafenessFactor(self, grid: List[List[int]]) -> int:\n        n\
        \ = len(grid)\n        dist = [[-1] * n for _ in range(n)]\n        q = deque()\n\
        \n        for r in range(n):\n            for c in range(n):\n             \
        \   if grid[r][c] == 1:\n                    dist[r][c] = 0\n              \
        \      q.append((r, c))\n\n        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]\n\
        \        while q:\n            r, c = q.popleft()\n            for dr, dc in\
        \ dirs:\n                nr, nc = r + dr, c + dc\n                if 0 <= nr\
        \ < n and 0 <= nc < n and dist[nr][nc] == -1:\n                    dist[nr][nc]\
        \ = dist[r][c] + 1\n                    q.append((nr, nc))\n\n        pq = [(-dist[0][0],\
        \ 0, 0)]\n        max_safe = [[-1] * n for _ in range(n)]\n        max_safe[0][0]\
        \ = dist[0][0]\n\n        while pq:\n            d, r, c = heapq.heappop(pq)\n\
        \            d = -d\n            if r == n - 1 and c == n - 1:\n           \
        \     return d\n            for dr, dc in dirs:\n                nr, nc = r\
        \ + dr, c + dc\n                if 0 <= nr < n and 0 <= nc < n:\n          \
        \          new_s = min(d, dist[nr][nc])\n                    if new_s > max_safe[nr][nc]:\n\
        \                        max_safe[nr][nc] = new_s\n                        heapq.heappush(pq,\
        \ (-new_s, nr, nc))\n        return 0"
      c: "#include <stdbool.h>\n#include <stdlib.h>\n#include <string.h>\n\n#define\
        \ MIN(a, b) ((a) < (b) ? (a) : (b))\n\nint dr[] = {0, 0, 1, -1};\nint dc[] =\
        \ {1, -1, 0, 0};\n\nbool canReach(int v, int n, int** dist, char** visited,\
        \ int* qr, int* qc) {\n    if (dist[0][0] < v || dist[n - 1][n - 1] < v) return\
        \ false;\n    for (int i = 0; i < n; i++) memset(visited[i], 0, n);\n    int\
        \ head = 0, tail = 0;\n    qr[tail] = 0; qc[tail] = 0; tail++;\n    visited[0][0]\
        \ = 1;\n    while (head < tail) {\n        int r = qr[head], c = qc[head]; head++;\n\
        \        if (r == n - 1 && c == n - 1) return true;\n        for (int i = 0;\
        \ i < 4; i++) {\n            int nr = r + dr[i], nc = c + dc[i];\n         \
        \   if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc] && dist[nr][nc]\
        \ >= v) {\n                visited[nr][nc] = 1;\n                qr[tail] =\
        \ nr; qc[tail] = nc; tail++;\n            }\n        }\n    }\n    return false;\n\
        }\n\nint maximumSafenessFactor(int** grid, int gridSize, int* gridColSize) {\n\
        \    int n = gridSize;\n    int** dist = (int**)malloc(n * sizeof(int*));\n\
        \    char** visited = (char**)malloc(n * sizeof(char*));\n    for (int i = 0;\
        \ i < n; i++) {\n        dist[i] = (int*)malloc(n * sizeof(int));\n        visited[i]\
        \ = (char*)malloc(n);\n        for (int j = 0; j < n; j++) dist[i][j] = -1;\n\
        \    }\n\n    int* qr = (int*)malloc(n * n * sizeof(int));\n    int* qc = (int*)malloc(n\
        \ * n * sizeof(int));\n    int head = 0, tail = 0;\n\n    for (int i = 0; i\
        \ < n; i++) {\n        for (int j = 0; j < n; j++) {\n            if (grid[i][j]\
        \ == 1) {\n                dist[i][j] = 0;\n                qr[tail] = i; qc[tail]\
        \ = j; tail++;\n            }\n        }\n    }\n\n    while (head < tail) {\n\
        \        int r = qr[head], c = qc[head]; head++;\n        for (int i = 0; i\
        \ < 4; i++) {\n            int nr = r + dr[i], nc = c + dc[i];\n           \
        \ if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] == -1) {\n    \
        \            dist[nr][nc] = dist[r][c] + 1;\n                qr[tail] = nr;\
        \ qc[tail] = nc; tail++;\n            }\n        }\n    }\n\n    int low = 0,\
        \ high = 2 * n, ans = 0;\n    while (low <= high) {\n        int mid = low +\
        \ (high - low) / 2;\n        if (canReach(mid, n, dist, visited, qr, qc)) {\n\
        \            ans = mid;\n            low = mid + 1;\n        } else {\n    \
        \        high = mid - 1;\n        }\n    }\n\n    for (int i = 0; i < n; i++)\
        \ {\n        free(dist[i]);\n        free(visited[i]);\n    }\n    free(dist);\
        \ free(visited); free(qr); free(qc);\n    return ans;\n}"
      csharp: "public class Solution {\n    public int MaximumSafenessFactor(IList<IList<int>>\
        \ grid) {\n        int n = grid.Count;\n        int[] dist = new int[n * n];\n\
        \        for (int i = 0; i < n * n; i++) dist[i] = -1;\n\n        Queue<int>\
        \ q = new Queue<int>();\n        for (int r = 0; r < n; r++) {\n           \
        \ for (int c = 0; c < n; c++) {\n                if (grid[r][c] == 1) {\n  \
        \                  dist[r * n + c] = 0;\n                    q.Enqueue(r * n\
        \ + c);\n                }\n            }\n        }\n\n        int[] dr = {\
        \ 0, 0, 1, -1 };\n        int[] dc = { 1, -1, 0, 0 };\n\n        while (q.Count\
        \ > 0) {\n            int idx = q.Dequeue();\n            int r = idx / n;\n\
        \            int c = idx % n;\n            for (int i = 0; i < 4; i++) {\n \
        \               int nr = r + dr[i], nc = c + dc[i];\n                if (nr\
        \ >= 0 && nr < n && nc >= 0 && nc < n) {\n                    int nidx = nr\
        \ * n + nc;\n                    if (dist[nidx] == -1) {\n                 \
        \       dist[nidx] = dist[idx] + 1;\n                        q.Enqueue(nidx);\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    int left = 0, right = Math.Min(dist[0], dist[n * n - 1]);\n        int\
        \ ans = 0;\n        while (left <= right) {\n            int mid = left + (right\
        \ - left) / 2;\n            if (CanReach(dist, mid, n)) {\n                ans\
        \ = mid;\n                left = mid + 1;\n            } else {\n          \
        \      right = mid - 1;\n            }\n        }\n        return ans;\n   \
        \ }\n\n    private bool CanReach(int[] dist, int minSafe, int n) {\n       \
        \ if (dist[0] < minSafe || dist[n * n - 1] < minSafe) return false;\n      \
        \  Queue<int> q = new Queue<int>();\n        bool[] visited = new bool[n * n];\n\
        \        q.Enqueue(0);\n        visited[0] = true;\n\n        int[] dr = { 0,\
        \ 0, 1, -1 };\n        int[] dc = { 1, -1, 0, 0 };\n\n        while (q.Count\
        \ > 0) {\n            int idx = q.Dequeue();\n            if (idx == n * n -\
        \ 1) return true;\n            int r = idx / n;\n            int c = idx % n;\n\
        \            for (int i = 0; i < 4; i++) {\n                int nr = r + dr[i],\
        \ nc = c + dc[i];\n                if (nr >= 0 && nr < n && nc >= 0 && nc <\
        \ n) {\n                    int nidx = nr * n + nc;\n                    if\
        \ (!visited[nidx] && dist[nidx] >= minSafe) {\n                        visited[nidx]\
        \ = true;\n                        q.Enqueue(nidx);\n                    }\n\
        \                }\n            }\n        }\n        return false;\n    }\n\
        }"
      javascript: "/**\n * @param {number[][]} grid\n * @return {number}\n */\nvar maximumSafenessFactor\
        \ = function(grid) {\n    const n = grid.length;\n    const dist = new Int32Array(n\
        \ * n).fill(-1);\n    const q = [];\n\n    for (let r = 0; r < n; r++) {\n \
        \       for (let c = 0; c < n; c++) {\n            if (grid[r][c] === 1) {\n\
        \                dist[r * n + c] = 0;\n                q.push(r * n + c);\n\
        \            }\n        }\n    }\n\n    let head = 0;\n    const dr = [0, 0,\
        \ 1, -1], dc = [1, -1, 0, 0];\n    while (head < q.length) {\n        const\
        \ idx = q[head++];\n        const r = Math.floor(idx / n), c = idx % n;\n  \
        \      for (let i = 0; i < 4; i++) {\n            const nr = r + dr[i], nc =\
        \ c + dc[i];\n            if (nr >= 0 && nr < n && nc >= 0 && nc < n) {\n  \
        \              const nidx = nr * n + nc;\n                if (dist[nidx] ===\
        \ -1) {\n                    dist[nidx] = dist[idx] + 1;\n                 \
        \   q.push(nidx);\n                }\n            }\n        }\n    }\n\n  \
        \  const canReach = (minSafe) => {\n        if (dist[0] < minSafe || dist[n\
        \ * n - 1] < minSafe) return false;\n        const q2 = [0];\n        const\
        \ visited = new Uint8Array(n * n);\n        visited[0] = 1;\n        let head2\
        \ = 0;\n        while (head2 < q2.length) {\n            const idx = q2[head2++];\n\
        \            if (idx === n * n - 1) return true;\n            const r = Math.floor(idx\
        \ / n), c = idx % n;\n            for (let i = 0; i < 4; i++) {\n          \
        \      const nr = r + dr[i], nc = c + dc[i];\n                if (nr >= 0 &&\
        \ nr < n && nc >= 0 && nc < n) {\n                    const nidx = nr * n +\
        \ nc;\n                    if (!visited[nidx] && dist[nidx] >= minSafe) {\n\
        \                        visited[nidx] = 1;\n                        q2.push(nidx);\n\
        \                    }\n                }\n            }\n        }\n      \
        \  return false;\n    };\n\n    let left = 0, right = Math.min(dist[0], dist[n\
        \ * n - 1]), ans = 0;\n    while (left <= right) {\n        const mid = Math.floor((left\
        \ + right) / 2);\n        if (canReach(mid)) {\n            ans = mid;\n   \
        \         left = mid + 1;\n        } else {\n            right = mid - 1;\n\
        \        }\n    }\n    return ans;\n};"
      typescript: "function maximumSafenessFactor(grid: number[][]): number {\n    const\
        \ n = grid.length;\n    const dist = new Int32Array(n * n).fill(-1);\n    const\
        \ q: number[] = [];\n\n    for (let r = 0; r < n; r++) {\n        for (let c\
        \ = 0; c < n; c++) {\n            if (grid[r][c] === 1) {\n                dist[r\
        \ * n + c] = 0;\n                q.push(r * n + c);\n            }\n       \
        \ }\n    }\n\n    let head = 0;\n    const dr = [0, 0, 1, -1], dc = [1, -1,\
        \ 0, 0];\n    while (head < q.length) {\n        const idx = q[head++];\n  \
        \      const r = Math.floor(idx / n), c = idx % n;\n        for (let i = 0;\
        \ i < 4; i++) {\n            const nr = r + dr[i], nc = c + dc[i];\n       \
        \     if (nr >= 0 && nr < n && nc >= 0 && nc < n) {\n                const nidx\
        \ = nr * n + nc;\n                if (dist[nidx] === -1) {\n               \
        \     dist[nidx] = dist[idx] + 1;\n                    q.push(nidx);\n     \
        \           }\n            }\n        }\n    }\n\n    const canReach = (minSafe:\
        \ number): boolean => {\n        if (dist[0] < minSafe || dist[n * n - 1] <\
        \ minSafe) return false;\n        const q2: number[] = [0];\n        const visited\
        \ = new Uint8Array(n * n);\n        visited[0] = 1;\n        let head2 = 0;\n\
        \        while (head2 < q2.length) {\n            const idx = q2[head2++];\n\
        \            if (idx === n * n - 1) return true;\n            const r = Math.floor(idx\
        \ / n), c = idx % n;\n            for (let i = 0; i < 4; i++) {\n          \
        \      const nr = r + dr[i], nc = c + dc[i];\n                if (nr >= 0 &&\
        \ nr < n && nc >= 0 && nc < n) {\n                    const nidx = nr * n +\
        \ nc;\n                    if (!visited[nidx] && dist[nidx] >= minSafe) {\n\
        \                        visited[nidx] = 1;\n                        q2.push(nidx);\n\
        \                    }\n                }\n            }\n        }\n      \
        \  return false;\n    };\n\n    let left = 0, right = Math.min(dist[0], dist[n\
        \ * n - 1]), ans = 0;\n    while (left <= right) {\n        const mid = Math.floor((left\
        \ + right) / 2);\n        if (canReach(mid)) {\n            ans = mid;\n   \
        \         left = mid + 1;\n        } else {\n            right = mid - 1;\n\
        \        }\n    }\n    return ans;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @return\
        \ Integer\n     */\n    function maximumSafenessFactor($grid) {\n        $n\
        \ = count($grid);\n        $dist = new \\SplFixedArray($n * $n);\n        for\
        \ ($i = 0; $i < $n * $n; $i++) $dist[$i] = -1;\n\n        $q = new \\SplQueue();\n\
        \        for ($r = 0; $r < $n; $r++) {\n            for ($c = 0; $c < $n; $c++)\
        \ {\n                if ($grid[$r][$c] == 1) {\n                    $dist[$r\
        \ * $n + $c] = 0;\n                    $q->enqueue($r * $n + $c);\n        \
        \        }\n            }\n        }\n\n        $dr = [0, 0, 1, -1];\n     \
        \   $dc = [1, -1, 0, 0];\n\n        while (!$q->isEmpty()) {\n            $idx\
        \ = $q->dequeue();\n            $r = (int)($idx / $n);\n            $c = $idx\
        \ % $n;\n            for ($i = 0; $i < 4; $i++) {\n                $nr = $r\
        \ + $dr[$i];\n                $nc = $c + $dc[$i];\n                if ($nr >=\
        \ 0 && $nr < $n && $nc >= 0 && $nc < $n) {\n                    $nidx = $nr\
        \ * $n + $nc;\n                    if ($dist[$nidx] === -1) {\n            \
        \            $dist[$nidx] = $dist[$idx] + 1;\n                        $q->enqueue($nidx);\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    $canReach = function($minSafe) use ($dist, $n, $dr, $dc) {\n          \
        \  if ($dist[0] < $minSafe || $dist[$n * $n - 1] < $minSafe) return false;\n\
        \            $q2 = new \\SplQueue();\n            $q2->enqueue(0);\n       \
        \     $visited = new \\SplFixedArray($n * $n);\n            $visited[0] = true;\n\
        \            while (!$q2->isEmpty()) {\n                $idx = $q2->dequeue();\n\
        \                if ($idx === $n * $n - 1) return true;\n                $r\
        \ = (int)($idx / $n);\n                $c = $idx % $n;\n                for\
        \ ($i = 0; $i < 4; $i++) {\n                    $nr = $r + $dr[$i];\n      \
        \              $nc = $c + $dc[$i];\n                    if ($nr >= 0 && $nr\
        \ < $n && $nc >= 0 && $nc < $n) {\n                        $nidx = $nr * $n\
        \ + $nc;\n                        if (!$visited[$nidx] && $dist[$nidx] >= $minSafe)\
        \ {\n                            $visited[$nidx] = true;\n                 \
        \           $q2->enqueue($nidx);\n                        }\n              \
        \      }\n                }\n            }\n            return false;\n    \
        \    };\n\n        $left = 0;\n        $right = min($dist[0], $dist[$n * $n\
        \ - 1]);\n        $ans = 0;\n        while ($left <= $right) {\n           \
        \ $mid = (int)(($left + $right) / 2);\n            if ($canReach($mid)) {\n\
        \                $ans = $mid;\n                $left = $mid + 1;\n         \
        \   } else {\n                $right = $mid - 1;\n            }\n        }\n\
        \        return $ans;\n    }\n}"
      swift: "class Solution {\n    func maximumSafenessFactor(_ grid: [[Int]]) -> Int\
        \ {\n        let n = grid.count\n        var dist = [Int](repeating: -1, count:\
        \ n * n)\n        var q = [Int]()\n\n        for r in 0..<n {\n            for\
        \ c in 0..<n {\n                if grid[r][c] == 1 {\n                    dist[r\
        \ * n + c] = 0\n                    q.append(r * n + c)\n                }\n\
        \            }\n        }\n\n        let dr = [0, 0, 1, -1]\n        let dc\
        \ = [1, -1, 0, 0]\n        var head = 0\n        while head < q.count {\n  \
        \          let idx = q[head]\n            head += 1\n            let r = idx\
        \ / n\n            let c = idx % n\n            for i in 0..<4 {\n         \
        \       let nr = r + dr[i]\n                let nc = c + dc[i]\n           \
        \     if nr >= 0 && nr < n && nc >= 0 && nc < n {\n                    let nidx\
        \ = nr * n + nc\n                    if dist[nidx] == -1 {\n               \
        \         dist[nidx] = dist[idx] + 1\n                        q.append(nidx)\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    func canReach(minSafe: Int) -> Bool {\n            if dist[0] < minSafe\
        \ || dist[n * n - 1] < minSafe { return false }\n            var visited = [Bool](repeating:\
        \ false, count: n * n)\n            var q2 = [0]\n            visited[0] = true\n\
        \            var head2 = 0\n            while head2 < q2.count {\n         \
        \       let idx = q2[head2]\n                head2 += 1\n                if\
        \ idx == n * n - 1 { return true }\n                let r = idx / n\n      \
        \          let c = idx % n\n                for i in 0..<4 {\n             \
        \       let nr = r + dr[i]\n                    let nc = c + dc[i]\n       \
        \             if nr >= 0 && nr < n && nc >= 0 && nc < n {\n                \
        \        let nidx = nr * n + nc\n                        if !visited[nidx] &&\
        \ dist[nidx] >= minSafe {\n                            visited[nidx] = true\n\
        \                            q2.append(nidx)\n                        }\n  \
        \                  }\n                }\n            }\n            return false\n\
        \        }\n\n        var left = 0\n        var right = min(dist[0], dist[n\
        \ * n - 1])\n        var ans = 0\n        while left <= right {\n          \
        \  let mid = (left + right) / 2\n            if canReach(minSafe: mid) {\n \
        \               ans = mid\n                left = mid + 1\n            } else\
        \ {\n                right = mid - 1\n            }\n        }\n        return\
        \ ans\n    }\n}"
      kotlin: "import java.util.ArrayDeque\n\nclass Solution {\n    fun maximumSafenessFactor(grid:\
        \ List<List<Int>>): Int {\n        val n = grid.size\n        if (grid[0][0]\
        \ == 1 || grid[n - 1][n - 1] == 1) return 0\n\n        val dist = Array(n) {\
        \ IntArray(n) { -1 } }\n        val q = ArrayDeque<Int>()\n\n        for (r\
        \ in 0 until n) {\n            for (c in 0 until n) {\n                if (grid[r][c]\
        \ == 1) {\n                    dist[r][c] = 0\n                    q.add(r *\
        \ n + c)\n                }\n            }\n        }\n\n        val dr = intArrayOf(0,\
        \ 0, 1, -1)\n        val dc = intArrayOf(1, -1, 0, 0)\n\n        while (q.isNotEmpty())\
        \ {\n            val curr = q.poll()\n            val r = curr / n\n       \
        \     val c = curr % n\n            for (i in 0 until 4) {\n               \
        \ val nr = r + dr[i]\n                val nc = c + dc[i]\n                if\
        \ (nr in 0 until n && nc in 0 until n && dist[nr][nc] == -1) {\n           \
        \         dist[nr][nc] = dist[r][c] + 1\n                    q.add(nr * n +\
        \ nc)\n                }\n            }\n        }\n\n        fun isPossible(v:\
        \ Int): Boolean {\n            if (dist[0][0] < v || dist[n - 1][n - 1] < v)\
        \ return false\n            val queue = ArrayDeque<Int>()\n            queue.add(0)\n\
        \            val visited = BooleanArray(n * n)\n            visited[0] = true\n\
        \            while (queue.isNotEmpty()) {\n                val curr = queue.poll()\n\
        \                val r = curr / n\n                val c = curr % n\n      \
        \          if (r == n - 1 && c == n - 1) return true\n                for (i\
        \ in 0 until 4) {\n                    val nr = r + dr[i]\n                \
        \    val nc = c + dc[i]\n                    val nIdx = nr * n + nc\n      \
        \              if (nr in 0 until n && nc in 0 until n && !visited[nIdx] && dist[nr][nc]\
        \ >= v) {\n                        visited[nIdx] = true\n                  \
        \      queue.add(nIdx)\n                    }\n                }\n         \
        \   }\n            return false\n        }\n\n        var low = 0\n        var\
        \ high = 2 * n\n        var ans = 0\n        while (low <= high) {\n       \
        \     val mid = (low + high) / 2\n            if (isPossible(mid)) {\n     \
        \           ans = mid\n                low = mid + 1\n            } else {\n\
        \                high = mid - 1\n            }\n        }\n        return ans\n\
        \    }\n}"
      dart: "import 'dart:collection';\nimport 'dart:math';\n\nclass Solution {\n  int\
        \ maximumSafenessFactor(List<List<int>> grid) {\n    int n = grid.length;\n\
        \    if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return 0;\n\n    List<List<int>>\
        \ dist = List.generate(n, (_) => List.filled(n, -1));\n    Queue<int> q = Queue<int>();\n\
        \n    for (int r = 0; r < n; r++) {\n      for (int c = 0; c < n; c++) {\n \
        \       if (grid[r][c] == 1) {\n          dist[r][c] = 0;\n          q.add(r\
        \ * n + c);\n        }\n      }\n    }\n\n    List<int> dr = [0, 0, 1, -1];\n\
        \    List<int> dc = [1, -1, 0, 0];\n\n    while (q.isNotEmpty) {\n      int\
        \ curr = q.removeFirst();\n      int r = curr ~/ n;\n      int c = curr % n;\n\
        \      for (int i = 0; i < 4; i++) {\n        int nr = r + dr[i];\n        int\
        \ nc = c + dc[i];\n        if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc]\
        \ == -1) {\n          dist[nr][nc] = dist[r][c] + 1;\n          q.add(nr * n\
        \ + nc);\n        }\n      }\n    }\n\n    bool isPossible(int v) {\n      if\
        \ (dist[0][0] < v || dist[n - 1][n - 1] < v) return false;\n      Queue<int>\
        \ queue = Queue<int>();\n      queue.add(0);\n      List<bool> visited = List.filled(n\
        \ * n, false);\n      visited[0] = true;\n      while (queue.isNotEmpty) {\n\
        \        int curr = queue.removeFirst();\n        int r = curr ~/ n;\n     \
        \   int c = curr % n;\n        if (r == n - 1 && c == n - 1) return true;\n\
        \        for (int i = 0; i < 4; i++) {\n          int nr = r + dr[i];\n    \
        \      int nc = c + dc[i];\n          int idx = nr * n + nc;\n          if (nr\
        \ >= 0 && nr < n && nc >= 0 && nc < n && !visited[idx] && dist[nr][nc] >= v)\
        \ {\n            visited[idx] = true;\n            queue.add(idx);\n       \
        \   }\n        }\n      }\n      return false;\n    }\n\n    int low = 0;\n\
        \    int high = 2 * n;\n    int ans = 0;\n    while (low <= high) {\n      int\
        \ mid = (low + high) ~/ 2;\n      if (isPossible(mid)) {\n        ans = mid;\n\
        \        low = mid + 1;\n      } else {\n        high = mid - 1;\n      }\n\
        \    }\n    return ans;\n  }\n}"
      go: "func maximumSafenessFactor(grid [][]int) int {\n\tn := len(grid)\n\tif grid[0][0]\
        \ == 1 || grid[n-1][n-1] == 1 {\n\t\treturn 0\n\t}\n\n\tdist := make([][]int,\
        \ n)\n\tfor i := range dist {\n\t\tdist[i] = make([]int, n)\n\t\tfor j := range\
        \ dist[i] {\n\t\t\tdist[i][j] = -1\n\t\t}\n\t}\n\n\tqueue := make([]int, 0,\
        \ n*n)\n\tfor r := 0; r < n; r++ {\n\t\tfor c := 0; c < n; c++ {\n\t\t\tif grid[r][c]\
        \ == 1 {\n\t\t\t\tdist[r][c] = 0\n\t\t\t\tqueue = append(queue, r*n+c)\n\t\t\
        \t}\n\t\t}\n\t}\n\n\tdr := []int{0, 0, 1, -1}\n\tdc := []int{1, -1, 0, 0}\n\n\
        \thead := 0\n\tfor head < len(queue) {\n\t\tcurr := queue[head]\n\t\thead++\n\
        \t\tr, c := curr/n, curr%n\n\t\tfor i := 0; i < 4; i++ {\n\t\t\tnr, nc := r+dr[i],\
        \ c+dc[i]\n\t\t\tif nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] ==\
        \ -1 {\n\t\t\t\tdist[nr][nc] = dist[r][c] + 1\n\t\t\t\tqueue = append(queue,\
        \ nr*n+nc)\n\t\t\t}\n\t\t}\n\t}\n\n\tisPossible := func(v int) bool {\n\t\t\
        if dist[0][0] < v || dist[n-1][n-1] < v {\n\t\t\treturn false\n\t\t}\n\t\tq\
        \ := make([]int, 0, n*n)\n\t\tq = append(q, 0)\n\t\tvisited := make([]bool,\
        \ n*n)\n\t\tvisited[0] = true\n\t\th := 0\n\t\tfor h < len(q) {\n\t\t\tcurr\
        \ := q[h]\n\t\th++\n\t\t\tr, c := curr/n, curr%n\n\t\t\tif r == n-1 && c ==\
        \ n-1 {\n\t\t\t\treturn true\n\t\t\t}\n\t\t\tfor i := 0; i < 4; i++ {\n\t\t\t\
        \tnr, nc := r+dr[i], c+dc[i]\n\t\t\t\tidx := nr*n + nc\n\t\t\t\tif nr >= 0 &&\
        \ nr < n && nc >= 0 && nc < n && !visited[idx] && dist[nr][nc] >= v {\n\t\t\t\
        \t\tvisited[idx] = true\n\t\t\t\t\tq = append(q, idx)\n\t\t\t\t}\n\t\t\t}\n\t\
        \t}\n\t\treturn false\n\t}\n\n\tlow, high := 0, 2*n\n\tans := 0\n\tfor low <=\
        \ high {\n\t\tmid := (low + high) / 2\n\t\tif isPossible(mid) {\n\t\t\tans =\
        \ mid\n\t\t\tlow = mid + 1\n\t\t} else {\n\t\t\thigh = mid - 1\n\t\t}\n\t}\n\
        \treturn ans\n}"
      ruby: "# @param {Integer[][]} grid\n# @return {Integer}\ndef maximum_safeness_factor(grid)\n\
        \  n = grid.length\n  return 0 if grid[0][0] == 1 || grid[n - 1][n - 1] == 1\n\
        \n  dist = Array.new(n) { Array.new(n, -1) }\n  queue = []\n  n.times do |r|\n\
        \    n.times do |c|\n      if grid[r][c] == 1\n        dist[r][c] = 0\n    \
        \    queue << (r * n + c)\n      end\n    end\n  end\n\n  dr = [0, 0, 1, -1]\n\
        \  dc = [1, -1, 0, 0]\n\n  head = 0\n  while head < queue.length\n    curr =\
        \ queue[head]\n    head += 1\n    r, c = curr / n, curr % n\n    4.times do\
        \ |i|\n      nr, nc = r + dr[i], c + dc[i]\n      if nr >= 0 && nr < n && nc\
        \ >= 0 && nc < n && dist[nr][nc] == -1\n        dist[nr][nc] = dist[r][c] +\
        \ 1\n        queue << (nr * n + nc)\n      end\n    end\n  end\n\n  is_possible\
        \ = lambda do |v|\n    return false if dist[0][0] < v || dist[n - 1][n - 1]\
        \ < v\n    q = [0]\n    visited = Array.new(n * n, false)\n    visited[0] =\
        \ true\n    h = 0\n    while h < q.length\n      curr = q[h]\n      h += 1\n\
        \      r, c = curr / n, curr % n\n      return true if r == n - 1 && c == n\
        \ - 1\n      4.times do |i|\n        nr, nc = r + dr[i], c + dc[i]\n       \
        \ idx = nr * n + nc\n        if nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[idx]\
        \ && dist[nr][nc] >= v\n          visited[idx] = true\n          q << idx\n\
        \        end\n      end\n    end\n    false\n  end\n\n  low, high = 0, 2 * n\n\
        \  ans = 0\n  while low <= high\n    mid = (low + high) / 2\n    if is_possible.call(mid)\n\
        \      ans = mid\n      low = mid + 1\n    else\n      high = mid - 1\n    end\n\
        \  end\n  ans\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def maximumSafenessFactor(grid:\
        \ List[List[Int]]): Int = {\n        val n = grid.size\n        val g = grid.map(_.toArray).toArray\n\
        \        if (g(0)(0) == 1 || g(n - 1)(n - 1) == 1) return 0\n\n        val dist\
        \ = Array.fill(n, n)(-1)\n        val q = mutable.Queue[Int]()\n\n        for\
        \ (r <- 0 until n; c <- 0 until n) {\n            if (g(r)(c) == 1) {\n    \
        \            dist(r)(c) = 0\n                q.enqueue(r * n + c)\n        \
        \    }\n        }\n\n        val dr = Array(0, 0, 1, -1)\n        val dc = Array(1,\
        \ -1, 0, 0)\n\n        while (q.nonEmpty) {\n            val curr = q.dequeue()\n\
        \            val r = curr / n\n            val c = curr % n\n            for\
        \ (i <- 0 until 4) {\n                val nr = r + dr(i)\n                val\
        \ nc = c + dc(i)\n                if (nr >= 0 && nr < n && nc >= 0 && nc < n\
        \ && dist(nr)(nc) == -1) {\n                    dist(nr)(nc) = dist(r)(c) +\
        \ 1\n                    q.enqueue(nr * n + nc)\n                }\n       \
        \     }\n        }\n\n        def isPossible(v: Int): Boolean = {\n        \
        \    if (dist(0)(0) < v || dist(n - 1)(n - 1) < v) return false\n          \
        \  val queue = mutable.Queue[Int]()\n            queue.enqueue(0)\n        \
        \    val visited = Array.fill(n * n)(false)\n            visited(0) = true\n\
        \            while (queue.nonEmpty) {\n                val curr = queue.dequeue()\n\
        \                val r = curr / n\n                val c = curr % n\n      \
        \          if (r == n - 1 && c == n - 1) return true\n                for (i\
        \ <- 0 until 4) {\n                    val nr = r + dr(i)\n                \
        \    val nc = c + dc(i)\n                    val idx = nr * n + nc\n       \
        \             if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited(idx) &&\
        \ dist(nr)(nc) >= v) {\n                        visited(idx) = true\n      \
        \                  queue.enqueue(idx)\n                    }\n             \
        \   }\n            }\n            false\n        }\n\n        var low = 0\n\
        \        var high = 2 * n\n        var ans = 0\n        while (low <= high)\
        \ {\n            val mid = (low + high) / 2\n            if (isPossible(mid))\
        \ {\n                ans = mid\n                low = mid + 1\n            }\
        \ else {\n                high = mid - 1\n            }\n        }\n       \
        \ ans\n    }\n}"
      rust: "use std::collections::{BinaryHeap, VecDeque};\n\nimpl Solution {\n    pub\
        \ fn maximum_safeness_factor(grid: Vec<Vec<i32>>) -> i32 {\n        let n =\
        \ grid.len();\n        if grid[0][0] == 1 || grid[n - 1][n - 1] == 1 {\n   \
        \         return 0;\n        }\n\n        let mut dist = vec![vec![-1; n]; n];\n\
        \        let mut q = VecDeque::new();\n\n        for r in 0..n {\n         \
        \   for c in 0..n {\n                if grid[r][c] == 1 {\n                \
        \    dist[r][c] = 0;\n                    q.push_back((r, c));\n           \
        \     }\n            }\n        }\n\n        let dr = [0, 0, 1, -1];\n     \
        \   let dc = [1, -1, 0, 0];\n\n        while let Some((r, c)) = q.pop_front()\
        \ {\n            for i in 0..4 {\n                let nr = r as i32 + dr[i];\n\
        \                let nc = c as i32 + dc[i];\n                if nr >= 0 && nr\
        \ < n as i32 && nc >= 0 && nc < n as i32 {\n                    let (nr, nc)\
        \ = (nr as usize, nc as usize);\n                    if dist[nr][nc] == -1 {\n\
        \                        dist[nr][nc] = dist[r][c] + 1;\n                  \
        \      q.push_back((nr, nc));\n                    }\n                }\n  \
        \          }\n        }\n\n        let mut pq = BinaryHeap::new();\n       \
        \ pq.push((dist[0][0], 0, 0));\n        let mut visited = vec![vec![false; n];\
        \ n];\n        visited[0][0] = true;\n\n        while let Some((d, r, c)) =\
        \ pq.pop() {\n            if r == n - 1 && c == n - 1 {\n                return\
        \ d;\n            }\n\n            for i in 0..4 {\n                let nr =\
        \ r as i32 + dr[i];\n                let nc = c as i32 + dc[i];\n          \
        \      if nr >= 0 && nr < n as i32 && nc >= 0 && nc < n as i32 {\n         \
        \           let (nr, nc) = (nr as usize, nc as usize);\n                   \
        \ if !visited[nr][nc] {\n                        visited[nr][nc] = true;\n \
        \                       pq.push((d.min(dist[nr][nc]), nr, nc));\n          \
        \          }\n                }\n            }\n        }\n\n        0\n   \
        \ }\n}"
      racket: "(define/contract (maximum-safeness-factor grid)\n  (-> (listof (listof\
        \ exact-integer?)) exact-integer?)\n  (let* ([n (length grid)]\n         [grid-vec\
        \ (list->vector (map list->vector grid))]\n         [dist-vec (make-vector n)])\n\
        \    (for ([i (in-range n)]) (vector-set! dist-vec i (make-vector n -1)))\n\
        \    (let ([q '()])\n      (for* ([r (in-range n)] [c (in-range n)])\n     \
        \   (when (= (vector-ref (vector-ref grid-vec r) c) 1)\n          (vector-set!\
        \ (vector-ref dist-vec r) c 0)\n          (set! q (cons (cons r c) q))))\n \
        \     (let dist-bfs ([current-layer q] [d 1])\n        (unless (null? current-layer)\n\
        \          (let ([next-layer '()])\n            (for ([curr current-layer])\n\
        \              (let ([r (car curr)] [c (cdr curr)])\n                (for ([dr\
        \ '(0 0 1 -1)] [dc '(1 -1 0 0)])\n                  (let ([nr (+ r dr)] [nc\
        \ (+ c dc)])\n                    (when (and (>= nr 0) (< nr n) (>= nc 0) (<\
        \ nc n)\n                               (= (vector-ref (vector-ref dist-vec\
        \ nr) nc) -1))\n                      (vector-set! (vector-ref dist-vec nr)\
        \ nc d)\n                      (set! next-layer (cons (cons nr nc) next-layer)))))))\n\
        \            (dist-bfs next-layer (+ d 1)))))\n      (define (can-reach? v)\n\
        \        (if (or (< (vector-ref (vector-ref dist-vec 0) 0) v)\n            \
        \    (< (vector-ref (vector-ref dist-vec (- n 1)) (- n 1)) v))\n           \
        \ #f\n            (let ([visited (make-vector n)])\n              (for ([i (in-range\
        \ n)]) (vector-set! visited i (make-vector n #f)))\n              (vector-set!\
        \ (vector-ref visited 0) 0 #t)\n              (let loop ([q (list (cons 0 0))])\n\
        \                (if (null? q) #f\n                    (let ([next-q '()] [reached\
        \ #f])\n                      (for ([curr q])\n                        (let\
        \ ([r (car curr)] [c (cdr curr)])\n                          (for ([dr '(0 0\
        \ 1 -1)] [dc '(1 -1 0 0)])\n                            (let ([nr (+ r dr)]\
        \ [nc (+ c dc)])\n                              (when (and (>= nr 0) (< nr n)\
        \ (>= nc 0) (< nc n)\n                                         (not (vector-ref\
        \ (vector-ref visited nr) nc))\n                                         (>=\
        \ (vector-ref (vector-ref dist-vec nr) nc) v))\n                           \
        \     (vector-set! (vector-ref visited nr) nc #t)\n                        \
        \        (if (and (= nr (- n 1)) (= nc (- n 1)))\n                         \
        \           (set! reached #t)\n                                    (set! next-q\
        \ (cons (cons nr nc) next-q))))))))\n                      (if reached #t (loop\
        \ next-q))))))))\n      (let binary-search ([low 0] [high (* 2 n)])\n      \
        \  (if (> low high)\n            high\n            (let* ([mid (quotient (+\
        \ low high) 2)]\n                   [can (can-reach? mid)])\n              (if\
        \ can\n                  (binary-search (+ mid 1) high)\n                  (binary-search\
        \ low (- mid 1)))))))))"
      erlang: "-spec maximum_safeness_factor(Grid :: [[integer()]]) -> integer().\n\
        maximum_safeness_factor(Grid) ->\n  N = length(Grid),\n  Thieves = find_thieves(Grid,\
        \ 0),\n  DistMap = bfs_distances(queue:from_list(Thieves), maps:from_list([{T,\
        \ 0} || T <- Thieves]), N),\n  DistTuple = list_to_tuple([list_to_tuple([maps:get({R,\
        \ C}, DistMap) || C <- lists:seq(0, N-1)]) || R <- lists:seq(0, N-1)]),\n  binary_search(0,\
        \ 2 * N, N, DistTuple).\n\nfind_thieves([], _) -> [];\nfind_thieves([Row | Rest],\
        \ R) ->\n  RowThieves = [{R, C} || {Val, C} <- lists:zip(Row, lists:seq(0, length(Row)\
        \ - 1)), Val == 1],\n  RowThieves ++ find_thieves(Rest, R + 1).\n\nbfs_distances(Q,\
        \ Map, N) ->\n  case queue:out(Q) of\n    {{value, {R, C}}, Q2} ->\n      D\
        \ = maps:get({R, C}, Map),\n      {NewQ, NewMap} = lists:foldl(fun({DR, DC},\
        \ {AccQ, AccM}) ->\n        NR = R + DR, NC = C + DC,\n        if NR >= 0, NR\
        \ < N, NC >= 0, NC < N ->\n          case maps:is_key({NR, NC}, AccM) of\n \
        \           false -> {queue:in({NR, NC}, AccQ), AccM#{{NR, NC} => D + 1}};\n\
        \            true -> {AccQ, AccM}\n          end;\n        true -> {AccQ, AccM}\n\
        \        end\n      end, {Q2, Map}, [{0,1},{0,-1},{1,0},{-1,0}]),\n      bfs_distances(NewQ,\
        \ NewMap, N);\n    {empty, _} -> Map\n  end.\n\nbinary_search(Low, High, N,\
        \ DistTuple) ->\n  if Low > High -> High;\n  true ->\n    Mid = (Low + High)\
        \ div 2,\n    case can_reach(Mid, N, DistTuple) of\n      true -> binary_search(Mid\
        \ + 1, High, N, DistTuple);\n      false -> binary_search(Low, Mid - 1, N, DistTuple)\n\
        \    end\n  end.\n\ncan_reach(V, N, DistTuple) ->\n  S = element(1, element(1,\
        \ DistTuple)),\n  E = element(N, element(N, DistTuple)),\n  if S < V; E < V\
        \ -> false;\n  true ->\n    bfs_check(queue:from_list([{0, 0}]), #{{0, 0} =>\
        \ true}, V, N, DistTuple)\n  end.\n\nbfs_check(Q, Visited, V, N, DistTuple)\
        \ ->\n  case queue:out(Q) of\n    {{value, {R, C}}, Q2} ->\n      if R == N\
        \ - 1, C == N - 1 -> true;\n      true ->\n        {NewQ, NewVisited} = lists:foldl(fun({DR,\
        \ DC}, {AccQ, AccV}) ->\n          NR = R + DR, NC = C + DC,\n          if NR\
        \ >= 0, NR < N, NC >= 0, NC < N ->\n            case maps:is_key({NR, NC}, AccV)\
        \ of\n              false ->\n                D = element(NC + 1, element(NR\
        \ + 1, DistTuple)),\n                if D >= V -> {queue:in({NR, NC}, AccQ),\
        \ AccV#{{NR, NC} => true}};\n                true -> {AccQ, AccV}\n        \
        \        end;\n              true -> {AccQ, AccV}\n            end;\n      \
        \    true -> {AccQ, AccV}\n          end\n        end, {Q2, Visited}, [{0,1},{0,-1},{1,0},{-1,0}]),\n\
        \        bfs_check(NewQ, NewVisited, V, N, DistTuple)\n      end;\n    {empty,\
        \ _} -> false\n  end."
      elixir: "defmodule Solution do\n  @spec maximum_safeness_factor(grid :: [[integer]])\
        \ :: integer\n  def maximum_safeness_factor(grid) do\n    n = length(grid)\n\
        \    thieves = for {row, r} <- Enum.with_index(grid), {val, c} <- Enum.with_index(row),\
        \ val == 1, do: {r, c}\n\n    dist_map = bfs_distances(:queue.from_list(thieves),\
        \ Map.new(thieves, fn t -> {t, 0} end), n)\n\n    dist_tuple = Enum.map(0..(n\
        \ - 1), fn r ->\n      Enum.map(0..(n - 1), fn c -> Map.get(dist_map, {r, c})\
        \ end) |> List.to_tuple()\n    end) |> List.to_tuple()\n\n    binary_search(0,\
        \ 2 * n, n, dist_tuple)\n  end\n\n  defp bfs_distances(q, dist_map, n) do\n\
        \    case :queue.out(q) do\n      {:empty, _} -> dist_map\n      {{:value, {r,\
        \ c}}, q2} ->\n        d = Map.get(dist_map, {r, c})\n        {new_q, new_map}\
        \ = Enum.reduce([{0, 1}, {0, -1}, {1, 0}, {-1, 0}], {q2, dist_map}, fn {dr,\
        \ dc}, {acc_q, acc_m} ->\n          nr = r + dr\n          nc = c + dc\n   \
        \       if nr >= 0 and nr < n and nc >= 0 and nc < n and not Map.has_key?(acc_m,\
        \ {nr, nc}) do\n            {:queue.in({nr, nc}, acc_q), Map.put(acc_m, {nr,\
        \ nc}, d + 1)}\n          else\n            {acc_q, acc_m}\n          end\n\
        \        end)\n        bfs_distances(new_q, new_map, n)\n    end\n  end\n\n\
        \  defp binary_search(low, high, n, dist_tuple) do\n    if low > high do\n \
        \     high\n    else\n      mid = div(low + high, 2)\n      if can_reach(mid,\
        \ n, dist_tuple) do\n        binary_search(mid + 1, high, n, dist_tuple)\n \
        \     else\n        binary_search(low, mid - 1, n, dist_tuple)\n      end\n\
        \    end\n  end\n\n  defp can_reach(v, n, dist_tuple) do\n    s_d = elem(elem(dist_tuple,\
        \ 0), 0)\n    e_d = elem(elem(dist_tuple, n - 1), n - 1)\n    if s_d < v or\
        \ e_d < v do\n      false\n    else\n      bfs_check(:queue.from_list([{0, 0}]),\
        \ %{{0, 0} => true}, v, n, dist_tuple)\n    end\n  end\n\n  defp bfs_check(q,\
        \ visited, v, n, dist_tuple) do\n    case :queue.out(q) do\n      {:empty, _}\
        \ -> false\n      {{:value, {r, c}}, q2} ->\n        if r == n - 1 and c ==\
        \ n - 1 do\n          true\n        else\n          {new_q, new_visited} = Enum.reduce([{0,\
        \ 1}, {0, -1}, {1, 0}, {-1, 0}], {q2, visited}, fn {dr, dc}, {acc_q, acc_v}\
        \ ->\n            nr = r + dr\n            nc = c + dc\n            if nr >=\
        \ 0 and nr < n and nc >= 0 and nc < n and not Map.has_key?(acc_v, {nr, nc})\
        \ and elem(elem(dist_tuple, nr), nc) >= v do\n              {:queue.in({nr,\
        \ nc}, acc_q), Map.put(acc_v, {nr, nc}, true)}\n            else\n         \
        \     {acc_q, acc_v}\n            end\n          end)\n          bfs_check(new_q,\
        \ new_visited, v, n, dist_tuple)\n        end\n    end\n  end\nend"
    approach: The problem asks to find a path from (0, 0) to (n-1, n-1) that maximizes
      the 'safeness factor', which is the minimum Manhattan distance to any thief along
      the path. This can be broken down into two main steps. First, we compute the distance
      from every cell in the grid to its nearest thief using a multi-source Breadth-First
      Search (BFS). All cells containing a thief are initialized with a distance of
      0 and added to a queue. The BFS then expands outwards to fill a distance matrix,
      where each cell's value represents its minimum Manhattan distance to any thief.
      Since moving between adjacent cells corresponds to a Manhattan step of 1, the
      BFS levels naturally represent these distances.
    time_complexity: O(n^2 \log n) where n is the grid side length. The multi-source
      BFS takes O(n^2) as each cell and edge are processed once. The subsequent pathfinding
      step using a Dijkstra-like max-priority queue takes O(n^2 \log n^2), which simplifies
      to O(n^2 \log n), as we perform priority queue operations for each cell. Alternatively,
      using binary search with BFS would result in O(n^2 \log(2n)), which is also effectively
      O(n^2 \log n).
    space_complexity: O(n^2) as we need to store the distance matrix of size n x n,
      a visited matrix or array to track processed cells, and auxiliary data structures
      like a queue for the initial BFS and a priority queue for the Dijkstra-like search.
    elapsed_time: 533.9695978164673
    model: gemini-3-flash-preview
    generated_at: '2026-07-01 02:54:02 '
---

## Problem #2812: Find the Safest Path in a Grid

**Difficulty:** Medium

**Topics:** Array, Binary Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix

## Problem Description

<p>You are given a <strong>0-indexed</strong> 2D matrix <code>grid</code> of size <code>n x n</code>, where <code>(r, c)</code> represents:</p>

<ul>
	<li>A cell containing a thief if <code>grid[r][c] = 1</code></li>
	<li>An empty cell if <code>grid[r][c] = 0</code></li>
</ul>

<p>You are initially positioned at cell <code>(0, 0)</code>. In one move, you can move to any adjacent cell in the grid, including cells containing thieves.</p>

<p>The <strong>safeness factor</strong> of a path on the grid is defined as the <strong>minimum</strong> manhattan distance from any cell in the path to any thief in the grid.</p>

<p>Return <em>the <strong>maximum safeness factor</strong> of all paths leading to cell </em><code>(n - 1, n - 1)</code><em>.</em></p>

<p>An <strong>adjacent</strong> cell of cell <code>(r, c)</code>, is one of the cells <code>(r, c + 1)</code>, <code>(r, c - 1)</code>, <code>(r + 1, c)</code> and <code>(r - 1, c)</code> if it exists.</p>

<p>The <strong>Manhattan distance</strong> between two cells <code>(a, b)</code> and <code>(x, y)</code> is equal to <code>|a - x| + |b - y|</code>, where <code>|val|</code> denotes the absolute value of val.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/07/02/example1.png" style="width: 362px; height: 242px;" />
<pre>
<strong>Input:</strong> grid = [[1,0,0],[0,0,0],[0,0,1]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/07/02/example2.png" style="width: 362px; height: 242px;" />
<pre>
<strong>Input:</strong> grid = [[0,0,1],[0,0,0],[0,0,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/07/02/example3.png" style="width: 362px; height: 242px;" />
<pre>
<strong>Input:</strong> grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
- The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= grid.length == n &lt;= 400</code></li>
	<li><code>grid[i].length == n</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
	<li>There is at least one thief in the <code>grid</code>.</li>
</ul>


## Hints

1. Consider using both BFS and binary search together.

2. Launch a BFS starting from all the cells containing thieves to calculate d[x][y] which is the smallest Manhattan distance from (x, y) to the nearest grid that contains thieves.

3. To check if the bottom-right cell of the grid can be reached through a path of safeness factor v, eliminate all cells (x, y) such that grid[x][y]  < v. if (0, 0) and (n - 1, n - 1) are still connected, there exists a path between (0, 0) and (n - 1, n - 1) of safeness factor v.

4. Binary search over the final safeness factor v.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks to find a path from (0, 0) to (n-1, n-1) that maximizes the 'safeness factor', which is the minimum Manhattan distance to any thief along the path. This can be broken down into two main steps. First, we compute the distance from every cell in the grid to its nearest thief using a multi-source Breadth-First Search (BFS). All cells containing a thief are initialized with a distance of 0 and added to a queue. The BFS then expands outwards to fill a distance matrix, where each cell's value represents its minimum Manhattan distance to any thief. Since moving between adjacent cells corresponds to a Manhattan step of 1, the BFS levels naturally represent these distances.

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
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return 0;

        vector<vector<int>> dist(n, vector<int>(n, -1));
        queue<pair<int, int>> q;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    dist[i][j] = 0;
                    q.push({i, j});
                }
            }
        }

        int dr[] = {0, 0, 1, -1};
        int dc[] = {1, -1, 0, 0};

        while (!q.empty()) {
            pair<int, int> curr = q.front();
            q.pop();
            for (int i = 0; i < 4; ++i) {
                int ni = curr.first + dr[i], nj = curr.second + dc[i];
                if (ni >= 0 && ni < n && nj >= 0 && nj < n && dist[ni][nj] == -1) {
                    dist[ni][nj] = dist[curr.first][curr.second] + 1;
                    q.push({ni, nj});
                }
            }
        }

        priority_queue<pair<int, pair<int, int>>> pq;
        pq.push({dist[0][0], {0, 0}});
        vector<vector<int>> max_safe(n, vector<int>(n, -1));
        max_safe[0][0] = dist[0][0];

        while (!pq.empty()) {
            int d = pq.top().first;
            int r = pq.top().second.first;
            int c = pq.top().second.second;
            pq.pop();

            if (r == n - 1 && c == n - 1) return d;

            for (int i = 0; i < 4; ++i) {
                int ni = r + dr[i], nj = c + dc[i];
                if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                    int new_s = min(d, dist[ni][nj]);
                    if (new_s > max_safe[ni][nj]) {
                        max_safe[ni][nj] = new_s;
                        pq.push({new_s, {ni, nj}});
                    }
                }
            }
        }

        return 0;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maximumSafenessFactor(List<List<Integer>> grid) {
        int n = grid.size();
        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++) Arrays.fill(dist[i], -1);
        Deque<int[]> q = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid.get(i).get(j) == 1) {
                    dist[i][j] = 0;
                    q.add(new int[]{i, j});
                }
            }
        }

        int[] dr = {0, 0, 1, -1};
        int[] dc = {1, -1, 0, 0};

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            for (int i = 0; i < 4; i++) {
                int ni = curr[0] + dr[i], nj = curr[1] + dc[i];
                if (ni >= 0 && ni < n && nj >= 0 && nj < n && dist[ni][nj] == -1) {
                    dist[ni][nj] = dist[curr[0]][curr[1]] + 1;
                    q.add(new int[]{ni, nj});
                }
            }
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[0] - a[0]);
        pq.add(new int[]{dist[0][0], 0, 0});
        int[][] maxSafe = new int[n][n];
        for (int i = 0; i < n; i++) Arrays.fill(maxSafe[i], -1);
        maxSafe[0][0] = dist[0][0];

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int d = curr[0], r = curr[1], c = curr[2];

            if (r == n - 1 && c == n - 1) return d;

            for (int i = 0; i < 4; i++) {
                int ni = r + dr[i], nj = c + dc[i];
                if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                    int s = Math.min(d, dist[ni][nj]);
                    if (s > maxSafe[ni][nj]) {
                        maxSafe[ni][nj] = s;
                        pq.add(new int[]{s, ni, nj});
                    }
                }
            }
        }

        return 0;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import heapq
from collections import deque

class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        pq = [(-dist[0][0], 0, 0)]
        max_safe = [[-1] * n for _ in range(n)]
        max_safe[0][0] = dist[0][0]

        while pq:
            d, r, c = heapq.heappop(pq)
            d = -d
            if r == n - 1 and c == n - 1:
                return d
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    new_s = min(d, dist[nr][nc])
                    if new_s > max_safe[nr][nc]:
                        max_safe[nr][nc] = new_s
                        heapq.heappush(pq, (-new_s, nr, nc))
        return 0
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import heapq
from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        pq = [(-dist[0][0], 0, 0)]
        max_safe = [[-1] * n for _ in range(n)]
        max_safe[0][0] = dist[0][0]

        while pq:
            d, r, c = heapq.heappop(pq)
            d = -d
            if r == n - 1 and c == n - 1:
                return d
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    new_s = min(d, dist[nr][nc])
                    if new_s > max_safe[nr][nc]:
                        max_safe[nr][nc] = new_s
                        heapq.heappush(pq, (-new_s, nr, nc))
        return 0
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#define MIN(a, b) ((a) < (b) ? (a) : (b))

int dr[] = {0, 0, 1, -1};
int dc[] = {1, -1, 0, 0};

bool canReach(int v, int n, int** dist, char** visited, int* qr, int* qc) {
    if (dist[0][0] < v || dist[n - 1][n - 1] < v) return false;
    for (int i = 0; i < n; i++) memset(visited[i], 0, n);
    int head = 0, tail = 0;
    qr[tail] = 0; qc[tail] = 0; tail++;
    visited[0][0] = 1;
    while (head < tail) {
        int r = qr[head], c = qc[head]; head++;
        if (r == n - 1 && c == n - 1) return true;
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i], nc = c + dc[i];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc] && dist[nr][nc] >= v) {
                visited[nr][nc] = 1;
                qr[tail] = nr; qc[tail] = nc; tail++;
            }
        }
    }
    return false;
}

int maximumSafenessFactor(int** grid, int gridSize, int* gridColSize) {
    int n = gridSize;
    int** dist = (int**)malloc(n * sizeof(int*));
    char** visited = (char**)malloc(n * sizeof(char*));
    for (int i = 0; i < n; i++) {
        dist[i] = (int*)malloc(n * sizeof(int));
        visited[i] = (char*)malloc(n);
        for (int j = 0; j < n; j++) dist[i][j] = -1;
    }

    int* qr = (int*)malloc(n * n * sizeof(int));
    int* qc = (int*)malloc(n * n * sizeof(int));
    int head = 0, tail = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) {
                dist[i][j] = 0;
                qr[tail] = i; qc[tail] = j; tail++;
            }
        }
    }

    while (head < tail) {
        int r = qr[head], c = qc[head]; head++;
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i], nc = c + dc[i];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1;
                qr[tail] = nr; qc[tail] = nc; tail++;
            }
        }
    }

    int low = 0, high = 2 * n, ans = 0;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (canReach(mid, n, dist, visited, qr, qc)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    for (int i = 0; i < n; i++) {
        free(dist[i]);
        free(visited[i]);
    }
    free(dist); free(visited); free(qr); free(qc);
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaximumSafenessFactor(IList<IList<int>> grid) {
        int n = grid.Count;
        int[] dist = new int[n * n];
        for (int i = 0; i < n * n; i++) dist[i] = -1;

        Queue<int> q = new Queue<int>();
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1) {
                    dist[r * n + c] = 0;
                    q.Enqueue(r * n + c);
                }
            }
        }

        int[] dr = { 0, 0, 1, -1 };
        int[] dc = { 1, -1, 0, 0 };

        while (q.Count > 0) {
            int idx = q.Dequeue();
            int r = idx / n;
            int c = idx % n;
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i], nc = c + dc[i];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                    int nidx = nr * n + nc;
                    if (dist[nidx] == -1) {
                        dist[nidx] = dist[idx] + 1;
                        q.Enqueue(nidx);
                    }
                }
            }
        }

        int left = 0, right = Math.Min(dist[0], dist[n * n - 1]);
        int ans = 0;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (CanReach(dist, mid, n)) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return ans;
    }

    private bool CanReach(int[] dist, int minSafe, int n) {
        if (dist[0] < minSafe || dist[n * n - 1] < minSafe) return false;
        Queue<int> q = new Queue<int>();
        bool[] visited = new bool[n * n];
        q.Enqueue(0);
        visited[0] = true;

        int[] dr = { 0, 0, 1, -1 };
        int[] dc = { 1, -1, 0, 0 };

        while (q.Count > 0) {
            int idx = q.Dequeue();
            if (idx == n * n - 1) return true;
            int r = idx / n;
            int c = idx % n;
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i], nc = c + dc[i];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                    int nidx = nr * n + nc;
                    if (!visited[nidx] && dist[nidx] >= minSafe) {
                        visited[nidx] = true;
                        q.Enqueue(nidx);
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
 * @return {number}
 */
var maximumSafenessFactor = function(grid) {
    const n = grid.length;
    const dist = new Int32Array(n * n).fill(-1);
    const q = [];

    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            if (grid[r][c] === 1) {
                dist[r * n + c] = 0;
                q.push(r * n + c);
            }
        }
    }

    let head = 0;
    const dr = [0, 0, 1, -1], dc = [1, -1, 0, 0];
    while (head < q.length) {
        const idx = q[head++];
        const r = Math.floor(idx / n), c = idx % n;
        for (let i = 0; i < 4; i++) {
            const nr = r + dr[i], nc = c + dc[i];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                const nidx = nr * n + nc;
                if (dist[nidx] === -1) {
                    dist[nidx] = dist[idx] + 1;
                    q.push(nidx);
                }
            }
        }
    }

    const canReach = (minSafe) => {
        if (dist[0] < minSafe || dist[n * n - 1] < minSafe) return false;
        const q2 = [0];
        const visited = new Uint8Array(n * n);
        visited[0] = 1;
        let head2 = 0;
        while (head2 < q2.length) {
            const idx = q2[head2++];
            if (idx === n * n - 1) return true;
            const r = Math.floor(idx / n), c = idx % n;
            for (let i = 0; i < 4; i++) {
                const nr = r + dr[i], nc = c + dc[i];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                    const nidx = nr * n + nc;
                    if (!visited[nidx] && dist[nidx] >= minSafe) {
                        visited[nidx] = 1;
                        q2.push(nidx);
                    }
                }
            }
        }
        return false;
    };

    let left = 0, right = Math.min(dist[0], dist[n * n - 1]), ans = 0;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (canReach(mid)) {
            ans = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
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
function maximumSafenessFactor(grid: number[][]): number {
    const n = grid.length;
    const dist = new Int32Array(n * n).fill(-1);
    const q: number[] = [];

    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            if (grid[r][c] === 1) {
                dist[r * n + c] = 0;
                q.push(r * n + c);
            }
        }
    }

    let head = 0;
    const dr = [0, 0, 1, -1], dc = [1, -1, 0, 0];
    while (head < q.length) {
        const idx = q[head++];
        const r = Math.floor(idx / n), c = idx % n;
        for (let i = 0; i < 4; i++) {
            const nr = r + dr[i], nc = c + dc[i];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                const nidx = nr * n + nc;
                if (dist[nidx] === -1) {
                    dist[nidx] = dist[idx] + 1;
                    q.push(nidx);
                }
            }
        }
    }

    const canReach = (minSafe: number): boolean => {
        if (dist[0] < minSafe || dist[n * n - 1] < minSafe) return false;
        const q2: number[] = [0];
        const visited = new Uint8Array(n * n);
        visited[0] = 1;
        let head2 = 0;
        while (head2 < q2.length) {
            const idx = q2[head2++];
            if (idx === n * n - 1) return true;
            const r = Math.floor(idx / n), c = idx % n;
            for (let i = 0; i < 4; i++) {
                const nr = r + dr[i], nc = c + dc[i];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                    const nidx = nr * n + nc;
                    if (!visited[nidx] && dist[nidx] >= minSafe) {
                        visited[nidx] = 1;
                        q2.push(nidx);
                    }
                }
            }
        }
        return false;
    };

    let left = 0, right = Math.min(dist[0], dist[n * n - 1]), ans = 0;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (canReach(mid)) {
            ans = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
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
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maximumSafenessFactor($grid) {
        $n = count($grid);
        $dist = new \SplFixedArray($n * $n);
        for ($i = 0; $i < $n * $n; $i++) $dist[$i] = -1;

        $q = new \SplQueue();
        for ($r = 0; $r < $n; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($grid[$r][$c] == 1) {
                    $dist[$r * $n + $c] = 0;
                    $q->enqueue($r * $n + $c);
                }
            }
        }

        $dr = [0, 0, 1, -1];
        $dc = [1, -1, 0, 0];

        while (!$q->isEmpty()) {
            $idx = $q->dequeue();
            $r = (int)($idx / $n);
            $c = $idx % $n;
            for ($i = 0; $i < 4; $i++) {
                $nr = $r + $dr[$i];
                $nc = $c + $dc[$i];
                if ($nr >= 0 && $nr < $n && $nc >= 0 && $nc < $n) {
                    $nidx = $nr * $n + $nc;
                    if ($dist[$nidx] === -1) {
                        $dist[$nidx] = $dist[$idx] + 1;
                        $q->enqueue($nidx);
                    }
                }
            }
        }

        $canReach = function($minSafe) use ($dist, $n, $dr, $dc) {
            if ($dist[0] < $minSafe || $dist[$n * $n - 1] < $minSafe) return false;
            $q2 = new \SplQueue();
            $q2->enqueue(0);
            $visited = new \SplFixedArray($n * $n);
            $visited[0] = true;
            while (!$q2->isEmpty()) {
                $idx = $q2->dequeue();
                if ($idx === $n * $n - 1) return true;
                $r = (int)($idx / $n);
                $c = $idx % $n;
                for ($i = 0; $i < 4; $i++) {
                    $nr = $r + $dr[$i];
                    $nc = $c + $dc[$i];
                    if ($nr >= 0 && $nr < $n && $nc >= 0 && $nc < $n) {
                        $nidx = $nr * $n + $nc;
                        if (!$visited[$nidx] && $dist[$nidx] >= $minSafe) {
                            $visited[$nidx] = true;
                            $q2->enqueue($nidx);
                        }
                    }
                }
            }
            return false;
        };

        $left = 0;
        $right = min($dist[0], $dist[$n * $n - 1]);
        $ans = 0;
        while ($left <= $right) {
            $mid = (int)(($left + $right) / 2);
            if ($canReach($mid)) {
                $ans = $mid;
                $left = $mid + 1;
            } else {
                $right = $mid - 1;
            }
        }
        return $ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maximumSafenessFactor(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var dist = [Int](repeating: -1, count: n * n)
        var q = [Int]()

        for r in 0..<n {
            for c in 0..<n {
                if grid[r][c] == 1 {
                    dist[r * n + c] = 0
                    q.append(r * n + c)
                }
            }
        }

        let dr = [0, 0, 1, -1]
        let dc = [1, -1, 0, 0]
        var head = 0
        while head < q.count {
            let idx = q[head]
            head += 1
            let r = idx / n
            let c = idx % n
            for i in 0..<4 {
                let nr = r + dr[i]
                let nc = c + dc[i]
                if nr >= 0 && nr < n && nc >= 0 && nc < n {
                    let nidx = nr * n + nc
                    if dist[nidx] == -1 {
                        dist[nidx] = dist[idx] + 1
                        q.append(nidx)
                    }
                }
            }
        }

        func canReach(minSafe: Int) -> Bool {
            if dist[0] < minSafe || dist[n * n - 1] < minSafe { return false }
            var visited = [Bool](repeating: false, count: n * n)
            var q2 = [0]
            visited[0] = true
            var head2 = 0
            while head2 < q2.count {
                let idx = q2[head2]
                head2 += 1
                if idx == n * n - 1 { return true }
                let r = idx / n
                let c = idx % n
                for i in 0..<4 {
                    let nr = r + dr[i]
                    let nc = c + dc[i]
                    if nr >= 0 && nr < n && nc >= 0 && nc < n {
                        let nidx = nr * n + nc
                        if !visited[nidx] && dist[nidx] >= minSafe {
                            visited[nidx] = true
                            q2.append(nidx)
                        }
                    }
                }
            }
            return false
        }

        var left = 0
        var right = min(dist[0], dist[n * n - 1])
        var ans = 0
        while left <= right {
            let mid = (left + right) / 2
            if canReach(minSafe: mid) {
                ans = mid
                left = mid + 1
            } else {
                right = mid - 1
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
import java.util.ArrayDeque

class Solution {
    fun maximumSafenessFactor(grid: List<List<Int>>): Int {
        val n = grid.size
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return 0

        val dist = Array(n) { IntArray(n) { -1 } }
        val q = ArrayDeque<Int>()

        for (r in 0 until n) {
            for (c in 0 until n) {
                if (grid[r][c] == 1) {
                    dist[r][c] = 0
                    q.add(r * n + c)
                }
            }
        }

        val dr = intArrayOf(0, 0, 1, -1)
        val dc = intArrayOf(1, -1, 0, 0)

        while (q.isNotEmpty()) {
            val curr = q.poll()
            val r = curr / n
            val c = curr % n
            for (i in 0 until 4) {
                val nr = r + dr[i]
                val nc = c + dc[i]
                if (nr in 0 until n && nc in 0 until n && dist[nr][nc] == -1) {
                    dist[nr][nc] = dist[r][c] + 1
                    q.add(nr * n + nc)
                }
            }
        }

        fun isPossible(v: Int): Boolean {
            if (dist[0][0] < v || dist[n - 1][n - 1] < v) return false
            val queue = ArrayDeque<Int>()
            queue.add(0)
            val visited = BooleanArray(n * n)
            visited[0] = true
            while (queue.isNotEmpty()) {
                val curr = queue.poll()
                val r = curr / n
                val c = curr % n
                if (r == n - 1 && c == n - 1) return true
                for (i in 0 until 4) {
                    val nr = r + dr[i]
                    val nc = c + dc[i]
                    val nIdx = nr * n + nc
                    if (nr in 0 until n && nc in 0 until n && !visited[nIdx] && dist[nr][nc] >= v) {
                        visited[nIdx] = true
                        queue.add(nIdx)
                    }
                }
            }
            return false
        }

        var low = 0
        var high = 2 * n
        var ans = 0
        while (low <= high) {
            val mid = (low + high) / 2
            if (isPossible(mid)) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
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
import 'dart:math';

class Solution {
  int maximumSafenessFactor(List<List<int>> grid) {
    int n = grid.length;
    if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return 0;

    List<List<int>> dist = List.generate(n, (_) => List.filled(n, -1));
    Queue<int> q = Queue<int>();

    for (int r = 0; r < n; r++) {
      for (int c = 0; c < n; c++) {
        if (grid[r][c] == 1) {
          dist[r][c] = 0;
          q.add(r * n + c);
        }
      }
    }

    List<int> dr = [0, 0, 1, -1];
    List<int> dc = [1, -1, 0, 0];

    while (q.isNotEmpty) {
      int curr = q.removeFirst();
      int r = curr ~/ n;
      int c = curr % n;
      for (int i = 0; i < 4; i++) {
        int nr = r + dr[i];
        int nc = c + dc[i];
        if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] == -1) {
          dist[nr][nc] = dist[r][c] + 1;
          q.add(nr * n + nc);
        }
      }
    }

    bool isPossible(int v) {
      if (dist[0][0] < v || dist[n - 1][n - 1] < v) return false;
      Queue<int> queue = Queue<int>();
      queue.add(0);
      List<bool> visited = List.filled(n * n, false);
      visited[0] = true;
      while (queue.isNotEmpty) {
        int curr = queue.removeFirst();
        int r = curr ~/ n;
        int c = curr % n;
        if (r == n - 1 && c == n - 1) return true;
        for (int i = 0; i < 4; i++) {
          int nr = r + dr[i];
          int nc = c + dc[i];
          int idx = nr * n + nc;
          if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[idx] && dist[nr][nc] >= v) {
            visited[idx] = true;
            queue.add(idx);
          }
        }
      }
      return false;
    }

    int low = 0;
    int high = 2 * n;
    int ans = 0;
    while (low <= high) {
      int mid = (low + high) ~/ 2;
      if (isPossible(mid)) {
        ans = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
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
func maximumSafenessFactor(grid [][]int) int {
	n := len(grid)
	if grid[0][0] == 1 || grid[n-1][n-1] == 1 {
		return 0
	}

	dist := make([][]int, n)
	for i := range dist {
		dist[i] = make([]int, n)
		for j := range dist[i] {
			dist[i][j] = -1
		}
	}

	queue := make([]int, 0, n*n)
	for r := 0; r < n; r++ {
		for c := 0; c < n; c++ {
			if grid[r][c] == 1 {
				dist[r][c] = 0
				queue = append(queue, r*n+c)
			}
		}
	}

	dr := []int{0, 0, 1, -1}
	dc := []int{1, -1, 0, 0}

	head := 0
	for head < len(queue) {
		curr := queue[head]
		head++
		r, c := curr/n, curr%n
		for i := 0; i < 4; i++ {
			nr, nc := r+dr[i], c+dc[i]
			if nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] == -1 {
				dist[nr][nc] = dist[r][c] + 1
				queue = append(queue, nr*n+nc)
			}
		}
	}

	isPossible := func(v int) bool {
		if dist[0][0] < v || dist[n-1][n-1] < v {
			return false
		}
		q := make([]int, 0, n*n)
		q = append(q, 0)
		visited := make([]bool, n*n)
		visited[0] = true
		h := 0
		for h < len(q) {
			curr := q[h]
		h++
			r, c := curr/n, curr%n
			if r == n-1 && c == n-1 {
				return true
			}
			for i := 0; i < 4; i++ {
				nr, nc := r+dr[i], c+dc[i]
				idx := nr*n + nc
				if nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[idx] && dist[nr][nc] >= v {
					visited[idx] = true
					q = append(q, idx)
				}
			}
		}
		return false
	}

	low, high := 0, 2*n
	ans := 0
	for low <= high {
		mid := (low + high) / 2
		if isPossible(mid) {
			ans = mid
			low = mid + 1
		} else {
			high = mid - 1
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
# @param {Integer[][]} grid
# @return {Integer}
def maximum_safeness_factor(grid)
  n = grid.length
  return 0 if grid[0][0] == 1 || grid[n - 1][n - 1] == 1

  dist = Array.new(n) { Array.new(n, -1) }
  queue = []
  n.times do |r|
    n.times do |c|
      if grid[r][c] == 1
        dist[r][c] = 0
        queue << (r * n + c)
      end
    end
  end

  dr = [0, 0, 1, -1]
  dc = [1, -1, 0, 0]

  head = 0
  while head < queue.length
    curr = queue[head]
    head += 1
    r, c = curr / n, curr % n
    4.times do |i|
      nr, nc = r + dr[i], c + dc[i]
      if nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] == -1
        dist[nr][nc] = dist[r][c] + 1
        queue << (nr * n + nc)
      end
    end
  end

  is_possible = lambda do |v|
    return false if dist[0][0] < v || dist[n - 1][n - 1] < v
    q = [0]
    visited = Array.new(n * n, false)
    visited[0] = true
    h = 0
    while h < q.length
      curr = q[h]
      h += 1
      r, c = curr / n, curr % n
      return true if r == n - 1 && c == n - 1
      4.times do |i|
        nr, nc = r + dr[i], c + dc[i]
        idx = nr * n + nc
        if nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[idx] && dist[nr][nc] >= v
          visited[idx] = true
          q << idx
        end
      end
    end
    false
  end

  low, high = 0, 2 * n
  ans = 0
  while low <= high
    mid = (low + high) / 2
    if is_possible.call(mid)
      ans = mid
      low = mid + 1
    else
      high = mid - 1
    end
  end
  ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def maximumSafenessFactor(grid: List[List[Int]]): Int = {
        val n = grid.size
        val g = grid.map(_.toArray).toArray
        if (g(0)(0) == 1 || g(n - 1)(n - 1) == 1) return 0

        val dist = Array.fill(n, n)(-1)
        val q = mutable.Queue[Int]()

        for (r <- 0 until n; c <- 0 until n) {
            if (g(r)(c) == 1) {
                dist(r)(c) = 0
                q.enqueue(r * n + c)
            }
        }

        val dr = Array(0, 0, 1, -1)
        val dc = Array(1, -1, 0, 0)

        while (q.nonEmpty) {
            val curr = q.dequeue()
            val r = curr / n
            val c = curr % n
            for (i <- 0 until 4) {
                val nr = r + dr(i)
                val nc = c + dc(i)
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist(nr)(nc) == -1) {
                    dist(nr)(nc) = dist(r)(c) + 1
                    q.enqueue(nr * n + nc)
                }
            }
        }

        def isPossible(v: Int): Boolean = {
            if (dist(0)(0) < v || dist(n - 1)(n - 1) < v) return false
            val queue = mutable.Queue[Int]()
            queue.enqueue(0)
            val visited = Array.fill(n * n)(false)
            visited(0) = true
            while (queue.nonEmpty) {
                val curr = queue.dequeue()
                val r = curr / n
                val c = curr % n
                if (r == n - 1 && c == n - 1) return true
                for (i <- 0 until 4) {
                    val nr = r + dr(i)
                    val nc = c + dc(i)
                    val idx = nr * n + nc
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited(idx) && dist(nr)(nc) >= v) {
                        visited(idx) = true
                        queue.enqueue(idx)
                    }
                }
            }
            false
        }

        var low = 0
        var high = 2 * n
        var ans = 0
        while (low <= high) {
            val mid = (low + high) / 2
            if (isPossible(mid)) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::{BinaryHeap, VecDeque};

impl Solution {
    pub fn maximum_safeness_factor(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        if grid[0][0] == 1 || grid[n - 1][n - 1] == 1 {
            return 0;
        }

        let mut dist = vec![vec![-1; n]; n];
        let mut q = VecDeque::new();

        for r in 0..n {
            for c in 0..n {
                if grid[r][c] == 1 {
                    dist[r][c] = 0;
                    q.push_back((r, c));
                }
            }
        }

        let dr = [0, 0, 1, -1];
        let dc = [1, -1, 0, 0];

        while let Some((r, c)) = q.pop_front() {
            for i in 0..4 {
                let nr = r as i32 + dr[i];
                let nc = c as i32 + dc[i];
                if nr >= 0 && nr < n as i32 && nc >= 0 && nc < n as i32 {
                    let (nr, nc) = (nr as usize, nc as usize);
                    if dist[nr][nc] == -1 {
                        dist[nr][nc] = dist[r][c] + 1;
                        q.push_back((nr, nc));
                    }
                }
            }
        }

        let mut pq = BinaryHeap::new();
        pq.push((dist[0][0], 0, 0));
        let mut visited = vec![vec![false; n]; n];
        visited[0][0] = true;

        while let Some((d, r, c)) = pq.pop() {
            if r == n - 1 && c == n - 1 {
                return d;
            }

            for i in 0..4 {
                let nr = r as i32 + dr[i];
                let nc = c as i32 + dc[i];
                if nr >= 0 && nr < n as i32 && nc >= 0 && nc < n as i32 {
                    let (nr, nc) = (nr as usize, nc as usize);
                    if !visited[nr][nc] {
                        visited[nr][nc] = true;
                        pq.push((d.min(dist[nr][nc]), nr, nc));
                    }
                }
            }
        }

        0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (maximum-safeness-factor grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([n (length grid)]
         [grid-vec (list->vector (map list->vector grid))]
         [dist-vec (make-vector n)])
    (for ([i (in-range n)]) (vector-set! dist-vec i (make-vector n -1)))
    (let ([q '()])
      (for* ([r (in-range n)] [c (in-range n)])
        (when (= (vector-ref (vector-ref grid-vec r) c) 1)
          (vector-set! (vector-ref dist-vec r) c 0)
          (set! q (cons (cons r c) q))))
      (let dist-bfs ([current-layer q] [d 1])
        (unless (null? current-layer)
          (let ([next-layer '()])
            (for ([curr current-layer])
              (let ([r (car curr)] [c (cdr curr)])
                (for ([dr '(0 0 1 -1)] [dc '(1 -1 0 0)])
                  (let ([nr (+ r dr)] [nc (+ c dc)])
                    (when (and (>= nr 0) (< nr n) (>= nc 0) (< nc n)
                               (= (vector-ref (vector-ref dist-vec nr) nc) -1))
                      (vector-set! (vector-ref dist-vec nr) nc d)
                      (set! next-layer (cons (cons nr nc) next-layer)))))))
            (dist-bfs next-layer (+ d 1)))))
      (define (can-reach? v)
        (if (or (< (vector-ref (vector-ref dist-vec 0) 0) v)
                (< (vector-ref (vector-ref dist-vec (- n 1)) (- n 1)) v))
            #f
            (let ([visited (make-vector n)])
              (for ([i (in-range n)]) (vector-set! visited i (make-vector n #f)))
              (vector-set! (vector-ref visited 0) 0 #t)
              (let loop ([q (list (cons 0 0))])
                (if (null? q) #f
                    (let ([next-q '()] [reached #f])
                      (for ([curr q])
                        (let ([r (car curr)] [c (cdr curr)])
                          (for ([dr '(0 0 1 -1)] [dc '(1 -1 0 0)])
                            (let ([nr (+ r dr)] [nc (+ c dc)])
                              (when (and (>= nr 0) (< nr n) (>= nc 0) (< nc n)
                                         (not (vector-ref (vector-ref visited nr) nc))
                                         (>= (vector-ref (vector-ref dist-vec nr) nc) v))
                                (vector-set! (vector-ref visited nr) nc #t)
                                (if (and (= nr (- n 1)) (= nc (- n 1)))
                                    (set! reached #t)
                                    (set! next-q (cons (cons nr nc) next-q))))))))
                      (if reached #t (loop next-q))))))))
      (let binary-search ([low 0] [high (* 2 n)])
        (if (> low high)
            high
            (let* ([mid (quotient (+ low high) 2)]
                   [can (can-reach? mid)])
              (if can
                  (binary-search (+ mid 1) high)
                  (binary-search low (- mid 1)))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec maximum_safeness_factor(Grid :: [[integer()]]) -> integer().
maximum_safeness_factor(Grid) ->
  N = length(Grid),
  Thieves = find_thieves(Grid, 0),
  DistMap = bfs_distances(queue:from_list(Thieves), maps:from_list([{T, 0} || T <- Thieves]), N),
  DistTuple = list_to_tuple([list_to_tuple([maps:get({R, C}, DistMap) || C <- lists:seq(0, N-1)]) || R <- lists:seq(0, N-1)]),
  binary_search(0, 2 * N, N, DistTuple).

find_thieves([], _) -> [];
find_thieves([Row | Rest], R) ->
  RowThieves = [{R, C} || {Val, C} <- lists:zip(Row, lists:seq(0, length(Row) - 1)), Val == 1],
  RowThieves ++ find_thieves(Rest, R + 1).

bfs_distances(Q, Map, N) ->
  case queue:out(Q) of
    {{value, {R, C}}, Q2} ->
      D = maps:get({R, C}, Map),
      {NewQ, NewMap} = lists:foldl(fun({DR, DC}, {AccQ, AccM}) ->
        NR = R + DR, NC = C + DC,
        if NR >= 0, NR < N, NC >= 0, NC < N ->
          case maps:is_key({NR, NC}, AccM) of
            false -> {queue:in({NR, NC}, AccQ), AccM#{{NR, NC} => D + 1}};
            true -> {AccQ, AccM}
          end;
        true -> {AccQ, AccM}
        end
      end, {Q2, Map}, [{0,1},{0,-1},{1,0},{-1,0}]),
      bfs_distances(NewQ, NewMap, N);
    {empty, _} -> Map
  end.

binary_search(Low, High, N, DistTuple) ->
  if Low > High -> High;
  true ->
    Mid = (Low + High) div 2,
    case can_reach(Mid, N, DistTuple) of
      true -> binary_search(Mid + 1, High, N, DistTuple);
      false -> binary_search(Low, Mid - 1, N, DistTuple)
    end
  end.

can_reach(V, N, DistTuple) ->
  S = element(1, element(1, DistTuple)),
  E = element(N, element(N, DistTuple)),
  if S < V; E < V -> false;
  true ->
    bfs_check(queue:from_list([{0, 0}]), #{{0, 0} => true}, V, N, DistTuple)
  end.

bfs_check(Q, Visited, V, N, DistTuple) ->
  case queue:out(Q) of
    {{value, {R, C}}, Q2} ->
      if R == N - 1, C == N - 1 -> true;
      true ->
        {NewQ, NewVisited} = lists:foldl(fun({DR, DC}, {AccQ, AccV}) ->
          NR = R + DR, NC = C + DC,
          if NR >= 0, NR < N, NC >= 0, NC < N ->
            case maps:is_key({NR, NC}, AccV) of
              false ->
                D = element(NC + 1, element(NR + 1, DistTuple)),
                if D >= V -> {queue:in({NR, NC}, AccQ), AccV#{{NR, NC} => true}};
                true -> {AccQ, AccV}
                end;
              true -> {AccQ, AccV}
            end;
          true -> {AccQ, AccV}
          end
        end, {Q2, Visited}, [{0,1},{0,-1},{1,0},{-1,0}]),
        bfs_check(NewQ, NewVisited, V, N, DistTuple)
      end;
    {empty, _} -> false
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximum_safeness_factor(grid :: [[integer]]) :: integer
  def maximum_safeness_factor(grid) do
    n = length(grid)
    thieves = for {row, r} <- Enum.with_index(grid), {val, c} <- Enum.with_index(row), val == 1, do: {r, c}

    dist_map = bfs_distances(:queue.from_list(thieves), Map.new(thieves, fn t -> {t, 0} end), n)

    dist_tuple = Enum.map(0..(n - 1), fn r ->
      Enum.map(0..(n - 1), fn c -> Map.get(dist_map, {r, c}) end) |> List.to_tuple()
    end) |> List.to_tuple()

    binary_search(0, 2 * n, n, dist_tuple)
  end

  defp bfs_distances(q, dist_map, n) do
    case :queue.out(q) do
      {:empty, _} -> dist_map
      {{:value, {r, c}}, q2} ->
        d = Map.get(dist_map, {r, c})
        {new_q, new_map} = Enum.reduce([{0, 1}, {0, -1}, {1, 0}, {-1, 0}], {q2, dist_map}, fn {dr, dc}, {acc_q, acc_m} ->
          nr = r + dr
          nc = c + dc
          if nr >= 0 and nr < n and nc >= 0 and nc < n and not Map.has_key?(acc_m, {nr, nc}) do
            {:queue.in({nr, nc}, acc_q), Map.put(acc_m, {nr, nc}, d + 1)}
          else
            {acc_q, acc_m}
          end
        end)
        bfs_distances(new_q, new_map, n)
    end
  end

  defp binary_search(low, high, n, dist_tuple) do
    if low > high do
      high
    else
      mid = div(low + high, 2)
      if can_reach(mid, n, dist_tuple) do
        binary_search(mid + 1, high, n, dist_tuple)
      else
        binary_search(low, mid - 1, n, dist_tuple)
      end
    end
  end

  defp can_reach(v, n, dist_tuple) do
    s_d = elem(elem(dist_tuple, 0), 0)
    e_d = elem(elem(dist_tuple, n - 1), n - 1)
    if s_d < v or e_d < v do
      false
    else
      bfs_check(:queue.from_list([{0, 0}]), %{{0, 0} => true}, v, n, dist_tuple)
    end
  end

  defp bfs_check(q, visited, v, n, dist_tuple) do
    case :queue.out(q) do
      {:empty, _} -> false
      {{:value, {r, c}}, q2} ->
        if r == n - 1 and c == n - 1 do
          true
        else
          {new_q, new_visited} = Enum.reduce([{0, 1}, {0, -1}, {1, 0}, {-1, 0}], {q2, visited}, fn {dr, dc}, {acc_q, acc_v} ->
            nr = r + dr
            nc = c + dc
            if nr >= 0 and nr < n and nc >= 0 and nc < n and not Map.has_key?(acc_v, {nr, nc}) and elem(elem(dist_tuple, nr), nc) >= v do
              {:queue.in({nr, nc}, acc_q), Map.put(acc_v, {nr, nc}, true)}
            else
              {acc_q, acc_v}
            end
          end)
          bfs_check(new_q, new_visited, v, n, dist_tuple)
        end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n^2 \log n) where n is the grid side length. The multi-source BFS takes O(n^2) as each cell and edge are processed once. The subsequent pathfinding step using a Dijkstra-like max-priority queue takes O(n^2 \log n^2), which simplifies to O(n^2 \log n), as we perform priority queue operations for each cell. Alternatively, using binary search with BFS would result in O(n^2 \log(2n)), which is also effectively O(n^2 \log n).
- **Space Complexity:** O(n^2) as we need to store the distance matrix of size n x n, a visited matrix or array to track processed cells, and auxiliary data structures like a queue for the initial BFS and a priority queue for the Dijkstra-like search.
