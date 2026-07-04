---
layout: post
title: "Minimum Score of a Path Between Two Cities"
date: 2026-07-04 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Depth-First Search", "Breadth-First Search", "Union-Find", "Graph Theory"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minScore(int n, vector<vector<int>>&\
        \ roads) {\n        vector<vector<pair<int, int>>> adj(n + 1);\n        for\
        \ (const auto& road : roads) {\n            adj[road[0]].push_back({road[1],\
        \ road[2]});\n            adj[road[1]].push_back({road[0], road[2]});\n    \
        \    }\n\n        int min_val = 10001;\n        vector<bool> visited(n + 1,\
        \ false);\n        queue<int> q;\n\n        q.push(1);\n        visited[1] =\
        \ true;\n\n        while (!q.empty()) {\n            int curr = q.front();\n\
        \            q.pop();\n\n            for (auto& edge : adj[curr]) {\n      \
        \          int neighbor = edge.first;\n                int weight = edge.second;\n\
        \                if (weight < min_val) min_val = weight;\n                if\
        \ (!visited[neighbor]) {\n                    visited[neighbor] = true;\n  \
        \                  q.push(neighbor);\n                }\n            }\n   \
        \     }\n\n        return min_val;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int minScore(int n,\
        \ int[][] roads) {\n        List<int[]>[] adj = new ArrayList[n + 1];\n    \
        \    for (int i = 1; i <= n; i++) {\n            adj[i] = new ArrayList<>();\n\
        \        }\n        for (int[] road : roads) {\n            adj[road[0]].add(new\
        \ int[]{road[1], road[2]});\n            adj[road[1]].add(new int[]{road[0],\
        \ road[2]});\n        }\n\n        int minScore = Integer.MAX_VALUE;\n     \
        \   boolean[] visited = new boolean[n + 1];\n        Queue<Integer> queue =\
        \ new LinkedList<>();\n\n        queue.offer(1);\n        visited[1] = true;\n\
        \n        while (!queue.isEmpty()) {\n            int curr = queue.poll();\n\
        \            for (int[] edge : adj[curr]) {\n                int neighbor =\
        \ edge[0];\n                int weight = edge[1];\n                minScore\
        \ = Math.min(minScore, weight);\n                if (!visited[neighbor]) {\n\
        \                    visited[neighbor] = true;\n                    queue.offer(neighbor);\n\
        \                }\n            }\n        }\n\n        return minScore;\n \
        \   }\n}"
      python: "import collections\n\nclass Solution(object):\n    def minScore(self,\
        \ n, roads):\n        \"\"\"\n        :type n: int\n        :type roads: List[List[int]]\n\
        \        :rtype: int\n        \"\"\"\n        adj = collections.defaultdict(list)\n\
        \        for u, v, w in roads:\n            adj[u].append((v, w))\n        \
        \    adj[v].append((u, w))\n\n        min_score = float('inf')\n        q =\
        \ collections.deque([1])\n        visited = set([1])\n\n        while q:\n \
        \           u = q.popleft()\n            for v, w in adj[u]:\n             \
        \   if w < min_score:\n                    min_score = w\n                if\
        \ v not in visited:\n                    visited.add(v)\n                  \
        \  q.append(v)\n\n        return int(min_score)"
      python3: "import collections\n\nclass Solution:\n    def minScore(self, n: int,\
        \ roads: List[List[int]]) -> int:\n        adj = collections.defaultdict(list)\n\
        \        for u, v, w in roads:\n            adj[u].append((v, w))\n        \
        \    adj[v].append((u, w))\n\n        min_score = float('inf')\n        q =\
        \ collections.deque([1])\n        visited = {1}\n\n        while q:\n      \
        \      u = q.popleft()\n            for v, w in adj[u]:\n                if\
        \ w < min_score:\n                    min_score = w\n                if v not\
        \ in visited:\n                    visited.add(v)\n                    q.append(v)\n\
        \n        return int(min_score)"
      c: "#include <stdlib.h>\n#include <limits.h>\n\nint find(int* parent, int i) {\n\
        \    if (parent[i] == i) return i;\n    return parent[i] = find(parent, parent[i]);\n\
        }\n\nvoid unite(int* parent, int* rank, int i, int j) {\n    int rootI = find(parent,\
        \ i);\n    int rootJ = find(parent, j);\n    if (rootI != rootJ) {\n       \
        \ if (rank[rootI] < rank[rootJ]) {\n            parent[rootI] = rootJ;\n   \
        \     } else if (rank[rootI] > rank[rootJ]) {\n            parent[rootJ] = rootI;\n\
        \        } else {\n            parent[rootI] = rootJ;\n            rank[rootJ]++;\n\
        \        }\n    }\n}\n\nint minScore(int n, int** roads, int roadsSize, int*\
        \ roadsColSize) {\n    int* parent = (int*)malloc((n + 1) * sizeof(int));\n\
        \    int* rank = (int*)calloc((n + 1), sizeof(int));\n    for (int i = 1; i\
        \ <= n; i++) {\n        parent[i] = i;\n    }\n\n    for (int i = 0; i < roadsSize;\
        \ i++) {\n        unite(parent, rank, roads[i][0], roads[i][1]);\n    }\n\n\
        \    int root1 = find(parent, 1);\n    int min_val = INT_MAX;\n\n    for (int\
        \ i = 0; i < roadsSize; i++) {\n        if (find(parent, roads[i][0]) == root1)\
        \ {\n            if (roads[i][2] < min_val) {\n                min_val = roads[i][2];\n\
        \            }\n        }\n    }\n\n    free(parent);\n    free(rank);\n   \
        \ return min_val;\n}"
      csharp: "public class Solution {\n    public int MinScore(int n, int[][] roads)\
        \ {\n        System.Collections.Generic.List<int>[] adj = new System.Collections.Generic.List<int>[n\
        \ + 1];\n        for (int i = 0; i <= n; i++) {\n            adj[i] = new System.Collections.Generic.List<int>();\n\
        \        }\n        foreach (int[] road in roads) {\n            int u = road[0],\
        \ v = road[1], w = road[2];\n            adj[u].Add(v);\n            adj[u].Add(w);\n\
        \            adj[v].Add(u);\n            adj[v].Add(w);\n        }\n\n     \
        \   int minS = int.MaxValue;\n        System.Collections.Generic.Queue<int>\
        \ q = new System.Collections.Generic.Queue<int>();\n        bool[] visited =\
        \ new bool[n + 1];\n\n        q.Enqueue(1);\n        visited[1] = true;\n\n\
        \        while (q.Count > 0) {\n            int u = q.Dequeue();\n         \
        \   System.Collections.Generic.List<int> neighbors = adj[u];\n            for\
        \ (int i = 0; i < neighbors.Count; i += 2) {\n                int v = neighbors[i];\n\
        \                int w = neighbors[i + 1];\n                if (w < minS) minS\
        \ = w;\n                if (!visited[v]) {\n                    visited[v] =\
        \ true;\n                    q.Enqueue(v);\n                }\n            }\n\
        \        }\n\n        return minS;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number[][]} roads\n * @return\
        \ {number}\n */\nvar minScore = function(n, roads) {\n    const adj = Array.from({\
        \ length: n + 1 }, () => []);\n    for (let i = 0; i < roads.length; i++) {\n\
        \        const road = roads[i];\n        const u = road[0], v = road[1], w =\
        \ road[2];\n        adj[u].push(v, w);\n        adj[v].push(u, w);\n    }\n\n\
        \    let minS = Infinity;\n    const visited = new Uint8Array(n + 1);\n    const\
        \ queue = [1];\n    visited[1] = 1;\n    let head = 0;\n\n    while (head <\
        \ queue.length) {\n        const u = queue[head++];\n        const list = adj[u];\n\
        \        for (let i = 0; i < list.length; i += 2) {\n            const v = list[i];\n\
        \            const w = list[i + 1];\n            if (w < minS) minS = w;\n \
        \           if (!visited[v]) {\n                visited[v] = 1;\n          \
        \      queue.push(v);\n            }\n        }\n    }\n\n    return minS;\n\
        };"
      typescript: "function minScore(n: number, roads: number[][]): number {\n    const\
        \ adj: number[][] = Array.from({ length: n + 1 }, () => []);\n    for (let i\
        \ = 0; i < roads.length; i++) {\n        const road = roads[i];\n        const\
        \ u = road[0], v = road[1], w = road[2];\n        adj[u].push(v, w);\n     \
        \   adj[v].push(u, w);\n    }\n\n    let minS = Infinity;\n    const visited\
        \ = new Uint8Array(n + 1);\n    const queue: number[] = [1];\n    visited[1]\
        \ = 1;\n    let head = 0;\n\n    while (head < queue.length) {\n        const\
        \ u = queue[head++];\n        const list = adj[u];\n        for (let i = 0;\
        \ i < list.length; i += 2) {\n            const v = list[i];\n            const\
        \ w = list[i + 1];\n            if (w < minS) minS = w;\n            if (!visited[v])\
        \ {\n                visited[v] = 1;\n                queue.push(v);\n     \
        \       }\n        }\n    }\n\n    return minS;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @param Integer[][]\
        \ $roads\n     * @return Integer\n     */\n    function minScore($n, $roads)\
        \ {\n        $adj = [];\n        for ($i = 1; $i <= $n; $i++) {\n          \
        \  $adj[$i] = [];\n        }\n        foreach ($roads as $road) {\n        \
        \    $u = $road[0];\n            $v = $road[1];\n            $w = $road[2];\n\
        \            $adj[$u][] = $v;\n            $adj[$u][] = $w;\n            $adj[$v][]\
        \ = $u;\n            $adj[$v][] = $w;\n        }\n\n        $minS = PHP_INT_MAX;\n\
        \        $visited = array_fill(1, $n, false);\n        $queue = new \\SplQueue();\n\
        \        $queue->enqueue(1);\n        $visited[1] = true;\n\n        while (!$queue->isEmpty())\
        \ {\n            $u = $queue->dequeue();\n            $list = $adj[$u];\n  \
        \          $cnt = count($list);\n            for ($i = 0; $i < $cnt; $i += 2)\
        \ {\n                $v = $list[$i];\n                $w = $list[$i + 1];\n\
        \                if ($w < $minS) $minS = $w;\n                if (!$visited[$v])\
        \ {\n                    $visited[$v] = true;\n                    $queue->enqueue($v);\n\
        \                }\n            }\n        }\n\n        return $minS;\n    }\n\
        }"
      swift: "class Solution {\n    func minScore(_ n: Int, _ roads: [[Int]]) -> Int\
        \ {\n        var adj = [[Int]](repeating: [], count: n + 1)\n        for road\
        \ in roads {\n            let u = road[0], v = road[1], w = road[2]\n      \
        \      adj[u].append(v)\n            adj[u].append(w)\n            adj[v].append(u)\n\
        \            adj[v].append(w)\n        }\n\n        var minS = Int.max\n   \
        \     var visited = [Bool](repeating: false, count: n + 1)\n        var queue\
        \ = [1]\n        var head = 0\n        visited[1] = true\n\n        while head\
        \ < queue.count {\n            let u = queue[head]\n            head += 1\n\
        \            let list = adj[u]\n            var i = 0\n            let count\
        \ = list.count\n            while i < count {\n                let v = list[i]\n\
        \                let w = list[i + 1]\n                if w < minS {\n      \
        \              minS = w\n                }\n                if !visited[v] {\n\
        \                    visited[v] = true\n                    queue.append(v)\n\
        \                }\n                i += 2\n            }\n        }\n\n   \
        \     return minS\n    }\n}"
      kotlin: "import java.util.*\n\nclass Solution {\n    fun minScore(n: Int, roads:\
        \ Array<IntArray>): Int {\n        val adj = Array(n + 1) { mutableListOf<IntArray>()\
        \ }\n        for (road in roads) {\n            val u = road[0]\n          \
        \  val v = road[1]\n            val d = road[2]\n            adj[u].add(intArrayOf(v,\
        \ d))\n            adj[v].add(intArrayOf(u, d))\n        }\n\n        var minDistance\
        \ = 10001\n        val visited = BooleanArray(n + 1)\n        val queue: Queue<Int>\
        \ = LinkedList<Int>()\n\n        queue.add(1)\n        visited[1] = true\n\n\
        \        while (queue.isNotEmpty()) {\n            val u = queue.remove()\n\
        \            for (edge in adj[u]) {\n                val v = edge[0]\n     \
        \           val d = edge[1]\n                if (d < minDistance) {\n      \
        \              minDistance = d\n                }\n                if (!visited[v])\
        \ {\n                    visited[v] = true\n                    queue.add(v)\n\
        \                }\n            }\n        }\n\n        return minDistance\n\
        \    }\n}"
      dart: "import 'dart:collection';\n\nclass Solution {\n  int minScore(int n, List<List<int>>\
        \ roads) {\n    List<List<List<int>>> adj = List.generate(n + 1, (_) => []);\n\
        \    for (var road in roads) {\n      int u = road[0];\n      int v = road[1];\n\
        \      int d = road[2];\n      adj[u].add([v, d]);\n      adj[v].add([u, d]);\n\
        \    }\n\n    int minDistance = 10001;\n    List<bool> visited = List.filled(n\
        \ + 1, false);\n    Queue<int> queue = Queue<int>();\n\n    queue.add(1);\n\
        \    visited[1] = true;\n\n    while (queue.isNotEmpty) {\n      int u = queue.removeFirst();\n\
        \      for (var edge in adj[u]) {\n        int v = edge[0];\n        int d =\
        \ edge[1];\n        if (d < minDistance) {\n          minDistance = d;\n   \
        \     }\n        if (!visited[v]) {\n          visited[v] = true;\n        \
        \  queue.add(v);\n        }\n      }\n    }\n\n    return minDistance;\n  }\n\
        }"
      go: "func minScore(n int, roads [][]int) int {\n    type edge struct {\n     \
        \   to   int\n        dist int\n    }\n    adj := make([][]edge, n+1)\n    for\
        \ _, road := range roads {\n        u, v, d := road[0], road[1], road[2]\n \
        \       adj[u] = append(adj[u], edge{v, d})\n        adj[v] = append(adj[v],\
        \ edge{u, d})\n    }\n\n    minDist := 10001\n    visited := make([]bool, n+1)\n\
        \    queue := make([]int, 0, n)\n    queue = append(queue, 1)\n    visited[1]\
        \ = true\n\n    for len(queue) > 0 {\n        u := queue[0]\n        queue =\
        \ queue[1:]\n\n        for _, e := range adj[u] {\n            if e.dist < minDist\
        \ {\n                minDist = e.dist\n            }\n            if !visited[e.to]\
        \ {\n                visited[e.to] = true\n                queue = append(queue,\
        \ e.to)\n            }\n        }\n    }\n\n    return minDist\n}"
      ruby: "# @param {Integer} n\n# @param {Integer[][]} roads\n# @return {Integer}\n\
        def min_score(n, roads)\n  adj = Array.new(n + 1) { [] }\n  roads.each do |u,\
        \ v, d|\n    adj[u] << [v, d]\n    adj[v] << [u, d]\n  end\n\n  min_dist = 10001\n\
        \  visited = Array.new(n + 1, false)\n  queue = [1]\n  visited[1] = true\n \
        \ head = 0\n\n  while head < queue.length\n    u = queue[head]\n    head +=\
        \ 1\n\n    adj[u].each do |v, d|\n      min_dist = d if d < min_dist\n     \
        \ unless visited[v]\n        visited[v] = true\n        queue << v\n      end\n\
        \    end\n  end\n\n  min_dist\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def minScore(n:\
        \ Int, roads: Array[Array[Int]]): Int = {\n        val adj = Array.tabulate(n\
        \ + 1)(_ => mutable.ArrayBuffer[(Int, Int)]())\n        for (road <- roads)\
        \ {\n            val u = road(0)\n            val v = road(1)\n            val\
        \ d = road(2)\n            adj(u) += ((v, d))\n            adj(v) += ((u, d))\n\
        \        }\n\n        var minDistance = 10001\n        val visited = new Array[Boolean](n\
        \ + 1)\n        val queue = new mutable.Queue[Int]()\n\n        queue.enqueue(1)\n\
        \        visited(1) = true\n\n        while (queue.nonEmpty) {\n           \
        \ val u = queue.dequeue()\n            for ((v, d) <- adj(u)) {\n          \
        \      if (d < minDistance) {\n                    minDistance = d\n       \
        \         }\n                if (!visited(v)) {\n                    visited(v)\
        \ = true\n                    queue.enqueue(v)\n                }\n        \
        \    }\n        }\n\n        minDistance\n    }\n}"
      rust: "use std::collections::VecDeque;\n\nimpl Solution {\n    pub fn min_score(n:\
        \ i32, roads: Vec<Vec<i32>>) -> i32 {\n        let n = n as usize;\n       \
        \ let mut adj = vec![vec![]; n + 1];\n        for road in roads {\n        \
        \    let u = road[0] as usize;\n            let v = road[1] as usize;\n    \
        \        let d = road[2];\n            adj[u].push((v, d));\n            adj[v].push((u,\
        \ d));\n        }\n\n        let mut min_val = 10001;\n        let mut visited\
        \ = vec![false; n + 1];\n        let mut stack = Vec::new();\n\n        stack.push(1);\n\
        \        visited[1] = true;\n\n        while let Some(u) = stack.pop() {\n \
        \           for &(v, d) in &adj[u] {\n                if d < min_val {\n   \
        \                 min_val = d;\n                }\n                if !visited[v]\
        \ {\n                    visited[v] = true;\n                    stack.push(v);\n\
        \                }\n            }\n        }\n\n        min_val\n    }\n}"
      racket: "(define/contract (min-score n roads)\n  (-> exact-integer? (listof (listof\
        \ exact-integer?)) exact-integer?)\n  (let* ([adj (make-vector (+ n 1) '())]\n\
        \         [visited (make-vector (+ n 1) #f)]\n         [min-val (box 10001)])\n\
        \    (for ([road roads])\n      (let ([u (list-ref road 0)]\n            [v\
        \ (list-ref road 1)]\n            [d (list-ref road 2)])\n        (vector-set!\
        \ adj u (cons (list v d) (vector-ref adj u)))\n        (vector-set! adj v (cons\
        \ (list u d) (vector-ref adj v)))))\n    (vector-set! visited 1 #t)\n    (let\
        \ loop ([stack '(1)])\n      (if (null? stack)\n          (unbox min-val)\n\
        \          (let* ([u (car stack)]\n                 [rest (cdr stack)]\n   \
        \              [neighbors (vector-ref adj u)])\n            (let ([next-stack\n\
        \                   (foldl (lambda (edge acc)\n                            (let\
        \ ([v (car edge)]\n                                  [d (cadr edge)])\n    \
        \                          (when (< d (unbox min-val))\n                   \
        \             (set-box! min-val d))\n                              (if (vector-ref\
        \ visited v)\n                                  acc\n                      \
        \            (begin\n                                    (vector-set! visited\
        \ v #t)\n                                    (cons v acc)))))\n            \
        \              rest\n                          neighbors)])\n              (loop\
        \ next-stack)))))))"
      erlang: "-spec min_score(N :: integer(), Roads :: [[integer()]]) -> integer().\n\
        min_score(_N, Roads) ->\n  Adj = lists:foldl(fun([U, V, D], Acc) ->\n    A1\
        \ = maps:put(U, [{V, D} | maps:get(U, Acc, [])], Acc),\n    maps:put(V, [{U,\
        \ D} | maps:get(V, A1, [])], A1)\n  end, #{}, Roads),\n  bfs([1], sets:from_list([1]),\
        \ Adj, 10001).\n\nbfs([], _, _, Min) -> \n  Min;\nbfs([U | Rest], Visited, Adj,\
        \ Min) ->\n  Neighbors = maps:get(U, Adj, []),\n  {NewRest, NewVisited, NewMin}\
        \ = lists:foldl(fun({V, D}, {AccRest, AccVisited, AccMin}) ->\n    NewAccMin\
        \ = min(AccMin, D),\n    case sets:is_element(V, AccVisited) of\n      true\
        \ -> {AccRest, AccVisited, NewAccMin};\n      false -> {[V | AccRest], sets:add_element(V,\
        \ AccVisited), NewAccMin}\n    end\n  end, {Rest, Visited, Min}, Neighbors),\n\
        \  bfs(NewRest, NewVisited, Adj, NewMin)."
      elixir: "defmodule Solution do\n  @spec min_score(n :: integer, roads :: [[integer]])\
        \ :: integer\n  def min_score(_n, roads) do\n    adj = Enum.reduce(roads, %{},\
        \ fn [u, v, d], acc ->\n      acc\n      |> Map.update(u, [{v, d}], &([{v, d}\
        \ | &1]))\n      |> Map.update(v, [{u, d}], &([{u, d} | &1]))\n    end)\n  \
        \  bfs([1], MapSet.new([1]), adj, 10001)\n  end\n\n  defp bfs([], _visited,\
        \ _adj, min_val), do: min_val\n  defp bfs([u | rest], visited, adj, min_val)\
        \ do\n    neighbors = Map.get(adj, u, [])\n    {new_rest, new_visited, new_min}\
        \ = Enum.reduce(neighbors, {rest, visited, min_val}, fn {v, d}, {acc_rest, acc_visited,\
        \ acc_min} ->\n      new_acc_min = min(acc_min, d)\n      if MapSet.member?(acc_visited,\
        \ v) do\n        {acc_rest, acc_visited, new_acc_min}\n      else\n        {[v\
        \ | acc_rest], MapSet.put(acc_visited, v), new_acc_min}\n      end\n    end)\n\
        \    bfs(new_rest, new_visited, adj, new_min)\n  end\nend"
    approach: 'The problem asks for the minimum road distance along any path between
      city 1 and city $n$. Because the path can visit any road or city multiple times,
      any road that belongs to the same connected component as city 1 can be included
      in the path from 1 to $n$. Since city 1 and city $n$ are guaranteed to be connected,
      the problem simplifies to finding the minimum weight among all roads in the connected
      component containing city 1.


      To solve this, we can perform a graph traversal like Breadth-First Search (BFS)
      or Depth-First Search (DFS) starting from city 1 to identify all reachable nodes
      and edges. While traversing, we keep track of the minimum weight of every edge
      connected to the cities in this component. Alternatively, a Union-Find (Disjoint
      Set Union) approach can be used to group nodes and then iterate through all roads
      to find the minimum distance belonging to the set containing city 1.'
    time_complexity: O(N + E) where N is the number of cities and E is the number of
      roads. In the BFS/DFS approach, we visit every node and edge in the connected
      component at most once. In the Union-Find approach, the complexity is $O(E \cdot
      \alpha(N))$, where $\alpha$ is the inverse Ackermann function, which is nearly
      constant for all practical purposes.
    space_complexity: O(N + E) to store the graph as an adjacency list and keep track
      of visited nodes. In the Union-Find approach, the space complexity is $O(N)$ for
      the parent and rank arrays, as it doesn't require storing the full adjacency list.
    elapsed_time: 201.06195282936096
    model: gemini-3-flash-preview
    generated_at: '2026-07-04 02:12:11 '
