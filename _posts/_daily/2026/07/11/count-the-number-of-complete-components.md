---
layout: post
title: "Count the Number of Complete Components"
date: 2026-07-11 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Depth-First Search", "Breadth-First Search", "Union-Find", "Graph Theory"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-the-number-of-complete-components/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <queue>\n\nusing namespace std;\n\nclass Solution\
        \ {\npublic:\n    int countCompleteComponents(int n, vector<vector<int>>& edges)\
        \ {\n        vector<vector<int>> adj(n);\n        for (const auto& edge : edges)\
        \ {\n            adj[edge[0]].push_back(edge[1]);\n            adj[edge[1]].push_back(edge[0]);\n\
        \        }\n\n        vector<bool> visited(n, false);\n        int completeComponents\
        \ = 0;\n\n        for (int i = 0; i < n; ++i) {\n            if (!visited[i])\
        \ {\n                int nodeCount = 0;\n                int degSum = 0;\n \
        \               queue<int> q;\n                q.push(i);\n                visited[i]\
        \ = true;\n\n                while (!q.empty()) {\n                    int u\
        \ = q.front();\n                    q.pop();\n                    nodeCount++;\n\
        \                    degSum += adj[u].size();\n                    for (int\
        \ v : adj[u]) {\n                        if (!visited[v]) {\n              \
        \              visited[v] = true;\n                            q.push(v);\n\
        \                        }\n                    }\n                }\n\n   \
        \             if (degSum == (long long)nodeCount * (nodeCount - 1)) {\n    \
        \                completeComponents++;\n                }\n            }\n \
        \       }\n\n        return completeComponents;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int countCompleteComponents(int\
        \ n, int[][] edges) {\n        List<List<Integer>> adj = new ArrayList<>();\n\
        \        for (int i = 0; i < n; i++) {\n            adj.add(new ArrayList<>());\n\
        \        }\n        for (int[] edge : edges) {\n            adj.get(edge[0]).add(edge[1]);\n\
        \            adj.get(edge[1]).add(edge[0]);\n        }\n\n        boolean[]\
        \ visited = new boolean[n];\n        int completeComponents = 0;\n\n       \
        \ for (int i = 0; i < n; i++) {\n            if (!visited[i]) {\n          \
        \      int nodeCount = 0;\n                int degSum = 0;\n               \
        \ Queue<Integer> queue = new LinkedList<>();\n                queue.offer(i);\n\
        \                visited[i] = true;\n\n                while (!queue.isEmpty())\
        \ {\n                    int u = queue.poll();\n                    nodeCount++;\n\
        \                    degSum += adj.get(u).size();\n                    for (int\
        \ v : adj.get(u)) {\n                        if (!visited[v]) {\n          \
        \                  visited[v] = true;\n                            queue.offer(v);\n\
        \                        }\n                    }\n                }\n\n   \
        \             if (degSum == (long) nodeCount * (nodeCount - 1)) {\n        \
        \            completeComponents++;\n                }\n            }\n     \
        \   }\n\n        return completeComponents;\n    }\n}"
      python: "class Solution(object):\n    def countCompleteComponents(self, n, edges):\n\
        \        \"\"\"\n        :type n: int\n        :type edges: List[List[int]]\n\
        \        :rtype: int\n        \"\"\"\n        adj = [[] for _ in range(n)]\n\
        \        for u, v in edges:\n            adj[u].append(v)\n            adj[v].append(u)\n\
        \n        visited = [False] * n\n        complete_count = 0\n\n        for i\
        \ in range(n):\n            if not visited[i]:\n                q = [i]\n  \
        \              visited[i] = True\n                nodes = 0\n              \
        \  deg_sum = 0\n                while q:\n                    u = q.pop(0)\n\
        \                    nodes += 1\n                    deg_sum += len(adj[u])\n\
        \                    for v in adj[u]:\n                        if not visited[v]:\n\
        \                            visited[v] = True\n                           \
        \ q.append(v)\n\n                if deg_sum == nodes * (nodes - 1):\n      \
        \              complete_count += 1\n\n        return complete_count"
      python3: "from typing import List\n\nclass Solution:\n    def countCompleteComponents(self,\
        \ n: int, edges: List[List[int]]) -> int:\n        adj = [[] for _ in range(n)]\n\
        \        for u, v in edges:\n            adj[u].append(v)\n            adj[v].append(u)\n\
        \n        visited = [False] * n\n        complete_count = 0\n\n        for i\
        \ in range(n):\n            if not visited[i]:\n                q = [i]\n  \
        \              visited[i] = True\n                nodes = 0\n              \
        \  deg_sum = 0\n                while q:\n                    u = q.pop(0)\n\
        \                    nodes += 1\n                    deg_sum += len(adj[u])\n\
        \                    for v in adj[u]:\n                        if not visited[v]:\n\
        \                            visited[v] = True\n                           \
        \ q.append(v)\n\n                if deg_sum == nodes * (nodes - 1):\n      \
        \              complete_count += 1\n\n        return complete_count"
      c: "int countCompleteComponents(int n, int** edges, int edgesSize, int* edgesColSize)\
        \ {\n    int adj[50][50];\n    for (int i = 0; i < n; i++) {\n        for (int\
        \ j = 0; j < n; j++) {\n            adj[i][j] = 0;\n        }\n    }\n\n   \
        \ for (int i = 0; i < edgesSize; i++) {\n        int u = edges[i][0];\n    \
        \    int v = edges[i][1];\n        adj[u][v] = 1;\n        adj[v][u] = 1;\n\
        \    }\n\n    int visited[50];\n    for (int i = 0; i < n; i++) {\n        visited[i]\
        \ = 0;\n    }\n\n    int completeCount = 0;\n    for (int i = 0; i < n; i++)\
        \ {\n        if (!visited[i]) {\n            int q[50];\n            int head\
        \ = 0, tail = 0;\n            q[tail++] = i;\n            visited[i] = 1;\n\n\
        \            int nodeCount = 0;\n            int degSum = 0;\n\n           \
        \ while (head < tail) {\n                int u = q[head++];\n              \
        \  nodeCount++;\n                for (int v = 0; v < n; v++) {\n           \
        \         if (adj[u][v]) {\n                        degSum++;\n            \
        \            if (!visited[v]) {\n                            visited[v] = 1;\n\
        \                            q[tail++] = v;\n                        }\n   \
        \                 }\n                }\n            }\n\n            if (degSum\
        \ == nodeCount * (nodeCount - 1)) {\n                completeCount++;\n    \
        \        }\n        }\n    }\n\n    return completeCount;\n}"
      csharp: "public class Solution {\n    public int CountCompleteComponents(int n,\
        \ int[][] edges) {\n        var adj = new System.Collections.Generic.List<int>[n];\n\
        \        for (int i = 0; i < n; i++) adj[i] = new System.Collections.Generic.List<int>();\n\
        \        foreach (var edge in edges) {\n            adj[edge[0]].Add(edge[1]);\n\
        \            adj[edge[1]].Add(edge[0]);\n        }\n\n        bool[] visited\
        \ = new bool[n];\n        int completeCount = 0;\n\n        for (int i = 0;\
        \ i < n; i++) {\n            if (!visited[i]) {\n                int nodes =\
        \ 0;\n                int degreeSum = 0;\n                var stack = new System.Collections.Generic.Stack<int>();\n\
        \                stack.Push(i);\n                visited[i] = true;\n\n    \
        \            while (stack.Count > 0) {\n                    int curr = stack.Pop();\n\
        \                    nodes++;\n                    degreeSum += adj[curr].Count;\n\
        \                    foreach (int neighbor in adj[curr]) {\n               \
        \         if (!visited[neighbor]) {\n                            visited[neighbor]\
        \ = true;\n                            stack.Push(neighbor);\n             \
        \           }\n                    }\n                }\n                if\
        \ (degreeSum == nodes * (nodes - 1)) {\n                    completeCount++;\n\
        \                }\n            }\n        }\n        return completeCount;\n\
        \    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number[][]} edges\n * @return\
        \ {number}\n */\nvar countCompleteComponents = function(n, edges) {\n    const\
        \ adj = Array.from({ length: n }, () => []);\n    for (const [u, v] of edges)\
        \ {\n        adj[u].push(v);\n        adj[v].push(u);\n    }\n\n    const visited\
        \ = new Uint8Array(n);\n    let completeCount = 0;\n\n    for (let i = 0; i\
        \ < n; i++) {\n        if (!visited[i]) {\n            let nodes = 0;\n    \
        \        let degreeSum = 0;\n            const stack = [i];\n            visited[i]\
        \ = 1;\n\n            while (stack.length > 0) {\n                const curr\
        \ = stack.pop();\n                nodes++;\n                degreeSum += adj[curr].length;\n\
        \                for (const neighbor of adj[curr]) {\n                    if\
        \ (!visited[neighbor]) {\n                        visited[neighbor] = 1;\n \
        \                       stack.push(neighbor);\n                    }\n     \
        \           }\n            }\n            if (degreeSum === nodes * (nodes -\
        \ 1)) {\n                completeCount++;\n            }\n        }\n    }\n\
        \    return completeCount;\n};"
      typescript: "function countCompleteComponents(n: number, edges: number[][]): number\
        \ {\n    const adj: number[][] = Array.from({ length: n }, () => []);\n    for\
        \ (const [u, v] of edges) {\n        adj[u].push(v);\n        adj[v].push(u);\n\
        \    }\n\n    const visited: boolean[] = new Array(n).fill(false);\n    let\
        \ completeCount: number = 0;\n\n    for (let i = 0; i < n; i++) {\n        if\
        \ (!visited[i]) {\n            let nodes = 0;\n            let degreeSum = 0;\n\
        \            const stack: number[] = [i];\n            visited[i] = true;\n\n\
        \            while (stack.length > 0) {\n                const curr = stack.pop()!;\n\
        \                nodes++;\n                degreeSum += adj[curr].length;\n\
        \                for (const neighbor of adj[curr]) {\n                    if\
        \ (!visited[neighbor]) {\n                        visited[neighbor] = true;\n\
        \                        stack.push(neighbor);\n                    }\n    \
        \            }\n            }\n            if (degreeSum === nodes * (nodes\
        \ - 1)) {\n                completeCount++;\n            }\n        }\n    }\n\
        \    return completeCount;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @param Integer[][]\
        \ $edges\n     * @return Integer\n     */\n    function countCompleteComponents($n,\
        \ $edges) {\n        $adj = array_fill(0, $n, []);\n        foreach ($edges\
        \ as $edge) {\n            $adj[$edge[0]][] = $edge[1];\n            $adj[$edge[1]][]\
        \ = $edge[0];\n        }\n\n        $visited = array_fill(0, $n, false);\n \
        \       $completeCount = 0;\n\n        for ($i = 0; $i < $n; $i++) {\n     \
        \       if (!$visited[$i]) {\n                $nodes = 0;\n                $degreeSum\
        \ = 0;\n                $stack = [$i];\n                $visited[$i] = true;\n\
        \n                while (!empty($stack)) {\n                    $curr = array_pop($stack);\n\
        \                    $nodes++;\n                    $degreeSum += count($adj[$curr]);\n\
        \                    foreach ($adj[$curr] as $neighbor) {\n                \
        \        if (!$visited[$neighbor]) {\n                            $visited[$neighbor]\
        \ = true;\n                            $stack[] = $neighbor;\n             \
        \           }\n                    }\n                }\n                if\
        \ ($degreeSum === $nodes * ($nodes - 1)) {\n                    $completeCount++;\n\
        \                }\n            }\n        }\n        return $completeCount;\n\
        \    }\n}"
      swift: "class Solution {\n    func countCompleteComponents(_ n: Int, _ edges:\
        \ [[Int]]) -> Int {\n        var adj = [[Int]](repeating: [], count: n)\n  \
        \      for edge in edges {\n            adj[edge[0]].append(edge[1])\n     \
        \       adj[edge[1]].append(edge[0])\n        }\n\n        var visited = [Bool](repeating:\
        \ false, count: n)\n        var completeCount = 0\n\n        for i in 0..<n\
        \ {\n            if !visited[i] {\n                var nodes = 0\n         \
        \       var degreeSum = 0\n                var stack = [i]\n               \
        \ visited[i] = true\n\n                while !stack.isEmpty {\n            \
        \        let curr = stack.removeLast()\n                    nodes += 1\n   \
        \                 degreeSum += adj[curr].count\n                    for neighbor\
        \ in adj[curr] {\n                        if !visited[neighbor] {\n        \
        \                    visited[neighbor] = true\n                            stack.append(neighbor)\n\
        \                        }\n                    }\n                }\n     \
        \           if degreeSum == nodes * (nodes - 1) {\n                    completeCount\
        \ += 1\n                }\n            }\n        }\n        return completeCount\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun countCompleteComponents(n: Int, edges: Array<IntArray>):\
        \ Int {\n        val adj = Array(n) { mutableListOf<Int>() }\n        for (edge\
        \ in edges) {\n            adj[edge[0]].add(edge[1])\n            adj[edge[1]].add(edge[0])\n\
        \        }\n\n        val visited = BooleanArray(n)\n        var count = 0\n\
        \n        for (i in 0 until n) {\n            if (!visited[i]) {\n         \
        \       val component = mutableListOf<Int>()\n                fun dfs(u: Int)\
        \ {\n                    visited[u] = true\n                    component.add(u)\n\
        \                    for (v in adj[u]) {\n                        if (!visited[v])\
        \ {\n                            dfs(v)\n                        }\n       \
        \             }\n                }\n                dfs(i)\n\n             \
        \   val m = component.size\n                var totalDegrees = 0\n         \
        \       for (node in component) {\n                    totalDegrees += adj[node].size\n\
        \                }\n\n                if (totalDegrees == m * (m - 1)) {\n \
        \                   count++\n                }\n            }\n        }\n \
        \       return count\n    }\n}"
      dart: "class Solution {\n  int countCompleteComponents(int n, List<List<int>>\
        \ edges) {\n    List<List<int>> adj = List.generate(n, (_) => []);\n    for\
        \ (var edge in edges) {\n      adj[edge[0]].add(edge[1]);\n      adj[edge[1]].add(edge[0]);\n\
        \    }\n\n    List<bool> visited = List.filled(n, false);\n    int count = 0;\n\
        \n    for (int i = 0; i < n; i++) {\n      if (!visited[i]) {\n        List<int>\
        \ component = [];\n        void dfs(int u) {\n          visited[u] = true;\n\
        \          component.add(u);\n          for (int v in adj[u]) {\n          \
        \  if (!visited[v]) {\n              dfs(v);\n            }\n          }\n \
        \       }\n        dfs(i);\n\n        int m = component.length;\n        int\
        \ totalDegrees = 0;\n        for (int node in component) {\n          totalDegrees\
        \ += adj[node].length;\n        }\n\n        if (totalDegrees == m * (m - 1))\
        \ {\n          count++;\n        }\n      }\n    }\n    return count;\n  }\n\
        }"
      go: "func countCompleteComponents(n int, edges [][]int) int {\n    adj := make([][]int,\
        \ n)\n    for _, edge := range edges {\n        u, v := edge[0], edge[1]\n \
        \       adj[u] = append(adj[u], v)\n        adj[v] = append(adj[v], u)\n   \
        \ }\n\n    visited := make([]bool, n)\n    count := 0\n\n    for i := 0; i <\
        \ n; i++ {\n        if !visited[i] {\n            component := []int{}\n   \
        \         var dfs func(int)\n            dfs = func(u int) {\n             \
        \   visited[u] = true\n                component = append(component, u)\n  \
        \              for _, v := range adj[u] {\n                    if !visited[v]\
        \ {\n                        dfs(v)\n                    }\n               \
        \ }\n            }\n            dfs(i)\n\n            m := len(component)\n\
        \            totalDegrees := 0\n            for _, node := range component {\n\
        \                totalDegrees += len(adj[node])\n            }\n\n         \
        \   if totalDegrees == m*(m-1) {\n                count++\n            }\n \
        \       }\n    }\n    return count\n}"
      ruby: "# @param {Integer} n\n# @param {Integer[][]} edges\n# @return {Integer}\n\
        def count_complete_components(n, edges)\n  adj = Array.new(n) { [] }\n  edges.each\
        \ do |u, v|\n    adj[u] << v\n    adj[v] << u\n  end\n\n  visited = Array.new(n,\
        \ false)\n  count = 0\n\n  (0...n).each do |i|\n    next if visited[i]\n\n \
        \   component = []\n    stack = [i]\n    visited[i] = true\n\n    while !stack.empty?\n\
        \      u = stack.pop\n      component << u\n      adj[u].each do |v|\n     \
        \   unless visited[v]\n          visited[v] = true\n          stack.push(v)\n\
        \        end\n      end\n    end\n\n    m = component.length\n    total_degrees\
        \ = 0\n    component.each do |node|\n      total_degrees += adj[node].length\n\
        \    end\n\n    count += 1 if total_degrees == m * (m - 1)\n  end\n  count\n\
        end"
      scala: "object Solution {\n    def countCompleteComponents(n: Int, edges: Array[Array[Int]]):\
        \ Int = {\n        val adj = Array.fill(n)(scala.collection.mutable.ListBuffer[Int]())\n\
        \        for (edge <- edges) {\n            adj(edge(0)) += edge(1)\n      \
        \      adj(edge(1)) += edge(0)\n        }\n\n        val visited = new Array[Boolean](n)\n\
        \        var count = 0\n\n        for (i <- 0 until n) {\n            if (!visited(i))\
        \ {\n                val component = scala.collection.mutable.ListBuffer[Int]()\n\
        \                def dfs(u: Int): Unit = {\n                    visited(u) =\
        \ true\n                    component += u\n                    for (v <- adj(u))\
        \ {\n                        if (!visited(v)) {\n                          \
        \  dfs(v)\n                        }\n                    }\n              \
        \  }\n                dfs(i)\n\n                val m = component.size\n   \
        \             var totalDegrees = 0\n                for (node <- component)\
        \ {\n                    totalDegrees += adj(node).size\n                }\n\
        \n                if (totalDegrees == m * (m - 1)) {\n                    count\
        \ += 1\n                }\n            }\n        }\n        count\n    }\n}"
      rust: "impl Solution {\n    pub fn count_complete_components(n: i32, edges: Vec<Vec<i32>>)\
        \ -> i32 {\n        let n = n as usize;\n        let mut adj = vec![vec![];\
        \ n];\n        for edge in edges {\n            let u = edge[0] as usize;\n\
        \            let v = edge[1] as usize;\n            adj[u].push(v);\n      \
        \      adj[v].push(u);\n        }\n\n        let mut visited = vec![false; n];\n\
        \        let mut complete_count = 0;\n\n        for i in 0..n {\n          \
        \  if !visited[i] {\n                let mut nodes = 0;\n                let\
        \ mut edges_sum = 0;\n                let mut stack = vec![i];\n           \
        \     visited[i] = true;\n\n                while let Some(u) = stack.pop()\
        \ {\n                    nodes += 1;\n                    edges_sum += adj[u].len();\n\
        \                    for &v in &adj[u] {\n                        if !visited[v]\
        \ {\n                            visited[v] = true;\n                      \
        \      stack.push(v);\n                        }\n                    }\n  \
        \              }\n\n                if edges_sum == nodes * (nodes - 1) {\n\
        \                    complete_count += 1;\n                }\n            }\n\
        \        }\n        complete_count as i32\n    }\n}"
      racket: "(define/contract (count-complete-components n edges)\n  (-> exact-integer?\
        \ (listof (listof exact-integer?)) exact-integer?)\n  (let* ([adj (make-vector\
        \ n '())]\n         [visited (make-vector n #f)])\n    (for ([edge edges])\n\
        \      (let ([u (first edge)]\n            [v (second edge)])\n        (vector-set!\
        \ adj u (cons v (vector-ref adj u)))\n        (vector-set! adj v (cons u (vector-ref\
        \ adj v)))))\n    (letrec ([dfs (lambda (u)\n                    (vector-set!\
        \ visited u #t)\n                    (let ([initial-nodes 1]\n             \
        \             [initial-edges (length (vector-ref adj u))])\n               \
        \       (for/fold ([n-acc initial-nodes]\n                                 [e-acc\
        \ initial-edges])\n                                ([v (vector-ref adj u)])\n\
        \                        (if (vector-ref visited v)\n                      \
        \      (values n-acc e-acc)\n                            (let-values ([(sn se)\
        \ (dfs v)])\n                              (values (+ n-acc sn) (+ e-acc se)))))))])\n\
        \      (for/fold ([complete-count 0])\n                ([i (in-range n)])\n\
        \        (if (vector-ref visited i)\n            complete-count\n          \
        \  (let-values ([(nodes edges-sum) (dfs i)])\n              (if (= edges-sum\
        \ (* nodes (- nodes 1)))\n                  (+ complete-count 1)\n         \
        \         complete-count)))))))"
      erlang: "-spec count_complete_components(N :: integer(), Edges :: [[integer()]])\
        \ -> integer().\ncount_complete_components(N, Edges) ->\n    Adj = lists:foldl(fun([U,\
        \ V], Acc) ->\n        UList = maps:get(U, Acc, []),\n        VList = maps:get(V,\
        \ Acc, []),\n        Acc1 = maps:put(U, [V | UList], Acc),\n        maps:put(V,\
        \ [U | VList], Acc1)\n    end, #{}, Edges),\n    {_, Count} = lists:foldl(fun(I,\
        \ {Visited, Cnt}) ->\n        case sets:is_element(I, Visited) of\n        \
        \    true -> {Visited, Cnt};\n            false ->\n                {Nodes,\
        \ NodeEdges, NewVisited} = dfs(I, Adj, sets:add_element(I, Visited), 0, 0),\n\
        \                NewCnt = case NodeEdges == Nodes * (Nodes - 1) of\n       \
        \             true -> Cnt + 1;\n                    false -> Cnt\n         \
        \       end,\n                {NewVisited, NewCnt}\n        end\n    end, {sets:new(),\
        \ 0}, lists:seq(0, N - 1)),\n    Count.\n\ndfs(U, Adj, Visited, Nodes, Edges)\
        \ ->\n    Neighbors = maps:get(U, Adj, []),\n    lists:foldl(fun(V, {N_acc,\
        \ E_acc, Vst_acc}) ->\n        case sets:is_element(V, Vst_acc) of\n       \
        \     true -> {N_acc, E_acc, Vst_acc};\n            false -> dfs(V, Adj, sets:add_element(V,\
        \ Vst_acc), N_acc, E_acc)\n        end\n    end, {Nodes + 1, Edges + length(Neighbors),\
        \ Visited}, Neighbors)."
      elixir: "defmodule Solution do\n  @spec count_complete_components(n :: integer,\
        \ edges :: [[integer]]) :: integer\n  def count_complete_components(n, edges)\
        \ do\n    adj = Enum.reduce(edges, %{}, fn [u, v], acc ->\n      acc\n     \
        \ |> Map.update(u, [v], &[v | &1])\n      |> Map.update(v, [u], &[u | &1])\n\
        \    end)\n\n    {_visited, count} = Enum.reduce(0..(n - 1), {MapSet.new(),\
        \ 0}, fn i, {visited, cnt} ->\n      if MapSet.member?(visited, i) do\n    \
        \    {visited, cnt}\n      else\n        {nodes, node_edges, new_visited} =\
        \ dfs(i, adj, MapSet.put(visited, i), 0, 0)\n        if node_edges == nodes\
        \ * (nodes - 1) do\n          {new_visited, cnt + 1}\n        else\n       \
        \   {new_visited, cnt}\n        end\n      end\n    end)\n    count\n  end\n\
        \n  defp dfs(u, adj, visited, nodes, edges) do\n    neighbors = Map.get(adj,\
        \ u, [])\n\n    Enum.reduce(neighbors, {nodes + 1, edges + length(neighbors),\
        \ visited}, fn v, {n, e, vst} ->\n      if MapSet.member?(vst, v) do\n     \
        \   {n, e, vst}\n      else\n        dfs(v, adj, MapSet.put(vst, v), n, e)\n\
        \      end\n    end)\n  end\nend"
    approach: 'The algorithm identifies each connected component in the undirected graph
      using a traversal method such as Breadth-First Search (BFS) or Depth-First Search
      (DFS). For each unvisited vertex, it initiates a traversal to discover all nodes
      within that component. During the traversal, we maintain two specific counters
      for the component: the total number of vertices ($V_c$) and the sum of the degrees
      of all those vertices ($D_c$). Since the graph is undirected, each edge within
      the component is counted exactly twice in the degree sum, once for each endpoint.


      A connected component is considered complete if every pair of its vertices is
      connected by an edge. A complete component with $V_c$ vertices must have $V_c(V_c
      - 1) / 2$ unique edges, which is equivalent to saying that the sum of the degrees
      of all its vertices must be $V_c(V_c - 1)$. After a component is fully explored,
      we evaluate this degree sum condition. If it holds true, we increment our count
      of complete components and repeat the process for any remaining unvisited nodes.'
    time_complexity: O(V + E), where V is the number of vertices and E is the number
      of edges. Initializing the adjacency structure takes O(V + E) time, and the subsequent
      BFS/DFS traversals visit each node and its respective edges once. For all components,
      this total traversal time remains O(V + E).
    space_complexity: O(V + E) to store the adjacency list and the visited status of
      each node. The traversal algorithm (BFS or DFS) also requires O(V) space for the
      queue or recursion stack. In the C solution, an adjacency matrix is used, which
      results in O(V^2) space, which is efficient enough for the constraint V ≤ 50.
    elapsed_time: 407.36414790153503
    model: gemini-3-flash-preview
    generated_at: '2026-07-11 02:03:05 '
