---
layout: post
title: "Network Recovery Pathways"
date: 2026-07-03 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Binary Search", "Dynamic Programming", "Graph Theory", "Topological Sort", "Heap (Priority Queue)", "Shortest Path"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/network-recovery-pathways/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int findMaxPathScore(vector<vector<int>>&\
        \ edges, vector<bool>& online, long long k) {\n        int n = online.size();\n\
        \        vector<vector<pair<int, int>>> adj(n);\n        vector<int> in_degree(n,\
        \ 0);\n        vector<int> all_costs;\n\n        for (auto& e : edges) {\n \
        \           int u = e[0], v = e[1], cost = e[2];\n            if (online[u]\
        \ && online[v]) {\n                adj[u].push_back({v, cost});\n          \
        \      in_degree[v]++;\n                all_costs.push_back(cost);\n       \
        \     }\n        }\n\n        vector<int> topo_order;\n        queue<int> q;\n\
        \        for (int i = 0; i < n; i++) {\n            if (online[i] && in_degree[i]\
        \ == 0) {\n                q.push(i);\n            }\n        }\n\n        while\
        \ (!q.empty()) {\n            int u = q.front();\n            q.pop();\n   \
        \         topo_order.push_back(u);\n            for (auto& edge : adj[u]) {\n\
        \                if (--in_degree[edge.first] == 0) {\n                    q.push(edge.first);\n\
        \                }\n            }\n        }\n\n        sort(all_costs.begin(),\
        \ all_costs.end());\n        all_costs.erase(unique(all_costs.begin(), all_costs.end()),\
        \ all_costs.end());\n\n        auto check = [&](int min_edge_cost) {\n     \
        \       vector<long long> dist(n, 1000000000000000LL);\n            dist[0]\
        \ = 0;\n            for (int u : topo_order) {\n                if (dist[u]\
        \ > k) continue;\n                for (auto& edge : adj[u]) {\n            \
        \        if (edge.second >= min_edge_cost) {\n                        if (dist[u]\
        \ + edge.second < dist[edge.first]) {\n                            dist[edge.first]\
        \ = dist[u] + edge.second;\n                        }\n                    }\n\
        \                }\n            }\n            return dist[n - 1] <= k;\n  \
        \      };\n\n        int low = 0, high = (int)all_costs.size() - 1, ans = -1;\n\
        \        while (low <= high) {\n            int mid = low + (high - low) / 2;\n\
        \            if (check(all_costs[mid])) {\n                ans = all_costs[mid];\n\
        \                low = mid + 1;\n            } else {\n                high\
        \ = mid - 1;\n            }\n        }\n\n        return ans;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    static class Edge {\n    \
        \    int to;\n        int cost;\n        Edge(int to, int cost) {\n        \
        \    this.to = to;\n            this.cost = cost;\n        }\n    }\n\n    public\
        \ int findMaxPathScore(int[][] edges, boolean[] online, long k) {\n        int\
        \ n = online.length;\n        ArrayList<Edge>[] adj = new ArrayList[n];\n  \
        \      for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();\n        int[]\
        \ inDegree = new int[n];\n\n        int edgeCount = 0;\n        for (int[] e\
        \ : edges) {\n            if (online[e[0]] && online[e[1]]) edgeCount++;\n \
        \       }\n\n        int[] allCosts = new int[edgeCount];\n        int costIdx\
        \ = 0;\n        for (int[] e : edges) {\n            int u = e[0], v = e[1],\
        \ cost = e[2];\n            if (online[u] && online[v]) {\n                adj[u].add(new\
        \ Edge(v, cost));\n                inDegree[v]++;\n                allCosts[costIdx++]\
        \ = cost;\n            }\n        }\n\n        int[] topoOrder = new int[n];\n\
        \        int topoPtr = 0;\n        ArrayDeque<Integer> q = new ArrayDeque<>();\n\
        \        for (int i = 0; i < n; i++) {\n            if (online[i] && inDegree[i]\
        \ == 0) q.add(i);\n        }\n\n        while (!q.isEmpty()) {\n           \
        \ int u = q.poll();\n            topoOrder[topoPtr++] = u;\n            for\
        \ (Edge e : adj[u]) {\n                if (--inDegree[e.to] == 0) q.add(e.to);\n\
        \            }\n        }\n\n        Arrays.sort(allCosts);\n        int uniqueCount\
        \ = 0;\n        if (edgeCount > 0) {\n            uniqueCount = 1;\n       \
        \     for (int i = 1; i < edgeCount; i++) {\n                if (allCosts[i]\
        \ != allCosts[i - 1]) uniqueCount++;\n            }\n        }\n        int[]\
        \ uniqueCosts = new int[uniqueCount];\n        if (uniqueCount > 0) {\n    \
        \        uniqueCosts[0] = allCosts[0];\n            int idx = 1;\n         \
        \   for (int i = 1; i < edgeCount; i++) {\n                if (allCosts[i] !=\
        \ allCosts[i - 1]) uniqueCosts[idx++] = allCosts[i];\n            }\n      \
        \  }\n\n        int low = 0, high = uniqueCount - 1, ans = -1;\n        while\
        \ (low <= high) {\n            int mid = low + (high - low) / 2;\n         \
        \   if (isValid(uniqueCosts[mid], adj, topoOrder, topoPtr, n, k)) {\n      \
        \          ans = uniqueCosts[mid];\n                low = mid + 1;\n       \
        \     } else {\n                high = mid - 1;\n            }\n        }\n\
        \        return ans;\n    }\n\n    private boolean isValid(int minCost, ArrayList<Edge>[]\
        \ adj, int[] topoOrder, int topoSize, int n, long k) {\n        long[] dist\
        \ = new long[n];\n        Arrays.fill(dist, Long.MAX_VALUE / 2);\n        dist[0]\
        \ = 0;\n        for (int i = 0; i < topoSize; i++) {\n            int u = topoOrder[i];\n\
        \            if (dist[u] > k) continue;\n            for (Edge e : adj[u]) {\n\
        \                if (e.cost >= minCost) {\n                    if (dist[u] +\
        \ e.cost < dist[e.to]) {\n                        dist[e.to] = dist[u] + e.cost;\n\
        \                    }\n                }\n            }\n        }\n      \
        \  return dist[n - 1] <= k;\n    }\n}"
      python: "import collections\n\nclass Solution(object):\n    def findMaxPathScore(self,\
        \ edges, online, k):\n        \"\"\"\n        :type edges: List[List[int]]\n\
        \        :type online: List[bool]\n        :type k: int\n        :rtype: int\n\
        \        \"\"\"\n        n = len(online)\n        adj = [[] for _ in range(n)]\n\
        \        in_degree = [0] * n\n        unique_costs_set = set()\n\n        for\
        \ u, v, cost in edges:\n            if online[u] and online[v]:\n          \
        \      adj[u].append((v, cost))\n                in_degree[v] += 1\n       \
        \         unique_costs_set.add(cost)\n\n        topo_order = []\n        queue\
        \ = collections.deque([i for i in range(n) if online[i] and in_degree[i] ==\
        \ 0])\n        while queue:\n            u = queue.popleft()\n            topo_order.append(u)\n\
        \            for v, cost in adj[u]:\n                in_degree[v] -= 1\n   \
        \             if in_degree[v] == 0:\n                    queue.append(v)\n\n\
        \        sorted_costs = sorted(list(unique_costs_set))\n\n        def check(min_val):\n\
        \            dist = [float('inf')] * n\n            dist[0] = 0\n          \
        \  for u in topo_order:\n                d_u = dist[u]\n                if d_u\
        \ > k:\n                    continue\n                for v, c in adj[u]:\n\
        \                    if c >= min_val:\n                        new_dist = d_u\
        \ + c\n                        if new_dist < dist[v]:\n                    \
        \        dist[v] = new_dist\n            return dist[n - 1] <= k\n\n       \
        \ low, high = 0, len(sorted_costs) - 1\n        ans = -1\n        while low\
        \ <= high:\n            mid = (low + high) // 2\n            if check(sorted_costs[mid]):\n\
        \                ans = sorted_costs[mid]\n                low = mid + 1\n  \
        \          else:\n                high = mid - 1\n        return ans"
      python3: "from typing import List\nimport collections\n\nclass Solution:\n   \
        \ def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k:\
        \ int) -> int:\n        n = len(online)\n        adj = [[] for _ in range(n)]\n\
        \        in_degree = [0] * n\n\n        for u, v, c in edges:\n            if\
        \ online[u] and online[v]:\n                adj[u].append((v, c))\n        \
        \        in_degree[v] += 1\n\n        topo_order = []\n        queue = collections.deque([i\
        \ for i in range(n) if online[i] and in_degree[i] == 0])\n        while queue:\n\
        \            u = queue.popleft()\n            topo_order.append(u)\n       \
        \     for v, c in adj[u]:\n                in_degree[v] -= 1\n             \
        \   if in_degree[v] == 0:\n                    queue.append(v)\n\n        unique_costs\
        \ = sorted(list(set(e[2] for e in edges)))\n\n        def check(min_val):\n\
        \            dist = [float('inf')] * n\n            dist[0] = 0\n          \
        \  for u in topo_order:\n                d_u = dist[u]\n                if d_u\
        \ > k:\n                    continue\n                for v, c in adj[u]:\n\
        \                    if c >= min_val:\n                        new_dist = d_u\
        \ + c\n                        if dist[v] > new_dist:\n                    \
        \        dist[v] = new_dist\n            return dist[n-1] <= k\n\n        ans\
        \ = -1\n        low, high = 0, len(unique_costs) - 1\n        while low <= high:\n\
        \            mid = (low + high) // 2\n            if check(unique_costs[mid]):\n\
        \                ans = unique_costs[mid]\n                low = mid + 1\n  \
        \          else:\n                high = mid - 1\n        return ans"
      c: "#include <stdbool.h>\n#include <stdlib.h>\n#include <string.h>\n#include <limits.h>\n\
        \ntypedef struct {\n    int to;\n    int cost;\n    int next;\n} EdgePool;\n\
        \nint compare_ints(const void* a, const void* b) {\n    int x = *(const int*)a;\n\
        \    int y = *(const int*)b;\n    if (x < y) return -1;\n    if (x > y) return\
        \ 1;\n    return 0;\n}\n\nint findMaxPathScore(int** edges, int edgesSize, int*\
        \ edgesColSize, bool* online, int onlineSize, long long k) {\n    int n = onlineSize;\n\
        \    int m = edgesSize;\n    if (m == 0) return -1;\n\n    int* head = malloc(n\
        \ * sizeof(int));\n    memset(head, -1, n * sizeof(int));\n    EdgePool* pool\
        \ = malloc(m * sizeof(EdgePool));\n    int* in_degree = calloc(n, sizeof(int));\n\
        \    int edge_count = 0;\n\n    for (int i = 0; i < m; i++) {\n        int u\
        \ = edges[i][0];\n        int v = edges[i][1];\n        int c = edges[i][2];\n\
        \        if (online[u] && online[v]) {\n            pool[edge_count].to = v;\n\
        \            pool[edge_count].cost = c;\n            pool[edge_count].next =\
        \ head[u];\n            head[u] = edge_count++;\n            in_degree[v]++;\n\
        \        }\n    }\n\n    int* topo_order = malloc(n * sizeof(int));\n    int\
        \ topo_size = 0;\n    int* queue = malloc(n * sizeof(int));\n    int q_head\
        \ = 0, q_tail = 0;\n    for (int i = 0; i < n; i++) {\n        if (online[i]\
        \ && in_degree[i] == 0) queue[q_tail++] = i;\n    }\n\n    while (q_head < q_tail)\
        \ {\n        int u = queue[q_head++];\n        topo_order[topo_size++] = u;\n\
        \        for (int i = head[u]; i != -1; i = pool[i].next) {\n            int\
        \ v = pool[i].to;\n            if (--in_degree[v] == 0) queue[q_tail++] = v;\n\
        \        }\n    }\n\n    int* costs = malloc(m * sizeof(int));\n    for (int\
        \ i = 0; i < m; i++) costs[i] = edges[i][2];\n    qsort(costs, m, sizeof(int),\
        \ compare_ints);\n    int m_unique = 0;\n    if (m > 0) {\n        m_unique\
        \ = 1;\n        for (int i = 1; i < m; i++) {\n            if (costs[i] != costs[i\
        \ - 1]) costs[m_unique++] = costs[i];\n        }\n    }\n\n    long long* dist\
        \ = malloc(n * sizeof(long long));\n    long long INF = 200000000000000LL;\n\
        \n    int ans = -1;\n    int low = 0, high = m_unique - 1;\n    while (low <=\
        \ high) {\n        int mid_idx = low + (high - low) / 2;\n        int min_val\
        \ = costs[mid_idx];\n\n        for (int i = 0; i < n; i++) dist[i] = INF;\n\
        \        dist[0] = 0;\n\n        for (int i = 0; i < topo_size; i++) {\n   \
        \         int u = topo_order[i];\n            if (dist[u] > k) continue;\n \
        \           for (int j = head[u]; j != -1; j = pool[j].next) {\n           \
        \     if (pool[j].cost >= min_val) {\n                    int v = pool[j].to;\n\
        \                    if (dist[v] > dist[u] + pool[j].cost) {\n             \
        \           dist[v] = dist[u] + pool[j].cost;\n                    }\n     \
        \           }\n            }\n        }\n\n        if (dist[n - 1] <= k) {\n\
        \            ans = min_val;\n            low = mid_idx + 1;\n        } else\
        \ {\n            high = mid_idx - 1;\n        }\n    }\n\n    free(head); free(pool);\
        \ free(in_degree); free(topo_order); free(queue); free(costs); free(dist);\n\
        \    return ans;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    public int FindMaxPathScore(int[][] edges, bool[]\
        \ online, long k) {\n        int n = online.Length;\n        int m = edges.Length;\n\
        \        if (m == 0) return -1;\n\n        int[] head = new int[n];\n      \
        \  Array.Fill(head, -1);\n        int[] next = new int[m];\n        int[] to\
        \ = new int[m];\n        int[] edgeCost = new int[m];\n        int[] inDegree\
        \ = new int[n];\n        int edgeCount = 0;\n\n        for (int i = 0; i < m;\
        \ i++) {\n            int u = edges[i][0];\n            int v = edges[i][1];\n\
        \            int c = edges[i][2];\n            if (online[u] && online[v]) {\n\
        \                to[edgeCount] = v;\n                edgeCost[edgeCount] = c;\n\
        \                next[edgeCount] = head[u];\n                head[u] = edgeCount++;\n\
        \                inDegree[v]++;\n            }\n        }\n\n        int[] topoOrder\
        \ = new int[n];\n        int topoSize = 0;\n        int[] q = new int[n];\n\
        \        int qHead = 0, qTail = 0;\n        for (int i = 0; i < n; i++) {\n\
        \            if (online[i] && inDegree[i] == 0) q[qTail++] = i;\n        }\n\
        \n        while (qHead < qTail) {\n            int u = q[qHead++];\n       \
        \     topoOrder[topoSize++] = u;\n            for (int i = head[u]; i != -1;\
        \ i = next[i]) {\n                int v = to[i];\n                if (--inDegree[v]\
        \ == 0) q[qTail++] = v;\n            }\n        }\n\n        int[] uniqueCosts\
        \ = edges.Select(e => e[2]).Distinct().ToArray();\n        Array.Sort(uniqueCosts);\n\
        \n        long[] dist = new long[n];\n        int ans = -1;\n        int low\
        \ = 0, high = uniqueCosts.Length - 1;\n        while (low <= high) {\n     \
        \       int midIdx = low + (high - low) / 2;\n            int minVal = uniqueCosts[midIdx];\n\
        \n            for (int i = 0; i < n; i++) dist[i] = 100000000000000L; // 1e14\n\
        \            dist[0] = 0;\n\n            for (int i = 0; i < topoSize; i++)\
        \ {\n                int u = topoOrder[i];\n                if (dist[u] > k)\
        \ continue;\n                for (int j = head[u]; j != -1; j = next[j]) {\n\
        \                    if (edgeCost[j] >= minVal) {\n                        int\
        \ v = to[j];\n                        if (dist[v] > dist[u] + edgeCost[j]) {\n\
        \                            dist[v] = dist[u] + (long)edgeCost[j];\n      \
        \                  }\n                    }\n                }\n           \
        \ }\n\n            if (dist[n - 1] <= k) {\n                ans = minVal;\n\
        \                low = midIdx + 1;\n            } else {\n                high\
        \ = midIdx - 1;\n            }\n        }\n\n        return ans;\n    }\n}"
      javascript: "/**\n * @param {number[][]} edges\n * @param {boolean[]} online\n\
        \ * @param {number} k\n * @return {number}\n */\nvar findMaxPathScore = function(edges,\
        \ online, k) {\n    const n = online.length;\n    const m = edges.length;\n\
        \    if (m === 0) return -1;\n\n    const head = new Int32Array(n).fill(-1);\n\
        \    const next = new Int32Array(m);\n    const to = new Int32Array(m);\n  \
        \  const edgeCost = new Int32Array(m);\n    const inDegree = new Int32Array(n).fill(0);\n\
        \    let edgeCount = 0;\n\n    for (let i = 0; i < m; i++) {\n        const\
        \ u = edges[i][0];\n        const v = edges[i][1];\n        const c = edges[i][2];\n\
        \        if (online[u] && online[v]) {\n            to[edgeCount] = v;\n   \
        \         edgeCost[edgeCount] = c;\n            next[edgeCount] = head[u];\n\
        \            head[u] = edgeCount++;\n            inDegree[v]++;\n        }\n\
        \    }\n\n    const topoOrder = [];\n    const q = [];\n    for (let i = 0;\
        \ i < n; i++) {\n        if (online[i] && inDegree[i] === 0) q.push(i);\n  \
        \  }\n\n    let qIdx = 0;\n    while (qIdx < q.length) {\n        const u =\
        \ q[qIdx++];\n        topoOrder.push(u);\n        for (let i = head[u]; i !==\
        \ -1; i = next[i]) {\n            const v = to[i];\n            if (--inDegree[v]\
        \ === 0) q.push(v);\n        }\n    }\n\n    const uniqueCosts = Array.from(new\
        \ Set(edges.map(e => e[2]))).sort((a, b) => a - b);\n    const dist = new Float64Array(n);\n\
        \n    function check(minVal) {\n        dist.fill(1e15);\n        dist[0] =\
        \ 0;\n        for (let i = 0; i < topoOrder.length; i++) {\n            const\
        \ u = topoOrder[i];\n            if (dist[u] > k) continue;\n            for\
        \ (let j = head[u]; j !== -1; j = next[j]) {\n                if (edgeCost[j]\
        \ >= minVal) {\n                    const v = to[j];\n                    if\
        \ (dist[v] > dist[u] + edgeCost[j]) {\n                        dist[v] = dist[u]\
        \ + edgeCost[j];\n                    }\n                }\n            }\n\
        \        }\n        return dist[n - 1] <= k;\n    }\n\n    let ans = -1;\n \
        \   let low = 0, high = uniqueCosts.length - 1;\n    while (low <= high) {\n\
        \        const midIdx = Math.floor((low + high) / 2);\n        if (check(uniqueCosts[midIdx]))\
        \ {\n            ans = uniqueCosts[midIdx];\n            low = midIdx + 1;\n\
        \        } else {\n            high = midIdx - 1;\n        }\n    }\n\n    return\
        \ ans;\n};"
      typescript: "function findMaxPathScore(edges: number[][], online: boolean[], k:\
        \ number): number {\n    const n = online.length;\n    const adj: [number, number][][]\
        \ = Array.from({ length: n }, () => []);\n    const inDegree = new Int32Array(n).fill(0);\n\
        \    for (const [u, v, cost] of edges) {\n        adj[u].push([v, cost]);\n\
        \        inDegree[v]++;\n    }\n\n    const queue = new Int32Array(n);\n   \
        \ let head = 0, tail = 0;\n    for (let i = 0; i < n; i++) {\n        if (inDegree[i]\
        \ === 0) queue[tail++] = i;\n    }\n\n    const topoOrder = new Int32Array(n);\n\
        \    let topoIdx = 0;\n    while (head < tail) {\n        const u = queue[head++];\n\
        \        topoOrder[topoIdx++] = u;\n        const neighbors = adj[u];\n    \
        \    for (let i = 0; i < neighbors.length; i++) {\n            const v = neighbors[i][0];\n\
        \            if (--inDegree[v] === 0) queue[tail++] = v;\n        }\n    }\n\
        \n    const uniqueWeights = Array.from(new Set(edges.map(e => e[2]))).sort((a,\
        \ b) => a - b);\n\n    const check = (threshold: number): boolean => {\n   \
        \     const dist = new Float64Array(n).fill(Infinity);\n        dist[0] = 0;\n\
        \        for (let i = 0; i < n; i++) {\n            const u = topoOrder[i];\n\
        \            if (dist[u] === Infinity || dist[u] > k) continue;\n          \
        \  const neighbors = adj[u];\n            for (let j = 0; j < neighbors.length;\
        \ j++) {\n                const [v, cost] = neighbors[j];\n                if\
        \ (online[v] && cost >= threshold) {\n                    const newDist = dist[u]\
        \ + cost;\n                    if (newDist < dist[v]) {\n                  \
        \      dist[v] = newDist;\n                    }\n                }\n      \
        \      }\n        }\n        return dist[n - 1] <= k;\n    };\n\n    let low\
        \ = 0, high = uniqueWeights.length - 1, ans = -1;\n    while (low <= high) {\n\
        \        const mid = (low + high) >> 1;\n        if (check(uniqueWeights[mid]))\
        \ {\n            ans = uniqueWeights[mid];\n            low = mid + 1;\n   \
        \     } else {\n            high = mid - 1;\n        }\n    }\n    return ans;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $edges\n     * @param\
        \ Boolean[] $online\n     * @param Integer $k\n     * @return Integer\n    \
        \ */\n    function findMaxPathScore($edges, $online, $k) {\n        $n = count($online);\n\
        \        $adj = array_fill(0, $n, []);\n        $inDegree = array_fill(0, $n,\
        \ 0);\n        foreach ($edges as $e) {\n            $u = $e[0]; $v = $e[1];\
        \ $cost = $e[2];\n            $adj[$u][] = [$v, $cost];\n            $inDegree[$v]++;\n\
        \        }\n\n        $queue = new SplQueue();\n        for ($i = 0; $i < $n;\
        \ $i++) {\n            if ($inDegree[$i] === 0) $queue->enqueue($i);\n     \
        \   }\n\n        $topoOrder = [];\n        while (!$queue->isEmpty()) {\n  \
        \          $u = $queue->dequeue();\n            $topoOrder[] = $u;\n       \
        \     foreach ($adj[$u] as $neighbor) {\n                $v = $neighbor[0];\n\
        \                $inDegree[$v]--;\n                if ($inDegree[$v] === 0)\
        \ $queue->enqueue($v);\n            }\n        }\n\n        $weights = [];\n\
        \        foreach ($edges as $e) {\n            $weights[] = $e[2];\n       \
        \ }\n        $weights = array_values(array_unique($weights));\n        sort($weights);\n\
        \n        $ans = -1;\n        $low = 0;\n        $high = count($weights) - 1;\n\
        \        while ($low <= $high) {\n            $mid = (int)(($low + $high) /\
        \ 2);\n            $threshold = $weights[$mid];\n            if ($this->check($threshold,\
        \ $n, $adj, $online, $k, $topoOrder)) {\n                $ans = $threshold;\n\
        \                $low = $mid + 1;\n            } else {\n                $high\
        \ = $mid - 1;\n            }\n        }\n        return $ans;\n    }\n\n   \
        \ private function check($threshold, $n, $adj, $online, $k, $topoOrder) {\n\
        \        $dist = array_fill(0, $n, INF);\n        $dist[0] = 0.0;\n        foreach\
        \ ($topoOrder as $u) {\n            if ($dist[$u] === INF || $dist[$u] > $k)\
        \ continue;\n            foreach ($adj[$u] as $neighbor) {\n               \
        \ $v = $neighbor[0];\n                $cost = $neighbor[1];\n              \
        \  if ($online[$v] && $cost >= $threshold) {\n                    $newDist =\
        \ $dist[$u] + $cost;\n                    if ($newDist < $dist[$v]) {\n    \
        \                    $dist[$v] = $newDist;\n                    }\n        \
        \        }\n            }\n        }\n        return $dist[$n - 1] <= $k;\n\
        \    }\n}"
      swift: "class Solution {\n    func findMaxPathScore(_ edges: [[Int]], _ online:\
        \ [Bool], _ k: Int) -> Int {\n        let n = online.count\n        var adj\
        \ = Array(repeating: [(Int, Int)](), count: n)\n        var inDegree = [Int](repeating:\
        \ 0, count: n)\n        for edge in edges {\n            let u = edge[0]\n \
        \           let v = edge[1]\n            let cost = edge[2]\n            adj[u].append((v,\
        \ cost))\n            inDegree[v] += 1\n        }\n\n        var queue = [Int]()\n\
        \        for i in 0..<n {\n            if inDegree[i] == 0 {\n             \
        \   queue.append(i)\n            }\n        }\n\n        var head = 0\n    \
        \    var topoOrder = [Int]()\n        while head < queue.count {\n         \
        \   let u = queue[head]\n            head += 1\n            topoOrder.append(u)\n\
        \            for (v, _) in adj[u] {\n                inDegree[v] -= 1\n    \
        \            if inDegree[v] == 0 {\n                    queue.append(v)\n  \
        \              }\n            }\n        }\n\n        var uniqueWeightsSet =\
        \ Set<Int>()\n        for edge in edges { uniqueWeightsSet.insert(edge[2]) }\n\
        \        let uniqueWeights = uniqueWeightsSet.sorted()\n\n        func check(_\
        \ threshold: Int) -> Bool {\n            let INF = Int.max / 2\n           \
        \ var dist = [Int](repeating: INF, count: n)\n            dist[0] = 0\n    \
        \        for u in topoOrder {\n                if dist[u] >= INF || dist[u]\
        \ > k { continue }\n                for (v, cost) in adj[u] {\n            \
        \        if online[v] && cost >= threshold {\n                        let newDist\
        \ = dist[u] + cost\n                        if newDist < dist[v] {\n       \
        \                     dist[v] = newDist\n                        }\n       \
        \             }\n                }\n            }\n            return dist[n\
        \ - 1] <= k\n        }\n\n        var low = 0\n        var high = uniqueWeights.count\
        \ - 1\n        var ans = -1\n        while low <= high {\n            let mid\
        \ = (low + high) / 2\n            if check(uniqueWeights[mid]) {\n         \
        \       ans = uniqueWeights[mid]\n                low = mid + 1\n          \
        \  } else {\n                high = mid - 1\n            }\n        }\n    \
        \    return ans\n    }\n}"
      kotlin: "import java.util.*\n\nclass Solution {\n    fun findMaxPathScore(edges:\
        \ Array<IntArray>, online: BooleanArray, k: Long): Int {\n        val n = online.size\n\
        \        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }\n        val\
        \ inDegree = IntArray(n)\n        for (edge in edges) {\n            val u =\
        \ edge[0]\n            val v = edge[1]\n            val cost = edge[2]\n   \
        \         adj[u].add(v to cost)\n            inDegree[v]++\n        }\n\n  \
        \      val queue: Queue<Int> = LinkedList()\n        for (i in 0 until n) {\n\
        \            if (inDegree[i] == 0) {\n                queue.add(i)\n       \
        \     }\n        }\n\n        val topoOrder = IntArray(n)\n        var idx =\
        \ 0\n        while (queue.isNotEmpty()) {\n            val u = queue.poll()\n\
        \            topoOrder[idx++] = u\n            for (neighbor in adj[u]) {\n\
        \                val v = neighbor.first\n                inDegree[v]--\n   \
        \             if (inDegree[v] == 0) {\n                    queue.add(v)\n  \
        \              }\n            }\n        }\n\n        val weights = edges.map\
        \ { it[2] }.distinct().sorted()\n        if (weights.isEmpty()) return -1\n\n\
        \        fun check(threshold: Int): Boolean {\n            val INF = Long.MAX_VALUE\
        \ / 2\n            val dist = LongArray(n) { INF }\n            dist[0] = 0L\n\
        \            for (u in topoOrder) {\n                if (dist[u] >= INF || dist[u]\
        \ > k) continue\n                for (neighbor in adj[u]) {\n              \
        \      val v = neighbor.first\n                    val cost = neighbor.second\n\
        \                    if (online[v] && cost >= threshold) {\n               \
        \         val newDist = dist[u] + cost.toLong()\n                        if\
        \ (newDist < dist[v]) {\n                            dist[v] = newDist\n   \
        \                     }\n                    }\n                }\n        \
        \    }\n            return dist[n - 1] <= k\n        }\n\n        var low =\
        \ 0\n        var high = weights.size - 1\n        var ans = -1\n        while\
        \ (low <= high) {\n            val mid = low + (high - low) / 2\n          \
        \  if (check(weights[mid])) {\n                ans = weights[mid]\n        \
        \        low = mid + 1\n            } else {\n                high = mid - 1\n\
        \            }\n        }\n        return ans\n    }\n}"
      dart: "class Solution {\n  int findMaxPathScore(List<List<int>> edges, List<bool>\
        \ online, int k) {\n    int n = online.length;\n    List<List<_Edge>> adj =\
        \ List.generate(n, (_) => []);\n    List<int> inDegree = List.filled(n, 0);\n\
        \n    for (var edge in edges) {\n      int u = edge[0];\n      int v = edge[1];\n\
        \      int cost = edge[2];\n      adj[u].add(_Edge(v, cost));\n      inDegree[v]++;\n\
        \    }\n\n    List<int> queue = [];\n    for (int i = 0; i < n; i++) {\n   \
        \   if (inDegree[i] == 0) {\n        queue.add(i);\n      }\n    }\n\n    List<int>\
        \ topoOrder = [];\n    int head = 0;\n    while (head < queue.length) {\n  \
        \    int u = queue[head++];\n      topoOrder.add(u);\n      for (var edge in\
        \ adj[u]) {\n        inDegree[edge.to]--;\n        if (inDegree[edge.to] ==\
        \ 0) {\n          queue.add(edge.to);\n        }\n      }\n    }\n\n    List<int>\
        \ uniqueCosts = edges.map((e) => e[2]).toSet().toList();\n    uniqueCosts.sort();\n\
        \n    bool check(int threshold) {\n      List<int> dist = List.filled(n, 1000000000000000);\n\
        \      dist[0] = 0;\n      for (int i = 0; i < topoOrder.length; i++) {\n  \
        \      int u = topoOrder[i];\n        if (!online[u] || dist[u] > k) continue;\n\
        \        for (var edge in adj[u]) {\n          if (online[edge.to] && edge.cost\
        \ >= threshold) {\n            if (dist[u] + edge.cost < dist[edge.to]) {\n\
        \              dist[edge.to] = dist[u] + edge.cost;\n            }\n       \
        \   }\n        }\n      }\n      return dist[n - 1] <= k;\n    }\n\n    int\
        \ ans = -1;\n    int low = 0;\n    int high = uniqueCosts.length - 1;\n    while\
        \ (low <= high) {\n      int mid = low + (high - low) ~/ 2;\n      if (check(uniqueCosts[mid]))\
        \ {\n        ans = uniqueCosts[mid];\n        low = mid + 1;\n      } else {\n\
        \        high = mid - 1;\n      }\n    }\n\n    return ans;\n  }\n}\n\nclass\
        \ _Edge {\n  final int to;\n  final int cost;\n  _Edge(this.to, this.cost);\n\
        }"
      go: "import (\n\t\"sort\"\n)\n\nfunc findMaxPathScore(edges [][]int, online []bool,\
        \ k int64) int {\n\ttype edge struct {\n\t\tto   int\n\t\tcost int\n\t}\n\n\t\
        n := len(online)\n\tadj := make([][]edge, n)\n\tinDegree := make([]int, n)\n\
        \tfor _, e := range edges {\n\t\tu, v, cost := e[0], e[1], e[2]\n\t\tadj[u]\
        \ = append(adj[u], edge{v, cost})\n\t\tinDegree[v]++\n\t}\n\n\tqueue := make([]int,\
        \ 0, n)\n\tfor i := 0; i < n; i++ {\n\t\tif inDegree[i] == 0 {\n\t\t\tqueue\
        \ = append(queue, i)\n\t\t}\n\t}\n\n\ttopoOrder := make([]int, 0, n)\n\tfor\
        \ len(queue) > 0 {\n\t\tu := queue[0]\n\t\tqueue = queue[1:]\n\t\ttopoOrder\
        \ = append(topoOrder, u)\n\t\tfor _, e := range adj[u] {\n\t\t\tinDegree[e.to]--\n\
        \t\t\tif inDegree[e.to] == 0 {\n\t\t\t\tqueue = append(queue, e.to)\n\t\t\t\
        }\n\t\t}\n\t}\n\n\tcostMap := make(map[int]bool)\n\tfor _, e := range edges\
        \ {\n\t\tcostMap[e[2]] = true\n\t}\n\tuniqueCosts := make([]int, 0, len(costMap))\n\
        \tfor c := range costMap {\n\t\tuniqueCosts = append(uniqueCosts, c)\n\t}\n\t\
        sort.Ints(uniqueCosts)\n\n\tcheck := func(threshold int) bool {\n\t\tdist :=\
        \ make([]int64, n)\n\t\tfor i := range dist {\n\t\t\tdist[i] = 1000000000000000\n\
        \t\t}\n\t\tdist[0] = 0\n\n\t\tfor _, u := range topoOrder {\n\t\t\tif !online[u]\
        \ || dist[u] > k {\n\t\t\t\tcontinue\n\t\t\t}\n\t\t\tfor _, e := range adj[u]\
        \ {\n\t\t\t\tif online[e.to] && e.cost >= threshold {\n\t\t\t\t\tif dist[u]+int64(e.cost)\
        \ < dist[e.to] {\n\t\t\t\t\t\tdist[e.to] = dist[u] + int64(e.cost)\n\t\t\t\t\
        \t}\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t\treturn dist[n-1] <= k\n\t}\n\n\tans := -1\n\
        \tlow, high := 0, len(uniqueCosts)-1\n\tfor low <= high {\n\t\tmid := (low +\
        \ high) / 2\n\t\tif check(uniqueCosts[mid]) {\n\t\t\tans = uniqueCosts[mid]\n\
        \t\t\tlow = mid + 1\n\t\t} else {\n\t\t\thigh = mid - 1\n\t\t}\n\t}\n\n\treturn\
        \ ans\n}"
      ruby: "def find_max_path_score(edges, online, k)\n  n = online.length\n  adj =\
        \ Array.new(n) { [] }\n  in_degree = Array.new(n, 0)\n\n  edges.each do |e|\n\
        \    u, v, cost = e[0], e[1], e[2]\n    adj[u] << [v, cost]\n    in_degree[v]\
        \ += 1\n  end\n\n  queue = []\n  n.times { |i| queue << i if in_degree[i] ==\
        \ 0 }\n\n  topo_order = []\n  head = 0\n  while head < queue.length\n    u =\
        \ queue[head]\n    head += 1\n    topo_order << u\n    adj[u].each do |v, cost|\n\
        \      in_degree[v] -= 1\n      queue << v if in_degree[v] == 0\n    end\n \
        \ end\n\n  unique_costs = edges.map { |e| e[2] }.uniq.sort\n\n  check = lambda\
        \ do |threshold|\n    dist = Array.new(n, 1000000000000000)\n    dist[0] = 0\n\
        \    topo_order.each do |u|\n      next if !online[u] || dist[u] > k\n     \
        \ adj[u].each do |v, cost|\n        if online[v] && cost >= threshold\n    \
        \      if dist[u] + cost < dist[v]\n            dist[v] = dist[u] + cost\n \
        \         end\n        end\n      end\n    end\n    dist[n - 1] <= k\n  end\n\
        \n  ans = -1\n  low = 0\n  high = unique_costs.length - 1\n  while low <= high\n\
        \    mid = (low + high) / 2\n    if check.call(unique_costs[mid])\n      ans\
        \ = unique_costs[mid]\n      low = mid + 1\n    else\n      high = mid - 1\n\
        \    end\n  end\n\n  ans\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    case class Edge(to:\
        \ Int, cost: Int)\n\n    def findMaxPathScore(edges: Array[Array[Int]], online:\
        \ Array[Boolean], k: Long): Int = {\n        val n = online.length\n       \
        \ val adj = Array.tabulate(n)(_ => mutable.ArrayBuffer.empty[Edge])\n      \
        \  val inDegree = new Array[Int](n)\n\n        for (edge <- edges) {\n     \
        \       val u = edge(0)\n            val v = edge(1)\n            val cost =\
        \ edge(2)\n            adj(u) += Edge(v, cost)\n            inDegree(v) += 1\n\
        \        }\n\n        val queue = mutable.Queue[Int]()\n        for (i <- 0\
        \ until n) if (inDegree(i) == 0) queue.enqueue(i)\n\n        val topoOrder =\
        \ new Array[Int](n)\n        var topoIdx = 0\n        while (queue.nonEmpty)\
        \ {\n            val u = queue.dequeue()\n            topoOrder(topoIdx) = u\n\
        \            topoIdx += 1\n            for (e <- adj(u)) {\n               \
        \ inDegree(e.to) -= 1\n                if (inDegree(e.to) == 0) queue.enqueue(e.to)\n\
        \            }\n        }\n\n        val uniqueCosts = edges.map(_(2)).distinct.sorted\n\
        \n        def check(threshold: Int): Boolean = {\n            val dist = Array.fill(n)(1000000000000000L)\n\
        \            dist(0) = 0L\n            var i = 0\n            while (i < n)\
        \ {\n                val u = topoOrder(i)\n                if (online(u) &&\
        \ dist(u) <= k) {\n                    val neighbors = adj(u)\n            \
        \        var j = 0\n                    while (j < neighbors.length) {\n   \
        \                     val e = neighbors(j)\n                        if (online(e.to)\
        \ && e.cost >= threshold) {\n                            val newDist = dist(u)\
        \ + e.cost\n                            if (newDist < dist(e.to)) {\n      \
        \                          dist(e.to) = newDist\n                          \
        \  }\n                        }\n                        j += 1\n          \
        \          }\n                }\n                i += 1\n            }\n   \
        \         dist(n - 1) <= k\n        }\n\n        var ans = -1\n        var low\
        \ = 0\n        var high = uniqueCosts.length - 1\n        while (low <= high)\
        \ {\n            val mid = (low + high) / 2\n            if (check(uniqueCosts(mid)))\
        \ {\n                ans = uniqueCosts(mid)\n                low = mid + 1\n\
        \            } else {\n                high = mid - 1\n            }\n     \
        \   }\n        ans\n    }\n}"
      rust: "use std::collections::VecDeque;\n\nimpl Solution {\n    pub fn find_max_path_score(edges:\
        \ Vec<Vec<i32>>, online: Vec<bool>, k: i64) -> i32 {\n        let n = online.len();\n\
        \        let mut adj = vec![vec![]; n];\n        let mut in_degree = vec![0;\
        \ n];\n\n        for edge in &edges {\n            let u = edge[0] as usize;\n\
        \            let v = edge[1] as usize;\n            let cost = edge[2];\n  \
        \          if online[u] && online[v] {\n                adj[u].push((v, cost));\n\
        \                in_degree[v] += 1;\n            }\n        }\n\n        let\
        \ mut topo_order = Vec::with_capacity(n);\n        let mut queue = VecDeque::new();\n\
        \        for i in 0..n {\n            if online[i] && in_degree[i] == 0 {\n\
        \                queue.push_back(i);\n            }\n        }\n\n        while\
        \ let Some(u) = queue.pop_front() {\n            topo_order.push(u);\n     \
        \       for &(v, _) in &adj[u] {\n                in_degree[v] -= 1;\n     \
        \           if in_degree[v] == 0 {\n                    queue.push_back(v);\n\
        \                }\n            }\n        }\n\n        let mut unique_costs:\
        \ Vec<i32> = edges\n            .iter()\n            .filter(|e| online[e[0]\
        \ as usize] && online[e[1] as usize])\n            .map(|e| e[2])\n        \
        \    .collect();\n        unique_costs.sort_unstable();\n        unique_costs.dedup();\n\
        \n        let mut low = 0;\n        let mut high = (unique_costs.len() as i32)\
        \ - 1;\n        let mut ans = -1;\n\n        while low <= high {\n         \
        \   let mid = low + (high - low) / 2;\n            let threshold = unique_costs[mid\
        \ as usize];\n            if Self::check(threshold, &topo_order, &adj, n, k)\
        \ {\n                ans = threshold;\n                low = mid + 1;\n    \
        \        } else {\n                high = mid - 1;\n            }\n        }\n\
        \n        ans\n    }\n\n    fn check(threshold: i32, topo_order: &[usize], adj:\
        \ &[Vec<(usize, i32)>], n: usize, k: i64) -> bool {\n        let mut dist =\
        \ vec![i64::MAX; n];\n        dist[0] = 0;\n        for &u in topo_order {\n\
        \            if dist[u] == i64::MAX {\n                continue;\n         \
        \   }\n            for &(v, cost) in &adj[u] {\n                if cost >= threshold\
        \ {\n                    let new_dist = dist[u] + cost as i64;\n           \
        \         if new_dist <= k && new_dist < dist[v] {\n                       \
        \ dist[v] = new_dist;\n                    }\n                }\n          \
        \  }\n        }\n        dist[n - 1] <= k\n    }\n}"
      racket: "(require racket/list)\n\n(define/contract (find-max-path-score edges\
        \ online k)\n  (-> (listof (listof exact-integer?)) (listof boolean?) exact-integer?\
        \ exact-integer?)\n  (let* ([n (length online)]\n         [online-vec (list->vector\
        \ online)]\n         [adj (make-vector n '())]\n         [in-degree (make-vector\
        \ n 0)])\n    (for ([edge edges])\n      (let ([u (first edge)]\n          \
        \  [v (second edge)]\n            [cost (third edge)])\n        (when (and (vector-ref\
        \ online-vec u) (vector-ref online-vec v))\n          (vector-set! adj u (cons\
        \ (cons v cost) (vector-ref adj u)))\n          (vector-set! in-degree v (+\
        \ (vector-ref in-degree v) 1)))))\n\n    (let ([topo-order '()]\n          [queue\
        \ '()])\n      (for ([i (in-range n)])\n        (when (and (vector-ref online-vec\
        \ i) (= (vector-ref in-degree i) 0))\n          (set! queue (cons i queue))))\n\
        \      (let loop ([q queue])\n        (unless (null? q)\n          (let* ([u\
        \ (car q)]\n                 [next-q (cdr q)])\n            (set! topo-order\
        \ (cons u topo-order))\n            (let ([current-next-q next-q])\n       \
        \       (for ([edge (vector-ref adj u)])\n                (let ([v (car edge)])\n\
        \                  (vector-set! in-degree v (- (vector-ref in-degree v) 1))\n\
        \                  (when (= (vector-ref in-degree v) 0)\n                  \
        \  (set! current-next-q (cons v current-next-q)))))\n              (loop current-next-q)))))\n\
        \      (set! topo-order (reverse topo-order))\n\n      (let* ([valid-costs (filter-map\
        \ (lambda (e)\n                                        (if (and (vector-ref\
        \ online-vec (first e))\n                                                 (vector-ref\
        \ online-vec (second e)))\n                                            (third\
        \ e)\n                                            #f))\n                   \
        \                   edges)]\n             [unique-costs (list->vector (sort\
        \ (remove-duplicates valid-costs) <))])\n        (define (check threshold)\n\
        \          (let ([dist (make-vector n -1)])\n            (vector-set! dist 0\
        \ 0)\n            (for ([u topo-order])\n              (let ([du (vector-ref\
        \ dist u)])\n                (unless (= du -1)\n                  (for ([edge\
        \ (vector-ref adj u)])\n                    (let ([v (car edge)]\n         \
        \                 [cost (cdr edge)])\n                      (when (>= cost threshold)\n\
        \                        (let ([new-dist (+ du cost)])\n                   \
        \       (when (<= new-dist k)\n                            (let ([dv (vector-ref\
        \ dist v)])\n                              (when (or (= dv -1) (< new-dist dv))\n\
        \                                (vector-set! dist v new-dist)))))))))))\n \
        \           (let ([final (vector-ref dist (- n 1))])\n              (and (not\
        \ (= final -1)) (<= final k)))))\n\n        (let bsearch ([low 0] [high (- (vector-length\
        \ unique-costs) 1)] [ans -1])\n          (if (> low high)\n              ans\n\
        \              (let* ([mid (quotient (+ low high) 2)]\n                    \
        \ [threshold (vector-ref unique-costs mid)])\n                (if (check threshold)\n\
        \                    (bsearch (+ mid 1) high threshold)\n                  \
        \  (bsearch low (- mid 1) ans)))))))))"
      erlang: "-spec find_max_path_score(Edges :: [[integer()]], Online :: [boolean()],\
        \ K :: integer()) -> integer().\nfind_max_path_score(Edges, Online, K) ->\n\
        \    OnlineVec = list_to_tuple(Online),\n    N = tuple_size(OnlineVec),\n  \
        \  ValidEdges = [ {U, V, C} || [U, V, C] <- Edges, \n                      \
        \          element(U + 1, OnlineVec), \n                                element(V\
        \ + 1, OnlineVec) ],\n    InDegree = lists:foldl(fun({_U, V, _C}, Acc) ->\n\
        \        Acc#{V => maps:get(V, Acc, 0) + 1}\n    end, #{}, ValidEdges),\n  \
        \  Adj = lists:foldl(fun({U, V, C}, Acc) ->\n        Acc#{U => [{V, C} | maps:get(U,\
        \ Acc, [])]}\n    end, #{}, ValidEdges),\n    InAdj = lists:foldl(fun({U, V,\
        \ C}, Acc) ->\n        Acc#{V => [{U, C} | maps:get(V, Acc, [])]}\n    end,\
        \ #{}, ValidEdges),\n\n    InitialQueue = [I || I <- lists:seq(0, N-1), \n \
        \                        element(I + 1, OnlineVec), \n                     \
        \    maps:get(I, InDegree, 0) == 0],\n\n    TopoSort = fun TS([], _Degs, Acc)\
        \ -> lists:reverse(Acc);\n                   TS([U | Rest], Degs, Acc) ->\n\
        \                       Neighbors = maps:get(U, Adj, []),\n                \
        \       {NewQueue, NewDegs} = lists:foldl(fun({V, _C}, {Q, D}) ->\n        \
        \                   DV = maps:get(V, D) - 1,\n                           if\
        \ DV == 0 -> {[V | Q], D#{V => DV}}; true -> {Q, D#{V => DV}} end\n        \
        \               end, {Rest, Degs}, Neighbors),\n                       TS(NewQueue,\
        \ NewDegs, [U | Acc])\n               end,\n    TopoOrder = TopoSort(InitialQueue,\
        \ InDegree, []),\n\n    UniqueCosts = lists:usort([C || {_, _, C} <- ValidEdges]),\n\
        \    UniqueCostsTuple = list_to_tuple(UniqueCosts),\n\n    Check = fun(Threshold)\
        \ ->\n        FinalDistMap = lists:foldl(fun(V, Acc) ->\n            if V ==\
        \ 0 -> Acc#{0 => 0};\n               true ->\n                   Predecessors\
        \ = maps:get(V, InAdj, []),\n                   MinV = lists:foldl(fun({U, C},\
        \ CurrentMin) ->\n                       if C >= Threshold ->\n            \
        \                case maps:find(U, Acc) of\n                               \
        \ {ok, DU} ->\n                                    NewD = DU + C,\n        \
        \                            if NewD =< K andalso (CurrentMin == infinity orelse\
        \ NewD < CurrentMin) -> NewD;\n                                       true ->\
        \ CurrentMin\n                                    end;\n                   \
        \             error -> CurrentMin\n                            end;\n      \
        \                    true -> CurrentMin\n                       end\n      \
        \             end, infinity, Predecessors),\n                   if MinV == infinity\
        \ -> Acc; true -> Acc#{V => MinV} end\n            end\n        end, #{}, TopoOrder),\n\
        \        case maps:find(N - 1, FinalDistMap) of\n            {ok, Dist} -> Dist\
        \ =< K;\n            error -> false\n        end\n    end,\n\n    BS = fun BS_inner(Low,\
        \ High, Best) ->\n        if Low > High -> Best;\n           true ->\n     \
        \          Mid = (Low + High) div 2,\n               Threshold = element(Mid\
        \ + 1, UniqueCostsTuple),\n               case Check(Threshold) of\n       \
        \            true -> BS_inner(Mid + 1, High, Threshold);\n                 \
        \  false -> BS_inner(Low, Mid - 1, Best)\n               end\n        end\n\
        \    end,\n    BS(0, tuple_size(UniqueCostsTuple) - 1, -1)."
      elixir: "defmodule Solution do\n  @spec find_max_path_score(edges :: [[integer]],\
        \ online :: [boolean], k :: integer) :: integer\n  def find_max_path_score(edges,\
        \ online, k) do\n    n = length(online)\n    online_tuple = List.to_tuple(online)\n\
        \n    valid_edges = for [u, v, c] <- edges, elem(online_tuple, u) and elem(online_tuple,\
        \ v), do: {u, v, c}\n\n    in_degree_map = Enum.reduce(valid_edges, %{}, fn\
        \ {_, v, _}, acc ->\n      Map.update(acc, v, 1, &(&1 + 1))\n    end)\n\n  \
        \  adj_map = Enum.reduce(valid_edges, %{}, fn {u, v, c}, acc ->\n      Map.update(acc,\
        \ u, [{v, c}], &([{v, c} | &1]))\n    end)\n\n    in_adj_map = Enum.reduce(valid_edges,\
        \ %{}, fn {u, v, c}, acc ->\n      Map.update(acc, v, [{u, c}], &([{u, c} |\
        \ &1]))\n    end)\n\n    initial_queue = Enum.filter(0..(n - 1), fn i ->\n \
        \     elem(online_tuple, i) and Map.get(in_degree_map, i, 0) == 0\n    end)\n\
        \n    topo_order = do_topo_sort(initial_queue, in_degree_map, adj_map, [])\n\
        \n    unique_costs = valid_edges |> Enum.map(fn {_, _, c} -> c end) |> Enum.sort()\
        \ |> Enum.uniq() |> List.to_tuple()\n\n    binary_search(0, tuple_size(unique_costs)\
        \ - 1, unique_costs, topo_order, in_adj_map, k, n, -1)\n  end\n\n  defp do_topo_sort([],\
        \ _degs, _adj, acc), do: Enum.reverse(acc)\n  defp do_topo_sort([u | rest],\
        \ degs, adj, acc) do\n    {new_queue, new_degs} = Enum.reduce(Map.get(adj, u,\
        \ []), {rest, degs}, fn {v, _}, {q, d} ->\n      dv = Map.get(d, v) - 1\n  \
        \    if dv == 0, do: {[v | q], Map.put(d, v, dv)}, else: {q, Map.put(d, v, dv)}\n\
        \    end)\n    do_topo_sort(new_queue, new_degs, adj, [u | acc])\n  end\n\n\
        \  defp check(threshold, topo_order, in_adj, k, n) do\n    dist_map = Enum.reduce(topo_order,\
        \ %{}, fn v, acc ->\n      cond do\n        v == 0 -> Map.put(acc, 0, 0)\n \
        \       true ->\n          min_val = Enum.reduce(Map.get(in_adj, v, []), :infinity,\
        \ fn {u, cost}, current_min ->\n            if cost >= threshold do\n      \
        \        case Map.get(acc, u, :infinity) do\n                :infinity -> current_min\n\
        \                du ->\n                  new_dist = du + cost\n           \
        \       if new_dist <= k and (current_min == :infinity or new_dist < current_min),\
        \ do: new_dist, else: current_min\n              end\n            else\n   \
        \           current_min\n            end\n          end)\n          if min_val\
        \ != :infinity, do: Map.put(acc, v, min_val), else: acc\n      end\n    end)\n\
        \    Map.get(dist_map, n - 1, :infinity) != :infinity\n  end\n\n  defp binary_search(low,\
        \ high, unique_costs, topo_order, in_adj, k, n, best) do\n    if low > high\
        \ do\n      best\n    else\n      mid = div(low + high, 2)\n      threshold\
        \ = elem(unique_costs, mid)\n      if check(threshold, topo_order, in_adj, k,\
        \ n) do\n        binary_search(mid + 1, high, unique_costs, topo_order, in_adj,\
        \ k, n, threshold)\n      else\n        binary_search(low, mid - 1, unique_costs,\
        \ topo_order, in_adj, k, n, best)\n      end\n    end\n  end\nend"
    approach: 'To find the maximum possible minimum edge cost (score), we use binary
      search over the unique edge weights present in the graph. For a fixed weight $X$,
      we test if there exists a valid path from node 0 to node $n-1$ where every edge
      in the path has a cost at least $X$. A path is valid if all its intermediate nodes
      are online and its total cost does not exceed $k$. Since node 0 and node $n-1$
      are always online, this is equivalent to requiring that every node on the path
      is online. We filter out all nodes that are offline and any edges connected to
      them, leaving a subgraph where only online nodes and edges between them exist.


      In each step of the binary search, we perform a reachability check with a cost
      constraint. Because the graph is a Directed Acyclic Graph (DAG), we can find the
      shortest path from node 0 to $n-1$ in $O(N+M)$ time using dynamic programming
      in topological order. We pre-compute a topological order for all online nodes
      once. For a given threshold $X$, we relax edges only if their cost is $\ge X$.
      If the shortest path distance to node $n-1$ is less than or equal to $k$, then
      the threshold $X$ is achievable. The binary search ensures we find the largest
      such $X$.'
    time_complexity: O((N + M) \log M) where $N$ is the number of nodes and $M$ is the
      number of edges. Topological sorting takes $O(N + M)$, and the binary search runs
      for $O(\log M)$ iterations, with each iteration performing a DP traversal over
      the graph in $O(N + M)$ time.
    space_complexity: O(N + M) to store the adjacency list of the graph, the topological
      order, and the DP array for shortest path distances.
    elapsed_time: 704.6172313690186
    model: gemini-3-flash-preview
    generated_at: '2026-07-03 02:22:09 '
