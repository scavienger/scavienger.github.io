---
layout: post
title: "Number of Ways to Assign Edge Weights II"
date: 2026-06-12 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Math", "Dynamic Programming", "Bit Manipulation", "Tree", "Depth-First Search"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> assignEdgeWeights(vector<vector<int>>&\
        \ edges, vector<vector<int>>& queries) {\n        int n = edges.size() + 1;\n\
        \        vector<vector<int>> adj(n + 1);\n        for (const auto& edge : edges)\
        \ {\n            adj[edge[0]].push_back(edge[1]);\n            adj[edge[1]].push_back(edge[0]);\n\
        \        }\n\n        int LOG = 18;\n        vector<vector<int>> up(n + 1, vector<int>(LOG,\
        \ 0));\n        vector<int> depth(n + 1, 0);\n        vector<int> q;\n     \
        \   q.push_back(1);\n        vector<bool> visited(n + 1, false);\n        visited[1]\
        \ = true;\n\n        int head = 0;\n        while (head < q.size()) {\n    \
        \        int u = q[head++];\n            for (int v : adj[u]) {\n          \
        \      if (!visited[v]) {\n                    visited[v] = true;\n        \
        \            depth[v] = depth[u] + 1;\n                    up[v][0] = u;\n \
        \                   q.push_back(v);\n                }\n            }\n    \
        \    }\n\n        for (int i = 1; i < LOG; i++) {\n            for (int u =\
        \ 1; u <= n; u++) {\n                up[u][i] = up[up[u][i - 1]][i - 1];\n \
        \           }\n        }\n\n        auto get_lca = [&](int u, int v) {\n   \
        \         if (depth[u] < depth[v]) swap(u, v);\n            int diff = depth[u]\
        \ - depth[v];\n            for (int i = 0; i < LOG; i++) {\n               \
        \ if ((diff >> i) & 1) u = up[u][i];\n            }\n            if (u == v)\
        \ return u;\n            for (int i = LOG - 1; i >= 0; i--) {\n            \
        \    if (up[u][i] != up[v][i]) {\n                    u = up[u][i];\n      \
        \              v = up[v][i];\n                }\n            }\n           \
        \ return up[u][0];\n        };\n\n        const int MOD = 1000000007;\n    \
        \    vector<int> pow2(n + 1);\n        pow2[0] = 1;\n        for (int i = 1;\
        \ i <= n; i++) {\n            pow2[i] = (int)((pow2[i - 1] * 2LL) % MOD);\n\
        \        }\n\n        vector<int> results;\n        results.reserve(queries.size());\n\
        \        for (const auto& query : queries) {\n            int u = query[0],\
        \ v = query[1];\n            if (u == v) {\n                results.push_back(0);\n\
        \                continue;\n            }\n            int l = get_lca(u, v);\n\
        \            int dist = depth[u] + depth[v] - 2 * depth[l];\n            results.push_back(pow2[dist\
        \ - 1]);\n        }\n        return results;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int[] assignEdgeWeights(int[][]\
        \ edges, int[][] queries) {\n        int n = edges.length + 1;\n        List<Integer>[]\
        \ adj = new ArrayList[n + 1];\n        for (int i = 0; i <= n; i++) adj[i] =\
        \ new ArrayList<>();\n        for (int[] edge : edges) {\n            adj[edge[0]].add(edge[1]);\n\
        \            adj[edge[1]].add(edge[0]);\n        }\n\n        int LOG = 18;\n\
        \        int[][] up = new int[n + 1][LOG];\n        int[] depth = new int[n\
        \ + 1];\n        int[] q = new int[n];\n        boolean[] visited = new boolean[n\
        \ + 1];\n\n        int head = 0, tail = 0;\n        q[tail++] = 1;\n       \
        \ visited[1] = true;\n        while (head < tail) {\n            int u = q[head++];\n\
        \            for (int v : adj[u]) {\n                if (!visited[v]) {\n  \
        \                  visited[v] = true;\n                    depth[v] = depth[u]\
        \ + 1;\n                    up[v][0] = u;\n                    q[tail++] = v;\n\
        \                }\n            }\n        }\n\n        for (int i = 1; i <\
        \ LOG; i++) {\n            for (int u = 1; u <= n; u++) {\n                up[u][i]\
        \ = up[up[u][i - 1]][i - 1];\n            }\n        }\n\n        int MOD =\
        \ 1000000007;\n        int[] pow2 = new int[n + 1];\n        pow2[0] = 1;\n\
        \        for (int i = 1; i <= n; i++) pow2[i] = (int)((pow2[i - 1] * 2L) % MOD);\n\
        \n        int[] results = new int[queries.length];\n        for (int i = 0;\
        \ i < queries.length; i++) {\n            int u = queries[i][0];\n         \
        \   int v = queries[i][1];\n            if (u == v) {\n                results[i]\
        \ = 0;\n                continue;\n            }\n            int l = getLCA(u,\
        \ v, up, depth, LOG);\n            int dist = depth[u] + depth[v] - 2 * depth[l];\n\
        \            results[i] = pow2[dist - 1];\n        }\n        return results;\n\
        \    }\n\n    private int getLCA(int u, int v, int[][] up, int[] depth, int\
        \ LOG) {\n        if (depth[u] < depth[v]) { int tmp = u; u = v; v = tmp; }\n\
        \        int diff = depth[u] - depth[v];\n        for (int i = 0; i < LOG; i++)\
        \ if (((diff >> i) & 1) == 1) u = up[u][i];\n        if (u == v) return u;\n\
        \        for (int i = LOG - 1; i >= 0; i--) {\n            if (up[u][i] != up[v][i])\
        \ {\n                u = up[u][i];\n                v = up[v][i];\n        \
        \    }\n        }\n        return up[u][0];\n    }\n}"
      python: "class Solution(object):\n    def assignEdgeWeights(self, edges, queries):\n\
        \        n = len(edges) + 1\n        adj = [[] for _ in range(n + 1)]\n    \
        \    for u, v in edges:\n            adj[u].append(v)\n            adj[v].append(u)\n\
        \n        LOG = 18\n        up = [[0] * (n + 1) for _ in range(LOG)]\n     \
        \   depth = [0] * (n + 1)\n        stack = [1]\n        visited = [False] *\
        \ (n + 1)\n        visited[1] = True\n        up0 = up[0]\n\n        while stack:\n\
        \            u = stack.pop()\n            du = depth[u]\n            for v in\
        \ adj[u]:\n                if not visited[v]:\n                    visited[v]\
        \ = True\n                    up0[v] = u\n                    depth[v] = du\
        \ + 1\n                    stack.append(v)\n\n        for i in range(1, LOG):\n\
        \            upi = up[i]\n            up_prev = up[i-1]\n            for u in\
        \ range(1, n + 1):\n                upi[u] = up_prev[up_prev[u]]\n\n       \
        \ MOD = 10**9 + 7\n        pow2 = [1] * (n + 1)\n        for i in range(1, n\
        \ + 1):\n            pow2[i] = (pow2[i-1] * 2) % MOD\n\n        ans = []\n \
        \       for u, v in queries:\n            if u == v:\n                ans.append(0)\n\
        \                continue\n            ou, ov = u, v\n            if depth[u]\
        \ < depth[v]:\n                u, v = v, u\n            diff = depth[u] - depth[v]\n\
        \            for i in range(LOG):\n                if (diff >> i) & 1: u = up[i][u]\n\
        \            if u == v:\n                lca = u\n            else:\n      \
        \          for i in range(LOG - 1, -1, -1):\n                    upi = up[i]\n\
        \                    if upi[u] != upi[v]:\n                        u, v = upi[u],\
        \ upi[v]\n                lca = up0[u]\n            dist = depth[ou] + depth[ov]\
        \ - 2 * depth[lca]\n            ans.append(pow2[dist - 1])\n        return ans"
      python3: "import collections\n\nclass Solution:\n    def assignEdgeWeights(self,\
        \ edges: list[list[int]], queries: list[list[int]]) -> list[int]:\n        n\
        \ = len(edges) + 1\n        adj = [[] for _ in range(n + 1)]\n        for u,\
        \ v in edges:\n            adj[u].append(v)\n            adj[v].append(u)\n\n\
        \        LOG = 18\n        depth = [0] * (n + 1)\n        up = [[0] * (n + 1)\
        \ for _ in range(LOG)]\n\n        queue = collections.deque([1])\n        visited\
        \ = [False] * (n + 1)\n        visited[1] = True\n        while queue:\n   \
        \         u = queue.popleft()\n            for v in adj[u]:\n              \
        \  if not visited[v]:\n                    visited[v] = True\n             \
        \       depth[v] = depth[u] + 1\n                    up[0][v] = u\n        \
        \            queue.append(v)\n\n        for j in range(1, LOG):\n          \
        \  up_j = up[j]\n            up_prev = up[j-1]\n            for i in range(1,\
        \ n + 1):\n                up_j[i] = up_prev[up_prev[i]]\n\n        MOD = 1000000007\n\
        \        pow2 = [1] * (n + 1)\n        for i in range(1, n + 1):\n         \
        \   pow2[i] = (pow2[i-1] * 2) % MOD\n\n        res = []\n        for original_u,\
        \ original_v in queries:\n            u, v = original_u, original_v\n      \
        \      if depth[u] < depth[v]:\n                u, v = v, u\n            diff\
        \ = depth[u] - depth[v]\n            for i in range(LOG):\n                if\
        \ (diff >> i) & 1:\n                    u = up[i][u]\n            if u == v:\n\
        \                lca = u\n            else:\n                for i in range(LOG\
        \ - 1, -1, -1):\n                    if up[i][u] != up[i][v]:\n            \
        \            u = up[i][u]\n                        v = up[i][v]\n          \
        \      lca = up[0][u]\n\n            dist = depth[original_u] + depth[original_v]\
        \ - 2 * depth[lca]\n            if dist == 0:\n                res.append(0)\n\
        \            else:\n                res.append(pow2[dist-1])\n        return\
        \ res"
      c: "#include <stdlib.h>\n#include <string.h>\n\nint* assignEdgeWeights(int** edges,\
        \ int edgesSize, int* edgesColSize, int** queries, int queriesSize, int* queriesColSize,\
        \ int* returnSize) {\n    int n = edgesSize + 1;\n    int* head = (int*)malloc(sizeof(int)\
        \ * (n + 1));\n    for (int i = 0; i <= n; i++) head[i] = -1;\n    int* to =\
        \ (int*)malloc(sizeof(int) * (2 * n));\n    int* next = (int*)malloc(sizeof(int)\
        \ * (2 * n));\n    int edgeCount = 0;\n    for (int i = 0; i < edgesSize; i++)\
        \ {\n        int u = edges[i][0];\n        int v = edges[i][1];\n        to[edgeCount]\
        \ = v; next[edgeCount] = head[u]; head[u] = edgeCount++;\n        to[edgeCount]\
        \ = u; next[edgeCount] = head[v]; head[v] = edgeCount++;\n    }\n\n    int*\
        \ depth = (int*)malloc(sizeof(int) * (n + 1));\n    int* up = (int*)calloc(18\
        \ * (n + 1), sizeof(int));\n    int* queue = (int*)malloc(sizeof(int) * (n +\
        \ 1));\n    int head_q = 0, tail_q = 0;\n    int* visited = (int*)calloc(n +\
        \ 1, sizeof(int));\n\n    queue[tail_q++] = 1;\n    visited[1] = 1;\n    depth[1]\
        \ = 0;\n    while (head_q < tail_q) {\n        int u = queue[head_q++];\n  \
        \      for (int i = head[u]; i != -1; i = next[i]) {\n            int v = to[i];\n\
        \            if (!visited[v]) {\n                visited[v] = 1;\n         \
        \       depth[v] = depth[u] + 1;\n                up[0 * (n + 1) + v] = u;\n\
        \                queue[tail_q++] = v;\n            }\n        }\n    }\n\n \
        \   for (int j = 1; j < 18; j++) {\n        for (int i = 1; i <= n; i++) {\n\
        \            int prev = up[(j - 1) * (n + 1) + i];\n            up[j * (n +\
        \ 1) + i] = up[(j - 1) * (n + 1) + prev];\n        }\n    }\n\n    long long*\
        \ pow2 = (long long*)malloc(sizeof(long long) * (n + 1));\n    pow2[0] = 1;\n\
        \    for (int i = 1; i <= n; i++) pow2[i] = (pow2[i - 1] * 2) % 1000000007;\n\
        \n    int* result = (int*)malloc(sizeof(int) * queriesSize);\n    for (int k\
        \ = 0; k < queriesSize; k++) {\n        int u0 = queries[k][0], v0 = queries[k][1];\n\
        \        int u = u0, v = v0;\n        if (depth[u] < depth[v]) { int temp =\
        \ u; u = v; v = temp; }\n        int diff = depth[u] - depth[v];\n        for\
        \ (int i = 0; i < 18; i++) if ((diff >> i) & 1) u = up[i * (n + 1) + u];\n \
        \       int lca;\n        if (u == v) lca = u;\n        else {\n           \
        \ for (int i = 17; i >= 0; i--) {\n                if (up[i * (n + 1) + u] !=\
        \ up[i * (n + 1) + v]) {\n                    u = up[i * (n + 1) + u];\n   \
        \                 v = up[i * (n + 1) + v];\n                }\n            }\n\
        \            lca = up[0 * (n + 1) + u];\n        }\n        int dist = depth[u0]\
        \ + depth[v0] - 2 * depth[lca];\n        result[k] = (dist == 0) ? 0 : (int)pow2[dist\
        \ - 1];\n    }\n\n    free(head); free(to); free(next); free(depth); free(up);\
        \ free(queue); free(visited); free(pow2);\n    *returnSize = queriesSize;\n\
        \    return result;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int[] AssignEdgeWeights(int[][] edges, int[][] queries) {\n\
        \        int n = edges.Length + 1;\n        List<int>[] adj = new List<int>[n\
        \ + 1];\n        for (int i = 1; i <= n; i++) adj[i] = new List<int>();\n  \
        \      foreach (var edge in edges) {\n            adj[edge[0]].Add(edge[1]);\n\
        \            adj[edge[1]].Add(edge[0]);\n        }\n\n        int[,] up = new\
        \ int[18, n + 1];\n        int[] depth = new int[n + 1];\n        bool[] visited\
        \ = new bool[n + 1];\n        Queue<int> queue = new Queue<int>();\n\n     \
        \   queue.Enqueue(1);\n        visited[1] = true;\n        depth[1] = 0;\n \
        \       while (queue.Count > 0) {\n            int u = queue.Dequeue();\n  \
        \          foreach (int v in adj[u]) {\n                if (!visited[v]) {\n\
        \                    visited[v] = true;\n                    depth[v] = depth[u]\
        \ + 1;\n                    up[0, v] = u;\n                    queue.Enqueue(v);\n\
        \                }\n            }\n        }\n\n        for (int j = 1; j <\
        \ 18; j++) {\n            for (int i = 1; i <= n; i++) {\n                up[j,\
        \ i] = up[j - 1, up[j - 1, i]];\n            }\n        }\n\n        int MOD\
        \ = 1000000007;\n        long[] pow2 = new long[n + 1];\n        pow2[0] = 1;\n\
        \        for (int i = 1; i <= n; i++) pow2[i] = (pow2[i - 1] * 2) % MOD;\n\n\
        \        int[] result = new int[queries.Length];\n        for (int k = 0; k\
        \ < queries.Length; k++) {\n            int u0 = queries[k][0], v0 = queries[k][1];\n\
        \            int u = u0, v = v0;\n            if (depth[u] < depth[v]) { int\
        \ temp = u; u = v; v = temp; }\n            int diff = depth[u] - depth[v];\n\
        \            for (int i = 0; i < 18; i++) if (((diff >> i) & 1) == 1) u = up[i,\
        \ u];\n            int lca;\n            if (u == v) lca = u;\n            else\
        \ {\n                for (int i = 17; i >= 0; i--) {\n                    if\
        \ (up[i, u] != up[i, v]) {\n                        u = up[i, u];\n        \
        \                v = up[i, v];\n                    }\n                }\n \
        \               lca = up[0, u];\n            }\n            int dist = depth[u0]\
        \ + depth[v0] - 2 * depth[lca];\n            result[k] = (dist == 0) ? 0 : (int)pow2[dist\
        \ - 1];\n        }\n        return result;\n    }\n}"
      javascript: "/**\n * @param {number[][]} edges\n * @param {number[][]} queries\n\
        \ * @return {number[]}\n */\nvar assignEdgeWeights = function(edges, queries)\
        \ {\n    const n = edges.length + 1;\n    const adj = Array.from({ length: n\
        \ + 1 }, () => []);\n    for (const [u, v] of edges) {\n        adj[u].push(v);\n\
        \        adj[v].push(u);\n    }\n\n    const up = new Int32Array(18 * (n + 1));\n\
        \    const depth = new Int32Array(n + 1);\n    const visited = new Uint8Array(n\
        \ + 1);\n    const queue = new Int32Array(n);\n    let headPtr = 0, tailPtr\
        \ = 0;\n\n    queue[tailPtr++] = 1;\n    visited[1] = 1;\n    depth[1] = 0;\n\
        \    while (headPtr < tailPtr) {\n        const u = queue[headPtr++];\n    \
        \    const neighbors = adj[u];\n        for (let i = 0; i < neighbors.length;\
        \ i++) {\n            const v = neighbors[i];\n            if (!visited[v])\
        \ {\n                visited[v] = 1;\n                depth[v] = depth[u] +\
        \ 1;\n                up[0 * (n + 1) + v] = u;\n                queue[tailPtr++]\
        \ = v;\n            }\n        }\n    }\n\n    for (let j = 1; j < 18; j++)\
        \ {\n        for (let i = 1; i <= n; i++) {\n            const prev = up[(j\
        \ - 1) * (n + 1) + i];\n            up[j * (n + 1) + i] = up[(j - 1) * (n +\
        \ 1) + prev];\n        }\n    }\n\n    const MOD = 1000000007;\n    const pow2\
        \ = new Int32Array(n + 1);\n    pow2[0] = 1;\n    for (let i = 1; i <= n; i++)\
        \ pow2[i] = (pow2[i - 1] * 2) % MOD;\n\n    const result = new Int32Array(queries.length);\n\
        \    for (let k = 0; k < queries.length; k++) {\n        const u0 = queries[k][0],\
        \ v0 = queries[k][1];\n        let u = u0, v = v0;\n        if (depth[u] < depth[v])\
        \ { let t = u; u = v; v = t; }\n        const diff = depth[u] - depth[v];\n\
        \        for (let i = 0; i < 18; i++) if ((diff >> i) & 1) u = up[i * (n + 1)\
        \ + u];\n        let lca;\n        if (u === v) lca = u;\n        else {\n \
        \           for (let i = 17; i >= 0; i--) {\n                if (up[i * (n +\
        \ 1) + u] !== up[i * (n + 1) + v]) {\n                    u = up[i * (n + 1)\
        \ + u];\n                    v = up[i * (n + 1) + v];\n                }\n \
        \           }\n            lca = up[0 * (n + 1) + u];\n        }\n        const\
        \ dist = depth[u0] + depth[v0] - 2 * depth[lca];\n        result[k] = (dist\
        \ === 0) ? 0 : pow2[dist - 1];\n    }\n    return Array.from(result);\n};"
      typescript: "function assignEdgeWeights(edges: number[][], queries: number[][]):\
        \ number[] {\n    const n = edges.length + 1;\n    const maxLog = 17;\n    const\
        \ head = new Int32Array(n + 1).fill(-1);\n    const next = new Int32Array(2\
        \ * n);\n    const to = new Int32Array(2 * n);\n    let edgeCount = 0;\n\n \
        \   for (const [u, v] of edges) {\n        to[edgeCount] = v;\n        next[edgeCount]\
        \ = head[u];\n        head[u] = edgeCount++;\n        to[edgeCount] = u;\n \
        \       next[edgeCount] = head[v];\n        head[v] = edgeCount++;\n    }\n\n\
        \    const depth = new Int32Array(n + 1);\n    const up = Array.from({ length:\
        \ n + 1 }, () => new Int32Array(maxLog + 1));\n    const visited = new Uint8Array(n\
        \ + 1);\n\n    const queue = new Int32Array(n);\n    let headQ = 0;\n    let\
        \ tailQ = 0;\n\n    queue[tailQ++] = 1;\n    visited[1] = 1;\n    depth[1] =\
        \ 0;\n\n    while (headQ < tailQ) {\n        const u = queue[headQ++];\n   \
        \     for (let e = head[u]; e !== -1; e = next[e]) {\n            const v =\
        \ to[e];\n            if (!visited[v]) {\n                visited[v] = 1;\n\
        \                depth[v] = depth[u] + 1;\n                up[v][0] = u;\n \
        \               queue[tailQ++] = v;\n            }\n        }\n    }\n\n   \
        \ for (let i = 1; i <= maxLog; i++) {\n        for (let u = 1; u <= n; u++)\
        \ {\n            up[u][i] = up[up[u][i - 1]][i - 1];\n        }\n    }\n\n \
        \   const MOD = 1000000007;\n    const pow2 = new Int32Array(n + 1);\n    pow2[0]\
        \ = 1;\n    for (let i = 1; i <= n; i++) {\n        pow2[i] = (pow2[i - 1] *\
        \ 2) % MOD;\n    }\n\n    const results: number[] = [];\n    for (const [uOrig,\
        \ vOrig] of queries) {\n        let u = uOrig;\n        let v = vOrig;\n   \
        \     if (depth[u] < depth[v]) {\n            [u, v] = [v, u];\n        }\n\n\
        \        for (let i = maxLog; i >= 0; i--) {\n            if (depth[u] - (1\
        \ << i) >= depth[v]) {\n                u = up[u][i];\n            }\n     \
        \   }\n\n        let lca = u;\n        if (u !== v) {\n            for (let\
        \ i = maxLog; i >= 0; i--) {\n                if (up[u][i] !== up[v][i]) {\n\
        \                    u = up[u][i];\n                    v = up[v][i];\n    \
        \            }\n            }\n            lca = up[u][0];\n        }\n\n  \
        \      const dist = depth[uOrig] + depth[vOrig] - 2 * depth[lca];\n        results.push(dist\
        \ === 0 ? 0 : pow2[dist - 1]);\n    }\n\n    return results;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $edges\n     * @param\
        \ Integer[][] $queries\n     * @return Integer[]\n     */\n    function assignEdgeWeights($edges,\
        \ $queries) {\n        $n = count($edges) + 1;\n        $maxLog = 17;\n    \
        \    $logStep = $maxLog + 1;\n        $MOD = 1000000007;\n\n        $head =\
        \ new SplFixedArray($n + 1);\n        for ($i = 0; $i <= $n; $i++) $head[$i]\
        \ = -1;\n        $next = new SplFixedArray(2 * $n);\n        $to = new SplFixedArray(2\
        \ * $n);\n        $edgeCount = 0;\n\n        foreach ($edges as $edge) {\n \
        \           $u = $edge[0]; $v = $edge[1];\n            $to[$edgeCount] = $v;\n\
        \            $next[$edgeCount] = $head[$u];\n            $head[$u] = $edgeCount++;\n\
        \            $to[$edgeCount] = $u;\n            $next[$edgeCount] = $head[$v];\n\
        \            $head[$v] = $edgeCount++;\n        }\n\n        $depth = new SplFixedArray($n\
        \ + 1);\n        $up = new SplFixedArray(($n + 1) * $logStep);\n        for\
        \ ($i = 0; $i < ($n + 1) * $logStep; $i++) $up[$i] = 0;\n        $visited =\
        \ new SplFixedArray($n + 1);\n        for ($i = 0; $i <= $n; $i++) $visited[$i]\
        \ = false;\n\n        $queue = new SplQueue();\n        $queue->enqueue(1);\n\
        \        $visited[1] = true;\n        $depth[1] = 0;\n\n        while (!$queue->isEmpty())\
        \ {\n            $u = $queue->dequeue();\n            for ($e = $head[$u]; $e\
        \ != -1; $e = $next[$e]) {\n                $v = $to[$e];\n                if\
        \ (!$visited[$v]) {\n                    $visited[$v] = true;\n            \
        \        $depth[$v] = $depth[$u] + 1;\n                    $up[$v * $logStep]\
        \ = $u;\n                    $queue->enqueue($v);\n                }\n     \
        \       }\n        }\n\n        for ($i = 1; $i <= $maxLog; $i++) {\n      \
        \      for ($u = 1; $u <= $n; $u++) {\n                $up[$u * $logStep + $i]\
        \ = $up[$up[$u * $logStep + $i - 1] * $logStep + $i - 1];\n            }\n \
        \       }\n\n        $pow2 = new SplFixedArray($n + 1);\n        $pow2[0] =\
        \ 1;\n        for ($i = 1; $i <= $n; $i++) {\n            $pow2[$i] = ($pow2[$i\
        \ - 1] * 2) % $MOD;\n        }\n\n        $results = [];\n        foreach ($queries\
        \ as $query) {\n            $uOrig = $query[0];\n            $vOrig = $query[1];\n\
        \            $u = $uOrig;\n            $v = $vOrig;\n\n            if ($depth[$u]\
        \ < $depth[$v]) {\n                $tmp = $u; $u = $v; $v = $tmp;\n        \
        \    }\n\n            for ($i = $maxLog; $i >= 0; $i--) {\n                if\
        \ ($depth[$u] - (1 << $i) >= $depth[$v]) {\n                    $u = $up[$u\
        \ * $logStep + $i];\n                }\n            }\n\n            $lca =\
        \ $u;\n            if ($u != $v) {\n                for ($i = $maxLog; $i >=\
        \ 0; $i--) {\n                    if ($up[$u * $logStep + $i] != $up[$v * $logStep\
        \ + $i]) {\n                        $u = $up[$u * $logStep + $i];\n        \
        \                $v = $up[$v * $logStep + $i];\n                    }\n    \
        \            }\n                $lca = $up[$u * $logStep];\n            }\n\n\
        \            $dist = $depth[$uOrig] + $depth[$vOrig] - 2 * $depth[$lca];\n \
        \           $results[] = ($dist == 0) ? 0 : $pow2[$dist - 1];\n        }\n\n\
        \        return $results;\n    }\n}"
      swift: "class Solution {\n    func assignEdgeWeights(_ edges: [[Int]], _ queries:\
        \ [[Int]]) -> [Int] {\n        let n = edges.count + 1\n        var head = [Int](repeating:\
        \ -1, count: n + 1)\n        var next = [Int](repeating: -1, count: 2 * n)\n\
        \        var to = [Int](repeating: 0, count: 2 * n)\n        var edgeCount =\
        \ 0\n\n        for edge in edges {\n            let u = edge[0], v = edge[1]\n\
        \            to[edgeCount] = v\n            next[edgeCount] = head[u]\n    \
        \        head[u] = edgeCount\n            edgeCount += 1\n\n            to[edgeCount]\
        \ = u\n            next[edgeCount] = head[v]\n            head[v] = edgeCount\n\
        \            edgeCount += 1\n        }\n\n        let maxLog = 17\n        var\
        \ depth = [Int](repeating: 0, count: n + 1)\n        var up = Array(repeating:\
        \ Array(repeating: 0, count: maxLog + 1), count: n + 1)\n        var visited\
        \ = [Bool](repeating: false, count: n + 1)\n\n        var queue = [Int]()\n\
        \        queue.reserveCapacity(n)\n        queue.append(1)\n        var qHead\
        \ = 0\n        visited[1] = true\n        depth[1] = 0\n\n        while qHead\
        \ < queue.count {\n            let u = queue[qHead]\n            qHead += 1\n\
        \n            var e = head[u]\n            while e != -1 {\n               \
        \ let v = to[e]\n                if !visited[v] {\n                    visited[v]\
        \ = true\n                    depth[v] = depth[u] + 1\n                    up[v][0]\
        \ = u\n                    queue.append(v)\n                }\n            \
        \    e = next[e]\n            }\n        }\n\n        for i in 1...maxLog {\n\
        \            for u in 1...n {\n                up[u][i] = up[up[u][i-1]][i-1]\n\
        \            }\n        }\n\n        let mod = 1_000_000_007\n        var pow2\
        \ = [Int](repeating: 0, count: n + 1)\n        pow2[0] = 1\n        if n >=\
        \ 1 {\n            for i in 1...n {\n                pow2[i] = (pow2[i-1] *\
        \ 2) % mod\n            }\n        }\n\n        var results = [Int]()\n    \
        \    results.reserveCapacity(queries.count)\n        for query in queries {\n\
        \            let uOrig = query[0], vOrig = query[1]\n            var u = uOrig,\
        \ v = vOrig\n\n            if depth[u] < depth[v] {\n                let tmp\
        \ = u; u = v; v = tmp\n            }\n\n            for i in stride(from: maxLog,\
        \ through: 0, by: -1) {\n                if depth[u] - (1 << i) >= depth[v]\
        \ {\n                    u = up[u][i]\n                }\n            }\n\n\
        \            var lca = u\n            if u != v {\n                for i in\
        \ stride(from: maxLog, through: 0, by: -1) {\n                    if up[u][i]\
        \ != up[v][i] {\n                        u = up[u][i]\n                    \
        \    v = up[v][i]\n                    }\n                }\n              \
        \  lca = up[u][0]\n            }\n\n            let dist = depth[uOrig] + depth[vOrig]\
        \ - 2 * depth[lca]\n            results.append(dist == 0 ? 0 : pow2[dist - 1])\n\
        \        }\n\n        return results\n    }\n}"
      kotlin: "import java.util.*\n\nclass Solution {\n    fun assignEdgeWeights(edges:\
        \ Array<IntArray>, queries: Array<IntArray>): IntArray {\n        val n = edges.size\
        \ + 1\n        val head = IntArray(n + 1) { -1 }\n        val next = IntArray(2\
        \ * n)\n        val to = IntArray(2 * n)\n        var edgeCount = 0\n\n    \
        \    for (edge in edges) {\n            val u = edge[0]\n            val v =\
        \ edge[1]\n            to[edgeCount] = v\n            next[edgeCount] = head[u]\n\
        \            head[u] = edgeCount++\n            to[edgeCount] = u\n        \
        \    next[edgeCount] = head[v]\n            head[v] = edgeCount++\n        }\n\
        \n        val maxLog = 17\n        val depth = IntArray(n + 1)\n        val\
        \ up = Array(n + 1) { IntArray(maxLog + 1) }\n        val queue: Deque<Int>\
        \ = ArrayDeque()\n        val visited = BooleanArray(n + 1)\n\n        queue.add(1)\n\
        \        visited[1] = true\n        depth[1] = 0\n\n        while (queue.isNotEmpty())\
        \ {\n            val u = queue.poll()\n            var e = head[u]\n       \
        \     while (e != -1) {\n                val v = to[e]\n                if (!visited[v])\
        \ {\n                    visited[v] = true\n                    depth[v] = depth[u]\
        \ + 1\n                    up[v][0] = u\n                    queue.add(v)\n\
        \                }\n                e = next[e]\n            }\n        }\n\n\
        \        for (i in 1..maxLog) {\n            for (u in 1..n) {\n           \
        \     up[u][i] = up[up[u][i - 1]][i - 1]\n            }\n        }\n\n     \
        \   val mod = 1000000007\n        val pow2 = IntArray(n + 1)\n        pow2[0]\
        \ = 1\n        for (i in 1..n) {\n            pow2[i] = ((pow2[i - 1].toLong()\
        \ * 2) % mod).toInt()\n        }\n\n        val results = IntArray(queries.size)\n\
        \        for (i in queries.indices) {\n            val uOrig = queries[i][0]\n\
        \            val vOrig = queries[i][1]\n            var u = uOrig\n        \
        \    var v = vOrig\n\n            if (depth[u] < depth[v]) {\n             \
        \   val tmp = u\n                u = v\n                v = tmp\n          \
        \  }\n\n            for (j in maxLog downTo 0) {\n                if (depth[u]\
        \ - (1 shl j) >= depth[v]) {\n                    u = up[u][j]\n           \
        \     }\n            }\n\n            var lca = u\n            if (u != v) {\n\
        \                for (j in maxLog downTo 0) {\n                    if (up[u][j]\
        \ != up[v][j]) {\n                        u = up[u][j]\n                   \
        \     v = up[v][j]\n                    }\n                }\n             \
        \   lca = up[u][0]\n            }\n\n            val dist = depth[uOrig] + depth[vOrig]\
        \ - 2 * depth[lca]\n            results[i] = if (dist == 0) 0 else pow2[dist\
        \ - 1]\n        }\n\n        return results\n    }\n}"
      dart: "import 'dart:typed_data';\n\nclass Solution {\n  List<int> assignEdgeWeights(List<List<int>>\
        \ edges, List<List<int>> queries) {\n    int n = edges.length + 1;\n    List<List<int>>\
        \ adj = List.generate(n + 1, (_) => []);\n    for (var edge in edges) {\n  \
        \    adj[edge[0]].add(edge[1]);\n      adj[edge[1]].add(edge[0]);\n    }\n\n\
        \    Int32List depth = Int32List(n + 1);\n    List<Int32List> up = List.generate(18,\
        \ (_) => Int32List(n + 1));\n    List<bool> visited = List.filled(n + 1, false);\n\
        \n    List<int> queue = [1];\n    visited[1] = true;\n    depth[1] = 0;\n  \
        \  int head = 0;\n    while (head < queue.length) {\n      int u = queue[head++];\n\
        \      for (int v in adj[u]) {\n        if (!visited[v]) {\n          visited[v]\
        \ = true;\n          depth[v] = depth[u] + 1;\n          up[0][v] = u;\n   \
        \       queue.add(v);\n        }\n      }\n    }\n\n    for (int i = 1; i <\
        \ 18; i++) {\n      for (int j = 1; j <= n; j++) {\n        up[i][j] = up[i\
        \ - 1][up[i - 1][j]];\n      }\n    }\n\n    const int mod = 1000000007;\n \
        \   Int32List pow2 = Int32List(n + 1);\n    pow2[0] = 1;\n    for (int i = 1;\
        \ i <= n; i++) {\n      pow2[i] = (pow2[i - 1] * 2) % mod;\n    }\n\n    List<int>\
        \ results = [];\n    for (var query in queries) {\n      int u = query[0];\n\
        \      int v = query[1];\n      int uOrig = u;\n      int vOrig = v;\n\n   \
        \   if (depth[u] < depth[v]) {\n        int temp = u;\n        u = v;\n    \
        \    v = temp;\n      }\n      int diff = depth[u] - depth[v];\n      for (int\
        \ i = 0; i < 18; i++) {\n        if ((diff >> i) & 1 == 1) {\n          u =\
        \ up[i][u];\n        }\n      }\n\n      int lca;\n      if (u == v) {\n   \
        \     lca = u;\n      } else {\n        for (int i = 17; i >= 0; i--) {\n  \
        \        if (up[i][u] != up[i][v]) {\n            u = up[i][u];\n          \
        \  v = up[i][v];\n          }\n        }\n        lca = up[0][u];\n      }\n\
        \n      int dist = depth[uOrig] + depth[vOrig] - 2 * depth[lca];\n      results.add(dist\
        \ == 0 ? 0 : pow2[dist - 1]);\n    }\n    return results;\n  }\n}"
      go: "func assignEdgeWeights(edges [][]int, queries [][]int) []int {\n\tn := len(edges)\
        \ + 1\n\tadj := make([][]int, n+1)\n\tfor _, edge := range edges {\n\t\tu, v\
        \ := edge[0], edge[1]\n\t\tadj[u] = append(adj[u], v)\n\t\tadj[v] = append(adj[v],\
        \ u)\n\t}\n\n\tdepth := make([]int, n+1)\n\tup := make([][]int, 18)\n\tfor i\
        \ := range up {\n\t\tup[i] = make([]int, n+1)\n\t}\n\tvisited := make([]bool,\
        \ n+1)\n\n\tqueue := []int{1}\n\tvisited[1] = true\n\tdepth[1] = 0\n\tfor len(queue)\
        \ > 0 {\n\t\tu := queue[0]\n\t\tqueue = queue[1:]\n\t\tfor _, v := range adj[u]\
        \ {\n\t\t\tif !visited[v] {\n\t\t\t\tvisited[v] = true\n\t\t\t\tdepth[v] = depth[u]\
        \ + 1\n\t\t\t\tup[0][v] = u\n\t\t\t\tqueue = append(queue, v)\n\t\t\t}\n\t\t\
        }\n\t}\n\n\tfor i := 1; i < 18; i++ {\n\t\tfor j := 1; j <= n; j++ {\n\t\t\t\
        up[i][j] = up[i-1][up[i-1][j]]\n\t\t}\n\t}\n\n\tmod := 1000000007\n\tpow2 :=\
        \ make([]int, n+1)\n\tpow2[0] = 1\n\tfor i := 1; i <= n; i++ {\n\t\tpow2[i]\
        \ = (pow2[i-1] * 2) % mod\n\t}\n\n\tresults := make([]int, len(queries))\n\t\
        for i, query := range queries {\n\t\tu, v := query[0], query[1]\n\t\tuOrig,\
        \ vOrig := u, v\n\n\t\tif depth[u] < depth[v] {\n\t\t\tu, v = v, u\n\t\t}\n\t\
        \tdiff := depth[u] - depth[v]\n\t\tfor j := 0; j < 18; j++ {\n\t\t\tif (diff>>j)&1\
        \ == 1 {\n\t\t\t\tu = up[j][u]\n\t\t\t}\n\t\t}\n\n\t\tlca := 0\n\t\tif u ==\
        \ v {\n\t\t\tlca = u\n\t\t} else {\n\t\t\tfor j := 17; j >= 0; j-- {\n\t\t\t\
        \tif up[j][u] != up[j][v] {\n\t\t\t\t\tu = up[j][u]\n\t\t\t\t\tv = up[j][v]\n\
        \t\t\t\t}\n\t\t\t}\n\t\t\tlca = up[0][u]\n\t\t}\n\n\t\tdist := depth[uOrig]\
        \ + depth[vOrig] - 2*depth[lca]\n\t\tif dist == 0 {\n\t\t\tresults[i] = 0\n\t\
        \t} else {\n\t\t\tresults[i] = pow2[dist-1]\n\t\t}\n\t}\n\treturn results\n}"
      ruby: "def assign_edge_weights(edges, queries)\n  n = edges.length + 1\n  adj\
        \ = Array.new(n + 1) { [] }\n  edges.each do |u, v|\n    adj[u] << v\n    adj[v]\
        \ << u\n  end\n\n  depth = Array.new(n + 1, 0)\n  up = Array.new(18) { Array.new(n\
        \ + 1, 0) }\n  visited = Array.new(n + 1, false)\n  queue = [1]\n  visited[1]\
        \ = true\n  depth[1] = 0\n\n  head = 0\n  while head < queue.length\n    u =\
        \ queue[head]\n    head += 1\n    adj[u].each do |v|\n      if !visited[v]\n\
        \        visited[v] = true\n        depth[v] = depth[u] + 1\n        up[0][v]\
        \ = u\n        queue << v\n      end\n    end\n  end\n\n  (1..17).each do |i|\n\
        \    up_i = up[i]\n    up_prev = up[i - 1]\n    (1..n).each do |j|\n      up_i[j]\
        \ = up_prev[up_prev[j]]\n    end\n  end\n\n  mod = 1_000_000_007\n  pow2 = Array.new(n\
        \ + 1)\n  pow2[0] = 1\n  (1..n).each { |i| pow2[i] = (pow2[i - 1] * 2) % mod\
        \ }\n\n  ans = Array.new(queries.length)\n  idx = 0\n  while idx < queries.length\n\
        \    u = queries[idx][0]\n    v = queries[idx][1]\n    u_orig, v_orig = u, v\n\
        \n    if depth[u] < depth[v]\n      u, v = v, u\n    end\n    diff = depth[u]\
        \ - depth[v]\n    18.times { |i| u = up[i][u] if diff[i] == 1 }\n\n    if u\
        \ == v\n      lca = u\n    else\n      i = 17\n      while i >= 0\n        if\
        \ up[i][u] != up[i][v]\n          u = up[i][u]\n          v = up[i][v]\n   \
        \     end\n        i -= 1\n      end\n      lca = up[0][u]\n    end\n\n    dist\
        \ = depth[u_orig] + depth[v_orig] - 2 * depth[lca]\n    ans[idx] = (dist ==\
        \ 0 ? 0 : pow2[dist - 1])\n    idx += 1\n  end\n  ans\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n  def assignEdgeWeights(edges:\
        \ Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {\n    val n\
        \ = edges.length + 1\n    val adj = Array.fill(n + 1)(mutable.ArrayBuffer.empty[Int])\n\
        \    for (edge <- edges) {\n      adj(edge(0)) += edge(1)\n      adj(edge(1))\
        \ += edge(0)\n    }\n\n    val depth = new Array[Int](n + 1)\n    val up = Array.ofDim[Int](18,\
        \ n + 1)\n    val visited = new Array[Boolean](n + 1)\n\n    val queue = mutable.Queue[Int]()\n\
        \    queue.enqueue(1)\n    visited(1) = true\n    depth(1) = 0\n\n    while\
        \ (queue.nonEmpty) {\n      val u = queue.dequeue()\n      for (v <- adj(u))\
        \ {\n        if (!visited(v)) {\n          visited(v) = true\n          depth(v)\
        \ = depth(u) + 1\n          up(0)(v) = u\n          queue.enqueue(v)\n     \
        \   }\n      }\n    }\n\n    for (i <- 1 until 18) {\n      for (j <- 1 to n)\
        \ {\n        up(i)(j) = up(i - 1)(up(i - 1)(j))\n      }\n    }\n\n    val mod\
        \ = 1000000007\n    val pow2 = new Array[Int](n + 1)\n    pow2(0) = 1\n    for\
        \ (i <- 1 to n) {\n      pow2(i) = ((pow2(i - 1).toLong * 2) % mod).toInt\n\
        \    }\n\n    val results = new Array[Int](queries.length)\n    for (idx <-\
        \ queries.indices) {\n      val uOrig = queries(idx)(0)\n      val vOrig = queries(idx)(1)\n\
        \      var u = uOrig\n      var v = vOrig\n\n      if (depth(u) < depth(v))\
        \ {\n        val temp = u\n        u = v\n        v = temp\n      }\n      val\
        \ diff = depth(u) - depth(v)\n      for (i <- 0 until 18) {\n        if (((diff\
        \ >> i) & 1) == 1) {\n          u = up(i)(u)\n        }\n      }\n\n      val\
        \ lca = if (u == v) u else {\n        var i = 17\n        while (i >= 0) {\n\
        \          if (up(i)(u) != up(i)(v)) {\n            u = up(i)(u)\n         \
        \   v = up(i)(v)\n          }\n          i -= 1\n        }\n        up(0)(u)\n\
        \      }\n\n      val dist = depth(uOrig) + depth(vOrig) - 2 * depth(lca)\n\
        \      results(idx) = if (dist == 0) 0 else pow2(dist - 1)\n    }\n    results\n\
        \  }\n}"
      rust: "impl Solution {\n    pub fn assign_edge_weights(edges: Vec<Vec<i32>>, queries:\
        \ Vec<Vec<i32>>) -> Vec<i32> {\n        let n = edges.len() + 1;\n        let\
        \ mut adj = vec![vec![]; n + 1];\n        for e in edges {\n            let\
        \ u = e[0] as usize;\n            let v = e[1] as usize;\n            adj[u].push(v);\n\
        \            adj[v].push(u);\n        }\n\n        let mut depth = vec![0; n\
        \ + 1];\n        let mut up = vec![vec![0; 18]; n + 1];\n        let mut visited\
        \ = vec![false; n + 1];\n        let mut queue = std::collections::VecDeque::new();\n\
        \n        queue.push_back(1);\n        visited[1] = true;\n        up[1][0]\
        \ = 1;\n\n        while let Some(u) = queue.pop_front() {\n            for &v\
        \ in &adj[u] {\n                if !visited[v] {\n                    visited[v]\
        \ = true;\n                    depth[v] = depth[u] + 1;\n                  \
        \  up[v][0] = u;\n                    queue.push_back(v);\n                }\n\
        \            }\n        }\n\n        for i in 1..18 {\n            for u in\
        \ 1..=n {\n                up[u][i] = up[up[u][i - 1]][i - 1];\n           \
        \ }\n        }\n\n        let mut pow2 = vec![1; n + 1];\n        let mod_val\
        \ = 1_000_000_007;\n        for i in 1..=n {\n            pow2[i] = (pow2[i\
        \ - 1] * 2) % mod_val;\n        }\n\n        queries.iter().map(|q| {\n    \
        \        let mut u = q[0] as usize;\n            let mut v = q[1] as usize;\n\
        \            if u == v { return 0; }\n            let (original_u, original_v)\
        \ = (u, v);\n\n            if depth[u] < depth[v] { std::mem::swap(&mut u, &mut\
        \ v); }\n            let diff = depth[u] - depth[v];\n            for i in 0..18\
        \ {\n                if (diff >> i) & 1 == 1 {\n                    u = up[u][i];\n\
        \                }\n            }\n\n            let lca = if u == v {\n   \
        \             u\n            } else {\n                for i in (0..18).rev()\
        \ {\n                    if up[u][i] != up[v][i] {\n                       \
        \ u = up[u][i];\n                        v = up[v][i];\n                   \
        \ }\n                }\n                up[u][0]\n            };\n\n       \
        \     let dist = depth[original_u] + depth[original_v] - 2 * depth[lca];\n \
        \           pow2[dist - 1] as i32\n        }).collect()\n    }\n}"
      racket: "(define/contract (assign-edge-weights edges queries)\n  (-> (listof (listof\
        \ exact-integer?)) (listof (listof exact-integer?)) (listof exact-integer?))\n\
        \  (let* ([n (+ (length edges) 1)]\n         [adj (make-vector (+ n 1) '())])\n\
        \    (for ([e edges])\n      (let ([u (first e)] [v (second e)])\n        (vector-set!\
        \ adj u (cons v (vector-ref adj u)))\n        (vector-set! adj v (cons u (vector-ref\
        \ adj v)))))\n\n    (define depth (make-vector (+ n 1) 0))\n    (define up (make-vector\
        \ 18))\n    (for ([i 18]) (vector-set! up i (make-vector (+ n 1) 0)))\n\n  \
        \  (define visited (make-vector (+ n 1) #f))\n    (vector-set! visited 1 #t)\n\
        \    (vector-set! (vector-ref up 0) 1 1)\n    (let loop-q ([q-in '()] [q-out\
        \ (list 1)])\n      (cond\n        [(and (null? q-in) (null? q-out)) (void)]\n\
        \        [(null? q-out) (loop-q '() (reverse q-in))]\n        [else\n      \
        \   (let* ([u (car q-out)]\n                [neighbors (vector-ref adj u)]\n\
        \                [next-in (foldl (lambda (v acc)\n                         \
        \         (if (vector-ref visited v)\n                                     \
        \ acc\n                                      (begin\n                      \
        \                  (vector-set! visited v #t)\n                            \
        \            (vector-set! depth v (+ (vector-ref depth u) 1))\n            \
        \                            (vector-set! (vector-ref up 0) v u)\n         \
        \                               (cons v acc))))\n                          \
        \      q-in neighbors)])\n           (loop-q next-in (cdr q-out)))]))\n\n  \
        \  (for ([i (in-range 1 18)])\n      (let ([prev-up (vector-ref up (- i 1))]\n\
        \            [curr-up (vector-ref up i)])\n        (for ([u (in-range 1 (+ n\
        \ 1))])\n          (vector-set! curr-up u (vector-ref prev-up (vector-ref prev-up\
        \ u))))))\n\n    (define (get-lca u v)\n      (let* ([du (vector-ref depth u)]\n\
        \             [dv (vector-ref depth v)]\n             [u-ref (if (< du dv) v\
        \ u)]\n             [v-ref (if (< du dv) u v)]\n             [diff (- (vector-ref\
        \ depth u-ref) (vector-ref depth v-ref))])\n        (let loop-u ([u u-ref] [i\
        \ 17])\n          (if (>= i 0)\n              (if (bitwise-bit-set? diff i)\n\
        \                  (loop-u (vector-ref (vector-ref up i) u) (- i 1))\n     \
        \             (loop-u u (- i 1)))\n              (if (= u v-ref) u\n       \
        \           (let loop-uv ([u u] [v v-ref] [i 17])\n                    (if (>=\
        \ i 0)\n                        (let ([ui (vector-ref (vector-ref up i) u)]\n\
        \                              [vi (vector-ref (vector-ref up i) v)])\n    \
        \                      (if (not (= ui vi))\n                              (loop-uv\
        \ ui vi (- i 1))\n                              (loop-uv u v (- i 1))))\n  \
        \                      (vector-ref (vector-ref up 0) u))))))))\n\n    (define\
        \ pow2 (make-vector (+ n 1) 1))\n    (for ([i (in-range 1 (+ n 1))])\n     \
        \ (vector-set! pow2 i (modulo (* (vector-ref pow2 (- i 1)) 2) 1000000007)))\n\
        \n    (map (lambda (query)\n           (let ([u (first query)] [v (second query)])\n\
        \             (if (= u v) 0\n                 (let* ([lca (get-lca u v)]\n \
        \                       [dist (- (+ (vector-ref depth u) (vector-ref depth v))\
        \ (* 2 (vector-ref depth lca)))])\n                   (vector-ref pow2 (- dist\
        \ 1))))))\n         queries)))"
      erlang: "-spec assign_edge_weights(Edges :: [[integer()]], Queries :: [[integer()]])\
        \ -> [integer()].\nassign_edge_weights(Edges, Queries) ->\n    N = length(Edges)\
        \ + 1,\n    Adj = lists:foldl(fun([U, V], Acc) ->\n        Acc1 = maps:put(U,\
        \ [V | maps:get(U, Acc, [])], Acc),\n        maps:put(V, [U | maps:get(V, Acc,\
        \ [])], Acc1)\n    end, #{}, Edges),\n\n    {Depths, Parents} = bfs([1], #{1\
        \ => true}, #{1 => 0}, #{1 => 1}, Adj),\n\n    Up0 = list_to_tuple([if I ==\
        \ 0 -> 0; true -> maps:get(I, Parents, 1) end || I <- lists:seq(0, N)]),\n \
        \   Up = compute_up_table(Up0, 1, [Up0], N),\n\n    DepthTuple = list_to_tuple([if\
        \ I == 0 -> 0; true -> maps:get(I, Depths, 0) end || I <- lists:seq(0, N)]),\n\
        \n    Pow2 = list_to_tuple(compute_pow2_list(N)),\n\n    [begin\n        [U,\
        \ V] = Q,\n        if U == V -> 0;\n           true ->\n               LCA =\
        \ get_lca(U, V, Up, DepthTuple),\n               Dist = element(U+1, DepthTuple)\
        \ + element(V+1, DepthTuple) - 2 * element(LCA+1, DepthTuple),\n           \
        \    element(Dist, Pow2)\n        end\n     end || Q <- Queries].\n\nbfs([],\
        \ _Visited, Depths, Parents, _Adj) -> {Depths, Parents};\nbfs(Level, Visited,\
        \ Depths, Parents, Adj) ->\n    {NextLevel, NewVisited, NewDepths, NewParents}\
        \ = \n        lists:foldl(fun(U, {L_acc, V_acc, D_acc, P_acc}) ->\n        \
        \    Neighbors = maps:get(U, Adj, []),\n            lists:foldl(fun(V, {L_in,\
        \ V_in, D_in, P_in}) ->\n                case maps:is_key(V, V_in) of\n    \
        \                false -> {[V | L_in], V_in#{V => true}, D_in#{V => maps:get(U,\
        \ D_in) + 1}, P_in#{V => U}};\n                    true -> {L_in, V_in, D_in,\
        \ P_in}\n                end\n            end, {L_acc, V_acc, D_acc, P_acc},\
        \ Neighbors)\n        end, {[], Visited, Depths, Parents}, Level),\n    bfs(NextLevel,\
        \ NewVisited, NewDepths, NewParents, Adj).\n\ncompute_up_table(_PrevUp, 18,\
        \ Acc, _N) -> list_to_tuple(lists:reverse(Acc));\ncompute_up_table(PrevUp, I,\
        \ Acc, N) ->\n    CurrUp = list_to_tuple([if J == 0 -> 0; true -> element(element(J+1,\
        \ PrevUp)+1, PrevUp) end || J <- lists:seq(0, N)]),\n    compute_up_table(CurrUp,\
        \ I+1, [CurrUp | Acc], N).\n\nget_lca(U, V, Up, DepthTuple) ->\n    DU = element(U+1,\
        \ DepthTuple),\n    DV = element(V+1, DepthTuple),\n    {U1, V1} = if DU < DV\
        \ -> {V, U}; true -> {U, V} end,\n    Diff = element(U1+1, DepthTuple) - element(V1+1,\
        \ DepthTuple),\n    U2 = lift_up(U1, Diff, Up),\n    if U2 == V1 -> U2;\n  \
        \     true -> find_common_ancestor(U2, V1, 17, Up)\n    end.\n\nlift_up(U, Diff,\
        \ Up) ->\n    lists:foldl(fun(I, AccU) ->\n        if (Diff band (1 bsl I))\
        \ =/= 0 ->\n            element(AccU+1, element(I+1, Up));\n           true\
        \ -> AccU\n        end\n    end, U, lists:seq(0, 17)).\n\nfind_common_ancestor(U,\
        \ V, -1, Up) -> element(U+1, element(1, Up));\nfind_common_ancestor(U, V, I,\
        \ Up) ->\n    UI = element(U+1, element(I+1, Up)),\n    VI = element(V+1, element(I+1,\
        \ Up)),\n    if UI =/= VI -> find_common_ancestor(UI, VI, I-1, Up);\n      \
        \ true -> find_common_ancestor(U, V, I-1, Up)\n    end.\n\ncompute_pow2_list(N)\
        \ ->\n    {List, _} = lists:foldl(fun(_, {Acc, Last}) -> \n        Next = (Last\
        \ * 2) rem 1000000007,\n        {[Next | Acc], Next}\n    end, {[1], 1}, lists:seq(1,\
        \ N)),\n    lists:reverse(List)."
      elixir: "defmodule Solution do\n  @spec assign_edge_weights(edges :: [[integer]],\
        \ queries :: [[integer]]) :: [integer]\n  def assign_edge_weights(edges, queries)\
        \ do\n    n = length(edges) + 1\n    adj = Enum.reduce(edges, %{}, fn [u, v],\
        \ acc ->\n      acc\n      |> Map.update(u, [v], &[v | &1])\n      |> Map.update(v,\
        \ [u], &[u | &1])\n    end)\n\n    {depths, parents} = bfs([1], %{1 => true},\
        \ %{1 => 0}, %{1 => 1}, adj)\n\n    up0 = List.to_tuple(for i <- 0..n, do: Map.get(parents,\
        \ i, 0))\n    up = compute_up_table(up0, 1, [up0], n)\n\n    depth_tuple = List.to_tuple(for\
        \ i <- 0..n, do: Map.get(depths, i, 0))\n\n    pow2 = List.to_tuple(compute_pow2_list(n))\n\
        \n    Enum.map(queries, fn [u, v] ->\n      if u == v do\n        0\n      else\n\
        \        lca = get_lca(u, v, up, depth_tuple)\n        dist = elem(depth_tuple,\
        \ u) + elem(depth_tuple, v) - 2 * elem(depth_tuple, lca)\n        elem(pow2,\
        \ dist - 1)\n      end\n    end)\n  end\n\n  defp bfs([], _visited, depths,\
        \ parents, _adj), do: {depths, parents}\n  defp bfs(level, visited, depths,\
        \ parents, adj) do\n    {next_level, new_visited, new_depths, new_parents} =\
        \ \n      Enum.reduce(level, {[], visited, depths, parents}, fn u, {l_acc, v_acc,\
        \ d_acc, p_acc} ->\n        neighbors = Map.get(adj, u, [])\n        Enum.reduce(neighbors,\
        \ {l_acc, v_acc, d_acc, p_acc}, fn v, {l_in, v_in, d_in, p_in} ->\n        \
        \  if Map.has_key?(v_in, v) do\n            {l_in, v_in, d_in, p_in}\n     \
        \     else\n            {[v | l_in], Map.put(v_in, v, true), Map.put(d_in, v,\
        \ Map.get(d_in, u) + 1), Map.put(p_in, v, u)}\n          end\n        end)\n\
        \      end)\n    bfs(next_level, new_visited, new_depths, new_parents, adj)\n\
        \  end\n\n  defp compute_up_table(_prev_up, 18, acc, _n), do: List.to_tuple(Enum.reverse(acc))\n\
        \  defp compute_up_table(prev_up, i, acc, n) do\n    curr_up = List.to_tuple(for\
        \ j <- 0..n do\n      if j == 0, do: 0, else: elem(prev_up, elem(prev_up, j))\n\
        \    end)\n    compute_up_table(curr_up, i + 1, [curr_up | acc], n)\n  end\n\
        \n  defp get_lca(u, v, up, depth_tuple) do\n    du = elem(depth_tuple, u)\n\
        \    dv = elem(depth_tuple, v)\n    {u1, v1} = if du < dv, do: {v, u}, else:\
        \ {u, v}\n    diff = elem(depth_tuple, u1) - elem(depth_tuple, v1)\n    u2 =\
        \ lift_up(u1, diff, up)\n    if u2 == v1 do\n      u2\n    else\n      find_common_ancestor(u2,\
        \ v1, 17, up)\n    end\n  end\n\n  defp lift_up(u, diff, up) do\n    use Bitwise\n\
        \    Enum.reduce(0..17, u, fn i, acc_u ->\n      if (diff &&& (1 <<< i)) !=\
        \ 0 do\n        elem(elem(up, i), acc_u)\n      else\n        acc_u\n      end\n\
        \    end)\n  end\n\n  defp find_common_ancestor(u, v, -1, up), do: elem(elem(up,\
        \ 0), u)\n  defp find_common_ancestor(u, v, i, up) do\n    ui = elem(elem(up,\
        \ i), u)\n    vi = elem(elem(up, i), v)\n    if ui != vi do\n      find_common_ancestor(ui,\
        \ vi, i - 1, up)\n    else\n      find_common_ancestor(u, v, i - 1, up)\n  \
        \  end\n  end\n\n  defp compute_pow2_list(n) do\n    Enum.reduce(1..n, [1],\
        \ fn _, [h | _] = acc ->\n      [rem(h * 2, 1_000_000_007) | acc]\n    end)\
        \ |> Enum.reverse()\n  end\nend"
    approach: The problem asks for the number of ways to assign weights 1 or 2 to the
      edges on a path between two nodes $u$ and $v$ such that the path sum is odd. Let
      $k$ be the number of edges on the path. Since assigning weight 2 is equivalent
      to a modulo 2 cost of 0 and weight 1 is equivalent to a modulo 2 cost of 1, the
      total path cost is odd if and only if the number of edges with weight 1 is odd.
      From combinatorics, the number of ways to choose an odd number of items out of
      $k$ items is $\sum_{i \in \{1, 3, 5, \dots\}} \binom{k}{i} = 2^{k-1}$ for $k \ge
      1$, and 0 for $k=0$.
    time_complexity: O((n + q) \log n) where $n$ is the number of nodes and $q$ is the
      number of queries. Precomputing the tree's depth and the binary lifting table
      for Lowest Common Ancestor (LCA) takes $O(n \log n)$, and each query is answered
      in $O(\log n)$ by finding the LCA to calculate the path distance.
    space_complexity: O(n \log n) because we store a binary lifting table of size $(n+1)
      \times \lceil \log_2 n \rceil$ and an adjacency list for the tree.
    elapsed_time: 588.8913164138794
    model: gemini-3-flash-preview
    generated_at: '2026-06-12 02:58:25 '
