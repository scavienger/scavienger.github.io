---
layout: post
title: "Maximum Total Subarray Value II"
date: 2026-06-10 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Greedy", "Segment Tree", "Heap (Priority Queue)"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/maximum-total-subarray-value-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long maxTotalValue(vector<int>& nums,\
        \ int k) {\n        int n = nums.size();\n        if (n == 0) return 0;\n\n\
        \        int max_log = 0;\n        while ((1 << (max_log + 1)) <= n) max_log++;\n\
        \n        vector<int> logs(n + 1, 0);\n        for (int i = 2; i <= n; ++i)\
        \ logs[i] = logs[i >> 1] + 1;\n\n        vector<vector<int>> st_max(max_log\
        \ + 1, vector<int>(n));\n        vector<vector<int>> st_min(max_log + 1, vector<int>(n));\n\
        \n        for (int i = 0; i < n; ++i) {\n            st_max[0][i] = nums[i];\n\
        \            st_min[0][i] = nums[i];\n        }\n\n        for (int j = 1; j\
        \ <= max_log; ++j) {\n            for (int i = 0; i + (1 << j) <= n; ++i) {\n\
        \                st_max[j][i] = max(st_max[j - 1][i], st_max[j - 1][i + (1 <<\
        \ (j - 1))]);\n                st_min[j][i] = min(st_min[j - 1][i], st_min[j\
        \ - 1][i + (1 << (j - 1))]);\n            }\n        }\n\n        auto get_val\
        \ = [&](int l, int r) {\n            int len = r - l + 1;\n            int j\
        \ = logs[len];\n            int mx = max(st_max[j][l], st_max[j][r - (1 << j)\
        \ + 1]);\n            int mn = min(st_min[j][l], st_min[j][r - (1 << j) + 1]);\n\
        \            return (long long)mx - mn;\n        };\n\n        priority_queue<pair<long\
        \ long, pair<int, int>>> pq;\n        for (int i = 0; i < n; ++i) {\n      \
        \      pq.push({get_val(i, n - 1), {i, n - 1}});\n        }\n\n        long\
        \ long total = 0;\n        for (int i = 0; i < k; ++i) {\n            auto top\
        \ = pq.top();\n            pq.pop();\n            long long val = top.first;\n\
        \            int l = top.second.first;\n            int r = top.second.second;\n\
        \            total += val;\n            if (r > l) {\n                pq.push({get_val(l,\
        \ r - 1), {l, r - 1}});\n            }\n        }\n\n        return total;\n\
        \    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public long maxTotalValue(int[]\
        \ nums, int k) {\n        int n = nums.length;\n        if (n == 0) return 0;\n\
        \n        int maxLog = 0;\n        while ((1 << (maxLog + 1)) <= n) maxLog++;\n\
        \n        int[] logs = new int[n + 1];\n        for (int i = 2; i <= n; i++)\
        \ logs[i] = logs[i >> 1] + 1;\n\n        int[][] stMax = new int[maxLog + 1][n];\n\
        \        int[][] stMin = new int[maxLog + 1][n];\n\n        for (int i = 0;\
        \ i < n; i++) {\n            stMax[0][i] = nums[i];\n            stMin[0][i]\
        \ = nums[i];\n        }\n\n        for (int j = 1; j <= maxLog; j++) {\n   \
        \         for (int i = 0; i + (1 << j) <= n; i++) {\n                stMax[j][i]\
        \ = Math.max(stMax[j - 1][i], stMax[j - 1][i + (1 << (j - 1))]);\n         \
        \       stMin[j][i] = Math.min(stMin[j - 1][i], stMin[j - 1][i + (1 << (j -\
        \ 1))]);\n            }\n        }\n\n        PriorityQueue<long[]> pq = new\
        \ PriorityQueue<>((a, b) -> Long.compare(b[0], a[0]));\n        for (int i =\
        \ 0; i < n; i++) {\n            pq.offer(new long[]{getVal(i, n - 1, stMax,\
        \ stMin, logs), i, n - 1});\n        }\n\n        long total = 0;\n        for\
        \ (int i = 0; i < k; i++) {\n            long[] curr = pq.poll();\n        \
        \    long val = curr[0];\n            int l = (int) curr[1];\n            int\
        \ r = (int) curr[2];\n            total += val;\n            if (r > l) {\n\
        \                pq.offer(new long[]{getVal(l, r - 1, stMax, stMin, logs), l,\
        \ r - 1});\n            }\n        }\n\n        return total;\n    }\n\n   \
        \ private long getVal(int l, int r, int[][] stMax, int[][] stMin, int[] logs)\
        \ {\n        int len = r - l + 1;\n        int j = logs[len];\n        int mx\
        \ = Math.max(stMax[j][l], stMax[j][r - (1 << j) + 1]);\n        int mn = Math.min(stMin[j][l],\
        \ stMin[j][r - (1 << j) + 1]);\n        return (long) mx - mn;\n    }\n}"
      python: "import heapq\n\nclass Solution(object):\n    def maxTotalValue(self,\
        \ nums, k):\n        \"\"\"\n        :type nums: List[int]\n        :type k:\
        \ int\n        :rtype: int\n        \"\"\"\n        n = len(nums)\n        if\
        \ n == 0:\n            return 0\n\n        logs = [0] * (n + 1)\n        for\
        \ i in range(2, n + 1):\n            logs[i] = logs[i >> 1] + 1\n\n        max_log\
        \ = logs[n]\n        st_max = [nums]\n        st_min = [nums]\n\n        for\
        \ j in range(1, max_log + 1):\n            prev_mx = st_max[-1]\n          \
        \  prev_mn = st_min[-1]\n            offset = 1 << (j - 1)\n            curr_mx\
        \ = [0] * (n - (1 << j) + 1)\n            curr_mn = [0] * (n - (1 << j) + 1)\n\
        \            for i in range(n - (1 << j) + 1):\n                v1, v2 = prev_mx[i],\
        \ prev_mx[i + offset]\n                curr_mx[i] = v1 if v1 > v2 else v2\n\
        \                v1, v2 = prev_mn[i], prev_mn[i + offset]\n                curr_mn[i]\
        \ = v1 if v1 < v2 else v2\n            st_max.append(curr_mx)\n            st_min.append(curr_mn)\n\
        \n        def get_val(l, r):\n            length = r - l + 1\n            j\
        \ = logs[length]\n            offset = length - (1 << j)\n            mx_j,\
        \ mn_j = st_max[j], st_min[j]\n            v1, v2 = mx_j[l], mx_j[l + offset]\n\
        \            mx = v1 if v1 > v2 else v2\n            v1, v2 = mn_j[l], mn_j[l\
        \ + offset]\n            mn = v1 if v1 < v2 else v2\n            return mx -\
        \ mn\n\n        heap = []\n        for i in range(n):\n            val = get_val(i,\
        \ n - 1)\n            heap.append((-val, i, n - 1))\n\n        heapq.heapify(heap)\n\
        \n        ans = 0\n        for _ in range(k):\n            neg_v, l, r = heapq.heappop(heap)\n\
        \            ans -= neg_v\n            if r > l:\n                next_r = r\
        \ - 1\n                next_v = get_val(l, next_r)\n                heapq.heappush(heap,\
        \ (-next_v, l, next_r))\n\n        return ans"
      python3: "import heapq\n\nclass Solution:\n    def maxTotalValue(self, nums: list[int],\
        \ k: int) -> int:\n        n = len(nums)\n        if n == 0:\n            return\
        \ 0\n\n        log_n = n.bit_length()\n        st_min = [[0] * n for _ in range(log_n)]\n\
        \        st_max = [[0] * n for _ in range(log_n)]\n\n        st_min[0] = nums[:]\n\
        \        st_max[0] = nums[:]\n\n        for j in range(1, log_n):\n        \
        \    offset = 1 << (j - 1)\n            st_min_j = st_min[j]\n            st_min_prev\
        \ = st_min[j - 1]\n            st_max_j = st_max[j]\n            st_max_prev\
        \ = st_max[j - 1]\n            for i in range(n - (1 << j) + 1):\n         \
        \       v1, v2 = st_min_prev[i], st_min_prev[i + offset]\n                st_min_j[i]\
        \ = v1 if v1 < v2 else v2\n                v1, v2 = st_max_prev[i], st_max_prev[i\
        \ + offset]\n                st_max_j[i] = v1 if v1 > v2 else v2\n\n       \
        \ logs = [0] * (n + 1)\n        for i in range(2, n + 1):\n            logs[i]\
        \ = logs[i >> 1] + 1\n\n        def query(l, r):\n            j = logs[r - l\
        \ + 1]\n            offset = (1 << j)\n            mn = min(st_min[j][l], st_min[j][r\
        \ - offset + 1])\n            mx = max(st_max[j][l], st_max[j][r - offset +\
        \ 1])\n            return mx - mn\n\n        h = []\n        for i in range(n):\n\
        \            val = query(i, n - 1)\n            h.append((-val, i, n - 1))\n\
        \        heapq.heapify(h)\n\n        total = 0\n        for _ in range(k):\n\
        \            if not h:\n                break\n            neg_val, l, r = heapq.heappop(h)\n\
        \            total += -neg_val\n            if r > l:\n                new_r\
        \ = r - 1\n                new_val = query(l, new_r)\n                heapq.heappush(h,\
        \ (-new_val, l, new_r))\n\n        return total"
      c: "#include <stdlib.h>\n#include <string.h>\n\ntypedef struct {\n    int val;\n\
        \    int l;\n    int r;\n} Node;\n\nvoid heapifyDown(Node* heap, int size, int\
        \ i) {\n    while (1) {\n        int largest = i;\n        int left = 2 * i\
        \ + 1;\n        int right = 2 * i + 2;\n        if (left < size && heap[left].val\
        \ > heap[largest].val) largest = left;\n        if (right < size && heap[right].val\
        \ > heap[largest].val) largest = right;\n        if (largest == i) break;\n\
        \        Node temp = heap[i];\n        heap[i] = heap[largest];\n        heap[largest]\
        \ = temp;\n        i = largest;\n    }\n}\n\nvoid heapifyUp(Node* heap, int\
        \ i) {\n    while (i > 0) {\n        int parent = (i - 1) / 2;\n        if (heap[i].val\
        \ > heap[parent].val) {\n            Node temp = heap[i];\n            heap[i]\
        \ = heap[parent];\n            heap[parent] = temp;\n            i = parent;\n\
        \        } else break;\n    }\n}\n\nint query(int l, int r, int* st_min, int*\
        \ st_max, int* logs, int n) {\n    int len = r - l + 1;\n    int j = logs[len];\n\
        \    int offset = 1 << j;\n    int min1 = st_min[j * n + l];\n    int min2 =\
        \ st_min[j * n + r - offset + 1];\n    int mn = min1 < min2 ? min1 : min2;\n\
        \    int max1 = st_max[j * n + l];\n    int max2 = st_max[j * n + r - offset\
        \ + 1];\n    int mx = max1 > max2 ? max1 : max2;\n    return mx - mn;\n}\n\n\
        long long maxTotalValue(int* nums, int numsSize, int k) {\n    int n = numsSize;\n\
        \    int log_n = 0;\n    while ((1 << log_n) <= n) log_n++;\n    int* st_min\
        \ = (int*)malloc(log_n * n * sizeof(int));\n    int* st_max = (int*)malloc(log_n\
        \ * n * sizeof(int));\n    int* logs = (int*)malloc((n + 1) * sizeof(int));\n\
        \    for (int i = 0; i < n; i++) {\n        st_min[i] = nums[i];\n        st_max[i]\
        \ = nums[i];\n    }\n    for (int j = 1; j < log_n; j++) {\n        int offset\
        \ = 1 << (j - 1);\n        for (int i = 0; i + (1 << j) <= n; i++) {\n     \
        \       int m1 = st_min[(j - 1) * n + i];\n            int m2 = st_min[(j -\
        \ 1) * n + i + offset];\n            st_min[j * n + i] = m1 < m2 ? m1 : m2;\n\
        \            int x1 = st_max[(j - 1) * n + i];\n            int x2 = st_max[(j\
        \ - 1) * n + i + offset];\n            st_max[j * n + i] = x1 > x2 ? x1 : x2;\n\
        \        }\n    }\n    logs[1] = 0;\n    for (int i = 2; i <= n; i++) logs[i]\
        \ = logs[i / 2] + 1;\n    Node* heap = (Node*)malloc(n * sizeof(Node));\n  \
        \  int heapSize = 0;\n    for (int i = 0; i < n; i++) {\n        heap[i].l =\
        \ i;\n        heap[i].r = n - 1;\n        heap[i].val = query(i, n - 1, st_min,\
        \ st_max, logs, n);\n    }\n    heapSize = n;\n    for (int i = (n / 2) - 1;\
        \ i >= 0; i--) heapifyDown(heap, heapSize, i);\n    long long total = 0;\n \
        \   for (int i = 0; i < k; i++) {\n        if (heapSize == 0) break;\n     \
        \   Node top = heap[0];\n        total += top.val;\n        if (top.r > top.l)\
        \ {\n            top.r--;\n            top.val = query(top.l, top.r, st_min,\
        \ st_max, logs, n);\n            heap[0] = top;\n            heapifyDown(heap,\
        \ heapSize, 0);\n        } else {\n            heap[0] = heap[heapSize - 1];\n\
        \            heapSize--;\n            heapifyDown(heap, heapSize, 0);\n    \
        \    }\n    }\n    free(st_min); free(st_max); free(logs); free(heap);\n   \
        \ return total;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public class Node {\n        public int Val { get; set; }\n       \
        \ public int L { get; set; }\n        public int R { get; set; }\n    }\n\n\
        \    public long MaxTotalValue(int[] nums, int k) {\n        int n = nums.Length;\n\
        \        int logN = 0;\n        while ((1 << logN) <= n) logN++;\n        int[][]\
        \ stMin = new int[logN][];\n        int[][] stMax = new int[logN][];\n     \
        \   for (int j = 0; j < logN; j++) {\n            stMin[j] = new int[n];\n \
        \           stMax[j] = new int[n];\n        }\n        for (int i = 0; i < n;\
        \ i++) {\n            stMin[0][i] = nums[i];\n            stMax[0][i] = nums[i];\n\
        \        }\n        for (int j = 1; j < logN; j++) {\n            int offset\
        \ = 1 << (j - 1);\n            for (int i = 0; i + (1 << j) <= n; i++) {\n \
        \               stMin[j][i] = Math.Min(stMin[j - 1][i], stMin[j - 1][i + offset]);\n\
        \                stMax[j][i] = Math.Max(stMax[j - 1][i], stMax[j - 1][i + offset]);\n\
        \            }\n        }\n        int[] logs = new int[n + 1];\n        for\
        \ (int i = 2; i <= n; i++) logs[i] = logs[i / 2] + 1;\n\n        Func<int, int,\
        \ int> query = (l, r) => {\n            int len = r - l + 1;\n            int\
        \ j = logs[len];\n            int offset = 1 << j;\n            int mn = Math.Min(stMin[j][l],\
        \ stMin[j][r - offset + 1]);\n            int mx = Math.Max(stMax[j][l], stMax[j][r\
        \ - offset + 1]);\n            return mx - mn;\n        };\n\n        var pq\
        \ = new PriorityQueue<Node, int>(Comparer<int>.Create((a, b) => b.CompareTo(a)));\n\
        \        for (int i = 0; i < n; i++) {\n            int val = query(i, n - 1);\n\
        \            pq.Enqueue(new Node { Val = val, L = i, R = n - 1 }, val);\n  \
        \      }\n\n        long total = 0;\n        for (int i = 0; i < k; i++) {\n\
        \            if (pq.Count == 0) break;\n            var node = pq.Dequeue();\n\
        \            total += node.Val;\n            if (node.R > node.L) {\n      \
        \          node.R--;\n                node.Val = query(node.L, node.R);\n  \
        \              pq.Enqueue(node, node.Val);\n            }\n        }\n     \
        \   return total;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @return\
        \ {number}\n */\nvar maxTotalValue = function(nums, k) {\n    const n = nums.length;\n\
        \    let logN = 0;\n    while ((1 << logN) <= n) logN++;\n    const stMin =\
        \ Array.from({ length: logN }, () => new Int32Array(n));\n    const stMax =\
        \ Array.from({ length: logN }, () => new Int32Array(n));\n    for (let i = 0;\
        \ i < n; i++) {\n        stMin[0][i] = nums[i];\n        stMax[0][i] = nums[i];\n\
        \    }\n    for (let j = 1; j < logN; j++) {\n        const offset = 1 << (j\
        \ - 1);\n        for (let i = 0; i + (1 << j) <= n; i++) {\n            stMin[j][i]\
        \ = Math.min(stMin[j - 1][i], stMin[j - 1][i + offset]);\n            stMax[j][i]\
        \ = Math.max(stMax[j - 1][i], stMax[j - 1][i + offset]);\n        }\n    }\n\
        \    const logs = new Int32Array(n + 1);\n    for (let i = 2; i <= n; i++) logs[i]\
        \ = logs[i >> 1] + 1;\n    const query = (l, r) => {\n        const j = logs[r\
        \ - l + 1];\n        const offset = 1 << j;\n        const mn = Math.min(stMin[j][l],\
        \ stMin[j][r - offset + 1]);\n        const mx = Math.max(stMax[j][l], stMax[j][r\
        \ - offset + 1]);\n        return mx - mn;\n    };\n    class MaxHeap {\n  \
        \      constructor() { this.heap = []; }\n        push(node) {\n           \
        \ this.heap.push(node);\n            let idx = this.heap.length - 1;\n     \
        \       const el = this.heap[idx];\n            while (idx > 0) {\n        \
        \        let parentIdx = (idx - 1) >> 1;\n                let parent = this.heap[parentIdx];\n\
        \                if (el.val <= parent.val) break;\n                this.heap[idx]\
        \ = parent; idx = parentIdx;\n            }\n            this.heap[idx] = el;\n\
        \        }\n        pop() {\n            if (this.heap.length === 0) return\
        \ null;\n            const top = this.heap[0], last = this.heap.pop();\n   \
        \         if (this.heap.length > 0) {\n                this.heap[0] = last;\
        \ this.bubbleDown();\n            }\n            return top;\n        }\n  \
        \      bubbleDown() {\n            let idx = 0, el = this.heap[0], len = this.heap.length;\n\
        \            while (true) {\n                let lIdx = (idx << 1) + 1, rIdx\
        \ = (idx << 1) + 2, swap = null;\n                if (lIdx < len && this.heap[lIdx].val\
        \ > el.val) swap = lIdx;\n                if (rIdx < len && this.heap[rIdx].val\
        \ > (swap === null ? el.val : this.heap[lIdx].val)) swap = rIdx;\n         \
        \       if (swap === null) break;\n                this.heap[idx] = this.heap[swap];\
        \ idx = swap;\n            }\n            this.heap[idx] = el;\n        }\n\
        \    }\n    const heap = new MaxHeap();\n    for (let i = 0; i < n; i++) heap.push({\
        \ val: query(i, n - 1), l: i, r: n - 1 });\n    let total = 0;\n    for (let\
        \ i = 0; i < k; i++) {\n        const node = heap.pop();\n        if (!node)\
        \ break;\n        total += node.val;\n        if (node.r > node.l) {\n     \
        \       node.r--; node.val = query(node.l, node.r);\n            heap.push(node);\n\
        \        }\n    }\n    return total;\n};"
      typescript: "class MaxHeap {\n    private heap: { v: number; l: number; r: number\
        \ }[] = [];\n\n    push(node: { v: number; l: number; r: number }) {\n     \
        \   this.heap.push(node);\n        let i = this.heap.length - 1;\n        while\
        \ (i > 0) {\n            let p = (i - 1) >> 1;\n            if (this.heap[p].v\
        \ >= this.heap[i].v) break;\n            this.swap(p, i);\n            i = p;\n\
        \        }\n    }\n\n    pop(): { v: number; l: number; r: number } | undefined\
        \ {\n        if (this.heap.length === 0) return undefined;\n        if (this.heap.length\
        \ === 1) return this.heap.pop();\n        const root = this.heap[0];\n     \
        \   this.heap[0] = this.heap.pop()!;\n        this.bubbleDown(0);\n        return\
        \ root;\n    }\n\n    private bubbleDown(i: number) {\n        while (true)\
        \ {\n            let l = (i << 1) + 1;\n            let r = (i << 1) + 2;\n\
        \            let s = i;\n            if (l < this.heap.length && this.heap[l].v\
        \ > this.heap[s].v) s = l;\n            if (r < this.heap.length && this.heap[r].v\
        \ > this.heap[s].v) s = r;\n            if (s === i) break;\n            this.swap(i,\
        \ s);\n            i = s;\n        }\n    }\n\n    private swap(i: number, j:\
        \ number) {\n        const temp = this.heap[i];\n        this.heap[i] = this.heap[j];\n\
        \        this.heap[j] = temp;\n    }\n\n    size(): number {\n        return\
        \ this.heap.length;\n    }\n}\n\nfunction maxTotalValue(nums: number[], k: number):\
        \ number {\n    const n = nums.length;\n    const logs = new Int32Array(n +\
        \ 1);\n    for (let i = 2; i <= n; i++) logs[i] = logs[i >> 1] + 1;\n\n    const\
        \ maxLog = logs[n];\n    const stMax = Array.from({ length: maxLog + 1 }, ()\
        \ => new Int32Array(n));\n    const stMin = Array.from({ length: maxLog + 1\
        \ }, () => new Int32Array(n));\n\n    for (let i = 0; i < n; i++) {\n      \
        \  stMax[0][i] = nums[i];\n        stMin[0][i] = nums[i];\n    }\n\n    for\
        \ (let j = 1; j <= maxLog; j++) {\n        const half = 1 << (j - 1);\n    \
        \    for (let i = 0; i <= n - (1 << j); i++) {\n            stMax[j][i] = Math.max(stMax[j\
        \ - 1][i], stMax[j - 1][i + half]);\n            stMin[j][i] = Math.min(stMin[j\
        \ - 1][i], stMin[j - 1][i + half]);\n        }\n    }\n\n    const getV = (l:\
        \ number, r: number): number => {\n        const len = r - l + 1;\n        const\
        \ j = logs[len];\n        const mx = Math.max(stMax[j][l], stMax[j][r - (1 <<\
        \ j) + 1]);\n        const mn = Math.min(stMin[j][l], stMin[j][r - (1 << j)\
        \ + 1]);\n        return mx - mn;\n    };\n\n    const pq = new MaxHeap();\n\
        \    for (let l = 0; l < n; l++) {\n        const v = getV(l, n - 1);\n    \
        \    pq.push({ v, l, r: n - 1 });\n    }\n\n    let totalValue = 0;\n    while\
        \ (k > 0 && pq.size() > 0) {\n        const top = pq.pop()!;\n        totalValue\
        \ += top.v;\n        if (top.r > top.l) {\n            const nv = getV(top.l,\
        \ top.r - 1);\n            pq.push({ v: nv, l: top.l, r: top.r - 1 });\n   \
        \     }\n        k--;\n    }\n\n    return totalValue;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $k\n     * @return Integer\n     */\n    function maxTotalValue($nums,\
        \ $k) {\n        $n = count($nums);\n        $logs = new SplFixedArray($n +\
        \ 1);\n        for ($i = 2; $i <= $n; $i++) {\n            $logs[$i] = $logs[$i\
        \ >> 1] + 1;\n        }\n\n        $maxLog = $logs[$n];\n        $stMax = new\
        \ SplFixedArray($maxLog + 1);\n        $stMin = new SplFixedArray($maxLog +\
        \ 1);\n\n        for ($j = 0; $j <= $maxLog; $j++) {\n            $stMax[$j]\
        \ = new SplFixedArray($n);\n            $stMin[$j] = new SplFixedArray($n);\n\
        \        }\n\n        for ($i = 0; $i < $n; $i++) {\n            $stMax[0][$i]\
        \ = $nums[$i];\n            $stMin[0][$i] = $nums[$i];\n        }\n\n      \
        \  for ($j = 1; $j <= $maxLog; $j++) {\n            $half = 1 << ($j - 1);\n\
        \            for ($i = 0; $i <= $n - (1 << $j); $i++) {\n                $stMax[$j][$i]\
        \ = max($stMax[$j - 1][$i], $stMax[$j - 1][$i + $half]);\n                $stMin[$j][$i]\
        \ = min($stMin[$j - 1][$i], $stMin[$j - 1][$i + $half]);\n            }\n  \
        \      }\n\n        $getV = function($l, $r) use ($stMax, $stMin, $logs) {\n\
        \            $len = $r - $l + 1;\n            $j = $logs[$len];\n          \
        \  $mx = max($stMax[$j][$l], $stMax[$j][$r - (1 << $j) + 1]);\n            $mn\
        \ = min($stMin[$j][$l], $stMin[$j][$r - (1 << $j) + 1]);\n            return\
        \ $mx - $mn;\n        };\n\n        $pq = new SplPriorityQueue();\n        for\
        \ ($l = 0; $l < $n; $l++) {\n            $v = $getV($l, $n - 1);\n         \
        \   $pq->insert([$l, $n - 1, $v], $v);\n        }\n\n        $totalValue = 0;\n\
        \        while ($k > 0 && !$pq->isEmpty()) {\n            $top = $pq->extract();\n\
        \            $l = $top[0];\n            $r = $top[1];\n            $v = $top[2];\n\
        \            $totalValue += $v;\n            if ($r > $l) {\n              \
        \  $nv = $getV($l, $r - 1);\n                $pq->insert([$l, $r - 1, $nv],\
        \ $nv);\n            }\n            $k--;\n        }\n\n        return $totalValue;\n\
        \    }\n}"
      swift: "class Solution {\n    struct MaxHeap {\n        var heap: [(v: Int, l:\
        \ Int, r: Int)] = []\n\n        mutating func push(_ val: (v: Int, l: Int, r:\
        \ Int)) {\n            heap.append(val)\n            var i = heap.count - 1\n\
        \            while i > 0 {\n                let p = (i - 1) / 2\n          \
        \      if heap[i].v <= heap[p].v { break }\n                heap.swapAt(i, p)\n\
        \                i = p\n            }\n        }\n\n        mutating func pop()\
        \ -> (v: Int, l: Int, r: Int)? {\n            if heap.isEmpty { return nil }\n\
        \            if heap.count == 1 { return heap.removeLast() }\n            let\
        \ root = heap[0]\n            heap[0] = heap.removeLast()\n            var i\
        \ = 0\n            while true {\n                let l = i * 2 + 1\n       \
        \         let r = i * 2 + 2\n                var s = i\n                if l\
        \ < heap.count && heap[l].v > heap[s].v { s = l }\n                if r < heap.count\
        \ && heap[r].v > heap[s].v { s = r }\n                if s == i { break }\n\
        \                heap.swapAt(i, s)\n                i = s\n            }\n \
        \           return root\n        }\n\n        func isEmpty() -> Bool {\n   \
        \         return heap.isEmpty\n        }\n    }\n\n    func maxTotalValue(_\
        \ nums: [Int], _ k: Int) -> Int {\n        let n = nums.count\n        var logs\
        \ = [Int](repeating: 0, count: n + 1)\n        for i in 2...n { logs[i] = logs[i\
        \ >> 1] + 1 }\n\n        let maxLog = logs[n]\n        var stMax = Array(repeating:\
        \ [Int](repeating: 0, count: n), count: maxLog + 1)\n        var stMin = Array(repeating:\
        \ [Int](repeating: 0, count: n), count: maxLog + 1)\n\n        for i in 0..<n\
        \ {\n            stMax[0][i] = nums[i]\n            stMin[0][i] = nums[i]\n\
        \        }\n\n        if maxLog > 0 {\n            for j in 1...maxLog {\n \
        \               let half = 1 << (j - 1)\n                for i in 0...(n - (1\
        \ << j)) {\n                    stMax[j][i] = max(stMax[j - 1][i], stMax[j -\
        \ 1][i + half])\n                    stMin[j][i] = min(stMin[j - 1][i], stMin[j\
        \ - 1][i + half])\n                }\n            }\n        }\n\n        func\
        \ getV(_ l: Int, _ r: Int) -> Int {\n            let len = r - l + 1\n     \
        \       let j = logs[len]\n            let mx = max(stMax[j][l], stMax[j][r\
        \ - (1 << j) + 1])\n            let mn = min(stMin[j][l], stMin[j][r - (1 <<\
        \ j) + 1])\n            return mx - mn\n        }\n\n        var pq = MaxHeap()\n\
        \        for l in 0..<n {\n            let v = getV(l, n - 1)\n            pq.push((v:\
        \ v, l: l, r: n - 1))\n        }\n\n        var totalValue = 0\n        var\
        \ remainingK = k\n        while remainingK > 0 && !pq.isEmpty() {\n        \
        \    if let top = pq.pop() {\n                totalValue += top.v\n        \
        \        if top.r > top.l {\n                    let nv = getV(top.l, top.r\
        \ - 1)\n                    pq.push((v: nv, l: top.l, r: top.r - 1))\n     \
        \           }\n            }\n            remainingK -= 1\n        }\n\n   \
        \     return totalValue\n    }\n}"
      kotlin: "import java.util.PriorityQueue\n\nclass Solution {\n    data class Subarray(val\
        \ v: Int, val l: Int, val r: Int)\n\n    fun maxTotalValue(nums: IntArray, k:\
        \ Int): Long {\n        val n = nums.size\n        val logs = IntArray(n + 1)\n\
        \        for (i in 2..n) logs[i] = logs[i shr 1] + 1\n\n        val maxLog =\
        \ logs[n]\n        val stMax = Array(maxLog + 1) { IntArray(n) }\n        val\
        \ stMin = Array(maxLog + 1) { IntArray(n) }\n\n        for (i in 0 until n)\
        \ {\n            stMax[0][i] = nums[i]\n            stMin[0][i] = nums[i]\n\
        \        }\n\n        for (j in 1..maxLog) {\n            val half = 1 shl (j\
        \ - 1)\n            for (i in 0..n - (1 shl j)) {\n                stMax[j][i]\
        \ = maxOf(stMax[j - 1][i], stMax[j - 1][i + half])\n                stMin[j][i]\
        \ = minOf(stMin[j - 1][i], stMin[j - 1][i + half])\n            }\n        }\n\
        \n        fun getV(l: Int, r: Int): Int {\n            val len = r - l + 1\n\
        \            val j = logs[len]\n            val mx = maxOf(stMax[j][l], stMax[j][r\
        \ - (1 shl j) + 1])\n            val mn = minOf(stMin[j][l], stMin[j][r - (1\
        \ shl j) + 1])\n            return mx - mn\n        }\n\n        val pq = PriorityQueue<Subarray>\
        \ { a, b -> b.v.compareTo(a.v) }\n\n        for (l in 0 until n) {\n       \
        \     val v = getV(l, n - 1)\n            pq.add(Subarray(v, l, n - 1))\n  \
        \      }\n\n        var totalValue: Long = 0\n        var count = 0\n      \
        \  while (count < k && pq.isNotEmpty()) {\n            val top = pq.poll()\n\
        \            totalValue += top.v.toLong()\n            if (top.r > top.l) {\n\
        \                val nv = getV(top.l, top.r - 1)\n                pq.add(Subarray(nv,\
        \ top.l, top.r - 1))\n            }\n            count++\n        }\n\n    \
        \    return totalValue\n    }\n}"
      dart: "import 'dart:math' as math;\nimport 'dart:typed_data';\n\nclass Node {\n\
        \  int val, l, r;\n  Node(this.val, this.l, this.r);\n}\n\nclass MaxHeap {\n\
        \  List<Node> _heap = [];\n\n  void push(Node node) {\n    _heap.add(node);\n\
        \    _bubbleUp(_heap.length - 1);\n  }\n\n  Node pop() {\n    if (_heap.isEmpty)\
        \ throw Exception(\"Empty heap\");\n    Node top = _heap[0];\n    Node last\
        \ = _heap.removeLast();\n    if (_heap.isNotEmpty) {\n      _heap[0] = last;\n\
        \      _bubbleDown(0);\n    }\n    return top;\n  }\n\n  void _bubbleUp(int\
        \ idx) {\n    while (idx > 0) {\n      int p = (idx - 1) >> 1;\n      if (_heap[idx].val\
        \ > _heap[p].val) {\n        _swap(idx, p);\n        idx = p;\n      } else\
        \ {\n        break;\n      }\n    }\n  }\n\n  void _bubbleDown(int idx) {\n\
        \    while (true) {\n      int left = (idx << 1) + 1;\n      int right = (idx\
        \ << 1) + 2;\n      int largest = idx;\n      if (left < _heap.length && _heap[left].val\
        \ > _heap[largest].val) {\n        largest = left;\n      }\n      if (right\
        \ < _heap.length && _heap[right].val > _heap[largest].val) {\n        largest\
        \ = right;\n      }\n      if (largest != idx) {\n        _swap(idx, largest);\n\
        \        idx = largest;\n      } else {\n        break;\n      }\n    }\n  }\n\
        \n  void _swap(int i, int j) {\n    Node tmp = _heap[i];\n    _heap[i] = _heap[j];\n\
        \    _heap[j] = tmp;\n  }\n}\n\nclass Solution {\n  int maxTotalValue(List<int>\
        \ nums, int k) {\n    int n = nums.length;\n    Int32List logs = Int32List(n\
        \ + 1);\n    for (int i = 2; i <= n; i++) logs[i] = logs[i >> 1] + 1;\n\n  \
        \  List<Int32List> stMax = List.generate(17, (_) => Int32List(n));\n    List<Int32List>\
        \ stMin = List.generate(17, (_) => Int32List(n));\n\n    for (int i = 0; i <\
        \ n; i++) {\n      stMax[0][i] = nums[i];\n      stMin[0][i] = nums[i];\n  \
        \  }\n\n    for (int j = 1; j < 17; j++) {\n      for (int i = 0; i + (1 <<\
        \ j) <= n; i++) {\n        stMax[j][i] = math.max(stMax[j - 1][i], stMax[j -\
        \ 1][i + (1 << (j - 1))]);\n        stMin[j][i] = math.min(stMin[j - 1][i],\
        \ stMin[j - 1][i + (1 << (j - 1))]);\n      }\n    }\n\n    int query(int l,\
        \ int r) {\n      int j = logs[r - l + 1];\n      int mx = math.max(stMax[j][l],\
        \ stMax[j][r - (1 << j) + 1]);\n      int mn = math.min(stMin[j][l], stMin[j][r\
        \ - (1 << j) + 1]);\n      return mx - mn;\n    }\n\n    MaxHeap pq = MaxHeap();\n\
        \    for (int l = 0; l < n; l++) {\n      pq.push(Node(query(l, n - 1), l, n\
        \ - 1));\n    }\n\n    int totalValue = 0;\n    for (int i = 0; i < k; i++)\
        \ {\n      Node top = pq.pop();\n      totalValue += top.val;\n      if (top.r\
        \ > top.l) {\n        int nextR = top.r - 1;\n        pq.push(Node(query(top.l,\
        \ nextR), top.l, nextR));\n      }\n    }\n\n    return totalValue;\n  }\n}"
      go: "import (\n\t\"container/heap\"\n)\n\ntype Item struct {\n\tval, l, r int\n\
        }\n\ntype PriorityQueue []*Item\n\nfunc (pq PriorityQueue) Len() int       \
        \    { return len(pq) }\nfunc (pq PriorityQueue) Less(i, j int) bool { return\
        \ pq[i].val > pq[j].val }\nfunc (pq PriorityQueue) Swap(i, j int)      { pq[i],\
        \ pq[j] = pq[j], pq[i] }\nfunc (pq *PriorityQueue) Push(x interface{}) {\n\t\
        *pq = append(*pq, x.(*Item))\n}\nfunc (pq *PriorityQueue) Pop() interface{}\
        \ {\n\told := *pq\n\tn := len(old)\n\titem := old[n-1]\n\t*pq = old[0 : n-1]\n\
        \treturn item\n}\n\nfunc maxTotalValue(nums []int, k int) int64 {\n\tn := len(nums)\n\
        \tlogs := make([]int, n+1)\n\tfor i := 2; i <= n; i++ {\n\t\tlogs[i] = logs[i/2]\
        \ + 1\n\t}\n\n\tstMax := make([][]int, 17)\n\tstMin := make([][]int, 17)\n\t\
        for i := range stMax {\n\t\tstMax[i] = make([]int, n)\n\t\tstMin[i] = make([]int,\
        \ n)\n\t}\n\n\tfor i := 0; i < n; i++ {\n\t\tstMax[0][i] = nums[i]\n\t\tstMin[0][i]\
        \ = nums[i]\n\t}\n\n\tfor j := 1; j < 17; j++ {\n\t\tfor i := 0; i+(1<<j) <=\
        \ n; i++ {\n\t\t\tmx1, mx2 := stMax[j-1][i], stMax[j-1][i+(1<<(j-1))]\n\t\t\t\
        if mx1 > mx2 { stMax[j][i] = mx1 } else { stMax[j][i] = mx2 }\n\t\t\tmn1, mn2\
        \ := stMin[j-1][i], stMin[j-1][i+(1<<(j-1))]\n\t\t\tif mn1 < mn2 { stMin[j][i]\
        \ = mn1 } else { stMin[j][i] = mn2 }\n\t\t}\n\t}\n\n\tquery := func(l, r int)\
        \ int {\n\t\tj := logs[r-l+1]\n\t\tmx1, mx2 := stMax[j][l], stMax[j][r-(1<<j)+1]\n\
        \t\tmn1, mn2 := stMin[j][l], stMin[j][r-(1<<j)+1]\n\t\tmx, mn := mx1, mn1\n\t\
        \tif mx2 > mx { mx = mx2 }\n\t\tif mn2 < mn { mn = mn2 }\n\t\treturn mx - mn\n\
        \t}\n\n\tpq := make(PriorityQueue, 0, n)\n\theap.Init(&pq)\n\tfor l := 0; l\
        \ < n; l++ {\n\t\theap.Push(&pq, &Item{query(l, n-1), l, n-1})\n\t}\n\n\tvar\
        \ totalValue int64 = 0\n\tfor i := 0; i < k; i++ {\n\t\titem := heap.Pop(&pq).(*Item)\n\
        \t\ttotalValue += int64(item.val)\n\t\tif item.r > item.l {\n\t\t\tnextR :=\
        \ item.r - 1\n\t\t\theap.Push(&pq, &Item{query(item.l, nextR), item.l, nextR})\n\
        \t\t}\n\t}\n\n\treturn totalValue\n}"
      ruby: "class MaxHeap\n  def initialize\n    @heap = []\n  end\n  def push(node)\n\
        \    @heap << node\n    bubble_up(@heap.size - 1)\n  end\n  def pop\n    return\
        \ nil if @heap.empty?\n    if @heap.size == 1\n      return @heap.pop\n    end\n\
        \    res = @heap[0]\n    @heap[0] = @heap.pop\n    bubble_down(0)\n    res\n\
        \  end\n  def bubble_up(idx)\n    while idx > 0\n      p = (idx - 1) / 2\n \
        \     if @heap[idx][0] > @heap[p][0]\n        @heap[idx], @heap[p] = @heap[p],\
        \ @heap[idx]\n        idx = p\n      else\n        break\n      end\n    end\n\
        \  end\n  def bubble_down(idx)\n    while true\n      l = 2 * idx + 1\n    \
        \  r = 2 * idx + 2\n      largest = idx\n      if l < @heap.size && @heap[l][0]\
        \ > @heap[largest][0]\n        largest = l\n      end\n      if r < @heap.size\
        \ && @heap[r][0] > @heap[largest][0]\n        largest = r\n      end\n     \
        \ if largest != idx\n        @heap[idx], @heap[largest] = @heap[largest], @heap[idx]\n\
        \        idx = largest\n      else\n        break\n      end\n    end\n  end\n\
        end\n\ndef max_total_value(nums, k)\n  n = nums.length\n  logs = Array.new(n\
        \ + 1, 0)\n  (2..n).each { |i| logs[i] = logs[i / 2] + 1 }\n\n  st_max = Array.new(17)\
        \ { Array.new(n, 0) }\n  st_min = Array.new(17) { Array.new(n, 0) }\n  (0...n).each\
        \ do |i|\n    st_max[0][i] = nums[i]\n    st_min[0][i] = nums[i]\n  end\n\n\
        \  (1...17).each do |j|\n    (0..(n - (1 << j))).each do |i|\n      mx1, mx2\
        \ = st_max[j - 1][i], st_max[j - 1][i + (1 << (j - 1))]\n      st_max[j][i]\
        \ = mx1 > mx2 ? mx1 : mx2\n      mn1, mn2 = st_min[j - 1][i], st_min[j - 1][i\
        \ + (1 << (j - 1))]\n      st_min[j][i] = mn1 < mn2 ? mn1 : mn2\n    end\n \
        \ end\n\n  query = lambda do |l, r|\n    j = logs[r - l + 1]\n    mx1, mx2 =\
        \ st_max[j][l], st_max[j][r - (1 << j) + 1]\n    mx = mx1 > mx2 ? mx1 : mx2\n\
        \    mn1, mn2 = st_min[j][l], st_min[j][r - (1 << j) + 1]\n    mn = mn1 < mn2\
        \ ? mn1 : mn2\n    mx - mn\n  end\n\n  pq = MaxHeap.new\n  (0...n).each do |l|\n\
        \    pq.push([query.call(l, n - 1), l, n - 1])\n  end\n\n  total_value = 0\n\
        \  k.times do\n    top = pq.pop\n    val, l, r = top\n    total_value += val\n\
        \    if r > l\n      nr = r - 1\n      pq.push([query.call(l, nr), l, nr])\n\
        \    end\n  end\n\n  total_value\nend"
      scala: "import scala.collection.mutable.PriorityQueue\n\nobject Solution {\n \
        \ case class Item(v: Int, l: Int, r: Int)\n\n  def maxTotalValue(nums: Array[Int],\
        \ k: Int): Long = {\n    val n = nums.length\n    val logs = new Array[Int](n\
        \ + 1)\n    for (i <- 2 to n) logs(i) = logs(i / 2) + 1\n\n    val stMax = Array.ofDim[Int](17,\
        \ n)\n    val stMin = Array.ofDim[Int](17, n)\n\n    for (i <- 0 until n) {\n\
        \      stMax(0)(i) = nums(i)\n      stMin(0)(i) = nums(i)\n    }\n\n    for\
        \ (j <- 1 until 17) {\n      for (i <- 0 to (n - (1 << j))) {\n        stMax(j)(i)\
        \ = math.max(stMax(j - 1)(i), stMax(j - 1)(i + (1 << (j - 1))))\n        stMin(j)(i)\
        \ = math.min(stMin(j - 1)(i), stMin(j - 1)(i + (1 << (j - 1))))\n      }\n \
        \   }\n\n    def query(l: Int, r: Int): Int = {\n      val j = logs(r - l +\
        \ 1)\n      val mx = math.max(stMax(j)(l), stMax(j)(r - (1 << j) + 1))\n   \
        \   val mn = math.min(stMin(j)(l), stMin(j)(r - (1 << j) + 1))\n      mx - mn\n\
        \    }\n\n    val pq = PriorityQueue[Item]()(Ordering.by(_.v))\n    for (l <-\
        \ 0 until n) {\n      pq.enqueue(Item(query(l, n - 1), l, n - 1))\n    }\n\n\
        \    var totalValue: Long = 0\n    for (_ <- 0 until k) {\n      val item =\
        \ pq.dequeue()\n      totalValue += item.v\n      if (item.r > item.l) {\n \
        \       val nextR = item.r - 1\n        pq.enqueue(Item(query(item.l, nextR),\
        \ item.l, nextR))\n      }\n    }\n\n    totalValue\n  }\n}"
      rust: "impl Solution {\n    pub fn max_total_value(nums: Vec<i32>, k: i32) ->\
        \ i64 {\n        let n = nums.len();\n        let mut log_table = vec![0; n\
        \ + 1];\n        for i in 2..=n {\n            log_table[i] = log_table[i /\
        \ 2] + 1;\n        }\n        let max_log = log_table[n] as usize;\n       \
        \ let mut st_min = vec![vec![0; n]; max_log + 1];\n        let mut st_max =\
        \ vec![vec![0; n]; max_log + 1];\n        for i in 0..n {\n            st_min[0][i]\
        \ = nums[i];\n            st_max[0][i] = nums[i];\n        }\n        for j\
        \ in 1..=max_log {\n            let p2_prev = 1 << (j - 1);\n            for\
        \ i in 0..=(n - (1 << j)) {\n                st_min[j][i] = st_min[j - 1][i].min(st_min[j\
        \ - 1][i + p2_prev]);\n                st_max[j][i] = st_max[j - 1][i].max(st_max[j\
        \ - 1][i + p2_prev]);\n            }\n        }\n\n        let get_val = |l:\
        \ usize, r: usize, st_min: &Vec<Vec<i32>>, st_max: &Vec<Vec<i32>>, log_table:\
        \ &Vec<usize>| -> i64 {\n            let len = r - l + 1;\n            let j\
        \ = log_table[len];\n            let mn = st_min[j][l].min(st_min[j][r - (1\
        \ << j) + 1]);\n            let mx = st_max[j][l].max(st_max[j][r - (1 << j)\
        \ + 1]);\n            (mx - mn) as i64\n        };\n\n        let mut pq = std::collections::BinaryHeap::new();\n\
        \        for l in 0..n {\n            pq.push((get_val(l, n - 1, &st_min, &st_max,\
        \ &log_table), l, n - 1));\n        }\n\n        let mut total_value = 0i64;\n\
        \        let mut k_rem = k;\n        while k_rem > 0 {\n            if let Some((val,\
        \ l, r)) = pq.pop() {\n                total_value += val;\n               \
        \ if r > l {\n                    pq.push((get_val(l, r - 1, &st_min, &st_max,\
        \ &log_table), l, r - 1));\n                }\n            }\n            k_rem\
        \ -= 1;\n        }\n        total_value\n    }\n}"
      racket: "(define/contract (max-total-value nums k)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer?)\n  (let* ([n (length nums)]\n         [nums-vec\
        \ (list->vector nums)]\n         [log-table (let ([vec (make-vector (+ n 1)\
        \ 0)])\n                      (for ([i (in-range 2 (+ n 1))])\n            \
        \            (vector-set! vec i (+ (vector-ref vec (quotient i 2)) 1)))\n  \
        \                    vec)]\n         [max-log (vector-ref log-table n)]\n  \
        \       [st-min (let ([st (make-vector (+ max-log 1))])\n                  \
        \ (vector-set! st 0 nums-vec)\n                   (for ([j (in-range 1 (+ max-log\
        \ 1))])\n                     (let* ([p2-prev (arithmetic-shift 1 (- j 1))]\n\
        \                            [len (+ (- n (arithmetic-shift 1 j)) 1)]\n    \
        \                        [curr-level (make-vector len)])\n                 \
        \      (for ([i (in-range len)])\n                         (vector-set! curr-level\
        \ i (min (vector-ref (vector-ref st (- j 1)) i)\n                          \
        \                              (vector-ref (vector-ref st (- j 1)) (+ i p2-prev)))))\n\
        \                       (vector-set! st j curr-level)))\n                  \
        \ st)]\n         [st-max (let ([st (make-vector (+ max-log 1))])\n         \
        \          (vector-set! st 0 nums-vec)\n                   (for ([j (in-range\
        \ 1 (+ max-log 1))])\n                     (let* ([p2-prev (arithmetic-shift\
        \ 1 (- j 1))]\n                            [len (+ (- n (arithmetic-shift 1\
        \ j)) 1)]\n                            [curr-level (make-vector len)])\n   \
        \                    (for ([i (in-range len)])\n                         (vector-set!\
        \ curr-level i (max (vector-ref (vector-ref st (- j 1)) i)\n               \
        \                                         (vector-ref (vector-ref st (- j 1))\
        \ (+ i p2-prev)))))\n                       (vector-set! st j curr-level)))\n\
        \                   st)]\n         [get-val (lambda (l r)\n                \
        \    (let* ([len (+ (- r l) 1)]\n                           [j (vector-ref log-table\
        \ len)]\n                           [p2 (arithmetic-shift 1 j)]\n          \
        \                 [mn (min (vector-ref (vector-ref st-min j) l)\n          \
        \                          (vector-ref (vector-ref st-min j) (+ (- r p2) 1)))]\n\
        \                           [mx (max (vector-ref (vector-ref st-max j) l)\n\
        \                                    (vector-ref (vector-ref st-max j) (+ (-\
        \ r p2) 1)))])\n                      (- mx mn)))]\n         [pq-vec (make-vector\
        \ (+ n 1))]\n         [pq-size 0]\n         [heap-push! (lambda (val)\n    \
        \                   (set! pq-size (+ pq-size 1))\n                       (vector-set!\
        \ pq-vec pq-size val)\n                       (let loop ([curr pq-size])\n \
        \                        (when (> curr 1)\n                           (let ([parent\
        \ (quotient curr 2)])\n                             (when (> (car (vector-ref\
        \ pq-vec curr)) (car (vector-ref pq-vec parent)))\n                        \
        \       (let ([tmp (vector-ref pq-vec curr)])\n                            \
        \     (vector-set! pq-vec curr (vector-ref pq-vec parent))\n               \
        \                  (vector-set! pq-vec parent tmp)\n                       \
        \          (loop parent)))))))]\n         [heap-pop! (lambda ()\n          \
        \            (let ([top (vector-ref pq-vec 1)])\n                        (vector-set!\
        \ pq-vec 1 (vector-ref pq-vec pq-size))\n                        (set! pq-size\
        \ (- pq-size 1))\n                        (let loop ([curr 1])\n           \
        \               (let* ([left (* curr 2)]\n                                 [right\
        \ (+ (* curr 2) 1)]\n                                 [largest curr])\n    \
        \                        (let* ([largest (if (and (<= left pq-size) (> (car\
        \ (vector-ref pq-vec left)) (car (vector-ref pq-vec largest)))) left largest)]\n\
        \                                   [largest (if (and (<= right pq-size) (>\
        \ (car (vector-ref pq-vec right)) (car (vector-ref pq-vec largest)))) right\
        \ largest)])\n                              (when (not (= largest curr))\n \
        \                               (let ([tmp (vector-ref pq-vec curr)])\n    \
        \                              (vector-set! pq-vec curr (vector-ref pq-vec largest))\n\
        \                                  (vector-set! pq-vec largest tmp)\n      \
        \                            (loop largest))))))\n                        top))])\n\
        \    (for ([l (in-range n)])\n      (heap-push! (list (get-val l (- n 1)) l\
        \ (- n 1))))\n    (let loop ([k-rem k] [total 0])\n      (if (> k-rem 0)\n \
        \         (let* ([node (heap-pop!)]\n                 [val (car node)]\n   \
        \              [l (cadr node)]\n                 [r (caddr node)])\n       \
        \     (if (> r l)\n                (heap-push! (list (get-val l (- r 1)) l (-\
        \ r 1)))\n                (void))\n            (loop (- k-rem 1) (+ total val)))\n\
        \          total))))"
      erlang: "-spec max_total_value(Nums :: [integer()], K :: integer()) -> integer().\n\
        max_total_value(Nums, K) ->\n    N = length(Nums),\n    NumsTuple = list_to_tuple(Nums),\n\
        \    LogTable = build_log_table(N),\n    MaxLog = get_max_log(N),\n    STMin\
        \ = build_st_min(NumsTuple, N, MaxLog),\n    STMax = build_st_max(NumsTuple,\
        \ N, MaxLog),\n    GetVal = fun(L, R) ->\n        Len = R - L + 1,\n       \
        \ J = element(Len, LogTable),\n        P2 = 1 bsl J,\n        Mn = min(element(L\
        \ + 1, element(J + 1, STMin)), element(R - P2 + 2, element(J + 1, STMin))),\n\
        \        Mx = max(element(L + 1, element(J + 1, STMax)), element(R - P2 + 2,\
        \ element(J + 1, STMax))),\n        Mx - Mn\n    end,\n    InitialHeap = lists:foldl(fun(L,\
        \ Acc) ->\n        Val = GetVal(L, N - 1),\n        gb_trees:enter({-Val, L,\
        \ N - 1}, true, Acc)\n    end, gb_trees:empty(), lists:seq(0, N - 1)),\n   \
        \ solve(InitialHeap, K, GetVal, 0).\n\nget_max_log(N) when N =< 1 -> 0;\nget_max_log(N)\
        \ -> 1 + get_max_log(N div 2).\n\nbuild_log_table(N) ->\n    list_to_tuple(lists:reverse(build_log_table_list(2,\
        \ N, [0]))).\n\nbuild_log_table_list(I, N, [H | _] = Acc) when I =< N ->\n \
        \   if I < (1 bsl (H + 1)) ->\n        build_log_table_list(I + 1, N, [H | Acc]);\n\
        \    true ->\n        build_log_table_list(I + 1, N, [H + 1 | Acc])\n    end;\n\
        build_log_table_list(_, _, Acc) -> Acc.\n\nbuild_st_min(NumsTuple, N, MaxLog)\
        \ ->\n    build_st_levels(1, MaxLog, [NumsTuple], N, fun(A, B) -> min(A, B)\
        \ end).\n\nbuild_st_max(NumsTuple, N, MaxLog) ->\n    build_st_levels(1, MaxLog,\
        \ [NumsTuple], N, fun(A, B) -> max(A, B) end).\n\nbuild_st_levels(J, MaxLog,\
        \ [Prev | _] = Levels, N, Op) when J =< MaxLog ->\n    P2Prev = 1 bsl (J - 1),\n\
        \    Limit = N - (1 bsl J) + 1,\n    NewLevel = list_to_tuple([Op(element(I,\
        \ Prev), element(I + P2Prev, Prev)) || I <- lists:seq(1, Limit)]),\n    build_st_levels(J\
        \ + 1, MaxLog, [NewLevel | Levels], N, Op);\nbuild_st_levels(_, _, Levels, _,\
        \ _) ->\n    list_to_tuple(lists:reverse(Levels)).\n\nsolve(_, 0, _, Acc) ->\
        \ Acc;\nsolve(Heap, K, GetVal, Acc) ->\n    {{ValNeg, L, R}, _, NewHeap} = gb_trees:take_smallest(Heap),\n\
        \    Val = -ValNeg,\n    if R > L ->\n        NextVal = GetVal(L, R - 1),\n\
        \        solve(gb_trees:enter({-NextVal, L, R - 1}, true, NewHeap), K - 1, GetVal,\
        \ Acc + Val);\n    true ->\n        solve(NewHeap, K - 1, GetVal, Acc + Val)\n\
        \    end."
      elixir: "defmodule Solution do\n  use Bitwise\n\n  @spec max_total_value(nums\
        \ :: [integer], k :: integer) :: integer\n  def max_total_value(nums, k) do\n\
        \    n = length(nums)\n    nums_tuple = List.to_tuple(nums)\n    log_table =\
        \ build_log_table(n)\n    max_log = get_max_log(n)\n    st_min = build_st_min(nums_tuple,\
        \ n, max_log)\n    st_max = build_st_max(nums_tuple, n, max_log)\n\n    get_val\
        \ = fn l, r ->\n      len = r - l + 1\n      j = elem(log_table, len - 1)\n\
        \      p2 = Bitwise.bsl(1, j)\n      mn = min(elem(elem(st_min, j), l), elem(elem(st_min,\
        \ j), r - p2 + 1))\n      mx = max(elem(elem(st_max, j), l), elem(elem(st_max,\
        \ j), r - p2 + 1))\n      mx - mn\n    end\n\n    initial_heap = Enum.reduce(0..(n\
        \ - 1), :gb_trees.empty(), fn l, acc ->\n      val = get_val.(l, n - 1)\n  \
        \    :gb_trees.enter({-val, l, n - 1}, true, acc)\n    end)\n\n    solve(initial_heap,\
        \ k, get_val, 0)\n  end\n\n  defp get_max_log(n) when n <= 1, do: 0\n  defp\
        \ get_max_log(n), do: 1 + get_max_log(div(n, 2))\n\n  defp build_log_table(n)\
        \ do\n    Enum.reduce(2..n, [0], fn i, [h | _] = acc ->\n      if i < Bitwise.bsl(1,\
        \ h + 1) do\n        [h | acc]\n      else\n        [h + 1 | acc]\n      end\n\
        \    end)\n    |> Enum.reverse()\n    |> List.to_tuple()\n  end\n\n  defp build_st_min(nums_tuple,\
        \ n, max_log), do: build_st_levels(1, max_log, [nums_tuple], n, &min/2)\n  defp\
        \ build_st_max(nums_tuple, n, max_log), do: build_st_levels(1, max_log, [nums_tuple],\
        \ n, &max/2)\n\n  defp build_st_levels(j, max_log, [prev | _] = levels, n, op)\
        \ when j <= max_log do\n    p2_prev = Bitwise.bsl(1, j - 1)\n    limit = n -\
        \ Bitwise.bsl(1, j) + 1\n    new_level = Enum.map(1..limit, fn i -> op.(elem(prev,\
        \ i - 1), elem(prev, i + p2_prev - 1)) end) |> List.to_tuple()\n    build_st_levels(j\
        \ + 1, max_log, [new_level | levels], n, op)\n  end\n  defp build_st_levels(_,\
        \ _, levels, _, _), do: Enum.reverse(levels) |> List.to_tuple()\n\n  defp solve(_heap,\
        \ 0, _get_val, acc), do: acc\n  defp solve(heap, k, get_val, acc) do\n    {{val_neg,\
        \ l, r}, _, new_heap} = :gb_trees.take_smallest(heap)\n    val = -val_neg\n\
        \    if r > l do\n      next_val = get_val.(l, r - 1)\n      solve(:gb_trees.enter({-next_val,\
        \ l, r - 1}, true, new_heap), k - 1, get_val, acc + val)\n    else\n      solve(new_heap,\
        \ k - 1, get_val, acc + val)\n    end\n  end\nend"
    approach: 'The problem asks for the maximum sum of values from exactly $k$ distinct
      subarrays, where the value of a subarray is $max(nums[l..r]) - min(nums[l..r])$.
      A key observation is that for a fixed starting index $l$, as the end index $r$
      decreases, the range maximum non-increases and the range minimum non-decreases.
      Consequently, the subarray value $v(l, r)$ is monotonically non-decreasing with
      respect to $r$ for a fixed $l$. This monotonicity allows us to utilize a greedy
      approach with a max-heap to extract the $k$ largest values efficiently.


      To compute $v(l, r)$ in $O(1)$ time, we precompute a Sparse Table for both Range
      Maximum Query (RMQ) and Range Minimum Query. We initialize a max-priority queue
      with the largest possible value for each starting index $l$, which is $v(l, n-1)$.
      In each of the $k$ steps, we extract the maximum value $(v, l, r)$ from the heap,
      add it to our total, and if $r > l$, we calculate the value of the next candidate
      for that starting index, $v(l, r-1)$, and push it back into the heap. This ensures
      we always consider the next largest available subarray value while maintaining
      a heap size of at most $n$.'
    time_complexity: O((n + k) \log n). Building the sparse table takes $O(n \log n)$
      time. Initializing the heap with $n$ elements takes $O(n)$ or $O(n \log n)$, and
      extracting the top $k$ elements while performing $k$ pushes takes $O(k \log n)$.
      With $n=5 \times 10^4$ and $k=10^5$, this is well within performance limits.
    space_complexity: O(n \log n). The sparse table requires $O(n \log n)$ space to
      store the max and min values for each power-of-two length. The priority queue
      stores at most $n$ elements, contributing $O(n)$ space.
    elapsed_time: 379.171852350235
    model: gemini-3-flash-preview
    generated_at: '2026-06-10 02:48:47 '
