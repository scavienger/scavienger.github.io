---
layout: post
title: "Find a Safe Walk Through a Grid"
date: 2026-07-02 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Breadth-First Search", "Graph Theory", "Heap (Priority Queue)", "Matrix", "Shortest Path"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/find-a-safe-walk-through-a-grid/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <deque>\n#include <climits>\n\nusing namespace\
        \ std;\n\nclass Solution {\npublic:\n    bool findSafeWalk(vector<vector<int>>&\
        \ grid, int health) {\n        int m = grid.size();\n        int n = grid[0].size();\n\
        \        vector<vector<int>> dist(m, vector<int>(n, INT_MAX));\n\n        deque<pair<int,\
        \ int>> dq;\n        dist[0][0] = grid[0][0];\n        dq.push_back({0, 0});\n\
        \n        int dr[] = {0, 0, 1, -1};\n        int dc[] = {1, -1, 0, 0};\n\n \
        \       while (!dq.empty()) {\n            pair<int, int> curr = dq.front();\n\
        \            dq.pop_front();\n            int r = curr.first;\n            int\
        \ c = curr.second;\n\n            for (int i = 0; i < 4; i++) {\n          \
        \      int nr = r + dr[i];\n                int nc = c + dc[i];\n\n        \
        \        if (nr >= 0 && nr < m && nc >= 0 && nc < n) {\n                   \
        \ int weight = grid[nr][nc];\n                    if (dist[r][c] + weight <\
        \ dist[nr][nc]) {\n                        dist[nr][nc] = dist[r][c] + weight;\n\
        \                        if (weight == 0) {\n                            dq.push_front({nr,\
        \ nc});\n                        } else {\n                            dq.push_back({nr,\
        \ nc});\n                        }\n                    }\n                }\n\
        \            }\n        }\n\n        return dist[m - 1][n - 1] < health;\n \
        \   }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public boolean findSafeWalk(List<List<Integer>>\
        \ grid, int health) {\n        int m = grid.size();\n        int n = grid.get(0).size();\n\
        \        int[][] dist = new int[m][n];\n        for (int i = 0; i < m; i++)\
        \ {\n            Arrays.fill(dist[i], Integer.MAX_VALUE);\n        }\n\n   \
        \     Deque<int[]> dq = new ArrayDeque<>();\n        dist[0][0] = grid.get(0).get(0);\n\
        \        dq.addFirst(new int[]{0, 0});\n\n        int[] dr = {0, 0, 1, -1};\n\
        \        int[] dc = {1, -1, 0, 0};\n\n        while (!dq.isEmpty()) {\n    \
        \        int[] curr = dq.pollFirst();\n            int r = curr[0];\n      \
        \      int c = curr[1];\n\n            for (int i = 0; i < 4; i++) {\n     \
        \           int nr = r + dr[i];\n                int nc = c + dc[i];\n\n   \
        \             if (nr >= 0 && nr < m && nc >= 0 && nc < n) {\n              \
        \      int weight = grid.get(nr).get(nc);\n                    if (dist[r][c]\
        \ + weight < dist[nr][nc]) {\n                        dist[nr][nc] = dist[r][c]\
        \ + weight;\n                        if (weight == 0) {\n                  \
        \          dq.addFirst(new int[]{nr, nc});\n                        } else {\n\
        \                            dq.addLast(new int[]{nr, nc});\n              \
        \          }\n                    }\n                }\n            }\n    \
        \    }\n\n        return dist[m - 1][n - 1] < health;\n    }\n}"
      python: "import collections\n\nclass Solution(object):\n    def findSafeWalk(self,\
        \ grid, health):\n        \"\"\"\n        :type grid: List[List[int]]\n    \
        \    :type health: int\n        :rtype: bool\n        \"\"\"\n        m = len(grid)\n\
        \        n = len(grid[0])\n        dist = [[float('inf')] * n for _ in range(m)]\n\
        \n        dist[0][0] = grid[0][0]\n        dq = collections.deque([(0, 0)])\n\
        \n        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]\n\n        while dq:\n\
        \            r, c = dq.popleft()\n\n            for dr, dc in directions:\n\
        \                nr, nc = r + dr, c + dc\n\n                if 0 <= nr < m and\
        \ 0 <= nc < n:\n                    weight = grid[nr][nc]\n                \
        \    if dist[r][c] + weight < dist[nr][nc]:\n                        dist[nr][nc]\
        \ = dist[r][c] + weight\n                        if weight == 0:\n         \
        \                   dq.appendleft((nr, nc))\n                        else:\n\
        \                            dq.append((nr, nc))\n\n        return dist[m -\
        \ 1][n - 1] < health"
      python3: "from typing import List\nimport collections\n\nclass Solution:\n   \
        \ def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:\n    \
        \    m = len(grid)\n        n = len(grid[0])\n        dist = [[float('inf')]\
        \ * n for _ in range(m)]\n\n        dist[0][0] = grid[0][0]\n        dq = collections.deque([(0,\
        \ 0)])\n\n        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]\n\n      \
        \  while dq:\n            r, c = dq.popleft()\n\n            for dr, dc in directions:\n\
        \                nr, nc = r + dr, c + dc\n\n                if 0 <= nr < m and\
        \ 0 <= nc < n:\n                    weight = grid[nr][nc]\n                \
        \    if dist[r][c] + weight < dist[nr][nc]:\n                        dist[nr][nc]\
        \ = dist[r][c] + weight\n                        if weight == 0:\n         \
        \                   dq.appendleft((nr, nc))\n                        else:\n\
        \                            dq.append((nr, nc))\n\n        return dist[m -\
        \ 1][n - 1] < health"
      c: "#include <stdbool.h>\n#include <stdlib.h>\n\nbool findSafeWalk(int** grid,\
        \ int gridSize, int* gridColSize, int health) {\n    int m = gridSize;\n   \
        \ int n = gridColSize[0];\n    int dist[50][50];\n    for (int i = 0; i < m;\
        \ i++) {\n        for (int j = 0; j < n; j++) {\n            dist[i][j] = 1000000;\n\
        \        }\n    }\n\n    int dq[10000][2];\n    int head = 5000, tail = 5000;\n\
        \n    dist[0][0] = grid[0][0];\n    dq[tail][0] = 0;\n    dq[tail][1] = 0;\n\
        \    tail++;\n\n    int dr[] = {0, 0, 1, -1};\n    int dc[] = {1, -1, 0, 0};\n\
        \n    while (head < tail) {\n        int r = dq[head][0];\n        int c = dq[head][1];\n\
        \        head++;\n\n        for (int i = 0; i < 4; i++) {\n            int nr\
        \ = r + dr[i];\n            int nc = c + dc[i];\n\n            if (nr >= 0 &&\
        \ nr < m && nc >= 0 && nc < n) {\n                int weight = grid[nr][nc];\n\
        \                if (dist[r][c] + weight < dist[nr][nc]) {\n               \
        \     dist[nr][nc] = dist[r][c] + weight;\n                    if (weight ==\
        \ 0) {\n                        head--;\n                        dq[head][0]\
        \ = nr;\n                        dq[head][1] = nc;\n                    } else\
        \ {\n                        dq[tail][0] = nr;\n                        dq[tail][1]\
        \ = nc;\n                        tail++;\n                    }\n          \
        \      }\n            }\n        }\n    }\n\n    return dist[m - 1][n - 1] <\
        \ health;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public bool FindSafeWalk(IList<IList<int>> grid, int health) {\n  \
        \      int m = grid.Count;\n        int n = grid[0].Count;\n        int[,] dist\
        \ = new int[m, n];\n        for (int i = 0; i < m; i++) {\n            for (int\
        \ j = 0; j < n; j++) {\n                dist[i, j] = int.MaxValue;\n       \
        \     }\n        }\n\n        PriorityQueue<(int r, int c), int> pq = new PriorityQueue<(int,\
        \ int), int>();\n        dist[0, 0] = grid[0][0];\n        pq.Enqueue((0, 0),\
        \ dist[0, 0]);\n\n        int[] dr = { 0, 0, 1, -1 };\n        int[] dc = {\
        \ 1, -1, 0, 0 };\n\n        while (pq.Count > 0) {\n            if (pq.TryDequeue(out\
        \ (int r, int c) curr, out int d)) {\n                if (d > dist[curr.r, curr.c])\
        \ continue;\n                if (curr.r == m - 1 && curr.c == n - 1) break;\n\
        \n                for (int i = 0; i < 4; i++) {\n                    int nr\
        \ = curr.r + dr[i];\n                    int nc = curr.c + dc[i];\n\n      \
        \              if (nr >= 0 && nr < m && nc >= 0 && nc < n) {\n             \
        \           int weight = grid[nr][nc];\n                        if (dist[curr.r,\
        \ curr.c] + weight < dist[nr, nc]) {\n                            dist[nr, nc]\
        \ = dist[curr.r, curr.c] + weight;\n                            pq.Enqueue((nr,\
        \ nc), dist[nr, nc]);\n                        }\n                    }\n  \
        \              }\n            }\n        }\n\n        return dist[m - 1, n -\
        \ 1] < health;\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @param {number} health\n * @return\
        \ {boolean}\n */\nvar findSafeWalk = function(grid, health) {\n    const m =\
        \ grid.length;\n    const n = grid[0].length;\n    const dist = Array.from({\
        \ length: m }, () => Array(n).fill(Infinity));\n    const deque = [[0, 0]];\n\
        \    dist[0][0] = grid[0][0];\n\n    const dr = [0, 0, 1, -1];\n    const dc\
        \ = [1, -1, 0, 0];\n\n    while (deque.length > 0) {\n        const [r, c] =\
        \ deque.shift();\n\n        for (let i = 0; i < 4; i++) {\n            const\
        \ nr = r + dr[i];\n            const nc = c + dc[i];\n\n            if (nr >=\
        \ 0 && nr < m && nc >= 0 && nc < n) {\n                const weight = grid[nr][nc];\n\
        \                if (dist[r][c] + weight < dist[nr][nc]) {\n               \
        \     dist[nr][nc] = dist[r][c] + weight;\n                    if (weight ===\
        \ 0) {\n                        deque.unshift([nr, nc]);\n                 \
        \   } else {\n                        deque.push([nr, nc]);\n              \
        \      }\n                }\n            }\n        }\n    }\n\n    return dist[m\
        \ - 1][n - 1] < health;\n};"
      typescript: "function findSafeWalk(grid: number[][], health: number): boolean\
        \ {\n    const m = grid.length;\n    const n = grid[0].length;\n    const dist:\
        \ number[][] = Array.from({ length: m }, () => Array(n).fill(Infinity));\n \
        \   const deque: [number, number][] = [[0, 0]];\n    dist[0][0] = grid[0][0];\n\
        \n    const dr = [0, 0, 1, -1];\n    const dc = [1, -1, 0, 0];\n\n    while\
        \ (deque.length > 0) {\n        const [r, c] = deque.shift()!;\n\n        for\
        \ (let i = 0; i < 4; i++) {\n            const nr = r + dr[i];\n           \
        \ const nc = c + dc[i];\n\n            if (nr >= 0 && nr < m && nc >= 0 && nc\
        \ < n) {\n                const weight = grid[nr][nc];\n                if (dist[r][c]\
        \ + weight < dist[nr][nc]) {\n                    dist[nr][nc] = dist[r][c]\
        \ + weight;\n                    if (weight === 0) {\n                     \
        \   deque.unshift([nr, nc]);\n                    } else {\n               \
        \         deque.push([nr, nc]);\n                    }\n                }\n\
        \            }\n        }\n    }\n\n    return dist[m - 1][n - 1] < health;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @param\
        \ Integer $health\n     * @return Boolean\n     */\n    function findSafeWalk($grid,\
        \ $health) {\n        $m = count($grid);\n        $n = count($grid[0]);\n  \
        \      $dist = array_fill(0, $m, array_fill(0, $n, 2147483647));\n        $pq\
        \ = new SplPriorityQueue();\n\n        $dist[0][0] = $grid[0][0];\n        $pq->insert([0,\
        \ 0], -$dist[0][0]);\n\n        $dr = [0, 0, 1, -1];\n        $dc = [1, -1,\
        \ 0, 0];\n\n        while (!$pq->isEmpty()) {\n            $curr = $pq->extract();\n\
        \            $r = $curr[0];\n            $c = $curr[1];\n\n            for ($i\
        \ = 0; $i < 4; $i++) {\n                $nr = $r + $dr[$i];\n              \
        \  $nc = $c + $dc[$i];\n\n                if ($nr >= 0 && $nr < $m && $nc >=\
        \ 0 && $nc < $n) {\n                    $newDist = $dist[$r][$c] + $grid[$nr][$nc];\n\
        \                    if ($newDist < $dist[$nr][$nc]) {\n                   \
        \     $dist[$nr][$nc] = $newDist;\n                        $pq->insert([$nr,\
        \ $nc], -$newDist);\n                    }\n                }\n            }\n\
        \        }\n\n        return $dist[$m - 1][$n - 1] < $health;\n    }\n}"
      swift: "class Solution {\n    func findSafeWalk(_ grid: [[Int]], _ health: Int)\
        \ -> Bool {\n        let m = grid.count\n        let n = grid[0].count\n   \
        \     var dist = Array(repeating: Array(repeating: Int.max, count: n), count:\
        \ m)\n\n        dist[0][0] = grid[0][0]\n        var queue: [(Int, Int)] = [(0,\
        \ 0)]\n\n        let dr = [0, 0, 1, -1]\n        let dc = [1, -1, 0, 0]\n  \
        \      var head = 0\n\n        while head < queue.count {\n            let (r,\
        \ c) = queue[head]\n            head += 1\n\n            for i in 0..<4 {\n\
        \                let nr = r + dr[i]\n                let nc = c + dc[i]\n\n\
        \                if nr >= 0 && nr < m && nc >= 0 && nc < n {\n             \
        \       let newDist = dist[r][c] + grid[nr][nc]\n                    if newDist\
        \ < dist[nr][nc] {\n                        dist[nr][nc] = newDist\n       \
        \                 queue.append((nr, nc))\n                    }\n          \
        \      }\n            }\n        }\n\n        return dist[m - 1][n - 1] < health\n\
        \    }\n}"
      kotlin: "import java.util.ArrayDeque\n\nclass Solution {\n    fun findSafeWalk(grid:\
        \ List<List<Int>>, health: Int): Boolean {\n        val m = grid.size\n    \
        \    val n = grid[0].size\n        val g = Array(m) { i -> grid[i].toIntArray()\
        \ }\n        val dist = Array(m) { IntArray(n) { 1000000 } }\n        val deque\
        \ = ArrayDeque<IntArray>()\n\n        dist[0][0] = g[0][0]\n        deque.addFirst(intArrayOf(0,\
        \ 0))\n\n        val dr = intArrayOf(0, 0, 1, -1)\n        val dc = intArrayOf(1,\
        \ -1, 0, 0)\n\n        while (deque.isNotEmpty()) {\n            val curr =\
        \ deque.removeFirst()\n            val r = curr[0]\n            val c = curr[1]\n\
        \n            for (i in 0 until 4) {\n                val nr = r + dr[i]\n \
        \               val nc = c + dc[i]\n\n                if (nr in 0 until m &&\
        \ nc in 0 until n) {\n                    val weight = g[nr][nc]\n         \
        \           if (dist[r][c] + weight < dist[nr][nc]) {\n                    \
        \    dist[nr][nc] = dist[r][c] + weight\n                        if (weight\
        \ == 0) {\n                            deque.addFirst(intArrayOf(nr, nc))\n\
        \                        } else {\n                            deque.addLast(intArrayOf(nr,\
        \ nc))\n                        }\n                    }\n                }\n\
        \            }\n        }\n\n        return dist[m - 1][n - 1] < health\n  \
        \  }\n}"
      dart: "import 'dart:collection';\n\nclass Solution {\n  bool findSafeWalk(List<List<int>>\
        \ grid, int health) {\n    int m = grid.length;\n    int n = grid[0].length;\n\
        \    List<List<int>> dist = List.generate(m, (_) => List.filled(n, 1000000));\n\
        \    ListQueue<List<int>> q = ListQueue<List<int>>();\n\n    dist[0][0] = grid[0][0];\n\
        \    q.addFirst([0, 0]);\n\n    List<int> dr = [0, 0, 1, -1];\n    List<int>\
        \ dc = [1, -1, 0, 0];\n\n    while (q.isNotEmpty) {\n      List<int> curr =\
        \ q.removeFirst();\n      int r = curr[0];\n      int c = curr[1];\n\n     \
        \ for (int i = 0; i < 4; i++) {\n        int nr = r + dr[i];\n        int nc\
        \ = c + dc[i];\n\n        if (nr >= 0 && nr < m && nc >= 0 && nc < n) {\n  \
        \        int weight = grid[nr][nc];\n          if (dist[r][c] + weight < dist[nr][nc])\
        \ {\n            dist[nr][nc] = dist[r][c] + weight;\n            if (weight\
        \ == 0) {\n              q.addFirst([nr, nc]);\n            } else {\n     \
        \         q.addLast([nr, nc]);\n            }\n          }\n        }\n    \
        \  }\n    }\n\n    return dist[m - 1][n - 1] < health;\n  }\n}"
      go: "import \"container/list\"\n\nfunc findSafeWalk(grid [][]int, health int)\
        \ bool {\n\tm, n := len(grid), len(grid[0])\n\tdist := make([][]int, m)\n\t\
        for i := range dist {\n\t\tdist[i] = make([]int, n)\n\t\tfor j := range dist[i]\
        \ {\n\t\t\tdist[i][j] = 1000000\n\t\t}\n\t}\n\n\tq := list.New()\n\tdist[0][0]\
        \ = grid[0][0]\n\tq.PushFront([2]int{0, 0})\n\n\tdr := []int{0, 0, 1, -1}\n\t\
        dc := []int{1, -1, 0, 0}\n\n\tfor q.Len() > 0 {\n\t\telem := q.Front()\n\t\t\
        curr := q.Remove(elem).([2]int)\n\t\tr, c := curr[0], curr[1]\n\n\t\tfor i :=\
        \ 0; i < 4; i++ {\n\t\t\tnr, nc := r+dr[i], c+dc[i]\n\t\t\tif nr >= 0 && nr\
        \ < m && nc >= 0 && nc < n {\n\t\t\t\tweight := grid[nr][nc]\n\t\t\t\tif dist[r][c]+weight\
        \ < dist[nr][nc] {\n\t\t\t\t\tdist[nr][nc] = dist[r][c] + weight\n\t\t\t\t\t\
        if weight == 0 {\n\t\t\t\t\t\tq.PushFront([2]int{nr, nc})\n\t\t\t\t\t} else\
        \ {\n\t\t\t\t\t\tq.PushBack([2]int{nr, nc})\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\
        }\n\t\t}\n\t}\n\n\treturn dist[m-1][n-1] < health\n}"
      ruby: "# @param {Integer[][]} grid\n# @param {Integer} health\n# @return {Boolean}\n\
        def find_safe_walk(grid, health)\n  m = grid.length\n  n = grid[0].length\n\
        \  dist = Array.new(m) { Array.new(n, 1000000) }\n\n  q = [[0, 0]]\n  dist[0][0]\
        \ = grid[0][0]\n\n  dr = [0, 0, 1, -1]\n  dc = [1, -1, 0, 0]\n\n  while !q.empty?\n\
        \    r, c = q.shift\n\n    4.times do |i|\n      nr, nc = r + dr[i], c + dc[i]\n\
        \n      if nr >= 0 && nr < m && nc >= 0 && nc < n\n        weight = grid[nr][nc]\n\
        \        if dist[r][c] + weight < dist[nr][nc]\n          dist[nr][nc] = dist[r][c]\
        \ + weight\n          if weight == 0\n            q.unshift([nr, nc])\n    \
        \      else\n            q.push([nr, nc])\n          end\n        end\n    \
        \  end\n    end\n  end\n\n  dist[m - 1][n - 1] < health\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n  def findSafeWalk(grid:\
        \ List[List[Int]], health: Int): Boolean = {\n    val m = grid.length\n    val\
        \ n = grid(0).length\n    val g = grid.map(_.toArray).toArray\n    val dist\
        \ = Array.fill(m, n)(1000000)\n    val dq = mutable.ArrayDeque[(Int, Int)]()\n\
        \n    dist(0)(0) = g(0)(0)\n    dq.append((0, 0))\n\n    val dr = Array(0, 0,\
        \ 1, -1)\n    val dc = Array(1, -1, 0, 0)\n\n    while (dq.nonEmpty) {\n   \
        \   val (r, c) = dq.removeFirst()\n\n      for (i <- 0 until 4) {\n        val\
        \ nr = r + dr(i)\n        val nc = c + dc(i)\n\n        if (nr >= 0 && nr <\
        \ m && nc >= 0 && nc < n) {\n          val weight = g(nr)(nc)\n          if\
        \ (dist(r)(c) + weight < dist(nr)(nc)) {\n            dist(nr)(nc) = dist(r)(c)\
        \ + weight\n            if (weight == 0) {\n              dq.prepend((nr, nc))\n\
        \            } else {\n              dq.append((nr, nc))\n            }\n  \
        \        }\n        }\n      }\n    }\n\n    dist(m - 1)(n - 1) < health\n \
        \ }\n}"
      rust: "use std::collections::VecDeque;\n\nimpl Solution {\n    pub fn find_safe_walk(grid:\
        \ Vec<Vec<i32>>, health: i32) -> bool {\n        let m = grid.len();\n     \
        \   let n = grid[0].len();\n        let mut dist = vec![vec![10000; n]; m];\n\
        \        let mut deque = VecDeque::new();\n\n        dist[0][0] = grid[0][0];\n\
        \        deque.push_back((0, 0));\n\n        let dx: [i32; 4] = [0, 0, 1, -1];\n\
        \        let dy: [i32; 4] = [1, -1, 0, 0];\n\n        while let Some((r, c))\
        \ = deque.pop_front() {\n            for i in 0..4 {\n                let nr\
        \ = r as i32 + dx[i];\n                let nc = c as i32 + dy[i];\n\n      \
        \          if nr >= 0 && nr < m as i32 && nc >= 0 && nc < n as i32 {\n     \
        \               let nr_u = nr as usize;\n                    let nc_u = nc as\
        \ usize;\n                    let new_dist = dist[r][c] + grid[nr_u][nc_u];\n\
        \                    if new_dist < dist[nr_u][nc_u] {\n                    \
        \    dist[nr_u][nc_u] = new_dist;\n                        if grid[nr_u][nc_u]\
        \ == 0 {\n                            deque.push_front((nr_u, nc_u));\n    \
        \                    } else {\n                            deque.push_back((nr_u,\
        \ nc_u));\n                        }\n                    }\n              \
        \  }\n            }\n        }\n\n        health - dist[m - 1][n - 1] >= 1\n\
        \    }\n}"
      racket: "(define/contract (find-safe-walk grid health)\n  (-> (listof (listof\
        \ exact-integer?)) exact-integer? boolean?)\n  (let* ([m (length grid)]\n  \
        \       [n (length (car grid))]\n         [grid-vec (list->vector (map list->vector\
        \ grid))]\n         [max-h (make-vector m)])\n    (for ([i (in-range m)])\n\
        \      (vector-set! max-h i (make-vector n -1)))\n    (let ([start-h (- health\
        \ (vector-ref (vector-ref grid-vec 0) 0))])\n      (if (< start-h 1)\n     \
        \     #f\n          (begin\n            (vector-set! (vector-ref max-h 0) 0\
        \ start-h)\n            (let loop ([q (list (list 0 0 start-h))])\n        \
        \      (if (null? q)\n                  (let ([final-h (vector-ref (vector-ref\
        \ max-h (- m 1)) (- n 1))])\n                    (>= final-h 1))\n         \
        \         (let ([next-q (for/fold ([acc '()])\n                            \
        \              ([curr q])\n                                  (let ([r (car curr)]\n\
        \                                        [c (second curr)]\n               \
        \                         [h (third curr)])\n                              \
        \      (if (< h (vector-ref (vector-ref max-h r) c))\n                     \
        \                   acc\n                                        (for/fold ([inner-acc\
        \ acc])\n                                                  ([d '((0 1) (0 -1)\
        \ (1 0) (-1 0))])\n                                          (let* ([nr (+ r\
        \ (car d))]\n                                                 [nc (+ c (second\
        \ d))])\n                                            (if (and (>= nr 0) (< nr\
        \ m) (>= nc 0) (< nc n))\n                                                (let*\
        \ ([nh (- h (vector-ref (vector-ref grid-vec nr) nc))])\n                  \
        \                                (if (and (>= nh 1) (> nh (vector-ref (vector-ref\
        \ max-h nr) nc)))\n                                                      (begin\n\
        \                                                        (vector-set! (vector-ref\
        \ max-h nr) nc nh)\n                                                       \
        \ (cons (list nr nc nh) inner-acc))\n                                      \
        \                inner-acc))\n                                             \
        \   inner-acc))))))])\n                    (loop next-q)))))))))"
      erlang: "-spec find_safe_walk(Grid :: [[integer()]], Health :: integer()) -> boolean().\n\
        find_safe_walk(Grid, Health) ->\n  M = length(Grid),\n  N = length(hd(Grid)),\n\
        \  GridTuple = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),\n  StartCost\
        \ = element(1, element(1, GridTuple)),\n  Dist = maps:put({0, 0}, StartCost,\
        \ #{}),\n  PQ = gb_sets:add_element({StartCost, 0, 0}, gb_sets:empty()),\n \
        \ dijkstra(PQ, Dist, GridTuple, M, N, Health).\n\ndijkstra(PQ, Dist, GridTuple,\
        \ M, N, Health) ->\n  case gb_sets:is_empty(PQ) of\n    true -> false;\n   \
        \ false ->\n      {{D, R, C}, PQ2} = gb_sets:take_smallest(PQ),\n      CurrentD\
        \ = maps:get({R, C}, Dist, 1000000),\n      if\n        D > CurrentD -> dijkstra(PQ2,\
        \ Dist, GridTuple, M, N, Health);\n        true ->\n          if\n         \
        \   R == M - 1, C == N - 1 -> Health - D >= 1;\n            true ->\n      \
        \        Neighbors = [{R+1, C}, {R-1, C}, {R, C+1}, {R, C-1}],\n           \
        \   {NewPQ, NewDist} = lists:foldl(\n                fun({NR, NC}, {AccPQ, AccDist})\
        \ ->\n                  if\n                    NR >= 0, NR < M, NC >= 0, NC\
        \ < N ->\n                      Cost = element(NC + 1, element(NR + 1, GridTuple)),\n\
        \                      ND = D + Cost,\n                      OldD = maps:get({NR,\
        \ NC}, AccDist, 1000000),\n                      if\n                      \
        \  ND < OldD -> {gb_sets:add_element({ND, NR, NC}, AccPQ), maps:put({NR, NC},\
        \ ND, AccDist)};\n                        true -> {AccPQ, AccDist}\n       \
        \               end;\n                    true -> {AccPQ, AccDist}\n       \
        \           end\n                end, {PQ2, Dist}, Neighbors),\n           \
        \   dijkstra(NewPQ, NewDist, GridTuple, M, N, Health)\n          end\n     \
        \ end\n  end."
      elixir: "defmodule Solution do\n  @spec find_safe_walk(grid :: [[integer]], health\
        \ :: integer) :: boolean\n  def find_safe_walk(grid, health) do\n    m = length(grid)\n\
        \    n = length(hd(grid))\n    grid_map = for {row, r} <- Enum.with_index(grid),\n\
        \                   {val, c} <- Enum.with_index(row),\n                   into:\
        \ %{}, do: {{r, c}, val}\n\n    start_cost = grid_map[{0, 0}]\n    pq = :gb_sets.add_element({start_cost,\
        \ 0, 0}, :gb_sets.empty())\n    dist = %{{0, 0} => start_cost}\n\n    dijkstra(pq,\
        \ dist, grid_map, m, n, health)\n  end\n\n  defp dijkstra(pq, dist, grid_map,\
        \ m, n, health) do\n    case :gb_sets.is_empty(pq) do\n      true -> false\n\
        \      false ->\n        {{d, r, c}, pq2} = :gb_sets.take_smallest(pq)\n   \
        \     current_d = Map.get(dist, {r, c}, 1_000_000)\n        cond do\n      \
        \    d > current_d ->\n            dijkstra(pq2, dist, grid_map, m, n, health)\n\
        \          r == m - 1 and c == n - 1 ->\n            health - d >= 1\n     \
        \     true ->\n            neighbors = [{r + 1, c}, {r - 1, c}, {r, c + 1},\
        \ {r, c - 1}]\n            {new_pq, new_dist} = Enum.reduce(neighbors, {pq2,\
        \ dist}, fn {nr, nc}, {acc_pq, acc_dist} ->\n              if nr >= 0 and nr\
        \ < m and nc >= 0 and nc < n do\n                nd = d + grid_map[{nr, nc}]\n\
        \                if nd < Map.get(acc_dist, {nr, nc}, 1_000_000) do\n       \
        \           {:gb_sets.add_element({nd, nr, nc}, acc_pq), Map.put(acc_dist, {nr,\
        \ nc}, nd)}\n                else\n                  {acc_pq, acc_dist}\n  \
        \              end\n              else\n                {acc_pq, acc_dist}\n\
        \              end\n            end)\n            dijkstra(new_pq, new_dist,\
        \ grid_map, m, n, health)\n        end\n    end\n  end\nend"
    approach: The problem asks whether we can navigate from the top-left to the bottom-right
      of a grid while keeping our health positive, where passing through a cell with
      a value of 1 reduces health by 1. This can be modeled as a shortest path problem
      on a graph where each cell (i, j) has an entry weight equal to grid[i][j]. The
      goal is to find a path such that the sum of weights from the starting cell (0,
      0) to the target cell (m-1, n-1) is strictly less than the initial health value,
      ensuring at least one health point remains.
    time_complexity: O(M * N) where M is the number of rows and N is the number of columns.
      This is achieved using 0-1 Breadth-First Search, where each cell is added and
      removed from the deque at most twice (and processed only once), and each edge
      is explored once.
    space_complexity: O(M * N) to store the distance matrix that keeps track of the
      minimum health reduction for each cell and to maintain the double-ended queue
      for the search process.
    elapsed_time: 1142.6642796993256
    model: gemini-3-flash-preview
    generated_at: '2026-07-02 02:54:10 '
