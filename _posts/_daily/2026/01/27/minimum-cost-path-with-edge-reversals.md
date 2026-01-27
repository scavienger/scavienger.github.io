---
layout: post
title: "Minimum Cost Path with Edge Reversals"
date: 2026-01-27 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Graph Theory", "Heap (Priority Queue)", "Shortest Path"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minCost(int n, vector<vector<int>>& edges)\
        \ {\n        vector<vector<pair<int, int>>> adj(n);\n        for (auto& edge\
        \ : edges) {\n            int u = edge[0], v = edge[1], w = edge[2];\n     \
        \       adj[u].push_back({v, w});\n            adj[v].push_back({u, 2 * w});\n\
        \        }\n\n        vector<long long> dist(n, LLONG_MAX);\n        priority_queue<pair<long\
        \ long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;\n\
        \n        dist[0] = 0;\n        pq.push({0LL, 0});\n\n        while (!pq.empty())\
        \ {\n            long long d = pq.top().first;\n            int u = pq.top().second;\n\
        \            pq.pop();\n\n            if (d > dist[u]) continue;\n\n       \
        \     for (auto& edge : adj[u]) {\n                int v = edge.first;\n   \
        \             int w = edge.second;\n                if (dist[u] + w < dist[v])\
        \ {\n                    dist[v] = dist[u] + w;\n                    pq.push({dist[v],\
        \ v});\n                }\n            }\n        }\n\n        return dist[n\
        \ - 1] == LLONG_MAX ? -1 : (int)dist[n - 1];\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int minCost(int n,\
        \ int[][] edges) {\n        List<int[]>[] adj = new ArrayList[n];\n        for\
        \ (int i = 0; i < n; i++) adj[i] = new ArrayList<>();\n        for (int[] edge\
        \ : edges) {\n            int u = edge[0], v = edge[1], w = edge[2];\n     \
        \       adj[u].add(new int[]{v, w});\n            adj[v].add(new int[]{u, 2\
        \ * w});\n        }\n\n        long[] dist = new long[n];\n        Arrays.fill(dist,\
        \ Long.MAX_VALUE);\n        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a\
        \ -> a[1]));\n\n        dist[0] = 0;\n        pq.offer(new long[]{0, 0});\n\n\
        \        while (!pq.isEmpty()) {\n            long[] curr = pq.poll();\n   \
        \         int u = (int) curr[0];\n            long d = curr[1];\n\n        \
        \    if (d > dist[u]) continue;\n\n            for (int[] neighbor : adj[u])\
        \ {\n                int v = neighbor[0];\n                int w = neighbor[1];\n\
        \                if (dist[u] + w < dist[v]) {\n                    dist[v] =\
        \ dist[u] + w;\n                    pq.offer(new long[]{v, dist[v]});\n    \
        \            }\n            }\n        }\n\n        return dist[n - 1] == Long.MAX_VALUE\
        \ ? -1 : (int) dist[n - 1];\n    }\n}"
      python: "import heapq\n\nclass Solution(object):\n    def minCost(self, n, edges):\n\
        \        \"\"\"\n        :type n: int\n        :type edges: List[List[int]]\n\
        \        :rtype: int\n        \"\"\"\n        adj = [[] for _ in range(n)]\n\
        \        for u, v, w in edges:\n            adj[u].append((v, w))\n        \
        \    adj[v].append((u, 2 * w))\n\n        dist = [float('inf')] * n\n      \
        \  dist[0] = 0\n        pq = [(0, 0)]\n\n        while pq:\n            d, u\
        \ = heapq.heappop(pq)\n\n            if d > dist[u]:\n                continue\n\
        \n            for v, w in adj[u]:\n                if dist[u] + w < dist[v]:\n\
        \                    dist[v] = dist[u] + w\n                    heapq.heappush(pq,\
        \ (dist[v], v))\n\n        return int(dist[n - 1]) if dist[n - 1] != float('inf')\
        \ else -1"
      python3: "import heapq\nfrom typing import List\n\nclass Solution:\n    def minCost(self,\
        \ n: int, edges: List[List[int]]) -> int:\n        adj = [[] for _ in range(n)]\n\
        \        for u, v, w in edges:\n            adj[u].append((v, w))\n        \
        \    adj[v].append((u, 2 * w))\n\n        dist = [float('inf')] * n\n      \
        \  dist[0] = 0\n        pq = [(0, 0)]\n\n        while pq:\n            d, u\
        \ = heapq.heappop(pq)\n\n            if d > dist[u]:\n                continue\n\
        \n            for v, w in adj[u]:\n                if dist[u] + w < dist[v]:\n\
        \                    dist[v] = dist[u] + w\n                    heapq.heappush(pq,\
        \ (dist[v], v))\n\n        return int(dist[n - 1]) if dist[n - 1] != float('inf')\
        \ else -1"
      c: "#include <stdlib.h>\n#include <limits.h>\n\ntypedef struct {\n    long long\
        \ cost;\n    int node;\n} HeapNode;\n\ntypedef struct {\n    HeapNode* data;\n\
        \    int size;\n} MinHeap;\n\nvoid push(MinHeap* heap, long long cost, int node)\
        \ {\n    int i = heap->size++;\n    while (i > 0) {\n        int p = (i - 1)\
        \ / 2;\n        if (heap->data[p].cost <= cost) break;\n        heap->data[i]\
        \ = heap->data[p];\n        i = p;\n    }\n    heap->data[i].cost = cost;\n\
        \    heap->data[i].node = node;\n}\n\nHeapNode pop(MinHeap* heap) {\n    HeapNode\
        \ res = heap->data[0];\n    HeapNode last = heap->data[--heap->size];\n    int\
        \ i = 0;\n    while (i * 2 + 1 < heap->size) {\n        int child = i * 2 +\
        \ 1;\n        if (child + 1 < heap->size && heap->data[child + 1].cost < heap->data[child].cost)\
        \ child++;\n        if (last.cost <= heap->data[child].cost) break;\n      \
        \  heap->data[i] = heap->data[child];\n        i = child;\n    }\n    heap->data[i]\
        \ = last;\n    return res;\n}\n\nint minCost(int n, int** edges, int edgesSize,\
        \ int* edgesColSize) {\n    int* head = (int*)malloc(n * sizeof(int));\n   \
        \ for (int i = 0; i < n; i++) head[i] = -1;\n    int* to = (int*)malloc(2 *\
        \ edgesSize * sizeof(int));\n    int* weight = (int*)malloc(2 * edgesSize *\
        \ sizeof(int));\n    int* next = (int*)malloc(2 * edgesSize * sizeof(int));\n\
        \    int edgeCount = 0;\n\n    for (int i = 0; i < edgesSize; i++) {\n     \
        \   int u = edges[i][0], v = edges[i][1], w = edges[i][2];\n        to[edgeCount]\
        \ = v; weight[edgeCount] = w; next[edgeCount] = head[u]; head[u] = edgeCount++;\n\
        \        to[edgeCount] = u; weight[edgeCount] = 2 * w; next[edgeCount] = head[v];\
        \ head[v] = edgeCount++;\n    }\n\n    long long* dist = (long long*)malloc(n\
        \ * sizeof(long long));\n    for (int i = 0; i < n; i++) dist[i] = LLONG_MAX;\n\
        \    dist[0] = 0;\n\n    MinHeap heap;\n    heap.data = (HeapNode*)malloc(2\
        \ * edgesSize * sizeof(HeapNode));\n    heap.size = 0;\n    push(&heap, 0, 0);\n\
        \n    while (heap.size > 0) {\n        HeapNode top = pop(&heap);\n        if\
        \ (top.cost > dist[top.node]) continue;\n        for (int e = head[top.node];\
        \ e != -1; e = next[e]) {\n            if (dist[top.node] + weight[e] < dist[to[e]])\
        \ {\n                dist[to[e]] = dist[top.node] + weight[e];\n           \
        \     push(&heap, dist[to[e]], to[e]);\n            }\n        }\n    }\n\n\
        \    long long result = dist[n - 1];\n    free(head); free(to); free(weight);\
        \ free(next); free(dist); free(heap.data);\n    return result == LLONG_MAX ?\
        \ -1 : (int)result;\n}"
      csharp: "using System.Collections.Generic;\n\npublic class Solution {\n    public\
        \ int MinCost(int n, int[][] edges) {\n        List<(int v, int w)>[] adj =\
        \ new List<(int v, int w)>[n];\n        for (int i = 0; i < n; i++) adj[i] =\
        \ new List<(int v, int w)>();\n        foreach (var edge in edges) {\n     \
        \       int u = edge[0], v = edge[1], w = edge[2];\n            adj[u].Add((v,\
        \ w));\n            adj[v].Add((u, 2 * w));\n        }\n\n        long[] dist\
        \ = new long[n];\n        for (int i = 0; i < n; i++) dist[i] = long.MaxValue;\n\
        \        PriorityQueue<int, long> pq = new PriorityQueue<int, long>();\n\n \
        \       dist[0] = 0;\n        pq.Enqueue(0, 0);\n\n        while (pq.Count >\
        \ 0) {\n            pq.TryDequeue(out int u, out long d);\n            if (d\
        \ > dist[u]) continue;\n\n            foreach (var neighbor in adj[u]) {\n \
        \               if (dist[u] + neighbor.w < dist[neighbor.v]) {\n           \
        \         dist[neighbor.v] = dist[u] + neighbor.w;\n                    pq.Enqueue(neighbor.v,\
        \ dist[neighbor.v]);\n                }\n            }\n        }\n\n      \
        \  return dist[n - 1] == long.MaxValue ? -1 : (int)dist[n - 1];\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number[][]} edges\n * @return\
        \ {number}\n */\nvar minCost = function(n, edges) {\n    const adj = Array.from({\
        \ length: n }, () => []);\n    for (const [u, v, w] of edges) {\n        adj[u].push([v,\
        \ w]);\n        adj[v].push([u, 2 * w]);\n    }\n\n    const dist = new Array(n).fill(Infinity);\n\
        \    dist[0] = 0;\n    const pq = new MinPriorityQueue({ priority: (x) => x.cost\
        \ });\n    pq.enqueue({ node: 0, cost: 0 });\n\n    while (!pq.isEmpty()) {\n\
        \        const { node, cost } = pq.dequeue().element;\n        if (cost > dist[node])\
        \ continue;\n\n        for (const [v, w] of adj[node]) {\n            if (dist[node]\
        \ + w < dist[v]) {\n                dist[v] = dist[node] + w;\n            \
        \    pq.enqueue({ node: v, cost: dist[v] });\n            }\n        }\n   \
        \ }\n\n    return dist[n - 1] === Infinity ? -1 : dist[n - 1];\n};"
      typescript: "class MinHeap {\n    heap: { node: number, dist: number }[] = [];\n\
        \    push(val: { node: number, dist: number }) {\n        this.heap.push(val);\n\
        \        this.bubbleUp();\n    }\n    pop() {\n        if (this.heap.length\
        \ === 0) return null;\n        if (this.heap.length === 1) return this.heap.pop()!;\n\
        \        const top = this.heap[0];\n        this.heap[0] = this.heap.pop()!;\n\
        \        this.bubbleDown();\n        return top;\n    }\n    bubbleUp() {\n\
        \        let index = this.heap.length - 1;\n        while (index > 0) {\n  \
        \          let parent = Math.floor((index - 1) / 2);\n            if (this.heap[parent].dist\
        \ <= this.heap[index].dist) break;\n            [this.heap[parent], this.heap[index]]\
        \ = [this.heap[index], this.heap[parent]];\n            index = parent;\n  \
        \      }\n    }\n    bubbleDown() {\n        let index = 0;\n        while (true)\
        \ {\n            let left = 2 * index + 1, right = 2 * index + 2, smallest =\
        \ index;\n            if (left < this.heap.length && this.heap[left].dist <\
        \ this.heap[smallest].dist) smallest = left;\n            if (right < this.heap.length\
        \ && this.heap[right].dist < this.heap[smallest].dist) smallest = right;\n \
        \           if (smallest === index) break;\n            [this.heap[smallest],\
        \ this.heap[index]] = [this.heap[index], this.heap[smallest]];\n           \
        \ index = smallest;\n        }\n    }\n}\n\nfunction minCost(n: number, edges:\
        \ number[][]): number {\n    const adj: [number, number][][] = Array.from({\
        \ length: n }, () => []);\n    for (const [u, v, w] of edges) {\n        adj[u].push([v,\
        \ w]);\n        adj[v].push([u, 2 * w]);\n    }\n    const dist = new Float64Array(n).fill(Infinity);\n\
        \    dist[0] = 0;\n    const pq = new MinHeap();\n    pq.push({ node: 0, dist:\
        \ 0 });\n    while (pq.heap.length > 0) {\n        const current = pq.pop()!;\n\
        \        const u = current.node;\n        const d = current.dist;\n        if\
        \ (d > dist[u]) continue;\n        if (u === n - 1) return d;\n        for (const\
        \ [v, w] of adj[u]) {\n            if (dist[u] + w < dist[v]) {\n          \
        \      dist[v] = dist[u] + w;\n                pq.push({ node: v, dist: dist[v]\
        \ });\n            }\n        }\n    }\n    return dist[n - 1] === Infinity\
        \ ? -1 : dist[n - 1];\n};"
      php: "class Solution {\n    /**\n     * @param Integer $n\n     * @param Integer[][]\
        \ $edges\n     * @return Integer\n     */\n    function minCost($n, $edges)\
        \ {\n        $adj = array_fill(0, $n, []);\n        foreach ($edges as $edge)\
        \ {\n            $u = $edge[0];\n            $v = $edge[1];\n            $w\
        \ = $edge[2];\n            $adj[$u][] = [$v, $w];\n            $adj[$v][] =\
        \ [$u, 2 * $w];\n        }\n        $dist = array_fill(0, $n, PHP_INT_MAX);\n\
        \        $dist[0] = 0;\n        $pq = new SplPriorityQueue();\n        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);\n\
        \        $pq->insert(0, 0);\n        while (!$pq->isEmpty()) {\n           \
        \ $top = $pq->extract();\n            $u = $top['data'];\n            $d = -$top['priority'];\n\
        \            if ($d > $dist[$u]) continue;\n            if ($u == $n - 1) return\
        \ $d;\n            foreach ($adj[$u] as $neighbor) {\n                $v = $neighbor[0];\n\
        \                $w = $neighbor[1];\n                if ($dist[$u] + $w < $dist[$v])\
        \ {\n                    $dist[$v] = $dist[$u] + $w;\n                    $pq->insert($v,\
        \ -$dist[$v]);\n                }\n            }\n        }\n        return\
        \ $dist[$n - 1] === PHP_INT_MAX ? -1 : $dist[$n - 1];\n    }\n}"
      swift: "class Solution {\n    struct Item {\n        let node: Int\n        let\
        \ dist: Int\n    }\n    class MinHeap {\n        var heap = [Item]()\n     \
        \   func push(_ item: Item) {\n            heap.append(item)\n            var\
        \ curr = heap.count - 1\n            while curr > 0 {\n                let parent\
        \ = (curr - 1) / 2\n                if heap[parent].dist <= heap[curr].dist\
        \ { break }\n                heap.swapAt(parent, curr)\n                curr\
        \ = parent\n            }\n        }\n        func pop() -> Item? {\n      \
        \      if heap.isEmpty { return nil }\n            if heap.count == 1 { return\
        \ heap.removeFirst() }\n            let top = heap[0]\n            heap[0] =\
        \ heap.removeLast()\n            var curr = 0\n            while true {\n  \
        \              let left = 2 * curr + 1, right = 2 * curr + 2\n             \
        \   var smallest = curr\n                if left < heap.count && heap[left].dist\
        \ < heap[smallest].dist { smallest = left }\n                if right < heap.count\
        \ && heap[right].dist < heap[smallest].dist { smallest = right }\n         \
        \       if smallest == curr { break }\n                heap.swapAt(curr, smallest)\n\
        \                curr = smallest\n            }\n            return top\n  \
        \      }\n    }\n    func minCost(_ n: Int, _ edges: [[Int]]) -> Int {\n   \
        \     var adj = Array(repeating: [(Int, Int)](), count: n)\n        for edge\
        \ in edges {\n            adj[edge[0]].append((edge[1], edge[2]))\n        \
        \    adj[edge[1]].append((edge[0], 2 * edge[2]))\n        }\n        var dist\
        \ = Array(repeating: Int.max, count: n)\n        dist[0] = 0\n        let pq\
        \ = MinHeap()\n        pq.push(Item(node: 0, dist: 0))\n        while let current\
        \ = pq.pop() {\n            let u = current.node\n            let d = current.dist\n\
        \            if d > dist[u] { continue }\n            if u == n - 1 { return\
        \ d }\n            for (v, w) in adj[u] {\n                if dist[u] != Int.max\
        \ && dist[u] + w < dist[v] {\n                    dist[v] = dist[u] + w\n  \
        \                  pq.push(Item(node: v, dist: dist[v]))\n                }\n\
        \            }\n        }\n        return dist[n - 1] == Int.max ? -1 : dist[n\
        \ - 1]\n    }\n}"
      kotlin: "import java.util.PriorityQueue\n\nclass Solution {\n    fun minCost(n:\
        \ Int, edges: Array<IntArray>): Int {\n        val adj = Array(n) { mutableListOf<Pair<Int,\
        \ Int>>() }\n        for (edge in edges) {\n            adj[edge[0]].add(Pair(edge[1],\
        \ edge[2]))\n            adj[edge[1]].add(Pair(edge[0], 2 * edge[2]))\n    \
        \    }\n        val dist = IntArray(n) { Int.MAX_VALUE }\n        dist[0] =\
        \ 0\n        val pq = PriorityQueue<Pair<Int, Int>>(compareBy { it.second })\n\
        \        pq.offer(Pair(0, 0))\n        while (pq.isNotEmpty()) {\n         \
        \   val (u, d) = pq.poll()\n            if (d > dist[u]) continue\n        \
        \    if (u == n - 1) return d\n            for ((v, w) in adj[u]) {\n      \
        \          if (dist[u] + w < dist[v]) {\n                    dist[v] = dist[u]\
        \ + w\n                    pq.offer(Pair(v, dist[v]))\n                }\n \
        \           }\n        }\n        return if (dist[n - 1] == Int.MAX_VALUE) -1\
        \ else dist[n - 1]\n    }\n}"
      dart: "import 'dart:collection';\n\nclass Item {\n  final int node;\n  final int\
        \ dist;\n  Item(this.node, this.dist);\n}\n\nclass MinHeap {\n  List<Item> heap\
        \ = [];\n  void push(Item item) {\n    heap.add(item);\n    int curr = heap.length\
        \ - 1;\n    while (curr > 0) {\n      int parent = (curr - 1) ~/ 2;\n      if\
        \ (heap[parent].dist <= heap[curr].dist) break;\n      Item temp = heap[parent];\n\
        \      heap[parent] = heap[curr];\n      heap[curr] = temp;\n      curr = parent;\n\
        \    }\n  }\n  Item pop() {\n    if (heap.length == 1) return heap.removeLast();\n\
        \    Item top = heap[0];\n    heap[0] = heap.removeLast();\n    int curr = 0;\n\
        \    while (true) {\n      int left = 2 * curr + 1, right = 2 * curr + 2, smallest\
        \ = curr;\n      if (left < heap.length && heap[left].dist < heap[smallest].dist)\
        \ smallest = left;\n      if (right < heap.length && heap[right].dist < heap[smallest].dist)\
        \ smallest = right;\n      if (smallest == curr) break;\n      Item temp = heap[smallest];\n\
        \      heap[smallest] = heap[curr];\n      heap[curr] = temp;\n      curr =\
        \ smallest;\n    }\n    return top;\n  }\n  bool get isEmpty => heap.isEmpty;\n\
        }\n\nclass Solution {\n  int minCost(int n, List<List<int>> edges) {\n    List<List<List<int>>>\
        \ adj = List.generate(n, (_) => []);\n    for (var edge in edges) {\n      adj[edge[0]].add([edge[1],\
        \ edge[2]]);\n      adj[edge[1]].add([edge[0], 2 * edge[2]]);\n    }\n    List<int>\
        \ dist = List.filled(n, 2147483647);\n    dist[0] = 0;\n    MinHeap pq = MinHeap();\n\
        \    pq.push(Item(0, 0));\n    while (!pq.isEmpty) {\n      Item current = pq.pop();\n\
        \      int u = current.node, d = current.dist;\n      if (d > dist[u]) continue;\n\
        \      if (u == n - 1) return d;\n      for (var neighbor in adj[u]) {\n   \
        \     int v = neighbor[0], w = neighbor[1];\n        if (dist[u] + w < dist[v])\
        \ {\n          dist[v] = dist[u] + w;\n          pq.push(Item(v, dist[v]));\n\
        \        }\n      }\n    }\n    return dist[n - 1] == 2147483647 ? -1 : dist[n\
        \ - 1];\n  }\n}"
      go: "import (\n\t\"container/heap\"\n)\n\ntype Item struct {\n\tnode int\n\tdist\
        \ int\n}\n\ntype PriorityQueue []*Item\n\nfunc (pq PriorityQueue) Len() int\
        \           { return len(pq) }\nfunc (pq PriorityQueue) Less(i, j int) bool\
        \ { return pq[i].dist < pq[j].dist }\nfunc (pq PriorityQueue) Swap(i, j int)\
        \      { pq[i], pq[j] = pq[j], pq[i] }\nfunc (pq *PriorityQueue) Push(x interface{})\
        \ {\n\t*pq = append(*pq, x.(*Item))\n}\nfunc (pq *PriorityQueue) Pop() interface{}\
        \ {\n\told := *pq\n\tn := len(old)\n\titem := old[n-1]\n\t*pq = old[0 : n-1]\n\
        \treturn item\n}\n\nfunc minCost(n int, edges [][]int) int {\n\tadj := make([][][2]int,\
        \ n)\n\tfor _, edge := range edges {\n\t\tu, v, w := edge[0], edge[1], edge[2]\n\
        \t\tadj[u] = append(adj[u], [2]int{v, w})\n\t\tadj[v] = append(adj[v], [2]int{u,\
        \ 2 * w})\n\t}\n\tdist := make([]int, n)\n\tfor i := range dist {\n\t\tdist[i]\
        \ = 2e9\n\t}\n\tdist[0] = 0\n\tpq := &PriorityQueue{}\n\theap.Init(pq)\n\theap.Push(pq,\
        \ &Item{node: 0, dist: 0})\n\tfor pq.Len() > 0 {\n\t\tcurrent := heap.Pop(pq).(*Item)\n\
        \t\tu, d := current.node, current.dist\n\t\tif d > dist[u] {\n\t\t\tcontinue\n\
        \t\t}\n\t\tif u == n-1 {\n\t\t\treturn d\n\t\t}\n\t\tfor _, neighbor := range\
        \ adj[u] {\n\t\t\tv, w := neighbor[0], neighbor[1]\n\t\t\tif dist[u]+w < dist[v]\
        \ {\n\t\t\t\tdist[v] = dist[u] + w\n\t\t\t\theap.Push(pq, &Item{node: v, dist:\
        \ dist[v]})\n\t\t\t}\n\t\t}\n\t}\n\tif dist[n-1] == 2e9 {\n\t\treturn -1\n\t\
        }\n\treturn dist[n-1]\n}"
      ruby: "class MinHeap\n  def initialize\n    @heap = []\n  end\n  def push(val)\n\
        \    @heap << val\n    bubble_up(@heap.size - 1)\n  end\n  def pop\n    return\
        \ nil if @heap.empty?\n    swap(0, @heap.size - 1)\n    val = @heap.pop\n  \
        \  bubble_down(0)\n    val\n  end\n  def empty?\n    @heap.empty?\n  end\n \
        \ private\n  def bubble_up(idx)\n    while idx > 0\n      parent = (idx - 1)\
        \ / 2\n      break if @heap[parent][0] <= @heap[idx][0]\n      swap(parent,\
        \ idx)\n      idx = parent\n    end\n  end\n  def bubble_down(idx)\n    while\
        \ (child = 2 * idx + 1) < @heap.size\n      child += 1 if child + 1 < @heap.size\
        \ && @heap[child + 1][0] < @heap[child][0]\n      break if @heap[idx][0] <=\
        \ @heap[child][0]\n      swap(idx, child)\n      idx = child\n    end\n  end\n\
        \  def swap(i, j)\n    @heap[i], @heap[j] = @heap[j], @heap[i]\n  end\nend\n\
        \n# @param {Integer} n\n# @param {Integer[][]} edges\n# @return {Integer}\n\
        def min_cost(n, edges)\n  adj = Array.new(n) { [] }\n  edges.each do |u, v,\
        \ w|\n    adj[u] << [v, w]\n    adj[v] << [u, 2 * w]\n  end\n  dist = Array.new(n,\
        \ Float::INFINITY)\n  dist[0] = 0\n  pq = MinHeap.new\n  pq.push([0, 0])\n \
        \ while !pq.empty?\n    d, u = pq.pop\n    next if d > dist[u]\n    adj[u].each\
        \ do |v, w|\n      if dist[u] + w < dist[v]\n        dist[v] = dist[u] + w\n\
        \        pq.push([dist[v], v])\n      end\n    end\n  end\n  dist[n - 1] ==\
        \ Float::INFINITY ? -1 : dist[n - 1].to_i\nend"
      scala: "import scala.collection.mutable\nimport scala.collection.mutable.ListBuffer\n\
        \nobject Solution {\n  def minCost(n: Int, edges: Array[Array[Int]]): Int =\
        \ {\n    val adj = Array.tabulate(n)(_ => ListBuffer[(Int, Long)]())\n    for\
        \ (edge <- edges) {\n      val u = edge(0)\n      val v = edge(1)\n      val\
        \ w = edge(2).toLong\n      adj(u) += ((v, w))\n      adj(v) += ((u, 2 * w))\n\
        \    }\n    val dist = Array.fill(n)(Long.MaxValue)\n    dist(0) = 0\n    val\
        \ pq = mutable.PriorityQueue.empty[(Long, Int)](Ordering.by[(Long, Int), Long](-_._1))\n\
        \    pq.enqueue((0L, 0))\n    while (pq.nonEmpty) {\n      val (d, u) = pq.dequeue()\n\
        \      if (d <= dist(u)) {\n        for ((v, w) <- adj(u)) {\n          if (dist(u)\
        \ + w < dist(v)) {\n            dist(v) = dist(u) + w\n            pq.enqueue((dist(v),\
        \ v))\n          }\n        }\n      }\n    }\n    if (dist(n - 1) == Long.MaxValue)\
        \ -1 else dist(n - 1).toInt\n  }\n}"
      rust: "use std::collections::BinaryHeap;\nuse std::cmp::Ordering;\n\n#[derive(Copy,\
        \ Clone, Eq, PartialEq)]\nstruct State {\n    cost: i64,\n    node: usize,\n\
        }\n\nimpl Ord for State {\n    fn cmp(&self, other: &Self) -> Ordering {\n \
        \       other.cost.cmp(&self.cost)\n    }\n}\n\nimpl PartialOrd for State {\n\
        \    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {\n        Some(self.cmp(other))\n\
        \    }\n}\n\nimpl Solution {\n    pub fn min_cost(n: i32, edges: Vec<Vec<i32>>)\
        \ -> i32 {\n        let n = n as usize;\n        let mut adj = vec![vec![];\
        \ n];\n        for edge in edges {\n            let u = edge[0] as usize;\n\
        \            let v = edge[1] as usize;\n            let w = edge[2] as i64;\n\
        \            adj[u].push((v, w));\n            adj[v].push((u, 2 * w));\n  \
        \      }\n        let mut dist = vec![i64::MAX; n];\n        dist[0] = 0;\n\
        \        let mut pq = BinaryHeap::new();\n        pq.push(State { cost: 0, node:\
        \ 0 });\n        while let Some(State { cost, node }) = pq.pop() {\n       \
        \     if cost > dist[node] {\n                continue;\n            }\n   \
        \         for &(next_node, weight) in &adj[node] {\n                if dist[node]\
        \ + weight < dist[next_node] {\n                    dist[next_node] = dist[node]\
        \ + weight;\n                    pq.push(State {\n                        cost:\
        \ dist[next_node],\n                        node: next_node,\n             \
        \       });\n                }\n            }\n        }\n        if dist[n\
        \ - 1] == i64::MAX { -1 } else { dist[n - 1] as i32 }\n    }\n}"
      racket: "(require data/heap)\n(define/contract (min-cost n edges)\n  (-> exact-integer?\
        \ (listof (listof exact-integer?)) exact-integer?)\n  (let ([adj (make-vector\
        \ n '())])\n    (for ([edge edges])\n      (let ([u (first edge)]\n        \
        \    [v (second edge)]\n            [w (third edge)])\n        (vector-set!\
        \ adj u (cons (list v w) (vector-ref adj u)))\n        (vector-set! adj v (cons\
        \ (list u (* 2 w)) (vector-ref adj v)))))\n    (let ([dist (make-vector n 1000000000000)]\n\
        \          [h (make-heap (lambda (a b) (<= (car a) (car b))))])\n      (vector-set!\
        \ dist 0 0)\n      (heap-add! h (list 0 0))\n      (let loop ()\n        (when\
        \ (> (heap-count h) 0)\n          (let* ([top (heap-min h)]\n              \
        \   [d (first top)]\n                 [u (second top)])\n            (heap-remove-min!\
        \ h)\n            (when (<= d (vector-ref dist u))\n              (for ([neighbor\
        \ (vector-ref adj u)])\n                (let* ([v (first neighbor)]\n      \
        \                 [w (second neighbor)]\n                       [new-dist (+\
        \ d w)])\n                  (when (< new-dist (vector-ref dist v))\n       \
        \             (vector-set! dist v new-dist)\n                    (heap-add!\
        \ h (list new-dist v)))))))\n          (loop)))\n      (let ([final-dist (vector-ref\
        \ dist (- n 1))])\n        (if (>= final-dist 1000000000000) -1 final-dist)))))"
      erlang: "-spec min_cost(N :: integer(), Edges :: [[integer()]]) -> integer().\n\
        min_cost(N, Edges) ->\n  Adj = lists:foldl(fun([U, V, W], Acc) ->\n    Acc1\
        \ = maps:put(U, [{V, W} | maps:get(U, Acc, [])], Acc),\n    maps:put(V, [{U,\
        \ 2 * W} | maps:get(V, Acc1, [])], Acc1)\n  end, #{}, Edges),\n  Dist = dijkstra(0,\
        \ Adj, N),\n  FinalDist = maps:get(N - 1, Dist, infinity),\n  if FinalDist ==\
        \ infinity -> -1; true -> FinalDist end.\n\ndijkstra(Start, Adj, N) ->\n  PQ\
        \ = gb_sets:add_element({0, Start}, gb_sets:empty()),\n  Dist = #{Start => 0},\
        \ loop(PQ, Dist, Adj).\n\nloop(PQ, Dist, Adj) ->\n  case gb_sets:is_empty(PQ)\
        \ of\n    true -> Dist;\n    false ->\n      {{D, U}, PQ1} = gb_sets:take_smallest(PQ),\n\
        \      case D > maps:get(U, Dist, infinity) of\n        true -> loop(PQ1, Dist,\
        \ Adj);\n        false ->\n          Neighbors = maps:get(U, Adj, []),\n   \
        \       {NewPQ, NewDist} = lists:foldl(fun({V, W}, {PQA, DA}) ->\n         \
        \   NewW = D + W,\n            case NewW < maps:get(V, DA, infinity) of\n  \
        \            true -> {gb_sets:add_element({NewW, V}, PQA), DA#{V => NewW}};\n\
        \              false -> {PQA, DA}\n            end\n          end, {PQ1, Dist},\
        \ Neighbors),\n          loop(NewPQ, NewDist, Adj)\n      end\n  end."
      elixir: "defmodule Solution do\n  @spec min_cost(n :: integer, edges :: [[integer]])\
        \ :: integer\n  def min_cost(n, edges) do\n    adj = Enum.reduce(edges, %{},\
        \ fn [u, v, w], acc ->\n      acc\n      |> Map.update(u, [{v, w}], &([{v, w}\
        \ | &1]))\n      |> Map.update(v, [{u, 2 * w}], &([{u, 2 * w} | &1]))\n    end)\n\
        \    dist = %{0 => 0}\n    pq = :gb_sets.add_element({0, 0}, :gb_sets.empty())\n\
        \    final_dist = dijkstra_loop(pq, dist, adj, n)\n    if final_dist == :infinity,\
        \ do: -1, else: final_dist\n  end\n\n  defp dijkstra_loop(pq, dist, adj, n)\
        \ do\n    if :gb_sets.is_empty(pq) do\n      Map.get(dist, n - 1, :infinity)\n\
        \    else\n      {{d, u}, pq_rest} = :gb_sets.take_smallest(pq)\n      if d\
        \ > Map.get(dist, u, :infinity) do\n        dijkstra_loop(pq_rest, dist, adj,\
        \ n)\n      else\n        neighbors = Map.get(adj, u, [])\n        {new_pq,\
        \ new_dist} = Enum.reduce(neighbors, {pq_rest, dist}, fn {v, w}, {pq_acc, dist_acc}\
        \ ->\n          new_w = d + w\n          if new_w < Map.get(dist_acc, v, :infinity)\
        \ do\n            {:gb_sets.add_element({new_w, v}, pq_acc), Map.put(dist_acc,\
        \ v, new_w)}\n          else\n            {pq_acc, dist_acc}\n          end\n\
        \        end)\n        dijkstra_loop(new_pq, new_dist, adj, n)\n      end\n\
        \    end\n  end\nend"
    approach: "The problem can be modeled as finding the shortest path on an augmented\
      \ graph where nodes represent locations and edges represent possible travels.\
      \ For every directed edge $(u, v)$ with cost $w$ in the original graph, we can\
      \ traverse it normally as $u \to v$ for cost $w$. Additionally, the switch at\
      \ node $v$ allows us to reverse the incoming edge $u \to v$ into $v \to u$ with\
      \ a cost of $2w$. Since the reversal is only valid for that single traversal and\
      \ each node's switch can be used at most once, the restriction is equivalent to\
      \ choosing between a set of normal edges and a set of reversed edges available\
      \ at each node.\n\nIn a graph with strictly positive edge weights, the shortest\
      \ path from node $0$ to node $n-1$ will never contain a cycle. Because each node\
      \ is visited at most once along such a path, the 'at most once' constraint on\
      \ each node's switch is naturally satisfied. Thus, we can construct a graph with\
      \ $n$ nodes and $2E$ edges (for each original edge $u \to v$ with weight $w$,\
      \ we add $u \to v$ with weight $w$ and $v \to u$ with weight $2w$) and run Dijkstra's\
      \ algorithm to find the minimum cost to travel from node $0$ to node $n-1$."
    time_complexity: O((E + N) log N) where N is the number of nodes and E is the number
      of original edges. Building the augmented graph takes O(E) time, and Dijkstra's
      algorithm takes O((E + N) log N) using a priority queue.
    space_complexity: O(N + E) as we need to store the adjacency list containing 2E
      edges and a distance array of size N.
    elapsed_time: 292.5668087005615
    model: gemini-3-flash-preview
    generated_at: '2026-01-27 01:19:41 '