---

## Problem #3691: Maximum Total Subarray Value II

**Difficulty:** Hard

**Topics:** Array, Greedy, Segment Tree, Heap (Priority Queue)

## Problem Description

<p>You are given an integer array <code>nums</code> of length <code>n</code> and an integer <code>k</code>.</p>

<p>You must select <strong>exactly</strong> <code>k</code> <strong>distinct</strong> non-empty <span data-keyword="subarray-nonempty">subarrays</span> <code>nums[l..r]</code> of <code>nums</code>. Subarrays may overlap, but the exact same subarray (same <code>l</code> and <code>r</code>) <strong>cannot</strong> be chosen more than once.</p>

<p>The <strong>value</strong> of a subarray <code>nums[l..r]</code> is defined as: <code>max(nums[l..r]) - min(nums[l..r])</code>.</p>

<p>The <strong>total value</strong> is the sum of the <strong>values</strong> of all chosen subarrays.</p>

<p>Return the <strong>maximum</strong> possible total value you can achieve.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,3,2], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>One optimal approach is:</p>

<ul>
	<li>Choose <code>nums[0..1] = [1, 3]</code>. The maximum is 3 and the minimum is 1, giving a value of <code>3 - 1 = 2</code>.</li>
	<li>Choose <code>nums[0..2] = [1, 3, 2]</code>. The maximum is still 3 and the minimum is still 1, so the value is also <code>3 - 1 = 2</code>.</li>
