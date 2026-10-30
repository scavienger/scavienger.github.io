---
layout: post
title: "Shortest Path With At Most K Consecutive Identical Characters"
date: 2026-10-30 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Graph Theory", "Heap (Priority Queue)", "Shortest Path"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    struct State {\n        int d, u, c;\n  \
        \      bool operator<(const State& other) const {\n            return d > other.d;\n\
        \        }\n    };\n\n    int shortestPath(int n, vector<vector<int>>& edges,\
        \ string labels, int k) {\n        vector<vector<pair<int, int>>> adj(n);\n\
        \        for (const auto& edge : edges) {\n            adj[edge[0]].push_back({edge[1],\
        \ edge[2]});\n        }\n\n        int max_c = k + 1;\n        vector<vector<int>>\
        \ dist(n, vector<int>(max_c, 1e9 + 7));\n        priority_queue<State> pq;\n\
        \n        dist[0][1] = 0;\n        pq.push({0, 0, 1});\n\n        while (!pq.empty())\
        \ {\n            State top = pq.top();\n            pq.pop();\n            int\
        \ d = top.d, u = top.u, c = top.c;\n\n            if (d > dist[u][c]) continue;\n\
        \            if (u == n - 1) return d;\n\n            char label_u = labels[u];\n\
        \            for (auto& edge : adj[u]) {\n                int v = edge.first;\n\
        \                int w = edge.second;\n                int nc = (label_u ==\
        \ labels[v]) ? c + 1 : 1;\n\n                if (nc <= k && d + w < dist[v][nc])\
        \ {\n                    dist[v][nc] = d + w;\n                    pq.push({dist[v][nc],\
        \ v, nc});\n                }\n            }\n        }\n\n        return -1;\n\
        \    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    static class State implements\
        \ Comparable<State> {\n        int d, u, c;\n        State(int d, int u, int\
        \ c) {\n            this.d = d;\n            this.u = u;\n            this.c\
        \ = c;\n        }\n        public int compareTo(State other) {\n           \
        \ return Integer.compare(this.d, other.d);\n        }\n    }\n\n    public int\
        \ shortestPath(int n, int[][] edges, String labels, int k) {\n        List<int[]>[]\
        \ adj = new ArrayList[n];\n        for (int i = 0; i < n; i++) adj[i] = new\
        \ ArrayList<>();\n        for (int[] e : edges) {\n            adj[e[0]].add(new\
        \ int[]{e[1], e[2]});\n        }\n\n        int[][] dist = new int[n][k + 1];\n\
        \        for (int i = 0; i < n; i++) Arrays.fill(dist[i], Integer.MAX_VALUE);\n\
        \n        PriorityQueue<State> pq = new PriorityQueue<>();\n        dist[0][1]\
        \ = 0;\n        pq.offer(new State(0, 0, 1));\n\n        while (!pq.isEmpty())\
        \ {\n            State top = pq.poll();\n            int d = top.d, u = top.u,\
        \ c = top.c;\n\n            if (d > dist[u][c]) continue;\n            if (u\
        \ == n - 1) return d;\n\n            char labelU = labels.charAt(u);\n     \
        \       for (int[] edge : adj[u]) {\n                int v = edge[0];\n    \
        \            int w = edge[1];\n                int nc = (labelU == labels.charAt(v))\
        \ ? c + 1 : 1;\n\n                if (nc <= k && d != Integer.MAX_VALUE && d\
        \ + w < dist[v][nc]) {\n                    dist[v][nc] = d + w;\n         \
        \           pq.offer(new State(dist[v][nc], v, nc));\n                }\n  \
        \          }\n        }\n\n        return -1;\n    }\n}"
      python: "import heapq\n\nclass Solution(object):\n    def shortestPath(self, n,\
        \ edges, labels, k):\n        \"\"\"\n        :type n: int\n        :type edges:\
        \ List[List[int]]\n        :type labels: str\n        :type k: int\n       \
        \ :rtype: int\n        \"\"\"\n        adj = [[] for _ in range(n)]\n      \
        \  for u, v, w in edges:\n            adj[u].append((v, w))\n\n        max_c\
        \ = k + 1\n        dist = [float('inf')] * (n * max_c)\n\n        dist[0 * max_c\
        \ + 1] = 0\n        pq = [(0, 0, 1)] # (distance, node, count)\n\n        while\
        \ pq:\n            d, u, c = heapq.heappop(pq)\n\n            if d > dist[u\
        \ * max_c + c]:\n                continue\n            if u == n - 1:\n    \
        \            return d\n\n            label_u = labels[u]\n            for v,\
        \ w in adj[u]:\n                nc = c + 1 if label_u == labels[v] else 1\n\
        \                if nc <= k:\n                    idx = v * max_c + nc\n   \
        \                 if d + w < dist[idx]:\n                        dist[idx] =\
        \ d + w\n                        heapq.heappush(pq, (d + w, v, nc))\n      \
        \  return -1"
      python3: "import heapq\n\nclass Solution:\n    def shortestPath(self, n: int,\
        \ edges: List[List[int]], labels: str, k: int) -> int: \n        adj = [[] for\
        \ _ in range(n)]\n        for u, v, w in edges:\n            adj[u].append((v,\
        \ w))\n\n        max_c = k + 1\n        dist = [float('inf')] * (n * max_c)\n\
        \n        dist[0 * max_c + 1] = 0\n        pq = [(0, 0, 1)] # (distance, node,\
        \ count)\n\n        while pq:\n            d, u, c = heapq.heappop(pq)\n\n \
        \           if d > dist[u * max_c + c]:\n                continue\n        \
        \    if u == n - 1:\n                return d\n\n            label_u = labels[u]\n\
        \            for v, w in adj[u]:\n                nc = c + 1 if label_u == labels[v]\
        \ else 1\n                if nc <= k:\n                    idx = v * max_c +\
        \ nc\n                    if d + w < dist[idx]:\n                        dist[idx]\
        \ = d + w\n                        heapq.heappush(pq, (d + w, v, nc))\n\n  \
        \      return -1"
      c: "#include <stdlib.h>\n#include <string.h>\n#include <limits.h>\n\ntypedef struct\
        \ {\n    int d, u, c;\n} State;\n\ntypedef struct {\n    int to, weight, next;\n\
        } Edge;\n\nvoid push(State* heap, int* heapSize, int d, int u, int c) {\n  \
        \  int i = ++(*heapSize);\n    while (i > 1 && d < heap[i / 2].d) {\n      \
        \  heap[i] = heap[i / 2];\n        i /= 2;\n    }\n    heap[i].d = d;\n    heap[i].u\
        \ = u;\n    heap[i].c = c;\n}\n\nState pop(State* heap, int* heapSize) {\n \
        \   State res = heap[1];\n    State last = heap[(*heapSize)--];\n    int i =\
        \ 1, child;\n    while (i * 2 <= *heapSize) {\n        child = i * 2;\n    \
        \    if (child < *heapSize && heap[child + 1].d < heap[child].d) child++;\n\
        \        if (last.d <= heap[child].d) break;\n        heap[i] = heap[child];\n\
        \        i = child;\n    }\n    heap[i] = last;\n    return res;\n}\n\nint shortestPath(int\
        \ n, int** edges, int edgesSize, int* edgesColSize, char* labels, int k) {\n\
        \    Edge* e = (Edge*)malloc(sizeof(Edge) * edgesSize);\n    int* head = (int*)malloc(sizeof(int)\
        \ * n);\n    for (int i = 0; i < n; i++) head[i] = -1;\n    for (int i = 0;\
        \ i < edgesSize; i++) {\n        int u = edges[i][0];\n        e[i].to = edges[i][1];\n\
        \        e[i].weight = edges[i][2];\n        e[i].next = head[u];\n        head[u]\
        \ = i;\n    }\n\n    int max_c = k + 1;\n    int* dist = (int*)malloc(sizeof(int)\
        \ * n * max_c);\n    for (int i = 0; i < n * max_c; i++) dist[i] = INT_MAX;\n\
        \n    State* heap = (State*)malloc(sizeof(State) * (edgesSize * k + 100));\n\
        \    int heapSize = 0;\n\n    dist[0 * max_c + 1] = 0;\n    push(heap, &heapSize,\
        \ 0, 0, 1);\n\n    while (heapSize > 0) {\n        State top = pop(heap, &heapSize);\n\
        \        int d = top.d, u = top.u, c = top.c;\n\n        if (d > dist[u * max_c\
        \ + c]) continue;\n        if (u == n - 1) {\n            free(e); free(head);\
        \ free(dist); free(heap);\n            return d;\n        }\n\n        for (int\
        \ i = head[u]; i != -1; i = e[i].next) {\n            int v = e[i].to;\n   \
        \         int w = e[i].weight;\n            int nc = (labels[u] == labels[v])\
        \ ? c + 1 : 1;\n            if (nc <= k) {\n                if (d + w < dist[v\
        \ * max_c + nc]) {\n                    dist[v * max_c + nc] = d + w;\n    \
        \                push(heap, &heapSize, d + w, v, nc);\n                }\n \
        \           }\n        }\n    }\n\n    free(e); free(head); free(dist); free(heap);\n\
        \    return -1;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int ShortestPath(int n, int[][] edges, string labels, int k)\
        \ {\n        if (n == 0) return -1;\n        if (n == 1) return 0;\n\n     \
        \   List<(int to, int weight)>[] adj = new List<(int, int)>[n];\n        for\
        \ (int i = 0; i < n; i++) {\n            adj[i] = new List<(int, int)>();\n\
        \        }\n        foreach (var edge in edges) {\n            adj[edge[0]].Add((edge[1],\
        \ edge[2]));\n        }\n\n        long[] dist = new long[n * (k + 1)];\n  \
        \      Array.Fill(dist, long.MaxValue);\n\n        PriorityQueue<(int node,\
        \ int count), long> pq = new PriorityQueue<(int node, int count), long>();\n\
        \n        dist[0 * (k + 1) + 1] = 0;\n        pq.Enqueue((0, 1), 0);\n\n   \
        \     while (pq.Count > 0) {\n            if (pq.TryDequeue(out var state, out\
        \ long d)) {\n                int u = state.node;\n                int count\
        \ = state.count;\n\n                if (d > dist[u * (k + 1) + count]) continue;\n\
        \                if (u == n - 1) return (int)d;\n\n                foreach (var\
        \ edge in adj[u]) {\n                    int v = edge.to;\n                \
        \    int w = edge.weight;\n                    int nextCount = (labels[u] ==\
        \ labels[v]) ? count + 1 : 1;\n\n                    if (nextCount <= k) {\n\
        \                        if (dist[v * (k + 1) + nextCount] > d + w) {\n    \
        \                        dist[v * (k + 1) + nextCount] = d + w;\n          \
        \                  pq.Enqueue((v, nextCount), dist[v * (k + 1) + nextCount]);\n\
        \                        }\n                    }\n                }\n     \
        \       }\n        }\n\n        return -1;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number[][]} edges\n * @param\
        \ {string} labels\n * @param {number} k\n * @return {number}\n */\nvar shortestPath\
        \ = function(n, edges, labels, k) {\n    if (n === 1) return 0;\n\n    const\
        \ adj = Array.from({ length: n }, () => []);\n    for (const [u, v, w] of edges)\
        \ {\n        adj[u].push([v, w]);\n    }\n\n    const INF = 1000000000;\n  \
        \  const dist = new Int32Array(n * (k + 1)).fill(INF);\n\n    class MinHeap\
        \ {\n        constructor() {\n            this.heap = [];\n        }\n     \
        \   push(priority, node, count) {\n            this.heap.push({ priority, node,\
        \ count });\n            this.bubbleUp();\n        }\n        pop() {\n    \
        \        if (this.heap.length === 0) return null;\n            if (this.heap.length\
        \ === 1) return this.heap.pop();\n            const top = this.heap[0];\n  \
        \          this.heap[0] = this.heap.pop();\n            this.bubbleDown();\n\
        \            return top;\n        }\n        bubbleUp() {\n            let idx\
        \ = this.heap.length - 1;\n            while (idx > 0) {\n                let\
        \ p = (idx - 1) >> 1;\n                if (this.heap[p].priority <= this.heap[idx].priority)\
        \ break;\n                let temp = this.heap[p];\n                this.heap[p]\
        \ = this.heap[idx];\n                this.heap[idx] = temp;\n              \
        \  idx = p;\n            }\n        }\n        bubbleDown() {\n            let\
        \ idx = 0;\n            while (true) {\n                let l = (idx << 1) +\
        \ 1, r = (idx << 1) + 2, s = idx;\n                if (l < this.heap.length\
        \ && this.heap[l].priority < this.heap[s].priority) s = l;\n               \
        \ if (r < this.heap.length && this.heap[r].priority < this.heap[s].priority)\
        \ s = r;\n                if (s === idx) break;\n                let temp =\
        \ this.heap[idx];\n                this.heap[idx] = this.heap[s];\n        \
        \        this.heap[s] = temp;\n                idx = s;\n            }\n   \
        \     }\n    }\n\n    const pq = new MinHeap();\n    dist[0 * (k + 1) + 1] =\
        \ 0;\n    pq.push(0, 0, 1);\n\n    while (pq.heap.length > 0) {\n        const\
        \ { priority: d, node: u, count } = pq.pop();\n\n        if (d > dist[u * (k\
        \ + 1) + count]) continue;\n        if (u === n - 1) return d;\n\n        for\
        \ (const [v, w] of adj[u]) {\n            const nextCount = (labels[u] === labels[v])\
        \ ? count + 1 : 1;\n            if (nextCount <= k) {\n                const\
        \ newDist = d + w;\n                if (newDist < dist[v * (k + 1) + nextCount])\
        \ {\n                    dist[v * (k + 1) + nextCount] = newDist;\n        \
        \            pq.push(newDist, v, nextCount);\n                }\n          \
        \  }\n        }\n    }\n\n    return -1;\n};"
      typescript: "function shortestPath(n: number, edges: number[][], labels: string,\
        \ k: number): number {\n    if (n === 1) return 0;\n\n    const adj: [number,\
        \ number][][] = Array.from({ length: n }, () => []);\n    for (const [u, v,\
        \ w] of edges) {\n        adj[u].push([v, w]);\n    }\n\n    const INF = 1000000000;\n\
        \    const dist = new Int32Array(n * (k + 1)).fill(INF);\n\n    class MinHeap\
        \ {\n        public heap: { priority: number, node: number, count: number }[]\
        \ = [];\n        push(priority: number, node: number, count: number) {\n   \
        \         this.heap.push({ priority, node, count });\n            this.bubbleUp();\n\
        \        }\n        pop() {\n            if (this.heap.length === 0) return\
        \ null;\n            if (this.heap.length === 1) return this.heap.pop();\n \
        \           const top = this.heap[0];\n            this.heap[0] = this.heap.pop()!;\n\
        \            this.bubbleDown();\n            return top;\n        }\n      \
        \  private bubbleUp() {\n            let idx = this.heap.length - 1;\n     \
        \       while (idx > 0) {\n                let p = (idx - 1) >> 1;\n       \
        \         if (this.heap[p].priority <= this.heap[idx].priority) break;\n   \
        \             let temp = this.heap[p];\n                this.heap[p] = this.heap[idx];\n\
        \                this.heap[idx] = temp;\n                idx = p;\n        \
        \    }\n        }\n        private bubbleDown() {\n            let idx = 0;\n\
        \            while (true) {\n                let l = (idx << 1) + 1, r = (idx\
        \ << 1) + 2, s = idx;\n                if (l < this.heap.length && this.heap[l].priority\
        \ < this.heap[s].priority) s = l;\n                if (r < this.heap.length\
        \ && this.heap[r].priority < this.heap[s].priority) s = r;\n               \
        \ if (s === idx) break;\n                let temp = this.heap[idx];\n      \
        \          this.heap[idx] = this.heap[s];\n                this.heap[s] = temp;\n\
        \                idx = s;\n            }\n        }\n    }\n\n    const pq =\
        \ new MinHeap();\n    dist[0 * (k + 1) + 1] = 0;\n    pq.push(0, 0, 1);\n\n\
        \    while (pq.heap.length > 0) {\n        const current = pq.pop();\n     \
        \   if (!current) break;\n        const { priority: d, node: u, count } = current;\n\
        \n        if (d > dist[u * (k + 1) + count]) continue;\n        if (u === n\
        \ - 1) return d;\n\n        for (const [v, w] of adj[u]) {\n            const\
        \ nextCount = (labels[u] === labels[v]) ? count + 1 : 1;\n            if (nextCount\
        \ <= k) {\n                const newDist = d + w;\n                if (newDist\
        \ < dist[v * (k + 1) + nextCount]) {\n                    dist[v * (k + 1) +\
        \ nextCount] = newDist;\n                    pq.push(newDist, v, nextCount);\n\
        \                }\n            }\n        }\n    }\n\n    return -1;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @param Integer[][]\
        \ $edges\n     * @param String $labels\n     * @param Integer $k\n     * @return\
        \ Integer\n     */\n    function shortestPath($n, $edges, $labels, $k) {\n \
        \       if ($n === 1) return 0;\n\n        $adj = array_fill(0, $n, []);\n \
        \       foreach ($edges as $edge) {\n            $adj[$edge[0]][] = [$edge[1],\
        \ $edge[2]];\n        }\n\n        $inf = 1000000000;\n        $distSize = $n\
        \ * ($k + 1);\n        $dist = new SplFixedArray($distSize);\n        for ($i\
        \ = 0; $i < $distSize; $i++) $dist[$i] = $inf;\n\n        $pq = new SplPriorityQueue();\n\
        \        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);\n\n        $dist[1]\
        \ = 0; // 0 * (k + 1) + 1\n        $pq->insert([0, 1], 0);\n\n        while\
        \ (!$pq->isEmpty()) {\n            $item = $pq->extract();\n            $u =\
        \ $item['data'][0];\n            $count = $item['data'][1];\n            $d\
        \ = -$item['priority'];\n\n            if ($d > $dist[$u * ($k + 1) + $count])\
        \ continue;\n            if ($u == $n - 1) return $d;\n\n            if (isset($adj[$u]))\
        \ {\n                foreach ($adj[$u] as $edge) {\n                    $v =\
        \ $edge[0];\n                    $w = $edge[1];\n                    $nextCount\
        \ = ($labels[$u] == $labels[$v]) ? $count + 1 : 1;\n                    if ($nextCount\
        \ <= $k) {\n                        $newDist = $d + $w;\n                  \
        \      $idx = $v * ($k + 1) + $nextCount;\n                        if ($newDist\
        \ < $dist[$idx]) {\n                            $dist[$idx] = $newDist;\n  \
        \                          $pq->insert([$v, $nextCount], -$newDist);\n     \
        \                   }\n                    }\n                }\n          \
        \  }\n        }\n\n        return -1;\n    }\n}"
      swift: "class Solution {\n    struct State {\n        let node: Int\n        let\
        \ count: Int\n        let dist: Int\n    }\n\n    struct MinHeap {\n       \
        \ var heap: [State] = []\n        mutating func push(_ state: State) {\n   \
        \         heap.append(state)\n            var idx = heap.count - 1\n       \
        \     while idx > 0 {\n                let p = (idx - 1) / 2\n             \
        \   if heap[idx].dist < heap[p].dist {\n                    heap.swapAt(idx,\
        \ p)\n                    idx = p\n                } else {\n              \
        \      break\n                }\n            }\n        }\n        mutating\
        \ func pop() -> State? {\n            if heap.isEmpty { return nil }\n     \
        \       if heap.count == 1 { return heap.removeLast() }\n            let res\
        \ = heap[0]\n            heap[0] = heap.removeLast()\n            var idx =\
        \ 0\n            while true {\n                let l = 2 * idx + 1, r = 2 *\
        \ idx + 2\n                var s = idx\n                if l < heap.count &&\
        \ heap[l].dist < heap[s].dist { s = l }\n                if r < heap.count &&\
        \ heap[r].dist < heap[s].dist { s = r }\n                if s == idx { break\
        \ }\n                heap.swapAt(idx, s)\n                idx = s\n        \
        \    }\n            return res\n        }\n    }\n\n    func shortestPath(_\
        \ n: Int, _ edges: [[Int]], _ labels: String, _ k: Int) -> Int {\n        if\
        \ n == 1 { return 0 }\n\n        let labelArr = Array(labels)\n        var adj\
        \ = [[(to: Int, weight: Int)]](repeating: [], count: n)\n        for edge in\
        \ edges {\n            adj[edge[0]].append((edge[1], edge[2]))\n        }\n\n\
        \        var dist = [Int](repeating: Int.max, count: n * (k + 1))\n        var\
        \ pq = MinHeap()\n\n        dist[0 * (k + 1) + 1] = 0\n        pq.push(State(node:\
        \ 0, count: 1, dist: 0))\n\n        while let state = pq.pop() {\n         \
        \   let u = state.node\n            let count = state.count\n            let\
        \ d = state.dist\n\n            if d > dist[u * (k + 1) + count] { continue\
        \ }\n            if u == n - 1 { return d }\n\n            for edge in adj[u]\
        \ {\n                let v = edge.to\n                let w = edge.weight\n\
        \                let nextCount = (labelArr[u] == labelArr[v]) ? count + 1 :\
        \ 1\n\n                if nextCount <= k {\n                    let newDist\
        \ = d + w\n                    if newDist < dist[v * (k + 1) + nextCount] {\n\
        \                        dist[v * (k + 1) + nextCount] = newDist\n         \
        \               pq.push(State(node: v, count: nextCount, dist: newDist))\n \
        \                   }\n                }\n            }\n        }\n\n     \
        \   return -1\n    }\n}"
      kotlin: "import java.util.PriorityQueue\n\nclass Solution {\n    data class Edge(val\
        \ to: Int, val weight: Int)\n    data class State(val dist: Int, val u: Int,\
        \ val c: Int)\n\n    fun shortestPath(n: Int, edges: Array<IntArray>, labels:\
        \ String, k: Int): Int {\n        val adj = Array(n) { mutableListOf<Edge>()\
        \ }\n        for (edge in edges) {\n            adj[edge[0]].add(Edge(edge[1],\
        \ edge[2]))\n        }\n\n        val inf = 1000000000\n        val dist = IntArray(n\
        \ * (k + 1)) { inf }\n        val pq = PriorityQueue<State>(compareBy { it.dist\
        \ })\n\n        dist[1] = 0\n        pq.offer(State(0, 0, 1))\n\n        while\
        \ (pq.isNotEmpty()) {\n            val (d, u, c) = pq.poll()\n\n           \
        \ if (d > dist[u * (k + 1) + c]) continue\n\n            for (edge in adj[u])\
        \ {\n                val v = edge.to\n                val w = edge.weight\n\
        \                val nc = if (labels[u] == labels[v]) c + 1 else 1\n\n     \
        \           if (nc <= k) {\n                    if (d + w < dist[v * (k + 1)\
        \ + nc]) {\n                        dist[v * (k + 1) + nc] = d + w\n       \
        \                 pq.offer(State(dist[v * (k + 1) + nc], v, nc))\n         \
        \           }\n                }\n            }\n        }\n\n        var minWeight\
        \ = inf\n        for (c in 1..k) {\n            minWeight = minOf(minWeight,\
        \ dist[(n - 1) * (k + 1) + c])\n        }\n\n        return if (minWeight ==\
        \ inf) -1 else minWeight\n    }\n}"
      dart: "import 'dart:collection';\nimport 'dart:math';\n\nclass Edge {\n  final\
        \ int to;\n  final int weight;\n  Edge(this.to, this.weight);\n}\n\nclass PriorityQueue\
        \ {\n  final List<List<int>> heap = [];\n\n  void push(List<int> val) {\n  \
        \  heap.add(val);\n    int idx = heap.length - 1;\n    while (idx > 0) {\n \
        \     int parent = (idx - 1) ~/ 2;\n      if (heap[idx][0] < heap[parent][0])\
        \ {\n        List<int> tmp = heap[idx];\n        heap[idx] = heap[parent];\n\
        \        heap[parent] = tmp;\n        idx = parent;\n      } else {\n      \
        \  break;\n      }\n    }\n  }\n\n  List<int> pop() {\n    if (heap.isEmpty)\
        \ return [];\n    if (heap.length == 1) return heap.removeLast();\n    List<int>\
        \ res = heap[0];\n    heap[0] = heap.removeLast();\n    int idx = 0;\n    while\
        \ (true) {\n      int left = 2 * idx + 1;\n      int right = 2 * idx + 2;\n\
        \      int small = idx;\n      if (left < heap.length && heap[left][0] < heap[small][0])\
        \ small = left;\n      if (right < heap.length && heap[right][0] < heap[small][0])\
        \ small = right;\n      if (small == idx) break;\n      List<int> tmp = heap[idx];\n\
        \      heap[idx] = heap[small];\n      heap[small] = tmp;\n      idx = small;\n\
        \    }\n    return res;\n  }\n\n  bool get isEmpty => heap.isEmpty;\n  bool\
        \ get isNotEmpty => heap.isNotEmpty;\n}\n\nclass Solution {\n  int shortestPath(int\
        \ n, List<List<int>> edges, String labels, int k) {\n    List<List<Edge>> adj\
        \ = List.generate(n, (i) => <Edge>[]);\n    for (var edge in edges) {\n    \
        \  adj[edge[0]].add(Edge(edge[1], edge[2]));\n    }\n\n    const int inf = 1000000000;\n\
        \    List<int> dist = List.filled(n * (k + 1), inf);\n    PriorityQueue pq =\
        \ PriorityQueue();\n\n    dist[1] = 0;\n    pq.push([0, 0, 1]);\n\n    while\
        \ (pq.isNotEmpty) {\n      List<int> cur = pq.pop();\n      int d = cur[0];\n\
        \      int u = cur[1];\n      int c = cur[2];\n\n      if (d > dist[u * (k +\
        \ 1) + c]) continue;\n\n      for (var edge in adj[u]) {\n        int v = edge.to;\n\
        \        int w = edge.weight;\n        int nc = (labels[u] == labels[v]) ? c\
        \ + 1 : 1;\n\n        if (nc <= k) {\n          if (d + w < dist[v * (k + 1)\
        \ + nc]) {\n            dist[v * (k + 1) + nc] = d + w;\n            pq.push([dist[v\
        \ * (k + 1) + nc], v, nc]);\n          }\n        }\n      }\n    }\n\n    int\
        \ minWeight = inf;\n    for (int c = 1; c <= k; c++) {\n      minWeight = min(minWeight,\
        \ dist[(n - 1) * (k + 1) + c]);\n    }\n\n    return minWeight == inf ? -1 :\
        \ minWeight;\n  }\n}"
      go: "import (\n\t\"container/heap\"\n)\n\ntype Edge struct {\n\tto     int\n\t\
        weight int\n}\n\ntype Item struct {\n\tdist, u, c int\n}\n\ntype PriorityQueue\
        \ []*Item\n\nfunc (pq PriorityQueue) Len() int           { return len(pq) }\n\
        func (pq PriorityQueue) Less(i, j int) bool { return pq[i].dist < pq[j].dist\
        \ }\nfunc (pq PriorityQueue) Swap(i, j int)      { pq[i], pq[j] = pq[j], pq[i]\
        \ }\n\nfunc (pq *PriorityQueue) Push(x interface{}) {\n\t*pq = append(*pq, x.(*Item))\n\
        }\n\nfunc (pq *PriorityQueue) Pop() interface{} {\n\told := *pq\n\tn := len(old)\n\
        \titem := old[n-1]\n\t*pq = old[0 : n-1]\n\treturn item\n}\n\nfunc shortestPath(n\
        \ int, edges [][]int, labels string, k int) int {\n\tadj := make([][]Edge, n)\n\
        \tfor _, edge := range edges {\n\t\tu, v, w := edge[0], edge[1], edge[2]\n\t\
        \tadj[u] = append(adj[u], Edge{v, w})\n\t}\n\n\tinf := 1000000000\n\tdist :=\
        \ make([]int, n*(k+1))\n\tfor i := range dist {\n\t\tdist[i] = inf\n\t}\n\n\t\
        pq := &PriorityQueue{}\n\theap.Init(pq)\n\n\tdist[1] = 0\n\theap.Push(pq, &Item{0,\
        \ 0, 1})\n\n\tfor pq.Len() > 0 {\n\t\tcurr := heap.Pop(pq).(*Item)\n\t\td, u,\
        \ c := curr.dist, curr.u, curr.c\n\n\t\tif d > dist[u*(k+1)+c] {\n\t\t\tcontinue\n\
        \t\t}\n\n\t\tfor _, edge := range adj[u] {\n\t\t\tv, w := edge.to, edge.weight\n\
        \t\t\tnc := 1\n\t\t\tif labels[u] == labels[v] {\n\t\t\t\tnc = c + 1\n\t\t\t\
        }\n\n\t\t\tif nc <= k {\n\t\t\t\tif d+w < dist[v*(k+1)+nc] {\n\t\t\t\t\tdist[v*(k+1)+nc]\
        \ = d + w\n\t\t\t\t\theap.Push(pq, &Item{dist[v*(k+1)+nc], v, nc})\n\t\t\t\t\
        }\n\t\t\t}\n\t\t}\n\t}\n\n\tminWeight := inf\n\tfor c := 1; c <= k; c++ {\n\t\
        \tif dist[(n-1)*(k+1)+c] < minWeight {\n\t\t\tminWeight = dist[(n-1)*(k+1)+c]\n\
        \t\t}\n\t}\n\n\tif minWeight == inf {\n\t\treturn -1\n\t}\n\treturn minWeight\n\
        }"
      ruby: "# @param {Integer} n\n# @param {Integer[][]} edges\n# @param {String} labels\n\
        # @param {Integer} k\n# @return {Integer}\ndef shortest_path(n, edges, labels,\
        \ k)\n  adj = Array.new(n) { [] }\n  edges.each do |u, v, w|\n    adj[u] <<\
        \ [v, w]\n  end\n\n  inf = 1_000_000_000\n  dist = Array.new(n * (k + 1), inf)\n\
        \n  pq = PriorityQueue.new\n  dist[1] = 0\n  pq.push([0, 0, 1])\n\n  while !pq.empty?\n\
        \    d, u, c = pq.pop\n    next if d > dist[u * (k + 1) + c]\n\n    adj[u].each\
        \ do |v, w|\n      nc = (labels[u] == labels[v]) ? c + 1 : 1\n      if nc <=\
        \ k\n        if d + w < dist[v * (k + 1) + nc]\n          dist[v * (k + 1) +\
        \ nc] = d + w\n          pq.push([dist[v * (k + 1) + nc], v, nc])\n\n      \
        \  end\n      end\n    end\n  end\n\n  ans = inf\n  (1..k).each do |c|\n   \
        \ ans = [ans, dist[(n - 1) * (k + 1) + c]].min\n  end\n\n  ans == inf ? -1 :\
        \ ans\nend\n\nclass PriorityQueue\n  def initialize\n    @heap = []\n  end\n\
        \n  def push(val)\n    @heap << val\n    idx = @heap.size - 1\n    while idx\
        \ > 0\n      parent = (idx - 1) / 2\n      if @heap[idx][0] < @heap[parent][0]\n\
        \        @heap[idx], @heap[parent] = @heap[parent], @heap[idx]\n        idx\
        \ = parent\n      else\n        break\n      end\n    end\n  end\n\n  def pop\n\
        \    return nil if @heap.empty?\n    return @heap.pop if @heap.size == 1\n \
        \   res = @heap[0]\n    @heap[0] = @heap.pop\n    idx = 0\n    while (left =\
        \ 2 * idx + 1) < @heap.size\n      right = left + 1\n      small = left\n  \
        \    if right < @heap.size && @heap[right][0] < @heap[left][0]\n        small\
        \ = right\n      end\n      if @heap[idx][0] <= @heap[small][0]\n        break\n\
        \      end\n      @heap[idx], @heap[small] = @heap[small], @heap[idx]\n    \
        \  idx = small\n    end\n    res\n  end\n\n  def empty?\n    @heap.empty?\n\
        \  end\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    case class Edge(to:\
        \ Int, weight: Int)\n    case class State(dist: Int, u: Int, c: Int)\n\n   \
        \ def shortestPath(n: Int, edges: Array[Array[Int]], labels: String, k: Int):\
        \ Int = {\n        val adj = Array.fill(n)(mutable.ArrayBuffer[Edge]())\n  \
        \      for (edge <- edges) {\n            adj(edge(0)) += Edge(edge(1), edge(2))\n\
        \        }\n\n        val inf = 1000000000\n        val dist = Array.fill(n\
        \ * (k + 1))(inf)\n        val pq = mutable.PriorityQueue[State]()(Ordering.by(-_.dist))\n\
        \n        dist(1) = 0\n        pq.enqueue(State(0, 0, 1))\n\n        while (pq.nonEmpty)\
        \ {\n            val State(d, u, c) = pq.dequeue()\n\n            if (d <= dist(u\
        \ * (k + 1) + c)) {\n                for (edge <- adj(u)) {\n              \
        \      val v = edge.to\n                    val w = edge.weight\n          \
        \          val nc = if (labels(u) == labels(v)) c + 1 else 1\n\n           \
        \         if (nc <= k) {\n                        if (d + w < dist(v * (k +\
        \ 1) + nc)) {\n                            dist(v * (k + 1) + nc) = d + w\n\
        \                            pq.enqueue(State(d + w, v, nc))\n             \
        \           }\n                    }\n                }\n            }\n   \
        \     }\n\n        var minWeight = inf\n        for (c <- 1 to k) {\n      \
        \      if (dist((n - 1) * (k + 1) + c) < minWeight) {\n                minWeight\
        \ = dist((n - 1) * (k + 1) + c)\n            }\n        }\n\n        if (minWeight\
        \ == inf) -1 else minWeight\n    }\n}"
      rust: "use std::cmp::Reverse;\nuse std::collections::BinaryHeap;\n\nimpl Solution\
        \ {\n    pub fn shortest_path(n: i32, edges: Vec<Vec<i32>>, labels: String,\
        \ k: i32) -> i32 {\n        let n = n as usize;\n        let k = k as usize;\n\
        \        let labels = labels.as_bytes();\n        let mut adj = vec![vec![];\
        \ n];\n        for edge in edges {\n            adj[edge[0] as usize].push((edge[1]\
        \ as usize, edge[2]));\n        }\n\n        let mut dist = vec![i32::MAX; n\
        \ * (k + 1)];\n        let mut pq = BinaryHeap::new();\n\n        if n > 0 {\n\
        \            let start_idx = 1; \n            dist[start_idx] = 0;\n       \
        \     pq.push(Reverse((0, 0, 1)));\n        }\n\n        while let Some(Reverse((d,\
        \ u, c1))) = pq.pop() {\n            if d > dist[u * (k + 1) + c1] {\n     \
        \           continue;\n            }\n            if u == n - 1 {\n        \
        \        return d;\n            }\n\n            for &(v, w) in &adj[u] {\n\
        \                let c2 = if labels[u] == labels[v] {\n                    c1\
        \ + 1\n                } else {\n                    1\n                };\n\
        \                if c2 <= k {\n                    let next_d = d + w;\n   \
        \                 let next_idx = v * (k + 1) + c2;\n                    if next_d\
        \ < dist[next_idx] {\n                        dist[next_idx] = next_d;\n   \
        \                     pq.push(Reverse((next_d, v, c2)));\n                 \
        \   }\n                }\n            }\n        }\n\n        -1\n    }\n}"
      racket: "(require data/heap)\n\n(define/contract (shortest-path n edges labels\
        \ k)\n  (-> exact-integer? (listof (listof exact-integer?)) string? exact-integer?\
        \ exact-integer?)\n  (let* ([k-plus-1 (+ k 1)]\n         [adj (make-vector n\
        \ '())]\n         [dist (make-vector (* n k-plus-1) +inf.0)]\n         [pq (make-heap\
        \ (lambda (a b) (<= (car a) (car b))))])\n    (for ([edge edges])\n      (let\
        \ ([u (first edge)]\n            [v (second edge)]\n            [w (third edge)])\n\
        \        (vector-set! adj u (cons (list v w) (vector-ref adj u)))))\n\n    (vector-set!\
        \ dist 1 0)\n    (heap-add! pq (list 0 0 1))\n\n    (let loop ()\n      (if\
        \ (zero? (heap-count pq))\n          -1\n          (let* ([top (heap-min pq)]\n\
        \                 [d (first top)]\n                 [u (second top)]\n     \
        \            [c1 (third top)])\n            (heap-remove-min! pq)\n        \
        \    (if (= u (- n 1))\n                d\n                (begin\n        \
        \          (if (<= d (vector-ref dist (+ (* u k-plus-1) c1)))\n            \
        \          (for ([edge (vector-ref adj u)])\n                        (let* ([v\
        \ (first edge)]\n                               [w (second edge)]\n        \
        \                       [c2 (if (char=? (string-ref labels u) (string-ref labels\
        \ v))\n                                       (+ c1 1)\n                   \
        \                    1)])\n                          (when (<= c2 k)\n     \
        \                       (let* ([idx (+ (* v k-plus-1) c2)]\n               \
        \                    [old-d (vector-ref dist idx)]\n                       \
        \            [new-d (+ d w)])\n                              (when (< new-d\
        \ old-d)\n                                (vector-set! dist idx new-d)\n   \
        \                             (heap-add! pq (list new-d v c2)))))))\n      \
        \                (void))\n                  (loop))))))))"
      erlang: "-spec shortest_path(N :: integer(), Edges :: [[integer()]], Labels ::\
        \ unicode:unicode_binary(), K :: integer()) -> integer().\nshortest_path(N,\
        \ Edges, Labels, K) ->\n  Adj = build_adj(Edges, maps:new()),\n  LabelsTuple\
        \ = list_to_tuple(binary_to_list(Labels)),\n  PQ = gb_sets:add_element({0, 0,\
        \ 1}, gb_sets:empty()),\n  Dist = maps:put({0, 1}, 0, maps:new()),\n  dijkstra(PQ,\
        \ Dist, Adj, LabelsTuple, K, N).\n\nbuild_adj([], Map) -> Map;\nbuild_adj([[U,\
        \ V, W] | T], Map) ->\n  List = maps:get(U, Map, []),\n  build_adj(T, maps:put(U,\
        \ [{V, W} | List], Map)).\n\ndijkstra(PQ, Dist, Adj, Labels, K, N) ->\n  case\
        \ gb_sets:is_empty(PQ) of\n    true -> -1;\n    false ->\n      {{D, U, C1},\
        \ PQ1} = gb_sets:take_shortest(PQ),\n      case U == N - 1 of\n        true\
        \ -> D;\n        false ->\n          case D > maps:get({U, C1}, Dist, infinity)\
        \ of\n            true -> dijkstra(PQ1, Dist, Adj, Labels, K, N);\n        \
        \    false ->\n              {NewPQ, NewDist} = process_neighbors(maps:get(U,\
        \ Adj, []), D, U, C1, PQ1, Dist, Labels, K),\n              dijkstra(NewPQ,\
        \ NewDist, Adj, Labels, K, N)\n          end\n      end\n  end.\n\nprocess_neighbors([],\
        \ _D, _U, _C1, PQ, Dist, _Labels, _K) -> {PQ, Dist};\nprocess_neighbors([{V,\
        \ W} | T], D, U, C1, PQ, Dist, Labels, K) ->\n  C2 = case element(U + 1, Labels)\
        \ == element(V + 1, Labels) of\n    true -> C1 + 1;\n    false -> 1\n  end,\n\
        \  if C2 =< K ->\n    NewD = D + W,\n    OldD = maps:get({V, C2}, Dist, infinity),\n\
        \    if NewD < OldD ->\n      process_neighbors(T, D, U, C1, gb_sets:add_element({NewD,\
        \ V, C2}, PQ), maps:put({V, C2}, NewD, Dist), Labels, K);\n    true ->\n   \
        \   process_neighbors(T, D, U, C1, PQ, Dist, Labels, K)\n    end;\n  true ->\n\
        \    process_neighbors(T, D, U, C1, PQ, Dist, Labels, K)\n  end."
      elixir: "defmodule Solution do\n  @spec shortest_path(n :: integer, edges :: [[integer]],\
        \ labels :: String.t, k :: integer) :: integer\n  def shortest_path(n, edges,\
        \ labels, k) do\n    adj = Enum.reduce(edges, %{}, fn [u, v, w], acc ->\n  \
        \    Map.update(acc, u, [{v, w}], &([{v, w} | &1]))\n    end)\n\n    labels_tuple\
        \ = labels |> String.to_charlist() |> List.to_tuple()\n\n    pq = :gb_sets.add_element({0,\
        \ 0, 1}, :gb_sets.empty())\n    dist = %{{0, 1} => 0}\n\n    dijkstra(pq, dist,\
        \ adj, labels_tuple, k, n)\n  end\n\n  defp dijkstra(pq, dist, adj, labels,\
        \ k, n) do\n    if :gb_sets.is_empty(pq) do\n      -1\n    else\n      {{d,\
        \ u, c1}, pq1} = :gb_sets.take_shortest(pq)\n\n      cond do\n        u == n\
        \ - 1 ->\n          d\n        d > Map.get(dist, {u, c1}, :infinity) ->\n  \
        \        dijkstra(pq1, dist, adj, labels, k, n)\n        true ->\n         \
        \ {new_pq, new_dist} = process_neighbors(Map.get(adj, u, []), d, u, c1, pq1,\
        \ dist, labels, k)\n          dijkstra(new_pq, new_dist, adj, labels, k, n)\n\
        \      end\n    end\n  end\n\n  defp process_neighbors([], _d, _u, _c1, pq,\
        \ dist, _labels, _k), do: {pq, dist}\n  defp process_neighbors([{v, w} | tail],\
        \ d, u, c1, pq, dist, labels, k) do\n    c2 = if elem(labels, u) == elem(labels,\
        \ v), do: c1 + 1, else: 1\n\n    if c2 <= k do\n      new_d = d + w\n      old_d\
        \ = Map.get(dist, {v, c2}, :infinity)\n\n      if new_d < old_d do\n       \
        \ process_neighbors(tail, d, u, c1, :gb_sets.add_element({new_d, v, c2}, pq),\
        \ Map.put(dist, {v, c2}, new_d), labels, k)\n      else\n        process_neighbors(tail,\
        \ d, u, c1, pq, dist, labels, k)\n      end\n    else\n      process_neighbors(tail,\
        \ d, u, c1, pq, dist, labels, k)\n    end\n  end\nend"
    approach: 'To solve this problem, we use Dijkstra''s algorithm on an expanded graph
      where the state is defined by the current node and the number of consecutive identical
      characters ending at that node. A state is represented as $(u, c)$, where $u$
      is the current node and $c$ is the consecutive run length of the character $labels[u]$
      at the end of the current path. Starting from node 0 with an initial run length
      of 1, we traverse the graph. For each directed edge $(u, v)$ with weight $w$,
      we determine the new consecutive run length $nc$: if $labels[u] == labels[v]$,
      then $nc = c + 1$; otherwise, $nc = 1$. The transition is valid only if $nc \le
      k$.


      By tracking the shortest distance to each state $(u, c)$ using a distance array
      $dist[u][c]$, we can efficiently find the minimum weight to reach any state of
      node $n-1$. The state space consists of $N \times K$ states, and since each edge
      $(u, v)$ can be processed for each possible incoming run length $c$, the total
      number of transitions is at most $M \times K$. Dijkstra''s algorithm ensures we
      find the shortest path to node $n-1$ while respecting the consecutive character
      constraint. The first time we extract a state $(n-1, c)$ from the priority queue,
      we have found the minimum total edge weight.'
    time_complexity: O(M \cdot K \cdot \log(N \cdot K)) where $N$ is the number of nodes,
      $M$ is the number of edges, and $K$ is the maximum consecutive character constraint.
      The expanded graph has $N \cdot K$ states and $M \cdot K$ possible transitions,
      and Dijkstra's algorithm performs log-time priority queue operations for each
      transition.
    space_complexity: O(N \cdot K + M) to store the adjacency list for the original
      $M$ edges and the distance array for the $N \cdot K$ states in the expanded graph.
    elapsed_time: 563.9734029769897
    model: gemini-3-flash-preview
    generated_at: '2026-10-30 03:57:15 '
