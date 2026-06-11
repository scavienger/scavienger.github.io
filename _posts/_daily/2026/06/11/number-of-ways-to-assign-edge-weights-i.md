---
layout: post
title: "Number of Ways to Assign Edge Weights I"
date: 2026-06-11 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Math", "Tree", "Depth-First Search"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long power(long long base, long long\
        \ exp) {\n        long long res = 1;\n        long long mod = 1000000007;\n\
        \        while (exp > 0) {\n            if (exp % 2 == 1) res = (res * base)\
        \ % mod;\n            base = (base * base) % mod;\n            exp /= 2;\n \
        \       }\n        return res;\n    }\n\n    int assignEdgeWeights(vector<vector<int>>&\
        \ edges) {\n        int n = edges.size() + 1;\n        vector<vector<int>> adj(n\
        \ + 1);\n        for (const auto& e : edges) {\n            adj[e[0]].push_back(e[1]);\n\
        \            adj[e[1]].push_back(e[0]);\n        }\n\n        vector<int> dist(n\
        \ + 1, -1);\n        queue<int> q;\n        q.push(1);\n        dist[1] = 0;\n\
        \        int max_depth = 0;\n\n        while (!q.empty()) {\n            int\
        \ u = q.front();\n            q.pop();\n            if (dist[u] > max_depth)\
        \ max_depth = dist[u];\n            for (int v : adj[u]) {\n               \
        \ if (dist[v] == -1) {\n                    dist[v] = dist[u] + 1;\n       \
        \             q.push(v);\n                }\n            }\n        }\n\n  \
        \      return (int)power(2, max_depth - 1);\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int assignEdgeWeights(int[][]\
        \ edges) {\n        int n = edges.length + 1;\n        List<Integer>[] adj =\
        \ new ArrayList[n + 1];\n        for (int i = 1; i <= n; i++) adj[i] = new ArrayList<>();\n\
        \        for (int[] edge : edges) {\n            adj[edge[0]].add(edge[1]);\n\
        \            adj[edge[1]].add(edge[0]);\n        }\n\n        int maxDepth =\
        \ 0;\n        int[] dist = new int[n + 1];\n        Arrays.fill(dist, -1);\n\
        \        Queue<Integer> q = new ArrayDeque<>();\n        q.add(1);\n       \
        \ dist[1] = 0;\n\n        while (!q.isEmpty()) {\n            int u = q.poll();\n\
        \            if (dist[u] > maxDepth) maxDepth = dist[u];\n            for (int\
        \ v : adj[u]) {\n                if (dist[v] == -1) {\n                    dist[v]\
        \ = dist[u] + 1;\n                    q.add(v);\n                }\n       \
        \     }\n        }\n\n        return (int) power(2, maxDepth - 1);\n    }\n\n\
        \    private long power(long base, long exp) {\n        long res = 1;\n    \
        \    long mod = 1000000007;\n        while (exp > 0) {\n            if (exp\
        \ % 2 == 1) res = (res * base) % mod;\n            base = (base * base) % mod;\n\
        \            exp /= 2;\n        }\n        return res;\n    }\n}"
      python: "class Solution(object):\n    def assignEdgeWeights(self, edges):\n  \
        \      \"\"\"\n        :type edges: List[List[int]]\n        :rtype: int\n \
        \       \"\"\"\n        import collections\n        n = len(edges) + 1\n   \
        \     adj = [[] for _ in range(n + 1)]\n        for u, v in edges:\n       \
        \     adj[u].append(v)\n            adj[v].append(u)\n\n        max_depth =\
        \ 0\n        q = collections.deque([(1, 0)])\n        visited = [-1] * (n +\
        \ 1)\n        visited[1] = 0\n\n        while q:\n            u, d = q.popleft()\n\
        \            if d > max_depth: \n                max_depth = d\n           \
        \ for v in adj[u]:\n                if visited[v] == -1:\n                 \
        \   visited[v] = d + 1\n                    q.append((v, d + 1))\n\n       \
        \ return pow(2, max_depth - 1, 1000000007)"
      python3: "from collections import deque\n\nclass Solution:\n    def assignEdgeWeights(self,\
        \ edges: List[List[int]]) -> int:\n        n = len(edges) + 1\n        adj =\
        \ [[] for _ in range(n + 1)]\n        for u, v in edges:\n            adj[u].append(v)\n\
        \            adj[v].append(u)\n\n        max_depth = 0\n        q = deque([(1,\
        \ 0)])\n        visited = [-1] * (n + 1)\n        visited[1] = 0\n\n       \
        \ while q:\n            u, d = q.popleft()\n            if d > max_depth:\n\
        \                max_depth = d\n            for v in adj[u]:\n             \
        \   if visited[v] == -1:\n                    visited[v] = d + 1\n         \
        \           q.append((v, d + 1))\n\n        if max_depth == 0:\n           \
        \ return 0\n\n        return pow(2, max_depth - 1, 10**9 + 7)"
      c: "#include <stdlib.h>\n#include <stdio.h>\n\ntypedef struct Node {\n    int\
        \ to;\n    struct Node* next;\n} Node;\n\nlong long power(long long base, long\
        \ long exp) {\n    long long res = 1;\n    long long mod = 1000000007;\n   \
        \ while (exp > 0) {\n        if (exp % 2 == 1) res = (res * base) % mod;\n \
        \       base = (base * base) % mod;\n        exp /= 2;\n    }\n    return res;\n\
        }\n\nint assignEdgeWeights(int** edges, int edgesSize, int* edgesColSize) {\n\
        \    int n = edgesSize + 1;\n    Node** adj = (Node**)calloc(n + 1, sizeof(Node*));\n\
        \    for (int i = 0; i < edgesSize; i++) {\n        int u = edges[i][0];\n \
        \       int v = edges[i][1];\n        Node* n1 = (Node*)malloc(sizeof(Node));\n\
        \        n1->to = v;\n        n1->next = adj[u];\n        adj[u] = n1;\n   \
        \     Node* n2 = (Node*)malloc(sizeof(Node));\n        n2->to = u;\n       \
        \ n2->next = adj[v];\n        adj[v] = n2;\n    }\n\n    int* dist = (int*)malloc(sizeof(int)\
        \ * (n + 1));\n    for (int i = 0; i <= n; i++) dist[i] = -1;\n    int* q =\
        \ (int*)malloc(sizeof(int) * (n + 1));\n    int head = 0, tail = 0;\n    q[tail++]\
        \ = 1;\n    dist[1] = 0;\n    int max_depth = 0;\n\n    while (head < tail)\
        \ {\n        int u = q[head++];\n        if (dist[u] > max_depth) max_depth\
        \ = dist[u];\n        Node* curr = adj[u];\n        while (curr) {\n       \
        \     int v = curr->to;\n            if (dist[v] == -1) {\n                dist[v]\
        \ = dist[u] + 1;\n                q[tail++] = v;\n            }\n          \
        \  curr = curr->next;\n        }\n    }\n\n    long long result = power(2, max_depth\
        \ - 1);\n\n    for (int i = 1; i <= n; i++) {\n        Node* curr = adj[i];\n\
        \        while (curr) {\n            Node* tmp = curr;\n            curr = curr->next;\n\
        \            free(tmp);\n        }\n    }\n    free(adj);\n    free(dist);\n\
        \    free(q);\n\n    return (int)result;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int AssignEdgeWeights(int[][] edges) {\n        int n = edges.Length\
        \ + 1;\n        List<int>[] adj = new List<int>[n + 1];\n        for (int i\
        \ = 0; i <= n; i++) {\n            adj[i] = new List<int>();\n        }\n\n\
        \        foreach (var edge in edges) {\n            adj[edge[0]].Add(edge[1]);\n\
        \            adj[edge[1]].Add(edge[0]);\n        }\n\n        int maxDepth =\
        \ 0;\n        int[] depth = new int[n + 1];\n        bool[] visited = new bool[n\
        \ + 1];\n        Queue<int> queue = new Queue<int>();\n\n        queue.Enqueue(1);\n\
        \        visited[1] = true;\n        depth[1] = 0;\n\n        while (queue.Count\
        \ > 0) {\n            int u = queue.Dequeue();\n            if (depth[u] > maxDepth)\
        \ {\n                maxDepth = depth[u];\n            }\n\n            foreach\
        \ (int v in adj[u]) {\n                if (!visited[v]) {\n                \
        \    visited[v] = true;\n                    depth[v] = depth[u] + 1;\n    \
        \                queue.Enqueue(v);\n                }\n            }\n     \
        \   }\n\n        return (int)Power(2, maxDepth - 1, 1000000007);\n    }\n\n\
        \    private long Power(long baseVal, int exp, int mod) {\n        if (exp <\
        \ 0) return 0;\n        long res = 1;\n        baseVal %= mod;\n        while\
        \ (exp > 0) {\n            if (exp % 2 == 1) res = (res * baseVal) % mod;\n\
        \            baseVal = (baseVal * baseVal) % mod;\n            exp /= 2;\n \
        \       }\n        return res;\n    }\n}"
      javascript: "/**\n * @param {number[][]} edges\n * @return {number}\n */\nvar\
        \ assignEdgeWeights = function(edges) {\n    const n = edges.length + 1;\n \
        \   const adj = Array.from({ length: n + 1 }, () => []);\n    for (const [u,\
        \ v] of edges) {\n        adj[u].push(v);\n        adj[v].push(u);\n    }\n\n\
        \    let maxDepth = 0;\n    const depth = new Array(n + 1).fill(-1);\n    const\
        \ queue = [1];\n    depth[1] = 0;\n    let head = 0;\n\n    while (head < queue.length)\
        \ {\n        const u = queue[head++];\n        if (depth[u] > maxDepth) {\n\
        \            maxDepth = depth[u];\n        }\n\n        for (const v of adj[u])\
        \ {\n            if (depth[v] === -1) {\n                depth[v] = depth[u]\
        \ + 1;\n                queue.push(v);\n            }\n        }\n    }\n\n\
        \    return Number(power(2n, BigInt(maxDepth - 1), 1000000007n));\n};\n\nfunction\
        \ power(base, exp, mod) {\n    if (exp < 0n) return 0n;\n    let res = 1n;\n\
        \    base %= mod;\n    while (exp > 0n) {\n        if (exp % 2n === 1n) res\
        \ = (res * base) % mod;\n        base = (base * base) % mod;\n        exp =\
        \ exp / 2n;\n    }\n    return res;\n}"
      typescript: "function assignEdgeWeights(edges: number[][]): number {\n    const\
        \ n = edges.length + 1;\n    const adj: number[][] = Array.from({ length: n\
        \ + 1 }, () => []);\n    for (const [u, v] of edges) {\n        adj[u].push(v);\n\
        \        adj[v].push(u);\n    }\n\n    let maxDepth = 0;\n    const depth =\
        \ new Int32Array(n + 1).fill(-1);\n    const queue: number[] = [1];\n    depth[1]\
        \ = 0;\n    let head = 0;\n\n    while (head < queue.length) {\n        const\
        \ u = queue[head++];\n        if (depth[u] > maxDepth) {\n            maxDepth\
        \ = depth[u];\n        }\n\n        for (const v of adj[u]) {\n            if\
        \ (depth[v] === -1) {\n                depth[v] = depth[u] + 1;\n          \
        \      queue.push(v);\n            }\n        }\n    }\n\n    function power(base:\
        \ bigint, exp: bigint, mod: bigint): bigint {\n        if (exp < 0n) return\
        \ 0n;\n        let res = 1n;\n        base %= mod;\n        while (exp > 0n)\
        \ {\n            if (exp % 2n === 1n) res = (res * base) % mod;\n          \
        \  base = (base * base) % mod;\n            exp = exp / 2n;\n        }\n   \
        \     return res;\n    }\n\n    return Number(power(2n, BigInt(maxDepth - 1),\
        \ 1000000007n));\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $edges\n     * @return\
        \ Integer\n     */\n    function assignEdgeWeights($edges) {\n        $n = count($edges)\
        \ + 1;\n        $adj = array_fill(1, $n, []);\n        foreach ($edges as $edge)\
        \ {\n            $u = $edge[0];\n            $v = $edge[1];\n            $adj[$u][]\
        \ = $v;\n            $adj[$v][] = $u;\n        }\n\n        $maxDepth = 0;\n\
        \        $depth = array_fill(1, $n, -1);\n        $queue = new SplQueue();\n\
        \n        $queue->enqueue(1);\n        $depth[1] = 0;\n\n        while (!$queue->isEmpty())\
        \ {\n            $u = $queue->dequeue();\n            if ($depth[$u] > $maxDepth)\
        \ {\n                $maxDepth = $depth[$u];\n            }\n\n            foreach\
        \ ($adj[$u] as $v) {\n                if ($depth[$v] === -1) {\n           \
        \         $depth[$v] = $depth[$u] + 1;\n                    $queue->enqueue($v);\n\
        \                }\n            }\n        }\n\n        return $this->power(2,\
        \ $maxDepth - 1, 1000000007);\n    }\n\n    private function power($base, $exp,\
        \ $mod) {\n        if ($exp < 0) return 0;\n        $res = 1;\n        $base\
        \ %= $mod;\n        while ($exp > 0) {\n            if ($exp % 2 == 1) {\n \
        \               $res = ($res * $base) % $mod;\n            }\n            $base\
        \ = ($base * $base) % $mod;\n            $exp = (int)($exp / 2);\n        }\n\
        \        return $res;\n    }\n}"
      swift: "class Solution {\n    func assignEdgeWeights(_ edges: [[Int]]) -> Int\
        \ {\n        let n = edges.count + 1\n        var adj = Array(repeating: [Int](),\
        \ count: n + 1)\n        for edge in edges {\n            adj[edge[0]].append(edge[1])\n\
        \            adj[edge[1]].append(edge[0])\n        }\n\n        var maxDepth\
        \ = 0\n        var depth = Array(repeating: -1, count: n + 1)\n        var queue\
        \ = [1]\n        var head = 0\n\n        depth[1] = 0\n\n        while head\
        \ < queue.count {\n            let u = queue[head]\n            head += 1\n\n\
        \            if depth[u] > maxDepth {\n                maxDepth = depth[u]\n\
        \            }\n\n            for v in adj[u] {\n                if depth[v]\
        \ == -1 {\n                    depth[v] = depth[u] + 1\n                   \
        \ queue.append(v)\n                }\n            }\n        }\n\n        return\
        \ power(2, maxDepth - 1, 1000000007)\n    }\n\n    private func power(_ base:\
        \ Int, _ exp: Int, _ mod: Int) -> Int {\n        if exp < 0 { return 0 }\n \
        \       var res: Int64 = 1\n        var b: Int64 = Int64(base) % Int64(mod)\n\
        \        var e = exp\n        let m: Int64 = Int64(mod)\n\n        while e >\
        \ 0 {\n            if e % 2 == 1 {\n                res = (res * b) % m\n  \
        \          }\n            b = (b * b) % m\n            e /= 2\n        }\n\n\
        \        return Int(res)\n    }\n}"
      kotlin: "class Solution {\n    fun assignEdgeWeights(edges: Array<IntArray>):\
        \ Int {\n        val n = edges.size + 1\n        val adj = Array(n + 1) { mutableListOf<Int>()\
        \ }\n        for (edge in edges) {\n            adj[edge[0]].add(edge[1])\n\
        \            adj[edge[1]].add(edge[0])\n        }\n\n        var maxDepth =\
        \ 0\n        val dist = IntArray(n + 1) { -1 }\n        val queue = java.util.ArrayDeque<Int>()\n\
        \n        queue.add(1)\n        dist[1] = 0\n\n        while (queue.isNotEmpty())\
        \ {\n            val u = queue.poll()\n            if (dist[u] > maxDepth) {\n\
        \                maxDepth = dist[u]\n            }\n            for (v in adj[u])\
        \ {\n                if (dist[v] == -1) {\n                    dist[v] = dist[u]\
        \ + 1\n                    queue.add(v)\n                }\n            }\n\
        \        }\n\n        var res = 1L\n        var b = 2L\n        var e = (maxDepth\
        \ - 1).toLong()\n        val mod = 1000000007L\n\n        if (e < 0) return\
        \ 0\n\n        while (e > 0) {\n            if (e % 2 == 1L) {\n           \
        \     res = (res * b) % mod\n            }\n            b = (b * b) % mod\n\
        \            e /= 2\n        }\n\n        return res.toInt()\n    }\n}"
      dart: "import 'dart:collection';\n\nclass Solution {\n  int assignEdgeWeights(List<List<int>>\
        \ edges) {\n    int n = edges.length + 1;\n    List<List<int>> adj = List.generate(n\
        \ + 1, (_) => []);\n    for (var edge in edges) {\n      adj[edge[0]].add(edge[1]);\n\
        \      adj[edge[1]].add(edge[0]);\n    }\n\n    int maxDepth = 0;\n    List<int>\
        \ dist = List.filled(n + 1, -1);\n    Queue<int> queue = Queue<int>();\n\n \
        \   queue.add(1);\n    dist[1] = 0;\n\n    while (queue.isNotEmpty) {\n    \
        \  int u = queue.removeFirst();\n      if (dist[u] > maxDepth) {\n        maxDepth\
        \ = dist[u];\n      }\n      for (int v in adj[u]) {\n        if (dist[v] ==\
        \ -1) {\n          dist[v] = dist[u] + 1;\n          queue.add(v);\n       \
        \ }\n      }\n    }\n\n    return power(2, maxDepth - 1, 1000000007);\n  }\n\
        \n  int power(int base, int exp, int mod) {\n    if (exp < 0) return 1;\n  \
        \  int res = 1;\n    base %= mod;\n    while (exp > 0) {\n      if (exp % 2\
        \ == 1) {\n        res = (res * base) % mod;\n      }\n      base = (base *\
        \ base) % mod;\n      exp ~/= 2;\n    }\n    return res;\n  }\n}"
      go: "func assignEdgeWeights(edges [][]int) int {\n    n := len(edges) + 1\n  \
        \  adj := make([][]int, n+1)\n    for _, edge := range edges {\n        u, v\
        \ := edge[0], edge[1]\n        adj[u] = append(adj[u], v)\n        adj[v] =\
        \ append(adj[v], u)\n    }\n\n    maxDepth := 0\n    dist := make([]int, n+1)\n\
        \    for i := range dist {\n        dist[i] = -1\n    }\n\n    queue := []int{1}\n\
        \    dist[1] = 0\n\n    for len(queue) > 0 {\n        u := queue[0]\n      \
        \  queue = queue[1:]\n\n        if dist[u] > maxDepth {\n            maxDepth\
        \ = dist[u]\n        }\n\n        for _, v := range adj[u] {\n            if\
        \ dist[v] == -1 {\n                dist[v] = dist[u] + 1\n                queue\
        \ = append(queue, v)\n            }\n        }\n    }\n\n    return int(power(2,\
        \ int64(maxDepth-1), 1000000007))\n}\n\nfunc power(base, exp, mod int64) int64\
        \ {\n    if exp < 0 {\n        return 1\n    }\n    res := int64(1)\n    base\
        \ %= mod\n    for exp > 0 {\n        if exp%2 == 1 {\n            res = (res\
        \ * base) % mod\n        }\n        base = (base * base) % mod\n        exp\
        \ /= 2\n    }\n    return res\n}"
      ruby: "# @param {Integer[][]} edges\n# @return {Integer}\ndef assign_edge_weights(edges)\n\
        \  n = edges.length + 1\n  adj = Array.new(n + 1) { [] }\n  edges.each do |u,\
        \ v|\n    adj[u] << v\n    adj[v] << u\n  end\n\n  max_depth = 0\n  dist = Array.new(n\
        \ + 1, -1)\n  queue = [1]\n  dist[1] = 0\n  head = 0\n\n  while head < queue.length\n\
        \    u = queue[head]\n    head += 1\n    max_depth = dist[u] if dist[u] > max_depth\n\
        \n    adj[u].each do |v|\n      if dist[v] == -1\n        dist[v] = dist[u]\
        \ + 1\n        queue << v\n      end\n    end\n  end\n\n  return 2.pow(max_depth\
        \ - 1, 1000000007)\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def assignEdgeWeights(edges:\
        \ Array[Array[Int]]): Int = {\n        val n = edges.length + 1\n        val\
        \ adj = Array.tabulate(n + 1)(_ => mutable.ListBuffer[Int]())\n        for (edge\
        \ <- edges) {\n            adj(edge(0)).append(edge(1))\n            adj(edge(1)).append(edge(0))\n\
        \        }\n\n        var maxDepth = 0\n        val dist = Array.fill(n + 1)(-1)\n\
        \        val queue = mutable.Queue[Int]()\n\n        queue.enqueue(1)\n    \
        \    dist(1) = 0\n\n        while (queue.nonEmpty) {\n            val u = queue.dequeue()\n\
        \            if (dist(u) > maxDepth) maxDepth = dist(u)\n\n            for (v\
        \ <- adj(u)) {\n                if (dist(v) == -1) {\n                    dist(v)\
        \ = dist(u) + 1\n                    queue.enqueue(v)\n                }\n \
        \           }\n        }\n\n        power(2, maxDepth.toLong - 1, 1000000007L).toInt\n\
        \    }\n\n    def power(base: Long, exp: Long, mod: Long): Long = {\n      \
        \  if (exp < 0) return 1L\n        var res = 1L\n        var b = base % mod\n\
        \        var e = exp\n        while (e > 0) {\n            if (e % 2 == 1) res\
        \ = (res * b) % mod\n            b = (b * b) % mod\n            e /= 2\n   \
        \     }\n        res\n    }\n}"
      rust: "use std::collections::VecDeque;\n\nimpl Solution {\n    pub fn assign_edge_weights(edges:\
        \ Vec<Vec<i32>>) -> i32 {\n        let n = edges.len() + 1;\n        let mut\
        \ adj = vec![vec![]; n + 1];\n        for edge in edges {\n            let u\
        \ = edge[0] as usize;\n            let v = edge[1] as usize;\n            adj[u].push(v);\n\
        \            adj[v].push(u);\n        }\n\n        let mut max_depth = 0;\n\
        \        let mut queue = VecDeque::new();\n        let mut visited = vec![false;\
        \ n + 1];\n\n        queue.push_back((1, 0));\n        visited[1] = true;\n\n\
        \        while let Some((u, d)) = queue.pop_front() {\n            if d > max_depth\
        \ {\n                max_depth = d;\n            }\n            for &v in &adj[u]\
        \ {\n                if !visited[v] {\n                    visited[v] = true;\n\
        \                    queue.push_back((v, d + 1));\n                }\n     \
        \       }\n        }\n\n        if max_depth == 0 {\n            return 0;\n\
        \        }\n\n        Self::pow_mod(2, (max_depth - 1) as u64, 1_000_000_007)\
        \ as i32\n    }\n\n    fn pow_mod(mut base: u64, mut exp: u64, m: u64) -> u64\
        \ {\n        let mut res = 1;\n        base %= m;\n        while exp > 0 {\n\
        \            if exp % 2 == 1 {\n                res = (res * base) % m;\n  \
        \          }\n            base = (base * base) % m;\n            exp /= 2;\n\
        \        }\n        res\n    }\n}"
      racket: "(define/contract (assign-edge-weights edges)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer?)\n  (let* ([n (+ (length edges) 1)]\n         [adj (make-vector\
        \ (+ n 1) '())])\n    (for ([edge edges])\n      (let ([u (car edge)]\n    \
        \        [v (cadr edge)])\n        (vector-set! adj u (cons v (vector-ref adj\
        \ u)))\n        (vector-set! adj v (cons u (vector-ref adj v)))))\n    (let\
        \ ([visited (make-vector (+ n 1) #f)]\n          [max-d 0])\n      (vector-set!\
        \ visited 1 #t)\n      (let loop ([queue (list (cons 1 0))]\n              \
        \   [tail '()])\n        (cond\n          [(and (null? queue) (null? tail))\n\
        \           (if (>= max-d 1)\n               (let loop-pow ([b 2] [e (- max-d\
        \ 1)] [res 1])\n                 (cond\n                   [(= e 0) res]\n \
        \                  [(odd? e) (loop-pow (remainder (* b b) 1000000007) (quotient\
        \ e 2) (remainder (* res b) 1000000007))]\n                   [else (loop-pow\
        \ (remainder (* b b) 1000000007) (quotient e 2) res)]))\n               0)]\n\
        \          [(null? queue) (loop (reverse tail) '())]\n          [else\n    \
        \       (let* ([curr (car queue)]\n                  [u (car curr)]\n      \
        \            [d (cdr curr)])\n             (when (> d max-d) (set! max-d d))\n\
        \             (let ([new-tail tail])\n               (for-each (lambda (v)\n\
        \                           (unless (vector-ref visited v)\n               \
        \              (vector-set! visited v #t)\n                             (set!\
        \ new-tail (cons (cons v (+ d 1)) new-tail))))\n                         (vector-ref\
        \ adj u))\n               (loop (cdr queue) new-tail)))])))))"
      erlang: "-spec assign_edge_weights(Edges :: [[integer()]]) -> integer().\nassign_edge_weights(Edges)\
        \ ->\n  Adj = build_adj(Edges, #{}),\n  MaxDepth = find_max_depth(Adj),\n  if\
        \ MaxDepth < 1 -> 0;\n     true -> pow_mod(2, MaxDepth - 1, 1000000007)\n  end.\n\
        \nbuild_adj([], Map) -> Map;\nbuild_adj([[U, V] | T], Map) ->\n  M1 = maps:update_with(U,\
        \ fun(L) -> [V | L] end, [V], Map),\n  M2 = maps:update_with(V, fun(L) -> [U\
        \ | L] end, [U], M1),\n  build_adj(T, M2).\n\nfind_max_depth(Adj) ->\n  Q =\
        \ queue:in({1, 0}, queue:new()),\n  V = #{1 => true},\n  bfs(Q, V, Adj, 0).\n\
        \nbfs(Q, V, Adj, MaxD) ->\n  case queue:out(Q) of\n    {empty, _} -> MaxD;\n\
        \    {{value, {U, D}}, Q2} ->\n      Neighbors = maps:get(U, Adj, []),\n   \
        \   {NewQ, NewV} = lists:foldl(fun(Node, {AccQ, AccV}) ->\n        case maps:is_key(Node,\
        \ AccV) of\n          true -> {AccQ, AccV};\n          false -> {queue:in({Node,\
        \ D + 1}, AccQ), AccV#{Node => true}}\n        end\n      end, {Q2, V}, Neighbors),\n\
        \      bfs(NewQ, NewV, Adj, max(MaxD, D))\n  end.\n\npow_mod(B, E, M) ->\n \
        \ pow_mod_iter(B, E, M, 1).\n\npow_mod_iter(_B, 0, _M, Acc) -> Acc;\npow_mod_iter(B,\
        \ E, M, Acc) ->\n  NewAcc = if E rem 2 =:= 1 -> (Acc * B) rem M; true -> Acc\
        \ end,\n  pow_mod_iter((B * B) rem M, E div 2, M, NewAcc)."
      elixir: "defmodule Solution do\n  @spec assign_edge_weights(edges :: [[integer]])\
        \ :: integer\n  def assign_edge_weights(edges) do\n    adj = Enum.reduce(edges,\
        \ %{}, fn [u, v], acc ->\n      acc\n      |> Map.update(u, [v], &[v | &1])\n\
        \      |> Map.update(v, [u], &[u | &1])\n    end)\n\n    max_depth = find_max_depth(adj)\n\
        \    if max_depth < 1 do\n      0\n    else\n      pow_mod(2, max_depth - 1,\
        \ 1_000_000_007)\n    end\n  end\n\n  defp find_max_depth(adj) do\n    q = :queue.in({1,\
        \ 0}, :queue.new())\n    v = MapSet.new([1])\n    bfs(q, v, adj, 0)\n  end\n\
        \n  defp bfs(q, v, adj, max_d) do\n    case :queue.out(q) do\n      {:empty,\
        \ _} -> max_d\n      {{:value, {u, d}}, q2} ->\n        neighbors = Map.get(adj,\
        \ u, [])\n        {new_q, new_v} = Enum.reduce(neighbors, {q2, v}, fn node,\
        \ {acc_q, acc_v} ->\n          if MapSet.member?(acc_v, node) do\n         \
        \   {acc_q, acc_v}\n          else\n            {:queue.in({node, d + 1}, acc_q),\
        \ MapSet.put(acc_v, node)}\n          end\n        end)\n        bfs(new_q,\
        \ new_v, adj, max(max_d, d))\n    end\n  end\n\n  defp pow_mod(b, e, m) do\n\
        \    pow_mod_iter(b, e, m, 1)\n  end\n\n  defp pow_mod_iter(_b, 0, _m, acc),\
        \ do: acc\n  defp pow_mod_iter(b, e, m, acc) do\n    new_acc = if rem(e, 2)\
        \ == 1, do: rem(acc * b, m), else: acc\n    pow_mod_iter(rem(b * b, m), div(e,\
        \ 2), m, new_acc)\n  end\nend"
    approach: 'The problem asks for the number of ways to assign weights 1 or 2 to the
      edges on a path from the root to a node at maximum depth such that the total path
      cost is odd. Let $L$ be the length of this path (number of edges), which is equal
      to the maximum depth of the tree from root 1. Since $2 \equiv 0 \pmod 2$ and $1
      \equiv 1 \pmod 2$, the parity of the total cost is determined solely by the number
      of edges assigned a weight of 1. If an odd number of edges are assigned weight
      1, the total cost will be odd, regardless of how many edges are assigned weight
      2.


      The algorithm first identifies the maximum depth $L$ of the tree using a Breadth-First
      Search (BFS) or Depth-First Search (DFS) starting from the root (node 1). For
      a path of length $L$, the number of ways to choose an odd number of edges to receive
      the weight 1 (and the remaining edges to receive the weight 2) is given by the
      combinatorial identity $\sum_{k \in \{1, 3, 5, \dots\}} \binom{L}{k} = 2^{L-1}$.
      We calculate $2^{L-1} \pmod{10^9 + 7}$ using modular exponentiation to efficiently
      compute the result for large values of $L$.'
    time_complexity: O(n) with one-paragraph explanation. The algorithm constructs an
      adjacency list from the input edges in $O(n)$ time and performs a BFS traversal
      to find the maximum depth, which visits each node and edge once, taking $O(n)$
      time. The modular exponentiation for $2^{L-1}$ takes $O(\log n)$ time.
    space_complexity: O(n) with one-paragraph explanation. The adjacency list stores
      $n$ nodes and $n-1$ undirected edges, requiring $O(n)$ space. Additionally, the
      BFS uses a queue and a distance array of size $n$, contributing $O(n)$ space complexity.
    elapsed_time: 824.8763346672058
    model: gemini-3-flash-preview
    generated_at: '2026-06-11 03:05:34 '
