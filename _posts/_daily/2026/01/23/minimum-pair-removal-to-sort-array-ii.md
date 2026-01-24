---
layout: post
title: "Minimum Pair Removal to Sort Array II"
date: 2026-01-23 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Hash Table", "Linked List", "Heap (Priority Queue)", "Simulation", "Doubly-Linked List", "Ordered Set"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumPairRemoval(vector<int>& nums)\
        \ {\n        int n = nums.size();\n        if (n < 2) return 0;\n        vector<long\
        \ long> val(n);\n        vector<int> L(n), R(n);\n        vector<bool> alive(n,\
        \ true);\n        for (int i = 0; i < n; ++i) {\n            val[i] = nums[i];\n\
        \            L[i] = i - 1;\n            R[i] = (i == n - 1) ? -1 : i + 1;\n\
        \        }\n        typedef pair<long long, int> P;\n        priority_queue<P,\
        \ vector<P>, greater<P>> pq;\n        int violations = 0;\n        for (int\
        \ i = 0; i < n - 1; ++i) {\n            if (val[i] > val[i + 1]) violations++;\n\
        \            pq.push({val[i] + val[i + 1], i});\n        }\n        int ops\
        \ = 0;\n        while (violations > 0 && !pq.empty()) {\n            P top =\
        \ pq.top();\n            pq.pop();\n            int i = top.second;\n      \
        \      if (!alive[i] || R[i] == -1 || val[i] + val[R[i]] != top.first) continue;\n\
        \            int j = R[i];\n            if (L[i] != -1 && val[L[i]] > val[i])\
        \ violations--;\n            if (val[i] > val[j]) violations--;\n          \
        \  if (R[j] != -1 && val[j] > val[R[j]]) violations--;\n            val[i] +=\
        \ val[j];\n            alive[j] = false;\n            R[i] = R[j];\n       \
        \     if (R[j] != -1) L[R[j]] = i;\n            if (L[i] != -1 && val[L[i]]\
        \ > val[i]) violations++;\n            if (R[i] != -1 && val[i] > val[R[i]])\
        \ violations++;\n            if (L[i] != -1) pq.push({val[L[i]] + val[i], L[i]});\n\
        \            if (R[i] != -1) pq.push({val[i] + val[R[i]], i});\n           \
        \ ops++;\n        }\n        return ops;\n    }\n};"
      java: "class Solution {\n    static class Node implements Comparable<Node> {\n\
        \        long sum;\n        int idx;\n        Node(long s, int i) {\n      \
        \      this.sum = s;\n            this.idx = i;\n        }\n        public int\
        \ compareTo(Node other) {\n            if (this.sum != other.sum) return Long.compare(this.sum,\
        \ other.sum);\n            return Integer.compare(this.idx, other.idx);\n  \
        \      }\n    }\n    public int minimumPairRemoval(int[] nums) {\n        int\
        \ n = nums.length;\n        if (n < 2) return 0;\n        long[] val = new long[n];\n\
        \        int[] L = new int[n];\n        int[] R = new int[n];\n        boolean[]\
        \ alive = new boolean[n];\n        PriorityQueue<Node> pq = new PriorityQueue<>();\n\
        \        int violations = 0;\n        for (int i = 0; i < n; i++) {\n      \
        \      val[i] = nums[i];\n            L[i] = i - 1;\n            R[i] = (i ==\
        \ n - 1) ? -1 : i + 1;\n            alive[i] = true;\n        }\n        for\
        \ (int i = 0; i < n - 1; i++) {\n            if (val[i] > val[i + 1]) violations++;\n\
        \            pq.add(new Node(val[i] + val[i + 1], i));\n        }\n        int\
        \ ops = 0;\n        while (violations > 0 && !pq.isEmpty()) {\n            Node\
        \ top = pq.poll();\n            int i = top.idx;\n            if (!alive[i]\
        \ || R[i] == -1 || val[i] + val[R[i]] != top.sum) continue;\n            int\
        \ j = R[i];\n            if (L[i] != -1 && val[L[i]] > val[i]) violations--;\n\
        \            if (val[i] > val[j]) violations--;\n            if (R[j] != -1\
        \ && val[j] > val[R[j]]) violations--;\n            val[i] += val[j];\n    \
        \        alive[j] = false;\n            R[i] = R[j];\n            if (R[j] !=\
        \ -1) L[R[j]] = i;\n            if (L[i] != -1 && val[L[i]] > val[i]) violations++;\n\
        \            if (R[i] != -1 && val[i] > val[R[i]]) violations++;\n         \
        \   if (L[i] != -1) pq.add(new Node(val[L[i]] + val[i], L[i]));\n          \
        \  if (R[i] != -1) pq.add(new Node(val[i] + val[R[i]], i));\n            ops++;\n\
        \        }\n        return ops;\n    }\n}"
      python: "import heapq\n\nclass Solution(object):\n    def minimumPairRemoval(self,\
        \ nums):\n        \"\"\"\n        :type nums: List[int]\n        :rtype: int\n\
        \        \"\"\"\n        n = len(nums)\n        if n < 2:\n            return\
        \ 0\n        val = [long(x) for x in nums]\n        L = [i - 1 for i in range(n)]\n\
        \        R = [i + 1 for i in range(n)]\n        R[n - 1] = -1\n        alive\
        \ = [True] * n\n        pq = []\n        violations = 0\n        for i in range(n\
        \ - 1):\n            if val[i] > val[i + 1]:\n                violations +=\
        \ 1\n            heapq.heappush(pq, (val[i] + val[i + 1], i))\n\n        ops\
        \ = 0\n        while violations > 0 and pq:\n            s, i = heapq.heappop(pq)\n\
        \            if not alive[i] or R[i] == -1 or val[i] + val[R[i]] != s:\n   \
        \             continue\n            j = R[i]\n            if L[i] != -1 and\
        \ val[L[i]] > val[i]: violations -= 1\n            if val[i] > val[j]: violations\
        \ -= 1\n            if R[j] != -1 and val[j] > val[R[j]]: violations -= 1\n\
        \            val[i] += val[j]\n            alive[j] = False\n            R[i]\
        \ = R[j]\n            if R[j] != -1: L[R[j]] = i\n            if L[i] != -1\
        \ and val[L[i]] > val[i]: violations += 1\n            if R[i] != -1 and val[i]\
        \ > val[R[i]]: violations += 1\n            if L[i] != -1: heapq.heappush(pq,\
        \ (val[L[i]] + val[i], L[i]))\n            if R[i] != -1: heapq.heappush(pq,\
        \ (val[i] + val[R[i]], i))\n            ops += 1\n        return ops"
      python3: "import heapq\n\nclass Solution:\n    def minimumPairRemoval(self, nums:\
        \ List[int]) -> int:\n        n = len(nums)\n        if n < 2:\n           \
        \ return 0\n        val = [int(x) for x in nums]\n        L = [i - 1 for i in\
        \ range(n)]\n        R = [i + 1 for i in range(n)]\n        R[n - 1] = -1\n\
        \        alive = [True] * n\n        pq = []\n        violations = 0\n     \
        \   for i in range(n - 1):\n            if val[i] > val[i + 1]:\n          \
        \      violations += 1\n            heapq.heappush(pq, (val[i] + val[i + 1],\
        \ i))\n\n        ops = 0\n        while violations > 0 and pq:\n           \
        \ s, i = heapq.heappop(pq)\n            if not alive[i] or R[i] == -1 or val[i]\
        \ + val[R[i]] != s:\n                continue\n            j = R[i]\n      \
        \      if L[i] != -1 and val[L[i]] > val[i]: violations -= 1\n            if\
        \ val[i] > val[j]: violations -= 1\n            if R[j] != -1 and val[j] > val[R[j]]:\
        \ violations -= 1\n            val[i] += val[j]\n            alive[j] = False\n\
        \            R[i] = R[j]\n            if R[j] != -1: L[R[j]] = i\n         \
        \   if L[i] != -1 and val[L[i]] > val[i]: violations += 1\n            if R[i]\
        \ != -1 and val[i] > val[R[i]]: violations += 1\n            if L[i] != -1:\
        \ heapq.heappush(pq, (val[L[i]] + val[i], L[i]))\n            if R[i] != -1:\
        \ heapq.heappush(pq, (val[i] + val[R[i]], i))\n            ops += 1\n      \
        \  return ops"
      c: "#include <stdlib.h>\n#include <stdbool.h>\n\ntypedef struct {\n    long long\
        \ sum;\n    int idx;\n} HeapNode;\n\ntypedef struct {\n    HeapNode* data;\n\
        \    int size;\n    int capacity;\n} MinHeap;\n\nvoid push(MinHeap* h, long\
        \ long sum, int idx) {\n    if (h->size == h->capacity) {\n        h->capacity\
        \ *= 2;\n        h->data = (HeapNode*)realloc(h->data, sizeof(HeapNode) * h->capacity);\n\
        \    }\n    int i = h->size++;\n    while (i > 0) {\n        int p = (i - 1)\
        \ / 2;\n        if (h->data[p].sum < sum || (h->data[p].sum == sum && h->data[p].idx\
        \ <= idx)) break;\n        h->data[i] = h->data[p];\n        i = p;\n    }\n\
        \    h->data[i].sum = sum; h->data[i].idx = idx;\n}\n\nHeapNode pop(MinHeap*\
        \ h) {\n    HeapNode res = h->data[0];\n    h->size--;\n    if (h->size > 0)\
        \ {\n        HeapNode last = h->data[h->size];\n        int i = 0;\n       \
        \ while (i * 2 + 1 < h->size) {\n            int child = i * 2 + 1;\n      \
        \      if (child + 1 < h->size && (h->data[child + 1].sum < h->data[child].sum\
        \ || (h->data[child+1].sum == h->data[child].sum && h->data[child+1].idx < h->data[child].idx)))\
        \ child++;\n            if (last.sum < h->data[child].sum || (last.sum == h->data[child].sum\
        \ && last.idx <= h->data[child].idx)) break;\n            h->data[i] = h->data[child];\
        \ i = child;\n        }\n        h->data[i] = last;\n    }\n    return res;\n\
        }\n\nint minimumPairRemoval(int* nums, int numsSize) {\n    if (numsSize < 2)\
        \ return 0;\n    long long* val = (long long*)malloc(sizeof(long long) * numsSize);\n\
        \    int* L = (int*)malloc(sizeof(int) * numsSize);\n    int* R = (int*)malloc(sizeof(int)\
        \ * numsSize);\n    bool* alive = (bool*)malloc(sizeof(bool) * numsSize);\n\
        \    for (int i = 0; i < numsSize; i++) {\n        val[i] = nums[i]; L[i] =\
        \ i - 1;\n        R[i] = (i == numsSize - 1) ? -1 : i + 1; alive[i] = true;\n\
        \    }\n    MinHeap h; h.capacity = numsSize * 3; h.data = (HeapNode*)malloc(sizeof(HeapNode)\
        \ * h.capacity); h.size = 0;\n    int violations = 0;\n    for (int i = 0; i\
        \ < numsSize - 1; i++) {\n        if (val[i] > val[i + 1]) violations++;\n \
        \       push(&h, val[i] + val[i + 1], i);\n    }\n    int ops = 0;\n    while\
        \ (violations > 0 && h.size > 0) {\n        HeapNode top = pop(&h);\n      \
        \  int i = top.idx;\n        if (!alive[i] || R[i] == -1 || val[i] + val[R[i]]\
        \ != top.sum) continue;\n        int j = R[i];\n        if (L[i] != -1 && val[L[i]]\
        \ > val[i]) violations--;\n        if (val[i] > val[j]) violations--;\n    \
        \    if (R[j] != -1 && val[j] > val[R[j]]) violations--;\n        val[i] +=\
        \ val[j]; alive[j] = false; R[i] = R[j];\n        if (R[j] != -1) L[R[j]] =\
        \ i;\n        if (L[i] != -1 && val[L[i]] > val[i]) violations++;\n        if\
        \ (R[i] != -1 && val[i] > val[R[i]]) violations++;\n        if (L[i] != -1)\
        \ push(&h, val[L[i]] + val[i], L[i]);\n        if (R[i] != -1) push(&h, val[i]\
        \ + val[R[i]], i);\n        ops++;\n    }\n    free(val); free(L); free(R);\
        \ free(alive); free(h.data);\n    return ops;\n}"
      csharp: "public class Solution {\n    public int MinimumPairRemoval(int[] nums)\
        \ {\n        int n = nums.Length;\n        if (n < 2) return 0;\n        long[]\
        \ val = new long[n];\n        int[] L = new int[n];\n        int[] R = new int[n];\n\
        \        bool[] alive = new bool[n];\n        var pq = new PriorityQueue<int,\
        \ (long sum, int idx)>(\n            Comparer<(long sum, int idx)>.Create((a,\
        \ b) => {\n                int cmp = a.sum.CompareTo(b.sum);\n             \
        \   return cmp != 0 ? cmp : a.idx.CompareTo(b.idx);\n            })\n      \
        \  );\n        int violations = 0;\n        for (int i = 0; i < n; i++) {\n\
        \            val[i] = nums[i];\n            L[i] = i - 1;\n            R[i]\
        \ = (i == n - 1) ? -1 : i + 1;\n            alive[i] = true;\n        }\n  \
        \      for (int i = 0; i < n - 1; i++) {\n            if (val[i] > val[i + 1])\
        \ violations++;\n            pq.Enqueue(i, (val[i] + val[i + 1], i));\n    \
        \    }\n        int ops = 0;\n        while (violations > 0 && pq.Count > 0)\
        \ {\n            pq.TryDequeue(out int i, out var top);\n            if (!alive[i]\
        \ || R[i] == -1 || val[i] + val[R[i]] != top.sum) continue;\n            int\
        \ j = R[i];\n            if (L[i] != -1 && val[L[i]] > val[i]) violations--;\n\
        \            if (val[i] > val[j]) violations--;\n            if (R[j] != -1\
        \ && val[j] > val[R[j]]) violations--;\n            val[i] += val[j];\n    \
        \        alive[j] = false;\n            R[i] = R[j];\n            if (R[j] !=\
        \ -1) L[R[j]] = i;\n            if (L[i] != -1 && val[L[i]] > val[i]) violations++;\n\
        \            if (R[i] != -1 && val[i] > val[R[i]]) violations++;\n         \
        \   if (L[i] != -1) pq.Enqueue(L[i], (val[L[i]] + val[i], L[i]));\n        \
        \    if (R[i] != -1) pq.Enqueue(i, (val[i] + val[R[i]], i));\n            ops++;\n\
        \        }\n        return ops;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minimumPairRemoval\
        \ = function(nums) {\n    let n = nums.length;\n    if (n < 2) return 0;\n \
        \   let val = new BigInt64Array(nums.map(BigInt));\n    let L = new Int32Array(n).fill(-1);\n\
        \    let R = new Int32Array(n).fill(-1);\n    let alive = new Uint8Array(n).fill(1);\n\
        \    for (let i = 0; i < n; i++) {\n        L[i] = i - 1;\n        R[i] = (i\
        \ === n - 1) ? -1 : i + 1;\n    }\n    const pq = new MinPriorityQueue({\n \
        \       compare: (a, b) => {\n            if (a.sum < b.sum) return -1;\n  \
        \          if (a.sum > b.sum) return 1;\n            return a.idx - b.idx;\n\
        \        }\n    });\n    let violations = 0;\n    for (let i = 0; i < n - 1;\
        \ i++) {\n        if (val[i] > val[i + 1]) violations++;\n        pq.enqueue({\
        \ sum: val[i] + val[i + 1], idx: i });\n    }\n    let ops = 0;\n    while (violations\
        \ > 0 && !pq.isEmpty()) {\n        let { sum, idx } = pq.dequeue();\n      \
        \  if (!alive[idx] || R[idx] === -1 || val[idx] + val[R[idx]] !== sum) continue;\n\
        \        let nextIdx = R[idx];\n        if (L[idx] !== -1 && val[L[idx]] > val[idx])\
        \ violations--;\n        if (val[idx] > val[nextIdx]) violations--;\n      \
        \  if (R[nextIdx] !== -1 && val[nextIdx] > val[R[nextIdx]]) violations--;\n\
        \        val[idx] += val[nextIdx];\n        alive[nextIdx] = 0;\n        R[idx]\
        \ = R[nextIdx];\n        if (R[nextIdx] !== -1) L[R[nextIdx]] = idx;\n     \
        \   if (L[idx] !== -1 && val[L[idx]] > val[idx]) violations++;\n        if (R[idx]\
        \ !== -1 && val[idx] > val[R[idx]]) violations++;\n        if (L[idx] !== -1)\
        \ pq.enqueue({ sum: val[L[idx]] + val[idx], idx: L[idx] });\n        if (R[idx]\
        \ !== -1) pq.enqueue({ sum: val[idx] + val[R[idx]], idx: idx });\n        ops++;\n\
        \    }\n    return ops;\n};"
      typescript: '// Generation failed for TypeScript

        // Reason: Generation failed: STOP'
      php: '// Generation failed for PHP

        // Reason: Generation failed: STOP'
      swift: '// Generation failed for Swift

        // Reason: Generation failed: STOP'
      kotlin: '// Generation failed for Kotlin

        // Reason: Generation failed: STOP'
      dart: '// Generation failed for Dart

        // Reason: Generation failed: STOP'
      go: '// Generation failed for Go

        // Reason: Generation failed: STOP'
      ruby: "class MinHeap\n  def initialize\n    @heap = []\n  end\n  def push(val)\n\
        \    @heap << val\n    bubble_up(@heap.size - 1)\n  end\n  def pop\n    return\
        \ nil if @heap.empty?\n    return @heap.pop if @heap.size == 1\n    res = @heap[0]\n\
        \    @heap[0] = @heap.pop\n    bubble_down(0)\n    res\n  end\n  def empty?\n\
        \    @heap.empty?\n  end\n  private\n  def bubble_up(index)\n    while index\
        \ > 0\n      parent = (index - 1) / 2\n      if @heap[index][0] < @heap[parent][0]\
        \ || (@heap[index][0] == @heap[parent][0] && @heap[index][1] < @heap[parent][1])\n\
        \        @heap[index], @heap[parent] = @heap[parent], @heap[index]\n       \
        \ index = parent\n      else\n        break\n      end\n    end\n  end\n  def\
        \ bubble_down(index)\n    while true\n      left = 2 * index + 1\n      right\
        \ = 2 * index + 2\n      smallest = index\n      if left < @heap.size && (@heap[left][0]\
        \ < @heap[smallest][0] || (@heap[left][0] == @heap[smallest][0] && @heap[left][1]\
        \ < @heap[smallest][1]))\n        smallest = left\n      end\n      if right\
        \ < @heap.size && (@heap[right][0] < @heap[smallest][0] || (@heap[right][0]\
        \ == @heap[smallest][0] && @heap[right][1] < @heap[smallest][1]))\n        smallest\
        \ = right\n      end\n      if smallest != index\n        @heap[index], @heap[smallest]\
        \ = @heap[smallest], @heap[index]\n        index = smallest\n      else\n  \
        \      break\n      end\n    end\n  end\nend\n\ndef minimum_pair_removal(nums)\n\
        \  n = nums.length\n  return 0 if n <= 1\n  vals = nums.map(&:to_i)\n  nxt =\
        \ Array.new(n) { |i| i == n - 1 ? -1 : i + 1 }\n  prv = Array.new(n) { |i| i\
        \ == 0 ? -1 : i - 1 }\n  active = Array.new(n, true)\n  pq = MinHeap.new\n \
        \ decreasing_count = 0\n  (0...n - 1).each do |i|\n    pq.push([vals[i] + vals[i\
        \ + 1], i])\n    decreasing_count += 1 if vals[i] > vals[i + 1]\n  end\n  ops\
        \ = 0\n  while decreasing_count > 0 && !pq.empty?\n    s, l = pq.pop\n    next\
        \ if !active[l] || nxt[l] == -1\n    r = nxt[l]\n    next if !active[r] || vals[l]\
        \ + vals[r] != s\n    p, nn = prv[l], nxt[r]\n    decreasing_count -= 1 if p\
        \ != -1 && vals[p] > vals[l]\n    decreasing_count -= 1 if vals[l] > vals[r]\n\
        \    decreasing_count -= 1 if nn != -1 && vals[r] > vals[nn]\n    vals[l] +=\
        \ vals[r]\n    active[r] = false\n    nxt[l] = nn\n    prv[nn] = l if nn !=\
        \ -1\n    decreasing_count += 1 if p != -1 && vals[p] > vals[l]\n    decreasing_count\
        \ += 1 if nn != -1 && vals[l] > vals[nn]\n    pq.push([vals[p] + vals[l], p])\
        \ if p != -1\n    pq.push([vals[l] + vals[nn], l]) if nn != -1\n    ops += 1\n\
        \  end\n  ops\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n  def minimumPairRemoval(nums:\
        \ Array[Int]): Int = {\n    val n = nums.length\n    if (n <= 1) return 0\n\
        \    val vals = nums.map(_.toLong)\n    val nxt = Array.tabulate(n)(i => if\
        \ (i == n - 1) -1 else i + 1)\n    val prv = Array.tabulate(n)(i => i - 1)\n\
        \    val active = Array.fill(n)(true)\n    val pq = mutable.PriorityQueue.empty[(Long,\
        \ Int)](\n      Ordering.by[(Long, Int), (Long, Int)](x => (-x._1, -x._2))\n\
        \    )\n    for (i <- 0 until n - 1) pq.enqueue((vals(i) + vals(i + 1), i))\n\
        \    var decCount = 0\n    for (i <- 0 until n - 1) if (vals(i) > vals(i + 1))\
        \ decCount += 1\n    var ops = 0\n    while (decCount > 0 && pq.nonEmpty) {\n\
        \      val (s, l) = pq.dequeue()\n      if (active(l) && nxt(l) != -1) {\n \
        \       val r = nxt(l)\n        if (active(r) && vals(l) + vals(r) == s) {\n\
        \          val p = prv(l)\n          val nn = nxt(r)\n          if (p != -1\
        \ && vals(p) > vals(l)) decCount -= 1\n          if (vals(l) > vals(r)) decCount\
        \ -= 1\n          if (nn != -1 && vals(r) > vals(nn)) decCount -= 1\n      \
        \    vals(l) += vals(r)\n          active(r) = false\n          nxt(l) = nn\n\
        \          if (nn != -1) prv(nn) = l\n          if (p != -1 && vals(p) > vals(l))\
        \ decCount += 1\n          if (nn != -1 && vals(l) > vals(nn)) decCount += 1\n\
        \          if (p != -1) pq.enqueue((vals(p) + vals(l), p))\n          if (nn\
        \ != -1) pq.enqueue((vals(l) + vals(nn), l))\n          ops += 1\n        }\n\
        \      }\n    }\n    ops\n  }\n}"
      rust: "use std::collections::BinaryHeap;\nuse std::cmp::Reverse;\n\nimpl Solution\
        \ {\n    pub fn minimum_pair_removal(nums: Vec<i32>) -> i32 {\n        let n\
        \ = nums.len();\n        if n <= 1 { return 0; }\n        let mut vals: Vec<i64>\
        \ = nums.into_iter().map(|x| x as i64).collect();\n        let mut nxt: Vec<i32>\
        \ = (0..n as i32).map(|i| if i == (n as i32 - 1) { -1 } else { i + 1 }).collect();\n\
        \        let mut prv: Vec<i32> = (0..n as i32).map(|i| if i == 0 { -1 } else\
        \ { i - 1 }).collect();\n        let mut active = vec![true; n];\n        let\
        \ mut pq = BinaryHeap::new();\n        for i in 0..n-1 {\n            pq.push(Reverse((vals[i]\
        \ + vals[i+1], i)));\n        }\n        let mut dec_count = 0;\n        for\
        \ i in 0..n-1 {\n            if vals[i] > vals[i+1] { dec_count += 1; }\n  \
        \      }\n        let mut ops = 0;\n        while dec_count > 0 {\n        \
        \    if let Some(Reverse((s, l_idx))) = pq.pop() {\n                let l =\
        \ l_idx;\n                let r_idx = nxt[l];\n                if r_idx != -1\
        \ {\n                    let r = r_idx as usize;\n                    if active[l]\
        \ && active[r] && vals[l] + vals[r] == s {\n                        let p =\
        \ prv[l];\n                        let nn = nxt[r];\n                      \
        \  if p != -1 && vals[p as usize] > vals[l] { dec_count -= 1; }\n          \
        \              if vals[l] > vals[r] { dec_count -= 1; }\n                  \
        \      if nn != -1 && vals[r] > vals[nn as usize] { dec_count -= 1; }\n    \
        \                    vals[l] += vals[r];\n                        active[r]\
        \ = false;\n                        nxt[l] = nn;\n                        if\
        \ nn != -1 { prv[nn as usize] = l as i32; }\n                        if p !=\
        \ -1 && vals[p as usize] > vals[l] { dec_count += 1; }\n                   \
        \     if nn != -1 && vals[l] > vals[nn as usize] { dec_count += 1; }\n     \
        \                   if p != -1 { pq.push(Reverse((vals[p as usize] + vals[l],\
        \ p as usize))); }\n                        if nn != -1 { pq.push(Reverse((vals[l]\
        \ + vals[nn as usize], l))); }\n                        ops += 1;\n        \
        \            }\n                }\n            } else { break; }\n        }\n\
        \        ops\n    }\n}"
      racket: "(require data/heap)\n(define/contract (minimum-pair-removal nums)\n \
        \ (-> (listof exact-integer?) exact-integer?)\n  (let* ([n (length nums)])\n\
        \    (if (<= n 1) 0\n        (let ([vals (list->vector nums)] [nxt (make-vector\
        \ n -1)] [prv (make-vector n -1)] [active (make-vector n #t)]\n            \
        \  [pq (make-heap (lambda (a b) (if (= (car a) (car b)) (<= (cdr a) (cdr b))\
        \ (< (car a) (car b)))))])\n          (for ([i (in-range (- n 1))])\n      \
        \      (vector-set! nxt i (+ i 1))\n            (vector-set! prv (+ i 1) i)\n\
        \            (heap-add! pq (cons (+ (vector-ref vals i) (vector-ref vals (+\
        \ i 1))) i)))\n          (let ([dc 0])\n            (for ([i (in-range (- n\
        \ 1))]) (when (> (vector-ref vals i) (vector-ref vals (+ i 1))) (set! dc (+\
        \ dc 1))))\n            (let loop ([dc dc] [ops 0])\n              (if (<= dc\
        \ 0) ops\n                  (if (= (heap-count pq) 0) ops\n                \
        \      (let* ([top (heap-min pq)] [s (car top)] [l (cdr top)])\n           \
        \             (heap-remove-min! pq)\n                        (let ([r (vector-ref\
        \ nxt l)])\n                          (if (and (not (= r -1)) (vector-ref active\
        \ l) (vector-ref active r) (= (+ (vector-ref vals l) (vector-ref vals r)) s))\n\
        \                              (let* ([p (vector-ref prv l)] [nn (vector-ref\
        \ nxt r)] [new-dc dc])\n                                (when (and (not (= p\
        \ -1)) (> (vector-ref vals p) (vector-ref vals l))) (set! new-dc (- new-dc 1)))\n\
        \                                (when (> (vector-ref vals l) (vector-ref vals\
        \ r)) (set! new-dc (- new-dc 1)))\n                                (when (and\
        \ (not (= nn -1)) (> (vector-ref vals r) (vector-ref vals nn))) (set! new-dc\
        \ (- new-dc 1)))\n                                (vector-set! vals l (+ (vector-ref\
        \ vals l) (vector-ref vals r)))\n                                (vector-set!\
        \ active r #f) (vector-set! nxt l nn)\n                                (when\
        \ (not (= nn -1)) (vector-set! prv nn l))\n                                (when\
        \ (and (not (= p -1)) (> (vector-ref vals p) (vector-ref vals l))) (set! new-dc\
        \ (+ new-dc 1)))\n                                (when (and (not (= nn -1))\
        \ (> (vector-ref vals l) (vector-ref vals nn))) (set! new-dc (+ new-dc 1)))\n\
        \                                (when (not (= p -1)) (heap-add! pq (cons (+\
        \ (vector-ref vals p) (vector-ref vals l)) p)))\n                          \
        \      (when (not (= nn -1)) (heap-add! pq (cons (+ (vector-ref vals l) (vector-ref\
        \ vals nn)) l)))\n                                (loop new-dc (+ ops 1))) (loop\
        \ dc ops)))))))))))"
      erlang: "-spec minimum_pair_removal(Nums :: [integer()]) -> integer().\nminimum_pair_removal(Nums)\
        \ ->\n  N = length(Nums),\n  if N =< 1 -> 0; true ->\n    Idxs = lists:seq(0,\
        \ N-1), Vals = maps:from_list(lists:zip(Idxs, Nums)),\n    Nxt = maps:from_list(lists:zip(lists:droplast(Idxs),\
        \ lists:nthtail(1, Idxs))),\n    Prv = maps:from_list(lists:zip(lists:nthtail(1,\
        \ Idxs), lists:droplast(Idxs))),\n    PQ = lists:foldl(fun(I, Acc) -> gb_sets:add({maps:get(I,\
        \ Vals) + maps:get(I+1, Vals), I}, Acc) end, gb_sets:new(), lists:droplast(Idxs)),\n\
        \    DC = lists:foldl(fun(I, Acc) -> if maps:get(I, Vals) > maps:get(I+1, Vals)\
        \ -> Acc + 1; true -> Acc end end, 0, lists:droplast(Idxs)),\n    simulate(Vals,\
        \ Nxt, Prv, PQ, DC, 0) end.\nsimulate(_, _, _, _, 0, Ops) -> Ops;\nsimulate(Vals,\
        \ Nxt, Prv, PQ, DC, Ops) ->\n  case gb_sets:is_empty(PQ) of true -> Ops; false\
        \ -> {{S, L}, PQ1} = gb_sets:take_smallest(PQ),\n    case maps:find(L, Nxt)\
        \ of {ok, R} -> SumLR = maps:get(L, Vals) + maps:get(R, Vals),\n      if SumLR\
        \ == S -> P = maps:get(L, Prv, -1), NN = maps:get(R, Nxt, -1),\n        D1 =\
        \ if P /= -1 andalso maps:get(P, Vals) > maps:get(L, Vals) -> DC - 1; true ->\
        \ DC end,\n        D2 = if maps:get(L, Vals) > maps:get(R, Vals) -> D1 - 1;\
        \ true -> D1 end,\n        D3 = if NN /= -1 andalso maps:get(R, Vals) > maps:get(NN,\
        \ Vals) -> D2 - 1; true -> D2 end,\n        NV = maps:put(L, SumLR, maps:remove(R,\
        \ Vals)), NX = maps:remove(R, Nxt), PV = maps:remove(R, Prv),\n        {NX2,\
        \ PV2} = if NN /= -1 -> {maps:put(L, NN, NX), maps:put(NN, L, PV)}; true ->\
        \ {maps:remove(L, NX), PV} end,\n        D4 = if P /= -1 andalso maps:get(P,\
        \ NV) > maps:get(L, NV) -> D3 + 1; true -> D3 end,\n        D5 = if NN /= -1\
        \ andalso maps:get(L, NV) > maps:get(NN, NV) -> D4 + 1; true -> D4 end,\n  \
        \      PQ2 = if P /= -1 -> gb_sets:add({maps:get(P, NV) + maps:get(L, NV), P},\
        \ PQ1); true -> PQ1 end,\n        PQ3 = if NN /= -1 -> gb_sets:add({maps:get(L,\
        \ NV) + maps:get(NN, NV), L}, PQ2); true -> PQ2 end,\n        simulate(NV, NX2,\
        \ PV2, PQ3, D5, Ops + 1); true -> simulate(Vals, Nxt, Prv, PQ1, DC, Ops) end;\n\
        \      error -> simulate(Vals, Nxt, Prv, PQ1, DC, Ops) end end."
      elixir: "defmodule Solution do\n  @spec minimum_pair_removal(nums :: [integer])\
        \ :: integer\n  def minimum_pair_removal(nums) do\n    n = length(nums)\n  \
        \  if n <= 1 do 0 else\n      vals = nums |> Enum.with_index() |> Enum.reduce(%{},\
        \ fn {v, i}, acc -> Map.put(acc, i, v) end)\n      nxt = if n > 1, do: 0..(n-2)\
        \ |> Enum.reduce(%{}, fn i, acc -> Map.put(acc, i, i + 1) end), else: %{}\n\
        \      prv = if n > 1, do: 1..(n-1) |> Enum.reduce(%{}, fn i, acc -> Map.put(acc,\
        \ i, i - 1) end), else: %{}\n      pq = if n > 1, do: 0..(n-2) |> Enum.reduce(:gb_sets.new(),\
        \ fn i, acc -> :gb_sets.add({Map.get(vals, i) + Map.get(vals, i + 1), i}, acc)\
        \ end), else: :gb_sets.new()\n      dc = if n > 1, do: 0..(n-2) |> Enum.count(fn\
        \ i -> Map.get(vals, i) > Map.get(vals, i + 1) end), else: 0\n      simulate(vals,\
        \ nxt, prv, pq, dc, 0)\n    end\n  end\n  defp simulate(vals, nxt, prv, pq,\
        \ dc, ops) do\n    if dc == 0 do ops else\n      case :gb_sets.is_empty(pq)\
        \ do\n        true -> ops\n        false -> {{s, l}, pq} = :gb_sets.take_smallest(pq)\n\
        \          case Map.get(nxt, l) do\n            nil -> simulate(vals, nxt, prv,\
        \ pq, dc, ops)\n            r -> if Map.get(vals, l) + Map.get(vals, r) == s\
        \ do\n                p = Map.get(prv, l, -1)\n                nn = Map.get(nxt,\
        \ r, -1)\n                new_dc = dc\n                if p != -1 and Map.get(vals,\
        \ p) > Map.get(vals, l), do: new_dc = new_dc - 1\n                if Map.get(vals,\
        \ l) > Map.get(vals, r), do: new_dc = new_dc - 1\n                if nn != -1\
        \ and Map.get(vals, r) > Map.get(vals, nn), do: new_dc = new_dc - 1\n      \
        \          sum = Map.get(vals, l) + Map.get(vals, r)\n                new_vals\
        \ = vals |> Map.put(l, sum) |> Map.delete(r)\n                new_nxt = nxt\
        \ |> Map.delete(r)\n                new_nxt = if nn != -1, do: Map.put(new_nxt,\
        \ l, nn), else: Map.delete(new_nxt, l)\n                new_prv = prv |> Map.delete(r)\n\
        \                if nn != -1, do: new_prv = Map.put(new_prv, nn, l)\n      \
        \          if p != -1 and Map.get(new_vals, p) > Map.get(new_vals, l), do: new_dc\
        \ = new_dc + 1\n                if nn != -1 and Map.get(new_vals, l) > Map.get(new_vals,\
        \ nn), do: new_dc = new_dc + 1\n                new_pq = pq\n              \
        \  if p != -1, do: new_pq = :gb_sets.add({Map.get(new_vals, p) + Map.get(new_vals,\
        \ l), p}, new_pq)\n                if nn != -1, do: new_pq = :gb_sets.add({Map.get(new_vals,\
        \ l) + Map.get(new_vals, nn), l}, new_pq)\n                simulate(new_vals,\
        \ new_nxt, new_prv, new_pq, new_dc, ops + 1)\n              else\n         \
        \       simulate(vals, nxt, prv, pq, dc, ops)\n              end\n         \
        \ end\n      end\n    end\n  end\nend"
    approach: 'The problem specifies a deterministic simulation process where the adjacent
      pair with the minimum sum (and the leftmost one in case of ties) is repeatedly
      merged until the array is non-decreasing. To implement this efficiently, we use
      a doubly linked list structure (represented by arrays L and R for left and right
      neighbors) to manage the merges and a Min-Priority Queue to quickly find the pair
      with the minimum sum. We also maintain a count of ''violations'' (where nums[i]
      > nums[i+1]) to quickly determine when the array becomes non-decreasing.


      Each merge operation involves popping the minimum sum pair (s, i) from the priority
      queue and verifying its validity (checking if indices are still alive and if their
      current sum matches ''s''). Upon a valid merge of index i and its right neighbor
      j, we update the value at index i to the new sum, update the adjacency pointers,
      and decrement the violation count if the removed pairs (L[i], i), (i, j), and
      (j, R[j]) were violations. We then increment the violation count based on the
      new pairs (L[i], i) and (i, R[j]). New sums for these adjacent pairs are pushed
      into the priority queue. This approach ensures each merge and update is O(log
      N), leading to an overall efficient simulation.'
    time_complexity: O(N log N), where N is the length of the array. Each of the at
      most N-1 merges involves popping from and pushing into the priority queue, which
      takes logarithmic time. The total number of elements pushed into the queue is
      proportional to N.
    space_complexity: O(N), as we maintain several arrays (L, R, val, alive) and a priority
      queue, each storing at most O(N) elements to manage the state of the simulation.
    elapsed_time: 479.20956921577454
    model: gemini-3-pro-preview
    generated_at: '2026-01-23 14:55:35 '
