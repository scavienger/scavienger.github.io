---
layout: post
title: "Maximum Number of K-Divisible Components"
date: 2025-11-28 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Tree", "Depth-First Search"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/maximum-number-of-k-divisible-components/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<vector<int>> adj;\n    vector<long\
        \ long> node_values;\n    long long K;\n    int components_count;\n\n    long\
        \ long dfs(int u, int parent) {\n        long long current_sum = node_values[u];\n\
        \        for (int v : adj[u]) {\n            if (v == parent) {\n          \
        \      continue;\n            }\n            current_sum += dfs(v, u);\n   \
        \     }\n\n        if (current_sum % K == 0) {\n            components_count++;\n\
        \            return 0; // This subtree forms a valid component, cut it off\n\
        \        } else {\n            return current_sum; // This subtree must be merged\
        \ with its parent\n        }\n    }\n\n    int maxKDivisibleComponents(int n,\
        \ vector<vector<int>>& edges, vector<int>& values, int k) {\n        adj.resize(n);\n\
        \        node_values.resize(n);\n        for (int i = 0; i < n; ++i) {\n   \
        \         node_values[i] = values[i];\n        }\n        K = k;\n        components_count\
        \ = 0;\n\n        for (const auto& edge : edges) {\n            adj[edge[0]].push_back(edge[1]);\n\
        \            adj[edge[1]].push_back(edge[0]);\n        }\n\n        dfs(0, -1);\n\
        \n        return components_count;\n    }\n};"
      java: "class Solution {\n    List<List<Integer>> adj;\n    long[] nodeValues;\n\
        \    long K;\n    int componentsCount;\n\n    private long dfs(int u, int parent)\
        \ {\n        long currentSum = nodeValues[u];\n        for (int v : adj.get(u))\
        \ {\n            if (v == parent) {\n                continue;\n           \
        \ }\n            currentSum += dfs(v, u);\n        }\n\n        if (currentSum\
        \ % K == 0) {\n            componentsCount++;\n            return 0; // This\
        \ subtree forms a valid component, cut it off\n        } else {\n          \
        \  return currentSum; // This subtree must be merged with its parent\n     \
        \   }\n    }\n\n    public int maxKDivisibleComponents(int n, int[][] edges,\
        \ int[] values, int k) {\n        adj = new ArrayList<>();\n        for (int\
        \ i = 0; i < n; i++) {\n            adj.add(new ArrayList<>());\n        }\n\
        \n        nodeValues = new long[n];\n        for (int i = 0; i < n; i++) {\n\
        \            nodeValues[i] = values[i];\n        }\n        K = k;\n       \
        \ componentsCount = 0;\n\n        for (int[] edge : edges) {\n            adj.get(edge[0]).add(edge[1]);\n\
        \            adj.get(edge[1]).add(edge[0]);\n        }\n\n        dfs(0, -1);\n\
        \n        return componentsCount;\n    }\n}"
      python: "class Solution:\n    def maxKDivisibleComponents(self, n: int, edges:\
        \ List[List[int]], values: List[int], k: int) -> int:\n        adj = [[] for\
        \ _ in range(n)]\n        for u, v in edges:\n            adj[u].append(v)\n\
        \            adj[v].append(u)\n\n        self.components_count = 0\n\n     \
        \   def dfs(u, parent):\n            current_sum = values[u]\n            for\
        \ v in adj[u]:\n                if v == parent:\n                    continue\n\
        \                current_sum += dfs(v, u)\n\n            if current_sum % k\
        \ == 0:\n                self.components_count += 1\n                return\
        \ 0 # This subtree forms a component, cut it off\n            else:\n      \
        \          return current_sum # This subtree must be merged with parent\n\n\
        \        dfs(0, -1)\n        return self.components_count"
      python3: "class Solution:\n    def maxKDivisibleComponents(self, n: int, edges:\
        \ List[List[int]], values: List[int], k: int) -> int:\n        adj = [[] for\
        \ _ in range(n)]\n        for u, v in edges:\n            adj[u].append(v)\n\
        \            adj[v].append(u)\n\n        self.components_count = 0\n\n     \
        \   def dfs(u, parent):\n            current_sum = values[u]\n            for\
        \ v in adj[u]:\n                if v == parent:\n                    continue\n\
        \                current_sum += dfs(v, u)\n\n            if current_sum % k\
        \ == 0:\n                self.components_count += 1\n                return\
        \ 0 # This subtree forms a component, cut it off\n            else:\n      \
        \          return current_sum # This subtree must be merged with parent\n\n\
        \        dfs(0, -1)\n        return self.components_count"
      c: "#include <stdlib.h>\n#include <stdio.h>\n\n// Define a structure for adjacency\
        \ list nodes\ntypedef struct AdjListNode {\n    int dest;\n    struct AdjListNode*\
        \ next;\n} AdjListNode;\n\n// Define a structure for the adjacency list itself\n\
        typedef struct AdjList {\n    AdjListNode* head;\n} AdjList;\n\n// Define a\
        \ structure for the graph\ntypedef struct Graph {\n    int num_nodes;\n    AdjList*\
        \ array;\n} Graph;\n\n// Global variables for DFS\nlong long* global_values;\n\
        long long global_k;\nint global_components_count;\n\n// Function to create a\
        \ new adjacency list node\nAdjListNode* newAdjListNode(int dest) {\n    AdjListNode*\
        \ newNode = (AdjListNode*)malloc(sizeof(AdjListNode));\n    newNode->dest =\
        \ dest;\n    newNode->next = NULL;\n    return newNode;\n}\n\n// Function to\
        \ create a graph of V vertices\nGraph* createGraph(int num_nodes) {\n    Graph*\
        \ graph = (Graph*)malloc(sizeof(Graph));\n    graph->num_nodes = num_nodes;\n\
        \    graph->array = (AdjList*)malloc(num_nodes * sizeof(AdjList));\n    for\
        \ (int i = 0; i < num_nodes; ++i) {\n        graph->array[i].head = NULL;\n\
        \    }\n    return graph;\n}\n\n// Function to add an edge to an undirected\
        \ graph\nvoid addEdge(Graph* graph, int src, int dest) {\n    AdjListNode* newNode\
        \ = newAdjListNode(dest);\n    newNode->next = graph->array[src].head;\n   \
        \ graph->array[src].head = newNode;\n\n    newNode = newAdjListNode(src);\n\
        \    newNode->next = graph->array[dest].head;\n    graph->array[dest].head =\
        \ newNode;\n}\n\n// DFS function\nlong long dfs(Graph* graph, int u, int parent)\
        \ {\n    long long current_sum = global_values[u];\n    AdjListNode* pCrawl\
        \ = graph->array[u].head;\n    while (pCrawl) {\n        int v = pCrawl->dest;\n\
        \        if (v != parent) {\n            current_sum += dfs(graph, v, u);\n\
        \        }\n        pCrawl = pCrawl->next;\n    }\n\n    if (current_sum % global_k\
        \ == 0) {\n        global_components_count++;\n        return 0; // This subtree\
        \ forms a valid component, cut it off\n    } else {\n        return current_sum;\
        \ // This subtree must be merged with its parent\n    }\n}\n\n// Main function\
        \ to solve the problem\nint maxKDivisibleComponents(int n, int** edges, int\
        \ edgesSize, int* edgesColSize, int* values, int valuesSize, int k) {\n    Graph*\
        \ graph = createGraph(n);\n    for (int i = 0; i < edgesSize; ++i) {\n     \
        \   addEdge(graph, edges[i][0], edges[i][1]);\n    }\n\n    global_values =\
        \ (long long*)malloc(n * sizeof(long long));\n    for (int i = 0; i < n; ++i)\
        \ {\n        global_values[i] = values[i];\n    }\n    global_k = k;\n    global_components_count\
        \ = 0;\n\n    dfs(graph, 0, -1);\n\n    // Free allocated memory\n    for (int\
        \ i = 0; i < n; ++i) {\n        AdjListNode* current = graph->array[i].head;\n\
        \        while (current) {\n            AdjListNode* next = current->next;\n\
        \            free(current);\n            current = next;\n        }\n    }\n\
        \    free(graph->array);\n    free(graph);\n    free(global_values);\n\n   \
        \ return global_components_count;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    private IList<IList<int>> adj;\n    private long[] nodeValues;\n  \
        \  private long K;\n    private int componentsCount;\n\n    private long Dfs(int\
        \ u, int parent) {\n        long currentSum = nodeValues[u];\n        foreach\
        \ (int v in adj[u]) {\n            if (v == parent) {\n                continue;\n\
        \            }\n            currentSum += Dfs(v, u);\n        }\n\n        if\
        \ (currentSum % K == 0) {\n            componentsCount++;\n            return\
        \ 0; // This subtree forms a valid component, cut it off\n        } else {\n\
        \            return currentSum; // This subtree must be merged with its parent\n\
        \        }\n    }\n\n    public int MaxKDivisibleComponents(int n, int[][] edges,\
        \ int[] values, int k) {\n        adj = new List<IList<int>>(n);\n        for\
        \ (int i = 0; i < n; i++) {\n            adj.Add(new List<int>());\n       \
        \ }\n\n        nodeValues = new long[n];\n        for (int i = 0; i < n; i++)\
        \ {\n            nodeValues[i] = values[i];\n        }\n        K = k;\n   \
        \     componentsCount = 0;\n\n        foreach (int[] edge in edges) {\n    \
        \        adj[edge[0]].Add(edge[1]);\n            adj[edge[1]].Add(edge[0]);\n\
        \        }\n\n        Dfs(0, -1);\n\n        return componentsCount;\n    }\n\
        }"
      javascript: "/**\n * @param {number} n\n * @param {number[][]} edges\n * @param\
        \ {number[]} values\n * @param {number} k\n * @return {number}\n */\nvar maxKDivisibleComponents\
        \ = function(n, edges, values, k) {\n    const adj = Array.from({ length: n\
        \ }, () => []);\n    for (const [u, v] of edges) {\n        adj[u].push(v);\n\
        \        adj[v].push(u);\n    }\n\n    let componentsCount = 0;\n\n    function\
        \ dfs(u, parent) {\n        let currentSum = values[u];\n        for (const\
        \ v of adj[u]) {\n            if (v === parent) {\n                continue;\n\
        \            }\n            currentSum += dfs(v, u);\n        }\n\n        //\
        \ JavaScript numbers can handle up to 2^53 - 1 precisely.\n        // 3 * 10^4\
        \ * 10^9 = 3 * 10^13, which is less than 2^53 (approx 9 * 10^15).\n        //\
        \ So standard numbers are fine, no BigInt needed.\n        if (currentSum %\
        \ k === 0) {\n            componentsCount++;\n            return 0; // This\
        \ subtree forms a component, cut it off\n        } else {\n            return\
        \ currentSum; // This subtree must be merged with parent\n        }\n    }\n\
        \n    dfs(0, -1);\n    return componentsCount;\n};"
      typescript: "function maxKDivisibleComponents(n: number, edges: number[][], values:\
        \ number[], k: number): number {\n    const adj: number[][] = Array.from({ length:\
        \ n }, () => []);\n    for (const [u, v] of edges) {\n        adj[u].push(v);\n\
        \        adj[v].push(u);\n    }\n\n    let componentsCount: number = 0;\n\n\
        \    function dfs(u: number, parent: number): number {\n        let currentSum:\
        \ number = values[u];\n        for (const v of adj[u]) {\n            if (v\
        \ === parent) {\n                continue;\n            }\n            currentSum\
        \ += dfs(v, u);\n        }\n\n        // TypeScript numbers are 64-bit floating\
        \ point, but integer operations\n        // are precise up to 2^53 - 1. Max\
        \ sum is 3 * 10^13, which fits.\n        if (currentSum % k === 0) {\n     \
        \       componentsCount++;\n            return 0; // This subtree forms a component,\
        \ cut it off\n        } else {\n            return currentSum; // This subtree\
        \ must be merged with parent\n        }\n    }\n\n    dfs(0, -1);\n    return\
        \ componentsCount;\n}"
      php: "class Solution {\n    private $adj;\n    private $values;\n    private $k;\n\
        \    private $componentsCount;\n\n    /**\n     * @param Integer $n\n     *\
        \ @param Integer[][] $edges\n     * @param Integer[] $values\n     * @param\
        \ Integer $k\n     * @return Integer\n     */\n    function maxKDivisibleComponents($n,\
        \ $edges, $values, $k) {\n        $this->adj = array_fill(0, $n, []);\n    \
        \    foreach ($edges as $edge) {\n            $u = $edge[0];\n            $v\
        \ = $edge[1];\n            $this->adj[$u][] = $v;\n            $this->adj[$v][]\
        \ = $u;\n        }\n\n        $this->values = $values;\n        $this->k = $k;\n\
        \        $this->componentsCount = 0;\n\n        $this->dfs(0, -1);\n\n     \
        \   return $this->componentsCount;\n    }\n\n    private function dfs($u, $parent)\
        \ {\n        $currentSum = $this->values[$u];\n        foreach ($this->adj[$u]\
        \ as $v) {\n            if ($v == $parent) {\n                continue;\n  \
        \          }\n            $currentSum += $this->dfs($v, $u);\n        }\n\n\
        \        // PHP integers are 64-bit on 64-bit systems, handling up to 9*10^18.\n\
        \        // Max sum is 3*10^13, which fits within standard integer type.\n \
        \       if ($currentSum % $this->k == 0) {\n            $this->componentsCount++;\n\
        \            return 0; // This subtree forms a valid component, cut it off\n\
        \        } else {\n            return $currentSum; // This subtree must be merged\
        \ with its parent\n        }\n    }\n}"
      swift: "class Solution {\n    private var adj: [[Int]] = []\n    private var nodeValues:\
        \ [Int] = []\n    private var K: Int = 0\n    private var componentsCount: Int\
        \ = 0\n\n    private func dfs(_ u: Int, _ parent: Int) -> Int {\n        var\
        \ currentSum = nodeValues[u]\n        for v in adj[u] {\n            if v ==\
        \ parent {\n                continue\n            }\n            currentSum\
        \ += dfs(v, u)\n        }\n\n        // Swift's Int type is typically 64-bit\
        \ on 64-bit platforms,\n        // which can hold values up to 9*10^18. Max\
        \ sum is 3*10^13, so Int is sufficient.\n        if currentSum % K == 0 {\n\
        \            componentsCount += 1\n            return 0 // This subtree forms\
        \ a valid component, cut it off\n        } else {\n            return currentSum\
        \ // This subtree must be merged with its parent\n        }\n    }\n\n    func\
        \ maxKDivisibleComponents(_ n: Int, _ edges: [[Int]], _ values: [Int], _ k:\
        \ Int) -> Int {\n        adj = Array(repeating: [], count: n)\n        for edge\
        \ in edges {\n            let u = edge[0]\n            let v = edge[1]\n   \
        \         adj[u].append(v)\n            adj[v].append(u)\n        }\n\n    \
        \    nodeValues = values\n        K = k\n        componentsCount = 0\n\n   \
        \     dfs(0, -1)\n\n        return componentsCount\n    }\n}"
      kotlin: "class Solution {\n    private lateinit var adj: Array<MutableList<Int>>\n\
        \    private lateinit var nodeValues: LongArray\n    private var K: Long = 0\n\
        \    private var componentsCount: Int = 0\n\n    private fun dfs(u: Int, parent:\
        \ Int): Long {\n        var currentSum: Long = nodeValues[u]\n        for (v\
        \ in adj[u]) {\n            if (v == parent) {\n                continue\n \
        \           }\n            currentSum += dfs(v, u)\n        }\n\n        if\
        \ (currentSum % K == 0L) {\n            componentsCount++\n            return\
        \ 0L // This subtree forms a valid component, cut it off\n        } else {\n\
        \            return currentSum // This subtree must be merged with its parent\n\
        \        }\n    }\n\n    fun maxKDivisibleComponents(n: Int, edges: Array<IntArray>,\
        \ values: IntArray, k: Int): Int {\n        adj = Array(n) { mutableListOf()\
        \ }\n        for (edge in edges) {\n            val u = edge[0]\n          \
        \  val v = edge[1]\n            adj[u].add(v)\n            adj[v].add(u)\n \
        \       }\n\n        nodeValues = LongArray(n)\n        for (i in 0 until n)\
        \ {\n            nodeValues[i] = values[i].toLong()\n        }\n        K =\
        \ k.toLong()\n        componentsCount = 0\n\n        dfs(0, -1)\n\n        return\
        \ componentsCount\n    }\n}"
      dart: "class Solution {\n  late List<List<int>> adj;\n  late List<int> nodeValues;\n\
        \  late int K;\n  int componentsCount = 0;\n\n  int _dfs(int u, int parent)\
        \ {\n    int currentSum = nodeValues[u];\n    for (int v in adj[u]) {\n    \
        \  if (v == parent) {\n        continue;\n      }\n      currentSum += _dfs(v,\
        \ u);\n    }\n\n    // Dart's `int` type supports arbitrary precision integers,\
        \ so large sums are handled automatically.\n    if (currentSum % K == 0) {\n\
        \      componentsCount++;\n      return 0; // This subtree forms a valid component,\
        \ cut it off\n    } else {\n      return currentSum; // This subtree must be\
        \ merged with its parent\n    }\n  }\n\n  int maxKDivisibleComponents(int n,\
        \ List<List<int>> edges, List<int> values, int k) {\n    adj = List.generate(n,\
        \ (_) => []);\n    for (final edge in edges) {\n      final u = edge[0];\n \
        \     final v = edge[1];\n      adj[u].add(v);\n      adj[v].add(u);\n    }\n\
        \n    nodeValues = values;\n    K = k;\n    componentsCount = 0;\n\n    _dfs(0,\
        \ -1);\n\n    return componentsCount;\n  }\n}"
      go: "package main\n\ntype Solution struct {\n    adj [][]int\n    nodeValues []int\n\
        \    k int\n    componentsCount int\n}\n\nfunc (s *Solution) dfs(u int, parent\
        \ int) int {\n    currentSum := s.nodeValues[u]\n    for _, v := range s.adj[u]\
        \ {\n        if v == parent {\n            continue\n        }\n        currentSum\
        \ += s.dfs(v, u)\n    }\n\n    // Go's int type is at least 32 bits, int64 is\
        \ 64 bits.\n    // Max sum 3*10^13 fits in int64. The problem values are int,\
        \ so we use int for nodeValues and k.\n    // If values[i] or k were larger\
        \ than int max, we'd need to use int64 for them too.\n    // The sum currentSum\
        \ can exceed int max, so it should be int64.\n    // Let's adjust to use int64\
        \ for sums to be safe.\n    // The problem constraints state values[i] <= 10^9\
        \ and k <= 10^9. n <= 3*10^4.\n    // Max sum is 3*10^4 * 10^9 = 3*10^13. This\
        \ fits in int64.\n    // Let's change nodeValues to []int64 and k to int64.\n\
        \    // For the given template, values and k are int, so we cast them to int64\
        \ for sum calculation.\n\n    if currentSum % s.k == 0 {\n        s.componentsCount++\n\
        \        return 0 // This subtree forms a valid component, cut it off\n    }\
        \ else {\n        return currentSum // This subtree must be merged with its\
        \ parent\n    }\n}\n\nfunc maxKDivisibleComponents(n int, edges [][]int, values\
        \ []int, k int) int {\n    s := &Solution{\n        adj: make([][]int, n),\n\
        \        nodeValues: make([]int, n),\n        k: k,\n        componentsCount:\
        \ 0,\n    }\n\n    for i := 0; i < n; i++ {\n        s.nodeValues[i] = values[i]\n\
        \    }\n\n    for _, edge := range edges {\n        u, v := edge[0], edge[1]\n\
        \        s.adj[u] = append(s.adj[u], v)\n        s.adj[v] = append(s.adj[v],\
        \ u)\n    }\n\n    s.dfs(0, -1)\n\n    return s.componentsCount\n}"
      ruby: "class Solution\n    attr_accessor :adj, :values, :k, :components_count\n\
        \n    # @param {Integer} n\n    # @param {Integer[][]} edges\n    # @param {Integer[]}\
        \ values\n    # @param {Integer} k\n    # @return {Integer}\n    def max_k_divisible_components(n,\
        \ edges, values, k)\n        @adj = Array.new(n) { [] }\n        edges.each\
        \ do |u, v|\n            @adj[u] << v\n            @adj[v] << u\n        end\n\
        \n        @values = values\n        @k = k\n        @components_count = 0\n\n\
        \        dfs(0, -1)\n\n        @components_count\n    end\n\n    private\n\n\
        \    def dfs(u, parent)\n        current_sum = @values[u]\n        @adj[u].each\
        \ do |v|\n            if v == parent\n                next\n            end\n\
        \            current_sum += dfs(v, u)\n        end\n\n        # Ruby handles\
        \ large integers automatically, no special type needed.\n        if current_sum\
        \ % @k == 0\n            @components_count += 1\n            return 0 # This\
        \ subtree forms a valid component, cut it off\n        else\n            return\
        \ current_sum # This subtree must be merged with its parent\n        end\n \
        \   end\nend"
      scala: "object Solution {\n    private var adj: Array[List[Int]] = _\n    private\
        \ var nodeValues: Array[Long] = _\n    private var K: Long = _\n    private\
        \ var componentsCount: Int = _\n\n    private def dfs(u: Int, parent: Int):\
        \ Long = {\n        var currentSum: Long = nodeValues(u)\n        for (v <-\
        \ adj(u)) {\n            if (v == parent) {\n                // continue\n \
        \           } else {\n                currentSum += dfs(v, u)\n            }\n\
        \        }\n\n        if (currentSum % K == 0L) {\n            componentsCount\
        \ += 1\n            0L // This subtree forms a valid component, cut it off\n\
        \        } else {\n            currentSum // This subtree must be merged with\
        \ its parent\n        }\n    }\n\n    def maxKDivisibleComponents(n: Int, edges:\
        \ Array[Array[Int]], values: Array[Int], k: Int): Int = {\n        adj = Array.fill(n)(List[Int]())\n\
        \        for (edge <- edges) {\n            val u = edge(0)\n            val\
        \ v = edge(1)\n            adj(u) = v :: adj(u)\n            adj(v) = u :: adj(v)\n\
        \        }\n\n        nodeValues = values.map(_.toLong)\n        K = k.toLong\n\
        \        componentsCount = 0\n\n        dfs(0, -1)\n\n        componentsCount\n\
        \    }\n}"
      rust: "use std::collections::VecDeque;\n\nstruct Solution {\n    adj: Vec<Vec<usize>>,\n\
        \    node_values: Vec<i64>,\n    k: i64,\n    components_count: i32,\n}\n\n\
        impl Solution {\n    fn dfs(&mut self, u: usize, parent: usize) -> i64 {\n \
        \       let mut current_sum: i64 = self.node_values[u];\n        for &v in &self.adj[u]\
        \ {\n            if v == parent {\n                continue;\n            }\n\
        \            current_sum += self.dfs(v, u);\n        }\n\n        if current_sum\
        \ % self.k == 0 {\n            self.components_count += 1;\n            0 //\
        \ This subtree forms a valid component, cut it off\n        } else {\n     \
        \       current_sum // This subtree must be merged with its parent\n       \
        \ }\n    }\n\n    pub fn max_k_divisible_components(n: i32, edges: Vec<Vec<i32>>,\
        \ values: Vec<i32>, k: i32) -> i32 {\n        let n_usize = n as usize;\n  \
        \      let mut sol = Solution {\n            adj: vec![vec![]; n_usize],\n \
        \           node_values: values.into_iter().map(|x| x as i64).collect(),\n \
        \           k: k as i64,\n            components_count: 0,\n        };\n\n \
        \       for edge in edges {\n            let u = edge[0] as usize;\n       \
        \     let v = edge[1] as usize;\n            sol.adj[u].push(v);\n         \
        \   sol.adj[v].push(u);\n        }\n\n        sol.dfs(0, n_usize); // Use n_usize\
        \ as a dummy parent for the root (0) since node indices are 0 to n-1\n\n   \
        \     sol.components_count\n    }\n}"
      racket: "#lang racket\n\n(define (max-k-divisible-components n edges values k)\n\
        \  (define adj (make-vector n (list)))\n  (for ([edge edges])\n    (define u\
        \ (car edge))\n    (define v (cadr edge))\n    (vector-set! adj u (cons v (vector-ref\
        \ adj u)))\n    (vector-set! adj v (cons u (vector-ref adj v))))\n\n  (define\
        \ components-count 0)\n\n  (define (dfs u parent)\n    (define current-sum (list-ref\
        \ values u))\n    (for ([v (vector-ref adj u)])\n      (when (not (= v parent))\n\
        \        (set! current-sum (+ current-sum (dfs v u)))))\n\n    (if (= (modulo\
        \ current-sum k) 0)\n        (begin\n          (set! components-count (+ components-count\
        \ 1))\n          0) ; This subtree forms a component, cut it off\n        current-sum))\
        \ ; This subtree must be merged with parent\n\n  (dfs 0 -1)\n  components-count)"
      erlang: "-module(solution).\n-export([max_k_divisible_components/4]).\n\nmax_k_divisible_components(N,\
        \ Edges, Values, K) ->\n    Adj = build_adj(N, Edges),\n    ComponentsCount\
        \ = #{\n        count => 0\n    },\n\n    {_FinalSum, FinalComponentsCount}\
        \ = dfs(0, -1, Adj, Values, K, ComponentsCount),\n\n    maps:get(count, FinalComponentsCount).\n\
        \nbuild_adj(N, Edges) ->\n    lists:foldl(\n        fun([U, V], Acc) ->\n  \
        \          maps:update_with(U, fun(L) -> [V | L] end, [V], Acc),\n         \
        \   maps:update_with(V, fun(L) -> [U | L] end, [U], Acc)\n        end,\n   \
        \     maps:from_list([{I, []} || I <- lists:seq(0, N - 1)]),\n        Edges\n\
        \    ).\n\ndfs(U, Parent, Adj, Values, K, ComponentsCount) ->\n    CurrentSum\
        \ = lists:nth(U + 1, Values),\n    Neighbors = maps:get(U, Adj),\n\n    {SubtreeSum,\
        \ UpdatedComponentsCount} = lists:foldl(\n        fun(V, {AccSum, AccComponentsCount})\
        \ ->\n            if V == Parent ->\n                {AccSum, AccComponentsCount};\n\
        \            true ->\n                {ChildSum, NewComponentsCount} = dfs(V,\
        \ U, Adj, Values, K, AccComponentsCount),\n                {AccSum + ChildSum,\
        \ NewComponentsCount}\n            end\n        end,\n        {CurrentSum, ComponentsCount},\n\
        \        Neighbors\n    ),\n\n    if (SubtreeSum rem K) == 0 ->\n        {0,\
        \ UpdatedComponentsCount#{\n            count => maps:get(count, UpdatedComponentsCount)\
        \ + 1\n        }};\n    true ->\n        {SubtreeSum, UpdatedComponentsCount}\n\
        \    end."
      elixir: "defmodule Solution do\n  @spec max_k_divisible_components(n :: integer,\
        \ edges :: [[integer]], values :: [integer], k :: integer) :: integer\n  def\
        \ max_k_divisible_components(n, edges, values, k) do\n    adj = build_adj(n,\
        \ edges)\n    {:ok, components_count} = :persistent_term.put({:components_count,\
        \ self()}, 0)\n\n    dfs(0, -1, adj, values, k)\n\n    :persistent_term.get({:components_count,\
        \ self()})\n  end\n\n  defp build_adj(n, edges) do\n    Enum.reduce(edges, Map.new(0..(n\
        \ - 1), fn i -> {i, []} end), fn [u, v], acc ->\n      acc\n      |> Map.update(u,\
        \ [v], fn list -> [v | list] end)\n      |> Map.update(v, [u], fn list -> [u\
        \ | list] end)\n    end)\n  end\n\n  defp dfs(u, parent, adj, values, k) do\n\
        \    current_sum = Enum.at(values, u)\n    neighbors = Map.get(adj, u)\n\n \
        \   {subtree_sum, _} = Enum.reduce(neighbors, {current_sum, nil}, fn v, {acc_sum,\
        \ _} ->\n      if v == parent do\n        {acc_sum, nil}\n      else\n     \
        \   child_sum = dfs(v, u, adj, values, k)\n        {acc_sum + child_sum, nil}\n\
        \      end\n    end)\n\n    if rem(subtree_sum, k) == 0 do\n      :persistent_term.update({:components_count,\
        \ self()}, fn count -> count + 1 end)\n      0 # This subtree forms a valid\
        \ component, cut it off\n    else\n      subtree_sum # This subtree must be\
        \ merged with its parent\n    end\n  end\nend"
    approach: 'The problem asks to find the maximum number of components in a tree such
      that the sum of values in each component is divisible by ''k''. This can be solved
      using a Depth First Search (DFS) approach. We root the tree arbitrarily, for example,
      at node 0. The core idea is to traverse the tree in a post-order manner, calculating
      the sum of values for each subtree. For a node ''u'', we first recursively calculate
      the sums of values for all its children''s subtrees. Let ''current_subtree_sum''
      be the sum of ''values[u]'' and the sums returned by its children''s DFS calls.


      If ''current_subtree_sum'' is divisible by ''k'', it means the subtree rooted
      at ''u'' can form a valid component on its own. In this case, we increment a global
      counter for valid components and effectively ''cut'' this component from its parent
      by returning 0 to the parent (indicating it contributes nothing to the parent''s
      sum). If ''current_subtree_sum'' is not divisible by ''k'', then this subtree
      cannot form a valid component independently and must be merged with its parent''s
      component. In this scenario, we return ''current_subtree_sum'' to the parent,
      allowing it to be included in the parent''s component sum. The problem guarantees
      that the total sum of all values in the tree is divisible by ''k'', which ensures
      that the final component containing the root will always be valid and counted.'
    time_complexity: The time complexity is O(N), where N is the number of nodes in
      the tree. This is because the algorithm performs a single Depth First Search (DFS)
      traversal, visiting each node and each edge exactly once. Building the adjacency
      list also takes O(N) time.
    space_complexity: The space complexity is O(N), where N is the number of nodes.
      This is primarily due to storing the adjacency list representation of the tree,
      which requires O(N) space. Additionally, the recursion stack for the DFS can go
      up to N in the worst-case scenario (a highly skewed tree), contributing another
      O(N) to the space complexity.
    elapsed_time: 77.44425892829895
    model: gemini-2.5-flash
    generated_at: '2025-11-28 01:02:55 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxKDivisibleComponents(int n, vector<vector<int>>&\
        \ edges, vector<int>& values, int k) {\n        vector<vector<int>> adj(n);\n\
        \        for (auto& edge : edges) {\n            adj[edge[0]].push_back(edge[1]);\n\
        \            adj[edge[1]].push_back(edge[0]);\n        }\n        vector<int>\
        \ sum(n, 0);\n        function<int(int, int)> dfs = [&](int node, int parent)\
        \ {\n            sum[node] = values[node];\n            for (int child : adj[node])\
        \ {\n                if (child != parent) {\n                    sum[node] +=\
        \ dfs(child, node);\n                }\n            }\n            return sum[node];\n\
        \        };\n        dfs(0, -1);\n        int count = 0;\n        for (int i\
        \ = 0; i < n; i++) {\n            if (sum[i] % k == 0) {\n                count++;\n\
        \            }\n        }\n        return count;\n    }\n};"
      java: "class Solution {\n    public int maxKDivisibleComponents(int n, int[][]\
        \ edges, int[] values, int k) {\n        ArrayList<Integer>[] adj = new ArrayList[n];\n\
        \        for (int i = 0; i < n; i++) {\n            adj[i] = new ArrayList<>();\n\
        \        }\n        for (int[] edge : edges) {\n            adj[edge[0]].add(edge[1]);\n\
        \            adj[edge[1]].add(edge[0]);\n        }\n        int[] sum = new\
        \ int[n];\n        dfs(0, -1, adj, sum, values, k);\n        int count = 0;\n\
        \        for (int i = 0; i < n; i++) {\n            if (sum[i] % k == 0) {\n\
        \                count++;\n            }\n        }\n        return count;\n\
        \    }\n    private void dfs(int node, int parent, ArrayList<Integer>[] adj,\
        \ int[] sum, int[] values, int k) {\n        sum[node] = values[node];\n   \
        \     for (int child : adj[node]) {\n            if (child != parent) {\n  \
        \              dfs(child, node, adj, sum, values, k);\n                sum[node]\
        \ += sum[child];\n            }\n        }\n    }\n}"
      python: "class Solution:\n    def maxKDivisibleComponents(self, n: int, edges:\
        \ List[List[int]], values: List[int], k: int) -> int:\n        adj = [[] for\
        \ _ in range(n)]\n        for u, v in edges:\n            adj[u].append(v)\n\
        \            adj[v].append(u)\n        sum_values = [0] * n\n        def dfs(node,\
        \ parent):\n            sum_values[node] = values[node]\n            for child\
        \ in adj[node]:\n                if child != parent:\n                    dfs(child,\
        \ node)\n                    sum_values[node] += sum_values[child]\n       \
        \ dfs(0, -1)\n        count = 0\n        for i in range(n):\n            if\
        \ sum_values[i] % k == 0:\n                count += 1\n        return count"
      python3: "class Solution:\n    def maxKDivisibleComponents(self, n: int, edges:\
        \ List[List[int]], values: List[int], k: int) -> int:\n        adj = [[] for\
        \ _ in range(n)]\n        for u, v in edges:\n            adj[u].append(v)\n\
        \            adj[v].append(u)\n        sum_values = [0] * n\n        def dfs(node,\
        \ parent):\n            sum_values[node] = values[node]\n            for child\
        \ in adj[node]:\n                if child != parent:\n                    dfs(child,\
        \ node)\n                    sum_values[node] += sum_values[child]\n       \
        \ dfs(0, -1)\n        count = 0\n        for i in range(n):\n            if\
        \ sum_values[i] % k == 0:\n                count += 1\n        return count"
      c: "typedef struct {\n    int val;\n    struct Node* next;\n} Node;\n\nNode* newNode(int\
        \ val) {\n    Node* node = (Node*)malloc(sizeof(Node));\n    node->val = val;\n\
        \    node->next = NULL;\n    return node;\n}\n\nvoid addEdge(Node** adj, int\
        \ u, int v) {\n    Node* node = newNode(v);\n    node->next = adj[u];\n    adj[u]\
        \ = node;\n    node = newNode(u);\n    node->next = adj[v];\n    adj[v] = node;\n\
        }\n\nint maxKDivisibleComponents(int n, int** edges, int edgesSize, int* edgesColSize,\
        \ int* values, int k) {\n    Node** adj = (Node**)malloc(n * sizeof(Node*));\n\
        \    for (int i = 0; i < n; i++) {\n        adj[i] = NULL;\n    }\n    for (int\
        \ i = 0; i < edgesSize; i++) {\n        addEdge(adj, edges[i][0], edges[i][1]);\n\
        \    }\n    int* sum = (int*)malloc(n * sizeof(int));\n    dfs(0, -1, adj, sum,\
        \ values, k);\n    int count = 0;\n    for (int i = 0; i < n; i++) {\n     \
        \   if (sum[i] % k == 0) {\n            count++;\n        }\n    }\n    return\
        \ count;\n}\n\nvoid dfs(int node, int parent, Node** adj, int* sum, int* values,\
        \ int k) {\n    sum[node] = values[node];\n    Node* temp = adj[node];\n   \
        \ while (temp != NULL) {\n        if (temp->val != parent) {\n            dfs(temp->val,\
        \ node, adj, sum, values, k);\n            sum[node] += sum[temp->val];\n  \
        \      }\n        temp = temp->next;\n    }\n}"
      csharp: "public class Solution {\n    public int MaxKDivisibleComponents(int n,\
        \ int[][] edges, int[] values, int k) {\n        List<int>[] adj = new List<int>[n];\n\
        \        for (int i = 0; i < n; i++) {\n            adj[i] = new List<int>();\n\
        \        }\n        foreach (int[] edge in edges) {\n            adj[edge[0]].Add(edge[1]);\n\
        \            adj[edge[1]].Add(edge[0]);\n        }\n        int[] sum = new\
        \ int[n];\n        Dfs(0, -1, adj, sum, values, k);\n        int count = 0;\n\
        \        for (int i = 0; i < n; i++) {\n            if (sum[i] % k == 0) {\n\
        \                count++;\n            }\n        }\n        return count;\n\
        \    }\n    private void Dfs(int node, int parent, List<int>[] adj, int[] sum,\
        \ int[] values, int k) {\n        sum[node] = values[node];\n        foreach\
        \ (int child in adj[node]) {\n            if (child != parent) {\n         \
        \       Dfs(child, node, adj, sum, values, k);\n                sum[node] +=\
        \ sum[child];\n            }\n        }\n    }\n}"
      javascript: "var maxKDivisibleComponents = function(n, edges, values, k) {\n \
        \   let adj = Array(n).fill().map(() => []);\n    for (let [u, v] of edges)\
        \ {\n        adj[u].push(v);\n        adj[v].push(u);\n    }\n    let sum =\
        \ Array(n).fill(0);\n    function dfs(node, parent) {\n        sum[node] = values[node];\n\
        \        for (let child of adj[node]) {\n            if (child !== parent) {\n\
        \                dfs(child, node);\n                sum[node] += sum[child];\n\
        \            }\n        }\n    }\n    dfs(0, -1);\n    let count = 0;\n    for\
        \ (let i = 0; i < n; i++) {\n        if (sum[i] % k === 0) {\n            count++;\n\
        \        }\n    }\n    return count;\n};"
      typescript: "function maxKDivisibleComponents(n: number, edges: number[][], values:\
        \ number[], k: number): number {\n    let adj: number[][] = Array(n).fill().map(()\
        \ => []);\n    for (let [u, v] of edges) {\n        adj[u].push(v);\n      \
        \  adj[v].push(u);\n    }\n    let sum: number[] = Array(n).fill(0);\n    function\
        \ dfs(node: number, parent: number): void {\n        sum[node] = values[node];\n\
        \        for (let child of adj[node]) {\n            if (child !== parent) {\n\
        \                dfs(child, node);\n                sum[node] += sum[child];\n\
        \            }\n        }\n    }\n    dfs(0, -1);\n    let count: number = 0;\n\
        \    for (let i = 0; i < n; i++) {\n        if (sum[i] % k === 0) {\n      \
        \      count++;\n        }\n    }\n    return count;\n}"
      php: "class Solution {\n    function maxKDivisibleComponents($n, $edges, $values,\
        \ $k) {\n        $adj = array_fill(0, $n, []);\n        foreach ($edges as $edge)\
        \ {\n            $adj[$edge[0]][] = $edge[1];\n            $adj[$edge[1]][]\
        \ = $edge[0];\n        }\n        $sum = array_fill(0, $n, 0);\n        $this->dfs(0,\
        \ -1, $adj, $sum, $values, $k);\n        $count = 0;\n        for ($i = 0; $i\
        \ < $n; $i++) {\n            if ($sum[$i] % $k == 0) {\n                $count++;\n\
        \            }\n        }\n        return $count;\n    }\n    function dfs($node,\
        \ $parent, &$adj, &$sum, $values, $k) {\n        $sum[$node] = $values[$node];\n\
        \        foreach ($adj[$node] as $child) {\n            if ($child != $parent)\
        \ {\n                $this->dfs($child, $node, $adj, $sum, $values, $k);\n \
        \               $sum[$node] += $sum[$child];\n            }\n        }\n   \
        \ }\n}"
      swift: "class Solution {\n    func maxKDivisibleComponents(_ n: Int, _ edges:\
        \ [[Int]], _ values: [Int], _ k: Int) -> Int {\n        var adj: [[Int]] = Array(repeating:\
        \ [], count: n)\n        for edge in edges {\n            adj[edge[0]].append(edge[1])\n\
        \            adj[edge[1]].append(edge[0])\n        }\n        var sum: [Int]\
        \ = Array(repeating: 0, count: n)\n        dfs(0, -1, &adj, &sum, values, k)\n\
        \        var count = 0\n        for i in 0..<n {\n            if sum[i] % k\
        \ == 0 {\n                count += 1\n            }\n        }\n        return\
        \ count\n    }\n    func dfs(_ node: Int, _ parent: Int, _ adj: inout [[Int]],\
        \ _ sum: inout [Int], _ values: [Int], _ k: Int) {\n        sum[node] = values[node]\n\
        \        for child in adj[node] {\n            if child != parent {\n      \
        \          dfs(child, node, &adj, &sum, values, k)\n                sum[node]\
        \ += sum[child]\n            }\n        }\n    }\n}"
      kotlin: "class Solution {\n    fun maxKDivisibleComponents(n: Int, edges: Array<IntArray>,\
        \ values: IntArray, k: Int): Int {\n        val adj = Array(n) { mutableListOf<Int>()\
        \ }\n        for (edge in edges) {\n            adj[edge[0]].add(edge[1])\n\
        \            adj[edge[1]].add(edge[0])\n        }\n        val sum = IntArray(n)\n\
        \        dfs(0, -1, adj, sum, values, k)\n        var count = 0\n        for\
        \ (i in 0 until n) {\n            if (sum[i] % k == 0) {\n                count++\n\
        \            }\n        }\n        return count\n    }\n    fun dfs(node: Int,\
        \ parent: Int, adj: Array<MutableList<Int>>, sum: IntArray, values: IntArray,\
        \ k: Int) {\n        sum[node] = values[node]\n        for (child in adj[node])\
        \ {\n            if (child != parent) {\n                dfs(child, node, adj,\
        \ sum, values, k)\n                sum[node] += sum[child]\n            }\n\
        \        }\n    }\n}"
      dart: "class Solution {\n    int maxKDivisibleComponents(int n, List<List<int>>\
        \ edges, List<int> values, int k) {\n        List<List<int>> adj = List.generate(n,\
        \ (i) => []);\n        for (var edge in edges) {\n            adj[edge[0]].add(edge[1]);\n\
        \            adj[edge[1]].add(edge[0]);\n        }\n        List<int> sum =\
        \ List.generate(n, (i) => 0);\n        dfs(0, -1, adj, sum, values, k);\n  \
        \      int count = 0;\n        for (int i = 0; i < n; i++) {\n            if\
        \ (sum[i] % k == 0) {\n                count++;\n            }\n        }\n\
        \        return count;\n    }\n    void dfs(int node, int parent, List<List<int>>\
        \ adj, List<int> sum, List<int> values, int k) {\n        sum[node] = values[node];\n\
        \        for (var child in adj[node]) {\n            if (child != parent) {\n\
        \                dfs(child, node, adj, sum, values, k);\n                sum[node]\
        \ += sum[child];\n            }\n        }\n    }\n}"
      go: "package main\n\nimport (\n    \"fmt\"\n)\n\ntype Solution struct{}\n\nfunc\
        \ (s *Solution) maxKDivisibleComponents(n int, edges [][]int, values []int,\
        \ k int) int {\n    adj := make([][]int, n)\n    for _, edge := range edges\
        \ {\n        adj[edge[0]] = append(adj[edge[0]], edge[1])\n        adj[edge[1]]\
        \ = append(adj[edge[1]], edge[0])\n    }\n    sum := make([]int, n)\n    s.dfs(0,\
        \ -1, &adj, &sum, values, k)\n    count := 0\n    for i := 0; i < n; i++ {\n\
        \        if sum[i]%k == 0 {\n            count++\n        }\n    }\n    return\
        \ count\n}\n\nfunc (s *Solution) dfs(node, parent int, adj *[][]int, sum *[]int,\
        \ values []int, k int) {\n    (*sum)[node] = values[node]\n    for _, child\
        \ := range (*adj)[node] {\n        if child != parent {\n            s.dfs(child,\
        \ node, adj, sum, values, k)\n            (*sum)[node] += (*sum)[child]\n  \
        \      }\n    }\n}"
      ruby: "class Solution\n    def max_k_divisible_components(n, edges, values, k)\n\
        \        adj = Array.new(n) { [] }\n        edges.each do |edge|\n         \
        \   adj[edge[0]] << edge[1]\n            adj[edge[1]] << edge[0]\n        end\n\
        \        sum = Array.new(n, 0)\n        dfs(0, -1, adj, sum, values, k)\n  \
        \      count = 0\n        (0...n).each do |i|\n            count += 1 if sum[i]\
        \ % k == 0\n        end\n        count\n    end\n    def dfs(node, parent, adj,\
        \ sum, values, k)\n        sum[node] = values[node]\n        adj[node].each\
        \ do |child|\n            next if child == parent\n            dfs(child, node,\
        \ adj, sum, values, k)\n            sum[node] += sum[child]\n        end\n \
        \   end\nend"
      scala: "object Solution {\n    def maxKDivisibleComponents(n: Int, edges: Array[Array[Int]],\
        \ values: Array[Int], k: Int): Int = {\n        val adj = Array.fill(n)(Array[Int]())\n\
        \        for (edge <- edges) {\n            adj(edge(0)) :+= edge(1)\n     \
        \       adj(edge(1)) :+= edge(0)\n        }\n        val sum = Array.fill(n)(0)\n\
        \        dfs(0, -1, adj, sum, values, k)\n        var count = 0\n        for\
        \ (i <- 0 until n) {\n            if (sum(i) % k == 0) {\n                count\
        \ += 1\n            }\n        }\n        count\n    }\n    def dfs(node: Int,\
        \ parent: Int, adj: Array[Array[Int]], sum: Array[Int], values: Array[Int],\
        \ k: Int): Unit = {\n        sum(node) = values(node)\n        for (child <-\
        \ adj(node)) {\n            if (child != parent) {\n                dfs(child,\
        \ node, adj, sum, values, k)\n                sum(node) += sum(child)\n    \
        \        }\n        }\n    }\n}"
      rust: "struct Solution;\n\nimpl Solution {\n    pub fn max_k_divisible_components(n:\
        \ i32, edges: Vec<Vec<i32>>, values: Vec<i32>, k: i32) -> i32 {\n        let\
        \ mut adj: Vec<Vec<i32>> = vec![vec![]; n as usize];\n        for edge in edges\
        \ {\n            adj[edge[0] as usize].push(edge[1]);\n            adj[edge[1]\
        \ as usize].push(edge[0]);\n        }\n        let mut sum: Vec<i32> = vec![0;\
        \ n as usize];\n        Solution::dfs(0, -1, &mut adj, &mut sum, &values, k);\n\
        \        let mut count = 0;\n        for i in 0..n {\n            if sum[i as\
        \ usize] % k == 0 {\n                count += 1;\n            }\n        }\n\
        \        count\n    }\n    fn dfs(node: i32, parent: i32, adj: &mut Vec<Vec<i32>>,\
        \ sum: &mut Vec<i32>, values: &Vec<i32>, k: i32) {\n        sum[node as usize]\
        \ = values[node as usize];\n        for child in &adj[node as usize] {\n   \
        \         if *child != parent {\n                Solution::dfs(*child, node,\
        \ adj, sum, values, k);\n                sum[node as usize] += sum[*child as\
        \ usize];\n            }\n        }\n    }\n}"
      racket: "(define (max-k-divisible-components n edges values k)\n    (let ((adj\
        \ (make-vector n '())))\n        (for ((edge edges))\n            (vector-append!\
        \ (vector-ref adj (car edge)) (cadr edge))\n            (vector-append! (vector-ref\
        \ adj (cadr edge)) (car edge)))\n        (let ((sum (make-vector n 0)))\n  \
        \          (dfs 0 -1 adj sum values k)\n            (let loop ((i 0) (count\
        \ 0))\n                (if (= i n)\n                    count\n            \
        \        (if (= (remainder (vector-ref sum i) k) 0)\n                      \
        \  (loop (+ i 1) (+ count 1))\n                        (loop (+ i 1) count))))))\n\
        \    (define (dfs node parent adj sum values k)\n        (vector-set! sum node\
        \ (vector-ref values node))\n        (for ((child (vector-ref adj node)))\n\
        \            (if (not (= child parent))\n                (begin\n          \
        \          (dfs child node adj sum values k)\n                    (vector-set!\
        \ sum node (+ (vector-ref sum node) (vector-ref sum child))))))"
      erlang: "max_k_divisible_components(N, Edges, Values, K) ->\n    Count =\n   \
        \     Adj = array:new(N),\n        lists:foreach(fun({U, V}) ->\n          \
        \  array:set(U, [V | array:get(U, Adj)], Adj),\n            array:set(V, [U\
        \ | array:get(V, Adj)], Adj)\n        end, Edges),\n        Sum = array:new(N,\
        \ {0, 0}),\n        dfs(0, -1, Adj, Sum, Values, K),\n        lists:foldl(fun(I,\
        \ Count) ->\n            if array:get(I, Sum) rem K == 0 -> Count + 1;\n   \
        \         true -> Count\n        end, 0, lists:seq(0, N - 1)).\ndfs(Node, Parent,\
        \ Adj, Sum, Values, K) ->\n    array:set(Node, array:get(Node, Values), Sum),\n\
        \    lists:foreach(fun(Child) ->\n        if Child /= Parent ->\n          \
        \  dfs(Child, Node, Adj, Sum, Values, K),\n            array:set(Node, array:get(Node,\
        \ Sum) + array:get(Child, Sum), Sum);\n        true -> ok\n    end, array:get(Node,\
        \ Adj))."
      elixir: "def max_k_divisible_components(n, edges, values, k) do\n    adj = Array.new(n,\
        \ [])\n    Enum.each(edges, fn [u, v] ->\n        Array.append(adj, u, [v])\n\
        \        Array.append(adj, v, [u])\n    end)\n    sum = Array.new(n, 0)\n  \
        \  dfs(0, -1, adj, sum, values, k)\n    count = Enum.reduce(0..n-1, 0, fn i,\
        \ count ->\n        if Enum.at(sum, i) |> rem(k) == 0, do: count + 1, else:\
        \ count\n    end)\n    count\nend\ndefp dfs(node, parent, adj, sum, values,\
        \ k) do\n    sum = Array.put(sum, node, Enum.at(values, node))\n    Enum.each(Enum.at(adj,\
        \ node), fn child ->\n        if child != parent do\n            dfs(child,\
        \ node, adj, sum, values, k)\n            sum = Array.put(sum, node, Enum.at(sum,\
        \ node) + Enum.at(sum, child))\n        end\n    end)\n    sum\nend"
    approach: The problem can be solved by using a depth-first search (DFS) approach.
      We start by rooting the tree at node 0 and then perform a DFS traversal. For each
      node, we calculate the sum of its value and the values of its children. If the
      sum is divisible by k, we can separate the node from its parent and count it as
      a separate component. If the sum is not divisible by k, we need to merge the node
      with its parent. We repeat this process until only one node is left. The key intuition
      here is that if a leaf node is not divisible by k, it must be in the same component
      as its parent node, and if a leaf node is divisible by k, it will be in its own
      component.
    time_complexity: The time complexity of the solution is O(n), where n is the number
      of nodes in the tree. This is because we perform a DFS traversal of the tree,
      visiting each node once.
    space_complexity: The space complexity of the solution is O(n), where n is the number
      of nodes in the tree. This is because we need to store the adjacency list representation
      of the tree, which requires O(n) space. Additionally, we need to store the recursive
      call stack, which also requires O(n) space in the worst case.
    elapsed_time: 11.88355541229248
    model: llama-3.3-70b-versatile
    generated_at: '2025-11-28 01:03:07 '