---

## Problem #3650: Minimum Cost Path with Edge Reversals

**Difficulty:** Medium

**Topics:** Graph Theory, Heap (Priority Queue), Shortest Path

## Problem Description

<p>You are given a directed, weighted graph with <code>n</code> nodes labeled from 0 to <code>n - 1</code>, and an array <code>edges</code> where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]</code> represents a directed edge from node <code>u<sub>i</sub></code> to node <code>v<sub>i</sub></code> with cost <code>w<sub>i</sub></code>.</p>

<p>Each node <code>u<sub>i</sub></code> has a switch that can be used <strong>at most once</strong>: when you arrive at <code>u<sub>i</sub></code> and have not yet used its switch, you may activate it on one of its incoming edges <code>v<sub>i</sub> &rarr; u<sub>i</sub></code> reverse that edge to <code>u<sub>i</sub> &rarr; v<sub>i</sub></code> and <strong>immediately</strong> traverse it.</p>

<p>The reversal is only valid for that single move, and using a reversed edge costs <code>2 * w<sub>i</sub></code>.</p>

<p>Return the <strong>minimum</strong> total cost to travel from node 0 to node <code>n - 1</code>. If it is not possible, return -1.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation: </strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2025/05/07/e1drawio.png" style="width: 171px; height: 111px;" /></strong></p>

