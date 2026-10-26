---
layout: post
title: "Count Islands With Total Value Divisible by K"
date: 2026-10-26 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Depth-First Search", "Breadth-First Search", "Union-Find", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <queue>\n#include <utility>\n\nusing namespace\
        \ std;\n\nclass Solution {\npublic:\n    int countIslands(vector<vector<int>>&\
        \ grid, int k) {\n        int m = grid.size();\n        if (m == 0) return 0;\n\
        \        int n = grid[0].size();\n        int count = 0;\n        int dr[] =\
        \ {0, 0, 1, -1};\n        int dc[] = {1, -1, 0, 0};\n\n        for (int i =\
        \ 0; i < m; ++i) {\n            for (int j = 0; j < n; ++j) {\n            \
        \    if (grid[i][j] > 0) {\n                    long long islandSum = 0;\n \
        \                   queue<pair<int, int>> q;\n                    islandSum\
        \ += (long long)grid[i][j];\n                    grid[i][j] = 0;\n         \
        \           q.push({i, j});\n\n                    while (!q.empty()) {\n  \
        \                      pair<int, int> curr = q.front();\n                  \
        \      q.pop();\n                        for (int d = 0; d < 4; ++d) {\n   \
        \                         int ni = curr.first + dr[d];\n                   \
        \         int nj = curr.second + dc[d];\n                            if (ni\
        \ >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] > 0) {\n             \
        \                   islandSum += (long long)grid[ni][nj];\n                \
        \                grid[ni][nj] = 0;\n                                q.push({ni,\
        \ nj});\n                            }\n                        }\n        \
        \            }\n                    if (islandSum % k == 0) count++;\n     \
        \           }\n            }\n        }\n        return count;\n    }\n};"
      java: "import java.util.ArrayDeque;\nimport java.util.Queue;\n\nclass Solution\
        \ {\n    public int countIslands(int[][] grid, int k) {\n        int m = grid.length;\n\
        \        if (m == 0) return 0;\n        int n = grid[0].length;\n        int\
        \ count = 0;\n        int[] dr = {0, 0, 1, -1};\n        int[] dc = {1, -1,\
        \ 0, 0};\n\n        for (int i = 0; i < m; i++) {\n            for (int j =\
        \ 0; j < n; j++) {\n                if (grid[i][j] > 0) {\n                \
        \    long islandSum = 0;\n                    Queue<int[]> q = new ArrayDeque<>();\n\
        \                    islandSum += grid[i][j];\n                    grid[i][j]\
        \ = 0;\n                    q.offer(new int[]{i, j});\n\n                  \
        \  while (!q.isEmpty()) {\n                        int[] curr = q.poll();\n\
        \                        for (int d = 0; d < 4; d++) {\n                   \
        \         int ni = curr[0] + dr[d];\n                            int nj = curr[1]\
        \ + dc[d];\n                            if (ni >= 0 && ni < m && nj >= 0 &&\
        \ nj < n && grid[ni][nj] > 0) {\n                                islandSum +=\
        \ grid[ni][nj];\n                                grid[ni][nj] = 0;\n       \
        \                         q.offer(new int[]{ni, nj});\n                    \
        \        }\n                        }\n                    }\n             \
        \       if (islandSum % k == 0) {\n                        count++;\n      \
        \              }\n                }\n            }\n        }\n        return\
        \ count;\n    }\n}"
      python: "from collections import deque\n\nclass Solution(object):\n    def countIslands(self,\
        \ grid, k):\n        \"\"\"\n        :type grid: List[List[int]]\n        :type\
        \ k: int\n        :rtype: int\n        \"\"\"\n        if not grid or not grid[0]:\n\
        \            return 0\n        m = len(grid)\n        n = len(grid[0])\n   \
        \     count = 0\n        for i in range(m):\n            for j in range(n):\n\
        \                if grid[i][j] > 0:\n                    island_sum = 0\n  \
        \                  q = deque([(i, j)])\n                    island_sum += grid[i][j]\n\
        \                    grid[i][j] = 0\n                    while q:\n        \
        \                r, c = q.popleft()\n                        for dr, dc in [(0,\
        \ 1), (0, -1), (1, 0), (-1, 0)]:\n                            nr, nc = r + dr,\
        \ c + dc\n                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc]\
        \ > 0:\n                                island_sum += grid[nr][nc]\n       \
        \                         grid[nr][nc] = 0\n                               \
        \ q.append((nr, nc))\n                    if island_sum % k == 0:\n        \
        \                count += 1\n        return count"
      python3: "from typing import List\nfrom collections import deque\n\nclass Solution:\n\
        \    def countIslands(self, grid: List[List[int]], k: int) -> int: \n      \
        \  if not grid or not grid[0]:\n            return 0\n        m, n = len(grid),\
        \ len(grid[0])\n        count = 0\n        for i in range(m):\n            for\
        \ j in range(n):\n                if grid[i][j] > 0:\n                    island_sum\
        \ = 0\n                    q = deque([(i, j)])\n                    island_sum\
        \ += grid[i][j]\n                    grid[i][j] = 0\n                    while\
        \ q:\n                        r, c = q.popleft()\n                        for\
        \ dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:\n                          \
        \  nr, nc = r + dr, c + dc\n                            if 0 <= nr < m and 0\
        \ <= nc < n and grid[nr][nc] > 0:\n                                island_sum\
        \ += grid[nr][nc]\n                                grid[nr][nc] = 0\n      \
        \                          q.append((nr, nc))\n                    if island_sum\
        \ % k == 0:\n                        count += 1\n        return count"
      c: "#include <stdlib.h>\n\nint countIslands(int** grid, int gridSize, int* gridColSize,\
        \ int k) {\n    if (gridSize == 0) return 0;\n    int m = gridSize;\n    int\
        \ count = 0;\n    int dr[] = {0, 0, 1, -1};\n    int dc[] = {1, -1, 0, 0};\n\
        \n    int totalCells = 0;\n    for (int i = 0; i < m; i++) totalCells += gridColSize[i];\n\
        \n    int* qr = (int*)malloc(sizeof(int) * totalCells);\n    int* qc = (int*)malloc(sizeof(int)\
        \ * totalCells);\n\n    for (int i = 0; i < m; i++) {\n        int n = gridColSize[i];\n\
        \        for (int j = 0; j < n; j++) {\n            if (grid[i][j] > 0) {\n\
        \                long long islandSum = 0;\n                int h = 0, t = 0;\n\
        \                islandSum += (long long)grid[i][j];\n                grid[i][j]\
        \ = 0;\n                qr[t] = i;\n                qc[t++] = j;\n\n       \
        \         while (h < t) {\n                    int r = qr[h];\n            \
        \        int c = qc[h++];\n                    for (int d = 0; d < 4; d++) {\n\
        \                        int nr = r + dr[d];\n                        int nc\
        \ = c + dc[d];\n                        if (nr >= 0 && nr < m && nc >= 0 &&\
        \ nc < gridColSize[nr] && grid[nr][nc] > 0) {\n                            islandSum\
        \ += (long long)grid[nr][nc];\n                            grid[nr][nc] = 0;\n\
        \                            qr[t] = nr;\n                            qc[t++]\
        \ = nc;\n                        }\n                    }\n                }\n\
        \                if (islandSum % (long long)k == 0) count++;\n            }\n\
        \        }\n    }\n\n    free(qr);\n    free(qc);\n    return count;\n}"
      csharp: "using System.Collections.Generic;\n\npublic class Solution {\n    public\
        \ int CountIslands(int[][] grid, int k) {\n        int m = grid.Length;\n  \
        \      if (m == 0) return 0;\n        int n = grid[0].Length;\n        int count\
        \ = 0;\n        int[] dr = { 0, 0, 1, -1 };\n        int[] dc = { 1, -1, 0,\
        \ 0 };\n\n        for (int r = 0; r < m; r++) {\n            for (int c = 0;\
        \ c < n; c++) {\n                if (grid[r][c] > 0) {\n                   \
        \ long islandSum = 0;\n                    Queue<int> queue = new Queue<int>();\n\
        \n                    islandSum += (long)grid[r][c];\n                    grid[r][c]\
        \ = 0;\n                    queue.Enqueue(r * n + c);\n\n                  \
        \  while (queue.Count > 0) {\n                        int pos = queue.Dequeue();\n\
        \                        int currR = pos / n;\n                        int currC\
        \ = pos % n;\n\n                        for (int i = 0; i < 4; i++) {\n    \
        \                        int nr = currR + dr[i];\n                         \
        \   int nc = currC + dc[i];\n                            if (nr >= 0 && nr <\
        \ m && nc >= 0 && nc < n && grid[nr][nc] > 0) {\n                          \
        \      islandSum += (long)grid[nr][nc];\n                                grid[nr][nc]\
        \ = 0;\n                                queue.Enqueue(nr * n + nc);\n      \
        \                      }\n                        }\n                    }\n\
        \                    if (islandSum % k == 0) {\n                        count++;\n\
        \                    }\n                }\n            }\n        }\n      \
        \  return count;\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @param {number} k\n * @return\
        \ {number}\n */\nvar countIslands = function(grid, k) {\n    const m = grid.length;\n\
        \    if (m === 0) return 0;\n    const n = grid[0].length;\n    let count =\
        \ 0;\n    const dr = [0, 0, 1, -1];\n    const dc = [1, -1, 0, 0];\n\n    for\
        \ (let r = 0; r < m; r++) {\n        for (let c = 0; c < n; c++) {\n       \
        \     if (grid[r][c] > 0) {\n                let islandSum = 0;\n          \
        \      let queue = [r * n + c];\n                islandSum += grid[r][c];\n\
        \                grid[r][c] = 0;\n                let head = 0;\n\n        \
        \        while (head < queue.length) {\n                    const pos = queue[head++];\n\
        \                    const currR = Math.floor(pos / n);\n                  \
        \  const currC = pos % n;\n\n                    for (let i = 0; i < 4; i++)\
        \ {\n                        const nr = currR + dr[i];\n                   \
        \     const nc = currC + dc[i];\n                        if (nr >= 0 && nr <\
        \ m && nc >= 0 && nc < n && grid[nr][nc] > 0) {\n                          \
        \  islandSum += grid[nr][nc];\n                            grid[nr][nc] = 0;\n\
        \                            queue.push(nr * n + nc);\n                    \
        \    }\n                    }\n                }\n                if (islandSum\
        \ % k === 0) {\n                    count++;\n                }\n          \
        \  }\n        }\n    }\n    return count;\n};"
      typescript: "function countIslands(grid: number[][], k: number): number {\n  \
        \  const m = grid.length;\n    if (m === 0) return 0;\n    const n = grid[0].length;\n\
        \    let count = 0;\n    const dr = [0, 0, 1, -1];\n    const dc = [1, -1, 0,\
        \ 0];\n\n    for (let r = 0; r < m; r++) {\n        for (let c = 0; c < n; c++)\
        \ {\n            if (grid[r][c] > 0) {\n                let islandSum: number\
        \ = 0;\n                let queue: number[] = [r * n + c];\n               \
        \ islandSum += grid[r][c];\n                grid[r][c] = 0;\n              \
        \  let head = 0;\n\n                while (head < queue.length) {\n        \
        \            const pos = queue[head++];\n                    const currR = Math.floor(pos\
        \ / n);\n                    const currC = pos % n;\n\n                    for\
        \ (let i = 0; i < 4; i++) {\n                        const nr = currR + dr[i];\n\
        \                        const nc = currC + dc[i];\n                       \
        \ if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > 0) {\n      \
        \                      islandSum += grid[nr][nc];\n                        \
        \    grid[nr][nc] = 0;\n                            queue.push(nr * n + nc);\n\
        \                        }\n                    }\n                }\n     \
        \           if (islandSum % k === 0) {\n                    count++;\n     \
        \           }\n            }\n        }\n    }\n    return count;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @param\
        \ Integer $k\n     * @return Integer\n     */\n    function countIslands($grid,\
        \ $k) {\n        $m = count($grid);\n        if ($m === 0) return 0;\n     \
        \   $n = count($grid[0]);\n        $count = 0;\n        $dr = [0, 0, 1, -1];\n\
        \        $dc = [1, -1, 0, 0];\n\n        for ($r = 0; $r < $m; $r++) {\n   \
        \         for ($c = 0; $c < $n; $c++) {\n                if ($grid[$r][$c] >\
        \ 0) {\n                    $islandSum = (float)$grid[$r][$c];\n           \
        \         $grid[$r][$c] = 0;\n                    $queue = [$r * $n + $c];\n\
        \                    $head = 0;\n\n                    while ($head < count($queue))\
        \ {\n                        $pos = $queue[$head++];\n                     \
        \   $currR = (int)($pos / $n);\n                        $currC = $pos % $n;\n\
        \n                        for ($i = 0; $i < 4; $i++) {\n                   \
        \         $nr = $currR + $dr[$i];\n                            $nc = $currC\
        \ + $dc[$i];\n                            if ($nr >= 0 && $nr < $m && $nc >=\
        \ 0 && $nc < $n && $grid[$nr][$nc] > 0) {\n                                $islandSum\
        \ += (float)$grid[$nr][$nc];\n                                $grid[$nr][$nc]\
        \ = 0;\n                                $queue[] = $nr * $n + $nc;\n       \
        \                     }\n                        }\n                    }\n\
        \                    if (fmod($islandSum, (float)$k) == 0.0) {\n           \
        \             $count++;\n                    }\n                }\n        \
        \    }\n        }\n        return $count;\n    }\n}"
      swift: "class Solution {\n    func countIslands(_ grid: [[Int]], _ k: Int) ->\
        \ Int {\n        var grid = grid\n        let m = grid.count\n        if m ==\
        \ 0 { return 0 }\n        let n = grid[0].count\n        var totalCount = 0\n\
        \        let dr = [0, 0, 1, -1]\n        let dc = [1, -1, 0, 0]\n\n        for\
        \ r in 0..<m {\n            for c in 0..<n {\n                if grid[r][c]\
        \ > 0 {\n                    var islandSum = 0\n                    var queue\
        \ = [Int]()\n\n                    islandSum += grid[r][c]\n               \
        \     grid[r][c] = 0\n                    queue.append(r * n + c)\n\n      \
        \              var head = 0\n                    while head < queue.count {\n\
        \                        let pos = queue[head]\n                        head\
        \ += 1\n                        let currR = pos / n\n                      \
        \  let currC = pos % n\n\n                        for i in 0..<4 {\n       \
        \                     let nr = currR + dr[i]\n                            let\
        \ nc = currC + dc[i]\n                            if nr >= 0 && nr < m && nc\
        \ >= 0 && nc < n && grid[nr][nc] > 0 {\n                                islandSum\
        \ += grid[nr][nc]\n                                grid[nr][nc] = 0\n      \
        \                          queue.append(nr * n + nc)\n                     \
        \       }\n                        }\n                    }\n              \
        \      if islandSum % k == 0 {\n                        totalCount += 1\n  \
        \                  }\n                }\n            }\n        }\n        return\
        \ totalCount\n    }\n}"
      kotlin: "class Solution {\n    fun countIslands(grid: Array<IntArray>, k: Int):\
        \ Int {\n        val m = grid.size\n        val n = grid[0].size\n        var\
        \ count = 0\n        val dr = intArrayOf(0, 0, 1, -1)\n        val dc = intArrayOf(1,\
        \ -1, 0, 0)\n\n        for (i in 0 until m) {\n            for (j in 0 until\
        \ n) {\n                if (grid[i][j] > 0) {\n                    var islandSum:\
        \ Long = grid[i][j].toLong()\n                    grid[i][j] = 0\n         \
        \           val queue = java.util.ArrayDeque<Int>()\n                    queue.add(i\
        \ * n + j)\n\n                    while (queue.isNotEmpty()) {\n           \
        \             val curr = queue.poll()\n                        val r = curr\
        \ / n\n                        val c = curr % n\n\n                        for\
        \ (d in 0 until 4) {\n                            val nr = r + dr[d]\n     \
        \                       val nc = c + dc[d]\n                            if (nr\
        \ in 0 until m && nc in 0 until n && grid[nr][nc] > 0) {\n                 \
        \               islandSum += grid[nr][nc].toLong()\n                       \
        \         grid[nr][nc] = 0\n                                queue.add(nr * n\
        \ + nc)\n                            }\n                        }\n        \
        \            }\n                    if (islandSum % k.toLong() == 0L) {\n  \
        \                      count++\n                    }\n                }\n \
        \           }\n        }\n        return count\n    }\n}"
      dart: "class Solution {\n  int countIslands(List<List<int>> grid, int k) {\n \
        \   int m = grid.length;\n    int n = grid[0].length;\n    int count = 0;\n\
        \    List<int> dr = [0, 0, 1, -1];\n    List<int> dc = [1, -1, 0, 0];\n\n  \
        \  for (int i = 0; i < m; i++) {\n      for (int j = 0; j < n; j++) {\n    \
        \    if (grid[i][j] > 0) {\n          int islandSum = grid[i][j];\n        \
        \  grid[i][j] = 0;\n          List<int> queue = [i * n + j];\n          int\
        \ head = 0;\n\n          while (head < queue.length) {\n            int curr\
        \ = queue[head++];\n            int r = curr ~/ n;\n            int c = curr\
        \ % n;\n\n            for (int d = 0; d < 4; d++) {\n              int nr =\
        \ r + dr[d];\n              int nc = c + dc[d];\n              if (nr >= 0 &&\
        \ nr < m && nc >= 0 && nc < n && grid[nr][nc] > 0) {\n                islandSum\
        \ += grid[nr][nc];\n                grid[nr][nc] = 0;\n                queue.add(nr\
        \ * n + nc);\n              }\n            }\n          }\n          if (islandSum\
        \ % k == 0) {\n            count++;\n          }\n        }\n      }\n    }\n\
        \    return count;\n  }\n}"
      go: "func countIslands(grid [][]int, k int) int {\n\tm := len(grid)\n\tn := len(grid[0])\n\
        \tcount := 0\n\tdr := []int{0, 0, 1, -1}\n\tdc := []int{1, -1, 0, 0}\n\n\tfor\
        \ i := 0; i < m; i++ {\n\t\tfor j := 0; j < n; j++ {\n\t\t\tif grid[i][j] >\
        \ 0 {\n\t\t\t\tislandSum := int64(grid[i][j])\n\t\t\t\tgrid[i][j] = 0\n\t\t\t\
        \tqueue := []int{i*n + j}\n\t\t\t\tfor head := 0; head < len(queue); head++\
        \ {\n\t\t\t\t\tcurr := queue[head]\n\t\t\t\t\tr, c := curr/n, curr%n\n\t\t\t\
        \t\tfor d := 0; d < 4; d++ {\n\t\t\t\t\t\tnr, nc := r+dr[d], c+dc[d]\n\t\t\t\
        \t\t\tif nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > 0 {\n\t\t\t\
        \t\t\t\tislandSum += int64(grid[nr][nc])\n\t\t\t\t\t\t\tgrid[nr][nc] = 0\n\t\
        \t\t\t\t\t\tqueue = append(queue, nr*n+nc)\n\t\t\t\t\t\t}\n\t\t\t\t\t}\n\t\t\
        \t\t}\n\t\t\t\tif islandSum%int64(k) == 0 {\n\t\t\t\t\tcount++\n\t\t\t\t}\n\t\
        \t\t}\n\t\t}\n\t}\n\treturn count\n}"
      ruby: "# @param {Integer[][]} grid\n# @param {Integer} k\n# @return {Integer}\n\
        def count_islands(grid, k)\n  m = grid.length\n  n = grid[0].length\n  count\
        \ = 0\n  dr = [0, 0, 1, -1]\n  dc = [1, -1, 0, 0]\n\n  (0...m).each do |i|\n\
        \    (0...n).each do |j|\n      if grid[i][j] > 0\n        island_sum = grid[i][j]\n\
        \        grid[i][j] = 0\n        queue = [i * n + j]\n        head = 0\n\n \
        \       while head < queue.length\n          curr = queue[head]\n          head\
        \ += 1\n          r = curr / n\n          c = curr % n\n\n          (0...4).each\
        \ do |d|\n            nr, nc = r + dr[d], c + dc[d]\n            if nr >= 0\
        \ && nr < m && nc >= 0 && nc < n && grid[nr][nc] > 0\n              island_sum\
        \ += grid[nr][nc]\n              grid[nr][nc] = 0\n              queue << (nr\
        \ * n + nc)\n            end\n          end\n        end\n        count += 1\
        \ if island_sum % k == 0\n      end\n    end\n  end\n  count\nend"
      scala: "object Solution {\n    def countIslands(grid: Array[Array[Int]], k: Int):\
        \ Int = {\n        val m = grid.length\n        val n = grid(0).length\n   \
        \     var count = 0\n        val dr = Array(0, 0, 1, -1)\n        val dc = Array(1,\
        \ -1, 0, 0)\n\n        for (i <- 0 until m) {\n            for (j <- 0 until\
        \ n) {\n                if (grid(i)(j) > 0) {\n                    var islandSum:\
        \ Long = grid(i)(j).toLong\n                    grid(i)(j) = 0\n           \
        \         val queue = scala.collection.mutable.Queue[Int]()\n              \
        \      queue.enqueue(i * n + j)\n\n                    while (queue.nonEmpty)\
        \ {\n                        val curr = queue.dequeue()\n                  \
        \      val r = curr / n\n                        val c = curr % n\n\n      \
        \                  for (d <- 0 until 4) {\n                            val nr\
        \ = r + dr(d)\n                            val nc = c + dc(d)\n            \
        \                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr)(nc)\
        \ > 0) {\n                                islandSum += grid(nr)(nc).toLong\n\
        \                                grid(nr)(nc) = 0\n                        \
        \        queue.enqueue(nr * n + nc)\n                            }\n       \
        \                 }\n                    }\n                    if (islandSum\
        \ % k.toLong == 0L) {\n                        count += 1\n                \
        \    }\n                }\n            }\n        }\n        count\n    }\n}"
      rust: "impl Solution {\n    pub fn count_islands(grid: Vec<Vec<i32>>, k: i32)\
        \ -> i32 {\n        let mut grid = grid;\n        let m = grid.len();\n    \
        \    if m == 0 { return 0; }\n        let n = grid[0].len();\n        let mut\
        \ count = 0;\n        let mut stack = Vec::with_capacity(m * n);\n        let\
        \ k_val = k as i64;\n\n        for r in 0..m {\n            for c in 0..n {\n\
        \                if grid[r][c] > 0 {\n                    let mut island_sum:\
        \ i64 = 0;\n                    island_sum += grid[r][c] as i64;\n         \
        \           grid[r][c] = 0;\n                    stack.push((r, c));\n\n   \
        \                 while let Some((curr_r, curr_c)) = stack.pop() {\n       \
        \                 let dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)];\n         \
        \               for (dr, dc) in dirs {\n                            let nr =\
        \ curr_r as i32 + dr;\n                            let nc = curr_c as i32 +\
        \ dc;\n                            if nr >= 0 && nr < m as i32 && nc >= 0 &&\
        \ nc < n as i32 {\n                                let ur = nr as usize;\n \
        \                               let uc = nc as usize;\n                    \
        \            if grid[ur][uc] > 0 {\n                                    island_sum\
        \ += grid[ur][uc] as i64;\n                                    grid[ur][uc]\
        \ = 0;\n                                    stack.push((ur, uc));\n        \
        \                        }\n                            }\n                \
        \        }\n                    }\n                    if island_sum % k_val\
        \ == 0 {\n                        count += 1;\n                    }\n     \
        \           }\n            }\n        }\n        count\n    }\n}"
      racket: "(define/contract (count-islands grid k)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer? exact-integer?)\n  (let* ([m (length grid)]\n         [n (length\
        \ (car grid))]\n         [vec (make-vector (* m n))]\n         [visited (make-vector\
        \ (* m n) #f)])\n    (for ([r (in-range m)]\n          [row grid])\n      (for\
        \ ([c (in-range n)]\n            [val row])\n        (vector-set! vec (+ (*\
        \ r n) c) val)))\n    (let ([count 0])\n      (for ([r (in-range m)])\n    \
        \    (for ([c (in-range n)])\n          (let ([idx (+ (* r n) c)])\n       \
        \     (when (and (> (vector-ref vec idx) 0) (not (vector-ref visited idx)))\n\
        \              (let ([island-sum 0]\n                    [stack (list (cons\
        \ r c))])\n                (vector-set! visited idx #t)\n                (let\
        \ loop ([s stack] [total 0])\n                  (if (null? s)\n            \
        \          (set! island-sum total)\n                      (let* ([curr (car\
        \ s)]\n                             [rest (cdr s)]\n                       \
        \      [cr (car curr)]\n                             [cc (cdr curr)]\n     \
        \                        [c-idx (+ (* cr n) cc)]\n                         \
        \    [val (vector-ref vec c-idx)]\n                             [next-total\
        \ (+ total val)]\n                             [new-neighbors '()])\n      \
        \                  (for ([dir '((0 . 1) (0 . -1) (1 . 0) (-1 . 0))])\n     \
        \                     (let ([nr (+ cr (car dir))]\n                        \
        \        [nc (+ cc (cdr dir))])\n                            (when (and (>=\
        \ nr 0) (< nr m) (>= nc 0) (< nc n))\n                              (let ([n-idx\
        \ (+ (* nr n) nc)])\n                                (when (and (> (vector-ref\
        \ vec n-idx) 0) (not (vector-ref visited n-idx)))\n                        \
        \          (vector-set! visited n-idx #t)\n                                \
        \  (set! new-neighbors (cons (cons nr nc) new-neighbors)))))))\n           \
        \             (loop (append new-neighbors rest) next-total))))\n           \
        \     (when (= 0 (remainder island-sum k))\n                  (set! count (+\
        \ count 1))))))))\n      count)))"
      erlang: "-spec count_islands(Grid :: [[integer()]], K :: integer()) -> integer().\n\
        count_islands(Grid, K) ->\n  Map = build_map(Grid),\n  process_islands(Map,\
        \ K).\n\nbuild_map(Grid) ->\n  {FinalMap, _} = lists:foldl(fun(Row, {M1, R})\
        \ ->\n    {M2, _} = lists:foldl(fun(Val, {M_inner, C}) ->\n      NewM = if Val\
        \ > 0 -> maps:put({R, C}, Val, M_inner); true -> M_inner end,\n      {NewM,\
        \ C + 1}\n    end, {M1, 0}, Row),\n    {M2, R + 1}\n  end, {maps:new(), 0},\
        \ Grid),\n  FinalMap.\n\nprocess_islands(Map, K) ->\n  Keys = maps:keys(Map),\n\
        \  {_, FinalCount} = lists:foldl(fun(Key, {Visited, Count}) ->\n    case sets:is_element(Key,\
        \ Visited) of\n      true -> {Visited, Count};\n      false ->\n        {IslandSum,\
        \ NewVisited} = bfs([Key], Map, 0, sets:add_element(Key, Visited)),\n      \
        \  NewCount = if IslandSum rem K =:= 0 -> Count + 1; true -> Count end,\n  \
        \      {NewVisited, NewCount}\n    end\n  end, {sets:new(), 0}, Keys),\n  FinalCount.\n\
        \nbfs([], _Map, Sum, Visited) -> {Sum, Visited};\nbfs([{R, C} | Rest], Map,\
        \ Sum, Visited) ->\n  Val = maps:get({R, C}, Map),\n  Dirs = [{0, 1}, {0, -1},\
        \ {1, 0}, {-1, 0}],\n  {Neighbors, NewVisited} = lists:foldl(fun({DR, DC}, {Acc,\
        \ V}) ->\n    NR = R + DR, NC = C + DC,\n    case maps:is_key({NR, NC}, Map)\
        \ andalso not sets:is_element({NR, NC}, V) of\n      true -> {[{NR, NC} | Acc],\
        \ sets:add_element({NR, NC}, V)};\n      false -> {Acc, V}\n    end\n  end,\
        \ {[], Visited}, Dirs),\n  bfs(Neighbors ++ Rest, Map, Sum + Val, NewVisited)."
      elixir: "defmodule Solution do\n  @spec count_islands(grid :: [[integer]], k ::\
        \ integer) :: integer\n  def count_islands(grid, k) do\n    map = build_map(grid)\n\
        \    process_islands(map, k)\n  end\n\n  defp build_map(grid) do\n    grid\n\
        \    |> Enum.with_index()\n    |> Enum.reduce(%{}, fn {row, r}, m_acc ->\n \
        \     row\n      |> Enum.with_index()\n      |> Enum.reduce(m_acc, fn {val,\
        \ c}, m_inner ->\n        if val > 0, do: Map.put(m_inner, {r, c}, val), else:\
        \ m_inner\n      end)\n    end)\n  end\n\n  defp process_islands(map, k) do\n\
        \    keys = Map.keys(map)\n    {_visited, count} = Enum.reduce(keys, {MapSet.new(),\
        \ 0}, fn key, {visited, count} ->\n      if MapSet.member?(visited, key) do\n\
        \        {visited, count}\n      else\n        {island_sum, updated_visited}\
        \ = bfs([key], map, 0, MapSet.put(visited, key))\n        new_count = if rem(island_sum,\
        \ k) == 0, do: count + 1, else: count\n        {updated_visited, new_count}\n\
        \      end\n    end)\n    count\n  end\n\n  defp bfs([], _map, sum, visited),\
        \ do: {sum, visited}\n  defp bfs([{r, c} | rest], map, sum, visited) do\n  \
        \  val = Map.get(map, {r, c})\n    dirs = [{0, 1}, {0, -1}, {1, 0}, {-1, 0}]\n\
        \    {neighbors, new_visited} = Enum.reduce(dirs, {[], visited}, fn {dr, dc},\
        \ {acc_n, acc_v} ->\n      nr = r + dr\n      nc = c + dc\n      if Map.has_key?(map,\
        \ {nr, nc}) and not MapSet.member?(acc_v, {nr, nc}) do\n        {[{nr, nc} |\
        \ acc_n], MapSet.put(acc_v, {nr, nc})}\n      else\n        {acc_n, acc_v}\n\
        \      end\n    end)\n    bfs(neighbors ++ rest, map, sum + val, new_visited)\n\
        \  end\nend"
    approach: 'The algorithm identifies islands by traversing the grid and performing
      a Breadth-First Search (BFS) for every unvisited positive integer found. Each
      positive integer cell acts as part of an island, while zero or already visited
      cells are ignored. During the BFS, we maintain a running total of the island''s
      values and mark each visited cell by setting its value to zero (in-place modification)
      to ensure every cell is processed exactly once.


      After fully exploring an island, we calculate the total sum of its values. If
      this sum is divisible by k, we increment the island count. This approach ensures
      each cell is visited once during the linear scan and BFS, making it efficient
      for large grids. By modifying the grid in-place, we avoid the overhead of an additional
      visited matrix while maintaining clear and effective island separation.'
    time_complexity: O(m * n), where m and n are the dimensions of the grid. Each cell
      is visited at most twice (once during the grid traversal and once during an island
      BFS), resulting in a complexity proportional to the total number of cells.
    space_complexity: O(m * n) in the worst case. This occurs when the entire grid forms
      a single large island, requiring the BFS queue or DFS recursion stack to store
      coordinates for up to all m * n cells.
    elapsed_time: 365.13938999176025
    model: gemini-3-flash-preview
    generated_at: '2026-10-26 02:39:23 '
