---
layout: post
title: "Maximize Spanning Tree Stability with Upgrades"
date: 2026-03-12 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Binary Search", "Greedy", "Union-Find", "Graph Theory", "Minimum Spanning Tree"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    struct Edge { int u, v, s; };\n    struct\
        \ DSU {\n        vector<int> parent;\n        int components;\n        DSU(int\
        \ n) : parent(n), components(n) {\n            for (int i = 0; i < n; ++i) parent[i]\
        \ = i;\n        }\n        int find(int i) {\n            if (parent[i] == i)\
        \ return i;\n            return parent[i] = find(parent[i]);\n        }\n  \
        \      bool unite(int i, int j) {\n            int root_i = find(i), root_j\
        \ = find(j);\n            if (root_i != root_j) {\n                parent[root_i]\
        \ = root_j;\n                components--;\n                return true;\n \
        \           }\n            return false;\n        }\n    };\n\n    int maxStability(int\
        \ n, vector<vector<int>>& edges, int k) {\n        vector<Edge> e_must, e_opt;\n\
        \        int min_must = 200001;\n        for (const auto& e : edges) {\n   \
        \         if (e[3] == 1) {\n                e_must.push_back({e[0], e[1], e[2]});\n\
        \                min_must = min(min_must, e[2]);\n            } else {\n   \
        \             e_opt.push_back({e[0], e[1], e[2]});\n            }\n        }\n\
        \n        DSU base_dsu(n);\n        for (const auto& e : e_must) {\n       \
        \     if (!base_dsu.unite(e.u, e.v)) return -1;\n        }\n\n        sort(e_opt.begin(),\
        \ e_opt.end(), [](const Edge& a, const Edge& b) {\n            return a.s <\
        \ b.s;\n        });\n\n        auto check = [&](int X) {\n            if (min_must\
        \ < X) return false;\n            DSU dsu = base_dsu;\n            int cost\
        \ = 0;\n            auto it0 = lower_bound(e_opt.begin(), e_opt.end(), X, [](const\
        \ Edge& e, int val) { return e.s < val; });\n            for (auto it = it0;\
        \ it != e_opt.end(); ++it) {\n                dsu.unite(it->u, it->v);\n   \
        \         }\n            auto it1 = lower_bound(e_opt.begin(), it0, (X + 1)\
        \ / 2, [](const Edge& e, int val) { return e.s < val; });\n            for (auto\
        \ it = it1; it != it0; ++it) {\n                if (dsu.unite(it->u, it->v))\
        \ cost++;\n            }\n            return dsu.components == 1 && cost <=\
        \ k;\n        };\n\n        if (!check(1)) return -1;\n\n        int low = 1,\
        \ high = min(200000, min_must), ans = 1;\n        while (low <= high) {\n  \
        \          int mid = low + (high - low) / 2;\n            if (check(mid)) {\n\
        \                ans = mid;\n                low = mid + 1;\n            } else\
        \ {\n                high = mid - 1;\n            }\n        }\n        return\
        \ ans;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    static class Edge {\n    \
        \    int u, v, s;\n        Edge(int u, int v, int s) { this.u = u; this.v =\
        \ v; this.s = s; }\n    }\n\n    static class DSU {\n        int[] parent;\n\
        \        int components;\n        DSU(int n) {\n            parent = new int[n];\n\
        \            for (int i = 0; i < n; i++) parent[i] = i;\n            components\
        \ = n;\n        }\n        DSU(DSU other) {\n            this.parent = other.parent.clone();\n\
        \            this.components = other.components;\n        }\n        int find(int\
        \ i) {\n            if (parent[i] == i) return i;\n            return parent[i]\
        \ = find(parent[i]);\n        }\n        boolean unite(int i, int j) {\n   \
        \         int root_i = find(i), root_j = find(j);\n            if (root_i !=\
        \ root_j) {\n                parent[root_i] = root_j;\n                components--;\n\
        \                return true;\n            }\n            return false;\n  \
        \      }\n    }\n\n    public int maxStability(int n, int[][] edges, int k)\
        \ {\n        List<Edge> e_must = new ArrayList<>(), e_opt = new ArrayList<>();\n\
        \        int min_must = 200001;\n        for (int[] e : edges) {\n         \
        \   if (e[3] == 1) {\n                e_must.add(new Edge(e[0], e[1], e[2]));\n\
        \                min_must = Math.min(min_must, e[2]);\n            } else {\n\
        \                e_opt.add(new Edge(e[0], e[1], e[2]));\n            }\n   \
        \     }\n\n        DSU base_dsu = new DSU(n);\n        for (Edge e : e_must)\
        \ {\n            if (!base_dsu.unite(e.u, e.v)) return -1;\n        }\n\n  \
        \      e_opt.sort(Comparator.comparingInt(e -> e.s));\n        int[] e_opt_s\
        \ = new int[e_opt.size()];\n        for (int i = 0; i < e_opt.size(); i++) e_opt_s[i]\
        \ = e_opt.get(i).s;\n\n        int low = 1, high = Math.min(200000, min_must),\
        \ ans = -1;\n        while (low <= high) {\n            int mid = low + (high\
        \ - low) / 2;\n            if (isValid(mid, n, e_opt, e_opt_s, base_dsu, k,\
        \ min_must)) {\n                ans = mid;\n                low = mid + 1;\n\
        \            } else {\n                high = mid - 1;\n            }\n    \
        \    }\n        return ans;\n    }\n\n    private boolean isValid(int X, int\
        \ n, List<Edge> e_opt, int[] e_opt_s, DSU base, int k, int min_must) {\n   \
        \     if (min_must < X) return false;\n        DSU dsu = new DSU(base);\n  \
        \      int idx0 = lowerBound(e_opt_s, X);\n        for (int i = idx0; i < e_opt.size();\
        \ i++) dsu.unite(e_opt.get(i).u, e_opt.get(i).v);\n        int idx1 = lowerBound(e_opt_s,\
        \ (X + 1) / 2);\n        int cost = 0;\n        for (int i = idx1; i < idx0;\
        \ i++) {\n            if (dsu.unite(e_opt.get(i).u, e_opt.get(i).v)) cost++;\n\
        \        }\n        return dsu.components == 1 && cost <= k;\n    }\n\n    private\
        \ int lowerBound(int[] arr, int val) {\n        int l = 0, r = arr.length;\n\
        \        while (l < r) {\n            int m = l + (r - l) / 2;\n           \
        \ if (arr[m] < val) l = m + 1;\n            else r = m;\n        }\n       \
        \ return l;\n    }\n}"
      python: "import bisect\n\nclass Solution(object):\n    def maxStability(self,\
        \ n, edges, k):\n        e_must, e_opt = [], []\n        min_must = 200001\n\
        \        for u, v, s, must in edges:\n            if must == 1:\n          \
        \      e_must.append((u, v, s))\n                if s < min_must: min_must =\
        \ s\n            else:\n                e_opt.append((u, v, s))\n\n        parent\
        \ = list(range(n))\n        def find(p, i):\n            while p[i] != i:\n\
        \                p[i] = p[p[i]]\n                i = p[i]\n            return\
        \ i\n\n        comp = n\n        for u, v, s in e_must:\n            root_u,\
        \ root_v = find(parent, u), find(parent, v)\n            if root_u == root_v:\
        \ return -1\n            parent[root_u] = root_v\n            comp -= 1\n\n\
        \        base_parent = parent[:]\n        base_comp = comp\n        e_opt.sort(key=lambda\
        \ x: x[2])\n        e_opt_s = [x[2] for x in e_opt]\n\n        def check(X):\n\
        \            if min_must < X: return False\n            p = base_parent[:]\n\
        \            c = base_comp\n            idx0 = bisect.bisect_left(e_opt_s, X)\n\
        \            for i in range(idx0, len(e_opt)):\n                u, v, s = e_opt[i]\n\
        \                ru, rv = find(p, u), find(p, v)\n                if ru != rv:\
        \ p[ru] = rv; c -= 1\n            idx1 = bisect.bisect_left(e_opt_s, (X + 1)\
        \ // 2)\n            cost = 0\n            for i in range(idx1, idx0):\n   \
        \             u, v, s = e_opt[i]\n                ru, rv = find(p, u), find(p,\
        \ v)\n                if ru != rv: p[ru] = rv; c -= 1; cost += 1\n         \
        \   return c == 1 and cost <= k\n\n        low, high, ans = 1, min(200000, min_must),\
        \ -1\n        while low <= high:\n            mid = (low + high) // 2\n    \
        \        if check(mid):\n                ans = mid\n                low = mid\
        \ + 1\n            else:\n                high = mid - 1\n        return ans"
      python3: "import bisect\n\nclass Solution:\n    def maxStability(self, n: int,\
        \ edges: list[list[int]], k: int) -> int:\n        e_must, e_opt = [], []\n\
        \        min_must = 200001\n        for u, v, s, must in edges:\n          \
        \  if must == 1:\n                e_must.append((u, v, s))\n               \
        \ if s < min_must: min_must = s\n            else:\n                e_opt.append((u,\
        \ v, s))\n\n        parent = list(range(n))\n        def find(p, i):\n     \
        \       while p[i] != i:\n                p[i] = p[p[i]]\n                i\
        \ = p[i]\n            return i\n\n        comp = n\n        for u, v, s in e_must:\n\
        \            root_u, root_v = find(parent, u), find(parent, v)\n           \
        \ if root_u == root_v: return -1\n            parent[root_u] = root_v\n    \
        \        comp -= 1\n\n        base_parent = list(parent)\n        base_comp\
        \ = comp\n        e_opt.sort(key=lambda x: x[2])\n        e_opt_s = [x[2] for\
        \ x in e_opt]\n\n        def check(X):\n            if min_must < X: return\
        \ False\n            p = list(base_parent)\n            c = base_comp\n    \
        \        idx0 = bisect.bisect_left(e_opt_s, X)\n            for i in range(idx0,\
        \ len(e_opt)):\n                u, v, s = e_opt[i]\n                ru, rv =\
        \ find(p, u), find(p, v)\n                if ru != rv: p[ru] = rv; c -= 1\n\
        \            idx1 = bisect.bisect_left(e_opt_s, (X + 1) // 2)\n            cost\
        \ = 0\n            for i in range(idx1, idx0):\n                u, v, s = e_opt[i]\n\
        \                ru, rv = find(p, u), find(p, v)\n                if ru != rv:\
        \ p[ru] = rv; c -= 1; cost += 1\n            return c == 1 and cost <= k\n\n\
        \        low, high, ans = 1, min(200000, min_must), -1\n        while low <=\
        \ high:\n            mid = (low + high) // 2\n            if check(mid):\n \
        \               ans = mid\n                low = mid + 1\n            else:\n\
        \                high = mid - 1\n        return ans"
      c: "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\ntypedef struct\
        \ { int u, v, s; } Edge;\n\nint compareEdges(const void* a, const void* b) {\n\
        \    return ((Edge*)a)->s - ((Edge*)b)->s;\n}\n\nint find(int* p, int i) {\n\
        \    if (p[i] == i) return i;\n    return p[i] = find(p, p[i]);\n}\n\nint check(int\
        \ X, int n, int k, Edge* e_opt, int e_opt_size, int* base_p, int base_c, int\
        \ min_must) {\n    if (min_must < X) return 0;\n    int* p = (int*)malloc(n\
        \ * sizeof(int));\n    memcpy(p, base_p, n * sizeof(int));\n    int c = base_c;\n\
        \    int cost = 0;\n\n    int low = 0, high = e_opt_size;\n    while(low < high)\
        \ {\n        int mid = low + (high - low) / 2;\n        if(e_opt[mid].s < X)\
        \ low = mid + 1; else high = mid;\n    }\n    int idx0 = low;\n    for(int i\
        \ = idx0; i < e_opt_size; i++) {\n        int ru = find(p, e_opt[i].u), rv =\
        \ find(p, e_opt[i].v);\n        if(ru != rv) { p[ru] = rv; c--; }\n    }\n\n\
        \    low = 0, high = idx0;\n    int val1 = (X + 1) / 2;\n    while(low < high)\
        \ {\n        int mid = low + (high - low) / 2;\n        if(e_opt[mid].s < val1)\
        \ low = mid + 1; else high = mid;\n    }\n    int idx1 = low;\n    for(int i\
        \ = idx1; i < idx0; i++) {\n        int ru = find(p, e_opt[i].u), rv = find(p,\
        \ e_opt[i].v);\n        if(ru != rv) { p[ru] = rv; c--; cost++; }\n    }\n\n\
        \    int res = (c == 1 && cost <= k);\n    free(p);\n    return res;\n}\n\n\
        int maxStability(int n, int** edges, int edgesSize, int* edgesColSize, int k)\
        \ {\n    Edge *e_must = malloc(edgesSize * sizeof(Edge)), *e_opt = malloc(edgesSize\
        \ * sizeof(Edge));\n    int m_size = 0, o_size = 0, min_must = 200001;\n   \
        \ for(int i = 0; i < edgesSize; i++) {\n        if(edges[i][3] == 1) {\n   \
        \         e_must[m_size++] = (Edge){edges[i][0], edges[i][1], edges[i][2]};\n\
        \            if(edges[i][2] < min_must) min_must = edges[i][2];\n        } else\
        \ {\n            e_opt[o_size++] = (Edge){edges[i][0], edges[i][1], edges[i][2]};\n\
        \        }\n    }\n\n    int* base_p = malloc(n * sizeof(int));\n    for(int\
        \ i = 0; i < n; i++) base_p[i] = i;\n    int base_c = n;\n    for(int i = 0;\
        \ i < m_size; i++) {\n        int ru = find(base_p, e_must[i].u), rv = find(base_p,\
        \ e_must[i].v);\n        if(ru == rv) { free(e_must); free(e_opt); free(base_p);\
        \ return -1; }\n        base_p[ru] = rv; base_c--;\n    }\n\n    qsort(e_opt,\
        \ o_size, sizeof(Edge), compareEdges);\n\n    int low = 1, high = (min_must\
        \ < 200000) ? min_must : 200000, ans = -1;\n    while(low <= high) {\n     \
        \   int mid = low + (high - low) / 2;\n        if(check(mid, n, k, e_opt, o_size,\
        \ base_p, base_c, min_must)) { ans = mid; low = mid + 1; } else high = mid -\
        \ 1;\n    }\n    free(e_must); free(e_opt); free(base_p);\n    return ans;\n\
        }"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public class DSU {\n        public int[] Parent;\n        public int\
        \ Components;\n        public DSU(int n) {\n            Parent = new int[n];\n\
        \            for (int i = 0; i < n; i++) Parent[i] = i;\n            Components\
        \ = n;\n        }\n        public DSU(DSU other) {\n            Parent = (int[])other.Parent.Clone();\n\
        \            Components = other.Components;\n        }\n        public int Find(int\
        \ i) {\n            if (Parent[i] == i) return i;\n            return Parent[i]\
        \ = Find(Parent[i]);\n        }\n        public bool Unite(int i, int j) {\n\
        \            int root_i = Find(i), root_j = Find(j);\n            if (root_i\
        \ != root_j) {\n                Parent[root_i] = root_j;\n                Components--;\n\
        \                return true;\n            }\n            return false;\n  \
        \      }\n    }\n\n    public int MaxStability(int n, int[][] edges, int k)\
        \ {\n        var eMust = new List<(int u, int v, int s)>();\n        var eOpt\
        \ = new List<(int u, int v, int s)>();\n        int minMust = 200001;\n    \
        \    foreach (var e in edges) {\n            if (e[3] == 1) {\n            \
        \    eMust.Add((e[0], e[1], e[2]));\n                minMust = Math.Min(minMust,\
        \ e[2]);\n            } else eOpt.Add((e[0], e[1], e[2]));\n        }\n\n  \
        \      var baseDsu = new DSU(n);\n        foreach (var e in eMust) if (!baseDsu.Unite(e.u,\
        \ e.v)) return -1;\n\n        eOpt.Sort((a, b) => a.s.CompareTo(b.s));\n   \
        \     int[] eOptS = new int[eOpt.Count];\n        for (int i = 0; i < eOpt.Count;\
        \ i++) eOptS[i] = eOpt[i].s;\n\n        int low = 1, high = Math.Min(200000,\
        \ minMust), ans = -1;\n        while (low <= high) {\n            int mid =\
        \ low + (high - low) / 2;\n            if (IsValid(mid, baseDsu, eOpt, eOptS,\
        \ k, minMust)) {\n                ans = mid;\n                low = mid + 1;\n\
        \            } else high = mid - 1;\n        }\n        return ans;\n    }\n\
        \n    private bool IsValid(int X, DSU baseDsu, List<(int u, int v, int s)> eOpt,\
        \ int[] eOptS, int k, int minMust) {\n        if (minMust < X) return false;\n\
        \        var dsu = new DSU(baseDsu);\n        int idx0 = Array.BinarySearch(eOptS,\
        \ X);\n        if (idx0 < 0) idx0 = ~idx0;\n        for (int i = idx0; i < eOpt.Count;\
        \ i++) dsu.Unite(eOpt[i].u, eOpt[i].v);\n        int idx1 = Array.BinarySearch(eOptS,\
        \ (X + 1) / 2);\n        if (idx1 < 0) idx1 = ~idx1;\n        int cost = 0;\n\
        \        for (int i = idx1; i < idx0; i++) if (dsu.Unite(eOpt[i].u, eOpt[i].v))\
        \ cost++;\n        return dsu.Components == 1 && cost <= k;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number[][]} edges\n * @param\
        \ {number} k\n * @return {number}\n */\nvar maxStability = function(n, edges,\
        \ k) {\n    let e_must = [], e_opt = [], min_must = 200001;\n    for (let e\
        \ of edges) {\n        if (e[3] === 1) {\n            e_must.push({u: e[0],\
        \ v: e[1], s: e[2]});\n            if (e[2] < min_must) min_must = e[2];\n \
        \       } else {\n            e_opt.push({u: e[0], v: e[1], s: e[2]});\n   \
        \     }\n    }\n\n    let base_parent = new Int32Array(n).map((_, i) => i);\n\
        \    let base_comp = n;\n    function find(p, i) {\n        while (p[i] !==\
        \ i) {\n            p[i] = p[p[i]];\n            i = p[i];\n        }\n    \
        \    return i;\n    }\n\n    for (let e of e_must) {\n        let ru = find(base_parent,\
        \ e.u), rv = find(base_parent, e.v);\n        if (ru === rv) return -1;\n  \
        \      base_parent[ru] = rv;\n        base_comp--;\n    }\n\n    e_opt.sort((a,\
        \ b) => a.s - b.s);\n    let e_opt_s = e_opt.map(e => e.s);\n\n    function\
        \ lowerBound(arr, val) {\n        let l = 0, r = arr.length;\n        while\
        \ (l < r) {\n            let m = (l + r) >> 1;\n            if (arr[m] < val)\
        \ l = m + 1; else r = m;\n        }\n        return l;\n    }\n\n    function\
        \ check(X) {\n        if (min_must < X) return false;\n        let p = new Int32Array(base_parent);\n\
        \        let c = base_comp;\n        let idx0 = lowerBound(e_opt_s, X);\n  \
        \      for (let i = idx0; i < e_opt.length; i++) {\n            let ru = find(p,\
        \ e_opt[i].u), rv = find(p, e_opt[i].v);\n            if (ru !== rv) { p[ru]\
        \ = rv; c--; }\n        }\n        let idx1 = lowerBound(e_opt_s, Math.ceil(X\
        \ / 2));\n        let cost = 0;\n        for (let i = idx1; i < idx0; i++) {\n\
        \            let ru = find(p, e_opt[i].u), rv = find(p, e_opt[i].v);\n     \
        \       if (ru !== rv) { p[ru] = rv; c--; cost++; }\n        }\n        return\
        \ c === 1 && cost <= k;\n    }\n\n    let low = 1, high = Math.min(200000, min_must),\
        \ ans = -1;\n    while (low <= high) {\n        let mid = (low + high) >> 1;\n\
        \        if (check(mid)) {\n            ans = mid;\n            low = mid +\
        \ 1;\n        } else {\n            high = mid - 1;\n        }\n    }\n    return\
        \ ans;\n};"
      typescript: "function maxStability(n: number, edges: number[][], k: number): number\
        \ {\n    class DSU {\n        parent: Int32Array;\n        size: Int32Array;\n\
        \        count: number;\n        constructor(n: number) {\n            this.parent\
        \ = new Int32Array(n);\n            this.size = new Int32Array(n);\n       \
        \     this.count = n;\n            for (let i = 0; i < n; i++) {\n         \
        \       this.parent[i] = i;\n                this.size[i] = 1;\n           \
        \ }\n        }\n        reset() {\n            this.count = n;\n           \
        \ for (let i = 0; i < n; i++) {\n                this.parent[i] = i;\n     \
        \           this.size[i] = 1;\n            }\n        }\n        find(i: number):\
        \ number {\n            let root = i;\n            while (this.parent[root]\
        \ !== root) root = this.parent[root];\n            while (this.parent[i] !==\
        \ root) {\n                let next = this.parent[i];\n                this.parent[i]\
        \ = root;\n                i = next;\n            }\n            return root;\n\
        \        }\n        union(i: number, j: number): boolean {\n            let\
        \ rootI = this.find(i);\n            let rootJ = this.find(j);\n           \
        \ if (rootI !== rootJ) {\n                if (this.size[rootI] < this.size[rootJ])\
        \ {\n                    this.parent[rootI] = rootJ;\n                    this.size[rootJ]\
        \ += this.size[rootI];\n                } else {\n                    this.parent[rootJ]\
        \ = rootI;\n                    this.size[rootI] += this.size[rootJ];\n    \
        \            }\n                this.count--;\n                return true;\n\
        \            }\n            return false;\n        }\n    }\n\n    const must1\
        \ = edges.filter(e => e[3] === 1);\n    const must0 = edges.filter(e => e[3]\
        \ === 0);\n    const dsu = new DSU(n);\n\n    for (const e of must1) {\n   \
        \     if (!dsu.union(e[0], e[1])) return -1;\n    }\n\n    function check(X:\
        \ number): boolean {\n        for (const e of must1) if (e[2] < X) return false;\n\
        \        dsu.reset();\n        for (const e of must1) dsu.union(e[0], e[1]);\n\
        \        for (const e of must0) {\n            if (e[2] >= X) dsu.union(e[0],\
        \ e[1]);\n            if (dsu.count === 1) break;\n        }\n        if (dsu.count\
        \ > 1 && k > 0) {\n            let upgradesUsed = 0;\n            for (const\
        \ e of must0) {\n                if (e[2] < X && 2 * e[2] >= X) {\n        \
        \            if (dsu.union(e[0], e[1])) {\n                        upgradesUsed++;\n\
        \                        if (upgradesUsed === k || dsu.count === 1) break;\n\
        \                    }\n                }\n            }\n        }\n      \
        \  return dsu.count === 1;\n    }\n\n    let low = 1, high = 200000, ans = -1;\n\
        \    while (low <= high) {\n        let mid = Math.floor((low + high) / 2);\n\
        \        if (check(mid)) {\n            ans = mid;\n            low = mid +\
        \ 1;\n        } else {\n            high = mid - 1;\n        }\n    }\n    return\
        \ ans;\n}"
      php: "class Solution {\n    function maxStability($n, $edges, $k) {\n        $must1\
        \ = [];\n        $must0 = [];\n        foreach ($edges as $e) {\n          \
        \  if ($e[3] == 1) $must1[] = $e;\n            else $must0[] = $e;\n       \
        \ }\n\n        $parent = range(0, $n - 1);\n        $size = array_fill(0, $n,\
        \ 1);\n        $count = $n;\n\n        function find(&$parent, $i) {\n     \
        \       $root = $i;\n            while ($parent[$root] !== $root) $root = $parent[$root];\n\
        \            while ($parent[$i] !== $root) {\n                $next = $parent[$i];\n\
        \                $parent[$i] = $root;\n                $i = $next;\n       \
        \     }\n            return $root;\n        }\n\n        function union(&$parent,\
        \ &$size, &$count, $i, $j) {\n            $rootI = find($parent, $i);\n    \
        \        $rootJ = find($parent, $j);\n            if ($rootI !== $rootJ) {\n\
        \                if ($size[$rootI] < $size[$rootJ]) {\n                    $parent[$rootI]\
        \ = $rootJ;\n                    $size[$rootJ] += $size[$rootI];\n         \
        \       } else {\n                    $parent[$rootJ] = $rootI;\n          \
        \          $size[$rootI] += $size[$rootJ];\n                }\n            \
        \    $count--;\n                return true;\n            }\n            return\
        \ false;\n        }\n\n        foreach ($must1 as $e) {\n            if (!union($parent,\
        \ $size, $count, $e[0], $e[1])) return -1;\n        }\n\n        $low = 1; $high\
        \ = 200000; $ans = -1;\n        while ($low <= $high) {\n            $mid =\
        \ floor(($low + $high) / 2);\n            if ($this->check($n, $must1, $must0,\
        \ $k, $mid)) {\n                $ans = $mid;\n                $low = $mid +\
        \ 1;\n            } else {\n                $high = $mid - 1;\n            }\n\
        \        }\n        return $ans;\n    }\n\n    function check($n, $must1, $must0,\
        \ $k, $X) {\n        foreach ($must1 as $e) if ($e[2] < $X) return false;\n\
        \        $parent = range(0, $n - 1);\n        $size = array_fill(0, $n, 1);\n\
        \        $count = $n;\n        foreach ($must1 as $e) {\n            $rootI\
        \ = $e[0]; while($parent[$rootI] !== $rootI) $rootI = $parent[$rootI];\n   \
        \         $rootJ = $e[1]; while($parent[$rootJ] !== $rootJ) $rootJ = $parent[$rootJ];\n\
        \            if ($rootI !== $rootJ) {\n                $parent[$rootI] = $rootJ;\n\
        \                $count--;\n            }\n        }\n        foreach ($must0\
        \ as $e) {\n            if ($e[2] >= $X) {\n                $rootI = $e[0];\
        \ while($parent[$rootI] !== $rootI) $rootI = $parent[$rootI];\n            \
        \    $rootJ = $e[1]; while($parent[$rootJ] !== $rootJ) $rootJ = $parent[$rootJ];\n\
        \                if ($rootI !== $rootJ) {\n                    $parent[$rootI]\
        \ = $rootJ;\n                    $count--;\n                    if ($count ===\
        \ 1) break;\n                }\n            }\n        }\n        if ($count\
        \ > 1 && $k > 0) {\n            $upgrades = 0;\n            foreach ($must0\
        \ as $e) {\n                if ($e[2] < $X && 2 * $e[2] >= $X) {\n         \
        \           $rootI = $e[0]; while($parent[$rootI] !== $rootI) $rootI = $parent[$rootI];\n\
        \                    $rootJ = $e[1]; while($parent[$rootJ] !== $rootJ) $rootJ\
        \ = $parent[$rootJ];\n                    if ($rootI !== $rootJ) {\n       \
        \                 $parent[$rootI] = $rootJ;\n                        $count--;\n\
        \                        $upgrades++;\n                        if ($upgrades\
        \ == $k || $count === 1) break;\n                    }\n                }\n\
        \            }\n        }\n        return $count === 1;\n    }\n}"
      swift: "class Solution {\n    func maxStability(_ n: Int, _ edges: [[Int]], _\
        \ k: Int) -> Int {\n        let must1 = edges.filter { $0[3] == 1 }\n      \
        \  let must0 = edges.filter { $0[3] == 0 }\n\n        var parent = Array(0..<n)\n\
        \        var count = n\n\n        func find(_ i: Int, _ p: inout [Int]) -> Int\
        \ {\n            var root = i\n            while p[root] != root { root = p[root]\
        \ }\n            var curr = i\n            while p[curr] != root {\n       \
        \         let next = p[curr]\n                p[curr] = root\n             \
        \   curr = next\n            }\n            return root\n        }\n\n     \
        \   for e in must1 {\n            let r1 = find(e[0], &parent), r2 = find(e[1],\
        \ &parent)\n            if r1 != r2 { parent[r1] = r2; count -= 1 } else { return\
        \ -1 }\n        }\n\n        func check(_ X: Int) -> Bool {\n            for\
        \ e in must1 { if e[2] < X { return false } }\n            var p = Array(0..<n),\
        \ c = n\n            for e in must1 {\n                let r1 = find(e[0], &p),\
        \ r2 = find(e[1], &p)\n                if r1 != r2 { p[r1] = r2; c -= 1 }\n\
        \            }\n            for e in must0 where e[2] >= X {\n             \
        \   let r1 = find(e[0], &p), r2 = find(e[1], &p)\n                if r1 != r2\
        \ { p[r1] = r2; c -= 1 }\n                if c == 1 { break }\n            }\n\
        \            if c > 1 && k > 0 {\n                var u = 0\n              \
        \  for e in must0 where e[2] < X && 2 * e[2] >= X {\n                    let\
        \ r1 = find(e[0], &p), r2 = find(e[1], &p)\n                    if r1 != r2\
        \ { p[r1] = r2; c -= 1; u += 1 }\n                    if u == k || c == 1 {\
        \ break }\n                }\n            }\n            return c == 1\n   \
        \     }\n\n        var low = 1, high = 200000, ans = -1\n        while low <=\
        \ high {\n            let mid = (low + high) / 2\n            if check(mid)\
        \ { ans = mid; low = mid + 1 } else { high = mid - 1 }\n        }\n        return\
        \ ans\n    }\n}"
      kotlin: "class Solution {\n    fun maxStability(n: Int, edges: Array<IntArray>,\
        \ k: Int): Int {\n        val must1 = edges.filter { it[3] == 1 }\n        val\
        \ must0 = edges.filter { it[3] == 0 }\n\n        class DSU(val n: Int) {\n \
        \           val parent = IntArray(n) { it }\n            var count = n\n   \
        \         fun reset() {\n                for (i in 0 until n) parent[i] = i\n\
        \                count = n\n            }\n            fun find(i: Int): Int\
        \ {\n                var root = i\n                while (parent[root] != root)\
        \ root = parent[root]\n                var curr = i\n                while (parent[curr]\
        \ != root) {\n                    val next = parent[curr]\n                \
        \    parent[curr] = root\n                    curr = next\n                }\n\
        \                return root\n            }\n            fun union(i: Int, j:\
        \ Int): Boolean {\n                val rI = find(i); val rJ = find(j)\n    \
        \            if (rI != rJ) { parent[rI] = rJ; count--; return true }\n     \
        \           return false\n            }\n        }\n\n        val dsu = DSU(n)\n\
        \        for (e in must1) if (!dsu.union(e[0], e[1])) return -1\n\n        fun\
        \ check(X: Int): Boolean {\n            for (e in must1) if (e[2] < X) return\
        \ false\n            dsu.reset()\n            for (e in must1) dsu.union(e[0],\
        \ e[1])\n            for (e in must0) {\n                if (e[2] >= X) dsu.union(e[0],\
        \ e[1])\n                if (dsu.count == 1) break\n            }\n        \
        \    if (dsu.count > 1 && k > 0) {\n                var u = 0\n            \
        \    for (e in must0) {\n                    if (e[2] < X && 2 * e[2] >= X)\
        \ {\n                        if (dsu.union(e[0], e[1])) {\n                \
        \            u++; if (u == k || dsu.count == 1) break\n                    \
        \    }\n                    }\n                }\n            }\n          \
        \  return dsu.count == 1\n        }\n\n        var low = 1; var high = 200000;\
        \ var ans = -1\n        while (low <= high) {\n            val mid = (low +\
        \ high) / 2\n            if (check(mid)) { ans = mid; low = mid + 1 } else {\
        \ high = mid - 1 }\n        }\n        return ans\n    }\n}"
      dart: "class Solution {\n  int maxStability(int n, List<List<int>> edges, int\
        \ k) {\n    final must1 = edges.where((e) => e[3] == 1).toList();\n    final\
        \ must0 = edges.where((e) => e[3] == 0).toList();\n\n    List<int> parent =\
        \ List.generate(n, (i) => i);\n    int count = n;\n\n    int find(int i, List<int>\
        \ p) {\n      int root = i;\n      while (p[root] != root) root = p[root];\n\
        \      while (p[i] != root) {\n        int next = p[i];\n        p[i] = root;\n\
        \        i = next;\n      }\n      return root;\n    }\n\n    for (var e in\
        \ must1) {\n      int r1 = find(e[0], parent), r2 = find(e[1], parent);\n  \
        \    if (r1 != r2) { parent[r1] = r2; count--; } else return -1;\n    }\n\n\
        \    bool check(int X) {\n      for (var e in must1) if (e[2] < X) return false;\n\
        \      List<int> p = List.generate(n, (i) => i);\n      int c = n;\n      for\
        \ (var e in must1) {\n        int r1 = find(e[0], p), r2 = find(e[1], p);\n\
        \        if (r1 != r2) { p[r1] = r2; c--; }\n      }\n      for (var e in must0)\
        \ {\n        if (e[2] >= X) {\n          int r1 = find(e[0], p), r2 = find(e[1],\
        \ p);\n          if (r1 != r2) { p[r1] = r2; c--; }\n          if (c == 1) break;\n\
        \        }\n      }\n      if (c > 1 && k > 0) {\n        int u = 0;\n     \
        \   for (var e in must0) {\n          if (e[2] < X && 2 * e[2] >= X) {\n   \
        \         int r1 = find(e[0], p), r2 = find(e[1], p);\n            if (r1 !=\
        \ r2) { p[r1] = r2; c--; u++; }\n            if (u == k || c == 1) break;\n\
        \          }\n        }\n      }\n      return c == 1;\n    }\n\n    int low\
        \ = 1, high = 200000, ans = -1;\n    while (low <= high) {\n      int mid =\
        \ (low + high) ~/ 2;\n      if (check(mid)) { ans = mid; low = mid + 1; } else\
        \ high = mid - 1;\n    }\n    return ans;\n  }\n}"
      go: "func maxStability(n int, edges [][]int, k int) int {\n\ttype edge struct{\
        \ u, v, s int }\n\tvar must1, must0 []edge\n\tfor _, e := range edges {\n\t\t\
        if e[3] == 1 {\n\t\t\tmust1 = append(must1, edge{e[0], e[1], e[2]})\n\t\t} else\
        \ {\n\t\t\tmust0 = append(must0, edge{e[0], e[1], e[2]})\n\t\t}\n\t}\n\tparent\
        \ := make([]int, n)\n\tfind := func(p []int, i int) int {\n\t\troot := i\n\t\
        \tfor p[root] != root { root = p[root] }\n\t\tfor p[i] != root { next := p[i];\
        \ p[i] = root; i = next }\n\t\treturn root\n\t}\n\tfor i := 0; i < n; i++ {\
        \ parent[i] = i }\n\tcount := n\n\tfor _, e := range must1 {\n\t\tr1, r2 :=\
        \ find(parent, e.u), find(parent, e.v)\n\t\tif r1 != r2 { parent[r1] = r2; count--\
        \ } else { return -1 }\n\t}\n\tcheck := func(X int) bool {\n\t\tfor _, e :=\
        \ range must1 { if e.s < X { return false } }\n\t\tp := make([]int, n)\n\t\t\
        for i := 0; i < n; i++ { p[i] = i }\n\t\tc := n\n\t\tfor _, e := range must1\
        \ {\n\t\t\tr1, r2 := find(p, e.u), find(p, e.v)\n\t\t\tif r1 != r2 { p[r1] =\
        \ r2; c-- }\n\t\t}\n\t\tfor _, e := range must0 {\n\t\t\tif e.s >= X {\n\t\t\
        \t\tr1, r2 := find(p, e.u), find(p, e.v)\n\t\t\t\tif r1 != r2 { p[r1] = r2;\
        \ c-- }\n\t\t\t\tif c == 1 { break }\n\t\t\t}\n\t\t}\n\t\tif c > 1 && k > 0\
        \ {\n\t\t\tu := 0\n\t\t\tfor _, e := range must0 {\n\t\t\t\tif e.s < X && 2*e.s\
        \ >= X {\n\t\t\t\t\tr1, r2 := find(p, e.u), find(p, e.v)\n\t\t\t\t\tif r1 !=\
        \ r2 { p[r1] = r2; c--; u++ }\n\t\t\t\t\tif u == k || c == 1 { break }\n\t\t\
        \t\t}\n\t\t\t}\n\t\t}\n\t\treturn c == 1\n\t}\n\tlow, high, ans := 1, 200000,\
        \ -1\n\tfor low <= high {\n\t\tmid := (low + high) / 2\n\t\tif check(mid) {\
        \ ans = mid; low = mid + 1 } else { high = mid - 1 }\n\t}\n\treturn ans\n}"
      ruby: "class DSU\n  attr_accessor :parent, :rank, :num_components\n  def initialize(n)\n\
        \    @parent = (0...n).to_a\n    @rank = Array.new(n, 0)\n    @num_components\
        \ = n\n  end\n  def find(i)\n    return i if @parent[i] == i\n    @parent[i]\
        \ = find(@parent[i])\n  end\n  def union(i, j)\n    root_i = find(i)\n    root_j\
        \ = find(j)\n    if root_i != root_j\n      if @rank[root_i] < @rank[root_j]\n\
        \        @parent[root_i] = root_j\n      elsif @rank[root_i] > @rank[root_j]\n\
        \        @parent[root_j] = root_i\n      else\n        @parent[root_i] = root_j\n\
        \        @rank[root_j] += 1\n      end\n      @num_components -= 1\n      return\
        \ true\n    end\n    false\n  end\n  def initialize_copy(source)\n    @parent\
        \ = source.parent.dup\n    @rank = source.rank.dup\n    @num_components = source.num_components\n\
        \  end\nend\n\ndef max_stability(n, edges, k)\n  must_edges = []\n  optional_edges\
        \ = []\n  edges.each do |u, v, s, m|\n    if m == 1\n      must_edges << [u,\
        \ v, s]\n    else\n      optional_edges << [u, v, s]\n    end\n  end\n  dsu_must\
        \ = DSU.new(n)\n  min_must_s = 200001\n  must_edges.each do |u, v, s|\n    return\
        \ -1 if !dsu_must.union(u, v)\n    min_must_s = s if s < min_must_s\n  end\n\
        \  check = lambda do |x|\n    return false if x > min_must_s\n    dsu = dsu_must.clone\n\
        \    comp = dsu.num_components\n    return true if comp == 1\n    optional_edges.each\
        \ do |u, v, s|\n      if s >= x\n        if dsu.union(u, v)\n          comp\
        \ -= 1\n          return true if comp == 1\n        end\n      end\n    end\n\
        \    upgrades = 0\n    optional_edges.each do |u, v, s|\n      if s < x && 2\
        \ * s >= x\n        if upgrades < k\n          if dsu.union(u, v)\n        \
        \    comp -= 1\n            upgrades += 1\n            return true if comp ==\
        \ 1\n          end\n        end\n      end\n    end\n    comp == 1\n  end\n\
        \  low, high, ans = 1, 200000, -1\n  while low <= high\n    mid = (low + high)\
        \ / 2\n    if check.call(mid)\n      ans = mid\n      low = mid + 1\n    else\n\
        \      high = mid - 1\n    end\n  end\n  ans\nend"
      scala: "object Solution {\n  class DSU(n: Int) {\n    val parent: Array[Int] =\
        \ Array.range(0, n)\n    val rank: Array[Int] = Array.fill(n)(0)\n    var numComponents:\
        \ Int = n\n\n    def find(i: Int): Int = {\n      if (parent(i) == i) i\n  \
        \    else {\n        parent(i) = find(parent(i))\n        parent(i)\n      }\n\
        \    }\n\n    def union(i: Int, j: Int): Boolean = {\n      val rootI = find(i)\n\
        \      val rootJ = find(j)\n      if (rootI != rootJ) {\n        if (rank(rootI)\
        \ < rank(rootJ)) parent(rootI) = rootJ\n        else if (rank(rootI) > rank(rootJ))\
        \ parent(rootJ) = rootI\n        else {\n          parent(rootI) = rootJ\n \
        \         rank(rootJ) += 1\n        }\n        numComponents -= 1\n        true\n\
        \      } else false\n    }\n\n    def copy(): DSU = {\n      val res = new DSU(n)\n\
        \      System.arraycopy(parent, 0, res.parent, 0, n)\n      System.arraycopy(rank,\
        \ 0, res.rank, 0, n)\n      res.numComponents = numComponents\n      res\n \
        \   }\n  }\n\n  def maxStability(n: Int, edges: Array[Array[Int]], k: Int):\
        \ Int = {\n    val mustEdges = edges.filter(_(3) == 1)\n    val optionalEdges\
        \ = edges.filter(_(3) == 0)\n    val dsuMust = new DSU(n)\n    var minMustS\
        \ = 200001\n    for (e <- mustEdges) {\n      if (!dsuMust.union(e(0), e(1)))\
        \ return -1\n      if (e(2) < minMustS) minMustS = e(2)\n    }\n\n    def check(x:\
        \ Int): Boolean = {\n      if (x > minMustS) return false\n      val dsu = dsuMust.copy()\n\
        \      var comp = dsu.numComponents\n      if (comp == 1) return true\n    \
        \  for (e <- optionalEdges if e(2) >= x) {\n        if (dsu.union(e(0), e(1)))\
        \ {\n          comp -= 1\n          if (comp == 1) return true\n        }\n\
        \      }\n      var upgradesUsed = 0\n      for (e <- optionalEdges if e(2)\
        \ < x && 2 * e(2) >= x) {\n        if (upgradesUsed < k) {\n          if (dsu.union(e(0),\
        \ e(1))) {\n            comp -= 1\n            upgradesUsed += 1\n         \
        \   if (comp == 1) return true\n          }\n        }\n      }\n      comp\
        \ == 1\n    }\n\n    var low = 1\n    var high = 200000\n    var ans = -1\n\
        \    while (low <= high) {\n      val mid = low + (high - low) / 2\n      if\
        \ (check(mid)) {\n        ans = mid\n        low = mid + 1\n      } else {\n\
        \        high = mid - 1\n      }\n    }\n    ans\n  }\n}"
      rust: "impl Solution {\n    pub fn max_stability(n: i32, edges: Vec<Vec<i32>>,\
        \ k: i32) -> i32 {\n        let mut must_edges = Vec::new();\n        let mut\
        \ optional_edges = Vec::new();\n        for e in edges {\n            if e[3]\
        \ == 1 {\n                must_edges.push((e[0] as usize, e[1] as usize, e[2]));\n\
        \            } else {\n                optional_edges.push((e[0] as usize, e[1]\
        \ as usize, e[2]));\n            }\n        }\n        let mut dsu_must = DSU::new(n\
        \ as usize);\n        let mut min_must_s = 200001;\n        for &(u, v, s) in\
        \ &must_edges {\n            if !dsu_must.union(u, v) {\n                return\
        \ -1;\n            }\n            if s < min_must_s {\n                min_must_s\
        \ = s;\n            }\n        }\n        let mut low = 1;\n        let mut\
        \ high = 200000;\n        let mut ans = -1;\n        while low <= high {\n \
        \           let mid = low + (high - low) / 2;\n            if Self::check(mid,\
        \ k, min_must_s, &optional_edges, &dsu_must) {\n                ans = mid;\n\
        \                low = mid + 1;\n            } else {\n                high\
        \ = mid - 1;\n            }\n        }\n        ans\n    }\n\n    fn check(x:\
        \ i32, k: i32, min_must_s: i32, optional: &[(usize, usize, i32)], dsu_must:\
        \ &DSU) -> bool {\n        if x > min_must_s {\n            return false;\n\
        \        }\n        let mut dsu = dsu_must.clone();\n        let mut comp =\
        \ dsu.num_components;\n        if comp == 1 {\n            return true;\n  \
        \      }\n        for &(u, v, s) in optional {\n            if s >= x {\n  \
        \              if dsu.union(u, v) {\n                    comp -= 1;\n      \
        \              if comp == 1 {\n                        return true;\n      \
        \              }\n                }\n            }\n        }\n        let mut\
        \ upgrades = 0;\n        for &(u, v, s) in optional {\n            if s < x\
        \ && 2 * s >= x {\n                if upgrades < k {\n                    if\
        \ dsu.union(u, v) {\n                        comp -= 1;\n                  \
        \      upgrades += 1;\n                        if comp == 1 {\n            \
        \                return true;\n                        }\n                 \
        \   }\n                }\n            }\n        }\n        comp == 1\n    }\n\
        }\n\n#[derive(Clone)]\nstruct DSU {\n    parent: Vec<usize>,\n    rank: Vec<usize>,\n\
        \    num_components: usize,\n}\n\nimpl DSU {\n    fn new(n: usize) -> Self {\n\
        \        Self {\n            parent: (0..n).collect(),\n            rank: vec![0;\
        \ n],\n            num_components: n,\n        }\n    }\n    fn find(&mut self,\
        \ i: usize) -> usize {\n        if self.parent[i] == i {\n            i\n  \
        \      } else {\n            let root = self.find(self.parent[i]);\n       \
        \     self.parent[i] = root;\n            root\n        }\n    }\n    fn union(&mut\
        \ self, i: usize, j: usize) -> bool {\n        let root_i = self.find(i);\n\
        \        let root_j = self.find(j);\n        if root_i != root_j {\n       \
        \     if self.rank[root_i] < self.rank[root_j] {\n                self.parent[root_i]\
        \ = root_j;\n            } else if self.rank[root_i] > self.rank[root_j] {\n\
        \                self.parent[root_j] = root_i;\n            } else {\n     \
        \           self.parent[root_i] = root_j;\n                self.rank[root_j]\
        \ += 1;\n            }\n            self.num_components -= 1;\n            true\n\
        \        } else {\n            false\n        }\n    }\n}"
      racket: "(define/contract (max-stability n edges k)\n  (-> exact-integer? (listof\
        \ (listof exact-integer?)) exact-integer? exact-integer?)\n  (define (find parent\
        \ i)\n    (let ([p (vector-ref parent i)])\n      (if (= p i)\n          i\n\
        \          (let ([root (find parent p)])\n            (vector-set! parent i\
        \ root)\n            root))))\n  (define (union! parent rank i j)\n    (let\
        \ ([root-i (find parent i)]\n          [root-j (find parent j)])\n      (if\
        \ (= root-i root-j)\n          #f\n          (let ([rank-i (vector-ref rank\
        \ root-i)]\n                [rank-j (vector-ref rank root-j)])\n           \
        \ (cond\n              [(< rank-i rank-j) (vector-set! parent root-i root-j)]\n\
        \              [(> rank-i rank-j) (vector-set! parent root-j root-i)]\n    \
        \          [else\n               (vector-set! parent root-i root-j)\n      \
        \         (vector-set! rank root-j (+ rank-j 1))])\n            #t))))\n  (let*\
        \ ([must-edges (filter (lambda (e) (= (fourth e) 1)) edges)]\n         [opt-edges\
        \ (filter (lambda (e) (= (fourth e) 0)) edges)]\n         [dsu-p (vector-copy\
        \ (build-vector n (lambda (i) i)))]\n         [dsu-r (make-vector n 0)]\n  \
        \       [comp (box n)]\n         [min-must (box 200001)]\n         [possible\
        \ (box #t)])\n    (for ([e must-edges])\n      (if (union! dsu-p dsu-r (first\
        \ e) (second e))\n          (begin\n            (set-box! comp (- (unbox comp)\
        \ 1))\n            (if (< (third e) (unbox min-must))\n                (set-box!\
        \ min-must (third e)) (void)))\n          (set-box! possible #f)))\n    (if\
        \ (not (unbox possible))\n        -1\n        (let* ([check (lambda (x)\n  \
        \                      (if (> x (unbox min-must)) #f\n                     \
        \       (let ([p (vector-copy dsu-p)] [r (vector-copy dsu-r)] [c (unbox comp)])\n\
        \                              (let ([c2 (for/fold ([curr-c c]) ([e opt-edges]\
        \ #:when (>= (third e) x))\n                                          (if (union!\
        \ p r (first e) (second e)) (- curr-c 1) curr-c))])\n                      \
        \          (if (= c2 1) #t\n                                    (let-values\
        \ ([(final-c final-u) (for/fold ([curr-c c2] [u 0]) ([e opt-edges] #:when (and\
        \ (< (third e) x) (>= (* 2 (third e)) x)))\n                               \
        \                                      (if (and (< u k) (union! p r (first e)\
        \ (second e)))\n                                                           \
        \              (values (- curr-c 1) (+ u 1))\n                             \
        \                                            (values curr-c u)))])\n       \
        \                               (= final-c 1))))))])\n               [low (box\
        \ 1)] [high (box 200000)] [ans (box -1)])\n          (while (<= (unbox low)\
        \ (unbox high))\n            (let ([mid (quotient (+ (unbox low) (unbox high))\
        \ 2)])\n              (if (check mid)\n                  (begin (set-box! ans\
        \ mid) (set-box! low (+ mid 1)))\n                  (set-box! high (- mid 1)))))\n\
        \          (unbox ans)))))\n(define-syntax-rule (while condition body ...)\n\
        \  (let loop () (when condition body ... (loop))))"
      erlang: "-spec max_stability(N :: integer(), Edges :: [[integer()]], K :: integer())\
        \ -> integer().\nmax_stability(N, Edges, K) ->\n    MustEdges = [E || E <- Edges,\
        \ lists:nth(4, E) == 1],\n    OptionalEdges = [E || E <- Edges, lists:nth(4,\
        \ E) == 0],\n    Parent = array:from_list(lists:seq(0, N - 1)),\n    Rank =\
        \ array:new(N, {default, 0}),\n    case build_must_dsu(MustEdges, Parent, Rank,\
        \ N, 200001) of\n        error -> -1;\n        {DsuP, DsuR, Comp, MinMustS}\
        \ -> binary_search(1, 200000, -1, K, MinMustS, OptionalEdges, DsuP, DsuR, Comp)\n\
        \    end.\n\nbuild_must_dsu([], P, R, C, M) -> {P, R, C, M};\nbuild_must_dsu([[U,\
        \ V, S, _] | T], P, R, C, M) ->\n    {RootU, P1} = find(U, P),\n    {RootV,\
        \ P2} = find(V, P1),\n    if RootU == RootV -> error;\n       true ->\n    \
        \       {NewP, NewR} = union_roots(RootU, RootV, P2, R),\n           build_must_dsu(T,\
        \ NewP, NewR, C - 1, min(M, S))\n    end.\n\nbinary_search(Low, High, Ans, K,\
        \ MinMust, Opt, DsuP, DsuR, Comp) when Low =< High ->\n    Mid = (Low + High)\
        \ div 2,\n    case check(Mid, K, MinMust, Opt, DsuP, DsuR, Comp) of\n      \
        \  true -> binary_search(Mid + 1, High, Mid, K, MinMust, Opt, DsuP, DsuR, Comp);\n\
        \        false -> binary_search(Low, Mid - 1, Ans, K, MinMust, Opt, DsuP, DsuR,\
        \ Comp)\n    end;\nbinary_search(_, _, Ans, _, _, _, _, _, _) -> Ans.\n\ncheck(X,\
        \ _K, MinMustS, _Opt, _P, _R, _Comp) when X > MinMustS -> false;\ncheck(X, K,\
        \ _MinMustS, Opt, P, R, Comp) ->\n    {P1, Comp1} = add_free(X, Opt, P, R, Comp),\n\
        \    if Comp1 == 1 -> true;\n       true -> {Comp2, _} = add_paid(X, K, Opt,\
        \ P1, R, Comp1, 0), Comp2 == 1\n    end.\n\nadd_free(_, [], P, _, C) -> {P,\
        \ C};\nadd_free(X, [[U, V, S] | T], P, R, C) when S >= X ->\n    {RootU, P1}\
        \ = find(U, P),\n    {RootV, P2} = find(V, P1),\n    if RootU /= RootV ->\n\
        \           {NewP, _} = union_roots(RootU, RootV, P2, R),\n           if C -\
        \ 1 == 1 -> {NewP, 1}; true -> add_free(X, T, NewP, R, C - 1) end;\n       true\
        \ -> add_free(X, T, P2, R, C)\n    end;\nadd_free(X, [_ | T], P, R, C) -> add_free(X,\
        \ T, P, R, C).\n\nadd_paid(_, _, [], _, _, C, U) -> {C, U};\nadd_paid(X, K,\
        \ [[U, V, S] | T], P, R, C, Up) when S < X, 2 * S >= X, Up < K ->\n    {RootU,\
        \ P1} = find(U, P),\n    {RootV, P2} = find(V, P1),\n    if RootU /= RootV ->\n\
        \           {NewP, _} = union_roots(RootU, RootV, P2, R),\n           if C -\
        \ 1 == 1 -> {1, Up + 1}; true -> add_paid(X, K, T, NewP, R, C - 1, Up + 1) end;\n\
        \       true -> add_paid(X, K, T, P2, R, C, Up)\n    end;\nadd_paid(X, K, [_\
        \ | T], P, R, C, Up) -> add_paid(X, K, T, P, R, C, Up).\n\nfind(I, P) ->\n \
        \   Parent = array:get(I, P),\n    if Parent == I -> {I, P};\n       true ->\n\
        \           {Root, NewP} = find(Parent, P),\n           {Root, array:set(I,\
        \ Root, NewP)}\n    end.\n\nunion_roots(RootU, RootV, P, R) ->\n    RankU =\
        \ array:get(RootU, R), RankV = array:get(RootV, R),\n    if RankU < RankV ->\
        \ {array:set(RootU, RootV, P), R};\n       RankU > RankV -> {array:set(RootV,\
        \ RootU, P), R};\n       true -> {array:set(RootU, RootV, P), array:set(RootV,\
        \ RankV + 1, R)}\n    end."
      elixir: "defmodule Solution do\n  @spec max_stability(n :: integer, edges :: [[integer]],\
        \ k :: integer) :: integer\n  def max_stability(n, edges, k) do\n    must_edges\
        \ = Enum.filter(edges, fn [_, _, _, m] -> m == 1 end)\n    optional_edges =\
        \ Enum.filter(edges, fn [_, _, _, m] -> m == 0 end) |> Enum.map(fn [u, v, s,\
        \ _] -> [u, v, s] end)\n    parent = :array.from_list(Enum.to_list(0..(n - 1)))\n\
        \    rank = :array.new(n, default: 0)\n    case build_must_dsu(must_edges, parent,\
        \ rank, n, 200001) do\n      :error -> -1\n      {dsu_p, dsu_r, comp, min_must_s}\
        \ -> binary_search(1, 200000, -1, k, min_must_s, optional_edges, dsu_p, dsu_r,\
        \ comp)\n    end\n  end\n\n  defp build_must_dsu([], p, r, c, m), do: {p, r,\
        \ c, m}\n  defp build_must_dsu([[u, v, s, _] | t], p, r, c, m) do\n    {root_u,\
        \ p1} = find(u, p)\n    {root_v, p2} = find(v, p1)\n    if root_u == root_v\
        \ do\n      :error\n    else\n      {new_p, new_r} = union_roots(root_u, root_v,\
        \ p2, r)\n      build_must_dsu(t, new_p, new_r, c - 1, min(m, s))\n    end\n\
        \  end\n\n  defp binary_search(low, high, ans, k, min_must, opt, dsu_p, dsu_r,\
        \ comp) when low <= high do\n    mid = div(low + high, 2)\n    if check(mid,\
        \ k, min_must, opt, dsu_p, dsu_r, comp) do\n      binary_search(mid + 1, high,\
        \ mid, k, min_must, opt, dsu_p, dsu_r, comp)\n    else\n      binary_search(low,\
        \ mid - 1, ans, k, min_must, opt, dsu_p, dsu_r, comp)\n    end\n  end\n  defp\
        \ binary_search(_, _, ans, _, _, _, _, _, _), do: ans\n\n  defp check(x, _k,\
        \ min_must_s, _opt, _p, _r, _comp) when x > min_must_s, do: false\n  defp check(x,\
        \ k, _min_must_s, opt, p, r, comp) do\n    {p1, comp1} = add_free(x, opt, p,\
        \ r, comp)\n    if comp1 == 1 do\n      true\n    else\n      {comp2, _} = add_paid(x,\
        \ k, opt, p1, r, comp1, 0)\n      comp2 == 1\n    end\n  end\n\n  defp add_free(_,\
        \ [], p, _, c), do: {p, c}\n  defp add_free(x, [[u, v, s] | t], p, r, c) when\
        \ s >= x do\n    {root_u, p1} = find(u, p)\n    {root_v, p2} = find(v, p1)\n\
        \    if root_u != root_v do\n      {new_p, _} = union_roots(root_u, root_v,\
        \ p2, r)\n      if c - 1 == 1, do: {new_p, 1}, else: add_free(x, t, new_p, r,\
        \ c - 1)\n    else\n      add_free(x, t, p2, r, c)\n    end\n  end\n  defp add_free(x,\
        \ [_ | t], p, r, c), do: add_free(x, t, p, r, c)\n\n  defp add_paid(_, _, [],\
        \ _, _, c, u), do: {c, u}\n  defp add_paid(x, k, [[u, v, s] | t], p, r, c, up)\
        \ when s < x and 2 * s >= x and up < k do\n    {root_u, p1} = find(u, p)\n \
        \   {root_v, p2} = find(v, p1)\n    if root_u != root_v do\n      {new_p, _}\
        \ = union_roots(root_u, root_v, p2, r)\n      if c - 1 == 1, do: {1, up + 1},\
        \ else: add_paid(x, k, t, new_p, r, c - 1, up + 1)\n    else\n      add_paid(x,\
        \ k, t, p2, r, c, up)\n    end\n  end\n  defp add_paid(x, k, [_ | t], p, r,\
        \ c, up), do: add_paid(x, k, t, p, r, c, up)\n\n  defp find(i, p) do\n    parent\
        \ = :array.get(i, p)\n    if parent == i do\n      {i, p}\n    else\n      {root,\
        \ new_p} = find(parent, p)\n      {root, :array.set(i, root, new_p)}\n    end\n\
        \  end\n\n  defp union_roots(root_u, root_v, p, r) do\n    rank_u = :array.get(root_u,\
        \ r)\n    rank_v = :array.get(root_v, r)\n    cond do\n      rank_u < rank_v\
        \ -> {:array.set(root_u, root_v, p), r}\n      rank_u > rank_v -> {:array.set(root_v,\
        \ root_u, p), r}\n      true -> {:array.set(root_u, root_v, p), :array.set(root_v,\
        \ rank_v + 1, r)}\n    end\n  end\nend"
    approach: "The problem asks for the maximum possible stability (minimum edge strength)\
      \ of a valid spanning tree. This structure suggests binary search on the answer\
      \ $X$. For a fixed threshold $X$, we must check if it's possible to form a spanning\
      \ tree where every edge has strength $\\ge X$ while including all mandatory edges\
      \ ($must_i = 1$) and using at most $k$ upgrades on optional edges. Mandatory edges\
      \ cannot be upgraded, so if any mandatory edge has a strength $s_i < X$, the threshold\
      \ $X$ is immediately impossible. Furthermore, the set of mandatory edges must\
      \ not contain any cycles; if they do, no valid spanning tree can be formed. \n\
      \nTo efficiently perform the check, we first ensure the mandatory edges are acyclic\
      \ and the graph as a whole is connected. For a given threshold $X$, we use a Disjoint\
      \ Set Union (DSU) starting with all mandatory edges. We then greedily add optional\
      \ edges that already satisfy $s_i \\ge X$ (zero-cost) to connect components. If\
      \ the graph is still not connected, we add optional edges that satisfy $2s_i \\\
      ge X$ (one-cost) until the graph is connected. If the number of components reaches\
      \ 1 and the total upgrades used is $\\le k$, the threshold $X$ is feasible. Sorting\
      \ the optional edges by strength allows us to use binary search (bisect) to quickly\
      \ find relevant edge ranges for each $X$ in the check function."
    time_complexity: O(M \log M + M \log(\max S) \cdot \alpha(N)), where $N$ is the
      number of nodes, $M$ is the number of edges, and $S$ is the maximum strength.
      Sorting optional edges takes $O(M \log M)$, and the binary search on stability
      takes $\log(\max S)$ iterations, with each check performing $O(M \alpha(N))$ DSU
      operations.
    space_complexity: O(N + M) to store the edges, the DSU parent/rank arrays, and the
      pre-categorized mandatory and optional edge lists.
    elapsed_time: 369.5732686519623
    model: gemini-3-flash-preview
    generated_at: '2026-03-12 01:25:11 '