---

## Problem #3559: Number of Ways to Assign Edge Weights II

**Difficulty:** Hard

**Topics:** Array, Math, Dynamic Programming, Bit Manipulation, Tree, Depth-First Search

## Problem Description

<p>There is an undirected tree with <code>n</code> nodes labeled from 1 to <code>n</code>, rooted at node 1. The tree is represented by a 2D integer array <code>edges</code> of length <code>n - 1</code>, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> indicates that there is an edge between nodes <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code>.</p>

<p>Initially, all edges have a weight of 0. You must assign each edge a weight of either <strong>1</strong> or <strong>2</strong>.</p>

<p>The <strong>cost</strong> of a path between any two nodes <code>u</code> and <code>v</code> is the total weight of all edges in the path connecting them.</p>

<p>You are given a 2D integer array <code>queries</code>. For each <code>queries[i] = [u<sub>i</sub>, v<sub>i</sub>]</code>, determine the number of ways to assign weights to edges <strong>in the path</strong> such that the cost of the path between <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code> is <strong>odd</strong>.</p>

<p>Return an array <code>answer</code>, where <code>answer[i]</code> is the number of valid assignments for <code>queries[i]</code>.</p>

<p>Since the answer may be large, apply <strong>modulo</strong> <code>10<sup>9</sup> + 7</code> to each <code>answer[i]</code>.</p>