---

## Problem #3970: Shortest Path With At Most K Consecutive Identical Characters

**Difficulty:** Medium

**Topics:** String, Graph Theory, Heap (Priority Queue), Shortest Path

## Problem Description

<p>You are given an integer <code>n</code> representing the number of nodes in a <strong>directed weighted</strong> graph, numbered from 0 to <code>n - 1</code>. This is represented by a 2D integer array <code>edges</code>, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]</code> represents a directed edge from node <code>u<sub>i</sub></code> to node <code>v<sub>i</sub></code> with weight <code>w<sub>i</sub></code>.</p>

<p>You are also given a string <code>labels</code> of length <code>n</code>, where <code>labels[i]</code> is the character assigned to node <code>i</code>, and an integer <code>k</code>.</p>

<p>Return the <strong>minimum</strong> <strong>total</strong> edge weight of a path from node 0 to node <code>n - 1</code> such that the concatenation of the labels of the nodes along the path contains <strong>at most</strong> <code>k</code> <strong>consecutive</strong> <strong>identical</strong> characters. If no valid path exists, return -1.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = &quot;aab&quot;, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The optimal valid path from node 0 to node 2 is as follows:</p>

<ul>
	<li>Use <code>edges[2] = [0, 2, 3]</code> to reach node 2 with a weight <code>w<sub>i</sub> = 3</code>.</li>