<ul>
	<li>Use the path <code>0 &rarr; 1</code> (cost 3).</li>
	<li>At node 1 reverse the original edge <code>3 &rarr; 1</code> into <code>1 &rarr; 3</code> and traverse it at cost <code>2 * 1 = 2</code>.</li>
	<li>Total cost is <code>3 + 2 = 5</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>No reversal is needed. Take the path <code>0 &rarr; 2</code> (cost 1), then <code>2 &rarr; 1</code> (cost 1), then <code>1 &rarr; 3</code> (cost 1).</li>
	<li>Total cost is <code>1 + 1 + 1 = 3</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= edges.length &lt;= 10<sup>5</sup></code></li>
	<li><code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]</code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>1 &lt;= w<sub>i</sub> &lt;= 1000</code></li>
</ul>


## Hints

1. Do we only need to reverse at most one edge for each node? If so, can we add reversed edges for each node and use the one that helps in the shortest path?

2. Add reverse edges: `{u, v, w}` -> `{v, u, 2 * w}`, and use Dijkstra.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be modeled as finding the shortest path on an augmented graph where nodes represent locations and edges represent possible travels. For every directed edge $(u, v)$ with cost $w$ in the original graph, we can traverse it normally as $u 	o v$ for cost $w$. Additionally, the switch at node $v$ allows us to reverse the incoming edge $u 	o v$ into $v 	o u$ with a cost of $2w$. Since the reversal is only valid for that single traversal and each node's switch can be used at most once, the restriction is equivalent to choosing between a set of normal edges and a set of reversed edges available at each node.