---

## Problem #2492: Minimum Score of a Path Between Two Cities

**Difficulty:** Medium

**Topics:** Depth-First Search, Breadth-First Search, Union-Find, Graph Theory

## Problem Description

<p>You are given a positive integer <code>n</code> representing <code>n</code> cities numbered from <code>1</code> to <code>n</code>. You are also given a <strong>2D</strong> array <code>roads</code> where <code>roads[i] = [a<sub>i</sub>, b<sub>i</sub>, distance<sub>i</sub>]</code> indicates that there is a <strong>bidirectional </strong>road between cities <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> with a distance equal to <code>distance<sub>i</sub></code>. The cities graph is not necessarily connected.</p>

<p>The <strong>score</strong> of a path between two cities is defined as the <strong>minimum </strong>distance of a road in this path.</p>

<p>Return <em>the <strong>minimum </strong>possible score of a path between cities </em><code>1</code><em> and </em><code>n</code>.</p>

<p><strong>Note</strong>:</p>

<ul>
	<li>A path is a sequence of roads between two cities.</li>
	<li>It is allowed for a path to contain the same road <strong>multiple</strong> times, and you can visit cities <code>1</code> and <code>n</code> multiple times along the path.</li>
	<li>The test cases are generated such that there is <strong>at least</strong> one path between <code>1</code> and <code>n</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/10/12/graph11.png" style="width: 190px; height: 231px;" />