---

## Problem #3600: Maximize Spanning Tree Stability with Upgrades

**Difficulty:** Hard

**Topics:** Binary Search, Greedy, Union-Find, Graph Theory, Minimum Spanning Tree

## Problem Description

<p>You are given an integer <code>n</code>, representing <code>n</code> nodes numbered from 0 to <code>n - 1</code> and a list of <code>edges</code>, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>, s<sub>i</sub>, must<sub>i</sub>]</code>:</p>

<ul>
	<li><code>u<sub>i</sub></code> and <code>v<sub>i</sub></code> indicates an undirected edge between nodes <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code>.</li>
	<li><code>s<sub>i</sub></code> is the strength of the edge.</li>
	<li><code>must<sub>i</sub></code> is an integer (0 or 1). If <code>must<sub>i</sub> == 1</code>, the edge <strong>must</strong> be included in the<strong> </strong><strong>spanning tree</strong>. These edges <strong>cannot</strong> be <strong>upgraded</strong>.</li>
</ul>

<p>You are also given an integer <code>k</code>, the <strong>maximum</strong> number of upgrades you can perform. Each upgrade <strong>doubles</strong> the strength of an edge, and each eligible edge (with <code>must<sub>i</sub> == 0</code>) can be upgraded <strong>at most</strong> once.</p>