In a graph with strictly positive edge weights, the shortest path from node $0$ to node $n-1$ will never contain a cycle. Because each node is visited at most once along such a path, the 'at most once' constraint on each node's switch is naturally satisfied. Thus, we can construct a graph with $n$ nodes and $2E$ edges (for each original edge $u 	o v$ with weight $w$, we add $u 	o v$ with weight $w$ and $v 	o u$ with weight $2w$) and run Dijkstra's algorithm to find the minimum cost to travel from node $0$ to node $n-1$.

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
    int minCost(int n, vector<vector<int>>& edges) {
        vector<vector<pair<int, int>>> adj(n);
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            adj[u].push_back({v, w});
            adj[v].push_back({u, 2 * w});
        }

        vector<long long> dist(n, LLONG_MAX);
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

        dist[0] = 0;
        pq.push({0LL, 0});

        while (!pq.empty()) {
            long long d = pq.top().first;
            int u = pq.top().second;
            pq.pop();

            if (d > dist[u]) continue;

            for (auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    pq.push({dist[v], v});
                }
            }
        }

        return dist[n - 1] == LLONG_MAX ? -1 : (int)dist[n - 1];
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
    public int minCost(int n, int[][] edges) {
        List<int[]>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            adj[u].add(new int[]{v, w});
            adj[v].add(new int[]{u, 2 * w});
        }

        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[1]));

        dist[0] = 0;
        pq.offer(new long[]{0, 0});

        while (!pq.isEmpty()) {
            long[] curr = pq.poll();
            int u = (int) curr[0];
            long d = curr[1];

            if (d > dist[u]) continue;

            for (int[] neighbor : adj[u]) {
                int v = neighbor[0];
                int w = neighbor[1];
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    pq.offer(new long[]{v, dist[v]});
                }
            }
        }

        return dist[n - 1] == Long.MAX_VALUE ? -1 : (int) dist[n - 1];
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
    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))

        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0, 0)]

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        return int(dist[n - 1]) if dist[n - 1] != float('inf') else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))

        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0, 0)]

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        return int(dist[n - 1]) if dist[n - 1] != float('inf') else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <limits.h>