---

## Problem #3619: Count Islands With Total Value Divisible by K

**Difficulty:** Medium

**Topics:** Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix

## Problem Description

<p>You are given an <code>m x n</code> matrix <code>grid</code> and a positive integer <code>k</code>. An <strong>island</strong> is a group of <strong>positive</strong> integers (representing land) that are <strong>4-directionally</strong> connected (horizontally or vertically).</p>

<p>The <strong>total value</strong> of an island is the sum of the values of all cells in the island.</p>

<p>Return the number of islands with a total value <strong>divisible by</strong> <code>k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2025/03/06/example1griddrawio-1.png" style="width: 200px; height: 200px;" />
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.</p>
</div>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2025/03/06/example2griddrawio.png" style="width: 200px; height: 150px;" />
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>The grid contains six islands, each with a total value that is divisible by 3.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 1000</code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>6</sup></code></li>
</ul>


## Hints

1. Use a BFS/DFS to find connected components.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm identifies islands by traversing the grid and performing a Breadth-First Search (BFS) for every unvisited positive integer found. Each positive integer cell acts as part of an island, while zero or already visited cells are ignored. During the BFS, we maintain a running total of the island's values and mark each visited cell by setting its value to zero (in-place modification) to ensure every cell is processed exactly once.

After fully exploring an island, we calculate the total sum of its values. If this sum is divisible by k, we increment the island count. This approach ensures each cell is visited once during the linear scan and BFS, making it efficient for large grids. By modifying the grid in-place, we avoid the overhead of an additional visited matrix while maintaining clear and effective island separation.

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
#include <vector>
#include <queue>
#include <utility>