<p>The <strong>stability</strong> of a spanning tree is defined as the <strong>minimum</strong> strength score among all edges included in it.</p>

<p>Return the <strong>maximum</strong> possible stability of any valid spanning tree. If it is impossible to connect all nodes, return <code>-1</code>.</p>

<p><strong>Note</strong>: A <strong>spanning tree</strong> of a graph with <code>n</code> nodes is a subset of the edges that connects all nodes together (i.e. the graph is <strong>connected</strong>) <em>without</em> forming any cycles, and uses <strong>exactly</strong> <code>n - 1</code> edges.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Edge <code>[0,1]</code> with strength = 2 must be included in the spanning tree.</li>
	<li>Edge <code>[1,2]</code> is optional and can be upgraded from 3 to 6 using one upgrade.</li>
	<li>The resulting spanning tree includes these two edges with strengths 2 and 6.</li>
	<li>The minimum strength in the spanning tree is 2, which is the maximum possible stability.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Since all edges are optional and up to <code>k = 2</code> upgrades are allowed.</li>
	<li>Upgrade edges <code>[0,1]</code> from 4 to 8 and <code>[1,2]</code> from 3 to 6.</li>
	<li>The resulting spanning tree includes these two edges with strengths 8 and 6.</li>
	<li>The minimum strength in the tree is 6, which is the maximum possible stability.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>All edges are mandatory and form a cycle, which violates the spanning tree property of acyclicity. Thus, the answer is -1.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= edges.length &lt;= 10<sup>5</sup></code></li>
	<li><code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>, s<sub>i</sub>, must<sub>i</sub>]</code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt; n</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li><code>1 &lt;= s<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li><code>must<sub>i</sub></code> is either <code>0</code> or <code>1</code>.</li>
	<li><code>0 &lt;= k &lt;= n</code></li>
	<li>There are no duplicate edges.</li>
