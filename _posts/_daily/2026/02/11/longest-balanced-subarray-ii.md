---
layout: post
title: "Longest Balanced Subarray II"
date: 2026-02-11 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Hash Table", "Divide and Conquer", "Segment Tree", "Prefix Sum"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/longest-balanced-subarray-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\n    int tree_min[400005], tree_max[400005], tree_lazy[400005];\n\
        \    void push_down(int v) {\n        if (tree_lazy[v] != 0) {\n           \
        \ int lz = tree_lazy[v];\n            tree_min[2 * v] += lz; tree_max[2 * v]\
        \ += lz; tree_lazy[2 * v] += lz;\n            tree_min[2 * v + 1] += lz; tree_max[2\
        \ * v + 1] += lz; tree_lazy[2 * v + 1] += lz;\n            tree_lazy[v] = 0;\n\
        \        }\n    }\n    void update(int v, int tl, int tr, int l, int r, int\
        \ add) {\n        if (l > r) return;\n        if (l == tl && r == tr) {\n  \
        \          tree_min[v] += add; tree_max[v] += add; tree_lazy[v] += add;\n  \
        \      } else {\n            push_down(v);\n            int tm = (tl + tr) /\
        \ 2;\n            update(2 * v, tl, tm, l, std::min(r, tm), add);\n        \
        \    update(2 * v + 1, tm + 1, tr, std::max(l, tm + 1), r, add);\n         \
        \   tree_min[v] = std::min(tree_min[2 * v], tree_min[2 * v + 1]);\n        \
        \    tree_max[v] = std::max(tree_max[2 * v], tree_max[2 * v + 1]);\n       \
        \ }\n    }\n    int find_last(int v, int tl, int tr, int l, int r) {\n     \
        \   if (l > tr || r < tl || tree_min[v] > 0 || tree_max[v] < 0) return -1;\n\
        \        if (tl == tr) return tl;\n        push_down(v);\n        int tm = (tl\
        \ + tr) / 2;\n        int res = find_last(2 * v + 1, tm + 1, tr, l, r);\n  \
        \      if (res == -1) res = find_last(2 * v, tl, tm, l, r);\n        return\
        \ res;\n    }\npublic:\n    int longestBalanced(vector<int>& nums) {\n     \
        \   int n = nums.size();\n        std::vector<int> pos[100001];\n        for\
        \ (int i = 0; i < n; i++) pos[nums[i]].push_back(i);\n        std::fill(tree_min,\
        \ tree_min + 4 * n + 1, 0);\n        std::fill(tree_max, tree_max + 4 * n +\
        \ 1, 0);\n        std::fill(tree_lazy, tree_lazy + 4 * n + 1, 0);\n        int\
        \ sign[100001];\n        for (int i = 0; i < 100001; i++) sign[i] = (i % 2 ==\
        \ 0) ? -1 : 1;\n        for (int i = 0; i < 100001; i++) {\n            if (!pos[i].empty())\
        \ update(1, 0, n - 1, pos[i][0], n - 1, sign[i]);\n        }\n        int ans\
        \ = 0;\n        std::vector<int> curr_idx(100001, 0);\n        for (int l =\
        \ 0; l < n; l++) {\n            int r = find_last(1, 0, n - 1, l, n - 1);\n\
        \            if (r != -1) ans = std::max(ans, r - l + 1);\n            int v\
        \ = nums[l];\n            int next_p = (curr_idx[v] + 1 < pos[v].size()) ? pos[v][curr_idx[v]\
        \ + 1] : n;\n            update(1, 0, n - 1, 0, next_p - 1, -sign[v]);\n   \
        \         curr_idx[v]++;\n        }\n        return ans;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    int[] treeMin, treeMax, treeLazy;\n\
        \    private void pushDown(int v) {\n        if (treeLazy[v] != 0) {\n     \
        \       int lz = treeLazy[v];\n            treeMin[2 * v] += lz; treeMax[2 *\
        \ v] += lz; treeLazy[2 * v] += lz;\n            treeMin[2 * v + 1] += lz; treeMax[2\
        \ * v + 1] += lz; treeLazy[2 * v + 1] += lz;\n            treeLazy[v] = 0;\n\
        \        }\n    }\n    private void update(int v, int tl, int tr, int l, int\
        \ r, int add) {\n        if (l > r) return;\n        if (l == tl && r == tr)\
        \ {\n            treeMin[v] += add; treeMax[v] += add; treeLazy[v] += add;\n\
        \        } else {\n            pushDown(v);\n            int tm = (tl + tr)\
        \ / 2;\n            update(2 * v, tl, tm, l, Math.min(r, tm), add);\n      \
        \      update(2 * v + 1, tm + 1, tr, Math.max(l, tm + 1), r, add);\n       \
        \     treeMin[v] = Math.min(treeMin[2 * v], treeMin[2 * v + 1]);\n         \
        \   treeMax[v] = Math.max(treeMax[2 * v], treeMax[2 * v + 1]);\n        }\n\
        \    }\n    private int findLast(int v, int tl, int tr, int l, int r) {\n  \
        \      if (l > tr || r < tl || treeMin[v] > 0 || treeMax[v] < 0) return -1;\n\
        \        if (tl == tr) return tl;\n        pushDown(v);\n        int tm = (tl\
        \ + tr) / 2;\n        int res = findLast(2 * v + 1, tm + 1, tr, l, r);\n   \
        \     if (res == -1) res = findLast(2 * v, tl, tm, l, r);\n        return res;\n\
        \    }\n    public int longestBalanced(int[] nums) {\n        int n = nums.length;\n\
        \        treeMin = new int[4 * n + 1];\n        treeMax = new int[4 * n + 1];\n\
        \        treeLazy = new int[4 * n + 1];\n        List<Integer>[] pos = new ArrayList[100001];\n\
        \        for (int i = 0; i < 100001; i++) pos[i] = new ArrayList<>();\n    \
        \    for (int i = 0; i < n; i++) pos[nums[i]].add(i);\n        int[] sign =\
        \ new int[100001];\n        for (int i = 0; i < 100001; i++) sign[i] = (i %\
        \ 2 == 0) ? -1 : 1;\n        for (int i = 0; i < 100001; i++) {\n          \
        \  if (!pos[i].isEmpty()) update(1, 0, n - 1, pos[i].get(0), n - 1, sign[i]);\n\
        \        }\n        int ans = 0;\n        int[] currIdx = new int[100001];\n\
        \        for (int l = 0; l < n; l++) {\n            int r = findLast(1, 0, n\
        \ - 1, l, n - 1);\n            if (r != -1) ans = Math.max(ans, r - l + 1);\n\
        \            int v = nums[l];\n            int nextP = (currIdx[v] + 1 < pos[v].size())\
        \ ? pos[v].get(currIdx[v] + 1) : n;\n            update(1, 0, n - 1, 0, nextP\
        \ - 1, -sign[v]);\n            currIdx[v]++;\n        }\n        return ans;\n\
        \    }\n}"
      python: "class Solution(object):\n    def longestBalanced(self, nums):\n     \
        \   n = len(nums)\n        tree_min = [0] * (4 * n + 1)\n        tree_max =\
        \ [0] * (4 * n + 1)\n        tree_lazy = [0] * (4 * n + 1)\n\n        def update(v,\
        \ tl, tr, l, r, add):\n            if l <= tl and tr <= r:\n               \
        \ tree_min[v] += add\n                tree_max[v] += add\n                tree_lazy[v]\
        \ += add\n                return\n            lz = tree_lazy[v]\n          \
        \  if lz:\n                v2, v21 = v << 1, (v << 1) | 1\n                tree_min[v2]\
        \ += lz; tree_max[v2] += lz; tree_lazy[v2] += lz\n                tree_min[v21]\
        \ += lz; tree_max[v21] += lz; tree_lazy[v21] += lz\n                tree_lazy[v]\
        \ = 0\n            tm = (tl + tr) >> 1\n            if l <= tm: update(v <<\
        \ 1, tl, tm, l, r, add)\n            if r > tm: update((v << 1) | 1, tm + 1,\
        \ tr, l, r, add)\n            tree_min[v] = min(tree_min[v << 1], tree_min[(v\
        \ << 1) | 1])\n            tree_max[v] = max(tree_max[v << 1], tree_max[(v <<\
        \ 1) | 1])\n\n        def find_last(v, tl, tr, l, r):\n            if l > tr\
        \ or r < tl or tree_min[v] > 0 or tree_max[v] < 0:\n                return -1\n\
        \            if tl == tr: return tl\n            lz = tree_lazy[v]\n       \
        \     if lz:\n                v2, v21 = v << 1, (v << 1) | 1\n             \
        \   tree_min[v2] += lz; tree_max[v2] += lz; tree_lazy[v2] += lz\n          \
        \      tree_min[v21] += lz; tree_max[v21] += lz; tree_lazy[v21] += lz\n    \
        \            tree_lazy[v] = 0\n            tm = (tl + tr) >> 1\n           \
        \ res = find_last((v << 1) | 1, tm + 1, tr, l, r)\n            if res == -1:\
        \ res = find_last(v << 1, tl, tm, l, r)\n            return res\n\n        pos\
        \ = [[] for _ in range(100001)]\n        for i, val in enumerate(nums): pos[val].append(i)\n\
        \        sign = [-1 if i % 2 == 0 else 1 for i in range(100001)]\n        for\
        \ i in range(100001):\n            if pos[i]: update(1, 0, n - 1, pos[i][0],\
        \ n - 1, sign[i])\n\n        ans, curr_idx = 0, [0] * 100001\n        for l\
        \ in range(n):\n            r = find_last(1, 0, n - 1, l, n - 1)\n         \
        \   if r != -1: ans = max(ans, r - l + 1)\n            v = nums[l]\n       \
        \     next_p = pos[v][curr_idx[v] + 1] if curr_idx[v] + 1 < len(pos[v]) else\
        \ n\n            update(1, 0, n - 1, 0, next_p - 1, -sign[v])\n            curr_idx[v]\
        \ += 1\n        return ans"
      python3: "class Solution:\n    def longestBalanced(self, nums: List[int]) -> int:\n\
        \        n = len(nums)\n        tree_min = [0] * (4 * n + 1)\n        tree_max\
        \ = [0] * (4 * n + 1)\n        tree_lazy = [0] * (4 * n + 1)\n\n        def\
        \ update(v, tl, tr, l, r, add):\n            if l <= tl and tr <= r:\n     \
        \           tree_min[v] += add\n                tree_max[v] += add\n       \
        \         tree_lazy[v] += add\n                return\n            lz = tree_lazy[v]\n\
        \            if lz:\n                v2, v21 = v << 1, (v << 1) | 1\n      \
        \          tree_min[v2] += lz; tree_max[v2] += lz; tree_lazy[v2] += lz\n   \
        \             tree_min[v21] += lz; tree_max[v21] += lz; tree_lazy[v21] += lz\n\
        \                tree_lazy[v] = 0\n            tm = (tl + tr) >> 1\n       \
        \     if l <= tm: update(v << 1, tl, tm, l, r, add)\n            if r > tm:\
        \ update((v << 1) | 1, tm + 1, tr, l, r, add)\n            tree_min[v] = min(tree_min[v\
        \ << 1], tree_min[(v << 1) | 1])\n            tree_max[v] = max(tree_max[v <<\
        \ 1], tree_max[(v << 1) | 1])\n\n        def find_last(v, tl, tr, l, r):\n \
        \           if l > tr or r < tl or tree_min[v] > 0 or tree_max[v] < 0:\n   \
        \             return -1\n            if tl == tr: return tl\n            lz\
        \ = tree_lazy[v]\n            if lz:\n                v2, v21 = v << 1, (v <<\
        \ 1) | 1\n                tree_min[v2] += lz; tree_max[v2] += lz; tree_lazy[v2]\
        \ += lz\n                tree_min[v21] += lz; tree_max[v21] += lz; tree_lazy[v21]\
        \ += lz\n                tree_lazy[v] = 0\n            tm = (tl + tr) >> 1\n\
        \            res = find_last((v << 1) | 1, tm + 1, tr, l, r)\n            if\
        \ res == -1: res = find_last(v << 1, tl, tm, l, r)\n            return res\n\
        \n        pos = [[] for _ in range(100001)]\n        for i, val in enumerate(nums):\
        \ pos[val].append(i)\n        sign = [-1 if i % 2 == 0 else 1 for i in range(100001)]\n\
        \        for i in range(100001):\n            if pos[i]: update(1, 0, n - 1,\
        \ pos[i][0], n - 1, sign[i])\n\n        ans, curr_idx = 0, [0] * 100001\n  \
        \      for l in range(n):\n            r = find_last(1, 0, n - 1, l, n - 1)\n\
        \            if r != -1: ans = max(ans, r - l + 1)\n            v = nums[l]\n\
        \            next_p = pos[v][curr_idx[v] + 1] if curr_idx[v] + 1 < len(pos[v])\
        \ else n\n            update(1, 0, n - 1, 0, next_p - 1, -sign[v])\n       \
        \     curr_idx[v] += 1\n        return ans"
      c: "#include <stdlib.h>\n#include <string.h>\n\n#define MIN(a, b) ((a) < (b) ?\
        \ (a) : (b))\n#define MAX(a, b) ((a) > (b) ? (a) : (b))\n\nint tree_min[400005],\
        \ tree_max[400005], tree_lazy[400005];\n\nvoid push_down(int v) {\n    if (tree_lazy[v]\
        \ != 0) {\n        int lz = tree_lazy[v];\n        tree_min[2 * v] += lz; tree_max[2\
        \ * v] += lz; tree_lazy[2 * v] += lz;\n        tree_min[2 * v + 1] += lz; tree_max[2\
        \ * v + 1] += lz; tree_lazy[2 * v + 1] += lz;\n        tree_lazy[v] = 0;\n \
        \   }\n}\n\nvoid update(int v, int tl, int tr, int l, int r, int add) {\n  \
        \  if (l > r) return;\n    if (l == tl && r == tr) {\n        tree_min[v] +=\
        \ add; tree_max[v] += add; tree_lazy[v] += add;\n    } else {\n        push_down(v);\n\
        \        int tm = (tl + tr) / 2;\n        update(2 * v, tl, tm, l, MIN(r, tm),\
        \ add);\n        update(2 * v + 1, tm + 1, tr, MAX(l, tm + 1), r, add);\n  \
        \      tree_min[v] = MIN(tree_min[2 * v], tree_min[2 * v + 1]);\n        tree_max[v]\
        \ = MAX(tree_max[2 * v], tree_max[2 * v + 1]);\n    }\n}\n\nint find_last(int\
        \ v, int tl, int tr, int l, int r) {\n    if (l > tr || r < tl || tree_min[v]\
        \ > 0 || tree_max[v] < 0) return -1;\n    if (tl == tr) return tl;\n    push_down(v);\n\
        \    int tm = (tl + tr) / 2;\n    int res = find_last(2 * v + 1, tm + 1, tr,\
        \ l, r);\n    if (res == -1) res = find_last(2 * v, tl, tm, l, r);\n    return\
        \ res;\n}\n\nint longestBalanced(int* nums, int numsSize) {\n    memset(tree_min,\
        \ 0, sizeof(tree_min));\n    memset(tree_max, 0, sizeof(tree_max));\n    memset(tree_lazy,\
        \ 0, sizeof(tree_lazy));\n    int* head = malloc(100001 * sizeof(int));\n  \
        \  int* next = malloc(numsSize * sizeof(int));\n    int* curr = malloc(100001\
        \ * sizeof(int));\n    for (int i = 0; i < 100001; i++) head[i] = -1;\n    for\
        \ (int i = numsSize - 1; i >= 0; i--) {\n        next[i] = head[nums[i]];\n\
        \        head[nums[i]] = i;\n    }\n    memcpy(curr, head, 100001 * sizeof(int));\n\
        \    int sign[100001];\n    for (int i = 0; i < 100001; i++) {\n        sign[i]\
        \ = (i % 2 == 0) ? -1 : 1;\n        if (head[i] != -1) update(1, 0, numsSize\
        \ - 1, head[i], numsSize - 1, sign[i]);\n    }\n    int ans = 0;\n    for (int\
        \ l = 0; l < numsSize; l++) {\n        int r = find_last(1, 0, numsSize - 1,\
        \ l, numsSize - 1);\n        if (r != -1) ans = MAX(ans, r - l + 1);\n     \
        \   int v = nums[l];\n        int nxt_p = next[curr[v]];\n        curr[v] =\
        \ nxt_p;\n        if (nxt_p == -1) nxt_p = numsSize;\n        update(1, 0, numsSize\
        \ - 1, 0, nxt_p - 1, -sign[v]);\n    }\n    free(head); free(next); free(curr);\n\
        \    return ans;\n}"
      csharp: "public class Solution {\n    int[] treeMin, treeMax, treeLazy;\n    private\
        \ void PushDown(int v) {\n        if (treeLazy[v] != 0) {\n            int lz\
        \ = treeLazy[v];\n            treeMin[2 * v] += lz; treeMax[2 * v] += lz; treeLazy[2\
        \ * v] += lz;\n            treeMin[2 * v + 1] += lz; treeMax[2 * v + 1] += lz;\
        \ treeLazy[2 * v + 1] += lz;\n            treeLazy[v] = 0;\n        }\n    }\n\
        \    private void Update(int v, int tl, int tr, int l, int r, int add) {\n \
        \       if (l > r) return;\n        if (l == tl && r == tr) {\n            treeMin[v]\
        \ += add; treeMax[v] += add; treeLazy[v] += add;\n        } else {\n       \
        \     PushDown(v);\n            int tm = (tl + tr) / 2;\n            Update(2\
        \ * v, tl, tm, l, Math.Min(r, tm), add);\n            Update(2 * v + 1, tm +\
        \ 1, tr, Math.Max(l, tm + 1), r, add);\n            treeMin[v] = Math.Min(treeMin[2\
        \ * v], treeMin[2 * v + 1]);\n            treeMax[v] = Math.Max(treeMax[2 *\
        \ v], treeMax[2 * v + 1]);\n        }\n    }\n    private int FindLast(int v,\
        \ int tl, int tr, int l, int r) {\n        if (l > tr || r < tl || treeMin[v]\
        \ > 0 || treeMax[v] < 0) return -1;\n        if (tl == tr) return tl;\n    \
        \    PushDown(v);\n        int tm = (tl + tr) / 2;\n        int res = FindLast(2\
        \ * v + 1, tm + 1, tr, l, r);\n        if (res == -1) res = FindLast(2 * v,\
        \ tl, tm, l, r);\n        return res;\n    }\n    public int LongestBalanced(int[]\
        \ nums) {\n        int n = nums.Length;\n        treeMin = new int[4 * n + 1];\
        \ treeMax = new int[4 * n + 1]; treeLazy = new int[4 * n + 1];\n        List<int>[]\
        \ pos = new List<int>[100001];\n        for (int i = 0; i < 100001; i++) pos[i]\
        \ = new List<int>();\n        for (int i = 0; i < n; i++) pos[nums[i]].Add(i);\n\
        \        int[] sign = new int[100001];\n        for (int i = 0; i < 100001;\
        \ i++) sign[i] = (i % 2 == 0) ? -1 : 1;\n        for (int i = 0; i < 100001;\
        \ i++) {\n            if (pos[i].Count > 0) Update(1, 0, n - 1, pos[i][0], n\
        \ - 1, sign[i]);\n        }\n        int ans = 0;\n        int[] currIdx = new\
        \ int[100001];\n        for (int l = 0; l < n; l++) {\n            int r = FindLast(1,\
        \ 0, n - 1, l, n - 1);\n            if (r != -1) ans = Math.Max(ans, r - l +\
        \ 1);\n            int v = nums[l];\n            int nextP = (currIdx[v] + 1\
        \ < pos[v].Count) ? pos[v][currIdx[v] + 1] : n;\n            Update(1, 0, n\
        \ - 1, 0, nextP - 1, -sign[v]);\n            currIdx[v]++;\n        }\n    \
        \    return ans;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar longestBalanced\
        \ = function(nums) {\n    let n = nums.length;\n    let treeMin = new Int32Array(4\
        \ * n + 1);\n    let treeMax = new Int32Array(4 * n + 1);\n    let treeLazy\
        \ = new Int32Array(4 * n + 1);\n\n    function pushDown(v) {\n        if (treeLazy[v]\
        \ !== 0) {\n            let lz = treeLazy[v];\n            treeMin[2 * v] +=\
        \ lz; treeMax[2 * v] += lz; treeLazy[2 * v] += lz;\n            treeMin[2 *\
        \ v + 1] += lz; treeMax[2 * v + 1] += lz; treeLazy[2 * v + 1] += lz;\n     \
        \       treeLazy[v] = 0;\n        }\n    }\n\n    function update(v, tl, tr,\
        \ l, r, add) {\n        if (l > r) return;\n        if (l === tl && r === tr)\
        \ {\n            treeMin[v] += add; treeMax[v] += add; treeLazy[v] += add;\n\
        \        } else {\n            pushDown(v);\n            let tm = Math.floor((tl\
        \ + tr) / 2);\n            update(2 * v, tl, tm, l, Math.min(r, tm), add);\n\
        \            update(2 * v + 1, tm + 1, tr, Math.max(l, tm + 1), r, add);\n \
        \           treeMin[v] = Math.min(treeMin[2 * v], treeMin[2 * v + 1]);\n   \
        \         treeMax[v] = Math.max(treeMax[2 * v], treeMax[2 * v + 1]);\n     \
        \   }\n    }\n\n    function findLast(v, tl, tr, l, r) {\n        if (l > tr\
        \ || r < tl || treeMin[v] > 0 || treeMax[v] < 0) return -1;\n        if (tl\
        \ === tr) return tl;\n        pushDown(v);\n        let tm = Math.floor((tl\
        \ + tr) / 2);\n        let res = findLast(2 * v + 1, tm + 1, tr, l, r);\n  \
        \      if (res === -1) res = findLast(2 * v, tl, tm, l, r);\n        return\
        \ res;\n    }\n\n    let pos = new Array(100001);\n    for (let i = 0; i < n;\
        \ i++) {\n        if (!pos[nums[i]]) pos[nums[i]] = [];\n        pos[nums[i]].push(i);\n\
        \    }\n    let sign = new Int32Array(100001);\n    for (let i = 0; i < 100001;\
        \ i++) sign[i] = (i % 2 === 0) ? -1 : 1;\n    for (let i = 0; i < 100001; i++)\
        \ {\n        if (pos[i]) update(1, 0, n - 1, pos[i][0], n - 1, sign[i]);\n \
        \   }\n\n    let ans = 0, currIdx = new Int32Array(100001);\n    for (let l\
        \ = 0; l < n; l++) {\n        let r = findLast(1, 0, n - 1, l, n - 1);\n   \
        \     if (r !== -1) ans = Math.max(ans, r - l + 1);\n        let v = nums[l];\n\
        \        let nextP = (currIdx[v] + 1 < pos[v].length) ? pos[v][currIdx[v] +\
        \ 1] : n;\n        update(1, 0, n - 1, 0, nextP - 1, -sign[v]);\n        currIdx[v]++;\n\
        \    }\n    return ans;\n};"
      typescript: "class SegmentTree {\n    min: Int32Array;\n    max: Int32Array;\n\
        \    lazy: Int32Array;\n    n: number;\n\n    constructor(n: number) {\n   \
        \     this.n = n;\n        this.min = new Int32Array(4 * n);\n        this.max\
        \ = new Int32Array(4 * n);\n        this.lazy = new Int32Array(4 * n);\n   \
        \ }\n\n    pushDown(node: number) {\n        if (this.lazy[node] !== 0) {\n\
        \            const val = this.lazy[node];\n            this.min[2 * node + 1]\
        \ += val;\n            this.max[2 * node + 1] += val;\n            this.lazy[2\
        \ * node + 1] += val;\n            this.min[2 * node + 2] += val;\n        \
        \    this.max[2 * node + 2] += val;\n            this.lazy[2 * node + 2] +=\
        \ val;\n            this.lazy[node] = 0;\n        }\n    }\n\n    update(node:\
        \ number, start: number, end: number, qL: number, qR: number, val: number) {\n\
        \        if (qL > end || qR < start) return;\n        if (qL <= start && end\
        \ <= qR) {\n            this.min[node] += val;\n            this.max[node] +=\
        \ val;\n            this.lazy[node] += val;\n            return;\n        }\n\
        \        this.pushDown(node);\n        const mid = (start + end) >> 1;\n   \
        \     this.update(2 * node + 1, start, mid, qL, qR, val);\n        this.update(2\
        \ * node + 2, mid + 1, end, qL, qR, val);\n        this.min[node] = Math.min(this.min[2\
        \ * node + 1], this.min[2 * node + 2]);\n        this.max[node] = Math.max(this.max[2\
        \ * node + 1], this.max[2 * node + 2]);\n    }\n\n    findMax(node: number,\
        \ start: number, end: number, qL: number, qR: number): number {\n        if\
        \ (qL > end || qR < start || this.min[node] > 0 || this.max[node] < 0) return\
        \ -1;\n        if (start === end) return start;\n        this.pushDown(node);\n\
        \        const mid = (start + end) >> 1;\n        let res = this.findMax(2 *\
        \ node + 2, mid + 1, end, qL, qR);\n        if (res === -1) {\n            res\
        \ = this.findMax(2 * node + 1, start, mid, qL, qR);\n        }\n        return\
        \ res;\n    }\n}\n\nfunction longestBalanced(nums: number[]): number {\n   \
        \ const n = nums.length;\n    const nextIdx = new Int32Array(n).fill(n);\n \
        \   const lastOcc = new Int32Array(100001).fill(-1);\n    for (let i = n - 1;\
        \ i >= 0; i--) {\n        if (lastOcc[nums[i]] !== -1) nextIdx[i] = lastOcc[nums[i]];\n\
        \        lastOcc[nums[i]] = i;\n    }\n\n    const st = new SegmentTree(n);\n\
        \    const firstOcc = new Int32Array(100001).fill(-1);\n    for (let i = 0;\
        \ i < n; i++) {\n        if (firstOcc[nums[i]] === -1) {\n            firstOcc[nums[i]]\
        \ = i;\n            const sign = (nums[i] % 2 === 0 ? -1 : 1);\n           \
        \ st.update(0, 0, n - 1, i, n - 1, sign);\n        }\n    }\n\n    let ans =\
        \ 0;\n    for (let l = 0; l < n; l++) {\n        const r = st.findMax(0, 0,\
        \ n - 1, l, n - 1);\n        if (r !== -1) ans = Math.max(ans, r - l + 1);\n\
        \        const sign = (nums[l] % 2 === 0 ? -1 : 1);\n        st.update(0, 0,\
        \ n - 1, l, nextIdx[l] - 1, -sign);\n    }\n    return ans;\n};"
      php: "class Solution {\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function longestBalanced($nums) {\n        $n = count($nums);\n\
        \        $nextIdx = array_fill(0, $n, $n);\n        $lastOcc = array_fill(0,\
        \ 100001, -1);\n        for ($i = $n - 1; $i >= 0; $i--) {\n            if ($lastOcc[$nums[$i]]\
        \ !== -1) $nextIdx[$i] = $lastOcc[$nums[$i]];\n            $lastOcc[$nums[$i]]\
        \ = $i;\n        }\n\n        $treeMin = new SplFixedArray(4 * $n);\n      \
        \  $treeMax = new SplFixedArray(4 * $n);\n        $lazy = new SplFixedArray(4\
        \ * $n);\n        for ($i = 0; $i < 4 * $n; $i++) {\n            $treeMin[$i]\
        \ = 0; $treeMax[$i] = 0; $lazy[$i] = 0;\n        }\n\n        $update = function($node,\
        \ $start, $end, $qL, $qR, $val) use (&$update, &$treeMin, &$treeMax, &$lazy)\
        \ {\n            if ($qL > $end || $qR < $start) return;\n            if ($qL\
        \ <= $start && $end <= $qR) {\n                $treeMin[$node] += $val;\n  \
        \              $treeMax[$node] += $val;\n                $lazy[$node] += $val;\n\
        \                return;\n            }\n            if ($lazy[$node] != 0)\
        \ {\n                $v = $lazy[$node];\n                $treeMin[2*$node+1]\
        \ += $v; $treeMax[2*$node+1] += $v; $lazy[2*$node+1] += $v;\n              \
        \  $treeMin[2*$node+2] += $v; $treeMax[2*$node+2] += $v; $lazy[2*$node+2] +=\
        \ $v;\n                $lazy[$node] = 0;\n            }\n            $mid =\
        \ ($start + $end) >> 1;\n            $update(2 * $node + 1, $start, $mid, $qL,\
        \ $qR, $val);\n            $update(2 * $node + 2, $mid + 1, $end, $qL, $qR,\
        \ $val);\n            $treeMin[$node] = min($treeMin[2 * $node + 1], $treeMin[2\
        \ * $node + 2]);\n            $treeMax[$node] = max($treeMax[2 * $node + 1],\
        \ $treeMax[2 * $node + 2]);\n        };\n\n        $findMax = function($node,\
        \ $start, $end, $qL, $qR) use (&$findMax, &$treeMin, &$treeMax, &$lazy) {\n\
        \            if ($qL > $end || $qR < $start || $treeMin[$node] > 0 || $treeMax[$node]\
        \ < 0) return -1;\n            if ($start == $end) return $start;\n        \
        \    if ($lazy[$node] != 0) {\n                $v = $lazy[$node];\n        \
        \        $treeMin[2*$node+1] += $v; $treeMax[2*$node+1] += $v; $lazy[2*$node+1]\
        \ += $v;\n                $treeMin[2*$node+2] += $v; $treeMax[2*$node+2] +=\
        \ $v; $lazy[2*$node+2] += $v;\n                $lazy[$node] = 0;\n         \
        \   }\n            $mid = ($start + $end) >> 1;\n            $res = $findMax(2\
        \ * $node + 2, $mid + 1, $end, $qL, $qR);\n            if ($res == -1) $res\
        \ = $findMax(2 * $node + 1, $start, $mid, $qL, $qR);\n            return $res;\n\
        \        };\n\n        $firstOcc = array_fill(0, 100001, -1);\n        for ($i\
        \ = 0; $i < $n; $i++) {\n            if ($firstOcc[$nums[$i]] === -1) {\n  \
        \              $firstOcc[$nums[$i]] = $i;\n                $sign = ($nums[$i]\
        \ % 2 === 0 ? -1 : 1);\n                $update(0, 0, $n - 1, $i, $n - 1, $sign);\n\
        \            }\n        }\n\n        $ans = 0;\n        for ($l = 0; $l < $n;\
        \ $l++) {\n            $r = $findMax(0, 0, $n - 1, $l, $n - 1);\n          \
        \  if ($r != -1) $ans = max($ans, $r - $l + 1);\n            $sign = ($nums[$l]\
        \ % 2 === 0 ? -1 : 1);\n            $update(0, 0, $n - 1, $l, $nextIdx[$l] -\
        \ 1, -$sign);\n        }\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    class SegmentTree {\n        var treeMin: [Int]\n\
        \        var treeMax: [Int]\n        var lazy: [Int]\n        var n: Int\n\n\
        \        init(_ n: Int) {\n            self.n = n\n            self.treeMin\
        \ = Array(repeating: 0, count: 4 * n)\n            self.treeMax = Array(repeating:\
        \ 0, count: 4 * n)\n            self.lazy = Array(repeating: 0, count: 4 * n)\n\
        \        }\n\n        func pushDown(_ node: Int) {\n            if lazy[node]\
        \ != 0 {\n                let val = lazy[node]\n                treeMin[2 *\
        \ node + 1] += val\n                treeMax[2 * node + 1] += val\n         \
        \       lazy[2 * node + 1] += val\n                treeMin[2 * node + 2] +=\
        \ val\n                treeMax[2 * node + 2] += val\n                lazy[2\
        \ * node + 2] += val\n                lazy[node] = 0\n            }\n      \
        \  }\n\n        func update(_ node: Int, _ start: Int, _ end: Int, _ qL: Int,\
        \ _ qR: Int, _ val: Int) {\n            if qL > end || qR < start { return }\n\
        \            if qL <= start && end <= qR {\n                treeMin[node] +=\
        \ val\n                treeMax[node] += val\n                lazy[node] += val\n\
        \                return\n            }\n            pushDown(node)\n       \
        \     let mid = (start + end) / 2\n            update(2 * node + 1, start, mid,\
        \ qL, qR, val)\n            update(2 * node + 2, mid + 1, end, qL, qR, val)\n\
        \            treeMin[node] = min(treeMin[2 * node + 1], treeMin[2 * node + 2])\n\
        \            treeMax[node] = max(treeMax[2 * node + 1], treeMax[2 * node + 2])\n\
        \        }\n\n        func findMax(_ node: Int, _ start: Int, _ end: Int, _\
        \ qL: Int, _ qR: Int) -> Int {\n            if qL > end || qR < start || treeMin[node]\
        \ > 0 || treeMax[node] < 0 { return -1 }\n            if start == end { return\
        \ start }\n            pushDown(node)\n            let mid = (start + end) /\
        \ 2\n            var res = findMax(2 * node + 2, mid + 1, end, qL, qR)\n   \
        \         if res == -1 {\n                res = findMax(2 * node + 1, start,\
        \ mid, qL, qR)\n            }\n            return res\n        }\n    }\n\n\
        \    func longestBalanced(_ nums: [Int]) -> Int {\n        let n = nums.length\n\
        \        var nextIdx = Array(repeating: n, count: n)\n        var lastOcc =\
        \ Array(repeating: -1, count: 100001)\n        for i in (0..<n).reversed() {\n\
        \            if lastOcc[nums[i]] != -1 { nextIdx[i] = lastOcc[nums[i]] }\n \
        \           lastOcc[nums[i]] = i\n        }\n\n        let st = SegmentTree(n)\n\
        \        var firstOcc = Array(repeating: -1, count: 100001)\n        for i in\
        \ 0..<n {\n            if firstOcc[nums[i]] == -1 {\n                firstOcc[nums[i]]\
        \ = i\n                let sign = (nums[i] % 2 == 0 ? -1 : 1)\n            \
        \    st.update(0, 0, n - 1, i, n - 1, sign)\n            }\n        }\n\n  \
        \      var ans = 0\n        for l in 0..<n {\n            let r = st.findMax(0,\
        \ 0, n - 1, l, n - 1)\n            if r != -1 { ans = max(ans, r - l + 1) }\n\
        \            let sign = (nums[l] % 2 == 0 ? -1 : 1)\n            st.update(0,\
        \ 0, n - 1, l, nextIdx[l] - 1, -sign)\n        }\n        return ans\n    }\n\
        }\n\nextension Array {\n    var length: Int { return self.count }\n}"
      kotlin: "class Solution {\n    class SegmentTree(val n: Int) {\n        private\
        \ val treeMin = IntArray(4 * n)\n        private val treeMax = IntArray(4 *\
        \ n)\n        private val lazy = IntArray(4 * n)\n\n        private fun pushDown(node:\
        \ Int) {\n            if (lazy[node] != 0) {\n                val v = lazy[node]\n\
        \                treeMin[2 * node + 1] += v\n                treeMax[2 * node\
        \ + 1] += v\n                lazy[2 * node + 1] += v\n                treeMin[2\
        \ * node + 2] += v\n                treeMax[2 * node + 2] += v\n           \
        \     lazy[2 * node + 2] += v\n                lazy[node] = 0\n            }\n\
        \        }\n\n        fun update(node: Int, start: Int, end: Int, qL: Int, qR:\
        \ Int, v: Int) {\n            if (qL > end || qR < start) return\n         \
        \   if (qL <= start && end <= qR) {\n                treeMin[node] += v\n  \
        \              treeMax[node] += v\n                lazy[node] += v\n       \
        \         return\n            }\n            pushDown(node)\n            val\
        \ mid = (start + end) / 2\n            update(2 * node + 1, start, mid, qL,\
        \ qR, v)\n            update(2 * node + 2, mid + 1, end, qL, qR, v)\n      \
        \      treeMin[node] = minOf(treeMin[2 * node + 1], treeMin[2 * node + 2])\n\
        \            treeMax[node] = maxOf(treeMax[2 * node + 1], treeMax[2 * node +\
        \ 2])\n        }\n\n        fun findMax(node: Int, start: Int, end: Int, qL:\
        \ Int, qR: Int): Int {\n            if (qL > end || qR < start || treeMin[node]\
        \ > 0 || treeMax[node] < 0) return -1\n            if (start == end) return\
        \ start\n            pushDown(node)\n            val mid = (start + end) / 2\n\
        \            var res = findMax(2 * node + 2, mid + 1, end, qL, qR)\n       \
        \     if (res == -1) res = findMax(2 * node + 1, start, mid, qL, qR)\n     \
        \       return res\n        }\n    }\n\n    fun longestBalanced(nums: IntArray):\
        \ Int {\n        val n = nums.size\n        val nextIdx = IntArray(n) { n }\n\
        \        val lastOcc = IntArray(100001) { -1 }\n        for (i in n - 1 downTo\
        \ 0) {\n            if (lastOcc[nums[i]] != -1) nextIdx[i] = lastOcc[nums[i]]\n\
        \            lastOcc[nums[i]] = i\n        }\n\n        val st = SegmentTree(n)\n\
        \        val firstOcc = IntArray(100001) { -1 }\n        for (i in 0 until n)\
        \ {\n            if (firstOcc[nums[i]] == -1) {\n                firstOcc[nums[i]]\
        \ = i\n                val sign = if (nums[i] % 2 == 0) -1 else 1\n        \
        \        st.update(0, 0, n - 1, i, n - 1, sign)\n            }\n        }\n\n\
        \        var ans = 0\n        for (l in 0 until n) {\n            val r = st.findMax(0,\
        \ 0, n - 1, l, n - 1)\n            if (r != -1) ans = maxOf(ans, r - l + 1)\n\
        \            val sign = if (nums[l] % 2 == 0) -1 else 1\n            st.update(0,\
        \ 0, n - 1, l, nextIdx[l] - 1, -sign)\n        }\n        return ans\n    }\n\
        }"
      dart: "import 'dart:typed_data';\nimport 'dart:math';\n\nclass SegmentTree {\n\
        \  final int n;\n  final Int32List treeMin;\n  final Int32List treeMax;\n  final\
        \ Int32List lazy;\n\n  SegmentTree(this.n) \n    : treeMin = Int32List(4 * n),\n\
        \      treeMax = Int32List(4 * n),\n      lazy = Int32List(4 * n);\n\n  void\
        \ pushDown(int node) {\n    if (lazy[node] != 0) {\n      int v = lazy[node];\n\
        \      treeMin[2 * node + 1] += v;\n      treeMax[2 * node + 1] += v;\n    \
        \  lazy[2 * node + 1] += v;\n      treeMin[2 * node + 2] += v;\n      treeMax[2\
        \ * node + 2] += v;\n      lazy[2 * node + 2] += v;\n      lazy[node] = 0;\n\
        \    }\n  }\n\n  void update(int node, int start, int end, int qL, int qR, int\
        \ v) {\n    if (qL > end || qR < start) return;\n    if (qL <= start && end\
        \ <= qR) {\n      treeMin[node] += v;\n      treeMax[node] += v;\n      lazy[node]\
        \ += v;\n      return;\n    }\n    pushDown(node);\n    int mid = (start + end)\
        \ >> 1;\n    update(2 * node + 1, start, mid, qL, qR, v);\n    update(2 * node\
        \ + 2, mid + 1, end, qL, qR, v);\n    treeMin[node] = min(treeMin[2 * node +\
        \ 1], treeMin[2 * node + 2]);\n    treeMax[node] = max(treeMax[2 * node + 1],\
        \ treeMax[2 * node + 2]);\n  }\n\n  int findMax(int node, int start, int end,\
        \ int qL, int qR) {\n    if (qL > end || qR < start || treeMin[node] > 0 ||\
        \ treeMax[node] < 0) return -1;\n    if (start == end) return start;\n    pushDown(node);\n\
        \    int mid = (start + end) >> 1;\n    int res = findMax(2 * node + 2, mid\
        \ + 1, end, qL, qR);\n    if (res == -1) res = findMax(2 * node + 1, start,\
        \ mid, qL, qR);\n    return res;\n  }\n}\n\nclass Solution {\n  int longestBalanced(List<int>\
        \ nums) {\n    int n = nums.length;\n    Int32List nextIdx = Int32List(n);\n\
        \    Int32List lastOcc = Int32List(100001);\n    for(int i=0; i<100001; i++)\
        \ lastOcc[i] = -1;\n    for (int i = n - 1; i >= 0; i--) {\n      nextIdx[i]\
        \ = (lastOcc[nums[i]] != -1) ? lastOcc[nums[i]] : n;\n      lastOcc[nums[i]]\
        \ = i;\n    }\n\n    SegmentTree st = SegmentTree(n);\n    Int32List firstOcc\
        \ = Int32List(100001);\n    for(int i=0; i<100001; i++) firstOcc[i] = -1;\n\
        \    for (int i = 0; i < n; i++) {\n      if (firstOcc[nums[i]] == -1) {\n \
        \       firstOcc[nums[i]] = i;\n        int sign = (nums[i] % 2 == 0) ? -1 :\
        \ 1;\n        st.update(0, 0, n - 1, i, n - 1, sign);\n      }\n    }\n\n  \
        \  int ans = 0;\n    for (int l = 0; l < n; l++) {\n      int r = st.findMax(0,\
        \ 0, n - 1, l, n - 1);\n      if (r != -1) ans = max(ans, r - l + 1);\n    \
        \  int sign = (nums[l] % 2 == 0) ? -1 : 1;\n      st.update(0, 0, n - 1, l,\
        \ nextIdx[l] - 1, -sign);\n    }\n    return ans;\n  }\n}"
      go: "func longestBalanced(nums []int) int {\n    n := len(nums)\n    nextIdx :=\
        \ make([]int, n)\n    lastOcc := make([]int, 100001)\n    for i := range lastOcc\
        \ { lastOcc[i] = -1 }\n    for i := n - 1; i >= 0; i-- {\n        if lastOcc[nums[i]]\
        \ != -1 { nextIdx[i] = lastOcc[nums[i]] } else { nextIdx[i] = n }\n        lastOcc[nums[i]]\
        \ = i\n    }\n\n    treeMin := make([]int, 4*n)\n    treeMax := make([]int,\
        \ 4*n)\n    lazy := make([]int, 4*n)\n\n    var update func(int, int, int, int,\
        \ int, int)\n    update = func(node, start, end, qL, qR, val int) {\n      \
        \  if qL > end || qR < start { return }\n        if qL <= start && end <= qR\
        \ {\n            treeMin[node] += val; treeMax[node] += val; lazy[node] += val\n\
        \            return\n        }\n        if lazy[node] != 0 {\n            v\
        \ := lazy[node]\n            treeMin[2*node+1] += v; treeMax[2*node+1] += v;\
        \ lazy[2*node+1] += v\n            treeMin[2*node+2] += v; treeMax[2*node+2]\
        \ += v; lazy[2*node+2] += v\n            lazy[node] = 0\n        }\n       \
        \ mid := (start + end) >> 1\n        update(2*node+1, start, mid, qL, qR, val)\n\
        \        update(2*node+2, mid+1, end, qL, qR, val)\n        treeMin[node] =\
        \ treeMin[2*node+1]; if treeMin[2*node+2] < treeMin[node] { treeMin[node] =\
        \ treeMin[2*node+2] }\n        treeMax[node] = treeMax[2*node+1]; if treeMax[2*node+2]\
        \ > treeMax[node] { treeMax[node] = treeMax[2*node+2] }\n    }\n\n    var findMax\
        \ func(int, int, int, int, int) int\n    findMax = func(node, start, end, qL,\
        \ qR int) int {\n        if qL > end || qR < start || treeMin[node] > 0 || treeMax[node]\
        \ < 0 { return -1 }\n        if start == end { return start }\n        if lazy[node]\
        \ != 0 {\n            v := lazy[node]\n            treeMin[2*node+1] += v; treeMax[2*node+1]\
        \ += v; lazy[2*node+1] += v\n            treeMin[2*node+2] += v; treeMax[2*node+2]\
        \ += v; lazy[2*node+2] += v\n            lazy[node] = 0\n        }\n       \
        \ mid := (start + end) >> 1\n        res := findMax(2*node+2, mid+1, end, qL,\
        \ qR)\n        if res == -1 { res = findMax(2*node+1, start, mid, qL, qR) }\n\
        \        return res\n    }\n\n    firstOcc := make([]int, 100001)\n    for i\
        \ := range firstOcc { firstOcc[i] = -1 }\n    for i := 0; i < n; i++ {\n   \
        \     if firstOcc[nums[i]] == -1 {\n            firstOcc[nums[i]] = i\n    \
        \        sign := 1; if nums[i]%2 == 0 { sign = -1 }\n            update(0, 0,\
        \ n-1, i, n-1, sign)\n        }\n    }\n\n    ans := 0\n    for l := 0; l <\
        \ n; l++ {\n        r := findMax(0, 0, n-1, l, n-1)\n        if r != -1 {\n\
        \            len := r - l + 1\n            if len > ans { ans = len }\n    \
        \    }\n        sign := 1; if nums[l]%2 == 0 { sign = -1 }\n        update(0,\
        \ 0, n-1, l, nextIdx[l]-1, -sign)\n    }\n    return ans\n}"
      ruby: "def longest_balanced(nums)\n  n = nums.length\n  next_occ = Array.new(n,\
        \ n)\n  last_pos = Array.new(100001, n)\n  (n - 1).downto(0) do |i|\n    next_occ[i]\
        \ = last_pos[nums[i]]\n    last_pos[nums[i]] = i\n  end\n\n  first_occ = Array.new(100001,\
        \ -1)\n  nums.each_with_index { |v, i| first_occ[v] = i if first_occ[v] == -1\
        \ }\n\n  @tree_min = Array.new(4 * n, 0)\n  @tree_max = Array.new(4 * n, 0)\n\
        \  @tree_lazy = Array.new(4 * n, 0)\n\n  def push(v)\n    if @tree_lazy[v] !=\
        \ 0\n      lazy = @tree_lazy[v]\n      v2, v21 = 2 * v, 2 * v + 1\n      @tree_min[v2]\
        \ += lazy; @tree_max[v2] += lazy; @tree_lazy[v2] += lazy\n      @tree_min[v21]\
        \ += lazy; @tree_max[v21] += lazy; @tree_lazy[v21] += lazy\n      @tree_lazy[v]\
        \ = 0\n    end\n  end\n\n  def update(v, tl, tr, l, r, add)\n    return if l\
        \ > r\n    if l == tl && r == tr\n      @tree_min[v] += add; @tree_max[v] +=\
        \ add; @tree_lazy[v] += add\n    else\n      push(v)\n      tm = (tl + tr) /\
        \ 2\n      update(2 * v, tl, tm, l, r < tm ? r : tm, add)\n      update(2 *\
        \ v + 1, tm + 1, tr, l > tm + 1 ? l : tm + 1, r, add)\n      v2, v21 = 2 * v,\
        \ 2 * v + 1\n      @tree_min[v] = @tree_min[v2] < @tree_min[v21] ? @tree_min[v2]\
        \ : @tree_min[v21]\n      @tree_max[v] = @tree_max[v2] > @tree_max[v21] ? @tree_max[v2]\
        \ : @tree_max[v21]\n    end\n  end\n\n  def find_last_zero(v, tl, tr, l, r)\n\
        \    return -1 if l > tr || r < tl || @tree_min[v] > 0 || @tree_max[v] < 0\n\
        \    return tl if tl == tr\n    push(v)\n    tm = (tl + tr) / 2\n    res = find_last_zero(2\
        \ * v + 1, tm + 1, tr, l, r)\n    res = find_last_zero(2 * v, tl, tm, l, r)\
        \ if res == -1\n    res\n  end\n\n  (1..100000).each do |v|\n    if first_occ[v]\
        \ != -1\n      sign = (v % 2 == 1 ? 1 : -1)\n      update(1, 0, n - 1, first_occ[v],\
        \ n - 1, sign)\n    end\n  end\n\n  ans = 0\n  (0...n).each do |l|\n    r =\
        \ find_last_zero(1, 0, n - 1, l, n - 1)\n    ans = [ans, r - l + 1].max if r\
        \ != -1\n    sign = (nums[l] % 2 == 1 ? 1 : -1)\n    update(1, 0, n - 1, l,\
        \ next_occ[l] - 1, -sign)\n  end\n  ans\nend"
      scala: "object Solution {\n    def longestBalanced(nums: Array[Int]): Int = {\n\
        \        val n = nums.length\n        val next_occ = Array.fill(n)(n)\n    \
        \    val last_pos = Array.fill(100001)(n)\n        for (i <- n - 1 to 0 by -1)\
        \ {\n            next_occ(i) = last_pos(nums(i))\n            last_pos(nums(i))\
        \ = i\n        }\n        val first_occ = Array.fill(100001)(-1)\n        for\
        \ (i <- 0 until n) {\n            if (first_occ(nums(i)) == -1) first_occ(nums(i))\
        \ = i\n        }\n\n        val tree_min = Array.fill(4 * n)(0)\n        val\
        \ tree_max = Array.fill(4 * n)(0)\n        val tree_lazy = Array.fill(4 * n)(0)\n\
        \n        def push(v: Int): Unit = {\n            if (tree_lazy(v) != 0) {\n\
        \                val lazyVal = tree_lazy(v)\n                val v2 = 2 * v\n\
        \                val v21 = 2 * v + 1\n                tree_min(v2) += lazyVal;\
        \ tree_max(v2) += lazyVal; tree_lazy(v2) += lazyVal\n                tree_min(v21)\
        \ += lazyVal; tree_max(v21) += lazyVal; tree_lazy(v21) += lazyVal\n        \
        \        tree_lazy(v) = 0\n            }\n        }\n\n        def update(v:\
        \ Int, tl: Int, tr: Int, l: Int, r: Int, add: Int): Unit = {\n            if\
        \ (l > r) return\n            if (l == tl && r == tr) {\n                tree_min(v)\
        \ += add; tree_max(v) += add; tree_lazy(v) += add\n            } else {\n  \
        \              push(v)\n                val tm = (tl + tr) / 2\n           \
        \     update(2 * v, tl, tm, l, math.min(r, tm), add)\n                update(2\
        \ * v + 1, tm + 1, tr, math.max(l, tm + 1), r, add)\n                tree_min(v)\
        \ = math.min(tree_min(2 * v), tree_min(2 * v + 1))\n                tree_max(v)\
        \ = math.max(tree_max(2 * v), tree_max(2 * v + 1))\n            }\n        }\n\
        \n        def findLastZero(v: Int, tl: Int, tr: Int, l: Int, r: Int): Int =\
        \ {\n            if (l > r || tree_min(v) > 0 || tree_max(v) < 0) return -1\n\
        \            if (tl == tr) return tl\n            push(v)\n            val tm\
        \ = (tl + tr) / 2\n            var res = findLastZero(2 * v + 1, tm + 1, tr,\
        \ math.max(l, tm + 1), r)\n            if (res == -1) res = findLastZero(2 *\
        \ v, tl, tm, l, math.min(r, tm))\n            res\n        }\n\n        for\
        \ (v <- 1 to 100000) {\n            if (first_occ(v) != -1) {\n            \
        \    val sign = if (v % 2 == 1) 1 else -1\n                update(1, 0, n -\
        \ 1, first_occ(v), n - 1, sign)\n            }\n        }\n\n        var ans\
        \ = 0\n        for (l <- 0 until n) {\n            val r = findLastZero(1, 0,\
        \ n - 1, l, n - 1)\n            if (r != -1) ans = math.max(ans, r - l + 1)\n\
        \            val sign = if (nums(l) % 2 == 1) 1 else -1\n            update(1,\
        \ 0, n - 1, l, next_occ(l) - 1, -sign)\n        }\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn longest_balanced(nums: Vec<i32>) -> i32 {\n\
        \        let n = nums.len();\n        let mut next_occ = vec![n; n];\n     \
        \   let mut last_pos = vec![n; 100001];\n        for i in (0..n).rev() {\n \
        \           next_occ[i] = last_pos[nums[i] as usize];\n            last_pos[nums[i]\
        \ as usize] = i;\n        }\n        let mut first_occ = vec![n; 100001];\n\
        \        for i in 0..n {\n            if first_occ[nums[i] as usize] == n {\n\
        \                first_occ[nums[i] as usize] = i;\n            }\n        }\n\
        \n        let mut tree_min = vec![0; 4 * n + 1];\n        let mut tree_max =\
        \ vec![0; 4 * n + 1];\n        let mut tree_lazy = vec![0; 4 * n + 1];\n\n \
        \       fn push(v: usize, tree_min: &mut Vec<i32>, tree_max: &mut Vec<i32>,\
        \ tree_lazy: &mut Vec<i32>) {\n            if tree_lazy[v] != 0 {\n        \
        \        let lazy = tree_lazy[v];\n                tree_min[2 * v] += lazy;\
        \ tree_max[2 * v] += lazy; tree_lazy[2 * v] += lazy;\n                tree_min[2\
        \ * v + 1] += lazy; tree_max[2 * v + 1] += lazy; tree_lazy[2 * v + 1] += lazy;\n\
        \                tree_lazy[v] = 0;\n            }\n        }\n\n        fn update(v:\
        \ usize, tl: usize, tr: usize, l: usize, r: usize, add: i32, tree_min: &mut\
        \ Vec<i32>, tree_max: &mut Vec<i32>, tree_lazy: &mut Vec<i32>) {\n         \
        \   if l > r { return; }\n            if l == tl && r == tr {\n            \
        \    tree_min[v] += add; tree_max[v] += add; tree_lazy[v] += add;\n        \
        \    } else {\n                push(v, tree_min, tree_max, tree_lazy);\n   \
        \             let tm = (tl + tr) / 2;\n                update(2 * v, tl, tm,\
        \ l, std::cmp::min(r, tm), add, tree_min, tree_max, tree_lazy);\n          \
        \      update(2 * v + 1, tm + 1, tr, std::cmp::max(l, tm + 1), r, add, tree_min,\
        \ tree_max, tree_lazy);\n                tree_min[v] = std::cmp::min(tree_min[2\
        \ * v], tree_min[2 * v + 1]);\n                tree_max[v] = std::cmp::max(tree_max[2\
        \ * v], tree_max[2 * v + 1]);\n            }\n        }\n\n        fn find_last_zero(v:\
        \ usize, tl: usize, tr: usize, l: usize, r: usize, tree_min: &mut Vec<i32>,\
        \ tree_max: &mut Vec<i32>, tree_lazy: &mut Vec<i32>) -> i32 {\n            if\
        \ l > r || tree_min[v] > 0 || tree_max[v] < 0 { return -1; }\n            if\
        \ tl == tr { return tl as i32; }\n            push(v, tree_min, tree_max, tree_lazy);\n\
        \            let tm = (tl + tr) / 2;\n            let mut res = find_last_zero(2\
        \ * v + 1, tm + 1, tr, std::cmp::max(l, tm + 1), r, tree_min, tree_max, tree_lazy);\n\
        \            if res == -1 { res = find_last_zero(2 * v, tl, tm, l, std::cmp::min(r,\
        \ tm), tree_min, tree_max, tree_lazy); }\n            res\n        }\n\n   \
        \     for v in 1..100001 {\n            if first_occ[v] != n {\n           \
        \     let sign = if v % 2 == 1 { 1 } else { -1 };\n                update(1,\
        \ 0, n - 1, first_occ[v], n - 1, sign, &mut tree_min, &mut tree_max, &mut tree_lazy);\n\
        \            }\n        }\n\n        let mut ans = 0;\n        for l in 0..n\
        \ {\n            let r = find_last_zero(1, 0, n - 1, l, n - 1, &mut tree_min,\
        \ &mut tree_max, &mut tree_lazy);\n            if r != -1 { ans = std::cmp::max(ans,\
        \ r - l as i32 + 1); }\n            let sign = if nums[l] % 2 == 1 { 1 } else\
        \ { -1 };\n            update(1, 0, n - 1, l, next_occ[l] - 1, -sign, &mut tree_min,\
        \ &mut tree_max, &mut tree_lazy);\n        }\n        ans\n    }\n}"
      racket: "(define/contract (longest-balanced nums-list)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let* ([nums (list->vector nums-list)]\n         [n (vector-length\
        \ nums)]\n         [next-occ (make-vector n n)]\n         [last-pos (make-vector\
        \ 100001 n)]\n         [tree-min (make-vector (* 4 n) 0)]\n         [tree-max\
        \ (make-vector (* 4 n) 0)]\n         [tree-lazy (make-vector (* 4 n) 0)])\n\
        \    (for ([i (in-range (- n 1) -1 -1)])\n      (let ([v (vector-ref nums i)])\n\
        \        (vector-set! next-occ i (vector-ref last-pos v))\n        (vector-set!\
        \ last-pos v i)))\n    (define first-occ (make-vector 100001 -1))\n    (for\
        \ ([i (in-range n)])\n      (let ([v (vector-ref nums i)])\n        (when (=\
        \ (vector-ref first-occ v) -1) (vector-set! first-occ v i))))\n    (define (push\
        \ v)\n      (let ([lazy (vector-ref tree-lazy v)])\n        (when (not (= lazy\
        \ 0))\n          (let ([v2 (* 2 v)] [v21 (+ (* 2 v) 1)])\n            (vector-set!\
        \ tree-min v2 (+ (vector-ref tree-min v2) lazy))\n            (vector-set! tree-max\
        \ v2 (+ (vector-ref tree-max v2) lazy))\n            (vector-set! tree-lazy\
        \ v2 (+ (vector-ref tree-lazy v2) lazy))\n            (vector-set! tree-min\
        \ v21 (+ (vector-ref tree-min v21) lazy))\n            (vector-set! tree-max\
        \ v21 (+ (vector-ref tree-max v21) lazy))\n            (vector-set! tree-lazy\
        \ v21 (+ (vector-ref tree-lazy v21) lazy))\n            (vector-set! tree-lazy\
        \ v 0)))))\n    (define (update v tl tr l r add)\n      (if (> l r) (void)\n\
        \          (if (and (= l tl) (= r tr))\n              (begin\n             \
        \   (vector-set! tree-min v (+ (vector-ref tree-min v) add))\n             \
        \   (vector-set! tree-max v (+ (vector-ref tree-max v) add))\n             \
        \   (vector-set! tree-lazy v (+ (vector-ref tree-lazy v) add)))\n          \
        \    (begin\n                (push v)\n                (let* ([tm (quotient\
        \ (+ tl tr) 2)] [v2 (* 2 v)] [v21 (+ v2 1)])\n                  (update v2 tl\
        \ tm l (min r tm) add)\n                  (update v21 (+ tm 1) tr (max l (+\
        \ tm 1)) r add)\n                  (vector-set! tree-min v (min (vector-ref\
        \ tree-min v2) (vector-ref tree-min v21)))\n                  (vector-set! tree-max\
        \ v (max (vector-ref tree-max v2) (vector-ref tree-max v21))))))))\n    (define\
        \ (find-last-zero v tl tr l r)\n      (if (or (> l r) (> (vector-ref tree-min\
        \ v) 0) (< (vector-ref tree-max v) 0)) -1\n          (if (= tl tr) tl\n    \
        \          (begin\n                (push v)\n                (let* ([tm (quotient\
        \ (+ tl tr) 2)] [v2 (* 2 v)] [v21 (+ v2 1)])\n                  (let ([res (find-last-zero\
        \ v21 (+ tm 1) tr (max l (+ tm 1)) r)])\n                    (if (= res -1)\
        \ (find-last-zero v2 tl tm l (min r tm)) res)))))))\n    (for ([v (in-range\
        \ 1 100001)])\n      (let ([p (vector-ref first-occ v)])\n        (when (not\
        \ (= p -1))\n          (let ([sign (if (odd? v) 1 -1)]) (update 1 0 (- n 1)\
        \ p (- n 1) sign)))))\n    (let ([ans 0])\n      (for ([l (in-range n)])\n \
        \       (let ([r (find-last-zero 1 0 (- n 1) l (- n 1))])\n          (when (not\
        \ (= r -1)) (set! ans (max ans (+ (- r l) 1))))\n          (let ([sign (if (odd?\
        \ (vector-ref nums l)) 1 -1)])\n            (update 1 0 (- n 1) l (- (vector-ref\
        \ next-occ l) 1) (- sign)))))\n      ans)))"
      erlang: "-spec longest_balanced(Nums :: [integer()]) -> integer().\nlongest_balanced(Nums)\
        \ ->\n  N = length(Nums),\n  NumsTuple = list_to_tuple(Nums),\n  {NextOccList,\
        \ _} = lists:foldr(fun({Num, Index}, {AccNext, AccLast}) ->\n    Next = maps:get(Num,\
        \ AccLast, N),\n    {[Next | AccNext], maps:put(Num, Index, AccLast)}\n  end,\
        \ {[], #{}}, lists:zip(Nums, lists:seq(0, N-1))),\n  NextOccTuple = list_to_tuple(NextOccList),\n\
        \  FirstOccs = maps:to_list(lists:foldl(fun({Num, Index}, Acc) ->\n    case\
        \ maps:is_key(Num, Acc) of true -> Acc; false -> maps:put(Num, Index, Acc) end\n\
        \  end, #{}, lists:zip(Nums, lists:seq(0, N-1)))),\n  Tree1 = build(0, N-1),\n\
        \  Tree2 = lists:foldl(fun({Num, Index}, T) ->\n    Sign = if Num rem 2 == 1\
        \ -> 1; true -> -1 end,\n    update(0, N-1, Index, N-1, Sign, T)\n  end, Tree1,\
        \ FirstOccs),\n  solve(0, N, NumsTuple, NextOccTuple, Tree2, 0).\n\nbuild(TL,\
        \ TR) when TL == TR -> {0, 0, 0, nil, nil};\nbuild(TL, TR) -> TM = (TL + TR)\
        \ div 2, {0, 0, 0, build(TL, TM), build(TM + 1, TR)}.\n\npush(Node, 0) -> Node;\n\
        push({Min, Max, Lazy, L, R}, Add) -> {Min + Add, Max + Add, Lazy + Add, L, R}.\n\
        \nupdate(TL, TR, L, R, Add, {Min, Max, Lazy, Left, Right}) ->\n  if (L > TR)\
        \ or (R < TL) -> {Min, Max, Lazy, Left, Right};\n     (L =< TL) and (TR =< R)\
        \ -> {Min + Add, Max + Add, Lazy + Add, Left, Right};\n     true -> TM = (TL\
        \ + TR) div 2, L1 = push(Left, Lazy), R1 = push(Right, Lazy),\n            \
        \ NL = update(TL, TM, L, R, Add, L1), NR = update(TM + 1, TR, L, R, Add, R1),\n\
        \             {LMin, LMax, _, _, _} = NL, {RMin, RMax, _, _, _} = NR,\n    \
        \         {erlang:min(LMin, RMin), erlang:max(LMax, RMax), 0, NL, NR}\n  end.\n\
        \nfind_last(TL, TR, L, R, {Min, Max, Lazy, Left, Right}) ->\n  if (L > TR) or\
        \ (R < TL) or (Min > 0) or (Max < 0) -> -1;\n     TL == TR -> TL;\n     true\
        \ -> TM = (TL + TR) div 2, Res = find_last(TM + 1, TR, L, R, push(Right, Lazy)),\n\
        \             if Res == -1 -> find_last(TL, TM, L, R, push(Left, Lazy)); true\
        \ -> Res end\n  end.\n\nsolve(L, N, _, _, _, Ans) when L == N -> Ans;\nsolve(L,\
        \ N, Nums, Nexts, Tree, Ans) ->\n  R = find_last(0, N-1, L, N-1, Tree),\n  NewAns\
        \ = if R == -1 -> Ans; true -> erlang:max(Ans, R - L + 1) end,\n  Val = element(L\
        \ + 1, Nums), Next = element(L + 1, Nexts),\n  Sign = if Val rem 2 == 1 -> 1;\
        \ true -> -1 end,\n  NewTree = update(0, N-1, L, Next - 1, -Sign, Tree),\n \
        \ solve(L + 1, N, Nums, Nexts, NewTree, NewAns)."
      elixir: "defmodule Solution do\n  def longest_balanced(nums) do\n    n = length(nums)\n\
        \    nums_tuple = List.to_tuple(nums)\n    {next_occ_list, _} = Enum.reduce(Enum.zip(nums,\
        \ 0..n-1) |> Enum.reverse(), {[], %{}}, fn {num, index}, {acc_next, acc_last}\
        \ ->\n      next = Map.get(acc_last, num, n)\n      {[next | acc_next], Map.put(acc_last,\
        \ num, index)}\n    end)\n    next_occ_tuple = List.to_tuple(next_occ_list)\n\
        \    first_occs = Enum.reduce(Enum.zip(nums, 0..n-1), %{}, fn {num, index},\
        \ acc ->\n      if Map.has_key?(acc, num), do: acc, else: Map.put(acc, num,\
        \ index)\n    end) |> Map.to_list()\n    tree = build(0, n-1)\n    tree = Enum.reduce(first_occs,\
        \ tree, fn {num, index}, t ->\n      sign = if rem(num, 2) == 1, do: 1, else:\
        \ -1\n      update(0, n-1, index, n-1, sign, t)\n    end)\n    solve(0, n, nums_tuple,\
        \ next_occ_tuple, tree, 0)\n  end\n\n  defp solve(l, n, _, _, _, ans) when l\
        \ == n, do: ans\n  defp solve(l, n, nums, nexts, tree, ans) do\n    r = find_last(0,\
        \ n-1, l, n-1, tree)\n    new_ans = if r == -1, do: ans, else: max(ans, r -\
        \ l + 1)\n    val = elem(nums, l)\n    next = elem(nexts, l)\n    sign = if\
        \ rem(val, 2) == 1, do: 1, else: -1\n    new_tree = update(0, n-1, l, next -\
        \ 1, -sign, tree)\n    solve(l + 1, n, nums, nexts, new_tree, new_ans)\n  end\n\
        \n  defp build(tl, tr) when tl == tr, do: {0, 0, 0, nil, nil}\n  defp build(tl,\
        \ tr) do\n    tm = div(tl + tr, 2)\n    {0, 0, 0, build(tl, tm), build(tm +\
        \ 1, tr)}\n  end\n\n  defp push(node, 0), do: node\n  defp push({min, max, lazy,\
        \ l, r}, add), do: {min + add, max + add, lazy + add, l, r}\n\n  defp update(tl,\
        \ tr, l, r, add, {min, max, lazy, left, right}) do\n    cond do\n      l > tr\
        \ or r < tl -> {min, max, lazy, left, right}\n      l <= tl and tr <= r -> {min\
        \ + add, max + add, lazy + add, left, right}\n      true ->\n        tm = div(tl\
        \ + tr, 2)\n        nl = update(tl, tm, l, r, add, push(left, lazy))\n     \
        \   nr = update(tm + 1, tr, l, r, add, push(right, lazy))\n        {lmin, lmax,\
        \ _, _, _} = nl\n        {rmin, rmax, _, _, _} = nr\n        {min(lmin, rmin),\
        \ max(lmax, rmax), 0, nl, nr}\n    end\n  end\n\n  defp find_last(tl, tr, l,\
        \ r, {min, max, lazy, left, right}) do\n    if l > tr or r < tl or min > 0 or\
        \ max < 0 do\n      -1\n    else\n      if tl == tr do\n        tl\n      else\n\
        \        tm = div(tl + tr, 2)\n        res = find_last(tm + 1, tr, l, r, push(right,\
        \ lazy))\n        if res == -1, do: find_last(tl, tm, l, r, push(left, lazy)),\
        \ else: res\n      end\n    end\n  end\nend"
    approach: 'We need to find the longest subarray where the number of distinct even
      numbers equals the number of distinct odd numbers. This problem can be modeled
      by assigning a sign to each distinct value: -1 for even and +1 for odd. A subarray
      $nums[l..r]$ is balanced if the sum of these signs for all distinct values in
      the subarray is exactly zero. We use a segment tree that stores the cumulative
      sign sum at each index $r$ for a fixed starting index $l$. By iterating $l$ from
      $0$ to $n-1$, we maintain this segment tree and query it for the largest index
      $r \ge l$ where the cumulative sum is zero, updating our answer with $r - l +
      1$.'
    time_complexity: O(N log N) where N is the length of the array. The segment tree
      is initialized in O(N log N) time, and we perform N queries and N updates, each
      taking O(log N) time. Mapping unique values to their occurrences also takes O(N)
      time.
    space_complexity: O(N + V) where N is the length of the array and V is the maximum
      value in nums (up to 10^5). This space is used to store the segment tree nodes,
      the positions of each number, and their associated signs.
    elapsed_time: 419.1355016231537
    model: gemini-3-flash-preview
    generated_at: '2026-02-11 01:53:35 '