---

## Problem #3558: Number of Ways to Assign Edge Weights I

**Difficulty:** Medium

**Topics:** Math, Tree, Depth-First Search

## Problem Description

<p>There is an undirected tree with <code>n</code> nodes labeled from 1 to <code>n</code>, rooted at node 1. The tree is represented by a 2D integer array <code>edges</code> of length <code>n - 1</code>, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> indicates that there is an edge between nodes <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code>.</p>

<p>Initially, all edges have a weight of 0. You must assign each edge a weight of either <strong>1</strong> or <strong>2</strong>.</p>

<p>The <strong>cost</strong> of a path between any two nodes <code>u</code> and <code>v</code> is the total weight of all edges in the path connecting them.</p>

<p>Select any one node <code>x</code> at the <strong>maximum</strong> depth. Return the number of ways to assign edge weights in the path from node 1 to <code>x</code> such that its total cost is <strong>odd</strong>.</p>

<p>Since the answer may be large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p><strong>Note:</strong> Ignore all edges <strong>not</strong> in the path from node 1 to <code>x</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2025/03/23/screenshot-2025-03-24-at-060006.png" style="width: 200px; height: 72px;" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">edges = [[1,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The path from Node 1 to Node 2 consists of one edge (<code>1 &rarr; 2</code>).</li>
	<li>Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2025/03/23/screenshot-2025-03-24-at-055820.png" style="width: 220px; height: 207px;" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">edges = [[1,2],[1,3],[3,4],[3,5]]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The maximum depth is 2, with nodes 4 and 5 at the same depth. Either node can be selected for processing.</li>
	<li>For example, the path from Node 1 to Node 4 consists of two edges (<code>1 &rarr; 3</code> and <code>3 &rarr; 4</code>).</li>
	<li>Assigning weights (1,2) or (2,1) results in an odd cost. Thus, the number of valid assignments is 2.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i] == [u<sub>i</sub>, v<sub>i</sub>]</code></li>
	<li><code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code></li>
	<li><code>edges</code> represents a valid tree.</li>
</ul>


## Hints

1. Depth‑First Search (DFS) to compute the depth of each node from the root.

2. Find the maximum depth, `max_depth`.

3. The number of `2`s doesn’t affect parity; we only need an odd number of `1`s along the path.

4. The number of ways to choose an odd count of 1s among `max_depth` edges is `2^(max_depth-1)`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the number of ways to assign weights 1 or 2 to the edges on a path from the root to a node at maximum depth such that the total path cost is odd. Let $L$ be the length of this path (number of edges), which is equal to the maximum depth of the tree from root 1. Since $2 \equiv 0 \pmod 2$ and $1 \equiv 1 \pmod 2$, the parity of the total cost is determined solely by the number of edges assigned a weight of 1. If an odd number of edges are assigned weight 1, the total cost will be odd, regardless of how many edges are assigned weight 2.

The algorithm first identifies the maximum depth $L$ of the tree using a Breadth-First Search (BFS) or Depth-First Search (DFS) starting from the root (node 1). For a path of length $L$, the number of ways to choose an odd number of edges to receive the weight 1 (and the remaining edges to receive the weight 2) is given by the combinatorial identity $\sum_{k \in \{1, 3, 5, \dots\}} \binom{L}{k} = 2^{L-1}$. We calculate $2^{L-1} \pmod{10^9 + 7}$ using modular exponentiation to efficiently compute the result for large values of $L$.

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
    long long power(long long base, long long exp) {
        long long res = 1;
        long long mod = 1000000007;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp /= 2;
        }
        return res;
    }

    int assignEdgeWeights(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        vector<vector<int>> adj(n + 1);
        for (const auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }

        vector<int> dist(n + 1, -1);
        queue<int> q;
        q.push(1);
        dist[1] = 0;
        int max_depth = 0;

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            if (dist[u] > max_depth) max_depth = dist[u];
            for (int v : adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.push(v);
                }
            }
        }

        return (int)power(2, max_depth - 1);
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
    public int assignEdgeWeights(int[][] edges) {
        int n = edges.length + 1;
        List<Integer>[] adj = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) adj[i] = new ArrayList<>();
        for (int[] edge : edges) {
            adj[edge[0]].add(edge[1]);
            adj[edge[1]].add(edge[0]);
        }

        int maxDepth = 0;
        int[] dist = new int[n + 1];
        Arrays.fill(dist, -1);
        Queue<Integer> q = new ArrayDeque<>();
        q.add(1);
        dist[1] = 0;

        while (!q.isEmpty()) {
            int u = q.poll();
            if (dist[u] > maxDepth) maxDepth = dist[u];
            for (int v : adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.add(v);
                }
            }
        }

        return (int) power(2, maxDepth - 1);
    }

    private long power(long base, long exp) {
        long res = 1;
        long mod = 1000000007;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp /= 2;
        }
        return res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        import collections
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        max_depth = 0
        q = collections.deque([(1, 0)])
        visited = [-1] * (n + 1)
        visited[1] = 0

        while q:
            u, d = q.popleft()
            if d > max_depth: 
                max_depth = d
            for v in adj[u]:
                if visited[v] == -1:
                    visited[v] = d + 1
                    q.append((v, d + 1))

        return pow(2, max_depth - 1, 1000000007)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        max_depth = 0
        q = deque([(1, 0)])
        visited = [-1] * (n + 1)
        visited[1] = 0

        while q:
            u, d = q.popleft()
            if d > max_depth:
                max_depth = d
            for v in adj[u]:
                if visited[v] == -1:
                    visited[v] = d + 1
                    q.append((v, d + 1))

        if max_depth == 0:
            return 0

        return pow(2, max_depth - 1, 10**9 + 7)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdio.h>