---

## Problem #2685: Count the Number of Complete Components

**Difficulty:** Medium

**Topics:** Depth-First Search, Breadth-First Search, Union-Find, Graph Theory

## Problem Description

<p>You are given an integer <code>n</code>. There is an <strong>undirected</strong> graph with <code>n</code> vertices, numbered from <code>0</code> to <code>n - 1</code>. You are given a 2D integer array <code>edges</code> where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> denotes that there exists an <strong>undirected</strong> edge connecting vertices <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code>.</p>

<p>Return <em>the number of <strong>complete connected components</strong> of the graph</em>.</p>

<p>A <strong>connected component</strong> is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.</p>

<p>A connected component is said to be <b>complete</b> if there exists an edge between every pair of its vertices.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><strong class="example"><img alt="" src="https://assets.leetcode.com/uploads/2023/04/11/screenshot-from-2023-04-11-23-31-23.png" style="width: 671px; height: 270px;" /></strong></p>

<pre>
<strong>Input:</strong> n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> From the picture above, one can see that all of the components of this graph are complete.
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><strong class="example"><img alt="" src="https://assets.leetcode.com/uploads/2023/04/11/screenshot-from-2023-04-11-23-32-00.png" style="width: 671px; height: 270px;" /></strong></p>

<pre>
<strong>Input:</strong> n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 50</code></li>
	<li><code>0 &lt;= edges.length &lt;= n * (n - 1) / 2</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>There are no repeated edges.</li>