typedef struct {
    long long cost;
    int node;
} HeapNode;

typedef struct {
    HeapNode* data;
    int size;
} MinHeap;

void push(MinHeap* heap, long long cost, int node) {
    int i = heap->size++;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (heap->data[p].cost <= cost) break;
        heap->data[i] = heap->data[p];
        i = p;
    }
    heap->data[i].cost = cost;
    heap->data[i].node = node;
}

HeapNode pop(MinHeap* heap) {
    HeapNode res = heap->data[0];
    HeapNode last = heap->data[--heap->size];
    int i = 0;
    while (i * 2 + 1 < heap->size) {
        int child = i * 2 + 1;
        if (child + 1 < heap->size && heap->data[child + 1].cost < heap->data[child].cost) child++;
        if (last.cost <= heap->data[child].cost) break;
        heap->data[i] = heap->data[child];
        i = child;
    }
    heap->data[i] = last;
    return res;
}

int minCost(int n, int** edges, int edgesSize, int* edgesColSize) {
    int* head = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) head[i] = -1;
    int* to = (int*)malloc(2 * edgesSize * sizeof(int));
    int* weight = (int*)malloc(2 * edgesSize * sizeof(int));
    int* next = (int*)malloc(2 * edgesSize * sizeof(int));
    int edgeCount = 0;

    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1], w = edges[i][2];
        to[edgeCount] = v; weight[edgeCount] = w; next[edgeCount] = head[u]; head[u] = edgeCount++;
        to[edgeCount] = u; weight[edgeCount] = 2 * w; next[edgeCount] = head[v]; head[v] = edgeCount++;
    }

    long long* dist = (long long*)malloc(n * sizeof(long long));
    for (int i = 0; i < n; i++) dist[i] = LLONG_MAX;
    dist[0] = 0;

    MinHeap heap;
    heap.data = (HeapNode*)malloc(2 * edgesSize * sizeof(HeapNode));
    heap.size = 0;
    push(&heap, 0, 0);

    while (heap.size > 0) {
        HeapNode top = pop(&heap);
        if (top.cost > dist[top.node]) continue;
        for (int e = head[top.node]; e != -1; e = next[e]) {
            if (dist[top.node] + weight[e] < dist[to[e]]) {
                dist[to[e]] = dist[top.node] + weight[e];
                push(&heap, dist[to[e]], to[e]);
            }
        }
    }

    long long result = dist[n - 1];
    free(head); free(to); free(weight); free(next); free(dist); free(heap.data);
    return result == LLONG_MAX ? -1 : (int)result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Collections.Generic;