<pre>
<strong>Input:</strong> n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The path from city 1 to 4 with the minimum score is: 1 -&gt; 2 -&gt; 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/10/12/graph22.png" style="width: 190px; height: 231px;" />
<pre>
<strong>Input:</strong> n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The path from city 1 to 4 with the minimum score is: 1 -&gt; 2 -&gt; 1 -&gt; 3 -&gt; 4. The score of this path is min(2,2,4,7) = 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= roads.length &lt;= 10<sup>5</sup></code></li>
	<li><code>roads[i].length == 3</code></li>
	<li><code>1 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>1 &lt;= distance<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
	<li>There are no repeated edges.</li>
	<li>There is at least one path between <code>1</code> and <code>n</code>.</li>
</ul>


## Hints

1. Can you solve the problem if the whole graph is connected?

2. Notice that if the graph is connected, you can always use any edge of the graph in your path.

3. How to solve the general problem in a similar way? Remove all the nodes that are not connected to 1 and n, then apply the previous solution in the new graph.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the minimum road distance along any path between city 1 and city $n$. Because the path can visit any road or city multiple times, any road that belongs to the same connected component as city 1 can be included in the path from 1 to $n$. Since city 1 and city $n$ are guaranteed to be connected, the problem simplifies to finding the minimum weight among all roads in the connected component containing city 1.