using namespace std;

class Solution {
public:
    int countIslands(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        int count = 0;
        int dr[] = {0, 0, 1, -1};
        int dc[] = {1, -1, 0, 0};

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] > 0) {
                    long long islandSum = 0;
                    queue<pair<int, int>> q;
                    islandSum += (long long)grid[i][j];
                    grid[i][j] = 0;
                    q.push({i, j});

                    while (!q.empty()) {
                        pair<int, int> curr = q.front();
                        q.pop();
                        for (int d = 0; d < 4; ++d) {
                            int ni = curr.first + dr[d];
                            int nj = curr.second + dc[d];
                            if (ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] > 0) {
                                islandSum += (long long)grid[ni][nj];
                                grid[ni][nj] = 0;
                                q.push({ni, nj});
                            }
                        }
                    }
                    if (islandSum % k == 0) count++;
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
import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int countIslands(int[][] grid, int k) {
        int m = grid.length;
        if (m == 0) return 0;
        int n = grid[0].length;
        int count = 0;
        int[] dr = {0, 0, 1, -1};
        int[] dc = {1, -1, 0, 0};

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > 0) {
                    long islandSum = 0;
                    Queue<int[]> q = new ArrayDeque<>();
                    islandSum += grid[i][j];
                    grid[i][j] = 0;
                    q.offer(new int[]{i, j});

                    while (!q.isEmpty()) {
                        int[] curr = q.poll();
                        for (int d = 0; d < 4; d++) {
                            int ni = curr[0] + dr[d];
                            int nj = curr[1] + dc[d];
                            if (ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] > 0) {
                                islandSum += grid[ni][nj];
                                grid[ni][nj] = 0;
                                q.offer(new int[]{ni, nj});
                            }
                        }
                    }
                    if (islandSum % k == 0) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