</ul>


## Hints

1. Find the connected components of an undirected graph using depth-first search (DFS) or breadth-first search (BFS).

2. For each connected component, count the number of nodes and edges in the component.

3. A connected component is complete if and only if the number of edges in the component is equal to m*(m-1)/2, where m is the number of nodes in the component.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm identifies each connected component in the undirected graph using a traversal method such as Breadth-First Search (BFS) or Depth-First Search (DFS). For each unvisited vertex, it initiates a traversal to discover all nodes within that component. During the traversal, we maintain two specific counters for the component: the total number of vertices ($V_c$) and the sum of the degrees of all those vertices ($D_c$). Since the graph is undirected, each edge within the component is counted exactly twice in the degree sum, once for each endpoint.

A connected component is considered complete if every pair of its vertices is connected by an edge. A complete component with $V_c$ vertices must have $V_c(V_c - 1) / 2$ unique edges, which is equivalent to saying that the sum of the degrees of all its vertices must be $V_c(V_c - 1)$. After a component is fully explored, we evaluate this degree sum condition. If it holds true, we increment our count of complete components and repeat the process for any remaining unvisited nodes.

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
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        vector<bool> visited(n, false);
        int completeComponents = 0;

        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                int nodeCount = 0;
                int degSum = 0;
                queue<int> q;
                q.push(i);
                visited[i] = true;

                while (!q.empty()) {
                    int u = q.front();
                    q.pop();
                    nodeCount++;
                    degSum += adj[u].size();
                    for (int v : adj[u]) {
                        if (!visited[v]) {
                            visited[v] = true;
                            q.push(v);
                        }
                    }
                }

                if (degSum == (long long)nodeCount * (nodeCount - 1)) {
                    completeComponents++;
                }
            }
        }

        return completeComponents;
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
    public int countCompleteComponents(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        boolean[] visited = new boolean[n];
        int completeComponents = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                int nodeCount = 0;
                int degSum = 0;
                Queue<Integer> queue = new LinkedList<>();
                queue.offer(i);
                visited[i] = true;

                while (!queue.isEmpty()) {
                    int u = queue.poll();
                    nodeCount++;
                    degSum += adj.get(u).size();
                    for (int v : adj.get(u)) {
                        if (!visited[v]) {
                            visited[v] = true;
                            queue.offer(v);
                        }
                    }
                }

                if (degSum == (long) nodeCount * (nodeCount - 1)) {
                    completeComponents++;
                }
            }
        }

        return completeComponents;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        complete_count = 0

        for i in range(n):
            if not visited[i]:
                q = [i]
                visited[i] = True
                nodes = 0
                deg_sum = 0
                while q:
                    u = q.pop(0)
                    nodes += 1
                    deg_sum += len(adj[u])
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            q.append(v)

                if deg_sum == nodes * (nodes - 1):
                    complete_count += 1

        return complete_count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        complete_count = 0

        for i in range(n):
            if not visited[i]:
                q = [i]
                visited[i] = True
                nodes = 0
                deg_sum = 0
                while q:
                    u = q.pop(0)
                    nodes += 1
                    deg_sum += len(adj[u])
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            q.append(v)

                if deg_sum == nodes * (nodes - 1):
                    complete_count += 1

        return complete_count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countCompleteComponents(int n, int** edges, int edgesSize, int* edgesColSize) {
    int adj[50][50];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            adj[i][j] = 0;
        }
    }

    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u][v] = 1;
        adj[v][u] = 1;
    }

    int visited[50];
    for (int i = 0; i < n; i++) {
        visited[i] = 0;
    }

    int completeCount = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            int q[50];
            int head = 0, tail = 0;
            q[tail++] = i;
            visited[i] = 1;

            int nodeCount = 0;
            int degSum = 0;

            while (head < tail) {
                int u = q[head++];
                nodeCount++;
                for (int v = 0; v < n; v++) {
                    if (adj[u][v]) {
                        degSum++;
                        if (!visited[v]) {
                            visited[v] = 1;
                            q[tail++] = v;
                        }
                    }
                }
            }

            if (degSum == nodeCount * (nodeCount - 1)) {
                completeCount++;
            }
        }
    }

    return completeCount;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountCompleteComponents(int n, int[][] edges) {
        var adj = new System.Collections.Generic.List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new System.Collections.Generic.List<int>();
        foreach (var edge in edges) {
            adj[edge[0]].Add(edge[1]);
            adj[edge[1]].Add(edge[0]);
        }

        bool[] visited = new bool[n];
        int completeCount = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                int nodes = 0;
                int degreeSum = 0;
                var stack = new System.Collections.Generic.Stack<int>();
                stack.Push(i);
                visited[i] = true;

                while (stack.Count > 0) {
                    int curr = stack.Pop();
                    nodes++;
                    degreeSum += adj[curr].Count;
                    foreach (int neighbor in adj[curr]) {
                        if (!visited[neighbor]) {
                            visited[neighbor] = true;
                            stack.Push(neighbor);
                        }
                    }
                }
                if (degreeSum == nodes * (nodes - 1)) {
                    completeCount++;
                }
            }
        }
        return completeCount;
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
 * @return {number}
 */