---

## Problem #3286: Find a Safe Walk Through a Grid

**Difficulty:** Medium

**Topics:** Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path

## Problem Description

<p>You are given an <code>m x n</code> binary matrix <code>grid</code> and an integer <code>health</code>.</p>

<p>You start on the upper-left corner <code>(0, 0)</code> and would like to get to the lower-right corner <code>(m - 1, n - 1)</code>.</p>

<p>You can move up, down, left, or right from one cell to another adjacent cell as long as your health <em>remains</em> <strong>positive</strong>.</p>

<p>Cells <code>(i, j)</code> with <code>grid[i][j] = 1</code> are considered <strong>unsafe</strong> and reduce your health by 1.</p>

<p>Return <code>true</code> if you can reach the final cell with a health value of 1 or more, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>The final cell can be reached safely by walking along the gray cells below.</p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/08/04/3868_examples_1drawio.png" style="width: 301px; height: 121px;" /></div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>A minimum of 4 health points is needed to reach the final cell safely.</p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/08/04/3868_examples_2drawio.png" style="width: 361px; height: 161px;" /></div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>The final cell can be reached safely by walking along the gray cells below.</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/08/04/3868_examples_3drawio.png" style="width: 181px; height: 121px;" /></p>

<p>Any path that does not go through the cell <code>(1, 1)</code> is unsafe since your health will drop to 0 when reaching the final cell.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code><font face="monospace">2 &lt;= m * n</font></code></li>
	<li><code>1 &lt;= health &lt;= m + n</code></li>
	<li><code>grid[i][j]</code> is either 0 or 1.</li>
