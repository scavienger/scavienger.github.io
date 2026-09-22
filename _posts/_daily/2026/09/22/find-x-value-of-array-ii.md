---
layout: post
title: "Find X Value of Array II"
date: 2026-09-22 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Math", "Segment Tree"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/find-x-value-of-array-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\n    int size;\n    vector<int> treeProd;\n    vector<int>\
        \ treeCounts;\n    int K;\n\npublic:\n    vector<int> resultArray(vector<int>&\
        \ nums, int k, vector<vector<int>>& queries) {\n        K = k;\n        int\
        \ n = nums.size();\n        size = 1;\n        while (size < n) size <<= 1;\n\
        \        treeProd.assign(2 * size, 1);\n        treeCounts.assign(2 * size *\
        \ 5, 0);\n\n        for (int i = 0; i < n; ++i) {\n            int node = i\
        \ + size;\n            int v = nums[i] % K;\n            treeProd[node] = v;\n\
        \            treeCounts[node * 5 + v] = 1;\n        }\n\n        for (int i\
        \ = size - 1; i >= 1; --i) {\n            int left = i << 1;\n            int\
        \ right = left | 1;\n            int lp = treeProd[left];\n            treeProd[i]\
        \ = (lp * treeProd[right]) % K;\n            int idx_i = i * 5, idx_l = left\
        \ * 5, idx_r = right * 5;\n            for (int j = 0; j < K; ++j) treeCounts[idx_i\
        \ + j] = treeCounts[idx_l + j];\n            for (int j = 0; j < K; ++j) treeCounts[idx_i\
        \ + (lp * j) % K] += treeCounts[idx_r + j];\n        }\n\n        vector<int>\
        \ results;\n        results.reserve(queries.size());\n        for (const auto&\
        \ q : queries) {\n            update(q[0], q[1]);\n            results.push_back(query(q[2],\
        \ n - 1, q[3]));\n        }\n        return results;\n    }\n\n    void update(int\
        \ i, int val) {\n        int node = i + size;\n        int v = val % K;\n  \
        \      treeProd[node] = v;\n        for (int j = 0; j < 5; ++j) treeCounts[node\
        \ * 5 + j] = 0;\n        treeCounts[node * 5 + v] = 1;\n\n        while (node\
        \ > 1) {\n            node >>= 1;\n            int left = node << 1;\n     \
        \       int right = left | 1;\n            int lp = treeProd[left];\n      \
        \      treeProd[node] = (lp * treeProd[right]) % K;\n            int idx_n =\
        \ node * 5, idx_l = left * 5, idx_r = right * 5;\n            for (int j = 0;\
        \ j < K; ++j) treeCounts[idx_n + j] = treeCounts[idx_l + j];\n            for\
        \ (int j = 0; j < K; ++j) treeCounts[idx_n + (lp * j) % K] += treeCounts[idx_r\
        \ + j];\n        }\n    }\n\n    int query(int l, int r, int xi) {\n       \
        \ l += size;\n        r += size;\n        int leftNodes[64], rightNodes[64];\n\
        \        int lIdx = 0, rIdx = 0;\n        while (l <= r) {\n            if (l\
        \ % 2 == 1) leftNodes[lIdx++] = l++;\n            if (r % 2 == 0) rightNodes[rIdx++]\
        \ = r--;\n            l >>= 1;\n            r >>= 1;\n        }\n\n        int\
        \ resP = 1;\n        int resC[5] = {0, 0, 0, 0, 0};\n        auto mergeNode\
        \ = [&](int node) {\n            int nextC[5];\n            for (int j = 0;\
        \ j < K; ++j) nextC[j] = resC[j];\n            int idx = node * 5;\n       \
        \     for (int j = 0; j < K; ++j) {\n                nextC[(resP * j) % K] +=\
        \ treeCounts[idx + j];\n            }\n            for (int j = 0; j < K; ++j)\
        \ resC[j] = nextC[j];\n            resP = (resP * treeProd[node]) % K;\n   \
        \     };\n\n        for (int i = 0; i < lIdx; ++i) mergeNode(leftNodes[i]);\n\
        \        for (int i = rIdx - 1; i >= 0; --i) mergeNode(rightNodes[i]);\n\n \
        \       return resC[xi];\n    }\n};"
      java: "class Solution {\n    int size;\n    int[] treeProd;\n    int[] treeCounts;\n\
        \    int K;\n\n    public int[] resultArray(int[] nums, int k, int[][] queries)\
        \ {\n        this.K = k;\n        int n = nums.length;\n        size = 1;\n\
        \        while (size < n) size *= 2;\n        treeProd = new int[2 * size];\n\
        \        java.util.Arrays.fill(treeProd, 1);\n        treeCounts = new int[2\
        \ * size * 5];\n\n        for (int i = 0; i < n; i++) {\n            int node\
        \ = i + size;\n            int v = nums[i] % K;\n            treeProd[node]\
        \ = v;\n            treeCounts[node * 5 + v] = 1;\n        }\n\n        for\
        \ (int i = size - 1; i >= 1; i--) {\n            int left = 2 * i;\n       \
        \     int right = 2 * i + 1;\n            int lp = treeProd[left];\n       \
        \     treeProd[i] = (lp * treeProd[right]) % K;\n            for (int j = 0;\
        \ j < K; j++) {\n                treeCounts[i * 5 + j] = treeCounts[left * 5\
        \ + j];\n            }\n            for (int j = 0; j < K; j++) {\n        \
        \        treeCounts[i * 5 + (lp * j) % K] += treeCounts[right * 5 + j];\n  \
        \          }\n        }\n\n        int[] results = new int[queries.length];\n\
        \        for (int i = 0; i < queries.length; i++) {\n            update(queries[i][0],\
        \ queries[i][1]);\n            results[i] = query(queries[i][2], n - 1, queries[i][3]);\n\
        \        }\n        return results;\n    }\n\n    private void update(int i,\
        \ int val) {\n        int node = i + size;\n        int v = val % K;\n     \
        \   treeProd[node] = v;\n        for (int j = 0; j < 5; j++) treeCounts[node\
        \ * 5 + j] = 0;\n        treeCounts[node * 5 + v] = 1;\n\n        while (node\
        \ > 1) {\n            node /= 2;\n            int left = 2 * node;\n       \
        \     int right = 2 * node + 1;\n            int lp = treeProd[left];\n    \
        \        treeProd[node] = (lp * treeProd[right]) % K;\n            for (int\
        \ j = 0; j < K; j++) {\n                treeCounts[node * 5 + j] = treeCounts[left\
        \ * 5 + j];\n            }\n            for (int j = 0; j < K; j++) {\n    \
        \            treeCounts[node * 5 + (lp * j) % K] += treeCounts[right * 5 + j];\n\
        \            }\n        }\n    }\n\n    private int query(int l, int r, int\
        \ xi) {\n        l += size;\n        r += size;\n        int[] leftNodes = new\
        \ int[64];\n        int[] rightNodes = new int[64];\n        int lIdx = 0, rIdx\
        \ = 0;\n        while (l <= r) {\n            if (l % 2 == 1) leftNodes[lIdx++]\
        \ = l++;\n            if (r % 2 == 0) rightNodes[rIdx++] = r--;\n          \
        \  l /= 2;\n            r /= 2;\n        }\n\n        int resP = 1;\n      \
        \  int[] resC = new int[5];\n        for (int i = 0; i < lIdx; i++) {\n    \
        \        int node = leftNodes[i];\n            int[] nextC = resC.clone();\n\
        \            for (int j = 0; j < K; j++) {\n                nextC[(resP * j)\
        \ % K] += treeCounts[node * 5 + j];\n            }\n            resC = nextC;\n\
        \            resP = (resP * treeProd[node]) % K;\n        }\n        for (int\
        \ i = rIdx - 1; i >= 0; i--) {\n            int node = rightNodes[i];\n    \
        \        int[] nextC = resC.clone();\n            for (int j = 0; j < K; j++)\
        \ {\n                nextC[(resP * j) % K] += treeCounts[node * 5 + j];\n  \
        \          }\n            resC = nextC;\n            resP = (resP * treeProd[node])\
        \ % K;\n        }\n        return resC[xi];\n    }\n}"
      python: "class Solution(object):\n    def resultArray(self, nums, k, queries):\n\
        \        \"\"\"\n        :type nums: List[int]\n        :type k: int\n     \
        \   :type queries: List[List[int]]\n        :rtype: List[int]\n        \"\"\"\
        \n        n = len(nums)\n        size = 1\n        while size < n:\n       \
        \     size <<= 1\n\n        tree_prod = [1] * (2 * size)\n        tree_counts\
        \ = [0] * (2 * size * 5)\n\n        def update(i, val):\n            node =\
        \ i + size\n            v = val % k\n            tree_prod[node] = v\n     \
        \       idx = node * 5\n            for j in range(5):\n                tree_counts[idx\
        \ + j] = 0\n            tree_counts[idx + v] = 1\n            while node > 1:\n\
        \                node >>= 1\n                left = node << 1\n            \
        \    right = left | 1\n                lp = tree_prod[left]\n              \
        \  tree_prod[node] = (lp * tree_prod[right]) % k\n                idx_n, idx_l,\
        \ idx_r = node * 5, left * 5, right * 5\n                for j in range(k):\n\
        \                    tree_counts[idx_n + j] = tree_counts[idx_l + j]\n     \
        \           for j in range(k):\n                    tree_counts[idx_n + (lp\
        \ * j) % k] += tree_counts[idx_r + j]\n\n        for i, val in enumerate(nums):\n\
        \            node = i + size\n            v = val % k\n            tree_prod[node]\
        \ = v\n            tree_counts[node * 5 + v] = 1\n\n        for i in range(size\
        \ - 1, 0, -1):\n            left = i << 1\n            right = left | 1\n  \
        \          lp = tree_prod[left]\n            tree_prod[i] = (lp * tree_prod[right])\
        \ % k\n            idx_i, idx_l, idx_r = i * 5, left * 5, right * 5\n      \
        \      for j in range(k):\n                tree_counts[idx_i + j] = tree_counts[idx_l\
        \ + j]\n            for j in range(k):\n                tree_counts[idx_i +\
        \ (lp * j) % k] += tree_counts[idx_r + j]\n\n        results = []\n        for\
        \ idx, val, start, xi in queries:\n            update(idx, val)\n\n        \
        \    l, r = start + size, (n - 1) + size\n            left_nodes, right_nodes\
        \ = [], []\n            while l <= r:\n                if l % 2 == 1:\n    \
        \                left_nodes.append(l)\n                    l += 1\n        \
        \        if r % 2 == 0:\n                    right_nodes.append(r)\n       \
        \             r -= 1\n                l >>= 1\n                r >>= 1\n\n \
        \           res_p = 1\n            res_c = [0] * 5\n            for node in\
        \ left_nodes + right_nodes[::-1]:\n                new_c = list(res_c)\n   \
        \             idx = node * 5\n                for j in range(k):\n         \
        \           new_c[(res_p * j) % k] += tree_counts[idx + j]\n               \
        \ res_c = new_c\n                res_p = (res_p * tree_prod[node]) % k\n   \
        \         results.append(res_c[xi])\n\n        return results"
      python3: "import math\n\nclass Solution:\n    def resultArray(self, nums: List[int],\
        \ k: int, queries: List[List[int]]) -> List[int]:\n        n = len(nums)\n \
        \       if n == 0:\n            return []\n\n        N = 1\n        while N\
        \ < n:\n            N *= 2\n\n        tree_prod = [1] * (2 * N)\n        tree_cnt\
        \ = [0] * (2 * N * k)\n\n        for i in range(n):\n            v = nums[i]\
        \ % k\n            tree_prod[N + i] = v\n            tree_cnt[(N + i) * k +\
        \ v] = 1\n\n        for i in range(N - 1, 0, -1):\n            lp = tree_prod[2\
        \ * i]\n            rp = tree_prod[2 * i + 1]\n            tree_prod[i] = (lp\
        \ * rp) % k\n            idx_k = i * k\n            lc_k = 2 * i * k\n     \
        \       rc_k = (2 * i + 1) * k\n            for j in range(k):\n           \
        \     tree_cnt[idx_k + j] = tree_cnt[lc_k + j]\n            for j in range(k):\n\
        \                tree_cnt[idx_k + (lp * j) % k] += tree_cnt[rc_k + j]\n\n  \
        \      res = []\n        for idx, val, start, x in queries:\n            curr\
        \ = idx + N\n            v = val % k\n            tree_prod[curr] = v\n    \
        \        for j in range(k):\n                tree_cnt[curr * k + j] = 0\n  \
        \          tree_cnt[curr * k + v] = 1\n            curr //= 2\n            while\
        \ curr >= 1:\n                lp = tree_prod[2 * curr]\n                rp =\
        \ tree_prod[2 * curr + 1]\n                tree_prod[curr] = (lp * rp) % k\n\
        \                idx_k = curr * k\n                lc_k = 2 * curr * k\n   \
        \             rc_k = (2 * curr + 1) * k\n                for j in range(k):\n\
        \                    tree_cnt[idx_k + j] = tree_cnt[lc_k + j]\n            \
        \    for j in range(k):\n                    tree_cnt[idx_k + (lp * j) % k]\
        \ += tree_cnt[rc_k + j]\n                curr //= 2\n\n            l, r = start\
        \ + N, n - 1 + N\n            l_res, r_res = [], []\n            while l <=\
        \ r:\n                if l % 2 == 1:\n                    l_res.append(l)\n\
        \                    l += 1\n                if r % 2 == 0:\n              \
        \      r_res.append(r)\n                    r -= 1\n                l //= 2\n\
        \                r //= 2\n\n            all_nodes = l_res + r_res[::-1]\n  \
        \          first_node = all_nodes[0]\n            curr_prod = tree_prod[first_node]\n\
        \            curr_cnt = tree_cnt[first_node * k : (first_node + 1) * k]\n\n\
        \            for i in range(1, len(all_nodes)):\n                node_idx =\
        \ all_nodes[i]\n                lp = curr_prod\n                rc_start = node_idx\
        \ * k\n                new_cnt = list(curr_cnt)\n                for j in range(k):\n\
        \                    new_cnt[(lp * j) % k] += tree_cnt[rc_start + j]\n     \
        \           curr_cnt = new_cnt\n                curr_prod = (lp * tree_prod[node_idx])\
        \ % k\n\n            res.append(curr_cnt[x])\n\n        return res"
      c: "#include <stdlib.h>\n#include <string.h>\n\ntypedef struct {\n    int prod;\n\
        \    int cnt[5];\n} Node;\n\nNode* tree;\nint treeSize;\n\nvoid merge(Node*\
        \ res, const Node* left, const Node* right, int k) {\n    res->prod = (left->prod\
        \ * right->prod) % k;\n    for (int i = 0; i < k; i++) {\n        res->cnt[i]\
        \ = left->cnt[i];\n    }\n    for (int i = 0; i < k; i++) {\n        res->cnt[(left->prod\
        \ * i) % k] += right->cnt[i];\n    }\n}\n\nvoid build(int v, int tl, int tr,\
        \ int* nums, int k) {\n    if (tl == tr) {\n        int val = nums[tl] % k;\n\
        \        tree[v].prod = val;\n        for (int i = 0; i < k; i++) tree[v].cnt[i]\
        \ = 0;\n        tree[v].cnt[val] = 1;\n    } else {\n        int tm = (tl +\
        \ tr) / 2;\n        build(2 * v, tl, tm, nums, k);\n        build(2 * v + 1,\
        \ tm + 1, tr, nums, k);\n        merge(&tree[v], &tree[2 * v], &tree[2 * v +\
        \ 1], k);\n    }\n}\n\nvoid update(int v, int tl, int tr, int pos, int newVal,\
        \ int k) {\n    if (tl == tr) {\n        int val = newVal % k;\n        tree[v].prod\
        \ = val;\n        for (int i = 0; i < k; i++) tree[v].cnt[i] = 0;\n        tree[v].cnt[val]\
        \ = 1;\n    } else {\n        int tm = (tl + tr) / 2;\n        if (pos <= tm)\n\
        \            update(2 * v, tl, tm, pos, newVal, k);\n        else\n        \
        \    update(2 * v + 1, tm + 1, tr, pos, newVal, k);\n        merge(&tree[v],\
        \ &tree[2 * v], &tree[2 * v + 1], k);\n    }\n}\n\nNode query(int v, int tl,\
        \ int tr, int l, int r, int k) {\n    if (l == tl && r == tr) return tree[v];\n\
        \    int tm = (tl + tr) / 2;\n    if (r <= tm) return query(2 * v, tl, tm, l,\
        \ r, k);\n    if (l > tm) return query(2 * v + 1, tm + 1, tr, l, r, k);\n  \
        \  Node leftResult = query(2 * v, tl, tm, l, tm, k);\n    Node rightResult =\
        \ query(2 * v + 1, tm + 1, tr, tm + 1, r, k);\n    Node res;\n    merge(&res,\
        \ &leftResult, &rightResult, k);\n    return res;\n}\n\nint* resultArray(int*\
        \ nums, int numsSize, int k, int** queries, int queriesSize, int* queriesColSize,\
        \ int* returnSize) {\n    tree = (Node*)malloc(4 * numsSize * sizeof(Node));\n\
        \    build(1, 0, numsSize - 1, nums, k);\n\n    int* result = (int*)malloc(queriesSize\
        \ * sizeof(int));\n    *returnSize = queriesSize;\n\n    for (int i = 0; i <\
        \ queriesSize; i++) {\n        int idx = queries[i][0];\n        int val = queries[i][1];\n\
        \        int start = queries[i][2];\n        int x = queries[i][3];\n\n    \
        \    update(1, 0, numsSize - 1, idx, val, k);\n        Node qNode = query(1,\
        \ 0, numsSize - 1, start, numsSize - 1, k);\n        result[i] = qNode.cnt[x];\n\
        \    }\n\n    free(tree);\n    return result;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    private struct Node {\n        public int Prod;\n        public int[]\
        \ Cnt;\n\n        public Node(int k) {\n            Prod = 1;\n            Cnt\
        \ = new int[k];\n        }\n    }\n\n    private Node[] tree;\n\n    private\
        \ void Merge(ref Node res, Node left, Node right, int k) {\n        res.Prod\
        \ = (left.Prod * right.Prod) % k;\n        for (int i = 0; i < k; i++) {\n \
        \           res.Cnt[i] = left.Cnt[i];\n        }\n        for (int i = 0; i\
        \ < k; i++) {\n            res.Cnt[(left.Prod * i) % k] += right.Cnt[i];\n \
        \       }\n    }\n\n    private void Build(int v, int tl, int tr, int[] nums,\
        \ int k) {\n        tree[v] = new Node(k);\n        if (tl == tr) {\n      \
        \      int val = nums[tl] % k;\n            tree[v].Prod = val;\n          \
        \  tree[v].Cnt[val] = 1;\n        } else {\n            int tm = (tl + tr) /\
        \ 2;\n            Build(2 * v, tl, tm, nums, k);\n            Build(2 * v +\
        \ 1, tm + 1, tr, nums, k);\n            Merge(ref tree[v], tree[2 * v], tree[2\
        \ * v + 1], k);\n        }\n    }\n\n    private void Update(int v, int tl,\
        \ int tr, int pos, int newVal, int k) {\n        if (tl == tr) {\n         \
        \   int val = newVal % k;\n            tree[v].Prod = val;\n            Array.Clear(tree[v].Cnt,\
        \ 0, k);\n            tree[v].Cnt[val] = 1;\n        } else {\n            int\
        \ tm = (tl + tr) / 2;\n            if (pos <= tm)\n                Update(2\
        \ * v, tl, tm, pos, newVal, k);\n            else\n                Update(2\
        \ * v + 1, tm + 1, tr, pos, newVal, k);\n            Merge(ref tree[v], tree[2\
        \ * v], tree[2 * v + 1], k);\n        }\n    }\n\n    private Node Query(int\
        \ v, int tl, int tr, int l, int r, int k) {\n        if (l == tl && r == tr)\
        \ return tree[v];\n        int tm = (tl + tr) / 2;\n        if (r <= tm) return\
        \ Query(2 * v, tl, tm, l, r, k);\n        if (l > tm) return Query(2 * v + 1,\
        \ tm + 1, tr, l, r, k);\n        Node leftRes = Query(2 * v, tl, tm, l, tm,\
        \ k);\n        Node rightRes = Query(2 * v + 1, tm + 1, tr, tm + 1, r, k);\n\
        \        Node res = new Node(k);\n        Merge(ref res, leftRes, rightRes,\
        \ k);\n        return res;\n    }\n\n    public int[] ResultArray(int[] nums,\
        \ int k, int[][] queries) {\n        int n = nums.Length;\n        tree = new\
        \ Node[4 * n];\n        Build(1, 0, n - 1, nums, k);\n\n        int[] result\
        \ = new int[queries.Length];\n        for (int i = 0; i < queries.Length; i++)\
        \ {\n            int idx = queries[i][0];\n            int val = queries[i][1];\n\
        \            int start = queries[i][2];\n            int x = queries[i][3];\n\
        \n            Update(1, 0, n - 1, idx, val, k);\n            Node qNode = Query(1,\
        \ 0, n - 1, start, n - 1, k);\n            result[i] = qNode.Cnt[x];\n     \
        \   }\n\n        return result;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @param {number[][]}\
        \ queries\n * @return {number[]}\n */\nvar resultArray = function(nums, k, queries)\
        \ {\n    const n = nums.length;\n    let N = 1;\n    while (N < n) N *= 2;\n\
        \n    const treeProd = new Int32Array(2 * N);\n    const treeCnt = new Int32Array(2\
        \ * N * k);\n    treeProd.fill(1);\n\n    for (let i = 0; i < n; i++) {\n  \
        \      const val = nums[i] % k;\n        treeProd[N + i] = val;\n        treeCnt[(N\
        \ + i) * k + val] = 1;\n    }\n\n    for (let i = N - 1; i > 0; i--) {\n   \
        \     const lc = 2 * i, rc = 2 * i + 1;\n        const lp = treeProd[lc], rp\
        \ = treeProd[rc];\n        treeProd[i] = (lp * rp) % k;\n        const idxK\
        \ = i * k, lcK = lc * k, rcK = rc * k;\n        for (let j = 0; j < k; j++)\
        \ treeCnt[idxK + j] = treeCnt[lcK + j];\n        for (let j = 0; j < k; j++)\
        \ treeCnt[idxK + (lp * j) % k] += treeCnt[rcK + j];\n    }\n\n    const results\
        \ = [];\n    for (const [idx, val, start, x] of queries) {\n        let curr\
        \ = idx + N;\n        const v = val % k;\n        treeProd[curr] = v;\n    \
        \    for (let j = 0; j < k; j++) treeCnt[curr * k + j] = 0;\n        treeCnt[curr\
        \ * k + v] = 1;\n        curr = Math.floor(curr / 2);\n        while (curr >=\
        \ 1) {\n            const lc = 2 * curr, rc = 2 * curr + 1;\n            const\
        \ lp = treeProd[lc], rp = treeProd[rc];\n            treeProd[curr] = (lp *\
        \ rp) % k;\n            const idxK = curr * k, lcK = lc * k, rcK = rc * k;\n\
        \            for (let j = 0; j < k; j++) treeCnt[idxK + j] = treeCnt[lcK + j];\n\
        \            for (let j = 0; j < k; j++) treeCnt[idxK + (lp * j) % k] += treeCnt[rcK\
        \ + j];\n            curr = Math.floor(curr / 2);\n        }\n\n        let\
        \ l = start + N, r = n - 1 + N;\n        const lNodes = [], rNodes = [];\n \
        \       while (l <= r) {\n            if (l % 2 === 1) lNodes.push(l++);\n \
        \           if (r % 2 === 0) rNodes.push(r--);\n            l = Math.floor(l\
        \ / 2);\n            r = Math.floor(r / 2);\n        }\n\n        const allNodes\
        \ = lNodes.concat(rNodes.reverse());\n        const firstNode = allNodes[0];\n\
        \        let currProd = treeProd[firstNode];\n        let currCnt = new Int32Array(k);\n\
        \        for (let j = 0; j < k; j++) currCnt[j] = treeCnt[firstNode * k + j];\n\
        \n        for (let i = 1; i < allNodes.length; i++) {\n            const nodeIdx\
        \ = allNodes[i];\n            const lp = currProd, rcStart = nodeIdx * k;\n\
        \            const nextCnt = new Int32Array(currCnt);\n            for (let\
        \ j = 0; j < k; j++) nextCnt[(lp * j) % k] += treeCnt[rcStart + j];\n      \
        \      currCnt = nextCnt;\n            currProd = (lp * treeProd[nodeIdx]) %\
        \ k;\n        }\n        results.push(currCnt[x]);\n    }\n    return results;\n\
        };"
      typescript: "function resultArray(nums: number[], k: number, queries: number[][]):\
        \ number[] {\n    const n = nums.length;\n    const treeCounts = new Int32Array((4\
        \ * n + 1) * k);\n    const treeProducts = new Int32Array(4 * n + 1);\n\n  \
        \  function merge(v: number, left: number, right: number): void {\n        const\
        \ pL = treeProducts[left];\n        const vOffset = v * k;\n        const lOffset\
        \ = left * k;\n        const rOffset = right * k;\n        for (let i = 0; i\
        \ < k; i++) {\n            treeCounts[vOffset + i] = treeCounts[lOffset + i];\n\
        \        }\n        for (let vp = 0; vp < k; vp++) {\n            const target\
        \ = (pL * vp) % k;\n            treeCounts[vOffset + target] += treeCounts[rOffset\
        \ + vp];\n        }\n        treeProducts[v] = (pL * treeProducts[right]) %\
        \ k;\n    }\n\n    function build(v: number, tl: number, tr: number): void {\n\
        \        if (tl === tr) {\n            const rem = nums[tl] % k;\n         \
        \   const vOffset = v * k;\n            for (let i = 0; i < k; i++) treeCounts[vOffset\
        \ + i] = 0;\n            treeCounts[vOffset + rem] = 1;\n            treeProducts[v]\
        \ = rem;\n        } else {\n            const tm = (tl + tr) >> 1;\n       \
        \     build(2 * v, tl, tm);\n            build(2 * v + 1, tm + 1, tr);\n   \
        \         merge(v, 2 * v, 2 * v + 1);\n        }\n    }\n\n    function update(v:\
        \ number, tl: number, tr: number, pos: number, newVal: number): void {\n   \
        \     if (tl === tr) {\n            const vOffset = v * k;\n            for\
        \ (let i = 0; i < k; i++) treeCounts[vOffset + i] = 0;\n            treeCounts[vOffset\
        \ + newVal] = 1;\n            treeProducts[v] = newVal;\n        } else {\n\
        \            const tm = (tl + tr) >> 1;\n            if (pos <= tm) update(2\
        \ * v, tl, tm, pos, newVal);\n            else update(2 * v + 1, tm + 1, tr,\
        \ pos, newVal);\n            merge(v, 2 * v, 2 * v + 1);\n        }\n    }\n\
        \n    interface Node {\n        counts: Int32Array;\n        product: number;\n\
        \    }\n\n    function query(v: number, tl: number, tr: number, l: number, r:\
        \ number): Node {\n        if (l === tl && r === tr) {\n            const counts\
        \ = new Int32Array(k);\n            const offset = v * k;\n            for (let\
        \ i = 0; i < k; i++) counts[i] = treeCounts[offset + i];\n            return\
        \ { counts, product: treeProducts[v] };\n        }\n        const tm = (tl +\
        \ tr) >> 1;\n        if (r <= tm) return query(2 * v, tl, tm, l, r);\n     \
        \   if (l > tm) return query(2 * v + 1, tm + 1, tr, l, r);\n\n        const\
        \ leftRes = query(2 * v, tl, tm, l, tm);\n        const rightRes = query(2 *\
        \ v + 1, tm + 1, tr, tm + 1, r);\n\n        const mergedCounts = new Int32Array(leftRes.counts);\n\
        \        const pL = leftRes.product;\n        for (let vp = 0; vp < k; vp++)\
        \ {\n            const target = (pL * vp) % k;\n            mergedCounts[target]\
        \ += rightRes.counts[vp];\n        }\n        return {\n            counts:\
        \ mergedCounts,\n            product: (pL * rightRes.product) % k\n        };\n\
        \    }\n\n    build(1, 0, n - 1);\n    const result: number[] = [];\n    for\
        \ (let i = 0; i < queries.length; i++) {\n        const q = queries[i];\n  \
        \      update(1, 0, n - 1, q[0], q[1] % k);\n        const res = query(1, 0,\
        \ n - 1, q[2], n - 1);\n        result.push(res.counts[q[3]]);\n    }\n    return\
        \ result;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $k\n     * @param Integer[][] $queries\n     * @return Integer[]\n\
        \     */\n    function resultArray($nums, $k, $queries) {\n        $this->k\
        \ = $k;\n        $this->n = count($nums);\n        $this->treeCounts = new SplFixedArray((4\
        \ * $this->n + 1) * $this->k);\n        $this->treeProducts = new SplFixedArray(4\
        \ * $this->n + 1);\n\n        $this->build($nums, 1, 0, $this->n - 1);\n\n \
        \       $results = [];\n        foreach ($queries as $q) {\n            $this->update(1,\
        \ 0, $this->n - 1, $q[0], $q[1] % $k);\n            $res = $this->query(1, 0,\
        \ $this->n - 1, $q[2], $this->n - 1);\n            $results[] = $res['counts'][$q[3]];\n\
        \        }\n        return $results;\n    }\n\n    private $k;\n    private\
        \ $n;\n    private $treeCounts;\n    private $treeProducts;\n\n    private function\
        \ merge($v, $left, $right) {\n        $vOffset = $v * $this->k;\n        $lOffset\
        \ = $left * $this->k;\n        $rOffset = $right * $this->k;\n        $pL =\
        \ $this->treeProducts[$left];\n        for ($i = 0; $i < $this->k; $i++) {\n\
        \            $this->treeCounts[$vOffset + $i] = $this->treeCounts[$lOffset +\
        \ $i];\n        }\n        for ($vp = 0; $vp < $this->k; $vp++) {\n        \
        \    $target = ($pL * $vp) % $this->k;\n            $this->treeCounts[$vOffset\
        \ + $target] += $this->treeCounts[$rOffset + $vp];\n        }\n        $this->treeProducts[$v]\
        \ = ($pL * $this->treeProducts[$right]) % $this->k;\n    }\n\n    private function\
        \ build(&$nums, $v, $tl, $tr) {\n        if ($tl == $tr) {\n            $rem\
        \ = $nums[$tl] % $this->k;\n            $vOffset = $v * $this->k;\n        \
        \    for ($i = 0; $i < $this->k; $i++) $this->treeCounts[$vOffset + $i] = 0;\n\
        \            $this->treeCounts[$vOffset + $rem] = 1;\n            $this->treeProducts[$v]\
        \ = $rem;\n        } else {\n            $tm = ($tl + $tr) >> 1;\n         \
        \   $this->build($nums, 2 * $v, $tl, $tm);\n            $this->build($nums,\
        \ 2 * $v + 1, $tm + 1, $tr);\n            $this->merge($v, 2 * $v, 2 * $v +\
        \ 1);\n        }\n    }\n\n    private function update($v, $tl, $tr, $pos, $newVal)\
        \ {\n        if ($tl == $tr) {\n            $vOffset = $v * $this->k;\n    \
        \        for ($i = 0; $i < $this->k; $i++) $this->treeCounts[$vOffset + $i]\
        \ = 0;\n            $this->treeCounts[$vOffset + $newVal] = 1;\n           \
        \ $this->treeProducts[$v] = $newVal;\n        } else {\n            $tm = ($tl\
        \ + $tr) >> 1;\n            if ($pos <= $tm) $this->update(2 * $v, $tl, $tm,\
        \ $pos, $newVal);\n            else $this->update(2 * $v + 1, $tm + 1, $tr,\
        \ $pos, $newVal);\n            $this->merge($v, 2 * $v, 2 * $v + 1);\n     \
        \   }\n    }\n\n    private function query($v, $tl, $tr, $l, $r) {\n       \
        \ if ($l == $tl && $r == $tr) {\n            $counts = array_fill(0, $this->k,\
        \ 0);\n            $offset = $v * $this->k;\n            for ($i = 0; $i < $this->k;\
        \ $i++) {\n                $counts[$i] = $this->treeCounts[$offset + $i];\n\
        \            }\n            return ['counts' => $counts, 'product' => $this->treeProducts[$v]];\n\
        \        }\n        $tm = ($tl + $tr) >> 1;\n        if ($r <= $tm) return $this->query(2\
        \ * $v, $tl, $tm, $l, $r);\n        if ($l > $tm) return $this->query(2 * $v\
        \ + 1, $tm + 1, $tr, $l, $r);\n\n        $leftRes = $this->query(2 * $v, $tl,\
        \ $tm, $l, $tm);\n        $rightRes = $this->query(2 * $v + 1, $tm + 1, $tr,\
        \ $tm + 1, $r);\n\n        $mergedCounts = $leftRes['counts'];\n        $pL\
        \ = $leftRes['product'];\n        for ($vp = 0; $vp < $this->k; $vp++) {\n \
        \           $target = ($pL * $vp) % $this->k;\n            $mergedCounts[$target]\
        \ += $rightRes['counts'][$vp];\n        }\n        return [\n            'counts'\
        \ => $mergedCounts,\n            'product' => ($pL * $rightRes['product']) %\
        \ $this->k\n        ];\n    }\n}"
      swift: "class Solution {\n    private var treeCounts: [Int] = []\n    private\
        \ var treeProducts: [Int] = []\n    private var k: Int = 0\n    private var\
        \ n: Int = 0\n\n    struct Node {\n        var counts: [Int]\n        var product:\
        \ Int\n    }\n\n    func resultArray(_ nums: [Int], _ k: Int, _ queries: [[Int]])\
        \ -> [Int] {\n        self.k = k\n        self.n = nums.count\n        self.treeCounts\
        \ = [Int](repeating: 0, count: (4 * n + 1) * k)\n        self.treeProducts =\
        \ [Int](repeating: 0, count: 4 * n + 1)\n\n        build(nums, 1, 0, n - 1)\n\
        \n        var results = [Int]()\n        for q in queries {\n            update(1,\
        \ 0, n - 1, q[0], q[1] % k)\n            let res = query(1, 0, n - 1, q[2],\
        \ n - 1)\n            results.append(res.counts[q[3]])\n        }\n        return\
        \ results\n    }\n\n    private func merge(_ v: Int, _ left: Int, _ right: Int)\
        \ {\n        let pL = treeProducts[left]\n        let vOffset = v * k\n    \
        \    let lOffset = left * k\n        let rOffset = right * k\n        for i\
        \ in 0..<k {\n            treeCounts[vOffset + i] = treeCounts[lOffset + i]\n\
        \        }\n        for vp in 0..<k {\n            let target = (pL * vp) %\
        \ k\n            treeCounts[vOffset + target] += treeCounts[rOffset + vp]\n\
        \        }\n        treeProducts[v] = (pL * treeProducts[right]) % k\n    }\n\
        \n    private func build(_ nums: [Int], _ v: Int, _ tl: Int, _ tr: Int) {\n\
        \        if tl == tr {\n            let rem = nums[tl] % k\n            let\
        \ offset = v * k\n            for i in 0..<k { treeCounts[offset + i] = 0 }\n\
        \            treeCounts[offset + rem] = 1\n            treeProducts[v] = rem\n\
        \        } else {\n            let tm = (tl + tr) / 2\n            build(nums,\
        \ 2 * v, tl, tm)\n            build(nums, 2 * v + 1, tm + 1, tr)\n         \
        \   merge(v, 2 * v, 2 * v + 1)\n        }\n    }\n\n    private func update(_\
        \ v: Int, _ tl: Int, _ tr: Int, _ pos: Int, _ newVal: Int) {\n        if tl\
        \ == tr {\n            let offset = v * k\n            for i in 0..<k { treeCounts[offset\
        \ + i] = 0 }\n            treeCounts[offset + newVal] = 1\n            treeProducts[v]\
        \ = newVal\n        } else {\n            let tm = (tl + tr) / 2\n         \
        \   if pos <= tm { update(2 * v, tl, tm, pos, newVal) }\n            else {\
        \ update(2 * v + 1, tm + 1, tr, pos, newVal) }\n            merge(v, 2 * v,\
        \ 2 * v + 1)\n        }\n    }\n\n    private func query(_ v: Int, _ tl: Int,\
        \ _ tr: Int, _ l: Int, _ r: Int) -> Node {\n        if l == tl && r == tr {\n\
        \            var counts = [Int](repeating: 0, count: k)\n            let offset\
        \ = v * k\n            for i in 0..<k { counts[i] = treeCounts[offset + i] }\n\
        \            return Node(counts: counts, product: treeProducts[v])\n       \
        \ }\n        let tm = (tl + tr) / 2\n        if r <= tm { return query(2 * v,\
        \ tl, tm, l, r) }\n        if l > tm { return query(2 * v + 1, tm + 1, tr, l,\
        \ r) }\n\n        let leftRes = query(2 * v, tl, tm, l, tm)\n        let rightRes\
        \ = query(2 * v + 1, tm + 1, tr, tm + 1, r)\n\n        var mergedCounts = leftRes.counts\n\
        \        let pL = leftRes.product\n        for vp in 0..<k {\n            let\
        \ target = (pL * vp) % k\n            mergedCounts[target] += rightRes.counts[vp]\n\
        \        }\n        return Node(counts: mergedCounts, product: (pL * rightRes.product)\
        \ % k)\n    }\n}"
      kotlin: "class Solution {\n    private var treeCounts = IntArray(0)\n    private\
        \ var treeProducts = IntArray(0)\n    private var k: Int = 0\n    private var\
        \ n: Int = 0\n\n    private class Node(val counts: IntArray, val product: Int)\n\
        \n    fun resultArray(nums: IntArray, k: Int, queries: Array<IntArray>): IntArray\
        \ {\n        this.k = k\n        this.n = nums.size\n        this.treeCounts\
        \ = IntArray((4 * n + 1) * k)\n        this.treeProducts = IntArray(4 * n +\
        \ 1)\n\n        build(nums, 1, 0, n - 1)\n\n        val results = IntArray(queries.size)\n\
        \        for (i in queries.indices) {\n            val q = queries[i]\n    \
        \        update(1, 0, n - 1, q[0], q[1] % k)\n            val resNode = query(1,\
        \ 0, n - 1, q[2], n - 1)\n            results[i] = resNode.counts[q[3]]\n  \
        \      }\n        return results\n    }\n\n    private fun merge(v: Int, left:\
        \ Int, right: Int) {\n        val pL = treeProducts[left]\n        val vOffset\
        \ = v * k\n        val lOffset = left * k\n        val rOffset = right * k\n\
        \        for (i in 0 until k) {\n            treeCounts[vOffset + i] = treeCounts[lOffset\
        \ + i]\n        }\n        for (vp in 0 until k) {\n            val target =\
        \ (pL * vp) % k\n            treeCounts[vOffset + target] += treeCounts[rOffset\
        \ + vp]\n        }\n        treeProducts[v] = (pL * treeProducts[right]) % k\n\
        \    }\n\n    private fun build(nums: IntArray, v: Int, tl: Int, tr: Int) {\n\
        \        if (tl == tr) {\n            val rem = nums[tl] % k\n            val\
        \ offset = v * k\n            for (i in 0 until k) treeCounts[offset + i] =\
        \ 0\n            treeCounts[offset + rem] = 1\n            treeProducts[v] =\
        \ rem\n        } else {\n            val tm = (tl + tr) / 2\n            build(nums,\
        \ 2 * v, tl, tm)\n            build(nums, 2 * v + 1, tm + 1, tr)\n         \
        \   merge(v, 2 * v, 2 * v + 1)\n        }\n    }\n\n    private fun update(v:\
        \ Int, tl: Int, tr: Int, pos: Int, newVal: Int) {\n        if (tl == tr) {\n\
        \            val offset = v * k\n            for (i in 0 until k) treeCounts[offset\
        \ + i] = 0\n            treeCounts[offset + newVal] = 1\n            treeProducts[v]\
        \ = newVal\n        } else {\n            val tm = (tl + tr) / 2\n         \
        \   if (pos <= tm) update(2 * v, tl, tm, pos, newVal)\n            else update(2\
        \ * v + 1, tm + 1, tr, pos, newVal)\n            merge(v, 2 * v, 2 * v + 1)\n\
        \        }\n    }\n\n    private fun query(v: Int, tl: Int, tr: Int, l: Int,\
        \ r: Int): Node {\n        if (l == tl && r == tr) {\n            val counts\
        \ = IntArray(k)\n            val offset = v * k\n            for (i in 0 until\
        \ k) counts[i] = treeCounts[offset + i]\n            return Node(counts, treeProducts[v])\n\
        \        }\n        val tm = (tl + tr) / 2\n        if (r <= tm) return query(2\
        \ * v, tl, tm, l, r)\n        if (l > tm) return query(2 * v + 1, tm + 1, tr,\
        \ l, r)\n\n        val leftRes = query(2 * v, tl, tm, l, tm)\n        val rightRes\
        \ = query(2 * v + 1, tm + 1, tr, tm + 1, r)\n\n        val mergedCounts = leftRes.counts.copyOf()\n\
        \        val pL = leftRes.product\n        for (vp in 0 until k) {\n       \
        \     val target = (pL * vp) % k\n            mergedCounts[target] += rightRes.counts[vp]\n\
        \        }\n        return Node(mergedCounts, (pL * rightRes.product) % k)\n\
        \    }\n}"
      dart: "import 'dart:typed_data';\n\nclass Node {\n  int totalProd;\n  final List<int>\
        \ counts;\n  Node(this.totalProd, this.counts);\n}\n\nclass Solution {\n  late\
        \ Int32List treeTotal;\n  late Int32List treeCounts;\n\n  void mergeToNode(int\
        \ v, int leftV, int rightV, int k) {\n    treeTotal[v] = (treeTotal[leftV] *\
        \ treeTotal[rightV]) % k;\n    int v5 = v * 5;\n    int l5 = leftV * 5;\n  \
        \  int r5 = rightV * 5;\n    int lt = treeTotal[leftV];\n\n    for (int i =\
        \ 0; i < k; i++) {\n      treeCounts[v5 + i] = treeCounts[l5 + i];\n    }\n\
        \    for (int i = 0; i < k; i++) {\n      int idx = (lt * i) % k;\n      treeCounts[v5\
        \ + idx] += treeCounts[r5 + i];\n    }\n  }\n\n  void build(int v, int tl, int\
        \ tr, List<int> nums, int k) {\n    if (tl == tr) {\n      int val = nums[tl]\
        \ % k;\n      treeTotal[v] = val;\n      int v5 = v * 5;\n      for (int i =\
        \ 0; i < 5; i++) treeCounts[v5 + i] = 0;\n      treeCounts[v5 + val] = 1;\n\
        \    } else {\n      int tm = (tl + tr) ~/ 2;\n      build(2 * v, tl, tm, nums,\
        \ k);\n      build(2 * v + 1, tm + 1, tr, nums, k);\n      mergeToNode(v, 2\
        \ * v, 2 * v + 1, k);\n    }\n  }\n\n  void update(int v, int tl, int tr, int\
        \ pos, int newVal, int k) {\n    if (tl == tr) {\n      int val = newVal % k;\n\
        \      treeTotal[v] = val;\n      int v5 = v * 5;\n      for (int i = 0; i <\
        \ 5; i++) treeCounts[v5 + i] = 0;\n      treeCounts[v5 + val] = 1;\n    } else\
        \ {\n      int tm = (tl + tr) ~/ 2;\n      if (pos <= tm) {\n        update(2\
        \ * v, tl, tm, pos, newVal, k);\n      } else {\n        update(2 * v + 1, tm\
        \ + 1, tr, pos, newVal, k);\n      }\n      mergeToNode(v, 2 * v, 2 * v + 1,\
        \ k);\n    }\n  }\n\n  Node query(int v, int tl, int tr, int l, int r, int k)\
        \ {\n    if (l == tl && r == tr) {\n      int v5 = v * 5;\n      List<int> resCounts\
        \ = List<int>.filled(5, 0);\n      for (int i = 0; i < 5; i++) resCounts[i]\
        \ = treeCounts[v5 + i];\n      return Node(treeTotal[v], resCounts);\n    }\n\
        \    int tm = (tl + tr) ~/ 2;\n    if (r <= tm) {\n      return query(2 * v,\
        \ tl, tm, l, r, k);\n    } else if (l > tm) {\n      return query(2 * v + 1,\
        \ tm + 1, tr, l, r, k);\n    } else {\n      Node leftRes = query(2 * v, tl,\
        \ tm, l, tm, k);\n      Node rightRes = query(2 * v + 1, tm + 1, tr, tm + 1,\
        \ r, k);\n      int resTotal = (leftRes.totalProd * rightRes.totalProd) % k;\n\
        \      List<int> resCounts = List<int>.filled(5, 0);\n      for (int i = 0;\
        \ i < k; i++) {\n        resCounts[i] = leftRes.counts[i];\n      }\n      for\
        \ (int i = 0; i < k; i++) {\n        int idx = (leftRes.totalProd * i) % k;\n\
        \        resCounts[idx] += rightRes.counts[i];\n      }\n      return Node(resTotal,\
        \ resCounts);\n    }\n  }\n\n  List<int> resultArray(List<int> nums, int k,\
        \ List<List<int>> queries) {\n    int n = nums.length;\n    treeTotal = Int32List(4\
        \ * n + 1);\n    treeCounts = Int32List((4 * n + 1) * 5);\n\n    build(1, 0,\
        \ n - 1, nums, k);\n\n    List<int> result = [];\n    for (var q in queries)\
        \ {\n      int idx = q[0];\n      int val = q[1];\n      int start = q[2];\n\
        \      int x = q[3];\n\n      update(1, 0, n - 1, idx, val, k);\n      Node\
        \ res = query(1, 0, n - 1, start, n - 1, k);\n      result.add(res.counts[x]);\n\
        \    }\n\n    return result;\n  }\n}"
      go: "package main\n\ntype Node struct {\n\ttotalProd int\n\tcounts    [5]int\n\
        }\n\ntype SegmentTree struct {\n\ttreeTotal  []int\n\ttreeCounts []int\n\tk\
        \          int\n\tn          int\n}\n\nfunc (st *SegmentTree) mergeToNode(v,\
        \ leftV, rightV int) {\n\tst.treeTotal[v] = (st.treeTotal[leftV] * st.treeTotal[rightV])\
        \ % st.k\n\tv5, l5, r5 := v*5, leftV*5, rightV*5\n\tlt := st.treeTotal[leftV]\n\
        \n\tfor i := 0; i < st.k; i++ {\n\t\tst.treeCounts[v5+i] = st.treeCounts[l5+i]\n\
        \t}\n\tfor i := 0; i < st.k; i++ {\n\t\tidx := (lt * i) % st.k\n\t\tst.treeCounts[v5+idx]\
        \ += st.treeCounts[r5+i]\n\t}\n}\n\nfunc (st *SegmentTree) build(v, tl, tr int,\
        \ nums []int) {\n\tif tl == tr {\n\t\tval := nums[tl] % st.k\n\t\tst.treeTotal[v]\
        \ = val\n\t\tv5 := v * 5\n\t\tfor i := 0; i < 5; i++ {\n\t\t\tst.treeCounts[v5+i]\
        \ = 0\n\t\t}\n\t\tst.treeCounts[v5+val] = 1\n\t} else {\n\t\ttm := (tl + tr)\
        \ / 2\n\t\tst.build(2*v, tl, tm, nums)\n\t\tst.build(2*v+1, tm+1, tr, nums)\n\
        \t\tst.mergeToNode(v, 2*v, 2*v+1)\n\t}\n}\n\nfunc (st *SegmentTree) update(v,\
        \ tl, tr, pos, newVal int) {\n\tif tl == tr {\n\t\tval := newVal % st.k\n\t\t\
        st.treeTotal[v] = val\n\t\tv5 := v * 5\n\t\tfor i := 0; i < 5; i++ {\n\t\t\t\
        st.treeCounts[v5+i] = 0\n\t\t}\n\t\tst.treeCounts[v5+val] = 1\n\t} else {\n\t\
        \ttm := (tl + tr) / 2\n\t\tif pos <= tm {\n\t\t\tst.update(2*v, tl, tm, pos,\
        \ newVal)\n\t\t} else {\n\t\t\tst.update(2*v+1, tm+1, tr, pos, newVal)\n\t\t\
        }\n\t\tst.mergeToNode(v, 2*v, 2*v+1)\n\t}\n}\n\nfunc (st *SegmentTree) query(v,\
        \ tl, tr, l, r int) Node {\n\tif l == tl && r == tr {\n\t\toffset := v * 5\n\
        \t\tvar res Node\n\t\tres.totalProd = st.treeTotal[v]\n\t\tfor i := 0; i < 5;\
        \ i++ {\n\t\t\tres.counts[i] = st.treeCounts[offset+i]\n\t\t}\n\t\treturn res\n\
        \t}\n\ttm := (tl + tr) / 2\n\tif r <= tm {\n\t\treturn st.query(2*v, tl, tm,\
        \ l, r)\n\t} else if l > tm {\n\t\treturn st.query(2*v+1, tm+1, tr, l, r)\n\t\
        } else {\n\t\tleftRes := st.query(2*v, tl, tm, l, tm)\n\t\trightRes := st.query(2*v+1,\
        \ tm+1, tr, tm+1, r)\n\t\tvar res Node\n\t\tres.totalProd = (leftRes.totalProd\
        \ * rightRes.totalProd) % st.k\n\t\tfor i := 0; i < st.k; i++ {\n\t\t\tres.counts[i]\
        \ = leftRes.counts[i]\n\t\t}\n\t\tfor i := 0; i < st.k; i++ {\n\t\t\tidx :=\
        \ (leftRes.totalProd * i) % st.k\n\t\t\tres.counts[idx] += rightRes.counts[i]\n\
        \t\t}\n\t\treturn res\n\t}\n}\n\nfunc resultArray(nums []int, k int, queries\
        \ [][]int) []int {\n\tn := len(nums)\n\tst := &SegmentTree{\n\t\ttreeTotal:\
        \  make([]int, 4*n+1),\n\t\ttreeCounts: make([]int, (4*n+1)*5),\n\t\tk:    \
        \      k,\n\t\tn:          n,\n\t}\n\n\tst.build(1, 0, n-1, nums)\n\n\tresult\
        \ := make([]int, len(queries))\n\tfor i, q := range queries {\n\t\tidx, val,\
        \ start, x := q[0], q[1], q[2], q[3]\n\t\tst.update(1, 0, n-1, idx, val)\n\t\
        \tresNode := st.query(1, 0, n-1, start, n-1)\n\t\tresult[i] = resNode.counts[x]\n\
        \t}\n\n\treturn result\n}"
      ruby: "def result_array(nums, k, queries)\n  n = nums.length\n  @tree_total =\
        \ Array.new(4 * n + 1, 0)\n  @tree_counts = Array.new((4 * n + 1) * 5, 0)\n\n\
        \  def merge_to_node(v, left_v, right_v, k)\n    @tree_total[v] = (@tree_total[left_v]\
        \ * @tree_total[right_v]) % k\n    v5 = v * 5\n    l5 = left_v * 5\n    r5 =\
        \ right_v * 5\n    lt = @tree_total[left_v]\n\n    i = 0\n    while i < k\n\
        \      @tree_counts[v5 + i] = @tree_counts[l5 + i]\n      i += 1\n    end\n\
        \    i = 0\n    while i < k\n      idx = (lt * i) % k\n      @tree_counts[v5\
        \ + idx] += @tree_counts[r5 + i]\n      i += 1\n    end\n  end\n\n  def build(v,\
        \ tl, tr, nums, k)\n    if tl == tr\n      val = nums[tl] % k\n      @tree_total[v]\
        \ = val\n      v5 = v * 5\n      @tree_counts[v5 + val] = 1\n    else\n    \
        \  tm = (tl + tr) / 2\n      build(2 * v, tl, tm, nums, k)\n      build(2 *\
        \ v + 1, tm + 1, tr, nums, k)\n      merge_to_node(v, 2 * v, 2 * v + 1, k)\n\
        \    end\n  end\n\n  def update(v, tl, tr, pos, new_val, k)\n    if tl == tr\n\
        \      val = new_val % k\n      @tree_total[v] = val\n      v5 = v * 5\n   \
        \   i = 0\n      while i < 5\n        @tree_counts[v5 + i] = 0\n        i +=\
        \ 1\n      end\n      @tree_counts[v5 + val] = 1\n    else\n      tm = (tl +\
        \ tr) / 2\n      if pos <= tm\n        update(2 * v, tl, tm, pos, new_val, k)\n\
        \      else\n        update(2 * v + 1, tm + 1, tr, pos, new_val, k)\n      end\n\
        \      merge_to_node(v, 2 * v, 2 * v + 1, k)\n    end\n  end\n\n  def query(v,\
        \ tl, tr, l, r, k)\n    if l == tl && r == tr\n      v5 = v * 5\n      return\
        \ [@tree_total[v], @tree_counts[v5, 5]]\n    end\n    tm = (tl + tr) / 2\n \
        \   if r <= tm\n      return query(2 * v, tl, tm, l, r, k)\n    elsif l > tm\n\
        \      return query(2 * v + 1, tm + 1, tr, l, r, k)\n    else\n      left_total,\
        \ left_counts = query(2 * v, tl, tm, l, tm, k)\n      right_total, right_counts\
        \ = query(2 * v + 1, tm + 1, tr, tm + 1, r, k)\n      res_total = (left_total\
        \ * right_total) % k\n      res_counts = Array.new(5, 0)\n      i = 0\n    \
        \  while i < k\n        res_counts[i] = left_counts[i]\n        i += 1\n   \
        \   end\n      i = 0\n      while i < k\n        idx = (left_total * i) % k\n\
        \        res_counts[idx] += right_counts[i]\n        i += 1\n      end\n   \
        \   return [res_total, res_counts]\n    end\n  end\n\n  build(1, 0, n - 1, nums,\
        \ k)\n\n  results = []\n  queries.each do |index, value, start, x|\n    update(1,\
        \ 0, n - 1, index, value, k)\n    res_total, res_counts = query(1, 0, n - 1,\
        \ start, n - 1, k)\n    results << res_counts[x]\n  end\n\n  results\nend"
      scala: "class Node(val totalProd: Int, val counts: Array[Int])\n\nobject Solution\
        \ {\n    def resultArray(nums: Array[Int], k: Int, queries: Array[Array[Int]]):\
        \ Array[Int] = {\n        val n = nums.length\n        val treeTotal = new Array[Int](4\
        \ * n + 1)\n        val treeCounts = new Array[Int]((4 * n + 1) * 5)\n\n   \
        \     def mergeToNode(v: Int, leftV: Int, rightV: Int): Unit = {\n         \
        \   treeTotal(v) = (treeTotal(leftV) * treeTotal(rightV)) % k\n            val\
        \ v5 = v * 5\n            val l5 = leftV * 5\n            val r5 = rightV *\
        \ 5\n            val lt = treeTotal(leftV)\n\n            var i = 0\n      \
        \      while (i < k) {\n                treeCounts(v5 + i) = treeCounts(l5 +\
        \ i)\n                i += 1\n            }\n            i = 0\n           \
        \ while (i < k) {\n                val idx = (lt * i) % k\n                treeCounts(v5\
        \ + idx) += treeCounts(r5 + i)\n                i += 1\n            }\n    \
        \    }\n\n        def build(v: Int, tl: Int, tr: Int): Unit = {\n          \
        \  if (tl == tr) {\n                val valMod = nums(tl) % k\n            \
        \    treeTotal(v) = valMod\n                val v5 = v * 5\n               \
        \ var i = 0\n                while (i < 5) {\n                    treeCounts(v5\
        \ + i) = 0\n                    i += 1\n                }\n                treeCounts(v5\
        \ + valMod) = 1\n            } else {\n                val tm = (tl + tr) /\
        \ 2\n                build(2 * v, tl, tm)\n                build(2 * v + 1,\
        \ tm + 1, tr)\n                mergeToNode(v, 2 * v, 2 * v + 1)\n          \
        \  }\n        }\n\n        def update(v: Int, tl: Int, tr: Int, pos: Int, newVal:\
        \ Int): Unit = {\n            if (tl == tr) {\n                val valMod =\
        \ newVal % k\n                treeTotal(v) = valMod\n                val v5\
        \ = v * 5\n                var i = 0\n                while (i < 5) {\n    \
        \                treeCounts(v5 + i) = 0\n                    i += 1\n      \
        \          }\n                treeCounts(v5 + valMod) = 1\n            } else\
        \ {\n                val tm = (tl + tr) / 2\n                if (pos <= tm)\
        \ {\n                    update(2 * v, tl, tm, pos, newVal)\n              \
        \  } else {\n                    update(2 * v + 1, tm + 1, tr, pos, newVal)\n\
        \                }\n                mergeToNode(v, 2 * v, 2 * v + 1)\n     \
        \       }\n        }\n\n        def query(v: Int, tl: Int, tr: Int, l: Int,\
        \ r: Int): Node = {\n            if (l == tl && r == tr) {\n               \
        \ val counts = new Array[Int](5)\n                val offset = v * 5\n     \
        \           var i = 0\n                while (i < 5) {\n                   \
        \ counts(i) = treeCounts(offset + i)\n                    i += 1\n         \
        \       }\n                return new Node(treeTotal(v), counts)\n         \
        \   }\n            val tm = (tl + tr) / 2\n            if (r <= tm) {\n    \
        \            query(2 * v, tl, tm, l, r)\n            } else if (l > tm) {\n\
        \                query(2 * v + 1, tm + 1, tr, l, r)\n            } else {\n\
        \                val leftRes = query(2 * v, tl, tm, l, tm)\n               \
        \ val rightRes = query(2 * v + 1, tm + 1, tr, tm + 1, r)\n                val\
        \ resTotal = (leftRes.totalProd * rightRes.totalProd) % k\n                val\
        \ resCounts = new Array[Int](5)\n                var i = 0\n               \
        \ while (i < k) {\n                    resCounts(i) = leftRes.counts(i)\n  \
        \                  i += 1\n                }\n                i = 0\n      \
        \          while (i < k) {\n                    val idx = (leftRes.totalProd\
        \ * i) % k\n                    resCounts(idx) += rightRes.counts(i)\n     \
        \               i += 1\n                }\n                new Node(resTotal,\
        \ resCounts)\n            }\n        }\n\n        build(1, 0, n - 1)\n\n   \
        \     val resArr = new Array[Int](queries.length)\n        var idx = 0\n   \
        \     while (idx < queries.length) {\n            val q = queries(idx)\n   \
        \         update(1, 0, n - 1, q(0), q(1))\n            val qResult = query(1,\
        \ 0, n - 1, q(2), n - 1)\n            resArr(idx) = qResult.counts(q(3))\n \
        \           idx += 1\n        }\n        resArr\n    }\n}"
      rust: "impl Solution {\n    pub fn result_array(nums: Vec<i32>, k: i32, queries:\
        \ Vec<Vec<i32>>) -> Vec<i32> {\n        let n = nums.len();\n        let k_usize\
        \ = k as usize;\n\n        #[derive(Clone, Copy)]\n        struct Node {\n \
        \           prod: i32,\n            counts: [i32; 5],\n        }\n\n       \
        \ fn merge(l: &Node, r: &Node, k: usize) -> Node {\n            let mut res\
        \ = Node {\n                prod: (l.prod * r.prod) % k as i32,\n          \
        \      counts: [0; 5],\n            };\n            for i in 0..k {\n      \
        \          res.counts[i] += l.counts[i];\n                let target = (l.prod\
        \ as usize * i) % k;\n                res.counts[target] += r.counts[i];\n \
        \           }\n            res\n        }\n\n        let mut tree = vec![Node\
        \ { prod: 0, counts: [0; 5] }; 4 * n];\n\n        fn build(tree: &mut [Node],\
        \ nums: &[i32], node: usize, start: usize, end: usize, k: usize) {\n       \
        \     if start == end {\n                let val_mod = (nums[start] % k as i32)\
        \ as usize;\n                tree[node].prod = val_mod as i32;\n           \
        \     tree[node].counts[val_mod] = 1;\n                return;\n           \
        \ }\n            let mid = (start + end) / 2;\n            build(tree, nums,\
        \ 2 * node, start, mid, k);\n            build(tree, nums, 2 * node + 1, mid\
        \ + 1, end, k);\n            tree[node] = merge(&tree[2 * node], &tree[2 * node\
        \ + 1], k);\n        }\n\n        fn update(tree: &mut [Node], node: usize,\
        \ start: usize, end: usize, idx: usize, val: i32, k: usize) {\n            if\
        \ start == end {\n                let val_mod = (val % k as i32) as usize;\n\
        \                tree[node].prod = val_mod as i32;\n                tree[node].counts\
        \ = [0; 5];\n                tree[node].counts[val_mod] = 1;\n             \
        \   return;\n            }\n            let mid = (start + end) / 2;\n     \
        \       if idx <= mid {\n                update(tree, 2 * node, start, mid,\
        \ idx, val, k);\n            } else {\n                update(tree, 2 * node\
        \ + 1, mid + 1, end, idx, val, k);\n            }\n            tree[node] =\
        \ merge(&tree[2 * node], &tree[2 * node + 1], k);\n        }\n\n        fn query(tree:\
        \ &[Node], node: usize, start: usize, end: usize, l: usize, r: usize, k: usize)\
        \ -> Node {\n            if l == start && r == end {\n                return\
        \ tree[node];\n            }\n            let mid = (start + end) / 2;\n   \
        \         if r <= mid {\n                return query(tree, 2 * node, start,\
        \ mid, l, r, k);\n            } else if l > mid {\n                return query(tree,\
        \ 2 * node + 1, mid + 1, end, l, r, k);\n            }\n            let left_res\
        \ = query(tree, 2 * node, start, mid, l, mid, k);\n            let right_res\
        \ = query(tree, 2 * node + 1, mid + 1, end, mid + 1, r, k);\n            merge(&left_res,\
        \ &right_res, k)\n        }\n\n        build(&mut tree, &nums, 1, 0, n - 1,\
        \ k_usize);\n\n        let mut results = Vec::with_capacity(queries.len());\n\
        \        for q in queries {\n            let idx = q[0] as usize;\n        \
        \    let val = q[1];\n            let start = q[2] as usize;\n            let\
        \ x = q[3] as usize;\n            update(&mut tree, 1, 0, n - 1, idx, val, k_usize);\n\
        \            let res_node = query(&tree, 1, 0, n - 1, start, n - 1, k_usize);\n\
        \            results.push(res_node.counts[x]);\n        }\n        results\n\
        \    }\n}"
      racket: "(define/contract (result-array nums k queries)\n  (-> (listof exact-integer?)\
        \ exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))\n\
        \  (let* ([n (length nums)]\n         [nums-vec (list->vector nums)]\n     \
        \    [tree (make-vector (* 4 n))])\n\n    (define (merge-nodes l-prod l-counts\
        \ r-prod r-counts k)\n      (let* ([new-prod (modulo (* l-prod r-prod) k)]\n\
        \             [new-counts (vector-copy l-counts)])\n        (for ([i (in-range\
        \ k)])\n          (let* ([r-val (vector-ref r-counts i)]\n                 [target-idx\
        \ (modulo (* l-prod i) k)]\n                 [old-val (vector-ref new-counts\
        \ target-idx)])\n            (vector-set! new-counts target-idx (+ old-val r-val))))\n\
        \        (cons new-prod new-counts)))\n\n    (define (build tree-vec nums-vec\
        \ node start end k)\n      (if (= start end)\n          (let* ([v (modulo (vector-ref\
        \ nums-vec start) k)]\n                 [counts (make-vector k 0)])\n      \
        \      (vector-set! counts v 1)\n            (vector-set! tree-vec node (cons\
        \ v counts)))\n          (let* ([mid (quotient (+ start end) 2)]\n         \
        \        [left-node (* 2 node)]\n                 [right-node (+ 1 (* 2 node))])\n\
        \            (build tree-vec nums-vec left-node start mid k)\n            (build\
        \ tree-vec nums-vec right-node (+ mid 1) end k)\n            (let ([left-res\
        \ (vector-ref tree-vec left-node)]\n                  [right-res (vector-ref\
        \ tree-vec right-node)])\n              (vector-set! tree-vec node (merge-nodes\
        \ (car left-res) (cdr left-res)\n                                          \
        \           (car right-res) (cdr right-res) k))))))\n\n    (define (update tree-vec\
        \ node start end idx val k)\n      (if (= start end)\n          (let* ([v (modulo\
        \ val k)]\n                 [counts (make-vector k 0)])\n            (vector-set!\
        \ counts v 1)\n            (vector-set! tree-vec node (cons v counts)))\n  \
        \        (let* ([mid (quotient (+ start end) 2)]\n                 [left-node\
        \ (* 2 node)]\n                 [right-node (+ 1 (* 2 node))])\n           \
        \ (if (<= idx mid)\n                (update tree-vec left-node start mid idx\
        \ val k)\n                (update tree-vec right-node (+ mid 1) end idx val\
        \ k))\n            (let ([left-res (vector-ref tree-vec left-node)]\n      \
        \            [right-res (vector-ref tree-vec right-node)])\n              (vector-set!\
        \ tree-vec node (merge-nodes (car left-res) (cdr left-res)\n               \
        \                                      (car right-res) (cdr right-res) k))))))\n\
        \n    (define (query tree-vec node start end l r k)\n      (if (and (= l start)\
        \ (= r end))\n          (vector-ref tree-vec node)\n          (let* ([mid (quotient\
        \ (+ start end) 2)]\n                 [left-node (* 2 node)]\n             \
        \    [right-node (+ 1 (* 2 node))])\n            (cond\n              [(<= r\
        \ mid) (query tree-vec left-node start mid l r k)]\n              [(> l mid)\
        \ (query tree-vec right-node (+ mid 1) end l r k)]\n              [else\n  \
        \             (let ([left-res (query tree-vec left-node start mid l mid k)]\n\
        \                     [right-res (query tree-vec right-node (+ mid 1) end (+\
        \ mid 1) r k)])\n                 (merge-nodes (car left-res) (cdr left-res)\n\
        \                             (car right-res) (cdr right-res) k))]))))\n\n \
        \   (build tree nums-vec 1 0 (- n 1) k)\n    (for/list ([q queries])\n     \
        \ (let ([idx (list-ref q 0)]\n            [val (list-ref q 1)]\n           \
        \ [start (list-ref q 2)]\n            [x (list-ref q 3)])\n        (update tree\
        \ 1 0 (- n 1) idx val k)\n        (let* ([res-node (query tree 1 0 (- n 1) start\
        \ (- n 1) k)]\n               [counts (cdr res-node)])\n          (vector-ref\
        \ counts x))))))"
      erlang: "-spec result_array(Nums :: [integer()], K :: integer(), Queries :: [[integer()]])\
        \ -> [integer()].\nresult_array(Nums, K, Queries) ->\n    N = length(Nums),\n\
        \    NumsTuple = list_to_tuple(Nums),\n    Tree = build_tree(NumsTuple, 1, N,\
        \ K),\n    process_queries(Queries, Tree, N, K, []).\n\nbuild_tree(NumsTuple,\
        \ Start, End, K) ->\n    if Start == End ->\n        Val = element(Start, NumsTuple)\
        \ rem K,\n        Counts = setelement(Val + 1, erlang:make_tuple(K, 0), 1),\n\
        \        {Val, Counts, nil, nil};\n    true ->\n        Mid = (Start + End)\
        \ div 2,\n        Left = build_tree(NumsTuple, Start, Mid, K),\n        Right\
        \ = build_tree(NumsTuple, Mid + 1, End, K),\n        merge_full(Left, Right,\
        \ K)\n    end.\n\nmerge_full(Left, Right, K) ->\n    {LProd, LCounts, _, _}\
        \ = Left,\n    {RProd, RCounts, _, _} = Right,\n    {NewProd, NewCounts} = merge_counts(LProd,\
        \ LCounts, RProd, RCounts, K),\n    {NewProd, NewCounts, Left, Right}.\n\nmerge_counts(LProd,\
        \ LCounts, RProd, RCounts, K) ->\n    NewProd = (LProd * RProd) rem K,\n   \
        \ FinalCounts = lists:foldl(fun(I, Acc) ->\n        TargetIdx = (LProd * I)\
        \ rem K,\n        OldVal = element(TargetIdx + 1, Acc),\n        RI = element(I\
        \ + 1, RCounts),\n        setelement(TargetIdx + 1, Acc, OldVal + RI)\n    end,\
        \ LCounts, lists:seq(0, K - 1)),\n    {NewProd, FinalCounts}.\n\nupdate_tree(Tree,\
        \ Start, End, Idx, Val, K) ->\n    if Start == End ->\n        V = Val rem K,\n\
        \        Counts = setelement(V + 1, erlang:make_tuple(K, 0), 1),\n        {V,\
        \ Counts, nil, nil};\n    true ->\n        Mid = (Start + End) div 2,\n    \
        \    {_, _, Left, Right} = Tree,\n        if\n            Idx =< Mid ->\n  \
        \              NewLeft = update_tree(Left, Start, Mid, Idx, Val, K),\n     \
        \           merge_full(NewLeft, Right, K);\n            true ->\n          \
        \      NewRight = update_tree(Right, Mid + 1, End, Idx, Val, K),\n         \
        \       merge_full(Left, NewRight, K)\n        end\n    end.\n\nquery_tree(Tree,\
        \ Start, End, QStart, QEnd, K) ->\n    if (QStart == Start) and (QEnd == End)\
        \ ->\n        {element(1, Tree), element(2, Tree)};\n    true ->\n        Mid\
        \ = (Start + End) div 2,\n        {_, _, Left, Right} = Tree,\n        if\n\
        \            QEnd =< Mid -> query_tree(Left, Start, Mid, QStart, QEnd, K);\n\
        \            QStart > Mid -> query_tree(Right, Mid + 1, End, QStart, QEnd, K);\n\
        \            true ->\n                {LP, LC} = query_tree(Left, Start, Mid,\
        \ QStart, Mid, K),\n                {RP, RC} = query_tree(Right, Mid + 1, End,\
        \ Mid + 1, QEnd, K),\n                merge_counts(LP, LC, RP, RC, K)\n    \
        \    end\n    end.\n\nprocess_queries([], _Tree, _N, _K, Acc) -> lists:reverse(Acc);\n\
        process_queries([[Idx, Val, Start, X] | Rest], Tree, N, K, Acc) ->\n    NewTree\
        \ = update_tree(Tree, 1, N, Idx + 1, Val, K),\n    {_, Counts} = query_tree(NewTree,\
        \ 1, N, Start + 1, N, K),\n    process_queries(Rest, NewTree, N, K, [element(X\
        \ + 1, Counts) | Acc])."
      elixir: "defmodule Solution do\n  @spec result_array(nums :: [integer], k :: integer,\
        \ queries :: [[integer]]) :: [integer]\n  def result_array(nums, k, queries)\
        \ do\n    n = length(nums)\n    nums_tuple = List.to_tuple(nums)\n    tree =\
        \ build(nums_tuple, 0, n - 1, k)\n\n    {_final_tree, results} = Enum.map_reduce(queries,\
        \ tree, fn [idx, val, start, x], current_tree ->\n      updated_tree = update(current_tree,\
        \ 0, n - 1, idx, val, k)\n      {_p, counts} = query(updated_tree, 0, n - 1,\
        \ start, n - 1, k)\n      {elem(counts, x), updated_tree}\n    end)\n    results\n\
        \  end\n\n  defp build(nums_tuple, start, stop, k) do\n    if start == stop\
        \ do\n      val = Integer.mod(elem(nums_tuple, start), k)\n      counts = List.to_tuple(for\
        \ i <- 0..(k - 1), do: (if i == val, do: 1, else: 0))\n      {val, counts, nil,\
        \ nil}\n    else\n      mid = div(start + stop, 2)\n      left = build(nums_tuple,\
        \ start, mid, k)\n      right = build(nums_tuple, mid + 1, stop, k)\n      merge_full(left,\
        \ right, k)\n    end\n  end\n\n  defp update(tree, start, stop, idx, val, k)\
        \ do\n    if start == stop do\n      val_mod = Integer.mod(val, k)\n      counts\
        \ = List.to_tuple(for i <- 0..(k - 1), do: (if i == val_mod, do: 1, else: 0))\n\
        \      {val_mod, counts, nil, nil}\n    else\n      mid = div(start + stop,\
        \ 2)\n      {_, _, left, right} = tree\n      if idx <= mid do\n        new_left\
        \ = update(left, start, mid, idx, val, k)\n        merge_full(new_left, right,\
        \ k)\n      else\n        new_right = update(right, mid + 1, stop, idx, val,\
        \ k)\n        merge_full(left, new_right, k)\n      end\n    end\n  end\n\n\
        \  defp query(tree, start, stop, q_start, q_stop, k) do\n    if q_start == start\
        \ and q_stop == stop do\n      {elem(tree, 0), elem(tree, 1)}\n    else\n  \
        \    mid = div(start + stop, 2)\n      {_, _, left, right} = tree\n      cond\
        \ do\n        q_stop <= mid -> query(left, start, mid, q_start, q_stop, k)\n\
        \        q_start > mid -> query(right, mid + 1, stop, q_start, q_stop, k)\n\
        \        true ->\n          {lp, lc} = query(left, start, mid, q_start, mid,\
        \ k)\n          {rp, rc} = query(right, mid + 1, stop, mid + 1, q_stop, k)\n\
        \          merge_counts(lp, lc, rp, rc, k)\n      end\n    end\n  end\n\n  defp\
        \ merge_full({lp, lc, ll, lr}, {rp, rc, rl, rr}, k) do\n    {p, nc} = merge_counts(lp,\
        \ lc, rp, rc, k)\n    {p, nc, {lp, lc, ll, lr}, {rp, rc, rl, rr}}\n  end\n\n\
        \  defp merge_counts(lp, lc, _rp, rc, k) do\n    p = Integer.mod(lp * _rp, k)\n\
        \    nc = Enum.reduce(0..(k - 1), lc, fn i, acc ->\n      target = Integer.mod(lp\
        \ * i, k)\n      put_elem(acc, target, elem(acc, target) + elem(rc, i))\n  \
        \  end)\n    {p, nc}\n  end\nend"
    approach: 'The problem asks us to efficiently update an array and find the number
      of prefixes of a given subarray `nums[start..n-1]` whose product modulo `k` equals
      a target `x`. Since `k` is very small (between 1 and 5), we can use a segment
      tree where each node stores the total product of its range modulo `k` and an array
      of size `k` representing the counts of prefixes within that range that result
      in each possible remainder [0, k-1]. This allows us to merge two adjacent segments:
      the prefix counts of the combined segment consist of all prefix counts from the
      left child plus the prefix counts from the right child multiplied by the total
      product of the left child (modulo `k`).'
    time_complexity: O((N + Q) * k * log N), where N is the length of the array and
      Q is the number of queries. Building the tree takes O(N * k), and each query involves
      one point update and one range query, each taking O(k * log N) time.
    space_complexity: O(N * k) to store the segment tree nodes, with each node containing
      an array of size k for prefix product counts and a scalar for the range product.
    elapsed_time: 424.0671167373657
    model: gemini-3-flash-preview
    generated_at: '2026-09-22 02:47:34 '