---

## Problem #3721: Longest Balanced Subarray II

**Difficulty:** Hard

**Topics:** Array, Hash Table, Divide and Conquer, Segment Tree, Prefix Sum

## Problem Description

<p>You are given an integer array <code>nums</code>.</p>

<p>A <strong><span data-keyword="subarray-nonempty">subarray</span></strong> is called <strong>balanced</strong> if the number of <strong>distinct even</strong> numbers in the subarray is equal to the number of <strong>distinct odd</strong> numbers.</p>

<p>Return the length of the <strong>longest</strong> balanced subarray.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,5,4,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The longest balanced subarray is <code>[2, 5, 4, 3]</code>.</li>
	<li>It has 2 distinct even numbers <code>[2, 4]</code> and 2 distinct odd numbers <code>[5, 3]</code>. Thus, the answer is 4.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,2,2,5,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The longest balanced subarray is <code>[3, 2, 2, 5, 4]</code>.</li>
	<li>It has 2 distinct even numbers <code>[2, 4]</code> and 2 distinct odd numbers <code>[3, 5]</code>. Thus, the answer is 5.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The longest balanced subarray is <code>[2, 3, 2]</code>.</li>
	<li>It has 1 distinct even number <code>[2]</code> and 1 distinct odd number <code>[3]</code>. Thus, the answer is 3.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Store the first (or all) occurrences for each value in `pos[val]`.