public class Solution {
    public int MinCost(int n, int[][] edges) {
        List<(int v, int w)>[] adj = new List<(int v, int w)>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<(int v, int w)>();
        foreach (var edge in edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            adj[u].Add((v, w));
            adj[v].Add((u, 2 * w));
        }

        long[] dist = new long[n];
        for (int i = 0; i < n; i++) dist[i] = long.MaxValue;
        PriorityQueue<int, long> pq = new PriorityQueue<int, long>();

        dist[0] = 0;
        pq.Enqueue(0, 0);

        while (pq.Count > 0) {
            pq.TryDequeue(out int u, out long d);
            if (d > dist[u]) continue;

            foreach (var neighbor in adj[u]) {
                if (dist[u] + neighbor.w < dist[neighbor.v]) {
                    dist[neighbor.v] = dist[u] + neighbor.w;
                    pq.Enqueue(neighbor.v, dist[neighbor.v]);
                }
            }
        }

        return dist[n - 1] == long.MaxValue ? -1 : (int)dist[n - 1];
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
 * @return {number}
 */
var minCost = function(n, edges) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        adj[v].push([u, 2 * w]);
    }

    const dist = new Array(n).fill(Infinity);
    dist[0] = 0;
    const pq = new MinPriorityQueue({ priority: (x) => x.cost });
    pq.enqueue({ node: 0, cost: 0 });

    while (!pq.isEmpty()) {
        const { node, cost } = pq.dequeue().element;
        if (cost > dist[node]) continue;

        for (const [v, w] of adj[node]) {
            if (dist[node] + w < dist[v]) {
                dist[v] = dist[node] + w;
                pq.enqueue({ node: v, cost: dist[v] });
            }
        }
    }