<p><strong>Note:</strong> For each query, disregard all edges <strong>not</strong> in the path between node <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><img src="https://assets.leetcode.com/uploads/2025/03/23/screenshot-2025-03-24-at-060006.png" style="height: 72px; width: 200px;" /></p>

<p><strong>Input:</strong> <span class="example-io">edges = [[1,2]], queries = [[1,1],[1,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,1]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Query <code>[1,1]</code>: The path from Node 1 to itself consists of no edges, so the cost is 0. Thus, the number of valid assignments is 0.</li>
	<li>Query <code>[1,2]</code>: The path from Node 1 to Node 2 consists of one edge (<code>1 &rarr; 2</code>). Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2025/03/23/screenshot-2025-03-24-at-055820.png" style="height: 207px; width: 220px;" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">edges = [[1,2],[1,3],[3,4],[3,5]], queries = [[1,4],[3,4],[2,5]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,1,4]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Query <code>[1,4]</code>: The path from Node 1 to Node 4 consists of two edges (<code>1 &rarr; 3</code> and <code>3 &rarr; 4</code>). Assigning weights (1,2) or (2,1) results in an odd cost. Thus, the number of valid assignments is 2.</li>
	<li>Query <code>[3,4]</code>: The path from Node 3 to Node 4 consists of one edge (<code>3 &rarr; 4</code>). Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.</li>
	<li>Query <code>[2,5]</code>: The path from Node 2 to Node 5 consists of three edges (<code>2 &rarr; 1, 1 &rarr; 3</code>, and <code>3 &rarr; 5</code>). Assigning (1,2,2), (2,1,2), (2,2,1), or (1,1,1) makes the cost odd. Thus, the number of valid assignments is 4.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i] == [u<sub>i</sub>, v<sub>i</sub>]</code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i] == [u<sub>i</sub>, v<sub>i</sub>]</code></li>
	<li><code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code></li>
	<li><code>edges</code> represents a valid tree.</li>