var countCompleteComponents = function(n, edges) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const visited = new Uint8Array(n);
    let completeCount = 0;

    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            let nodes = 0;
            let degreeSum = 0;
            const stack = [i];
            visited[i] = 1;

            while (stack.length > 0) {
                const curr = stack.pop();
                nodes++;
                degreeSum += adj[curr].length;
                for (const neighbor of adj[curr]) {
                    if (!visited[neighbor]) {
                        visited[neighbor] = 1;
                        stack.push(neighbor);
                    }
                }
            }
            if (degreeSum === nodes * (nodes - 1)) {
                completeCount++;
            }
        }
    }
    return completeCount;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countCompleteComponents(n: number, edges: number[][]): number {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const visited: boolean[] = new Array(n).fill(false);
    let completeCount: number = 0;

    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            let nodes = 0;
            let degreeSum = 0;
            const stack: number[] = [i];
            visited[i] = true;

            while (stack.length > 0) {
                const curr = stack.pop()!;
                nodes++;
                degreeSum += adj[curr].length;
                for (const neighbor of adj[curr]) {
                    if (!visited[neighbor]) {
                        visited[neighbor] = true;
                        stack.push(neighbor);
                    }
                }
            }
            if (degreeSum === nodes * (nodes - 1)) {
                completeCount++;
            }
        }
    }
    return completeCount;
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
     * @param Integer[][] $edges
     * @return Integer
     */
    function countCompleteComponents($n, $edges) {
        $adj = array_fill(0, $n, []);
        foreach ($edges as $edge) {
            $adj[$edge[0]][] = $edge[1];
            $adj[$edge[1]][] = $edge[0];
        }

        $visited = array_fill(0, $n, false);
        $completeCount = 0;

        for ($i = 0; $i < $n; $i++) {
            if (!$visited[$i]) {
                $nodes = 0;
                $degreeSum = 0;
                $stack = [$i];
                $visited[$i] = true;

                while (!empty($stack)) {
                    $curr = array_pop($stack);
                    $nodes++;
                    $degreeSum += count($adj[$curr]);
                    foreach ($adj[$curr] as $neighbor) {
                        if (!$visited[$neighbor]) {
                            $visited[$neighbor] = true;
                            $stack[] = $neighbor;
                        }
                    }
                }
                if ($degreeSum === $nodes * ($nodes - 1)) {
                    $completeCount++;
                }
            }
        }
        return $completeCount;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countCompleteComponents(_ n: Int, _ edges: [[Int]]) -> Int {
        var adj = [[Int]](repeating: [], count: n)
        for edge in edges {
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        }

        var visited = [Bool](repeating: false, count: n)
        var completeCount = 0

        for i in 0..<n {
            if !visited[i] {
                var nodes = 0
                var degreeSum = 0
                var stack = [i]
                visited[i] = true

                while !stack.isEmpty {
                    let curr = stack.removeLast()
                    nodes += 1
                    degreeSum += adj[curr].count
                    for neighbor in adj[curr] {
                        if !visited[neighbor] {
                            visited[neighbor] = true
                            stack.append(neighbor)
                        }
                    }
                }
                if degreeSum == nodes * (nodes - 1) {
                    completeCount += 1
                }
            }
        }
        return completeCount
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countCompleteComponents(n: Int, edges: Array<IntArray>): Int {
        val adj = Array(n) { mutableListOf<Int>() }
        for (edge in edges) {
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
        }

        val visited = BooleanArray(n)
        var count = 0

        for (i in 0 until n) {
            if (!visited[i]) {
                val component = mutableListOf<Int>()
                fun dfs(u: Int) {
                    visited[u] = true
                    component.add(u)
                    for (v in adj[u]) {
                        if (!visited[v]) {
                            dfs(v)
                        }
                    }
                }
                dfs(i)

                val m = component.size
                var totalDegrees = 0
                for (node in component) {
                    totalDegrees += adj[node].size
                }

                if (totalDegrees == m * (m - 1)) {
                    count++
                }
            }
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int countCompleteComponents(int n, List<List<int>> edges) {
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var edge in edges) {
      adj[edge[0]].add(edge[1]);
      adj[edge[1]].add(edge[0]);
    }

    List<bool> visited = List.filled(n, false);
    int count = 0;

    for (int i = 0; i < n; i++) {
      if (!visited[i]) {
        List<int> component = [];
        void dfs(int u) {
          visited[u] = true;
          component.add(u);
          for (int v in adj[u]) {
            if (!visited[v]) {
              dfs(v);
            }
          }
        }
        dfs(i);

        int m = component.length;
        int totalDegrees = 0;
        for (int node in component) {
          totalDegrees += adj[node].length;
        }

        if (totalDegrees == m * (m - 1)) {
          count++;
        }
      }
    }
    return count;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func countCompleteComponents(n int, edges [][]int) int {
    adj := make([][]int, n)
    for _, edge := range edges {
        u, v := edge[0], edge[1]
        adj[u] = append(adj[u], v)
        adj[v] = append(adj[v], u)
    }

    visited := make([]bool, n)
    count := 0

    for i := 0; i < n; i++ {
        if !visited[i] {
            component := []int{}
            var dfs func(int)
            dfs = func(u int) {
                visited[u] = true
                component = append(component, u)
                for _, v := range adj[u] {
                    if !visited[v] {
                        dfs(v)
                    }
                }
            }
            dfs(i)

            m := len(component)
            totalDegrees := 0
            for _, node := range component {
                totalDegrees += len(adj[node])
            }

            if totalDegrees == m*(m-1) {
                count++
            }
        }
    }
    return count
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def count_complete_components(n, edges)
  adj = Array.new(n) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  visited = Array.new(n, false)
  count = 0

  (0...n).each do |i|
    next if visited[i]

    component = []
    stack = [i]
    visited[i] = true

    while !stack.empty?
      u = stack.pop
      component << u
      adj[u].each do |v|
        unless visited[v]
          visited[v] = true
          stack.push(v)
        end
      end
    end

    m = component.length
    total_degrees = 0
    component.each do |node|
      total_degrees += adj[node].length
    end

    count += 1 if total_degrees == m * (m - 1)
  end
  count
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countCompleteComponents(n: Int, edges: Array[Array[Int]]): Int = {
        val adj = Array.fill(n)(scala.collection.mutable.ListBuffer[Int]())
        for (edge <- edges) {
            adj(edge(0)) += edge(1)
            adj(edge(1)) += edge(0)
        }

        val visited = new Array[Boolean](n)
        var count = 0

        for (i <- 0 until n) {
            if (!visited(i)) {
                val component = scala.collection.mutable.ListBuffer[Int]()
                def dfs(u: Int): Unit = {
                    visited(u) = true
                    component += u
                    for (v <- adj(u)) {
                        if (!visited(v)) {
                            dfs(v)
                        }
                    }
                }
                dfs(i)

                val m = component.size
                var totalDegrees = 0
                for (node <- component) {
                    totalDegrees += adj(node).size
                }

                if (totalDegrees == m * (m - 1)) {
                    count += 1
                }
            }
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_complete_components(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut adj = vec![vec![]; n];
        for edge in edges {
            let u = edge[0] as usize;
            let v = edge[1] as usize;
            adj[u].push(v);
            adj[v].push(u);
        }

        let mut visited = vec![false; n];
        let mut complete_count = 0;

        for i in 0..n {
            if !visited[i] {
                let mut nodes = 0;
                let mut edges_sum = 0;
                let mut stack = vec![i];
                visited[i] = true;

                while let Some(u) = stack.pop() {
                    nodes += 1;
                    edges_sum += adj[u].len();
                    for &v in &adj[u] {
                        if !visited[v] {
                            visited[v] = true;
                            stack.push(v);
                        }
                    }
                }

                if edges_sum == nodes * (nodes - 1) {
                    complete_count += 1;
                }
            }
        }
        complete_count as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (count-complete-components n edges)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ([adj (make-vector n '())]
         [visited (make-vector n #f)])
    (for ([edge edges])
      (let ([u (first edge)]
            [v (second edge)])
        (vector-set! adj u (cons v (vector-ref adj u)))
        (vector-set! adj v (cons u (vector-ref adj v)))))
    (letrec ([dfs (lambda (u)
                    (vector-set! visited u #t)
                    (let ([initial-nodes 1]
                          [initial-edges (length (vector-ref adj u))])
                      (for/fold ([n-acc initial-nodes]
                                 [e-acc initial-edges])
                                ([v (vector-ref adj u)])
                        (if (vector-ref visited v)
                            (values n-acc e-acc)
                            (let-values ([(sn se) (dfs v)])
                              (values (+ n-acc sn) (+ e-acc se)))))))])
      (for/fold ([complete-count 0])
                ([i (in-range n)])
        (if (vector-ref visited i)
            complete-count
            (let-values ([(nodes edges-sum) (dfs i)])
              (if (= edges-sum (* nodes (- nodes 1)))
                  (+ complete-count 1)
                  complete-count)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec count_complete_components(N :: integer(), Edges :: [[integer()]]) -> integer().
count_complete_components(N, Edges) ->
    Adj = lists:foldl(fun([U, V], Acc) ->
        UList = maps:get(U, Acc, []),
        VList = maps:get(V, Acc, []),
        Acc1 = maps:put(U, [V | UList], Acc),
        maps:put(V, [U | VList], Acc1)
    end, #{}, Edges),
    {_, Count} = lists:foldl(fun(I, {Visited, Cnt}) ->
        case sets:is_element(I, Visited) of
            true -> {Visited, Cnt};
            false ->
                {Nodes, NodeEdges, NewVisited} = dfs(I, Adj, sets:add_element(I, Visited), 0, 0),
                NewCnt = case NodeEdges == Nodes * (Nodes - 1) of
                    true -> Cnt + 1;
                    false -> Cnt
                end,
                {NewVisited, NewCnt}
        end
    end, {sets:new(), 0}, lists:seq(0, N - 1)),
    Count.

dfs(U, Adj, Visited, Nodes, Edges) ->
    Neighbors = maps:get(U, Adj, []),
    lists:foldl(fun(V, {N_acc, E_acc, Vst_acc}) ->
        case sets:is_element(V, Vst_acc) of
            true -> {N_acc, E_acc, Vst_acc};
            false -> dfs(V, Adj, sets:add_element(V, Vst_acc), N_acc, E_acc)
        end
    end, {Nodes + 1, Edges + length(Neighbors), Visited}, Neighbors).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_complete_components(n :: integer, edges :: [[integer]]) :: integer
  def count_complete_components(n, edges) do
    adj = Enum.reduce(edges, %{}, fn [u, v], acc ->
      acc
      |> Map.update(u, [v], &[v | &1])
      |> Map.update(v, [u], &[u | &1])
    end)

    {_visited, count} = Enum.reduce(0..(n - 1), {MapSet.new(), 0}, fn i, {visited, cnt} ->
      if MapSet.member?(visited, i) do
        {visited, cnt}
      else
        {nodes, node_edges, new_visited} = dfs(i, adj, MapSet.put(visited, i), 0, 0)
        if node_edges == nodes * (nodes - 1) do
          {new_visited, cnt + 1}
        else
          {new_visited, cnt}
        end
      end
    end)
    count
  end

  defp dfs(u, adj, visited, nodes, edges) do
    neighbors = Map.get(adj, u, [])

    Enum.reduce(neighbors, {nodes + 1, edges + length(neighbors), visited}, fn v, {n, e, vst} ->
      if MapSet.member?(vst, v) do
        {n, e, vst}
      else
        dfs(v, adj, MapSet.put(vst, v), n, e)
      end
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(V + E), where V is the number of vertices and E is the number of edges. Initializing the adjacency structure takes O(V + E) time, and the subsequent BFS/DFS traversals visit each node and its respective edges once. For all components, this total traversal time remains O(V + E).
- **Space Complexity:** O(V + E) to store the adjacency list and the visited status of each node. The traversal algorithm (BFS or DFS) also requires O(V) space for the queue or recursion stack. In the C solution, an adjacency matrix is used, which results in O(V^2) space, which is efficient enough for the constraint V ≤ 50.