---

## Problem #3620: Network Recovery Pathways

**Difficulty:** Hard

**Topics:** Array, Binary Search, Dynamic Programming, Graph Theory, Topological Sort, Heap (Priority Queue), Shortest Path

## Problem Description

<p data-end="502" data-start="75">You are given a directed acyclic graph of <code>n</code> nodes numbered from 0 to <code>n &minus; 1</code>. This is represented by a 2D array <code data-end="201" data-start="194">edges</code> of length<font face="monospace"> <code>m</code></font>, where <code data-end="255" data-start="227">edges[i] = [u<sub>i</sub>, v<sub>i</sub>, cost<sub>i</sub>]</code> indicates a one‑way communication from node <code data-end="304" data-start="300">u<sub>i</sub></code> to node <code data-end="317" data-start="313">v<sub>i</sub></code> with a recovery cost of <code data-end="349" data-start="342">cost<sub>i</sub></code>.</p>

<p data-end="502" data-start="75">Some nodes may be offline. You are given a boolean array <code data-end="416" data-start="408">online</code> where <code data-end="441" data-start="423">online[i] = true</code> means node <code data-end="456" data-start="453">i</code> is online. Nodes 0 and <code>n &minus; 1</code> are always online.</p>

<p data-end="547" data-start="504">A path from 0 to <code>n &minus; 1</code> is <strong data-end="541" data-start="532">valid</strong> if:</p>