---

## Problem #3510: Minimum Pair Removal to Sort Array II

**Difficulty:** Hard

**Topics:** Array, Hash Table, Linked List, Heap (Priority Queue), Simulation, Doubly-Linked List, Ordered Set

## Problem Description

<p>Given an array <code>nums</code>, you can perform the following operation any number of times:</p>

<ul>
	<li>Select the <strong>adjacent</strong> pair with the <strong>minimum</strong> sum in <code>nums</code>. If multiple such pairs exist, choose the leftmost one.</li>
	<li>Replace the pair with their sum.</li>
</ul>

<p>Return the <strong>minimum number of operations</strong> needed to make the array <strong>non-decreasing</strong>.</p>

<p>An array is said to be <strong>non-decreasing</strong> if each element is greater than or equal to its previous element (if it exists).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,2,3,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The pair <code>(3,1)</code> has the minimum sum of 4. After replacement, <code>nums = [5,2,4]</code>.</li>
	<li>The pair <code>(2,4)</code> has the minimum sum of 6. After replacement, <code>nums = [5,6]</code>.</li>
</ul>

<p>The array <code>nums</code> became non-decreasing in two operations.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>The array <code>nums</code> is already sorted.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. We can perform the simulation using data structures.

2. Maintain an array index and value using a map since we need to find the next and previous ones.