2. Build a lazy segment tree over start indices `l in [0..n-1]` that supports range add and can tell if any index has value `0` (keep `mn`/`mx`).

3. Use `sign = +1` for odd values and `sign = -1` for even values.

4. Initialize by adding each value's contribution with `update(p, n-1, sign)` where `p` is its current first occurrence.

5. Slide left `l`: pop `pos[nums[l]]`, let `next` = next occurrence or `n`, do `update(0, next-1, -sign)`, then query for any `r >= l` with value `0` and update `ans = max(ans, r-l+1)`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

We need to find the longest subarray where the number of distinct even numbers equals the number of distinct odd numbers. This problem can be modeled by assigning a sign to each distinct value: -1 for even and +1 for odd. A subarray $nums[l..r]$ is balanced if the sum of these signs for all distinct values in the subarray is exactly zero. We use a segment tree that stores the cumulative sign sum at each index $r$ for a fixed starting index $l$. By iterating $l$ from $0$ to $n-1$, we maintain this segment tree and query it for the largest index $r \ge l$ where the cumulative sum is zero, updating our answer with $r - l + 1$.

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
    int tree_min[400005], tree_max[400005], tree_lazy[400005];
    void push_down(int v) {
        if (tree_lazy[v] != 0) {
            int lz = tree_lazy[v];
            tree_min[2 * v] += lz; tree_max[2 * v] += lz; tree_lazy[2 * v] += lz;
            tree_min[2 * v + 1] += lz; tree_max[2 * v + 1] += lz; tree_lazy[2 * v + 1] += lz;
            tree_lazy[v] = 0;
        }
    }
    void update(int v, int tl, int tr, int l, int r, int add) {
        if (l > r) return;
        if (l == tl && r == tr) {
            tree_min[v] += add; tree_max[v] += add; tree_lazy[v] += add;
        } else {
            push_down(v);
            int tm = (tl + tr) / 2;
            update(2 * v, tl, tm, l, std::min(r, tm), add);
            update(2 * v + 1, tm + 1, tr, std::max(l, tm + 1), r, add);
            tree_min[v] = std::min(tree_min[2 * v], tree_min[2 * v + 1]);
            tree_max[v] = std::max(tree_max[2 * v], tree_max[2 * v + 1]);
        }
    }
    int find_last(int v, int tl, int tr, int l, int r) {
        if (l > tr || r < tl || tree_min[v] > 0 || tree_max[v] < 0) return -1;
        if (tl == tr) return tl;
        push_down(v);
        int tm = (tl + tr) / 2;
        int res = find_last(2 * v + 1, tm + 1, tr, l, r);
        if (res == -1) res = find_last(2 * v, tl, tm, l, r);
        return res;
    }