</ul>


## Hints

1. Dynamic programming with states `chainLength` and `sumParity`.

2. Use Lowest Common Ancestor to find the distance between any two nodes quickly in `O(logn)`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the number of ways to assign weights 1 or 2 to the edges on a path between two nodes $u$ and $v$ such that the path sum is odd. Let $k$ be the number of edges on the path. Since assigning weight 2 is equivalent to a modulo 2 cost of 0 and weight 1 is equivalent to a modulo 2 cost of 1, the total path cost is odd if and only if the number of edges with weight 1 is odd. From combinatorics, the number of ways to choose an odd number of items out of $k$ items is $\sum_{i \in \{1, 3, 5, \dots\}} \binom{k}{i} = 2^{k-1}$ for $k \ge 1$, and 0 for $k=0$.

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
    vector<int> assignEdgeWeights(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int n = edges.size() + 1;
        vector<vector<int>> adj(n + 1);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        int LOG = 18;
        vector<vector<int>> up(n + 1, vector<int>(LOG, 0));
        vector<int> depth(n + 1, 0);
        vector<int> q;
        q.push_back(1);
        vector<bool> visited(n + 1, false);
        visited[1] = true;

        int head = 0;
        while (head < q.size()) {
            int u = q[head++];
            for (int v : adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    depth[v] = depth[u] + 1;
                    up[v][0] = u;
                    q.push_back(v);
                }
            }
        }

        for (int i = 1; i < LOG; i++) {
            for (int u = 1; u <= n; u++) {
                up[u][i] = up[up[u][i - 1]][i - 1];
            }
        }

        auto get_lca = [&](int u, int v) {
            if (depth[u] < depth[v]) swap(u, v);
            int diff = depth[u] - depth[v];
            for (int i = 0; i < LOG; i++) {
                if ((diff >> i) & 1) u = up[u][i];
            }
            if (u == v) return u;
            for (int i = LOG - 1; i >= 0; i--) {
                if (up[u][i] != up[v][i]) {
                    u = up[u][i];
                    v = up[v][i];
                }
            }
            return up[u][0];
        };

        const int MOD = 1000000007;
        vector<int> pow2(n + 1);
        pow2[0] = 1;
        for (int i = 1; i <= n; i++) {
            pow2[i] = (int)((pow2[i - 1] * 2LL) % MOD);
        }

        vector<int> results;
        results.reserve(queries.size());
        for (const auto& query : queries) {
            int u = query[0], v = query[1];
            if (u == v) {
                results.push_back(0);
                continue;
            }
            int l = get_lca(u, v);
            int dist = depth[u] + depth[v] - 2 * depth[l];
            results.push_back(pow2[dist - 1]);
        }
        return results;
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
    public int[] assignEdgeWeights(int[][] edges, int[][] queries) {
        int n = edges.length + 1;
        List<Integer>[] adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();
        for (int[] edge : edges) {
            adj[edge[0]].add(edge[1]);
            adj[edge[1]].add(edge[0]);
        }

        int LOG = 18;
        int[][] up = new int[n + 1][LOG];
        int[] depth = new int[n + 1];
        int[] q = new int[n];
        boolean[] visited = new boolean[n + 1];

        int head = 0, tail = 0;
        q[tail++] = 1;
        visited[1] = true;
        while (head < tail) {
            int u = q[head++];
            for (int v : adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    depth[v] = depth[u] + 1;
                    up[v][0] = u;
                    q[tail++] = v;
                }
            }
        }

        for (int i = 1; i < LOG; i++) {
            for (int u = 1; u <= n; u++) {
                up[u][i] = up[up[u][i - 1]][i - 1];
            }
        }

        int MOD = 1000000007;
        int[] pow2 = new int[n + 1];
        pow2[0] = 1;
        for (int i = 1; i <= n; i++) pow2[i] = (int)((pow2[i - 1] * 2L) % MOD);

        int[] results = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int u = queries[i][0];
            int v = queries[i][1];
            if (u == v) {
                results[i] = 0;
                continue;
            }
            int l = getLCA(u, v, up, depth, LOG);
            int dist = depth[u] + depth[v] - 2 * depth[l];
            results[i] = pow2[dist - 1];
        }
        return results;
    }

    private int getLCA(int u, int v, int[][] up, int[] depth, int LOG) {
        if (depth[u] < depth[v]) { int tmp = u; u = v; v = tmp; }
        int diff = depth[u] - depth[v];
        for (int i = 0; i < LOG; i++) if (((diff >> i) & 1) == 1) u = up[u][i];
        if (u == v) return u;
        for (int i = LOG - 1; i >= 0; i--) {
            if (up[u][i] != up[v][i]) {
                u = up[u][i];
                v = up[v][i];
            }
        }
        return up[u][0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = 18
        up = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)
        stack = [1]
        visited = [False] * (n + 1)
        visited[1] = True
        up0 = up[0]

        while stack:
            u = stack.pop()
            du = depth[u]
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    up0[v] = u
                    depth[v] = du + 1
                    stack.append(v)

        for i in range(1, LOG):
            upi = up[i]
            up_prev = up[i-1]
            for u in range(1, n + 1):
                upi[u] = up_prev[up_prev[u]]

        MOD = 10**9 + 7
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD

        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
            ou, ov = u, v
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1: u = up[i][u]
            if u == v:
                lca = u
            else:
                for i in range(LOG - 1, -1, -1):
                    upi = up[i]
                    if upi[u] != upi[v]:
                        u, v = upi[u], upi[v]
                lca = up0[u]
            dist = depth[ou] + depth[ov] - 2 * depth[lca]
            ans.append(pow2[dist - 1])
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = 18
        depth = [0] * (n + 1)
        up = [[0] * (n + 1) for _ in range(LOG)]

        queue = collections.deque([1])
        visited = [False] * (n + 1)
        visited[1] = True
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    up[0][v] = u
                    queue.append(v)

        for j in range(1, LOG):
            up_j = up[j]
            up_prev = up[j-1]
            for i in range(1, n + 1):
                up_j[i] = up_prev[up_prev[i]]

        MOD = 1000000007
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD

        res = []
        for original_u, original_v in queries:
            u, v = original_u, original_v
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[i][u]
            if u == v:
                lca = u
            else:
                for i in range(LOG - 1, -1, -1):
                    if up[i][u] != up[i][v]:
                        u = up[i][u]
                        v = up[i][v]
                lca = up[0][u]

            dist = depth[original_u] + depth[original_v] - 2 * depth[lca]
            if dist == 0:
                res.append(0)
            else:
                res.append(pow2[dist-1])
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

int* assignEdgeWeights(int** edges, int edgesSize, int* edgesColSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int n = edgesSize + 1;
    int* head = (int*)malloc(sizeof(int) * (n + 1));
    for (int i = 0; i <= n; i++) head[i] = -1;
    int* to = (int*)malloc(sizeof(int) * (2 * n));
    int* next = (int*)malloc(sizeof(int) * (2 * n));
    int edgeCount = 0;
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0];
        int v = edges[i][1];
        to[edgeCount] = v; next[edgeCount] = head[u]; head[u] = edgeCount++;
        to[edgeCount] = u; next[edgeCount] = head[v]; head[v] = edgeCount++;
    }

    int* depth = (int*)malloc(sizeof(int) * (n + 1));
    int* up = (int*)calloc(18 * (n + 1), sizeof(int));
    int* queue = (int*)malloc(sizeof(int) * (n + 1));
    int head_q = 0, tail_q = 0;
    int* visited = (int*)calloc(n + 1, sizeof(int));

    queue[tail_q++] = 1;
    visited[1] = 1;
    depth[1] = 0;
    while (head_q < tail_q) {
        int u = queue[head_q++];
        for (int i = head[u]; i != -1; i = next[i]) {
            int v = to[i];
            if (!visited[v]) {
                visited[v] = 1;
                depth[v] = depth[u] + 1;
                up[0 * (n + 1) + v] = u;
                queue[tail_q++] = v;
            }
        }
    }

    for (int j = 1; j < 18; j++) {
        for (int i = 1; i <= n; i++) {
            int prev = up[(j - 1) * (n + 1) + i];
            up[j * (n + 1) + i] = up[(j - 1) * (n + 1) + prev];
        }
    }

    long long* pow2 = (long long*)malloc(sizeof(long long) * (n + 1));
    pow2[0] = 1;
    for (int i = 1; i <= n; i++) pow2[i] = (pow2[i - 1] * 2) % 1000000007;

    int* result = (int*)malloc(sizeof(int) * queriesSize);
    for (int k = 0; k < queriesSize; k++) {
        int u0 = queries[k][0], v0 = queries[k][1];
        int u = u0, v = v0;
        if (depth[u] < depth[v]) { int temp = u; u = v; v = temp; }
        int diff = depth[u] - depth[v];
        for (int i = 0; i < 18; i++) if ((diff >> i) & 1) u = up[i * (n + 1) + u];
        int lca;
        if (u == v) lca = u;
        else {
            for (int i = 17; i >= 0; i--) {
                if (up[i * (n + 1) + u] != up[i * (n + 1) + v]) {
                    u = up[i * (n + 1) + u];
                    v = up[i * (n + 1) + v];
                }
            }
            lca = up[0 * (n + 1) + u];
        }
        int dist = depth[u0] + depth[v0] - 2 * depth[lca];
        result[k] = (dist == 0) ? 0 : (int)pow2[dist - 1];
    }

    free(head); free(to); free(next); free(depth); free(up); free(queue); free(visited); free(pow2);
    *returnSize = queriesSize;
    return result;
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
    public int[] AssignEdgeWeights(int[][] edges, int[][] queries) {
        int n = edges.Length + 1;
        List<int>[] adj = new List<int>[n + 1];
        for (int i = 1; i <= n; i++) adj[i] = new List<int>();
        foreach (var edge in edges) {
            adj[edge[0]].Add(edge[1]);
            adj[edge[1]].Add(edge[0]);
        }

        int[,] up = new int[18, n + 1];
        int[] depth = new int[n + 1];
        bool[] visited = new bool[n + 1];
        Queue<int> queue = new Queue<int>();

        queue.Enqueue(1);
        visited[1] = true;
        depth[1] = 0;
        while (queue.Count > 0) {
            int u = queue.Dequeue();
            foreach (int v in adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    depth[v] = depth[u] + 1;
                    up[0, v] = u;
                    queue.Enqueue(v);
                }
            }
        }

        for (int j = 1; j < 18; j++) {
            for (int i = 1; i <= n; i++) {
                up[j, i] = up[j - 1, up[j - 1, i]];
            }
        }

        int MOD = 1000000007;
        long[] pow2 = new long[n + 1];
        pow2[0] = 1;
        for (int i = 1; i <= n; i++) pow2[i] = (pow2[i - 1] * 2) % MOD;

        int[] result = new int[queries.Length];
        for (int k = 0; k < queries.Length; k++) {
            int u0 = queries[k][0], v0 = queries[k][1];
            int u = u0, v = v0;
            if (depth[u] < depth[v]) { int temp = u; u = v; v = temp; }
            int diff = depth[u] - depth[v];
            for (int i = 0; i < 18; i++) if (((diff >> i) & 1) == 1) u = up[i, u];
            int lca;
            if (u == v) lca = u;
            else {
                for (int i = 17; i >= 0; i--) {
                    if (up[i, u] != up[i, v]) {
                        u = up[i, u];
                        v = up[i, v];
                    }
                }
                lca = up[0, u];
            }
            int dist = depth[u0] + depth[v0] - 2 * depth[lca];
            result[k] = (dist == 0) ? 0 : (int)pow2[dist - 1];
        }
        return result;
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
 * @param {number[][]} queries
 * @return {number[]}
 */