    return dist[n - 1] === Infinity ? -1 : dist[n - 1];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
class MinHeap {
    heap: { node: number, dist: number }[] = [];
    push(val: { node: number, dist: number }) {
        this.heap.push(val);
        this.bubbleUp();
    }
    pop() {
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop()!;
        const top = this.heap[0];
        this.heap[0] = this.heap.pop()!;
        this.bubbleDown();
        return top;
    }
    bubbleUp() {
        let index = this.heap.length - 1;
        while (index > 0) {
            let parent = Math.floor((index - 1) / 2);
            if (this.heap[parent].dist <= this.heap[index].dist) break;
            [this.heap[parent], this.heap[index]] = [this.heap[index], this.heap[parent]];
            index = parent;
        }
    }
    bubbleDown() {
        let index = 0;
        while (true) {
            let left = 2 * index + 1, right = 2 * index + 2, smallest = index;
            if (left < this.heap.length && this.heap[left].dist < this.heap[smallest].dist) smallest = left;
            if (right < this.heap.length && this.heap[right].dist < this.heap[smallest].dist) smallest = right;
            if (smallest === index) break;
            [this.heap[smallest], this.heap[index]] = [this.heap[index], this.heap[smallest]];
            index = smallest;
        }
    }
}

function minCost(n: number, edges: number[][]): number {
    const adj: [number, number][][] = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        adj[v].push([u, 2 * w]);
    }
    const dist = new Float64Array(n).fill(Infinity);
    dist[0] = 0;
    const pq = new MinHeap();
    pq.push({ node: 0, dist: 0 });
    while (pq.heap.length > 0) {
        const current = pq.pop()!;
        const u = current.node;
        const d = current.dist;
        if (d > dist[u]) continue;
        if (u === n - 1) return d;
        for (const [v, w] of adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({ node: v, dist: dist[v] });
            }
        }
    }
    return dist[n - 1] === Infinity ? -1 : dist[n - 1];
};
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
     * @return Integer
     */
    function minCost($n, $edges) {
        $adj = array_fill(0, $n, []);
        foreach ($edges as $edge) {
            $u = $edge[0];
            $v = $edge[1];
            $w = $edge[2];
            $adj[$u][] = [$v, $w];
            $adj[$v][] = [$u, 2 * $w];
        }
        $dist = array_fill(0, $n, PHP_INT_MAX);
        $dist[0] = 0;
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $pq->insert(0, 0);
        while (!$pq->isEmpty()) {
            $top = $pq->extract();
            $u = $top['data'];
            $d = -$top['priority'];
            if ($d > $dist[$u]) continue;
            if ($u == $n - 1) return $d;
            foreach ($adj[$u] as $neighbor) {
                $v = $neighbor[0];
                $w = $neighbor[1];
                if ($dist[$u] + $w < $dist[$v]) {
                    $dist[$v] = $dist[$u] + $w;
                    $pq->insert($v, -$dist[$v]);
                }
            }
        }
        return $dist[$n - 1] === PHP_INT_MAX ? -1 : $dist[$n - 1];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    struct Item {
        let node: Int
        let dist: Int
    }
    class MinHeap {
        var heap = [Item]()
        func push(_ item: Item) {
            heap.append(item)
            var curr = heap.count - 1
            while curr > 0 {
                let parent = (curr - 1) / 2
                if heap[parent].dist <= heap[curr].dist { break }
                heap.swapAt(parent, curr)
                curr = parent
            }
        }
        func pop() -> Item? {
            if heap.isEmpty { return nil }
            if heap.count == 1 { return heap.removeFirst() }
            let top = heap[0]
            heap[0] = heap.removeLast()
            var curr = 0
            while true {
                let left = 2 * curr + 1, right = 2 * curr + 2
                var smallest = curr
                if left < heap.count && heap[left].dist < heap[smallest].dist { smallest = left }
                if right < heap.count && heap[right].dist < heap[smallest].dist { smallest = right }
                if smallest == curr { break }
                heap.swapAt(curr, smallest)
                curr = smallest
            }
            return top
        }
    }
    func minCost(_ n: Int, _ edges: [[Int]]) -> Int {
        var adj = Array(repeating: [(Int, Int)](), count: n)
        for edge in edges {
            adj[edge[0]].append((edge[1], edge[2]))
            adj[edge[1]].append((edge[0], 2 * edge[2]))
        }
        var dist = Array(repeating: Int.max, count: n)
        dist[0] = 0
        let pq = MinHeap()
        pq.push(Item(node: 0, dist: 0))
        while let current = pq.pop() {
            let u = current.node
            let d = current.dist
            if d > dist[u] { continue }
            if u == n - 1 { return d }
            for (v, w) in adj[u] {
                if dist[u] != Int.max && dist[u] + w < dist[v] {
                    dist[v] = dist[u] + w
                    pq.push(Item(node: v, dist: dist[v]))
                }
            }
        }
        return dist[n - 1] == Int.max ? -1 : dist[n - 1]
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
    fun minCost(n: Int, edges: Array<IntArray>): Int {
        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (edge in edges) {
            adj[edge[0]].add(Pair(edge[1], edge[2]))
            adj[edge[1]].add(Pair(edge[0], 2 * edge[2]))
        }
        val dist = IntArray(n) { Int.MAX_VALUE }
        dist[0] = 0
        val pq = PriorityQueue<Pair<Int, Int>>(compareBy { it.second })
        pq.offer(Pair(0, 0))
        while (pq.isNotEmpty()) {
            val (u, d) = pq.poll()
            if (d > dist[u]) continue
            if (u == n - 1) return d
            for ((v, w) in adj[u]) {
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w
                    pq.offer(Pair(v, dist[v]))
                }
            }
        }
        return if (dist[n - 1] == Int.MAX_VALUE) -1 else dist[n - 1]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:collection';

class Item {
  final int node;
  final int dist;
  Item(this.node, this.dist);
}

class MinHeap {
  List<Item> heap = [];
  void push(Item item) {
    heap.add(item);
    int curr = heap.length - 1;
    while (curr > 0) {
      int parent = (curr - 1) ~/ 2;
      if (heap[parent].dist <= heap[curr].dist) break;
      Item temp = heap[parent];
      heap[parent] = heap[curr];
      heap[curr] = temp;
      curr = parent;
    }
  }
  Item pop() {
    if (heap.length == 1) return heap.removeLast();
    Item top = heap[0];
    heap[0] = heap.removeLast();
    int curr = 0;
    while (true) {
      int left = 2 * curr + 1, right = 2 * curr + 2, smallest = curr;
      if (left < heap.length && heap[left].dist < heap[smallest].dist) smallest = left;
      if (right < heap.length && heap[right].dist < heap[smallest].dist) smallest = right;
      if (smallest == curr) break;
      Item temp = heap[smallest];
      heap[smallest] = heap[curr];
      heap[curr] = temp;
      curr = smallest;
    }
    return top;
  }
  bool get isEmpty => heap.isEmpty;
}

class Solution {
  int minCost(int n, List<List<int>> edges) {
    List<List<List<int>>> adj = List.generate(n, (_) => []);
    for (var edge in edges) {
      adj[edge[0]].add([edge[1], edge[2]]);
      adj[edge[1]].add([edge[0], 2 * edge[2]]);
    }
    List<int> dist = List.filled(n, 2147483647);
    dist[0] = 0;
    MinHeap pq = MinHeap();
    pq.push(Item(0, 0));
    while (!pq.isEmpty) {
      Item current = pq.pop();
      int u = current.node, d = current.dist;
      if (d > dist[u]) continue;
      if (u == n - 1) return d;
      for (var neighbor in adj[u]) {
        int v = neighbor[0], w = neighbor[1];
        if (dist[u] + w < dist[v]) {
          dist[v] = dist[u] + w;
          pq.push(Item(v, dist[v]));
        }
      }
    }
    return dist[n - 1] == 2147483647 ? -1 : dist[n - 1];
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

type Item struct {
	node int
	dist int
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

func minCost(n int, edges [][]int) int {
	adj := make([][][2]int, n)
	for _, edge := range edges {
		u, v, w := edge[0], edge[1], edge[2]
		adj[u] = append(adj[u], [2]int{v, w})
		adj[v] = append(adj[v], [2]int{u, 2 * w})
	}
	dist := make([]int, n)
	for i := range dist {
		dist[i] = 2e9
	}
	dist[0] = 0
	pq := &PriorityQueue{}
	heap.Init(pq)
	heap.Push(pq, &Item{node: 0, dist: 0})
	for pq.Len() > 0 {
		current := heap.Pop(pq).(*Item)
		u, d := current.node, current.dist
		if d > dist[u] {
			continue
		}
		if u == n-1 {
			return d
		}
		for _, neighbor := range adj[u] {
			v, w := neighbor[0], neighbor[1]
			if dist[u]+w < dist[v] {
				dist[v] = dist[u] + w
				heap.Push(pq, &Item{node: v, dist: dist[v]})
			}
		}
	}
	if dist[n-1] == 2e9 {
		return -1
	}
	return dist[n-1]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class MinHeap
  def initialize
    @heap = []
  end
  def push(val)
    @heap << val
    bubble_up(@heap.size - 1)
  end
  def pop
    return nil if @heap.empty?
    swap(0, @heap.size - 1)
    val = @heap.pop
    bubble_down(0)
    val
  end
  def empty?
    @heap.empty?
  end
  private
  def bubble_up(idx)
    while idx > 0
      parent = (idx - 1) / 2
      break if @heap[parent][0] <= @heap[idx][0]
      swap(parent, idx)
      idx = parent
    end
  end
  def bubble_down(idx)
    while (child = 2 * idx + 1) < @heap.size
      child += 1 if child + 1 < @heap.size && @heap[child + 1][0] < @heap[child][0]
      break if @heap[idx][0] <= @heap[child][0]
      swap(idx, child)
      idx = child
    end
  end
  def swap(i, j)
    @heap[i], @heap[j] = @heap[j], @heap[i]
  end
end

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def min_cost(n, edges)
  adj = Array.new(n) { [] }
  edges.each do |u, v, w|
    adj[u] << [v, w]
    adj[v] << [u, 2 * w]
  end
  dist = Array.new(n, Float::INFINITY)
  dist[0] = 0
  pq = MinHeap.new
  pq.push([0, 0])
  while !pq.empty?
    d, u = pq.pop
    next if d > dist[u]
    adj[u].each do |v, w|
      if dist[u] + w < dist[v]
        dist[v] = dist[u] + w
        pq.push([dist[v], v])
      end
    end
  end
  dist[n - 1] == Float::INFINITY ? -1 : dist[n - 1].to_i
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable
import scala.collection.mutable.ListBuffer

object Solution {
  def minCost(n: Int, edges: Array[Array[Int]]): Int = {
    val adj = Array.tabulate(n)(_ => ListBuffer[(Int, Long)]())
    for (edge <- edges) {
      val u = edge(0)
      val v = edge(1)
      val w = edge(2).toLong
      adj(u) += ((v, w))
      adj(v) += ((u, 2 * w))
    }
    val dist = Array.fill(n)(Long.MaxValue)
    dist(0) = 0
    val pq = mutable.PriorityQueue.empty[(Long, Int)](Ordering.by[(Long, Int), Long](-_._1))
    pq.enqueue((0L, 0))
    while (pq.nonEmpty) {
      val (d, u) = pq.dequeue()
      if (d <= dist(u)) {
        for ((v, w) <- adj(u)) {
          if (dist(u) + w < dist(v)) {
            dist(v) = dist(u) + w
            pq.enqueue((dist(v), v))
          }
        }
      }
    }
    if (dist(n - 1) == Long.MaxValue) -1 else dist(n - 1).toInt
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::BinaryHeap;
use std::cmp::Ordering;

#[derive(Copy, Clone, Eq, PartialEq)]
struct State {
    cost: i64,
    node: usize,
}

impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        other.cost.cmp(&self.cost)
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Solution {
    pub fn min_cost(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut adj = vec![vec![]; n];
        for edge in edges {
            let u = edge[0] as usize;
            let v = edge[1] as usize;
            let w = edge[2] as i64;
            adj[u].push((v, w));
            adj[v].push((u, 2 * w));
        }
        let mut dist = vec![i64::MAX; n];
        dist[0] = 0;
        let mut pq = BinaryHeap::new();
        pq.push(State { cost: 0, node: 0 });
        while let Some(State { cost, node }) = pq.pop() {
            if cost > dist[node] {
                continue;
            }
            for &(next_node, weight) in &adj[node] {
                if dist[node] + weight < dist[next_node] {
                    dist[next_node] = dist[node] + weight;
                    pq.push(State {
                        cost: dist[next_node],
                        node: next_node,
                    });
                }
            }
        }
        if dist[n - 1] == i64::MAX { -1 } else { dist[n - 1] as i32 }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(require data/heap)
(define/contract (min-cost n edges)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let ([adj (make-vector n '())])
    (for ([edge edges])
      (let ([u (first edge)]
            [v (second edge)]
            [w (third edge)])
        (vector-set! adj u (cons (list v w) (vector-ref adj u)))
        (vector-set! adj v (cons (list u (* 2 w)) (vector-ref adj v)))))
    (let ([dist (make-vector n 1000000000000)]
          [h (make-heap (lambda (a b) (<= (car a) (car b))))])
      (vector-set! dist 0 0)
      (heap-add! h (list 0 0))
      (let loop ()
        (when (> (heap-count h) 0)
          (let* ([top (heap-min h)]
                 [d (first top)]
                 [u (second top)])
            (heap-remove-min! h)
            (when (<= d (vector-ref dist u))
              (for ([neighbor (vector-ref adj u)])
                (let* ([v (first neighbor)]
                       [w (second neighbor)]
                       [new-dist (+ d w)])
                  (when (< new-dist (vector-ref dist v))
                    (vector-set! dist v new-dist)
                    (heap-add! h (list new-dist v)))))))
          (loop)))
      (let ([final-dist (vector-ref dist (- n 1))])
        (if (>= final-dist 1000000000000) -1 final-dist)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_cost(N :: integer(), Edges :: [[integer()]]) -> integer().
min_cost(N, Edges) ->
  Adj = lists:foldl(fun([U, V, W], Acc) ->
    Acc1 = maps:put(U, [{V, W} | maps:get(U, Acc, [])], Acc),
    maps:put(V, [{U, 2 * W} | maps:get(V, Acc1, [])], Acc1)
  end, #{}, Edges),
  Dist = dijkstra(0, Adj, N),
  FinalDist = maps:get(N - 1, Dist, infinity),
  if FinalDist == infinity -> -1; true -> FinalDist end.

dijkstra(Start, Adj, N) ->
  PQ = gb_sets:add_element({0, Start}, gb_sets:empty()),
  Dist = #{Start => 0}, loop(PQ, Dist, Adj).

loop(PQ, Dist, Adj) ->
  case gb_sets:is_empty(PQ) of
    true -> Dist;
    false ->
      {{D, U}, PQ1} = gb_sets:take_smallest(PQ),
      case D > maps:get(U, Dist, infinity) of
        true -> loop(PQ1, Dist, Adj);
        false ->
          Neighbors = maps:get(U, Adj, []),
          {NewPQ, NewDist} = lists:foldl(fun({V, W}, {PQA, DA}) ->
            NewW = D + W,
            case NewW < maps:get(V, DA, infinity) of
              true -> {gb_sets:add_element({NewW, V}, PQA), DA#{V => NewW}};
              false -> {PQA, DA}
            end
          end, {PQ1, Dist}, Neighbors),
          loop(NewPQ, NewDist, Adj)
      end
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_cost(n :: integer, edges :: [[integer]]) :: integer
  def min_cost(n, edges) do
    adj = Enum.reduce(edges, %{}, fn [u, v, w], acc ->
      acc
      |> Map.update(u, [{v, w}], &([{v, w} | &1]))
      |> Map.update(v, [{u, 2 * w}], &([{u, 2 * w} | &1]))
    end)
    dist = %{0 => 0}
    pq = :gb_sets.add_element({0, 0}, :gb_sets.empty())
    final_dist = dijkstra_loop(pq, dist, adj, n)
    if final_dist == :infinity, do: -1, else: final_dist
  end

  defp dijkstra_loop(pq, dist, adj, n) do
    if :gb_sets.is_empty(pq) do
      Map.get(dist, n - 1, :infinity)
    else
      {{d, u}, pq_rest} = :gb_sets.take_smallest(pq)
      if d > Map.get(dist, u, :infinity) do
        dijkstra_loop(pq_rest, dist, adj, n)
      else
        neighbors = Map.get(adj, u, [])
        {new_pq, new_dist} = Enum.reduce(neighbors, {pq_rest, dist}, fn {v, w}, {pq_acc, dist_acc} ->
          new_w = d + w
          if new_w < Map.get(dist_acc, v, :infinity) do
            {:gb_sets.add_element({new_w, v}, pq_acc), Map.put(dist_acc, v, new_w)}
          else
            {pq_acc, dist_acc}
          end
        end)
        dijkstra_loop(new_pq, new_dist, adj, n)
      end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O((E + N) log N) where N is the number of nodes and E is the number of original edges. Building the augmented graph takes O(E) time, and Dijkstra's algorithm takes O((E + N) log N) using a priority queue.
- **Space Complexity:** O(N + E) as we need to store the adjacency list containing 2E edges and a distance array of size N.