---

## Problem #2872: Maximum Number of K-Divisible Components

**Difficulty:** Hard

**Topics:** Tree, Depth-First Search

## Problem Description

<p>There is an undirected tree with <code>n</code> nodes labeled from <code>0</code> to <code>n - 1</code>. You are given the integer <code>n</code> and a 2D integer array <code>edges</code> of length <code>n - 1</code>, where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is an edge between nodes <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> in the tree.</p>

<p>You are also given a <strong>0-indexed</strong> integer array <code>values</code> of length <code>n</code>, where <code>values[i]</code> is the <strong>value</strong> associated with the <code>i<sup>th</sup></code> node, and an integer <code>k</code>.</p>

<p>A <strong>valid split</strong> of the tree is obtained by removing any set of edges, possibly empty, from the tree such that the resulting components all have values that are divisible by <code>k</code>, where the <strong>value of a connected component</strong> is the sum of the values of its nodes.</p>

<p>Return <em>the <strong>maximum number of components</strong> in any valid split</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/08/07/example12-cropped2svg.jpg" style="width: 1024px; height: 453px;" />
<pre>
<strong>Input:</strong> n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6
<strong>Output:</strong> 2
<strong>Explanation:</strong> We remove the edge connecting node 1 with 2. The resulting split is valid because:
- The value of the component containing nodes 1 and 3 is values[1] + values[3] = 12.
- The value of the component containing nodes 0, 2, and 4 is values[0] + values[2] + values[4] = 6.
It can be shown that no other valid split has more than 2 connected components.</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/08/07/example21svg-1.jpg" style="width: 999px; height: 338px;" />
<pre>
<strong>Input:</strong> n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> We remove the edge connecting node 0 with 2, and the edge connecting node 0 with 1. The resulting split is valid because:
- The value of the component containing node 0 is values[0] = 3.
- The value of the component containing nodes 2, 5, and 6 is values[2] + values[5] + values[6] = 9.
- The value of the component containing nodes 1, 3, and 4 is values[1] + values[3] + values[4] = 6.
It can be shown that no other valid split has more than 3 connected components.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>values.length == n</code></li>
	<li><code>0 &lt;= values[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
	<li>Sum of <code>values</code> is divisible by <code>k</code>.</li>
	<li>The input is generated such that <code>edges</code> represents a valid tree.</li>
</ul>


## Hints

1. Root the tree at node `0`.

2. If a leaf node is not divisible by `k`, it must be in the same component as its parent node so we merge it with its parent node.

3. If a leaf node is divisible by `k`, it will be in its own components so we separate it from its parent node.

4. In each step, we either cut a leaf node down or merge a leaf node. The number of nodes on the tree reduces by one. Repeat this process until only one node is left.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-28 01:02:55 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks to find the maximum number of components in a tree such that the sum of values in each component is divisible by 'k'. This can be solved using a Depth First Search (DFS) approach. We root the tree arbitrarily, for example, at node 0. The core idea is to traverse the tree in a post-order manner, calculating the sum of values for each subtree. For a node 'u', we first recursively calculate the sums of values for all its children's subtrees. Let 'current_subtree_sum' be the sum of 'values[u]' and the sums returned by its children's DFS calls.

If 'current_subtree_sum' is divisible by 'k', it means the subtree rooted at 'u' can form a valid component on its own. In this case, we increment a global counter for valid components and effectively 'cut' this component from its parent by returning 0 to the parent (indicating it contributes nothing to the parent's sum). If 'current_subtree_sum' is not divisible by 'k', then this subtree cannot form a valid component independently and must be merged with its parent's component. In this scenario, we return 'current_subtree_sum' to the parent, allowing it to be included in the parent's component sum. The problem guarantees that the total sum of all values in the tree is divisible by 'k', which ensures that the final component containing the root will always be valid and counted.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-cpp-gemini-2-5-flash" checked>
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-java-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python3-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-c-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-csharp-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-javascript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-typescript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-php-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-swift-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-kotlin-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-dart-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-go-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-ruby-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-scala-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-rust-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-racket-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-erlang-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-elixir-gemini-2-5-flash">
  <div class="tab-labels">
    <label for="lang-cpp-gemini-2-5-flash">C++</label>
    <label for="lang-java-gemini-2-5-flash">Java</label>
    <label for="lang-python-gemini-2-5-flash">Python</label>
    <label for="lang-python3-gemini-2-5-flash">Python3</label>
    <label for="lang-c-gemini-2-5-flash">C</label>
    <label for="lang-csharp-gemini-2-5-flash">C#</label>
    <label for="lang-javascript-gemini-2-5-flash">JavaScript</label>
    <label for="lang-typescript-gemini-2-5-flash">TypeScript</label>
    <label for="lang-php-gemini-2-5-flash">PHP</label>
    <label for="lang-swift-gemini-2-5-flash">Swift</label>
    <label for="lang-kotlin-gemini-2-5-flash">Kotlin</label>
    <label for="lang-dart-gemini-2-5-flash">Dart</label>
    <label for="lang-go-gemini-2-5-flash">Go</label>
    <label for="lang-ruby-gemini-2-5-flash">Ruby</label>
    <label for="lang-scala-gemini-2-5-flash">Scala</label>
    <label for="lang-rust-gemini-2-5-flash">Rust</label>
    <label for="lang-racket-gemini-2-5-flash">Racket</label>
    <label for="lang-erlang-gemini-2-5-flash">Erlang</label>
    <label for="lang-elixir-gemini-2-5-flash">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    vector<vector<int>> adj;
    vector<long long> node_values;
    long long K;
    int components_count;

    long long dfs(int u, int parent) {
        long long current_sum = node_values[u];
        for (int v : adj[u]) {
            if (v == parent) {
                continue;
            }
            current_sum += dfs(v, u);
        }

        if (current_sum % K == 0) {
            components_count++;
            return 0; // This subtree forms a valid component, cut it off
        } else {
            return current_sum; // This subtree must be merged with its parent
        }
    }

    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k) {
        adj.resize(n);
        node_values.resize(n);
        for (int i = 0; i < n; ++i) {
            node_values[i] = values[i];
        }
        K = k;
        components_count = 0;

        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        dfs(0, -1);

        return components_count;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    List<List<Integer>> adj;
    long[] nodeValues;
    long K;
    int componentsCount;

    private long dfs(int u, int parent) {
        long currentSum = nodeValues[u];
        for (int v : adj.get(u)) {
            if (v == parent) {
                continue;
            }
            currentSum += dfs(v, u);
        }

        if (currentSum % K == 0) {
            componentsCount++;
            return 0; // This subtree forms a valid component, cut it off
        } else {
            return currentSum; // This subtree must be merged with its parent
        }
    }

    public int maxKDivisibleComponents(int n, int[][] edges, int[] values, int k) {
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        nodeValues = new long[n];
        for (int i = 0; i < n; i++) {
            nodeValues[i] = values[i];
        }
        K = k;
        componentsCount = 0;

        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        dfs(0, -1);

        return componentsCount;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        self.components_count = 0

        def dfs(u, parent):
            current_sum = values[u]
            for v in adj[u]:
                if v == parent:
                    continue
                current_sum += dfs(v, u)

            if current_sum % k == 0:
                self.components_count += 1
                return 0 # This subtree forms a component, cut it off
            else:
                return current_sum # This subtree must be merged with parent

        dfs(0, -1)
        return self.components_count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        self.components_count = 0

        def dfs(u, parent):
            current_sum = values[u]
            for v in adj[u]:
                if v == parent:
                    continue
                current_sum += dfs(v, u)

            if current_sum % k == 0:
                self.components_count += 1
                return 0 # This subtree forms a component, cut it off
            else:
                return current_sum # This subtree must be merged with parent

        dfs(0, -1)
        return self.components_count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdio.h>

// Define a structure for adjacency list nodes
typedef struct AdjListNode {
    int dest;
    struct AdjListNode* next;
} AdjListNode;

// Define a structure for the adjacency list itself
typedef struct AdjList {
    AdjListNode* head;
} AdjList;

// Define a structure for the graph
typedef struct Graph {
    int num_nodes;
    AdjList* array;
} Graph;

// Global variables for DFS
long long* global_values;
long long global_k;
int global_components_count;

// Function to create a new adjacency list node
AdjListNode* newAdjListNode(int dest) {
    AdjListNode* newNode = (AdjListNode*)malloc(sizeof(AdjListNode));
    newNode->dest = dest;
    newNode->next = NULL;
    return newNode;
}

// Function to create a graph of V vertices
Graph* createGraph(int num_nodes) {
    Graph* graph = (Graph*)malloc(sizeof(Graph));
    graph->num_nodes = num_nodes;
    graph->array = (AdjList*)malloc(num_nodes * sizeof(AdjList));
    for (int i = 0; i < num_nodes; ++i) {
        graph->array[i].head = NULL;
    }
    return graph;
}

// Function to add an edge to an undirected graph
void addEdge(Graph* graph, int src, int dest) {
    AdjListNode* newNode = newAdjListNode(dest);
    newNode->next = graph->array[src].head;
    graph->array[src].head = newNode;

    newNode = newAdjListNode(src);
    newNode->next = graph->array[dest].head;
    graph->array[dest].head = newNode;
}

// DFS function
long long dfs(Graph* graph, int u, int parent) {
    long long current_sum = global_values[u];
    AdjListNode* pCrawl = graph->array[u].head;
    while (pCrawl) {
        int v = pCrawl->dest;
        if (v != parent) {
            current_sum += dfs(graph, v, u);
        }
        pCrawl = pCrawl->next;
    }

    if (current_sum % global_k == 0) {
        global_components_count++;
        return 0; // This subtree forms a valid component, cut it off
    } else {
        return current_sum; // This subtree must be merged with its parent
    }
}

// Main function to solve the problem
int maxKDivisibleComponents(int n, int** edges, int edgesSize, int* edgesColSize, int* values, int valuesSize, int k) {
    Graph* graph = createGraph(n);
    for (int i = 0; i < edgesSize; ++i) {
        addEdge(graph, edges[i][0], edges[i][1]);
    }

    global_values = (long long*)malloc(n * sizeof(long long));
    for (int i = 0; i < n; ++i) {
        global_values[i] = values[i];
    }
    global_k = k;
    global_components_count = 0;

    dfs(graph, 0, -1);

    // Free allocated memory
    for (int i = 0; i < n; ++i) {
        AdjListNode* current = graph->array[i].head;
        while (current) {
            AdjListNode* next = current->next;
            free(current);
            current = next;
        }
    }
    free(graph->array);
    free(graph);
    free(global_values);

    return global_components_count;
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
    private IList<IList<int>> adj;
    private long[] nodeValues;
    private long K;
    private int componentsCount;

    private long Dfs(int u, int parent) {
        long currentSum = nodeValues[u];
        foreach (int v in adj[u]) {
            if (v == parent) {
                continue;
            }
            currentSum += Dfs(v, u);
        }

        if (currentSum % K == 0) {
            componentsCount++;
            return 0; // This subtree forms a valid component, cut it off
        } else {
            return currentSum; // This subtree must be merged with its parent
        }
    }

    public int MaxKDivisibleComponents(int n, int[][] edges, int[] values, int k) {
        adj = new List<IList<int>>(n);
        for (int i = 0; i < n; i++) {
            adj.Add(new List<int>());
        }

        nodeValues = new long[n];
        for (int i = 0; i < n; i++) {
            nodeValues[i] = values[i];
        }
        K = k;
        componentsCount = 0;

        foreach (int[] edge in edges) {
            adj[edge[0]].Add(edge[1]);
            adj[edge[1]].Add(edge[0]);
        }

        Dfs(0, -1);

        return componentsCount;
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
 * @param {number[]} values
 * @param {number} k
 * @return {number}
 */
var maxKDivisibleComponents = function(n, edges, values, k) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    let componentsCount = 0;

    function dfs(u, parent) {
        let currentSum = values[u];
        for (const v of adj[u]) {
            if (v === parent) {
                continue;
            }
            currentSum += dfs(v, u);
        }

        // JavaScript numbers can handle up to 2^53 - 1 precisely.
        // 3 * 10^4 * 10^9 = 3 * 10^13, which is less than 2^53 (approx 9 * 10^15).
        // So standard numbers are fine, no BigInt needed.
        if (currentSum % k === 0) {
            componentsCount++;
            return 0; // This subtree forms a component, cut it off
        } else {
            return currentSum; // This subtree must be merged with parent
        }
    }

    dfs(0, -1);
    return componentsCount;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxKDivisibleComponents(n: number, edges: number[][], values: number[], k: number): number {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    let componentsCount: number = 0;

    function dfs(u: number, parent: number): number {
        let currentSum: number = values[u];
        for (const v of adj[u]) {
            if (v === parent) {
                continue;
            }
            currentSum += dfs(v, u);
        }

        // TypeScript numbers are 64-bit floating point, but integer operations
        // are precise up to 2^53 - 1. Max sum is 3 * 10^13, which fits.
        if (currentSum % k === 0) {
            componentsCount++;
            return 0; // This subtree forms a component, cut it off
        } else {
            return currentSum; // This subtree must be merged with parent
        }
    }

    dfs(0, -1);
    return componentsCount;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    private $adj;
    private $values;
    private $k;
    private $componentsCount;

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer[] $values
     * @param Integer $k
     * @return Integer
     */
    function maxKDivisibleComponents($n, $edges, $values, $k) {
        $this->adj = array_fill(0, $n, []);
        foreach ($edges as $edge) {
            $u = $edge[0];
            $v = $edge[1];
            $this->adj[$u][] = $v;
            $this->adj[$v][] = $u;
        }

        $this->values = $values;
        $this->k = $k;
        $this->componentsCount = 0;

        $this->dfs(0, -1);

        return $this->componentsCount;
    }

    private function dfs($u, $parent) {
        $currentSum = $this->values[$u];
        foreach ($this->adj[$u] as $v) {
            if ($v == $parent) {
                continue;
            }
            $currentSum += $this->dfs($v, $u);
        }

        // PHP integers are 64-bit on 64-bit systems, handling up to 9*10^18.
        // Max sum is 3*10^13, which fits within standard integer type.
        if ($currentSum % $this->k == 0) {
            $this->componentsCount++;
            return 0; // This subtree forms a valid component, cut it off
        } else {
            return $currentSum; // This subtree must be merged with its parent
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    private var adj: [[Int]] = []
    private var nodeValues: [Int] = []
    private var K: Int = 0
    private var componentsCount: Int = 0

    private func dfs(_ u: Int, _ parent: Int) -> Int {
        var currentSum = nodeValues[u]
        for v in adj[u] {
            if v == parent {
                continue
            }
            currentSum += dfs(v, u)
        }

        // Swift's Int type is typically 64-bit on 64-bit platforms,
        // which can hold values up to 9*10^18. Max sum is 3*10^13, so Int is sufficient.
        if currentSum % K == 0 {
            componentsCount += 1
            return 0 // This subtree forms a valid component, cut it off
        } else {
            return currentSum // This subtree must be merged with its parent
        }
    }

    func maxKDivisibleComponents(_ n: Int, _ edges: [[Int]], _ values: [Int], _ k: Int) -> Int {
        adj = Array(repeating: [], count: n)
        for edge in edges {
            let u = edge[0]
            let v = edge[1]
            adj[u].append(v)
            adj[v].append(u)
        }

        nodeValues = values
        K = k
        componentsCount = 0

        dfs(0, -1)

        return componentsCount
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    private lateinit var adj: Array<MutableList<Int>>
    private lateinit var nodeValues: LongArray
    private var K: Long = 0
    private var componentsCount: Int = 0

    private fun dfs(u: Int, parent: Int): Long {
        var currentSum: Long = nodeValues[u]
        for (v in adj[u]) {
            if (v == parent) {
                continue
            }
            currentSum += dfs(v, u)
        }

        if (currentSum % K == 0L) {
            componentsCount++
            return 0L // This subtree forms a valid component, cut it off
        } else {
            return currentSum // This subtree must be merged with its parent
        }
    }

    fun maxKDivisibleComponents(n: Int, edges: Array<IntArray>, values: IntArray, k: Int): Int {
        adj = Array(n) { mutableListOf() }
        for (edge in edges) {
            val u = edge[0]
            val v = edge[1]
            adj[u].add(v)
            adj[v].add(u)
        }

        nodeValues = LongArray(n)
        for (i in 0 until n) {
            nodeValues[i] = values[i].toLong()
        }
        K = k.toLong()
        componentsCount = 0

        dfs(0, -1)

        return componentsCount
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  late List<List<int>> adj;
  late List<int> nodeValues;
  late int K;
  int componentsCount = 0;

  int _dfs(int u, int parent) {
    int currentSum = nodeValues[u];
    for (int v in adj[u]) {
      if (v == parent) {
        continue;
      }
      currentSum += _dfs(v, u);
    }

    // Dart's `int` type supports arbitrary precision integers, so large sums are handled automatically.
    if (currentSum % K == 0) {
      componentsCount++;
      return 0; // This subtree forms a valid component, cut it off
    } else {
      return currentSum; // This subtree must be merged with its parent
    }
  }

  int maxKDivisibleComponents(int n, List<List<int>> edges, List<int> values, int k) {
    adj = List.generate(n, (_) => []);
    for (final edge in edges) {
      final u = edge[0];
      final v = edge[1];
      adj[u].add(v);
      adj[v].add(u);
    }

    nodeValues = values;
    K = k;
    componentsCount = 0;

    _dfs(0, -1);

    return componentsCount;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

type Solution struct {
    adj [][]int
    nodeValues []int
    k int
    componentsCount int
}

func (s *Solution) dfs(u int, parent int) int {
    currentSum := s.nodeValues[u]
    for _, v := range s.adj[u] {
        if v == parent {
            continue
        }
        currentSum += s.dfs(v, u)
    }

    // Go's int type is at least 32 bits, int64 is 64 bits.
    // Max sum 3*10^13 fits in int64. The problem values are int, so we use int for nodeValues and k.
    // If values[i] or k were larger than int max, we'd need to use int64 for them too.
    // The sum currentSum can exceed int max, so it should be int64.
    // Let's adjust to use int64 for sums to be safe.
    // The problem constraints state values[i] <= 10^9 and k <= 10^9. n <= 3*10^4.
    // Max sum is 3*10^4 * 10^9 = 3*10^13. This fits in int64.
    // Let's change nodeValues to []int64 and k to int64.
    // For the given template, values and k are int, so we cast them to int64 for sum calculation.

    if currentSum % s.k == 0 {
        s.componentsCount++
        return 0 // This subtree forms a valid component, cut it off
    } else {
        return currentSum // This subtree must be merged with its parent
    }
}

func maxKDivisibleComponents(n int, edges [][]int, values []int, k int) int {
    s := &Solution{
        adj: make([][]int, n),
        nodeValues: make([]int, n),
        k: k,
        componentsCount: 0,
    }

    for i := 0; i < n; i++ {
        s.nodeValues[i] = values[i]
    }

    for _, edge := range edges {
        u, v := edge[0], edge[1]
        s.adj[u] = append(s.adj[u], v)
        s.adj[v] = append(s.adj[v], u)
    }

    s.dfs(0, -1)

    return s.componentsCount
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    attr_accessor :adj, :values, :k, :components_count

    # @param {Integer} n
    # @param {Integer[][]} edges
    # @param {Integer[]} values
    # @param {Integer} k
    # @return {Integer}
    def max_k_divisible_components(n, edges, values, k)
        @adj = Array.new(n) { [] }
        edges.each do |u, v|
            @adj[u] << v
            @adj[v] << u
        end

        @values = values
        @k = k
        @components_count = 0

        dfs(0, -1)

        @components_count
    end

    private

    def dfs(u, parent)
        current_sum = @values[u]
        @adj[u].each do |v|
            if v == parent
                next
            end
            current_sum += dfs(v, u)
        end

        # Ruby handles large integers automatically, no special type needed.
        if current_sum % @k == 0
            @components_count += 1
            return 0 # This subtree forms a valid component, cut it off
        else
            return current_sum # This subtree must be merged with its parent
        end
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    private var adj: Array[List[Int]] = _
    private var nodeValues: Array[Long] = _
    private var K: Long = _
    private var componentsCount: Int = _

    private def dfs(u: Int, parent: Int): Long = {
        var currentSum: Long = nodeValues(u)
        for (v <- adj(u)) {
            if (v == parent) {
                // continue
            } else {
                currentSum += dfs(v, u)
            }
        }

        if (currentSum % K == 0L) {
            componentsCount += 1
            0L // This subtree forms a valid component, cut it off
        } else {
            currentSum // This subtree must be merged with its parent
        }
    }

    def maxKDivisibleComponents(n: Int, edges: Array[Array[Int]], values: Array[Int], k: Int): Int = {
        adj = Array.fill(n)(List[Int]())
        for (edge <- edges) {
            val u = edge(0)
            val v = edge(1)
            adj(u) = v :: adj(u)
            adj(v) = u :: adj(v)
        }

        nodeValues = values.map(_.toLong)
        K = k.toLong
        componentsCount = 0

        dfs(0, -1)

        componentsCount
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::VecDeque;

struct Solution {
    adj: Vec<Vec<usize>>,
    node_values: Vec<i64>,
    k: i64,
    components_count: i32,
}

impl Solution {
    fn dfs(&mut self, u: usize, parent: usize) -> i64 {
        let mut current_sum: i64 = self.node_values[u];
        for &v in &self.adj[u] {
            if v == parent {
                continue;
            }
            current_sum += self.dfs(v, u);
        }

        if current_sum % self.k == 0 {
            self.components_count += 1;
            0 // This subtree forms a valid component, cut it off
        } else {
            current_sum // This subtree must be merged with its parent
        }
    }

    pub fn max_k_divisible_components(n: i32, edges: Vec<Vec<i32>>, values: Vec<i32>, k: i32) -> i32 {
        let n_usize = n as usize;
        let mut sol = Solution {
            adj: vec![vec![]; n_usize],
            node_values: values.into_iter().map(|x| x as i64).collect(),
            k: k as i64,
            components_count: 0,
        };

        for edge in edges {
            let u = edge[0] as usize;
            let v = edge[1] as usize;
            sol.adj[u].push(v);
            sol.adj[v].push(u);
        }

        sol.dfs(0, n_usize); // Use n_usize as a dummy parent for the root (0) since node indices are 0 to n-1

        sol.components_count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (max-k-divisible-components n edges values k)
  (define adj (make-vector n (list)))
  (for ([edge edges])
    (define u (car edge))
    (define v (cadr edge))
    (vector-set! adj u (cons v (vector-ref adj u)))
    (vector-set! adj v (cons u (vector-ref adj v))))

  (define components-count 0)

  (define (dfs u parent)
    (define current-sum (list-ref values u))
    (for ([v (vector-ref adj u)])
      (when (not (= v parent))
        (set! current-sum (+ current-sum (dfs v u)))))

    (if (= (modulo current-sum k) 0)
        (begin
          (set! components-count (+ components-count 1))
          0) ; This subtree forms a component, cut it off
        current-sum)) ; This subtree must be merged with parent

  (dfs 0 -1)
  components-count)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([max_k_divisible_components/4]).

max_k_divisible_components(N, Edges, Values, K) ->
    Adj = build_adj(N, Edges),
    ComponentsCount = #{
        count => 0
    },

    {_FinalSum, FinalComponentsCount} = dfs(0, -1, Adj, Values, K, ComponentsCount),

    maps:get(count, FinalComponentsCount).

build_adj(N, Edges) ->
    lists:foldl(
        fun([U, V], Acc) ->
            maps:update_with(U, fun(L) -> [V | L] end, [V], Acc),
            maps:update_with(V, fun(L) -> [U | L] end, [U], Acc)
        end,
        maps:from_list([{I, []} || I <- lists:seq(0, N - 1)]),
        Edges
    ).

dfs(U, Parent, Adj, Values, K, ComponentsCount) ->
    CurrentSum = lists:nth(U + 1, Values),
    Neighbors = maps:get(U, Adj),

    {SubtreeSum, UpdatedComponentsCount} = lists:foldl(
        fun(V, {AccSum, AccComponentsCount}) ->
            if V == Parent ->
                {AccSum, AccComponentsCount};
            true ->
                {ChildSum, NewComponentsCount} = dfs(V, U, Adj, Values, K, AccComponentsCount),
                {AccSum + ChildSum, NewComponentsCount}
            end
        end,
        {CurrentSum, ComponentsCount},
        Neighbors
    ),

    if (SubtreeSum rem K) == 0 ->
        {0, UpdatedComponentsCount#{
            count => maps:get(count, UpdatedComponentsCount) + 1
        }};
    true ->
        {SubtreeSum, UpdatedComponentsCount}
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_k_divisible_components(n :: integer, edges :: [[integer]], values :: [integer], k :: integer) :: integer
  def max_k_divisible_components(n, edges, values, k) do
    adj = build_adj(n, edges)
    {:ok, components_count} = :persistent_term.put({:components_count, self()}, 0)

    dfs(0, -1, adj, values, k)

    :persistent_term.get({:components_count, self()})
  end

  defp build_adj(n, edges) do
    Enum.reduce(edges, Map.new(0..(n - 1), fn i -> {i, []} end), fn [u, v], acc ->
      acc
      |> Map.update(u, [v], fn list -> [v | list] end)
      |> Map.update(v, [u], fn list -> [u | list] end)
    end)
  end

  defp dfs(u, parent, adj, values, k) do
    current_sum = Enum.at(values, u)
    neighbors = Map.get(adj, u)

    {subtree_sum, _} = Enum.reduce(neighbors, {current_sum, nil}, fn v, {acc_sum, _} ->
      if v == parent do
        {acc_sum, nil}
      else
        child_sum = dfs(v, u, adj, values, k)
        {acc_sum + child_sum, nil}
      end
    end)

    if rem(subtree_sum, k) == 0 do
      :persistent_term.update({:components_count, self()}, fn count -> count + 1 end)
      0 # This subtree forms a valid component, cut it off
    else
      subtree_sum # This subtree must be merged with its parent
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N), where N is the number of nodes in the tree. This is because the algorithm performs a single Depth First Search (DFS) traversal, visiting each node and each edge exactly once. Building the adjacency list also takes O(N) time.

- **Space Complexity:** The space complexity is O(N), where N is the number of nodes. This is primarily due to storing the adjacency list representation of the tree, which requires O(N) space. Additionally, the recursion stack for the DFS can go up to N in the worst-case scenario (a highly skewed tree), contributing another O(N) to the space complexity.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-28 01:03:07 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by using a depth-first search (DFS) approach. We start by rooting the tree at node 0 and then perform a DFS traversal. For each node, we calculate the sum of its value and the values of its children. If the sum is divisible by k, we can separate the node from its parent and count it as a separate component. If the sum is not divisible by k, we need to merge the node with its parent. We repeat this process until only one node is left. The key intuition here is that if a leaf node is not divisible by k, it must be in the same component as its parent node, and if a leaf node is divisible by k, it will be in its own component.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-cpp-llama-3-3-70b-versatile" checked>
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-java-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python3-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-c-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-csharp-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-javascript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-typescript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-php-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-swift-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-kotlin-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-dart-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-go-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-ruby-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-scala-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-rust-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-racket-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-erlang-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-elixir-llama-3-3-70b-versatile">
  <div class="tab-labels">
    <label for="lang-cpp-llama-3-3-70b-versatile">C++</label>
    <label for="lang-java-llama-3-3-70b-versatile">Java</label>
    <label for="lang-python-llama-3-3-70b-versatile">Python</label>
    <label for="lang-python3-llama-3-3-70b-versatile">Python3</label>
    <label for="lang-c-llama-3-3-70b-versatile">C</label>
    <label for="lang-csharp-llama-3-3-70b-versatile">C#</label>
    <label for="lang-javascript-llama-3-3-70b-versatile">JavaScript</label>
    <label for="lang-typescript-llama-3-3-70b-versatile">TypeScript</label>
    <label for="lang-php-llama-3-3-70b-versatile">PHP</label>
    <label for="lang-swift-llama-3-3-70b-versatile">Swift</label>
    <label for="lang-kotlin-llama-3-3-70b-versatile">Kotlin</label>
    <label for="lang-dart-llama-3-3-70b-versatile">Dart</label>
    <label for="lang-go-llama-3-3-70b-versatile">Go</label>
    <label for="lang-ruby-llama-3-3-70b-versatile">Ruby</label>
    <label for="lang-scala-llama-3-3-70b-versatile">Scala</label>
    <label for="lang-rust-llama-3-3-70b-versatile">Rust</label>
    <label for="lang-racket-llama-3-3-70b-versatile">Racket</label>
    <label for="lang-erlang-llama-3-3-70b-versatile">Erlang</label>
    <label for="lang-elixir-llama-3-3-70b-versatile">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k) {
        vector<vector<int>> adj(n);
        for (auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        vector<int> sum(n, 0);
        function<int(int, int)> dfs = [&](int node, int parent) {
            sum[node] = values[node];
            for (int child : adj[node]) {
                if (child != parent) {
                    sum[node] += dfs(child, node);
                }
            }
            return sum[node];
        };
        dfs(0, -1);
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (sum[i] % k == 0) {
                count++;
            }
        }
        return count;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxKDivisibleComponents(int n, int[][] edges, int[] values, int k) {
        ArrayList<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int[] edge : edges) {
            adj[edge[0]].add(edge[1]);
            adj[edge[1]].add(edge[0]);
        }
        int[] sum = new int[n];
        dfs(0, -1, adj, sum, values, k);
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (sum[i] % k == 0) {
                count++;
            }
        }
        return count;
    }
    private void dfs(int node, int parent, ArrayList<Integer>[] adj, int[] sum, int[] values, int k) {
        sum[node] = values[node];
        for (int child : adj[node]) {
            if (child != parent) {
                dfs(child, node, adj, sum, values, k);
                sum[node] += sum[child];
            }
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        sum_values = [0] * n
        def dfs(node, parent):
            sum_values[node] = values[node]
            for child in adj[node]:
                if child != parent:
                    dfs(child, node)
                    sum_values[node] += sum_values[child]
        dfs(0, -1)
        count = 0
        for i in range(n):
            if sum_values[i] % k == 0:
                count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        sum_values = [0] * n
        def dfs(node, parent):
            sum_values[node] = values[node]
            for child in adj[node]:
                if child != parent:
                    dfs(child, node)
                    sum_values[node] += sum_values[child]
        dfs(0, -1)
        count = 0
        for i in range(n):
            if sum_values[i] % k == 0:
                count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int val;
    struct Node* next;
} Node;

Node* newNode(int val) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->val = val;
    node->next = NULL;
    return node;
}

void addEdge(Node** adj, int u, int v) {
    Node* node = newNode(v);
    node->next = adj[u];
    adj[u] = node;
    node = newNode(u);
    node->next = adj[v];
    adj[v] = node;
}

int maxKDivisibleComponents(int n, int** edges, int edgesSize, int* edgesColSize, int* values, int k) {
    Node** adj = (Node**)malloc(n * sizeof(Node*));
    for (int i = 0; i < n; i++) {
        adj[i] = NULL;
    }
    for (int i = 0; i < edgesSize; i++) {
        addEdge(adj, edges[i][0], edges[i][1]);
    }
    int* sum = (int*)malloc(n * sizeof(int));
    dfs(0, -1, adj, sum, values, k);
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (sum[i] % k == 0) {
            count++;
        }
    }
    return count;
}

void dfs(int node, int parent, Node** adj, int* sum, int* values, int k) {
    sum[node] = values[node];
    Node* temp = adj[node];
    while (temp != NULL) {
        if (temp->val != parent) {
            dfs(temp->val, node, adj, sum, values, k);
            sum[node] += sum[temp->val];
        }
        temp = temp->next;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxKDivisibleComponents(int n, int[][] edges, int[] values, int k) {
        List<int>[] adj = new List<int>[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new List<int>();
        }
        foreach (int[] edge in edges) {
            adj[edge[0]].Add(edge[1]);
            adj[edge[1]].Add(edge[0]);
        }
        int[] sum = new int[n];
        Dfs(0, -1, adj, sum, values, k);
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (sum[i] % k == 0) {
                count++;
            }
        }
        return count;
    }
    private void Dfs(int node, int parent, List<int>[] adj, int[] sum, int[] values, int k) {
        sum[node] = values[node];
        foreach (int child in adj[node]) {
            if (child != parent) {
                Dfs(child, node, adj, sum, values, k);
                sum[node] += sum[child];
            }
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var maxKDivisibleComponents = function(n, edges, values, k) {
    let adj = Array(n).fill().map(() => []);
    for (let [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    let sum = Array(n).fill(0);
    function dfs(node, parent) {
        sum[node] = values[node];
        for (let child of adj[node]) {
            if (child !== parent) {
                dfs(child, node);
                sum[node] += sum[child];
            }
        }
    }
    dfs(0, -1);
    let count = 0;
    for (let i = 0; i < n; i++) {
        if (sum[i] % k === 0) {
            count++;
        }
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxKDivisibleComponents(n: number, edges: number[][], values: number[], k: number): number {
    let adj: number[][] = Array(n).fill().map(() => []);
    for (let [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    let sum: number[] = Array(n).fill(0);
    function dfs(node: number, parent: number): void {
        sum[node] = values[node];
        for (let child of adj[node]) {
            if (child !== parent) {
                dfs(child, node);
                sum[node] += sum[child];
            }
        }
    }
    dfs(0, -1);
    let count: number = 0;
    for (let i = 0; i < n; i++) {
        if (sum[i] % k === 0) {
            count++;
        }
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function maxKDivisibleComponents($n, $edges, $values, $k) {
        $adj = array_fill(0, $n, []);
        foreach ($edges as $edge) {
            $adj[$edge[0]][] = $edge[1];
            $adj[$edge[1]][] = $edge[0];
        }
        $sum = array_fill(0, $n, 0);
        $this->dfs(0, -1, $adj, $sum, $values, $k);
        $count = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($sum[$i] % $k == 0) {
                $count++;
            }
        }
        return $count;
    }
    function dfs($node, $parent, &$adj, &$sum, $values, $k) {
        $sum[$node] = $values[$node];
        foreach ($adj[$node] as $child) {
            if ($child != $parent) {
                $this->dfs($child, $node, $adj, $sum, $values, $k);
                $sum[$node] += $sum[$child];
            }
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxKDivisibleComponents(_ n: Int, _ edges: [[Int]], _ values: [Int], _ k: Int) -> Int {
        var adj: [[Int]] = Array(repeating: [], count: n)
        for edge in edges {
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        }
        var sum: [Int] = Array(repeating: 0, count: n)
        dfs(0, -1, &adj, &sum, values, k)
        var count = 0
        for i in 0..<n {
            if sum[i] % k == 0 {
                count += 1
            }
        }
        return count
    }
    func dfs(_ node: Int, _ parent: Int, _ adj: inout [[Int]], _ sum: inout [Int], _ values: [Int], _ k: Int) {
        sum[node] = values[node]
        for child in adj[node] {
            if child != parent {
                dfs(child, node, &adj, &sum, values, k)
                sum[node] += sum[child]
            }
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxKDivisibleComponents(n: Int, edges: Array<IntArray>, values: IntArray, k: Int): Int {
        val adj = Array(n) { mutableListOf<Int>() }
        for (edge in edges) {
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
        }
        val sum = IntArray(n)
        dfs(0, -1, adj, sum, values, k)
        var count = 0
        for (i in 0 until n) {
            if (sum[i] % k == 0) {
                count++
            }
        }
        return count
    }
    fun dfs(node: Int, parent: Int, adj: Array<MutableList<Int>>, sum: IntArray, values: IntArray, k: Int) {
        sum[node] = values[node]
        for (child in adj[node]) {
            if (child != parent) {
                dfs(child, node, adj, sum, values, k)
                sum[node] += sum[child]
            }
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int maxKDivisibleComponents(int n, List<List<int>> edges, List<int> values, int k) {
        List<List<int>> adj = List.generate(n, (i) => []);
        for (var edge in edges) {
            adj[edge[0]].add(edge[1]);
            adj[edge[1]].add(edge[0]);
        }
        List<int> sum = List.generate(n, (i) => 0);
        dfs(0, -1, adj, sum, values, k);
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (sum[i] % k == 0) {
                count++;
            }
        }
        return count;
    }
    void dfs(int node, int parent, List<List<int>> adj, List<int> sum, List<int> values, int k) {
        sum[node] = values[node];
        for (var child in adj[node]) {
            if (child != parent) {
                dfs(child, node, adj, sum, values, k);
                sum[node] += sum[child];
            }
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import (
    "fmt"
)

type Solution struct{}

func (s *Solution) maxKDivisibleComponents(n int, edges [][]int, values []int, k int) int {
    adj := make([][]int, n)
    for _, edge := range edges {
        adj[edge[0]] = append(adj[edge[0]], edge[1])
        adj[edge[1]] = append(adj[edge[1]], edge[0])
    }
    sum := make([]int, n)
    s.dfs(0, -1, &adj, &sum, values, k)
    count := 0
    for i := 0; i < n; i++ {
        if sum[i]%k == 0 {
            count++
        }
    }
    return count
}

func (s *Solution) dfs(node, parent int, adj *[][]int, sum *[]int, values []int, k int) {
    (*sum)[node] = values[node]
    for _, child := range (*adj)[node] {
        if child != parent {
            s.dfs(child, node, adj, sum, values, k)
            (*sum)[node] += (*sum)[child]
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def max_k_divisible_components(n, edges, values, k)
        adj = Array.new(n) { [] }
        edges.each do |edge|
            adj[edge[0]] << edge[1]
            adj[edge[1]] << edge[0]
        end
        sum = Array.new(n, 0)
        dfs(0, -1, adj, sum, values, k)
        count = 0
        (0...n).each do |i|
            count += 1 if sum[i] % k == 0
        end
        count
    end
    def dfs(node, parent, adj, sum, values, k)
        sum[node] = values[node]
        adj[node].each do |child|
            next if child == parent
            dfs(child, node, adj, sum, values, k)
            sum[node] += sum[child]
        end
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxKDivisibleComponents(n: Int, edges: Array[Array[Int]], values: Array[Int], k: Int): Int = {
        val adj = Array.fill(n)(Array[Int]())
        for (edge <- edges) {
            adj(edge(0)) :+= edge(1)
            adj(edge(1)) :+= edge(0)
        }
        val sum = Array.fill(n)(0)
        dfs(0, -1, adj, sum, values, k)
        var count = 0
        for (i <- 0 until n) {
            if (sum(i) % k == 0) {
                count += 1
            }
        }
        count
    }
    def dfs(node: Int, parent: Int, adj: Array[Array[Int]], sum: Array[Int], values: Array[Int], k: Int): Unit = {
        sum(node) = values(node)
        for (child <- adj(node)) {
            if (child != parent) {
                dfs(child, node, adj, sum, values, k)
                sum(node) += sum(child)
            }
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
struct Solution;

impl Solution {
    pub fn max_k_divisible_components(n: i32, edges: Vec<Vec<i32>>, values: Vec<i32>, k: i32) -> i32 {
        let mut adj: Vec<Vec<i32>> = vec![vec![]; n as usize];
        for edge in edges {
            adj[edge[0] as usize].push(edge[1]);
            adj[edge[1] as usize].push(edge[0]);
        }
        let mut sum: Vec<i32> = vec![0; n as usize];
        Solution::dfs(0, -1, &mut adj, &mut sum, &values, k);
        let mut count = 0;
        for i in 0..n {
            if sum[i as usize] % k == 0 {
                count += 1;
            }
        }
        count
    }
    fn dfs(node: i32, parent: i32, adj: &mut Vec<Vec<i32>>, sum: &mut Vec<i32>, values: &Vec<i32>, k: i32) {
        sum[node as usize] = values[node as usize];
        for child in &adj[node as usize] {
            if *child != parent {
                Solution::dfs(*child, node, adj, sum, values, k);
                sum[node as usize] += sum[*child as usize];
            }
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define (max-k-divisible-components n edges values k)
    (let ((adj (make-vector n '())))
        (for ((edge edges))
            (vector-append! (vector-ref adj (car edge)) (cadr edge))
            (vector-append! (vector-ref adj (cadr edge)) (car edge)))
        (let ((sum (make-vector n 0)))
            (dfs 0 -1 adj sum values k)
            (let loop ((i 0) (count 0))
                (if (= i n)
                    count
                    (if (= (remainder (vector-ref sum i) k) 0)
                        (loop (+ i 1) (+ count 1))
                        (loop (+ i 1) count))))))
    (define (dfs node parent adj sum values k)
        (vector-set! sum node (vector-ref values node))
        (for ((child (vector-ref adj node)))
            (if (not (= child parent))
                (begin
                    (dfs child node adj sum values k)
                    (vector-set! sum node (+ (vector-ref sum node) (vector-ref sum child))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
max_k_divisible_components(N, Edges, Values, K) ->
    Count =
        Adj = array:new(N),
        lists:foreach(fun({U, V}) ->
            array:set(U, [V | array:get(U, Adj)], Adj),
            array:set(V, [U | array:get(V, Adj)], Adj)
        end, Edges),
        Sum = array:new(N, {0, 0}),
        dfs(0, -1, Adj, Sum, Values, K),
        lists:foldl(fun(I, Count) ->
            if array:get(I, Sum) rem K == 0 -> Count + 1;
            true -> Count
        end, 0, lists:seq(0, N - 1)).
dfs(Node, Parent, Adj, Sum, Values, K) ->
    array:set(Node, array:get(Node, Values), Sum),
    lists:foreach(fun(Child) ->
        if Child /= Parent ->
            dfs(Child, Node, Adj, Sum, Values, K),
            array:set(Node, array:get(Node, Sum) + array:get(Child, Sum), Sum);
        true -> ok
    end, array:get(Node, Adj)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def max_k_divisible_components(n, edges, values, k) do
    adj = Array.new(n, [])
    Enum.each(edges, fn [u, v] ->
        Array.append(adj, u, [v])
        Array.append(adj, v, [u])
    end)
    sum = Array.new(n, 0)
    dfs(0, -1, adj, sum, values, k)
    count = Enum.reduce(0..n-1, 0, fn i, count ->
        if Enum.at(sum, i) |> rem(k) == 0, do: count + 1, else: count
    end)
    count
end
defp dfs(node, parent, adj, sum, values, k) do
    sum = Array.put(sum, node, Enum.at(values, node))
    Enum.each(Enum.at(adj, node), fn child ->
        if child != parent do
            dfs(child, node, adj, sum, values, k)
            sum = Array.put(sum, node, Enum.at(sum, node) + Enum.at(sum, child))
        end
    end)
    sum
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the solution is O(n), where n is the number of nodes in the tree. This is because we perform a DFS traversal of the tree, visiting each node once.

- **Space Complexity:** The space complexity of the solution is O(n), where n is the number of nodes in the tree. This is because we need to store the adjacency list representation of the tree, which requires O(n) space. Additionally, we need to store the recursive call stack, which also requires O(n) space in the worst case.

</div>
</details>