</ul>

<p>Adding these gives <code>2 + 2 = 4</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,2,5,1], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<p>One optimal approach is:</p>

<ul>
	<li>Choose <code>nums[0..3] = [4, 2, 5, 1]</code>. The maximum is 5 and the minimum is 1, giving a value of <code>5 - 1 = 4</code>.</li>
	<li>Choose <code>nums[1..3] = [2, 5, 1]</code>. The maximum is 5 and the minimum is 1, so the value is also <code>4</code>.</li>
	<li>Choose <code>nums[2..3] = [5, 1]</code>. The maximum is 5 and the minimum is 1, so the value is again <code>4</code>.</li>
</ul>

<p>Adding these gives <code>4 + 4 + 4 = 12</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 5 * 10<sup>​​​​​​​4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= min(10<sup>5</sup>, n * (n + 1) / 2)</code></li>
</ul>


## Hints

1. For fixed `l`, the sequence `v(l,r)=max(nums[l..r])−min(nums[l..r])` is non-increasing as `r` moves left.

2. Build RMQs (sparse tables) for range max/min so each `v(l,r)` is queryable in `O(1)`.

3. Use a max-heap with `v(l,n-1)` for all `l`; pop the largest `k` times, and after popping an entry from `(l,r)` push `(l,r-1)` if `r>l`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the maximum sum of values from exactly $k$ distinct subarrays, where the value of a subarray is $max(nums[l..r]) - min(nums[l..r])$. A key observation is that for a fixed starting index $l$, as the end index $r$ decreases, the range maximum non-increases and the range minimum non-decreases. Consequently, the subarray value $v(l, r)$ is monotonically non-decreasing with respect to $r$ for a fixed $l$. This monotonicity allows us to utilize a greedy approach with a max-heap to extract the $k$ largest values efficiently.

