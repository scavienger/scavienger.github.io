---
layout: post
title: "Palindromic Path Queries in a Tree"
date: 2026-10-29 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "String", "Divide and Conquer", "Bit Manipulation", "Tree", "Depth-First Search", "Binary Indexed Tree", "Segment Tree"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/palindromic-path-queries-in-a-tree/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<bool> palindromePath(int n, vector<vector<int>>&\
        \ edges, string s, vector<string>& queries) {\n        vector<vector<int>> adj(n);\n\
        \        for (const auto& e : edges) {\n            adj[e[0]].push_back(e[1]);\n\
        \            adj[e[1]].push_back(e[0]);\n        }\n\n        vector<int> parent(n,\
        \ -1), depth(n, 0), sz(n, 0), heavy(n, -1);\n        vector<int> order;\n  \
        \      vector<int> stack = {0};\n        parent[0] = -1;\n        while (!stack.empty())\
        \ {\n            int u = stack.back();\n            stack.pop_back();\n    \
        \        order.push_back(u);\n            for (int v : adj[u]) {\n         \
        \       if (v != parent[u]) {\n                    parent[v] = u;\n        \
        \            depth[v] = depth[u] + 1;\n                    stack.push_back(v);\n\
        \                }\n            }\n        }\n\n        for (int i = n - 1;\
        \ i >= 0; --i) {\n            int u = order[i];\n            sz[u] = 1;\n  \
        \          int max_c_sz = 0;\n            for (int v : adj[u]) {\n         \
        \       if (v != parent[u]) {\n                    sz[u] += sz[v];\n       \
        \             if (sz[v] > max_c_sz) {\n                        max_c_sz = sz[v];\n\
        \                        heavy[u] = v;\n                    }\n            \
        \    }\n            }\n        }\n\n        vector<int> head(n), pos(n);\n \
        \       int cur_pos = 1;\n        vector<pair<int, int>> hstack = {{0, 0}};\n\
        \        while (!hstack.empty()) {\n            auto [u, h] = hstack.back();\n\
        \            hstack.pop_back();\n            head[u] = h;\n            pos[u]\
        \ = cur_pos++;\n            for (int v : adj[u]) {\n                if (v !=\
        \ parent[u] && v != heavy[u]) {\n                    hstack.push_back({v, v});\n\
        \                }\n            }\n            if (heavy[u] != -1) {\n     \
        \           hstack.push_back({heavy[u], h});\n            }\n        }\n\n \
        \       vector<int> node_masks(n);\n        for (int i = 0; i < n; ++i) node_masks[i]\
        \ = 1 << (s[i] - 'a');\n\n        vector<int> bit(n + 1, 0);\n        vector<int>\
        \ node_at_pos(n + 1);\n        for (int i = 0; i < n; i++) node_at_pos[pos[i]]\
        \ = i;\n        for (int i = 1; i <= n; i++) {\n            bit[i] ^= node_masks[node_at_pos[i]];\n\
        \            int j = i + (i & -i);\n            if (j <= n) bit[j] ^= bit[i];\n\
        \        }\n\n        auto bit_update = [&](int idx, int val) {\n          \
        \  for (; idx <= n; idx += idx & -idx) bit[idx] ^= val;\n        };\n      \
        \  auto bit_query = [&](int idx) {\n            int res = 0;\n            for\
        \ (; idx > 0; idx -= idx & -idx) res ^= bit[idx];\n            return res;\n\
        \        };\n\n        vector<bool> ans;\n        for (const string& q : queries)\
        \ {\n            if (q[0] == 'u') {\n                int u = 0, i = 7;\n   \
        \             while (isdigit(q[i])) u = u * 10 + (q[i++] - '0');\n         \
        \       int new_mask = 1 << (q.back() - 'a');\n                bit_update(pos[u],\
        \ node_masks[u] ^ new_mask);\n                node_masks[u] = new_mask;\n  \
        \          } else {\n                int u = 0, v = 0, i = 6;\n            \
        \    while (isdigit(q[i])) u = u * 10 + (q[i++] - '0');\n                i++;\n\
        \                while (i < q.size()) v = v * 10 + (q[i++] - '0');\n       \
        \         int res = 0;\n                while (head[u] != head[v]) {\n     \
        \               if (depth[head[u]] < depth[head[v]]) swap(u, v);\n         \
        \           res ^= bit_query(pos[u]) ^ bit_query(pos[head[u]] - 1);\n      \
        \              u = parent[head[u]];\n                }\n                if (depth[u]\
        \ < depth[v]) swap(u, v);\n                res ^= bit_query(pos[u]) ^ bit_query(pos[v]\
        \ - 1);\n                ans.push_back((res & (res - 1LL)) == 0);\n        \
        \    }\n        }\n        return ans;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public List<Boolean> palindromePath(int\
        \ n, int[][] edges, String s, String[] queries) {\n        List<Integer>[] adj\
        \ = new ArrayList[n];\n        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();\n\
        \        for (int[] e : edges) {\n            adj[e[0]].add(e[1]);\n       \
        \     adj[e[1]].add(e[0]);\n        }\n\n        int[] parent = new int[n];\n\
        \        int[] depth = new int[n];\n        int[] sz = new int[n];\n       \
        \ int[] heavy = new int[n];\n        Arrays.fill(heavy, -1);\n\n        int[]\
        \ stack = new int[n];\n        int[] order = new int[n];\n        int top =\
        \ 0, oTop = 0;\n        stack[top++] = 0;\n        parent[0] = -1;\n       \
        \ while (top > 0) {\n            int u = stack[--top];\n            order[oTop++]\
        \ = u;\n            for (int v : adj[u]) {\n                if (v != parent[u])\
        \ {\n                    parent[v] = u;\n                    depth[v] = depth[u]\
        \ + 1;\n                    stack[top++] = v;\n                }\n         \
        \   }\n        }\n\n        for (int i = n - 1; i >= 0; i--) {\n           \
        \ int u = order[i];\n            sz[u] = 1;\n            int maxCSz = 0;\n \
        \           for (int v : adj[u]) {\n                if (v != parent[u]) {\n\
        \                    sz[u] += sz[v];\n                    if (sz[v] > maxCSz)\
        \ {\n                        maxCSz = sz[v];\n                        heavy[u]\
        \ = v;\n                    }\n                }\n            }\n        }\n\
        \n        int[] head = new int[n];\n        int[] pos = new int[n];\n      \
        \  int curPos = 1;\n        int[] stackNode = new int[n];\n        int[] stackHead\
        \ = new int[n];\n        top = 0;\n        stackNode[top] = 0; stackHead[top]\
        \ = 0; top++;\n        while (top > 0) {\n            int u = stackNode[--top];\n\
        \            int h = stackHead[top];\n            head[u] = h;\n           \
        \ pos[u] = curPos++;\n            for (int v : adj[u]) {\n                if\
        \ (v != parent[u] && v != heavy[u]) {\n                    stackNode[top] =\
        \ v; stackHead[top] = v; top++;\n                }\n            }\n        \
        \    if (heavy[u] != -1) {\n                stackNode[top] = heavy[u]; stackHead[top]\
        \ = h; top++;\n            }\n        }\n\n        int[] bit = new int[n + 1];\n\
        \        int[] nodeMasks = new int[n];\n        for (int i = 0; i < n; i++)\
        \ nodeMasks[i] = 1 << (s.charAt(i) - 'a');\n        int[] nodeAtPos = new int[n\
        \ + 1];\n        for (int i = 0; i < n; i++) nodeAtPos[pos[i]] = i;\n      \
        \  for (int i = 1; i <= n; i++) {\n            bit[i] ^= nodeMasks[nodeAtPos[i]];\n\
        \            int j = i + (i & -i);\n            if (j <= n) bit[j] ^= bit[i];\n\
        \        }\n\n        List<Boolean> ans = new ArrayList<>();\n        for (String\
        \ q : queries) {\n            String[] parts = q.split(\" \");\n           \
        \ if (parts[0].charAt(0) == 'u') {\n                int u = Integer.parseInt(parts[1]);\n\
        \                int newMask = 1 << (parts[2].charAt(0) - 'a');\n          \
        \      int diff = nodeMasks[u] ^ newMask;\n                nodeMasks[u] = newMask;\n\
        \                for (int idx = pos[u]; idx <= n; idx += idx & -idx) bit[idx]\
        \ ^= diff;\n            } else {\n                int u = Integer.parseInt(parts[1]),\
        \ v = Integer.parseInt(parts[2]);\n                int res = 0;\n          \
        \      while (head[u] != head[v]) {\n                    if (depth[head[u]]\
        \ < depth[head[v]]) { int t = u; u = v; v = t; }\n                    for (int\
        \ idx = pos[u]; idx > 0; idx -= idx & -idx) res ^= bit[idx];\n             \
        \       for (int idx = pos[head[u]] - 1; idx > 0; idx -= idx & -idx) res ^=\
        \ bit[idx];\n                    u = parent[head[u]];\n                }\n \
        \               if (depth[u] < depth[v]) { int t = u; u = v; v = t; }\n    \
        \            for (int idx = pos[u]; idx > 0; idx -= idx & -idx) res ^= bit[idx];\n\
        \                for (int idx = pos[v] - 1; idx > 0; idx -= idx & -idx) res\
        \ ^= bit[idx];\n                ans.add((res & (res - 1)) == 0);\n         \
        \   }\n        }\n        return ans;\n    }\n}"
      python: "class Solution(object):\n    def palindromePath(self, n, edges, s, queries):\n\
        \        adj = [[] for _ in range(n)]\n        for u, v in edges:\n        \
        \    adj[u].append(v)\n            adj[v].append(u)\n\n        parent = [-1]\
        \ * n\n        depth = [0] * n\n        order = []\n        stack = [0]\n  \
        \      while stack:\n            u = stack.pop()\n            order.append(u)\n\
        \            for v in adj[u]:\n                if v != parent[u]:\n        \
        \            parent[v] = u\n                    depth[v] = depth[u] + 1\n  \
        \                  stack.append(v)\n\n        sz = [1] * n\n        heavy =\
        \ [-1] * n\n        for u in reversed(order):\n            if parent[u] != -1:\n\
        \                sz[parent[u]] += sz[u]\n                if heavy[parent[u]]\
        \ == -1 or sz[u] > sz[heavy[parent[u]]]:\n                    heavy[parent[u]]\
        \ = u\n\n        head = [0] * n\n        pos = [0] * n\n        cur_pos = 1\n\
        \        stack = [(0, 0)]\n        while stack:\n            u, h = stack.pop()\n\
        \            head[u] = h\n            pos[u] = cur_pos\n            cur_pos\
        \ += 1\n            for v in adj[u]:\n                if v != parent[u] and\
        \ v != heavy[u]:\n                    stack.append((v, v))\n            if heavy[u]\
        \ != -1:\n                stack.append((heavy[u], h))\n\n        node_masks\
        \ = [1 << (ord(c) - 97) for c in s]\n        bit = [0] * (n + 1)\n        node_at_pos\
        \ = [0] * (n + 1)\n        for i in range(n): node_at_pos[pos[i]] = i\n    \
        \    for i in range(1, n + 1):\n            bit[i] ^= node_masks[node_at_pos[i]]\n\
        \            j = i + (i & -i)\n            if j <= n: bit[j] ^= bit[i]\n\n \
        \       ans = []\n        for q in queries:\n            parts = q.split()\n\
        \            if parts[0][0] == 'u':\n                u = int(parts[1])\n   \
        \             new_mask = 1 << (ord(parts[2]) - 97)\n                diff = node_masks[u]\
        \ ^ new_mask\n                node_masks[u] = new_mask\n                idx\
        \ = pos[u]\n                while idx <= n:\n                    bit[idx] ^=\
        \ diff\n                    idx += idx & -idx\n            else:\n         \
        \       u, v = int(parts[1]), int(parts[2])\n                res = 0\n     \
        \           while head[u] != head[v]:\n                    if depth[head[u]]\
        \ < depth[head[v]]: u, v = v, u\n                    idx = pos[u]\n        \
        \            while idx > 0: res ^= bit[idx]; idx -= idx & -idx\n           \
        \         idx = head_p_minus = pos[head[u]] - 1\n                    while idx\
        \ > 0: res ^= bit[idx]; idx -= idx & -idx\n                    u = parent[head[u]]\n\
        \                if depth[u] < depth[v]: u, v = v, u\n                idx =\
        \ pos[u]\n                while idx > 0: res ^= bit[idx]; idx -= idx & -idx\n\
        \                idx = pos[v] - 1\n                while idx > 0: res ^= bit[idx];\
        \ idx -= idx & -idx\n                ans.append((res & (res - 1)) == 0)\n  \
        \      return ans"
      python3: "class Solution:\n    def palindromePath(self, n: int, edges: list[list[int]],\
        \ s: str, queries: list[str]) -> list[bool]:\n        adj = [[] for _ in range(n)]\n\
        \        for u, v in edges:\n            adj[u].append(v)\n            adj[v].append(u)\n\
        \n        parent = [-1] * n\n        depth = [0] * n\n        order = []\n \
        \       stack = [0]\n        while stack:\n            u = stack.pop()\n   \
        \         order.append(u)\n            for v in adj[u]:\n                if\
        \ v != parent[u]:\n                    parent[v] = u\n                    depth[v]\
        \ = depth[u] + 1\n                    stack.append(v)\n\n        sz = [1] *\
        \ n\n        heavy = [-1] * n\n        for i in range(n - 1, -1, -1):\n    \
        \        u = order[i]\n            if parent[u] != -1:\n                p =\
        \ parent[u]\n                sz[p] += sz[u]\n                if heavy[p] ==\
        \ -1 or sz[u] > sz[heavy[p]]:\n                    heavy[p] = u\n\n        head\
        \ = [0] * n\n        pos = [0] * n\n        timer = 1\n        stack = [(0,\
        \ 0)]\n        while stack:\n            u, h = stack.pop()\n            head[u]\
        \ = h\n            pos[u] = timer\n            timer += 1\n            for v\
        \ in adj[u]:\n                if v != parent[u] and v != heavy[u]:\n       \
        \             stack.append((v, v))\n            if heavy[u] != -1:\n       \
        \         stack.append((heavy[u], h))\n\n        bit = [0] * (n + 1)\n     \
        \   def bit_update(i, val):\n            while i <= n:\n                bit[i]\
        \ ^= val\n                i += i & -i\n        def bit_query(i):\n         \
        \   res = 0\n            while i > 0:\n                res ^= bit[i]\n     \
        \           i -= i & -i\n            return res\n\n        node_masks = [(1\
        \ << (ord(c) - ord('a'))) for c in s]\n        for i in range(n):\n        \
        \    bit_update(pos[i], node_masks[i])\n\n        ans = []\n        for q in\
        \ queries:\n            parts = q.split(' ')\n            if parts[0][0] ==\
        \ 'q':\n                u, v = int(parts[1]), int(parts[2])\n              \
        \  xor_sum = 0\n                while head[u] != head[v]:\n                \
        \    if depth[head[u]] < depth[head[v]]:\n                        u, v = v,\
        \ u\n                    xor_sum ^= bit_query(pos[u]) ^ bit_query(pos[head[u]]\
        \ - 1)\n                    u = parent[head[u]]\n                if depth[u]\
        \ < depth[v]:\n                    u, v = v, u\n                xor_sum ^= bit_query(pos[u])\
        \ ^ bit_query(pos[v] - 1)\n                ans.append((xor_sum & (xor_sum -\
        \ 1)) == 0)\n            else:\n                u = int(parts[1])\n        \
        \        c = parts[2]\n                mask = 1 << (ord(c) - ord('a'))\n   \
        \             bit_update(pos[u], node_masks[u] ^ mask)\n                node_masks[u]\
        \ = mask\n        return ans"
      c: "#include <stdbool.h>\n#include <stdlib.h>\n#include <stdio.h>\n#include <string.h>\n\
        \ntypedef struct {\n    int to;\n    int next;\n} Edge;\n\nbool* palindromePath(int\
        \ n, int** edges, int edgesSize, int* edgesColSize, char* s, char** queries,\
        \ int queriesSize, int* returnSize) {\n    int* head_adj = (int*)malloc(n *\
        \ sizeof(int));\n    for (int i = 0; i < n; i++) head_adj[i] = -1;\n    Edge*\
        \ edge_list = (Edge*)malloc(2 * (n - 1) * sizeof(Edge));\n    int edge_count\
        \ = 0;\n    for (int i = 0; i < n - 1; i++) {\n        int u = edges[i][0];\n\
        \        int v = edges[i][1];\n        edge_list[edge_count].to = v; edge_list[edge_count].next\
        \ = head_adj[u];\n        head_adj[u] = edge_count++;\n        edge_list[edge_count].to\
        \ = u; edge_list[edge_count].next = head_adj[v];\n        head_adj[v] = edge_count++;\n\
        \    }\n    int* parent = (int*)malloc(n * sizeof(int));\n    int* dep = (int*)malloc(n\
        \ * sizeof(int));\n    int* order = (int*)malloc(n * sizeof(int));\n    int\
        \ h_idx = 0, t_idx = 0;\n    for (int i = 0; i < n; i++) parent[i] = -1;\n \
        \   order[t_idx++] = 0;\n    while (h_idx < t_idx) {\n        int u = order[h_idx++];\n\
        \        for (int e = head_adj[u]; e != -1; e = edge_list[e].next) {\n     \
        \       int v = edge_list[e].to;\n            if (v != parent[u]) {\n      \
        \          parent[v] = u; dep[v] = dep[u] + 1; order[t_idx++] = v;\n       \
        \     }\n        }\n    }\n    int* sz = (int*)malloc(n * sizeof(int));\n  \
        \  int* heavy = (int*)malloc(n * sizeof(int));\n    for (int i = 0; i < n; i++)\
        \ { sz[i] = 1; heavy[i] = -1; }\n    for (int i = n - 1; i >= 0; i--) {\n  \
        \      int u = order[i];\n        if (parent[u] != -1) {\n            int p\
        \ = parent[u]; sz[p] += sz[u];\n            if (heavy[p] == -1 || sz[u] > sz[heavy[p]])\
        \ heavy[p] = u;\n        }\n    }\n    int* head = (int*)malloc(n * sizeof(int));\n\
        \    int* pos = (int*)malloc(n * sizeof(int));\n    int timer = 1;\n    int*\
        \ stack = (int*)malloc(n * sizeof(int));\n    int* head_stack = (int*)malloc(n\
        \ * sizeof(int));\n    int top = 0;\n    stack[top] = 0; head_stack[top++] =\
        \ 0;\n    while (top > 0) {\n        int u = stack[--top];\n        int h =\
        \ head_stack[top];\n        head[u] = h; pos[u] = timer++;\n        for (int\
        \ e = head_adj[u]; e != -1; e = edge_list[e].next) {\n            int v = edge_list[e].to;\n\
        \            if (v != parent[u] && v != heavy[u]) {\n                stack[top]\
        \ = v; head_stack[top++] = v;\n            }\n        }\n        if (heavy[u]\
        \ != -1) { stack[top] = heavy[u]; head_stack[top++] = h; }\n    }\n    int*\
        \ bit = (int*)calloc(n + 1, sizeof(int));\n    int* node_masks = (int*)malloc(n\
        \ * sizeof(int));\n    for (int i = 0; i < n; i++) {\n        node_masks[i]\
        \ = 1 << (s[i] - 'a');\n        for (int k = pos[i]; k <= n; k += k & -k) bit[k]\
        \ ^= node_masks[i];\n    }\n    int q_count = 0;\n    for (int i = 0; i < queriesSize;\
        \ i++) if (queries[i][0] == 'q') q_count++;\n    bool* res = (bool*)malloc(q_count\
        \ * sizeof(bool));\n    int res_idx = 0;\n    for (int i = 0; i < queriesSize;\
        \ i++) {\n        if (queries[i][0] == 'q') {\n            int u, v, xor_sum\
        \ = 0;\n            sscanf(queries[i], \"query %d %d\", &u, &v);\n         \
        \   while (head[u] != head[v]) {\n                if (dep[head[u]] < dep[head[v]])\
        \ { int t = u; u = v; v = t; }\n                for (int k = pos[u]; k > 0;\
        \ k -= k & -k) xor_sum ^= bit[k];\n                for (int k = pos[head[u]]\
        \ - 1; k > 0; k -= k & -k) xor_sum ^= bit[k];\n                u = parent[head[u]];\n\
        \            }\n            if (dep[u] < dep[v]) { int t = u; u = v; v = t;\
        \ }\n            for (int k = pos[u]; k > 0; k -= k & -k) xor_sum ^= bit[k];\n\
        \            for (int k = pos[v] - 1; k > 0; k -= k & -k) xor_sum ^= bit[k];\n\
        \            res[res_idx++] = (xor_sum & (xor_sum - 1)) == 0;\n        } else\
        \ {\n            int u; char c_str[10];\n            sscanf(queries[i], \"update\
        \ %d %s\", &u, c_str);\n            int mask = 1 << (c_str[0] - 'a'), diff =\
        \ node_masks[u] ^ mask;\n            for (int k = pos[u]; k <= n; k += k & -k)\
        \ bit[k] ^= diff;\n            node_masks[u] = mask;\n        }\n    }\n   \
        \ *returnSize = res_idx;\n    free(head_adj); free(edge_list); free(parent);\
        \ free(dep); free(order);\n    free(sz); free(heavy); free(head); free(pos);\
        \ free(stack); free(head_stack); free(bit); free(node_masks);\n    return res;\n\
        }"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public IList<bool> PalindromePath(int n, int[][] edges, string s, string[]\
        \ queries) {\n        List<int>[] adj = new List<int>[n];\n        for (int\
        \ i = 0; i < n; i++) adj[i] = new List<int>();\n        foreach (var edge in\
        \ edges) {\n            adj[edge[0]].Add(edge[1]);\n            adj[edge[1]].Add(edge[0]);\n\
        \        }\n        int[] parent = new int[n];\n        int[] depth = new int[n];\n\
        \        int[] order = new int[n];\n        int headIdx = 0, tailIdx = 0;\n\
        \        for (int i = 0; i < n; i++) parent[i] = -1;\n        order[tailIdx++]\
        \ = 0;\n        while (headIdx < tailIdx) {\n            int u = order[headIdx++];\n\
        \            foreach (int v in adj[u]) {\n                if (v != parent[u])\
        \ {\n                    parent[v] = u; depth[v] = depth[u] + 1; order[tailIdx++]\
        \ = v;\n                }\n            }\n        }\n        int[] sz = new\
        \ int[n];\n        int[] heavy = new int[n];\n        for (int i = 0; i < n;\
        \ i++) { sz[i] = 1; heavy[i] = -1; }\n        for (int i = n - 1; i >= 0; i--)\
        \ {\n            int u = order[i];\n            if (parent[u] != -1) {\n   \
        \             int p = parent[u]; sz[p] += sz[u];\n                if (heavy[p]\
        \ == -1 || sz[u] > sz[heavy[p]]) heavy[p] = u;\n            }\n        }\n \
        \       int[] head = new int[n];\n        int[] pos = new int[n];\n        int\
        \ timer = 1;\n        Stack<(int, int)> stack = new Stack<(int, int)>();\n \
        \       stack.Push((0, 0));\n        while (stack.Count > 0) {\n           \
        \ var (u, h) = stack.Pop();\n            head[u] = h; pos[u] = timer++;\n  \
        \          foreach (int v in adj[u]) {\n                if (v != parent[u] &&\
        \ v != heavy[u]) stack.Push((v, v));\n            }\n            if (heavy[u]\
        \ != -1) stack.Push((heavy[u], h));\n        }\n        int[] bit = new int[n\
        \ + 1];\n        int[] nodeMasks = new int[n];\n        Action<int, int> update\
        \ = (idx, val) => {\n            for (; idx <= n; idx += idx & -idx) bit[idx]\
        \ ^= val;\n        };\n        Func<int, int> query = (idx) => {\n         \
        \   int res = 0;\n            for (; idx > 0; idx -= idx & -idx) res ^= bit[idx];\n\
        \            return res;\n        };\n        for (int i = 0; i < n; i++) {\n\
        \            nodeMasks[i] = 1 << (s[i] - 'a');\n            update(pos[i], nodeMasks[i]);\n\
        \        }\n        List<bool> results = new List<bool>();\n        foreach\
        \ (string q in queries) {\n            string[] parts = q.Split(' ');\n    \
        \        if (parts[0][0] == 'q') {\n                int u = int.Parse(parts[1]),\
        \ v = int.Parse(parts[2]), xorSum = 0;\n                while (head[u] != head[v])\
        \ {\n                    if (depth[head[u]] < depth[head[v]]) { int t = u; u\
        \ = v; v = t; }\n                    xorSum ^= query(pos[u]) ^ query(pos[head[u]]\
        \ - 1);\n                    u = parent[head[u]];\n                }\n     \
        \           if (depth[u] < depth[v]) { int t = u; u = v; v = t; }\n        \
        \        xorSum ^= query(pos[u]) ^ query(pos[v] - 1);\n                results.Add((xorSum\
        \ & (xorSum - 1)) == 0);\n            } else {\n                int u = int.Parse(parts[1]);\
        \ char c = parts[2][0];\n                int mask = 1 << (c - 'a');\n      \
        \          update(pos[u], nodeMasks[u] ^ mask);\n                nodeMasks[u]\
        \ = mask;\n            }\n        }\n        return results;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number[][]} edges\n * @param\
        \ {string} s\n * @param {string[]} queries\n * @return {boolean[]} // Must be\
        \ an array of booleans\n */\nvar palindromePath = function(n, edges, s, queries)\
        \ {\n    const adj = Array.from({length: n}, () => []);\n    for (const [u,\
        \ v] of edges) {\n        adj[u].push(v);\n        adj[v].push(u);\n    }\n\
        \    const parent = new Int32Array(n).fill(-1);\n    const dep = new Int32Array(n);\n\
        \    const order = new Int32Array(n);\n    let hIdx = 0, tIdx = 0;\n    order[tIdx++]\
        \ = 0;\n    while (hIdx < tIdx) {\n        const u = order[hIdx++];\n      \
        \  for (const v of adj[u]) {\n            if (v !== parent[u]) {\n         \
        \       parent[v] = u; dep[v] = dep[u] + 1; order[tIdx++] = v;\n           \
        \ }\n        }\n    }\n    const sz = new Int32Array(n).fill(1);\n    const\
        \ heavy = new Int32Array(n).fill(-1);\n    for (let i = n - 1; i >= 0; i--)\
        \ {\n        const u = order[i];\n        if (parent[u] !== -1) {\n        \
        \    const p = parent[u]; sz[p] += sz[u];\n            if (heavy[p] === -1 ||\
        \ sz[u] > sz[heavy[p]]) heavy[p] = u;\n        }\n    }\n    const head = new\
        \ Int32Array(n), pos = new Int32Array(n);\n    let timer = 1, stack = [[0, 0]];\n\
        \    while (stack.length > 0) {\n        const [u, h] = stack.pop();\n     \
        \   head[u] = h; pos[u] = timer++;\n        for (const v of adj[u]) {\n    \
        \        if (v !== parent[u] && v !== heavy[u]) stack.push([v, v]);\n      \
        \  }\n        if (heavy[u] !== -1) stack.push([heavy[u], h]);\n    }\n    const\
        \ bit = new Int32Array(n + 1);\n    const update = (i, val) => {\n        for\
        \ (; i <= n; i += i & -i) bit[i] ^= val;\n    };\n    const getQuery = (i) =>\
        \ {\n        let res = 0;\n        for (; i > 0; i -= i & -i) res ^= bit[i];\n\
        \        return res;\n    };\n    const nodeMasks = new Int32Array(n);\n   \
        \ for (let i = 0; i < n; i++) {\n        nodeMasks[i] = 1 << (s.charCodeAt(i)\
        \ - 97);\n        update(pos[i], nodeMasks[i]);\n    }\n    const results =\
        \ [];\n    for (const q of queries) {\n        const parts = q.split(' ');\n\
        \        if (parts[0][0] === 'q') {\n            let u = +parts[1], v = +parts[2],\
        \ xorSum = 0;\n            while (head[u] !== head[v]) {\n                if\
        \ (dep[head[u]] < dep[head[v]]) [u, v] = [v, u];\n                xorSum ^=\
        \ getQuery(pos[u]) ^ getQuery(pos[head[u]] - 1);\n                u = parent[head[u]];\n\
        \            }\n            if (dep[u] < dep[v]) [u, v] = [v, u];\n        \
        \    xorSum ^= getQuery(pos[u]) ^ getQuery(pos[v] - 1);\n            results.push((xorSum\
        \ & (xorSum - 1)) === 0);\n        } else {\n            const u = +parts[1],\
        \ c = parts[2];\n            const mask = 1 << (c.charCodeAt(0) - 97);\n   \
        \         update(pos[u], nodeMasks[u] ^ mask); nodeMasks[u] = mask;\n      \
        \  }\n    }\n    return results;\n};"
      typescript: "function palindromePath(n: number, edges: number[][], s: string,\
        \ queries: string[]): boolean[] {\n    const adj: number[][] = Array.from({\
        \ length: n }, () => []);\n    for (const [u, v] of edges) {\n        adj[u].push(v);\n\
        \        adj[v].push(u);\n    }\n\n    const parent = new Int32Array(n).fill(-1);\n\
        \    const depth = new Int32Array(n);\n    const size = new Int32Array(n).fill(1);\n\
        \    const heavy = new Int32Array(n).fill(-1);\n    const head = new Int32Array(n);\n\
        \    const pos = new Int32Array(n);\n\n    let stack = [0];\n    const visited\
        \ = new Uint8Array(n);\n    visited[0] = 1;\n    const order = new Int32Array(n);\n\
        \    let orderIdx = 0;\n\n    while (stack.length > 0) {\n        const u =\
        \ stack.pop()!;\n        order[orderIdx++] = u;\n        for (const v of adj[u])\
        \ {\n            if (!visited[v]) {\n                visited[v] = 1;\n     \
        \           parent[v] = u;\n                depth[v] = depth[u] + 1;\n     \
        \           stack.push(v);\n            }\n        }\n    }\n\n    for (let\
        \ i = n - 1; i >= 0; i--) {\n        const u = order[i];\n        if (u ===\
        \ 0) continue;\n        const p = parent[u];\n        size[p] += size[u];\n\
        \        if (heavy[p] === -1 || size[u] > size[heavy[p]]) {\n            heavy[p]\
        \ = u;\n        }\n    }\n\n    const stack2: [number, number][] = [[0, 0]];\n\
        \    let curPos = 1;\n    while (stack2.length > 0) {\n        const [u, h]\
        \ = stack2.pop()!;\n        head[u] = h;\n        pos[u] = curPos++;\n     \
        \   for (const v of adj[u]) {\n            if (v !== parent[u] && v !== heavy[u])\
        \ {\n                stack2.push([v, v]);\n            }\n        }\n      \
        \  if (heavy[u] !== -1) {\n            stack2.push([heavy[u], h]);\n       \
        \ }\n    }\n\n    const bitTree = new Int32Array(n + 1);\n    function updateBIT(idx:\
        \ number, val: number) {\n        for (; idx <= n; idx += idx & -idx) {\n  \
        \          bitTree[idx] ^= val;\n        }\n    }\n\n    function updateRange(l:\
        \ number, r: number, val: number) {\n        updateBIT(l, val);\n        if\
        \ (r + 1 <= n) updateBIT(r + 1, val);\n    }\n\n    function pointQuery(idx:\
        \ number): number {\n        let res = 0;\n        for (; idx > 0; idx -= idx\
        \ & -idx) {\n            res ^= bitTree[idx];\n        }\n        return res;\n\
        \    }\n\n    function getLCA(u: number, v: number): number {\n        while\
        \ (head[u] !== head[v]) {\n            if (depth[head[u]] > depth[head[v]])\
        \ u = parent[head[u]];\n            else v = parent[head[v]];\n        }\n \
        \       return depth[u] < depth[v] ? u : v;\n    }\n\n    const sMasks = new\
        \ Int32Array(n);\n    for (let i = 0; i < n; i++) {\n        const mask = 1\
        \ << (s.charCodeAt(i) - 97);\n        sMasks[i] = mask;\n        updateRange(pos[i],\
        \ pos[i] + size[i] - 1, mask);\n    }\n\n    const results: boolean[] = [];\n\
        \    for (const q of queries) {\n        const parts = q.split(\" \");\n   \
        \     if (parts[0] === \"update\") {\n            const u = parseInt(parts[1]);\n\
        \            const newChar = parts[2];\n            const newMask = 1 << (newChar.charCodeAt(0)\
        \ - 97);\n            const delta = sMasks[u] ^ newMask;\n            sMasks[u]\
        \ = newMask;\n            updateRange(pos[u], pos[u] + size[u] - 1, delta);\n\
        \        } else {\n            const u = parseInt(parts[1]);\n            const\
        \ v = parseInt(parts[2]);\n            const lca = getLCA(u, v);\n         \
        \   const pathXor = pointQuery(pos[u]) ^ pointQuery(pos[v]) ^ sMasks[lca];\n\
        \            results.push((pathXor & (pathXor - 1)) === 0);\n        }\n   \
        \ }\n\n    return results;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @param Integer[][]\
        \ $edges\n     * @param String $s\n     * @param String[] $queries\n     * @return\
        \ Boolean[]\n     */\n    function palindromePath($n, $edges, $s, $queries)\
        \ {\n        $adj = array_fill(0, $n, []);\n        foreach ($edges as $edge)\
        \ {\n            $adj[$edge[0]][] = $edge[1];\n            $adj[$edge[1]][]\
        \ = $edge[0];\n        }\n\n        $parent = SplFixedArray::fromArray(array_fill(0,\
        \ $n, -1));\n        $depth = SplFixedArray::fromArray(array_fill(0, $n, 0));\n\
        \        $size = SplFixedArray::fromArray(array_fill(0, $n, 1));\n        $heavy\
        \ = SplFixedArray::fromArray(array_fill(0, $n, -1));\n        $order = new SplFixedArray($n);\n\
        \        $orderIdx = 0;\n\n        $stack = [0];\n        $visited = new SplFixedArray($n);\n\
        \        $visited[0] = 1;\n        while (!empty($stack)) {\n            $u\
        \ = array_pop($stack);\n            $order[$orderIdx++] = $u;\n            foreach\
        \ ($adj[$u] as $v) {\n                if ($visited[$v] === null) {\n       \
        \             $visited[$v] = 1;\n                    $parent[$v] = $u;\n   \
        \                 $depth[$v] = $depth[$u] + 1;\n                    $stack[]\
        \ = $v;\n                }\n            }\n        }\n\n        for ($i = $n\
        \ - 1; $i >= 0; $i--) {\n            $u = $order[$i];\n            if ($u ===\
        \ 0) continue;\n            $p = $parent[$u];\n            $size[$p] += $size[$u];\n\
        \            if ($heavy[$p] === -1 || $size[$u] > $size[$heavy[$p]]) {\n   \
        \             $heavy[$p] = $u;\n            }\n        }\n\n        $head =\
        \ new SplFixedArray($n);\n        $pos = new SplFixedArray($n);\n        $stack2\
        \ = [[0, 0]];\n        $curPos = 1;\n        while (!empty($stack2)) {\n   \
        \         list($u, $h) = array_pop($stack2);\n            $head[$u] = $h;\n\
        \            $pos[$u] = $curPos++;\n            foreach ($adj[$u] as $v) {\n\
        \                if ($v !== $parent[$u] && $v !== $heavy[$u]) {\n          \
        \          $stack2[] = [$v, $v];\n                }\n            }\n       \
        \     if ($heavy[$u] !== -1) {\n                $stack2[] = [$heavy[$u], $h];\n\
        \            }\n        }\n\n        $bitTree = new SplFixedArray($n + 1);\n\
        \        for ($i = 0; $i <= $n; $i++) $bitTree[$i] = 0;\n\n        $updateBIT\
        \ = function ($idx, $val) use ($bitTree, $n) {\n            for (; $idx <= $n;\
        \ $idx += $idx & -$idx) {\n                $bitTree[$idx] ^= $val;\n       \
        \     }\n        };\n\n        $pointQuery = function ($idx) use ($bitTree)\
        \ {\n            $res = 0;\n            for (; $idx > 0; $idx -= $idx & -$idx)\
        \ {\n                $res ^= $bitTree[$idx];\n            }\n            return\
        \ $res;\n        };\n\n        $sMasks = new SplFixedArray($n);\n        for\
        \ ($i = 0; $i < $n; $i++) {\n            $mask = 1 << (ord($s[$i]) - 97);\n\
        \            $sMasks[$i] = $mask;\n            $updateBIT($pos[$i], $mask);\n\
        \            $end = $pos[$i] + $size[$i];\n            if ($end <= $n) $updateBIT($end,\
        \ $mask);\n        }\n\n        $ans = [];\n        foreach ($queries as $q)\
        \ {\n            $parts = explode(\" \", $q);\n            if ($parts[0] ===\
        \ \"update\") {\n                $u = (int)$parts[1];\n                $newMask\
        \ = 1 << (ord($parts[2]) - 97);\n                $delta = $sMasks[$u] ^ $newMask;\n\
        \                $sMasks[$u] = $newMask;\n                $updateBIT($pos[$u],\
        \ $delta);\n                $end = $pos[$u] + $size[$u];\n                if\
        \ ($end <= $n) $updateBIT($end, $delta);\n            } else {\n           \
        \     $u = (int)$parts[1];\n                $v = (int)$parts[2];\n         \
        \       $a = $u; $b = $v;\n                while ($head[$a] !== $head[$b]) {\n\
        \                    if ($depth[$head[$a]] > $depth[$head[$b]]) $a = $parent[$head[$a]];\n\
        \                    else $b = $parent[$head[$b]];\n                }\n    \
        \            $lca = $depth[$a] < $depth[$b] ? $a : $b;\n                $pathXor\
        \ = $pointQuery($pos[$u]) ^ $pointQuery($pos[$v]) ^ $sMasks[$lca];\n       \
        \         $ans[] = ($pathXor & ($pathXor - 1)) === 0;\n            }\n     \
        \   }\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func palindromePath(_ n: Int, _ edges: [[Int]],\
        \ _ s: String, _ queries: [String]) -> [Bool] {\n        var adj = Array(repeating:\
        \ [Int](), count: n)\n        for edge in edges {\n            adj[edge[0]].append(edge[1])\n\
        \            adj[edge[1]].append(edge[0])\n        }\n\n        var parent =\
        \ Array(repeating: -1, count: n)\n        var depth = Array(repeating: 0, count:\
        \ n)\n        var size = Array(repeating: 1, count: n)\n        var heavy =\
        \ Array(repeating: -1, count: n)\n        var order = Array(repeating: 0, count:\
        \ n)\n        var orderIdx = 0\n\n        var stack = [0]\n        var visited\
        \ = Array(repeating: false, count: n)\n        visited[0] = true\n        while\
        \ !stack.isEmpty {\n            let u = stack.removeLast()\n            order[orderIdx]\
        \ = u\n            orderIdx += 1\n            for v in adj[u] {\n          \
        \      if !visited[v] {\n                    visited[v] = true\n           \
        \         parent[v] = u\n                    depth[v] = depth[u] + 1\n     \
        \               stack.append(v)\n                }\n            }\n        }\n\
        \n        for i in (0..<n).reversed() {\n            let u = order[i]\n    \
        \        if u == 0 { continue }\n            let p = parent[u]\n           \
        \ size[p] += size[u]\n            if heavy[p] == -1 || size[u] > size[heavy[p]]\
        \ {\n                heavy[p] = u\n            }\n        }\n\n        var head\
        \ = Array(repeating: 0, count: n)\n        var pos = Array(repeating: 0, count:\
        \ n)\n        var stack2 = [(0, 0)]\n        var curPos = 1\n        while !stack2.isEmpty\
        \ {\n            let pair = stack2.removeLast()\n            let u = pair.0,\
        \ h = pair.1\n            head[u] = h\n            pos[u] = curPos\n       \
        \     curPos += 1\n            for v in adj[u] {\n                if v != parent[u]\
        \ && v != heavy[u] {\n                    stack2.append((v, v))\n          \
        \      }\n            }\n            if heavy[u] != -1 {\n                stack2.append((heavy[u],\
        \ h))\n            }\n        }\n\n        var bitTree = Array(repeating: 0,\
        \ count: n + 1)\n        func updateBIT(_ idx: Int, _ val: Int) {\n        \
        \    var i = idx\n            while i <= n {\n                bitTree[i] ^=\
        \ val\n                i += i & -i\n            }\n        }\n\n        func\
        \ updateRange(_ l: Int, _ r: Int, _ val: Int) {\n            updateBIT(l, val)\n\
        \            if r + 1 <= n {\n                updateBIT(r + 1, val)\n      \
        \      }\n        }\n\n        func pointQuery(_ idx: Int) -> Int {\n      \
        \      var res = 0\n            var i = idx\n            while i > 0 {\n   \
        \             res ^= bitTree[i]\n                i -= i & -i\n            }\n\
        \            return res\n        }\n\n        let sBytes = Array(s.utf8)\n \
        \       var sMasks = Array(repeating: 0, count: n)\n        for i in 0..<n {\n\
        \            let mask = 1 << (Int(sBytes[i]) - 97)\n            sMasks[i] =\
        \ mask\n            updateRange(pos[i], pos[i] + size[i] - 1, mask)\n      \
        \  }\n\n        var results = [Bool]()\n        for q in queries {\n       \
        \     let parts = q.split(separator: \" \")\n            if parts[0] == \"update\"\
        \ {\n                let u = Int(parts[1])!\n                let newChar = parts[2].first!\n\
        \                let newMask = 1 << (Int(newChar.asciiValue!) - 97)\n      \
        \          let delta = sMasks[u] ^ newMask\n                sMasks[u] = newMask\n\
        \                updateRange(pos[u], pos[u] + size[u] - 1, delta)\n        \
        \    } else {\n                let u = Int(parts[1])!\n                let v\
        \ = Int(parts[2])!\n                var a = u, b = v\n                while\
        \ head[a] != head[b] {\n                    if depth[head[a]] > depth[head[b]]\
        \ { a = parent[head[a]] }\n                    else { b = parent[head[b]] }\n\
        \                }\n                let lca = depth[a] < depth[b] ? a : b\n\
        \                let pathXor = pointQuery(pos[u]) ^ pointQuery(pos[v]) ^ sMasks[lca]\n\
        \                results.append((pathXor & (pathXor - 1)) == 0)\n          \
        \  }\n        }\n        return results\n    }\n}"
      kotlin: "class Solution {\n    fun palindromePath(n: Int, edges: Array<IntArray>,\
        \ s: String, queries: Array<String>): List<Boolean> {\n        val adj = Array(n)\
        \ { mutableListOf<Int>() }\n        for (edge in edges) {\n            adj[edge[0]].add(edge[1])\n\
        \            adj[edge[1]].add(edge[0])\n        }\n\n        val parent = IntArray(n)\
        \ { -1 }\n        val depth = IntArray(n)\n        val size = IntArray(n) {\
        \ 1 }\n        val heavy = IntArray(n) { -1 }\n        val order = IntArray(n)\n\
        \        var orderIdx = 0\n\n        val stack = java.util.ArrayDeque<Int>()\n\
        \        stack.add(0)\n        val visited = BooleanArray(n)\n        visited[0]\
        \ = true\n        while (stack.isNotEmpty()) {\n            val u = stack.removeLast()\n\
        \            order[orderIdx++] = u\n            for (v in adj[u]) {\n      \
        \          if (!visited[v]) {\n                    visited[v] = true\n     \
        \               parent[v] = u\n                    depth[v] = depth[u] + 1\n\
        \                    stack.add(v)\n                }\n            }\n      \
        \  }\n\n        for (i in n - 1 downTo 0) {\n            val u = order[i]\n\
        \            if (u == 0) continue\n            val p = parent[u]\n         \
        \   size[p] += size[u]\n            if (heavy[p] == -1 || size[u] > size[heavy[p]])\
        \ {\n                heavy[p] = u\n            }\n        }\n\n        val head\
        \ = IntArray(n)\n        val pos = IntArray(n)\n        val stack2 = java.util.ArrayDeque<Pair<Int,\
        \ Int>>()\n        stack2.add(0 to 0)\n        var curPos = 1\n        while\
        \ (stack2.isNotEmpty()) {\n            val pair = stack2.removeLast()\n    \
        \        val u = pair.first\n            val h = pair.second\n            head[u]\
        \ = h\n            pos[u] = curPos++\n            for (v in adj[u]) {\n    \
        \            if (v != parent[u] && v != heavy[u]) {\n                    stack2.add(v\
        \ to v)\n                }\n            }\n            if (heavy[u] != -1) {\n\
        \                stack2.add(heavy[u] to h)\n            }\n        }\n\n   \
        \     val bitTree = IntArray(n + 1)\n        fun updateBIT(idx: Int, valXor:\
        \ Int) {\n            var i = idx\n            while (i <= n) {\n          \
        \      bitTree[i] = bitTree[i] xor valXor\n                i += i and -i\n \
        \           }\n        }\n\n        fun updateRange(l: Int, r: Int, valXor:\
        \ Int) {\n            updateBIT(l, valXor)\n            if (r + 1 <= n) updateBIT(r\
        \ + 1, valXor)\n        }\n\n        fun pointQuery(idx: Int): Int {\n     \
        \       var res = 0\n            var i = idx\n            while (i > 0) {\n\
        \                res = res xor bitTree[i]\n                i -= i and -i\n \
        \           }\n            return res\n        }\n\n        val sMasks = IntArray(n)\n\
        \        for (i in 0 until n) {\n            val mask = 1 shl (s[i] - 'a')\n\
        \            sMasks[i] = mask\n            updateRange(pos[i], pos[i] + size[i]\
        \ - 1, mask)\n        }\n\n        val results = mutableListOf<Boolean>()\n\
        \        for (q in queries) {\n            val parts = q.split(\" \")\n    \
        \        if (parts[0] == \"update\") {\n                val u = parts[1].toInt()\n\
        \                val newChar = parts[2][0]\n                val newMask = 1\
        \ shl (newChar - 'a')\n                val delta = sMasks[u] xor newMask\n \
        \               sMasks[u] = newMask\n                updateRange(pos[u], pos[u]\
        \ + size[u] - 1, delta)\n            } else {\n                val u = parts[1].toInt()\n\
        \                val v = parts[2].toInt()\n                var a = u\n     \
        \           var b = v\n                while (head[a] != head[b]) {\n      \
        \              if (depth[head[a]] > depth[head[b]]) a = parent[head[a]]\n  \
        \                  else b = parent[head[b]]\n                }\n           \
        \     val lca = if (depth[a] < depth[b]) a else b\n                val pathXor\
        \ = pointQuery(pos[u]) xor pointQuery(pos[v]) xor sMasks[lca]\n            \
        \    results.add((pathXor.toLong() and (pathXor.toLong() - 1)) == 0L)\n    \
        \        }\n        }\n        return results\n    }\n}"
      dart: "import 'dart:typed_data';\n\nclass Solution {\n  List<bool> palindromePath(int\
        \ n, List<List<int>> edges, String s, List<String> queries) {\n    List<List<int>>\
        \ adj = List.generate(n, (_) => []);\n    for (var edge in edges) {\n      adj[edge[0]].add(edge[1]);\n\
        \      adj[edge[1]].add(edge[0]);\n    }\n\n    Int32List tin = Int32List(n);\n\
        \    Int32List tout = Int32List(n);\n    Int32List depth = Int32List(n);\n \
        \   int logn = 16;\n    Int32List up = Int32List(n * logn)..fillRange(0, n *\
        \ logn, -1);\n    int timer = 0;\n\n    List<List<int>> stack = [[0, -1, 0,\
        \ 0]]; // node, p, d, state\n    while (stack.isNotEmpty) {\n      var frame\
        \ = stack.last;\n      int u = frame[0];\n      int p = frame[1];\n      int\
        \ d = frame[2];\n      int state = frame[3];\n\n      if (state == 0) {\n  \
        \      tin[u] = ++timer;\n        depth[u] = d;\n        up[u * logn] = p;\n\
        \        frame[3] = 1;\n        for (int v in adj[u]) {\n          if (v !=\
        \ p) {\n            stack.add([v, u, d + 1, 0]);\n          }\n        }\n \
        \     } else {\n        tout[u] = timer;\n        stack.removeLast();\n    \
        \  }\n    }\n\n    for (int i = 1; i < logn; i++) {\n      for (int u = 0; u\
        \ < n; u++) {\n        int mid = up[u * logn + i - 1];\n        if (mid != -1)\
        \ {\n          up[u * logn + i] = up[mid * logn + i - 1];\n        }\n     \
        \ }\n    }\n\n    Int32List bit = Int32List(n + 2);\n    void updateBit(int\
        \ idx, int val) {\n      for (; idx < bit.length; idx += idx & -idx) {\n   \
        \     bit[idx] ^= val;\n      }\n    }\n\n    int prefixXor(int idx) {\n   \
        \   int res = 0;\n      for (; idx > 0; idx -= idx & -idx) {\n        res ^=\
        \ bit[idx];\n      }\n      return res;\n    }\n\n    Int32List currentS = Int32List(n);\n\
        \    for (int i = 0; i < n; i++) {\n      currentS[i] = 1 << (s.codeUnitAt(i)\
        \ - 97);\n      updateBit(tin[i], currentS[i]);\n      updateBit(tout[i] + 1,\
        \ currentS[i]);\n    }\n\n    int getLCA(int u, int v) {\n      if (depth[u]\
        \ < depth[v]) {\n        int tmp = u; u = v; v = tmp;\n      }\n      int diff\
        \ = depth[u] - depth[v];\n      for (int i = 0; i < logn; i++) {\n        if\
        \ (((diff >> i) & 1) == 1) {\n          u = up[u * logn + i];\n        }\n \
        \     }\n      if (u == v) return u;\n      for (int i = logn - 1; i >= 0; i--)\
        \ {\n        if (up[u * logn + i] != up[v * logn + i]) {\n          u = up[u\
        \ * logn + i];\n          v = up[v * logn + i];\n        }\n      }\n      return\
        \ up[u * logn];\n    }\n\n    List<bool> results = [];\n    for (String q in\
        \ queries) {\n      List<String> parts = q.split(' ');\n      if (parts[0] ==\
        \ 'query') {\n        int u = int.parse(parts[1]);\n        int v = int.parse(parts[2]);\n\
        \        int lca = getLCA(u, v);\n        int pathXor = prefixXor(tin[u]) ^\
        \ prefixXor(tin[v]) ^ currentS[lca];\n        results.add((pathXor & (pathXor\
        \ - 1)) == 0);\n      } else {\n        int u = int.parse(parts[1]);\n     \
        \   int newMask = 1 << (parts[2].codeUnitAt(0) - 97);\n        int diff = currentS[u]\
        \ ^ newMask;\n        updateBit(tin[u], diff);\n        updateBit(tout[u] +\
        \ 1, diff);\n        currentS[u] = newMask;\n      }\n    }\n    return results;\n\
        \  }\n}"
      go: "func palindromePath(n int, edges [][]int, s string, queries []string) []bool\
        \ {\n    adj := make([][]int, n)\n    for _, edge := range edges {\n       \
        \ u, v := edge[0], edge[1]\n        adj[u] = append(adj[u], v)\n        adj[v]\
        \ = append(adj[v], u)\n    }\n\n    tin := make([]int, n)\n    tout := make([]int,\
        \ n)\n    depth := make([]int, n)\n    logn := 16\n    up := make([]int, n*logn)\n\
        \    for i := range up { up[i] = -1 }\n    timer := 0\n\n    type frame struct\
        \ { u, p, d, state int }\n    stack := []frame{{0, -1, 0, 0}}\n    for len(stack)\
        \ > 0 {\n        f := &stack[len(stack)-1]\n        if f.state == 0 {\n    \
        \        timer++\n            tin[f.u] = timer\n            depth[f.u] = f.d\n\
        \            up[f.u*logn] = f.p\n            f.state = 1\n            for _,\
        \ v := range adj[f.u] {\n                if v != f.p {\n                   \
        \ stack = append(stack, frame{v, f.u, f.d + 1, 0})\n                }\n    \
        \        }\n        } else {\n            tout[f.u] = timer\n            stack\
        \ = stack[:len(stack)-1]\n        }\n    }\n\n    for i := 1; i < logn; i++\
        \ {\n        for u := 0; u < n; u++ {\n            mid := up[u*logn + i - 1]\n\
        \            if mid != -1 {\n                up[u*logn + i] = up[mid*logn +\
        \ i - 1]\n            }\n        }\n    }\n\n    bit := make([]int, n+2)\n \
        \   updateBit := func(idx, val int) {\n        for idx < len(bit) {\n      \
        \      bit[idx] ^= val\n            idx += idx & -idx\n        }\n    }\n  \
        \  prefixXor := func(idx int) int {\n        res := 0\n        for idx > 0 {\n\
        \            res ^= bit[idx]\n            idx -= idx & -idx\n        }\n   \
        \     return res\n    }\n\n    currentS := make([]int, n)\n    for i := 0; i\
        \ < n; i++ {\n        currentS[i] = 1 << (s[i] - 'a')\n        updateBit(tin[i],\
        \ currentS[i])\n        updateBit(tout[i]+1, currentS[i])\n    }\n\n    getLCA\
        \ := func(u, v int) int {\n        if depth[u] < depth[v] {\n            u,\
        \ v = v, u\n        }\n        diff := depth[u] - depth[v]\n        for i :=\
        \ 0; i < logn; i++ {\n            if (diff >> i) & 1 == 1 {\n              \
        \  u = up[u*logn + i]\n            }\n        }\n        if u == v { return\
        \ u }\n        for i := logn - 1; i >= 0; i-- {\n            if up[u*logn +\
        \ i] != up[v*logn + i] {\n                u = up[u*logn + i]\n             \
        \   v = up[v*logn + i]\n            }\n        }\n        return up[u*logn]\n\
        \    }\n\n    import \"strings\"\n    import \"strconv\"\n\n    results := make([]bool,\
        \ 0)\n    for _, q := range queries {\n        parts := strings.Split(q, \"\
        \ \")\n        if parts[0] == \"query\" {\n            u, _ := strconv.Atoi(parts[1])\n\
        \            v, _ := strconv.Atoi(parts[2])\n            lca := getLCA(u, v)\n\
        \            pathXor := prefixXor(tin[u]) ^ prefixXor(tin[v]) ^ currentS[lca]\n\
        \            results = append(results, (pathXor & (pathXor - 1)) == 0)\n   \
        \     } else {\n            u, _ := strconv.Atoi(parts[1])\n            newMask\
        \ := 1 << (parts[2][0] - 'a')\n            diff := currentS[u] ^ newMask\n \
        \           updateBit(tin[u], diff)\n            updateBit(tout[u]+1, diff)\n\
        \            currentS[u] = newMask\n        }\n    }\n    return results\n}"
      ruby: "def palindrome_path(n, edges, s, queries)\n  adj = Array.new(n) { [] }\n\
        \  edges.each { |u, v| adj[u] << v; adj[v] << u }\n\n  tin = Array.new(n)\n\
        \  tout = Array.new(n)\n  depth = Array.new(n, 0)\n  logn = 16\n  up = Array.new(n\
        \ * logn, -1)\n  timer = 0\n\n  stack = [[0, -1, 0, 0]]\n  while !stack.empty?\n\
        \    u, p, d, state = stack[-1]\n    if state == 0\n      timer += 1\n     \
        \ tin[u] = timer\n      depth[u] = d\n      up[u * logn] = p\n      stack[-1][3]\
        \ = 1\n      adj[u].each { |v| stack.push([v, u, d + 1, 0]) if v != p }\n  \
        \  else\n      tout[u] = timer\n      stack.pop\n    end\n  end\n\n  (1...logn).each\
        \ do |i|\n    (0...n).each do |u|\n      mid = up[u * logn + i - 1]\n      up[u\
        \ * logn + i] = mid == -1 ? -1 : up[mid * logn + i - 1]\n    end\n  end\n\n\
        \  bit = Array.new(n + 2, 0)\n  update_bit = lambda do |idx, val|\n    while\
        \ idx < bit.length\n      bit[idx] ^= val\n      idx += idx & -idx\n    end\n\
        \  end\n  prefix_xor = lambda do |idx|\n    res = 0\n    while idx > 0\n   \
        \   res ^= bit[idx]\n      idx -= idx & -idx\n    end\n    res\n  end\n\n  current_s\
        \ = Array.new(n)\n  (0...n).each do |i|\n    current_s[i] = 1 << (s[i].ord -\
        \ 97)\n    update_bit.call(tin[i], current_s[i])\n    update_bit.call(tout[i]\
        \ + 1, current_s[i])\n  end\n\n  get_lca = lambda do |u, v|\n    u, v = v, u\
        \ if depth[u] < depth[v]\n    diff = depth[u] - depth[v]\n    logn.times { |i|\
        \ u = up[u * logn + i] if (diff >> i) & 1 == 1 }\n    return u if u == v\n \
        \   (logn - 1).downto(0) do |i|\n      if up[u * logn + i] != up[v * logn +\
        \ i]\n        u = up[u * logn + i]\n        v = up[v * logn + i]\n      end\n\
        \    end\n    up[u * logn]\n  end\n\n  results = []\n  queries.each do |q|\n\
        \    parts = q.split\n    if parts[0] == \"query\"\n      u, v = parts[1].to_i,\
        \ parts[2].to_i\n      lca = get_lca.call(u, v)\n      xor_sum = prefix_xor.call(tin[u])\
        \ ^ prefix_xor.call(tin[v]) ^ current_s[lca]\n      results << ((xor_sum & (xor_sum\
        \ - 1)) == 0)\n    else\n      u, c = parts[1].to_i, parts[2]\n      new_mask\
        \ = 1 << (c.ord - 97)\n      diff = current_s[u] ^ new_mask\n      update_bit.call(tin[u],\
        \ diff)\n      update_bit.call(tout[u] + 1, diff)\n      current_s[u] = new_mask\n\
        \    end\n  end\n  results\nend"
      scala: "object Solution {\n    def palindromePath(n: Int, edges: Array[Array[Int]],\
        \ s: String, queries: Array[String]): List[Boolean] = {\n        val adj = Array.fill(n)(scala.collection.mutable.ListBuffer[Int]())\n\
        \        for (e <- edges) {\n            adj(e(0)) += e(1)\n            adj(e(1))\
        \ += e(0)\n        }\n\n        val tin = new Array[Int](n)\n        val tout\
        \ = new Array[Int](n)\n        val depth = new Array[Int](n)\n        val logn\
        \ = 16\n        val up = Array.fill(n * logn)(-1)\n        var timer = 0\n\n\
        \        val stack = scala.collection.mutable.Stack[(Int, Int, Int, Int)]()\n\
        \        stack.push((0, -1, 0, 0))\n        while (stack.nonEmpty) {\n     \
        \       val (u, p, d, state) = stack.pop()\n            if (state == 0) {\n\
        \                timer += 1\n                tin(u) = timer\n              \
        \  depth(u) = d\n                up(u * logn) = p\n                stack.push((u,\
        \ p, d, 1))\n                for (v <- adj(u)) {\n                    if (v\
        \ != p) stack.push((v, u, d + 1, 0))\n                }\n            } else\
        \ {\n                tout(u) = timer\n            }\n        }\n\n        for\
        \ (i <- 1 until logn) {\n            for (u <- 0 until n) {\n              \
        \  val mid = up(u * logn + i - 1)\n                if (mid != -1) {\n      \
        \              up(u * logn + i) = up(mid * logn + i - 1)\n                }\n\
        \            }\n        }\n\n        val bit = new Array[Int](n + 2)\n     \
        \   def updateBit(idxInit: Int, valXor: Int): Unit = {\n            var idx\
        \ = idxInit\n            while (idx < bit.length) {\n                bit(idx)\
        \ ^= valXor\n                idx += idx & -idx\n            }\n        }\n\n\
        \        def prefixXor(idxInit: Int): Int = {\n            var res = 0\n   \
        \         var idx = idxInit\n            while (idx > 0) {\n               \
        \ res ^= bit(idx)\n                idx -= idx & -idx\n            }\n      \
        \      res\n        }\n\n        val currentS = new Array[Int](n)\n        for\
        \ (i <- 0 until n) {\n            currentS(i) = 1 << (s(i) - 'a')\n        \
        \    updateBit(tin(i), currentS(i))\n            updateBit(tout(i) + 1, currentS(i))\n\
        \        }\n\n        def getLCA(uInit: Int, vInit: Int): Int = {\n        \
        \    var u = uInit\n            var v = vInit\n            if (depth(u) < depth(v))\
        \ {\n                val tmp = u; u = v; v = tmp\n            }\n          \
        \  val diff = depth(u) - depth(v)\n            for (i <- 0 until logn) {\n \
        \               if (((diff >> i) & 1) == 1) {\n                    u = up(u\
        \ * logn + i)\n                }\n            }\n            if (u == v) return\
        \ u\n            for (i <- logn - 1 to 0 by -1) {\n                if (up(u\
        \ * logn + i) != up(v * logn + i)) {\n                    u = up(u * logn +\
        \ i)\n                    v = up(v * logn + i)\n                }\n        \
        \    }\n            up(u * logn)\n        }\n\n        val results = scala.collection.mutable.ListBuffer[Boolean]()\n\
        \        for (q <- queries) {\n            val parts = q.split(\" \")\n    \
        \        if (parts(0) == \"query\") {\n                val u = parts(1).toInt\n\
        \                val v = parts(2).toInt\n                val lca = getLCA(u,\
        \ v)\n                val pathXor = prefixXor(tin(u)) ^ prefixXor(tin(v)) ^\
        \ currentS(lca)\n                results += ((pathXor & (pathXor - 1)) == 0)\n\
        \            } else {\n                val u = parts(1).toInt\n            \
        \    val newMask = 1 << (parts(2)(0) - 'a')\n                val diff = currentS(u)\
        \ ^ newMask\n                updateBit(tin(u), diff)\n                updateBit(tout(u)\
        \ + 1, diff)\n                currentS(u) = newMask\n            }\n       \
        \ }\n        results.toList\n    }\n}"
      rust: "impl Solution {\n    pub fn palindrome_path(n: i32, edges: Vec<Vec<i32>>,\
        \ s: String, queries: Vec<String>) -> Vec<bool> {\n        let n = n as usize;\n\
        \        let mut adj = vec![vec![]; n];\n        for edge in edges {\n     \
        \       adj[edge[0] as usize].push(edge[1]);\n            adj[edge[1] as usize].push(edge[0]);\n\
        \        }\n\n        let mut parent = vec![-1; n];\n        let mut depth =\
        \ vec![0; n];\n        let mut size = vec![0; n];\n        let mut heavy = vec![-1;\
        \ n];\n        let mut order = Vec::with_capacity(n);\n        let mut stack\
        \ = vec![(0, -1, 0)];\n\n        while let Some((u, p, d)) = stack.pop() {\n\
        \            order.push(u);\n            parent[u] = p;\n            depth[u]\
        \ = d;\n            for &v in &adj[u] {\n                if v != p {\n     \
        \               stack.push((v as usize, u as i32, d + 1));\n               \
        \ }\n            }\n        }\n\n        for &u in order.iter().rev() {\n  \
        \          size[u] = 1;\n            let mut max_size = 0;\n            for\
        \ &v in &adj[u] {\n                if v as i32 != parent[u] {\n            \
        \        size[u] += size[v as usize];\n                    if size[v as usize]\
        \ > max_size {\n                        max_size = size[v as usize];\n     \
        \                   heavy[u] = v;\n                    }\n                }\n\
        \            }\n        }\n\n        let mut head = vec![0; n];\n        let\
        \ mut pos = vec![0; n];\n        let mut timer = 0;\n        let mut stack2\
        \ = vec![(0, 0)];\n        while let Some((u, h)) = stack2.pop() {\n       \
        \     pos[u] = timer;\n            head[u] = h;\n            timer += 1;\n \
        \           for &v in &adj[u] {\n                let v = v as usize;\n     \
        \           if v as i32 != parent[u] && v as i32 != heavy[u] {\n           \
        \         stack2.push((v, v));\n                }\n            }\n         \
        \   if heavy[u] != -1 {\n                stack2.push((heavy[u] as usize, h));\n\
        \            }\n        }\n\n        let mut bit = vec![0; n + 1];\n       \
        \ let mut current_masks = vec![0; n];\n        let s_bytes = s.as_bytes();\n\
        \        for i in 0..n {\n            let mask = 1 << (s_bytes[i] - b'a');\n\
        \            current_masks[i] = mask;\n            Self::bit_update(pos[i] +\
        \ 1, mask, n, &mut bit);\n        }\n\n        let mut results = Vec::new();\n\
        \        for q in queries {\n            let parts: Vec<&str> = q.split(' ').collect();\n\
        \            if parts[0] == \"query\" {\n                let u = parts[1].parse::<usize>().unwrap();\n\
        \                let v = parts[2].parse::<usize>().unwrap();\n             \
        \   let res_xor = Self::path_query(u, v, &head, &pos, &parent, &depth, &bit,\
        \ n);\n                results.push((res_xor & (res_xor - 1)) == 0);\n     \
        \       } else {\n                let u = parts[1].parse::<usize>().unwrap();\n\
        \                let c = parts[2].as_bytes()[0];\n                let new_mask\
        \ = 1 << (c - b'a');\n                let delta = current_masks[u] ^ new_mask;\n\
        \                current_masks[u] = new_mask;\n                Self::bit_update(pos[u]\
        \ + 1, delta, n, &mut bit);\n            }\n        }\n\n        results\n \
        \   }\n\n    fn bit_update(mut idx: usize, delta: i32, n: usize, bit: &mut [i32])\
        \ {\n        while idx <= n {\n            bit[idx] ^= delta;\n            idx\
        \ += (idx as isize & -(idx as isize)) as usize;\n        }\n    }\n\n    fn\
        \ bit_query(mut idx: usize, bit: &[i32]) -> i32 {\n        let mut res = 0;\n\
        \        while idx > 0 {\n            res ^= bit[idx];\n            idx -= (idx\
        \ as isize & -(idx as isize)) as usize;\n        }\n        res\n    }\n\n \
        \   fn bit_query_range(l: usize, r: usize, bit: &[i32]) -> i32 {\n        Self::bit_query(r\
        \ + 1, bit) ^ Self::bit_query(l, bit)\n    }\n\n    fn path_query(mut u: usize,\
        \ mut v: usize, head: &[usize], pos: &[usize], parent: &[i32], depth: &[i32],\
        \ bit: &[i32], n: usize) -> i32 {\n        let mut res = 0;\n        while head[u]\
        \ != head[v] {\n            if depth[head[u]] < depth[head[v]] {\n         \
        \       res ^= Self::bit_query_range(pos[head[v]], pos[v], bit);\n         \
        \       v = parent[head[v]] as usize;\n            } else {\n              \
        \  res ^= Self::bit_query_range(pos[head[u]], pos[u], bit);\n              \
        \  u = parent[head[u]] as usize;\n            }\n        }\n        if depth[u]\
        \ < depth[v] {\n            res ^= Self::bit_query_range(pos[u], pos[v], bit);\n\
        \        } else {\n            res ^= Self::bit_query_range(pos[v], pos[u],\
        \ bit);\n        }\n        res\n    }\n}"
      racket: "(define/contract (palindrome-path n edges s queries)\n  (-> exact-integer?\
        \ (listof (listof exact-integer?)) string? (listof string?) (listof boolean?))\n\
        \  (let* ([adj (make-vector n '())]\n         [parent (make-vector n -1)]\n\
        \         [depth (make-vector n 0)]\n         [size (make-vector n 0)]\n   \
        \      [heavy (make-vector n -1)]\n         [head (make-vector n 0)]\n     \
        \    [pos (make-vector n 0)]\n         [bit (make-vector (+ n 1) 0)]\n     \
        \    [current-masks (make-vector n 0)])\n\n    (for ([edge edges])\n      (let\
        \ ([u (car edge)] [v (cadr edge)])\n        (vector-set! adj u (cons v (vector-ref\
        \ adj u)))\n        (vector-set! adj v (cons u (vector-ref adj v)))))\n\n  \
        \  (let ([order '()] [stack (list (list 0 -1 0))])\n      (let loop ()\n   \
        \     (unless (null? stack)\n          (let* ([curr (car stack)]\n         \
        \        [u (car curr)]\n                 [p (cadr curr)]\n                \
        \ [d (caddr curr)])\n            (set! stack (cdr stack))\n            (set!\
        \ order (cons u order))\n            (vector-set! parent u p)\n            (vector-set!\
        \ depth u d)\n            (for ([v (vector-ref adj u)])\n              (unless\
        \ (= v p)\n                (set! stack (cons (list v u (+ d 1)) stack))))\n\
        \            (loop))))\n\n      (for ([u order])\n        (let* ([u-size 1]\n\
        \               [max-s 0]\n               [h -1])\n          (for ([v (vector-ref\
        \ adj u)])\n            (unless (= v (vector-ref parent u))\n              (set!\
        \ u-size (+ u-size (vector-ref size v)))\n              (when (> (vector-ref\
        \ size v) max-s)\n                (set! max-s (vector-ref size v))\n       \
        \         (set! h v))))\n          (vector-set! size u u-size)\n          (vector-set!\
        \ heavy u h))))\n\n    (let ([timer 0] [stack (list (list 0 0))])\n      (let\
        \ loop ()\n        (unless (null? stack)\n          (let* ([curr (car stack)]\n\
        \                 [u (car curr)]\n                 [h (cadr curr)])\n      \
        \      (set! stack (cdr stack))\n            (vector-set! pos u timer)\n   \
        \         (vector-set! head u h)\n            (set! timer (+ timer 1))\n   \
        \         (for ([v (vector-ref adj u)])\n              (unless (or (= v (vector-ref\
        \ parent u)) (= v (vector-ref heavy u)))\n                (set! stack (cons\
        \ (list v v) stack))))\n            (when (not (= (vector-ref heavy u) -1))\n\
        \              (set! stack (cons (list (vector-ref heavy u) h) stack)))\n  \
        \          (loop)))))\n\n    (define (bit-update! idx delta)\n      (let loop\
        \ ([i idx])\n        (when (<= i n)\n          (vector-set! bit i (bitwise-xor\
        \ (vector-ref bit i) delta))\n          (loop (+ i (bitwise-and i (- i)))))))\n\
        \n    (define (bit-query idx)\n      (let loop ([i idx] [res 0])\n        (if\
        \ (> i 0)\n            (loop (- i (bitwise-and i (- i))) (bitwise-xor res (vector-ref\
        \ bit i)))\n            res)))\n\n    (define (bit-query-range l r)\n      (bitwise-xor\
        \ (bit-query (+ r 1)) (bit-query l)))\n\n    (define (at-most-one-bit-set? v)\n\
        \      (= (bitwise-and v (- v 1)) 0))\n\n    (for ([i (in-range n)])\n     \
        \ (let ([mask (arithmetic-shift 1 (- (char->integer (string-ref s i)) (char->integer\
        \ #\\a)))])\n        (vector-set! current-masks i mask)\n        (bit-update!\
        \ (+ (vector-ref pos i) 1) mask)))\n\n    (let ([ans '()])\n      (for ([q queries])\n\
        \        (let* ([parts (string-split q \" \")]\n               [type (car parts)])\n\
        \          (if (equal? type \"query\")\n              (let ([u (string->number\
        \ (cadr parts))]\n                    [v (string->number (caddr parts))])\n\
        \                (let loop ([u u] [v v] [res 0])\n                  (let ([hu\
        \ (vector-ref head u)] [hv (vector-ref head v)])\n                    (if (=\
        \ hu hv)\n                        (let* ([pu (vector-ref pos u)]\n         \
        \                      [pv (vector-ref pos v)]\n                           \
        \    [final-res (bitwise-xor res (if (< pu pv) (bit-query-range pu pv) (bit-query-range\
        \ pv pu)))])\n                          (set! ans (cons (at-most-one-bit-set?\
        \ final-res) ans)))\n                        (if (< (vector-ref depth hu) (vector-ref\
        \ depth hv))\n                            (loop u (vector-ref parent hv) (bitwise-xor\
        \ res (bit-query-range (vector-ref pos hv) (vector-ref pos v))))\n         \
        \                   (loop (vector-ref parent hu) v (bitwise-xor res (bit-query-range\
        \ (vector-ref pos hu) (vector-ref pos u)))))))))\n              (let* ([u (string->number\
        \ (cadr parts))]\n                     [new-c (string-ref (caddr parts) 0)]\n\
        \                     [new-mask (arithmetic-shift 1 (- (char->integer new-c)\
        \ (char->integer #\\a)))]\n                     [delta (bitwise-xor (vector-ref\
        \ current-masks u) new-mask)])\n                (vector-set! current-masks u\
        \ new-mask)\n                (bit-update! (+ (vector-ref pos u) 1) delta)))))\n\
        \      (reverse ans))))"
      erlang: "-spec palindrome_path(N :: integer(), Edges :: [[integer()]], S :: unicode:unicode_binary(),\
        \ Queries :: [unicode:unicode_binary()]) -> [boolean()].\npalindrome_path(N,\
        \ Edges, S, Queries) ->\n  Adj0 = array:new(N, {default, []}),\n  Adj = lists:foldl(fun([U,\
        \ V], A) ->\n    A1 = array:set(U, [V | array:get(U, A)], A),\n    array:set(V,\
        \ [U | array:get(V, A1)], A1)\n  end, Adj0, Edges),\n  {Parent, Depth, Order}\
        \ = dfs1_loop([{0, -1, 0}], Adj, array:new(N, {default, -1}), array:new(N, {default,\
        \ 0}), []),\n  {Size, Heavy} = lists:foldl(fun(U, {SArr, HArr}) ->\n    P =\
        \ array:get(U, Parent),\n    {USize, UHeavy, _MaxS} = lists:foldl(fun(V, {US,\
        \ UH, MS}) ->\n      if V /= P ->\n        VS = array:get(V, SArr),\n      \
        \  if VS > MS -> {US + VS, V, VS};\n        true -> {US + VS, UH, MS} end;\n\
        \      true -> {US, UH, MS} end\n    end, {1, -1, 0}, array:get(U, Adj)),\n\
        \    {array:set(U, USize, SArr), array:set(U, UHeavy, HArr)}\n  end, {array:new(N,\
        \ {default, 0}), array:new(N, {default, -1})}, Order),\n  {Head, Pos} = dfs2_loop([{0,\
        \ 0}], Adj, Parent, Heavy, 0, array:new(N, {default, -1}), array:new(N, {default,\
        \ -1})),\n  InitialMasks = array:from_list([1 bsl (C - $a) || C <- binary_to_list(S)]),\n\
        \  Bit0 = array:new(N + 1, {default, 0}),\n  Bit = lists:foldl(fun(I, B) ->\n\
        \    Mask = array:get(I, InitialMasks),\n    update_bit(array:get(I, Pos) +\
        \ 1, Mask, N, B)\n  end, Bit0, lists:seq(0, N - 1)),\n  process_queries(Queries,\
        \ N, Head, Pos, Parent, Depth, InitialMasks, Bit, []).\n\ndfs1_loop([], _Adj,\
        \ Parent, Depth, Order) -> {Parent, Depth, Order};\ndfs1_loop([{U, P, D} | Rest],\
        \ Adj, Parent, Depth, Order) ->\n  Children = [V || V <- array:get(U, Adj),\
        \ V /= P],\n  NewRest = lists:foldl(fun(V, Acc) -> [{V, U, D + 1} | Acc] end,\
        \ Rest, Children),\n  dfs1_loop(NewRest, Adj, array:set(U, P, Parent), array:set(U,\
        \ D, Depth), [U | Order]).\n\ndfs2_loop([], _Adj, _Parent, _Heavy, _Timer, Head,\
        \ Pos) -> {Head, Pos};\ndfs2_loop([{U, H} | Rest], Adj, Parent, Heavy, Timer,\
        \ Head, Pos) ->\n  NewHead = array:set(U, H, Head),\n  NewPos = array:set(U,\
        \ Timer, Pos),\n  Hvy = array:get(U, Heavy),\n  P = array:get(U, Parent),\n\
        \  Children = [V || V <- array:get(U, Adj), V /= P, V /= Hvy],\n  RestWithNonHeavy\
        \ = lists:foldl(fun(V, Acc) -> [{V, V} | Acc] end, Rest, Children),\n  NewRest\
        \ = if Hvy /= -1 -> [{Hvy, H} | RestWithNonHeavy]; true -> RestWithNonHeavy\
        \ end,\n  dfs2_loop(NewRest, Adj, Parent, Heavy, Timer + 1, NewHead, NewPos).\n\
        \nupdate_bit(Idx, Delta, N, Bit) when Idx =< N ->\n  NewBit = array:set(Idx,\
        \ array:get(Idx, Bit) bxor Delta, Bit),\n  update_bit(Idx + (Idx band -Idx),\
        \ Delta, N, NewBit);\nupdate_bit(_, _, _, Bit) -> Bit.\n\nquery_bit(0, _) ->\
        \ 0;\nquery_bit(Idx, Bit) -> array:get(Idx, Bit) bxor query_bit(Idx - (Idx band\
        \ -Idx), Bit).\n\nbit_query_range(L, R, Bit) -> query_bit(R + 1, Bit) bxor query_bit(L,\
        \ Bit).\n\nget_path_xor(U, V, Head, Pos, Parent, Depth, Bit, Acc) ->\n  HU =\
        \ array:get(U, Head),\n  HV = array:get(V, Head),\n  if HU =:= HV ->\n    PU\
        \ = array:get(U, Pos),\n    PV = array:get(V, Pos),\n    {P1, P2} = if PU <\
        \ PV -> {PU, PV}; true -> {PV, PU} end,\n    Acc bxor bit_query_range(P1, P2,\
        \ Bit);\n  true ->\n    D_HU = array:get(HU, Depth),\n    D_HV = array:get(HV,\
        \ Depth),\n    if D_HU < D_HV ->\n      get_path_xor(U, array:get(HV, Parent),\
        \ Head, Pos, Parent, Depth, Bit, Acc bxor bit_query_range(array:get(HV, Pos),\
        \ array:get(V, Pos), Bit));\n    true ->\n      get_path_xor(array:get(HU, Parent),\
        \ V, Head, Pos, Parent, Depth, Bit, Acc bxor bit_query_range(array:get(HU, Pos),\
        \ array:get(U, Pos), Bit))\n    end\n  end.\n\nprocess_queries([], _N, _Head,\
        \ _Pos, _Parent, _Depth, _Masks, _Bit, Ans) -> lists:reverse(Ans);\nprocess_queries([Q\
        \ | Rest], N, Head, Pos, Parent, Depth, Masks, Bit, Ans) ->\n  case binary:split(Q,\
        \ <<\" \">>, [global]) of\n    [<<\"query\">>, Ubin, Vbin] ->\n      U = binary_to_integer(Ubin),\n\
        \      V = binary_to_integer(Vbin),\n      Res = get_path_xor(U, V, Head, Pos,\
        \ Parent, Depth, Bit, 0),\n      process_queries(Rest, N, Head, Pos, Parent,\
        \ Depth, Masks, Bit, [(Res band (Res - 1)) =:= 0 | Ans]);\n    [<<\"update\"\
        >>, Ubin, Cbin] ->\n      U = binary_to_integer(Ubin),\n      [C] = binary_to_list(Cbin),\n\
        \      NewMask = 1 bsl (C - $a),\n      OldMask = array:get(U, Masks),\n   \
        \   Delta = OldMask bxor NewMask,\n      process_queries(Rest, N, Head, Pos,\
        \ Parent, Depth, array:set(U, NewMask, Masks), update_bit(array:get(U, Pos)\
        \ + 1, Delta, N, Bit), Ans)\n  end."
      elixir: "defmodule Solution do\n  import Bitwise\n\n  @spec palindrome_path(n\
        \ :: integer, edges :: [[integer]], s :: String.t, queries :: [String.t]) ::\
        \ [boolean]\n  def palindrome_path(n, edges, s, queries) do\n    adj = Enum.reduce(edges,\
        \ :array.new(n, default: []), fn [u, v], acc ->\n      acc |> :array.set(u,\
        \ [v | :array.get(u, acc)]) |> :array.set(v, [u | :array.get(v, acc)])\n   \
        \ end)\n\n    {parent, depth, order} = dfs1_loop([{0, -1, 0}], adj, :array.new(n,\
        \ default: -1), :array.new(n, default: 0), [])\n\n    {size, heavy} = Enum.reduce(order,\
        \ {:array.new(n, default: 0), :array.new(n, default: -1)}, fn u, {s_arr, h_arr}\
        \ ->\n      p = :array.get(u, parent)\n      {u_size, u_heavy, _max_s} = Enum.reduce(:array.get(u,\
        \ adj), {1, -1, 0}, fn v, {us, uh, ms} ->\n        if v != p do\n          vs\
        \ = :array.get(v, s_arr)\n          if vs > ms, do: {us + vs, v, vs}, else:\
        \ {us + vs, uh, ms}\n        else\n          {us, uh, ms}\n        end\n   \
        \   end)\n      {:array.set(u, u_size, s_arr), :array.set(u, u_heavy, h_arr)}\n\
        \    end)\n\n    {head, pos} = dfs2_loop([{0, 0}], adj, parent, heavy, 0, :array.new(n,\
        \ default: -1), :array.new(n, default: -1))\n\n    initial_masks = :array.from_list(for\
        \ <<c::8 <- s>>, do: 1 <<< (c - ?a))\n    bit = Enum.reduce(0..(n - 1), :array.new(n\
        \ + 1, default: 0), fn i, acc ->\n      bit_update(acc, :array.get(i, pos) +\
        \ 1, :array.get(i, initial_masks), n)\n    end)\n\n    process_queries(queries,\
        \ n, head, pos, parent, depth, initial_masks, bit, [])\n  end\n\n  defp dfs1_loop([],\
        \ _, parent, depth, order), do: {parent, depth, order}\n  defp dfs1_loop([{u,\
        \ p, d} | rest], adj, parent, depth, order) do\n    children = Enum.filter(:array.get(u,\
        \ adj), fn v -> v != p end)\n    new_rest = Enum.reduce(children, rest, fn v,\
        \ acc -> [{v, u, d + 1} | acc] end)\n    dfs1_loop(new_rest, adj, :array.set(u,\
        \ p, parent), :array.set(u, d, depth), [u | order])\n  end\n\n  defp dfs2_loop([],\
        \ _, _, _, _, head, pos), do: {head, pos}\n  defp dfs2_loop([{u, h} | rest],\
        \ adj, parent, heavy, timer, head, pos) do\n    hvy = :array.get(u, heavy)\n\
        \    p = :array.get(u, parent)\n    children = Enum.filter(:array.get(u, adj),\
        \ fn v -> v != p and v != hvy end)\n    rest_with_nh = Enum.reduce(children,\
        \ rest, fn v, acc -> [{v, v} | acc] end)\n    new_rest = if hvy != -1, do: [{hvy,\
        \ h} | rest_with_nh], else: rest_with_nh\n    dfs2_loop(new_rest, adj, parent,\
        \ heavy, timer + 1, :array.set(u, h, head), :array.set(u, timer, pos))\n  end\n\
        \n  defp bit_update(bit, idx, delta, n) when idx <= n do\n    bit_update(:array.set(idx,\
        \ :array.get(idx, bit) ^^^ delta, bit), idx + (idx &&& -idx), delta, n)\n  end\n\
        \  defp bit_update(bit, _, _, _), do: bit\n\n  defp bit_query(bit, 0), do: 0\n\
        \  defp bit_query(bit, idx), do: :array.get(idx, bit) ^^^ bit_query(bit, idx\
        \ - (idx &&& -idx))\n\n  defp bit_query_range(bit, l, r), do: bit_query(bit,\
        \ r + 1) ^^^ bit_query(bit, l)\n\n  defp get_path_xor(u, v, head, pos, parent,\
        \ depth, bit, acc) do\n    hu = :array.get(u, head)\n    hv = :array.get(v,\
        \ head)\n    if hu == hv do\n      {pu, pv} = if :array.get(u, pos) < :array.get(v,\
        \ pos), do: {:array.get(u, pos), :array.get(v, pos)}, else: {:array.get(v, pos),\
        \ :array.get(u, pos)}\n      acc ^^^ bit_query_range(bit, pu, pv)\n    else\n\
        \      if :array.get(hu, depth) < :array.get(hv, depth) do\n        get_path_xor(u,\
        \ :array.get(hv, parent), head, pos, parent, depth, bit, acc ^^^ bit_query_range(bit,\
        \ :array.get(hv, pos), :array.get(v, pos)))\n      else\n        get_path_xor(:array.get(hu,\
        \ parent), v, head, pos, parent, depth, bit, acc ^^^ bit_query_range(bit, :array.get(hu,\
        \ pos), :array.get(u, pos)))\n      end\n    end\n  end\n\n  defp process_queries([],\
        \ _, _, _, _, _, _, _, ans), do: Enum.reverse(ans)\n  defp process_queries([q\
        \ | rest], n, head, pos, parent, depth, masks, bit, ans) do\n    case String.split(q,\
        \ \" \") do\n      [\"query\", u_str, v_str] ->\n        res = get_path_xor(String.to_integer(u_str),\
        \ String.to_integer(v_str), head, pos, parent, depth, bit, 0)\n        process_queries(rest,\
        \ n, head, pos, parent, depth, masks, bit, [(res &&& (res - 1)) == 0 | ans])\n\
        \      [\"update\", u_str, c_str] ->\n        u = String.to_integer(u_str)\n\
        \        <<c::8>> = c_str\n        new_mask = 1 <<< (c - ?a)\n        old_mask\
        \ = :array.get(u, masks)\n        process_queries(rest, n, head, pos, parent,\
        \ depth, :array.set(u, new_mask, masks), bit_update(bit, :array.get(u, pos)\
        \ + 1, old_mask ^^^ new_mask, n), ans)\n    end\n  end\nend"
    approach: 'The problem asks whether the characters on a unique path between two
      nodes in a tree can be rearranged into a palindrome. A set of characters can form
      a palindrome if and only if at most one character has an odd frequency. We represent
      the frequency parity of the 26 lowercase English letters using a 26-bit integer
      mask, where the $i$-th bit is 1 if the $i$-th character appears an odd number
      of times and 0 otherwise. A mask represents a palindrome if it has at most one
      bit set, which can be checked using the condition $(mask \, \& \, (mask - 1))
      == 0$.


      To handle path queries and point updates efficiently, we use Heavy-Light Decomposition
      (HLD) combined with a Fenwick Tree (Binary Indexed Tree). HLD decomposes each
      path into $O(\log n)$ contiguous segments in the tree''s linear representation,
      and the BIT allows us to perform XOR range queries and point updates in $O(\log
      n)$ time. Point updates are performed by XORing the BIT at the node''s position
      with the XOR difference of the old and new character masks. The total time complexity
      is $O((n + q) \log^2 n)$, ensuring the solution runs efficiently within limits.'
    time_complexity: O((n + q) \log^2 n) where $n$ is the number of nodes and $q$ is
      the number of queries. Each query involves HLD decomposing the path into $O(\log
      n)$ segments, and for each segment, the Fenwick Tree performs an $O(\log n)$ operation.
      Point updates take $O(\log n)$ using the BIT.
    space_complexity: O(n) space to store the adjacency list, HLD structure (parent,
      depth, heavy child, head, position), and the Fenwick tree.
    elapsed_time: 768.2967524528503
    model: gemini-3-flash-preview
    generated_at: '2026-10-29 03:57:55 '
---

## Problem #3841: Palindromic Path Queries in a Tree

**Difficulty:** Hard

**Topics:** Array, String, Divide and Conquer, Bit Manipulation, Tree, Depth-First Search, Binary Indexed Tree, Segment Tree

## Problem Description

<p>You are given an undirected tree with <code>n</code> nodes labeled 0 to <code>n - 1</code>. This is represented by a 2D array <code>edges</code> of length <code>n - 1</code>, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> indicates an undirected edge between nodes <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code>.</p>

<p>You are also given a string <code>s</code> of length <code>n</code> consisting of lowercase English letters, where <code>s[i]</code> represents the character assigned to node <code>i</code>.</p>

<p>You are also given a string array <code>queries</code>, where each <code>queries[i]</code> is either:</p>

<ul>
	<li><code>&quot;update u<sub>i</sub> c&quot;</code>: Change the character at node <code>u<sub>i</sub></code> to <code>c</code>. Formally, update <code>s[u<sub>i</sub>] = c</code>.</li>
	<li><code>&quot;query u<sub>i</sub> v<sub>i</sub>&quot;</code>: Determine whether the string formed by the characters on the <strong>unique</strong> path from <code>u<sub>i</sub></code> to <code>v<sub>i</sub></code> (inclusive) can be <strong>rearranged</strong> into a <strong><span data-keyword="palindrome-string">palindrome</span></strong>.</li>
</ul>

<p>Return a boolean array <code>answer</code>, where <code>answer[j]</code> is <code>true</code> if the <code>j<sup>th</sup></code> query of type <code>&quot;query u<sub>i</sub> v<sub>i</sub>&quot;​​​​​​​</code> can be rearranged into a <strong>palindrome</strong>, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, edges = [[0,1],[1,2]], s = &quot;aac&quot;, queries = [&quot;query 0 2&quot;,&quot;update 1 b&quot;,&quot;query 0 2&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[true,false]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>&quot;query 0 2&quot;</code>: Path <code>0 &rarr; 1 &rarr; 2</code> gives <code>&quot;aac&quot;</code>, which can be rearranged to form <code>&quot;aca&quot;</code>, a palindrome. Thus, <code>answer[0] = true</code>.</li>
	<li><code>&quot;update 1 b&quot;</code>: Update node 1 to <code>&#39;b&#39;</code>, now <code>s = &quot;abc&quot;</code>.</li>
	<li><code>&quot;query 0 2&quot;</code>: Path characters are <code>&quot;abc&quot;</code>, which cannot be rearranged to form a palindrome. Thus, <code>answer[1] = false</code>.</li>
</ul>

<p>Thus, <code>answer = [true, false]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4, edges = [[0,1],[0,2],[0,3]], s = &quot;abca&quot;, queries = [&quot;query 1 2&quot;,&quot;update 0 b&quot;,&quot;query 2 3&quot;,&quot;update 3 a&quot;,&quot;query 1 3&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[false,false,true]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>&quot;query 1 2&quot;</code>: Path <code>1 &rarr; 0 &rarr; 2</code> gives <code>&quot;bac&quot;</code>, which cannot be rearranged to form a palindrome. Thus, <code>answer[0] = false</code>.</li>
	<li><code>&quot;update 0 b&quot;</code>: Update node 0 to <code>&#39;b&#39;</code>, now <code>s = &quot;bbca&quot;</code>.</li>
	<li><code>&quot;query 2 3&quot;</code>: Path <code>2 &rarr; 0 &rarr; 3</code> gives <code>&quot;cba&quot;</code>, which cannot be rearranged to form a palindrome. Thus, <code>answer[1] = false</code>.</li>
	<li><code>&quot;update 3 a&quot;</code>: Update node 3 to <code>&#39;a&#39;</code>, <code>s = &quot;bbca&quot;</code>.</li>
	<li><code>&quot;query 1 3&quot;</code>: Path <code>1 &rarr; 0 &rarr; 3</code> gives <code>&quot;bba&quot;</code>, which can be rearranged to form <code>&quot;bab&quot;</code>, a palindrome. Thus, <code>answer[2] = true</code>.</li>
</ul>

<p>Thus, <code>answer = [false, false, true]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li>The input is generated such that <code>edges</code> represents a valid tree.</li>
	<li><code>1 &lt;= queries.length &lt;= 5 * 10<sup>4</sup></code>​​​​​​​
	<ul>
		<li><code>queries[i] = &quot;update u<sub>i</sub> c&quot;</code> or</li>
		<li><code>queries[i] = &quot;query u<sub>i</sub> v<sub>i</sub>&quot;</code></li>
		<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n - 1</code></li>
		<li><code>c</code> is a lowercase English letter.</li>
	</ul>
	</li>
</ul>


## Hints

1. Use heavy light decomposition to break each path query into `O(log n)` segments.

2. Represent characters as a 26-bit mask and maintain segment data with XOR. A path can form a palindrome if the resulting mask has at most one bit set.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks whether the characters on a unique path between two nodes in a tree can be rearranged into a palindrome. A set of characters can form a palindrome if and only if at most one character has an odd frequency. We represent the frequency parity of the 26 lowercase English letters using a 26-bit integer mask, where the $i$-th bit is 1 if the $i$-th character appears an odd number of times and 0 otherwise. A mask represents a palindrome if it has at most one bit set, which can be checked using the condition $(mask \, \& \, (mask - 1)) == 0$.

To handle path queries and point updates efficiently, we use Heavy-Light Decomposition (HLD) combined with a Fenwick Tree (Binary Indexed Tree). HLD decomposes each path into $O(\log n)$ contiguous segments in the tree's linear representation, and the BIT allows us to perform XOR range queries and point updates in $O(\log n)$ time. Point updates are performed by XORing the BIT at the node's position with the XOR difference of the old and new character masks. The total time complexity is $O((n + q) \log^2 n)$, ensuring the solution runs efficiently within limits.

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
    vector<bool> palindromePath(int n, vector<vector<int>>& edges, string s, vector<string>& queries) {
        vector<vector<int>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }

        vector<int> parent(n, -1), depth(n, 0), sz(n, 0), heavy(n, -1);
        vector<int> order;
        vector<int> stack = {0};
        parent[0] = -1;
        while (!stack.empty()) {
            int u = stack.back();
            stack.pop_back();
            order.push_back(u);
            for (int v : adj[u]) {
                if (v != parent[u]) {
                    parent[v] = u;
                    depth[v] = depth[u] + 1;
                    stack.push_back(v);
                }
            }
        }

        for (int i = n - 1; i >= 0; --i) {
            int u = order[i];
            sz[u] = 1;
            int max_c_sz = 0;
            for (int v : adj[u]) {
                if (v != parent[u]) {
                    sz[u] += sz[v];
                    if (sz[v] > max_c_sz) {
                        max_c_sz = sz[v];
                        heavy[u] = v;
                    }
                }
            }
        }

        vector<int> head(n), pos(n);
        int cur_pos = 1;
        vector<pair<int, int>> hstack = {{0, 0}};
        while (!hstack.empty()) {
            auto [u, h] = hstack.back();
            hstack.pop_back();
            head[u] = h;
            pos[u] = cur_pos++;
            for (int v : adj[u]) {
                if (v != parent[u] && v != heavy[u]) {
                    hstack.push_back({v, v});
                }
            }
            if (heavy[u] != -1) {
                hstack.push_back({heavy[u], h});
            }
        }

        vector<int> node_masks(n);
        for (int i = 0; i < n; ++i) node_masks[i] = 1 << (s[i] - 'a');

        vector<int> bit(n + 1, 0);
        vector<int> node_at_pos(n + 1);
        for (int i = 0; i < n; i++) node_at_pos[pos[i]] = i;
        for (int i = 1; i <= n; i++) {
            bit[i] ^= node_masks[node_at_pos[i]];
            int j = i + (i & -i);
            if (j <= n) bit[j] ^= bit[i];
        }

        auto bit_update = [&](int idx, int val) {
            for (; idx <= n; idx += idx & -idx) bit[idx] ^= val;
        };
        auto bit_query = [&](int idx) {
            int res = 0;
            for (; idx > 0; idx -= idx & -idx) res ^= bit[idx];
            return res;
        };

        vector<bool> ans;
        for (const string& q : queries) {
            if (q[0] == 'u') {
                int u = 0, i = 7;
                while (isdigit(q[i])) u = u * 10 + (q[i++] - '0');
                int new_mask = 1 << (q.back() - 'a');
                bit_update(pos[u], node_masks[u] ^ new_mask);
                node_masks[u] = new_mask;
            } else {
                int u = 0, v = 0, i = 6;
                while (isdigit(q[i])) u = u * 10 + (q[i++] - '0');
                i++;
                while (i < q.size()) v = v * 10 + (q[i++] - '0');
                int res = 0;
                while (head[u] != head[v]) {
                    if (depth[head[u]] < depth[head[v]]) swap(u, v);
                    res ^= bit_query(pos[u]) ^ bit_query(pos[head[u]] - 1);
                    u = parent[head[u]];
                }
                if (depth[u] < depth[v]) swap(u, v);
                res ^= bit_query(pos[u]) ^ bit_query(pos[v] - 1);
                ans.push_back((res & (res - 1LL)) == 0);
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
    public List<Boolean> palindromePath(int n, int[][] edges, String s, String[] queries) {
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(e[1]);
            adj[e[1]].add(e[0]);
        }

        int[] parent = new int[n];
        int[] depth = new int[n];
        int[] sz = new int[n];
        int[] heavy = new int[n];
        Arrays.fill(heavy, -1);

        int[] stack = new int[n];
        int[] order = new int[n];
        int top = 0, oTop = 0;
        stack[top++] = 0;
        parent[0] = -1;
        while (top > 0) {
            int u = stack[--top];
            order[oTop++] = u;
            for (int v : adj[u]) {
                if (v != parent[u]) {
                    parent[v] = u;
                    depth[v] = depth[u] + 1;
                    stack[top++] = v;
                }
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            int u = order[i];
            sz[u] = 1;
            int maxCSz = 0;
            for (int v : adj[u]) {
                if (v != parent[u]) {
                    sz[u] += sz[v];
                    if (sz[v] > maxCSz) {
                        maxCSz = sz[v];
                        heavy[u] = v;
                    }
                }
            }
        }

        int[] head = new int[n];
        int[] pos = new int[n];
        int curPos = 1;
        int[] stackNode = new int[n];
        int[] stackHead = new int[n];
        top = 0;
        stackNode[top] = 0; stackHead[top] = 0; top++;
        while (top > 0) {
            int u = stackNode[--top];
            int h = stackHead[top];
            head[u] = h;
            pos[u] = curPos++;
            for (int v : adj[u]) {
                if (v != parent[u] && v != heavy[u]) {
                    stackNode[top] = v; stackHead[top] = v; top++;
                }
            }
            if (heavy[u] != -1) {
                stackNode[top] = heavy[u]; stackHead[top] = h; top++;
            }
        }

        int[] bit = new int[n + 1];
        int[] nodeMasks = new int[n];
        for (int i = 0; i < n; i++) nodeMasks[i] = 1 << (s.charAt(i) - 'a');
        int[] nodeAtPos = new int[n + 1];
        for (int i = 0; i < n; i++) nodeAtPos[pos[i]] = i;
        for (int i = 1; i <= n; i++) {
            bit[i] ^= nodeMasks[nodeAtPos[i]];
            int j = i + (i & -i);
            if (j <= n) bit[j] ^= bit[i];
        }

        List<Boolean> ans = new ArrayList<>();
        for (String q : queries) {
            String[] parts = q.split(" ");
            if (parts[0].charAt(0) == 'u') {
                int u = Integer.parseInt(parts[1]);
                int newMask = 1 << (parts[2].charAt(0) - 'a');
                int diff = nodeMasks[u] ^ newMask;
                nodeMasks[u] = newMask;
                for (int idx = pos[u]; idx <= n; idx += idx & -idx) bit[idx] ^= diff;
            } else {
                int u = Integer.parseInt(parts[1]), v = Integer.parseInt(parts[2]);
                int res = 0;
                while (head[u] != head[v]) {
                    if (depth[head[u]] < depth[head[v]]) { int t = u; u = v; v = t; }
                    for (int idx = pos[u]; idx > 0; idx -= idx & -idx) res ^= bit[idx];
                    for (int idx = pos[head[u]] - 1; idx > 0; idx -= idx & -idx) res ^= bit[idx];
                    u = parent[head[u]];
                }
                if (depth[u] < depth[v]) { int t = u; u = v; v = t; }
                for (int idx = pos[u]; idx > 0; idx -= idx & -idx) res ^= bit[idx];
                for (int idx = pos[v] - 1; idx > 0; idx -= idx & -idx) res ^= bit[idx];
                ans.add((res & (res - 1)) == 0);
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
class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)

        sz = [1] * n
        heavy = [-1] * n
        for u in reversed(order):
            if parent[u] != -1:
                sz[parent[u]] += sz[u]
                if heavy[parent[u]] == -1 or sz[u] > sz[heavy[parent[u]]]:
                    heavy[parent[u]] = u

        head = [0] * n
        pos = [0] * n
        cur_pos = 1
        stack = [(0, 0)]
        while stack:
            u, h = stack.pop()
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    stack.append((v, v))
            if heavy[u] != -1:
                stack.append((heavy[u], h))

        node_masks = [1 << (ord(c) - 97) for c in s]
        bit = [0] * (n + 1)
        node_at_pos = [0] * (n + 1)
        for i in range(n): node_at_pos[pos[i]] = i
        for i in range(1, n + 1):
            bit[i] ^= node_masks[node_at_pos[i]]
            j = i + (i & -i)
            if j <= n: bit[j] ^= bit[i]

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0][0] == 'u':
                u = int(parts[1])
                new_mask = 1 << (ord(parts[2]) - 97)
                diff = node_masks[u] ^ new_mask
                node_masks[u] = new_mask
                idx = pos[u]
                while idx <= n:
                    bit[idx] ^= diff
                    idx += idx & -idx
            else:
                u, v = int(parts[1]), int(parts[2])
                res = 0
                while head[u] != head[v]:
                    if depth[head[u]] < depth[head[v]]: u, v = v, u
                    idx = pos[u]
                    while idx > 0: res ^= bit[idx]; idx -= idx & -idx
                    idx = head_p_minus = pos[head[u]] - 1
                    while idx > 0: res ^= bit[idx]; idx -= idx & -idx
                    u = parent[head[u]]
                if depth[u] < depth[v]: u, v = v, u
                idx = pos[u]
                while idx > 0: res ^= bit[idx]; idx -= idx & -idx
                idx = pos[v] - 1
                while idx > 0: res ^= bit[idx]; idx -= idx & -idx
                ans.append((res & (res - 1)) == 0)
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)

        sz = [1] * n
        heavy = [-1] * n
        for i in range(n - 1, -1, -1):
            u = order[i]
            if parent[u] != -1:
                p = parent[u]
                sz[p] += sz[u]
                if heavy[p] == -1 or sz[u] > sz[heavy[p]]:
                    heavy[p] = u

        head = [0] * n
        pos = [0] * n
        timer = 1
        stack = [(0, 0)]
        while stack:
            u, h = stack.pop()
            head[u] = h
            pos[u] = timer
            timer += 1
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    stack.append((v, v))
            if heavy[u] != -1:
                stack.append((heavy[u], h))

        bit = [0] * (n + 1)
        def bit_update(i, val):
            while i <= n:
                bit[i] ^= val
                i += i & -i
        def bit_query(i):
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        node_masks = [(1 << (ord(c) - ord('a'))) for c in s]
        for i in range(n):
            bit_update(pos[i], node_masks[i])

        ans = []
        for q in queries:
            parts = q.split(' ')
            if parts[0][0] == 'q':
                u, v = int(parts[1]), int(parts[2])
                xor_sum = 0
                while head[u] != head[v]:
                    if depth[head[u]] < depth[head[v]]:
                        u, v = v, u
                    xor_sum ^= bit_query(pos[u]) ^ bit_query(pos[head[u]] - 1)
                    u = parent[head[u]]
                if depth[u] < depth[v]:
                    u, v = v, u
                xor_sum ^= bit_query(pos[u]) ^ bit_query(pos[v] - 1)
                ans.append((xor_sum & (xor_sum - 1)) == 0)
            else:
                u = int(parts[1])
                c = parts[2]
                mask = 1 << (ord(c) - ord('a'))
                bit_update(pos[u], node_masks[u] ^ mask)
                node_masks[u] = mask
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct {
    int to;
    int next;
} Edge;

bool* palindromePath(int n, int** edges, int edgesSize, int* edgesColSize, char* s, char** queries, int queriesSize, int* returnSize) {
    int* head_adj = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) head_adj[i] = -1;
    Edge* edge_list = (Edge*)malloc(2 * (n - 1) * sizeof(Edge));
    int edge_count = 0;
    for (int i = 0; i < n - 1; i++) {
        int u = edges[i][0];
        int v = edges[i][1];
        edge_list[edge_count].to = v; edge_list[edge_count].next = head_adj[u];
        head_adj[u] = edge_count++;
        edge_list[edge_count].to = u; edge_list[edge_count].next = head_adj[v];
        head_adj[v] = edge_count++;
    }
    int* parent = (int*)malloc(n * sizeof(int));
    int* dep = (int*)malloc(n * sizeof(int));
    int* order = (int*)malloc(n * sizeof(int));
    int h_idx = 0, t_idx = 0;
    for (int i = 0; i < n; i++) parent[i] = -1;
    order[t_idx++] = 0;
    while (h_idx < t_idx) {
        int u = order[h_idx++];
        for (int e = head_adj[u]; e != -1; e = edge_list[e].next) {
            int v = edge_list[e].to;
            if (v != parent[u]) {
                parent[v] = u; dep[v] = dep[u] + 1; order[t_idx++] = v;
            }
        }
    }
    int* sz = (int*)malloc(n * sizeof(int));
    int* heavy = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) { sz[i] = 1; heavy[i] = -1; }
    for (int i = n - 1; i >= 0; i--) {
        int u = order[i];
        if (parent[u] != -1) {
            int p = parent[u]; sz[p] += sz[u];
            if (heavy[p] == -1 || sz[u] > sz[heavy[p]]) heavy[p] = u;
        }
    }
    int* head = (int*)malloc(n * sizeof(int));
    int* pos = (int*)malloc(n * sizeof(int));
    int timer = 1;
    int* stack = (int*)malloc(n * sizeof(int));
    int* head_stack = (int*)malloc(n * sizeof(int));
    int top = 0;
    stack[top] = 0; head_stack[top++] = 0;
    while (top > 0) {
        int u = stack[--top];
        int h = head_stack[top];
        head[u] = h; pos[u] = timer++;
        for (int e = head_adj[u]; e != -1; e = edge_list[e].next) {
            int v = edge_list[e].to;
            if (v != parent[u] && v != heavy[u]) {
                stack[top] = v; head_stack[top++] = v;
            }
        }
        if (heavy[u] != -1) { stack[top] = heavy[u]; head_stack[top++] = h; }
    }
    int* bit = (int*)calloc(n + 1, sizeof(int));
    int* node_masks = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        node_masks[i] = 1 << (s[i] - 'a');
        for (int k = pos[i]; k <= n; k += k & -k) bit[k] ^= node_masks[i];
    }
    int q_count = 0;
    for (int i = 0; i < queriesSize; i++) if (queries[i][0] == 'q') q_count++;
    bool* res = (bool*)malloc(q_count * sizeof(bool));
    int res_idx = 0;
    for (int i = 0; i < queriesSize; i++) {
        if (queries[i][0] == 'q') {
            int u, v, xor_sum = 0;
            sscanf(queries[i], "query %d %d", &u, &v);
            while (head[u] != head[v]) {
                if (dep[head[u]] < dep[head[v]]) { int t = u; u = v; v = t; }
                for (int k = pos[u]; k > 0; k -= k & -k) xor_sum ^= bit[k];
                for (int k = pos[head[u]] - 1; k > 0; k -= k & -k) xor_sum ^= bit[k];
                u = parent[head[u]];
            }
            if (dep[u] < dep[v]) { int t = u; u = v; v = t; }
            for (int k = pos[u]; k > 0; k -= k & -k) xor_sum ^= bit[k];
            for (int k = pos[v] - 1; k > 0; k -= k & -k) xor_sum ^= bit[k];
            res[res_idx++] = (xor_sum & (xor_sum - 1)) == 0;
        } else {
            int u; char c_str[10];
            sscanf(queries[i], "update %d %s", &u, c_str);
            int mask = 1 << (c_str[0] - 'a'), diff = node_masks[u] ^ mask;
            for (int k = pos[u]; k <= n; k += k & -k) bit[k] ^= diff;
            node_masks[u] = mask;
        }
    }
    *returnSize = res_idx;
    free(head_adj); free(edge_list); free(parent); free(dep); free(order);
    free(sz); free(heavy); free(head); free(pos); free(stack); free(head_stack); free(bit); free(node_masks);
    return res;
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
    public IList<bool> PalindromePath(int n, int[][] edges, string s, string[] queries) {
        List<int>[] adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var edge in edges) {
            adj[edge[0]].Add(edge[1]);
            adj[edge[1]].Add(edge[0]);
        }
        int[] parent = new int[n];
        int[] depth = new int[n];
        int[] order = new int[n];
        int headIdx = 0, tailIdx = 0;
        for (int i = 0; i < n; i++) parent[i] = -1;
        order[tailIdx++] = 0;
        while (headIdx < tailIdx) {
            int u = order[headIdx++];
            foreach (int v in adj[u]) {
                if (v != parent[u]) {
                    parent[v] = u; depth[v] = depth[u] + 1; order[tailIdx++] = v;
                }
            }
        }
        int[] sz = new int[n];
        int[] heavy = new int[n];
        for (int i = 0; i < n; i++) { sz[i] = 1; heavy[i] = -1; }
        for (int i = n - 1; i >= 0; i--) {
            int u = order[i];
            if (parent[u] != -1) {
                int p = parent[u]; sz[p] += sz[u];
                if (heavy[p] == -1 || sz[u] > sz[heavy[p]]) heavy[p] = u;
            }
        }
        int[] head = new int[n];
        int[] pos = new int[n];
        int timer = 1;
        Stack<(int, int)> stack = new Stack<(int, int)>();
        stack.Push((0, 0));
        while (stack.Count > 0) {
            var (u, h) = stack.Pop();
            head[u] = h; pos[u] = timer++;
            foreach (int v in adj[u]) {
                if (v != parent[u] && v != heavy[u]) stack.Push((v, v));
            }
            if (heavy[u] != -1) stack.Push((heavy[u], h));
        }
        int[] bit = new int[n + 1];
        int[] nodeMasks = new int[n];
        Action<int, int> update = (idx, val) => {
            for (; idx <= n; idx += idx & -idx) bit[idx] ^= val;
        };
        Func<int, int> query = (idx) => {
            int res = 0;
            for (; idx > 0; idx -= idx & -idx) res ^= bit[idx];
            return res;
        };
        for (int i = 0; i < n; i++) {
            nodeMasks[i] = 1 << (s[i] - 'a');
            update(pos[i], nodeMasks[i]);
        }
        List<bool> results = new List<bool>();
        foreach (string q in queries) {
            string[] parts = q.Split(' ');
            if (parts[0][0] == 'q') {
                int u = int.Parse(parts[1]), v = int.Parse(parts[2]), xorSum = 0;
                while (head[u] != head[v]) {
                    if (depth[head[u]] < depth[head[v]]) { int t = u; u = v; v = t; }
                    xorSum ^= query(pos[u]) ^ query(pos[head[u]] - 1);
                    u = parent[head[u]];
                }
                if (depth[u] < depth[v]) { int t = u; u = v; v = t; }
                xorSum ^= query(pos[u]) ^ query(pos[v] - 1);
                results.Add((xorSum & (xorSum - 1)) == 0);
            } else {
                int u = int.Parse(parts[1]); char c = parts[2][0];
                int mask = 1 << (c - 'a');
                update(pos[u], nodeMasks[u] ^ mask);
                nodeMasks[u] = mask;
            }
        }
        return results;
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
 * @param {string} s
 * @param {string[]} queries
 * @return {boolean[]} // Must be an array of booleans
 */
var palindromePath = function(n, edges, s, queries) {
    const adj = Array.from({length: n}, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    const parent = new Int32Array(n).fill(-1);
    const dep = new Int32Array(n);
    const order = new Int32Array(n);
    let hIdx = 0, tIdx = 0;
    order[tIdx++] = 0;
    while (hIdx < tIdx) {
        const u = order[hIdx++];
        for (const v of adj[u]) {
            if (v !== parent[u]) {
                parent[v] = u; dep[v] = dep[u] + 1; order[tIdx++] = v;
            }
        }
    }
    const sz = new Int32Array(n).fill(1);
    const heavy = new Int32Array(n).fill(-1);
    for (let i = n - 1; i >= 0; i--) {
        const u = order[i];
        if (parent[u] !== -1) {
            const p = parent[u]; sz[p] += sz[u];
            if (heavy[p] === -1 || sz[u] > sz[heavy[p]]) heavy[p] = u;
        }
    }
    const head = new Int32Array(n), pos = new Int32Array(n);
    let timer = 1, stack = [[0, 0]];
    while (stack.length > 0) {
        const [u, h] = stack.pop();
        head[u] = h; pos[u] = timer++;
        for (const v of adj[u]) {
            if (v !== parent[u] && v !== heavy[u]) stack.push([v, v]);
        }
        if (heavy[u] !== -1) stack.push([heavy[u], h]);
    }
    const bit = new Int32Array(n + 1);
    const update = (i, val) => {
        for (; i <= n; i += i & -i) bit[i] ^= val;
    };
    const getQuery = (i) => {
        let res = 0;
        for (; i > 0; i -= i & -i) res ^= bit[i];
        return res;
    };
    const nodeMasks = new Int32Array(n);
    for (let i = 0; i < n; i++) {
        nodeMasks[i] = 1 << (s.charCodeAt(i) - 97);
        update(pos[i], nodeMasks[i]);
    }
    const results = [];
    for (const q of queries) {
        const parts = q.split(' ');
        if (parts[0][0] === 'q') {
            let u = +parts[1], v = +parts[2], xorSum = 0;
            while (head[u] !== head[v]) {
                if (dep[head[u]] < dep[head[v]]) [u, v] = [v, u];
                xorSum ^= getQuery(pos[u]) ^ getQuery(pos[head[u]] - 1);
                u = parent[head[u]];
            }
            if (dep[u] < dep[v]) [u, v] = [v, u];
            xorSum ^= getQuery(pos[u]) ^ getQuery(pos[v] - 1);
            results.push((xorSum & (xorSum - 1)) === 0);
        } else {
            const u = +parts[1], c = parts[2];
            const mask = 1 << (c.charCodeAt(0) - 97);
            update(pos[u], nodeMasks[u] ^ mask); nodeMasks[u] = mask;
        }
    }
    return results;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function palindromePath(n: number, edges: number[][], s: string, queries: string[]): boolean[] {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const parent = new Int32Array(n).fill(-1);
    const depth = new Int32Array(n);
    const size = new Int32Array(n).fill(1);
    const heavy = new Int32Array(n).fill(-1);
    const head = new Int32Array(n);
    const pos = new Int32Array(n);

    let stack = [0];
    const visited = new Uint8Array(n);
    visited[0] = 1;
    const order = new Int32Array(n);
    let orderIdx = 0;

    while (stack.length > 0) {
        const u = stack.pop()!;
        order[orderIdx++] = u;
        for (const v of adj[u]) {
            if (!visited[v]) {
                visited[v] = 1;
                parent[v] = u;
                depth[v] = depth[u] + 1;
                stack.push(v);
            }
        }
    }

    for (let i = n - 1; i >= 0; i--) {
        const u = order[i];
        if (u === 0) continue;
        const p = parent[u];
        size[p] += size[u];
        if (heavy[p] === -1 || size[u] > size[heavy[p]]) {
            heavy[p] = u;
        }
    }

    const stack2: [number, number][] = [[0, 0]];
    let curPos = 1;
    while (stack2.length > 0) {
        const [u, h] = stack2.pop()!;
        head[u] = h;
        pos[u] = curPos++;
        for (const v of adj[u]) {
            if (v !== parent[u] && v !== heavy[u]) {
                stack2.push([v, v]);
            }
        }
        if (heavy[u] !== -1) {
            stack2.push([heavy[u], h]);
        }
    }

    const bitTree = new Int32Array(n + 1);
    function updateBIT(idx: number, val: number) {
        for (; idx <= n; idx += idx & -idx) {
            bitTree[idx] ^= val;
        }
    }

    function updateRange(l: number, r: number, val: number) {
        updateBIT(l, val);
        if (r + 1 <= n) updateBIT(r + 1, val);
    }

    function pointQuery(idx: number): number {
        let res = 0;
        for (; idx > 0; idx -= idx & -idx) {
            res ^= bitTree[idx];
        }
        return res;
    }

    function getLCA(u: number, v: number): number {
        while (head[u] !== head[v]) {
            if (depth[head[u]] > depth[head[v]]) u = parent[head[u]];
            else v = parent[head[v]];
        }
        return depth[u] < depth[v] ? u : v;
    }

    const sMasks = new Int32Array(n);
    for (let i = 0; i < n; i++) {
        const mask = 1 << (s.charCodeAt(i) - 97);
        sMasks[i] = mask;
        updateRange(pos[i], pos[i] + size[i] - 1, mask);
    }

    const results: boolean[] = [];
    for (const q of queries) {
        const parts = q.split(" ");
        if (parts[0] === "update") {
            const u = parseInt(parts[1]);
            const newChar = parts[2];
            const newMask = 1 << (newChar.charCodeAt(0) - 97);
            const delta = sMasks[u] ^ newMask;
            sMasks[u] = newMask;
            updateRange(pos[u], pos[u] + size[u] - 1, delta);
        } else {
            const u = parseInt(parts[1]);
            const v = parseInt(parts[2]);
            const lca = getLCA(u, v);
            const pathXor = pointQuery(pos[u]) ^ pointQuery(pos[v]) ^ sMasks[lca];
            results.push((pathXor & (pathXor - 1)) === 0);
        }
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
     * @param Integer $n
     * @param Integer[][] $edges
     * @param String $s
     * @param String[] $queries
     * @return Boolean[]
     */
    function palindromePath($n, $edges, $s, $queries) {
        $adj = array_fill(0, $n, []);
        foreach ($edges as $edge) {
            $adj[$edge[0]][] = $edge[1];
            $adj[$edge[1]][] = $edge[0];
        }

        $parent = SplFixedArray::fromArray(array_fill(0, $n, -1));
        $depth = SplFixedArray::fromArray(array_fill(0, $n, 0));
        $size = SplFixedArray::fromArray(array_fill(0, $n, 1));
        $heavy = SplFixedArray::fromArray(array_fill(0, $n, -1));
        $order = new SplFixedArray($n);
        $orderIdx = 0;

        $stack = [0];
        $visited = new SplFixedArray($n);
        $visited[0] = 1;
        while (!empty($stack)) {
            $u = array_pop($stack);
            $order[$orderIdx++] = $u;
            foreach ($adj[$u] as $v) {
                if ($visited[$v] === null) {
                    $visited[$v] = 1;
                    $parent[$v] = $u;
                    $depth[$v] = $depth[$u] + 1;
                    $stack[] = $v;
                }
            }
        }

        for ($i = $n - 1; $i >= 0; $i--) {
            $u = $order[$i];
            if ($u === 0) continue;
            $p = $parent[$u];
            $size[$p] += $size[$u];
            if ($heavy[$p] === -1 || $size[$u] > $size[$heavy[$p]]) {
                $heavy[$p] = $u;
            }
        }

        $head = new SplFixedArray($n);
        $pos = new SplFixedArray($n);
        $stack2 = [[0, 0]];
        $curPos = 1;
        while (!empty($stack2)) {
            list($u, $h) = array_pop($stack2);
            $head[$u] = $h;
            $pos[$u] = $curPos++;
            foreach ($adj[$u] as $v) {
                if ($v !== $parent[$u] && $v !== $heavy[$u]) {
                    $stack2[] = [$v, $v];
                }
            }
            if ($heavy[$u] !== -1) {
                $stack2[] = [$heavy[$u], $h];
            }
        }

        $bitTree = new SplFixedArray($n + 1);
        for ($i = 0; $i <= $n; $i++) $bitTree[$i] = 0;

        $updateBIT = function ($idx, $val) use ($bitTree, $n) {
            for (; $idx <= $n; $idx += $idx & -$idx) {
                $bitTree[$idx] ^= $val;
            }
        };

        $pointQuery = function ($idx) use ($bitTree) {
            $res = 0;
            for (; $idx > 0; $idx -= $idx & -$idx) {
                $res ^= $bitTree[$idx];
            }
            return $res;
        };

        $sMasks = new SplFixedArray($n);
        for ($i = 0; $i < $n; $i++) {
            $mask = 1 << (ord($s[$i]) - 97);
            $sMasks[$i] = $mask;
            $updateBIT($pos[$i], $mask);
            $end = $pos[$i] + $size[$i];
            if ($end <= $n) $updateBIT($end, $mask);
        }

        $ans = [];
        foreach ($queries as $q) {
            $parts = explode(" ", $q);
            if ($parts[0] === "update") {
                $u = (int)$parts[1];
                $newMask = 1 << (ord($parts[2]) - 97);
                $delta = $sMasks[$u] ^ $newMask;
                $sMasks[$u] = $newMask;
                $updateBIT($pos[$u], $delta);
                $end = $pos[$u] + $size[$u];
                if ($end <= $n) $updateBIT($end, $delta);
            } else {
                $u = (int)$parts[1];
                $v = (int)$parts[2];
                $a = $u; $b = $v;
                while ($head[$a] !== $head[$b]) {
                    if ($depth[$head[$a]] > $depth[$head[$b]]) $a = $parent[$head[$a]];
                    else $b = $parent[$head[$b]];
                }
                $lca = $depth[$a] < $depth[$b] ? $a : $b;
                $pathXor = $pointQuery($pos[$u]) ^ $pointQuery($pos[$v]) ^ $sMasks[$lca];
                $ans[] = ($pathXor & ($pathXor - 1)) === 0;
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
    func palindromePath(_ n: Int, _ edges: [[Int]], _ s: String, _ queries: [String]) -> [Bool] {
        var adj = Array(repeating: [Int](), count: n)
        for edge in edges {
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        }

        var parent = Array(repeating: -1, count: n)
        var depth = Array(repeating: 0, count: n)
        var size = Array(repeating: 1, count: n)
        var heavy = Array(repeating: -1, count: n)
        var order = Array(repeating: 0, count: n)
        var orderIdx = 0

        var stack = [0]
        var visited = Array(repeating: false, count: n)
        visited[0] = true
        while !stack.isEmpty {
            let u = stack.removeLast()
            order[orderIdx] = u
            orderIdx += 1
            for v in adj[u] {
                if !visited[v] {
                    visited[v] = true
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)
                }
            }
        }

        for i in (0..<n).reversed() {
            let u = order[i]
            if u == 0 { continue }
            let p = parent[u]
            size[p] += size[u]
            if heavy[p] == -1 || size[u] > size[heavy[p]] {
                heavy[p] = u
            }
        }

        var head = Array(repeating: 0, count: n)
        var pos = Array(repeating: 0, count: n)
        var stack2 = [(0, 0)]
        var curPos = 1
        while !stack2.isEmpty {
            let pair = stack2.removeLast()
            let u = pair.0, h = pair.1
            head[u] = h
            pos[u] = curPos
            curPos += 1
            for v in adj[u] {
                if v != parent[u] && v != heavy[u] {
                    stack2.append((v, v))
                }
            }
            if heavy[u] != -1 {
                stack2.append((heavy[u], h))
            }
        }

        var bitTree = Array(repeating: 0, count: n + 1)
        func updateBIT(_ idx: Int, _ val: Int) {
            var i = idx
            while i <= n {
                bitTree[i] ^= val
                i += i & -i
            }
        }

        func updateRange(_ l: Int, _ r: Int, _ val: Int) {
            updateBIT(l, val)
            if r + 1 <= n {
                updateBIT(r + 1, val)
            }
        }

        func pointQuery(_ idx: Int) -> Int {
            var res = 0
            var i = idx
            while i > 0 {
                res ^= bitTree[i]
                i -= i & -i
            }
            return res
        }

        let sBytes = Array(s.utf8)
        var sMasks = Array(repeating: 0, count: n)
        for i in 0..<n {
            let mask = 1 << (Int(sBytes[i]) - 97)
            sMasks[i] = mask
            updateRange(pos[i], pos[i] + size[i] - 1, mask)
        }

        var results = [Bool]()
        for q in queries {
            let parts = q.split(separator: " ")
            if parts[0] == "update" {
                let u = Int(parts[1])!
                let newChar = parts[2].first!
                let newMask = 1 << (Int(newChar.asciiValue!) - 97)
                let delta = sMasks[u] ^ newMask
                sMasks[u] = newMask
                updateRange(pos[u], pos[u] + size[u] - 1, delta)
            } else {
                let u = Int(parts[1])!
                let v = Int(parts[2])!
                var a = u, b = v
                while head[a] != head[b] {
                    if depth[head[a]] > depth[head[b]] { a = parent[head[a]] }
                    else { b = parent[head[b]] }
                }
                let lca = depth[a] < depth[b] ? a : b
                let pathXor = pointQuery(pos[u]) ^ pointQuery(pos[v]) ^ sMasks[lca]
                results.append((pathXor & (pathXor - 1)) == 0)
            }
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
class Solution {
    fun palindromePath(n: Int, edges: Array<IntArray>, s: String, queries: Array<String>): List<Boolean> {
        val adj = Array(n) { mutableListOf<Int>() }
        for (edge in edges) {
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
        }

        val parent = IntArray(n) { -1 }
        val depth = IntArray(n)
        val size = IntArray(n) { 1 }
        val heavy = IntArray(n) { -1 }
        val order = IntArray(n)
        var orderIdx = 0

        val stack = java.util.ArrayDeque<Int>()
        stack.add(0)
        val visited = BooleanArray(n)
        visited[0] = true
        while (stack.isNotEmpty()) {
            val u = stack.removeLast()
            order[orderIdx++] = u
            for (v in adj[u]) {
                if (!visited[v]) {
                    visited[v] = true
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.add(v)
                }
            }
        }

        for (i in n - 1 downTo 0) {
            val u = order[i]
            if (u == 0) continue
            val p = parent[u]
            size[p] += size[u]
            if (heavy[p] == -1 || size[u] > size[heavy[p]]) {
                heavy[p] = u
            }
        }

        val head = IntArray(n)
        val pos = IntArray(n)
        val stack2 = java.util.ArrayDeque<Pair<Int, Int>>()
        stack2.add(0 to 0)
        var curPos = 1
        while (stack2.isNotEmpty()) {
            val pair = stack2.removeLast()
            val u = pair.first
            val h = pair.second
            head[u] = h
            pos[u] = curPos++
            for (v in adj[u]) {
                if (v != parent[u] && v != heavy[u]) {
                    stack2.add(v to v)
                }
            }
            if (heavy[u] != -1) {
                stack2.add(heavy[u] to h)
            }
        }

        val bitTree = IntArray(n + 1)
        fun updateBIT(idx: Int, valXor: Int) {
            var i = idx
            while (i <= n) {
                bitTree[i] = bitTree[i] xor valXor
                i += i and -i
            }
        }

        fun updateRange(l: Int, r: Int, valXor: Int) {
            updateBIT(l, valXor)
            if (r + 1 <= n) updateBIT(r + 1, valXor)
        }

        fun pointQuery(idx: Int): Int {
            var res = 0
            var i = idx
            while (i > 0) {
                res = res xor bitTree[i]
                i -= i and -i
            }
            return res
        }

        val sMasks = IntArray(n)
        for (i in 0 until n) {
            val mask = 1 shl (s[i] - 'a')
            sMasks[i] = mask
            updateRange(pos[i], pos[i] + size[i] - 1, mask)
        }

        val results = mutableListOf<Boolean>()
        for (q in queries) {
            val parts = q.split(" ")
            if (parts[0] == "update") {
                val u = parts[1].toInt()
                val newChar = parts[2][0]
                val newMask = 1 shl (newChar - 'a')
                val delta = sMasks[u] xor newMask
                sMasks[u] = newMask
                updateRange(pos[u], pos[u] + size[u] - 1, delta)
            } else {
                val u = parts[1].toInt()
                val v = parts[2].toInt()
                var a = u
                var b = v
                while (head[a] != head[b]) {
                    if (depth[head[a]] > depth[head[b]]) a = parent[head[a]]
                    else b = parent[head[b]]
                }
                val lca = if (depth[a] < depth[b]) a else b
                val pathXor = pointQuery(pos[u]) xor pointQuery(pos[v]) xor sMasks[lca]
                results.add((pathXor.toLong() and (pathXor.toLong() - 1)) == 0L)
            }
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
  List<bool> palindromePath(int n, List<List<int>> edges, String s, List<String> queries) {
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var edge in edges) {
      adj[edge[0]].add(edge[1]);
      adj[edge[1]].add(edge[0]);
    }

    Int32List tin = Int32List(n);
    Int32List tout = Int32List(n);
    Int32List depth = Int32List(n);
    int logn = 16;
    Int32List up = Int32List(n * logn)..fillRange(0, n * logn, -1);
    int timer = 0;

    List<List<int>> stack = [[0, -1, 0, 0]]; // node, p, d, state
    while (stack.isNotEmpty) {
      var frame = stack.last;
      int u = frame[0];
      int p = frame[1];
      int d = frame[2];
      int state = frame[3];

      if (state == 0) {
        tin[u] = ++timer;
        depth[u] = d;
        up[u * logn] = p;
        frame[3] = 1;
        for (int v in adj[u]) {
          if (v != p) {
            stack.add([v, u, d + 1, 0]);
          }
        }
      } else {
        tout[u] = timer;
        stack.removeLast();
      }
    }

    for (int i = 1; i < logn; i++) {
      for (int u = 0; u < n; u++) {
        int mid = up[u * logn + i - 1];
        if (mid != -1) {
          up[u * logn + i] = up[mid * logn + i - 1];
        }
      }
    }

    Int32List bit = Int32List(n + 2);
    void updateBit(int idx, int val) {
      for (; idx < bit.length; idx += idx & -idx) {
        bit[idx] ^= val;
      }
    }

    int prefixXor(int idx) {
      int res = 0;
      for (; idx > 0; idx -= idx & -idx) {
        res ^= bit[idx];
      }
      return res;
    }

    Int32List currentS = Int32List(n);
    for (int i = 0; i < n; i++) {
      currentS[i] = 1 << (s.codeUnitAt(i) - 97);
      updateBit(tin[i], currentS[i]);
      updateBit(tout[i] + 1, currentS[i]);
    }

    int getLCA(int u, int v) {
      if (depth[u] < depth[v]) {
        int tmp = u; u = v; v = tmp;
      }
      int diff = depth[u] - depth[v];
      for (int i = 0; i < logn; i++) {
        if (((diff >> i) & 1) == 1) {
          u = up[u * logn + i];
        }
      }
      if (u == v) return u;
      for (int i = logn - 1; i >= 0; i--) {
        if (up[u * logn + i] != up[v * logn + i]) {
          u = up[u * logn + i];
          v = up[v * logn + i];
        }
      }
      return up[u * logn];
    }

    List<bool> results = [];
    for (String q in queries) {
      List<String> parts = q.split(' ');
      if (parts[0] == 'query') {
        int u = int.parse(parts[1]);
        int v = int.parse(parts[2]);
        int lca = getLCA(u, v);
        int pathXor = prefixXor(tin[u]) ^ prefixXor(tin[v]) ^ currentS[lca];
        results.add((pathXor & (pathXor - 1)) == 0);
      } else {
        int u = int.parse(parts[1]);
        int newMask = 1 << (parts[2].codeUnitAt(0) - 97);
        int diff = currentS[u] ^ newMask;
        updateBit(tin[u], diff);
        updateBit(tout[u] + 1, diff);
        currentS[u] = newMask;
      }
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
func palindromePath(n int, edges [][]int, s string, queries []string) []bool {
    adj := make([][]int, n)
    for _, edge := range edges {
        u, v := edge[0], edge[1]
        adj[u] = append(adj[u], v)
        adj[v] = append(adj[v], u)
    }

    tin := make([]int, n)
    tout := make([]int, n)
    depth := make([]int, n)
    logn := 16
    up := make([]int, n*logn)
    for i := range up { up[i] = -1 }
    timer := 0

    type frame struct { u, p, d, state int }
    stack := []frame{{0, -1, 0, 0}}
    for len(stack) > 0 {
        f := &stack[len(stack)-1]
        if f.state == 0 {
            timer++
            tin[f.u] = timer
            depth[f.u] = f.d
            up[f.u*logn] = f.p
            f.state = 1
            for _, v := range adj[f.u] {
                if v != f.p {
                    stack = append(stack, frame{v, f.u, f.d + 1, 0})
                }
            }
        } else {
            tout[f.u] = timer
            stack = stack[:len(stack)-1]
        }
    }

    for i := 1; i < logn; i++ {
        for u := 0; u < n; u++ {
            mid := up[u*logn + i - 1]
            if mid != -1 {
                up[u*logn + i] = up[mid*logn + i - 1]
            }
        }
    }

    bit := make([]int, n+2)
    updateBit := func(idx, val int) {
        for idx < len(bit) {
            bit[idx] ^= val
            idx += idx & -idx
        }
    }
    prefixXor := func(idx int) int {
        res := 0
        for idx > 0 {
            res ^= bit[idx]
            idx -= idx & -idx
        }
        return res
    }

    currentS := make([]int, n)
    for i := 0; i < n; i++ {
        currentS[i] = 1 << (s[i] - 'a')
        updateBit(tin[i], currentS[i])
        updateBit(tout[i]+1, currentS[i])
    }

    getLCA := func(u, v int) int {
        if depth[u] < depth[v] {
            u, v = v, u
        }
        diff := depth[u] - depth[v]
        for i := 0; i < logn; i++ {
            if (diff >> i) & 1 == 1 {
                u = up[u*logn + i]
            }
        }
        if u == v { return u }
        for i := logn - 1; i >= 0; i-- {
            if up[u*logn + i] != up[v*logn + i] {
                u = up[u*logn + i]
                v = up[v*logn + i]
            }
        }
        return up[u*logn]
    }

    import "strings"
    import "strconv"

    results := make([]bool, 0)
    for _, q := range queries {
        parts := strings.Split(q, " ")
        if parts[0] == "query" {
            u, _ := strconv.Atoi(parts[1])
            v, _ := strconv.Atoi(parts[2])
            lca := getLCA(u, v)
            pathXor := prefixXor(tin[u]) ^ prefixXor(tin[v]) ^ currentS[lca]
            results = append(results, (pathXor & (pathXor - 1)) == 0)
        } else {
            u, _ := strconv.Atoi(parts[1])
            newMask := 1 << (parts[2][0] - 'a')
            diff := currentS[u] ^ newMask
            updateBit(tin[u], diff)
            updateBit(tout[u]+1, diff)
            currentS[u] = newMask
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
def palindrome_path(n, edges, s, queries)
  adj = Array.new(n) { [] }
  edges.each { |u, v| adj[u] << v; adj[v] << u }

  tin = Array.new(n)
  tout = Array.new(n)
  depth = Array.new(n, 0)
  logn = 16
  up = Array.new(n * logn, -1)
  timer = 0

  stack = [[0, -1, 0, 0]]
  while !stack.empty?
    u, p, d, state = stack[-1]
    if state == 0
      timer += 1
      tin[u] = timer
      depth[u] = d
      up[u * logn] = p
      stack[-1][3] = 1
      adj[u].each { |v| stack.push([v, u, d + 1, 0]) if v != p }
    else
      tout[u] = timer
      stack.pop
    end
  end

  (1...logn).each do |i|
    (0...n).each do |u|
      mid = up[u * logn + i - 1]
      up[u * logn + i] = mid == -1 ? -1 : up[mid * logn + i - 1]
    end
  end

  bit = Array.new(n + 2, 0)
  update_bit = lambda do |idx, val|
    while idx < bit.length
      bit[idx] ^= val
      idx += idx & -idx
    end
  end
  prefix_xor = lambda do |idx|
    res = 0
    while idx > 0
      res ^= bit[idx]
      idx -= idx & -idx
    end
    res
  end

  current_s = Array.new(n)
  (0...n).each do |i|
    current_s[i] = 1 << (s[i].ord - 97)
    update_bit.call(tin[i], current_s[i])
    update_bit.call(tout[i] + 1, current_s[i])
  end

  get_lca = lambda do |u, v|
    u, v = v, u if depth[u] < depth[v]
    diff = depth[u] - depth[v]
    logn.times { |i| u = up[u * logn + i] if (diff >> i) & 1 == 1 }
    return u if u == v
    (logn - 1).downto(0) do |i|
      if up[u * logn + i] != up[v * logn + i]
        u = up[u * logn + i]
        v = up[v * logn + i]
      end
    end
    up[u * logn]
  end

  results = []
  queries.each do |q|
    parts = q.split
    if parts[0] == "query"
      u, v = parts[1].to_i, parts[2].to_i
      lca = get_lca.call(u, v)
      xor_sum = prefix_xor.call(tin[u]) ^ prefix_xor.call(tin[v]) ^ current_s[lca]
      results << ((xor_sum & (xor_sum - 1)) == 0)
    else
      u, c = parts[1].to_i, parts[2]
      new_mask = 1 << (c.ord - 97)
      diff = current_s[u] ^ new_mask
      update_bit.call(tin[u], diff)
      update_bit.call(tout[u] + 1, diff)
      current_s[u] = new_mask
    end
  end
  results
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def palindromePath(n: Int, edges: Array[Array[Int]], s: String, queries: Array[String]): List[Boolean] = {
        val adj = Array.fill(n)(scala.collection.mutable.ListBuffer[Int]())
        for (e <- edges) {
            adj(e(0)) += e(1)
            adj(e(1)) += e(0)
        }

        val tin = new Array[Int](n)
        val tout = new Array[Int](n)
        val depth = new Array[Int](n)
        val logn = 16
        val up = Array.fill(n * logn)(-1)
        var timer = 0

        val stack = scala.collection.mutable.Stack[(Int, Int, Int, Int)]()
        stack.push((0, -1, 0, 0))
        while (stack.nonEmpty) {
            val (u, p, d, state) = stack.pop()
            if (state == 0) {
                timer += 1
                tin(u) = timer
                depth(u) = d
                up(u * logn) = p
                stack.push((u, p, d, 1))
                for (v <- adj(u)) {
                    if (v != p) stack.push((v, u, d + 1, 0))
                }
            } else {
                tout(u) = timer
            }
        }

        for (i <- 1 until logn) {
            for (u <- 0 until n) {
                val mid = up(u * logn + i - 1)
                if (mid != -1) {
                    up(u * logn + i) = up(mid * logn + i - 1)
                }
            }
        }

        val bit = new Array[Int](n + 2)
        def updateBit(idxInit: Int, valXor: Int): Unit = {
            var idx = idxInit
            while (idx < bit.length) {
                bit(idx) ^= valXor
                idx += idx & -idx
            }
        }

        def prefixXor(idxInit: Int): Int = {
            var res = 0
            var idx = idxInit
            while (idx > 0) {
                res ^= bit(idx)
                idx -= idx & -idx
            }
            res
        }

        val currentS = new Array[Int](n)
        for (i <- 0 until n) {
            currentS(i) = 1 << (s(i) - 'a')
            updateBit(tin(i), currentS(i))
            updateBit(tout(i) + 1, currentS(i))
        }

        def getLCA(uInit: Int, vInit: Int): Int = {
            var u = uInit
            var v = vInit
            if (depth(u) < depth(v)) {
                val tmp = u; u = v; v = tmp
            }
            val diff = depth(u) - depth(v)
            for (i <- 0 until logn) {
                if (((diff >> i) & 1) == 1) {
                    u = up(u * logn + i)
                }
            }
            if (u == v) return u
            for (i <- logn - 1 to 0 by -1) {
                if (up(u * logn + i) != up(v * logn + i)) {
                    u = up(u * logn + i)
                    v = up(v * logn + i)
                }
            }
            up(u * logn)
        }

        val results = scala.collection.mutable.ListBuffer[Boolean]()
        for (q <- queries) {
            val parts = q.split(" ")
            if (parts(0) == "query") {
                val u = parts(1).toInt
                val v = parts(2).toInt
                val lca = getLCA(u, v)
                val pathXor = prefixXor(tin(u)) ^ prefixXor(tin(v)) ^ currentS(lca)
                results += ((pathXor & (pathXor - 1)) == 0)
            } else {
                val u = parts(1).toInt
                val newMask = 1 << (parts(2)(0) - 'a')
                val diff = currentS(u) ^ newMask
                updateBit(tin(u), diff)
                updateBit(tout(u) + 1, diff)
                currentS(u) = newMask
            }
        }
        results.toList
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn palindrome_path(n: i32, edges: Vec<Vec<i32>>, s: String, queries: Vec<String>) -> Vec<bool> {
        let n = n as usize;
        let mut adj = vec![vec![]; n];
        for edge in edges {
            adj[edge[0] as usize].push(edge[1]);
            adj[edge[1] as usize].push(edge[0]);
        }

        let mut parent = vec![-1; n];
        let mut depth = vec![0; n];
        let mut size = vec![0; n];
        let mut heavy = vec![-1; n];
        let mut order = Vec::with_capacity(n);
        let mut stack = vec![(0, -1, 0)];

        while let Some((u, p, d)) = stack.pop() {
            order.push(u);
            parent[u] = p;
            depth[u] = d;
            for &v in &adj[u] {
                if v != p {
                    stack.push((v as usize, u as i32, d + 1));
                }
            }
        }

        for &u in order.iter().rev() {
            size[u] = 1;
            let mut max_size = 0;
            for &v in &adj[u] {
                if v as i32 != parent[u] {
                    size[u] += size[v as usize];
                    if size[v as usize] > max_size {
                        max_size = size[v as usize];
                        heavy[u] = v;
                    }
                }
            }
        }

        let mut head = vec![0; n];
        let mut pos = vec![0; n];
        let mut timer = 0;
        let mut stack2 = vec![(0, 0)];
        while let Some((u, h)) = stack2.pop() {
            pos[u] = timer;
            head[u] = h;
            timer += 1;
            for &v in &adj[u] {
                let v = v as usize;
                if v as i32 != parent[u] && v as i32 != heavy[u] {
                    stack2.push((v, v));
                }
            }
            if heavy[u] != -1 {
                stack2.push((heavy[u] as usize, h));
            }
        }

        let mut bit = vec![0; n + 1];
        let mut current_masks = vec![0; n];
        let s_bytes = s.as_bytes();
        for i in 0..n {
            let mask = 1 << (s_bytes[i] - b'a');
            current_masks[i] = mask;
            Self::bit_update(pos[i] + 1, mask, n, &mut bit);
        }

        let mut results = Vec::new();
        for q in queries {
            let parts: Vec<&str> = q.split(' ').collect();
            if parts[0] == "query" {
                let u = parts[1].parse::<usize>().unwrap();
                let v = parts[2].parse::<usize>().unwrap();
                let res_xor = Self::path_query(u, v, &head, &pos, &parent, &depth, &bit, n);
                results.push((res_xor & (res_xor - 1)) == 0);
            } else {
                let u = parts[1].parse::<usize>().unwrap();
                let c = parts[2].as_bytes()[0];
                let new_mask = 1 << (c - b'a');
                let delta = current_masks[u] ^ new_mask;
                current_masks[u] = new_mask;
                Self::bit_update(pos[u] + 1, delta, n, &mut bit);
            }
        }

        results
    }

    fn bit_update(mut idx: usize, delta: i32, n: usize, bit: &mut [i32]) {
        while idx <= n {
            bit[idx] ^= delta;
            idx += (idx as isize & -(idx as isize)) as usize;
        }
    }

    fn bit_query(mut idx: usize, bit: &[i32]) -> i32 {
        let mut res = 0;
        while idx > 0 {
            res ^= bit[idx];
            idx -= (idx as isize & -(idx as isize)) as usize;
        }
        res
    }

    fn bit_query_range(l: usize, r: usize, bit: &[i32]) -> i32 {
        Self::bit_query(r + 1, bit) ^ Self::bit_query(l, bit)
    }

    fn path_query(mut u: usize, mut v: usize, head: &[usize], pos: &[usize], parent: &[i32], depth: &[i32], bit: &[i32], n: usize) -> i32 {
        let mut res = 0;
        while head[u] != head[v] {
            if depth[head[u]] < depth[head[v]] {
                res ^= Self::bit_query_range(pos[head[v]], pos[v], bit);
                v = parent[head[v]] as usize;
            } else {
                res ^= Self::bit_query_range(pos[head[u]], pos[u], bit);
                u = parent[head[u]] as usize;
            }
        }
        if depth[u] < depth[v] {
            res ^= Self::bit_query_range(pos[u], pos[v], bit);
        } else {
            res ^= Self::bit_query_range(pos[v], pos[u], bit);
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (palindrome-path n edges s queries)
  (-> exact-integer? (listof (listof exact-integer?)) string? (listof string?) (listof boolean?))
  (let* ([adj (make-vector n '())]
         [parent (make-vector n -1)]
         [depth (make-vector n 0)]
         [size (make-vector n 0)]
         [heavy (make-vector n -1)]
         [head (make-vector n 0)]
         [pos (make-vector n 0)]
         [bit (make-vector (+ n 1) 0)]
         [current-masks (make-vector n 0)])

    (for ([edge edges])
      (let ([u (car edge)] [v (cadr edge)])
        (vector-set! adj u (cons v (vector-ref adj u)))
        (vector-set! adj v (cons u (vector-ref adj v)))))

    (let ([order '()] [stack (list (list 0 -1 0))])
      (let loop ()
        (unless (null? stack)
          (let* ([curr (car stack)]
                 [u (car curr)]
                 [p (cadr curr)]
                 [d (caddr curr)])
            (set! stack (cdr stack))
            (set! order (cons u order))
            (vector-set! parent u p)
            (vector-set! depth u d)
            (for ([v (vector-ref adj u)])
              (unless (= v p)
                (set! stack (cons (list v u (+ d 1)) stack))))
            (loop))))

      (for ([u order])
        (let* ([u-size 1]
               [max-s 0]
               [h -1])
          (for ([v (vector-ref adj u)])
            (unless (= v (vector-ref parent u))
              (set! u-size (+ u-size (vector-ref size v)))
              (when (> (vector-ref size v) max-s)
                (set! max-s (vector-ref size v))
                (set! h v))))
          (vector-set! size u u-size)
          (vector-set! heavy u h))))

    (let ([timer 0] [stack (list (list 0 0))])
      (let loop ()
        (unless (null? stack)
          (let* ([curr (car stack)]
                 [u (car curr)]
                 [h (cadr curr)])
            (set! stack (cdr stack))
            (vector-set! pos u timer)
            (vector-set! head u h)
            (set! timer (+ timer 1))
            (for ([v (vector-ref adj u)])
              (unless (or (= v (vector-ref parent u)) (= v (vector-ref heavy u)))
                (set! stack (cons (list v v) stack))))
            (when (not (= (vector-ref heavy u) -1))
              (set! stack (cons (list (vector-ref heavy u) h) stack)))
            (loop)))))

    (define (bit-update! idx delta)
      (let loop ([i idx])
        (when (<= i n)
          (vector-set! bit i (bitwise-xor (vector-ref bit i) delta))
          (loop (+ i (bitwise-and i (- i)))))))

    (define (bit-query idx)
      (let loop ([i idx] [res 0])
        (if (> i 0)
            (loop (- i (bitwise-and i (- i))) (bitwise-xor res (vector-ref bit i)))
            res)))

    (define (bit-query-range l r)
      (bitwise-xor (bit-query (+ r 1)) (bit-query l)))

    (define (at-most-one-bit-set? v)
      (= (bitwise-and v (- v 1)) 0))

    (for ([i (in-range n)])
      (let ([mask (arithmetic-shift 1 (- (char->integer (string-ref s i)) (char->integer #\a)))])
        (vector-set! current-masks i mask)
        (bit-update! (+ (vector-ref pos i) 1) mask)))

    (let ([ans '()])
      (for ([q queries])
        (let* ([parts (string-split q " ")]
               [type (car parts)])
          (if (equal? type "query")
              (let ([u (string->number (cadr parts))]
                    [v (string->number (caddr parts))])
                (let loop ([u u] [v v] [res 0])
                  (let ([hu (vector-ref head u)] [hv (vector-ref head v)])
                    (if (= hu hv)
                        (let* ([pu (vector-ref pos u)]
                               [pv (vector-ref pos v)]
                               [final-res (bitwise-xor res (if (< pu pv) (bit-query-range pu pv) (bit-query-range pv pu)))])
                          (set! ans (cons (at-most-one-bit-set? final-res) ans)))
                        (if (< (vector-ref depth hu) (vector-ref depth hv))
                            (loop u (vector-ref parent hv) (bitwise-xor res (bit-query-range (vector-ref pos hv) (vector-ref pos v))))
                            (loop (vector-ref parent hu) v (bitwise-xor res (bit-query-range (vector-ref pos hu) (vector-ref pos u)))))))))
              (let* ([u (string->number (cadr parts))]
                     [new-c (string-ref (caddr parts) 0)]
                     [new-mask (arithmetic-shift 1 (- (char->integer new-c) (char->integer #\a)))]
                     [delta (bitwise-xor (vector-ref current-masks u) new-mask)])
                (vector-set! current-masks u new-mask)
                (bit-update! (+ (vector-ref pos u) 1) delta)))))
      (reverse ans))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec palindrome_path(N :: integer(), Edges :: [[integer()]], S :: unicode:unicode_binary(), Queries :: [unicode:unicode_binary()]) -> [boolean()].
palindrome_path(N, Edges, S, Queries) ->
  Adj0 = array:new(N, {default, []}),
  Adj = lists:foldl(fun([U, V], A) ->
    A1 = array:set(U, [V | array:get(U, A)], A),
    array:set(V, [U | array:get(V, A1)], A1)
  end, Adj0, Edges),
  {Parent, Depth, Order} = dfs1_loop([{0, -1, 0}], Adj, array:new(N, {default, -1}), array:new(N, {default, 0}), []),
  {Size, Heavy} = lists:foldl(fun(U, {SArr, HArr}) ->
    P = array:get(U, Parent),
    {USize, UHeavy, _MaxS} = lists:foldl(fun(V, {US, UH, MS}) ->
      if V /= P ->
        VS = array:get(V, SArr),
        if VS > MS -> {US + VS, V, VS};
        true -> {US + VS, UH, MS} end;
      true -> {US, UH, MS} end
    end, {1, -1, 0}, array:get(U, Adj)),
    {array:set(U, USize, SArr), array:set(U, UHeavy, HArr)}
  end, {array:new(N, {default, 0}), array:new(N, {default, -1})}, Order),
  {Head, Pos} = dfs2_loop([{0, 0}], Adj, Parent, Heavy, 0, array:new(N, {default, -1}), array:new(N, {default, -1})),
  InitialMasks = array:from_list([1 bsl (C - $a) || C <- binary_to_list(S)]),
  Bit0 = array:new(N + 1, {default, 0}),
  Bit = lists:foldl(fun(I, B) ->
    Mask = array:get(I, InitialMasks),
    update_bit(array:get(I, Pos) + 1, Mask, N, B)
  end, Bit0, lists:seq(0, N - 1)),
  process_queries(Queries, N, Head, Pos, Parent, Depth, InitialMasks, Bit, []).

dfs1_loop([], _Adj, Parent, Depth, Order) -> {Parent, Depth, Order};
dfs1_loop([{U, P, D} | Rest], Adj, Parent, Depth, Order) ->
  Children = [V || V <- array:get(U, Adj), V /= P],
  NewRest = lists:foldl(fun(V, Acc) -> [{V, U, D + 1} | Acc] end, Rest, Children),
  dfs1_loop(NewRest, Adj, array:set(U, P, Parent), array:set(U, D, Depth), [U | Order]).

dfs2_loop([], _Adj, _Parent, _Heavy, _Timer, Head, Pos) -> {Head, Pos};
dfs2_loop([{U, H} | Rest], Adj, Parent, Heavy, Timer, Head, Pos) ->
  NewHead = array:set(U, H, Head),
  NewPos = array:set(U, Timer, Pos),
  Hvy = array:get(U, Heavy),
  P = array:get(U, Parent),
  Children = [V || V <- array:get(U, Adj), V /= P, V /= Hvy],
  RestWithNonHeavy = lists:foldl(fun(V, Acc) -> [{V, V} | Acc] end, Rest, Children),
  NewRest = if Hvy /= -1 -> [{Hvy, H} | RestWithNonHeavy]; true -> RestWithNonHeavy end,
  dfs2_loop(NewRest, Adj, Parent, Heavy, Timer + 1, NewHead, NewPos).

update_bit(Idx, Delta, N, Bit) when Idx =< N ->
  NewBit = array:set(Idx, array:get(Idx, Bit) bxor Delta, Bit),
  update_bit(Idx + (Idx band -Idx), Delta, N, NewBit);
update_bit(_, _, _, Bit) -> Bit.

query_bit(0, _) -> 0;
query_bit(Idx, Bit) -> array:get(Idx, Bit) bxor query_bit(Idx - (Idx band -Idx), Bit).

bit_query_range(L, R, Bit) -> query_bit(R + 1, Bit) bxor query_bit(L, Bit).

get_path_xor(U, V, Head, Pos, Parent, Depth, Bit, Acc) ->
  HU = array:get(U, Head),
  HV = array:get(V, Head),
  if HU =:= HV ->
    PU = array:get(U, Pos),
    PV = array:get(V, Pos),
    {P1, P2} = if PU < PV -> {PU, PV}; true -> {PV, PU} end,
    Acc bxor bit_query_range(P1, P2, Bit);
  true ->
    D_HU = array:get(HU, Depth),
    D_HV = array:get(HV, Depth),
    if D_HU < D_HV ->
      get_path_xor(U, array:get(HV, Parent), Head, Pos, Parent, Depth, Bit, Acc bxor bit_query_range(array:get(HV, Pos), array:get(V, Pos), Bit));
    true ->
      get_path_xor(array:get(HU, Parent), V, Head, Pos, Parent, Depth, Bit, Acc bxor bit_query_range(array:get(HU, Pos), array:get(U, Pos), Bit))
    end
  end.

process_queries([], _N, _Head, _Pos, _Parent, _Depth, _Masks, _Bit, Ans) -> lists:reverse(Ans);
process_queries([Q | Rest], N, Head, Pos, Parent, Depth, Masks, Bit, Ans) ->
  case binary:split(Q, <<" ">>, [global]) of
    [<<"query">>, Ubin, Vbin] ->
      U = binary_to_integer(Ubin),
      V = binary_to_integer(Vbin),
      Res = get_path_xor(U, V, Head, Pos, Parent, Depth, Bit, 0),
      process_queries(Rest, N, Head, Pos, Parent, Depth, Masks, Bit, [(Res band (Res - 1)) =:= 0 | Ans]);
    [<<"update">>, Ubin, Cbin] ->
      U = binary_to_integer(Ubin),
      [C] = binary_to_list(Cbin),
      NewMask = 1 bsl (C - $a),
      OldMask = array:get(U, Masks),
      Delta = OldMask bxor NewMask,
      process_queries(Rest, N, Head, Pos, Parent, Depth, array:set(U, NewMask, Masks), update_bit(array:get(U, Pos) + 1, Delta, N, Bit), Ans)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  import Bitwise

  @spec palindrome_path(n :: integer, edges :: [[integer]], s :: String.t, queries :: [String.t]) :: [boolean]
  def palindrome_path(n, edges, s, queries) do
    adj = Enum.reduce(edges, :array.new(n, default: []), fn [u, v], acc ->
      acc |> :array.set(u, [v | :array.get(u, acc)]) |> :array.set(v, [u | :array.get(v, acc)])
    end)

    {parent, depth, order} = dfs1_loop([{0, -1, 0}], adj, :array.new(n, default: -1), :array.new(n, default: 0), [])

    {size, heavy} = Enum.reduce(order, {:array.new(n, default: 0), :array.new(n, default: -1)}, fn u, {s_arr, h_arr} ->
      p = :array.get(u, parent)
      {u_size, u_heavy, _max_s} = Enum.reduce(:array.get(u, adj), {1, -1, 0}, fn v, {us, uh, ms} ->
        if v != p do
          vs = :array.get(v, s_arr)
          if vs > ms, do: {us + vs, v, vs}, else: {us + vs, uh, ms}
        else
          {us, uh, ms}
        end
      end)
      {:array.set(u, u_size, s_arr), :array.set(u, u_heavy, h_arr)}
    end)

    {head, pos} = dfs2_loop([{0, 0}], adj, parent, heavy, 0, :array.new(n, default: -1), :array.new(n, default: -1))

    initial_masks = :array.from_list(for <<c::8 <- s>>, do: 1 <<< (c - ?a))
    bit = Enum.reduce(0..(n - 1), :array.new(n + 1, default: 0), fn i, acc ->
      bit_update(acc, :array.get(i, pos) + 1, :array.get(i, initial_masks), n)
    end)

    process_queries(queries, n, head, pos, parent, depth, initial_masks, bit, [])
  end

  defp dfs1_loop([], _, parent, depth, order), do: {parent, depth, order}
  defp dfs1_loop([{u, p, d} | rest], adj, parent, depth, order) do
    children = Enum.filter(:array.get(u, adj), fn v -> v != p end)
    new_rest = Enum.reduce(children, rest, fn v, acc -> [{v, u, d + 1} | acc] end)
    dfs1_loop(new_rest, adj, :array.set(u, p, parent), :array.set(u, d, depth), [u | order])
  end

  defp dfs2_loop([], _, _, _, _, head, pos), do: {head, pos}
  defp dfs2_loop([{u, h} | rest], adj, parent, heavy, timer, head, pos) do
    hvy = :array.get(u, heavy)
    p = :array.get(u, parent)
    children = Enum.filter(:array.get(u, adj), fn v -> v != p and v != hvy end)
    rest_with_nh = Enum.reduce(children, rest, fn v, acc -> [{v, v} | acc] end)
    new_rest = if hvy != -1, do: [{hvy, h} | rest_with_nh], else: rest_with_nh
    dfs2_loop(new_rest, adj, parent, heavy, timer + 1, :array.set(u, h, head), :array.set(u, timer, pos))
  end

  defp bit_update(bit, idx, delta, n) when idx <= n do
    bit_update(:array.set(idx, :array.get(idx, bit) ^^^ delta, bit), idx + (idx &&& -idx), delta, n)
  end
  defp bit_update(bit, _, _, _), do: bit

  defp bit_query(bit, 0), do: 0
  defp bit_query(bit, idx), do: :array.get(idx, bit) ^^^ bit_query(bit, idx - (idx &&& -idx))

  defp bit_query_range(bit, l, r), do: bit_query(bit, r + 1) ^^^ bit_query(bit, l)

  defp get_path_xor(u, v, head, pos, parent, depth, bit, acc) do
    hu = :array.get(u, head)
    hv = :array.get(v, head)
    if hu == hv do
      {pu, pv} = if :array.get(u, pos) < :array.get(v, pos), do: {:array.get(u, pos), :array.get(v, pos)}, else: {:array.get(v, pos), :array.get(u, pos)}
      acc ^^^ bit_query_range(bit, pu, pv)
    else
      if :array.get(hu, depth) < :array.get(hv, depth) do
        get_path_xor(u, :array.get(hv, parent), head, pos, parent, depth, bit, acc ^^^ bit_query_range(bit, :array.get(hv, pos), :array.get(v, pos)))
      else
        get_path_xor(:array.get(hu, parent), v, head, pos, parent, depth, bit, acc ^^^ bit_query_range(bit, :array.get(hu, pos), :array.get(u, pos)))
      end
    end
  end

  defp process_queries([], _, _, _, _, _, _, _, ans), do: Enum.reverse(ans)
  defp process_queries([q | rest], n, head, pos, parent, depth, masks, bit, ans) do
    case String.split(q, " ") do
      ["query", u_str, v_str] ->
        res = get_path_xor(String.to_integer(u_str), String.to_integer(v_str), head, pos, parent, depth, bit, 0)
        process_queries(rest, n, head, pos, parent, depth, masks, bit, [(res &&& (res - 1)) == 0 | ans])
      ["update", u_str, c_str] ->
        u = String.to_integer(u_str)
        <<c::8>> = c_str
        new_mask = 1 <<< (c - ?a)
        old_mask = :array.get(u, masks)
        process_queries(rest, n, head, pos, parent, depth, :array.set(u, new_mask, masks), bit_update(bit, :array.get(u, pos) + 1, old_mask ^^^ new_mask, n), ans)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O((n + q) \log^2 n) where $n$ is the number of nodes and $q$ is the number of queries. Each query involves HLD decomposing the path into $O(\log n)$ segments, and for each segment, the Fenwick Tree performs an $O(\log n)$ operation. Point updates take $O(\log n)$ using the BIT.
- **Space Complexity:** O(n) space to store the adjacency list, HLD structure (parent, depth, heavy child, head, position), and the Fenwick tree.