To solve this, we can perform a graph traversal like Breadth-First Search (BFS) or Depth-First Search (DFS) starting from city 1 to identify all reachable nodes and edges. While traversing, we keep track of the minimum weight of every edge connected to the cities in this component. Alternatively, a Union-Find (Disjoint Set Union) approach can be used to group nodes and then iterate through all roads to find the minimum distance belonging to the set containing city 1.

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
    int minScore(int n, vector<vector<int>>& roads) {
        vector<vector<pair<int, int>>> adj(n + 1);
        for (const auto& road : roads) {
            adj[road[0]].push_back({road[1], road[2]});
            adj[road[1]].push_back({road[0], road[2]});
        }

        int min_val = 10001;
        vector<bool> visited(n + 1, false);
        queue<int> q;

        q.push(1);
        visited[1] = true;

        while (!q.empty()) {
            int curr = q.front();
            q.pop();

            for (auto& edge : adj[curr]) {
                int neighbor = edge.first;
                int weight = edge.second;
                if (weight < min_val) min_val = weight;
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }

        return min_val;
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
    public int minScore(int n, int[][] roads) {
        List<int[]>[] adj = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int[] road : roads) {
            adj[road[0]].add(new int[]{road[1], road[2]});
            adj[road[1]].add(new int[]{road[0], road[2]});
        }

        int minScore = Integer.MAX_VALUE;
        boolean[] visited = new boolean[n + 1];
        Queue<Integer> queue = new LinkedList<>();

        queue.offer(1);
        visited[1] = true;

        while (!queue.isEmpty()) {
            int curr = queue.poll();
            for (int[] edge : adj[curr]) {
                int neighbor = edge[0];
                int weight = edge[1];
                minScore = Math.min(minScore, weight);
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.offer(neighbor);
                }
            }
        }

        return minScore;
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
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adj = collections.defaultdict(list)
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        min_score = float('inf')
        q = collections.deque([1])
        visited = set([1])

        while q:
            u = q.popleft()
            for v, w in adj[u]:
                if w < min_score:
                    min_score = w
                if v not in visited:
                    visited.add(v)
                    q.append(v)

        return int(min_score)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        min_score = float('inf')
        q = collections.deque([1])
        visited = {1}

        while q:
            u = q.popleft()
            for v, w in adj[u]:
                if w < min_score:
                    min_score = w
                if v not in visited:
                    visited.add(v)
                    q.append(v)

        return int(min_score)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <limits.h>

int find(int* parent, int i) {
    if (parent[i] == i) return i;
    return parent[i] = find(parent, parent[i]);
}

void unite(int* parent, int* rank, int i, int j) {
    int rootI = find(parent, i);
    int rootJ = find(parent, j);
    if (rootI != rootJ) {
        if (rank[rootI] < rank[rootJ]) {
            parent[rootI] = rootJ;
        } else if (rank[rootI] > rank[rootJ]) {
            parent[rootJ] = rootI;
        } else {
            parent[rootI] = rootJ;
            rank[rootJ]++;
        }
    }
}

int minScore(int n, int** roads, int roadsSize, int* roadsColSize) {
    int* parent = (int*)malloc((n + 1) * sizeof(int));
    int* rank = (int*)calloc((n + 1), sizeof(int));
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }

    for (int i = 0; i < roadsSize; i++) {
        unite(parent, rank, roads[i][0], roads[i][1]);
    }

    int root1 = find(parent, 1);
    int min_val = INT_MAX;

    for (int i = 0; i < roadsSize; i++) {
        if (find(parent, roads[i][0]) == root1) {
            if (roads[i][2] < min_val) {
                min_val = roads[i][2];
            }
        }
    }

    free(parent);
    free(rank);
    return min_val;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinScore(int n, int[][] roads) {
        System.Collections.Generic.List<int>[] adj = new System.Collections.Generic.List<int>[n + 1];
        for (int i = 0; i <= n; i++) {
            adj[i] = new System.Collections.Generic.List<int>();
        }
        foreach (int[] road in roads) {
            int u = road[0], v = road[1], w = road[2];
            adj[u].Add(v);
            adj[u].Add(w);
            adj[v].Add(u);
            adj[v].Add(w);
        }

        int minS = int.MaxValue;
        System.Collections.Generic.Queue<int> q = new System.Collections.Generic.Queue<int>();
        bool[] visited = new bool[n + 1];

        q.Enqueue(1);
        visited[1] = true;

        while (q.Count > 0) {
            int u = q.Dequeue();
            System.Collections.Generic.List<int> neighbors = adj[u];
            for (int i = 0; i < neighbors.Count; i += 2) {
                int v = neighbors[i];
                int w = neighbors[i + 1];
                if (w < minS) minS = w;
                if (!visited[v]) {
                    visited[v] = true;
                    q.Enqueue(v);
                }
            }
        }

        return minS;
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
 * @param {number[][]} roads
 * @return {number}
 */
var minScore = function(n, roads) {
    const adj = Array.from({ length: n + 1 }, () => []);
    for (let i = 0; i < roads.length; i++) {
        const road = roads[i];
        const u = road[0], v = road[1], w = road[2];
        adj[u].push(v, w);
        adj[v].push(u, w);
    }

    let minS = Infinity;
    const visited = new Uint8Array(n + 1);
    const queue = [1];
    visited[1] = 1;
    let head = 0;

    while (head < queue.length) {
        const u = queue[head++];
        const list = adj[u];
        for (let i = 0; i < list.length; i += 2) {
            const v = list[i];
            const w = list[i + 1];
            if (w < minS) minS = w;
            if (!visited[v]) {
                visited[v] = 1;
                queue.push(v);
            }
        }
    }

    return minS;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minScore(n: number, roads: number[][]): number {
    const adj: number[][] = Array.from({ length: n + 1 }, () => []);
    for (let i = 0; i < roads.length; i++) {
        const road = roads[i];
        const u = road[0], v = road[1], w = road[2];
        adj[u].push(v, w);
        adj[v].push(u, w);
    }

    let minS = Infinity;
    const visited = new Uint8Array(n + 1);
    const queue: number[] = [1];
    visited[1] = 1;
    let head = 0;

    while (head < queue.length) {
        const u = queue[head++];
        const list = adj[u];
        for (let i = 0; i < list.length; i += 2) {
            const v = list[i];
            const w = list[i + 1];
            if (w < minS) minS = w;
            if (!visited[v]) {
                visited[v] = 1;
                queue.push(v);
            }
        }
    }

    return minS;
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
     * @param Integer[][] $roads
     * @return Integer
     */
    function minScore($n, $roads) {
        $adj = [];
        for ($i = 1; $i <= $n; $i++) {
            $adj[$i] = [];
        }
        foreach ($roads as $road) {
            $u = $road[0];
            $v = $road[1];
            $w = $road[2];
            $adj[$u][] = $v;
            $adj[$u][] = $w;
            $adj[$v][] = $u;
            $adj[$v][] = $w;
        }

        $minS = PHP_INT_MAX;
        $visited = array_fill(1, $n, false);
        $queue = new \SplQueue();
        $queue->enqueue(1);
        $visited[1] = true;

        while (!$queue->isEmpty()) {
            $u = $queue->dequeue();
            $list = $adj[$u];
            $cnt = count($list);
            for ($i = 0; $i < $cnt; $i += 2) {
                $v = $list[$i];
                $w = $list[$i + 1];
                if ($w < $minS) $minS = $w;
                if (!$visited[$v]) {
                    $visited[$v] = true;
                    $queue->enqueue($v);
                }
            }
        }

        return $minS;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minScore(_ n: Int, _ roads: [[Int]]) -> Int {
        var adj = [[Int]](repeating: [], count: n + 1)
        for road in roads {
            let u = road[0], v = road[1], w = road[2]
            adj[u].append(v)
            adj[u].append(w)
            adj[v].append(u)
            adj[v].append(w)
        }

        var minS = Int.max
        var visited = [Bool](repeating: false, count: n + 1)
        var queue = [1]
        var head = 0
        visited[1] = true

        while head < queue.count {
            let u = queue[head]
            head += 1
            let list = adj[u]
            var i = 0
            let count = list.count
            while i < count {
                let v = list[i]
                let w = list[i + 1]
                if w < minS {
                    minS = w
                }
                if !visited[v] {
                    visited[v] = true
                    queue.append(v)
                }
                i += 2
            }
        }

        return minS
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
    fun minScore(n: Int, roads: Array<IntArray>): Int {
        val adj = Array(n + 1) { mutableListOf<IntArray>() }
        for (road in roads) {
            val u = road[0]
            val v = road[1]
            val d = road[2]
            adj[u].add(intArrayOf(v, d))
            adj[v].add(intArrayOf(u, d))
        }

        var minDistance = 10001
        val visited = BooleanArray(n + 1)
        val queue: Queue<Int> = LinkedList<Int>()

        queue.add(1)
        visited[1] = true

        while (queue.isNotEmpty()) {
            val u = queue.remove()
            for (edge in adj[u]) {
                val v = edge[0]
                val d = edge[1]
                if (d < minDistance) {
                    minDistance = d
                }
                if (!visited[v]) {
                    visited[v] = true
                    queue.add(v)
                }
            }
        }

        return minDistance
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
  int minScore(int n, List<List<int>> roads) {
    List<List<List<int>>> adj = List.generate(n + 1, (_) => []);
    for (var road in roads) {
      int u = road[0];
      int v = road[1];
      int d = road[2];
      adj[u].add([v, d]);
      adj[v].add([u, d]);
    }

    int minDistance = 10001;
    List<bool> visited = List.filled(n + 1, false);
    Queue<int> queue = Queue<int>();

    queue.add(1);
    visited[1] = true;

    while (queue.isNotEmpty) {
      int u = queue.removeFirst();
      for (var edge in adj[u]) {
        int v = edge[0];
        int d = edge[1];
        if (d < minDistance) {
          minDistance = d;
        }
        if (!visited[v]) {
          visited[v] = true;
          queue.add(v);
        }
      }
    }

    return minDistance;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minScore(n int, roads [][]int) int {
    type edge struct {
        to   int
        dist int
    }
    adj := make([][]edge, n+1)
    for _, road := range roads {
        u, v, d := road[0], road[1], road[2]
        adj[u] = append(adj[u], edge{v, d})
        adj[v] = append(adj[v], edge{u, d})
    }

    minDist := 10001
    visited := make([]bool, n+1)
    queue := make([]int, 0, n)
    queue = append(queue, 1)
    visited[1] = true

    for len(queue) > 0 {
        u := queue[0]
        queue = queue[1:]

        for _, e := range adj[u] {
            if e.dist < minDist {
                minDist = e.dist
            }
            if !visited[e.to] {
                visited[e.to] = true
                queue = append(queue, e.to)
            }
        }
    }

    return minDist
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @param {Integer[][]} roads
# @return {Integer}
def min_score(n, roads)
  adj = Array.new(n + 1) { [] }
  roads.each do |u, v, d|
    adj[u] << [v, d]
    adj[v] << [u, d]
  end

  min_dist = 10001
  visited = Array.new(n + 1, false)
  queue = [1]
  visited[1] = true
  head = 0

  while head < queue.length
    u = queue[head]
    head += 1

    adj[u].each do |v, d|
      min_dist = d if d < min_dist
      unless visited[v]
        visited[v] = true
        queue << v
      end
    end
  end

  min_dist
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def minScore(n: Int, roads: Array[Array[Int]]): Int = {
        val adj = Array.tabulate(n + 1)(_ => mutable.ArrayBuffer[(Int, Int)]())
        for (road <- roads) {
            val u = road(0)
            val v = road(1)
            val d = road(2)
            adj(u) += ((v, d))
            adj(v) += ((u, d))
        }

        var minDistance = 10001
        val visited = new Array[Boolean](n + 1)
        val queue = new mutable.Queue[Int]()

        queue.enqueue(1)
        visited(1) = true

        while (queue.nonEmpty) {
            val u = queue.dequeue()
            for ((v, d) <- adj(u)) {
                if (d < minDistance) {
                    minDistance = d
                }
                if (!visited(v)) {
                    visited(v) = true
                    queue.enqueue(v)
                }
            }
        }

        minDistance
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
    pub fn min_score(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut adj = vec![vec![]; n + 1];
        for road in roads {
            let u = road[0] as usize;
            let v = road[1] as usize;
            let d = road[2];
            adj[u].push((v, d));
            adj[v].push((u, d));
        }

        let mut min_val = 10001;
        let mut visited = vec![false; n + 1];
        let mut stack = Vec::new();

        stack.push(1);
        visited[1] = true;

        while let Some(u) = stack.pop() {
            for &(v, d) in &adj[u] {
                if d < min_val {
                    min_val = d;
                }
                if !visited[v] {
                    visited[v] = true;
                    stack.push(v);
                }
            }
        }

        min_val
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-score n roads)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ([adj (make-vector (+ n 1) '())]
         [visited (make-vector (+ n 1) #f)]
         [min-val (box 10001)])
    (for ([road roads])
      (let ([u (list-ref road 0)]
            [v (list-ref road 1)]
            [d (list-ref road 2)])
        (vector-set! adj u (cons (list v d) (vector-ref adj u)))
        (vector-set! adj v (cons (list u d) (vector-ref adj v)))))
    (vector-set! visited 1 #t)
    (let loop ([stack '(1)])
      (if (null? stack)
          (unbox min-val)
          (let* ([u (car stack)]
                 [rest (cdr stack)]
                 [neighbors (vector-ref adj u)])
            (let ([next-stack
                   (foldl (lambda (edge acc)
                            (let ([v (car edge)]
                                  [d (cadr edge)])
                              (when (< d (unbox min-val))
                                (set-box! min-val d))
                              (if (vector-ref visited v)
                                  acc
                                  (begin
                                    (vector-set! visited v #t)
                                    (cons v acc)))))
                          rest
                          neighbors)])
              (loop next-stack)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_score(N :: integer(), Roads :: [[integer()]]) -> integer().
min_score(_N, Roads) ->
  Adj = lists:foldl(fun([U, V, D], Acc) ->
    A1 = maps:put(U, [{V, D} | maps:get(U, Acc, [])], Acc),
    maps:put(V, [{U, D} | maps:get(V, A1, [])], A1)
  end, #{}, Roads),
  bfs([1], sets:from_list([1]), Adj, 10001).

bfs([], _, _, Min) -> 
  Min;
bfs([U | Rest], Visited, Adj, Min) ->
  Neighbors = maps:get(U, Adj, []),
  {NewRest, NewVisited, NewMin} = lists:foldl(fun({V, D}, {AccRest, AccVisited, AccMin}) ->
    NewAccMin = min(AccMin, D),
    case sets:is_element(V, AccVisited) of
      true -> {AccRest, AccVisited, NewAccMin};
      false -> {[V | AccRest], sets:add_element(V, AccVisited), NewAccMin}
    end
  end, {Rest, Visited, Min}, Neighbors),
  bfs(NewRest, NewVisited, Adj, NewMin).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_score(n :: integer, roads :: [[integer]]) :: integer
  def min_score(_n, roads) do
    adj = Enum.reduce(roads, %{}, fn [u, v, d], acc ->
      acc
      |> Map.update(u, [{v, d}], &([{v, d} | &1]))
      |> Map.update(v, [{u, d}], &([{u, d} | &1]))
    end)
    bfs([1], MapSet.new([1]), adj, 10001)
  end

  defp bfs([], _visited, _adj, min_val), do: min_val
  defp bfs([u | rest], visited, adj, min_val) do
    neighbors = Map.get(adj, u, [])
    {new_rest, new_visited, new_min} = Enum.reduce(neighbors, {rest, visited, min_val}, fn {v, d}, {acc_rest, acc_visited, acc_min} ->
      new_acc_min = min(acc_min, d)
      if MapSet.member?(acc_visited, v) do
        {acc_rest, acc_visited, new_acc_min}
      else
        {[v | acc_rest], MapSet.put(acc_visited, v), new_acc_min}
      end
    end)
    bfs(new_rest, new_visited, adj, new_min)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N + E) where N is the number of cities and E is the number of roads. In the BFS/DFS approach, we visit every node and edge in the connected component at most once. In the Union-Find approach, the complexity is $O(E \cdot \alpha(N))$, where $\alpha$ is the inverse Ackermann function, which is nearly constant for all practical purposes.
- **Space Complexity:** O(N + E) to store the graph as an adjacency list and keep track of visited nodes. In the Union-Find approach, the space complexity is $O(N)$ for the parent and rank arrays, as it doesn't require storing the full adjacency list.