from collections import deque

class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    island_sum = 0
                    q = deque([(i, j)])
                    island_sum += grid[i][j]
                    grid[i][j] = 0
                    while q:
                        r, c = q.popleft()
                        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0
                                q.append((nr, nc))
                    if island_sum % k == 0:
                        count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List
from collections import deque

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int: 
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    island_sum = 0
                    q = deque([(i, j)])
                    island_sum += grid[i][j]
                    grid[i][j] = 0
                    while q:
                        r, c = q.popleft()
                        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0
                                q.append((nr, nc))
                    if island_sum % k == 0:
                        count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int countIslands(int** grid, int gridSize, int* gridColSize, int k) {
    if (gridSize == 0) return 0;
    int m = gridSize;
    int count = 0;
    int dr[] = {0, 0, 1, -1};
    int dc[] = {1, -1, 0, 0};

    int totalCells = 0;
    for (int i = 0; i < m; i++) totalCells += gridColSize[i];

    int* qr = (int*)malloc(sizeof(int) * totalCells);
    int* qc = (int*)malloc(sizeof(int) * totalCells);

    for (int i = 0; i < m; i++) {
        int n = gridColSize[i];
        for (int j = 0; j < n; j++) {
            if (grid[i][j] > 0) {
                long long islandSum = 0;
                int h = 0, t = 0;
                islandSum += (long long)grid[i][j];
                grid[i][j] = 0;
                qr[t] = i;
                qc[t++] = j;

                while (h < t) {
                    int r = qr[h];
                    int c = qc[h++];
                    for (int d = 0; d < 4; d++) {
                        int nr = r + dr[d];
                        int nc = c + dc[d];
                        if (nr >= 0 && nr < m && nc >= 0 && nc < gridColSize[nr] && grid[nr][nc] > 0) {
                            islandSum += (long long)grid[nr][nc];
                            grid[nr][nc] = 0;
                            qr[t] = nr;
                            qc[t++] = nc;
                        }
                    }
                }
                if (islandSum % (long long)k == 0) count++;
            }
        }
    }

    free(qr);
    free(qc);
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Collections.Generic;

public class Solution {
    public int CountIslands(int[][] grid, int k) {
        int m = grid.Length;
        if (m == 0) return 0;
        int n = grid[0].Length;
        int count = 0;
        int[] dr = { 0, 0, 1, -1 };
        int[] dc = { 1, -1, 0, 0 };

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] > 0) {
                    long islandSum = 0;
                    Queue<int> queue = new Queue<int>();

                    islandSum += (long)grid[r][c];
                    grid[r][c] = 0;
                    queue.Enqueue(r * n + c);

                    while (queue.Count > 0) {
                        int pos = queue.Dequeue();
                        int currR = pos / n;
                        int currC = pos % n;

                        for (int i = 0; i < 4; i++) {
                            int nr = currR + dr[i];
                            int nc = currC + dc[i];
                            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > 0) {
                                islandSum += (long)grid[nr][nc];
                                grid[nr][nc] = 0;
                                queue.Enqueue(nr * n + nc);
                            }
                        }
                    }
                    if (islandSum % k == 0) {
                        count++;
                    }
                }
            }
        }
        return count;
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
var countIslands = function(grid, k) {
    const m = grid.length;
    if (m === 0) return 0;
    const n = grid[0].length;
    let count = 0;
    const dr = [0, 0, 1, -1];
    const dc = [1, -1, 0, 0];

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (grid[r][c] > 0) {
                let islandSum = 0;
                let queue = [r * n + c];
                islandSum += grid[r][c];
                grid[r][c] = 0;
                let head = 0;

                while (head < queue.length) {
                    const pos = queue[head++];
                    const currR = Math.floor(pos / n);
                    const currC = pos % n;

                    for (let i = 0; i < 4; i++) {
                        const nr = currR + dr[i];
                        const nc = currC + dc[i];
                        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > 0) {
                            islandSum += grid[nr][nc];
                            grid[nr][nc] = 0;
                            queue.push(nr * n + nc);
                        }
                    }
                }
                if (islandSum % k === 0) {
                    count++;
                }
            }
        }
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countIslands(grid: number[][], k: number): number {
    const m = grid.length;
    if (m === 0) return 0;
    const n = grid[0].length;
    let count = 0;
    const dr = [0, 0, 1, -1];
    const dc = [1, -1, 0, 0];

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (grid[r][c] > 0) {
                let islandSum: number = 0;
                let queue: number[] = [r * n + c];
                islandSum += grid[r][c];
                grid[r][c] = 0;
                let head = 0;

                while (head < queue.length) {
                    const pos = queue[head++];
                    const currR = Math.floor(pos / n);
                    const currC = pos % n;

                    for (let i = 0; i < 4; i++) {
                        const nr = currR + dr[i];
                        const nc = currC + dc[i];
                        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > 0) {
                            islandSum += grid[nr][nc];
                            grid[nr][nc] = 0;
                            queue.push(nr * n + nc);
                        }
                    }
                }
                if (islandSum % k === 0) {
                    count++;
                }
            }
        }
    }
    return count;
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
    function countIslands($grid, $k) {
        $m = count($grid);
        if ($m === 0) return 0;
        $n = count($grid[0]);
        $count = 0;
        $dr = [0, 0, 1, -1];
        $dc = [1, -1, 0, 0];

        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($grid[$r][$c] > 0) {
                    $islandSum = (float)$grid[$r][$c];
                    $grid[$r][$c] = 0;
                    $queue = [$r * $n + $c];
                    $head = 0;

                    while ($head < count($queue)) {
                        $pos = $queue[$head++];
                        $currR = (int)($pos / $n);
                        $currC = $pos % $n;

                        for ($i = 0; $i < 4; $i++) {
                            $nr = $currR + $dr[$i];
                            $nc = $currC + $dc[$i];
                            if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $grid[$nr][$nc] > 0) {
                                $islandSum += (float)$grid[$nr][$nc];
                                $grid[$nr][$nc] = 0;
                                $queue[] = $nr * $n + $nc;
                            }
                        }
                    }
                    if (fmod($islandSum, (float)$k) == 0.0) {
                        $count++;
                    }
                }
            }
        }
        return $count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countIslands(_ grid: [[Int]], _ k: Int) -> Int {
        var grid = grid
        let m = grid.count
        if m == 0 { return 0 }
        let n = grid[0].count
        var totalCount = 0
        let dr = [0, 0, 1, -1]
        let dc = [1, -1, 0, 0]

        for r in 0..<m {
            for c in 0..<n {
                if grid[r][c] > 0 {
                    var islandSum = 0
                    var queue = [Int]()

                    islandSum += grid[r][c]
                    grid[r][c] = 0
                    queue.append(r * n + c)

                    var head = 0
                    while head < queue.count {
                        let pos = queue[head]
                        head += 1
                        let currR = pos / n
                        let currC = pos % n

                        for i in 0..<4 {
                            let nr = currR + dr[i]
                            let nc = currC + dc[i]
                            if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > 0 {
                                islandSum += grid[nr][nc]
                                grid[nr][nc] = 0
                                queue.append(nr * n + nc)
                            }
                        }
                    }
                    if islandSum % k == 0 {
                        totalCount += 1
                    }
                }
            }
        }
        return totalCount
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countIslands(grid: Array<IntArray>, k: Int): Int {
        val m = grid.size
        val n = grid[0].size
        var count = 0
        val dr = intArrayOf(0, 0, 1, -1)
        val dc = intArrayOf(1, -1, 0, 0)

        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] > 0) {
                    var islandSum: Long = grid[i][j].toLong()
                    grid[i][j] = 0
                    val queue = java.util.ArrayDeque<Int>()
                    queue.add(i * n + j)

                    while (queue.isNotEmpty()) {
                        val curr = queue.poll()
                        val r = curr / n
                        val c = curr % n

                        for (d in 0 until 4) {
                            val nr = r + dr[d]
                            val nc = c + dc[d]
                            if (nr in 0 until m && nc in 0 until n && grid[nr][nc] > 0) {
                                islandSum += grid[nr][nc].toLong()
                                grid[nr][nc] = 0
                                queue.add(nr * n + nc)
                            }
                        }
                    }
                    if (islandSum % k.toLong() == 0L) {
                        count++
                    }
                }
            }
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int countIslands(List<List<int>> grid, int k) {
    int m = grid.length;
    int n = grid[0].length;
    int count = 0;
    List<int> dr = [0, 0, 1, -1];
    List<int> dc = [1, -1, 0, 0];

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] > 0) {
          int islandSum = grid[i][j];
          grid[i][j] = 0;
          List<int> queue = [i * n + j];
          int head = 0;

          while (head < queue.length) {
            int curr = queue[head++];
            int r = curr ~/ n;
            int c = curr % n;

            for (int d = 0; d < 4; d++) {
              int nr = r + dr[d];
              int nc = c + dc[d];
              if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > 0) {
                islandSum += grid[nr][nc];
                grid[nr][nc] = 0;
                queue.add(nr * n + nc);
              }
            }
          }
          if (islandSum % k == 0) {
            count++;
          }
        }
      }
    }
    return count;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func countIslands(grid [][]int, k int) int {
	m := len(grid)
	n := len(grid[0])
	count := 0
	dr := []int{0, 0, 1, -1}
	dc := []int{1, -1, 0, 0}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] > 0 {
				islandSum := int64(grid[i][j])
				grid[i][j] = 0
				queue := []int{i*n + j}
				for head := 0; head < len(queue); head++ {
					curr := queue[head]
					r, c := curr/n, curr%n
					for d := 0; d < 4; d++ {
						nr, nc := r+dr[d], c+dc[d]
						if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > 0 {
							islandSum += int64(grid[nr][nc])
							grid[nr][nc] = 0
							queue = append(queue, nr*n+nc)
						}
					}
				}
				if islandSum%int64(k) == 0 {
					count++
				}
			}
		}
	}
	return count
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
def count_islands(grid, k)
  m = grid.length
  n = grid[0].length
  count = 0
  dr = [0, 0, 1, -1]
  dc = [1, -1, 0, 0]

  (0...m).each do |i|
    (0...n).each do |j|
      if grid[i][j] > 0
        island_sum = grid[i][j]
        grid[i][j] = 0
        queue = [i * n + j]
        head = 0

        while head < queue.length
          curr = queue[head]
          head += 1
          r = curr / n
          c = curr % n

          (0...4).each do |d|
            nr, nc = r + dr[d], c + dc[d]
            if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > 0
              island_sum += grid[nr][nc]
              grid[nr][nc] = 0
              queue << (nr * n + nc)
            end
          end
        end
        count += 1 if island_sum % k == 0
      end
    end
  end
  count
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countIslands(grid: Array[Array[Int]], k: Int): Int = {
        val m = grid.length
        val n = grid(0).length
        var count = 0
        val dr = Array(0, 0, 1, -1)
        val dc = Array(1, -1, 0, 0)

        for (i <- 0 until m) {
            for (j <- 0 until n) {
                if (grid(i)(j) > 0) {
                    var islandSum: Long = grid(i)(j).toLong
                    grid(i)(j) = 0
                    val queue = scala.collection.mutable.Queue[Int]()
                    queue.enqueue(i * n + j)

                    while (queue.nonEmpty) {
                        val curr = queue.dequeue()
                        val r = curr / n
                        val c = curr % n

                        for (d <- 0 until 4) {
                            val nr = r + dr(d)
                            val nc = c + dc(d)
                            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr)(nc) > 0) {
                                islandSum += grid(nr)(nc).toLong
                                grid(nr)(nc) = 0
                                queue.enqueue(nr * n + nc)
                            }
                        }
                    }
                    if (islandSum % k.toLong == 0L) {
                        count += 1
                    }
                }
            }
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_islands(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let mut grid = grid;
        let m = grid.len();
        if m == 0 { return 0; }
        let n = grid[0].len();
        let mut count = 0;
        let mut stack = Vec::with_capacity(m * n);
        let k_val = k as i64;

        for r in 0..m {
            for c in 0..n {
                if grid[r][c] > 0 {
                    let mut island_sum: i64 = 0;
                    island_sum += grid[r][c] as i64;
                    grid[r][c] = 0;
                    stack.push((r, c));

                    while let Some((curr_r, curr_c)) = stack.pop() {
                        let dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)];
                        for (dr, dc) in dirs {
                            let nr = curr_r as i32 + dr;
                            let nc = curr_c as i32 + dc;
                            if nr >= 0 && nr < m as i32 && nc >= 0 && nc < n as i32 {
                                let ur = nr as usize;
                                let uc = nc as usize;
                                if grid[ur][uc] > 0 {
                                    island_sum += grid[ur][uc] as i64;
                                    grid[ur][uc] = 0;
                                    stack.push((ur, uc));
                                }
                            }
                        }
                    }
                    if island_sum % k_val == 0 {
                        count += 1;
                    }
                }
            }
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (count-islands grid k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ([m (length grid)]
         [n (length (car grid))]
         [vec (make-vector (* m n))]
         [visited (make-vector (* m n) #f)])
    (for ([r (in-range m)]
          [row grid])
      (for ([c (in-range n)]
            [val row])
        (vector-set! vec (+ (* r n) c) val)))
    (let ([count 0])
      (for ([r (in-range m)])
        (for ([c (in-range n)])
          (let ([idx (+ (* r n) c)])
            (when (and (> (vector-ref vec idx) 0) (not (vector-ref visited idx)))
              (let ([island-sum 0]
                    [stack (list (cons r c))])
                (vector-set! visited idx #t)
                (let loop ([s stack] [total 0])
                  (if (null? s)
                      (set! island-sum total)
                      (let* ([curr (car s)]
                             [rest (cdr s)]
                             [cr (car curr)]
                             [cc (cdr curr)]
                             [c-idx (+ (* cr n) cc)]
                             [val (vector-ref vec c-idx)]
                             [next-total (+ total val)]
                             [new-neighbors '()])
                        (for ([dir '((0 . 1) (0 . -1) (1 . 0) (-1 . 0))])
                          (let ([nr (+ cr (car dir))]
                                [nc (+ cc (cdr dir))])
                            (when (and (>= nr 0) (< nr m) (>= nc 0) (< nc n))
                              (let ([n-idx (+ (* nr n) nc)])
                                (when (and (> (vector-ref vec n-idx) 0) (not (vector-ref visited n-idx)))
                                  (vector-set! visited n-idx #t)
                                  (set! new-neighbors (cons (cons nr nc) new-neighbors)))))))
                        (loop (append new-neighbors rest) next-total))))
                (when (= 0 (remainder island-sum k))
                  (set! count (+ count 1))))))))
      count)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec count_islands(Grid :: [[integer()]], K :: integer()) -> integer().
count_islands(Grid, K) ->
  Map = build_map(Grid),
  process_islands(Map, K).

build_map(Grid) ->
  {FinalMap, _} = lists:foldl(fun(Row, {M1, R}) ->
    {M2, _} = lists:foldl(fun(Val, {M_inner, C}) ->
      NewM = if Val > 0 -> maps:put({R, C}, Val, M_inner); true -> M_inner end,
      {NewM, C + 1}
    end, {M1, 0}, Row),
    {M2, R + 1}
  end, {maps:new(), 0}, Grid),
  FinalMap.

process_islands(Map, K) ->
  Keys = maps:keys(Map),
  {_, FinalCount} = lists:foldl(fun(Key, {Visited, Count}) ->
    case sets:is_element(Key, Visited) of
      true -> {Visited, Count};
      false ->
        {IslandSum, NewVisited} = bfs([Key], Map, 0, sets:add_element(Key, Visited)),
        NewCount = if IslandSum rem K =:= 0 -> Count + 1; true -> Count end,
        {NewVisited, NewCount}
    end
  end, {sets:new(), 0}, Keys),
  FinalCount.

bfs([], _Map, Sum, Visited) -> {Sum, Visited};
bfs([{R, C} | Rest], Map, Sum, Visited) ->
  Val = maps:get({R, C}, Map),
  Dirs = [{0, 1}, {0, -1}, {1, 0}, {-1, 0}],
  {Neighbors, NewVisited} = lists:foldl(fun({DR, DC}, {Acc, V}) ->
    NR = R + DR, NC = C + DC,
    case maps:is_key({NR, NC}, Map) andalso not sets:is_element({NR, NC}, V) of
      true -> {[{NR, NC} | Acc], sets:add_element({NR, NC}, V)};
      false -> {Acc, V}
    end
  end, {[], Visited}, Dirs),
  bfs(Neighbors ++ Rest, Map, Sum + Val, NewVisited).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_islands(grid :: [[integer]], k :: integer) :: integer
  def count_islands(grid, k) do
    map = build_map(grid)
    process_islands(map, k)
  end

  defp build_map(grid) do
    grid
    |> Enum.with_index()
    |> Enum.reduce(%{}, fn {row, r}, m_acc ->
      row
      |> Enum.with_index()
      |> Enum.reduce(m_acc, fn {val, c}, m_inner ->
        if val > 0, do: Map.put(m_inner, {r, c}, val), else: m_inner
      end)
    end)
  end

  defp process_islands(map, k) do
    keys = Map.keys(map)
    {_visited, count} = Enum.reduce(keys, {MapSet.new(), 0}, fn key, {visited, count} ->
      if MapSet.member?(visited, key) do
        {visited, count}
      else
        {island_sum, updated_visited} = bfs([key], map, 0, MapSet.put(visited, key))
        new_count = if rem(island_sum, k) == 0, do: count + 1, else: count
        {updated_visited, new_count}
      end
    end)
    count
  end

  defp bfs([], _map, sum, visited), do: {sum, visited}
  defp bfs([{r, c} | rest], map, sum, visited) do
    val = Map.get(map, {r, c})
    dirs = [{0, 1}, {0, -1}, {1, 0}, {-1, 0}]
    {neighbors, new_visited} = Enum.reduce(dirs, {[], visited}, fn {dr, dc}, {acc_n, acc_v} ->
      nr = r + dr
      nc = c + dc
      if Map.has_key?(map, {nr, nc}) and not MapSet.member?(acc_v, {nr, nc}) do
        {[{nr, nc} | acc_n], MapSet.put(acc_v, {nr, nc})}
      else
        {acc_n, acc_v}
      end
    end)
    bfs(neighbors ++ rest, map, sum + val, new_visited)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m * n), where m and n are the dimensions of the grid. Each cell is visited at most twice (once during the grid traversal and once during an island BFS), resulting in a complexity proportional to the total number of cells.
- **Space Complexity:** O(m * n) in the worst case. This occurs when the entire grid forms a single large island, requiring the BFS queue or DFS recursion stack to store coordinates for up to all m * n cells.