<ul>
	<li>All intermediate nodes on the path are online.</li>
	<li data-end="676" data-start="605">The total recovery cost of all edges on the path does not exceed <code>k</code>.</li>
</ul>

<p data-end="771" data-start="653">For each valid path, define its <strong data-end="694" data-start="685">score</strong> as the minimum edge‑cost along that path.</p>

<p data-end="913" data-start="847">Return the <strong>maximum</strong> path score (i.e., the largest <strong>minimum</strong>-edge cost) among all valid paths. If no valid path exists, return -1.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">edges = [[0,1,5],[1,3,10],[0,2,3],[2,3,4]], online = [true,true,true,true], k = 10</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/06/06/graph-10.png" style="width: 239px; height: 267px;" /></p>

<ul data-end="551" data-start="146">
	<li data-end="462" data-start="146">
	<p data-end="206" data-start="148">The graph has two possible routes from node 0 to node 3:</p>

	<ol data-end="462" data-start="209">
		<li data-end="315" data-start="209">
		<p data-end="228" data-start="212">Path <code>0 &rarr; 1 &rarr; 3</code></p>

		<ul data-end="315" data-start="234">
			<li data-end="315" data-start="234">
			<p data-end="315" data-start="236">Total cost = <code>5 + 10 = 15</code>, which exceeds k (<code>15 &gt; 10</code>), so this path is invalid.</p>
			</li>
		</ul>
		</li>
		<li data-end="462" data-start="318">
		<p data-end="337" data-start="321">Path <code>0 &rarr; 2 &rarr; 3</code></p>

		<ul data-end="462" data-start="343">
			<li data-end="397" data-start="343">
			<p data-end="397" data-start="345">Total cost = <code>3 + 4 = 7 &lt;= k</code>, so this path is valid.</p>
			</li>
			<li data-end="462" data-start="403">
			<p data-end="462" data-start="405">The minimum edge‐cost along this path is <code>min(3, 4) = 3</code>.</p>
			</li>
		</ul>
		</li>
	</ol>
	</li>
	<li data-end="551" data-start="463">
	<p data-end="551" data-start="465">There are no other valid paths. Hence, the maximum among all valid path‐scores is 3.</p>
	</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">edges = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], online = [true,true,true,false,true], k = 12</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/06/06/graph-11.png" style="width: 343px; height: 194px;" /></p>