var assignEdgeWeights = function(edges, queries) {
    const n = edges.length + 1;
    const adj = Array.from({ length: n + 1 }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const up = new Int32Array(18 * (n + 1));
    const depth = new Int32Array(n + 1);
    const visited = new Uint8Array(n + 1);
    const queue = new Int32Array(n);
    let headPtr = 0, tailPtr = 0;

    queue[tailPtr++] = 1;
    visited[1] = 1;
    depth[1] = 0;
    while (headPtr < tailPtr) {
        const u = queue[headPtr++];
        const neighbors = adj[u];
        for (let i = 0; i < neighbors.length; i++) {
            const v = neighbors[i];
            if (!visited[v]) {
                visited[v] = 1;
                depth[v] = depth[u] + 1;
                up[0 * (n + 1) + v] = u;
                queue[tailPtr++] = v;
            }
        }
    }

    for (let j = 1; j < 18; j++) {
        for (let i = 1; i <= n; i++) {
            const prev = up[(j - 1) * (n + 1) + i];
            up[j * (n + 1) + i] = up[(j - 1) * (n + 1) + prev];
        }
    }

    const MOD = 1000000007;
    const pow2 = new Int32Array(n + 1);
    pow2[0] = 1;
    for (let i = 1; i <= n; i++) pow2[i] = (pow2[i - 1] * 2) % MOD;

    const result = new Int32Array(queries.length);
    for (let k = 0; k < queries.length; k++) {
        const u0 = queries[k][0], v0 = queries[k][1];
        let u = u0, v = v0;
        if (depth[u] < depth[v]) { let t = u; u = v; v = t; }
        const diff = depth[u] - depth[v];
        for (let i = 0; i < 18; i++) if ((diff >> i) & 1) u = up[i * (n + 1) + u];
        let lca;
        if (u === v) lca = u;
        else {
            for (let i = 17; i >= 0; i--) {
                if (up[i * (n + 1) + u] !== up[i * (n + 1) + v]) {
                    u = up[i * (n + 1) + u];
                    v = up[i * (n + 1) + v];
                }
            }
            lca = up[0 * (n + 1) + u];
        }
        const dist = depth[u0] + depth[v0] - 2 * depth[lca];
        result[k] = (dist === 0) ? 0 : pow2[dist - 1];
    }
    return Array.from(result);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function assignEdgeWeights(edges: number[][], queries: number[][]): number[] {
    const n = edges.length + 1;
    const maxLog = 17;
    const head = new Int32Array(n + 1).fill(-1);
    const next = new Int32Array(2 * n);
    const to = new Int32Array(2 * n);
    let edgeCount = 0;

    for (const [u, v] of edges) {
        to[edgeCount] = v;
        next[edgeCount] = head[u];
        head[u] = edgeCount++;
        to[edgeCount] = u;
        next[edgeCount] = head[v];
        head[v] = edgeCount++;
    }

    const depth = new Int32Array(n + 1);
    const up = Array.from({ length: n + 1 }, () => new Int32Array(maxLog + 1));
    const visited = new Uint8Array(n + 1);

    const queue = new Int32Array(n);
    let headQ = 0;
    let tailQ = 0;

    queue[tailQ++] = 1;
    visited[1] = 1;
    depth[1] = 0;

    while (headQ < tailQ) {
        const u = queue[headQ++];
        for (let e = head[u]; e !== -1; e = next[e]) {
            const v = to[e];
            if (!visited[v]) {
                visited[v] = 1;
                depth[v] = depth[u] + 1;
                up[v][0] = u;
                queue[tailQ++] = v;
            }
        }
    }

    for (let i = 1; i <= maxLog; i++) {
        for (let u = 1; u <= n; u++) {
            up[u][i] = up[up[u][i - 1]][i - 1];
        }
    }

    const MOD = 1000000007;
    const pow2 = new Int32Array(n + 1);
    pow2[0] = 1;
    for (let i = 1; i <= n; i++) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }

    const results: number[] = [];
    for (const [uOrig, vOrig] of queries) {
        let u = uOrig;
        let v = vOrig;
        if (depth[u] < depth[v]) {
            [u, v] = [v, u];
        }

        for (let i = maxLog; i >= 0; i--) {
            if (depth[u] - (1 << i) >= depth[v]) {
                u = up[u][i];
            }
        }

        let lca = u;
        if (u !== v) {
            for (let i = maxLog; i >= 0; i--) {
                if (up[u][i] !== up[v][i]) {
                    u = up[u][i];
                    v = up[v][i];
                }
            }
            lca = up[u][0];
        }

        const dist = depth[uOrig] + depth[vOrig] - 2 * depth[lca];
        results.push(dist === 0 ? 0 : pow2[dist - 1]);
    }

    return results;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[][] $edges
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function assignEdgeWeights($edges, $queries) {
        $n = count($edges) + 1;
        $maxLog = 17;
        $logStep = $maxLog + 1;
        $MOD = 1000000007;

        $head = new SplFixedArray($n + 1);
        for ($i = 0; $i <= $n; $i++) $head[$i] = -1;
        $next = new SplFixedArray(2 * $n);
        $to = new SplFixedArray(2 * $n);
        $edgeCount = 0;

        foreach ($edges as $edge) {
            $u = $edge[0]; $v = $edge[1];
            $to[$edgeCount] = $v;
            $next[$edgeCount] = $head[$u];
            $head[$u] = $edgeCount++;
            $to[$edgeCount] = $u;
            $next[$edgeCount] = $head[$v];
            $head[$v] = $edgeCount++;
        }

        $depth = new SplFixedArray($n + 1);
        $up = new SplFixedArray(($n + 1) * $logStep);
        for ($i = 0; $i < ($n + 1) * $logStep; $i++) $up[$i] = 0;
        $visited = new SplFixedArray($n + 1);
        for ($i = 0; $i <= $n; $i++) $visited[$i] = false;

        $queue = new SplQueue();
        $queue->enqueue(1);
        $visited[1] = true;
        $depth[1] = 0;

        while (!$queue->isEmpty()) {
            $u = $queue->dequeue();
            for ($e = $head[$u]; $e != -1; $e = $next[$e]) {
                $v = $to[$e];
                if (!$visited[$v]) {
                    $visited[$v] = true;
                    $depth[$v] = $depth[$u] + 1;
                    $up[$v * $logStep] = $u;
                    $queue->enqueue($v);
                }
            }
        }

        for ($i = 1; $i <= $maxLog; $i++) {
            for ($u = 1; $u <= $n; $u++) {
                $up[$u * $logStep + $i] = $up[$up[$u * $logStep + $i - 1] * $logStep + $i - 1];
            }
        }

        $pow2 = new SplFixedArray($n + 1);
        $pow2[0] = 1;
        for ($i = 1; $i <= $n; $i++) {
            $pow2[$i] = ($pow2[$i - 1] * 2) % $MOD;
        }

        $results = [];
        foreach ($queries as $query) {
            $uOrig = $query[0];
            $vOrig = $query[1];
            $u = $uOrig;
            $v = $vOrig;

            if ($depth[$u] < $depth[$v]) {
                $tmp = $u; $u = $v; $v = $tmp;
            }

            for ($i = $maxLog; $i >= 0; $i--) {
                if ($depth[$u] - (1 << $i) >= $depth[$v]) {
                    $u = $up[$u * $logStep + $i];
                }
            }

            $lca = $u;
            if ($u != $v) {
                for ($i = $maxLog; $i >= 0; $i--) {
                    if ($up[$u * $logStep + $i] != $up[$v * $logStep + $i]) {
                        $u = $up[$u * $logStep + $i];
                        $v = $up[$v * $logStep + $i];
                    }
                }
                $lca = $up[$u * $logStep];
            }

            $dist = $depth[$uOrig] + $depth[$vOrig] - 2 * $depth[$lca];
            $results[] = ($dist == 0) ? 0 : $pow2[$dist - 1];
        }

        return $results;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func assignEdgeWeights(_ edges: [[Int]], _ queries: [[Int]]) -> [Int] {
        let n = edges.count + 1
        var head = [Int](repeating: -1, count: n + 1)
        var next = [Int](repeating: -1, count: 2 * n)
        var to = [Int](repeating: 0, count: 2 * n)
        var edgeCount = 0

        for edge in edges {
            let u = edge[0], v = edge[1]
            to[edgeCount] = v
            next[edgeCount] = head[u]
            head[u] = edgeCount
            edgeCount += 1

            to[edgeCount] = u
            next[edgeCount] = head[v]
            head[v] = edgeCount
            edgeCount += 1
        }

        let maxLog = 17
        var depth = [Int](repeating: 0, count: n + 1)
        var up = Array(repeating: Array(repeating: 0, count: maxLog + 1), count: n + 1)
        var visited = [Bool](repeating: false, count: n + 1)

        var queue = [Int]()
        queue.reserveCapacity(n)
        queue.append(1)
        var qHead = 0
        visited[1] = true
        depth[1] = 0

        while qHead < queue.count {
            let u = queue[qHead]
            qHead += 1

            var e = head[u]
            while e != -1 {
                let v = to[e]
                if !visited[v] {
                    visited[v] = true
                    depth[v] = depth[u] + 1
                    up[v][0] = u
                    queue.append(v)
                }
                e = next[e]
            }
        }

        for i in 1...maxLog {
            for u in 1...n {
                up[u][i] = up[up[u][i-1]][i-1]
            }
        }

        let mod = 1_000_000_007
        var pow2 = [Int](repeating: 0, count: n + 1)
        pow2[0] = 1
        if n >= 1 {
            for i in 1...n {
                pow2[i] = (pow2[i-1] * 2) % mod
            }
        }

        var results = [Int]()
        results.reserveCapacity(queries.count)
        for query in queries {
            let uOrig = query[0], vOrig = query[1]
            var u = uOrig, v = vOrig

            if depth[u] < depth[v] {
                let tmp = u; u = v; v = tmp
            }

            for i in stride(from: maxLog, through: 0, by: -1) {
                if depth[u] - (1 << i) >= depth[v] {
                    u = up[u][i]
                }
            }

            var lca = u
            if u != v {
                for i in stride(from: maxLog, through: 0, by: -1) {
                    if up[u][i] != up[v][i] {
                        u = up[u][i]
                        v = up[v][i]
                    }
                }
                lca = up[u][0]
            }

            let dist = depth[uOrig] + depth[vOrig] - 2 * depth[lca]
            results.append(dist == 0 ? 0 : pow2[dist - 1])
        }

        return results
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
    fun assignEdgeWeights(edges: Array<IntArray>, queries: Array<IntArray>): IntArray {
        val n = edges.size + 1
        val head = IntArray(n + 1) { -1 }
        val next = IntArray(2 * n)
        val to = IntArray(2 * n)
        var edgeCount = 0

        for (edge in edges) {
            val u = edge[0]
            val v = edge[1]
            to[edgeCount] = v
            next[edgeCount] = head[u]
            head[u] = edgeCount++
            to[edgeCount] = u
            next[edgeCount] = head[v]
            head[v] = edgeCount++
        }

        val maxLog = 17
        val depth = IntArray(n + 1)
        val up = Array(n + 1) { IntArray(maxLog + 1) }
        val queue: Deque<Int> = ArrayDeque()
        val visited = BooleanArray(n + 1)

        queue.add(1)
        visited[1] = true
        depth[1] = 0

        while (queue.isNotEmpty()) {
            val u = queue.poll()
            var e = head[u]
            while (e != -1) {
                val v = to[e]
                if (!visited[v]) {
                    visited[v] = true
                    depth[v] = depth[u] + 1
                    up[v][0] = u
                    queue.add(v)
                }
                e = next[e]
            }
        }

        for (i in 1..maxLog) {
            for (u in 1..n) {
                up[u][i] = up[up[u][i - 1]][i - 1]
            }
        }

        val mod = 1000000007
        val pow2 = IntArray(n + 1)
        pow2[0] = 1
        for (i in 1..n) {
            pow2[i] = ((pow2[i - 1].toLong() * 2) % mod).toInt()
        }

        val results = IntArray(queries.size)
        for (i in queries.indices) {
            val uOrig = queries[i][0]
            val vOrig = queries[i][1]
            var u = uOrig
            var v = vOrig

            if (depth[u] < depth[v]) {
                val tmp = u
                u = v
                v = tmp
            }

            for (j in maxLog downTo 0) {
                if (depth[u] - (1 shl j) >= depth[v]) {
                    u = up[u][j]
                }
            }

            var lca = u
            if (u != v) {
                for (j in maxLog downTo 0) {
                    if (up[u][j] != up[v][j]) {
                        u = up[u][j]
                        v = up[v][j]
                    }
                }
                lca = up[u][0]
            }

            val dist = depth[uOrig] + depth[vOrig] - 2 * depth[lca]
            results[i] = if (dist == 0) 0 else pow2[dist - 1]
        }

        return results
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:typed_data';

class Solution {
  List<int> assignEdgeWeights(List<List<int>> edges, List<List<int>> queries) {
    int n = edges.length + 1;
    List<List<int>> adj = List.generate(n + 1, (_) => []);
    for (var edge in edges) {
      adj[edge[0]].add(edge[1]);
      adj[edge[1]].add(edge[0]);
    }

    Int32List depth = Int32List(n + 1);
    List<Int32List> up = List.generate(18, (_) => Int32List(n + 1));
    List<bool> visited = List.filled(n + 1, false);

    List<int> queue = [1];
    visited[1] = true;
    depth[1] = 0;
    int head = 0;
    while (head < queue.length) {
      int u = queue[head++];
      for (int v in adj[u]) {
        if (!visited[v]) {
          visited[v] = true;
          depth[v] = depth[u] + 1;
          up[0][v] = u;
          queue.add(v);
        }
      }
    }

    for (int i = 1; i < 18; i++) {
      for (int j = 1; j <= n; j++) {
        up[i][j] = up[i - 1][up[i - 1][j]];
      }
    }

    const int mod = 1000000007;
    Int32List pow2 = Int32List(n + 1);
    pow2[0] = 1;
    for (int i = 1; i <= n; i++) {
      pow2[i] = (pow2[i - 1] * 2) % mod;
    }

    List<int> results = [];
    for (var query in queries) {
      int u = query[0];
      int v = query[1];
      int uOrig = u;
      int vOrig = v;

      if (depth[u] < depth[v]) {
        int temp = u;
        u = v;
        v = temp;
      }
      int diff = depth[u] - depth[v];
      for (int i = 0; i < 18; i++) {
        if ((diff >> i) & 1 == 1) {
          u = up[i][u];
        }
      }

      int lca;
      if (u == v) {
        lca = u;
      } else {
        for (int i = 17; i >= 0; i--) {
          if (up[i][u] != up[i][v]) {
            u = up[i][u];
            v = up[i][v];
          }
        }
        lca = up[0][u];
      }

      int dist = depth[uOrig] + depth[vOrig] - 2 * depth[lca];
      results.add(dist == 0 ? 0 : pow2[dist - 1]);
    }
    return results;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func assignEdgeWeights(edges [][]int, queries [][]int) []int {
	n := len(edges) + 1
	adj := make([][]int, n+1)
	for _, edge := range edges {
		u, v := edge[0], edge[1]
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}

	depth := make([]int, n+1)
	up := make([][]int, 18)
	for i := range up {
		up[i] = make([]int, n+1)
	}
	visited := make([]bool, n+1)

	queue := []int{1}
	visited[1] = true
	depth[1] = 0
	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]
		for _, v := range adj[u] {
			if !visited[v] {
				visited[v] = true
				depth[v] = depth[u] + 1
				up[0][v] = u
				queue = append(queue, v)
			}
		}
	}

	for i := 1; i < 18; i++ {
		for j := 1; j <= n; j++ {
			up[i][j] = up[i-1][up[i-1][j]]
		}
	}

	mod := 1000000007
	pow2 := make([]int, n+1)
	pow2[0] = 1
	for i := 1; i <= n; i++ {
		pow2[i] = (pow2[i-1] * 2) % mod
	}

	results := make([]int, len(queries))
	for i, query := range queries {
		u, v := query[0], query[1]
		uOrig, vOrig := u, v

		if depth[u] < depth[v] {
			u, v = v, u
		}
		diff := depth[u] - depth[v]
		for j := 0; j < 18; j++ {
			if (diff>>j)&1 == 1 {
				u = up[j][u]
			}
		}

		lca := 0
		if u == v {
			lca = u
		} else {
			for j := 17; j >= 0; j-- {
				if up[j][u] != up[j][v] {
					u = up[j][u]
					v = up[j][v]
				}
			}
			lca = up[0][u]
		}

		dist := depth[uOrig] + depth[vOrig] - 2*depth[lca]
		if dist == 0 {
			results[i] = 0
		} else {
			results[i] = pow2[dist-1]
		}
	}
	return results
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def assign_edge_weights(edges, queries)
  n = edges.length + 1
  adj = Array.new(n + 1) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  depth = Array.new(n + 1, 0)
  up = Array.new(18) { Array.new(n + 1, 0) }
  visited = Array.new(n + 1, false)
  queue = [1]
  visited[1] = true
  depth[1] = 0

  head = 0
  while head < queue.length
    u = queue[head]
    head += 1
    adj[u].each do |v|
      if !visited[v]
        visited[v] = true
        depth[v] = depth[u] + 1
        up[0][v] = u
        queue << v
      end
    end
  end

  (1..17).each do |i|
    up_i = up[i]
    up_prev = up[i - 1]
    (1..n).each do |j|
      up_i[j] = up_prev[up_prev[j]]
    end
  end

  mod = 1_000_000_007
  pow2 = Array.new(n + 1)
  pow2[0] = 1
  (1..n).each { |i| pow2[i] = (pow2[i - 1] * 2) % mod }

  ans = Array.new(queries.length)
  idx = 0
  while idx < queries.length
    u = queries[idx][0]
    v = queries[idx][1]
    u_orig, v_orig = u, v

    if depth[u] < depth[v]
      u, v = v, u
    end
    diff = depth[u] - depth[v]
    18.times { |i| u = up[i][u] if diff[i] == 1 }

    if u == v
      lca = u
    else
      i = 17
      while i >= 0
        if up[i][u] != up[i][v]
          u = up[i][u]
          v = up[i][v]
        end
        i -= 1
      end
      lca = up[0][u]
    end

    dist = depth[u_orig] + depth[v_orig] - 2 * depth[lca]
    ans[idx] = (dist == 0 ? 0 : pow2[dist - 1])
    idx += 1
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
  def assignEdgeWeights(edges: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val n = edges.length + 1
    val adj = Array.fill(n + 1)(mutable.ArrayBuffer.empty[Int])
    for (edge <- edges) {
      adj(edge(0)) += edge(1)
      adj(edge(1)) += edge(0)
    }

    val depth = new Array[Int](n + 1)
    val up = Array.ofDim[Int](18, n + 1)
    val visited = new Array[Boolean](n + 1)

    val queue = mutable.Queue[Int]()
    queue.enqueue(1)
    visited(1) = true
    depth(1) = 0

    while (queue.nonEmpty) {
      val u = queue.dequeue()
      for (v <- adj(u)) {
        if (!visited(v)) {
          visited(v) = true
          depth(v) = depth(u) + 1
          up(0)(v) = u
          queue.enqueue(v)
        }
      }
    }

    for (i <- 1 until 18) {
      for (j <- 1 to n) {
        up(i)(j) = up(i - 1)(up(i - 1)(j))
      }
    }

    val mod = 1000000007
    val pow2 = new Array[Int](n + 1)
    pow2(0) = 1
    for (i <- 1 to n) {
      pow2(i) = ((pow2(i - 1).toLong * 2) % mod).toInt
    }

    val results = new Array[Int](queries.length)
    for (idx <- queries.indices) {
      val uOrig = queries(idx)(0)
      val vOrig = queries(idx)(1)
      var u = uOrig
      var v = vOrig

      if (depth(u) < depth(v)) {
        val temp = u
        u = v
        v = temp
      }
      val diff = depth(u) - depth(v)
      for (i <- 0 until 18) {
        if (((diff >> i) & 1) == 1) {
          u = up(i)(u)
        }
      }

      val lca = if (u == v) u else {
        var i = 17
        while (i >= 0) {
          if (up(i)(u) != up(i)(v)) {
            u = up(i)(u)
            v = up(i)(v)
          }
          i -= 1
        }
        up(0)(u)
      }

      val dist = depth(uOrig) + depth(vOrig) - 2 * depth(lca)
      results(idx) = if (dist == 0) 0 else pow2(dist - 1)
    }
    results
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn assign_edge_weights(edges: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = edges.len() + 1;
        let mut adj = vec![vec![]; n + 1];
        for e in edges {
            let u = e[0] as usize;
            let v = e[1] as usize;
            adj[u].push(v);
            adj[v].push(u);
        }

        let mut depth = vec![0; n + 1];
        let mut up = vec![vec![0; 18]; n + 1];
        let mut visited = vec![false; n + 1];
        let mut queue = std::collections::VecDeque::new();

        queue.push_back(1);
        visited[1] = true;
        up[1][0] = 1;

        while let Some(u) = queue.pop_front() {
            for &v in &adj[u] {
                if !visited[v] {
                    visited[v] = true;
                    depth[v] = depth[u] + 1;
                    up[v][0] = u;
                    queue.push_back(v);
                }
            }
        }

        for i in 1..18 {
            for u in 1..=n {
                up[u][i] = up[up[u][i - 1]][i - 1];
            }
        }

        let mut pow2 = vec![1; n + 1];
        let mod_val = 1_000_000_007;
        for i in 1..=n {
            pow2[i] = (pow2[i - 1] * 2) % mod_val;
        }

        queries.iter().map(|q| {
            let mut u = q[0] as usize;
            let mut v = q[1] as usize;
            if u == v { return 0; }
            let (original_u, original_v) = (u, v);

            if depth[u] < depth[v] { std::mem::swap(&mut u, &mut v); }
            let diff = depth[u] - depth[v];
            for i in 0..18 {
                if (diff >> i) & 1 == 1 {
                    u = up[u][i];
                }
            }

            let lca = if u == v {
                u
            } else {
                for i in (0..18).rev() {
                    if up[u][i] != up[v][i] {
                        u = up[u][i];
                        v = up[v][i];
                    }
                }
                up[u][0]
            };

            let dist = depth[original_u] + depth[original_v] - 2 * depth[lca];
            pow2[dist - 1] as i32
        }).collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (assign-edge-weights edges queries)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([n (+ (length edges) 1)]
         [adj (make-vector (+ n 1) '())])
    (for ([e edges])
      (let ([u (first e)] [v (second e)])
        (vector-set! adj u (cons v (vector-ref adj u)))
        (vector-set! adj v (cons u (vector-ref adj v)))))

    (define depth (make-vector (+ n 1) 0))
    (define up (make-vector 18))
    (for ([i 18]) (vector-set! up i (make-vector (+ n 1) 0)))

    (define visited (make-vector (+ n 1) #f))
    (vector-set! visited 1 #t)
    (vector-set! (vector-ref up 0) 1 1)
    (let loop-q ([q-in '()] [q-out (list 1)])
      (cond
        [(and (null? q-in) (null? q-out)) (void)]
        [(null? q-out) (loop-q '() (reverse q-in))]
        [else
         (let* ([u (car q-out)]
                [neighbors (vector-ref adj u)]
                [next-in (foldl (lambda (v acc)
                                  (if (vector-ref visited v)
                                      acc
                                      (begin
                                        (vector-set! visited v #t)
                                        (vector-set! depth v (+ (vector-ref depth u) 1))
                                        (vector-set! (vector-ref up 0) v u)
                                        (cons v acc))))
                                q-in neighbors)])
           (loop-q next-in (cdr q-out)))]))

    (for ([i (in-range 1 18)])
      (let ([prev-up (vector-ref up (- i 1))]
            [curr-up (vector-ref up i)])
        (for ([u (in-range 1 (+ n 1))])
          (vector-set! curr-up u (vector-ref prev-up (vector-ref prev-up u))))))

    (define (get-lca u v)
      (let* ([du (vector-ref depth u)]
             [dv (vector-ref depth v)]
             [u-ref (if (< du dv) v u)]
             [v-ref (if (< du dv) u v)]
             [diff (- (vector-ref depth u-ref) (vector-ref depth v-ref))])
        (let loop-u ([u u-ref] [i 17])
          (if (>= i 0)
              (if (bitwise-bit-set? diff i)
                  (loop-u (vector-ref (vector-ref up i) u) (- i 1))
                  (loop-u u (- i 1)))
              (if (= u v-ref) u
                  (let loop-uv ([u u] [v v-ref] [i 17])
                    (if (>= i 0)
                        (let ([ui (vector-ref (vector-ref up i) u)]
                              [vi (vector-ref (vector-ref up i) v)])
                          (if (not (= ui vi))
                              (loop-uv ui vi (- i 1))
                              (loop-uv u v (- i 1))))
                        (vector-ref (vector-ref up 0) u))))))))

    (define pow2 (make-vector (+ n 1) 1))
    (for ([i (in-range 1 (+ n 1))])
      (vector-set! pow2 i (modulo (* (vector-ref pow2 (- i 1)) 2) 1000000007)))

    (map (lambda (query)
           (let ([u (first query)] [v (second query)])
             (if (= u v) 0
                 (let* ([lca (get-lca u v)]
                        [dist (- (+ (vector-ref depth u) (vector-ref depth v)) (* 2 (vector-ref depth lca)))])
                   (vector-ref pow2 (- dist 1))))))
         queries)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec assign_edge_weights(Edges :: [[integer()]], Queries :: [[integer()]]) -> [integer()].
assign_edge_weights(Edges, Queries) ->
    N = length(Edges) + 1,
    Adj = lists:foldl(fun([U, V], Acc) ->
        Acc1 = maps:put(U, [V | maps:get(U, Acc, [])], Acc),
        maps:put(V, [U | maps:get(V, Acc, [])], Acc1)
    end, #{}, Edges),

    {Depths, Parents} = bfs([1], #{1 => true}, #{1 => 0}, #{1 => 1}, Adj),

    Up0 = list_to_tuple([if I == 0 -> 0; true -> maps:get(I, Parents, 1) end || I <- lists:seq(0, N)]),
    Up = compute_up_table(Up0, 1, [Up0], N),

    DepthTuple = list_to_tuple([if I == 0 -> 0; true -> maps:get(I, Depths, 0) end || I <- lists:seq(0, N)]),

    Pow2 = list_to_tuple(compute_pow2_list(N)),

    [begin
        [U, V] = Q,
        if U == V -> 0;
           true ->
               LCA = get_lca(U, V, Up, DepthTuple),
               Dist = element(U+1, DepthTuple) + element(V+1, DepthTuple) - 2 * element(LCA+1, DepthTuple),
               element(Dist, Pow2)
        end
     end || Q <- Queries].

bfs([], _Visited, Depths, Parents, _Adj) -> {Depths, Parents};
bfs(Level, Visited, Depths, Parents, Adj) ->
    {NextLevel, NewVisited, NewDepths, NewParents} = 
        lists:foldl(fun(U, {L_acc, V_acc, D_acc, P_acc}) ->
            Neighbors = maps:get(U, Adj, []),
            lists:foldl(fun(V, {L_in, V_in, D_in, P_in}) ->
                case maps:is_key(V, V_in) of
                    false -> {[V | L_in], V_in#{V => true}, D_in#{V => maps:get(U, D_in) + 1}, P_in#{V => U}};
                    true -> {L_in, V_in, D_in, P_in}
                end
            end, {L_acc, V_acc, D_acc, P_acc}, Neighbors)
        end, {[], Visited, Depths, Parents}, Level),
    bfs(NextLevel, NewVisited, NewDepths, NewParents, Adj).

compute_up_table(_PrevUp, 18, Acc, _N) -> list_to_tuple(lists:reverse(Acc));
compute_up_table(PrevUp, I, Acc, N) ->
    CurrUp = list_to_tuple([if J == 0 -> 0; true -> element(element(J+1, PrevUp)+1, PrevUp) end || J <- lists:seq(0, N)]),
    compute_up_table(CurrUp, I+1, [CurrUp | Acc], N).

get_lca(U, V, Up, DepthTuple) ->
    DU = element(U+1, DepthTuple),
    DV = element(V+1, DepthTuple),
    {U1, V1} = if DU < DV -> {V, U}; true -> {U, V} end,
    Diff = element(U1+1, DepthTuple) - element(V1+1, DepthTuple),
    U2 = lift_up(U1, Diff, Up),
    if U2 == V1 -> U2;
       true -> find_common_ancestor(U2, V1, 17, Up)
    end.

lift_up(U, Diff, Up) ->
    lists:foldl(fun(I, AccU) ->
        if (Diff band (1 bsl I)) =/= 0 ->
            element(AccU+1, element(I+1, Up));
           true -> AccU
        end
    end, U, lists:seq(0, 17)).

find_common_ancestor(U, V, -1, Up) -> element(U+1, element(1, Up));
find_common_ancestor(U, V, I, Up) ->
    UI = element(U+1, element(I+1, Up)),
    VI = element(V+1, element(I+1, Up)),
    if UI =/= VI -> find_common_ancestor(UI, VI, I-1, Up);
       true -> find_common_ancestor(U, V, I-1, Up)
    end.

compute_pow2_list(N) ->
    {List, _} = lists:foldl(fun(_, {Acc, Last}) -> 
        Next = (Last * 2) rem 1000000007,
        {[Next | Acc], Next}
    end, {[1], 1}, lists:seq(1, N)),
    lists:reverse(List).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec assign_edge_weights(edges :: [[integer]], queries :: [[integer]]) :: [integer]
  def assign_edge_weights(edges, queries) do
    n = length(edges) + 1
    adj = Enum.reduce(edges, %{}, fn [u, v], acc ->
      acc
      |> Map.update(u, [v], &[v | &1])
      |> Map.update(v, [u], &[u | &1])
    end)

    {depths, parents} = bfs([1], %{1 => true}, %{1 => 0}, %{1 => 1}, adj)

    up0 = List.to_tuple(for i <- 0..n, do: Map.get(parents, i, 0))
    up = compute_up_table(up0, 1, [up0], n)

    depth_tuple = List.to_tuple(for i <- 0..n, do: Map.get(depths, i, 0))

    pow2 = List.to_tuple(compute_pow2_list(n))

    Enum.map(queries, fn [u, v] ->
      if u == v do
        0
      else
        lca = get_lca(u, v, up, depth_tuple)
        dist = elem(depth_tuple, u) + elem(depth_tuple, v) - 2 * elem(depth_tuple, lca)
        elem(pow2, dist - 1)
      end
    end)
  end

  defp bfs([], _visited, depths, parents, _adj), do: {depths, parents}
  defp bfs(level, visited, depths, parents, adj) do
    {next_level, new_visited, new_depths, new_parents} = 
      Enum.reduce(level, {[], visited, depths, parents}, fn u, {l_acc, v_acc, d_acc, p_acc} ->
        neighbors = Map.get(adj, u, [])
        Enum.reduce(neighbors, {l_acc, v_acc, d_acc, p_acc}, fn v, {l_in, v_in, d_in, p_in} ->
          if Map.has_key?(v_in, v) do
            {l_in, v_in, d_in, p_in}
          else
            {[v | l_in], Map.put(v_in, v, true), Map.put(d_in, v, Map.get(d_in, u) + 1), Map.put(p_in, v, u)}
          end
        end)
      end)
    bfs(next_level, new_visited, new_depths, new_parents, adj)
  end

  defp compute_up_table(_prev_up, 18, acc, _n), do: List.to_tuple(Enum.reverse(acc))
  defp compute_up_table(prev_up, i, acc, n) do
    curr_up = List.to_tuple(for j <- 0..n do
      if j == 0, do: 0, else: elem(prev_up, elem(prev_up, j))
    end)
    compute_up_table(curr_up, i + 1, [curr_up | acc], n)
  end

  defp get_lca(u, v, up, depth_tuple) do
    du = elem(depth_tuple, u)
    dv = elem(depth_tuple, v)
    {u1, v1} = if du < dv, do: {v, u}, else: {u, v}
    diff = elem(depth_tuple, u1) - elem(depth_tuple, v1)
    u2 = lift_up(u1, diff, up)
    if u2 == v1 do
      u2
    else
      find_common_ancestor(u2, v1, 17, up)
    end
  end

  defp lift_up(u, diff, up) do
    use Bitwise
    Enum.reduce(0..17, u, fn i, acc_u ->
      if (diff &&& (1 <<< i)) != 0 do
        elem(elem(up, i), acc_u)
      else
        acc_u
      end
    end)
  end

  defp find_common_ancestor(u, v, -1, up), do: elem(elem(up, 0), u)
  defp find_common_ancestor(u, v, i, up) do
    ui = elem(elem(up, i), u)
    vi = elem(elem(up, i), v)
    if ui != vi do
      find_common_ancestor(ui, vi, i - 1, up)
    else
      find_common_ancestor(u, v, i - 1, up)
    end
  end

  defp compute_pow2_list(n) do
    Enum.reduce(1..n, [1], fn _, [h | _] = acc ->
      [rem(h * 2, 1_000_000_007) | acc]
    end) |> Enum.reverse()
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O((n + q) \log n) where $n$ is the number of nodes and $q$ is the number of queries. Precomputing the tree's depth and the binary lifting table for Lowest Common Ancestor (LCA) takes $O(n \log n)$, and each query is answered in $O(\log n)$ by finding the LCA to calculate the path distance.
- **Space Complexity:** O(n \log n) because we store a binary lifting table of size $(n+1) \times \lceil \log_2 n \rceil$ and an adjacency list for the tree.