To compute $v(l, r)$ in $O(1)$ time, we precompute a Sparse Table for both Range Maximum Query (RMQ) and Range Minimum Query. We initialize a max-priority queue with the largest possible value for each starting index $l$, which is $v(l, n-1)$. In each of the $k$ steps, we extract the maximum value $(v, l, r)$ from the heap, add it to our total, and if $r > l$, we calculate the value of the next candidate for that starting index, $v(l, r-1)$, and push it back into the heap. This ensures we always consider the next largest available subarray value while maintaining a heap size of at most $n$.

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
    long long maxTotalValue(vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 0) return 0;

        int max_log = 0;
        while ((1 << (max_log + 1)) <= n) max_log++;

        vector<int> logs(n + 1, 0);
        for (int i = 2; i <= n; ++i) logs[i] = logs[i >> 1] + 1;

        vector<vector<int>> st_max(max_log + 1, vector<int>(n));
        vector<vector<int>> st_min(max_log + 1, vector<int>(n));

        for (int i = 0; i < n; ++i) {
            st_max[0][i] = nums[i];
            st_min[0][i] = nums[i];
        }

        for (int j = 1; j <= max_log; ++j) {
            for (int i = 0; i + (1 << j) <= n; ++i) {
                st_max[j][i] = max(st_max[j - 1][i], st_max[j - 1][i + (1 << (j - 1))]);
                st_min[j][i] = min(st_min[j - 1][i], st_min[j - 1][i + (1 << (j - 1))]);
            }
        }

        auto get_val = [&](int l, int r) {
            int len = r - l + 1;
            int j = logs[len];
            int mx = max(st_max[j][l], st_max[j][r - (1 << j) + 1]);
            int mn = min(st_min[j][l], st_min[j][r - (1 << j) + 1]);
            return (long long)mx - mn;
        };

        priority_queue<pair<long long, pair<int, int>>> pq;
        for (int i = 0; i < n; ++i) {
            pq.push({get_val(i, n - 1), {i, n - 1}});
        }

        long long total = 0;
        for (int i = 0; i < k; ++i) {
            auto top = pq.top();
            pq.pop();
            long long val = top.first;
            int l = top.second.first;
            int r = top.second.second;
            total += val;
            if (r > l) {
                pq.push({get_val(l, r - 1), {l, r - 1}});
            }
        }

        return total;
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
    public long maxTotalValue(int[] nums, int k) {
        int n = nums.length;
        if (n == 0) return 0;

        int maxLog = 0;
        while ((1 << (maxLog + 1)) <= n) maxLog++;

        int[] logs = new int[n + 1];
        for (int i = 2; i <= n; i++) logs[i] = logs[i >> 1] + 1;

        int[][] stMax = new int[maxLog + 1][n];
        int[][] stMin = new int[maxLog + 1][n];

        for (int i = 0; i < n; i++) {
            stMax[0][i] = nums[i];
            stMin[0][i] = nums[i];
        }

        for (int j = 1; j <= maxLog; j++) {
            for (int i = 0; i + (1 << j) <= n; i++) {
                stMax[j][i] = Math.max(stMax[j - 1][i], stMax[j - 1][i + (1 << (j - 1))]);
                stMin[j][i] = Math.min(stMin[j - 1][i], stMin[j - 1][i + (1 << (j - 1))]);
            }
        }

        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(b[0], a[0]));
        for (int i = 0; i < n; i++) {
            pq.offer(new long[]{getVal(i, n - 1, stMax, stMin, logs), i, n - 1});
        }

        long total = 0;
        for (int i = 0; i < k; i++) {
            long[] curr = pq.poll();
            long val = curr[0];
            int l = (int) curr[1];
            int r = (int) curr[2];
            total += val;
            if (r > l) {
                pq.offer(new long[]{getVal(l, r - 1, stMax, stMin, logs), l, r - 1});
            }
        }

        return total;
    }

    private long getVal(int l, int r, int[][] stMax, int[][] stMin, int[] logs) {
        int len = r - l + 1;
        int j = logs[len];
        int mx = Math.max(stMax[j][l], stMax[j][r - (1 << j) + 1]);
        int mn = Math.min(stMin[j][l], stMin[j][r - (1 << j) + 1]);
        return (long) mx - mn;
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
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        logs = [0] * (n + 1)
        for i in range(2, n + 1):
            logs[i] = logs[i >> 1] + 1

        max_log = logs[n]
        st_max = [nums]
        st_min = [nums]

        for j in range(1, max_log + 1):
            prev_mx = st_max[-1]
            prev_mn = st_min[-1]
            offset = 1 << (j - 1)
            curr_mx = [0] * (n - (1 << j) + 1)
            curr_mn = [0] * (n - (1 << j) + 1)
            for i in range(n - (1 << j) + 1):
                v1, v2 = prev_mx[i], prev_mx[i + offset]
                curr_mx[i] = v1 if v1 > v2 else v2
                v1, v2 = prev_mn[i], prev_mn[i + offset]
                curr_mn[i] = v1 if v1 < v2 else v2
            st_max.append(curr_mx)
            st_min.append(curr_mn)

        def get_val(l, r):
            length = r - l + 1
            j = logs[length]
            offset = length - (1 << j)
            mx_j, mn_j = st_max[j], st_min[j]
            v1, v2 = mx_j[l], mx_j[l + offset]
            mx = v1 if v1 > v2 else v2
            v1, v2 = mn_j[l], mn_j[l + offset]
            mn = v1 if v1 < v2 else v2
            return mx - mn

        heap = []
        for i in range(n):
            val = get_val(i, n - 1)
            heap.append((-val, i, n - 1))

        heapq.heapify(heap)

        ans = 0
        for _ in range(k):
            neg_v, l, r = heapq.heappop(heap)
            ans -= neg_v
            if r > l:
                next_r = r - 1
                next_v = get_val(l, next_r)
                heapq.heappush(heap, (-next_v, l, next_r))

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import heapq

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        log_n = n.bit_length()
        st_min = [[0] * n for _ in range(log_n)]
        st_max = [[0] * n for _ in range(log_n)]

        st_min[0] = nums[:]
        st_max[0] = nums[:]

        for j in range(1, log_n):
            offset = 1 << (j - 1)
            st_min_j = st_min[j]
            st_min_prev = st_min[j - 1]
            st_max_j = st_max[j]
            st_max_prev = st_max[j - 1]
            for i in range(n - (1 << j) + 1):
                v1, v2 = st_min_prev[i], st_min_prev[i + offset]
                st_min_j[i] = v1 if v1 < v2 else v2
                v1, v2 = st_max_prev[i], st_max_prev[i + offset]
                st_max_j[i] = v1 if v1 > v2 else v2

        logs = [0] * (n + 1)
        for i in range(2, n + 1):
            logs[i] = logs[i >> 1] + 1

        def query(l, r):
            j = logs[r - l + 1]
            offset = (1 << j)
            mn = min(st_min[j][l], st_min[j][r - offset + 1])
            mx = max(st_max[j][l], st_max[j][r - offset + 1])
            return mx - mn

        h = []
        for i in range(n):
            val = query(i, n - 1)
            h.append((-val, i, n - 1))
        heapq.heapify(h)

        total = 0
        for _ in range(k):
            if not h:
                break
            neg_val, l, r = heapq.heappop(h)
            total += -neg_val
            if r > l:
                new_r = r - 1
                new_val = query(l, new_r)
                heapq.heappush(h, (-new_val, l, new_r))

        return total
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

typedef struct {
    int val;
    int l;
    int r;
} Node;

void heapifyDown(Node* heap, int size, int i) {
    while (1) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        if (left < size && heap[left].val > heap[largest].val) largest = left;
        if (right < size && heap[right].val > heap[largest].val) largest = right;
        if (largest == i) break;
        Node temp = heap[i];
        heap[i] = heap[largest];
        heap[largest] = temp;
        i = largest;
    }
}