<ul>
	<li data-end="790" data-start="726">
	<p data-end="790" data-start="728">Node 3 is offline, so any path passing through 3 is invalid.</p>
	</li>
	<li data-end="1231" data-start="791">
	<p data-end="837" data-start="793">Consider the remaining routes from 0 to 4:</p>

	<ol data-end="1231" data-start="840">
		<li data-end="985" data-start="840">
		<p data-end="859" data-start="843">Path <code>0 &rarr; 1 &rarr; 4</code></p>

		<ul data-end="985" data-start="865">
			<li data-end="920" data-start="865">
			<p data-end="920" data-start="867">Total cost = <code>7 + 5 = 12 &lt;= k</code>, so this path is valid.</p>
			</li>
			<li data-end="985" data-start="926">
			<p data-end="985" data-start="928">The minimum edge‐cost along this path is <code>min(7, 5) = 5</code>.</p>
			</li>
		</ul>
		</li>
		<li data-end="1083" data-start="988">
		<p data-end="1011" data-start="991">Path <code>0 &rarr; 2 &rarr; 3 &rarr; 4</code></p>

		<ul data-end="1083" data-start="1017">
			<li data-end="1083" data-start="1017">
			<p data-end="1083" data-start="1019">Node 3 is offline, so this path is invalid regardless of cost.</p>
			</li>
		</ul>
		</li>
		<li data-end="1231" data-start="1086">
		<p data-end="1105" data-start="1089">Path <code>0 &rarr; 2 &rarr; 4</code></p>

		<ul data-end="1231" data-start="1111">
			<li data-end="1166" data-start="1111">
			<p data-end="1166" data-start="1113">Total cost = <code>6 + 6 = 12 &lt;= k</code>, so this path is valid.</p>
			</li>
			<li data-end="1231" data-start="1172">
			<p data-end="1231" data-start="1174">The minimum edge‐cost along this path is <code>min(6, 6) = 6</code>.</p>
			</li>
		</ul>
		</li>
	</ol>
	</li>
	<li data-end="1314" data-is-last-node="" data-start="1232">
	<p data-end="1314" data-is-last-node="" data-start="1234">Among the two valid paths, their scores are 5 and 6. Therefore, the answer is 6.</p>
	</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li data-end="42" data-start="20"><code data-end="40" data-start="20">n == online.length</code></li>
	<li data-end="63" data-start="45"><code data-end="61" data-start="45">2 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li data-end="102" data-start="66"><code data-end="100" data-start="66">0 &lt;= m == edges.length &lt;= </code><code>min(10<sup>5</sup>, n * (n - 1) / 2)</code></li>
	<li data-end="102" data-start="66"><code data-end="127" data-start="105">edges[i] = [u<sub>i</sub>, v<sub>i</sub>, cost<sub>i</sub>]</code></li>
	<li data-end="151" data-start="132"><code data-end="149" data-start="132">0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt; n</code></li>
	<li data-end="166" data-start="154"><code data-end="164" data-start="154">u<sub>i</sub> != v<sub>i</sub></code></li>
	<li data-end="191" data-start="169"><code data-end="189" data-start="169">0 &lt;= cost<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li data-end="213" data-start="194"><code data-end="211" data-start="194">0 &lt;= k &lt;= 5 * 10<sup>13</sup></code></li>
	<li data-end="309" data-start="216"><code data-end="227" data-start="216">online[i]</code> is either <code data-end="244" data-is-only-node="" data-start="238">true</code> or <code data-end="255" data-start="248">false</code>, and both <code data-end="277" data-start="266">online[0]</code> and <code data-end="295" data-start="282">online[n &minus; 1]</code> are <code data-end="306" data-start="300">true</code>.</li>
	<li data-end="362" data-is-last-node="" data-start="312">The given graph is a directed acyclic graph.</li>