3. Maintain the indices to be removed using a hash set.

4. Maintain the neighbor sums with the smaller indices (set or priority queue).

5. Keep the 3 structures in sync during the removals.

## ✨ AI-Generated Solution (gemini-3-pro-preview)

### Approach

The problem specifies a deterministic simulation process where the adjacent pair with the minimum sum (and the leftmost one in case of ties) is repeatedly merged until the array is non-decreasing. To implement this efficiently, we use a doubly linked list structure (represented by arrays L and R for left and right neighbors) to manage the merges and a Min-Priority Queue to quickly find the pair with the minimum sum. We also maintain a count of 'violations' (where nums[i] > nums[i+1]) to quickly determine when the array becomes non-decreasing.

Each merge operation involves popping the minimum sum pair (s, i) from the priority queue and verifying its validity (checking if indices are still alive and if their current sum matches 's'). Upon a valid merge of index i and its right neighbor j, we update the value at index i to the new sum, update the adjacency pointers, and decrement the violation count if the removed pairs (L[i], i), (i, j), and (j, R[j]) were violations. We then increment the violation count based on the new pairs (L[i], i) and (i, R[j]). New sums for these adjacent pairs are pushed into the priority queue. This approach ensures each merge and update is O(log N), leading to an overall efficient simulation.

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
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return 0;
        vector<long long> val(n);
        vector<int> L(n), R(n);
        vector<bool> alive(n, true);
        for (int i = 0; i < n; ++i) {
            val[i] = nums[i];
            L[i] = i - 1;
            R[i] = (i == n - 1) ? -1 : i + 1;
        }
        typedef pair<long long, int> P;
        priority_queue<P, vector<P>, greater<P>> pq;
        int violations = 0;
        for (int i = 0; i < n - 1; ++i) {
            if (val[i] > val[i + 1]) violations++;
            pq.push({val[i] + val[i + 1], i});
        }
        int ops = 0;
        while (violations > 0 && !pq.empty()) {
            P top = pq.top();
            pq.pop();
            int i = top.second;
            if (!alive[i] || R[i] == -1 || val[i] + val[R[i]] != top.first) continue;
            int j = R[i];
            if (L[i] != -1 && val[L[i]] > val[i]) violations--;
            if (val[i] > val[j]) violations--;
            if (R[j] != -1 && val[j] > val[R[j]]) violations--;
            val[i] += val[j];
            alive[j] = false;
            R[i] = R[j];
            if (R[j] != -1) L[R[j]] = i;
            if (L[i] != -1 && val[L[i]] > val[i]) violations++;
            if (R[i] != -1 && val[i] > val[R[i]]) violations++;
            if (L[i] != -1) pq.push({val[L[i]] + val[i], L[i]});
            if (R[i] != -1) pq.push({val[i] + val[R[i]], i});
            ops++;
        }
        return ops;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    static class Node implements Comparable<Node> {
        long sum;
        int idx;
        Node(long s, int i) {
            this.sum = s;
            this.idx = i;
        }
        public int compareTo(Node other) {
            if (this.sum != other.sum) return Long.compare(this.sum, other.sum);
            return Integer.compare(this.idx, other.idx);
        }
    }
    public int minimumPairRemoval(int[] nums) {
        int n = nums.length;
        if (n < 2) return 0;
        long[] val = new long[n];
        int[] L = new int[n];
        int[] R = new int[n];
        boolean[] alive = new boolean[n];
        PriorityQueue<Node> pq = new PriorityQueue<>();
        int violations = 0;
        for (int i = 0; i < n; i++) {
            val[i] = nums[i];
            L[i] = i - 1;
            R[i] = (i == n - 1) ? -1 : i + 1;
            alive[i] = true;
        }
        for (int i = 0; i < n - 1; i++) {
            if (val[i] > val[i + 1]) violations++;
            pq.add(new Node(val[i] + val[i + 1], i));
        }
        int ops = 0;
        while (violations > 0 && !pq.isEmpty()) {
            Node top = pq.poll();
            int i = top.idx;
            if (!alive[i] || R[i] == -1 || val[i] + val[R[i]] != top.sum) continue;
            int j = R[i];
            if (L[i] != -1 && val[L[i]] > val[i]) violations--;
            if (val[i] > val[j]) violations--;
            if (R[j] != -1 && val[j] > val[R[j]]) violations--;
            val[i] += val[j];
            alive[j] = false;
            R[i] = R[j];
            if (R[j] != -1) L[R[j]] = i;
            if (L[i] != -1 && val[L[i]] > val[i]) violations++;
            if (R[i] != -1 && val[i] > val[R[i]]) violations++;
            if (L[i] != -1) pq.add(new Node(val[L[i]] + val[i], L[i]));
            if (R[i] != -1) pq.add(new Node(val[i] + val[R[i]], i));
            ops++;
        }
        return ops;
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
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        val = [long(x) for x in nums]
        L = [i - 1 for i in range(n)]
        R = [i + 1 for i in range(n)]
        R[n - 1] = -1
        alive = [True] * n
        pq = []
        violations = 0
        for i in range(n - 1):
            if val[i] > val[i + 1]:
                violations += 1
            heapq.heappush(pq, (val[i] + val[i + 1], i))

        ops = 0
        while violations > 0 and pq:
            s, i = heapq.heappop(pq)
            if not alive[i] or R[i] == -1 or val[i] + val[R[i]] != s:
                continue
            j = R[i]
            if L[i] != -1 and val[L[i]] > val[i]: violations -= 1
            if val[i] > val[j]: violations -= 1
            if R[j] != -1 and val[j] > val[R[j]]: violations -= 1
            val[i] += val[j]
            alive[j] = False
            R[i] = R[j]
            if R[j] != -1: L[R[j]] = i
            if L[i] != -1 and val[L[i]] > val[i]: violations += 1
            if R[i] != -1 and val[i] > val[R[i]]: violations += 1
            if L[i] != -1: heapq.heappush(pq, (val[L[i]] + val[i], L[i]))
            if R[i] != -1: heapq.heappush(pq, (val[i] + val[R[i]], i))
            ops += 1
        return ops
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        val = [int(x) for x in nums]
        L = [i - 1 for i in range(n)]
        R = [i + 1 for i in range(n)]
        R[n - 1] = -1
        alive = [True] * n
        pq = []
        violations = 0
        for i in range(n - 1):
            if val[i] > val[i + 1]:
                violations += 1
            heapq.heappush(pq, (val[i] + val[i + 1], i))

        ops = 0
        while violations > 0 and pq:
            s, i = heapq.heappop(pq)
            if not alive[i] or R[i] == -1 or val[i] + val[R[i]] != s:
                continue
            j = R[i]
            if L[i] != -1 and val[L[i]] > val[i]: violations -= 1
            if val[i] > val[j]: violations -= 1
            if R[j] != -1 and val[j] > val[R[j]]: violations -= 1
            val[i] += val[j]
            alive[j] = False
            R[i] = R[j]
            if R[j] != -1: L[R[j]] = i
            if L[i] != -1 and val[L[i]] > val[i]: violations += 1
            if R[i] != -1 and val[i] > val[R[i]]: violations += 1
            if L[i] != -1: heapq.heappush(pq, (val[L[i]] + val[i], L[i]))
            if R[i] != -1: heapq.heappush(pq, (val[i] + val[R[i]], i))
            ops += 1
        return ops
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    long long sum;
    int idx;
} HeapNode;