</ul>


## Hints

1. Sort the `edges` array in descending order of weights.

2. Try using binary search on `ans`.

3. Implement a `chk` function which first adds all the edges with `must = 1`, and then adds the edges with `must = 0`, using any remaining upgrades greedily.

4. Use a `DSU` with path compression and union by size/rank to maintain connected components.

5. Don't forget the case where you cannot form an MST because more than one component remains after processing all edges.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the maximum possible stability (minimum edge strength) of a valid spanning tree. This structure suggests binary search on the answer $X$. For a fixed threshold $X$, we must check if it's possible to form a spanning tree where every edge has strength $\ge X$ while including all mandatory edges ($must_i = 1$) and using at most $k$ upgrades on optional edges. Mandatory edges cannot be upgraded, so if any mandatory edge has a strength $s_i < X$, the threshold $X$ is immediately impossible. Furthermore, the set of mandatory edges must not contain any cycles; if they do, no valid spanning tree can be formed. 

To efficiently perform the check, we first ensure the mandatory edges are acyclic and the graph as a whole is connected. For a given threshold $X$, we use a Disjoint Set Union (DSU) starting with all mandatory edges. We then greedily add optional edges that already satisfy $s_i \ge X$ (zero-cost) to connect components. If the graph is still not connected, we add optional edges that satisfy $2s_i \ge X$ (one-cost) until the graph is connected. If the number of components reaches 1 and the total upgrades used is $\le k$, the threshold $X$ is feasible. Sorting the optional edges by strength allows us to use binary search (bisect) to quickly find relevant edge ranges for each $X$ in the check function.

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
    struct Edge { int u, v, s; };
    struct DSU {
        vector<int> parent;
        int components;
        DSU(int n) : parent(n), components(n) {
            for (int i = 0; i < n; ++i) parent[i] = i;
        }
        int find(int i) {
            if (parent[i] == i) return i;
            return parent[i] = find(parent[i]);
        }
        bool unite(int i, int j) {
            int root_i = find(i), root_j = find(j);
            if (root_i != root_j) {
                parent[root_i] = root_j;
                components--;
                return true;
            }
            return false;
        }
    };

    int maxStability(int n, vector<vector<int>>& edges, int k) {
        vector<Edge> e_must, e_opt;
        int min_must = 200001;
        for (const auto& e : edges) {
            if (e[3] == 1) {
                e_must.push_back({e[0], e[1], e[2]});
                min_must = min(min_must, e[2]);
            } else {
                e_opt.push_back({e[0], e[1], e[2]});
            }
        }

        DSU base_dsu(n);
        for (const auto& e : e_must) {
            if (!base_dsu.unite(e.u, e.v)) return -1;
        }

        sort(e_opt.begin(), e_opt.end(), [](const Edge& a, const Edge& b) {
            return a.s < b.s;
        });

        auto check = [&](int X) {
            if (min_must < X) return false;
            DSU dsu = base_dsu;
            int cost = 0;
            auto it0 = lower_bound(e_opt.begin(), e_opt.end(), X, [](const Edge& e, int val) { return e.s < val; });
            for (auto it = it0; it != e_opt.end(); ++it) {
                dsu.unite(it->u, it->v);
            }
            auto it1 = lower_bound(e_opt.begin(), it0, (X + 1) / 2, [](const Edge& e, int val) { return e.s < val; });
            for (auto it = it1; it != it0; ++it) {
                if (dsu.unite(it->u, it->v)) cost++;
            }
            return dsu.components == 1 && cost <= k;
        };

        if (!check(1)) return -1;

        int low = 1, high = min(200000, min_must), ans = 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (check(mid)) {
                ans = mid;
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
        int u, v, s;
        Edge(int u, int v, int s) { this.u = u; this.v = v; this.s = s; }
    }

    static class DSU {
        int[] parent;
        int components;
        DSU(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
            components = n;
        }
        DSU(DSU other) {
            this.parent = other.parent.clone();
            this.components = other.components;
        }
        int find(int i) {
            if (parent[i] == i) return i;
            return parent[i] = find(parent[i]);
        }
        boolean unite(int i, int j) {
            int root_i = find(i), root_j = find(j);
            if (root_i != root_j) {
                parent[root_i] = root_j;
                components--;
                return true;
            }
            return false;
        }
    }

    public int maxStability(int n, int[][] edges, int k) {
        List<Edge> e_must = new ArrayList<>(), e_opt = new ArrayList<>();
        int min_must = 200001;
        for (int[] e : edges) {
            if (e[3] == 1) {
                e_must.add(new Edge(e[0], e[1], e[2]));
                min_must = Math.min(min_must, e[2]);
            } else {
                e_opt.add(new Edge(e[0], e[1], e[2]));
            }
        }

        DSU base_dsu = new DSU(n);
        for (Edge e : e_must) {
            if (!base_dsu.unite(e.u, e.v)) return -1;
        }

        e_opt.sort(Comparator.comparingInt(e -> e.s));
        int[] e_opt_s = new int[e_opt.size()];
        for (int i = 0; i < e_opt.size(); i++) e_opt_s[i] = e_opt.get(i).s;

        int low = 1, high = Math.min(200000, min_must), ans = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (isValid(mid, n, e_opt, e_opt_s, base_dsu, k, min_must)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }

    private boolean isValid(int X, int n, List<Edge> e_opt, int[] e_opt_s, DSU base, int k, int min_must) {
        if (min_must < X) return false;
        DSU dsu = new DSU(base);
        int idx0 = lowerBound(e_opt_s, X);
        for (int i = idx0; i < e_opt.size(); i++) dsu.unite(e_opt.get(i).u, e_opt.get(i).v);
        int idx1 = lowerBound(e_opt_s, (X + 1) / 2);
        int cost = 0;
        for (int i = idx1; i < idx0; i++) {
            if (dsu.unite(e_opt.get(i).u, e_opt.get(i).v)) cost++;
        }
        return dsu.components == 1 && cost <= k;
    }

    private int lowerBound(int[] arr, int val) {
        int l = 0, r = arr.length;
        while (l < r) {
            int m = l + (r - l) / 2;
            if (arr[m] < val) l = m + 1;
            else r = m;
        }
        return l;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import bisect

class Solution(object):
    def maxStability(self, n, edges, k):
        e_must, e_opt = [], []
        min_must = 200001
        for u, v, s, must in edges:
            if must == 1:
                e_must.append((u, v, s))
                if s < min_must: min_must = s
            else:
                e_opt.append((u, v, s))

        parent = list(range(n))
        def find(p, i):
            while p[i] != i:
                p[i] = p[p[i]]
                i = p[i]
            return i

        comp = n
        for u, v, s in e_must:
            root_u, root_v = find(parent, u), find(parent, v)
            if root_u == root_v: return -1
            parent[root_u] = root_v
            comp -= 1

        base_parent = parent[:]
        base_comp = comp
        e_opt.sort(key=lambda x: x[2])
        e_opt_s = [x[2] for x in e_opt]

        def check(X):
            if min_must < X: return False
            p = base_parent[:]
            c = base_comp
            idx0 = bisect.bisect_left(e_opt_s, X)
            for i in range(idx0, len(e_opt)):
                u, v, s = e_opt[i]
                ru, rv = find(p, u), find(p, v)
                if ru != rv: p[ru] = rv; c -= 1
            idx1 = bisect.bisect_left(e_opt_s, (X + 1) // 2)
            cost = 0
            for i in range(idx1, idx0):
                u, v, s = e_opt[i]
                ru, rv = find(p, u), find(p, v)
                if ru != rv: p[ru] = rv; c -= 1; cost += 1
            return c == 1 and cost <= k

        low, high, ans = 1, min(200000, min_must), -1
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
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
import bisect

class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        e_must, e_opt = [], []
        min_must = 200001
        for u, v, s, must in edges:
            if must == 1:
                e_must.append((u, v, s))
                if s < min_must: min_must = s
            else:
                e_opt.append((u, v, s))

        parent = list(range(n))
        def find(p, i):
            while p[i] != i:
                p[i] = p[p[i]]
                i = p[i]
            return i

        comp = n
        for u, v, s in e_must:
            root_u, root_v = find(parent, u), find(parent, v)
            if root_u == root_v: return -1
            parent[root_u] = root_v
            comp -= 1

        base_parent = list(parent)
        base_comp = comp
        e_opt.sort(key=lambda x: x[2])
        e_opt_s = [x[2] for x in e_opt]

        def check(X):
            if min_must < X: return False
            p = list(base_parent)
            c = base_comp
            idx0 = bisect.bisect_left(e_opt_s, X)
            for i in range(idx0, len(e_opt)):
                u, v, s = e_opt[i]
                ru, rv = find(p, u), find(p, v)
                if ru != rv: p[ru] = rv; c -= 1
            idx1 = bisect.bisect_left(e_opt_s, (X + 1) // 2)
            cost = 0
            for i in range(idx1, idx0):
                u, v, s = e_opt[i]
                ru, rv = find(p, u), find(p, v)
                if ru != rv: p[ru] = rv; c -= 1; cost += 1
            return c == 1 and cost <= k

        low, high, ans = 1, min(200000, min_must), -1
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
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
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct { int u, v, s; } Edge;

int compareEdges(const void* a, const void* b) {
    return ((Edge*)a)->s - ((Edge*)b)->s;
}

int find(int* p, int i) {
    if (p[i] == i) return i;
    return p[i] = find(p, p[i]);
}

int check(int X, int n, int k, Edge* e_opt, int e_opt_size, int* base_p, int base_c, int min_must) {
    if (min_must < X) return 0;
    int* p = (int*)malloc(n * sizeof(int));
    memcpy(p, base_p, n * sizeof(int));
    int c = base_c;
    int cost = 0;

    int low = 0, high = e_opt_size;
    while(low < high) {
        int mid = low + (high - low) / 2;
        if(e_opt[mid].s < X) low = mid + 1; else high = mid;
    }
    int idx0 = low;
    for(int i = idx0; i < e_opt_size; i++) {
        int ru = find(p, e_opt[i].u), rv = find(p, e_opt[i].v);
        if(ru != rv) { p[ru] = rv; c--; }
    }

    low = 0, high = idx0;
    int val1 = (X + 1) / 2;
    while(low < high) {
        int mid = low + (high - low) / 2;
        if(e_opt[mid].s < val1) low = mid + 1; else high = mid;
    }
    int idx1 = low;
    for(int i = idx1; i < idx0; i++) {
        int ru = find(p, e_opt[i].u), rv = find(p, e_opt[i].v);
        if(ru != rv) { p[ru] = rv; c--; cost++; }
    }

    int res = (c == 1 && cost <= k);
    free(p);
    return res;
}

int maxStability(int n, int** edges, int edgesSize, int* edgesColSize, int k) {
    Edge *e_must = malloc(edgesSize * sizeof(Edge)), *e_opt = malloc(edgesSize * sizeof(Edge));
    int m_size = 0, o_size = 0, min_must = 200001;
    for(int i = 0; i < edgesSize; i++) {
        if(edges[i][3] == 1) {
            e_must[m_size++] = (Edge){edges[i][0], edges[i][1], edges[i][2]};
            if(edges[i][2] < min_must) min_must = edges[i][2];
        } else {
            e_opt[o_size++] = (Edge){edges[i][0], edges[i][1], edges[i][2]};
        }
    }

    int* base_p = malloc(n * sizeof(int));
    for(int i = 0; i < n; i++) base_p[i] = i;
    int base_c = n;
    for(int i = 0; i < m_size; i++) {
        int ru = find(base_p, e_must[i].u), rv = find(base_p, e_must[i].v);
        if(ru == rv) { free(e_must); free(e_opt); free(base_p); return -1; }
        base_p[ru] = rv; base_c--;
    }

    qsort(e_opt, o_size, sizeof(Edge), compareEdges);

    int low = 1, high = (min_must < 200000) ? min_must : 200000, ans = -1;
    while(low <= high) {
        int mid = low + (high - low) / 2;
        if(check(mid, n, k, e_opt, o_size, base_p, base_c, min_must)) { ans = mid; low = mid + 1; } else high = mid - 1;
    }
    free(e_must); free(e_opt); free(base_p);
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
    public class DSU {
        public int[] Parent;
        public int Components;
        public DSU(int n) {
            Parent = new int[n];
            for (int i = 0; i < n; i++) Parent[i] = i;
            Components = n;
        }
        public DSU(DSU other) {
            Parent = (int[])other.Parent.Clone();
            Components = other.Components;
        }
        public int Find(int i) {
            if (Parent[i] == i) return i;
            return Parent[i] = Find(Parent[i]);
        }
        public bool Unite(int i, int j) {
            int root_i = Find(i), root_j = Find(j);
            if (root_i != root_j) {
                Parent[root_i] = root_j;
                Components--;
                return true;
            }
            return false;
        }
    }

    public int MaxStability(int n, int[][] edges, int k) {
        var eMust = new List<(int u, int v, int s)>();
        var eOpt = new List<(int u, int v, int s)>();
        int minMust = 200001;
        foreach (var e in edges) {
            if (e[3] == 1) {
                eMust.Add((e[0], e[1], e[2]));
                minMust = Math.Min(minMust, e[2]);
            } else eOpt.Add((e[0], e[1], e[2]));
        }

        var baseDsu = new DSU(n);
        foreach (var e in eMust) if (!baseDsu.Unite(e.u, e.v)) return -1;

        eOpt.Sort((a, b) => a.s.CompareTo(b.s));
        int[] eOptS = new int[eOpt.Count];
        for (int i = 0; i < eOpt.Count; i++) eOptS[i] = eOpt[i].s;

        int low = 1, high = Math.Min(200000, minMust), ans = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (IsValid(mid, baseDsu, eOpt, eOptS, k, minMust)) {
                ans = mid;
                low = mid + 1;
            } else high = mid - 1;
        }
        return ans;
    }

    private bool IsValid(int X, DSU baseDsu, List<(int u, int v, int s)> eOpt, int[] eOptS, int k, int minMust) {
        if (minMust < X) return false;
        var dsu = new DSU(baseDsu);
        int idx0 = Array.BinarySearch(eOptS, X);
        if (idx0 < 0) idx0 = ~idx0;
        for (int i = idx0; i < eOpt.Count; i++) dsu.Unite(eOpt[i].u, eOpt[i].v);
        int idx1 = Array.BinarySearch(eOptS, (X + 1) / 2);
        if (idx1 < 0) idx1 = ~idx1;
        int cost = 0;
        for (int i = idx1; i < idx0; i++) if (dsu.Unite(eOpt[i].u, eOpt[i].v)) cost++;
        return dsu.Components == 1 && cost <= k;
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
 * @param {number} k
 * @return {number}
 */
var maxStability = function(n, edges, k) {
    let e_must = [], e_opt = [], min_must = 200001;
    for (let e of edges) {
        if (e[3] === 1) {
            e_must.push({u: e[0], v: e[1], s: e[2]});
            if (e[2] < min_must) min_must = e[2];
        } else {
            e_opt.push({u: e[0], v: e[1], s: e[2]});
        }
    }

    let base_parent = new Int32Array(n).map((_, i) => i);
    let base_comp = n;
    function find(p, i) {
        while (p[i] !== i) {
            p[i] = p[p[i]];
            i = p[i];
        }
        return i;
    }

    for (let e of e_must) {
        let ru = find(base_parent, e.u), rv = find(base_parent, e.v);
        if (ru === rv) return -1;
        base_parent[ru] = rv;
        base_comp--;
    }

    e_opt.sort((a, b) => a.s - b.s);
    let e_opt_s = e_opt.map(e => e.s);

    function lowerBound(arr, val) {
        let l = 0, r = arr.length;
        while (l < r) {
            let m = (l + r) >> 1;
            if (arr[m] < val) l = m + 1; else r = m;
        }
        return l;
    }

    function check(X) {
        if (min_must < X) return false;
        let p = new Int32Array(base_parent);
        let c = base_comp;
        let idx0 = lowerBound(e_opt_s, X);
        for (let i = idx0; i < e_opt.length; i++) {
            let ru = find(p, e_opt[i].u), rv = find(p, e_opt[i].v);
            if (ru !== rv) { p[ru] = rv; c--; }
        }
        let idx1 = lowerBound(e_opt_s, Math.ceil(X / 2));
        let cost = 0;
        for (let i = idx1; i < idx0; i++) {
            let ru = find(p, e_opt[i].u), rv = find(p, e_opt[i].v);
            if (ru !== rv) { p[ru] = rv; c--; cost++; }
        }
        return c === 1 && cost <= k;
    }

    let low = 1, high = Math.min(200000, min_must), ans = -1;
    while (low <= high) {
        let mid = (low + high) >> 1;
        if (check(mid)) {
            ans = mid;
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

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxStability(n: number, edges: number[][], k: number): number {
    class DSU {
        parent: Int32Array;
        size: Int32Array;
        count: number;
        constructor(n: number) {
            this.parent = new Int32Array(n);
            this.size = new Int32Array(n);
            this.count = n;
            for (let i = 0; i < n; i++) {
                this.parent[i] = i;
                this.size[i] = 1;
            }
        }
        reset() {
            this.count = n;
            for (let i = 0; i < n; i++) {
                this.parent[i] = i;
                this.size[i] = 1;
            }
        }
        find(i: number): number {
            let root = i;
            while (this.parent[root] !== root) root = this.parent[root];
            while (this.parent[i] !== root) {
                let next = this.parent[i];
                this.parent[i] = root;
                i = next;
            }
            return root;
        }
        union(i: number, j: number): boolean {
            let rootI = this.find(i);
            let rootJ = this.find(j);
            if (rootI !== rootJ) {
                if (this.size[rootI] < this.size[rootJ]) {
                    this.parent[rootI] = rootJ;
                    this.size[rootJ] += this.size[rootI];
                } else {
                    this.parent[rootJ] = rootI;
                    this.size[rootI] += this.size[rootJ];
                }
                this.count--;
                return true;
            }
            return false;
        }
    }

    const must1 = edges.filter(e => e[3] === 1);
    const must0 = edges.filter(e => e[3] === 0);
    const dsu = new DSU(n);

    for (const e of must1) {
        if (!dsu.union(e[0], e[1])) return -1;
    }

    function check(X: number): boolean {
        for (const e of must1) if (e[2] < X) return false;
        dsu.reset();
        for (const e of must1) dsu.union(e[0], e[1]);
        for (const e of must0) {
            if (e[2] >= X) dsu.union(e[0], e[1]);
            if (dsu.count === 1) break;
        }
        if (dsu.count > 1 && k > 0) {
            let upgradesUsed = 0;
            for (const e of must0) {
                if (e[2] < X && 2 * e[2] >= X) {
                    if (dsu.union(e[0], e[1])) {
                        upgradesUsed++;
                        if (upgradesUsed === k || dsu.count === 1) break;
                    }
                }
            }
        }
        return dsu.count === 1;
    }

    let low = 1, high = 200000, ans = -1;
    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        if (check(mid)) {
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

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function maxStability($n, $edges, $k) {
        $must1 = [];
        $must0 = [];
        foreach ($edges as $e) {
            if ($e[3] == 1) $must1[] = $e;
            else $must0[] = $e;
        }

        $parent = range(0, $n - 1);
        $size = array_fill(0, $n, 1);
        $count = $n;

        function find(&$parent, $i) {
            $root = $i;
            while ($parent[$root] !== $root) $root = $parent[$root];
            while ($parent[$i] !== $root) {
                $next = $parent[$i];
                $parent[$i] = $root;
                $i = $next;
            }
            return $root;
        }

        function union(&$parent, &$size, &$count, $i, $j) {
            $rootI = find($parent, $i);
            $rootJ = find($parent, $j);
            if ($rootI !== $rootJ) {
                if ($size[$rootI] < $size[$rootJ]) {
                    $parent[$rootI] = $rootJ;
                    $size[$rootJ] += $size[$rootI];
                } else {
                    $parent[$rootJ] = $rootI;
                    $size[$rootI] += $size[$rootJ];
                }
                $count--;
                return true;
            }
            return false;
        }

        foreach ($must1 as $e) {
            if (!union($parent, $size, $count, $e[0], $e[1])) return -1;
        }

        $low = 1; $high = 200000; $ans = -1;
        while ($low <= $high) {
            $mid = floor(($low + $high) / 2);
            if ($this->check($n, $must1, $must0, $k, $mid)) {
                $ans = $mid;
                $low = $mid + 1;
            } else {
                $high = $mid - 1;
            }
        }
        return $ans;
    }

    function check($n, $must1, $must0, $k, $X) {
        foreach ($must1 as $e) if ($e[2] < $X) return false;
        $parent = range(0, $n - 1);
        $size = array_fill(0, $n, 1);
        $count = $n;
        foreach ($must1 as $e) {
            $rootI = $e[0]; while($parent[$rootI] !== $rootI) $rootI = $parent[$rootI];
            $rootJ = $e[1]; while($parent[$rootJ] !== $rootJ) $rootJ = $parent[$rootJ];
            if ($rootI !== $rootJ) {
                $parent[$rootI] = $rootJ;
                $count--;
            }
        }
        foreach ($must0 as $e) {
            if ($e[2] >= $X) {
                $rootI = $e[0]; while($parent[$rootI] !== $rootI) $rootI = $parent[$rootI];
                $rootJ = $e[1]; while($parent[$rootJ] !== $rootJ) $rootJ = $parent[$rootJ];
                if ($rootI !== $rootJ) {
                    $parent[$rootI] = $rootJ;
                    $count--;
                    if ($count === 1) break;
                }
            }
        }
        if ($count > 1 && $k > 0) {
            $upgrades = 0;
            foreach ($must0 as $e) {
                if ($e[2] < $X && 2 * $e[2] >= $X) {
                    $rootI = $e[0]; while($parent[$rootI] !== $rootI) $rootI = $parent[$rootI];
                    $rootJ = $e[1]; while($parent[$rootJ] !== $rootJ) $rootJ = $parent[$rootJ];
                    if ($rootI !== $rootJ) {
                        $parent[$rootI] = $rootJ;
                        $count--;
                        $upgrades++;
                        if ($upgrades == $k || $count === 1) break;
                    }
                }
            }
        }
        return $count === 1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxStability(_ n: Int, _ edges: [[Int]], _ k: Int) -> Int {
        let must1 = edges.filter { $0[3] == 1 }
        let must0 = edges.filter { $0[3] == 0 }

        var parent = Array(0..<n)
        var count = n

        func find(_ i: Int, _ p: inout [Int]) -> Int {
            var root = i
            while p[root] != root { root = p[root] }
            var curr = i
            while p[curr] != root {
                let next = p[curr]
                p[curr] = root
                curr = next
            }
            return root
        }

        for e in must1 {
            let r1 = find(e[0], &parent), r2 = find(e[1], &parent)
            if r1 != r2 { parent[r1] = r2; count -= 1 } else { return -1 }
        }

        func check(_ X: Int) -> Bool {
            for e in must1 { if e[2] < X { return false } }
            var p = Array(0..<n), c = n
            for e in must1 {
                let r1 = find(e[0], &p), r2 = find(e[1], &p)
                if r1 != r2 { p[r1] = r2; c -= 1 }
            }
            for e in must0 where e[2] >= X {
                let r1 = find(e[0], &p), r2 = find(e[1], &p)
                if r1 != r2 { p[r1] = r2; c -= 1 }
                if c == 1 { break }
            }
            if c > 1 && k > 0 {
                var u = 0
                for e in must0 where e[2] < X && 2 * e[2] >= X {
                    let r1 = find(e[0], &p), r2 = find(e[1], &p)
                    if r1 != r2 { p[r1] = r2; c -= 1; u += 1 }
                    if u == k || c == 1 { break }
                }
            }
            return c == 1
        }

        var low = 1, high = 200000, ans = -1
        while low <= high {
            let mid = (low + high) / 2
            if check(mid) { ans = mid; low = mid + 1 } else { high = mid - 1 }
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
class Solution {
    fun maxStability(n: Int, edges: Array<IntArray>, k: Int): Int {
        val must1 = edges.filter { it[3] == 1 }
        val must0 = edges.filter { it[3] == 0 }

        class DSU(val n: Int) {
            val parent = IntArray(n) { it }
            var count = n
            fun reset() {
                for (i in 0 until n) parent[i] = i
                count = n
            }
            fun find(i: Int): Int {
                var root = i
                while (parent[root] != root) root = parent[root]
                var curr = i
                while (parent[curr] != root) {
                    val next = parent[curr]
                    parent[curr] = root
                    curr = next
                }
                return root
            }
            fun union(i: Int, j: Int): Boolean {
                val rI = find(i); val rJ = find(j)
                if (rI != rJ) { parent[rI] = rJ; count--; return true }
                return false
            }
        }

        val dsu = DSU(n)
        for (e in must1) if (!dsu.union(e[0], e[1])) return -1

        fun check(X: Int): Boolean {
            for (e in must1) if (e[2] < X) return false
            dsu.reset()
            for (e in must1) dsu.union(e[0], e[1])
            for (e in must0) {
                if (e[2] >= X) dsu.union(e[0], e[1])
                if (dsu.count == 1) break
            }
            if (dsu.count > 1 && k > 0) {
                var u = 0
                for (e in must0) {
                    if (e[2] < X && 2 * e[2] >= X) {
                        if (dsu.union(e[0], e[1])) {
                            u++; if (u == k || dsu.count == 1) break
                        }
                    }
                }
            }
            return dsu.count == 1
        }

        var low = 1; var high = 200000; var ans = -1
        while (low <= high) {
            val mid = (low + high) / 2
            if (check(mid)) { ans = mid; low = mid + 1 } else { high = mid - 1 }
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
  int maxStability(int n, List<List<int>> edges, int k) {
    final must1 = edges.where((e) => e[3] == 1).toList();
    final must0 = edges.where((e) => e[3] == 0).toList();

    List<int> parent = List.generate(n, (i) => i);
    int count = n;

    int find(int i, List<int> p) {
      int root = i;
      while (p[root] != root) root = p[root];
      while (p[i] != root) {
        int next = p[i];
        p[i] = root;
        i = next;
      }
      return root;
    }

    for (var e in must1) {
      int r1 = find(e[0], parent), r2 = find(e[1], parent);
      if (r1 != r2) { parent[r1] = r2; count--; } else return -1;
    }

    bool check(int X) {
      for (var e in must1) if (e[2] < X) return false;
      List<int> p = List.generate(n, (i) => i);
      int c = n;
      for (var e in must1) {
        int r1 = find(e[0], p), r2 = find(e[1], p);
        if (r1 != r2) { p[r1] = r2; c--; }
      }
      for (var e in must0) {
        if (e[2] >= X) {
          int r1 = find(e[0], p), r2 = find(e[1], p);
          if (r1 != r2) { p[r1] = r2; c--; }
          if (c == 1) break;
        }
      }
      if (c > 1 && k > 0) {
        int u = 0;
        for (var e in must0) {
          if (e[2] < X && 2 * e[2] >= X) {
            int r1 = find(e[0], p), r2 = find(e[1], p);
            if (r1 != r2) { p[r1] = r2; c--; u++; }
            if (u == k || c == 1) break;
          }
        }
      }
      return c == 1;
    }

    int low = 1, high = 200000, ans = -1;
    while (low <= high) {
      int mid = (low + high) ~/ 2;
      if (check(mid)) { ans = mid; low = mid + 1; } else high = mid - 1;
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
func maxStability(n int, edges [][]int, k int) int {
	type edge struct{ u, v, s int }
	var must1, must0 []edge
	for _, e := range edges {
		if e[3] == 1 {
			must1 = append(must1, edge{e[0], e[1], e[2]})
		} else {
			must0 = append(must0, edge{e[0], e[1], e[2]})
		}
	}
	parent := make([]int, n)
	find := func(p []int, i int) int {
		root := i
		for p[root] != root { root = p[root] }
		for p[i] != root { next := p[i]; p[i] = root; i = next }
		return root
	}
	for i := 0; i < n; i++ { parent[i] = i }
	count := n
	for _, e := range must1 {
		r1, r2 := find(parent, e.u), find(parent, e.v)
		if r1 != r2 { parent[r1] = r2; count-- } else { return -1 }
	}
	check := func(X int) bool {
		for _, e := range must1 { if e.s < X { return false } }
		p := make([]int, n)
		for i := 0; i < n; i++ { p[i] = i }
		c := n
		for _, e := range must1 {
			r1, r2 := find(p, e.u), find(p, e.v)
			if r1 != r2 { p[r1] = r2; c-- }
		}
		for _, e := range must0 {
			if e.s >= X {
				r1, r2 := find(p, e.u), find(p, e.v)
				if r1 != r2 { p[r1] = r2; c-- }
				if c == 1 { break }
			}
		}
		if c > 1 && k > 0 {
			u := 0
			for _, e := range must0 {
				if e.s < X && 2*e.s >= X {
					r1, r2 := find(p, e.u), find(p, e.v)
					if r1 != r2 { p[r1] = r2; c--; u++ }
					if u == k || c == 1 { break }
				}
			}
		}
		return c == 1
	}
	low, high, ans := 1, 200000, -1
	for low <= high {
		mid := (low + high) / 2
		if check(mid) { ans = mid; low = mid + 1 } else { high = mid - 1 }
	}
	return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class DSU
  attr_accessor :parent, :rank, :num_components
  def initialize(n)
    @parent = (0...n).to_a
    @rank = Array.new(n, 0)
    @num_components = n
  end
  def find(i)
    return i if @parent[i] == i
    @parent[i] = find(@parent[i])
  end
  def union(i, j)
    root_i = find(i)
    root_j = find(j)
    if root_i != root_j
      if @rank[root_i] < @rank[root_j]
        @parent[root_i] = root_j
      elsif @rank[root_i] > @rank[root_j]
        @parent[root_j] = root_i
      else
        @parent[root_i] = root_j
        @rank[root_j] += 1
      end
      @num_components -= 1
      return true
    end
    false
  end
  def initialize_copy(source)
    @parent = source.parent.dup
    @rank = source.rank.dup
    @num_components = source.num_components
  end
end

def max_stability(n, edges, k)
  must_edges = []
  optional_edges = []
  edges.each do |u, v, s, m|
    if m == 1
      must_edges << [u, v, s]
    else
      optional_edges << [u, v, s]
    end
  end
  dsu_must = DSU.new(n)
  min_must_s = 200001
  must_edges.each do |u, v, s|
    return -1 if !dsu_must.union(u, v)
    min_must_s = s if s < min_must_s
  end
  check = lambda do |x|
    return false if x > min_must_s
    dsu = dsu_must.clone
    comp = dsu.num_components
    return true if comp == 1
    optional_edges.each do |u, v, s|
      if s >= x
        if dsu.union(u, v)
          comp -= 1
          return true if comp == 1
        end
      end
    end
    upgrades = 0
    optional_edges.each do |u, v, s|
      if s < x && 2 * s >= x
        if upgrades < k
          if dsu.union(u, v)
            comp -= 1
            upgrades += 1
            return true if comp == 1
          end
        end
      end
    end
    comp == 1
  end
  low, high, ans = 1, 200000, -1
  while low <= high
    mid = (low + high) / 2
    if check.call(mid)
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
object Solution {
  class DSU(n: Int) {
    val parent: Array[Int] = Array.range(0, n)
    val rank: Array[Int] = Array.fill(n)(0)
    var numComponents: Int = n

    def find(i: Int): Int = {
      if (parent(i) == i) i
      else {
        parent(i) = find(parent(i))
        parent(i)
      }
    }

    def union(i: Int, j: Int): Boolean = {
      val rootI = find(i)
      val rootJ = find(j)
      if (rootI != rootJ) {
        if (rank(rootI) < rank(rootJ)) parent(rootI) = rootJ
        else if (rank(rootI) > rank(rootJ)) parent(rootJ) = rootI
        else {
          parent(rootI) = rootJ
          rank(rootJ) += 1
        }
        numComponents -= 1
        true
      } else false
    }

    def copy(): DSU = {
      val res = new DSU(n)
      System.arraycopy(parent, 0, res.parent, 0, n)
      System.arraycopy(rank, 0, res.rank, 0, n)
      res.numComponents = numComponents
      res
    }
  }

  def maxStability(n: Int, edges: Array[Array[Int]], k: Int): Int = {
    val mustEdges = edges.filter(_(3) == 1)
    val optionalEdges = edges.filter(_(3) == 0)
    val dsuMust = new DSU(n)
    var minMustS = 200001
    for (e <- mustEdges) {
      if (!dsuMust.union(e(0), e(1))) return -1
      if (e(2) < minMustS) minMustS = e(2)
    }

    def check(x: Int): Boolean = {
      if (x > minMustS) return false
      val dsu = dsuMust.copy()
      var comp = dsu.numComponents
      if (comp == 1) return true
      for (e <- optionalEdges if e(2) >= x) {
        if (dsu.union(e(0), e(1))) {
          comp -= 1
          if (comp == 1) return true
        }
      }
      var upgradesUsed = 0
      for (e <- optionalEdges if e(2) < x && 2 * e(2) >= x) {
        if (upgradesUsed < k) {
          if (dsu.union(e(0), e(1))) {
            comp -= 1
            upgradesUsed += 1
            if (comp == 1) return true
          }
        }
      }
      comp == 1
    }

    var low = 1
    var high = 200000
    var ans = -1
    while (low <= high) {
      val mid = low + (high - low) / 2
      if (check(mid)) {
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
impl Solution {
    pub fn max_stability(n: i32, edges: Vec<Vec<i32>>, k: i32) -> i32 {
        let mut must_edges = Vec::new();
        let mut optional_edges = Vec::new();
        for e in edges {
            if e[3] == 1 {
                must_edges.push((e[0] as usize, e[1] as usize, e[2]));
            } else {
                optional_edges.push((e[0] as usize, e[1] as usize, e[2]));
            }
        }
        let mut dsu_must = DSU::new(n as usize);
        let mut min_must_s = 200001;
        for &(u, v, s) in &must_edges {
            if !dsu_must.union(u, v) {
                return -1;
            }
            if s < min_must_s {
                min_must_s = s;
            }
        }
        let mut low = 1;
        let mut high = 200000;
        let mut ans = -1;
        while low <= high {
            let mid = low + (high - low) / 2;
            if Self::check(mid, k, min_must_s, &optional_edges, &dsu_must) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        ans
    }

    fn check(x: i32, k: i32, min_must_s: i32, optional: &[(usize, usize, i32)], dsu_must: &DSU) -> bool {
        if x > min_must_s {
            return false;
        }
        let mut dsu = dsu_must.clone();
        let mut comp = dsu.num_components;
        if comp == 1 {
            return true;
        }
        for &(u, v, s) in optional {
            if s >= x {
                if dsu.union(u, v) {
                    comp -= 1;
                    if comp == 1 {
                        return true;
                    }
                }
            }
        }
        let mut upgrades = 0;
        for &(u, v, s) in optional {
            if s < x && 2 * s >= x {
                if upgrades < k {
                    if dsu.union(u, v) {
                        comp -= 1;
                        upgrades += 1;
                        if comp == 1 {
                            return true;
                        }
                    }
                }
            }
        }
        comp == 1
    }
}

#[derive(Clone)]
struct DSU {
    parent: Vec<usize>,
    rank: Vec<usize>,
    num_components: usize,
}

impl DSU {
    fn new(n: usize) -> Self {
        Self {
            parent: (0..n).collect(),
            rank: vec![0; n],
            num_components: n,
        }
    }
    fn find(&mut self, i: usize) -> usize {
        if self.parent[i] == i {
            i
        } else {
            let root = self.find(self.parent[i]);
            self.parent[i] = root;
            root
        }
    }
    fn union(&mut self, i: usize, j: usize) -> bool {
        let root_i = self.find(i);
        let root_j = self.find(j);
        if root_i != root_j {
            if self.rank[root_i] < self.rank[root_j] {
                self.parent[root_i] = root_j;
            } else if self.rank[root_i] > self.rank[root_j] {
                self.parent[root_j] = root_i;
            } else {
                self.parent[root_i] = root_j;
                self.rank[root_j] += 1;
            }
            self.num_components -= 1;
            true
        } else {
            false
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-stability n edges k)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (define (find parent i)
    (let ([p (vector-ref parent i)])
      (if (= p i)
          i
          (let ([root (find parent p)])
            (vector-set! parent i root)
            root))))
  (define (union! parent rank i j)
    (let ([root-i (find parent i)]
          [root-j (find parent j)])
      (if (= root-i root-j)
          #f
          (let ([rank-i (vector-ref rank root-i)]
                [rank-j (vector-ref rank root-j)])
            (cond
              [(< rank-i rank-j) (vector-set! parent root-i root-j)]
              [(> rank-i rank-j) (vector-set! parent root-j root-i)]
              [else
               (vector-set! parent root-i root-j)
               (vector-set! rank root-j (+ rank-j 1))])
            #t))))
  (let* ([must-edges (filter (lambda (e) (= (fourth e) 1)) edges)]
         [opt-edges (filter (lambda (e) (= (fourth e) 0)) edges)]
         [dsu-p (vector-copy (build-vector n (lambda (i) i)))]
         [dsu-r (make-vector n 0)]
         [comp (box n)]
         [min-must (box 200001)]
         [possible (box #t)])
    (for ([e must-edges])
      (if (union! dsu-p dsu-r (first e) (second e))
          (begin
            (set-box! comp (- (unbox comp) 1))
            (if (< (third e) (unbox min-must))
                (set-box! min-must (third e)) (void)))
          (set-box! possible #f)))
    (if (not (unbox possible))
        -1
        (let* ([check (lambda (x)
                        (if (> x (unbox min-must)) #f
                            (let ([p (vector-copy dsu-p)] [r (vector-copy dsu-r)] [c (unbox comp)])
                              (let ([c2 (for/fold ([curr-c c]) ([e opt-edges] #:when (>= (third e) x))
                                          (if (union! p r (first e) (second e)) (- curr-c 1) curr-c))])
                                (if (= c2 1) #t
                                    (let-values ([(final-c final-u) (for/fold ([curr-c c2] [u 0]) ([e opt-edges] #:when (and (< (third e) x) (>= (* 2 (third e)) x)))
                                                                     (if (and (< u k) (union! p r (first e) (second e)))
                                                                         (values (- curr-c 1) (+ u 1))
                                                                         (values curr-c u)))])
                                      (= final-c 1))))))])
               [low (box 1)] [high (box 200000)] [ans (box -1)])
          (while (<= (unbox low) (unbox high))
            (let ([mid (quotient (+ (unbox low) (unbox high)) 2)])
              (if (check mid)
                  (begin (set-box! ans mid) (set-box! low (+ mid 1)))
                  (set-box! high (- mid 1)))))
          (unbox ans)))))
(define-syntax-rule (while condition body ...)
  (let loop () (when condition body ... (loop))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_stability(N :: integer(), Edges :: [[integer()]], K :: integer()) -> integer().
max_stability(N, Edges, K) ->
    MustEdges = [E || E <- Edges, lists:nth(4, E) == 1],
    OptionalEdges = [E || E <- Edges, lists:nth(4, E) == 0],
    Parent = array:from_list(lists:seq(0, N - 1)),
    Rank = array:new(N, {default, 0}),
    case build_must_dsu(MustEdges, Parent, Rank, N, 200001) of
        error -> -1;
        {DsuP, DsuR, Comp, MinMustS} -> binary_search(1, 200000, -1, K, MinMustS, OptionalEdges, DsuP, DsuR, Comp)
    end.

build_must_dsu([], P, R, C, M) -> {P, R, C, M};
build_must_dsu([[U, V, S, _] | T], P, R, C, M) ->
    {RootU, P1} = find(U, P),
    {RootV, P2} = find(V, P1),
    if RootU == RootV -> error;
       true ->
           {NewP, NewR} = union_roots(RootU, RootV, P2, R),
           build_must_dsu(T, NewP, NewR, C - 1, min(M, S))
    end.

binary_search(Low, High, Ans, K, MinMust, Opt, DsuP, DsuR, Comp) when Low =< High ->
    Mid = (Low + High) div 2,
    case check(Mid, K, MinMust, Opt, DsuP, DsuR, Comp) of
        true -> binary_search(Mid + 1, High, Mid, K, MinMust, Opt, DsuP, DsuR, Comp);
        false -> binary_search(Low, Mid - 1, Ans, K, MinMust, Opt, DsuP, DsuR, Comp)
    end;
binary_search(_, _, Ans, _, _, _, _, _, _) -> Ans.

check(X, _K, MinMustS, _Opt, _P, _R, _Comp) when X > MinMustS -> false;
check(X, K, _MinMustS, Opt, P, R, Comp) ->
    {P1, Comp1} = add_free(X, Opt, P, R, Comp),
    if Comp1 == 1 -> true;
       true -> {Comp2, _} = add_paid(X, K, Opt, P1, R, Comp1, 0), Comp2 == 1
    end.

add_free(_, [], P, _, C) -> {P, C};
add_free(X, [[U, V, S] | T], P, R, C) when S >= X ->
    {RootU, P1} = find(U, P),
    {RootV, P2} = find(V, P1),
    if RootU /= RootV ->
           {NewP, _} = union_roots(RootU, RootV, P2, R),
           if C - 1 == 1 -> {NewP, 1}; true -> add_free(X, T, NewP, R, C - 1) end;
       true -> add_free(X, T, P2, R, C)
    end;
add_free(X, [_ | T], P, R, C) -> add_free(X, T, P, R, C).

add_paid(_, _, [], _, _, C, U) -> {C, U};
add_paid(X, K, [[U, V, S] | T], P, R, C, Up) when S < X, 2 * S >= X, Up < K ->
    {RootU, P1} = find(U, P),
    {RootV, P2} = find(V, P1),
    if RootU /= RootV ->
           {NewP, _} = union_roots(RootU, RootV, P2, R),
           if C - 1 == 1 -> {1, Up + 1}; true -> add_paid(X, K, T, NewP, R, C - 1, Up + 1) end;
       true -> add_paid(X, K, T, P2, R, C, Up)
    end;
add_paid(X, K, [_ | T], P, R, C, Up) -> add_paid(X, K, T, P, R, C, Up).

find(I, P) ->
    Parent = array:get(I, P),
    if Parent == I -> {I, P};
       true ->
           {Root, NewP} = find(Parent, P),
           {Root, array:set(I, Root, NewP)}
    end.

union_roots(RootU, RootV, P, R) ->
    RankU = array:get(RootU, R), RankV = array:get(RootV, R),
    if RankU < RankV -> {array:set(RootU, RootV, P), R};
       RankU > RankV -> {array:set(RootV, RootU, P), R};
       true -> {array:set(RootU, RootV, P), array:set(RootV, RankV + 1, R)}
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_stability(n :: integer, edges :: [[integer]], k :: integer) :: integer
  def max_stability(n, edges, k) do
    must_edges = Enum.filter(edges, fn [_, _, _, m] -> m == 1 end)
    optional_edges = Enum.filter(edges, fn [_, _, _, m] -> m == 0 end) |> Enum.map(fn [u, v, s, _] -> [u, v, s] end)
    parent = :array.from_list(Enum.to_list(0..(n - 1)))
    rank = :array.new(n, default: 0)
    case build_must_dsu(must_edges, parent, rank, n, 200001) do
      :error -> -1
      {dsu_p, dsu_r, comp, min_must_s} -> binary_search(1, 200000, -1, k, min_must_s, optional_edges, dsu_p, dsu_r, comp)
    end
  end

  defp build_must_dsu([], p, r, c, m), do: {p, r, c, m}
  defp build_must_dsu([[u, v, s, _] | t], p, r, c, m) do
    {root_u, p1} = find(u, p)
    {root_v, p2} = find(v, p1)
    if root_u == root_v do
      :error
    else
      {new_p, new_r} = union_roots(root_u, root_v, p2, r)
      build_must_dsu(t, new_p, new_r, c - 1, min(m, s))
    end
  end

  defp binary_search(low, high, ans, k, min_must, opt, dsu_p, dsu_r, comp) when low <= high do
    mid = div(low + high, 2)
    if check(mid, k, min_must, opt, dsu_p, dsu_r, comp) do
      binary_search(mid + 1, high, mid, k, min_must, opt, dsu_p, dsu_r, comp)
    else
      binary_search(low, mid - 1, ans, k, min_must, opt, dsu_p, dsu_r, comp)
    end
  end
  defp binary_search(_, _, ans, _, _, _, _, _, _), do: ans

  defp check(x, _k, min_must_s, _opt, _p, _r, _comp) when x > min_must_s, do: false
  defp check(x, k, _min_must_s, opt, p, r, comp) do
    {p1, comp1} = add_free(x, opt, p, r, comp)
    if comp1 == 1 do
      true
    else
      {comp2, _} = add_paid(x, k, opt, p1, r, comp1, 0)
      comp2 == 1
    end
  end

  defp add_free(_, [], p, _, c), do: {p, c}
  defp add_free(x, [[u, v, s] | t], p, r, c) when s >= x do
    {root_u, p1} = find(u, p)
    {root_v, p2} = find(v, p1)
    if root_u != root_v do
      {new_p, _} = union_roots(root_u, root_v, p2, r)
      if c - 1 == 1, do: {new_p, 1}, else: add_free(x, t, new_p, r, c - 1)
    else
      add_free(x, t, p2, r, c)
    end
  end
  defp add_free(x, [_ | t], p, r, c), do: add_free(x, t, p, r, c)

  defp add_paid(_, _, [], _, _, c, u), do: {c, u}
  defp add_paid(x, k, [[u, v, s] | t], p, r, c, up) when s < x and 2 * s >= x and up < k do
    {root_u, p1} = find(u, p)
    {root_v, p2} = find(v, p1)
    if root_u != root_v do
      {new_p, _} = union_roots(root_u, root_v, p2, r)
      if c - 1 == 1, do: {1, up + 1}, else: add_paid(x, k, t, new_p, r, c - 1, up + 1)
    else
      add_paid(x, k, t, p2, r, c, up)
    end
  end
  defp add_paid(x, k, [_ | t], p, r, c, up), do: add_paid(x, k, t, p, r, c, up)

  defp find(i, p) do
    parent = :array.get(i, p)
    if parent == i do
      {i, p}
    else
      {root, new_p} = find(parent, p)
      {root, :array.set(i, root, new_p)}
    end
  end

  defp union_roots(root_u, root_v, p, r) do
    rank_u = :array.get(root_u, r)
    rank_v = :array.get(root_v, r)
    cond do
      rank_u < rank_v -> {:array.set(root_u, root_v, p), r}
      rank_u > rank_v -> {:array.set(root_v, root_u, p), r}
      true -> {:array.set(root_u, root_v, p), :array.set(root_v, rank_v + 1, r)}
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(M \log M + M \log(\max S) \cdot \alpha(N)), where $N$ is the number of nodes, $M$ is the number of edges, and $S$ is the maximum strength. Sorting optional edges takes $O(M \log M)$, and the binary search on stability takes $\log(\max S)$ iterations, with each check performing $O(M \alpha(N))$ DSU operations.
- **Space Complexity:** O(N + M) to store the edges, the DSU parent/rank arrays, and the pre-categorized mandatory and optional edge lists.