</ul>


## Hints

1. Use binary search on `ans`.

2. Check if a particular `ans` is possible by including only the edges with weights ≥ `mid` (the current binary‐search pivot).

3. Implement the check function using either `Dijkstra` or DP (via topological sorting, since the graph is a DAG).

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To find the maximum possible minimum edge cost (score), we use binary search over the unique edge weights present in the graph. For a fixed weight $X$, we test if there exists a valid path from node 0 to node $n-1$ where every edge in the path has a cost at least $X$. A path is valid if all its intermediate nodes are online and its total cost does not exceed $k$. Since node 0 and node $n-1$ are always online, this is equivalent to requiring that every node on the path is online. We filter out all nodes that are offline and any edges connected to them, leaving a subgraph where only online nodes and edges between them exist.

In each step of the binary search, we perform a reachability check with a cost constraint. Because the graph is a Directed Acyclic Graph (DAG), we can find the shortest path from node 0 to $n-1$ in $O(N+M)$ time using dynamic programming in topological order. We pre-compute a topological order for all online nodes once. For a given threshold $X$, we relax edges only if their cost is $\ge X$. If the shortest path distance to node $n-1$ is less than or equal to $k$, then the threshold $X$ is achievable. The binary search ensures we find the largest such $X$.

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
    int findMaxPathScore(vector<vector<int>>& edges, vector<bool>& online, long long k) {
        int n = online.size();
        vector<vector<pair<int, int>>> adj(n);
        vector<int> in_degree(n, 0);
        vector<int> all_costs;

        for (auto& e : edges) {
            int u = e[0], v = e[1], cost = e[2];
            if (online[u] && online[v]) {
                adj[u].push_back({v, cost});
                in_degree[v]++;
                all_costs.push_back(cost);
            }
        }

        vector<int> topo_order;
        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (online[i] && in_degree[i] == 0) {
                q.push(i);
            }
        }

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            topo_order.push_back(u);
            for (auto& edge : adj[u]) {
                if (--in_degree[edge.first] == 0) {
                    q.push(edge.first);
                }
            }
        }

        sort(all_costs.begin(), all_costs.end());
        all_costs.erase(unique(all_costs.begin(), all_costs.end()), all_costs.end());

        auto check = [&](int min_edge_cost) {
            vector<long long> dist(n, 1000000000000000LL);
            dist[0] = 0;
            for (int u : topo_order) {
                if (dist[u] > k) continue;
                for (auto& edge : adj[u]) {
                    if (edge.second >= min_edge_cost) {
                        if (dist[u] + edge.second < dist[edge.first]) {
                            dist[edge.first] = dist[u] + edge.second;
                        }
                    }
                }
            }
            return dist[n - 1] <= k;
        };

        int low = 0, high = (int)all_costs.size() - 1, ans = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (check(all_costs[mid])) {
                ans = all_costs[mid];
                low = mid + 1;
            } else {
                high = mid - 1;
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
import java.util.*;

class Solution {
    static class Edge {
        int to;
        int cost;
        Edge(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }
    }

    public int findMaxPathScore(int[][] edges, boolean[] online, long k) {
        int n = online.length;
        ArrayList<Edge>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        int[] inDegree = new int[n];

        int edgeCount = 0;
        for (int[] e : edges) {
            if (online[e[0]] && online[e[1]]) edgeCount++;
        }

        int[] allCosts = new int[edgeCount];
        int costIdx = 0;
        for (int[] e : edges) {
            int u = e[0], v = e[1], cost = e[2];
            if (online[u] && online[v]) {
                adj[u].add(new Edge(v, cost));
                inDegree[v]++;
                allCosts[costIdx++] = cost;
            }
        }

        int[] topoOrder = new int[n];
        int topoPtr = 0;
        ArrayDeque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            if (online[i] && inDegree[i] == 0) q.add(i);
        }

        while (!q.isEmpty()) {
            int u = q.poll();
            topoOrder[topoPtr++] = u;
            for (Edge e : adj[u]) {
                if (--inDegree[e.to] == 0) q.add(e.to);
            }
        }

        Arrays.sort(allCosts);
        int uniqueCount = 0;
        if (edgeCount > 0) {
            uniqueCount = 1;
            for (int i = 1; i < edgeCount; i++) {
                if (allCosts[i] != allCosts[i - 1]) uniqueCount++;
            }
        }
        int[] uniqueCosts = new int[uniqueCount];
        if (uniqueCount > 0) {
            uniqueCosts[0] = allCosts[0];
            int idx = 1;
            for (int i = 1; i < edgeCount; i++) {
                if (allCosts[i] != allCosts[i - 1]) uniqueCosts[idx++] = allCosts[i];
            }
        }

        int low = 0, high = uniqueCount - 1, ans = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (isValid(uniqueCosts[mid], adj, topoOrder, topoPtr, n, k)) {
                ans = uniqueCosts[mid];
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }

    private boolean isValid(int minCost, ArrayList<Edge>[] adj, int[] topoOrder, int topoSize, int n, long k) {
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE / 2);
        dist[0] = 0;
        for (int i = 0; i < topoSize; i++) {
            int u = topoOrder[i];
            if (dist[u] > k) continue;
            for (Edge e : adj[u]) {
                if (e.cost >= minCost) {
                    if (dist[u] + e.cost < dist[e.to]) {
                        dist[e.to] = dist[u] + e.cost;
                    }
                }
            }
        }
        return dist[n - 1] <= k;
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
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        unique_costs_set = set()

        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                in_degree[v] += 1
                unique_costs_set.add(cost)

        topo_order = []
        queue = collections.deque([i for i in range(n) if online[i] and in_degree[i] == 0])
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v, cost in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        sorted_costs = sorted(list(unique_costs_set))

        def check(min_val):
            dist = [float('inf')] * n
            dist[0] = 0
            for u in topo_order:
                d_u = dist[u]
                if d_u > k:
                    continue
                for v, c in adj[u]:
                    if c >= min_val:
                        new_dist = d_u + c
                        if new_dist < dist[v]:
                            dist[v] = new_dist
            return dist[n - 1] <= k

        low, high = 0, len(sorted_costs) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if check(sorted_costs[mid]):
                ans = sorted_costs[mid]
                low = mid + 1
            else:
                high = mid - 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List
import collections

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        in_degree = [0] * n

        for u, v, c in edges:
            if online[u] and online[v]:
                adj[u].append((v, c))
                in_degree[v] += 1

        topo_order = []
        queue = collections.deque([i for i in range(n) if online[i] and in_degree[i] == 0])
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v, c in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        unique_costs = sorted(list(set(e[2] for e in edges)))

        def check(min_val):
            dist = [float('inf')] * n
            dist[0] = 0
            for u in topo_order:
                d_u = dist[u]
                if d_u > k:
                    continue
                for v, c in adj[u]:
                    if c >= min_val:
                        new_dist = d_u + c
                        if dist[v] > new_dist:
                            dist[v] = new_dist
            return dist[n-1] <= k

        ans = -1
        low, high = 0, len(unique_costs) - 1
        while low <= high:
            mid = (low + high) // 2
            if check(unique_costs[mid]):
                ans = unique_costs[mid]
                low = mid + 1
            else:
                high = mid - 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

typedef struct {
    int to;
    int cost;
    int next;
} EdgePool;

int compare_ints(const void* a, const void* b) {
    int x = *(const int*)a;
    int y = *(const int*)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

int findMaxPathScore(int** edges, int edgesSize, int* edgesColSize, bool* online, int onlineSize, long long k) {
    int n = onlineSize;
    int m = edgesSize;
    if (m == 0) return -1;

    int* head = malloc(n * sizeof(int));
    memset(head, -1, n * sizeof(int));
    EdgePool* pool = malloc(m * sizeof(EdgePool));
    int* in_degree = calloc(n, sizeof(int));
    int edge_count = 0;

    for (int i = 0; i < m; i++) {
        int u = edges[i][0];
        int v = edges[i][1];
        int c = edges[i][2];
        if (online[u] && online[v]) {
            pool[edge_count].to = v;
            pool[edge_count].cost = c;
            pool[edge_count].next = head[u];
            head[u] = edge_count++;
            in_degree[v]++;
        }
    }

    int* topo_order = malloc(n * sizeof(int));
    int topo_size = 0;
    int* queue = malloc(n * sizeof(int));
    int q_head = 0, q_tail = 0;
    for (int i = 0; i < n; i++) {
        if (online[i] && in_degree[i] == 0) queue[q_tail++] = i;
    }

    while (q_head < q_tail) {
        int u = queue[q_head++];
        topo_order[topo_size++] = u;
        for (int i = head[u]; i != -1; i = pool[i].next) {
            int v = pool[i].to;
            if (--in_degree[v] == 0) queue[q_tail++] = v;
        }
    }

    int* costs = malloc(m * sizeof(int));
    for (int i = 0; i < m; i++) costs[i] = edges[i][2];
    qsort(costs, m, sizeof(int), compare_ints);
    int m_unique = 0;
    if (m > 0) {
        m_unique = 1;
        for (int i = 1; i < m; i++) {
            if (costs[i] != costs[i - 1]) costs[m_unique++] = costs[i];
        }
    }

    long long* dist = malloc(n * sizeof(long long));
    long long INF = 200000000000000LL;

    int ans = -1;
    int low = 0, high = m_unique - 1;
    while (low <= high) {
        int mid_idx = low + (high - low) / 2;
        int min_val = costs[mid_idx];

        for (int i = 0; i < n; i++) dist[i] = INF;
        dist[0] = 0;

        for (int i = 0; i < topo_size; i++) {
            int u = topo_order[i];
            if (dist[u] > k) continue;
            for (int j = head[u]; j != -1; j = pool[j].next) {
                if (pool[j].cost >= min_val) {
                    int v = pool[j].to;
                    if (dist[v] > dist[u] + pool[j].cost) {
                        dist[v] = dist[u] + pool[j].cost;
                    }
                }
            }
        }

        if (dist[n - 1] <= k) {
            ans = min_val;
            low = mid_idx + 1;
        } else {
            high = mid_idx - 1;
        }
    }

    free(head); free(pool); free(in_degree); free(topo_order); free(queue); free(costs); free(dist);
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
using System.Linq;

public class Solution {
    public int FindMaxPathScore(int[][] edges, bool[] online, long k) {
        int n = online.Length;
        int m = edges.Length;
        if (m == 0) return -1;

        int[] head = new int[n];
        Array.Fill(head, -1);
        int[] next = new int[m];
        int[] to = new int[m];
        int[] edgeCost = new int[m];
        int[] inDegree = new int[n];
        int edgeCount = 0;

        for (int i = 0; i < m; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            int c = edges[i][2];
            if (online[u] && online[v]) {
                to[edgeCount] = v;
                edgeCost[edgeCount] = c;
                next[edgeCount] = head[u];
                head[u] = edgeCount++;
                inDegree[v]++;
            }
        }

        int[] topoOrder = new int[n];
        int topoSize = 0;
        int[] q = new int[n];
        int qHead = 0, qTail = 0;
        for (int i = 0; i < n; i++) {
            if (online[i] && inDegree[i] == 0) q[qTail++] = i;
        }

        while (qHead < qTail) {
            int u = q[qHead++];
            topoOrder[topoSize++] = u;
            for (int i = head[u]; i != -1; i = next[i]) {
                int v = to[i];
                if (--inDegree[v] == 0) q[qTail++] = v;
            }
        }

        int[] uniqueCosts = edges.Select(e => e[2]).Distinct().ToArray();
        Array.Sort(uniqueCosts);

        long[] dist = new long[n];
        int ans = -1;
        int low = 0, high = uniqueCosts.Length - 1;
        while (low <= high) {
            int midIdx = low + (high - low) / 2;
            int minVal = uniqueCosts[midIdx];

            for (int i = 0; i < n; i++) dist[i] = 100000000000000L; // 1e14
            dist[0] = 0;

            for (int i = 0; i < topoSize; i++) {
                int u = topoOrder[i];
                if (dist[u] > k) continue;
                for (int j = head[u]; j != -1; j = next[j]) {
                    if (edgeCost[j] >= minVal) {
                        int v = to[j];
                        if (dist[v] > dist[u] + edgeCost[j]) {
                            dist[v] = dist[u] + (long)edgeCost[j];
                        }
                    }
                }
            }

            if (dist[n - 1] <= k) {
                ans = minVal;
                low = midIdx + 1;
            } else {
                high = midIdx - 1;
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
 * @param {number[][]} edges
 * @param {boolean[]} online
 * @param {number} k
 * @return {number}
 */
var findMaxPathScore = function(edges, online, k) {
    const n = online.length;
    const m = edges.length;
    if (m === 0) return -1;

    const head = new Int32Array(n).fill(-1);
    const next = new Int32Array(m);
    const to = new Int32Array(m);
    const edgeCost = new Int32Array(m);
    const inDegree = new Int32Array(n).fill(0);
    let edgeCount = 0;

    for (let i = 0; i < m; i++) {
        const u = edges[i][0];
        const v = edges[i][1];
        const c = edges[i][2];
        if (online[u] && online[v]) {
            to[edgeCount] = v;
            edgeCost[edgeCount] = c;
            next[edgeCount] = head[u];
            head[u] = edgeCount++;
            inDegree[v]++;
        }
    }

    const topoOrder = [];
    const q = [];
    for (let i = 0; i < n; i++) {
        if (online[i] && inDegree[i] === 0) q.push(i);
    }

    let qIdx = 0;
    while (qIdx < q.length) {
        const u = q[qIdx++];
        topoOrder.push(u);
        for (let i = head[u]; i !== -1; i = next[i]) {
            const v = to[i];
            if (--inDegree[v] === 0) q.push(v);
        }
    }

    const uniqueCosts = Array.from(new Set(edges.map(e => e[2]))).sort((a, b) => a - b);
    const dist = new Float64Array(n);

    function check(minVal) {
        dist.fill(1e15);
        dist[0] = 0;
        for (let i = 0; i < topoOrder.length; i++) {
            const u = topoOrder[i];
            if (dist[u] > k) continue;
            for (let j = head[u]; j !== -1; j = next[j]) {
                if (edgeCost[j] >= minVal) {
                    const v = to[j];
                    if (dist[v] > dist[u] + edgeCost[j]) {
                        dist[v] = dist[u] + edgeCost[j];
                    }
                }
            }
        }
        return dist[n - 1] <= k;
    }

    let ans = -1;
    let low = 0, high = uniqueCosts.length - 1;
    while (low <= high) {
        const midIdx = Math.floor((low + high) / 2);
        if (check(uniqueCosts[midIdx])) {
            ans = uniqueCosts[midIdx];
            low = midIdx + 1;
        } else {
            high = midIdx - 1;
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
function findMaxPathScore(edges: number[][], online: boolean[], k: number): number {
    const n = online.length;
    const adj: [number, number][][] = Array.from({ length: n }, () => []);
    const inDegree = new Int32Array(n).fill(0);
    for (const [u, v, cost] of edges) {
        adj[u].push([v, cost]);
        inDegree[v]++;
    }

    const queue = new Int32Array(n);
    let head = 0, tail = 0;
    for (let i = 0; i < n; i++) {
        if (inDegree[i] === 0) queue[tail++] = i;
    }

    const topoOrder = new Int32Array(n);
    let topoIdx = 0;
    while (head < tail) {
        const u = queue[head++];
        topoOrder[topoIdx++] = u;
        const neighbors = adj[u];
        for (let i = 0; i < neighbors.length; i++) {
            const v = neighbors[i][0];
            if (--inDegree[v] === 0) queue[tail++] = v;
        }
    }

    const uniqueWeights = Array.from(new Set(edges.map(e => e[2]))).sort((a, b) => a - b);

    const check = (threshold: number): boolean => {
        const dist = new Float64Array(n).fill(Infinity);
        dist[0] = 0;
        for (let i = 0; i < n; i++) {
            const u = topoOrder[i];
            if (dist[u] === Infinity || dist[u] > k) continue;
            const neighbors = adj[u];
            for (let j = 0; j < neighbors.length; j++) {
                const [v, cost] = neighbors[j];
                if (online[v] && cost >= threshold) {
                    const newDist = dist[u] + cost;
                    if (newDist < dist[v]) {
                        dist[v] = newDist;
                    }
                }
            }
        }
        return dist[n - 1] <= k;
    };

    let low = 0, high = uniqueWeights.length - 1, ans = -1;
    while (low <= high) {
        const mid = (low + high) >> 1;
        if (check(uniqueWeights[mid])) {
            ans = uniqueWeights[mid];
            low = mid + 1;
        } else {
            high = mid - 1;
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
     * @param Integer[][] $edges
     * @param Boolean[] $online
     * @param Integer $k
     * @return Integer
     */
    function findMaxPathScore($edges, $online, $k) {
        $n = count($online);
        $adj = array_fill(0, $n, []);
        $inDegree = array_fill(0, $n, 0);
        foreach ($edges as $e) {
            $u = $e[0]; $v = $e[1]; $cost = $e[2];
            $adj[$u][] = [$v, $cost];
            $inDegree[$v]++;
        }

        $queue = new SplQueue();
        for ($i = 0; $i < $n; $i++) {
            if ($inDegree[$i] === 0) $queue->enqueue($i);
        }

        $topoOrder = [];
        while (!$queue->isEmpty()) {
            $u = $queue->dequeue();
            $topoOrder[] = $u;
            foreach ($adj[$u] as $neighbor) {
                $v = $neighbor[0];
                $inDegree[$v]--;
                if ($inDegree[$v] === 0) $queue->enqueue($v);
            }
        }

        $weights = [];
        foreach ($edges as $e) {
            $weights[] = $e[2];
        }
        $weights = array_values(array_unique($weights));
        sort($weights);

        $ans = -1;
        $low = 0;
        $high = count($weights) - 1;
        while ($low <= $high) {
            $mid = (int)(($low + $high) / 2);
            $threshold = $weights[$mid];
            if ($this->check($threshold, $n, $adj, $online, $k, $topoOrder)) {
                $ans = $threshold;
                $low = $mid + 1;
            } else {
                $high = $mid - 1;
            }
        }
        return $ans;
    }

    private function check($threshold, $n, $adj, $online, $k, $topoOrder) {
        $dist = array_fill(0, $n, INF);
        $dist[0] = 0.0;
        foreach ($topoOrder as $u) {
            if ($dist[$u] === INF || $dist[$u] > $k) continue;
            foreach ($adj[$u] as $neighbor) {
                $v = $neighbor[0];
                $cost = $neighbor[1];
                if ($online[$v] && $cost >= $threshold) {
                    $newDist = $dist[$u] + $cost;
                    if ($newDist < $dist[$v]) {
                        $dist[$v] = $newDist;
                    }
                }
            }
        }
        return $dist[$n - 1] <= $k;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func findMaxPathScore(_ edges: [[Int]], _ online: [Bool], _ k: Int) -> Int {
        let n = online.count
        var adj = Array(repeating: [(Int, Int)](), count: n)
        var inDegree = [Int](repeating: 0, count: n)
        for edge in edges {
            let u = edge[0]
            let v = edge[1]
            let cost = edge[2]
            adj[u].append((v, cost))
            inDegree[v] += 1
        }

        var queue = [Int]()
        for i in 0..<n {
            if inDegree[i] == 0 {
                queue.append(i)
            }
        }

        var head = 0
        var topoOrder = [Int]()
        while head < queue.count {
            let u = queue[head]
            head += 1
            topoOrder.append(u)
            for (v, _) in adj[u] {
                inDegree[v] -= 1
                if inDegree[v] == 0 {
                    queue.append(v)
                }
            }
        }

        var uniqueWeightsSet = Set<Int>()
        for edge in edges { uniqueWeightsSet.insert(edge[2]) }
        let uniqueWeights = uniqueWeightsSet.sorted()

        func check(_ threshold: Int) -> Bool {
            let INF = Int.max / 2
            var dist = [Int](repeating: INF, count: n)
            dist[0] = 0
            for u in topoOrder {
                if dist[u] >= INF || dist[u] > k { continue }
                for (v, cost) in adj[u] {
                    if online[v] && cost >= threshold {
                        let newDist = dist[u] + cost
                        if newDist < dist[v] {
                            dist[v] = newDist
                        }
                    }
                }
            }
            return dist[n - 1] <= k
        }

        var low = 0
        var high = uniqueWeights.count - 1
        var ans = -1
        while low <= high {
            let mid = (low + high) / 2
            if check(uniqueWeights[mid]) {
                ans = uniqueWeights[mid]
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

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.*

class Solution {
    fun findMaxPathScore(edges: Array<IntArray>, online: BooleanArray, k: Long): Int {
        val n = online.size
        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }
        val inDegree = IntArray(n)
        for (edge in edges) {
            val u = edge[0]
            val v = edge[1]
            val cost = edge[2]
            adj[u].add(v to cost)
            inDegree[v]++
        }

        val queue: Queue<Int> = LinkedList()
        for (i in 0 until n) {
            if (inDegree[i] == 0) {
                queue.add(i)
            }
        }

        val topoOrder = IntArray(n)
        var idx = 0
        while (queue.isNotEmpty()) {
            val u = queue.poll()
            topoOrder[idx++] = u
            for (neighbor in adj[u]) {
                val v = neighbor.first
                inDegree[v]--
                if (inDegree[v] == 0) {
                    queue.add(v)
                }
            }
        }

        val weights = edges.map { it[2] }.distinct().sorted()
        if (weights.isEmpty()) return -1

        fun check(threshold: Int): Boolean {
            val INF = Long.MAX_VALUE / 2
            val dist = LongArray(n) { INF }
            dist[0] = 0L
            for (u in topoOrder) {
                if (dist[u] >= INF || dist[u] > k) continue
                for (neighbor in adj[u]) {
                    val v = neighbor.first
                    val cost = neighbor.second
                    if (online[v] && cost >= threshold) {
                        val newDist = dist[u] + cost.toLong()
                        if (newDist < dist[v]) {
                            dist[v] = newDist
                        }
                    }
                }
            }
            return dist[n - 1] <= k
        }

        var low = 0
        var high = weights.size - 1
        var ans = -1
        while (low <= high) {
            val mid = low + (high - low) / 2
            if (check(weights[mid])) {
                ans = weights[mid]
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
class Solution {
  int findMaxPathScore(List<List<int>> edges, List<bool> online, int k) {
    int n = online.length;
    List<List<_Edge>> adj = List.generate(n, (_) => []);
    List<int> inDegree = List.filled(n, 0);

    for (var edge in edges) {
      int u = edge[0];
      int v = edge[1];
      int cost = edge[2];
      adj[u].add(_Edge(v, cost));
      inDegree[v]++;
    }

    List<int> queue = [];
    for (int i = 0; i < n; i++) {
      if (inDegree[i] == 0) {
        queue.add(i);
      }
    }

    List<int> topoOrder = [];
    int head = 0;
    while (head < queue.length) {
      int u = queue[head++];
      topoOrder.add(u);
      for (var edge in adj[u]) {
        inDegree[edge.to]--;
        if (inDegree[edge.to] == 0) {
          queue.add(edge.to);
        }
      }
    }

    List<int> uniqueCosts = edges.map((e) => e[2]).toSet().toList();
    uniqueCosts.sort();

    bool check(int threshold) {
      List<int> dist = List.filled(n, 1000000000000000);
      dist[0] = 0;
      for (int i = 0; i < topoOrder.length; i++) {
        int u = topoOrder[i];
        if (!online[u] || dist[u] > k) continue;
        for (var edge in adj[u]) {
          if (online[edge.to] && edge.cost >= threshold) {
            if (dist[u] + edge.cost < dist[edge.to]) {
              dist[edge.to] = dist[u] + edge.cost;
            }
          }
        }
      }
      return dist[n - 1] <= k;
    }

    int ans = -1;
    int low = 0;
    int high = uniqueCosts.length - 1;
    while (low <= high) {
      int mid = low + (high - low) ~/ 2;
      if (check(uniqueCosts[mid])) {
        ans = uniqueCosts[mid];
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return ans;
  }
}

class _Edge {
  final int to;
  final int cost;
  _Edge(this.to, this.cost);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
	"sort"
)

func findMaxPathScore(edges [][]int, online []bool, k int64) int {
	type edge struct {
		to   int
		cost int
	}

	n := len(online)
	adj := make([][]edge, n)
	inDegree := make([]int, n)
	for _, e := range edges {
		u, v, cost := e[0], e[1], e[2]
		adj[u] = append(adj[u], edge{v, cost})
		inDegree[v]++
	}

	queue := make([]int, 0, n)
	for i := 0; i < n; i++ {
		if inDegree[i] == 0 {
			queue = append(queue, i)
		}
	}

	topoOrder := make([]int, 0, n)
	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]
		topoOrder = append(topoOrder, u)
		for _, e := range adj[u] {
			inDegree[e.to]--
			if inDegree[e.to] == 0 {
				queue = append(queue, e.to)
			}
		}
	}

	costMap := make(map[int]bool)
	for _, e := range edges {
		costMap[e[2]] = true
	}
	uniqueCosts := make([]int, 0, len(costMap))
	for c := range costMap {
		uniqueCosts = append(uniqueCosts, c)
	}
	sort.Ints(uniqueCosts)

	check := func(threshold int) bool {
		dist := make([]int64, n)
		for i := range dist {
			dist[i] = 1000000000000000
		}
		dist[0] = 0

		for _, u := range topoOrder {
			if !online[u] || dist[u] > k {
				continue
			}
			for _, e := range adj[u] {
				if online[e.to] && e.cost >= threshold {
					if dist[u]+int64(e.cost) < dist[e.to] {
						dist[e.to] = dist[u] + int64(e.cost)
					}
				}
			}
		}
		return dist[n-1] <= k
	}

	ans := -1
	low, high := 0, len(uniqueCosts)-1
	for low <= high {
		mid := (low + high) / 2
		if check(uniqueCosts[mid]) {
			ans = uniqueCosts[mid]
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
def find_max_path_score(edges, online, k)
  n = online.length
  adj = Array.new(n) { [] }
  in_degree = Array.new(n, 0)

  edges.each do |e|
    u, v, cost = e[0], e[1], e[2]
    adj[u] << [v, cost]
    in_degree[v] += 1
  end

  queue = []
  n.times { |i| queue << i if in_degree[i] == 0 }

  topo_order = []
  head = 0
  while head < queue.length
    u = queue[head]
    head += 1
    topo_order << u
    adj[u].each do |v, cost|
      in_degree[v] -= 1
      queue << v if in_degree[v] == 0
    end
  end

  unique_costs = edges.map { |e| e[2] }.uniq.sort

  check = lambda do |threshold|
    dist = Array.new(n, 1000000000000000)
    dist[0] = 0
    topo_order.each do |u|
      next if !online[u] || dist[u] > k
      adj[u].each do |v, cost|
        if online[v] && cost >= threshold
          if dist[u] + cost < dist[v]
            dist[v] = dist[u] + cost
          end
        end
      end
    end
    dist[n - 1] <= k
  end

  ans = -1
  low = 0
  high = unique_costs.length - 1
  while low <= high
    mid = (low + high) / 2
    if check.call(unique_costs[mid])
      ans = unique_costs[mid]
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
    case class Edge(to: Int, cost: Int)

    def findMaxPathScore(edges: Array[Array[Int]], online: Array[Boolean], k: Long): Int = {
        val n = online.length
        val adj = Array.tabulate(n)(_ => mutable.ArrayBuffer.empty[Edge])
        val inDegree = new Array[Int](n)

        for (edge <- edges) {
            val u = edge(0)
            val v = edge(1)
            val cost = edge(2)
            adj(u) += Edge(v, cost)
            inDegree(v) += 1
        }

        val queue = mutable.Queue[Int]()
        for (i <- 0 until n) if (inDegree(i) == 0) queue.enqueue(i)

        val topoOrder = new Array[Int](n)
        var topoIdx = 0
        while (queue.nonEmpty) {
            val u = queue.dequeue()
            topoOrder(topoIdx) = u
            topoIdx += 1
            for (e <- adj(u)) {
                inDegree(e.to) -= 1
                if (inDegree(e.to) == 0) queue.enqueue(e.to)
            }
        }

        val uniqueCosts = edges.map(_(2)).distinct.sorted

        def check(threshold: Int): Boolean = {
            val dist = Array.fill(n)(1000000000000000L)
            dist(0) = 0L
            var i = 0
            while (i < n) {
                val u = topoOrder(i)
                if (online(u) && dist(u) <= k) {
                    val neighbors = adj(u)
                    var j = 0
                    while (j < neighbors.length) {
                        val e = neighbors(j)
                        if (online(e.to) && e.cost >= threshold) {
                            val newDist = dist(u) + e.cost
                            if (newDist < dist(e.to)) {
                                dist(e.to) = newDist
                            }
                        }
                        j += 1
                    }
                }
                i += 1
            }
            dist(n - 1) <= k
        }

        var ans = -1
        var low = 0
        var high = uniqueCosts.length - 1
        while (low <= high) {
            val mid = (low + high) / 2
            if (check(uniqueCosts(mid))) {
                ans = uniqueCosts(mid)
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
use std::collections::VecDeque;

impl Solution {
    pub fn find_max_path_score(edges: Vec<Vec<i32>>, online: Vec<bool>, k: i64) -> i32 {
        let n = online.len();
        let mut adj = vec![vec![]; n];
        let mut in_degree = vec![0; n];

        for edge in &edges {
            let u = edge[0] as usize;
            let v = edge[1] as usize;
            let cost = edge[2];
            if online[u] && online[v] {
                adj[u].push((v, cost));
                in_degree[v] += 1;
            }
        }

        let mut topo_order = Vec::with_capacity(n);
        let mut queue = VecDeque::new();
        for i in 0..n {
            if online[i] && in_degree[i] == 0 {
                queue.push_back(i);
            }
        }

        while let Some(u) = queue.pop_front() {
            topo_order.push(u);
            for &(v, _) in &adj[u] {
                in_degree[v] -= 1;
                if in_degree[v] == 0 {
                    queue.push_back(v);
                }
            }
        }

        let mut unique_costs: Vec<i32> = edges
            .iter()
            .filter(|e| online[e[0] as usize] && online[e[1] as usize])
            .map(|e| e[2])
            .collect();
        unique_costs.sort_unstable();
        unique_costs.dedup();

        let mut low = 0;
        let mut high = (unique_costs.len() as i32) - 1;
        let mut ans = -1;

        while low <= high {
            let mid = low + (high - low) / 2;
            let threshold = unique_costs[mid as usize];
            if Self::check(threshold, &topo_order, &adj, n, k) {
                ans = threshold;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        ans
    }

    fn check(threshold: i32, topo_order: &[usize], adj: &[Vec<(usize, i32)>], n: usize, k: i64) -> bool {
        let mut dist = vec![i64::MAX; n];
        dist[0] = 0;
        for &u in topo_order {
            if dist[u] == i64::MAX {
                continue;
            }
            for &(v, cost) in &adj[u] {
                if cost >= threshold {
                    let new_dist = dist[u] + cost as i64;
                    if new_dist <= k && new_dist < dist[v] {
                        dist[v] = new_dist;
                    }
                }
            }
        }
        dist[n - 1] <= k
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(require racket/list)

(define/contract (find-max-path-score edges online k)
  (-> (listof (listof exact-integer?)) (listof boolean?) exact-integer? exact-integer?)
  (let* ([n (length online)]
         [online-vec (list->vector online)]
         [adj (make-vector n '())]
         [in-degree (make-vector n 0)])
    (for ([edge edges])
      (let ([u (first edge)]
            [v (second edge)]
            [cost (third edge)])
        (when (and (vector-ref online-vec u) (vector-ref online-vec v))
          (vector-set! adj u (cons (cons v cost) (vector-ref adj u)))
          (vector-set! in-degree v (+ (vector-ref in-degree v) 1)))))

    (let ([topo-order '()]
          [queue '()])
      (for ([i (in-range n)])
        (when (and (vector-ref online-vec i) (= (vector-ref in-degree i) 0))
          (set! queue (cons i queue))))
      (let loop ([q queue])
        (unless (null? q)
          (let* ([u (car q)]
                 [next-q (cdr q)])
            (set! topo-order (cons u topo-order))
            (let ([current-next-q next-q])
              (for ([edge (vector-ref adj u)])
                (let ([v (car edge)])
                  (vector-set! in-degree v (- (vector-ref in-degree v) 1))
                  (when (= (vector-ref in-degree v) 0)
                    (set! current-next-q (cons v current-next-q)))))
              (loop current-next-q)))))
      (set! topo-order (reverse topo-order))

      (let* ([valid-costs (filter-map (lambda (e)
                                        (if (and (vector-ref online-vec (first e))
                                                 (vector-ref online-vec (second e)))
                                            (third e)
                                            #f))
                                      edges)]
             [unique-costs (list->vector (sort (remove-duplicates valid-costs) <))])
        (define (check threshold)
          (let ([dist (make-vector n -1)])
            (vector-set! dist 0 0)
            (for ([u topo-order])
              (let ([du (vector-ref dist u)])
                (unless (= du -1)
                  (for ([edge (vector-ref adj u)])
                    (let ([v (car edge)]
                          [cost (cdr edge)])
                      (when (>= cost threshold)
                        (let ([new-dist (+ du cost)])
                          (when (<= new-dist k)
                            (let ([dv (vector-ref dist v)])
                              (when (or (= dv -1) (< new-dist dv))
                                (vector-set! dist v new-dist)))))))))))
            (let ([final (vector-ref dist (- n 1))])
              (and (not (= final -1)) (<= final k)))))

        (let bsearch ([low 0] [high (- (vector-length unique-costs) 1)] [ans -1])
          (if (> low high)
              ans
              (let* ([mid (quotient (+ low high) 2)]
                     [threshold (vector-ref unique-costs mid)])
                (if (check threshold)
                    (bsearch (+ mid 1) high threshold)
                    (bsearch low (- mid 1) ans)))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec find_max_path_score(Edges :: [[integer()]], Online :: [boolean()], K :: integer()) -> integer().
find_max_path_score(Edges, Online, K) ->
    OnlineVec = list_to_tuple(Online),
    N = tuple_size(OnlineVec),
    ValidEdges = [ {U, V, C} || [U, V, C] <- Edges, 
                                element(U + 1, OnlineVec), 
                                element(V + 1, OnlineVec) ],
    InDegree = lists:foldl(fun({_U, V, _C}, Acc) ->
        Acc#{V => maps:get(V, Acc, 0) + 1}
    end, #{}, ValidEdges),
    Adj = lists:foldl(fun({U, V, C}, Acc) ->
        Acc#{U => [{V, C} | maps:get(U, Acc, [])]}
    end, #{}, ValidEdges),
    InAdj = lists:foldl(fun({U, V, C}, Acc) ->
        Acc#{V => [{U, C} | maps:get(V, Acc, [])]}
    end, #{}, ValidEdges),

    InitialQueue = [I || I <- lists:seq(0, N-1), 
                         element(I + 1, OnlineVec), 
                         maps:get(I, InDegree, 0) == 0],

    TopoSort = fun TS([], _Degs, Acc) -> lists:reverse(Acc);
                   TS([U | Rest], Degs, Acc) ->
                       Neighbors = maps:get(U, Adj, []),
                       {NewQueue, NewDegs} = lists:foldl(fun({V, _C}, {Q, D}) ->
                           DV = maps:get(V, D) - 1,
                           if DV == 0 -> {[V | Q], D#{V => DV}}; true -> {Q, D#{V => DV}} end
                       end, {Rest, Degs}, Neighbors),
                       TS(NewQueue, NewDegs, [U | Acc])
               end,
    TopoOrder = TopoSort(InitialQueue, InDegree, []),

    UniqueCosts = lists:usort([C || {_, _, C} <- ValidEdges]),
    UniqueCostsTuple = list_to_tuple(UniqueCosts),

    Check = fun(Threshold) ->
        FinalDistMap = lists:foldl(fun(V, Acc) ->
            if V == 0 -> Acc#{0 => 0};
               true ->
                   Predecessors = maps:get(V, InAdj, []),
                   MinV = lists:foldl(fun({U, C}, CurrentMin) ->
                       if C >= Threshold ->
                            case maps:find(U, Acc) of
                                {ok, DU} ->
                                    NewD = DU + C,
                                    if NewD =< K andalso (CurrentMin == infinity orelse NewD < CurrentMin) -> NewD;
                                       true -> CurrentMin
                                    end;
                                error -> CurrentMin
                            end;
                          true -> CurrentMin
                       end
                   end, infinity, Predecessors),
                   if MinV == infinity -> Acc; true -> Acc#{V => MinV} end
            end
        end, #{}, TopoOrder),
        case maps:find(N - 1, FinalDistMap) of
            {ok, Dist} -> Dist =< K;
            error -> false
        end
    end,

    BS = fun BS_inner(Low, High, Best) ->
        if Low > High -> Best;
           true ->
               Mid = (Low + High) div 2,
               Threshold = element(Mid + 1, UniqueCostsTuple),
               case Check(Threshold) of
                   true -> BS_inner(Mid + 1, High, Threshold);
                   false -> BS_inner(Low, Mid - 1, Best)
               end
        end
    end,
    BS(0, tuple_size(UniqueCostsTuple) - 1, -1).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec find_max_path_score(edges :: [[integer]], online :: [boolean], k :: integer) :: integer
  def find_max_path_score(edges, online, k) do
    n = length(online)
    online_tuple = List.to_tuple(online)

    valid_edges = for [u, v, c] <- edges, elem(online_tuple, u) and elem(online_tuple, v), do: {u, v, c}

    in_degree_map = Enum.reduce(valid_edges, %{}, fn {_, v, _}, acc ->
      Map.update(acc, v, 1, &(&1 + 1))
    end)

    adj_map = Enum.reduce(valid_edges, %{}, fn {u, v, c}, acc ->
      Map.update(acc, u, [{v, c}], &([{v, c} | &1]))
    end)

    in_adj_map = Enum.reduce(valid_edges, %{}, fn {u, v, c}, acc ->
      Map.update(acc, v, [{u, c}], &([{u, c} | &1]))
    end)

    initial_queue = Enum.filter(0..(n - 1), fn i ->
      elem(online_tuple, i) and Map.get(in_degree_map, i, 0) == 0
    end)

    topo_order = do_topo_sort(initial_queue, in_degree_map, adj_map, [])

    unique_costs = valid_edges |> Enum.map(fn {_, _, c} -> c end) |> Enum.sort() |> Enum.uniq() |> List.to_tuple()

    binary_search(0, tuple_size(unique_costs) - 1, unique_costs, topo_order, in_adj_map, k, n, -1)
  end

  defp do_topo_sort([], _degs, _adj, acc), do: Enum.reverse(acc)
  defp do_topo_sort([u | rest], degs, adj, acc) do
    {new_queue, new_degs} = Enum.reduce(Map.get(adj, u, []), {rest, degs}, fn {v, _}, {q, d} ->
      dv = Map.get(d, v) - 1
      if dv == 0, do: {[v | q], Map.put(d, v, dv)}, else: {q, Map.put(d, v, dv)}
    end)
    do_topo_sort(new_queue, new_degs, adj, [u | acc])
  end

  defp check(threshold, topo_order, in_adj, k, n) do
    dist_map = Enum.reduce(topo_order, %{}, fn v, acc ->
      cond do
        v == 0 -> Map.put(acc, 0, 0)
        true ->
          min_val = Enum.reduce(Map.get(in_adj, v, []), :infinity, fn {u, cost}, current_min ->
            if cost >= threshold do
              case Map.get(acc, u, :infinity) do
                :infinity -> current_min
                du ->
                  new_dist = du + cost
                  if new_dist <= k and (current_min == :infinity or new_dist < current_min), do: new_dist, else: current_min
              end
            else
              current_min
            end
          end)
          if min_val != :infinity, do: Map.put(acc, v, min_val), else: acc
      end
    end)
    Map.get(dist_map, n - 1, :infinity) != :infinity
  end

  defp binary_search(low, high, unique_costs, topo_order, in_adj, k, n, best) do
    if low > high do
      best
    else
      mid = div(low + high, 2)
      threshold = elem(unique_costs, mid)
      if check(threshold, topo_order, in_adj, k, n) do
        binary_search(mid + 1, high, unique_costs, topo_order, in_adj, k, n, threshold)
      else
        binary_search(low, mid - 1, unique_costs, topo_order, in_adj, k, n, best)
      end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O((N + M) \log M) where $N$ is the number of nodes and $M$ is the number of edges. Topological sorting takes $O(N + M)$, and the binary search runs for $O(\log M)$ iterations, with each iteration performing a DP traversal over the graph in $O(N + M)$ time.
- **Space Complexity:** O(N + M) to store the adjacency list of the graph, the topological order, and the DP array for shortest path distances.