typedef struct {
    HeapNode* data;
    int size;
    int capacity;
} MinHeap;

void push(MinHeap* h, long long sum, int idx) {
    if (h->size == h->capacity) {
        h->capacity *= 2;
        h->data = (HeapNode*)realloc(h->data, sizeof(HeapNode) * h->capacity);
    }
    int i = h->size++;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->data[p].sum < sum || (h->data[p].sum == sum && h->data[p].idx <= idx)) break;
        h->data[i] = h->data[p];
        i = p;
    }
    h->data[i].sum = sum; h->data[i].idx = idx;
}

HeapNode pop(MinHeap* h) {
    HeapNode res = h->data[0];
    h->size--;
    if (h->size > 0) {
        HeapNode last = h->data[h->size];
        int i = 0;
        while (i * 2 + 1 < h->size) {
            int child = i * 2 + 1;
            if (child + 1 < h->size && (h->data[child + 1].sum < h->data[child].sum || (h->data[child+1].sum == h->data[child].sum && h->data[child+1].idx < h->data[child].idx))) child++;
            if (last.sum < h->data[child].sum || (last.sum == h->data[child].sum && last.idx <= h->data[child].idx)) break;
            h->data[i] = h->data[child]; i = child;
        }
        h->data[i] = last;
    }
    return res;
}