---

## Problem #3525: Find X Value of Array II

**Difficulty:** Hard

**Topics:** Array, Math, Segment Tree

## Problem Description

<p>You are given an array of <strong>positive</strong> integers <code>nums</code> and a <strong>positive</strong> integer <code>k</code>. You are also given a 2D array <code>queries</code>, where <code>queries[i] = [index<sub>i</sub>, value<sub>i</sub>, start<sub>i</sub>, x<sub>i</sub>]</code>.</p>

<p>You are allowed to perform an operation <strong>once</strong> on <code>nums</code>, where you can remove any <strong>suffix</strong> from <code>nums</code> such that <code>nums</code> remains <strong>non-empty</strong>.</p>

<p>The <strong>x-value</strong> of <code>nums</code> <strong>for a given</strong> <code>x</code> is defined as the number of ways to perform this operation so that the <strong>product</strong> of the remaining elements leaves a <em>remainder</em> of <code>x</code> <strong>modulo</strong> <code>k</code>.</p>

<p>For each query in <code>queries</code> you need to determine the <strong>x-value</strong> of <code>nums</code> for <code>x<sub>i</sub></code> after performing the following actions:</p>

<ul>
	<li>Update <code>nums[index<sub>i</sub>]</code> to <code>value<sub>i</sub></code>. Only this step persists for the rest of the queries.</li>
	<li><strong>Remove</strong> the prefix <code>nums[0..(start<sub>i</sub> - 1)]</code> (where <code>nums[0..(-1)]</code> will be used to represent the <strong>empty</strong> prefix).</li>