</ul>


## Hints

1. Use 01 BFS.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks whether we can navigate from the top-left to the bottom-right of a grid while keeping our health positive, where passing through a cell with a value of 1 reduces health by 1. This can be modeled as a shortest path problem on a graph where each cell (i, j) has an entry weight equal to grid[i][j]. The goal is to find a path such that the sum of weights from the starting cell (0, 0) to the target cell (m-1, n-1) is strictly less than the initial health value, ensuring at least one health point remains.

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
#include <deque>
#include <climits>

using namespace std;

class Solution {
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> dist(m, vector<int>(n, INT_MAX));

        deque<pair<int, int>> dq;
        dist[0][0] = grid[0][0];
        dq.push_back({0, 0});

        int dr[] = {0, 0, 1, -1};
        int dc[] = {1, -1, 0, 0};

        while (!dq.empty()) {
            pair<int, int> curr = dq.front();
            dq.pop_front();
            int r = curr.first;
            int c = curr.second;

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int weight = grid[nr][nc];
                    if (dist[r][c] + weight < dist[nr][nc]) {
                        dist[nr][nc] = dist[r][c] + weight;
                        if (weight == 0) {
                            dq.push_front({nr, nc});
                        } else {
                            dq.push_back({nr, nc});
                        }
                    }
                }
            }
        }

        return dist[m - 1][n - 1] < health;
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
    public boolean findSafeWalk(List<List<Integer>> grid, int health) {
        int m = grid.size();
        int n = grid.get(0).size();
        int[][] dist = new int[m][n];
        for (int i = 0; i < m; i++) {
            Arrays.fill(dist[i], Integer.MAX_VALUE);
        }

        Deque<int[]> dq = new ArrayDeque<>();
        dist[0][0] = grid.get(0).get(0);
        dq.addFirst(new int[]{0, 0});

        int[] dr = {0, 0, 1, -1};
        int[] dc = {1, -1, 0, 0};

        while (!dq.isEmpty()) {
            int[] curr = dq.pollFirst();
            int r = curr[0];
            int c = curr[1];

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int weight = grid.get(nr).get(nc);
                    if (dist[r][c] + weight < dist[nr][nc]) {
                        dist[nr][nc] = dist[r][c] + weight;
                        if (weight == 0) {
                            dq.addFirst(new int[]{nr, nc});
                        } else {
                            dq.addLast(new int[]{nr, nc});
                        }
                    }
                }
            }
        }

        return dist[m - 1][n - 1] < health;
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
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]

        dist[0][0] = grid[0][0]
        dq = collections.deque([(0, 0)])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while dq:
            r, c = dq.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    weight = grid[nr][nc]
                    if dist[r][c] + weight < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + weight
                        if weight == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))

        return dist[m - 1][n - 1] < health
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List
import collections

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]

        dist[0][0] = grid[0][0]
        dq = collections.deque([(0, 0)])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while dq:
            r, c = dq.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    weight = grid[nr][nc]
                    if dist[r][c] + weight < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + weight
                        if weight == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))

        return dist[m - 1][n - 1] < health
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <stdlib.h>