typedef struct Node {
    int to;
    struct Node* next;
} Node;

long long power(long long base, long long exp) {
    long long res = 1;
    long long mod = 1000000007;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return res;
}

int assignEdgeWeights(int** edges, int edgesSize, int* edgesColSize) {
    int n = edgesSize + 1;
    Node** adj = (Node**)calloc(n + 1, sizeof(Node*));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0];
        int v = edges[i][1];
        Node* n1 = (Node*)malloc(sizeof(Node));
        n1->to = v;
        n1->next = adj[u];
        adj[u] = n1;
        Node* n2 = (Node*)malloc(sizeof(Node));
        n2->to = u;
        n2->next = adj[v];
        adj[v] = n2;
    }

    int* dist = (int*)malloc(sizeof(int) * (n + 1));
    for (int i = 0; i <= n; i++) dist[i] = -1;
    int* q = (int*)malloc(sizeof(int) * (n + 1));
    int head = 0, tail = 0;
    q[tail++] = 1;
    dist[1] = 0;
    int max_depth = 0;

    while (head < tail) {
        int u = q[head++];
        if (dist[u] > max_depth) max_depth = dist[u];
        Node* curr = adj[u];
        while (curr) {
            int v = curr->to;
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q[tail++] = v;
            }
            curr = curr->next;
        }
    }

    long long result = power(2, max_depth - 1);

    for (int i = 1; i <= n; i++) {
        Node* curr = adj[i];
        while (curr) {
            Node* tmp = curr;
            curr = curr->next;
            free(tmp);
        }
    }
    free(adj);
    free(dist);
    free(q);

    return (int)result;
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
    public int AssignEdgeWeights(int[][] edges) {
        int n = edges.Length + 1;
        List<int>[] adj = new List<int>[n + 1];
        for (int i = 0; i <= n; i++) {
            adj[i] = new List<int>();
        }

        foreach (var edge in edges) {
            adj[edge[0]].Add(edge[1]);
            adj[edge[1]].Add(edge[0]);
        }

        int maxDepth = 0;
        int[] depth = new int[n + 1];
        bool[] visited = new bool[n + 1];
        Queue<int> queue = new Queue<int>();

        queue.Enqueue(1);
        visited[1] = true;
        depth[1] = 0;

        while (queue.Count > 0) {
            int u = queue.Dequeue();
            if (depth[u] > maxDepth) {
                maxDepth = depth[u];
            }

            foreach (int v in adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    depth[v] = depth[u] + 1;
                    queue.Enqueue(v);
                }
            }
        }

        return (int)Power(2, maxDepth - 1, 1000000007);
    }

    private long Power(long baseVal, int exp, int mod) {
        if (exp < 0) return 0;
        long res = 1;
        baseVal %= mod;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * baseVal) % mod;
            baseVal = (baseVal * baseVal) % mod;
            exp /= 2;
        }
        return res;
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
 * @return {number}
 */