void heapifyUp(Node* heap, int i) {
    while (i > 0) {
        int parent = (i - 1) / 2;
        if (heap[i].val > heap[parent].val) {
            Node temp = heap[i];
            heap[i] = heap[parent];
            heap[parent] = temp;
            i = parent;
        } else break;
    }
}

int query(int l, int r, int* st_min, int* st_max, int* logs, int n) {
    int len = r - l + 1;
    int j = logs[len];
    int offset = 1 << j;
    int min1 = st_min[j * n + l];
    int min2 = st_min[j * n + r - offset + 1];
    int mn = min1 < min2 ? min1 : min2;
    int max1 = st_max[j * n + l];
    int max2 = st_max[j * n + r - offset + 1];
    int mx = max1 > max2 ? max1 : max2;
    return mx - mn;
}

long long maxTotalValue(int* nums, int numsSize, int k) {
    int n = numsSize;
    int log_n = 0;
    while ((1 << log_n) <= n) log_n++;
    int* st_min = (int*)malloc(log_n * n * sizeof(int));
    int* st_max = (int*)malloc(log_n * n * sizeof(int));
    int* logs = (int*)malloc((n + 1) * sizeof(int));
    for (int i = 0; i < n; i++) {
        st_min[i] = nums[i];
        st_max[i] = nums[i];
    }
    for (int j = 1; j < log_n; j++) {
        int offset = 1 << (j - 1);
        for (int i = 0; i + (1 << j) <= n; i++) {
            int m1 = st_min[(j - 1) * n + i];
            int m2 = st_min[(j - 1) * n + i + offset];
            st_min[j * n + i] = m1 < m2 ? m1 : m2;
            int x1 = st_max[(j - 1) * n + i];
            int x2 = st_max[(j - 1) * n + i + offset];
            st_max[j * n + i] = x1 > x2 ? x1 : x2;
        }
    }
    logs[1] = 0;
    for (int i = 2; i <= n; i++) logs[i] = logs[i / 2] + 1;
    Node* heap = (Node*)malloc(n * sizeof(Node));
    int heapSize = 0;
    for (int i = 0; i < n; i++) {
        heap[i].l = i;
        heap[i].r = n - 1;
        heap[i].val = query(i, n - 1, st_min, st_max, logs, n);
    }
    heapSize = n;
    for (int i = (n / 2) - 1; i >= 0; i--) heapifyDown(heap, heapSize, i);
    long long total = 0;
    for (int i = 0; i < k; i++) {
        if (heapSize == 0) break;
        Node top = heap[0];
        total += top.val;
        if (top.r > top.l) {
            top.r--;
            top.val = query(top.l, top.r, st_min, st_max, logs, n);
            heap[0] = top;
            heapifyDown(heap, heapSize, 0);
        } else {
            heap[0] = heap[heapSize - 1];
            heapSize--;
            heapifyDown(heap, heapSize, 0);
        }
    }
    free(st_min); free(st_max); free(logs); free(heap);
    return total;
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
    public class Node {
        public int Val { get; set; }
        public int L { get; set; }
        public int R { get; set; }
    }

    public long MaxTotalValue(int[] nums, int k) {
        int n = nums.Length;
        int logN = 0;
        while ((1 << logN) <= n) logN++;
        int[][] stMin = new int[logN][];
        int[][] stMax = new int[logN][];
        for (int j = 0; j < logN; j++) {
            stMin[j] = new int[n];
            stMax[j] = new int[n];
        }
        for (int i = 0; i < n; i++) {
            stMin[0][i] = nums[i];
            stMax[0][i] = nums[i];
        }
        for (int j = 1; j < logN; j++) {
            int offset = 1 << (j - 1);
            for (int i = 0; i + (1 << j) <= n; i++) {
                stMin[j][i] = Math.Min(stMin[j - 1][i], stMin[j - 1][i + offset]);
                stMax[j][i] = Math.Max(stMax[j - 1][i], stMax[j - 1][i + offset]);
            }
        }
        int[] logs = new int[n + 1];
        for (int i = 2; i <= n; i++) logs[i] = logs[i / 2] + 1;

        Func<int, int, int> query = (l, r) => {
            int len = r - l + 1;
            int j = logs[len];
            int offset = 1 << j;
            int mn = Math.Min(stMin[j][l], stMin[j][r - offset + 1]);
            int mx = Math.Max(stMax[j][l], stMax[j][r - offset + 1]);
            return mx - mn;
        };

        var pq = new PriorityQueue<Node, int>(Comparer<int>.Create((a, b) => b.CompareTo(a)));
        for (int i = 0; i < n; i++) {
            int val = query(i, n - 1);
            pq.Enqueue(new Node { Val = val, L = i, R = n - 1 }, val);
        }

        long total = 0;
        for (int i = 0; i < k; i++) {
            if (pq.Count == 0) break;
            var node = pq.Dequeue();
            total += node.Val;
            if (node.R > node.L) {
                node.R--;
                node.Val = query(node.L, node.R);
                pq.Enqueue(node, node.Val);
            }
        }
        return total;
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
 * @return {number}
 */
var maxTotalValue = function(nums, k) {
    const n = nums.length;
    let logN = 0;
    while ((1 << logN) <= n) logN++;
    const stMin = Array.from({ length: logN }, () => new Int32Array(n));
    const stMax = Array.from({ length: logN }, () => new Int32Array(n));
    for (let i = 0; i < n; i++) {
        stMin[0][i] = nums[i];
        stMax[0][i] = nums[i];
    }
    for (let j = 1; j < logN; j++) {
        const offset = 1 << (j - 1);
        for (let i = 0; i + (1 << j) <= n; i++) {
            stMin[j][i] = Math.min(stMin[j - 1][i], stMin[j - 1][i + offset]);
            stMax[j][i] = Math.max(stMax[j - 1][i], stMax[j - 1][i + offset]);
        }
    }
    const logs = new Int32Array(n + 1);
    for (let i = 2; i <= n; i++) logs[i] = logs[i >> 1] + 1;
    const query = (l, r) => {
        const j = logs[r - l + 1];
        const offset = 1 << j;
        const mn = Math.min(stMin[j][l], stMin[j][r - offset + 1]);
        const mx = Math.max(stMax[j][l], stMax[j][r - offset + 1]);
        return mx - mn;
    };
    class MaxHeap {
        constructor() { this.heap = []; }
        push(node) {
            this.heap.push(node);
            let idx = this.heap.length - 1;
            const el = this.heap[idx];
            while (idx > 0) {
                let parentIdx = (idx - 1) >> 1;
                let parent = this.heap[parentIdx];
                if (el.val <= parent.val) break;
                this.heap[idx] = parent; idx = parentIdx;
            }
            this.heap[idx] = el;
        }
        pop() {
            if (this.heap.length === 0) return null;
            const top = this.heap[0], last = this.heap.pop();
            if (this.heap.length > 0) {
                this.heap[0] = last; this.bubbleDown();
            }
            return top;
        }
        bubbleDown() {
            let idx = 0, el = this.heap[0], len = this.heap.length;
            while (true) {
                let lIdx = (idx << 1) + 1, rIdx = (idx << 1) + 2, swap = null;
                if (lIdx < len && this.heap[lIdx].val > el.val) swap = lIdx;
                if (rIdx < len && this.heap[rIdx].val > (swap === null ? el.val : this.heap[lIdx].val)) swap = rIdx;
                if (swap === null) break;
                this.heap[idx] = this.heap[swap]; idx = swap;
            }
            this.heap[idx] = el;
        }
    }
    const heap = new MaxHeap();
    for (let i = 0; i < n; i++) heap.push({ val: query(i, n - 1), l: i, r: n - 1 });
    let total = 0;
    for (let i = 0; i < k; i++) {
        const node = heap.pop();
        if (!node) break;
        total += node.val;
        if (node.r > node.l) {
            node.r--; node.val = query(node.l, node.r);
            heap.push(node);
        }
    }
    return total;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
class MaxHeap {
    private heap: { v: number; l: number; r: number }[] = [];

    push(node: { v: number; l: number; r: number }) {
        this.heap.push(node);
        let i = this.heap.length - 1;
        while (i > 0) {
            let p = (i - 1) >> 1;
            if (this.heap[p].v >= this.heap[i].v) break;
            this.swap(p, i);
            i = p;
        }
    }

    pop(): { v: number; l: number; r: number } | undefined {
        if (this.heap.length === 0) return undefined;
        if (this.heap.length === 1) return this.heap.pop();
        const root = this.heap[0];
        this.heap[0] = this.heap.pop()!;
        this.bubbleDown(0);
        return root;
    }

    private bubbleDown(i: number) {
        while (true) {
            let l = (i << 1) + 1;
            let r = (i << 1) + 2;
            let s = i;
            if (l < this.heap.length && this.heap[l].v > this.heap[s].v) s = l;
            if (r < this.heap.length && this.heap[r].v > this.heap[s].v) s = r;
            if (s === i) break;
            this.swap(i, s);
            i = s;
        }
    }

    private swap(i: number, j: number) {
        const temp = this.heap[i];
        this.heap[i] = this.heap[j];
        this.heap[j] = temp;
    }

    size(): number {
        return this.heap.length;
    }
}

function maxTotalValue(nums: number[], k: number): number {
    const n = nums.length;
    const logs = new Int32Array(n + 1);
    for (let i = 2; i <= n; i++) logs[i] = logs[i >> 1] + 1;

    const maxLog = logs[n];
    const stMax = Array.from({ length: maxLog + 1 }, () => new Int32Array(n));
    const stMin = Array.from({ length: maxLog + 1 }, () => new Int32Array(n));

    for (let i = 0; i < n; i++) {
        stMax[0][i] = nums[i];
        stMin[0][i] = nums[i];
    }

    for (let j = 1; j <= maxLog; j++) {
        const half = 1 << (j - 1);
        for (let i = 0; i <= n - (1 << j); i++) {
            stMax[j][i] = Math.max(stMax[j - 1][i], stMax[j - 1][i + half]);
            stMin[j][i] = Math.min(stMin[j - 1][i], stMin[j - 1][i + half]);
        }
    }

    const getV = (l: number, r: number): number => {
        const len = r - l + 1;
        const j = logs[len];
        const mx = Math.max(stMax[j][l], stMax[j][r - (1 << j) + 1]);
        const mn = Math.min(stMin[j][l], stMin[j][r - (1 << j) + 1]);
        return mx - mn;
    };

    const pq = new MaxHeap();
    for (let l = 0; l < n; l++) {
        const v = getV(l, n - 1);
        pq.push({ v, l, r: n - 1 });
    }

    let totalValue = 0;
    while (k > 0 && pq.size() > 0) {
        const top = pq.pop()!;
        totalValue += top.v;
        if (top.r > top.l) {
            const nv = getV(top.l, top.r - 1);
            pq.push({ v: nv, l: top.l, r: top.r - 1 });
        }
        k--;
    }

    return totalValue;
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
     * @return Integer
     */
    function maxTotalValue($nums, $k) {
        $n = count($nums);
        $logs = new SplFixedArray($n + 1);
        for ($i = 2; $i <= $n; $i++) {
            $logs[$i] = $logs[$i >> 1] + 1;
        }

        $maxLog = $logs[$n];
        $stMax = new SplFixedArray($maxLog + 1);
        $stMin = new SplFixedArray($maxLog + 1);

        for ($j = 0; $j <= $maxLog; $j++) {
            $stMax[$j] = new SplFixedArray($n);
            $stMin[$j] = new SplFixedArray($n);
        }

        for ($i = 0; $i < $n; $i++) {
            $stMax[0][$i] = $nums[$i];
            $stMin[0][$i] = $nums[$i];
        }

        for ($j = 1; $j <= $maxLog; $j++) {
            $half = 1 << ($j - 1);
            for ($i = 0; $i <= $n - (1 << $j); $i++) {
                $stMax[$j][$i] = max($stMax[$j - 1][$i], $stMax[$j - 1][$i + $half]);
                $stMin[$j][$i] = min($stMin[$j - 1][$i], $stMin[$j - 1][$i + $half]);
            }
        }

        $getV = function($l, $r) use ($stMax, $stMin, $logs) {
            $len = $r - $l + 1;
            $j = $logs[$len];
            $mx = max($stMax[$j][$l], $stMax[$j][$r - (1 << $j) + 1]);
            $mn = min($stMin[$j][$l], $stMin[$j][$r - (1 << $j) + 1]);
            return $mx - $mn;
        };

        $pq = new SplPriorityQueue();
        for ($l = 0; $l < $n; $l++) {
            $v = $getV($l, $n - 1);
            $pq->insert([$l, $n - 1, $v], $v);
        }

        $totalValue = 0;
        while ($k > 0 && !$pq->isEmpty()) {
            $top = $pq->extract();
            $l = $top[0];
            $r = $top[1];
            $v = $top[2];
            $totalValue += $v;
            if ($r > $l) {
                $nv = $getV($l, $r - 1);
                $pq->insert([$l, $r - 1, $nv], $nv);
            }
            $k--;
        }

        return $totalValue;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    struct MaxHeap {
        var heap: [(v: Int, l: Int, r: Int)] = []

        mutating func push(_ val: (v: Int, l: Int, r: Int)) {
            heap.append(val)
            var i = heap.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if heap[i].v <= heap[p].v { break }
                heap.swapAt(i, p)
                i = p
            }
        }

        mutating func pop() -> (v: Int, l: Int, r: Int)? {
            if heap.isEmpty { return nil }
            if heap.count == 1 { return heap.removeLast() }
            let root = heap[0]
            heap[0] = heap.removeLast()
            var i = 0
            while true {
                let l = i * 2 + 1
                let r = i * 2 + 2
                var s = i
                if l < heap.count && heap[l].v > heap[s].v { s = l }
                if r < heap.count && heap[r].v > heap[s].v { s = r }
                if s == i { break }
                heap.swapAt(i, s)
                i = s
            }
            return root
        }

        func isEmpty() -> Bool {
            return heap.isEmpty
        }
    }

    func maxTotalValue(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var logs = [Int](repeating: 0, count: n + 1)
        for i in 2...n { logs[i] = logs[i >> 1] + 1 }

        let maxLog = logs[n]
        var stMax = Array(repeating: [Int](repeating: 0, count: n), count: maxLog + 1)
        var stMin = Array(repeating: [Int](repeating: 0, count: n), count: maxLog + 1)

        for i in 0..<n {
            stMax[0][i] = nums[i]
            stMin[0][i] = nums[i]
        }

        if maxLog > 0 {
            for j in 1...maxLog {
                let half = 1 << (j - 1)
                for i in 0...(n - (1 << j)) {
                    stMax[j][i] = max(stMax[j - 1][i], stMax[j - 1][i + half])
                    stMin[j][i] = min(stMin[j - 1][i], stMin[j - 1][i + half])
                }
            }
        }

        func getV(_ l: Int, _ r: Int) -> Int {
            let len = r - l + 1
            let j = logs[len]
            let mx = max(stMax[j][l], stMax[j][r - (1 << j) + 1])
            let mn = min(stMin[j][l], stMin[j][r - (1 << j) + 1])
            return mx - mn
        }

        var pq = MaxHeap()
        for l in 0..<n {
            let v = getV(l, n - 1)
            pq.push((v: v, l: l, r: n - 1))
        }

        var totalValue = 0
        var remainingK = k
        while remainingK > 0 && !pq.isEmpty() {
            if let top = pq.pop() {
                totalValue += top.v
                if top.r > top.l {
                    let nv = getV(top.l, top.r - 1)
                    pq.push((v: nv, l: top.l, r: top.r - 1))
                }
            }
            remainingK -= 1
        }

        return totalValue
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
    data class Subarray(val v: Int, val l: Int, val r: Int)

    fun maxTotalValue(nums: IntArray, k: Int): Long {
        val n = nums.size
        val logs = IntArray(n + 1)
        for (i in 2..n) logs[i] = logs[i shr 1] + 1

        val maxLog = logs[n]
        val stMax = Array(maxLog + 1) { IntArray(n) }
        val stMin = Array(maxLog + 1) { IntArray(n) }

        for (i in 0 until n) {
            stMax[0][i] = nums[i]
            stMin[0][i] = nums[i]
        }

        for (j in 1..maxLog) {
            val half = 1 shl (j - 1)
            for (i in 0..n - (1 shl j)) {
                stMax[j][i] = maxOf(stMax[j - 1][i], stMax[j - 1][i + half])
                stMin[j][i] = minOf(stMin[j - 1][i], stMin[j - 1][i + half])
            }
        }

        fun getV(l: Int, r: Int): Int {
            val len = r - l + 1
            val j = logs[len]
            val mx = maxOf(stMax[j][l], stMax[j][r - (1 shl j) + 1])
            val mn = minOf(stMin[j][l], stMin[j][r - (1 shl j) + 1])
            return mx - mn
        }

        val pq = PriorityQueue<Subarray> { a, b -> b.v.compareTo(a.v) }

        for (l in 0 until n) {
            val v = getV(l, n - 1)
            pq.add(Subarray(v, l, n - 1))
        }

        var totalValue: Long = 0
        var count = 0
        while (count < k && pq.isNotEmpty()) {
            val top = pq.poll()
            totalValue += top.v.toLong()
            if (top.r > top.l) {
                val nv = getV(top.l, top.r - 1)
                pq.add(Subarray(nv, top.l, top.r - 1))
            }
            count++
        }

        return totalValue
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:math' as math;
import 'dart:typed_data';

class Node {
  int val, l, r;
  Node(this.val, this.l, this.r);
}

class MaxHeap {
  List<Node> _heap = [];

  void push(Node node) {
    _heap.add(node);
    _bubbleUp(_heap.length - 1);
  }

  Node pop() {
    if (_heap.isEmpty) throw Exception("Empty heap");
    Node top = _heap[0];
    Node last = _heap.removeLast();
    if (_heap.isNotEmpty) {
      _heap[0] = last;
      _bubbleDown(0);
    }
    return top;
  }

  void _bubbleUp(int idx) {
    while (idx > 0) {
      int p = (idx - 1) >> 1;
      if (_heap[idx].val > _heap[p].val) {
        _swap(idx, p);
        idx = p;
      } else {
        break;
      }
    }
  }

  void _bubbleDown(int idx) {
    while (true) {
      int left = (idx << 1) + 1;
      int right = (idx << 1) + 2;
      int largest = idx;
      if (left < _heap.length && _heap[left].val > _heap[largest].val) {
        largest = left;
      }
      if (right < _heap.length && _heap[right].val > _heap[largest].val) {
        largest = right;
      }
      if (largest != idx) {
        _swap(idx, largest);
        idx = largest;
      } else {
        break;
      }
    }
  }

  void _swap(int i, int j) {
    Node tmp = _heap[i];
    _heap[i] = _heap[j];
    _heap[j] = tmp;
  }
}

class Solution {
  int maxTotalValue(List<int> nums, int k) {
    int n = nums.length;
    Int32List logs = Int32List(n + 1);
    for (int i = 2; i <= n; i++) logs[i] = logs[i >> 1] + 1;

    List<Int32List> stMax = List.generate(17, (_) => Int32List(n));
    List<Int32List> stMin = List.generate(17, (_) => Int32List(n));

    for (int i = 0; i < n; i++) {
      stMax[0][i] = nums[i];
      stMin[0][i] = nums[i];
    }

    for (int j = 1; j < 17; j++) {
      for (int i = 0; i + (1 << j) <= n; i++) {
        stMax[j][i] = math.max(stMax[j - 1][i], stMax[j - 1][i + (1 << (j - 1))]);
        stMin[j][i] = math.min(stMin[j - 1][i], stMin[j - 1][i + (1 << (j - 1))]);
      }
    }

    int query(int l, int r) {
      int j = logs[r - l + 1];
      int mx = math.max(stMax[j][l], stMax[j][r - (1 << j) + 1]);
      int mn = math.min(stMin[j][l], stMin[j][r - (1 << j) + 1]);
      return mx - mn;
    }

    MaxHeap pq = MaxHeap();
    for (int l = 0; l < n; l++) {
      pq.push(Node(query(l, n - 1), l, n - 1));
    }

    int totalValue = 0;
    for (int i = 0; i < k; i++) {
      Node top = pq.pop();
      totalValue += top.val;
      if (top.r > top.l) {
        int nextR = top.r - 1;
        pq.push(Node(query(top.l, nextR), top.l, nextR));
      }
    }

    return totalValue;
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
	val, l, r int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int           { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool { return pq[i].val > pq[j].val }
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

func maxTotalValue(nums []int, k int) int64 {
	n := len(nums)
	logs := make([]int, n+1)
	for i := 2; i <= n; i++ {
		logs[i] = logs[i/2] + 1
	}

	stMax := make([][]int, 17)
	stMin := make([][]int, 17)
	for i := range stMax {
		stMax[i] = make([]int, n)
		stMin[i] = make([]int, n)
	}

	for i := 0; i < n; i++ {
		stMax[0][i] = nums[i]
		stMin[0][i] = nums[i]
	}

	for j := 1; j < 17; j++ {
		for i := 0; i+(1<<j) <= n; i++ {
			mx1, mx2 := stMax[j-1][i], stMax[j-1][i+(1<<(j-1))]
			if mx1 > mx2 { stMax[j][i] = mx1 } else { stMax[j][i] = mx2 }
			mn1, mn2 := stMin[j-1][i], stMin[j-1][i+(1<<(j-1))]
			if mn1 < mn2 { stMin[j][i] = mn1 } else { stMin[j][i] = mn2 }
		}
	}

	query := func(l, r int) int {
		j := logs[r-l+1]
		mx1, mx2 := stMax[j][l], stMax[j][r-(1<<j)+1]
		mn1, mn2 := stMin[j][l], stMin[j][r-(1<<j)+1]
		mx, mn := mx1, mn1
		if mx2 > mx { mx = mx2 }
		if mn2 < mn { mn = mn2 }
		return mx - mn
	}

	pq := make(PriorityQueue, 0, n)
	heap.Init(&pq)
	for l := 0; l < n; l++ {
		heap.Push(&pq, &Item{query(l, n-1), l, n-1})
	}

	var totalValue int64 = 0
	for i := 0; i < k; i++ {
		item := heap.Pop(&pq).(*Item)
		totalValue += int64(item.val)
		if item.r > item.l {
			nextR := item.r - 1
			heap.Push(&pq, &Item{query(item.l, nextR), item.l, nextR})
		}
	}

	return totalValue
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class MaxHeap
  def initialize
    @heap = []
  end
  def push(node)
    @heap << node
    bubble_up(@heap.size - 1)
  end
  def pop
    return nil if @heap.empty?
    if @heap.size == 1
      return @heap.pop
    end
    res = @heap[0]
    @heap[0] = @heap.pop
    bubble_down(0)
    res
  end
  def bubble_up(idx)
    while idx > 0
      p = (idx - 1) / 2
      if @heap[idx][0] > @heap[p][0]
        @heap[idx], @heap[p] = @heap[p], @heap[idx]
        idx = p
      else
        break
      end
    end
  end
  def bubble_down(idx)
    while true
      l = 2 * idx + 1
      r = 2 * idx + 2
      largest = idx
      if l < @heap.size && @heap[l][0] > @heap[largest][0]
        largest = l
      end
      if r < @heap.size && @heap[r][0] > @heap[largest][0]
        largest = r
      end
      if largest != idx
        @heap[idx], @heap[largest] = @heap[largest], @heap[idx]
        idx = largest
      else
        break
      end
    end
  end
end

def max_total_value(nums, k)
  n = nums.length
  logs = Array.new(n + 1, 0)
  (2..n).each { |i| logs[i] = logs[i / 2] + 1 }

  st_max = Array.new(17) { Array.new(n, 0) }
  st_min = Array.new(17) { Array.new(n, 0) }
  (0...n).each do |i|
    st_max[0][i] = nums[i]
    st_min[0][i] = nums[i]
  end

  (1...17).each do |j|
    (0..(n - (1 << j))).each do |i|
      mx1, mx2 = st_max[j - 1][i], st_max[j - 1][i + (1 << (j - 1))]
      st_max[j][i] = mx1 > mx2 ? mx1 : mx2
      mn1, mn2 = st_min[j - 1][i], st_min[j - 1][i + (1 << (j - 1))]
      st_min[j][i] = mn1 < mn2 ? mn1 : mn2
    end
  end

  query = lambda do |l, r|
    j = logs[r - l + 1]
    mx1, mx2 = st_max[j][l], st_max[j][r - (1 << j) + 1]
    mx = mx1 > mx2 ? mx1 : mx2
    mn1, mn2 = st_min[j][l], st_min[j][r - (1 << j) + 1]
    mn = mn1 < mn2 ? mn1 : mn2
    mx - mn
  end

  pq = MaxHeap.new
  (0...n).each do |l|
    pq.push([query.call(l, n - 1), l, n - 1])
  end

  total_value = 0
  k.times do
    top = pq.pop
    val, l, r = top
    total_value += val
    if r > l
      nr = r - 1
      pq.push([query.call(l, nr), l, nr])
    end
  end

  total_value
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable.PriorityQueue

object Solution {
  case class Item(v: Int, l: Int, r: Int)

  def maxTotalValue(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val logs = new Array[Int](n + 1)
    for (i <- 2 to n) logs(i) = logs(i / 2) + 1

    val stMax = Array.ofDim[Int](17, n)
    val stMin = Array.ofDim[Int](17, n)

    for (i <- 0 until n) {
      stMax(0)(i) = nums(i)
      stMin(0)(i) = nums(i)
    }

    for (j <- 1 until 17) {
      for (i <- 0 to (n - (1 << j))) {
        stMax(j)(i) = math.max(stMax(j - 1)(i), stMax(j - 1)(i + (1 << (j - 1))))
        stMin(j)(i) = math.min(stMin(j - 1)(i), stMin(j - 1)(i + (1 << (j - 1))))
      }
    }

    def query(l: Int, r: Int): Int = {
      val j = logs(r - l + 1)
      val mx = math.max(stMax(j)(l), stMax(j)(r - (1 << j) + 1))
      val mn = math.min(stMin(j)(l), stMin(j)(r - (1 << j) + 1))
      mx - mn
    }

    val pq = PriorityQueue[Item]()(Ordering.by(_.v))
    for (l <- 0 until n) {
      pq.enqueue(Item(query(l, n - 1), l, n - 1))
    }

    var totalValue: Long = 0
    for (_ <- 0 until k) {
      val item = pq.dequeue()
      totalValue += item.v
      if (item.r > item.l) {
        val nextR = item.r - 1
        pq.enqueue(Item(query(item.l, nextR), item.l, nextR))
      }
    }

    totalValue
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_total_value(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut log_table = vec![0; n + 1];
        for i in 2..=n {
            log_table[i] = log_table[i / 2] + 1;
        }
        let max_log = log_table[n] as usize;
        let mut st_min = vec![vec![0; n]; max_log + 1];
        let mut st_max = vec![vec![0; n]; max_log + 1];
        for i in 0..n {
            st_min[0][i] = nums[i];
            st_max[0][i] = nums[i];
        }
        for j in 1..=max_log {
            let p2_prev = 1 << (j - 1);
            for i in 0..=(n - (1 << j)) {
                st_min[j][i] = st_min[j - 1][i].min(st_min[j - 1][i + p2_prev]);
                st_max[j][i] = st_max[j - 1][i].max(st_max[j - 1][i + p2_prev]);
            }
        }

        let get_val = |l: usize, r: usize, st_min: &Vec<Vec<i32>>, st_max: &Vec<Vec<i32>>, log_table: &Vec<usize>| -> i64 {
            let len = r - l + 1;
            let j = log_table[len];
            let mn = st_min[j][l].min(st_min[j][r - (1 << j) + 1]);
            let mx = st_max[j][l].max(st_max[j][r - (1 << j) + 1]);
            (mx - mn) as i64
        };

        let mut pq = std::collections::BinaryHeap::new();
        for l in 0..n {
            pq.push((get_val(l, n - 1, &st_min, &st_max, &log_table), l, n - 1));
        }

        let mut total_value = 0i64;
        let mut k_rem = k;
        while k_rem > 0 {
            if let Some((val, l, r)) = pq.pop() {
                total_value += val;
                if r > l {
                    pq.push((get_val(l, r - 1, &st_min, &st_max, &log_table), l, r - 1));
                }
            }
            k_rem -= 1;
        }
        total_value
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-total-value nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([n (length nums)]
         [nums-vec (list->vector nums)]
         [log-table (let ([vec (make-vector (+ n 1) 0)])
                      (for ([i (in-range 2 (+ n 1))])
                        (vector-set! vec i (+ (vector-ref vec (quotient i 2)) 1)))
                      vec)]
         [max-log (vector-ref log-table n)]
         [st-min (let ([st (make-vector (+ max-log 1))])
                   (vector-set! st 0 nums-vec)
                   (for ([j (in-range 1 (+ max-log 1))])
                     (let* ([p2-prev (arithmetic-shift 1 (- j 1))]
                            [len (+ (- n (arithmetic-shift 1 j)) 1)]
                            [curr-level (make-vector len)])
                       (for ([i (in-range len)])
                         (vector-set! curr-level i (min (vector-ref (vector-ref st (- j 1)) i)
                                                        (vector-ref (vector-ref st (- j 1)) (+ i p2-prev)))))
                       (vector-set! st j curr-level)))
                   st)]
         [st-max (let ([st (make-vector (+ max-log 1))])
                   (vector-set! st 0 nums-vec)
                   (for ([j (in-range 1 (+ max-log 1))])
                     (let* ([p2-prev (arithmetic-shift 1 (- j 1))]
                            [len (+ (- n (arithmetic-shift 1 j)) 1)]
                            [curr-level (make-vector len)])
                       (for ([i (in-range len)])
                         (vector-set! curr-level i (max (vector-ref (vector-ref st (- j 1)) i)
                                                        (vector-ref (vector-ref st (- j 1)) (+ i p2-prev)))))
                       (vector-set! st j curr-level)))
                   st)]
         [get-val (lambda (l r)
                    (let* ([len (+ (- r l) 1)]
                           [j (vector-ref log-table len)]
                           [p2 (arithmetic-shift 1 j)]
                           [mn (min (vector-ref (vector-ref st-min j) l)
                                    (vector-ref (vector-ref st-min j) (+ (- r p2) 1)))]
                           [mx (max (vector-ref (vector-ref st-max j) l)
                                    (vector-ref (vector-ref st-max j) (+ (- r p2) 1)))])
                      (- mx mn)))]
         [pq-vec (make-vector (+ n 1))]
         [pq-size 0]
         [heap-push! (lambda (val)
                       (set! pq-size (+ pq-size 1))
                       (vector-set! pq-vec pq-size val)
                       (let loop ([curr pq-size])
                         (when (> curr 1)
                           (let ([parent (quotient curr 2)])
                             (when (> (car (vector-ref pq-vec curr)) (car (vector-ref pq-vec parent)))
                               (let ([tmp (vector-ref pq-vec curr)])
                                 (vector-set! pq-vec curr (vector-ref pq-vec parent))
                                 (vector-set! pq-vec parent tmp)
                                 (loop parent)))))))]
         [heap-pop! (lambda ()
                      (let ([top (vector-ref pq-vec 1)])
                        (vector-set! pq-vec 1 (vector-ref pq-vec pq-size))
                        (set! pq-size (- pq-size 1))
                        (let loop ([curr 1])
                          (let* ([left (* curr 2)]
                                 [right (+ (* curr 2) 1)]
                                 [largest curr])
                            (let* ([largest (if (and (<= left pq-size) (> (car (vector-ref pq-vec left)) (car (vector-ref pq-vec largest)))) left largest)]
                                   [largest (if (and (<= right pq-size) (> (car (vector-ref pq-vec right)) (car (vector-ref pq-vec largest)))) right largest)])
                              (when (not (= largest curr))
                                (let ([tmp (vector-ref pq-vec curr)])
                                  (vector-set! pq-vec curr (vector-ref pq-vec largest))
                                  (vector-set! pq-vec largest tmp)
                                  (loop largest))))))
                        top))])
    (for ([l (in-range n)])
      (heap-push! (list (get-val l (- n 1)) l (- n 1))))
    (let loop ([k-rem k] [total 0])
      (if (> k-rem 0)
          (let* ([node (heap-pop!)]
                 [val (car node)]
                 [l (cadr node)]
                 [r (caddr node)])
            (if (> r l)
                (heap-push! (list (get-val l (- r 1)) l (- r 1)))
                (void))
            (loop (- k-rem 1) (+ total val)))
          total))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_total_value(Nums :: [integer()], K :: integer()) -> integer().
max_total_value(Nums, K) ->
    N = length(Nums),
    NumsTuple = list_to_tuple(Nums),
    LogTable = build_log_table(N),
    MaxLog = get_max_log(N),
    STMin = build_st_min(NumsTuple, N, MaxLog),
    STMax = build_st_max(NumsTuple, N, MaxLog),
    GetVal = fun(L, R) ->
        Len = R - L + 1,
        J = element(Len, LogTable),
        P2 = 1 bsl J,
        Mn = min(element(L + 1, element(J + 1, STMin)), element(R - P2 + 2, element(J + 1, STMin))),
        Mx = max(element(L + 1, element(J + 1, STMax)), element(R - P2 + 2, element(J + 1, STMax))),
        Mx - Mn
    end,
    InitialHeap = lists:foldl(fun(L, Acc) ->
        Val = GetVal(L, N - 1),
        gb_trees:enter({-Val, L, N - 1}, true, Acc)
    end, gb_trees:empty(), lists:seq(0, N - 1)),
    solve(InitialHeap, K, GetVal, 0).

get_max_log(N) when N =< 1 -> 0;
get_max_log(N) -> 1 + get_max_log(N div 2).

build_log_table(N) ->
    list_to_tuple(lists:reverse(build_log_table_list(2, N, [0]))).

build_log_table_list(I, N, [H | _] = Acc) when I =< N ->
    if I < (1 bsl (H + 1)) ->
        build_log_table_list(I + 1, N, [H | Acc]);
    true ->
        build_log_table_list(I + 1, N, [H + 1 | Acc])
    end;
build_log_table_list(_, _, Acc) -> Acc.

build_st_min(NumsTuple, N, MaxLog) ->
    build_st_levels(1, MaxLog, [NumsTuple], N, fun(A, B) -> min(A, B) end).

build_st_max(NumsTuple, N, MaxLog) ->
    build_st_levels(1, MaxLog, [NumsTuple], N, fun(A, B) -> max(A, B) end).

build_st_levels(J, MaxLog, [Prev | _] = Levels, N, Op) when J =< MaxLog ->
    P2Prev = 1 bsl (J - 1),
    Limit = N - (1 bsl J) + 1,
    NewLevel = list_to_tuple([Op(element(I, Prev), element(I + P2Prev, Prev)) || I <- lists:seq(1, Limit)]),
    build_st_levels(J + 1, MaxLog, [NewLevel | Levels], N, Op);
build_st_levels(_, _, Levels, _, _) ->
    list_to_tuple(lists:reverse(Levels)).

solve(_, 0, _, Acc) -> Acc;
solve(Heap, K, GetVal, Acc) ->
    {{ValNeg, L, R}, _, NewHeap} = gb_trees:take_smallest(Heap),
    Val = -ValNeg,
    if R > L ->
        NextVal = GetVal(L, R - 1),
        solve(gb_trees:enter({-NextVal, L, R - 1}, true, NewHeap), K - 1, GetVal, Acc + Val);
    true ->
        solve(NewHeap, K - 1, GetVal, Acc + Val)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  use Bitwise

  @spec max_total_value(nums :: [integer], k :: integer) :: integer
  def max_total_value(nums, k) do
    n = length(nums)
    nums_tuple = List.to_tuple(nums)
    log_table = build_log_table(n)
    max_log = get_max_log(n)
    st_min = build_st_min(nums_tuple, n, max_log)
    st_max = build_st_max(nums_tuple, n, max_log)

    get_val = fn l, r ->
      len = r - l + 1
      j = elem(log_table, len - 1)
      p2 = Bitwise.bsl(1, j)
      mn = min(elem(elem(st_min, j), l), elem(elem(st_min, j), r - p2 + 1))
      mx = max(elem(elem(st_max, j), l), elem(elem(st_max, j), r - p2 + 1))
      mx - mn
    end

    initial_heap = Enum.reduce(0..(n - 1), :gb_trees.empty(), fn l, acc ->
      val = get_val.(l, n - 1)
      :gb_trees.enter({-val, l, n - 1}, true, acc)
    end)

    solve(initial_heap, k, get_val, 0)
  end

  defp get_max_log(n) when n <= 1, do: 0
  defp get_max_log(n), do: 1 + get_max_log(div(n, 2))

  defp build_log_table(n) do
    Enum.reduce(2..n, [0], fn i, [h | _] = acc ->
      if i < Bitwise.bsl(1, h + 1) do
        [h | acc]
      else
        [h + 1 | acc]
      end
    end)
    |> Enum.reverse()
    |> List.to_tuple()
  end

  defp build_st_min(nums_tuple, n, max_log), do: build_st_levels(1, max_log, [nums_tuple], n, &min/2)
  defp build_st_max(nums_tuple, n, max_log), do: build_st_levels(1, max_log, [nums_tuple], n, &max/2)

  defp build_st_levels(j, max_log, [prev | _] = levels, n, op) when j <= max_log do
    p2_prev = Bitwise.bsl(1, j - 1)
    limit = n - Bitwise.bsl(1, j) + 1
    new_level = Enum.map(1..limit, fn i -> op.(elem(prev, i - 1), elem(prev, i + p2_prev - 1)) end) |> List.to_tuple()
    build_st_levels(j + 1, max_log, [new_level | levels], n, op)
  end
  defp build_st_levels(_, _, levels, _, _), do: Enum.reverse(levels) |> List.to_tuple()

  defp solve(_heap, 0, _get_val, acc), do: acc
  defp solve(heap, k, get_val, acc) do
    {{val_neg, l, r}, _, new_heap} = :gb_trees.take_smallest(heap)
    val = -val_neg
    if r > l do
      next_val = get_val.(l, r - 1)
      solve(:gb_trees.enter({-next_val, l, r - 1}, true, new_heap), k - 1, get_val, acc + val)
    else
      solve(new_heap, k - 1, get_val, acc + val)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O((n + k) \log n). Building the sparse table takes $O(n \log n)$ time. Initializing the heap with $n$ elements takes $O(n)$ or $O(n \log n)$, and extracting the top $k$ elements while performing $k$ pushes takes $O(k \log n)$. With $n=5 \times 10^4$ and $k=10^5$, this is well within performance limits.
- **Space Complexity:** O(n \log n). The sparse table requires $O(n \log n)$ space to store the max and min values for each power-of-two length. The priority queue stores at most $n$ elements, contributing $O(n)$ space.