bool findSafeWalk(int** grid, int gridSize, int* gridColSize, int health) {
    int m = gridSize;
    int n = gridColSize[0];
    int dist[50][50];
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            dist[i][j] = 1000000;
        }
    }

    int dq[10000][2];
    int head = 5000, tail = 5000;

    dist[0][0] = grid[0][0];
    dq[tail][0] = 0;
    dq[tail][1] = 0;
    tail++;

    int dr[] = {0, 0, 1, -1};
    int dc[] = {1, -1, 0, 0};

    while (head < tail) {
        int r = dq[head][0];
        int c = dq[head][1];
        head++;

        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                int weight = grid[nr][nc];
                if (dist[r][c] + weight < dist[nr][nc]) {
                    dist[nr][nc] = dist[r][c] + weight;
                    if (weight == 0) {
                        head--;
                        dq[head][0] = nr;
                        dq[head][1] = nc;
                    } else {
                        dq[tail][0] = nr;
                        dq[tail][1] = nc;
                        tail++;
                    }
                }
            }
        }
    }

    return dist[m - 1][n - 1] < health;
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
    public bool FindSafeWalk(IList<IList<int>> grid, int health) {
        int m = grid.Count;
        int n = grid[0].Count;
        int[,] dist = new int[m, n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dist[i, j] = int.MaxValue;
            }
        }

        PriorityQueue<(int r, int c), int> pq = new PriorityQueue<(int, int), int>();
        dist[0, 0] = grid[0][0];
        pq.Enqueue((0, 0), dist[0, 0]);

        int[] dr = { 0, 0, 1, -1 };
        int[] dc = { 1, -1, 0, 0 };

        while (pq.Count > 0) {
            if (pq.TryDequeue(out (int r, int c) curr, out int d)) {
                if (d > dist[curr.r, curr.c]) continue;
                if (curr.r == m - 1 && curr.c == n - 1) break;

                for (int i = 0; i < 4; i++) {
                    int nr = curr.r + dr[i];
                    int nc = curr.c + dc[i];

                    if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                        int weight = grid[nr][nc];
                        if (dist[curr.r, curr.c] + weight < dist[nr, nc]) {
                            dist[nr, nc] = dist[curr.r, curr.c] + weight;
                            pq.Enqueue((nr, nc), dist[nr, nc]);
                        }
                    }
                }
            }
        }

        return dist[m - 1, n - 1] < health;
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
 * @param {number} health
 * @return {boolean}
 */