</ul>

<p>Return an array <code>result</code> of size <code>queries.length</code> where <code>result[i]</code> is the answer for the <code>i<sup>th</sup></code> query.</p>

<p>A <strong>prefix</strong> of an array is a <span data-keyword="subarray">subarray</span> that starts from the beginning of the array and extends to any point within it.</p>

<p>A <strong>suffix</strong> of an array is a <span data-keyword="subarray">subarray</span> that starts at any point within the array and extends to the end of the array.</p>

<p><strong>Note</strong> that the prefix and suffix to be chosen for the operation can be <strong>empty</strong>.</p>

<p><strong>Note</strong> that x-value has a <em>different</em> definition in this version.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,2,2]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For query 0, <code>nums</code> becomes <code>[1, 2, 2, 4, 5]</code>, and the empty prefix <strong>must</strong> be removed. The possible operations are:

	<ul>
		<li>Remove the suffix <code>[2, 4, 5]</code>. <code>nums</code> becomes <code>[1, 2]</code>.</li>
		<li>Remove the empty suffix. <code>nums</code> becomes <code>[1, 2, 2, 4, 5]</code> with a product 80, which gives remainder 2 when divided by 3.</li>
	</ul>
	</li>
	<li>For query 1, <code>nums</code> becomes <code>[1, 2, 2, 3, 5]</code>, and the prefix <code>[1, 2, 2]</code> <strong>must</strong> be removed. The possible operations are:
	<ul>
		<li>Remove the empty suffix. <code>nums</code> becomes <code>[3, 5]</code>.</li>
		<li>Remove the suffix <code>[5]</code>. <code>nums</code> becomes <code>[3]</code>.</li>
	</ul>
	</li>
	<li>For query 2, <code>nums</code> becomes <code>[1, 2, 2, 3, 5]</code>, and the empty prefix <strong>must</strong> be removed. The possible operations are:
	<ul>
		<li>Remove the suffix <code>[2, 2, 3, 5]</code>. <code>nums</code> becomes <code>[1]</code>.</li>
		<li>Remove the suffix <code>[3, 5]</code>. <code>nums</code> becomes <code>[1, 2, 2]</code>.</li>
	</ul>
	</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,4,8,16,32], k = 4, queries = [[0,2,0,2],[0,2,0,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,0]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For query 0, <code>nums</code> becomes <code>[2, 2, 4, 8, 16, 32]</code>. The only possible operation is:

	<ul>
		<li>Remove the suffix <code>[2, 4, 8, 16, 32]</code>.</li>
	</ul>
	</li>
	<li>For query 1, <code>nums</code> becomes <code>[2, 2, 4, 8, 16, 32]</code>. There is no possible way to perform the operation.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,2,1,1], k = 2, queries = [[2,1,0,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[5]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 5</code></li>
	<li><code>1 &lt;= queries.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>queries[i] == [index<sub>i</sub>, value<sub>i</sub>, start<sub>i</sub>, x<sub>i</sub>]</code></li>
	<li><code>0 &lt;= index<sub>i</sub> &lt;= nums.length - 1</code></li>
	<li><code>1 &lt;= value<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;= nums.length - 1</code></li>
	<li><code>0 &lt;= x<sub>i</sub> &lt;= k - 1</code></li>
</ul>


## Hints

1. Use a segment tree to efficiently maintain and merge product prefix information for the array `nums`.

2. In each segment tree node, store a frequency count of prefix product remainders for every `x` in the range [0, k - 1].

3. For each query, update `nums[index]` to `value`, then merge the segments corresponding to `nums[start..n - 1]` to compute the `x-value` for `xi`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks us to efficiently update an array and find the number of prefixes of a given subarray `nums[start..n-1]` whose product modulo `k` equals a target `x`. Since `k` is very small (between 1 and 5), we can use a segment tree where each node stores the total product of its range modulo `k` and an array of size `k` representing the counts of prefixes within that range that result in each possible remainder [0, k-1]. This allows us to merge two adjacent segments: the prefix counts of the combined segment consist of all prefix counts from the left child plus the prefix counts from the right child multiplied by the total product of the left child (modulo `k`).

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
    int size;
    vector<int> treeProd;
    vector<int> treeCounts;
    int K;

public:
    vector<int> resultArray(vector<int>& nums, int k, vector<vector<int>>& queries) {
        K = k;
        int n = nums.size();
        size = 1;
        while (size < n) size <<= 1;
        treeProd.assign(2 * size, 1);
        treeCounts.assign(2 * size * 5, 0);

        for (int i = 0; i < n; ++i) {
            int node = i + size;
            int v = nums[i] % K;
            treeProd[node] = v;
            treeCounts[node * 5 + v] = 1;
        }

        for (int i = size - 1; i >= 1; --i) {
            int left = i << 1;
            int right = left | 1;
            int lp = treeProd[left];
            treeProd[i] = (lp * treeProd[right]) % K;
            int idx_i = i * 5, idx_l = left * 5, idx_r = right * 5;
            for (int j = 0; j < K; ++j) treeCounts[idx_i + j] = treeCounts[idx_l + j];
            for (int j = 0; j < K; ++j) treeCounts[idx_i + (lp * j) % K] += treeCounts[idx_r + j];
        }

        vector<int> results;
        results.reserve(queries.size());
        for (const auto& q : queries) {
            update(q[0], q[1]);
            results.push_back(query(q[2], n - 1, q[3]));
        }
        return results;
    }

    void update(int i, int val) {
        int node = i + size;
        int v = val % K;
        treeProd[node] = v;
        for (int j = 0; j < 5; ++j) treeCounts[node * 5 + j] = 0;
        treeCounts[node * 5 + v] = 1;

        while (node > 1) {
            node >>= 1;
            int left = node << 1;
            int right = left | 1;
            int lp = treeProd[left];
            treeProd[node] = (lp * treeProd[right]) % K;
            int idx_n = node * 5, idx_l = left * 5, idx_r = right * 5;
            for (int j = 0; j < K; ++j) treeCounts[idx_n + j] = treeCounts[idx_l + j];
            for (int j = 0; j < K; ++j) treeCounts[idx_n + (lp * j) % K] += treeCounts[idx_r + j];
        }
    }

    int query(int l, int r, int xi) {
        l += size;
        r += size;
        int leftNodes[64], rightNodes[64];
        int lIdx = 0, rIdx = 0;
        while (l <= r) {
            if (l % 2 == 1) leftNodes[lIdx++] = l++;
            if (r % 2 == 0) rightNodes[rIdx++] = r--;
            l >>= 1;
            r >>= 1;
        }

        int resP = 1;
        int resC[5] = {0, 0, 0, 0, 0};
        auto mergeNode = [&](int node) {
            int nextC[5];
            for (int j = 0; j < K; ++j) nextC[j] = resC[j];
            int idx = node * 5;
            for (int j = 0; j < K; ++j) {
                nextC[(resP * j) % K] += treeCounts[idx + j];
            }
            for (int j = 0; j < K; ++j) resC[j] = nextC[j];
            resP = (resP * treeProd[node]) % K;
        };

        for (int i = 0; i < lIdx; ++i) mergeNode(leftNodes[i]);
        for (int i = rIdx - 1; i >= 0; --i) mergeNode(rightNodes[i]);

        return resC[xi];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    int size;
    int[] treeProd;
    int[] treeCounts;
    int K;

    public int[] resultArray(int[] nums, int k, int[][] queries) {
        this.K = k;
        int n = nums.length;
        size = 1;
        while (size < n) size *= 2;
        treeProd = new int[2 * size];
        java.util.Arrays.fill(treeProd, 1);
        treeCounts = new int[2 * size * 5];

        for (int i = 0; i < n; i++) {
            int node = i + size;
            int v = nums[i] % K;
            treeProd[node] = v;
            treeCounts[node * 5 + v] = 1;
        }

        for (int i = size - 1; i >= 1; i--) {
            int left = 2 * i;
            int right = 2 * i + 1;
            int lp = treeProd[left];
            treeProd[i] = (lp * treeProd[right]) % K;
            for (int j = 0; j < K; j++) {
                treeCounts[i * 5 + j] = treeCounts[left * 5 + j];
            }
            for (int j = 0; j < K; j++) {
                treeCounts[i * 5 + (lp * j) % K] += treeCounts[right * 5 + j];
            }
        }

        int[] results = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            update(queries[i][0], queries[i][1]);
            results[i] = query(queries[i][2], n - 1, queries[i][3]);
        }
        return results;
    }

    private void update(int i, int val) {
        int node = i + size;
        int v = val % K;
        treeProd[node] = v;
        for (int j = 0; j < 5; j++) treeCounts[node * 5 + j] = 0;
        treeCounts[node * 5 + v] = 1;

        while (node > 1) {
            node /= 2;
            int left = 2 * node;
            int right = 2 * node + 1;
            int lp = treeProd[left];
            treeProd[node] = (lp * treeProd[right]) % K;
            for (int j = 0; j < K; j++) {
                treeCounts[node * 5 + j] = treeCounts[left * 5 + j];
            }
            for (int j = 0; j < K; j++) {
                treeCounts[node * 5 + (lp * j) % K] += treeCounts[right * 5 + j];
            }
        }
    }

    private int query(int l, int r, int xi) {
        l += size;
        r += size;
        int[] leftNodes = new int[64];
        int[] rightNodes = new int[64];
        int lIdx = 0, rIdx = 0;
        while (l <= r) {
            if (l % 2 == 1) leftNodes[lIdx++] = l++;
            if (r % 2 == 0) rightNodes[rIdx++] = r--;
            l /= 2;
            r /= 2;
        }

        int resP = 1;
        int[] resC = new int[5];
        for (int i = 0; i < lIdx; i++) {
            int node = leftNodes[i];
            int[] nextC = resC.clone();
            for (int j = 0; j < K; j++) {
                nextC[(resP * j) % K] += treeCounts[node * 5 + j];
            }
            resC = nextC;
            resP = (resP * treeProd[node]) % K;
        }
        for (int i = rIdx - 1; i >= 0; i--) {
            int node = rightNodes[i];
            int[] nextC = resC.clone();
            for (int j = 0; j < K; j++) {
                nextC[(resP * j) % K] += treeCounts[node * 5 + j];
            }
            resC = nextC;
            resP = (resP * treeProd[node]) % K;
        }
        return resC[xi];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1

        tree_prod = [1] * (2 * size)
        tree_counts = [0] * (2 * size * 5)

        def update(i, val):
            node = i + size
            v = val % k
            tree_prod[node] = v
            idx = node * 5
            for j in range(5):
                tree_counts[idx + j] = 0
            tree_counts[idx + v] = 1
            while node > 1:
                node >>= 1
                left = node << 1
                right = left | 1
                lp = tree_prod[left]
                tree_prod[node] = (lp * tree_prod[right]) % k
                idx_n, idx_l, idx_r = node * 5, left * 5, right * 5
                for j in range(k):
                    tree_counts[idx_n + j] = tree_counts[idx_l + j]
                for j in range(k):
                    tree_counts[idx_n + (lp * j) % k] += tree_counts[idx_r + j]

        for i, val in enumerate(nums):
            node = i + size
            v = val % k
            tree_prod[node] = v
            tree_counts[node * 5 + v] = 1

        for i in range(size - 1, 0, -1):
            left = i << 1
            right = left | 1
            lp = tree_prod[left]
            tree_prod[i] = (lp * tree_prod[right]) % k
            idx_i, idx_l, idx_r = i * 5, left * 5, right * 5
            for j in range(k):
                tree_counts[idx_i + j] = tree_counts[idx_l + j]
            for j in range(k):
                tree_counts[idx_i + (lp * j) % k] += tree_counts[idx_r + j]

        results = []
        for idx, val, start, xi in queries:
            update(idx, val)

            l, r = start + size, (n - 1) + size
            left_nodes, right_nodes = [], []
            while l <= r:
                if l % 2 == 1:
                    left_nodes.append(l)
                    l += 1
                if r % 2 == 0:
                    right_nodes.append(r)
                    r -= 1
                l >>= 1
                r >>= 1

            res_p = 1
            res_c = [0] * 5
            for node in left_nodes + right_nodes[::-1]:
                new_c = list(res_c)
                idx = node * 5
                for j in range(k):
                    new_c[(res_p * j) % k] += tree_counts[idx + j]
                res_c = new_c
                res_p = (res_p * tree_prod[node]) % k
            results.append(res_c[xi])

        return results
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import math

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []

        N = 1
        while N < n:
            N *= 2

        tree_prod = [1] * (2 * N)
        tree_cnt = [0] * (2 * N * k)

        for i in range(n):
            v = nums[i] % k
            tree_prod[N + i] = v
            tree_cnt[(N + i) * k + v] = 1

        for i in range(N - 1, 0, -1):
            lp = tree_prod[2 * i]
            rp = tree_prod[2 * i + 1]
            tree_prod[i] = (lp * rp) % k
            idx_k = i * k
            lc_k = 2 * i * k
            rc_k = (2 * i + 1) * k
            for j in range(k):
                tree_cnt[idx_k + j] = tree_cnt[lc_k + j]
            for j in range(k):
                tree_cnt[idx_k + (lp * j) % k] += tree_cnt[rc_k + j]

        res = []
        for idx, val, start, x in queries:
            curr = idx + N
            v = val % k
            tree_prod[curr] = v
            for j in range(k):
                tree_cnt[curr * k + j] = 0
            tree_cnt[curr * k + v] = 1
            curr //= 2
            while curr >= 1:
                lp = tree_prod[2 * curr]
                rp = tree_prod[2 * curr + 1]
                tree_prod[curr] = (lp * rp) % k
                idx_k = curr * k
                lc_k = 2 * curr * k
                rc_k = (2 * curr + 1) * k
                for j in range(k):
                    tree_cnt[idx_k + j] = tree_cnt[lc_k + j]
                for j in range(k):
                    tree_cnt[idx_k + (lp * j) % k] += tree_cnt[rc_k + j]
                curr //= 2

            l, r = start + N, n - 1 + N
            l_res, r_res = [], []
            while l <= r:
                if l % 2 == 1:
                    l_res.append(l)
                    l += 1
                if r % 2 == 0:
                    r_res.append(r)
                    r -= 1
                l //= 2
                r //= 2

            all_nodes = l_res + r_res[::-1]
            first_node = all_nodes[0]
            curr_prod = tree_prod[first_node]
            curr_cnt = tree_cnt[first_node * k : (first_node + 1) * k]

            for i in range(1, len(all_nodes)):
                node_idx = all_nodes[i]
                lp = curr_prod
                rc_start = node_idx * k
                new_cnt = list(curr_cnt)
                for j in range(k):
                    new_cnt[(lp * j) % k] += tree_cnt[rc_start + j]
                curr_cnt = new_cnt
                curr_prod = (lp * tree_prod[node_idx]) % k

            res.append(curr_cnt[x])

        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

typedef struct {
    int prod;
    int cnt[5];
} Node;

Node* tree;
int treeSize;

void merge(Node* res, const Node* left, const Node* right, int k) {
    res->prod = (left->prod * right->prod) % k;
    for (int i = 0; i < k; i++) {
        res->cnt[i] = left->cnt[i];
    }
    for (int i = 0; i < k; i++) {
        res->cnt[(left->prod * i) % k] += right->cnt[i];
    }
}

void build(int v, int tl, int tr, int* nums, int k) {
    if (tl == tr) {
        int val = nums[tl] % k;
        tree[v].prod = val;
        for (int i = 0; i < k; i++) tree[v].cnt[i] = 0;
        tree[v].cnt[val] = 1;
    } else {
        int tm = (tl + tr) / 2;
        build(2 * v, tl, tm, nums, k);
        build(2 * v + 1, tm + 1, tr, nums, k);
        merge(&tree[v], &tree[2 * v], &tree[2 * v + 1], k);
    }
}

void update(int v, int tl, int tr, int pos, int newVal, int k) {
    if (tl == tr) {
        int val = newVal % k;
        tree[v].prod = val;
        for (int i = 0; i < k; i++) tree[v].cnt[i] = 0;
        tree[v].cnt[val] = 1;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(2 * v, tl, tm, pos, newVal, k);
        else
            update(2 * v + 1, tm + 1, tr, pos, newVal, k);
        merge(&tree[v], &tree[2 * v], &tree[2 * v + 1], k);
    }
}

Node query(int v, int tl, int tr, int l, int r, int k) {
    if (l == tl && r == tr) return tree[v];
    int tm = (tl + tr) / 2;
    if (r <= tm) return query(2 * v, tl, tm, l, r, k);
    if (l > tm) return query(2 * v + 1, tm + 1, tr, l, r, k);
    Node leftResult = query(2 * v, tl, tm, l, tm, k);
    Node rightResult = query(2 * v + 1, tm + 1, tr, tm + 1, r, k);
    Node res;
    merge(&res, &leftResult, &rightResult, k);
    return res;
}

int* resultArray(int* nums, int numsSize, int k, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    tree = (Node*)malloc(4 * numsSize * sizeof(Node));
    build(1, 0, numsSize - 1, nums, k);

    int* result = (int*)malloc(queriesSize * sizeof(int));
    *returnSize = queriesSize;

    for (int i = 0; i < queriesSize; i++) {
        int idx = queries[i][0];
        int val = queries[i][1];
        int start = queries[i][2];
        int x = queries[i][3];

        update(1, 0, numsSize - 1, idx, val, k);
        Node qNode = query(1, 0, numsSize - 1, start, numsSize - 1, k);
        result[i] = qNode.cnt[x];
    }

    free(tree);
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
    private struct Node {
        public int Prod;
        public int[] Cnt;

        public Node(int k) {
            Prod = 1;
            Cnt = new int[k];
        }
    }

    private Node[] tree;

    private void Merge(ref Node res, Node left, Node right, int k) {
        res.Prod = (left.Prod * right.Prod) % k;
        for (int i = 0; i < k; i++) {
            res.Cnt[i] = left.Cnt[i];
        }
        for (int i = 0; i < k; i++) {
            res.Cnt[(left.Prod * i) % k] += right.Cnt[i];
        }
    }

    private void Build(int v, int tl, int tr, int[] nums, int k) {
        tree[v] = new Node(k);
        if (tl == tr) {
            int val = nums[tl] % k;
            tree[v].Prod = val;
            tree[v].Cnt[val] = 1;
        } else {
            int tm = (tl + tr) / 2;
            Build(2 * v, tl, tm, nums, k);
            Build(2 * v + 1, tm + 1, tr, nums, k);
            Merge(ref tree[v], tree[2 * v], tree[2 * v + 1], k);
        }
    }

    private void Update(int v, int tl, int tr, int pos, int newVal, int k) {
        if (tl == tr) {
            int val = newVal % k;
            tree[v].Prod = val;
            Array.Clear(tree[v].Cnt, 0, k);
            tree[v].Cnt[val] = 1;
        } else {
            int tm = (tl + tr) / 2;
            if (pos <= tm)
                Update(2 * v, tl, tm, pos, newVal, k);
            else
                Update(2 * v + 1, tm + 1, tr, pos, newVal, k);
            Merge(ref tree[v], tree[2 * v], tree[2 * v + 1], k);
        }
    }

    private Node Query(int v, int tl, int tr, int l, int r, int k) {
        if (l == tl && r == tr) return tree[v];
        int tm = (tl + tr) / 2;
        if (r <= tm) return Query(2 * v, tl, tm, l, r, k);
        if (l > tm) return Query(2 * v + 1, tm + 1, tr, l, r, k);
        Node leftRes = Query(2 * v, tl, tm, l, tm, k);
        Node rightRes = Query(2 * v + 1, tm + 1, tr, tm + 1, r, k);
        Node res = new Node(k);
        Merge(ref res, leftRes, rightRes, k);
        return res;
    }

    public int[] ResultArray(int[] nums, int k, int[][] queries) {
        int n = nums.Length;
        tree = new Node[4 * n];
        Build(1, 0, n - 1, nums, k);

        int[] result = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int idx = queries[i][0];
            int val = queries[i][1];
            int start = queries[i][2];
            int x = queries[i][3];

            Update(1, 0, n - 1, idx, val, k);
            Node qNode = Query(1, 0, n - 1, start, n - 1, k);
            result[i] = qNode.Cnt[x];
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
 * @param {number[]} nums
 * @param {number} k
 * @param {number[][]} queries
 * @return {number[]}
 */
var resultArray = function(nums, k, queries) {
    const n = nums.length;
    let N = 1;
    while (N < n) N *= 2;

    const treeProd = new Int32Array(2 * N);
    const treeCnt = new Int32Array(2 * N * k);
    treeProd.fill(1);

    for (let i = 0; i < n; i++) {
        const val = nums[i] % k;
        treeProd[N + i] = val;
        treeCnt[(N + i) * k + val] = 1;
    }

    for (let i = N - 1; i > 0; i--) {
        const lc = 2 * i, rc = 2 * i + 1;
        const lp = treeProd[lc], rp = treeProd[rc];
        treeProd[i] = (lp * rp) % k;
        const idxK = i * k, lcK = lc * k, rcK = rc * k;
        for (let j = 0; j < k; j++) treeCnt[idxK + j] = treeCnt[lcK + j];
        for (let j = 0; j < k; j++) treeCnt[idxK + (lp * j) % k] += treeCnt[rcK + j];
    }

    const results = [];
    for (const [idx, val, start, x] of queries) {
        let curr = idx + N;
        const v = val % k;
        treeProd[curr] = v;
        for (let j = 0; j < k; j++) treeCnt[curr * k + j] = 0;
        treeCnt[curr * k + v] = 1;
        curr = Math.floor(curr / 2);
        while (curr >= 1) {
            const lc = 2 * curr, rc = 2 * curr + 1;
            const lp = treeProd[lc], rp = treeProd[rc];
            treeProd[curr] = (lp * rp) % k;
            const idxK = curr * k, lcK = lc * k, rcK = rc * k;
            for (let j = 0; j < k; j++) treeCnt[idxK + j] = treeCnt[lcK + j];
            for (let j = 0; j < k; j++) treeCnt[idxK + (lp * j) % k] += treeCnt[rcK + j];
            curr = Math.floor(curr / 2);
        }

        let l = start + N, r = n - 1 + N;
        const lNodes = [], rNodes = [];
        while (l <= r) {
            if (l % 2 === 1) lNodes.push(l++);
            if (r % 2 === 0) rNodes.push(r--);
            l = Math.floor(l / 2);
            r = Math.floor(r / 2);
        }

        const allNodes = lNodes.concat(rNodes.reverse());
        const firstNode = allNodes[0];
        let currProd = treeProd[firstNode];
        let currCnt = new Int32Array(k);
        for (let j = 0; j < k; j++) currCnt[j] = treeCnt[firstNode * k + j];

        for (let i = 1; i < allNodes.length; i++) {
            const nodeIdx = allNodes[i];
            const lp = currProd, rcStart = nodeIdx * k;
            const nextCnt = new Int32Array(currCnt);
            for (let j = 0; j < k; j++) nextCnt[(lp * j) % k] += treeCnt[rcStart + j];
            currCnt = nextCnt;
            currProd = (lp * treeProd[nodeIdx]) % k;
        }
        results.push(currCnt[x]);
    }
    return results;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function resultArray(nums: number[], k: number, queries: number[][]): number[] {
    const n = nums.length;
    const treeCounts = new Int32Array((4 * n + 1) * k);
    const treeProducts = new Int32Array(4 * n + 1);

    function merge(v: number, left: number, right: number): void {
        const pL = treeProducts[left];
        const vOffset = v * k;
        const lOffset = left * k;
        const rOffset = right * k;
        for (let i = 0; i < k; i++) {
            treeCounts[vOffset + i] = treeCounts[lOffset + i];
        }
        for (let vp = 0; vp < k; vp++) {
            const target = (pL * vp) % k;
            treeCounts[vOffset + target] += treeCounts[rOffset + vp];
        }
        treeProducts[v] = (pL * treeProducts[right]) % k;
    }

    function build(v: number, tl: number, tr: number): void {
        if (tl === tr) {
            const rem = nums[tl] % k;
            const vOffset = v * k;
            for (let i = 0; i < k; i++) treeCounts[vOffset + i] = 0;
            treeCounts[vOffset + rem] = 1;
            treeProducts[v] = rem;
        } else {
            const tm = (tl + tr) >> 1;
            build(2 * v, tl, tm);
            build(2 * v + 1, tm + 1, tr);
            merge(v, 2 * v, 2 * v + 1);
        }
    }

    function update(v: number, tl: number, tr: number, pos: number, newVal: number): void {
        if (tl === tr) {
            const vOffset = v * k;
            for (let i = 0; i < k; i++) treeCounts[vOffset + i] = 0;
            treeCounts[vOffset + newVal] = 1;
            treeProducts[v] = newVal;
        } else {
            const tm = (tl + tr) >> 1;
            if (pos <= tm) update(2 * v, tl, tm, pos, newVal);
            else update(2 * v + 1, tm + 1, tr, pos, newVal);
            merge(v, 2 * v, 2 * v + 1);
        }
    }

    interface Node {
        counts: Int32Array;
        product: number;
    }

    function query(v: number, tl: number, tr: number, l: number, r: number): Node {
        if (l === tl && r === tr) {
            const counts = new Int32Array(k);
            const offset = v * k;
            for (let i = 0; i < k; i++) counts[i] = treeCounts[offset + i];
            return { counts, product: treeProducts[v] };
        }
        const tm = (tl + tr) >> 1;
        if (r <= tm) return query(2 * v, tl, tm, l, r);
        if (l > tm) return query(2 * v + 1, tm + 1, tr, l, r);

        const leftRes = query(2 * v, tl, tm, l, tm);
        const rightRes = query(2 * v + 1, tm + 1, tr, tm + 1, r);

        const mergedCounts = new Int32Array(leftRes.counts);
        const pL = leftRes.product;
        for (let vp = 0; vp < k; vp++) {
            const target = (pL * vp) % k;
            mergedCounts[target] += rightRes.counts[vp];
        }
        return {
            counts: mergedCounts,
            product: (pL * rightRes.product) % k
        };
    }

    build(1, 0, n - 1);
    const result: number[] = [];
    for (let i = 0; i < queries.length; i++) {
        const q = queries[i];
        update(1, 0, n - 1, q[0], q[1] % k);
        const res = query(1, 0, n - 1, q[2], n - 1);
        result.push(res.counts[q[3]]);
    }
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function resultArray($nums, $k, $queries) {
        $this->k = $k;
        $this->n = count($nums);
        $this->treeCounts = new SplFixedArray((4 * $this->n + 1) * $this->k);
        $this->treeProducts = new SplFixedArray(4 * $this->n + 1);

        $this->build($nums, 1, 0, $this->n - 1);

        $results = [];
        foreach ($queries as $q) {
            $this->update(1, 0, $this->n - 1, $q[0], $q[1] % $k);
            $res = $this->query(1, 0, $this->n - 1, $q[2], $this->n - 1);
            $results[] = $res['counts'][$q[3]];
        }
        return $results;
    }

    private $k;
    private $n;
    private $treeCounts;
    private $treeProducts;

    private function merge($v, $left, $right) {
        $vOffset = $v * $this->k;
        $lOffset = $left * $this->k;
        $rOffset = $right * $this->k;
        $pL = $this->treeProducts[$left];
        for ($i = 0; $i < $this->k; $i++) {
            $this->treeCounts[$vOffset + $i] = $this->treeCounts[$lOffset + $i];
        }
        for ($vp = 0; $vp < $this->k; $vp++) {
            $target = ($pL * $vp) % $this->k;
            $this->treeCounts[$vOffset + $target] += $this->treeCounts[$rOffset + $vp];
        }
        $this->treeProducts[$v] = ($pL * $this->treeProducts[$right]) % $this->k;
    }

    private function build(&$nums, $v, $tl, $tr) {
        if ($tl == $tr) {
            $rem = $nums[$tl] % $this->k;
            $vOffset = $v * $this->k;
            for ($i = 0; $i < $this->k; $i++) $this->treeCounts[$vOffset + $i] = 0;
            $this->treeCounts[$vOffset + $rem] = 1;
            $this->treeProducts[$v] = $rem;
        } else {
            $tm = ($tl + $tr) >> 1;
            $this->build($nums, 2 * $v, $tl, $tm);
            $this->build($nums, 2 * $v + 1, $tm + 1, $tr);
            $this->merge($v, 2 * $v, 2 * $v + 1);
        }
    }

    private function update($v, $tl, $tr, $pos, $newVal) {
        if ($tl == $tr) {
            $vOffset = $v * $this->k;
            for ($i = 0; $i < $this->k; $i++) $this->treeCounts[$vOffset + $i] = 0;
            $this->treeCounts[$vOffset + $newVal] = 1;
            $this->treeProducts[$v] = $newVal;
        } else {
            $tm = ($tl + $tr) >> 1;
            if ($pos <= $tm) $this->update(2 * $v, $tl, $tm, $pos, $newVal);
            else $this->update(2 * $v + 1, $tm + 1, $tr, $pos, $newVal);
            $this->merge($v, 2 * $v, 2 * $v + 1);
        }
    }

    private function query($v, $tl, $tr, $l, $r) {
        if ($l == $tl && $r == $tr) {
            $counts = array_fill(0, $this->k, 0);
            $offset = $v * $this->k;
            for ($i = 0; $i < $this->k; $i++) {
                $counts[$i] = $this->treeCounts[$offset + $i];
            }
            return ['counts' => $counts, 'product' => $this->treeProducts[$v]];
        }
        $tm = ($tl + $tr) >> 1;
        if ($r <= $tm) return $this->query(2 * $v, $tl, $tm, $l, $r);
        if ($l > $tm) return $this->query(2 * $v + 1, $tm + 1, $tr, $l, $r);

        $leftRes = $this->query(2 * $v, $tl, $tm, $l, $tm);
        $rightRes = $this->query(2 * $v + 1, $tm + 1, $tr, $tm + 1, $r);

        $mergedCounts = $leftRes['counts'];
        $pL = $leftRes['product'];
        for ($vp = 0; $vp < $this->k; $vp++) {
            $target = ($pL * $vp) % $this->k;
            $mergedCounts[$target] += $rightRes['counts'][$vp];
        }
        return [
            'counts' => $mergedCounts,
            'product' => ($pL * $rightRes['product']) % $this->k
        ];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    private var treeCounts: [Int] = []
    private var treeProducts: [Int] = []
    private var k: Int = 0
    private var n: Int = 0

    struct Node {
        var counts: [Int]
        var product: Int
    }

    func resultArray(_ nums: [Int], _ k: Int, _ queries: [[Int]]) -> [Int] {
        self.k = k
        self.n = nums.count
        self.treeCounts = [Int](repeating: 0, count: (4 * n + 1) * k)
        self.treeProducts = [Int](repeating: 0, count: 4 * n + 1)

        build(nums, 1, 0, n - 1)

        var results = [Int]()
        for q in queries {
            update(1, 0, n - 1, q[0], q[1] % k)
            let res = query(1, 0, n - 1, q[2], n - 1)
            results.append(res.counts[q[3]])
        }
        return results
    }

    private func merge(_ v: Int, _ left: Int, _ right: Int) {
        let pL = treeProducts[left]
        let vOffset = v * k
        let lOffset = left * k
        let rOffset = right * k
        for i in 0..<k {
            treeCounts[vOffset + i] = treeCounts[lOffset + i]
        }
        for vp in 0..<k {
            let target = (pL * vp) % k
            treeCounts[vOffset + target] += treeCounts[rOffset + vp]
        }
        treeProducts[v] = (pL * treeProducts[right]) % k
    }

    private func build(_ nums: [Int], _ v: Int, _ tl: Int, _ tr: Int) {
        if tl == tr {
            let rem = nums[tl] % k
            let offset = v * k
            for i in 0..<k { treeCounts[offset + i] = 0 }
            treeCounts[offset + rem] = 1
            treeProducts[v] = rem
        } else {
            let tm = (tl + tr) / 2
            build(nums, 2 * v, tl, tm)
            build(nums, 2 * v + 1, tm + 1, tr)
            merge(v, 2 * v, 2 * v + 1)
        }
    }

    private func update(_ v: Int, _ tl: Int, _ tr: Int, _ pos: Int, _ newVal: Int) {
        if tl == tr {
            let offset = v * k
            for i in 0..<k { treeCounts[offset + i] = 0 }
            treeCounts[offset + newVal] = 1
            treeProducts[v] = newVal
        } else {
            let tm = (tl + tr) / 2
            if pos <= tm { update(2 * v, tl, tm, pos, newVal) }
            else { update(2 * v + 1, tm + 1, tr, pos, newVal) }
            merge(v, 2 * v, 2 * v + 1)
        }
    }

    private func query(_ v: Int, _ tl: Int, _ tr: Int, _ l: Int, _ r: Int) -> Node {
        if l == tl && r == tr {
            var counts = [Int](repeating: 0, count: k)
            let offset = v * k
            for i in 0..<k { counts[i] = treeCounts[offset + i] }
            return Node(counts: counts, product: treeProducts[v])
        }
        let tm = (tl + tr) / 2
        if r <= tm { return query(2 * v, tl, tm, l, r) }
        if l > tm { return query(2 * v + 1, tm + 1, tr, l, r) }

        let leftRes = query(2 * v, tl, tm, l, tm)
        let rightRes = query(2 * v + 1, tm + 1, tr, tm + 1, r)

        var mergedCounts = leftRes.counts
        let pL = leftRes.product
        for vp in 0..<k {
            let target = (pL * vp) % k
            mergedCounts[target] += rightRes.counts[vp]
        }
        return Node(counts: mergedCounts, product: (pL * rightRes.product) % k)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    private var treeCounts = IntArray(0)
    private var treeProducts = IntArray(0)
    private var k: Int = 0
    private var n: Int = 0

    private class Node(val counts: IntArray, val product: Int)

    fun resultArray(nums: IntArray, k: Int, queries: Array<IntArray>): IntArray {
        this.k = k
        this.n = nums.size
        this.treeCounts = IntArray((4 * n + 1) * k)
        this.treeProducts = IntArray(4 * n + 1)

        build(nums, 1, 0, n - 1)

        val results = IntArray(queries.size)
        for (i in queries.indices) {
            val q = queries[i]
            update(1, 0, n - 1, q[0], q[1] % k)
            val resNode = query(1, 0, n - 1, q[2], n - 1)
            results[i] = resNode.counts[q[3]]
        }
        return results
    }

    private fun merge(v: Int, left: Int, right: Int) {
        val pL = treeProducts[left]
        val vOffset = v * k
        val lOffset = left * k
        val rOffset = right * k
        for (i in 0 until k) {
            treeCounts[vOffset + i] = treeCounts[lOffset + i]
        }
        for (vp in 0 until k) {
            val target = (pL * vp) % k
            treeCounts[vOffset + target] += treeCounts[rOffset + vp]
        }
        treeProducts[v] = (pL * treeProducts[right]) % k
    }

    private fun build(nums: IntArray, v: Int, tl: Int, tr: Int) {
        if (tl == tr) {
            val rem = nums[tl] % k
            val offset = v * k
            for (i in 0 until k) treeCounts[offset + i] = 0
            treeCounts[offset + rem] = 1
            treeProducts[v] = rem
        } else {
            val tm = (tl + tr) / 2
            build(nums, 2 * v, tl, tm)
            build(nums, 2 * v + 1, tm + 1, tr)
            merge(v, 2 * v, 2 * v + 1)
        }
    }

    private fun update(v: Int, tl: Int, tr: Int, pos: Int, newVal: Int) {
        if (tl == tr) {
            val offset = v * k
            for (i in 0 until k) treeCounts[offset + i] = 0
            treeCounts[offset + newVal] = 1
            treeProducts[v] = newVal
        } else {
            val tm = (tl + tr) / 2
            if (pos <= tm) update(2 * v, tl, tm, pos, newVal)
            else update(2 * v + 1, tm + 1, tr, pos, newVal)
            merge(v, 2 * v, 2 * v + 1)
        }
    }

    private fun query(v: Int, tl: Int, tr: Int, l: Int, r: Int): Node {
        if (l == tl && r == tr) {
            val counts = IntArray(k)
            val offset = v * k
            for (i in 0 until k) counts[i] = treeCounts[offset + i]
            return Node(counts, treeProducts[v])
        }
        val tm = (tl + tr) / 2
        if (r <= tm) return query(2 * v, tl, tm, l, r)
        if (l > tm) return query(2 * v + 1, tm + 1, tr, l, r)

        val leftRes = query(2 * v, tl, tm, l, tm)
        val rightRes = query(2 * v + 1, tm + 1, tr, tm + 1, r)

        val mergedCounts = leftRes.counts.copyOf()
        val pL = leftRes.product
        for (vp in 0 until k) {
            val target = (pL * vp) % k
            mergedCounts[target] += rightRes.counts[vp]
        }
        return Node(mergedCounts, (pL * rightRes.product) % k)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:typed_data';

class Node {
  int totalProd;
  final List<int> counts;
  Node(this.totalProd, this.counts);
}

class Solution {
  late Int32List treeTotal;
  late Int32List treeCounts;

  void mergeToNode(int v, int leftV, int rightV, int k) {
    treeTotal[v] = (treeTotal[leftV] * treeTotal[rightV]) % k;
    int v5 = v * 5;
    int l5 = leftV * 5;
    int r5 = rightV * 5;
    int lt = treeTotal[leftV];

    for (int i = 0; i < k; i++) {
      treeCounts[v5 + i] = treeCounts[l5 + i];
    }
    for (int i = 0; i < k; i++) {
      int idx = (lt * i) % k;
      treeCounts[v5 + idx] += treeCounts[r5 + i];
    }
  }

  void build(int v, int tl, int tr, List<int> nums, int k) {
    if (tl == tr) {
      int val = nums[tl] % k;
      treeTotal[v] = val;
      int v5 = v * 5;
      for (int i = 0; i < 5; i++) treeCounts[v5 + i] = 0;
      treeCounts[v5 + val] = 1;
    } else {
      int tm = (tl + tr) ~/ 2;
      build(2 * v, tl, tm, nums, k);
      build(2 * v + 1, tm + 1, tr, nums, k);
      mergeToNode(v, 2 * v, 2 * v + 1, k);
    }
  }

  void update(int v, int tl, int tr, int pos, int newVal, int k) {
    if (tl == tr) {
      int val = newVal % k;
      treeTotal[v] = val;
      int v5 = v * 5;
      for (int i = 0; i < 5; i++) treeCounts[v5 + i] = 0;
      treeCounts[v5 + val] = 1;
    } else {
      int tm = (tl + tr) ~/ 2;
      if (pos <= tm) {
        update(2 * v, tl, tm, pos, newVal, k);
      } else {
        update(2 * v + 1, tm + 1, tr, pos, newVal, k);
      }
      mergeToNode(v, 2 * v, 2 * v + 1, k);
    }
  }

  Node query(int v, int tl, int tr, int l, int r, int k) {
    if (l == tl && r == tr) {
      int v5 = v * 5;
      List<int> resCounts = List<int>.filled(5, 0);
      for (int i = 0; i < 5; i++) resCounts[i] = treeCounts[v5 + i];
      return Node(treeTotal[v], resCounts);
    }
    int tm = (tl + tr) ~/ 2;
    if (r <= tm) {
      return query(2 * v, tl, tm, l, r, k);
    } else if (l > tm) {
      return query(2 * v + 1, tm + 1, tr, l, r, k);
    } else {
      Node leftRes = query(2 * v, tl, tm, l, tm, k);
      Node rightRes = query(2 * v + 1, tm + 1, tr, tm + 1, r, k);
      int resTotal = (leftRes.totalProd * rightRes.totalProd) % k;
      List<int> resCounts = List<int>.filled(5, 0);
      for (int i = 0; i < k; i++) {
        resCounts[i] = leftRes.counts[i];
      }
      for (int i = 0; i < k; i++) {
        int idx = (leftRes.totalProd * i) % k;
        resCounts[idx] += rightRes.counts[i];
      }
      return Node(resTotal, resCounts);
    }
  }

  List<int> resultArray(List<int> nums, int k, List<List<int>> queries) {
    int n = nums.length;
    treeTotal = Int32List(4 * n + 1);
    treeCounts = Int32List((4 * n + 1) * 5);

    build(1, 0, n - 1, nums, k);

    List<int> result = [];
    for (var q in queries) {
      int idx = q[0];
      int val = q[1];
      int start = q[2];
      int x = q[3];

      update(1, 0, n - 1, idx, val, k);
      Node res = query(1, 0, n - 1, start, n - 1, k);
      result.add(res.counts[x]);
    }

    return result;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

type Node struct {
	totalProd int
	counts    [5]int
}

type SegmentTree struct {
	treeTotal  []int
	treeCounts []int
	k          int
	n          int
}

func (st *SegmentTree) mergeToNode(v, leftV, rightV int) {
	st.treeTotal[v] = (st.treeTotal[leftV] * st.treeTotal[rightV]) % st.k
	v5, l5, r5 := v*5, leftV*5, rightV*5
	lt := st.treeTotal[leftV]

	for i := 0; i < st.k; i++ {
		st.treeCounts[v5+i] = st.treeCounts[l5+i]
	}
	for i := 0; i < st.k; i++ {
		idx := (lt * i) % st.k
		st.treeCounts[v5+idx] += st.treeCounts[r5+i]
	}
}

func (st *SegmentTree) build(v, tl, tr int, nums []int) {
	if tl == tr {
		val := nums[tl] % st.k
		st.treeTotal[v] = val
		v5 := v * 5
		for i := 0; i < 5; i++ {
			st.treeCounts[v5+i] = 0
		}
		st.treeCounts[v5+val] = 1
	} else {
		tm := (tl + tr) / 2
		st.build(2*v, tl, tm, nums)
		st.build(2*v+1, tm+1, tr, nums)
		st.mergeToNode(v, 2*v, 2*v+1)
	}
}

func (st *SegmentTree) update(v, tl, tr, pos, newVal int) {
	if tl == tr {
		val := newVal % st.k
		st.treeTotal[v] = val
		v5 := v * 5
		for i := 0; i < 5; i++ {
			st.treeCounts[v5+i] = 0
		}
		st.treeCounts[v5+val] = 1
	} else {
		tm := (tl + tr) / 2
		if pos <= tm {
			st.update(2*v, tl, tm, pos, newVal)
		} else {
			st.update(2*v+1, tm+1, tr, pos, newVal)
		}
		st.mergeToNode(v, 2*v, 2*v+1)
	}
}

func (st *SegmentTree) query(v, tl, tr, l, r int) Node {
	if l == tl && r == tr {
		offset := v * 5
		var res Node
		res.totalProd = st.treeTotal[v]
		for i := 0; i < 5; i++ {
			res.counts[i] = st.treeCounts[offset+i]
		}
		return res
	}
	tm := (tl + tr) / 2
	if r <= tm {
		return st.query(2*v, tl, tm, l, r)
	} else if l > tm {
		return st.query(2*v+1, tm+1, tr, l, r)
	} else {
		leftRes := st.query(2*v, tl, tm, l, tm)
		rightRes := st.query(2*v+1, tm+1, tr, tm+1, r)
		var res Node
		res.totalProd = (leftRes.totalProd * rightRes.totalProd) % st.k
		for i := 0; i < st.k; i++ {
			res.counts[i] = leftRes.counts[i]
		}
		for i := 0; i < st.k; i++ {
			idx := (leftRes.totalProd * i) % st.k
			res.counts[idx] += rightRes.counts[i]
		}
		return res
	}
}

func resultArray(nums []int, k int, queries [][]int) []int {
	n := len(nums)
	st := &SegmentTree{
		treeTotal:  make([]int, 4*n+1),
		treeCounts: make([]int, (4*n+1)*5),
		k:          k,
		n:          n,
	}

	st.build(1, 0, n-1, nums)

	result := make([]int, len(queries))
	for i, q := range queries {
		idx, val, start, x := q[0], q[1], q[2], q[3]
		st.update(1, 0, n-1, idx, val)
		resNode := st.query(1, 0, n-1, start, n-1)
		result[i] = resNode.counts[x]
	}

	return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def result_array(nums, k, queries)
  n = nums.length
  @tree_total = Array.new(4 * n + 1, 0)
  @tree_counts = Array.new((4 * n + 1) * 5, 0)

  def merge_to_node(v, left_v, right_v, k)
    @tree_total[v] = (@tree_total[left_v] * @tree_total[right_v]) % k
    v5 = v * 5
    l5 = left_v * 5
    r5 = right_v * 5
    lt = @tree_total[left_v]

    i = 0
    while i < k
      @tree_counts[v5 + i] = @tree_counts[l5 + i]
      i += 1
    end
    i = 0
    while i < k
      idx = (lt * i) % k
      @tree_counts[v5 + idx] += @tree_counts[r5 + i]
      i += 1
    end
  end

  def build(v, tl, tr, nums, k)
    if tl == tr
      val = nums[tl] % k
      @tree_total[v] = val
      v5 = v * 5
      @tree_counts[v5 + val] = 1
    else
      tm = (tl + tr) / 2
      build(2 * v, tl, tm, nums, k)
      build(2 * v + 1, tm + 1, tr, nums, k)
      merge_to_node(v, 2 * v, 2 * v + 1, k)
    end
  end

  def update(v, tl, tr, pos, new_val, k)
    if tl == tr
      val = new_val % k
      @tree_total[v] = val
      v5 = v * 5
      i = 0
      while i < 5
        @tree_counts[v5 + i] = 0
        i += 1
      end
      @tree_counts[v5 + val] = 1
    else
      tm = (tl + tr) / 2
      if pos <= tm
        update(2 * v, tl, tm, pos, new_val, k)
      else
        update(2 * v + 1, tm + 1, tr, pos, new_val, k)
      end
      merge_to_node(v, 2 * v, 2 * v + 1, k)
    end
  end

  def query(v, tl, tr, l, r, k)
    if l == tl && r == tr
      v5 = v * 5
      return [@tree_total[v], @tree_counts[v5, 5]]
    end
    tm = (tl + tr) / 2
    if r <= tm
      return query(2 * v, tl, tm, l, r, k)
    elsif l > tm
      return query(2 * v + 1, tm + 1, tr, l, r, k)
    else
      left_total, left_counts = query(2 * v, tl, tm, l, tm, k)
      right_total, right_counts = query(2 * v + 1, tm + 1, tr, tm + 1, r, k)
      res_total = (left_total * right_total) % k
      res_counts = Array.new(5, 0)
      i = 0
      while i < k
        res_counts[i] = left_counts[i]
        i += 1
      end
      i = 0
      while i < k
        idx = (left_total * i) % k
        res_counts[idx] += right_counts[i]
        i += 1
      end
      return [res_total, res_counts]
    end
  end

  build(1, 0, n - 1, nums, k)

  results = []
  queries.each do |index, value, start, x|
    update(1, 0, n - 1, index, value, k)
    res_total, res_counts = query(1, 0, n - 1, start, n - 1, k)
    results << res_counts[x]
  end

  results
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
class Node(val totalProd: Int, val counts: Array[Int])

object Solution {
    def resultArray(nums: Array[Int], k: Int, queries: Array[Array[Int]]): Array[Int] = {
        val n = nums.length
        val treeTotal = new Array[Int](4 * n + 1)
        val treeCounts = new Array[Int]((4 * n + 1) * 5)

        def mergeToNode(v: Int, leftV: Int, rightV: Int): Unit = {
            treeTotal(v) = (treeTotal(leftV) * treeTotal(rightV)) % k
            val v5 = v * 5
            val l5 = leftV * 5
            val r5 = rightV * 5
            val lt = treeTotal(leftV)

            var i = 0
            while (i < k) {
                treeCounts(v5 + i) = treeCounts(l5 + i)
                i += 1
            }
            i = 0
            while (i < k) {
                val idx = (lt * i) % k
                treeCounts(v5 + idx) += treeCounts(r5 + i)
                i += 1
            }
        }

        def build(v: Int, tl: Int, tr: Int): Unit = {
            if (tl == tr) {
                val valMod = nums(tl) % k
                treeTotal(v) = valMod
                val v5 = v * 5
                var i = 0
                while (i < 5) {
                    treeCounts(v5 + i) = 0
                    i += 1
                }
                treeCounts(v5 + valMod) = 1
            } else {
                val tm = (tl + tr) / 2
                build(2 * v, tl, tm)
                build(2 * v + 1, tm + 1, tr)
                mergeToNode(v, 2 * v, 2 * v + 1)
            }
        }

        def update(v: Int, tl: Int, tr: Int, pos: Int, newVal: Int): Unit = {
            if (tl == tr) {
                val valMod = newVal % k
                treeTotal(v) = valMod
                val v5 = v * 5
                var i = 0
                while (i < 5) {
                    treeCounts(v5 + i) = 0
                    i += 1
                }
                treeCounts(v5 + valMod) = 1
            } else {
                val tm = (tl + tr) / 2
                if (pos <= tm) {
                    update(2 * v, tl, tm, pos, newVal)
                } else {
                    update(2 * v + 1, tm + 1, tr, pos, newVal)
                }
                mergeToNode(v, 2 * v, 2 * v + 1)
            }
        }

        def query(v: Int, tl: Int, tr: Int, l: Int, r: Int): Node = {
            if (l == tl && r == tr) {
                val counts = new Array[Int](5)
                val offset = v * 5
                var i = 0
                while (i < 5) {
                    counts(i) = treeCounts(offset + i)
                    i += 1
                }
                return new Node(treeTotal(v), counts)
            }
            val tm = (tl + tr) / 2
            if (r <= tm) {
                query(2 * v, tl, tm, l, r)
            } else if (l > tm) {
                query(2 * v + 1, tm + 1, tr, l, r)
            } else {
                val leftRes = query(2 * v, tl, tm, l, tm)
                val rightRes = query(2 * v + 1, tm + 1, tr, tm + 1, r)
                val resTotal = (leftRes.totalProd * rightRes.totalProd) % k
                val resCounts = new Array[Int](5)
                var i = 0
                while (i < k) {
                    resCounts(i) = leftRes.counts(i)
                    i += 1
                }
                i = 0
                while (i < k) {
                    val idx = (leftRes.totalProd * i) % k
                    resCounts(idx) += rightRes.counts(i)
                    i += 1
                }
                new Node(resTotal, resCounts)
            }
        }

        build(1, 0, n - 1)

        val resArr = new Array[Int](queries.length)
        var idx = 0
        while (idx < queries.length) {
            val q = queries(idx)
            update(1, 0, n - 1, q(0), q(1))
            val qResult = query(1, 0, n - 1, q(2), n - 1)
            resArr(idx) = qResult.counts(q(3))
            idx += 1
        }
        resArr
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn result_array(nums: Vec<i32>, k: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len();
        let k_usize = k as usize;

        #[derive(Clone, Copy)]
        struct Node {
            prod: i32,
            counts: [i32; 5],
        }

        fn merge(l: &Node, r: &Node, k: usize) -> Node {
            let mut res = Node {
                prod: (l.prod * r.prod) % k as i32,
                counts: [0; 5],
            };
            for i in 0..k {
                res.counts[i] += l.counts[i];
                let target = (l.prod as usize * i) % k;
                res.counts[target] += r.counts[i];
            }
            res
        }

        let mut tree = vec![Node { prod: 0, counts: [0; 5] }; 4 * n];

        fn build(tree: &mut [Node], nums: &[i32], node: usize, start: usize, end: usize, k: usize) {
            if start == end {
                let val_mod = (nums[start] % k as i32) as usize;
                tree[node].prod = val_mod as i32;
                tree[node].counts[val_mod] = 1;
                return;
            }
            let mid = (start + end) / 2;
            build(tree, nums, 2 * node, start, mid, k);
            build(tree, nums, 2 * node + 1, mid + 1, end, k);
            tree[node] = merge(&tree[2 * node], &tree[2 * node + 1], k);
        }

        fn update(tree: &mut [Node], node: usize, start: usize, end: usize, idx: usize, val: i32, k: usize) {
            if start == end {
                let val_mod = (val % k as i32) as usize;
                tree[node].prod = val_mod as i32;
                tree[node].counts = [0; 5];
                tree[node].counts[val_mod] = 1;
                return;
            }
            let mid = (start + end) / 2;
            if idx <= mid {
                update(tree, 2 * node, start, mid, idx, val, k);
            } else {
                update(tree, 2 * node + 1, mid + 1, end, idx, val, k);
            }
            tree[node] = merge(&tree[2 * node], &tree[2 * node + 1], k);
        }

        fn query(tree: &[Node], node: usize, start: usize, end: usize, l: usize, r: usize, k: usize) -> Node {
            if l == start && r == end {
                return tree[node];
            }
            let mid = (start + end) / 2;
            if r <= mid {
                return query(tree, 2 * node, start, mid, l, r, k);
            } else if l > mid {
                return query(tree, 2 * node + 1, mid + 1, end, l, r, k);
            }
            let left_res = query(tree, 2 * node, start, mid, l, mid, k);
            let right_res = query(tree, 2 * node + 1, mid + 1, end, mid + 1, r, k);
            merge(&left_res, &right_res, k)
        }

        build(&mut tree, &nums, 1, 0, n - 1, k_usize);

        let mut results = Vec::with_capacity(queries.len());
        for q in queries {
            let idx = q[0] as usize;
            let val = q[1];
            let start = q[2] as usize;
            let x = q[3] as usize;
            update(&mut tree, 1, 0, n - 1, idx, val, k_usize);
            let res_node = query(&tree, 1, 0, n - 1, start, n - 1, k_usize);
            results.push(res_node.counts[x]);
        }
        results
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (result-array nums k queries)
  (-> (listof exact-integer?) exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([n (length nums)]
         [nums-vec (list->vector nums)]
         [tree (make-vector (* 4 n))])

    (define (merge-nodes l-prod l-counts r-prod r-counts k)
      (let* ([new-prod (modulo (* l-prod r-prod) k)]
             [new-counts (vector-copy l-counts)])
        (for ([i (in-range k)])
          (let* ([r-val (vector-ref r-counts i)]
                 [target-idx (modulo (* l-prod i) k)]
                 [old-val (vector-ref new-counts target-idx)])
            (vector-set! new-counts target-idx (+ old-val r-val))))
        (cons new-prod new-counts)))

    (define (build tree-vec nums-vec node start end k)
      (if (= start end)
          (let* ([v (modulo (vector-ref nums-vec start) k)]
                 [counts (make-vector k 0)])
            (vector-set! counts v 1)
            (vector-set! tree-vec node (cons v counts)))
          (let* ([mid (quotient (+ start end) 2)]
                 [left-node (* 2 node)]
                 [right-node (+ 1 (* 2 node))])
            (build tree-vec nums-vec left-node start mid k)
            (build tree-vec nums-vec right-node (+ mid 1) end k)
            (let ([left-res (vector-ref tree-vec left-node)]
                  [right-res (vector-ref tree-vec right-node)])
              (vector-set! tree-vec node (merge-nodes (car left-res) (cdr left-res)
                                                     (car right-res) (cdr right-res) k))))))

    (define (update tree-vec node start end idx val k)
      (if (= start end)
          (let* ([v (modulo val k)]
                 [counts (make-vector k 0)])
            (vector-set! counts v 1)
            (vector-set! tree-vec node (cons v counts)))
          (let* ([mid (quotient (+ start end) 2)]
                 [left-node (* 2 node)]
                 [right-node (+ 1 (* 2 node))])
            (if (<= idx mid)
                (update tree-vec left-node start mid idx val k)
                (update tree-vec right-node (+ mid 1) end idx val k))
            (let ([left-res (vector-ref tree-vec left-node)]
                  [right-res (vector-ref tree-vec right-node)])
              (vector-set! tree-vec node (merge-nodes (car left-res) (cdr left-res)
                                                     (car right-res) (cdr right-res) k))))))

    (define (query tree-vec node start end l r k)
      (if (and (= l start) (= r end))
          (vector-ref tree-vec node)
          (let* ([mid (quotient (+ start end) 2)]
                 [left-node (* 2 node)]
                 [right-node (+ 1 (* 2 node))])
            (cond
              [(<= r mid) (query tree-vec left-node start mid l r k)]
              [(> l mid) (query tree-vec right-node (+ mid 1) end l r k)]
              [else
               (let ([left-res (query tree-vec left-node start mid l mid k)]
                     [right-res (query tree-vec right-node (+ mid 1) end (+ mid 1) r k)])
                 (merge-nodes (car left-res) (cdr left-res)
                             (car right-res) (cdr right-res) k))]))))

    (build tree nums-vec 1 0 (- n 1) k)
    (for/list ([q queries])
      (let ([idx (list-ref q 0)]
            [val (list-ref q 1)]
            [start (list-ref q 2)]
            [x (list-ref q 3)])
        (update tree 1 0 (- n 1) idx val k)
        (let* ([res-node (query tree 1 0 (- n 1) start (- n 1) k)]
               [counts (cdr res-node)])
          (vector-ref counts x))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec result_array(Nums :: [integer()], K :: integer(), Queries :: [[integer()]]) -> [integer()].
result_array(Nums, K, Queries) ->
    N = length(Nums),
    NumsTuple = list_to_tuple(Nums),
    Tree = build_tree(NumsTuple, 1, N, K),
    process_queries(Queries, Tree, N, K, []).

build_tree(NumsTuple, Start, End, K) ->
    if Start == End ->
        Val = element(Start, NumsTuple) rem K,
        Counts = setelement(Val + 1, erlang:make_tuple(K, 0), 1),
        {Val, Counts, nil, nil};
    true ->
        Mid = (Start + End) div 2,
        Left = build_tree(NumsTuple, Start, Mid, K),
        Right = build_tree(NumsTuple, Mid + 1, End, K),
        merge_full(Left, Right, K)
    end.

merge_full(Left, Right, K) ->
    {LProd, LCounts, _, _} = Left,
    {RProd, RCounts, _, _} = Right,
    {NewProd, NewCounts} = merge_counts(LProd, LCounts, RProd, RCounts, K),
    {NewProd, NewCounts, Left, Right}.

merge_counts(LProd, LCounts, RProd, RCounts, K) ->
    NewProd = (LProd * RProd) rem K,
    FinalCounts = lists:foldl(fun(I, Acc) ->
        TargetIdx = (LProd * I) rem K,
        OldVal = element(TargetIdx + 1, Acc),
        RI = element(I + 1, RCounts),
        setelement(TargetIdx + 1, Acc, OldVal + RI)
    end, LCounts, lists:seq(0, K - 1)),
    {NewProd, FinalCounts}.

update_tree(Tree, Start, End, Idx, Val, K) ->
    if Start == End ->
        V = Val rem K,
        Counts = setelement(V + 1, erlang:make_tuple(K, 0), 1),
        {V, Counts, nil, nil};
    true ->
        Mid = (Start + End) div 2,
        {_, _, Left, Right} = Tree,
        if
            Idx =< Mid ->
                NewLeft = update_tree(Left, Start, Mid, Idx, Val, K),
                merge_full(NewLeft, Right, K);
            true ->
                NewRight = update_tree(Right, Mid + 1, End, Idx, Val, K),
                merge_full(Left, NewRight, K)
        end
    end.

query_tree(Tree, Start, End, QStart, QEnd, K) ->
    if (QStart == Start) and (QEnd == End) ->
        {element(1, Tree), element(2, Tree)};
    true ->
        Mid = (Start + End) div 2,
        {_, _, Left, Right} = Tree,
        if
            QEnd =< Mid -> query_tree(Left, Start, Mid, QStart, QEnd, K);
            QStart > Mid -> query_tree(Right, Mid + 1, End, QStart, QEnd, K);
            true ->
                {LP, LC} = query_tree(Left, Start, Mid, QStart, Mid, K),
                {RP, RC} = query_tree(Right, Mid + 1, End, Mid + 1, QEnd, K),
                merge_counts(LP, LC, RP, RC, K)
        end
    end.

process_queries([], _Tree, _N, _K, Acc) -> lists:reverse(Acc);
process_queries([[Idx, Val, Start, X] | Rest], Tree, N, K, Acc) ->
    NewTree = update_tree(Tree, 1, N, Idx + 1, Val, K),
    {_, Counts} = query_tree(NewTree, 1, N, Start + 1, N, K),
    process_queries(Rest, NewTree, N, K, [element(X + 1, Counts) | Acc]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec result_array(nums :: [integer], k :: integer, queries :: [[integer]]) :: [integer]
  def result_array(nums, k, queries) do
    n = length(nums)
    nums_tuple = List.to_tuple(nums)
    tree = build(nums_tuple, 0, n - 1, k)

    {_final_tree, results} = Enum.map_reduce(queries, tree, fn [idx, val, start, x], current_tree ->
      updated_tree = update(current_tree, 0, n - 1, idx, val, k)
      {_p, counts} = query(updated_tree, 0, n - 1, start, n - 1, k)
      {elem(counts, x), updated_tree}
    end)
    results
  end

  defp build(nums_tuple, start, stop, k) do
    if start == stop do
      val = Integer.mod(elem(nums_tuple, start), k)
      counts = List.to_tuple(for i <- 0..(k - 1), do: (if i == val, do: 1, else: 0))
      {val, counts, nil, nil}
    else
      mid = div(start + stop, 2)
      left = build(nums_tuple, start, mid, k)
      right = build(nums_tuple, mid + 1, stop, k)
      merge_full(left, right, k)
    end
  end

  defp update(tree, start, stop, idx, val, k) do
    if start == stop do
      val_mod = Integer.mod(val, k)
      counts = List.to_tuple(for i <- 0..(k - 1), do: (if i == val_mod, do: 1, else: 0))
      {val_mod, counts, nil, nil}
    else
      mid = div(start + stop, 2)
      {_, _, left, right} = tree
      if idx <= mid do
        new_left = update(left, start, mid, idx, val, k)
        merge_full(new_left, right, k)
      else
        new_right = update(right, mid + 1, stop, idx, val, k)
        merge_full(left, new_right, k)
      end
    end
  end

  defp query(tree, start, stop, q_start, q_stop, k) do
    if q_start == start and q_stop == stop do
      {elem(tree, 0), elem(tree, 1)}
    else
      mid = div(start + stop, 2)
      {_, _, left, right} = tree
      cond do
        q_stop <= mid -> query(left, start, mid, q_start, q_stop, k)
        q_start > mid -> query(right, mid + 1, stop, q_start, q_stop, k)
        true ->
          {lp, lc} = query(left, start, mid, q_start, mid, k)
          {rp, rc} = query(right, mid + 1, stop, mid + 1, q_stop, k)
          merge_counts(lp, lc, rp, rc, k)
      end
    end
  end

  defp merge_full({lp, lc, ll, lr}, {rp, rc, rl, rr}, k) do
    {p, nc} = merge_counts(lp, lc, rp, rc, k)
    {p, nc, {lp, lc, ll, lr}, {rp, rc, rl, rr}}
  end

  defp merge_counts(lp, lc, _rp, rc, k) do
    p = Integer.mod(lp * _rp, k)
    nc = Enum.reduce(0..(k - 1), lc, fn i, acc ->
      target = Integer.mod(lp * i, k)
      put_elem(acc, target, elem(acc, target) + elem(rc, i))
    end)
    {p, nc}
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O((N + Q) * k * log N), where N is the length of the array and Q is the number of queries. Building the tree takes O(N * k), and each query involves one point update and one range query, each taking O(k * log N) time.
- **Space Complexity:** O(N * k) to store the segment tree nodes, with each node containing an array of size k for prefix product counts and a scalar for the range product.