</ul>
The corresponding concatenation of labels is <code>&quot;ab&quot;</code>, which satisfies at most <code>k = 1</code> consecutive identical characters. Thus, the answer is 3.</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = &quot;aab&quot;, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The optimal valid path from node 0 to node 2 is as follows:</p>

<ul>
	<li>Use <code>edges[0] = [0, 1, 1]</code> to reach node 1 with weight <code>w<sub>i</sub> = 1</code>.</li>
	<li>Use <code>edges[1] = [1, 2, 1]</code> to reach node 2 with weight <code>w<sub>i</sub> = 1</code>.</li>
</ul>
The corresponding concatenation of labels is <code>&quot;aab&quot;</code>, which satisfies at most <code>k = 2</code> consecutive identical characters. Thus, the answer is 2.</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, edges = [[0,1,1],[1,2,1]], labels = &quot;aaa&quot;, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no valid path from node 0 to node 2 that satisfies at most <code>k = 2</code> consecutive identical characters. Thus, the answer is -1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == labels.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= edges.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>edges[i] == [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]</code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li><code>1 &lt;= w<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
	<li><code>labels</code> consists of lowercase English letters</li>
	<li><code>1 &lt;= k &lt;= 50</code></li>
</ul>


## Hints

1. The validity of a path depends not only on the current node, but also on how many consecutive times the current node’s label has appeared at the end of the path.