var findSafeWalk = function(grid, health) {
    const m = grid.length;
    const n = grid[0].length;
    const dist = Array.from({ length: m }, () => Array(n).fill(Infinity));
    const deque = [[0, 0]];
    dist[0][0] = grid[0][0];

    const dr = [0, 0, 1, -1];
    const dc = [1, -1, 0, 0];

    while (deque.length > 0) {
        const [r, c] = deque.shift();

        for (let i = 0; i < 4; i++) {
            const nr = r + dr[i];
            const nc = c + dc[i];

            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                const weight = grid[nr][nc];
                if (dist[r][c] + weight < dist[nr][nc]) {
                    dist[nr][nc] = dist[r][c] + weight;
                    if (weight === 0) {
                        deque.unshift([nr, nc]);
                    } else {
                        deque.push([nr, nc]);
                    }
                }
            }
        }
    }

    return dist[m - 1][n - 1] < health;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findSafeWalk(grid: number[][], health: number): boolean {
    const m = grid.length;
    const n = grid[0].length;
    const dist: number[][] = Array.from({ length: m }, () => Array(n).fill(Infinity));
    const deque: [number, number][] = [[0, 0]];
    dist[0][0] = grid[0][0];

    const dr = [0, 0, 1, -1];
    const dc = [1, -1, 0, 0];

    while (deque.length > 0) {
        const [r, c] = deque.shift()!;

        for (let i = 0; i < 4; i++) {
            const nr = r + dr[i];
            const nc = c + dc[i];

            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                const weight = grid[nr][nc];
                if (dist[r][c] + weight < dist[nr][nc]) {
                    dist[nr][nc] = dist[r][c] + weight;
                    if (weight === 0) {
                        deque.unshift([nr, nc]);
                    } else {
                        deque.push([nr, nc]);
                    }
                }
            }
        }
    }

    return dist[m - 1][n - 1] < health;
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
     * @param Integer $health
     * @return Boolean
     */
    function findSafeWalk($grid, $health) {
        $m = count($grid);
        $n = count($grid[0]);
        $dist = array_fill(0, $m, array_fill(0, $n, 2147483647));
        $pq = new SplPriorityQueue();

        $dist[0][0] = $grid[0][0];
        $pq->insert([0, 0], -$dist[0][0]);

        $dr = [0, 0, 1, -1];
        $dc = [1, -1, 0, 0];

        while (!$pq->isEmpty()) {
            $curr = $pq->extract();
            $r = $curr[0];
            $c = $curr[1];

            for ($i = 0; $i < 4; $i++) {
                $nr = $r + $dr[$i];
                $nc = $c + $dc[$i];

                if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n) {
                    $newDist = $dist[$r][$c] + $grid[$nr][$nc];
                    if ($newDist < $dist[$nr][$nc]) {
                        $dist[$nr][$nc] = $newDist;
                        $pq->insert([$nr, $nc], -$newDist);
                    }
                }
            }
        }

        return $dist[$m - 1][$n - 1] < $health;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func findSafeWalk(_ grid: [[Int]], _ health: Int) -> Bool {
        let m = grid.count
        let n = grid[0].count
        var dist = Array(repeating: Array(repeating: Int.max, count: n), count: m)

        dist[0][0] = grid[0][0]
        var queue: [(Int, Int)] = [(0, 0)]

        let dr = [0, 0, 1, -1]
        let dc = [1, -1, 0, 0]
        var head = 0

        while head < queue.count {
            let (r, c) = queue[head]
            head += 1

            for i in 0..<4 {
                let nr = r + dr[i]
                let nc = c + dc[i]

                if nr >= 0 && nr < m && nc >= 0 && nc < n {
                    let newDist = dist[r][c] + grid[nr][nc]
                    if newDist < dist[nr][nc] {
                        dist[nr][nc] = newDist
                        queue.append((nr, nc))
                    }
                }
            }
        }

        return dist[m - 1][n - 1] < health
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
    fun findSafeWalk(grid: List<List<Int>>, health: Int): Boolean {
        val m = grid.size
        val n = grid[0].size
        val g = Array(m) { i -> grid[i].toIntArray() }
        val dist = Array(m) { IntArray(n) { 1000000 } }
        val deque = ArrayDeque<IntArray>()

        dist[0][0] = g[0][0]
        deque.addFirst(intArrayOf(0, 0))

        val dr = intArrayOf(0, 0, 1, -1)
        val dc = intArrayOf(1, -1, 0, 0)

        while (deque.isNotEmpty()) {
            val curr = deque.removeFirst()
            val r = curr[0]
            val c = curr[1]

            for (i in 0 until 4) {
                val nr = r + dr[i]
                val nc = c + dc[i]

                if (nr in 0 until m && nc in 0 until n) {
                    val weight = g[nr][nc]
                    if (dist[r][c] + weight < dist[nr][nc]) {
                        dist[nr][nc] = dist[r][c] + weight
                        if (weight == 0) {
                            deque.addFirst(intArrayOf(nr, nc))
                        } else {
                            deque.addLast(intArrayOf(nr, nc))
                        }
                    }
                }
            }
        }

        return dist[m - 1][n - 1] < health
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
  bool findSafeWalk(List<List<int>> grid, int health) {
    int m = grid.length;
    int n = grid[0].length;
    List<List<int>> dist = List.generate(m, (_) => List.filled(n, 1000000));
    ListQueue<List<int>> q = ListQueue<List<int>>();

    dist[0][0] = grid[0][0];
    q.addFirst([0, 0]);

    List<int> dr = [0, 0, 1, -1];
    List<int> dc = [1, -1, 0, 0];

    while (q.isNotEmpty) {
      List<int> curr = q.removeFirst();
      int r = curr[0];
      int c = curr[1];

      for (int i = 0; i < 4; i++) {
        int nr = r + dr[i];
        int nc = c + dc[i];

        if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
          int weight = grid[nr][nc];
          if (dist[r][c] + weight < dist[nr][nc]) {
            dist[nr][nc] = dist[r][c] + weight;
            if (weight == 0) {
              q.addFirst([nr, nc]);
            } else {
              q.addLast([nr, nc]);
            }
          }
        }
      }
    }

    return dist[m - 1][n - 1] < health;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "container/list"

func findSafeWalk(grid [][]int, health int) bool {
	m, n := len(grid), len(grid[0])
	dist := make([][]int, m)
	for i := range dist {
		dist[i] = make([]int, n)
		for j := range dist[i] {
			dist[i][j] = 1000000
		}
	}

	q := list.New()
	dist[0][0] = grid[0][0]
	q.PushFront([2]int{0, 0})

	dr := []int{0, 0, 1, -1}
	dc := []int{1, -1, 0, 0}

	for q.Len() > 0 {
		elem := q.Front()
		curr := q.Remove(elem).([2]int)
		r, c := curr[0], curr[1]

		for i := 0; i < 4; i++ {
			nr, nc := r+dr[i], c+dc[i]
			if nr >= 0 && nr < m && nc >= 0 && nc < n {
				weight := grid[nr][nc]
				if dist[r][c]+weight < dist[nr][nc] {
					dist[nr][nc] = dist[r][c] + weight
					if weight == 0 {
						q.PushFront([2]int{nr, nc})
					} else {
						q.PushBack([2]int{nr, nc})
					}
				}
			}
		}
	}

	return dist[m-1][n-1] < health
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[][]} grid
# @param {Integer} health
# @return {Boolean}
def find_safe_walk(grid, health)
  m = grid.length
  n = grid[0].length
  dist = Array.new(m) { Array.new(n, 1000000) }

  q = [[0, 0]]
  dist[0][0] = grid[0][0]

  dr = [0, 0, 1, -1]
  dc = [1, -1, 0, 0]

  while !q.empty?
    r, c = q.shift

    4.times do |i|
      nr, nc = r + dr[i], c + dc[i]

      if nr >= 0 && nr < m && nc >= 0 && nc < n
        weight = grid[nr][nc]
        if dist[r][c] + weight < dist[nr][nc]
          dist[nr][nc] = dist[r][c] + weight
          if weight == 0
            q.unshift([nr, nc])
          else
            q.push([nr, nc])
          end
        end
      end
    end
  end

  dist[m - 1][n - 1] < health
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
  def findSafeWalk(grid: List[List[Int]], health: Int): Boolean = {
    val m = grid.length
    val n = grid(0).length
    val g = grid.map(_.toArray).toArray
    val dist = Array.fill(m, n)(1000000)
    val dq = mutable.ArrayDeque[(Int, Int)]()

    dist(0)(0) = g(0)(0)
    dq.append((0, 0))

    val dr = Array(0, 0, 1, -1)
    val dc = Array(1, -1, 0, 0)

    while (dq.nonEmpty) {
      val (r, c) = dq.removeFirst()

      for (i <- 0 until 4) {
        val nr = r + dr(i)
        val nc = c + dc(i)

        if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
          val weight = g(nr)(nc)
          if (dist(r)(c) + weight < dist(nr)(nc)) {
            dist(nr)(nc) = dist(r)(c) + weight
            if (weight == 0) {
              dq.prepend((nr, nc))
            } else {
              dq.append((nr, nc))
            }
          }
        }
      }
    }

    dist(m - 1)(n - 1) < health
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::VecDeque;

impl Solution {
    pub fn find_safe_walk(grid: Vec<Vec<i32>>, health: i32) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        let mut dist = vec![vec![10000; n]; m];
        let mut deque = VecDeque::new();

        dist[0][0] = grid[0][0];
        deque.push_back((0, 0));

        let dx: [i32; 4] = [0, 0, 1, -1];
        let dy: [i32; 4] = [1, -1, 0, 0];

        while let Some((r, c)) = deque.pop_front() {
            for i in 0..4 {
                let nr = r as i32 + dx[i];
                let nc = c as i32 + dy[i];

                if nr >= 0 && nr < m as i32 && nc >= 0 && nc < n as i32 {
                    let nr_u = nr as usize;
                    let nc_u = nc as usize;
                    let new_dist = dist[r][c] + grid[nr_u][nc_u];
                    if new_dist < dist[nr_u][nc_u] {
                        dist[nr_u][nc_u] = new_dist;
                        if grid[nr_u][nc_u] == 0 {
                            deque.push_front((nr_u, nc_u));
                        } else {
                            deque.push_back((nr_u, nc_u));
                        }
                    }
                }
            }
        }

        health - dist[m - 1][n - 1] >= 1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (find-safe-walk grid health)
  (-> (listof (listof exact-integer?)) exact-integer? boolean?)
  (let* ([m (length grid)]
         [n (length (car grid))]
         [grid-vec (list->vector (map list->vector grid))]
         [max-h (make-vector m)])
    (for ([i (in-range m)])
      (vector-set! max-h i (make-vector n -1)))
    (let ([start-h (- health (vector-ref (vector-ref grid-vec 0) 0))])
      (if (< start-h 1)
          #f
          (begin
            (vector-set! (vector-ref max-h 0) 0 start-h)
            (let loop ([q (list (list 0 0 start-h))])
              (if (null? q)
                  (let ([final-h (vector-ref (vector-ref max-h (- m 1)) (- n 1))])
                    (>= final-h 1))
                  (let ([next-q (for/fold ([acc '()])
                                          ([curr q])
                                  (let ([r (car curr)]
                                        [c (second curr)]
                                        [h (third curr)])
                                    (if (< h (vector-ref (vector-ref max-h r) c))
                                        acc
                                        (for/fold ([inner-acc acc])
                                                  ([d '((0 1) (0 -1) (1 0) (-1 0))])
                                          (let* ([nr (+ r (car d))]
                                                 [nc (+ c (second d))])
                                            (if (and (>= nr 0) (< nr m) (>= nc 0) (< nc n))
                                                (let* ([nh (- h (vector-ref (vector-ref grid-vec nr) nc))])
                                                  (if (and (>= nh 1) (> nh (vector-ref (vector-ref max-h nr) nc)))
                                                      (begin
                                                        (vector-set! (vector-ref max-h nr) nc nh)
                                                        (cons (list nr nc nh) inner-acc))
                                                      inner-acc))
                                                inner-acc))))))])
                    (loop next-q)))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec find_safe_walk(Grid :: [[integer()]], Health :: integer()) -> boolean().
find_safe_walk(Grid, Health) ->
  M = length(Grid),
  N = length(hd(Grid)),
  GridTuple = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),
  StartCost = element(1, element(1, GridTuple)),
  Dist = maps:put({0, 0}, StartCost, #{}),
  PQ = gb_sets:add_element({StartCost, 0, 0}, gb_sets:empty()),
  dijkstra(PQ, Dist, GridTuple, M, N, Health).

dijkstra(PQ, Dist, GridTuple, M, N, Health) ->
  case gb_sets:is_empty(PQ) of
    true -> false;
    false ->
      {{D, R, C}, PQ2} = gb_sets:take_smallest(PQ),
      CurrentD = maps:get({R, C}, Dist, 1000000),
      if
        D > CurrentD -> dijkstra(PQ2, Dist, GridTuple, M, N, Health);
        true ->
          if
            R == M - 1, C == N - 1 -> Health - D >= 1;
            true ->
              Neighbors = [{R+1, C}, {R-1, C}, {R, C+1}, {R, C-1}],
              {NewPQ, NewDist} = lists:foldl(
                fun({NR, NC}, {AccPQ, AccDist}) ->
                  if
                    NR >= 0, NR < M, NC >= 0, NC < N ->
                      Cost = element(NC + 1, element(NR + 1, GridTuple)),
                      ND = D + Cost,
                      OldD = maps:get({NR, NC}, AccDist, 1000000),
                      if
                        ND < OldD -> {gb_sets:add_element({ND, NR, NC}, AccPQ), maps:put({NR, NC}, ND, AccDist)};
                        true -> {AccPQ, AccDist}
                      end;
                    true -> {AccPQ, AccDist}
                  end
                end, {PQ2, Dist}, Neighbors),
              dijkstra(NewPQ, NewDist, GridTuple, M, N, Health)
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
  @spec find_safe_walk(grid :: [[integer]], health :: integer) :: boolean
  def find_safe_walk(grid, health) do
    m = length(grid)
    n = length(hd(grid))
    grid_map = for {row, r} <- Enum.with_index(grid),
                   {val, c} <- Enum.with_index(row),
                   into: %{}, do: {{r, c}, val}

    start_cost = grid_map[{0, 0}]
    pq = :gb_sets.add_element({start_cost, 0, 0}, :gb_sets.empty())
    dist = %{{0, 0} => start_cost}

    dijkstra(pq, dist, grid_map, m, n, health)
  end

  defp dijkstra(pq, dist, grid_map, m, n, health) do
    case :gb_sets.is_empty(pq) do
      true -> false
      false ->
        {{d, r, c}, pq2} = :gb_sets.take_smallest(pq)
        current_d = Map.get(dist, {r, c}, 1_000_000)
        cond do
          d > current_d ->
            dijkstra(pq2, dist, grid_map, m, n, health)
          r == m - 1 and c == n - 1 ->
            health - d >= 1
          true ->
            neighbors = [{r + 1, c}, {r - 1, c}, {r, c + 1}, {r, c - 1}]
            {new_pq, new_dist} = Enum.reduce(neighbors, {pq2, dist}, fn {nr, nc}, {acc_pq, acc_dist} ->
              if nr >= 0 and nr < m and nc >= 0 and nc < n do
                nd = d + grid_map[{nr, nc}]
                if nd < Map.get(acc_dist, {nr, nc}, 1_000_000) do
                  {:gb_sets.add_element({nd, nr, nc}, acc_pq), Map.put(acc_dist, {nr, nc}, nd)}
                else
                  {acc_pq, acc_dist}
                end
              else
                {acc_pq, acc_dist}
              end
            end)
            dijkstra(new_pq, new_dist, grid_map, m, n, health)
        end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(M * N) where M is the number of rows and N is the number of columns. This is achieved using 0-1 Breadth-First Search, where each cell is added and removed from the deque at most twice (and processed only once), and each edge is explored once.
- **Space Complexity:** O(M * N) to store the distance matrix that keeps track of the minimum health reduction for each cell and to maintain the double-ended queue for the search process.