public:
    int longestBalanced(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> pos[100001];
        for (int i = 0; i < n; i++) pos[nums[i]].push_back(i);
        std::fill(tree_min, tree_min + 4 * n + 1, 0);
        std::fill(tree_max, tree_max + 4 * n + 1, 0);
        std::fill(tree_lazy, tree_lazy + 4 * n + 1, 0);
        int sign[100001];
        for (int i = 0; i < 100001; i++) sign[i] = (i % 2 == 0) ? -1 : 1;
        for (int i = 0; i < 100001; i++) {
            if (!pos[i].empty()) update(1, 0, n - 1, pos[i][0], n - 1, sign[i]);
        }
        int ans = 0;
        std::vector<int> curr_idx(100001, 0);
        for (int l = 0; l < n; l++) {
            int r = find_last(1, 0, n - 1, l, n - 1);
            if (r != -1) ans = std::max(ans, r - l + 1);
            int v = nums[l];
            int next_p = (curr_idx[v] + 1 < pos[v].size()) ? pos[v][curr_idx[v] + 1] : n;
            update(1, 0, n - 1, 0, next_p - 1, -sign[v]);
            curr_idx[v]++;
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
    int[] treeMin, treeMax, treeLazy;
    private void pushDown(int v) {
        if (treeLazy[v] != 0) {
            int lz = treeLazy[v];
            treeMin[2 * v] += lz; treeMax[2 * v] += lz; treeLazy[2 * v] += lz;
            treeMin[2 * v + 1] += lz; treeMax[2 * v + 1] += lz; treeLazy[2 * v + 1] += lz;
            treeLazy[v] = 0;
        }
    }
    private void update(int v, int tl, int tr, int l, int r, int add) {
        if (l > r) return;
        if (l == tl && r == tr) {
            treeMin[v] += add; treeMax[v] += add; treeLazy[v] += add;
        } else {
            pushDown(v);
            int tm = (tl + tr) / 2;
            update(2 * v, tl, tm, l, Math.min(r, tm), add);
            update(2 * v + 1, tm + 1, tr, Math.max(l, tm + 1), r, add);
            treeMin[v] = Math.min(treeMin[2 * v], treeMin[2 * v + 1]);
            treeMax[v] = Math.max(treeMax[2 * v], treeMax[2 * v + 1]);
        }
    }
    private int findLast(int v, int tl, int tr, int l, int r) {
        if (l > tr || r < tl || treeMin[v] > 0 || treeMax[v] < 0) return -1;
        if (tl == tr) return tl;
        pushDown(v);
        int tm = (tl + tr) / 2;
        int res = findLast(2 * v + 1, tm + 1, tr, l, r);
        if (res == -1) res = findLast(2 * v, tl, tm, l, r);
        return res;
    }
    public int longestBalanced(int[] nums) {
        int n = nums.length;
        treeMin = new int[4 * n + 1];
        treeMax = new int[4 * n + 1];
        treeLazy = new int[4 * n + 1];
        List<Integer>[] pos = new ArrayList[100001];
        for (int i = 0; i < 100001; i++) pos[i] = new ArrayList<>();
        for (int i = 0; i < n; i++) pos[nums[i]].add(i);
        int[] sign = new int[100001];
        for (int i = 0; i < 100001; i++) sign[i] = (i % 2 == 0) ? -1 : 1;
        for (int i = 0; i < 100001; i++) {
            if (!pos[i].isEmpty()) update(1, 0, n - 1, pos[i].get(0), n - 1, sign[i]);
        }
        int ans = 0;
        int[] currIdx = new int[100001];
        for (int l = 0; l < n; l++) {
            int r = findLast(1, 0, n - 1, l, n - 1);
            if (r != -1) ans = Math.max(ans, r - l + 1);
            int v = nums[l];
            int nextP = (currIdx[v] + 1 < pos[v].size()) ? pos[v].get(currIdx[v] + 1) : n;
            update(1, 0, n - 1, 0, nextP - 1, -sign[v]);
            currIdx[v]++;
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
    def longestBalanced(self, nums):
        n = len(nums)
        tree_min = [0] * (4 * n + 1)
        tree_max = [0] * (4 * n + 1)
        tree_lazy = [0] * (4 * n + 1)

        def update(v, tl, tr, l, r, add):
            if l <= tl and tr <= r:
                tree_min[v] += add
                tree_max[v] += add
                tree_lazy[v] += add
                return
            lz = tree_lazy[v]
            if lz:
                v2, v21 = v << 1, (v << 1) | 1
                tree_min[v2] += lz; tree_max[v2] += lz; tree_lazy[v2] += lz
                tree_min[v21] += lz; tree_max[v21] += lz; tree_lazy[v21] += lz
                tree_lazy[v] = 0
            tm = (tl + tr) >> 1
            if l <= tm: update(v << 1, tl, tm, l, r, add)
            if r > tm: update((v << 1) | 1, tm + 1, tr, l, r, add)
            tree_min[v] = min(tree_min[v << 1], tree_min[(v << 1) | 1])
            tree_max[v] = max(tree_max[v << 1], tree_max[(v << 1) | 1])

        def find_last(v, tl, tr, l, r):
            if l > tr or r < tl or tree_min[v] > 0 or tree_max[v] < 0:
                return -1
            if tl == tr: return tl
            lz = tree_lazy[v]
            if lz:
                v2, v21 = v << 1, (v << 1) | 1
                tree_min[v2] += lz; tree_max[v2] += lz; tree_lazy[v2] += lz
                tree_min[v21] += lz; tree_max[v21] += lz; tree_lazy[v21] += lz
                tree_lazy[v] = 0
            tm = (tl + tr) >> 1
            res = find_last((v << 1) | 1, tm + 1, tr, l, r)
            if res == -1: res = find_last(v << 1, tl, tm, l, r)
            return res

        pos = [[] for _ in range(100001)]
        for i, val in enumerate(nums): pos[val].append(i)
        sign = [-1 if i % 2 == 0 else 1 for i in range(100001)]
        for i in range(100001):
            if pos[i]: update(1, 0, n - 1, pos[i][0], n - 1, sign[i])

        ans, curr_idx = 0, [0] * 100001
        for l in range(n):
            r = find_last(1, 0, n - 1, l, n - 1)
            if r != -1: ans = max(ans, r - l + 1)
            v = nums[l]
            next_p = pos[v][curr_idx[v] + 1] if curr_idx[v] + 1 < len(pos[v]) else n
            update(1, 0, n - 1, 0, next_p - 1, -sign[v])
            curr_idx[v] += 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        tree_min = [0] * (4 * n + 1)
        tree_max = [0] * (4 * n + 1)
        tree_lazy = [0] * (4 * n + 1)

        def update(v, tl, tr, l, r, add):
            if l <= tl and tr <= r:
                tree_min[v] += add
                tree_max[v] += add
                tree_lazy[v] += add
                return
            lz = tree_lazy[v]
            if lz:
                v2, v21 = v << 1, (v << 1) | 1
                tree_min[v2] += lz; tree_max[v2] += lz; tree_lazy[v2] += lz
                tree_min[v21] += lz; tree_max[v21] += lz; tree_lazy[v21] += lz
                tree_lazy[v] = 0
            tm = (tl + tr) >> 1
            if l <= tm: update(v << 1, tl, tm, l, r, add)
            if r > tm: update((v << 1) | 1, tm + 1, tr, l, r, add)
            tree_min[v] = min(tree_min[v << 1], tree_min[(v << 1) | 1])
            tree_max[v] = max(tree_max[v << 1], tree_max[(v << 1) | 1])

        def find_last(v, tl, tr, l, r):
            if l > tr or r < tl or tree_min[v] > 0 or tree_max[v] < 0:
                return -1
            if tl == tr: return tl
            lz = tree_lazy[v]
            if lz:
                v2, v21 = v << 1, (v << 1) | 1
                tree_min[v2] += lz; tree_max[v2] += lz; tree_lazy[v2] += lz
                tree_min[v21] += lz; tree_max[v21] += lz; tree_lazy[v21] += lz
                tree_lazy[v] = 0
            tm = (tl + tr) >> 1
            res = find_last((v << 1) | 1, tm + 1, tr, l, r)
            if res == -1: res = find_last(v << 1, tl, tm, l, r)
            return res

        pos = [[] for _ in range(100001)]
        for i, val in enumerate(nums): pos[val].append(i)
        sign = [-1 if i % 2 == 0 else 1 for i in range(100001)]
        for i in range(100001):
            if pos[i]: update(1, 0, n - 1, pos[i][0], n - 1, sign[i])

        ans, curr_idx = 0, [0] * 100001
        for l in range(n):
            r = find_last(1, 0, n - 1, l, n - 1)
            if r != -1: ans = max(ans, r - l + 1)
            v = nums[l]
            next_p = pos[v][curr_idx[v] + 1] if curr_idx[v] + 1 < len(pos[v]) else n
            update(1, 0, n - 1, 0, next_p - 1, -sign[v])
            curr_idx[v] += 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int tree_min[400005], tree_max[400005], tree_lazy[400005];

void push_down(int v) {
    if (tree_lazy[v] != 0) {
        int lz = tree_lazy[v];
        tree_min[2 * v] += lz; tree_max[2 * v] += lz; tree_lazy[2 * v] += lz;
        tree_min[2 * v + 1] += lz; tree_max[2 * v + 1] += lz; tree_lazy[2 * v + 1] += lz;
        tree_lazy[v] = 0;
    }
}

void update(int v, int tl, int tr, int l, int r, int add) {
    if (l > r) return;
    if (l == tl && r == tr) {
        tree_min[v] += add; tree_max[v] += add; tree_lazy[v] += add;
    } else {
        push_down(v);
        int tm = (tl + tr) / 2;
        update(2 * v, tl, tm, l, MIN(r, tm), add);
        update(2 * v + 1, tm + 1, tr, MAX(l, tm + 1), r, add);
        tree_min[v] = MIN(tree_min[2 * v], tree_min[2 * v + 1]);
        tree_max[v] = MAX(tree_max[2 * v], tree_max[2 * v + 1]);
    }
}

int find_last(int v, int tl, int tr, int l, int r) {
    if (l > tr || r < tl || tree_min[v] > 0 || tree_max[v] < 0) return -1;
    if (tl == tr) return tl;
    push_down(v);
    int tm = (tl + tr) / 2;
    int res = find_last(2 * v + 1, tm + 1, tr, l, r);
    if (res == -1) res = find_last(2 * v, tl, tm, l, r);
    return res;
}

int longestBalanced(int* nums, int numsSize) {
    memset(tree_min, 0, sizeof(tree_min));
    memset(tree_max, 0, sizeof(tree_max));
    memset(tree_lazy, 0, sizeof(tree_lazy));
    int* head = malloc(100001 * sizeof(int));
    int* next = malloc(numsSize * sizeof(int));
    int* curr = malloc(100001 * sizeof(int));
    for (int i = 0; i < 100001; i++) head[i] = -1;
    for (int i = numsSize - 1; i >= 0; i--) {
        next[i] = head[nums[i]];
        head[nums[i]] = i;
    }
    memcpy(curr, head, 100001 * sizeof(int));
    int sign[100001];
    for (int i = 0; i < 100001; i++) {
        sign[i] = (i % 2 == 0) ? -1 : 1;
        if (head[i] != -1) update(1, 0, numsSize - 1, head[i], numsSize - 1, sign[i]);
    }
    int ans = 0;
    for (int l = 0; l < numsSize; l++) {
        int r = find_last(1, 0, numsSize - 1, l, numsSize - 1);
        if (r != -1) ans = MAX(ans, r - l + 1);
        int v = nums[l];
        int nxt_p = next[curr[v]];
        curr[v] = nxt_p;
        if (nxt_p == -1) nxt_p = numsSize;
        update(1, 0, numsSize - 1, 0, nxt_p - 1, -sign[v]);
    }
    free(head); free(next); free(curr);
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    int[] treeMin, treeMax, treeLazy;
    private void PushDown(int v) {
        if (treeLazy[v] != 0) {
            int lz = treeLazy[v];
            treeMin[2 * v] += lz; treeMax[2 * v] += lz; treeLazy[2 * v] += lz;
            treeMin[2 * v + 1] += lz; treeMax[2 * v + 1] += lz; treeLazy[2 * v + 1] += lz;
            treeLazy[v] = 0;
        }
    }
    private void Update(int v, int tl, int tr, int l, int r, int add) {
        if (l > r) return;
        if (l == tl && r == tr) {
            treeMin[v] += add; treeMax[v] += add; treeLazy[v] += add;
        } else {
            PushDown(v);
            int tm = (tl + tr) / 2;
            Update(2 * v, tl, tm, l, Math.Min(r, tm), add);
            Update(2 * v + 1, tm + 1, tr, Math.Max(l, tm + 1), r, add);
            treeMin[v] = Math.Min(treeMin[2 * v], treeMin[2 * v + 1]);
            treeMax[v] = Math.Max(treeMax[2 * v], treeMax[2 * v + 1]);
        }
    }
    private int FindLast(int v, int tl, int tr, int l, int r) {
        if (l > tr || r < tl || treeMin[v] > 0 || treeMax[v] < 0) return -1;
        if (tl == tr) return tl;
        PushDown(v);
        int tm = (tl + tr) / 2;
        int res = FindLast(2 * v + 1, tm + 1, tr, l, r);
        if (res == -1) res = FindLast(2 * v, tl, tm, l, r);
        return res;
    }
    public int LongestBalanced(int[] nums) {
        int n = nums.Length;
        treeMin = new int[4 * n + 1]; treeMax = new int[4 * n + 1]; treeLazy = new int[4 * n + 1];
        List<int>[] pos = new List<int>[100001];
        for (int i = 0; i < 100001; i++) pos[i] = new List<int>();
        for (int i = 0; i < n; i++) pos[nums[i]].Add(i);
        int[] sign = new int[100001];
        for (int i = 0; i < 100001; i++) sign[i] = (i % 2 == 0) ? -1 : 1;
        for (int i = 0; i < 100001; i++) {
            if (pos[i].Count > 0) Update(1, 0, n - 1, pos[i][0], n - 1, sign[i]);
        }
        int ans = 0;
        int[] currIdx = new int[100001];
        for (int l = 0; l < n; l++) {
            int r = FindLast(1, 0, n - 1, l, n - 1);
            if (r != -1) ans = Math.Max(ans, r - l + 1);
            int v = nums[l];
            int nextP = (currIdx[v] + 1 < pos[v].Count) ? pos[v][currIdx[v] + 1] : n;
            Update(1, 0, n - 1, 0, nextP - 1, -sign[v]);
            currIdx[v]++;
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
 * @param {number[]} nums
 * @return {number}
 */
var longestBalanced = function(nums) {
    let n = nums.length;
    let treeMin = new Int32Array(4 * n + 1);
    let treeMax = new Int32Array(4 * n + 1);
    let treeLazy = new Int32Array(4 * n + 1);

    function pushDown(v) {
        if (treeLazy[v] !== 0) {
            let lz = treeLazy[v];
            treeMin[2 * v] += lz; treeMax[2 * v] += lz; treeLazy[2 * v] += lz;
            treeMin[2 * v + 1] += lz; treeMax[2 * v + 1] += lz; treeLazy[2 * v + 1] += lz;
            treeLazy[v] = 0;
        }
    }

    function update(v, tl, tr, l, r, add) {
        if (l > r) return;
        if (l === tl && r === tr) {
            treeMin[v] += add; treeMax[v] += add; treeLazy[v] += add;
        } else {
            pushDown(v);
            let tm = Math.floor((tl + tr) / 2);
            update(2 * v, tl, tm, l, Math.min(r, tm), add);
            update(2 * v + 1, tm + 1, tr, Math.max(l, tm + 1), r, add);
            treeMin[v] = Math.min(treeMin[2 * v], treeMin[2 * v + 1]);
            treeMax[v] = Math.max(treeMax[2 * v], treeMax[2 * v + 1]);
        }
    }

    function findLast(v, tl, tr, l, r) {
        if (l > tr || r < tl || treeMin[v] > 0 || treeMax[v] < 0) return -1;
        if (tl === tr) return tl;
        pushDown(v);
        let tm = Math.floor((tl + tr) / 2);
        let res = findLast(2 * v + 1, tm + 1, tr, l, r);
        if (res === -1) res = findLast(2 * v, tl, tm, l, r);
        return res;
    }

    let pos = new Array(100001);
    for (let i = 0; i < n; i++) {
        if (!pos[nums[i]]) pos[nums[i]] = [];
        pos[nums[i]].push(i);
    }
    let sign = new Int32Array(100001);
    for (let i = 0; i < 100001; i++) sign[i] = (i % 2 === 0) ? -1 : 1;
    for (let i = 0; i < 100001; i++) {
        if (pos[i]) update(1, 0, n - 1, pos[i][0], n - 1, sign[i]);
    }

    let ans = 0, currIdx = new Int32Array(100001);
    for (let l = 0; l < n; l++) {
        let r = findLast(1, 0, n - 1, l, n - 1);
        if (r !== -1) ans = Math.max(ans, r - l + 1);
        let v = nums[l];
        let nextP = (currIdx[v] + 1 < pos[v].length) ? pos[v][currIdx[v] + 1] : n;
        update(1, 0, n - 1, 0, nextP - 1, -sign[v]);
        currIdx[v]++;
    }
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
class SegmentTree {
    min: Int32Array;
    max: Int32Array;
    lazy: Int32Array;
    n: number;

    constructor(n: number) {
        this.n = n;
        this.min = new Int32Array(4 * n);
        this.max = new Int32Array(4 * n);
        this.lazy = new Int32Array(4 * n);
    }

    pushDown(node: number) {
        if (this.lazy[node] !== 0) {
            const val = this.lazy[node];
            this.min[2 * node + 1] += val;
            this.max[2 * node + 1] += val;
            this.lazy[2 * node + 1] += val;
            this.min[2 * node + 2] += val;
            this.max[2 * node + 2] += val;
            this.lazy[2 * node + 2] += val;
            this.lazy[node] = 0;
        }
    }

    update(node: number, start: number, end: number, qL: number, qR: number, val: number) {
        if (qL > end || qR < start) return;
        if (qL <= start && end <= qR) {
            this.min[node] += val;
            this.max[node] += val;
            this.lazy[node] += val;
            return;
        }
        this.pushDown(node);
        const mid = (start + end) >> 1;
        this.update(2 * node + 1, start, mid, qL, qR, val);
        this.update(2 * node + 2, mid + 1, end, qL, qR, val);
        this.min[node] = Math.min(this.min[2 * node + 1], this.min[2 * node + 2]);
        this.max[node] = Math.max(this.max[2 * node + 1], this.max[2 * node + 2]);
    }

    findMax(node: number, start: number, end: number, qL: number, qR: number): number {
        if (qL > end || qR < start || this.min[node] > 0 || this.max[node] < 0) return -1;
        if (start === end) return start;
        this.pushDown(node);
        const mid = (start + end) >> 1;
        let res = this.findMax(2 * node + 2, mid + 1, end, qL, qR);
        if (res === -1) {
            res = this.findMax(2 * node + 1, start, mid, qL, qR);
        }
        return res;
    }
}

function longestBalanced(nums: number[]): number {
    const n = nums.length;
    const nextIdx = new Int32Array(n).fill(n);
    const lastOcc = new Int32Array(100001).fill(-1);
    for (let i = n - 1; i >= 0; i--) {
        if (lastOcc[nums[i]] !== -1) nextIdx[i] = lastOcc[nums[i]];
        lastOcc[nums[i]] = i;
    }

    const st = new SegmentTree(n);
    const firstOcc = new Int32Array(100001).fill(-1);
    for (let i = 0; i < n; i++) {
        if (firstOcc[nums[i]] === -1) {
            firstOcc[nums[i]] = i;
            const sign = (nums[i] % 2 === 0 ? -1 : 1);
            st.update(0, 0, n - 1, i, n - 1, sign);
        }
    }

    let ans = 0;
    for (let l = 0; l < n; l++) {
        const r = st.findMax(0, 0, n - 1, l, n - 1);
        if (r !== -1) ans = Math.max(ans, r - l + 1);
        const sign = (nums[l] % 2 === 0 ? -1 : 1);
        st.update(0, 0, n - 1, l, nextIdx[l] - 1, -sign);
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
     * @param Integer[] $nums
     * @return Integer
     */
    function longestBalanced($nums) {
        $n = count($nums);
        $nextIdx = array_fill(0, $n, $n);
        $lastOcc = array_fill(0, 100001, -1);
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($lastOcc[$nums[$i]] !== -1) $nextIdx[$i] = $lastOcc[$nums[$i]];
            $lastOcc[$nums[$i]] = $i;
        }

        $treeMin = new SplFixedArray(4 * $n);
        $treeMax = new SplFixedArray(4 * $n);
        $lazy = new SplFixedArray(4 * $n);
        for ($i = 0; $i < 4 * $n; $i++) {
            $treeMin[$i] = 0; $treeMax[$i] = 0; $lazy[$i] = 0;
        }

        $update = function($node, $start, $end, $qL, $qR, $val) use (&$update, &$treeMin, &$treeMax, &$lazy) {
            if ($qL > $end || $qR < $start) return;
            if ($qL <= $start && $end <= $qR) {
                $treeMin[$node] += $val;
                $treeMax[$node] += $val;
                $lazy[$node] += $val;
                return;
            }
            if ($lazy[$node] != 0) {
                $v = $lazy[$node];
                $treeMin[2*$node+1] += $v; $treeMax[2*$node+1] += $v; $lazy[2*$node+1] += $v;
                $treeMin[2*$node+2] += $v; $treeMax[2*$node+2] += $v; $lazy[2*$node+2] += $v;
                $lazy[$node] = 0;
            }
            $mid = ($start + $end) >> 1;
            $update(2 * $node + 1, $start, $mid, $qL, $qR, $val);
            $update(2 * $node + 2, $mid + 1, $end, $qL, $qR, $val);
            $treeMin[$node] = min($treeMin[2 * $node + 1], $treeMin[2 * $node + 2]);
            $treeMax[$node] = max($treeMax[2 * $node + 1], $treeMax[2 * $node + 2]);
        };

        $findMax = function($node, $start, $end, $qL, $qR) use (&$findMax, &$treeMin, &$treeMax, &$lazy) {
            if ($qL > $end || $qR < $start || $treeMin[$node] > 0 || $treeMax[$node] < 0) return -1;
            if ($start == $end) return $start;
            if ($lazy[$node] != 0) {
                $v = $lazy[$node];
                $treeMin[2*$node+1] += $v; $treeMax[2*$node+1] += $v; $lazy[2*$node+1] += $v;
                $treeMin[2*$node+2] += $v; $treeMax[2*$node+2] += $v; $lazy[2*$node+2] += $v;
                $lazy[$node] = 0;
            }
            $mid = ($start + $end) >> 1;
            $res = $findMax(2 * $node + 2, $mid + 1, $end, $qL, $qR);
            if ($res == -1) $res = $findMax(2 * $node + 1, $start, $mid, $qL, $qR);
            return $res;
        };

        $firstOcc = array_fill(0, 100001, -1);
        for ($i = 0; $i < $n; $i++) {
            if ($firstOcc[$nums[$i]] === -1) {
                $firstOcc[$nums[$i]] = $i;
                $sign = ($nums[$i] % 2 === 0 ? -1 : 1);
                $update(0, 0, $n - 1, $i, $n - 1, $sign);
            }
        }

        $ans = 0;
        for ($l = 0; $l < $n; $l++) {
            $r = $findMax(0, 0, $n - 1, $l, $n - 1);
            if ($r != -1) $ans = max($ans, $r - $l + 1);
            $sign = ($nums[$l] % 2 === 0 ? -1 : 1);
            $update(0, 0, $n - 1, $l, $nextIdx[$l] - 1, -$sign);
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
    class SegmentTree {
        var treeMin: [Int]
        var treeMax: [Int]
        var lazy: [Int]
        var n: Int

        init(_ n: Int) {
            self.n = n
            self.treeMin = Array(repeating: 0, count: 4 * n)
            self.treeMax = Array(repeating: 0, count: 4 * n)
            self.lazy = Array(repeating: 0, count: 4 * n)
        }

        func pushDown(_ node: Int) {
            if lazy[node] != 0 {
                let val = lazy[node]
                treeMin[2 * node + 1] += val
                treeMax[2 * node + 1] += val
                lazy[2 * node + 1] += val
                treeMin[2 * node + 2] += val
                treeMax[2 * node + 2] += val
                lazy[2 * node + 2] += val
                lazy[node] = 0
            }
        }

        func update(_ node: Int, _ start: Int, _ end: Int, _ qL: Int, _ qR: Int, _ val: Int) {
            if qL > end || qR < start { return }
            if qL <= start && end <= qR {
                treeMin[node] += val
                treeMax[node] += val
                lazy[node] += val
                return
            }
            pushDown(node)
            let mid = (start + end) / 2
            update(2 * node + 1, start, mid, qL, qR, val)
            update(2 * node + 2, mid + 1, end, qL, qR, val)
            treeMin[node] = min(treeMin[2 * node + 1], treeMin[2 * node + 2])
            treeMax[node] = max(treeMax[2 * node + 1], treeMax[2 * node + 2])
        }

        func findMax(_ node: Int, _ start: Int, _ end: Int, _ qL: Int, _ qR: Int) -> Int {
            if qL > end || qR < start || treeMin[node] > 0 || treeMax[node] < 0 { return -1 }
            if start == end { return start }
            pushDown(node)
            let mid = (start + end) / 2
            var res = findMax(2 * node + 2, mid + 1, end, qL, qR)
            if res == -1 {
                res = findMax(2 * node + 1, start, mid, qL, qR)
            }
            return res
        }
    }

    func longestBalanced(_ nums: [Int]) -> Int {
        let n = nums.length
        var nextIdx = Array(repeating: n, count: n)
        var lastOcc = Array(repeating: -1, count: 100001)
        for i in (0..<n).reversed() {
            if lastOcc[nums[i]] != -1 { nextIdx[i] = lastOcc[nums[i]] }
            lastOcc[nums[i]] = i
        }

        let st = SegmentTree(n)
        var firstOcc = Array(repeating: -1, count: 100001)
        for i in 0..<n {
            if firstOcc[nums[i]] == -1 {
                firstOcc[nums[i]] = i
                let sign = (nums[i] % 2 == 0 ? -1 : 1)
                st.update(0, 0, n - 1, i, n - 1, sign)
            }
        }

        var ans = 0
        for l in 0..<n {
            let r = st.findMax(0, 0, n - 1, l, n - 1)
            if r != -1 { ans = max(ans, r - l + 1) }
            let sign = (nums[l] % 2 == 0 ? -1 : 1)
            st.update(0, 0, n - 1, l, nextIdx[l] - 1, -sign)
        }
        return ans
    }
}

extension Array {
    var length: Int { return self.count }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    class SegmentTree(val n: Int) {
        private val treeMin = IntArray(4 * n)
        private val treeMax = IntArray(4 * n)
        private val lazy = IntArray(4 * n)

        private fun pushDown(node: Int) {
            if (lazy[node] != 0) {
                val v = lazy[node]
                treeMin[2 * node + 1] += v
                treeMax[2 * node + 1] += v
                lazy[2 * node + 1] += v
                treeMin[2 * node + 2] += v
                treeMax[2 * node + 2] += v
                lazy[2 * node + 2] += v
                lazy[node] = 0
            }
        }

        fun update(node: Int, start: Int, end: Int, qL: Int, qR: Int, v: Int) {
            if (qL > end || qR < start) return
            if (qL <= start && end <= qR) {
                treeMin[node] += v
                treeMax[node] += v
                lazy[node] += v
                return
            }
            pushDown(node)
            val mid = (start + end) / 2
            update(2 * node + 1, start, mid, qL, qR, v)
            update(2 * node + 2, mid + 1, end, qL, qR, v)
            treeMin[node] = minOf(treeMin[2 * node + 1], treeMin[2 * node + 2])
            treeMax[node] = maxOf(treeMax[2 * node + 1], treeMax[2 * node + 2])
        }

        fun findMax(node: Int, start: Int, end: Int, qL: Int, qR: Int): Int {
            if (qL > end || qR < start || treeMin[node] > 0 || treeMax[node] < 0) return -1
            if (start == end) return start
            pushDown(node)
            val mid = (start + end) / 2
            var res = findMax(2 * node + 2, mid + 1, end, qL, qR)
            if (res == -1) res = findMax(2 * node + 1, start, mid, qL, qR)
            return res
        }
    }

    fun longestBalanced(nums: IntArray): Int {
        val n = nums.size
        val nextIdx = IntArray(n) { n }
        val lastOcc = IntArray(100001) { -1 }
        for (i in n - 1 downTo 0) {
            if (lastOcc[nums[i]] != -1) nextIdx[i] = lastOcc[nums[i]]
            lastOcc[nums[i]] = i
        }

        val st = SegmentTree(n)
        val firstOcc = IntArray(100001) { -1 }
        for (i in 0 until n) {
            if (firstOcc[nums[i]] == -1) {
                firstOcc[nums[i]] = i
                val sign = if (nums[i] % 2 == 0) -1 else 1
                st.update(0, 0, n - 1, i, n - 1, sign)
            }
        }

        var ans = 0
        for (l in 0 until n) {
            val r = st.findMax(0, 0, n - 1, l, n - 1)
            if (r != -1) ans = maxOf(ans, r - l + 1)
            val sign = if (nums[l] % 2 == 0) -1 else 1
            st.update(0, 0, n - 1, l, nextIdx[l] - 1, -sign)
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
import 'dart:typed_data';
import 'dart:math';

class SegmentTree {
  final int n;
  final Int32List treeMin;
  final Int32List treeMax;
  final Int32List lazy;

  SegmentTree(this.n) 
    : treeMin = Int32List(4 * n),
      treeMax = Int32List(4 * n),
      lazy = Int32List(4 * n);

  void pushDown(int node) {
    if (lazy[node] != 0) {
      int v = lazy[node];
      treeMin[2 * node + 1] += v;
      treeMax[2 * node + 1] += v;
      lazy[2 * node + 1] += v;
      treeMin[2 * node + 2] += v;
      treeMax[2 * node + 2] += v;
      lazy[2 * node + 2] += v;
      lazy[node] = 0;
    }
  }

  void update(int node, int start, int end, int qL, int qR, int v) {
    if (qL > end || qR < start) return;
    if (qL <= start && end <= qR) {
      treeMin[node] += v;
      treeMax[node] += v;
      lazy[node] += v;
      return;
    }
    pushDown(node);
    int mid = (start + end) >> 1;
    update(2 * node + 1, start, mid, qL, qR, v);
    update(2 * node + 2, mid + 1, end, qL, qR, v);
    treeMin[node] = min(treeMin[2 * node + 1], treeMin[2 * node + 2]);
    treeMax[node] = max(treeMax[2 * node + 1], treeMax[2 * node + 2]);
  }

  int findMax(int node, int start, int end, int qL, int qR) {
    if (qL > end || qR < start || treeMin[node] > 0 || treeMax[node] < 0) return -1;
    if (start == end) return start;
    pushDown(node);
    int mid = (start + end) >> 1;
    int res = findMax(2 * node + 2, mid + 1, end, qL, qR);
    if (res == -1) res = findMax(2 * node + 1, start, mid, qL, qR);
    return res;
  }
}

class Solution {
  int longestBalanced(List<int> nums) {
    int n = nums.length;
    Int32List nextIdx = Int32List(n);
    Int32List lastOcc = Int32List(100001);
    for(int i=0; i<100001; i++) lastOcc[i] = -1;
    for (int i = n - 1; i >= 0; i--) {
      nextIdx[i] = (lastOcc[nums[i]] != -1) ? lastOcc[nums[i]] : n;
      lastOcc[nums[i]] = i;
    }

    SegmentTree st = SegmentTree(n);
    Int32List firstOcc = Int32List(100001);
    for(int i=0; i<100001; i++) firstOcc[i] = -1;
    for (int i = 0; i < n; i++) {
      if (firstOcc[nums[i]] == -1) {
        firstOcc[nums[i]] = i;
        int sign = (nums[i] % 2 == 0) ? -1 : 1;
        st.update(0, 0, n - 1, i, n - 1, sign);
      }
    }

    int ans = 0;
    for (int l = 0; l < n; l++) {
      int r = st.findMax(0, 0, n - 1, l, n - 1);
      if (r != -1) ans = max(ans, r - l + 1);
      int sign = (nums[l] % 2 == 0) ? -1 : 1;
      st.update(0, 0, n - 1, l, nextIdx[l] - 1, -sign);
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
func longestBalanced(nums []int) int {
    n := len(nums)
    nextIdx := make([]int, n)
    lastOcc := make([]int, 100001)
    for i := range lastOcc { lastOcc[i] = -1 }
    for i := n - 1; i >= 0; i-- {
        if lastOcc[nums[i]] != -1 { nextIdx[i] = lastOcc[nums[i]] } else { nextIdx[i] = n }
        lastOcc[nums[i]] = i
    }

    treeMin := make([]int, 4*n)
    treeMax := make([]int, 4*n)
    lazy := make([]int, 4*n)

    var update func(int, int, int, int, int, int)
    update = func(node, start, end, qL, qR, val int) {
        if qL > end || qR < start { return }
        if qL <= start && end <= qR {
            treeMin[node] += val; treeMax[node] += val; lazy[node] += val
            return
        }
        if lazy[node] != 0 {
            v := lazy[node]
            treeMin[2*node+1] += v; treeMax[2*node+1] += v; lazy[2*node+1] += v
            treeMin[2*node+2] += v; treeMax[2*node+2] += v; lazy[2*node+2] += v
            lazy[node] = 0
        }
        mid := (start + end) >> 1
        update(2*node+1, start, mid, qL, qR, val)
        update(2*node+2, mid+1, end, qL, qR, val)
        treeMin[node] = treeMin[2*node+1]; if treeMin[2*node+2] < treeMin[node] { treeMin[node] = treeMin[2*node+2] }
        treeMax[node] = treeMax[2*node+1]; if treeMax[2*node+2] > treeMax[node] { treeMax[node] = treeMax[2*node+2] }
    }

    var findMax func(int, int, int, int, int) int
    findMax = func(node, start, end, qL, qR int) int {
        if qL > end || qR < start || treeMin[node] > 0 || treeMax[node] < 0 { return -1 }
        if start == end { return start }
        if lazy[node] != 0 {
            v := lazy[node]
            treeMin[2*node+1] += v; treeMax[2*node+1] += v; lazy[2*node+1] += v
            treeMin[2*node+2] += v; treeMax[2*node+2] += v; lazy[2*node+2] += v
            lazy[node] = 0
        }
        mid := (start + end) >> 1
        res := findMax(2*node+2, mid+1, end, qL, qR)
        if res == -1 { res = findMax(2*node+1, start, mid, qL, qR) }
        return res
    }

    firstOcc := make([]int, 100001)
    for i := range firstOcc { firstOcc[i] = -1 }
    for i := 0; i < n; i++ {
        if firstOcc[nums[i]] == -1 {
            firstOcc[nums[i]] = i
            sign := 1; if nums[i]%2 == 0 { sign = -1 }
            update(0, 0, n-1, i, n-1, sign)
        }
    }

    ans := 0
    for l := 0; l < n; l++ {
        r := findMax(0, 0, n-1, l, n-1)
        if r != -1 {
            len := r - l + 1
            if len > ans { ans = len }
        }
        sign := 1; if nums[l]%2 == 0 { sign = -1 }
        update(0, 0, n-1, l, nextIdx[l]-1, -sign)
    }
    return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def longest_balanced(nums)
  n = nums.length
  next_occ = Array.new(n, n)
  last_pos = Array.new(100001, n)
  (n - 1).downto(0) do |i|
    next_occ[i] = last_pos[nums[i]]
    last_pos[nums[i]] = i
  end

  first_occ = Array.new(100001, -1)
  nums.each_with_index { |v, i| first_occ[v] = i if first_occ[v] == -1 }

  @tree_min = Array.new(4 * n, 0)
  @tree_max = Array.new(4 * n, 0)
  @tree_lazy = Array.new(4 * n, 0)

  def push(v)
    if @tree_lazy[v] != 0
      lazy = @tree_lazy[v]
      v2, v21 = 2 * v, 2 * v + 1
      @tree_min[v2] += lazy; @tree_max[v2] += lazy; @tree_lazy[v2] += lazy
      @tree_min[v21] += lazy; @tree_max[v21] += lazy; @tree_lazy[v21] += lazy
      @tree_lazy[v] = 0
    end
  end

  def update(v, tl, tr, l, r, add)
    return if l > r
    if l == tl && r == tr
      @tree_min[v] += add; @tree_max[v] += add; @tree_lazy[v] += add
    else
      push(v)
      tm = (tl + tr) / 2
      update(2 * v, tl, tm, l, r < tm ? r : tm, add)
      update(2 * v + 1, tm + 1, tr, l > tm + 1 ? l : tm + 1, r, add)
      v2, v21 = 2 * v, 2 * v + 1
      @tree_min[v] = @tree_min[v2] < @tree_min[v21] ? @tree_min[v2] : @tree_min[v21]
      @tree_max[v] = @tree_max[v2] > @tree_max[v21] ? @tree_max[v2] : @tree_max[v21]
    end
  end

  def find_last_zero(v, tl, tr, l, r)
    return -1 if l > tr || r < tl || @tree_min[v] > 0 || @tree_max[v] < 0
    return tl if tl == tr
    push(v)
    tm = (tl + tr) / 2
    res = find_last_zero(2 * v + 1, tm + 1, tr, l, r)
    res = find_last_zero(2 * v, tl, tm, l, r) if res == -1
    res
  end

  (1..100000).each do |v|
    if first_occ[v] != -1
      sign = (v % 2 == 1 ? 1 : -1)
      update(1, 0, n - 1, first_occ[v], n - 1, sign)
    end
  end

  ans = 0
  (0...n).each do |l|
    r = find_last_zero(1, 0, n - 1, l, n - 1)
    ans = [ans, r - l + 1].max if r != -1
    sign = (nums[l] % 2 == 1 ? 1 : -1)
    update(1, 0, n - 1, l, next_occ[l] - 1, -sign)
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
    def longestBalanced(nums: Array[Int]): Int = {
        val n = nums.length
        val next_occ = Array.fill(n)(n)
        val last_pos = Array.fill(100001)(n)
        for (i <- n - 1 to 0 by -1) {
            next_occ(i) = last_pos(nums(i))
            last_pos(nums(i)) = i
        }
        val first_occ = Array.fill(100001)(-1)
        for (i <- 0 until n) {
            if (first_occ(nums(i)) == -1) first_occ(nums(i)) = i
        }

        val tree_min = Array.fill(4 * n)(0)
        val tree_max = Array.fill(4 * n)(0)
        val tree_lazy = Array.fill(4 * n)(0)

        def push(v: Int): Unit = {
            if (tree_lazy(v) != 0) {
                val lazyVal = tree_lazy(v)
                val v2 = 2 * v
                val v21 = 2 * v + 1
                tree_min(v2) += lazyVal; tree_max(v2) += lazyVal; tree_lazy(v2) += lazyVal
                tree_min(v21) += lazyVal; tree_max(v21) += lazyVal; tree_lazy(v21) += lazyVal
                tree_lazy(v) = 0
            }
        }

        def update(v: Int, tl: Int, tr: Int, l: Int, r: Int, add: Int): Unit = {
            if (l > r) return
            if (l == tl && r == tr) {
                tree_min(v) += add; tree_max(v) += add; tree_lazy(v) += add
            } else {
                push(v)
                val tm = (tl + tr) / 2
                update(2 * v, tl, tm, l, math.min(r, tm), add)
                update(2 * v + 1, tm + 1, tr, math.max(l, tm + 1), r, add)
                tree_min(v) = math.min(tree_min(2 * v), tree_min(2 * v + 1))
                tree_max(v) = math.max(tree_max(2 * v), tree_max(2 * v + 1))
            }
        }

        def findLastZero(v: Int, tl: Int, tr: Int, l: Int, r: Int): Int = {
            if (l > r || tree_min(v) > 0 || tree_max(v) < 0) return -1
            if (tl == tr) return tl
            push(v)
            val tm = (tl + tr) / 2
            var res = findLastZero(2 * v + 1, tm + 1, tr, math.max(l, tm + 1), r)
            if (res == -1) res = findLastZero(2 * v, tl, tm, l, math.min(r, tm))
            res
        }

        for (v <- 1 to 100000) {
            if (first_occ(v) != -1) {
                val sign = if (v % 2 == 1) 1 else -1
                update(1, 0, n - 1, first_occ(v), n - 1, sign)
            }
        }

        var ans = 0
        for (l <- 0 until n) {
            val r = findLastZero(1, 0, n - 1, l, n - 1)
            if (r != -1) ans = math.max(ans, r - l + 1)
            val sign = if (nums(l) % 2 == 1) 1 else -1
            update(1, 0, n - 1, l, next_occ(l) - 1, -sign)
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
    pub fn longest_balanced(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut next_occ = vec![n; n];
        let mut last_pos = vec![n; 100001];
        for i in (0..n).rev() {
            next_occ[i] = last_pos[nums[i] as usize];
            last_pos[nums[i] as usize] = i;
        }
        let mut first_occ = vec![n; 100001];
        for i in 0..n {
            if first_occ[nums[i] as usize] == n {
                first_occ[nums[i] as usize] = i;
            }
        }

        let mut tree_min = vec![0; 4 * n + 1];
        let mut tree_max = vec![0; 4 * n + 1];
        let mut tree_lazy = vec![0; 4 * n + 1];

        fn push(v: usize, tree_min: &mut Vec<i32>, tree_max: &mut Vec<i32>, tree_lazy: &mut Vec<i32>) {
            if tree_lazy[v] != 0 {
                let lazy = tree_lazy[v];
                tree_min[2 * v] += lazy; tree_max[2 * v] += lazy; tree_lazy[2 * v] += lazy;
                tree_min[2 * v + 1] += lazy; tree_max[2 * v + 1] += lazy; tree_lazy[2 * v + 1] += lazy;
                tree_lazy[v] = 0;
            }
        }

        fn update(v: usize, tl: usize, tr: usize, l: usize, r: usize, add: i32, tree_min: &mut Vec<i32>, tree_max: &mut Vec<i32>, tree_lazy: &mut Vec<i32>) {
            if l > r { return; }
            if l == tl && r == tr {
                tree_min[v] += add; tree_max[v] += add; tree_lazy[v] += add;
            } else {
                push(v, tree_min, tree_max, tree_lazy);
                let tm = (tl + tr) / 2;
                update(2 * v, tl, tm, l, std::cmp::min(r, tm), add, tree_min, tree_max, tree_lazy);
                update(2 * v + 1, tm + 1, tr, std::cmp::max(l, tm + 1), r, add, tree_min, tree_max, tree_lazy);
                tree_min[v] = std::cmp::min(tree_min[2 * v], tree_min[2 * v + 1]);
                tree_max[v] = std::cmp::max(tree_max[2 * v], tree_max[2 * v + 1]);
            }
        }

        fn find_last_zero(v: usize, tl: usize, tr: usize, l: usize, r: usize, tree_min: &mut Vec<i32>, tree_max: &mut Vec<i32>, tree_lazy: &mut Vec<i32>) -> i32 {
            if l > r || tree_min[v] > 0 || tree_max[v] < 0 { return -1; }
            if tl == tr { return tl as i32; }
            push(v, tree_min, tree_max, tree_lazy);
            let tm = (tl + tr) / 2;
            let mut res = find_last_zero(2 * v + 1, tm + 1, tr, std::cmp::max(l, tm + 1), r, tree_min, tree_max, tree_lazy);
            if res == -1 { res = find_last_zero(2 * v, tl, tm, l, std::cmp::min(r, tm), tree_min, tree_max, tree_lazy); }
            res
        }

        for v in 1..100001 {
            if first_occ[v] != n {
                let sign = if v % 2 == 1 { 1 } else { -1 };
                update(1, 0, n - 1, first_occ[v], n - 1, sign, &mut tree_min, &mut tree_max, &mut tree_lazy);
            }
        }

        let mut ans = 0;
        for l in 0..n {
            let r = find_last_zero(1, 0, n - 1, l, n - 1, &mut tree_min, &mut tree_max, &mut tree_lazy);
            if r != -1 { ans = std::cmp::max(ans, r - l as i32 + 1); }
            let sign = if nums[l] % 2 == 1 { 1 } else { -1 };
            update(1, 0, n - 1, l, next_occ[l] - 1, -sign, &mut tree_min, &mut tree_max, &mut tree_lazy);
        }
        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (longest-balanced nums-list)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([nums (list->vector nums-list)]
         [n (vector-length nums)]
         [next-occ (make-vector n n)]
         [last-pos (make-vector 100001 n)]
         [tree-min (make-vector (* 4 n) 0)]
         [tree-max (make-vector (* 4 n) 0)]
         [tree-lazy (make-vector (* 4 n) 0)])
    (for ([i (in-range (- n 1) -1 -1)])
      (let ([v (vector-ref nums i)])
        (vector-set! next-occ i (vector-ref last-pos v))
        (vector-set! last-pos v i)))
    (define first-occ (make-vector 100001 -1))
    (for ([i (in-range n)])
      (let ([v (vector-ref nums i)])
        (when (= (vector-ref first-occ v) -1) (vector-set! first-occ v i))))
    (define (push v)
      (let ([lazy (vector-ref tree-lazy v)])
        (when (not (= lazy 0))
          (let ([v2 (* 2 v)] [v21 (+ (* 2 v) 1)])
            (vector-set! tree-min v2 (+ (vector-ref tree-min v2) lazy))
            (vector-set! tree-max v2 (+ (vector-ref tree-max v2) lazy))
            (vector-set! tree-lazy v2 (+ (vector-ref tree-lazy v2) lazy))
            (vector-set! tree-min v21 (+ (vector-ref tree-min v21) lazy))
            (vector-set! tree-max v21 (+ (vector-ref tree-max v21) lazy))
            (vector-set! tree-lazy v21 (+ (vector-ref tree-lazy v21) lazy))
            (vector-set! tree-lazy v 0)))))
    (define (update v tl tr l r add)
      (if (> l r) (void)
          (if (and (= l tl) (= r tr))
              (begin
                (vector-set! tree-min v (+ (vector-ref tree-min v) add))
                (vector-set! tree-max v (+ (vector-ref tree-max v) add))
                (vector-set! tree-lazy v (+ (vector-ref tree-lazy v) add)))
              (begin
                (push v)
                (let* ([tm (quotient (+ tl tr) 2)] [v2 (* 2 v)] [v21 (+ v2 1)])
                  (update v2 tl tm l (min r tm) add)
                  (update v21 (+ tm 1) tr (max l (+ tm 1)) r add)
                  (vector-set! tree-min v (min (vector-ref tree-min v2) (vector-ref tree-min v21)))
                  (vector-set! tree-max v (max (vector-ref tree-max v2) (vector-ref tree-max v21))))))))
    (define (find-last-zero v tl tr l r)
      (if (or (> l r) (> (vector-ref tree-min v) 0) (< (vector-ref tree-max v) 0)) -1
          (if (= tl tr) tl
              (begin
                (push v)
                (let* ([tm (quotient (+ tl tr) 2)] [v2 (* 2 v)] [v21 (+ v2 1)])
                  (let ([res (find-last-zero v21 (+ tm 1) tr (max l (+ tm 1)) r)])
                    (if (= res -1) (find-last-zero v2 tl tm l (min r tm)) res)))))))
    (for ([v (in-range 1 100001)])
      (let ([p (vector-ref first-occ v)])
        (when (not (= p -1))
          (let ([sign (if (odd? v) 1 -1)]) (update 1 0 (- n 1) p (- n 1) sign)))))
    (let ([ans 0])
      (for ([l (in-range n)])
        (let ([r (find-last-zero 1 0 (- n 1) l (- n 1))])
          (when (not (= r -1)) (set! ans (max ans (+ (- r l) 1))))
          (let ([sign (if (odd? (vector-ref nums l)) 1 -1)])
            (update 1 0 (- n 1) l (- (vector-ref next-occ l) 1) (- sign)))))
      ans)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec longest_balanced(Nums :: [integer()]) -> integer().
longest_balanced(Nums) ->
  N = length(Nums),
  NumsTuple = list_to_tuple(Nums),
  {NextOccList, _} = lists:foldr(fun({Num, Index}, {AccNext, AccLast}) ->
    Next = maps:get(Num, AccLast, N),
    {[Next | AccNext], maps:put(Num, Index, AccLast)}
  end, {[], #{}}, lists:zip(Nums, lists:seq(0, N-1))),
  NextOccTuple = list_to_tuple(NextOccList),
  FirstOccs = maps:to_list(lists:foldl(fun({Num, Index}, Acc) ->
    case maps:is_key(Num, Acc) of true -> Acc; false -> maps:put(Num, Index, Acc) end
  end, #{}, lists:zip(Nums, lists:seq(0, N-1)))),
  Tree1 = build(0, N-1),
  Tree2 = lists:foldl(fun({Num, Index}, T) ->
    Sign = if Num rem 2 == 1 -> 1; true -> -1 end,
    update(0, N-1, Index, N-1, Sign, T)
  end, Tree1, FirstOccs),
  solve(0, N, NumsTuple, NextOccTuple, Tree2, 0).

build(TL, TR) when TL == TR -> {0, 0, 0, nil, nil};
build(TL, TR) -> TM = (TL + TR) div 2, {0, 0, 0, build(TL, TM), build(TM + 1, TR)}.

push(Node, 0) -> Node;
push({Min, Max, Lazy, L, R}, Add) -> {Min + Add, Max + Add, Lazy + Add, L, R}.

update(TL, TR, L, R, Add, {Min, Max, Lazy, Left, Right}) ->
  if (L > TR) or (R < TL) -> {Min, Max, Lazy, Left, Right};
     (L =< TL) and (TR =< R) -> {Min + Add, Max + Add, Lazy + Add, Left, Right};
     true -> TM = (TL + TR) div 2, L1 = push(Left, Lazy), R1 = push(Right, Lazy),
             NL = update(TL, TM, L, R, Add, L1), NR = update(TM + 1, TR, L, R, Add, R1),
             {LMin, LMax, _, _, _} = NL, {RMin, RMax, _, _, _} = NR,
             {erlang:min(LMin, RMin), erlang:max(LMax, RMax), 0, NL, NR}
  end.

find_last(TL, TR, L, R, {Min, Max, Lazy, Left, Right}) ->
  if (L > TR) or (R < TL) or (Min > 0) or (Max < 0) -> -1;
     TL == TR -> TL;
     true -> TM = (TL + TR) div 2, Res = find_last(TM + 1, TR, L, R, push(Right, Lazy)),
             if Res == -1 -> find_last(TL, TM, L, R, push(Left, Lazy)); true -> Res end
  end.

solve(L, N, _, _, _, Ans) when L == N -> Ans;
solve(L, N, Nums, Nexts, Tree, Ans) ->
  R = find_last(0, N-1, L, N-1, Tree),
  NewAns = if R == -1 -> Ans; true -> erlang:max(Ans, R - L + 1) end,
  Val = element(L + 1, Nums), Next = element(L + 1, Nexts),
  Sign = if Val rem 2 == 1 -> 1; true -> -1 end,
  NewTree = update(0, N-1, L, Next - 1, -Sign, Tree),
  solve(L + 1, N, Nums, Nexts, NewTree, NewAns).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  def longest_balanced(nums) do
    n = length(nums)
    nums_tuple = List.to_tuple(nums)
    {next_occ_list, _} = Enum.reduce(Enum.zip(nums, 0..n-1) |> Enum.reverse(), {[], %{}}, fn {num, index}, {acc_next, acc_last} ->
      next = Map.get(acc_last, num, n)
      {[next | acc_next], Map.put(acc_last, num, index)}
    end)
    next_occ_tuple = List.to_tuple(next_occ_list)
    first_occs = Enum.reduce(Enum.zip(nums, 0..n-1), %{}, fn {num, index}, acc ->
      if Map.has_key?(acc, num), do: acc, else: Map.put(acc, num, index)
    end) |> Map.to_list()
    tree = build(0, n-1)
    tree = Enum.reduce(first_occs, tree, fn {num, index}, t ->
      sign = if rem(num, 2) == 1, do: 1, else: -1
      update(0, n-1, index, n-1, sign, t)
    end)
    solve(0, n, nums_tuple, next_occ_tuple, tree, 0)
  end

  defp solve(l, n, _, _, _, ans) when l == n, do: ans
  defp solve(l, n, nums, nexts, tree, ans) do
    r = find_last(0, n-1, l, n-1, tree)
    new_ans = if r == -1, do: ans, else: max(ans, r - l + 1)
    val = elem(nums, l)
    next = elem(nexts, l)
    sign = if rem(val, 2) == 1, do: 1, else: -1
    new_tree = update(0, n-1, l, next - 1, -sign, tree)
    solve(l + 1, n, nums, nexts, new_tree, new_ans)
  end

  defp build(tl, tr) when tl == tr, do: {0, 0, 0, nil, nil}
  defp build(tl, tr) do
    tm = div(tl + tr, 2)
    {0, 0, 0, build(tl, tm), build(tm + 1, tr)}
  end

  defp push(node, 0), do: node
  defp push({min, max, lazy, l, r}, add), do: {min + add, max + add, lazy + add, l, r}

  defp update(tl, tr, l, r, add, {min, max, lazy, left, right}) do
    cond do
      l > tr or r < tl -> {min, max, lazy, left, right}
      l <= tl and tr <= r -> {min + add, max + add, lazy + add, left, right}
      true ->
        tm = div(tl + tr, 2)
        nl = update(tl, tm, l, r, add, push(left, lazy))
        nr = update(tm + 1, tr, l, r, add, push(right, lazy))
        {lmin, lmax, _, _, _} = nl
        {rmin, rmax, _, _, _} = nr
        {min(lmin, rmin), max(lmax, rmax), 0, nl, nr}
    end
  end

  defp find_last(tl, tr, l, r, {min, max, lazy, left, right}) do
    if l > tr or r < tl or min > 0 or max < 0 do
      -1
    else
      if tl == tr do
        tl
      else
        tm = div(tl + tr, 2)
        res = find_last(tm + 1, tr, l, r, push(right, lazy))
        if res == -1, do: find_last(tl, tm, l, r, push(left, lazy)), else: res
      end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log N) where N is the length of the array. The segment tree is initialized in O(N log N) time, and we perform N queries and N updates, each taking O(log N) time. Mapping unique values to their occurrences also takes O(N) time.
- **Space Complexity:** O(N + V) where N is the length of the array and V is the maximum value in nums (up to 10^5). This space is used to store the segment tree nodes, the positions of each number, and their associated signs.