2. Use Dijkstra on states `(node, count)`, where `count` is the current consecutive run length of `labels[node]`.

3. When moving from node `u` to node `v`, the next count becomes `count + 1` if `labels[u] == labels[v]`, otherwise it becomes 1. Ignore transitions where the next count exceeds `k`.

4. The answer is the minimum distance among all states ending at node `n - 1`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem, we use Dijkstra's algorithm on an expanded graph where the state is defined by the current node and the number of consecutive identical characters ending at that node. A state is represented as $(u, c)$, where $u$ is the current node and $c$ is the consecutive run length of the character $labels[u]$ at the end of the current path. Starting from node 0 with an initial run length of 1, we traverse the graph. For each directed edge $(u, v)$ with weight $w$, we determine the new consecutive run length $nc$: if $labels[u] == labels[v]$, then $nc = c + 1$; otherwise, $nc = 1$. The transition is valid only if $nc \le k$.

By tracking the shortest distance to each state $(u, c)$ using a distance array $dist[u][c]$, we can efficiently find the minimum weight to reach any state of node $n-1$. The state space consists of $N \times K$ states, and since each edge $(u, v)$ can be processed for each possible incoming run length $c$, the total number of transitions is at most $M \times K$. Dijkstra's algorithm ensures we find the shortest path to node $n-1$ while respecting the consecutive character constraint. The first time we extract a state $(n-1, c)$ from the priority queue, we have found the minimum total edge weight.

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
    struct State {
        int d, u, c;
        bool operator<(const State& other) const {
            return d > other.d;
        }
    };

    int shortestPath(int n, vector<vector<int>>& edges, string labels, int k) {
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back({edge[1], edge[2]});
        }

        int max_c = k + 1;
        vector<vector<int>> dist(n, vector<int>(max_c, 1e9 + 7));
        priority_queue<State> pq;

        dist[0][1] = 0;
        pq.push({0, 0, 1});

        while (!pq.empty()) {
            State top = pq.top();
            pq.pop();
            int d = top.d, u = top.u, c = top.c;

            if (d > dist[u][c]) continue;
            if (u == n - 1) return d;

            char label_u = labels[u];
            for (auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;
                int nc = (label_u == labels[v]) ? c + 1 : 1;

                if (nc <= k && d + w < dist[v][nc]) {
                    dist[v][nc] = d + w;
                    pq.push({dist[v][nc], v, nc});
                }
            }
        }

        return -1;
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
    static class State implements Comparable<State> {
        int d, u, c;
        State(int d, int u, int c) {
            this.d = d;
            this.u = u;
            this.c = c;
        }
        public int compareTo(State other) {
            return Integer.compare(this.d, other.d);
        }
    }

    public int shortestPath(int n, int[][] edges, String labels, int k) {
        List<int[]>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(new int[]{e[1], e[2]});
        }

        int[][] dist = new int[n][k + 1];
        for (int i = 0; i < n; i++) Arrays.fill(dist[i], Integer.MAX_VALUE);

        PriorityQueue<State> pq = new PriorityQueue<>();
        dist[0][1] = 0;
        pq.offer(new State(0, 0, 1));

        while (!pq.isEmpty()) {
            State top = pq.poll();
            int d = top.d, u = top.u, c = top.c;

            if (d > dist[u][c]) continue;
            if (u == n - 1) return d;

            char labelU = labels.charAt(u);
            for (int[] edge : adj[u]) {
                int v = edge[0];
                int w = edge[1];
                int nc = (labelU == labels.charAt(v)) ? c + 1 : 1;

                if (nc <= k && d != Integer.MAX_VALUE && d + w < dist[v][nc]) {
                    dist[v][nc] = d + w;
                    pq.offer(new State(dist[v][nc], v, nc));
                }
            }
        }

        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import heapq

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        max_c = k + 1
        dist = [float('inf')] * (n * max_c)

        dist[0 * max_c + 1] = 0
        pq = [(0, 0, 1)] # (distance, node, count)

        while pq:
            d, u, c = heapq.heappop(pq)

            if d > dist[u * max_c + c]:
                continue
            if u == n - 1:
                return d

            label_u = labels[u]
            for v, w in adj[u]:
                nc = c + 1 if label_u == labels[v] else 1
                if nc <= k:
                    idx = v * max_c + nc
                    if d + w < dist[idx]:
                        dist[idx] = d + w
                        heapq.heappush(pq, (d + w, v, nc))
        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int: 
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        max_c = k + 1
        dist = [float('inf')] * (n * max_c)

        dist[0 * max_c + 1] = 0
        pq = [(0, 0, 1)] # (distance, node, count)

        while pq:
            d, u, c = heapq.heappop(pq)

            if d > dist[u * max_c + c]:
                continue
            if u == n - 1:
                return d

            label_u = labels[u]
            for v, w in adj[u]:
                nc = c + 1 if label_u == labels[v] else 1
                if nc <= k:
                    idx = v * max_c + nc
                    if d + w < dist[idx]:
                        dist[idx] = d + w
                        heapq.heappush(pq, (d + w, v, nc))

        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>