int minimumPairRemoval(int* nums, int numsSize) {
    if (numsSize < 2) return 0;
    long long* val = (long long*)malloc(sizeof(long long) * numsSize);
    int* L = (int*)malloc(sizeof(int) * numsSize);
    int* R = (int*)malloc(sizeof(int) * numsSize);
    bool* alive = (bool*)malloc(sizeof(bool) * numsSize);
    for (int i = 0; i < numsSize; i++) {
        val[i] = nums[i]; L[i] = i - 1;
        R[i] = (i == numsSize - 1) ? -1 : i + 1; alive[i] = true;
    }
    MinHeap h; h.capacity = numsSize * 3; h.data = (HeapNode*)malloc(sizeof(HeapNode) * h.capacity); h.size = 0;
    int violations = 0;
    for (int i = 0; i < numsSize - 1; i++) {
        if (val[i] > val[i + 1]) violations++;
        push(&h, val[i] + val[i + 1], i);
    }
    int ops = 0;
    while (violations > 0 && h.size > 0) {
        HeapNode top = pop(&h);
        int i = top.idx;
        if (!alive[i] || R[i] == -1 || val[i] + val[R[i]] != top.sum) continue;
        int j = R[i];
        if (L[i] != -1 && val[L[i]] > val[i]) violations--;
        if (val[i] > val[j]) violations--;
        if (R[j] != -1 && val[j] > val[R[j]]) violations--;
        val[i] += val[j]; alive[j] = false; R[i] = R[j];
        if (R[j] != -1) L[R[j]] = i;
        if (L[i] != -1 && val[L[i]] > val[i]) violations++;
        if (R[i] != -1 && val[i] > val[R[i]]) violations++;
        if (L[i] != -1) push(&h, val[L[i]] + val[i], L[i]);
        if (R[i] != -1) push(&h, val[i] + val[R[i]], i);
        ops++;
    }
    free(val); free(L); free(R); free(alive); free(h.data);
    return ops;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinimumPairRemoval(int[] nums) {
        int n = nums.Length;
        if (n < 2) return 0;
        long[] val = new long[n];
        int[] L = new int[n];
        int[] R = new int[n];
        bool[] alive = new bool[n];
        var pq = new PriorityQueue<int, (long sum, int idx)>(
            Comparer<(long sum, int idx)>.Create((a, b) => {
                int cmp = a.sum.CompareTo(b.sum);
                return cmp != 0 ? cmp : a.idx.CompareTo(b.idx);
            })
        );
        int violations = 0;
        for (int i = 0; i < n; i++) {
            val[i] = nums[i];
            L[i] = i - 1;
            R[i] = (i == n - 1) ? -1 : i + 1;
            alive[i] = true;
        }
        for (int i = 0; i < n - 1; i++) {
            if (val[i] > val[i + 1]) violations++;
            pq.Enqueue(i, (val[i] + val[i + 1], i));
        }
        int ops = 0;
        while (violations > 0 && pq.Count > 0) {
            pq.TryDequeue(out int i, out var top);
            if (!alive[i] || R[i] == -1 || val[i] + val[R[i]] != top.sum) continue;
            int j = R[i];
            if (L[i] != -1 && val[L[i]] > val[i]) violations--;
            if (val[i] > val[j]) violations--;
            if (R[j] != -1 && val[j] > val[R[j]]) violations--;
            val[i] += val[j];
            alive[j] = false;
            R[i] = R[j];
            if (R[j] != -1) L[R[j]] = i;
            if (L[i] != -1 && val[L[i]] > val[i]) violations++;
            if (R[i] != -1 && val[i] > val[R[i]]) violations++;
            if (L[i] != -1) pq.Enqueue(L[i], (val[L[i]] + val[i], L[i]));
            if (R[i] != -1) pq.Enqueue(i, (val[i] + val[R[i]], i));
            ops++;
        }
        return ops;
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
var minimumPairRemoval = function(nums) {
    let n = nums.length;
    if (n < 2) return 0;
    let val = new BigInt64Array(nums.map(BigInt));
    let L = new Int32Array(n).fill(-1);
    let R = new Int32Array(n).fill(-1);
    let alive = new Uint8Array(n).fill(1);
    for (let i = 0; i < n; i++) {
        L[i] = i - 1;
        R[i] = (i === n - 1) ? -1 : i + 1;
    }
    const pq = new MinPriorityQueue({
        compare: (a, b) => {
            if (a.sum < b.sum) return -1;
            if (a.sum > b.sum) return 1;
            return a.idx - b.idx;
        }
    });
    let violations = 0;
    for (let i = 0; i < n - 1; i++) {
        if (val[i] > val[i + 1]) violations++;
        pq.enqueue({ sum: val[i] + val[i + 1], idx: i });
    }
    let ops = 0;
    while (violations > 0 && !pq.isEmpty()) {
        let { sum, idx } = pq.dequeue();
        if (!alive[idx] || R[idx] === -1 || val[idx] + val[R[idx]] !== sum) continue;
        let nextIdx = R[idx];
        if (L[idx] !== -1 && val[L[idx]] > val[idx]) violations--;
        if (val[idx] > val[nextIdx]) violations--;
        if (R[nextIdx] !== -1 && val[nextIdx] > val[R[nextIdx]]) violations--;
        val[idx] += val[nextIdx];
        alive[nextIdx] = 0;
        R[idx] = R[nextIdx];
        if (R[nextIdx] !== -1) L[R[nextIdx]] = idx;
        if (L[idx] !== -1 && val[L[idx]] > val[idx]) violations++;
        if (R[idx] !== -1 && val[idx] > val[R[idx]]) violations++;
        if (L[idx] !== -1) pq.enqueue({ sum: val[L[idx]] + val[idx], idx: L[idx] });
        if (R[idx] !== -1) pq.enqueue({ sum: val[idx] + val[R[idx]], idx: idx });
        ops++;
    }
    return ops;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
// Generation failed for TypeScript
// Reason: Generation failed: STOP
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
// Generation failed for PHP
// Reason: Generation failed: STOP
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
// Generation failed for Swift
// Reason: Generation failed: STOP
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
// Generation failed for Kotlin
// Reason: Generation failed: STOP
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
// Generation failed for Dart
// Reason: Generation failed: STOP
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
// Generation failed for Go
// Reason: Generation failed: STOP
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
    return @heap.pop if @heap.size == 1
    res = @heap[0]
    @heap[0] = @heap.pop
    bubble_down(0)
    res
  end
  def empty?
    @heap.empty?
  end
  private
  def bubble_up(index)
    while index > 0
      parent = (index - 1) / 2
      if @heap[index][0] < @heap[parent][0] || (@heap[index][0] == @heap[parent][0] && @heap[index][1] < @heap[parent][1])
        @heap[index], @heap[parent] = @heap[parent], @heap[index]
        index = parent
      else
        break
      end
    end
  end
  def bubble_down(index)
    while true
      left = 2 * index + 1
      right = 2 * index + 2
      smallest = index
      if left < @heap.size && (@heap[left][0] < @heap[smallest][0] || (@heap[left][0] == @heap[smallest][0] && @heap[left][1] < @heap[smallest][1]))
        smallest = left
      end
      if right < @heap.size && (@heap[right][0] < @heap[smallest][0] || (@heap[right][0] == @heap[smallest][0] && @heap[right][1] < @heap[smallest][1]))
        smallest = right
      end
      if smallest != index
        @heap[index], @heap[smallest] = @heap[smallest], @heap[index]
        index = smallest
      else
        break
      end
    end
  end
end

def minimum_pair_removal(nums)
  n = nums.length
  return 0 if n <= 1
  vals = nums.map(&:to_i)
  nxt = Array.new(n) { |i| i == n - 1 ? -1 : i + 1 }
  prv = Array.new(n) { |i| i == 0 ? -1 : i - 1 }
  active = Array.new(n, true)
  pq = MinHeap.new
  decreasing_count = 0
  (0...n - 1).each do |i|
    pq.push([vals[i] + vals[i + 1], i])
    decreasing_count += 1 if vals[i] > vals[i + 1]
  end
  ops = 0
  while decreasing_count > 0 && !pq.empty?
    s, l = pq.pop
    next if !active[l] || nxt[l] == -1
    r = nxt[l]
    next if !active[r] || vals[l] + vals[r] != s
    p, nn = prv[l], nxt[r]
    decreasing_count -= 1 if p != -1 && vals[p] > vals[l]
    decreasing_count -= 1 if vals[l] > vals[r]
    decreasing_count -= 1 if nn != -1 && vals[r] > vals[nn]
    vals[l] += vals[r]
    active[r] = false
    nxt[l] = nn
    prv[nn] = l if nn != -1
    decreasing_count += 1 if p != -1 && vals[p] > vals[l]
    decreasing_count += 1 if nn != -1 && vals[l] > vals[nn]
    pq.push([vals[p] + vals[l], p]) if p != -1
    pq.push([vals[l] + vals[nn], l]) if nn != -1
    ops += 1
  end
  ops
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
  def minimumPairRemoval(nums: Array[Int]): Int = {
    val n = nums.length
    if (n <= 1) return 0
    val vals = nums.map(_.toLong)
    val nxt = Array.tabulate(n)(i => if (i == n - 1) -1 else i + 1)
    val prv = Array.tabulate(n)(i => i - 1)
    val active = Array.fill(n)(true)
    val pq = mutable.PriorityQueue.empty[(Long, Int)](
      Ordering.by[(Long, Int), (Long, Int)](x => (-x._1, -x._2))
    )
    for (i <- 0 until n - 1) pq.enqueue((vals(i) + vals(i + 1), i))
    var decCount = 0
    for (i <- 0 until n - 1) if (vals(i) > vals(i + 1)) decCount += 1
    var ops = 0
    while (decCount > 0 && pq.nonEmpty) {
      val (s, l) = pq.dequeue()
      if (active(l) && nxt(l) != -1) {
        val r = nxt(l)
        if (active(r) && vals(l) + vals(r) == s) {
          val p = prv(l)
          val nn = nxt(r)
          if (p != -1 && vals(p) > vals(l)) decCount -= 1
          if (vals(l) > vals(r)) decCount -= 1
          if (nn != -1 && vals(r) > vals(nn)) decCount -= 1
          vals(l) += vals(r)
          active(r) = false
          nxt(l) = nn
          if (nn != -1) prv(nn) = l
          if (p != -1 && vals(p) > vals(l)) decCount += 1
          if (nn != -1 && vals(l) > vals(nn)) decCount += 1
          if (p != -1) pq.enqueue((vals(p) + vals(l), p))
          if (nn != -1) pq.enqueue((vals(l) + vals(nn), l))
          ops += 1
        }
      }
    }
    ops
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn minimum_pair_removal(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n <= 1 { return 0; }
        let mut vals: Vec<i64> = nums.into_iter().map(|x| x as i64).collect();
        let mut nxt: Vec<i32> = (0..n as i32).map(|i| if i == (n as i32 - 1) { -1 } else { i + 1 }).collect();
        let mut prv: Vec<i32> = (0..n as i32).map(|i| if i == 0 { -1 } else { i - 1 }).collect();
        let mut active = vec![true; n];
        let mut pq = BinaryHeap::new();
        for i in 0..n-1 {
            pq.push(Reverse((vals[i] + vals[i+1], i)));
        }
        let mut dec_count = 0;
        for i in 0..n-1 {
            if vals[i] > vals[i+1] { dec_count += 1; }
        }
        let mut ops = 0;
        while dec_count > 0 {
            if let Some(Reverse((s, l_idx))) = pq.pop() {
                let l = l_idx;
                let r_idx = nxt[l];
                if r_idx != -1 {
                    let r = r_idx as usize;
                    if active[l] && active[r] && vals[l] + vals[r] == s {
                        let p = prv[l];
                        let nn = nxt[r];
                        if p != -1 && vals[p as usize] > vals[l] { dec_count -= 1; }
                        if vals[l] > vals[r] { dec_count -= 1; }
                        if nn != -1 && vals[r] > vals[nn as usize] { dec_count -= 1; }
                        vals[l] += vals[r];
                        active[r] = false;
                        nxt[l] = nn;
                        if nn != -1 { prv[nn as usize] = l as i32; }
                        if p != -1 && vals[p as usize] > vals[l] { dec_count += 1; }
                        if nn != -1 && vals[l] > vals[nn as usize] { dec_count += 1; }
                        if p != -1 { pq.push(Reverse((vals[p as usize] + vals[l], p as usize))); }
                        if nn != -1 { pq.push(Reverse((vals[l] + vals[nn as usize], l))); }
                        ops += 1;
                    }
                }
            } else { break; }
        }
        ops
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(require data/heap)
(define/contract (minimum-pair-removal nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)])
    (if (<= n 1) 0
        (let ([vals (list->vector nums)] [nxt (make-vector n -1)] [prv (make-vector n -1)] [active (make-vector n #t)]
              [pq (make-heap (lambda (a b) (if (= (car a) (car b)) (<= (cdr a) (cdr b)) (< (car a) (car b)))))])
          (for ([i (in-range (- n 1))])
            (vector-set! nxt i (+ i 1))
            (vector-set! prv (+ i 1) i)
            (heap-add! pq (cons (+ (vector-ref vals i) (vector-ref vals (+ i 1))) i)))
          (let ([dc 0])
            (for ([i (in-range (- n 1))]) (when (> (vector-ref vals i) (vector-ref vals (+ i 1))) (set! dc (+ dc 1))))
            (let loop ([dc dc] [ops 0])
              (if (<= dc 0) ops
                  (if (= (heap-count pq) 0) ops
                      (let* ([top (heap-min pq)] [s (car top)] [l (cdr top)])
                        (heap-remove-min! pq)
                        (let ([r (vector-ref nxt l)])
                          (if (and (not (= r -1)) (vector-ref active l) (vector-ref active r) (= (+ (vector-ref vals l) (vector-ref vals r)) s))
                              (let* ([p (vector-ref prv l)] [nn (vector-ref nxt r)] [new-dc dc])
                                (when (and (not (= p -1)) (> (vector-ref vals p) (vector-ref vals l))) (set! new-dc (- new-dc 1)))
                                (when (> (vector-ref vals l) (vector-ref vals r)) (set! new-dc (- new-dc 1)))
                                (when (and (not (= nn -1)) (> (vector-ref vals r) (vector-ref vals nn))) (set! new-dc (- new-dc 1)))
                                (vector-set! vals l (+ (vector-ref vals l) (vector-ref vals r)))
                                (vector-set! active r #f) (vector-set! nxt l nn)
                                (when (not (= nn -1)) (vector-set! prv nn l))
                                (when (and (not (= p -1)) (> (vector-ref vals p) (vector-ref vals l))) (set! new-dc (+ new-dc 1)))
                                (when (and (not (= nn -1)) (> (vector-ref vals l) (vector-ref vals nn))) (set! new-dc (+ new-dc 1)))
                                (when (not (= p -1)) (heap-add! pq (cons (+ (vector-ref vals p) (vector-ref vals l)) p)))
                                (when (not (= nn -1)) (heap-add! pq (cons (+ (vector-ref vals l) (vector-ref vals nn)) l)))
                                (loop new-dc (+ ops 1))) (loop dc ops)))))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_pair_removal(Nums :: [integer()]) -> integer().
minimum_pair_removal(Nums) ->
  N = length(Nums),
  if N =< 1 -> 0; true ->
    Idxs = lists:seq(0, N-1), Vals = maps:from_list(lists:zip(Idxs, Nums)),
    Nxt = maps:from_list(lists:zip(lists:droplast(Idxs), lists:nthtail(1, Idxs))),
    Prv = maps:from_list(lists:zip(lists:nthtail(1, Idxs), lists:droplast(Idxs))),
    PQ = lists:foldl(fun(I, Acc) -> gb_sets:add({maps:get(I, Vals) + maps:get(I+1, Vals), I}, Acc) end, gb_sets:new(), lists:droplast(Idxs)),
    DC = lists:foldl(fun(I, Acc) -> if maps:get(I, Vals) > maps:get(I+1, Vals) -> Acc + 1; true -> Acc end end, 0, lists:droplast(Idxs)),
    simulate(Vals, Nxt, Prv, PQ, DC, 0) end.
simulate(_, _, _, _, 0, Ops) -> Ops;
simulate(Vals, Nxt, Prv, PQ, DC, Ops) ->
  case gb_sets:is_empty(PQ) of true -> Ops; false -> {{S, L}, PQ1} = gb_sets:take_smallest(PQ),
    case maps:find(L, Nxt) of {ok, R} -> SumLR = maps:get(L, Vals) + maps:get(R, Vals),
      if SumLR == S -> P = maps:get(L, Prv, -1), NN = maps:get(R, Nxt, -1),
        D1 = if P /= -1 andalso maps:get(P, Vals) > maps:get(L, Vals) -> DC - 1; true -> DC end,
        D2 = if maps:get(L, Vals) > maps:get(R, Vals) -> D1 - 1; true -> D1 end,
        D3 = if NN /= -1 andalso maps:get(R, Vals) > maps:get(NN, Vals) -> D2 - 1; true -> D2 end,
        NV = maps:put(L, SumLR, maps:remove(R, Vals)), NX = maps:remove(R, Nxt), PV = maps:remove(R, Prv),
        {NX2, PV2} = if NN /= -1 -> {maps:put(L, NN, NX), maps:put(NN, L, PV)}; true -> {maps:remove(L, NX), PV} end,
        D4 = if P /= -1 andalso maps:get(P, NV) > maps:get(L, NV) -> D3 + 1; true -> D3 end,
        D5 = if NN /= -1 andalso maps:get(L, NV) > maps:get(NN, NV) -> D4 + 1; true -> D4 end,
        PQ2 = if P /= -1 -> gb_sets:add({maps:get(P, NV) + maps:get(L, NV), P}, PQ1); true -> PQ1 end,
        PQ3 = if NN /= -1 -> gb_sets:add({maps:get(L, NV) + maps:get(NN, NV), L}, PQ2); true -> PQ2 end,
        simulate(NV, NX2, PV2, PQ3, D5, Ops + 1); true -> simulate(Vals, Nxt, Prv, PQ1, DC, Ops) end;
      error -> simulate(Vals, Nxt, Prv, PQ1, DC, Ops) end end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_pair_removal(nums :: [integer]) :: integer
  def minimum_pair_removal(nums) do
    n = length(nums)
    if n <= 1 do 0 else
      vals = nums |> Enum.with_index() |> Enum.reduce(%{}, fn {v, i}, acc -> Map.put(acc, i, v) end)
      nxt = if n > 1, do: 0..(n-2) |> Enum.reduce(%{}, fn i, acc -> Map.put(acc, i, i + 1) end), else: %{}
      prv = if n > 1, do: 1..(n-1) |> Enum.reduce(%{}, fn i, acc -> Map.put(acc, i, i - 1) end), else: %{}
      pq = if n > 1, do: 0..(n-2) |> Enum.reduce(:gb_sets.new(), fn i, acc -> :gb_sets.add({Map.get(vals, i) + Map.get(vals, i + 1), i}, acc) end), else: :gb_sets.new()
      dc = if n > 1, do: 0..(n-2) |> Enum.count(fn i -> Map.get(vals, i) > Map.get(vals, i + 1) end), else: 0
      simulate(vals, nxt, prv, pq, dc, 0)
    end
  end
  defp simulate(vals, nxt, prv, pq, dc, ops) do
    if dc == 0 do ops else
      case :gb_sets.is_empty(pq) do
        true -> ops
        false -> {{s, l}, pq} = :gb_sets.take_smallest(pq)
          case Map.get(nxt, l) do
            nil -> simulate(vals, nxt, prv, pq, dc, ops)
            r -> if Map.get(vals, l) + Map.get(vals, r) == s do
                p = Map.get(prv, l, -1)
                nn = Map.get(nxt, r, -1)
                new_dc = dc
                if p != -1 and Map.get(vals, p) > Map.get(vals, l), do: new_dc = new_dc - 1
                if Map.get(vals, l) > Map.get(vals, r), do: new_dc = new_dc - 1
                if nn != -1 and Map.get(vals, r) > Map.get(vals, nn), do: new_dc = new_dc - 1
                sum = Map.get(vals, l) + Map.get(vals, r)
                new_vals = vals |> Map.put(l, sum) |> Map.delete(r)
                new_nxt = nxt |> Map.delete(r)
                new_nxt = if nn != -1, do: Map.put(new_nxt, l, nn), else: Map.delete(new_nxt, l)
                new_prv = prv |> Map.delete(r)
                if nn != -1, do: new_prv = Map.put(new_prv, nn, l)
                if p != -1 and Map.get(new_vals, p) > Map.get(new_vals, l), do: new_dc = new_dc + 1
                if nn != -1 and Map.get(new_vals, l) > Map.get(new_vals, nn), do: new_dc = new_dc + 1
                new_pq = pq
                if p != -1, do: new_pq = :gb_sets.add({Map.get(new_vals, p) + Map.get(new_vals, l), p}, new_pq)
                if nn != -1, do: new_pq = :gb_sets.add({Map.get(new_vals, l) + Map.get(new_vals, nn), l}, new_pq)
                simulate(new_vals, new_nxt, new_prv, new_pq, new_dc, ops + 1)
              else
                simulate(vals, nxt, prv, pq, dc, ops)
              end
          end
      end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log N), where N is the length of the array. Each of the at most N-1 merges involves popping from and pushing into the priority queue, which takes logarithmic time. The total number of elements pushed into the queue is proportional to N.
- **Space Complexity:** O(N), as we maintain several arrays (L, R, val, alive) and a priority queue, each storing at most O(N) elements to manage the state of the simulation.