var assignEdgeWeights = function(edges) {
    const n = edges.length + 1;
    const adj = Array.from({ length: n + 1 }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    let maxDepth = 0;
    const depth = new Array(n + 1).fill(-1);
    const queue = [1];
    depth[1] = 0;
    let head = 0;

    while (head < queue.length) {
        const u = queue[head++];
        if (depth[u] > maxDepth) {
            maxDepth = depth[u];
        }

        for (const v of adj[u]) {
            if (depth[v] === -1) {
                depth[v] = depth[u] + 1;
                queue.push(v);
            }
        }
    }

    return Number(power(2n, BigInt(maxDepth - 1), 1000000007n));
};

function power(base, exp, mod) {
    if (exp < 0n) return 0n;
    let res = 1n;
    base %= mod;
    while (exp > 0n) {
        if (exp % 2n === 1n) res = (res * base) % mod;
        base = (base * base) % mod;
        exp = exp / 2n;
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function assignEdgeWeights(edges: number[][]): number {
    const n = edges.length + 1;
    const adj: number[][] = Array.from({ length: n + 1 }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    let maxDepth = 0;
    const depth = new Int32Array(n + 1).fill(-1);
    const queue: number[] = [1];
    depth[1] = 0;
    let head = 0;

    while (head < queue.length) {
        const u = queue[head++];
        if (depth[u] > maxDepth) {
            maxDepth = depth[u];
        }

        for (const v of adj[u]) {
            if (depth[v] === -1) {
                depth[v] = depth[u] + 1;
                queue.push(v);
            }
        }
    }

    function power(base: bigint, exp: bigint, mod: bigint): bigint {
        if (exp < 0n) return 0n;
        let res = 1n;
        base %= mod;
        while (exp > 0n) {
            if (exp % 2n === 1n) res = (res * base) % mod;
            base = (base * base) % mod;
            exp = exp / 2n;
        }
        return res;
    }

    return Number(power(2n, BigInt(maxDepth - 1), 1000000007n));
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
     * @return Integer
     */
    function assignEdgeWeights($edges) {
        $n = count($edges) + 1;
        $adj = array_fill(1, $n, []);
        foreach ($edges as $edge) {
            $u = $edge[0];
            $v = $edge[1];
            $adj[$u][] = $v;
            $adj[$v][] = $u;
        }

        $maxDepth = 0;
        $depth = array_fill(1, $n, -1);
        $queue = new SplQueue();

        $queue->enqueue(1);
        $depth[1] = 0;

        while (!$queue->isEmpty()) {
            $u = $queue->dequeue();
            if ($depth[$u] > $maxDepth) {
                $maxDepth = $depth[$u];
            }

            foreach ($adj[$u] as $v) {
                if ($depth[$v] === -1) {
                    $depth[$v] = $depth[$u] + 1;
                    $queue->enqueue($v);
                }
            }
        }

        return $this->power(2, $maxDepth - 1, 1000000007);
    }

    private function power($base, $exp, $mod) {
        if ($exp < 0) return 0;
        $res = 1;
        $base %= $mod;
        while ($exp > 0) {
            if ($exp % 2 == 1) {
                $res = ($res * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp = (int)($exp / 2);
        }
        return $res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func assignEdgeWeights(_ edges: [[Int]]) -> Int {
        let n = edges.count + 1
        var adj = Array(repeating: [Int](), count: n + 1)
        for edge in edges {
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        }

        var maxDepth = 0
        var depth = Array(repeating: -1, count: n + 1)
        var queue = [1]
        var head = 0

        depth[1] = 0

        while head < queue.count {
            let u = queue[head]
            head += 1

            if depth[u] > maxDepth {
                maxDepth = depth[u]
            }

            for v in adj[u] {
                if depth[v] == -1 {
                    depth[v] = depth[u] + 1
                    queue.append(v)
                }
            }
        }

        return power(2, maxDepth - 1, 1000000007)
    }

    private func power(_ base: Int, _ exp: Int, _ mod: Int) -> Int {
        if exp < 0 { return 0 }
        var res: Int64 = 1
        var b: Int64 = Int64(base) % Int64(mod)
        var e = exp
        let m: Int64 = Int64(mod)

        while e > 0 {
            if e % 2 == 1 {
                res = (res * b) % m
            }
            b = (b * b) % m
            e /= 2
        }

        return Int(res)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun assignEdgeWeights(edges: Array<IntArray>): Int {
        val n = edges.size + 1
        val adj = Array(n + 1) { mutableListOf<Int>() }
        for (edge in edges) {
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
        }

        var maxDepth = 0
        val dist = IntArray(n + 1) { -1 }
        val queue = java.util.ArrayDeque<Int>()

        queue.add(1)
        dist[1] = 0

        while (queue.isNotEmpty()) {
            val u = queue.poll()
            if (dist[u] > maxDepth) {
                maxDepth = dist[u]
            }
            for (v in adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1
                    queue.add(v)
                }
            }
        }

        var res = 1L
        var b = 2L
        var e = (maxDepth - 1).toLong()
        val mod = 1000000007L

        if (e < 0) return 0

        while (e > 0) {
            if (e % 2 == 1L) {
                res = (res * b) % mod
            }
            b = (b * b) % mod
            e /= 2
        }

        return res.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:collection';

class Solution {
  int assignEdgeWeights(List<List<int>> edges) {
    int n = edges.length + 1;
    List<List<int>> adj = List.generate(n + 1, (_) => []);
    for (var edge in edges) {
      adj[edge[0]].add(edge[1]);
      adj[edge[1]].add(edge[0]);
    }

    int maxDepth = 0;
    List<int> dist = List.filled(n + 1, -1);
    Queue<int> queue = Queue<int>();

    queue.add(1);
    dist[1] = 0;

    while (queue.isNotEmpty) {
      int u = queue.removeFirst();
      if (dist[u] > maxDepth) {
        maxDepth = dist[u];
      }
      for (int v in adj[u]) {
        if (dist[v] == -1) {
          dist[v] = dist[u] + 1;
          queue.add(v);
        }
      }
    }

    return power(2, maxDepth - 1, 1000000007);
  }

  int power(int base, int exp, int mod) {
    if (exp < 0) return 1;
    int res = 1;
    base %= mod;
    while (exp > 0) {
      if (exp % 2 == 1) {
        res = (res * base) % mod;
      }
      base = (base * base) % mod;
      exp ~/= 2;
    }
    return res;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func assignEdgeWeights(edges [][]int) int {
    n := len(edges) + 1
    adj := make([][]int, n+1)
    for _, edge := range edges {
        u, v := edge[0], edge[1]
        adj[u] = append(adj[u], v)
        adj[v] = append(adj[v], u)
    }

    maxDepth := 0
    dist := make([]int, n+1)
    for i := range dist {
        dist[i] = -1
    }

    queue := []int{1}
    dist[1] = 0

    for len(queue) > 0 {
        u := queue[0]
        queue = queue[1:]

        if dist[u] > maxDepth {
            maxDepth = dist[u]
        }

        for _, v := range adj[u] {
            if dist[v] == -1 {
                dist[v] = dist[u] + 1
                queue = append(queue, v)
            }
        }
    }

    return int(power(2, int64(maxDepth-1), 1000000007))
}

func power(base, exp, mod int64) int64 {
    if exp < 0 {
        return 1
    }
    res := int64(1)
    base %= mod
    for exp > 0 {
        if exp%2 == 1 {
            res = (res * base) % mod
        }
        base = (base * base) % mod
        exp /= 2
    }
    return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[][]} edges
# @return {Integer}
def assign_edge_weights(edges)
  n = edges.length + 1
  adj = Array.new(n + 1) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  max_depth = 0
  dist = Array.new(n + 1, -1)
  queue = [1]
  dist[1] = 0
  head = 0

  while head < queue.length
    u = queue[head]
    head += 1
    max_depth = dist[u] if dist[u] > max_depth

    adj[u].each do |v|
      if dist[v] == -1
        dist[v] = dist[u] + 1
        queue << v
      end
    end
  end

  return 2.pow(max_depth - 1, 1000000007)
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def assignEdgeWeights(edges: Array[Array[Int]]): Int = {
        val n = edges.length + 1
        val adj = Array.tabulate(n + 1)(_ => mutable.ListBuffer[Int]())
        for (edge <- edges) {
            adj(edge(0)).append(edge(1))
            adj(edge(1)).append(edge(0))
        }

        var maxDepth = 0
        val dist = Array.fill(n + 1)(-1)
        val queue = mutable.Queue[Int]()

        queue.enqueue(1)
        dist(1) = 0

        while (queue.nonEmpty) {
            val u = queue.dequeue()
            if (dist(u) > maxDepth) maxDepth = dist(u)

            for (v <- adj(u)) {
                if (dist(v) == -1) {
                    dist(v) = dist(u) + 1
                    queue.enqueue(v)
                }
            }
        }

        power(2, maxDepth.toLong - 1, 1000000007L).toInt
    }

    def power(base: Long, exp: Long, mod: Long): Long = {
        if (exp < 0) return 1L
        var res = 1L
        var b = base % mod
        var e = exp
        while (e > 0) {
            if (e % 2 == 1) res = (res * b) % mod
            b = (b * b) % mod
            e /= 2
        }
        res
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
    pub fn assign_edge_weights(edges: Vec<Vec<i32>>) -> i32 {
        let n = edges.len() + 1;
        let mut adj = vec![vec![]; n + 1];
        for edge in edges {
            let u = edge[0] as usize;
            let v = edge[1] as usize;
            adj[u].push(v);
            adj[v].push(u);
        }

        let mut max_depth = 0;
        let mut queue = VecDeque::new();
        let mut visited = vec![false; n + 1];

        queue.push_back((1, 0));
        visited[1] = true;

        while let Some((u, d)) = queue.pop_front() {
            if d > max_depth {
                max_depth = d;
            }
            for &v in &adj[u] {
                if !visited[v] {
                    visited[v] = true;
                    queue.push_back((v, d + 1));
                }
            }
        }

        if max_depth == 0 {
            return 0;
        }

        Self::pow_mod(2, (max_depth - 1) as u64, 1_000_000_007) as i32
    }

    fn pow_mod(mut base: u64, mut exp: u64, m: u64) -> u64 {
        let mut res = 1;
        base %= m;
        while exp > 0 {
            if exp % 2 == 1 {
                res = (res * base) % m;
            }
            base = (base * base) % m;
            exp /= 2;
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
(define/contract (assign-edge-weights edges)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([n (+ (length edges) 1)]
         [adj (make-vector (+ n 1) '())])
    (for ([edge edges])
      (let ([u (car edge)]
            [v (cadr edge)])
        (vector-set! adj u (cons v (vector-ref adj u)))
        (vector-set! adj v (cons u (vector-ref adj v)))))
    (let ([visited (make-vector (+ n 1) #f)]
          [max-d 0])
      (vector-set! visited 1 #t)
      (let loop ([queue (list (cons 1 0))]
                 [tail '()])
        (cond
          [(and (null? queue) (null? tail))
           (if (>= max-d 1)
               (let loop-pow ([b 2] [e (- max-d 1)] [res 1])
                 (cond
                   [(= e 0) res]
                   [(odd? e) (loop-pow (remainder (* b b) 1000000007) (quotient e 2) (remainder (* res b) 1000000007))]
                   [else (loop-pow (remainder (* b b) 1000000007) (quotient e 2) res)]))
               0)]
          [(null? queue) (loop (reverse tail) '())]
          [else
           (let* ([curr (car queue)]
                  [u (car curr)]
                  [d (cdr curr)])
             (when (> d max-d) (set! max-d d))
             (let ([new-tail tail])
               (for-each (lambda (v)
                           (unless (vector-ref visited v)
                             (vector-set! visited v #t)
                             (set! new-tail (cons (cons v (+ d 1)) new-tail))))
                         (vector-ref adj u))
               (loop (cdr queue) new-tail)))])))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec assign_edge_weights(Edges :: [[integer()]]) -> integer().
assign_edge_weights(Edges) ->
  Adj = build_adj(Edges, #{}),
  MaxDepth = find_max_depth(Adj),
  if MaxDepth < 1 -> 0;
     true -> pow_mod(2, MaxDepth - 1, 1000000007)
  end.

build_adj([], Map) -> Map;
build_adj([[U, V] | T], Map) ->
  M1 = maps:update_with(U, fun(L) -> [V | L] end, [V], Map),
  M2 = maps:update_with(V, fun(L) -> [U | L] end, [U], M1),
  build_adj(T, M2).

find_max_depth(Adj) ->
  Q = queue:in({1, 0}, queue:new()),
  V = #{1 => true},
  bfs(Q, V, Adj, 0).

bfs(Q, V, Adj, MaxD) ->
  case queue:out(Q) of
    {empty, _} -> MaxD;
    {{value, {U, D}}, Q2} ->
      Neighbors = maps:get(U, Adj, []),
      {NewQ, NewV} = lists:foldl(fun(Node, {AccQ, AccV}) ->
        case maps:is_key(Node, AccV) of
          true -> {AccQ, AccV};
          false -> {queue:in({Node, D + 1}, AccQ), AccV#{Node => true}}
        end
      end, {Q2, V}, Neighbors),
      bfs(NewQ, NewV, Adj, max(MaxD, D))
  end.

pow_mod(B, E, M) ->
  pow_mod_iter(B, E, M, 1).

pow_mod_iter(_B, 0, _M, Acc) -> Acc;
pow_mod_iter(B, E, M, Acc) ->
  NewAcc = if E rem 2 =:= 1 -> (Acc * B) rem M; true -> Acc end,
  pow_mod_iter((B * B) rem M, E div 2, M, NewAcc).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec assign_edge_weights(edges :: [[integer]]) :: integer
  def assign_edge_weights(edges) do
    adj = Enum.reduce(edges, %{}, fn [u, v], acc ->
      acc
      |> Map.update(u, [v], &[v | &1])
      |> Map.update(v, [u], &[u | &1])
    end)

    max_depth = find_max_depth(adj)
    if max_depth < 1 do
      0
    else
      pow_mod(2, max_depth - 1, 1_000_000_007)
    end
  end

  defp find_max_depth(adj) do
    q = :queue.in({1, 0}, :queue.new())
    v = MapSet.new([1])
    bfs(q, v, adj, 0)
  end

  defp bfs(q, v, adj, max_d) do
    case :queue.out(q) do
      {:empty, _} -> max_d
      {{:value, {u, d}}, q2} ->
        neighbors = Map.get(adj, u, [])
        {new_q, new_v} = Enum.reduce(neighbors, {q2, v}, fn node, {acc_q, acc_v} ->
          if MapSet.member?(acc_v, node) do
            {acc_q, acc_v}
          else
            {:queue.in({node, d + 1}, acc_q), MapSet.put(acc_v, node)}
          end
        end)
        bfs(new_q, new_v, adj, max(max_d, d))
    end
  end

  defp pow_mod(b, e, m) do
    pow_mod_iter(b, e, m, 1)
  end

  defp pow_mod_iter(_b, 0, _m, acc), do: acc
  defp pow_mod_iter(b, e, m, acc) do
    new_acc = if rem(e, 2) == 1, do: rem(acc * b, m), else: acc
    pow_mod_iter(rem(b * b, m), div(e, 2), m, new_acc)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) with one-paragraph explanation. The algorithm constructs an adjacency list from the input edges in $O(n)$ time and performs a BFS traversal to find the maximum depth, which visits each node and edge once, taking $O(n)$ time. The modular exponentiation for $2^{L-1}$ takes $O(\log n)$ time.
- **Space Complexity:** O(n) with one-paragraph explanation. The adjacency list stores $n$ nodes and $n-1$ undirected edges, requiring $O(n)$ space. Additionally, the BFS uses a queue and a distance array of size $n$, contributing $O(n)$ space complexity.