#include <limits.h>

typedef struct {
    int d, u, c;
} State;

typedef struct {
    int to, weight, next;
} Edge;

void push(State* heap, int* heapSize, int d, int u, int c) {
    int i = ++(*heapSize);
    while (i > 1 && d < heap[i / 2].d) {
        heap[i] = heap[i / 2];
        i /= 2;
    }
    heap[i].d = d;
    heap[i].u = u;
    heap[i].c = c;
}

State pop(State* heap, int* heapSize) {
    State res = heap[1];
    State last = heap[(*heapSize)--];
    int i = 1, child;
    while (i * 2 <= *heapSize) {
        child = i * 2;
        if (child < *heapSize && heap[child + 1].d < heap[child].d) child++;
        if (last.d <= heap[child].d) break;
        heap[i] = heap[child];
        i = child;
    }
    heap[i] = last;
    return res;
}

int shortestPath(int n, int** edges, int edgesSize, int* edgesColSize, char* labels, int k) {
    Edge* e = (Edge*)malloc(sizeof(Edge) * edgesSize);
    int* head = (int*)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) head[i] = -1;
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0];
        e[i].to = edges[i][1];
        e[i].weight = edges[i][2];
        e[i].next = head[u];
        head[u] = i;
    }

    int max_c = k + 1;
    int* dist = (int*)malloc(sizeof(int) * n * max_c);
    for (int i = 0; i < n * max_c; i++) dist[i] = INT_MAX;

    State* heap = (State*)malloc(sizeof(State) * (edgesSize * k + 100));
    int heapSize = 0;

    dist[0 * max_c + 1] = 0;
    push(heap, &heapSize, 0, 0, 1);

    while (heapSize > 0) {
        State top = pop(heap, &heapSize);
        int d = top.d, u = top.u, c = top.c;

        if (d > dist[u * max_c + c]) continue;
        if (u == n - 1) {
            free(e); free(head); free(dist); free(heap);
            return d;
        }

        for (int i = head[u]; i != -1; i = e[i].next) {
            int v = e[i].to;
            int w = e[i].weight;
            int nc = (labels[u] == labels[v]) ? c + 1 : 1;
            if (nc <= k) {
                if (d + w < dist[v * max_c + nc]) {
                    dist[v * max_c + nc] = d + w;
                    push(heap, &heapSize, d + w, v, nc);
                }
            }
        }
    }

    free(e); free(head); free(dist); free(heap);
    return -1;
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
    public int ShortestPath(int n, int[][] edges, string labels, int k) {
        if (n == 0) return -1;
        if (n == 1) return 0;

        List<(int to, int weight)>[] adj = new List<(int, int)>[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new List<(int, int)>();
        }
        foreach (var edge in edges) {
            adj[edge[0]].Add((edge[1], edge[2]));
        }

        long[] dist = new long[n * (k + 1)];
        Array.Fill(dist, long.MaxValue);

        PriorityQueue<(int node, int count), long> pq = new PriorityQueue<(int node, int count), long>();

        dist[0 * (k + 1) + 1] = 0;
        pq.Enqueue((0, 1), 0);

        while (pq.Count > 0) {
            if (pq.TryDequeue(out var state, out long d)) {
                int u = state.node;
                int count = state.count;

                if (d > dist[u * (k + 1) + count]) continue;
                if (u == n - 1) return (int)d;

                foreach (var edge in adj[u]) {
                    int v = edge.to;
                    int w = edge.weight;
                    int nextCount = (labels[u] == labels[v]) ? count + 1 : 1;

                    if (nextCount <= k) {
                        if (dist[v * (k + 1) + nextCount] > d + w) {
                            dist[v * (k + 1) + nextCount] = d + w;
                            pq.Enqueue((v, nextCount), dist[v * (k + 1) + nextCount]);
                        }
                    }
                }
            }
        }

        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {string} labels
 * @param {number} k
 * @return {number}
 */
var shortestPath = function(n, edges, labels, k) {
    if (n === 1) return 0;

    const adj = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
    }

    const INF = 1000000000;
    const dist = new Int32Array(n * (k + 1)).fill(INF);

    class MinHeap {
        constructor() {
            this.heap = [];
        }
        push(priority, node, count) {
            this.heap.push({ priority, node, count });
            this.bubbleUp();
        }
        pop() {
            if (this.heap.length === 0) return null;
            if (this.heap.length === 1) return this.heap.pop();
            const top = this.heap[0];
            this.heap[0] = this.heap.pop();
            this.bubbleDown();
            return top;
        }
        bubbleUp() {
            let idx = this.heap.length - 1;
            while (idx > 0) {
                let p = (idx - 1) >> 1;
                if (this.heap[p].priority <= this.heap[idx].priority) break;
                let temp = this.heap[p];
                this.heap[p] = this.heap[idx];
                this.heap[idx] = temp;
                idx = p;
            }
        }
        bubbleDown() {
            let idx = 0;
            while (true) {
                let l = (idx << 1) + 1, r = (idx << 1) + 2, s = idx;
                if (l < this.heap.length && this.heap[l].priority < this.heap[s].priority) s = l;
                if (r < this.heap.length && this.heap[r].priority < this.heap[s].priority) s = r;
                if (s === idx) break;
                let temp = this.heap[idx];
                this.heap[idx] = this.heap[s];
                this.heap[s] = temp;
                idx = s;
            }
        }
    }

    const pq = new MinHeap();
    dist[0 * (k + 1) + 1] = 0;
    pq.push(0, 0, 1);

    while (pq.heap.length > 0) {
        const { priority: d, node: u, count } = pq.pop();

        if (d > dist[u * (k + 1) + count]) continue;
        if (u === n - 1) return d;

        for (const [v, w] of adj[u]) {
            const nextCount = (labels[u] === labels[v]) ? count + 1 : 1;
            if (nextCount <= k) {
                const newDist = d + w;
                if (newDist < dist[v * (k + 1) + nextCount]) {
                    dist[v * (k + 1) + nextCount] = newDist;
                    pq.push(newDist, v, nextCount);
                }
            }
        }
    }

    return -1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function shortestPath(n: number, edges: number[][], labels: string, k: number): number {
    if (n === 1) return 0;

    const adj: [number, number][][] = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
    }

    const INF = 1000000000;
    const dist = new Int32Array(n * (k + 1)).fill(INF);

    class MinHeap {
        public heap: { priority: number, node: number, count: number }[] = [];
        push(priority: number, node: number, count: number) {
            this.heap.push({ priority, node, count });
            this.bubbleUp();
        }
        pop() {
            if (this.heap.length === 0) return null;
            if (this.heap.length === 1) return this.heap.pop();
            const top = this.heap[0];
            this.heap[0] = this.heap.pop()!;
            this.bubbleDown();
            return top;
        }
        private bubbleUp() {
            let idx = this.heap.length - 1;
            while (idx > 0) {
                let p = (idx - 1) >> 1;
                if (this.heap[p].priority <= this.heap[idx].priority) break;
                let temp = this.heap[p];
                this.heap[p] = this.heap[idx];
                this.heap[idx] = temp;
                idx = p;
            }
        }
        private bubbleDown() {
            let idx = 0;
            while (true) {
                let l = (idx << 1) + 1, r = (idx << 1) + 2, s = idx;
                if (l < this.heap.length && this.heap[l].priority < this.heap[s].priority) s = l;
                if (r < this.heap.length && this.heap[r].priority < this.heap[s].priority) s = r;
                if (s === idx) break;
                let temp = this.heap[idx];
                this.heap[idx] = this.heap[s];
                this.heap[s] = temp;
                idx = s;
            }
        }
    }

    const pq = new MinHeap();
    dist[0 * (k + 1) + 1] = 0;
    pq.push(0, 0, 1);

    while (pq.heap.length > 0) {
        const current = pq.pop();
        if (!current) break;
        const { priority: d, node: u, count } = current;

        if (d > dist[u * (k + 1) + count]) continue;
        if (u === n - 1) return d;

        for (const [v, w] of adj[u]) {
            const nextCount = (labels[u] === labels[v]) ? count + 1 : 1;
            if (nextCount <= k) {
                const newDist = d + w;
                if (newDist < dist[v * (k + 1) + nextCount]) {
                    dist[v * (k + 1) + nextCount] = newDist;
                    pq.push(newDist, v, nextCount);
                }
            }
        }
    }

    return -1;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param String $labels
     * @param Integer $k
     * @return Integer
     */
    function shortestPath($n, $edges, $labels, $k) {
        if ($n === 1) return 0;

        $adj = array_fill(0, $n, []);
        foreach ($edges as $edge) {
            $adj[$edge[0]][] = [$edge[1], $edge[2]];
        }

        $inf = 1000000000;
        $distSize = $n * ($k + 1);
        $dist = new SplFixedArray($distSize);
        for ($i = 0; $i < $distSize; $i++) $dist[$i] = $inf;

        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);

        $dist[1] = 0; // 0 * (k + 1) + 1
        $pq->insert([0, 1], 0);

        while (!$pq->isEmpty()) {
            $item = $pq->extract();
            $u = $item['data'][0];
            $count = $item['data'][1];
            $d = -$item['priority'];

            if ($d > $dist[$u * ($k + 1) + $count]) continue;
            if ($u == $n - 1) return $d;

            if (isset($adj[$u])) {
                foreach ($adj[$u] as $edge) {
                    $v = $edge[0];
                    $w = $edge[1];
                    $nextCount = ($labels[$u] == $labels[$v]) ? $count + 1 : 1;
                    if ($nextCount <= $k) {
                        $newDist = $d + $w;
                        $idx = $v * ($k + 1) + $nextCount;
                        if ($newDist < $dist[$idx]) {
                            $dist[$idx] = $newDist;
                            $pq->insert([$v, $nextCount], -$newDist);
                        }
                    }
                }
            }
        }

        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    struct State {
        let node: Int
        let count: Int
        let dist: Int
    }

    struct MinHeap {
        var heap: [State] = []
        mutating func push(_ state: State) {
            heap.append(state)
            var idx = heap.count - 1
            while idx > 0 {
                let p = (idx - 1) / 2
                if heap[idx].dist < heap[p].dist {
                    heap.swapAt(idx, p)
                    idx = p
                } else {
                    break
                }
            }
        }
        mutating func pop() -> State? {
            if heap.isEmpty { return nil }
            if heap.count == 1 { return heap.removeLast() }
            let res = heap[0]
            heap[0] = heap.removeLast()
            var idx = 0
            while true {
                let l = 2 * idx + 1, r = 2 * idx + 2
                var s = idx
                if l < heap.count && heap[l].dist < heap[s].dist { s = l }
                if r < heap.count && heap[r].dist < heap[s].dist { s = r }
                if s == idx { break }
                heap.swapAt(idx, s)
                idx = s
            }
            return res
        }
    }

    func shortestPath(_ n: Int, _ edges: [[Int]], _ labels: String, _ k: Int) -> Int {
        if n == 1 { return 0 }

        let labelArr = Array(labels)
        var adj = [[(to: Int, weight: Int)]](repeating: [], count: n)
        for edge in edges {
            adj[edge[0]].append((edge[1], edge[2]))
        }

        var dist = [Int](repeating: Int.max, count: n * (k + 1))
        var pq = MinHeap()

        dist[0 * (k + 1) + 1] = 0
        pq.push(State(node: 0, count: 1, dist: 0))

        while let state = pq.pop() {
            let u = state.node
            let count = state.count
            let d = state.dist

            if d > dist[u * (k + 1) + count] { continue }
            if u == n - 1 { return d }

            for edge in adj[u] {
                let v = edge.to
                let w = edge.weight
                let nextCount = (labelArr[u] == labelArr[v]) ? count + 1 : 1

                if nextCount <= k {
                    let newDist = d + w
                    if newDist < dist[v * (k + 1) + nextCount] {
                        dist[v * (k + 1) + nextCount] = newDist
                        pq.push(State(node: v, count: nextCount, dist: newDist))
                    }
                }
            }
        }

        return -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.PriorityQueue

class Solution {
    data class Edge(val to: Int, val weight: Int)
    data class State(val dist: Int, val u: Int, val c: Int)

    fun shortestPath(n: Int, edges: Array<IntArray>, labels: String, k: Int): Int {
        val adj = Array(n) { mutableListOf<Edge>() }
        for (edge in edges) {
            adj[edge[0]].add(Edge(edge[1], edge[2]))
        }

        val inf = 1000000000
        val dist = IntArray(n * (k + 1)) { inf }
        val pq = PriorityQueue<State>(compareBy { it.dist })

        dist[1] = 0
        pq.offer(State(0, 0, 1))

        while (pq.isNotEmpty()) {
            val (d, u, c) = pq.poll()

            if (d > dist[u * (k + 1) + c]) continue

            for (edge in adj[u]) {
                val v = edge.to
                val w = edge.weight
                val nc = if (labels[u] == labels[v]) c + 1 else 1

                if (nc <= k) {
                    if (d + w < dist[v * (k + 1) + nc]) {
                        dist[v * (k + 1) + nc] = d + w
                        pq.offer(State(dist[v * (k + 1) + nc], v, nc))
                    }
                }
            }
        }

        var minWeight = inf
        for (c in 1..k) {
            minWeight = minOf(minWeight, dist[(n - 1) * (k + 1) + c])
        }

        return if (minWeight == inf) -1 else minWeight
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

class Edge {
  final int to;
  final int weight;
  Edge(this.to, this.weight);
}

class PriorityQueue {
  final List<List<int>> heap = [];

  void push(List<int> val) {
    heap.add(val);
    int idx = heap.length - 1;
    while (idx > 0) {
      int parent = (idx - 1) ~/ 2;
      if (heap[idx][0] < heap[parent][0]) {
        List<int> tmp = heap[idx];
        heap[idx] = heap[parent];
        heap[parent] = tmp;
        idx = parent;
      } else {
        break;
      }
    }
  }

  List<int> pop() {
    if (heap.isEmpty) return [];
    if (heap.length == 1) return heap.removeLast();
    List<int> res = heap[0];
    heap[0] = heap.removeLast();
    int idx = 0;
    while (true) {
      int left = 2 * idx + 1;
      int right = 2 * idx + 2;
      int small = idx;
      if (left < heap.length && heap[left][0] < heap[small][0]) small = left;
      if (right < heap.length && heap[right][0] < heap[small][0]) small = right;
      if (small == idx) break;
      List<int> tmp = heap[idx];
      heap[idx] = heap[small];
      heap[small] = tmp;
      idx = small;
    }
    return res;
  }

  bool get isEmpty => heap.isEmpty;
  bool get isNotEmpty => heap.isNotEmpty;
}

class Solution {
  int shortestPath(int n, List<List<int>> edges, String labels, int k) {
    List<List<Edge>> adj = List.generate(n, (i) => <Edge>[]);
    for (var edge in edges) {
      adj[edge[0]].add(Edge(edge[1], edge[2]));
    }

    const int inf = 1000000000;
    List<int> dist = List.filled(n * (k + 1), inf);
    PriorityQueue pq = PriorityQueue();

    dist[1] = 0;
    pq.push([0, 0, 1]);

    while (pq.isNotEmpty) {
      List<int> cur = pq.pop();
      int d = cur[0];
      int u = cur[1];
      int c = cur[2];

      if (d > dist[u * (k + 1) + c]) continue;

      for (var edge in adj[u]) {
        int v = edge.to;
        int w = edge.weight;
        int nc = (labels[u] == labels[v]) ? c + 1 : 1;

        if (nc <= k) {
          if (d + w < dist[v * (k + 1) + nc]) {
            dist[v * (k + 1) + nc] = d + w;
            pq.push([dist[v * (k + 1) + nc], v, nc]);
          }
        }
      }
    }

    int minWeight = inf;
    for (int c = 1; c <= k; c++) {
      minWeight = min(minWeight, dist[(n - 1) * (k + 1) + c]);
    }

    return minWeight == inf ? -1 : minWeight;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
	"container/heap"
)

type Edge struct {
	to     int
	weight int
}

type Item struct {
	dist, u, c int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int           { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool { return pq[i].dist < pq[j].dist }
func (pq PriorityQueue) Swap(i, j int)      { pq[i], pq[j] = pq[j], pq[i] }

func (pq *PriorityQueue) Push(x interface{}) {
	*pq = append(*pq, x.(*Item))
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	*pq = old[0 : n-1]
	return item
}

func shortestPath(n int, edges [][]int, labels string, k int) int {
	adj := make([][]Edge, n)
	for _, edge := range edges {
		u, v, w := edge[0], edge[1], edge[2]
		adj[u] = append(adj[u], Edge{v, w})
	}

	inf := 1000000000
	dist := make([]int, n*(k+1))
	for i := range dist {
		dist[i] = inf
	}

	pq := &PriorityQueue{}
	heap.Init(pq)

	dist[1] = 0
	heap.Push(pq, &Item{0, 0, 1})

	for pq.Len() > 0 {
		curr := heap.Pop(pq).(*Item)
		d, u, c := curr.dist, curr.u, curr.c

		if d > dist[u*(k+1)+c] {
			continue
		}

		for _, edge := range adj[u] {
			v, w := edge.to, edge.weight
			nc := 1
			if labels[u] == labels[v] {
				nc = c + 1
			}

			if nc <= k {
				if d+w < dist[v*(k+1)+nc] {
					dist[v*(k+1)+nc] = d + w
					heap.Push(pq, &Item{dist[v*(k+1)+nc], v, nc})
				}
			}
		}
	}

	minWeight := inf
	for c := 1; c <= k; c++ {
		if dist[(n-1)*(k+1)+c] < minWeight {
			minWeight = dist[(n-1)*(k+1)+c]
		}
	}

	if minWeight == inf {
		return -1
	}
	return minWeight
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @param {Integer[][]} edges
# @param {String} labels
# @param {Integer} k
# @return {Integer}
def shortest_path(n, edges, labels, k)
  adj = Array.new(n) { [] }
  edges.each do |u, v, w|
    adj[u] << [v, w]
  end

  inf = 1_000_000_000
  dist = Array.new(n * (k + 1), inf)

  pq = PriorityQueue.new
  dist[1] = 0
  pq.push([0, 0, 1])

  while !pq.empty?
    d, u, c = pq.pop
    next if d > dist[u * (k + 1) + c]

    adj[u].each do |v, w|
      nc = (labels[u] == labels[v]) ? c + 1 : 1
      if nc <= k
        if d + w < dist[v * (k + 1) + nc]
          dist[v * (k + 1) + nc] = d + w
          pq.push([dist[v * (k + 1) + nc], v, nc])

        end
      end
    end
  end

  ans = inf
  (1..k).each do |c|
    ans = [ans, dist[(n - 1) * (k + 1) + c]].min
  end

  ans == inf ? -1 : ans
end

class PriorityQueue
  def initialize
    @heap = []
  end

  def push(val)
    @heap << val
    idx = @heap.size - 1
    while idx > 0
      parent = (idx - 1) / 2
      if @heap[idx][0] < @heap[parent][0]
        @heap[idx], @heap[parent] = @heap[parent], @heap[idx]
        idx = parent
      else
        break
      end
    end
  end

  def pop
    return nil if @heap.empty?
    return @heap.pop if @heap.size == 1
    res = @heap[0]
    @heap[0] = @heap.pop
    idx = 0
    while (left = 2 * idx + 1) < @heap.size
      right = left + 1
      small = left
      if right < @heap.size && @heap[right][0] < @heap[left][0]
        small = right
      end
      if @heap[idx][0] <= @heap[small][0]
        break
      end
      @heap[idx], @heap[small] = @heap[small], @heap[idx]
      idx = small
    end
    res
  end

  def empty?
    @heap.empty?
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
    case class Edge(to: Int, weight: Int)
    case class State(dist: Int, u: Int, c: Int)

    def shortestPath(n: Int, edges: Array[Array[Int]], labels: String, k: Int): Int = {
        val adj = Array.fill(n)(mutable.ArrayBuffer[Edge]())
        for (edge <- edges) {
            adj(edge(0)) += Edge(edge(1), edge(2))
        }

        val inf = 1000000000
        val dist = Array.fill(n * (k + 1))(inf)
        val pq = mutable.PriorityQueue[State]()(Ordering.by(-_.dist))

        dist(1) = 0
        pq.enqueue(State(0, 0, 1))

        while (pq.nonEmpty) {
            val State(d, u, c) = pq.dequeue()

            if (d <= dist(u * (k + 1) + c)) {
                for (edge <- adj(u)) {
                    val v = edge.to
                    val w = edge.weight
                    val nc = if (labels(u) == labels(v)) c + 1 else 1

                    if (nc <= k) {
                        if (d + w < dist(v * (k + 1) + nc)) {
                            dist(v * (k + 1) + nc) = d + w
                            pq.enqueue(State(d + w, v, nc))
                        }
                    }
                }
            }
        }

        var minWeight = inf
        for (c <- 1 to k) {
            if (dist((n - 1) * (k + 1) + c) < minWeight) {
                minWeight = dist((n - 1) * (k + 1) + c)
            }
        }

        if (minWeight == inf) -1 else minWeight
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn shortest_path(n: i32, edges: Vec<Vec<i32>>, labels: String, k: i32) -> i32 {
        let n = n as usize;
        let k = k as usize;
        let labels = labels.as_bytes();
        let mut adj = vec![vec![]; n];
        for edge in edges {
            adj[edge[0] as usize].push((edge[1] as usize, edge[2]));
        }

        let mut dist = vec![i32::MAX; n * (k + 1)];
        let mut pq = BinaryHeap::new();

        if n > 0 {
            let start_idx = 1; 
            dist[start_idx] = 0;
            pq.push(Reverse((0, 0, 1)));
        }

        while let Some(Reverse((d, u, c1))) = pq.pop() {
            if d > dist[u * (k + 1) + c1] {
                continue;
            }
            if u == n - 1 {
                return d;
            }

            for &(v, w) in &adj[u] {
                let c2 = if labels[u] == labels[v] {
                    c1 + 1
                } else {
                    1
                };
                if c2 <= k {
                    let next_d = d + w;
                    let next_idx = v * (k + 1) + c2;
                    if next_d < dist[next_idx] {
                        dist[next_idx] = next_d;
                        pq.push(Reverse((next_d, v, c2)));
                    }
                }
            }
        }

        -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(require data/heap)

(define/contract (shortest-path n edges labels k)
  (-> exact-integer? (listof (listof exact-integer?)) string? exact-integer? exact-integer?)
  (let* ([k-plus-1 (+ k 1)]
         [adj (make-vector n '())]
         [dist (make-vector (* n k-plus-1) +inf.0)]
         [pq (make-heap (lambda (a b) (<= (car a) (car b))))])
    (for ([edge edges])
      (let ([u (first edge)]
            [v (second edge)]
            [w (third edge)])
        (vector-set! adj u (cons (list v w) (vector-ref adj u)))))

    (vector-set! dist 1 0)
    (heap-add! pq (list 0 0 1))

    (let loop ()
      (if (zero? (heap-count pq))
          -1
          (let* ([top (heap-min pq)]
                 [d (first top)]
                 [u (second top)]
                 [c1 (third top)])
            (heap-remove-min! pq)
            (if (= u (- n 1))
                d
                (begin
                  (if (<= d (vector-ref dist (+ (* u k-plus-1) c1)))
                      (for ([edge (vector-ref adj u)])
                        (let* ([v (first edge)]
                               [w (second edge)]
                               [c2 (if (char=? (string-ref labels u) (string-ref labels v))
                                       (+ c1 1)
                                       1)])
                          (when (<= c2 k)
                            (let* ([idx (+ (* v k-plus-1) c2)]
                                   [old-d (vector-ref dist idx)]
                                   [new-d (+ d w)])
                              (when (< new-d old-d)
                                (vector-set! dist idx new-d)
                                (heap-add! pq (list new-d v c2)))))))
                      (void))
                  (loop))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec shortest_path(N :: integer(), Edges :: [[integer()]], Labels :: unicode:unicode_binary(), K :: integer()) -> integer().
shortest_path(N, Edges, Labels, K) ->
  Adj = build_adj(Edges, maps:new()),
  LabelsTuple = list_to_tuple(binary_to_list(Labels)),
  PQ = gb_sets:add_element({0, 0, 1}, gb_sets:empty()),
  Dist = maps:put({0, 1}, 0, maps:new()),
  dijkstra(PQ, Dist, Adj, LabelsTuple, K, N).

build_adj([], Map) -> Map;
build_adj([[U, V, W] | T], Map) ->
  List = maps:get(U, Map, []),
  build_adj(T, maps:put(U, [{V, W} | List], Map)).

dijkstra(PQ, Dist, Adj, Labels, K, N) ->
  case gb_sets:is_empty(PQ) of
    true -> -1;
    false ->
      {{D, U, C1}, PQ1} = gb_sets:take_shortest(PQ),
      case U == N - 1 of
        true -> D;
        false ->
          case D > maps:get({U, C1}, Dist, infinity) of
            true -> dijkstra(PQ1, Dist, Adj, Labels, K, N);
            false ->
              {NewPQ, NewDist} = process_neighbors(maps:get(U, Adj, []), D, U, C1, PQ1, Dist, Labels, K),
              dijkstra(NewPQ, NewDist, Adj, Labels, K, N)
          end
      end
  end.

process_neighbors([], _D, _U, _C1, PQ, Dist, _Labels, _K) -> {PQ, Dist};
process_neighbors([{V, W} | T], D, U, C1, PQ, Dist, Labels, K) ->
  C2 = case element(U + 1, Labels) == element(V + 1, Labels) of
    true -> C1 + 1;
    false -> 1
  end,
  if C2 =< K ->
    NewD = D + W,
    OldD = maps:get({V, C2}, Dist, infinity),
    if NewD < OldD ->
      process_neighbors(T, D, U, C1, gb_sets:add_element({NewD, V, C2}, PQ), maps:put({V, C2}, NewD, Dist), Labels, K);
    true ->
      process_neighbors(T, D, U, C1, PQ, Dist, Labels, K)
    end;
  true ->
    process_neighbors(T, D, U, C1, PQ, Dist, Labels, K)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec shortest_path(n :: integer, edges :: [[integer]], labels :: String.t, k :: integer) :: integer
  def shortest_path(n, edges, labels, k) do
    adj = Enum.reduce(edges, %{}, fn [u, v, w], acc ->
      Map.update(acc, u, [{v, w}], &([{v, w} | &1]))
    end)

    labels_tuple = labels |> String.to_charlist() |> List.to_tuple()

    pq = :gb_sets.add_element({0, 0, 1}, :gb_sets.empty())
    dist = %{{0, 1} => 0}

    dijkstra(pq, dist, adj, labels_tuple, k, n)
  end

  defp dijkstra(pq, dist, adj, labels, k, n) do
    if :gb_sets.is_empty(pq) do
      -1
    else
      {{d, u, c1}, pq1} = :gb_sets.take_shortest(pq)

      cond do
        u == n - 1 ->
          d
        d > Map.get(dist, {u, c1}, :infinity) ->
          dijkstra(pq1, dist, adj, labels, k, n)
        true ->
          {new_pq, new_dist} = process_neighbors(Map.get(adj, u, []), d, u, c1, pq1, dist, labels, k)
          dijkstra(new_pq, new_dist, adj, labels, k, n)
      end
    end
  end

  defp process_neighbors([], _d, _u, _c1, pq, dist, _labels, _k), do: {pq, dist}
  defp process_neighbors([{v, w} | tail], d, u, c1, pq, dist, labels, k) do
    c2 = if elem(labels, u) == elem(labels, v), do: c1 + 1, else: 1

    if c2 <= k do
      new_d = d + w
      old_d = Map.get(dist, {v, c2}, :infinity)

      if new_d < old_d do
        process_neighbors(tail, d, u, c1, :gb_sets.add_element({new_d, v, c2}, pq), Map.put(dist, {v, c2}, new_d), labels, k)
      else
        process_neighbors(tail, d, u, c1, pq, dist, labels, k)
      end
    else
      process_neighbors(tail, d, u, c1, pq, dist, labels, k)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(M \cdot K \cdot \log(N \cdot K)) where $N$ is the number of nodes, $M$ is the number of edges, and $K$ is the maximum consecutive character constraint. The expanded graph has $N \cdot K$ states and $M \cdot K$ possible transitions, and Dijkstra's algorithm performs log-time priority queue operations for each transition.
- **Space Complexity:** O(N \cdot K + M) to store the adjacency list for the original $M$ edges and the distance array for the $N \cdot K$ states in the expanded graph.
